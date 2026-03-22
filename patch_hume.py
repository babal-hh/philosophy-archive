#!/usr/bin/env python3
"""
Run from ~/Desktop/philosophy-archive/: python3 patch_hume.py
Adds Hume (Edinburgh Grey / Scottish Enlightenment theme)
"""
import os, sys, re

base       = os.path.dirname(os.path.abspath(__file__))
index_path = os.path.join(base, 'index.html')
css_path   = os.path.join(base, 'css', 'style.css')
changes    = []

with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

# ── 1. Script tags ────────────────────────────────────────────────
TAGS = ''.join([f'    <script src="js/data-22{x}.js"></script>\n' for x in 'abcde'])
if 'data-22a.js' not in html:
    m = re.search(r'(\s*<script\s+src="js/script\.js")', html)
    if m:
        html = html[:m.start()] + '\n' + TAGS + html[m.start():]
        changes.append('data-22a–22e script tags added')
    else:
        changes.append('WARNING: script.js tag not found')
else:
    changes.append('Script tags already present — skipped')

# ── 2. Filter tab ─────────────────────────────────────────────────
HUME_TAB = '''
                <button class="filter-tab" data-filter="hume" role="tab" aria-selected="false">
                    <span class="filter-dot hume-dot"></span>
                    Hume <span class="filter-count" id="countHume">0</span>
                </button>'''

if 'data-filter="hume"' not in html:
    # Insert after Berkeley tab
    m = re.search(r'(<button[^>]*data-filter="berkeley"[^>]*>.*?</button>)', html, re.DOTALL)
    if m:
        html = html[:m.end()] + HUME_TAB + html[m.end():]
        changes.append('Hume filter tab added')
    else:
        changes.append('WARNING: Berkeley tab not found for insertion')
else:
    changes.append('Filter tab already present — skipped')

# ── 3. Section HTML ───────────────────────────────────────────────
HUME_SECTION = '''

    <!-- HUME (1711–1776) -->
    <section class="works-section" id="hume-section" aria-label="Hume">
        <div class="container">
            <div class="section-header fade-in-element">
                <p class="section-tag hume-tag">Scottish Enlightenment &middot; Edinburgh &middot; 1711&ndash;1776</p>
                <h2 class="section-title">Hume\'s Works</h2>
                <div class="section-rule hume-rule"></div>
                <p class="section-description">The most thorough sceptic in the Western tradition &mdash; who demolished the rational foundations of causation, personal identity, and natural religion, and built in their place a philosophy of human nature grounded in custom, sentiment, and the limits of reason. He died calmly and without religious consolation, the closest thing the Enlightenment produced to a Socratic death.</p>
            </div>
            <div class="works-grid" id="humeGrid"></div>
        </div>
    </section>'''

if 'id="hume-section"' not in html:
    # Insert after Locke section, before Kant section
    for anchor_id in ['kant-section', 'berkeley-section', 'locke-section', 'timeline-section']:
        pattern = re.compile(r'(<section[^>]*id="' + anchor_id + r'"[^>]*>.*?</section>)', re.DOTALL)
        m = pattern.search(html)
        if m:
            html = html[:m.start()] + HUME_SECTION + '\n\n    ' + html[m.start():]
            changes.append(f'Hume section inserted before {anchor_id}')
            break
    else:
        changes.append('WARNING: could not find anchor section for Hume')
else:
    changes.append('Hume section already present — skipped')

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)

# ── 4. CSS — Edinburgh Grey / Scottish Enlightenment ─────────────
HUME_CSS = """

/* ============================================================
   HUME — Edinburgh Grey / Scottish Enlightenment (1711–1776)
   ============================================================ */

.hume-tag {
    color: #3E5368;
    border-color: rgba(62, 83, 104, 0.25);
}
.hume-rule {
    background: linear-gradient(90deg, #3E5368, #7A9BAF, transparent);
}
.hume-dot { background: #3E5368; }

.works-section#hume-section .card-philosopher-badge {
    background: rgba(62, 83, 104, 0.10);
    color: #3E5368;
    border-color: rgba(62, 83, 104, 0.25);
}
.works-section#hume-section .card[data-philosopher="hume"]:hover {
    border-top-color: #3E5368;
    box-shadow: 0 8px 32px rgba(62, 83, 104, 0.12);
}
.filter-tab[data-filter="hume"] .filter-dot { background: #3E5368; }
.filter-tab[data-filter="hume"].active,
.filter-tab[data-filter="hume"]:hover {
    color: #3E5368;
    border-color: rgba(62, 83, 104, 0.35);
}
.modal-header.modal-philosopher-hume { border-top-color: #3E5368; }

@media (prefers-color-scheme: dark) {
    .hume-tag { color: #8CAFC4; border-color: rgba(140, 175, 196, 0.20); }
    .hume-rule { background: linear-gradient(90deg, #8CAFC4, #B5D0E0, transparent); }
    .hume-dot { background: #8CAFC4; }
    .filter-tab[data-filter="hume"] .filter-dot { background: #8CAFC4; }
    .filter-tab[data-filter="hume"].active,
    .filter-tab[data-filter="hume"]:hover { color: #8CAFC4; border-color: rgba(140,175,196,0.35); }
    .modal-header.modal-philosopher-hume { border-top-color: #8CAFC4; }
}
"""

with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()
if '/* HUME' not in css:
    with open(css_path, 'a', encoding='utf-8') as f:
        f.write(HUME_CSS)
    changes.append('Hume CSS (Edinburgh Grey) appended')
else:
    changes.append('Hume CSS already present — skipped')

print('\nResults:')
for c in changes:
    print('  ' + ('⚠' if 'WARNING' in c else '✓'), c)
print('\nDone. Run:')
print('  git add index.html css/style.css js/data-22a.js js/data-22b.js js/data-22c.js js/data-22d.js js/data-22e.js')
print('  git commit -m "Add Hume — 10 works, Edinburgh Grey theme"')
print('  git push')
