#!/usr/bin/env python3
"""
Run from inside ~/Desktop/philosophy-archive/
  python3 patch_spinoza.py

Inserts data-12d.js and data-12e.js script tags after data-12c.js in index.html.
The data files themselves (12a-12e) are written by generate_spinoza_full.py.
Idempotent — safe to re-run.
"""
import os, sys

base = os.path.dirname(os.path.abspath(__file__))
index_path = os.path.join(base, 'index.html')

with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

errors = []

# ── Insert 12d and 12e script tags after 12c ─────────────────────────────────
OLD = '    <script src="js/data-12c.js"></script>'
NEW = '''    <script src="js/data-12c.js"></script>
    <script src="js/data-12d.js"></script>
    <script src="js/data-12e.js"></script>'''

if OLD in html:
    if 'data-12d.js' not in html:
        html = html.replace(OLD, NEW)
        print('  ✓ Added data-12d.js and data-12e.js script tags')
    else:
        print('  ✓ Script tags already present — skipped')
else:
    errors.append('Could not find <script src="js/data-12c.js"> in index.html')

if errors:
    print('\nERRORS — nothing written:')
    for e in errors:
        print('  ✗', e)
    sys.exit(1)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)

print('\nDone. Now run:')
print('  git add index.html js/data-12a.js js/data-12b.js js/data-12c.js js/data-12d.js js/data-12e.js')
print('  git commit -m "Update Spinoza — 5 parts, 8 works, full depth"')
print('  git push')
