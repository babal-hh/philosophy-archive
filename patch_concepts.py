#!/usr/bin/env python3
"""
Run from inside ~/Desktop/philosophy-archive/
  python3 patch_concepts.py
"""
import os

base       = os.path.dirname(os.path.abspath(__file__))
css_path   = os.path.join(base, 'css', 'style.css')
script_dst = os.path.join(base, 'js', 'script.js')
changes    = []

with open(script_dst, 'r', encoding='utf-8') as f:
    script = f.read()

# ── 1. Concepts → definition list ────────────────────────────────────────────
OLD_CONCEPTS = """        if (D.modalConcepts) {
            D.modalConcepts.innerHTML = (work.concepts||[]).map(function(c){
                var text = typeof c==='string' ? c : (c.text||'');
                return '<span class="modal-concept-chip '+phil+'-concept">'+escHtml(text)+'</span>';
            }).join('');
        }"""

NEW_CONCEPTS = """        if (D.modalConcepts) {
            D.modalConcepts.innerHTML = (work.concepts||[]).map(function(c){
                var text = typeof c==='string' ? c : (c.text||'');
                /* Split "Term \u2014 explanation" into headword + body */
                var dash = text.search(/\s[\u2014\u2013]\s/);
                if (dash !== -1) {
                    var term = text.substring(0, dash).trim();
                    var desc = text.substring(dash).replace(/^\s*[\u2014\u2013]\s*/, '').trim();
                    return '<div class="concept-item">'+
                        '<span class="concept-term">'+escHtml(term)+'</span>'+
                        '<span class="concept-desc">'+escHtml(desc)+'</span>'+
                    '</div>';
                }
                return '<div class="concept-item concept-plain">'+
                    '<span class="concept-desc">'+escHtml(text)+'</span>'+
                '</div>';
            }).join('');
        }"""

if OLD_CONCEPTS in script:
    script = script.replace(OLD_CONCEPTS, NEW_CONCEPTS)
    changes.append('Concepts redesigned as definition list')
else:
    changes.append('WARNING: concepts pattern not found — skipped')

# ── 2. Modal meta: reading time + word count ─────────────────────────────────
OLD_BADGE = """            if (work.estimatedWordCount) {
                var wc = work.estimatedWordCount>=1000 ? Math.round(work.estimatedWordCount/1000)+'k words' : work.estimatedWordCount+' words';
                badges += '<span class="meta-badge">~'+wc+'</span>';
            }"""

NEW_BADGE = """            if (work.estimatedWordCount) {
                var _m = Math.ceil(work.estimatedWordCount/200);
                var _rt = _m<60 ? _m+' min' : Math.floor(_m/60)+'h'+(_m%60?' '+_m%60+'m':'');
                var wc = work.estimatedWordCount>=1000 ? Math.round(work.estimatedWordCount/1000)+'k words' : work.estimatedWordCount+' words';
                badges += '<span class="meta-badge meta-badge-time">'+_rt+' read</span>';
                badges += '<span class="meta-badge meta-badge-words">~'+wc+'</span>';
            }"""

if OLD_BADGE in script:
    script = script.replace(OLD_BADGE, NEW_BADGE)
    changes.append('Modal meta: reading time added')
else:
    changes.append('WARNING: meta badge pattern not found — skipped')

with open(script_dst, 'w', encoding='utf-8') as f:
    f.write(script)

# ── 3. CSS ────────────────────────────────────────────────────────────────────
CONCEPTS_CSS = """

/* ================================================================
   CONCEPTS PATCH \u2014 definition list style
   ================================================================ */

.modal-concepts {
    display: flex !important;
    flex-direction: column !important;
    flex-wrap: nowrap !important;
    gap: 0 !important;
}

.concept-item {
    display: flex;
    flex-direction: column;
    gap: 3px;
    padding: 11px 0;
    border-bottom: 1px solid var(--border);
}
.concept-item:first-child { border-top: 1px solid var(--border); }

.concept-term {
    font-family: var(--font-heading);
    font-size: 0.95rem;
    font-weight: 700;
    font-style: italic;
    color: var(--text);
    line-height: 1.3;
}

.concept-desc {
    font-family: var(--font-body);
    font-size: 0.855rem;
    color: var(--text-secondary);
    line-height: 1.75;
}

.concept-plain .concept-desc { font-style: italic; }

/* Hide old monospace chips completely */
.modal-concept-chip { display: none !important; }

/* Reading time badge */
.meta-badge-time {
    background: var(--gold-bg);
    border-color: rgba(166,138,76,0.25);
    color: var(--gold);
    font-weight: 500;
}
.meta-badge-words { color: var(--text-muted); opacity: 0.65; }
"""

with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

if '/* CONCEPTS PATCH' not in css:
    with open(css_path, 'a', encoding='utf-8') as f:
        f.write(CONCEPTS_CSS)
    changes.append('Concept definition list CSS appended to style.css')
else:
    changes.append('CSS already present \u2014 skipped')

print('\nResults:')
for c in changes:
    print('  ' + ('\u26a0' if 'WARNING' in c else '\u2713'), c)
print('\nDone. Run:')
print('  git add css/style.css js/script.js')
print('  git commit -m "Concepts: definition list; modal: reading time"')
print('  git push')
