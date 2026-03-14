#!/usr/bin/env python3
"""
Run from inside ~/Desktop/philosophy-archive/
  python3 patch_locke.py

Does three things:
  1. Adds Locke filter tab to index.html (after Leibniz tab)
  2. Adds Locke section HTML to index.html (before <!-- TIMELINE -->)
  3. Adds 5 Locke script tags to index.html (after data-13c.js)
  4. Appends Locke CSS to css/style.css
"""
import os, sys

base = os.path.dirname(os.path.abspath(__file__))
index_path = os.path.join(base, 'index.html')
css_path   = os.path.join(base, 'css', 'style.css')

# ── read files ──────────────────────────────────────────────────────────────
with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

errors = []

# ── 1. Filter tab ────────────────────────────────────────────────────────────
LEIBNIZ_TAB = '''                    <button class="filter-tab" data-filter="leibniz" role="tab" aria-selected="false">
                        <span class="filter-dot leibniz-dot"></span>
                        Leibniz <span class="filter-count" id="countLeibniz">0</span>
                    </button>'''

LOCKE_TAB = '''                    <button class="filter-tab" data-filter="leibniz" role="tab" aria-selected="false">
                        <span class="filter-dot leibniz-dot"></span>
                        Leibniz <span class="filter-count" id="countLeibniz">0</span>
                    </button>
                    <button class="filter-tab" data-filter="locke" role="tab" aria-selected="false">
                        <span class="filter-dot locke-dot"></span>
                        Locke <span class="filter-count" id="countLocke">0</span>
                    </button>'''

if LEIBNIZ_TAB in html:
    if 'countLocke' not in html:
        html = html.replace(LEIBNIZ_TAB, LOCKE_TAB)
        print('  ✓ Filter tab added')
    else:
        print('  ✓ Filter tab already present — skipped')
else:
    errors.append('Could not find Leibniz filter tab to insert after.')

# ── 2. Section HTML ──────────────────────────────────────────────────────────
TIMELINE_MARKER = '    <!-- TIMELINE -->'

LOCKE_SECTION = '''    <!-- LOCKE -->
    <section class="works-section" id="locke-section" aria-label="Locke">
        <div class="container">
            <div class="section-header fade-in-element">
                <p class="section-tag locke-tag">Empiricism &middot; England &middot; 1632&ndash;1704</p>
                <h2 class="section-title">Locke's Works</h2>
                <div class="section-rule locke-rule"></div>
                <p class="section-description">
                    The founder of British empiricism and liberal political philosophy &mdash;
                    whose Essay remade epistemology, whose Two Treatises founded constitutional democracy,
                    and whose Letter on Toleration established the separation of church and state.
                </p>
            </div>
            <div class="works-grid" id="lockeGrid" aria-label="Locke's works"></div>
        </div>
    </section>

    <!-- TIMELINE -->'''

if TIMELINE_MARKER in html:
    if 'locke-section' not in html:
        html = html.replace(TIMELINE_MARKER, LOCKE_SECTION)
        print('  ✓ Locke section HTML added')
    else:
        print('  ✓ Locke section already present — skipped')
else:
    errors.append('Could not find <!-- TIMELINE --> marker to insert Locke section before.')

# ── 3. Script tags ───────────────────────────────────────────────────────────
DATA_13C = '    <script src="js/data-13c.js"></script>'

LOCKE_SCRIPTS = '''    <script src="js/data-13c.js"></script>
    <script src="js/data-14a.js"></script>
    <script src="js/data-14b.js"></script>
    <script src="js/data-14c.js"></script>
    <script src="js/data-14d.js"></script>
    <script src="js/data-14e.js"></script>'''

if DATA_13C in html:
    if 'data-14a.js' not in html:
        html = html.replace(DATA_13C, LOCKE_SCRIPTS)
        print('  ✓ Script tags added')
    else:
        print('  ✓ Script tags already present — skipped')
else:
    errors.append('Could not find data-13c.js script tag to insert after.')

# ── 4. CSS ───────────────────────────────────────────────────────────────────
LOCKE_CSS = """

/* ================================================================
   LOCKE — colour tokens and component rules
   ================================================================ */

/* ── colour tokens ── */
:root {
    --locke: #8B6520;
    --locke-light: #F5EDD8;
    --locke-mid: #B8892A;
    --locke-pale: #FAF6EC;
    --locke-border: rgba(139,101,32,0.2);
    --locke-bg: rgba(139,101,32,0.04);
}
[data-theme="dark"] {
    --locke: #C9A84C;
    --locke-light: #2A2010;
    --locke-mid: #D4B870;
    --locke-pale: #1E1808;
    --locke-border: rgba(201,168,76,0.22);
    --locke-bg: rgba(201,168,76,0.06);
}

/* ── section tag & rule ── */
.locke-tag  { color: var(--locke-mid) }
.locke-rule { background: var(--locke); opacity: 0.6 }

/* ── filter tab ── */
.locke-dot { background: var(--locke) }
.filter-tab[data-filter="locke"].active       { color: var(--text); border-bottom-color: var(--locke) }
.filter-tab[data-filter="locke"]:hover:not(.active) { color: var(--locke) }

/* ── cards ── */
.locke-card .card-dot       { background: var(--locke) }
.locke-card .card-category  { color: var(--locke-mid) }
.locke-card::before         { background: var(--locke) }
.locke-card:hover           { box-shadow: var(--shadow-md), 0 0 0 1px var(--locke-border) }
.locke-card:hover .card-title { color: var(--locke) }

/* ── modal ── */
.locke-modal-header         { border-top: 2px solid var(--locke) }
.locke-modal-tag            { color: var(--locke) }
.modal-concept-chip.locke-concept {
    border-color: var(--locke-border);
    color: var(--locke);
}

/* ── timeline node ── */
.locke-node .timeline-dot   { background: var(--locke) }
.locke-node:hover .timeline-dot { box-shadow: 0 0 0 4px var(--locke-bg) }
.locke-node .timeline-author { color: var(--locke) }
"""

if '--locke:' not in css:
    css = css + LOCKE_CSS
    print('  ✓ Locke CSS appended')
else:
    print('  ✓ Locke CSS already present — skipped')

# ── write files ──────────────────────────────────────────────────────────────
if errors:
    print('\nERRORS — nothing written:')
    for e in errors:
        print('  ✗', e)
    sys.exit(1)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)
with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print('\nDone. Now run:')
print('  git add index.html css/style.css js/data-14a.js js/data-14b.js js/data-14c.js js/data-14d.js js/data-14e.js')
print('  git commit -m "Add Locke — 5 parts, 9 works"')
print('  git push')
