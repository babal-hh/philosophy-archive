#!/usr/bin/env python3
"""
Run from inside ~/Desktop/philosophy-archive/
  python3 patch_kant.py

Adds Kant to the site (entirely new philosopher):
  1. Filter tab after Berkeley in index.html
  2. Kant section HTML after Berkeley section
  3. Five data-16*.js script tags before script.js
  4. Prussian Steel Blue CSS appended to css/style.css
Idempotent — safe to re-run.
"""
import os, sys, re

base       = os.path.dirname(os.path.abspath(__file__))
index_path = os.path.join(base, 'index.html')
css_path   = os.path.join(base, 'css', 'style.css')

with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

errors  = []
changes = []

# ── 1. Filter tab ─────────────────────────────────────────────────────────────
BERKELEY_TAB_RE = re.compile(
    r'(<button[^>]*data-filter="berkeley"[^>]*>.*?</button>)',
    re.DOTALL
)
KANT_TAB = '''
                <button class="filter-tab" data-filter="kant" role="tab" aria-selected="false">
                    <span class="filter-dot kant-dot"></span>
                    Kant <span class="filter-count" id="countKant">0</span>
                </button>'''

if 'data-filter="kant"' not in html:
    m = BERKELEY_TAB_RE.search(html)
    if m:
        html = html[:m.end()] + KANT_TAB + html[m.end():]
        changes.append('Filter tab added after Berkeley')
    else:
        errors.append('Could not find Berkeley filter tab')
else:
    changes.append('Filter tab already present — skipped')

# ── 2. Kant section ───────────────────────────────────────────────────────────
KANT_SECTION = '''

    <!-- ================================================================
         KANT (1724–1804)
         ================================================================ -->
    <section class="works-section" id="kant-section" aria-label="Kant">
        <div class="container">
            <div class="section-header fade-in-element">
                <p class="section-tag kant-tag">Transcendental Idealism &middot; Prussia &middot; 1724&ndash;1804</p>
                <h2 class="section-title">Kant\'s Works</h2>
                <div class="section-rule kant-rule"></div>
                <p class="section-description">The philosopher who drew the map of reason\'s territory &mdash; and marked its borders. Kant never travelled more than fifty miles from K&ouml;nigsberg, yet the revolution he accomplished in philosophy was more far-reaching than any journey could have produced. His three Critiques constitute the most ambitious and systematic philosophical project since Aristotle: a complete inventory of the powers and limits of human reason in its theoretical, moral, and aesthetic employment. His neighbours set their clocks by his daily walk. His last words were reported as &ldquo;Es ist gut&rdquo; &mdash; it is good.</p>
            </div>
            <div class="works-grid" id="kantGrid"></div>
        </div>
    </section>'''

if 'id="kant-section"' not in html:
    BERKELEY_SECTION_RE = re.compile(
        r'(<section[^>]*id="berkeley-section"[^>]*>.*?</section>)',
        re.DOTALL
    )
    m = BERKELEY_SECTION_RE.search(html)
    if m:
        html = html[:m.end()] + KANT_SECTION + html[m.end():]
        changes.append('Kant section inserted after Berkeley section')
    else:
        errors.append('Could not find berkeley-section to insert after')
else:
    changes.append('Kant section already present — skipped')

# ── 3. Script tags ────────────────────────────────────────────────────────────
SCRIPT_TAGS = '''    <script src="js/data-16a.js"></script>
    <script src="js/data-16b.js"></script>
    <script src="js/data-16c.js"></script>
    <script src="js/data-16d.js"></script>
    <script src="js/data-16e.js"></script>
'''
SCRIPT_JS_RE = re.compile(r'(\s*<script\s+src="js/script\.js")')

if 'data-16a.js' not in html:
    if SCRIPT_JS_RE.search(html):
        html = SCRIPT_JS_RE.sub('\n' + SCRIPT_TAGS + r'\1', html)
        changes.append('data-16a through data-16e script tags added')
    else:
        errors.append('Could not find js/script.js tag')
else:
    changes.append('Script tags already present — skipped')

if errors:
    print('\nERRORS — index.html NOT written:')
    for e in errors: print('  ✗', e)
    sys.exit(1)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)
for c in changes:
    print('  ✓', c)

# ── 4. CSS: Prussian Steel Blue / Königsberg Slate ────────────────────────────
KANT_CSS = """

/* ============================================================
   KANT — Prussian Steel Blue / Königsberg Slate (1724–1804)
   ============================================================ */

.kant-tag {
    color: #2B4C6F;
    border-color: rgba(43, 76, 111, 0.25);
}

.kant-rule {
    background: linear-gradient(90deg, #2B4C6F, #6B9FD4, transparent);
}

.kant-dot {
    background: #2B4C6F;
}

.works-section#kant-section .card-philosopher-badge {
    background: rgba(43, 76, 111, 0.10);
    color: #2B4C6F;
    border-color: rgba(43, 76, 111, 0.25);
}

.works-section#kant-section .card[data-philosopher="kant"]:hover {
    border-top-color: #2B4C6F;
    box-shadow: 0 8px 32px rgba(43, 76, 111, 0.12);
}

.filter-tab[data-filter="kant"] .filter-dot {
    background: #2B4C6F;
}

.filter-tab[data-filter="kant"].active,
.filter-tab[data-filter="kant"]:hover {
    color: #2B4C6F;
    border-color: rgba(43, 76, 111, 0.35);
}

.modal-philosopher-kant {
    border-top: 3px solid #2B4C6F;
}

.modal-philosopher-kant .modal-philosopher-name {
    color: #2B4C6F;
}

/* Dark mode */
@media (prefers-color-scheme: dark) {
    .kant-tag {
        color: #6B9FD4;
        border-color: rgba(107, 159, 212, 0.20);
    }

    .kant-rule {
        background: linear-gradient(90deg, #6B9FD4, #B8D4EF, transparent);
    }

    .kant-dot {
        background: #6B9FD4;
    }

    .works-section#kant-section .card-philosopher-badge {
        background: rgba(107, 159, 212, 0.10);
        color: #6B9FD4;
        border-color: rgba(107, 159, 212, 0.20);
    }

    .works-section#kant-section .card[data-philosopher="kant"]:hover {
        border-top-color: #6B9FD4;
        box-shadow: 0 8px 32px rgba(107, 159, 212, 0.10);
    }

    .filter-tab[data-filter="kant"] .filter-dot {
        background: #6B9FD4;
    }

    .filter-tab[data-filter="kant"].active,
    .filter-tab[data-filter="kant"]:hover {
        color: #6B9FD4;
        border-color: rgba(107, 159, 212, 0.35);
    }

    .modal-philosopher-kant {
        border-top: 3px solid #6B9FD4;
    }

    .modal-philosopher-kant .modal-philosopher-name {
        color: #6B9FD4;
    }
}
"""

with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

if '/* KANT' not in css:
    with open(css_path, 'a', encoding='utf-8') as f:
        f.write(KANT_CSS)
    print('  ✓ Kant CSS (Prussian Steel Blue) appended to style.css')
else:
    print('  ✓ Kant CSS already present — skipped')

print('\nDone. Now run:')
print('  git add index.html css/style.css js/data-16a.js js/data-16b.js js/data-16c.js js/data-16d.js js/data-16e.js')
print('  git commit -m "Add Kant — 5 parts, 10 works, Prussian Steel Blue theme"')
print('  git push')
