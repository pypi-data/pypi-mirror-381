import datetime
from typing import Tuple

import networkx as nx

from . import settings
from .node import Node

# for debugging:

from ipydex import IPS


class NodeManager:
    def __init__(self, root_id, root_node_data: dict, hl_string: str, spov_mode: bool):
        """
        :param root_id:     id of root node
        :param hl_string:   highlight string (optional)
        """
        self.id_map = {}
        self.G = nx.DiGraph()
        self.root_id = root_id
        self.hl_string = hl_string
        self.leaves = {}
        self.node_counter = 1
        self.spov_mode = spov_mode
        self.omitted_nodes = 0
        self.omitted_nodes_list = []  # keep track of omitted nodes (simplify debugging)

        self.root_id = root_id
        root_node_data["hl_string"] = hl_string
        self.running_svg_id = 1
        self.root_node = Node(data=root_node_data, node_id=1)

        # will be set if necessary
        self.trunk_node: Node = None

        self.id_map[root_id] = self.root_node
        self.node_id_map = {self.root_node.node_id: self.root_node}

        # will map level index tuples to node ids, see below
        # (currently not used, might be useful to sort leaves, but current sorting seems fine)
        self.lit_node_id_map = {}

        # node_id is wrt the graph, whereas id is the global id
        # self.id_to__node_id_map = {}  # todo: obsolete?

        # nested list of node ids, e.g. [[0], [1, 3], [2]]
        # meaning that 1 and 3 are on level 1, i.e. direct children of 0 (root node, level 0)
        # and 2 is on level 2
        self.levels = []

        self.add_node(self.root_node)

    def add_node(self, node: Node):

        # ensure consecutive svg_id-values, see comment _DOC__SVG_ID_
        node.svg_id = self.running_svg_id
        self.running_svg_id += 1
        self.G.add_node(node)


    def extend_graph_from_status_list(self, parent, descendants, limit=300):
        """
        :param: parent:         parent node (from self.G)
        :param: descendants:    list of statuses from res["descendants"]
        """

        # node_id_1 and svg_1 is already assigned to root_node
        for node_id, obj_data in enumerate(descendants, start=2):
            obj_data["hl_string"] = self.hl_string
            node = Node(obj_data, node_id=node_id)

            try:
                parent = self.id_map[str(node.data["in_reply_to_id"])]
            except KeyError:
                # omit Nodes without parent (probably they have been deleted)
                self.omitted_nodes +=1
                self.omitted_nodes_list.append(node)
                continue

            # this uses the mastodon id
            self.id_map[node.id] = node

            # this uses our internal id
            self.node_id_map[node.node_id] = node

            # keep track of the leaves (nodes with no children)
            self.leaves.pop(parent.id, None)
            self.leaves[node.id] = node

            self.add_node(node)
            self.G.add_edge(parent, node)
            self.node_counter += 1

    def optionally_introduce_additional_level1(self):
        """
        For better overview we want to add an additional node (trunk_node) at level one.
        It should be displayed directly under the root node.
        The trunk_node should be parent of all nodes with at least one child.
        Those level1-nodes without any child should be direct descendants of the root node
        """

        self.prepare_tree_structure_connectors()
        if len(self.levels) < 2:
            # very short tree, nothing todo
            return

        original_level_1_nodes = self.levels[1]

        level1_leaves = []
        level1_nodes_with_children = []

        for node_id in original_level_1_nodes:
            node = self.node_id_map[node_id]
            successors_iter = self.G.successors(node)
            try:
                next(successors_iter)
            except StopIteration:
                # that node has no successors
                level1_leaves.append(node)
            else:
                level1_nodes_with_children.append(node)

        MIN_NUM_L1_LEAVES = settings.AUX_NODE_MIN_NUM_LEVEL1_LEAVES
        MIN_NUM_L_N_LEAVES = settings.AUX_NODE_MIN_NUM_LEVEL_N_LEAVES
        if len(level1_leaves) < MIN_NUM_L1_LEAVES or len(level1_nodes_with_children) < MIN_NUM_L_N_LEAVES:
            return


        trunk_node_text = (
            "This tree-node does not correspond to a real post. "
            "However, it serves to achieve a more place-efficient arrangement of the nodes."
        )
        data = {
            "id": "__trunk__",
            "tags": [],
            "content": trunk_node_text,
            "url": "",
            "account": {
                "display_name": "spov system", "id": 0, "avatar_static": "", "acct": {},
            },
            "created_at": datetime.datetime.now()
        }
        self.trunk_node = Node(data, self.node_counter, is_auxiliary=True)
        self.trunk_node.dbg_cls = "trunk_node"
        self.node_counter += 1
        self.node_id_map[self.trunk_node.node_id] = self.trunk_node

        level1_lit_list = []
        for j in self.levels[1]:
            if self.node_id_map[j].is_auxiliary:
                continue
            level1_lit_list.append(self.node_id_map[j].lit)
        #  [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5)]

        # get the second arguments
        elements1 = list(zip(*level1_lit_list))[1]
        virtual_index = elements1[len(elements1)//2] - 0.5

        # this is for horizontal connection
        self.trunk_node.lit = (0, virtual_index)
        # this is for graphviz
        self.trunk_node.order_index = level1_leaves[len(level1_leaves)//2].order_index - 0.5

        # trunk_node.order_index = 0

        self.add_node(self.trunk_node)
        self.G.add_edge(self.root_node, self.trunk_node)

        for node in level1_nodes_with_children:
            self.G.remove_edge(self.root_node, node)
            self.G.add_edge(self.trunk_node, node)

        old_G = self.G
        new_G = nx.DiGraph(node_prefix='my_node_')
        new_G.add_nodes_from(sorted(self.G.nodes(data=True), key=lambda n: n[0].lit))
        new_G.add_edges_from(self.G.edges(data=True))
        self.G = new_G
        del old_G

        self.ensure_node_id_order()

    def ensure_node_id_order(self):
        # renumber all nodes to be consistent with the un-influencible node id
        # created by the graphviz renderer (starts at 1?)
        self.node_id_map.clear()
        node: Node
        for i, node in enumerate(self.G.nodes.keys(), start=1):

            node.node_id = i  # _GRAPHVIZ_ID_
            self.node_id_map[i] = node

    def get_yaml_dict(self, node: Node, node_id: int):

        reply_id = node.data["in_reply_to_id"]

        # get the graph-related node_id of the node for which this is an reply

        if rn := self.id_map.get(str(reply_id)):
            reply_node_id = rn.node_id
        else:
            reply_node_id = None
        return node.get_yaml_dict(node_id, reply_node_id)

    def prepare_tree_structure_connectors(self):
        """
        Fill the following data structures.
        self.levels,
        self.lit_node_id_map

        This method might be called several times because the structure of the graph might be
        manipulated for better displayability
        """

        self.levels = []
        self.lit_node_id_map = {}


        def key_func(node: Node) -> Tuple[int]:
            lit = node.lit
            if lit is None:
                lit = ()
            return lit

        def process_level(level: int, node_ids: Tuple[int], lit: Tuple[int]):
            """
            Recursive function which goes through the graph and fills some data structures.
            :param level:       int; distance from the root node
            :param node_ids:    Tuple[int]; sequence of node ids to process
            :param lit:         Tuple[int]; means: level index tuple


            The lit is a tuple of non-negative ints with the following meaning
                - (0,) is the root node.
                - (0, 0) is the first child of the root node (counting "naturally", i.e. starting with 1)
                - (0, 2, 5) is the 6th child of the 3rd child of the root node etc.
            """

            # if there is something to add create a new level-list
            if len(self.levels) == level and node_ids:
                self.levels.append([])

            for idx, node_id in enumerate(node_ids):
                # lit: level index-tuple
                new_lit = lit + (idx,)
                self.lit_node_id_map[new_lit] = node_id
                node = self.node_id_map[node_id]
                node.lit = new_lit
                self.levels[level].append(node.node_id)

                successors = sorted(self.G.successors(node), key=key_func)

                successor_ids = [n.node_id for n in successors]
                process_level(level=level+1, node_ids=successor_ids, lit=new_lit)

        # this processes all levels via recursion
        process_level(level=0, node_ids=[self.root_node.node_id], lit=())
