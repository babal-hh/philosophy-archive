#!/usr/bin/env python3
"""
Run from ~/Desktop/philosophy-archive/: python3 patch_hegel.py
Adds Hegel — Speculative Midnight Blue theme
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
HEGEL_TAB = '''
                <button class="filter-tab" data-filter="hegel" role="tab" aria-selected="false">
                    <span class="filter-dot hegel-dot"></span>
                    Hegel <span class="filter-count" id="countHegel">0</span>
                </button>'''

if 'data-filter="hegel"' not in html:
    # Insert after Schelling tab, or Fichte, or Kant
    inserted = False
    for anchor in ['schelling', 'fichte', 'kant']:
        m = re.search(r'(<button[^>]*data-filter="' + anchor + r'"[^>]*>.*?</button>)', html, re.DOTALL)
        if m:
            html = html[:m.end()] + HEGEL_TAB + html[m.end():]
            changes.append(f'Hegel filter tab added after {anchor}')
            inserted = True
            break
    if not inserted:
        changes.append('WARNING: no anchor tab found for Hegel insertion')
else:
    changes.append('Filter tab already present — skipped')

# ── 3. Section HTML ───────────────────────────────────────────────
HEGEL_SECTION = '''

    <!-- HEGEL (1770–1831) -->
    <section class="works-section" id="hegel-section" aria-label="Hegel">
        <div class="container">
            <div class="section-header fade-in-element">
                <p class="section-tag hegel-tag">German Idealism &middot; Berlin &middot; 1770&ndash;1831</p>
                <h2 class="section-title">Hegel\'s Works</h2>
                <div class="section-rule hegel-rule"></div>
                <p class="section-description">The most systematic philosopher in the Western tradition since Aristotle \u2014 who argued that reality is Spirit\u2019s progressive self-realisation, that truth is the whole, and that the Owl of Minerva spreads its wings only with the falling of the dusk. In the Phenomenology, the Science of Logic, and the Philosophy of Right, Hegel produced the most ambitious synthesis of epistemology, metaphysics, and political philosophy ever attempted.</p>
            </div>
            <div class="works-grid" id="hegelGrid"></div>
        </div>
    </section>'''

if 'id="hegel-section"' not in html:
    # Insert before schopenhauer-section, nietzsche-section, or timeline-section
    for anchor_id in ['schopenhauer-section', 'nietzsche-section', 'timeline-section']:
        pattern = re.compile(r'(<section[^>]*id="' + anchor_id + r'"[^>]*>)', re.DOTALL)
        m = pattern.search(html)
        if m:
            html = html[:m.start()] + HEGEL_SECTION + '\n\n    ' + html[m.start():]
            changes.append(f'Hegel section inserted before {anchor_id}')
            break
    else:
        changes.append('WARNING: no anchor section found for Hegel')
else:
    changes.append('Hegel section already present — skipped')

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)

# ── 4. CSS — Speculative Midnight / Berlin Ink ────────────────────
HEGEL_CSS = """

/* ============================================================
   HEGEL — Speculative Midnight Blue / Berlin Ink (1770–1831)
   ============================================================ */

.hegel-tag {
    color: #1E3A5F;
    border-color: rgba(30, 58, 95, 0.25);
}
.hegel-rule {
    background: linear-gradient(90deg, #1E3A5F, #4A78A8, transparent);
}
.hegel-dot { background: #1E3A5F; }

.works-section#hegel-section .card-philosopher-badge {
    background: rgba(30, 58, 95, 0.10);
    color: #1E3A5F;
    border-color: rgba(30, 58, 95, 0.25);
}
.works-section#hegel-section .card[data-philosopher="hegel"]:hover {
    border-top-color: #1E3A5F;
    box-shadow: 0 8px 32px rgba(30, 58, 95, 0.12);
}
.filter-tab[data-filter="hegel"] .filter-dot { background: #1E3A5F; }
.filter-tab[data-filter="hegel"].active,
.filter-tab[data-filter="hegel"]:hover {
    color: #1E3A5F;
    border-color: rgba(30, 58, 95, 0.35);
}
.modal-header.modal-philosopher-hegel { border-top-color: #1E3A5F; }

@media (prefers-color-scheme: dark) {
    .hegel-tag { color: #6FA3D0; border-color: rgba(111,163,208,0.20); }
    .hegel-rule { background: linear-gradient(90deg, #6FA3D0, #A8CCEA, transparent); }
    .hegel-dot { background: #6FA3D0; }
    .filter-tab[data-filter="hegel"] .filter-dot { background: #6FA3D0; }
    .filter-tab[data-filter="hegel"].active,
    .filter-tab[data-filter="hegel"]:hover { color: #6FA3D0; border-color: rgba(111,163,208,0.35); }
    .modal-header.modal-philosopher-hegel { border-top-color: #6FA3D0; }
}
"""

with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()
if '/* HEGEL' not in css:
    with open(css_path, 'a', encoding='utf-8') as f:
        f.write(HEGEL_CSS)
    changes.append('Hegel CSS (Speculative Midnight Blue) appended')
else:
    changes.append('Hegel CSS already present — skipped')

print('\nResults:')
for c in changes:
    print('  ' + ('⚠' if 'WARNING' in c else '✓'), c)
print('\nDone. Run:')
print('  git add index.html css/style.css js/data-20a.js js/data-20b.js js/data-20c.js js/data-20d.js js/data-20e.js')
print('  git commit -m "Add Hegel — 9 works, Speculative Midnight Blue theme"')
print('  git push')
