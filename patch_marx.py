#!/usr/bin/env python3
"""
Run from ~/Desktop/philosophy-archive/: python3 patch_marx.py
Adds Marx & Engels — Revolutionary Red / Capital Crimson theme
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
MARX_TAB = '''
                <button class="filter-tab" data-filter="marx" role="tab" aria-selected="false">
                    <span class="filter-dot marx-dot"></span>
                    Marx &amp; Engels <span class="filter-count" id="countMarx">0</span>
                </button>'''

if 'data-filter="marx"' not in html:
    inserted = False
    for anchor in ['kierkegaard', 'nietzsche', 'schopenhauer', 'hegel']:
        m = re.search(r'(<button[^>]*data-filter="' + anchor + r'"[^>]*>.*?</button>)',
                      html, re.DOTALL)
        if m:
            html = html[:m.end()] + MARX_TAB + html[m.end():]
            changes.append(f'Marx & Engels filter tab added after {anchor}')
            inserted = True
            break
    if not inserted:
        changes.append('WARNING: no anchor tab found')
else:
    changes.append('Filter tab already present — skipped')

# ── 3. Section HTML ───────────────────────────────────────────────
MARX_SECTION = '''

    <!-- MARX & ENGELS (1818–1895) -->
    <section class="works-section" id="marx-section" aria-label="Marx and Engels">
        <div class="container">
            <div class="section-header fade-in-element">
                <p class="section-tag marx-tag">Historical Materialism &middot; Germany &amp; England &middot; 1818&ndash;1895</p>
                <h2 class="section-title">Marx &amp; Engels</h2>
                <div class="section-rule marx-rule"></div>
                <p class="section-description">The two thinkers who turned Hegel right-side up, placed philosophy in the service of revolution, and produced the most consequential body of social thought in modern history. Marx spent thirty years in the British Museum working out the hidden logic of capital; Engels managed a Manchester cotton factory to fund the work. Together they wrote the document that changed the world: a spectre is haunting Europe.</p>
            </div>
            <div class="works-grid" id="marxGrid"></div>
        </div>
    </section>'''

if 'id="marx-section"' not in html:
    for anchor_id in ['timeline-section', 'about-section']:
        pattern = re.compile(r'(<section[^>]*id="' + anchor_id + r'"[^>]*>)',
                             re.DOTALL)
        m = pattern.search(html)
        if m:
            html = html[:m.start()] + MARX_SECTION + '\n\n    ' + html[m.start():]
            changes.append(f'Marx section inserted before {anchor_id}')
            break
    else:
        changes.append('WARNING: no anchor section found')
else:
    changes.append('Marx section already present — skipped')

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)

# ── 4. CSS — Revolutionary Red / Capital Crimson ──────────────────
MARX_CSS = """

/* ============================================================
   MARX & ENGELS — Revolutionary Red / Capital Crimson (1818–1895)
   ============================================================ */

.marx-tag {
    color: #8B1A1A;
    border-color: rgba(139, 26, 26, 0.25);
}
.marx-rule {
    background: linear-gradient(90deg, #8B1A1A, #C0392B, transparent);
}
.marx-dot { background: #8B1A1A; }

.works-section#marx-section .card-philosopher-badge {
    background: rgba(139, 26, 26, 0.10);
    color: #8B1A1A;
    border-color: rgba(139, 26, 26, 0.25);
}
.works-section#marx-section .card[data-philosopher="marx"]:hover {
    border-top-color: #8B1A1A;
    box-shadow: 0 8px 32px rgba(139, 26, 26, 0.12);
}
.filter-tab[data-filter="marx"] .filter-dot { background: #8B1A1A; }
.filter-tab[data-filter="marx"].active,
.filter-tab[data-filter="marx"]:hover {
    color: #8B1A1A;
    border-color: rgba(139, 26, 26, 0.35);
}
.modal-header.modal-philosopher-marx { border-top-color: #8B1A1A; }

@media (prefers-color-scheme: dark) {
    .marx-tag { color: #E57373; border-color: rgba(229, 115, 115, 0.20); }
    .marx-rule { background: linear-gradient(90deg, #E57373, #EF9A9A, transparent); }
    .marx-dot { background: #E57373; }
    .filter-tab[data-filter="marx"] .filter-dot { background: #E57373; }
    .filter-tab[data-filter="marx"].active,
    .filter-tab[data-filter="marx"]:hover {
        color: #E57373;
        border-color: rgba(229, 115, 115, 0.35);
    }
    .modal-header.modal-philosopher-marx { border-top-color: #E57373; }
}
"""

with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()
if '/* MARX' not in css:
    with open(css_path, 'a', encoding='utf-8') as f:
        f.write(MARX_CSS)
    changes.append('Marx CSS (Revolutionary Red) appended')
else:
    changes.append('CSS already present — skipped')

print('\nResults:')
for c in changes:
    print('  ' + ('⚠' if 'WARNING' in c else '✓'), c)
print('\nDone. Run:')
print('  git add index.html css/style.css js/data-21a.js js/data-21b.js js/data-21c.js js/data-21d.js js/data-21e.js')
print('  git commit -m "Add Marx & Engels — 11 works, Revolutionary Red theme"')
print('  git push')
