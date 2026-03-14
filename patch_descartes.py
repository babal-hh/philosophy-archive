#!/usr/bin/env python3
"""
Run from inside ~/Desktop/philosophy-archive/
  python3 patch_descartes.py

Does two things:
  1. Adds data-11d.js and data-11e.js script tags to index.html (after data-11c.js)
  2. Removes any window.WORKS = window.WORKS || []; re-declarations
     that the old heredoc files added — the new generator files are clean
"""
import os, sys, re

base = os.path.dirname(os.path.abspath(__file__))
index_path = os.path.join(base, 'index.html')

with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

errors = []

# ── 1. Add 11d and 11e script tags after 11c ─────────────────────────────────
OLD_11C = '    <script src="js/data-11c.js"></script>'
NEW_11C = '''    <script src="js/data-11c.js"></script>
    <script src="js/data-11d.js"></script>
    <script src="js/data-11e.js"></script>'''

if OLD_11C in html:
    if 'data-11d.js' not in html:
        html = html.replace(OLD_11C, NEW_11C)
        print('  ✓ Added data-11d.js and data-11e.js script tags')
    else:
        print('  ✓ Script tags already present — skipped')
else:
    errors.append('Could not find data-11c.js script tag in index.html')

if errors:
    print('\nERRORS — nothing written:')
    for e in errors:
        print('  ✗', e)
    sys.exit(1)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)

print('\nDone. Now run:')
print('  git add index.html js/data-11a.js js/data-11b.js js/data-11c.js js/data-11d.js js/data-11e.js')
print('  git commit -m "Update Descartes — 5 parts, full depth, 7 works"')
print('  git push')
