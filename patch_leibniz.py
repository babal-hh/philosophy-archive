#!/usr/bin/env python3
"""
Run from inside ~/Desktop/philosophy-archive/
  python3 patch_leibniz.py

1. Adds data-13d.js and data-13e.js script tags after data-13c.js in index.html
2. Appends Leibniz CSS (Prussian Blue / Royal Indigo) to css/style.css
Idempotent — safe to re-run.
"""
import os, sys

base = os.path.dirname(os.path.abspath(__file__))
index_path = os.path.join(base, 'index.html')
css_path   = os.path.join(base, 'css', 'style.css')

errors = []

# ── 1. index.html: add 13d and 13e script tags ───────────────────────────────
with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

OLD = '    <script src="js/data-13c.js"></script>'
NEW = '''    <script src="js/data-13c.js"></script>
    <script src="js/data-13d.js"></script>
    <script src="js/data-13e.js"></script>'''

if OLD in html:
    if 'data-13d.js' not in html:
        html = html.replace(OLD, NEW)
        print('  ✓ Added data-13d.js and data-13e.js script tags')
    else:
        print('  ✓ Script tags already present — skipped')
else:
    errors.append('Could not find <script src="js/data-13c.js"> in index.html')

if errors:
    print('\nERRORS:')
    for e in errors: print('  ✗', e)
    sys.exit(1)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)
print('  ✓ index.html written')

# ── 2. css/style.css: append Leibniz tokens ──────────────────────────────────
LEIBNIZ_CSS = """

/* ============================================================
   LEIBNIZ — Prussian Blue / Royal Indigo
   ============================================================ */

.leibniz-tag {
    color: #2E4057;
    border-color: rgba(46, 64, 87, 0.35);
}

.leibniz-rule {
    background: linear-gradient(90deg, #2E4057, #5B8BA0, transparent);
}

.leibniz-dot {
    background: #2E4057;
}

.works-section#leibniz-section .card-philosopher-badge {
    background: rgba(46, 64, 87, 0.1);
    color: #2E4057;
    border-color: rgba(46, 64, 87, 0.25);
}

.works-section#leibniz-section .card[data-philosopher="leibniz"]:hover {
    border-top-color: #2E4057;
    box-shadow: 0 8px 32px rgba(46, 64, 87, 0.14);
}

.modal-philosopher-leibniz {
    border-top: 3px solid #2E4057;
}

.modal-philosopher-leibniz .modal-philosopher-name {
    color: #2E4057;
}

/* Dark mode */
@media (prefers-color-scheme: dark) {
    .leibniz-tag {
        color: #7BADC4;
        border-color: rgba(123, 173, 196, 0.35);
    }

    .leibniz-rule {
        background: linear-gradient(90deg, #7BADC4, #A8D4E6, transparent);
    }

    .leibniz-dot {
        background: #7BADC4;
    }

    .works-section#leibniz-section .card-philosopher-badge {
        background: rgba(123, 173, 196, 0.12);
        color: #7BADC4;
        border-color: rgba(123, 173, 196, 0.25);
    }

    .works-section#leibniz-section .card[data-philosopher="leibniz"]:hover {
        border-top-color: #7BADC4;
        box-shadow: 0 8px 32px rgba(123, 173, 196, 0.12);
    }

    .modal-philosopher-leibniz {
        border-top: 3px solid #7BADC4;
    }

    .modal-philosopher-leibniz .modal-philosopher-name {
        color: #7BADC4;
    }
}
"""

with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

if '/* LEIBNIZ' not in css:
    with open(css_path, 'a', encoding='utf-8') as f:
        f.write(LEIBNIZ_CSS)
    print('  ✓ Leibniz CSS appended to style.css')
else:
    print('  ✓ Leibniz CSS already present — skipped')

print('\nDone. Now run:')
print('  git add index.html css/style.css js/data-13a.js js/data-13b.js js/data-13c.js js/data-13d.js js/data-13e.js')
print('  git commit -m "Update Leibniz — 5 parts, 8 works, full depth"')
print('  git push')
