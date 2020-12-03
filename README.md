<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/chrome-bookmarks.svg?maxAge=3600)](https://pypi.org/project/chrome-bookmarks/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/chrome-bookmarks.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/chrome-bookmarks.py/actions)

### Installation
```bash
$ [sudo] pip install chrome-bookmarks
```

#### Features
OS|path
-|-
`Linux`|`~/.config/google-chrome/Default/Bookmarks`
`macOS`|`~/Library/Application Support/Google/Chrome/Default/Bookmarks`
`Windows`|`~\AppData\Local\Google\Chrome\User Data\Default\Bookmarks`

#### Examples
```python
import chrome_bookmarks

for folder in chrome_bookmarks.folders:
    print(folder.name)
    print(folder.folders)
```

```python
for url in chrome_bookmarks.urls:
    print(url.url, url.name)
```

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>
