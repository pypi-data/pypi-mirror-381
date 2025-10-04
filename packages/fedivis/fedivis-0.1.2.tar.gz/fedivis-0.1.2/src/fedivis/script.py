"""
Command line interface for autobrowser package
"""

import argparse
from ipydex import IPS, activate_ips_on_exception
from . import core_base

activate_ips_on_exception()


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--reply-graph", "-r", help="create reply graph from url", metavar="URL"
    )
    parser.add_argument(
        "--highlight", "-hl", help="highlight nodes which contain a string"
    )
    parser.add_argument(
        "--use-cache", "-c", help="use a cache (save api traffic e.g. for debugging)", action='store_true'
    )
    parser.add_argument(
        "--export-to-png", "-png", help="also create an png file from the svg", action='store_true'
    )
    parser.add_argument(
        "--generate-tree-stats", "-s", help="optionally create tree statistics", action='store_true'
    )
    parser.add_argument(
        "--export-to-yaml", "-y", help="optionally export the graph to yaml", action='store_true'
    )
    parser.add_argument(
        "--spov", "-v", help="create the image in spov-mode", action='store_true'
    )

    args = parser.parse_args()

    if args.reply_graph:
        url = args.reply_graph
        RGG = core_base.ReplyGraphGenerator(spov_mode=args.spov)
        RGG.create_graph(url, hl_string=args.highlight, use_cache=args.use_cache, png=args.export_to_png)
        if args.generate_tree_stats:
            RGG.create_tree_stats()
        if args.export_to_yaml:
            RGG.export_to_yaml()
    else:
        print("nothing to do, see option `--help` for more info")
