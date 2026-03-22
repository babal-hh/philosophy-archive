#!/usr/bin/env python3
"""
Run from ~/Desktop/philosophy-archive/: python3 patch_kierkegaard.py
Adds Kierkegaard — Existential Burgundy / Copenhagen Dusk theme
"""
import os, re

base       = os.path.dirname(os.path.abspath(__file__))
index_path = os.path.join(base, 'index.html')
css_path   = os.path.join(base, 'css', 'style.css')
changes    = []

with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

# ── 1. Script tags ────────────────────────────────────────────────
TAGS = ''.join([f'    <script src="js/data-20{x}.js"></script>\n' for x in 'abcde'])
if 'data-20a.js' not in html:
    m = re.search(r'(\s*<script\s+src="js/script\.js")', html)
    if m:
        html = html[:m.start()] + '\n' + TAGS + html[m.start():]
        changes.append('data-20a–20e script tags added')
    else:
        changes.append('WARNING: script.js tag not found')
else:
    changes.append('Script tags already present — skipped')

# ── 2. Filter tab ─────────────────────────────────────────────────
K_TAB = '''
                <button class="filter-tab" data-filter="kierkegaard" role="tab" aria-selected="false">
                    <span class="filter-dot kierkegaard-dot"></span>
                    Kierkegaard <span class="filter-count" id="countKierkegaard">0</span>
                </button>'''

if 'data-filter="kierkegaard"' not in html:
    inserted = False
    for anchor in ['nietzsche', 'schopenhauer', 'hegel', 'kant']:
        m = re.search(r'(<button[^>]*data-filter="' + anchor + r'"[^>]*>.*?</button>)',
                      html, re.DOTALL)
        if m:
            html = html[:m.end()] + K_TAB + html[m.end():]
            changes.append(f'Kierkegaard filter tab added after {anchor}')
            inserted = True
            break
    if not inserted:
        changes.append('WARNING: no anchor tab found')
else:
    changes.append('Filter tab already present — skipped')

# ── 3. Section HTML ───────────────────────────────────────────────
K_SECTION = '''

    <!-- KIERKEGAARD (1813–1855) -->
    <section class="works-section" id="kierkegaard-section" aria-label="Kierkegaard">
        <div class="container">
            <div class="section-header fade-in-element">
                <p class="section-tag kierkegaard-tag">Existentialism &middot; Copenhagen &middot; 1813&ndash;1855</p>
                <h2 class="section-title">Kierkegaard\'s Works</h2>
                <div class="section-rule kierkegaard-rule"></div>
                <p class="section-description">The father of existentialism \u2014 who dismantled Hegel\u2019s system from within, insisted that existence cannot be reduced to thought, and spent his entire literary career asking one question: what does it mean to be a single individual before God? He died at forty-two, exhausted by his attack on the Danish State Church, refusing communion from an official pastor, convinced he had been used by Providence as a corrective.</p>
            </div>
            <div class="works-grid" id="kierkegaardGrid"></div>
        </div>
    </section>'''

if 'id="kierkegaard-section"' not in html:
    for anchor_id in ['timeline-section', 'about-section']:
        pattern = re.compile(r'(<section[^>]*id="' + anchor_id + r'"[^>]*>)',
                             re.DOTALL)
        m = pattern.search(html)
        if m:
            html = html[:m.start()] + K_SECTION + '\n\n    ' + html[m.start():]
            changes.append(f'Kierkegaard section inserted before {anchor_id}')
            break
    else:
        changes.append('WARNING: no anchor section found')
else:
    changes.append('Kierkegaard section already present — skipped')

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)

# ── 4. CSS ────────────────────────────────────────────────────────
K_CSS = """

/* ============================================================
   KIERKEGAARD — Existential Burgundy / Copenhagen Dusk (1813–1855)
   ============================================================ */

.kierkegaard-tag {
    color: #6B2737;
    border-color: rgba(107, 39, 55, 0.25);
}
.kierkegaard-rule {
    background: linear-gradient(90deg, #6B2737, #A05060, transparent);
}
.kierkegaard-dot { background: #6B2737; }

.works-section#kierkegaard-section .card-philosopher-badge {
    background: rgba(107, 39, 55, 0.10);
    color: #6B2737;
    border-color: rgba(107, 39, 55, 0.25);
}
.works-section#kierkegaard-section .card[data-philosopher="kierkegaard"]:hover {
    border-top-color: #6B2737;
    box-shadow: 0 8px 32px rgba(107, 39, 55, 0.12);
}
.filter-tab[data-filter="kierkegaard"] .filter-dot { background: #6B2737; }
.filter-tab[data-filter="kierkegaard"].active,
.filter-tab[data-filter="kierkegaard"]:hover {
    color: #6B2737;
    border-color: rgba(107, 39, 55, 0.35);
}
.modal-header.modal-philosopher-kierkegaard { border-top-color: #6B2737; }

@media (prefers-color-scheme: dark) {
    .kierkegaard-tag { color: #D4808E; border-color: rgba(212,128,142,0.20); }
    .kierkegaard-rule { background: linear-gradient(90deg, #D4808E, #E8B0B8, transparent); }
    .kierkegaard-dot { background: #D4808E; }
    .filter-tab[data-filter="kierkegaard"] .filter-dot { background: #D4808E; }
    .filter-tab[data-filter="kierkegaard"].active,
    .filter-tab[data-filter="kierkegaard"]:hover {
        color: #D4808E;
        border-color: rgba(212,128,142,0.35);
    }
    .modal-header.modal-philosopher-kierkegaard { border-top-color: #D4808E; }
}
"""

with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()
if '/* KIERKEGAARD' not in css:
    with open(css_path, 'a', encoding='utf-8') as f:
        f.write(K_CSS)
    changes.append('Kierkegaard CSS (Existential Burgundy) appended')
else:
    changes.append('CSS already present — skipped')

print('\nResults:')
for c in changes:
    print('  ' + ('⚠' if 'WARNING' in c else '✓'), c)
print('\nDone. Run:')
print('  git add index.html css/style.css js/data-20a.js js/data-20b.js js/data-20c.js js/data-20d.js js/data-20e.js')
print('  git commit -m "Add Kierkegaard — 10 works, Existential Burgundy theme"')
print('  git push')
