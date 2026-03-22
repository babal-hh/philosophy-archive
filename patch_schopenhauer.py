#!/usr/bin/env python3
"""
Run from ~/Desktop/philosophy-archive/: python3 patch_schopenhauer.py
Adds Schopenhauer — Dark Amber / Pessimist Bronze theme
"""
import os, re

base       = os.path.dirname(os.path.abspath(__file__))
index_path = os.path.join(base, 'index.html')
css_path   = os.path.join(base, 'css', 'style.css')
changes    = []

with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

# ── 1. Script tags ────────────────────────────────────────────────
TAGS = ''.join([f'    <script src="js/data-21{x}.js"></script>\n' for x in 'abcde'])
if 'data-21a.js' not in html:
    m = re.search(r'(\s*<script\s+src="js/script\.js")', html)
    if m:
        html = html[:m.start()] + '\n' + TAGS + html[m.start():]
        changes.append('data-21a–21e script tags added')
    else:
        changes.append('WARNING: script.js tag not found')
else:
    changes.append('Script tags already present — skipped')

# ── 2. Filter tab ─────────────────────────────────────────────────
SCHOP_TAB = '''
                <button class="filter-tab" data-filter="schopenhauer" role="tab" aria-selected="false">
                    <span class="filter-dot schopenhauer-dot"></span>
                    Schopenhauer <span class="filter-count" id="countSchopenhauer">0</span>
                </button>'''

if 'data-filter="schopenhauer"' not in html:
    inserted = False
    for anchor in ['hegel', 'kant', 'berkeley']:
        m = re.search(r'(<button[^>]*data-filter="' + anchor + r'"[^>]*>.*?</button>)', html, re.DOTALL)
        if m:
            html = html[:m.end()] + SCHOP_TAB + html[m.end():]
            changes.append(f'Schopenhauer filter tab added after {anchor}')
            inserted = True
            break
    if not inserted:
        changes.append('WARNING: no anchor tab found')
else:
    changes.append('Filter tab already present — skipped')

# ── 3. Section HTML ───────────────────────────────────────────────
SCHOP_SECTION = '''

    <!-- SCHOPENHAUER (1788–1860) -->
    <section class="works-section" id="schopenhauer-section" aria-label="Schopenhauer">
        <div class="container">
            <div class="section-header fade-in-element">
                <p class="section-tag schopenhauer-tag">Philosophical Pessimism &middot; Frankfurt &middot; 1788&ndash;1860</p>
                <h2 class="section-title">Schopenhauer\'s Works</h2>
                <div class="section-rule schopenhauer-rule"></div>
                <p class="section-description">The philosopher who named the unnameable \u2014 who argued that beneath the orderly surface of Kant\u2019s phenomenal world seethes a blind, insatiable Will, that suffering is the essence of existence, and that music is more metaphysically honest than philosophy. Ignored for thirty years, then suddenly famous, he ended his life eating alone with his poodle in Frankfurt, convinced he had been vindicated. He was right.</p>
            </div>
            <div class="works-grid" id="schopenhauerGrid"></div>
        </div>
    </section>'''

if 'id="schopenhauer-section"' not in html:
    for anchor_id in ['nietzsche-section', 'timeline-section']:
        pattern = re.compile(r'(<section[^>]*id="' + anchor_id + r'"[^>]*>)', re.DOTALL)
        m = pattern.search(html)
        if m:
            html = html[:m.start()] + SCHOP_SECTION + '\n\n    ' + html[m.start():]
            changes.append(f'Schopenhauer section inserted before {anchor_id}')
            break
    else:
        changes.append('WARNING: no anchor section found')
else:
    changes.append('Schopenhauer section already present — skipped')

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)

# ── 4. CSS — Dark Amber / Pessimist Bronze ────────────────────────
SCHOP_CSS = """

/* ============================================================
   SCHOPENHAUER — Dark Amber / Pessimist Bronze (1788–1860)
   ============================================================ */

.schopenhauer-tag {
    color: #7B4F2E;
    border-color: rgba(123, 79, 46, 0.25);
}
.schopenhauer-rule {
    background: linear-gradient(90deg, #7B4F2E, #B8845A, transparent);
}
.schopenhauer-dot { background: #7B4F2E; }

.works-section#schopenhauer-section .card-philosopher-badge {
    background: rgba(123, 79, 46, 0.10);
    color: #7B4F2E;
    border-color: rgba(123, 79, 46, 0.25);
}
.works-section#schopenhauer-section .card[data-philosopher="schopenhauer"]:hover {
    border-top-color: #7B4F2E;
    box-shadow: 0 8px 32px rgba(123, 79, 46, 0.12);
}
.filter-tab[data-filter="schopenhauer"] .filter-dot { background: #7B4F2E; }
.filter-tab[data-filter="schopenhauer"].active,
.filter-tab[data-filter="schopenhauer"]:hover {
    color: #7B4F2E;
    border-color: rgba(123, 79, 46, 0.35);
}
.modal-header.modal-philosopher-schopenhauer { border-top-color: #7B4F2E; }

@media (prefers-color-scheme: dark) {
    .schopenhauer-tag { color: #C99A6E; border-color: rgba(201,154,110,0.20); }
    .schopenhauer-rule { background: linear-gradient(90deg, #C99A6E, #E0C4A0, transparent); }
    .schopenhauer-dot { background: #C99A6E; }
    .filter-tab[data-filter="schopenhauer"] .filter-dot { background: #C99A6E; }
    .filter-tab[data-filter="schopenhauer"].active,
    .filter-tab[data-filter="schopenhauer"]:hover { color: #C99A6E; border-color: rgba(201,154,110,0.35); }
    .modal-header.modal-philosopher-schopenhauer { border-top-color: #C99A6E; }
}
"""

with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()
if '/* SCHOPENHAUER' not in css:
    with open(css_path, 'a', encoding='utf-8') as f:
        f.write(SCHOP_CSS)
    changes.append('Schopenhauer CSS (Dark Amber) appended')
else:
    changes.append('CSS already present — skipped')

print('\nResults:')
for c in changes:
    print('  ' + ('⚠' if 'WARNING' in c else '✓'), c)
print('\nDone. Run:')
print('  git add index.html css/style.css js/data-21a.js js/data-21b.js js/data-21c.js js/data-21d.js js/data-21e.js')
print('  git commit -m "Add Schopenhauer — 8 works, Dark Amber theme"')
print('  git push')
