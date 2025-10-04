import datetime
import bleach
from .core_base import get_formatted_followers_count, get_author_colors



class Node(object):
    spov_mode = False
    def __init__(self, data: dict, node_id: int, is_auxiliary=False):
        self.id = str(data["id"])
        self.order_index = node_id  # this might be changed by a function
        self.is_auxiliary = is_auxiliary

        # this will be reassigned with the id given by graphviz, see _GRAPHVIZ_ID_
        self.node_id = node_id
        self.svg_id = node_id + 1 # see comment for _DOC__SVG_ID_
        self.label = self.id
        self.data = data
        self.tags = data["tags"]
        self.title = "title"
        self.lit = None # level index tuple
        self.stripped_content = None

        # attributes to store connections for navigating through the nodes
        self.prev_horizontal = None
        self.next_horizontal = None
        self.prev_vertical = None
        self.next_vertical = None

        self.dbg_cls = "normal"

        display_name = data["account"]["display_name"]
        if display_name:
            self.author = display_name
        else:
            self.author = data["account"]["username"]
        if self.spov_mode:
            N = 25
        else:
            N = 10
        if len(self.author) > N:
            self.author = f"{self.author[:N-2]}…"
        # label-trick: generate strings like r'{K12345}'
        # these can be substituted later -> multiple keys for line break

        sep = "\n"
        if favs := self.data.get("favourites_count"):
            star_str = f"\n{favs}__FAVS__"
            sep = " "
        else:
            star_str = ""
        if boosts := self.data.get("reblogs_count"):
            # include line break only if necessary
            boosts_str = f"{sep}{boosts}__BOOSTS__"
            sep = " "
        else:
            boosts_str = ""

        followers_str = f"{sep}{get_formatted_followers_count(self.data)}__FF__"

        if star_str and boosts_str:
            self.impact_str = f"{star_str}{boosts_str}\n{followers_str}"
        else:
            self.impact_str = f"{star_str}{boosts_str}{followers_str}"


        self.repr_str = f"{{K{self.id}}}\n{{A{self.id}}}\n{{X{self.id}}}{self.impact_str}"

        self.highlight = None
        self.decide_highlight()

        edge_color, fill_color = self.get_colors()
        self.style_dict = {
            "color": f"{edge_color}",
            "fillcolor": fill_color,  # add low alpha-value for transparency
            "style": "filled, rounded",
            "shape": "square",
            "fontname": "Open Sans",
            "fixedsize": True,
            "width": 0.7,
            "fontsize": 8,
            "peripheries": 1, # more would be possible but I was unable to assign different colors
            "penwidth": 2,
        }

        self.date_str = self.time_str = ""
        self._get_date_and_time_str()
        self.adapt_for_spov_mode()

    def decide_highlight(self):
        if self.spov_mode:
            # in spov mode highlight is handled by java script
            return False
        if hl_string := self.data.get("hl_string"):
            if hl_string.lower() in self.data["content"].lower():
                self.highlight = True
            else:
                self.highlight = False

    def get_colors(self):
        """
        return node color (either for author-based coloring or for string highlighting)
        """

        if self.is_auxiliary:
            c = "#"+"c0"*3
            return c, c

        no_hl_color = "#777777"  # medium grey
        hl_color = "#ff7f0e"  # matplotlib orange
        if self.data.get("hl_string"):
            if self.highlight:
                return hl_color, hl_color + "20"
            else:
                return no_hl_color, no_hl_color + "20"
        else:
            return get_author_colors(self.data)

    def adapt_for_spov_mode(self):
        if self.spov_mode:
            self.repr_str = f"__node{self.node_id+1}__"

    def get_stripped_content(self):
            if self.stripped_content is not None:
                return self.stripped_content


            if self.spov_mode:
                allowed_tags = ["br", "a"]
            else:
                allowed_tags = []
            self.stripped_content = bleach.clean(self.data["content"], tags=allowed_tags, strip=True)

            # "&nbsp;" caused problems once
            self.stripped_content = self.stripped_content.replace("&nbsp;", " ")
            return self.stripped_content

    def get_yaml_dict(self, node_id, reply_node_id):
        """
        :param node_id:     int, id wrt the current graph (different from the global `id`)
        """

        if reply_node_id is not None:
            reply_diff = node_id - reply_node_id
        else:
            reply_diff = None

        res = {
            "id": self.id,
            "node_id": node_id,
            "in_reply_to_id": reply_node_id,
            "reply_diff": reply_diff,
            "delimiter1": "-"*5,
            "author": f'@{self.data["account"]["acct"]}',
            "content": self.get_stripped_content(),
            "delimiter2": "-"*5,
            "tags": {
                "approval_to_parent (-10, 10)": None,
                "kindness (-10, 10)": None,
                "information_content (0, 10)": None,
                "emotion_content (0, 10)": None,
            },
            "delimiter3": "-"*20,
        }

        if reply_node_id is None:
            res["tags"].pop("approval_to_parent (-10, 10)")

        return res

    def _get_date_and_time_str(self):
        date = self.data["created_at"]

        # this is needed because in the unittest data the type had been converted
        if isinstance(date, str):
            date = datetime.datetime.fromisoformat(date)

        if date:
            self.date_str = date.strftime(r"%Y-%m-%d")
            self.time_str = date.strftime(r"%H:%M:%S")

    def __repr__(self):

        # return self.repr_str
        return f"node_{self.svg_id}{self.dbg_cls[0]}"
