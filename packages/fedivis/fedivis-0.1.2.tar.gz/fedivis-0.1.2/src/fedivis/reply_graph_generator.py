import os
import datetime
import xml.etree.ElementTree as ET
import json
from typing import Tuple, Union

from mastodon import errors

from bs4 import BeautifulSoup, Tag

import networkx as nx

# monkey-patch workaround because nxv currently is broken for new networkx releases

if not hasattr(nx, "OrderedGraph"):
    nx.OrderedGraph = nx.Graph
    nx.OrderedDiGraph = nx.DiGraph
    nx.OrderedMultiGraph = nx.MultiGraph
    nx.OrderedMultiDiGraph = nx.MultiDiGraph

import nxv
import bleach

try:
    # useful during development
    from ipydex import IPS
except ModuleNotFoundError:
    pass

from . import settings

from .utils import FediRequestCache
from .data_acquisition import DataFetcher
from .node import Node
from .core_base import (
    FedivisError, TreeStats, User, get_conf,
    get_root_id_from_url, get_element_dict_by_id, slugify,
    GLOBAL_REPLACEMENT_TUPLES, SHORT_DATE_FORMAT, AVATAR_SIZE
)
from .node_manager import NodeManager

class ReplyGraphGenerator:

    def __init__(self, spov_mode: bool = False, graphviz_bin=None, confpath=None):
        """
        :param spov_mode:   generate the graph tailored for the spov web application
        """
        self.root_id: str = None
        self.svg_data: bytes = None
        self.inner_svg_data: str = None
        self.viewbox: list = None
        self.nm: NodeManager = None
        self.df: DataFetcher = None
        self.tree_stats = None
        self.spov_mode = spov_mode

        # this is needed for a specific unittest
        self.default_confpath = confpath

        # this is necessary to enforce custom graphviz version on uberspace
        self.graphviz_bin = graphviz_bin

        # influence how the nodes are created
        Node.spov_mode = spov_mode

    @property
    def cache_metadata(self):
        return self.df.cache_metadata

    def create_graph(self, url: str, hl_string: str = None, use_cache=False, png=False, save_inner=False):
        """
        calls _generate_svg_data and saves the result

        :param save_inner:  bool; save self.inner_svg_data (True) or self.svg_data (False)
        """

        self._generate_svg_data(url, hl_string, use_cache)

        if hl_string:
            hl_fname_appendix = f"_HL_{slugify(hl_string)}"
        else:
            hl_fname_appendix = ""

        svg_fname = f"toot-analysis-{self.root_id}{hl_fname_appendix}.svg"
        svg_fpath = os.path.abspath(svg_fname)

        if save_inner:
            data_to_save = self.inner_svg_data.encode("utf-8")
        else:
            data_to_save = self.svg_data

        with open(svg_fpath, "wb") as svgfile:
            svgfile.write(data_to_save)
        print("File written:", svg_fpath)
        if png:
            assert svg_fpath[-4:] == ".svg"
            png_fpath = f"{svg_fpath[:-4]}.png"

            # this requires 'imagemagick' installed
            cmd = f"convert {svg_fpath} {png_fpath}"
            ret = os.system(cmd)
            if ret == 0:
                print("File written:", png_fpath)
            else:
                print("Error during creation of", png_fpath)

    def _generate_svg_data(self, url: str, hl_string: str = None, use_cache=False):
        """
        Creates the graph
        """
        self._prepare_node_manager(url=url, hl_string=hl_string, use_cache=use_cache)
        self._generate_svg_data_from_nm()

    def _prepare_node_manager(
            self, url: str,
            hl_string: str = None,
            use_cache: Union[bool, FediRequestCache] = False,
            cachepath: str = None,
            confpath: str = None,
        ):

        if confpath is None:
            confpath = self.default_confpath

        self.df = DataFetcher(confpath=confpath, spov_mode=self.spov_mode)
        self.nm = self.df.get_node_manager(url, hl_string, use_cache, cachepath)

    def _generate_svg_data_from_nm(self):

        # <title>node0009</title>
        old_title_str_template = "<title>node{:04d}xx</title>"
        new_title_str_template = "<title>{}</title>"

        # generate replacement tuples
        rpl_tuples = []
        node: Node
        for node in self.nm.G.nodes:
            # todo: add + 1 here?
            s1 = old_title_str_template.format(node.node_id)

            title_content = f"{node.date_str} {node.time_str}\n{node.get_stripped_content()}"
            s2 = new_title_str_template.format(title_content)
            rpl_tuples.append((s1, s2))

        # define style for graph visualization

        # see https://nxv.readthedocs.io/en/latest/reference.html#styling
        style = nxv.Style(
            graph={"rankdir": "TB"},
            node=lambda u, d: u.style_dict,
                # u is a node and d is its attribute dict (which is ignored here)
            edge=lambda u, v, d: {"style": "solid", "arrowType": "normal", "label": ""},
        )

        # create the raw SVG of the graph

        self.raw_svg_data = nxv.render(self.nm.G, style, format="svg", graphviz_bin=self.graphviz_bin)

        if self.spov_mode:
            self._post_process_raw_svg_for_avatarmode()
        else:
            self._post_process_raw_svg_for_textmode(rpl_tuples)

        assert self.svg_data is not None
        self.create_inner_svg()
        self.root_id = self.nm.root_id

        if not self.spov_mode:
            # print some rough status info on the cli
            N = len(self.nm.G)
            print(f"{N} nodes processed")

    def _get_new_clip_path(self, node_id_str, x, y):
        """
        create something like
        <clipPath id="cp_node5">
            <rect x="74" y="-300" width="38" height="38" rx="10" ry="10" />
        </clipPath>
        """
        s = AVATAR_SIZE
        r = "11"
        clippath = Tag(name="clipPath", attrs={"id": f"cp_{node_id_str}"})
        rect = Tag(name="rect", attrs={"x": x, "y": y, "width": s,  "height": s, "rx": r,  "ry": r})
        clippath.append(rect)
        return clippath

    def _post_process_raw_svg_for_avatarmode(self) -> None:

        self.svg_data = self.raw_svg_data.decode("utf8")

        self.bs = BeautifulSoup(self.svg_data, 'xml')

        svg_obj = self.bs.find("svg")
        self.defs = Tag(name="defs")
        svg_obj.insert(0, self.defs)
        self.defs.append("\n")

        # new_xml_snippet = """<new_element>This is a new element</new_element>"""
        # new_tag = BeautifulSoup(new_xml_snippet, 'xml').new_element

        self.__process_g_elements()
        self.svg_data = self.bs.encode("utf8")

    def __process_g_elements(self):

        g_elements = get_element_dict_by_id(self.bs, "g")

        node: Node
        for _, node in self.nm.node_id_map.items():
            node_id_str = f"node{node.node_id}"

            g_element = g_elements[node_id_str]
            if not self.spov_mode and node.highlight:
                # in spov mode this is handled by javascript
                class_string = f'{g_element["class"]} node_highlight'
            else:
                class_string = f'{g_element["class"]}'

            g_element["class"] = class_string
            path = g_element.find("path")
            path.attrs["stroke-width"] = 3
            path.attrs["fill-opacity"] = 0.7

            txt_element = g_element.find("text")
            x, y = float(txt_element["x"]), float(txt_element["y"])
            s = AVATAR_SIZE
            d = AVATAR_SIZE/2

            xp = x - d
            yp = y - d*1.08
            img_url = node.data["account"]["avatar_static"]
            attrs = {"clip-path": f"url(#cp_{node_id_str})"}
            img_tag = Tag(name="image", attrs=attrs)
            img_tag["xlink:href"] = img_url
            img_tag["x"] = xp
            img_tag["y"] = yp
            img_tag["width"] = s
            img_tag["height"] = s
            self.defs.append(self._get_new_clip_path(node_id_str, xp, yp))
            self.defs.append("\n")

            g_element.insert(0, img_tag)
            txt_element.decompose()

    def _post_process_raw_svg_for_textmode(self, rpl_tuples) -> None:

        entity_links = []

        for node in self.nm.G.nodes.keys():
            date = node.data["created_at"]

            # this is needed because in the unittest data the type had been converted
            if isinstance(date, str):
                date = datetime.datetime.fromisoformat(date)

            if date:
                short_date_time_str = f'{date.strftime(SHORT_DATE_FORMAT)} {date.strftime("%H:%M")}'
                str1 = f'<a href="{node.data["url"]}" target="_blank">{short_date_time_str}</a>'
                str2 = f'<a href="{node.data["url"]}" target="_blank">{len(node.get_stripped_content())}C</a>'
            else:
                str1 = str2 = ""

            entity_links.append((f"A{node.id}", bleach.clean(node.author)))
            entity_links.append((f"K{node.id}", str1))
            entity_links.append((f"X{node.id}", str2))

        # insert links to wiki data urls
        self.raw_svg_data = self.raw_svg_data.decode("utf8").format(**dict(entity_links))

        # this looks like inefficient but can be tolerated as it is not used in spov mode
        import time
        t1 = time.time()
        for s1, s2 in rpl_tuples + GLOBAL_REPLACEMENT_TUPLES:
            self.raw_svg_data = self.raw_svg_data.replace(s1, s2)
        dt = time.time() - t1
        # print(f"{dt=}")

        self.svg_data = self.raw_svg_data.encode("utf8")

    def create_inner_svg(self):
        """
        create self.inner_svg_data as str for embedding in html
        """
        bs = BeautifulSoup(self.svg_data, 'xml')
        self.inner_svg_data = bs.find("svg").decode()
        self.calc_viewbox()

        g_elements = get_element_dict_by_id(bs, "g")

        # add relevant data as json (to make it accessible from js)
        node: Node
        for node in self.nm.G.nodes():
            node_svg_id = node.svg_id
            assert node_svg_id is not None

            # _DOC__SVG_ID_
            # note: .svg_id is different from .node_id in 2 aspects:
            # - for svg_id counting starts with 1, for node_id with 0
            # all svg_ids are consecutive integers while some node_id-values might be missing (omitted nodes)

            node_id_str = f"node{node.node_id}"
            g_element = g_elements[node_id_str]

            node_data = {
                "date_str": node.date_str,
                "time_str": node.time_str,
                "author": node.author,
                "url": node.data["url"],
                "author_avatar": node.data["account"]["avatar_static"],
                "impact_str": node.impact_str,
                "content": node.stripped_content,
                "is_auxiliary": node.is_auxiliary,
                "node_id": node.node_id,  # this is to ensure consistency between svg id and python id (not trivial)
                "node_svg_id": node.svg_id,
                "node_obj_id": node.id,# for debugging only
                "node_name": repr(node), # for debugging only
            }
            g_element["node-data"] = json.dumps(node_data)

        # convert the DOM back to string representation
        self.inner_svg_data = bs.decode()

        for s1, s2 in GLOBAL_REPLACEMENT_TUPLES:
            self.inner_svg_data = self.inner_svg_data.replace(s1, s2)

    def get_tree_structure_connectors(self):
        """
        For navigating through the tree: find horizontal and vertical connections.

        This function uses the "Level Index Tuple" (short: lit).

        It is a tuple of non-negative ints with the following meaning
            - (0,) is the root node.
            - (0, 0) is the first child of the root node (counting "naturally", i.e. starting with 1)
            - (0, 2, 5) is the 6th child of the 3rd child of the root node etc.
        """
        # this sets n.lit for each node
        self.nm.prepare_tree_structure_connectors()

        # connect horizontally
        for level in self.nm.levels:
            assert len(level) > 0

            # originally we used node.order_index -> sometimes strange orders
            # now we use node.lit
            level.sort(key=lambda j: self.nm.node_id_map[j].lit)

            # connect 0 <-> 1, 1 <-> 2, etc
            for node_id1, node_id2 in zip(level[:-1], level[1:]):
                self._connect_nodes(node_id1, node_id2, "horizontal")

            # connect last with first
            self._connect_nodes(level[-1], level[0], "horizontal")

        # connect vertically
        # sort leaves according to (maybe changed) structure
        leaves = sorted(self.nm.leaves.values(), key=lambda n: n.lit)
        for leave_node in leaves:
            self._connect_up(leave_node)

        bs = BeautifulSoup(self.inner_svg_data, 'xml')
        g_elements = get_element_dict_by_id(bs, "g")

        for node in self.nm.G.nodes.keys():
            node_id = node.node_id
            node_id_str = f"node{node_id}"
            g_element = g_elements[node_id_str]

            connection_data = {
                "prev_horizontal": node.prev_horizontal,
                "next_horizontal": node.next_horizontal,
                "next_vertical": node.next_vertical,
                "prev_vertical": node.prev_vertical,
            }

            g_element["node-connections"] = json.dumps(connection_data)

        self.inner_svg_data = bs.decode()

    def _connect_up(self, node: Node):
        """
        Recursive function to vertically connect the current node with its direct parent.
        End recursion once an existing connection is found or at root level.
        """
        predecessors: Tuple[Node] = tuple(self.nm.G.predecessors(node))

        if len(predecessors) == 0:
            return

        assert len(predecessors) == 1

        self._connect_nodes(predecessors[0].node_id, node.node_id, "vertical")
        if predecessors[0].next_vertical != f"node{node.node_id}":
            # this connection has not been set (due to earlier existing)
            # do not go further up the tree (towards the root)
            return
        else:
            self._connect_up(predecessors[0])

    def _connect_nodes(self, node_id1: int, node_id2: int, mode: str):
        """
        Save horizontal and vertical connections as node attributes.
        Existing vertical connections are not overwritten
        """
        node1: Node = self.nm.node_id_map[node_id1]
        node2: Node = self.nm.node_id_map[node_id2]

        if mode == "horizontal":
            node1.next_horizontal = f"node{node2.node_id}"
            node2.prev_horizontal = f"node{node1.node_id}"
        elif mode == "vertical":
            if node1.next_vertical is None:
                node1.next_vertical = f"node{node2.node_id}"
            if node2.prev_vertical is None:
                node2.prev_vertical = f"node{node1.node_id}"
        else:
            msg = f"unknown mode: {mode}"
            raise ValueError(mode)

    def calc_viewbox(self):

        # Load the SVG file
        tree0 = ET.fromstring(self.svg_data.decode("utf8"))
        tree = ET.fromstring(self.inner_svg_data)

        svg_node = next(tree.iter())

        viewbox_str = svg_node.attrib.get("viewBox")
        self.viewbox =[float(x) for x in viewbox_str.split(" ")]

    def create_tree_stats(self, save=True):

        self.tree_stats = TreeStats()
        node: Node
        for node in self.nm.G:
            self.tree_stats.total_messages += 1
            user = User.make_user(node.data["account"])
            self.tree_stats.message_count[user] += 1
            self.tree_stats.char_count[user] += len(node.get_stripped_content())
            for tag_dict in node.tags:
                tag = f'#{tag_dict["name"]}'
                self.tree_stats.hashtag_count[tag] += 1

        self.tree_stats.total_users = len(User.cache)
        if self.nm.trunk_node is not None:
            self.tree_stats.total_users -= 1
            self.tree_stats.total_messages -= 1

        if save:
            self.tree_stats.report(Nmax=10)
            report_fname = f"toot-report-{self.root_id}.txt"
            self.tree_stats.report(fpath=report_fname)

    def export_to_yaml(self):
        import yaml
        node: Node
        res = []
        for node_id, node in enumerate(self.nm.G):
            res.append(self.nm.get_yaml_dict(node, node_id))

        yaml_fpath = f"toot-graph-{self.root_id}.yaml"

        with open(yaml_fpath, "w") as myfile:
            yaml.safe_dump(res, myfile, allow_unicode=True, sort_keys=False)
