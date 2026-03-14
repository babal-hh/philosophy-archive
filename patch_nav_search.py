#!/usr/bin/env python3
"""
Run from inside ~/Desktop/philosophy-archive/
  python3 patch_nav_search.py

Does three things:
  1. Removes the <nav class="nav-links"> block from the navbar
  2. Replaces js/script.js with the new dynamic version
  3. Appends polished search + nav CSS to css/style.css
Idempotent — safe to re-run.
"""
import os, sys, re, shutil

base       = os.path.dirname(os.path.abspath(__file__))
index_path = os.path.join(base, 'index.html')
css_path   = os.path.join(base, 'css', 'style.css')
script_src = os.path.join(base, 'new_script.js')   # placed by generate step
script_dst = os.path.join(base, 'js', 'script.js')

changes = []
errors  = []

# ── 1. Remove nav-links from index.html ──────────────────────────────────────
with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

NAV_RE = re.compile(
    r'\s*<nav\s[^>]*class="nav-links"[^>]*>.*?</nav>',
    re.DOTALL
)

if 'nav-links' in html:
    if not html.count('nav-links-removed-marker'):
        html = NAV_RE.sub('', html)
        # Insert marker comment so we know it's been patched
        html = html.replace('<div class="nav-actions">', '<!-- nav-links-removed-marker -->\n            <div class="nav-actions">', 1)
        changes.append('nav-links block removed from navbar')
    else:
        changes.append('nav-links already removed — skipped')
else:
    changes.append('nav-links already absent — skipped')

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)

# ── 2. Copy new script.js ─────────────────────────────────────────────────────
if os.path.exists(script_src):
    shutil.copy2(script_src, script_dst)
    changes.append('js/script.js replaced with new dynamic version')
else:
    errors.append('new_script.js not found — copy it to project root first')

# ── 3. Append CSS tweaks ───────────────────────────────────────────────────────
SEARCH_CSS = """
/* ============================================================
   SEARCH BAR — polished
   ============================================================ */

.search-section {
    position: sticky;
    top: var(--nav-h, 64px);
    z-index: 90;
    background: var(--bg);
    border-bottom: 1px solid var(--border);
    padding: 14px 0;
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
}

.search-box {
    position: relative;
    display: flex;
    align-items: center;
}

.search-input {
    width: 100%;
    padding: 11px 44px 11px 16px;
    background: var(--bg-card, #faf9f6);
    border: 1.5px solid var(--border);
    border-radius: 8px;
    font-family: var(--font-sans);
    font-size: 14px;
    color: var(--text-primary);
    transition: border-color .2s, box-shadow .2s;
    outline: none;
}

.search-input:focus {
    border-color: var(--gold, #9A7840);
    box-shadow: 0 0 0 3px rgba(154,120,64,.10);
}

.search-input::placeholder {
    color: var(--text-tertiary, #aaa);
    font-style: italic;
}

.search-clear {
    position: absolute;
    right: 10px;
    top: 50%;
    transform: translateY(-50%);
    width: 28px;
    height: 28px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: none;
    border: none;
    color: var(--text-secondary);
    cursor: pointer;
    font-size: 18px;
    border-radius: 50%;
    transition: background .15s, color .15s;
    padding: 0;
}

.search-clear:hover {
    background: var(--border);
    color: var(--text-primary);
}

/* ── Filter tabs ── */
.filter-tabs {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    margin-top: 10px;
}

.filter-tab {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 5px 12px;
    border: 1.5px solid var(--border);
    border-radius: 20px;
    background: none;
    font-family: var(--font-sans);
    font-size: 12px;
    letter-spacing: .04em;
    color: var(--text-secondary);
    cursor: pointer;
    transition: border-color .15s, color .15s, background .15s;
    white-space: nowrap;
}

.filter-tab:hover {
    border-color: var(--gold, #9A7840);
    color: var(--text-primary);
}

.filter-tab.active {
    background: var(--text-primary);
    border-color: var(--text-primary);
    color: var(--bg);
}

.filter-tab.active .filter-count {
    opacity: .7;
}

.filter-count {
    font-variant-numeric: tabular-nums;
    font-size: 11px;
    opacity: .55;
}

/* ── Results info ── */
.search-results-info {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-top: 8px;
    font-size: 12px;
    color: var(--text-secondary);
    letter-spacing: .03em;
}

.clear-filters-btn {
    background: none;
    border: 1px solid var(--border);
    border-radius: 4px;
    padding: 2px 8px;
    font-size: 11px;
    color: var(--text-secondary);
    cursor: pointer;
    transition: border-color .15s, color .15s;
}

.clear-filters-btn:hover {
    border-color: var(--text-primary);
    color: var(--text-primary);
}

/* ── Navbar: hide the nav-links on desktop once removed ── */
.nav-links {
    display: none !important;
}
"""

with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

if '/* SEARCH BAR — polished */' not in css:
    with open(css_path, 'a', encoding='utf-8') as f:
        f.write(SEARCH_CSS)
    changes.append('Polished search + nav CSS appended to style.css')
else:
    changes.append('Search CSS already present — skipped')

# ── Report ─────────────────────────────────────────────────────────────────────
print('\nResults:')
for c in changes: print('  ✓', c)
if errors:
    print('\nWarnings:')
    for e in errors: print('  ⚠', e)

print('\nDone. Now run:')
print('  git add index.html js/script.js css/style.css')
print('  git commit -m "Remove top nav links; fix section visibility on filter; polish search"')
print('  git push')
