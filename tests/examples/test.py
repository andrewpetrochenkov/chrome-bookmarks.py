#!/usr/bin/env python
import chrome_bookmarks

print("folders (%s):" % len(chrome_bookmarks.folders))
for folder in chrome_bookmarks.folders:
    print(folder.name)

print("urls (%s):" % len(chrome_bookmarks.urls))
for url in chrome_bookmarks.urls:
    print(url.url)
    