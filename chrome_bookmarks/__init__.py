__all__ = ['Item', 'Bookmarks']


from datetime import datetime, timezone, timedelta
import json
import os
import sys


def dateFromWebkit(timestamp):
    epochStart = datetime(1601, 1, 1)
    delta = timedelta(microseconds=int(timestamp))
    return (epochStart + delta).replace(tzinfo=timezone.utc).astimezone()


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
        return dateFromWebkit(self["date_added"])

    @property
    def modified(self):
        if "date_modified" in self:
            return dateFromWebkit(self["date_modified"])

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


class Bookmarks:
    """Bookmarks class. attrs: `path`. properties: `folders`, `urls`"""
    path = None

    def __init__(self, path):
        self.path = path
        with open(path, encoding="utf-8") as f:
            self.data = json.load(f)
        self.attrList = self.processRoots()
        self.urls = self.attrList["urls"]
        self.folders = self.attrList["folders"]

    def processRoots(self):
        attrList = {"urls": [], "folders": []}
        with open(path, encoding="utf-8") as f:
            roots_data = json.load(f)
        for key, value in roots_data["roots"].items():
            if "children" in value:
                self.processTree(attrList, value["children"])
        return attrList

    def processTree(self, attrList, childrenList):
        for item in childrenList:
            self.processUrls(item, attrList, childrenList)
            self.processFolders(item, attrList, childrenList)

    def processUrls(self, item, attrList, childrenList):
        if "type" in item and item["type"] == "url":
            attrList["urls"].append(Item(item))

    def processFolders(self, item, attrList, childrenList):
        if "type" in item and item["type"] == "folder":
            attrList["folders"].append(Item(item))
            if "children" in item:
                self.processTree(attrList, item["children"])


paths = [
    os.path.expanduser("~/.config/google-chrome/Default/Bookmarks"),
    os.path.expanduser(
        "~/Library/Application Support/Google/Chrome/Default/Bookmarks"),
    os.path.expanduser(
        "~\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Bookmarks")
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
        instance = Bookmarks(f)
        folders = instance.folders
        urls = instance.urls
