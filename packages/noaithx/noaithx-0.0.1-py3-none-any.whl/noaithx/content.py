import os
import glob
import json
import random

DEFAULT_CONTENT_PATH = os.path.join(os.path.dirname(__file__), "content")
DEFAULT_OPENER_FILE = "opener.txt"
DEFAULT_CLOSER_FILE = "closer.txt"
DEFAULT_CONTENT_GLOB = "*.json"

class BaseContent:
    @staticmethod
    def grab_text(*path):
        with open(os.path.join(*path), "r") as f:
            return f.read()

    @staticmethod
    def validate_content(content_dict, filename):
        req_fields = [("name", str), ("description", str), ("content", list)]
        for field, field_type in req_fields:
            if field not in content_dict:
                raise ValueError("{} is missing the '{}' field".format(filename, field))
            elif not isinstance(content_dict[field], field_type):
                raise ValueError("{} has the wrong type for '{}': should be '{}' not '{}'".format(filename, field, field_type, type(content_dict[field])))
        return content_dict

class Content(BaseContent):
    @staticmethod
    def grab_content(path, content_glob, merge_content=None):
        content = {}

        for file in glob.glob(os.path.join(path, content_glob)):
            json_dict = BaseContent.validate_content(json.loads(BaseContent.grab_text(file)), file)
            content[json_dict["name"]] = {"description": json_dict["description"], "content": json_dict["content"]}

        if merge_content is not None:
            content = {**merge_content, **content}
        return content

    @classmethod
    def list_groups(cls):
        return list(cls.content.keys())

    @classmethod
    def list_content(cls, groups=None):
        ret = []
        if groups is None:
            groups = cls.list_groups()
        for group in groups:
            ret.append("Group " + "'" + group + "': " + cls.content[group]["description"] + "\n" + "\n".join(["\t" + x for x in cls.content[group]["content"]]))
        return "\n\n".join(ret)

    @classmethod
    def get_lines(cls, groups=None):
        if groups is None:
            groups = cls.list_groups()
        ret_lines = []
        for group in groups:
            ret_lines.extend(cls.content[group]["content"])
        return ret_lines

    @classmethod
    def get_random_line(cls, groups=None):
        if groups is None:
            groups = cls.list_groups()
        return random.choice(cls.get_lines(groups=groups))

    @classmethod
    def get_block(cls, content_line):
        return cls.opener + content_line + '\n' + cls.closer

    @classmethod
    def get_random(cls, groups=None):
        if groups is None:
            groups = cls.list_groups()
        return cls.get_block(cls.get_random_line(groups=groups))

    opener = BaseContent.grab_text(DEFAULT_CONTENT_PATH, DEFAULT_OPENER_FILE)
    closer = BaseContent.grab_text(DEFAULT_CONTENT_PATH, DEFAULT_CLOSER_FILE)
    content = grab_content(DEFAULT_CONTENT_PATH, DEFAULT_CONTENT_GLOB)

