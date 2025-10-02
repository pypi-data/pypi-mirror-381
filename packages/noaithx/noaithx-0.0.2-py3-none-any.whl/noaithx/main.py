import sys
import argparse

from .commentgen import CommentGen

def gen_argparser():
    parser = argparse.ArgumentParser(description="Anti-AI comment generator", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--commenter", "-c", help="Comment generator to use (required)", choices=CommentGen.get_commenters())
    parser.add_argument("--groups", "-g", help="Comment groups to use", choices=CommentGen.get_groups(), default=CommentGen.get_groups(), nargs="+", action="append")
    parser.add_argument("--indent", "-i", help="Number of spaces of indent to use", type=int, default=0)
    parser.add_argument("--width", "-w", help="Maximum line width to wrap around", type=int, default=79)
    parser.add_argument("--list-content", help="List all comment content and groups", action="store_true")
    parser.add_argument("--list-commenters", help="List all commenters", action="store_true")
    return parser

def main():
    parser = gen_argparser()
    args = parser.parse_args()
    do_something = True
    if args.list_content:
        do_something = False
        print("Available comment content:\n")
        print(CommentGen.list_content())
    if args.list_commenters:
        do_something = False
        if args.list_content:
            print("")
        print("Available comment generators:\n")
        print(CommentGen.list_commenters())

    if do_something:
        if args.commenter is None:
            print("--commenter is required")
            parser.print_help()
            return 1
        print(CommentGen.gen_comment(args.commenter, groups=args.groups, width=args.width, indent=args.indent))
    return 0
