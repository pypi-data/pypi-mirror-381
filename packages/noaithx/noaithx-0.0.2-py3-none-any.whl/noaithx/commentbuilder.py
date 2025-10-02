from .commenter import Commenter, DEFAULT_WIDTH

class CommentBuilder:
    commenters = {
        "c89": Commenter(start="/*", end="*/", multiline_header="*"),
        "cpp": "c99",
        "c++": "c99",
        "javascript": "c99",
        "js": "javascript",
        "c99": Commenter(start="//", multiline_start="/*", multiline_end="*/", multiline_header="*"),
        "python": Commenter(start="#"),
        "bash": "python",
        "sh": "bash",
        "awk": Commenter(start="#", multiline_start="###", multiline_end="###"),
        "julia": Commenter(start="#", multiline_start="#*", multiline_end="*#"),
        "powershell": Commenter(start="#", multiline_start="<#", multiline_end="#>"),
        "zig": Commenter(start="//", multiline_start="(*", multiline_end="*)"),
        "haskel": Commenter(start="--", multiline_start="{-", multiline_end="-}"),
        "lua": Commenter(start="--", multiline_start="--[[", multiline_end="]]"),
        "basic": Commenter(start="REM"),
        "vbnet": Commenter(start="'"),
        "vimscript": Commenter(start='"'),
        "matlab": Commenter(start="%", multiline_start="%{", multiline_end="%}"),
        "asm": Commenter(start=";"),
        "scheme": Commenter(start=";", multiline_start="#|", multiline_end="|#"),
        "html": Commenter(start="<!--", end="-->", multiline_start_newline=True, multiline_alignto=False, multiline_spaces_after=0)
    }
    default_width = DEFAULT_WIDTH

    @classmethod
    def get_commenter(cls, commenter, alias_stack=None):
        if alias_stack is None:
            alias_stack = []
        if isinstance(commenter, str):
            alias_stack.append(commenter)
            try:
                commenter = cls.commenters[commenter]
            except KeyError as e:
                raise ValueError("No such commenter '{}' - choose from '{}'".format(e.args[0], cls.list_commenters())) from e
        if isinstance(commenter, Commenter):
            return commenter
        elif isinstance(commenter, str):
            if commenter in alias_stack:
                raise Exception("Alias cycle detected! '{}'".format("->".join(alias_stack + [commenter])))
            return cls.get_commenter(commenter, alias_stack=alias_stack)
        else:
            raise ValueError("Invalid Commenter '{}'".format(commenter))

    @classmethod
    def gen_comment(cls, text, commenter, width=None, multiline_header=None, multiline_alignto=None,
                       multiline_start_newline=None, spaces_before=None, spaces_after=None,
                       multiline_spaces_after=None):
        if width is None:
            width = cls.default_width
        width = int(width)
        if isinstance(commenter, str):
            commenter = cls.get_commenter(commenter)
        return commenter(text, width=width, multiline_header=multiline_header, multiline_alignto=multiline_alignto,
                        multiline_start_newline=multiline_start_newline, spaces_before=spaces_before,
                        spaces_after=spaces_after, multiline_spaces_after=multiline_spaces_after)

    @classmethod
    def list_commenters(cls, show_commenter=False, show_alias=False):
        name_list = sorted(list(cls.commenters.keys()))
        if show_commenter is False and show_alias is False:
            return name_list
        ret = []
        for name in name_list:
            commenter = cls.commenters[name]
            new_str = name
            while isinstance(commenter, str):
                if show_alias:
                    new_str += "->" + commenter
                commenter = cls.commenters[commenter]
            if show_commenter:
                new_str += ": " + str(commenter)
            ret.append(new_str)
        return ret
