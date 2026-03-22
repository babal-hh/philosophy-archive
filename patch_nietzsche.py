#!/usr/bin/env python3
"""
Run from inside ~/Desktop/philosophy-archive/
  python3 patch_nietzsche.py

Adds Nietzsche to the site:
  1. Five data-19*.js script tags before script.js in index.html
  2. Nietzsche section HTML after Schopenhauer section
  3. Nietzsche CSS (Dionysian Crimson) appended to css/style.css
Idempotent — safe to re-run.
"""
import os, sys, re, shutil

base       = os.path.dirname(os.path.abspath(__file__))
index_path = os.path.join(base, 'index.html')
css_path   = os.path.join(base, 'css', 'style.css')

# Also copy new data-19a.js if the generator was run in the project root
src_19a = os.path.join(base, 'data-19a.js')        # if generated in root
dst_19a = os.path.join(base, 'js', 'data-19a.js')
if os.path.exists(src_19a) and not os.path.exists(dst_19a):
    shutil.copy2(src_19a, dst_19a)

with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

changes = []
errors  = []

# ── 1. Script tags ─────────────────────────────────────────────────────────
SCRIPT_TAGS = '''    <script src="js/data-19a.js"></script>
    <script src="js/data-19b.js"></script>
    <script src="js/data-19c.js"></script>
    <script src="js/data-19d.js"></script>
    <script src="js/data-19e.js"></script>
'''
SCRIPT_JS_RE = re.compile(r'(\s*<script\s+src="js/script\.js")')

if 'data-19a.js' not in html:
    if SCRIPT_JS_RE.search(html):
        html = SCRIPT_JS_RE.sub('\n' + SCRIPT_TAGS + r'\1', html)
        changes.append('data-19a through data-19e script tags added')
    else:
        errors.append('Could not find js/script.js tag')
else:
    changes.append('Script tags already present — skipped')

# ── 2. Nietzsche section ────────────────────────────────────────────────────
NIETZSCHE_SECTION = '''

    <!-- ================================================================
         NIETZSCHE (1844–1900)
         ================================================================ -->
    <section class="works-section" id="nietzsche-section" aria-label="Nietzsche">
        <div class="container">
            <div class="section-header fade-in-element">
                <p class="section-tag nietzsche-tag">Nihilism &amp; Revaluation &middot; Germany &middot; 1844&ndash;1900</p>
                <h2 class="section-title">Nietzsche\'s Works</h2>
                <div class="section-rule nietzsche-rule"></div>
                <p class="section-description">The philosopher with a hammer &mdash; who declared the death of God, diagnosed the nihilism of modern civilisation, and demanded a revaluation of all values. Nietzsche wrote ten major works in twelve years before a mental collapse at forty-four ended his productive life, but his influence on every subsequent philosophical, literary, and cultural movement has been incalculable. He died in 1900 having never recovered consciousness of what he had accomplished.</p>
            </div>
            <div class="works-grid" id="nietzscheGrid"></div>
        </div>
    </section>'''

if 'id="nietzsche-section"' not in html:
    # Insert after schopenhauer-section
    SCHOP_RE = re.compile(
        r'(<section[^>]*id="schopenhauer-section"[^>]*>.*?</section>)',
        re.DOTALL
    )
    m = SCHOP_RE.search(html)
    if m:
        html = html[:m.end()] + NIETZSCHE_SECTION + html[m.end():]
        changes.append('Nietzsche section inserted after Schopenhauer section')
    else:
        # Fall back: insert before timeline-section
        TL_RE = re.compile(r'(\s*<!--\s*TIMELINE|<section[^>]*id="timeline-section")', re.DOTALL)
        m2 = TL_RE.search(html)
        if m2:
            html = html[:m2.start()] + '\n' + NIETZSCHE_SECTION + html[m2.start():]
            changes.append('Nietzsche section inserted before timeline section')
        else:
            errors.append('Could not find schopenhauer-section or timeline-section')
else:
    changes.append('Nietzsche section already present — skipped')

# ── 3. Filter tab ────────────────────────────────────────────────────────────
SCHOP_TAB_RE = re.compile(
    r'(<button[^>]*data-filter="schopenhauer"[^>]*>.*?</button>)',
    re.DOTALL
)
NIETZSCHE_TAB = '''
                <button class="filter-tab" data-filter="nietzsche" role="tab" aria-selected="false">
                    <span class="filter-dot nietzsche-dot"></span>
                    Nietzsche <span class="filter-count" id="countNietzsche">0</span>
                </button>'''

if 'data-filter="nietzsche"' not in html:
    m = SCHOP_TAB_RE.search(html)
    if m:
        html = html[:m.end()] + NIETZSCHE_TAB + html[m.end():]
        changes.append('Nietzsche filter tab added after Schopenhauer')
    else:
        changes.append('No Schopenhauer filter tab found — skipped tab insertion')
else:
    changes.append('Filter tab already present — skipped')

if errors:
    print('\nERRORS — index.html NOT written:')
    for e in errors: print('  ✗', e)
    sys.exit(1)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)
for c in changes:
    print('  ✓', c)

# ── 4. CSS: Dionysian Crimson ────────────────────────────────────────────────
NIETZSCHE_CSS = """

/* ============================================================
   NIETZSCHE — Dionysian Crimson / Dark Wine (1844–1900)
   ============================================================ */

.nietzsche-tag {
    color: #8B1A1A;
    border-color: rgba(139, 26, 26, 0.25);
}

.nietzsche-rule {
    background: linear-gradient(90deg, #8B1A1A, #C0392B, transparent);
}

.nietzsche-dot {
    background: #8B1A1A;
}

.works-section#nietzsche-section .card-philosopher-badge {
    background: rgba(139, 26, 26, 0.10);
    color: #8B1A1A;
    border-color: rgba(139, 26, 26, 0.25);
}

.works-section#nietzsche-section .card[data-philosopher="nietzsche"]:hover {
    border-top-color: #8B1A1A;
    box-shadow: 0 8px 32px rgba(139, 26, 26, 0.12);
}

.filter-tab[data-filter="nietzsche"] .filter-dot {
    background: #8B1A1A;
}

.filter-tab[data-filter="nietzsche"].active,
.filter-tab[data-filter="nietzsche"]:hover {
    color: #8B1A1A;
    border-color: rgba(139, 26, 26, 0.35);
}

.modal-philosopher-nietzsche {
    border-top: 3px solid #8B1A1A;
}

.modal-philosopher-nietzsche .modal-philosopher-name {
    color: #8B1A1A;
}

/* Dark mode */
@media (prefers-color-scheme: dark) {
    .nietzsche-tag {
        color: #E57373;
        border-color: rgba(229, 115, 115, 0.20);
    }

    .nietzsche-rule {
        background: linear-gradient(90deg, #E57373, #EF9A9A, transparent);
    }

    .nietzsche-dot {
        background: #E57373;
    }

    .works-section#nietzsche-section .card-philosopher-badge {
        background: rgba(229, 115, 115, 0.10);
        color: #E57373;
        border-color: rgba(229, 115, 115, 0.20);
    }

    .works-section#nietzsche-section .card[data-philosopher="nietzsche"]:hover {
        border-top-color: #E57373;
        box-shadow: 0 8px 32px rgba(229, 115, 115, 0.10);
    }

    .filter-tab[data-filter="nietzsche"] .filter-dot {
        background: #E57373;
    }

    .filter-tab[data-filter="nietzsche"].active,
    .filter-tab[data-filter="nietzsche"]:hover {
        color: #E57373;
        border-color: rgba(229, 115, 115, 0.35);
    }

    .modal-philosopher-nietzsche {
        border-top: 3px solid #E57373;
    }

    .modal-philosopher-nietzsche .modal-philosopher-name {
        color: #E57373;
    }
}
"""

with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

if '/* NIETZSCHE' not in css:
    with open(css_path, 'a', encoding='utf-8') as f:
        f.write(NIETZSCHE_CSS)
    print('  ✓ Nietzsche CSS (Dionysian Crimson) appended to style.css')
else:
    print('  ✓ Nietzsche CSS already present — skipped')

print('\nDone. Now run:')
print('  git add index.html css/style.css js/data-19a.js js/data-19b.js js/data-19c.js js/data-19d.js js/data-19e.js')
print('  git commit -m "Add Nietzsche — 5 parts, 10 works, Dionysian Crimson theme"')
print('  git push')
