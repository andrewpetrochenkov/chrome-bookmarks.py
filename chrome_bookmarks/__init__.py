#!/usr/bin/env python
import datetime
import json
import os
import public
import sys


@public.add
class Item(dict):
    """Item class, dict based. properties: `id`, `name`, `type`, `url`, `folders`, `urls`"""

    @property
    def id(self):
        return self["id"]

    @property
    def name(self):
        return self["name"]

    @property
    def type(self):
        return self["type"]

    @property
    def url(self):
        if "url" in self:
            return self["url"]
        return ""

    @property
    def added(self):
        return datetime.datetime.fromtimestamp(self["date_added"])

    @property
    def modified(self):
        if "date_modified" in self:
            datetime.datetime.fromtimestamp(self["date_modified"])

    @property
    def folders(self):
        items = []
        for children in self["children"]:
            if children["type"] == "folder":
                items.append(Item(children))
        return items

    @property
    def urls(self):
        items = []
        for children in self["children"]:
            if children["type"] == "url":
                items.append(Item(children))
        return items


@public.add
class Bookmarks:
    """Bookmarks class. attrs: `path`. properties: `folders`, `urls`"""
    path = None

    def __init__(self, path):
        self.path = path
        self.data = json.loads(open(path).read())

    @property
    def folders(self):
        items = []
        for key, childrens in json.loads(open(path).read())["roots"]["bookmark_bar"].items():
            if key == "children":
                for children in childrens:
                    if "type" in children and children["type"] == "folder":
                        items.append(Item(children))
        return items

    @property
    def urls(self):
        items = []
        for key, childrens in self.data["roots"]["bookmark_bar"].items():
            if key == "children":
                for children in childrens:
                    if "type" in children and children["type"] == "url":
                        items.append(Item(children))
        return items


paths = [
    os.path.expanduser("~/.config/google-chrome/Default/Bookmarks"),
    os.path.expanduser("~/Library/Application Support/Google/Chrome/Default/Bookmarks"),
    os.path.expanduser("~\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Bookmarks")
]
path = ""
if "linux" in sys.platform.lower():
    path = "~/.config/google-chrome/Default/Bookmarks"
if "darwin" in sys.platform.lower():
    path = "~/Library/Application Support/Google/Chrome/Default/Bookmarks"
if "win32" in sys.platform.lower():
    path = "~\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Bookmarks"
path = os.path.expanduser(path)

folders = []
urls = []

for f in paths:
    if os.path.exists(f):
        folders = Bookmarks(f).folders
        urls = Bookmarks(f).urls
