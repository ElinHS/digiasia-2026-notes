#!/usr/bin/env python3
"""Wrap src/digiasia-notes.html into a standalone ../index.html for GitHub Pages."""
import pathlib
HERE = pathlib.Path(__file__).parent
b = (HERE / "digiasia-notes.html").read_text()
pre = '<!doctype html>\n<html lang="zh-Hant">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
k = '</style>\n\n<div class="view" data-view="home">'
assert b.count(k) == 1
b = b.replace(k, '</style>\n\n<style>body{margin:0}img{max-width:100%}</style>\n</head>\n<body>\n<div class="view" data-view="home">')
(HERE.parent / "index.html").write_text(pre + b + '\n</body>\n</html>\n')
