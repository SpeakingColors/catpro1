#!/usr/bin/env python3
"""Writes an offline copy of the patch book: docs/index.html with every patch inlined, so it opens from a file://
URL (browsers refuse fetch() there). Usage: python3 tools/build_offline.py <out.html>"""
import json, os, sys
root = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'docs')
html = open(os.path.join(root, 'index.html'), encoding='utf-8').read()
pats = {'index.json': json.load(open(os.path.join(root, 'patches', 'index.json'), encoding='utf-8'))}
for f in pats['index.json']['patches']:
    pats[f] = json.load(open(os.path.join(root, 'patches', f), encoding='utf-8'))
blob = json.dumps(pats).replace('</', '<\\/')
html = html.replace('<script>', '<script>window.CATPRO1_PATCHES=' + blob + ';</script>\n<script>', 1)
open(sys.argv[1], 'w', encoding='utf-8').write(html)
print('wrote', sys.argv[1], 'with', len(pats) - 1, 'patches')
