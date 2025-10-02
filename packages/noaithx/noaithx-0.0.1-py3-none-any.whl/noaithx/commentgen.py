from .commentbuilder import CommentBuilder
from .content import Content

class CommentGen:
    @staticmethod
    def gen_comment(commenter, groups=None, width=None, indent=None):
        return CommentBuilder.gen_comment(Content.get_random(groups=groups), commenter, width=width, spaces_before=indent)

    @staticmethod
    def get_commenters():
        return CommentBuilder.list_commenters()

    @staticmethod
    def list_commenters():
        return "\n".join(CommentBuilder.list_commenters(show_commenter=True))

    @staticmethod
    def get_groups():
        return Content.list_groups()

    @staticmethod
    def list_content():
        return Content.list_content()

