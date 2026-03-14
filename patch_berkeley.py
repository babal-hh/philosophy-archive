#!/usr/bin/env python3
"""
Run from inside ~/Desktop/philosophy-archive/
  python3 patch_berkeley.py

Adds Berkeley to the site (entirely new philosopher):
  1. Filter tab after Locke in index.html
  2. Berkeley section HTML after Locke section
  3. Five data-15*.js script tags before script.js
  4. Warm Amber / Irish Gold CSS appended to css/style.css
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
LOCKE_TAB_RE = re.compile(
    r'(<button[^>]*data-filter="locke"[^>]*>.*?</button>)',
    re.DOTALL
)
BERKELEY_TAB = '''
                <button class="filter-tab" data-filter="berkeley" role="tab" aria-selected="false">
                    <span class="filter-dot berkeley-dot"></span>
                    Berkeley <span class="filter-count" id="countBerkeley">0</span>
                </button>'''

if 'data-filter="berkeley"' not in html:
    m = LOCKE_TAB_RE.search(html)
    if m:
        html = html[:m.end()] + BERKELEY_TAB + html[m.end():]
        changes.append('Filter tab added after Locke')
    else:
        errors.append('Could not find Locke filter tab')
else:
    changes.append('Filter tab already present — skipped')

# ── 2. Berkeley section ───────────────────────────────────────────────────────
BERKELEY_SECTION = '''

    <!-- ================================================================
         BERKELEY (1685–1753)
         ================================================================ -->
    <section class="works-section" id="berkeley-section" aria-label="Berkeley">
        <div class="container">
            <div class="section-header fade-in-element">
                <p class="section-tag berkeley-tag">Immaterialism &middot; Ireland &middot; 1685&ndash;1753</p>
                <h2 class="section-title">Berkeley\'s Works</h2>
                <div class="section-rule berkeley-rule"></div>
                <p class="section-description">The Irish bishop who denied the existence of matter &mdash; and meant it. Berkeley\'s central claim that to be is to be perceived, that the physical world consists entirely of ideas in minds and has no existence independent of perception, was the most audacious thesis in the history of philosophy. He defended it with arguments of such clarity, force, and charm that Samuel Johnson\'s famous stone-kick refutation missed the point entirely; Berkeley had anticipated and answered every such objection before Johnson was born.</p>
            </div>
            <div class="works-grid" id="berkeleyGrid"></div>
        </div>
    </section>'''

if 'id="berkeley-section"' not in html:
    LOCKE_SECTION_RE = re.compile(
        r'(<section[^>]*id="locke-section"[^>]*>.*?</section>)',
        re.DOTALL
    )
    m = LOCKE_SECTION_RE.search(html)
    if m:
        html = html[:m.end()] + BERKELEY_SECTION + html[m.end():]
        changes.append('Berkeley section inserted after Locke section')
    else:
        errors.append('Could not find locke-section to insert after')
else:
    changes.append('Berkeley section already present — skipped')

# ── 3. Script tags ────────────────────────────────────────────────────────────
SCRIPT_TAGS = '''    <script src="js/data-15a.js"></script>
    <script src="js/data-15b.js"></script>
    <script src="js/data-15c.js"></script>
    <script src="js/data-15d.js"></script>
    <script src="js/data-15e.js"></script>
'''
SCRIPT_JS_RE = re.compile(r'(\s*<script\s+src="js/script\.js")')

if 'data-15a.js' not in html:
    if SCRIPT_JS_RE.search(html):
        html = SCRIPT_JS_RE.sub('\n' + SCRIPT_TAGS + r'\1', html)
        changes.append('data-15a through data-15e script tags added')
    else:
        errors.append('Could not find js/script.js tag')
else:
    changes.append('Script tags already present — skipped')

# ── Write index.html ──────────────────────────────────────────────────────────
if errors:
    print('\nERRORS — index.html NOT written:')
    for e in errors: print('  ✗', e)
    sys.exit(1)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)
for c in changes:
    print('  ✓', c)

# ── 4. CSS: Warm Amber / Irish Gold ───────────────────────────────────────────
BERKELEY_CSS = """

/* ============================================================
   BERKELEY — Warm Amber / Irish Gold (1685–1753)
   ============================================================ */

.berkeley-tag {
    color: #8B6914;
    border-color: rgba(139, 105, 20, 0.25);
}

.berkeley-rule {
    background: linear-gradient(90deg, #8B6914, #C9A84C, transparent);
}

.berkeley-dot {
    background: #8B6914;
}

.works-section#berkeley-section .card-philosopher-badge {
    background: rgba(139, 105, 20, 0.10);
    color: #8B6914;
    border-color: rgba(139, 105, 20, 0.25);
}

.works-section#berkeley-section .card[data-philosopher="berkeley"]:hover {
    border-top-color: #8B6914;
    box-shadow: 0 8px 32px rgba(139, 105, 20, 0.12);
}

.filter-tab[data-filter="berkeley"] .filter-dot {
    background: #8B6914;
}

.filter-tab[data-filter="berkeley"].active,
.filter-tab[data-filter="berkeley"]:hover {
    color: #8B6914;
    border-color: rgba(139, 105, 20, 0.35);
}

.modal-philosopher-berkeley {
    border-top: 3px solid #8B6914;
}

.modal-philosopher-berkeley .modal-philosopher-name {
    color: #8B6914;
}

/* Dark mode */
@media (prefers-color-scheme: dark) {
    .berkeley-tag {
        color: #D4B85C;
        border-color: rgba(212, 184, 92, 0.20);
    }

    .berkeley-rule {
        background: linear-gradient(90deg, #D4B85C, #E8D48B, transparent);
    }

    .berkeley-dot {
        background: #D4B85C;
    }

    .works-section#berkeley-section .card-philosopher-badge {
        background: rgba(212, 184, 92, 0.10);
        color: #D4B85C;
        border-color: rgba(212, 184, 92, 0.20);
    }

    .works-section#berkeley-section .card[data-philosopher="berkeley"]:hover {
        border-top-color: #D4B85C;
        box-shadow: 0 8px 32px rgba(212, 184, 92, 0.10);
    }

    .filter-tab[data-filter="berkeley"] .filter-dot {
        background: #D4B85C;
    }

    .filter-tab[data-filter="berkeley"].active,
    .filter-tab[data-filter="berkeley"]:hover {
        color: #D4B85C;
        border-color: rgba(212, 184, 92, 0.35);
    }

    .modal-philosopher-berkeley {
        border-top: 3px solid #D4B85C;
    }

    .modal-philosopher-berkeley .modal-philosopher-name {
        color: #D4B85C;
    }
}
"""

with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

if '/* BERKELEY' not in css:
    with open(css_path, 'a', encoding='utf-8') as f:
        f.write(BERKELEY_CSS)
    print('  ✓ Berkeley CSS (Warm Amber / Irish Gold) appended to style.css')
else:
    print('  ✓ Berkeley CSS already present — skipped')

print('\nDone. Now run:')
print('  git add index.html css/style.css js/data-15a.js js/data-15b.js js/data-15c.js js/data-15d.js js/data-15e.js')
print('  git commit -m "Add Berkeley — 5 parts, 8 works, Warm Amber theme"')
print('  git push')
