"""
This module handles all steps to acquire the necessary data to produce a reply graph
"""

import os
from typing import Union
import requests
from collections import OrderedDict

from mastodon import Mastodon, AttribAccessDict, errors

try:
    # useful during development
    from ipydex import IPS
except ModuleNotFoundError:
    pass

from . import settings

from .core_base import (
    FedivisError, get_conf,
    get_root_id_from_url,
)
from .node_manager import NodeManager
from .utils import FediRequestCache


class DataFetcher:

    def __init__(self, confpath: str, spov_mode: bool = False):
        self.confpath = confpath
        self.mc: Mastodon = None
        self.spov_mode = spov_mode
        self.root_id: str = None
        self.cache_metadata: dict = None

    def _handle_cached_request(self, use_cache: Union[bool, FediRequestCache], cachepath: str) -> dict:
        """
        This function handles three cases:

        - (1) file based caching
        - (2) external cache-provider (e.g. database, used by spov)
        - (3) no caching activated
        """

        # Case (1)
        if use_cache is True:
            assert cachepath is not None
            # this is useful for debugging (to prevent too much api traffic)
            import cachewrapper as cw
            normalizer_func = cw.utils.dict_converter_factory(AttribAccessDict, OrderedDict)
            self.mc = cw.CacheWrapper(self.mc, normalize_result=normalizer_func)
            if os.path.isfile(cachepath):
                msg = f"using existing cache file: {cachepath}"
                print(msg)
                self.mc.load_cache(cachepath)
            else:
                msg = f"{cachepath} not found"
                print(msg)
        # Case (2)
        if isinstance(use_cache, FediRequestCache):

            def fallback():
                res: dict = self._wrapped_request(self.mc.status_context, self.root_id)
                # this dict contains "ancestors" and "descendants"
                # now retrieve date for the root node itself
                res["root_node"] = self._wrapped_request(self.mc.status, self.root_id)
                return res

            mc_res = use_cache.get(self.root_id, fallback=fallback)

        # Case (3) and (1, due to cachewrapper)
        else:
            mc_res = self._wrapped_request(self.mc.status_context, self.root_id)
            mc_res["root_node"] = self._wrapped_request(self.mc.status, self.root_id)

        # postprocessing: adapt timestamp of caching
        self.cache_metadata = mc_res.get("__cache_metadata__", {})
        if ts := self.cache_metadata.get("timestamp"):
            self.cache_metadata["timestamp_str"] = ts.strftime(r"%Y-%m-%d %H:%M:%S")
        else:
            self.cache_metadata["timestamp_str"] = None

        assert isinstance(mc_res, dict)
        return mc_res

    def get_node_manager(
            self, url: str,
            hl_string: str = None,
            use_cache: Union[bool, FediRequestCache] = False,
            cachepath: str = None,
        ) -> NodeManager:

        CONF = get_conf(confpath=self.confpath)
        if use_cache == True and cachepath is None:
            cachepath = settings.CACHE_PATH

        # mc means "mastodon-client"
        if self.mc is None:
            self.mc = Mastodon(
                access_token=CONF["access_token"],
                api_base_url=CONF["mastodon_url"],
            )

        self._preparation_step1(url, hl_string, use_cache, cachepath, CONF)

        # TODO: this takes too much time even if cached!
        mc_res = self._handle_cached_request(use_cache=use_cache, cachepath=cachepath)
        self.nm = NodeManager(
            root_id=self.root_id,
            root_node_data=mc_res["root_node"],
            hl_string=hl_string,
            spov_mode=self.spov_mode
        )

        MAX_NODES = 4000
        if len(mc_res["descendants"]) > MAX_NODES:
            msg = f"The requested graph contains more than {MAX_NODES} nodes and is thus too big to be visualized."
            raise FedivisError(msg, 500)

        self.nm.extend_graph_from_status_list(parent=self.nm.root_node, descendants=mc_res["descendants"])

        # +1 to account for the root node
        # (omitted nodes are those whose parent has been deleted and which are thus disconnected from the graph)
        assert len(self.nm.G) == len(mc_res["descendants"]) - self.nm.omitted_nodes + 1
        if self.spov_mode:
            self.nm.optionally_introduce_additional_level1()
        else:
            self.nm.ensure_node_id_order()

        if use_cache == True:
            # this is for the file-based cache
            self.mc.save_cache(cachepath)

        assert isinstance(self.nm, NodeManager)
        return self.nm

    def _preparation_step1(self, url, hl_string, use_cache, cachepath, CONF):
        """
        The provided url might be a redirect or something similar. This function resolves it.
        """
        if not url.startswith(CONF["mastodon_url"]):
            # the provided url does not belong to our instance
            # -> determine corresponding URL on our instance
            search_res = self.mc.search(url)["statuses"]
            if "/deck/@" in url:
                url = url.replace("/deck/@", "/@")
                search_res = self.mc.search(url)["statuses"]

            if len(search_res) == 0:
                # this is triggered for a url like [1] (copied from a logged in session of another instance)
                # [1] https://social.tchncs.de/deck/@ReproducibiliTeaGlobal@scicomm.xyz/112551561595360270
                # for non-logged in access it should return a 302 redirect response
                try:
                    direct_res =  requests.get(url, allow_redirects=False)
                except requests.exceptions.ConnectionError as ex:
                    # endow the exception with useful information (status and failing url)
                    ex.args = (*ex.args, 404, url)
                    raise ex

                if direct_res.is_redirect:
                    new_url = direct_res.headers["Location"]
                    # call this method again
                    return self.get_node_manager(
                        url = new_url,
                        hl_string = hl_string,
                        use_cache = use_cache,
                        cachepath = cachepath,
                    )

                # some instances seem to not respond with a redirect but with a
                # 'please enable javascript'-page.
                # current problematic url: 'https://toot.teckids.org/@nik/114641557689967190/'
                # We need to access the data otherwise, probably via mastodon api

                # Extract the base URL from the problematic URL
                from urllib.parse import urlparse
                parsed_url = urlparse(url)
                external_instance_url = f"{parsed_url.scheme}://{parsed_url.netloc}"

                # Create a new Mastodon instance for the external instance without access token
                try:
                    external_mc = Mastodon(api_base_url=external_instance_url)
                    # Extract the status ID from the URL
                    status_id = url.rstrip('/').split('/')[-1]
                    external_status = external_mc.status(status_id)

                    self.root_id = external_status["id"]

                except Exception as ex:
                    msg = f"Failed to access external instance {external_instance_url} for url: {url}. Error: {str(ex)}"
                    raise FedivisError(msg, 500)

            if len(search_res) > 1:
                msg = f"unexpected length of search results: {len(search_res)}"
                raise FedivisError(msg, 500)
            if self.root_id is None:
                self.root_id = str(search_res[0]["id"])
        else:
            self.root_id = get_root_id_from_url(url)

    def _wrapped_request(self, func, arg1):
        """
        execute a function and convert errors to expected format
        """
        try:
            return func(arg1)
        except errors.MastodonNotFoundError as ex:
            # this might happen if an account is blocked by our primary retrieval instance
            msg = f"Mastodon API could not find data record for url: {arg1}"
            raise FedivisError(msg, 404)
