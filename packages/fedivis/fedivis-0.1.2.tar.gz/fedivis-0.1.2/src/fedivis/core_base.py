import os
import datetime
import re
import unicodedata
import random
import itertools as it
import collections
import xml.etree.ElementTree as ET
import json
from typing import Tuple, Union
import requests

from mastodon import Mastodon, errors
import networkx as nx

from bs4 import BeautifulSoup, Tag
import nxv
import tabulate
import yaml

try:
    # this will be part of standard library for python >= 3.11
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib # type: ignore

try:
    # useful during development
    from ipydex import IPS
except ModuleNotFoundError:
    pass



from . import settings
random.seed(1706)

AVATAR_SIZE = 48


class FedivisError(ValueError):
    pass


all_colors = [
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2',
    '#7f7f7f', '#bcbd22', '#17becf'
]

SHORT_DATE_FORMAT = "%m-%d"


def get_conf(confpath: str = None):
    if confpath is None:
        confpath = "config.toml"

    confpath = os.path.abspath(confpath)
    try:
        with open(confpath, "rb") as fp:
            CONF = tomllib.load(fp)
    except FileNotFoundError:
        print(f"No config file found at {confpath}. Using API in public mode")

        # use default value
        CONF = {
            "access_token": "pymastoclient_123_usercred.secret",
            "mastodon_url": "https://social.tchncs.de"
        }

    return CONF


def sortkey(pair):
    c1, c2 = pair

    L = len(c1)
    return (c1 != c2[:L], all_colors.index(c1), all_colors.index(c2[:L]))


def get_sorted_pairs(colors):
    colors2 = [c+"20" for c in colors]

    pairs = list(it.product(colors, colors2))

    pairs.sort(key=sortkey)
    return pairs


def get_color_pair_cycler():
    """
    get pairs for colors (edge and fill color) such that the resulting graph looks somewhat nice

    but also enable a total of 100 combinations
    """

    # 'tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple'
    # nice colors
    colors1 =  all_colors[:5]

    pairs1 = get_sorted_pairs(colors1)
    pairs2 = get_sorted_pairs(all_colors)

    # remove duplicates but maintain order
    pairs = [*pairs1]
    for p in pairs2:
        if p in pairs1:
            continue
        pairs.append(p)

    while True:
        for pair in pairs:
            yield pair

author_color_map = {}
color_pair_cycler = get_color_pair_cycler()


def get_author_colors(data):
    aid = data["account"]["id"]
    colors = author_color_map.get(aid)
    if colors:
        return colors
    else:
        # get new color from cycler, save it, return it
        colors = next(color_pair_cycler)
        author_color_map[aid] = colors
        return colors


def get_formatted_followers_count(data):

    c = data["account"].get("followers_count")
    if not c:
        return ""

    assert isinstance(c, int)
    if c < 1000:
        c_str = str(c)
    elif c < 10_000:
        c_str = f"{c/1e3:3.1f}K"
    elif c < 1000_000:
        c_str = f"{c/1e3:3.0f}K"
    elif c < 10_000_000:
        c_str = f"{c/1e6:3.1f}M"
    elif c < 1000_000_000:
        c_str = f"{c/1e6:3.0f}M"
    else:
        c_str = f"{c/1e9:3.1f}B"

    return c_str


def get_root_id_from_url(url: str):

    # expect something like:
    # https://social.tchncs.de/web/@ueckueck@dresden.network/109253718049953006

    parts = url.split("/")

    root_id = parts[-1]

    return root_id


GLOBAL_REPLACEMENT_TUPLES = [
    ("__FF__", "&#128100;"),
    ("__FAVS__", "&#x2B50;"),
    # ("__BOOSTS__", "&#8613;"),
    ("__BOOSTS__", "&#x1F504;"),
    ]

class User:
    cache = {}
    def __init__(self, account_dict: dict):
        self.id = account_dict["id"]
        self.acct = account_dict["acct"]
        self.displayname = account_dict.get("display_name")
        self.followers_count = account_dict.get("followers_count")

    def __repr__(self):
        return f"@{self.acct} ({self.followers_count}F)"

    @staticmethod
    def init_cache():
        """
        Reset the cache to an empty dict.
        """
        User.cache = {}

    @staticmethod
    def make_user(account_dict: dict):
        id = account_dict["id"]
        existing_user = User.cache.get(id)
        if existing_user is not None:
            return existing_user
        user = User(account_dict)
        User.cache[id] = user
        return user


def get_element_dict_by_id(bs_obj: BeautifulSoup, tag_name: str) -> dict:

    elements = {}
    for element in bs_obj.find_all(tag_name):
            id_str = element.get("id")
            if id_str is not None:
                elements[id_str] = element

    return elements


class TreeStats:
    """
    For every user count
        - number of messages
        - number of total characters

    Also: offer possibilities for sorting and reporting
    """
    def __init__(self):

        self.total_messages = 0
        self.total_users = 0
        self.message_count = collections.defaultdict(lambda: 0)
        self.char_count = collections.defaultdict(lambda: 0)
        self.hashtag_count = collections.defaultdict(lambda: 0)

        User.init_cache()


    def report(self, Nmax=None, fpath=None):
        tab = tabulate.tabulate
        lines = []
        lines.append("message count stats")
        lines.append(tab(sort_items(self.message_count.items(), reverse=True)[:Nmax], showindex=True))
        lines.append("\n")
        lines.append("character count stats")
        lines.append(tab(sort_items(self.char_count.items(), reverse=True)[:Nmax], showindex=True))
        lines.append(f"sum of all posts: {sum_items(self.char_count.items())}")

        lines.append("\n")
        lines.append("hashtag stats")
        lines.append(tab(sort_items(self.hashtag_count.items(), reverse=True)[:Nmax], showindex=True))

        lines.append("\n")
        lines.append(self.follower_report(Nmax=Nmax))

        res_str = "\n".join(lines)
        if fpath:
            with open(fpath, "w") as fp:
                fp.write(res_str)
            print(f"File written: {fpath}")
        else:
            print(res_str)

    def follower_report(self, Nmax=None) -> list:
        account_objs = self.message_count.keys()
        account_followers = []
        aobj: User
        for aobj in account_objs:
            account_followers.append(
                (aobj.acct, aobj.followers_count, self.message_count[aobj], self.char_count[aobj])
            )

        headers = ("account", "followers", "msg count", "char count")
        return tabulate.tabulate(sort_items(account_followers, reverse=True)[:Nmax], showindex=True, headers=headers)

    def hashtag_report(self):
        pass


def sort_items(items, reverse=False):
    items_list = list(items)
    items_list.sort(key=lambda tup: tup[1], reverse=reverse)
    return items_list

def sum_items(items):
    items_list = list(items)
    return sum(list(zip(*items_list))[1])



# based on https://stackoverflow.com/a/295466
def slugify(value, allow_unicode=False):
    """
    Taken from https://github.com/django/django/blob/master/django/utils/text.py
    Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
    dashes to single dashes. Remove characters that aren't alphanumerics,
    underscores, or hyphens. Convert to lowercase. Also strip leading and
    trailing whitespace, dashes, and underscores.
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
    else:
        value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value.lower())
    return re.sub(r'[-\s]+', '-', value).strip('-_')


def script_main():

    print("Script successfully executed")
