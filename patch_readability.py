#!/usr/bin/env python3
import os, sys, re

base       = os.path.dirname(os.path.abspath(__file__))
index_path = os.path.join(base, 'index.html')
css_path   = os.path.join(base, 'css', 'style.css')
script_dst = os.path.join(base, 'js', 'script.js')
changes    = []

# ═══════════════════════════════════════════════════════════════
# 1. CSS
# ═══════════════════════════════════════════════════════════════
READABILITY_CSS = '''

/* ================================================================
   READABILITY PATCH
   ================================================================ */

.modal { max-width: 800px; position: relative; }

/* Summary: paragraph breathing */
.modal-summary p {
    font-size: 0.935rem;
    color: var(--text-secondary);
    line-height: 1.92;
    margin-bottom: 1.15em;
}
.modal-summary p:last-child { margin-bottom: 0; }
.modal-summary p:first-child { margin-top: 0; }

/* Progress bar */
.modal-progress {
    position: absolute;
    top: 0; left: 0;
    height: 3px; width: 0%;
    transition: width 0.07s linear;
    pointer-events: none;
    border-radius: 0 3px 0 0;
    z-index: 20;
    background: var(--gold);
}

/* Card description: fade not hard-cut */
.card-description {
    display: block !important;
    position: relative;
    -webkit-line-clamp: unset !important;
    max-height: 4.9em;
    overflow: hidden;
    margin-bottom: 14px;
}
.card-description::after {
    content: "";
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 2.2em;
    background: linear-gradient(to bottom, rgba(255,255,255,0) 0%, var(--bg-card) 100%);
    pointer-events: none;
}

/* Reading time badge */
.card-reading-time {
    font-family: var(--font-mono);
    font-size: 0.61rem;
    letter-spacing: 0.05em;
    color: var(--text-muted);
    white-space: nowrap;
    padding: 2px 7px;
    border: 1px solid var(--border);
    border-radius: 9px;
    background: var(--bg-secondary);
    flex-shrink: 0;
}
.card-footer-left {
    display: flex;
    align-items: center;
    gap: 7px;
    flex-shrink: 0;
}
.card-footer { flex-wrap: nowrap; align-items: center; gap: 8px; }
.card-themes { flex: 1; min-width: 0; }

/* Filter tabs — unified row with bottom anchor */
.filter-tabs {
    border-bottom: 1px solid var(--border);
    padding-bottom: 0;
    row-gap: 0;
}

/* Search hint */
#searchShortcut {
    font-size: 10px !important;
    opacity: 0.4;
    right: 46px !important;
    font-family: var(--font-mono) !important;
    letter-spacing: 0.1em !important;
}

/* Modal header: top stripe */
.modal-header { border-left: none !important; border-top: 3px solid var(--border); }
.modal-header.modal-philosopher-plato        { border-top-color: var(--plato); }
.modal-header.modal-philosopher-aristotle    { border-top-color: var(--aristotle); }
.modal-header.modal-philosopher-descartes    { border-top-color: #2B4C8C; }
.modal-header.modal-philosopher-spinoza      { border-top-color: #2D6A4F; }
.modal-header.modal-philosopher-leibniz      { border-top-color: #2E4057; }
.modal-header.modal-philosopher-locke        { border-top-color: #8B6520; }
.modal-header.modal-philosopher-berkeley     { border-top-color: #8B6914; }
.modal-header.modal-philosopher-kant         { border-top-color: #2B4C6F; }
.modal-header.modal-philosopher-nietzsche    { border-top-color: #8B1A1A; }
.modal-header.modal-philosopher-hegel        { border-top-color: #2C5F6E; }
.modal-header.modal-philosopher-schopenhauer { border-top-color: #7B4F2E; }
.modal-header.modal-philosopher-fichte       { border-top-color: #4A5568; }
.modal-header.modal-philosopher-schelling    { border-top-color: #553C7B; }

/* Section label style */
.modal-section-title {
    font-family: var(--font-mono);
    font-size: 0.59rem;
    font-weight: 400;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    font-variant: normal;
    color: var(--text-muted);
    margin-bottom: 10px;
    padding-bottom: 7px;
    border-bottom: 1px solid var(--border);
}

/* Commentary entries */
.commentary-entry {
    padding: 16px 20px;
    border-left: 2px solid var(--border);
    border-radius: 0 var(--radius) var(--radius) 0;
    background: var(--bg-secondary);
    transition: border-color var(--speed), background var(--speed);
}
.commentary-entry:hover { border-left-color: var(--gold); background: var(--bg); }
.commentary-philosopher { font-size: 1rem; font-weight: 700; margin-bottom: 6px; }
.commentary-text { font-size: 0.875rem; line-height: 1.82; }

/* Structure block */
.modal-structure {
    font-family: var(--font-mono);
    font-size: 0.8rem;
    line-height: 1.9;
    white-space: pre-line;
    background: var(--bg-secondary);
    padding: 16px 20px;
    border-radius: var(--radius);
    border: 1px solid var(--border);
}

/* Concept chips */
.modal-concept-chip { border-radius: 4px; font-size: 0.7rem; line-height: 1.5; }

/* Related works */
.related-link { background: var(--bg-secondary); font-size: 0.68rem; }
.related-link:hover { background: var(--gold-bg); border-color: var(--gold); color: var(--gold); }

@media (max-width: 600px) {
    .modal { max-width: 100%; }
    .modal-summary p { font-size: 0.9rem; line-height: 1.82; }
    .card-reading-time { display: none; }
}
'''

with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()
if '/* READABILITY PATCH' not in css:
    with open(css_path, 'a', encoding='utf-8') as f:
        f.write(READABILITY_CSS)
    changes.append('Readability CSS appended to style.css')
else:
    changes.append('CSS already present — skipped')

# ═══════════════════════════════════════════════════════════════
# 2. INDEX.HTML — progress bar div
# ═══════════════════════════════════════════════════════════════
with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

PROG_DIV = '<div class="modal-progress" id="modalProgress"></div>'
if 'modal-progress' not in html:
    m = re.search(r'(<div\s+[^>]*class="modal"[^>]*>)', html)
    if m:
        html = html[:m.end()] + '\n        ' + PROG_DIV + html[m.end():]
        changes.append('Progress bar div inserted in index.html')
    else:
        changes.append('WARNING: .modal div not found')
else:
    changes.append('Progress bar already in index.html — skipped')

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)

# ═══════════════════════════════════════════════════════════════
# 3. SCRIPT.JS
# ═══════════════════════════════════════════════════════════════
with open(script_dst, 'r', encoding='utf-8') as f:
    script = f.read()

# 3a. readingTime helper
RT_FN = """    function readingTime(wc) {
        var m = Math.ceil(wc / 200);
        return m < 60 ? m + ' min' : Math.floor(m/60)+'h'+(m%60?' '+m%60+'m':'');
    }

"""
if 'function readingTime' not in script:
    for anchor in ['    function escHtml(s) {', '    function cardHTML(work, idx) {']:
        if anchor in script:
            script = script.replace(anchor, RT_FN + anchor)
            changes.append('readingTime() added')
            break
    else:
        changes.append('WARNING: anchor for readingTime() not found')
else:
    changes.append('readingTime() already present — skipped')

# 3b. Inject reading time into card footer
if 'card-reading-time' not in script:
    # Pattern A — new script.js (escHtml version)
    OLD_A = """'<div class="card-footer">'+
                '<span class="card-date">'+escHtml(work.readingDifficulty||'')+'</span>'+
                '<div class="card-themes">'+themes+'</div>'+
            '</div>'+"""
    NEW_A = """'<div class="card-footer">'+
                '<div class="card-footer-left">'+
                    '<span class="card-date">'+escHtml(work.readingDifficulty||'')+'</span>'+
                    (work.estimatedWordCount?'<span class="card-reading-time">'+readingTime(work.estimatedWordCount)+'</span>':'')+
                '</div>'+
                '<div class="card-themes">'+themes+'</div>'+
            '</div>'+"""
    # Pattern B — old script.js
    OLD_B_RE = re.compile(
        r"'<div class=\"card-footer\">' \+\s*\n\s*'<span class=\"card-date\">' \+\s*\n\s*\(work\.readingDifficulty \? work\.readingDifficulty : ''\) \+\s*\n\s*'</span>' \+\s*\n\s*'<div class=\"card-themes\">' \+ themes \+ '</div>' \+\s*\n\s*'</div>' \+",
        re.MULTILINE
    )
    NEW_B = """'<div class="card-footer">' +
                '<div class="card-footer-left">' +
                    '<span class="card-date">' + (work.readingDifficulty ? work.readingDifficulty : '') + '</span>' +
                    (work.estimatedWordCount ? '<span class="card-reading-time">' + readingTime(work.estimatedWordCount) + '</span>' : '') +
                '</div>' +
                '<div class="card-themes">' + themes + '</div>' +
            '</div>' +"""

    if OLD_A in script:
        script = script.replace(OLD_A, NEW_A)
        changes.append('Reading time added to card footer (new pattern)')
    elif OLD_B_RE.search(script):
        script = OLD_B_RE.sub(NEW_B, script, count=1)
        changes.append('Reading time added to card footer (old pattern)')
    else:
        changes.append('WARNING: card footer pattern not matched')
else:
    changes.append('Reading time already present — skipped')

# 3c. Summary as paragraphs — old script.js only
if 'D.modalSummary.textContent = work.summary' in script:
    script = script.replace(
        'D.modalSummary.textContent = work.summary;',
        """D.modalSummary.innerHTML = (work.summary||'').split('\\n\\n').map(function(p){
            return '<p>'+p.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').trim()+'</p>';
        }).filter(function(p){return p!=='<p></p>';}).join('');"""
    )
    changes.append('Summary rendered as paragraphs (old script)')
else:
    changes.append('Summary paragraphs already handled — skipped')

# 3d. Progress bar wiring
PROG_JS = """
        var _pg=document.getElementById('modalProgress'),_mb=document.querySelector('.modal-body');
        if(_pg&&_mb){_pg.style.width='0%';_mb.scrollTop=0;
            if(_mb._ph)_mb.removeEventListener('scroll',_mb._ph);
            _mb._ph=function(){var h=_mb.scrollHeight-_mb.clientHeight;
                _pg.style.width=(h<=0?100:Math.min(100,_mb.scrollTop/h*100)).toFixed(1)+'%';};
            _mb.addEventListener('scroll',_mb._ph,{passive:true});}"""

if 'modalProgress' not in script:
    # Look for the closing of openModal — updateModalNav(); followed by }
    m = re.search(r'(updateModalNav\(\);)\s*\n(\s*\})', script)
    if m:
        # Make sure it's inside openModal by checking context
        pos = m.start()
        if 'S.modalOpen = true' in script[max(0,pos-3000):pos]:
            script = script[:m.end(1)] + PROG_JS + '\n' + script[m.start(2):]
            changes.append('Progress bar scroll wired')
        else:
            changes.append('WARNING: updateModalNav found but not inside openModal')
    else:
        changes.append('WARNING: could not wire progress bar')
else:
    changes.append('Progress bar JS already present — skipped')

with open(script_dst, 'w', encoding='utf-8') as f:
    f.write(script)

print('\nResults:')
for c in changes:
    print('  ' + ('⚠' if 'WARNING' in c else '✓'), c)
print('\nDone. Run:')
print('  git add css/style.css js/script.js index.html')
print('  git commit -m "Readability: paragraphs, reading time, progress bar, card fade, filter separator"')
print('  git push')
