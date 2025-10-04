import os
import unittest
import pickle
import json
import json

from bs4 import BeautifulSoup

from fedivis import settings, core, core_base, utils

# make old pickle-files work (after refactoring of the mastodon library):
import mastodon
mastodon.utility.AttribAccessDict = mastodon.AttribAccessDict

from ipydex import IPS, activate_ips_on_exception

activate_ips_on_exception()

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# assumes package to be installed by pip install -e
TEST_CACHE = os.path.join(CURRENT_DIR, "data", "test_cache.pcl")
TEST_WORKDIR = os.path.join(CURRENT_DIR, "tmp")

REPO_ROOT = os.path.dirname(CURRENT_DIR)
CONFPATH = os.path.join(REPO_ROOT, "config.toml")

settings.CACHE_PATH = TEST_CACHE

# noinspection PyPep8Naming
class TestCore(unittest.TestCase):
    def setUp(self):
        os.makedirs(TEST_WORKDIR, exist_ok=True)
        self.old_dir = os.getcwd()
        os.chdir(TEST_WORKDIR)

    def test_a_core1(self):
        with open(TEST_CACHE, "rb") as pfile:
            pdict = pickle.load(pfile)

    def test_b_colors(self):
        cc = core_base.get_color_pair_cycler()
        pair1 = next(cc)
        c1, c2 = pair1
        # self.assertNotEqual(c1, c2[:len(c1)])

    def test_c01_graph1(self):

        url = "https://social.tchncs.de/@GratianRiter@bildung.social/110943047250920198"
        RGG = core.ReplyGraphGenerator()
        RGG.create_graph(url, use_cache=True)


    def test_c02_assertion_error(self):
        url = "https://social.vivaldi.net/@StefanMuenz/114812572428261451"
        RGG = core.ReplyGraphGenerator(confpath=CONFPATH)
        RGG.create_graph(url, use_cache=True)

    def test_c03_node_id_problem_in_spov_mode(self):
        url = "https://scicomm.xyz/@MajaMielke/114496625462814972"
        RGG = core.ReplyGraphGenerator(confpath=CONFPATH, spov_mode=True)
        RGG.create_graph(url, use_cache=True, save_inner=True)
        self.assertEqual(RGG.inner_svg_data.count("node-data"), RGG.inner_svg_data.count('class="node"'))


    def test_c04_auxiliary_node(self):
        url = "https://mastodontech.de/@svkd/112469285277802451"
        with utils.temp_setting(settings, 'AUX_NODE_MIN_NUM_LEVEL_N_LEAVES', 2):
            RGG = core.ReplyGraphGenerator(confpath=CONFPATH, spov_mode=True)
            RGG.create_graph(url, use_cache=True, save_inner=True)
            tmp = "This tree-node does not correspond to a real post."
            bs = BeautifulSoup(RGG.inner_svg_data, 'xml')

            aux_node_list = []
            for node_obj in bs.find_all("g", attrs={"class": "node"}):
                node_data = json.loads(node_obj.get("node-data"))
                if node_data["is_auxiliary"]:
                    aux_node_list.append((node_obj["id"], node_data, node_obj))

            self.assertEqual(aux_node_list[0][1]["node_id"], 9)
            self.assertEqual(aux_node_list[0][1]["node_svg_id"], 15)

            trunk_node_svg_obj = aux_node_list[0][2]
            self.assertEqual(trunk_node_svg_obj.find("path")["stroke"], "#c0c0c0")
