/* ================================================================
   THE ACADEMY & THE LYCEUM
   Application Logic — Fully dynamic edition
   Works with any number of philosophers.
   ================================================================ */

;(function () {
    'use strict';

    var $ = function (s) { return document.querySelector(s); };
    var $$ = function (s) { return document.querySelectorAll(s); };

    var D = {
        loader:            $('#loader'),
        body:              document.body,
        html:              document.documentElement,
        navbar:            $('#navbar'),
        hamburger:         $('#hamburger'),
        mobileNavOverlay:  $('#mobileNavOverlay'),
        mobileNavLinks:    $$('.mobile-nav-link'),
        searchToggle:      $('#searchToggle'),
        mobileSearchBar:   $('#mobileSearchBar'),
        mobileSearchInput: $('#mobileSearchInput'),
        mobileSearchClose: $('#mobileSearchClose'),
        themeToggle:       $('#themeToggle'),
        shareBtn:          $('#shareBtn'),
        footerShareTwitter:$('#footerShareTwitter'),
        footerCopyLink:    $('#footerCopyLink'),
        searchInput:       $('#searchInput'),
        searchClear:       $('#searchClear'),
        searchShortcut:    null,
        filterTabs:        $$('.filter-tab'),
        categoryChips:     $$('.category-chip'),
        searchResultsInfo: $('#searchResultsInfo'),
        resultsCount:      $('#resultsCount'),
        clearFiltersBtn:   $('#clearFiltersBtn'),
        timelineTrack:     $('#timelineTrack'),
        timelineContainer: $('#timelineContainer'),
        timelinePrev:      $('#timelinePrev'),
        timelineNext:      $('#timelineNext'),
        modalOverlay:      $('#modalOverlay'),
        modalHeader:       $('#modalHeader'),
        modalTag:          $('#modalTag'),
        modalTitle:        $('#modalTitle'),
        modalMeta:         $('#modalMeta'),
        modalMetaBadges:   $('#modalMetaBadges'),
        modalSummary:      $('#modalSummary'),
        modalCharacters:   $('#modalCharacters'),
        modalCharactersSection: $('#modalCharactersSection'),
        modalThemes:       $('#modalThemes'),
        modalThemesSection:    $('#modalThemesSection'),
        modalConcepts:     $('#modalConcepts'),
        modalStructure:    $('#modalStructure'),
        modalStructureSection: $('#modalStructureSection'),
        modalQuote:        $('#modalQuote'),
        modalExtraQuotes:  $('#modalExtraQuotes'),
        modalCommentary:   $('#modalCommentary'),
        modalRelevance:    $('#modalRelevance'),
        modalRelevanceSection: $('#modalRelevanceSection'),
        modalContext:      $('#modalContext'),
        modalRelated:      $('#modalRelated'),
        modalRelatedSection:   $('#modalRelatedSection'),
        modalClose:        $('#modalClose'),
        modalShareTwitter: $('#modalShareTwitter'),
        modalCopyLink:     $('#modalCopyLink'),
        modalPrev:         $('#modalPrev'),
        modalNext:         $('#modalNext'),
        toast:             $('#toast'),
        toastMessage:      $('#toastMessage'),
        backToTop:         $('#backToTop'),
        currentYear:       $('#currentYear'),
        footerFilterLinks: $$('[data-filter-link]')
    };

    var S = {
        filter:    'all',
        category:  'all',
        query:     '',
        modalIdx:  -1,
        filtered:  [],
        menuOpen:  false,
        searchOpen:false,
        modalOpen: false
    };

    function W() { return window.WORKS || []; }

    function allPhilosopherIds() {
        var seen = {}, ids = [];
        W().forEach(function (w) {
            if (!seen[w.philosopher]) { seen[w.philosopher] = true; ids.push(w.philosopher); }
        });
        return ids;
    }

    function cap(s) { return s.charAt(0).toUpperCase() + s.slice(1); }

    var PHIL_NAMES = {
        plato:'Plato', aristotle:'Aristotle', descartes:'Descartes',
        spinoza:'Spinoza', leibniz:'Leibniz', locke:'Locke',
        berkeley:'Berkeley', kant:'Kant', fichte:'Fichte',
        schelling:'Schelling', hegel:'Hegel', schopenhauer:'Schopenhauer',
        nietzsche:'Nietzsche', kierkegaard:'Kierkegaard', marx:'Marx & Engels'
    };
    function philName(id) { return PHIL_NAMES[id] || cap(id); }

    function readingTime(wc) {
        var m = Math.ceil(wc / 200);
        return m < 60 ? m + ' min' : Math.floor(m/60)+'h'+(m%60?' '+m%60+'m':'');
    }

    function escHtml(s) {
        return String(s||'').replace(/&/g,'&amp;').replace(/</g,'&lt;')
            .replace(/>/g,'&gt;').replace(/"/g,'&quot;');
    }
    function escAttr(s) {
        return String(s||'').replace(/"/g,'&quot;').replace(/'/g,'&#39;');
    }

    /* ── INIT ── */
    function init() {
        if (D.currentYear) D.currentYear.textContent = new Date().getFullYear();
        loadTheme();
        renderCards();
        renderTimeline();
        updateCounts();
        bindEvents();
        initObservers();
        addSearchShortcutHint();
        setTimeout(function () {
            if (D.loader) D.loader.classList.add('hidden');
            D.body.classList.remove('no-scroll');
        }, 1200);
    }

    /* ── THEME ── */
    function loadTheme() {
        var saved = localStorage.getItem('pa-theme');
        if (saved) D.html.setAttribute('data-theme', saved);
    }
    function toggleTheme() {
        var nxt = D.html.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
        D.html.setAttribute('data-theme', nxt);
        localStorage.setItem('pa-theme', nxt);
    }

    /* ── CARDS ── */
    function cardHTML(work, idx) {
        var phil = work.philosopher;
        var themes = '';
        if (work.themes && work.themes.length > 0) {
            themes = work.themes.slice(0,3).map(function(t){
                return '<span class="card-theme">'+escHtml(t)+'</span>';
            }).join('<span class="card-theme">\u00b7</span>');
        }
        var wideClass = work.cardSize === 'wide' ? ' card-wide' : '';
        return '<article class="work-card'+wideClass+'"'+
            ' data-id="'+work.id+'"'+
            ' data-index="'+idx+'"'+
            ' data-philosopher="'+phil+'"'+
            ' data-category="'+work.category+'"'+
            ' role="button" tabindex="0"'+
            ' aria-label="'+escAttr(work.title)+'">'+
            '<div class="card-header">'+
                '<span class="card-dot '+phil+'-dot"></span>'+
                '<span class="card-category">'+escHtml(work.categoryLabel)+' \u00b7 '+escHtml(work.date)+'</span>'+
            '</div>'+
            '<h3 class="card-title">'+escHtml(work.title)+'</h3>'+
            '<p class="card-greek">'+escHtml(work.greekTitle)+'</p>'+
            '<p class="card-description">'+escHtml(work.shortDesc)+'</p>'+
            '<div class="card-footer">'+
                '<div class="card-footer-left">'+
                    '<span class="card-date">'+escHtml(work.readingDifficulty||'')+'</span>'+
                    (work.estimatedWordCount?'<span class="card-reading-time">'+readingTime(work.estimatedWordCount)+'</span>':'')+
                '</div>'+
                '<div class="card-themes">'+themes+'</div>'+
            '</div>'+
        '</article>';
    }

    function renderCards() {
        var all = getFiltered();
        var hasQuery = S.query.trim().length > 0;

        allPhilosopherIds().forEach(function(philId) {
            var grid = document.getElementById(philId+'Grid');
            if (!grid) return;
            var works = all.filter(function(w){ return w.philosopher === philId; });
            grid.innerHTML = works.length > 0
                ? works.map(function(w){ return cardHTML(w, W().indexOf(w)); }).join('')
                : '';
        });

        updateSectionVisibility(all, hasQuery);

        requestAnimationFrame(function() {
            $$('.work-card').forEach(function(c,i){
                setTimeout(function(){ c.classList.add('visible'); }, i*30);
            });
        });
        bindCardEvents();
        updateResultsInfo();
    }

    /* ── SECTION VISIBILITY: the core fix ── */
    function updateSectionVisibility(filteredWorks, hasQuery) {
        $$('.works-section').forEach(function(sec) {
            var philId = (sec.id||'').replace('-section','');
            if (S.filter !== 'all') {
                sec.style.display = (philId === S.filter) ? '' : 'none';
            } else if (hasQuery) {
                var hasResults = filteredWorks.some(function(w){ return w.philosopher === philId; });
                sec.style.display = hasResults ? '' : 'none';
            } else {
                sec.style.display = '';
            }
        });
    }

    /* ── FILTER / SEARCH ── */
    function getFiltered() {
        var r = W().slice();
        if (S.filter !== 'all') r = r.filter(function(w){ return w.philosopher === S.filter; });
        if (S.category !== 'all') r = r.filter(function(w){ return w.category === S.category; });
        if (S.query.trim()) {
            var q = S.query.toLowerCase().trim();
            r = r.filter(function(w) {
                var blob = [
                    w.title, w.greekTitle, w.philosopher,
                    w.category, w.categoryLabel, w.shortDesc,
                    w.summary||'', w.date, w.modernRelevance||'', w.context||''
                ].concat(w.concepts||[])
                 .concat(w.themes||[])
                 .concat((w.keyCharacters||[]).map(function(c){ return c.name+' '+c.role; }))
                 .concat((w.commentary||[]).map(function(c){ return c.philosopher+' '+c.text; }))
                 .join(' ').toLowerCase();
                return blob.indexOf(q) !== -1;
            });
        }
        S.filtered = r;
        return r;
    }

    function handleSearch(e) {
        S.query = e.target.value;
        if (e.target === D.searchInput && D.mobileSearchInput) D.mobileSearchInput.value = S.query;
        else if (e.target === D.mobileSearchInput && D.searchInput) D.searchInput.value = S.query;
        if (D.searchClear) D.searchClear.style.display = S.query ? 'flex' : 'none';
        if (D.searchShortcut) D.searchShortcut.style.opacity = S.query ? '0' : '0';
        renderCards();
    }

    function clearSearch() {
        S.query = '';
        if (D.searchInput) D.searchInput.value = '';
        if (D.mobileSearchInput) D.mobileSearchInput.value = '';
        if (D.searchClear) D.searchClear.style.display = 'none';
        if (D.searchShortcut) D.searchShortcut.style.opacity = '1';
        renderCards();
    }

    function setFilter(f) {
        S.filter = f;
        D.filterTabs.forEach(function(t){
            t.classList.toggle('active', t.dataset.filter === f);
            t.setAttribute('aria-selected', String(t.dataset.filter === f));
        });
        if (f !== 'all') {
            S.category = 'all';
            D.categoryChips.forEach(function(c){ c.classList.toggle('active', c.dataset.category === 'all'); });
        }
        renderCards();
        var sec = $('#searchSection');
        if (sec) sec.scrollIntoView({behavior:'smooth', block:'start'});
    }

    function setCategory(c) {
        S.category = c;
        D.categoryChips.forEach(function(ch){ ch.classList.toggle('active', ch.dataset.category === c); });
        renderCards();
    }

    function clearAll() {
        S.filter='all'; S.category='all'; S.query='';
        if (D.searchInput) D.searchInput.value='';
        if (D.mobileSearchInput) D.mobileSearchInput.value='';
        if (D.searchClear) D.searchClear.style.display='none';
        if (D.searchShortcut) D.searchShortcut.style.opacity='1';
        D.filterTabs.forEach(function(t){
            t.classList.toggle('active', t.dataset.filter==='all');
            t.setAttribute('aria-selected', String(t.dataset.filter==='all'));
        });
        D.categoryChips.forEach(function(c){ c.classList.toggle('active', c.dataset.category==='all'); });
        renderCards();
    }

    function updateCounts() {
        var w = W();
        var el = document.getElementById('countAll');
        if (el) el.textContent = w.length;
        allPhilosopherIds().forEach(function(id) {
            var countEl = document.getElementById('count'+cap(id));
            if (countEl) countEl.textContent = w.filter(function(x){ return x.philosopher===id; }).length;
        });
    }

    function updateResultsInfo() {
        var on = S.query || S.filter!=='all' || S.category!=='all';
        if (D.searchResultsInfo) D.searchResultsInfo.style.display = on ? 'flex' : 'none';
        if (D.resultsCount) D.resultsCount.textContent = S.filtered.length;
    }

    function addSearchShortcutHint() {
        var box = D.searchInput && D.searchInput.parentElement;
        if (!box || document.getElementById('searchShortcut')) return;
        var hint = document.createElement('span');
        hint.id = 'searchShortcut';
        hint.setAttribute('aria-hidden','true');
        hint.style.cssText = 'position:absolute;right:44px;top:50%;transform:translateY(-50%);'+
            'font-size:11px;letter-spacing:.08em;color:var(--text-tertiary,#aaa);'+
            'pointer-events:none;transition:opacity .15s;font-family:var(--font-mono,monospace)';
        hint.textContent = '/ to search';
        box.style.position = 'relative';
        box.appendChild(hint);
        D.searchShortcut = hint;
    }

    /* ── MODAL ── */
    function openModal(idx) {
        var work = W()[idx];
        if (!work) return;
        S.modalIdx = idx; S.modalOpen = true;
        var phil = work.philosopher;

        if (D.modalHeader) D.modalHeader.className = 'modal-header modal-philosopher-'+phil;
        if (D.modalTag) { D.modalTag.className='modal-tag'; D.modalTag.textContent=philName(phil)+' \u00b7 '+work.categoryLabel; }
        if (D.modalTitle) D.modalTitle.textContent = work.title;
        if (D.modalMeta) D.modalMeta.innerHTML = '<em>'+escHtml(work.greekTitle)+'</em> \u00b7 '+escHtml(work.date);

        if (D.modalMetaBadges) {
            var badges = '';
            if (work.readingDifficulty) badges += '<span class="meta-badge">'+escHtml(work.readingDifficulty)+'</span>';
            if (work.estimatedWordCount) {
                var _m = Math.ceil(work.estimatedWordCount/200);
                var _rt = _m<60 ? _m+' min' : Math.floor(_m/60)+'h'+(_m%60?' '+_m%60+'m':'');
                var wc = work.estimatedWordCount>=1000 ? Math.round(work.estimatedWordCount/1000)+'k words' : work.estimatedWordCount+' words';
                badges += '<span class="meta-badge meta-badge-time">'+_rt+' read</span>';
                badges += '<span class="meta-badge meta-badge-words">~'+wc+'</span>';
            }
            D.modalMetaBadges.innerHTML = badges;
        }

        if (D.modalSummary) {
            D.modalSummary.innerHTML = (work.summary||'').split('\n\n').map(function(p){
                return '<p>'+escHtml(p.trim())+'</p>';
            }).join('');
        }

        if (D.modalCharactersSection) {
            var hasChars = work.keyCharacters && work.keyCharacters.length > 0;
            D.modalCharactersSection.style.display = hasChars ? 'block' : 'none';
            if (hasChars) D.modalCharacters.innerHTML = work.keyCharacters.map(function(ch){
                return '<div class="character-entry"><div class="character-name">'+escHtml(ch.name)+'</div>'+
                    '<div class="character-role">'+escHtml(ch.role)+'</div></div>';
            }).join('');
        }

        if (D.modalThemesSection) {
            var hasThemes = work.themes && work.themes.length > 0;
            D.modalThemesSection.style.display = hasThemes ? 'block' : 'none';
            if (hasThemes) D.modalThemes.innerHTML = work.themes.map(function(t){
                return '<span class="theme-tag">'+escHtml(t)+'</span>';
            }).join('');
        }

        if (D.modalConcepts) {
            D.modalConcepts.innerHTML = (work.concepts||[]).map(function(c){
                var text = typeof c==='string' ? c : (c.text||'');
                /* Split "Term — explanation" into headword + body */
                var dash = text.search(/\s[—–]\s/);
                if (dash !== -1) {
                    var term = text.substring(0, dash).trim();
                    var desc = text.substring(dash).replace(/^\s*[—–]\s*/, '').trim();
                    return '<div class="concept-item">'+
                        '<span class="concept-term">'+escHtml(term)+'</span>'+
                        '<span class="concept-desc">'+escHtml(desc)+'</span>'+
                    '</div>';
                }
                return '<div class="concept-item concept-plain">'+
                    '<span class="concept-desc">'+escHtml(text)+'</span>'+
                '</div>';
            }).join('');
        }

        if (D.modalStructureSection) {
            D.modalStructureSection.style.display = work.structure ? 'block' : 'none';
            if (work.structure && D.modalStructure) D.modalStructure.textContent = work.structure;
        }

        if (D.modalQuote) {
            var qraw = work.quote||'';
            var di = qraw.lastIndexOf('\u2014');
            var qT = di!==-1 ? qraw.substring(0,di).replace(/^"|"$/g,'').trim() : qraw.replace(/^"|"$/g,'').trim();
            var qC = di!==-1 ? qraw.substring(di+1).trim() : '';
            D.modalQuote.innerHTML = '\u201c'+escHtml(qT)+'\u201d'+(qC?'<cite>\u2014 '+escHtml(qC)+'</cite>':'');
        }

        if (D.modalExtraQuotes) {
            var hasExtra = work.additionalQuotes && work.additionalQuotes.length > 0;
            D.modalExtraQuotes.style.display = hasExtra ? 'block' : 'none';
            D.modalExtraQuotes.innerHTML = hasExtra ? work.additionalQuotes.map(function(aq){
                return '<blockquote class="extra-quote">\u201c'+escHtml(aq.text)+'\u201d<cite>'+escHtml(aq.citation)+'</cite></blockquote>';
            }).join('') : '';
        }

        if (D.modalCommentary) {
            D.modalCommentary.innerHTML = (work.commentary||[]).map(function(c){
                return '<div class="commentary-entry"><div class="commentary-philosopher">'+escHtml(c.philosopher)+'</div>'+
                    '<p class="commentary-text">'+escHtml(c.text)+'</p></div>';
            }).join('');
        }

        if (D.modalRelevanceSection) {
            D.modalRelevanceSection.style.display = work.modernRelevance ? 'block' : 'none';
            if (work.modernRelevance && D.modalRelevance) D.modalRelevance.textContent = work.modernRelevance;
        }

        if (D.modalContext) D.modalContext.textContent = work.context||'';

        if (D.modalRelatedSection) {
            var relHtml = '';
            if (work.relatedWorks && work.relatedWorks.length > 0) {
                relHtml = work.relatedWorks.map(function(rid){
                    var rw = W().find(function(x){ return x.id===rid; });
                    return rw ? '<button class="related-link" data-rid="'+escAttr(rid)+'">'+escHtml(rw.title)+'</button>' : '';
                }).join('');
            }
            D.modalRelatedSection.style.display = relHtml ? 'block' : 'none';
            if (relHtml) {
                D.modalRelated.innerHTML = relHtml;
                D.modalRelated.querySelectorAll('.related-link').forEach(function(btn){
                    btn.addEventListener('click', function(){
                        var ri = W().findIndex(function(x){ return x.id===btn.dataset.rid; });
                        if (ri!==-1) openModal(ri);
                    });
                });
            }
        }

        if (D.modalOverlay) { D.modalOverlay.classList.add('active'); D.modalOverlay.setAttribute('aria-hidden','false'); }
        D.body.classList.add('no-scroll');
        if (D.modalClose) D.modalClose.focus();
        updateModalNav();
    }

    function closeModal() {
        if (D.modalOverlay) { D.modalOverlay.classList.remove('active'); D.modalOverlay.setAttribute('aria-hidden','true'); }
        D.body.classList.remove('no-scroll');
        S.modalOpen=false; S.modalIdx=-1;
    }

    function updateModalNav() {
        var hp = S.modalIdx > 0, hn = S.modalIdx < W().length-1;
        if (D.modalPrev) { D.modalPrev.style.opacity=hp?'1':'0.3'; D.modalPrev.style.pointerEvents=hp?'auto':'none'; }
        if (D.modalNext) { D.modalNext.style.opacity=hn?'1':'0.3'; D.modalNext.style.pointerEvents=hn?'auto':'none'; }
    }

    function navModal(dir) {
        var ni = S.modalIdx+dir;
        if (ni>=0 && ni<W().length) openModal(ni);
    }

    /* ── TIMELINE ── */
    function renderTimeline() {
        if (!D.timelineTrack) return;

        /* Which philosophers have works loaded? */
        var present = {};
        W().forEach(function(w){ present[w.philosopher] = true; });
        var active = PHIL_TIMELINE.filter(function(p){ return present[p.id]; });
        if (active.length === 0) { active = PHIL_TIMELINE; }

        /* Sort chronologically by birth year */
        active = active.slice().sort(function(a, b){ return a.born - b.born; });

        /* Era bands — defined by index ranges in sorted order */
        var ERAS = [
          { label:'Ancient Greece',  ids:['plato','aristotle'] },
          { label:'Early Modern',    ids:['descartes','spinoza','locke','leibniz','berkeley'] },
          { label:'Enlightenment',   ids:['hume','kant'] },
          { label:'German Idealism', ids:['fichte','schelling','hegel','schopenhauer'] },
          { label:'19th Century',    ids:['kierkegaard','marx','nietzsche'] }
        ];

        /* Track layout */
        var N = active.length;
        var PAD = 5;           /* % padding each side */
        var USABLE = 100 - PAD * 2;
        function nodeLeft(i){ return (PAD + (i / Math.max(N - 1, 1)) * USABLE).toFixed(2); }

        D.timelineTrack.style.position = 'relative';
        D.timelineTrack.style.height   = '180px';
        D.timelineTrack.innerHTML      = '';

        /* Horizontal line */
        var line = document.createElement('div');
        line.style.cssText = 'position:absolute;top:64px;left:'+PAD+'%;right:'+PAD+'%;height:1px;background:var(--border);';
        D.timelineTrack.appendChild(line);

        /* Era background bands */
        ERAS.forEach(function(era){
            var indices = [];
            active.forEach(function(p, i){ if (era.ids.indexOf(p.id) !== -1) indices.push(i); });
            if (indices.length === 0) return;
            var firstI = Math.min.apply(null, indices);
            var lastI  = Math.max.apply(null, indices);
            /* Extend band half a slot either side */
            var step   = USABLE / Math.max(N - 1, 1);
            var left   = Math.max(0, parseFloat(nodeLeft(firstI)) - step / 2);
            var right  = Math.min(100, parseFloat(nodeLeft(lastI))  + step / 2);
            var band   = document.createElement('div');
            band.style.cssText = 'position:absolute;top:0;bottom:0;' +
                'left:' + left.toFixed(2) + '%;width:' + (right - left).toFixed(2) + '%;' +
                'background:rgba(154,120,64,0.04);pointer-events:none;' +
                'border-left:1px solid rgba(154,120,64,0.10);';
            var lbl = document.createElement('span');
            lbl.style.cssText = 'position:absolute;bottom:6px;left:50%;' +
                'transform:translateX(-50%);' +
                'font-family:var(--font-mono);font-size:0.55rem;' +
                'letter-spacing:0.1em;color:var(--text-muted);white-space:nowrap;';
            lbl.textContent = era.label.toUpperCase();
            band.appendChild(lbl);
            D.timelineTrack.appendChild(band);
        });

        /* Philosopher nodes — evenly spaced */
        active.forEach(function(phil, i){
            var node = document.createElement('div');
            node.style.cssText = 'position:absolute;left:'+nodeLeft(i)+'%;top:0;' +
                'transform:translateX(-50%);' +
                'display:flex;flex-direction:column;align-items:center;' +
                'cursor:pointer;width:90px;transition:transform 0.18s;';
            node.setAttribute('role','button');
            node.setAttribute('tabindex','0');
            node.setAttribute('aria-label', phil.name + ' ' +
                (phil.born < 0 ? Math.abs(phil.born)+'BC' : phil.born+'AD'));

            /* Date label */
            var dateEl = document.createElement('span');
            dateEl.style.cssText = 'font-family:var(--font-mono);font-size:0.58rem;' +
                'color:var(--gold);letter-spacing:0.06em;margin-bottom:8px;white-space:nowrap;';
            dateEl.textContent = phil.born < 0 ? Math.abs(phil.born)+' BC' : phil.born;
            node.appendChild(dateEl);

            /* Dot */
            var dot = document.createElement('div');
            dot.style.cssText = 'width:10px;height:10px;border-radius:50%;' +
                'background:'+phil.color+';border:2px solid var(--bg);' +
                'margin-bottom:8px;z-index:2;flex-shrink:0;' +
                'transition:transform 0.18s,box-shadow 0.18s;';
            node.appendChild(dot);

            /* Name */
            var nameEl = document.createElement('span');
            nameEl.style.cssText = 'font-family:var(--font-heading);font-size:0.78rem;' +
                'font-weight:600;text-align:center;color:var(--text);' +
                'line-height:1.2;max-width:86px;';
            nameEl.textContent = phil.name;
            node.appendChild(nameEl);

            /* Hover */
            node.addEventListener('mouseenter', function(){
                dot.style.transform  = 'scale(1.55)';
                dot.style.boxShadow  = '0 0 0 4px '+phil.color+'28';
                node.style.transform = 'translateX(-50%) translateY(-4px)';
            });
            node.addEventListener('mouseleave', function(){
                dot.style.transform  = '';
                dot.style.boxShadow  = '';
                node.style.transform = 'translateX(-50%)';
            });

            /* Click: filter + scroll to section */
            function goToPhil(){
                var tab = document.querySelector('[data-filter="'+phil.id+'"]');
                if (tab) tab.click();
                var sec = document.getElementById(phil.id+'-section');
                if (sec) sec.scrollIntoView({behavior:'smooth',block:'start'});
            }
            node.addEventListener('click', goToPhil);
            node.addEventListener('keydown', function(e){
                if (e.key==='Enter'||e.key===' '){ e.preventDefault(); goToPhil(); }
            });

            D.timelineTrack.appendChild(node);
        });

        /* Era label: update to show hovered / scrolled era */
        if (D.timelineContainer) {
            D.timelineContainer.addEventListener('scroll', function(){
                var ratio = D.timelineContainer.scrollLeft /
                    (D.timelineContainer.scrollWidth - D.timelineContainer.clientWidth || 1);
                var idx   = Math.round(ratio * (active.length - 1));
                var phil  = active[Math.min(idx, active.length - 1)];
                var lbl   = 'Western Philosophy';
                if (phil) {
                    ERAS.forEach(function(e){
                        if (e.ids.indexOf(phil.id) !== -1) lbl = e.label;
                    });
                }
                if (D.timelineEra) D.timelineEra.textContent = lbl;
            });
        }
    }

    function scrollTL(dir) {
        if (D.timelineContainer) D.timelineContainer.scrollBy({left:dir*300,behavior:'smooth'});
    }

    /* ── OBSERVERS ── */
    function initObservers() {
        var obs = new IntersectionObserver(function(entries){
            entries.forEach(function(en){
                if (en.isIntersecting){ en.target.classList.add('visible'); obs.unobserve(en.target); }
            });
        }, {threshold:0.1, rootMargin:'0px 0px -30px 0px'});
        $$('.fade-in-element').forEach(function(el){ obs.observe(el); });
    }

    /* ── CARD EVENTS ── */
    function bindCardEvents() {
        $$('.work-card').forEach(function(card){
            card.addEventListener('click', function(){ openModal(parseInt(card.dataset.index,10)); });
            card.addEventListener('keydown', function(e){
                if (e.key==='Enter'||e.key===' '){ e.preventDefault(); openModal(parseInt(card.dataset.index,10)); }
            });
        });
    }

    /* ── MOBILE NAV ── */
    function toggleMenu() {
        S.menuOpen=!S.menuOpen;
        if (D.hamburger){ D.hamburger.classList.toggle('active',S.menuOpen); D.hamburger.setAttribute('aria-expanded',String(S.menuOpen)); }
        if (D.mobileNavOverlay){ D.mobileNavOverlay.classList.toggle('active',S.menuOpen); D.mobileNavOverlay.setAttribute('aria-hidden',String(!S.menuOpen)); }
        D.body.classList.toggle('no-scroll',S.menuOpen);
    }
    function closeMenu() {
        S.menuOpen=false;
        if (D.hamburger){ D.hamburger.classList.remove('active'); D.hamburger.setAttribute('aria-expanded','false'); }
        if (D.mobileNavOverlay){ D.mobileNavOverlay.classList.remove('active'); D.mobileNavOverlay.setAttribute('aria-hidden','true'); }
        D.body.classList.remove('no-scroll');
    }
    function toggleMobileSearch() {
        S.searchOpen=!S.searchOpen;
        if (D.mobileSearchBar) D.mobileSearchBar.classList.toggle('active',S.searchOpen);
        if (S.searchOpen && D.mobileSearchInput) D.mobileSearchInput.focus();
    }
    function closeMobileSearch() {
        S.searchOpen=false;
        if (D.mobileSearchBar) D.mobileSearchBar.classList.remove('active');
    }

    /* ── SCROLL ── */
    function onScroll() {
        var y = window.scrollY;
        if (D.navbar) D.navbar.classList.toggle('scrolled', y>40);
        if (D.backToTop) D.backToTop.classList.toggle('visible', y>500);
    }

    /* ── SHARE / TOAST ── */
    function showToast(msg) {
        if (D.toastMessage) D.toastMessage.textContent=msg;
        if (D.toast){ D.toast.classList.add('active'); setTimeout(function(){ D.toast.classList.remove('active'); },2500); }
    }
    function copyLink(url) {
        var u = url||window.location.href;
        if (navigator.clipboard) { navigator.clipboard.writeText(u).then(function(){ showToast('Link copied'); }); }
        else {
            var ta=document.createElement('textarea'); ta.value=u; ta.style.cssText='position:fixed;opacity:0';
            document.body.appendChild(ta); ta.select(); document.execCommand('copy'); document.body.removeChild(ta);
            showToast('Link copied');
        }
    }
    function shareTwitter(text) {
        var t=text||'The Academy & The Lyceum \u2014 a complete philosophy archive.';
        window.open('https://twitter.com/intent/tweet?text='+encodeURIComponent(t)+'&url='+encodeURIComponent(window.location.href),'_blank','width=550,height=420');
    }
    function shareSite() {
        if (navigator.share) { navigator.share({title:'The Academy & The Lyceum',text:'A complete philosophy archive.',url:window.location.href}).catch(function(){}); }
        else { copyLink(); }
    }

    /* ── BIND ALL EVENTS ── */
    function bindEvents() {
        if (D.themeToggle) D.themeToggle.addEventListener('click',toggleTheme);
        if (D.hamburger) D.hamburger.addEventListener('click',toggleMenu);
        D.mobileNavLinks.forEach(function(l){ l.addEventListener('click',closeMenu); });
        if (D.searchToggle) D.searchToggle.addEventListener('click',toggleMobileSearch);
        if (D.mobileSearchClose) D.mobileSearchClose.addEventListener('click',closeMobileSearch);
        if (D.mobileSearchInput) D.mobileSearchInput.addEventListener('input',handleSearch);
        if (D.searchInput) D.searchInput.addEventListener('input',handleSearch);
        if (D.searchClear) D.searchClear.addEventListener('click',clearSearch);

        D.filterTabs.forEach(function(t){ t.addEventListener('click',function(){ setFilter(t.dataset.filter); }); });
        D.categoryChips.forEach(function(c){ c.addEventListener('click',function(){ setCategory(c.dataset.category); }); });
        if (D.clearFiltersBtn) D.clearFiltersBtn.addEventListener('click',clearAll);

        if (D.modalClose) D.modalClose.addEventListener('click',closeModal);
        if (D.modalOverlay) D.modalOverlay.addEventListener('click',function(e){ if(e.target===D.modalOverlay) closeModal(); });
        if (D.modalPrev) D.modalPrev.addEventListener('click',function(){ navModal(-1); });
        if (D.modalNext) D.modalNext.addEventListener('click',function(){ navModal(1); });

        if (D.modalShareTwitter) D.modalShareTwitter.addEventListener('click',function(){
            var w=W()[S.modalIdx]; if(w) shareTwitter(w.title+' \u2014 '+philName(w.philosopher)+' \u2014 The Academy & The Lyceum.');
        });
        if (D.modalCopyLink) D.modalCopyLink.addEventListener('click',function(){
            var w=W()[S.modalIdx]; if(w) copyLink(window.location.href+'#'+w.id);
        });
        if (D.shareBtn) D.shareBtn.addEventListener('click',shareSite);
        if (D.footerShareTwitter) D.footerShareTwitter.addEventListener('click',function(){ shareTwitter(); });
        if (D.footerCopyLink) D.footerCopyLink.addEventListener('click',function(){ copyLink(); });
        if (D.timelinePrev) D.timelinePrev.addEventListener('click',function(){ scrollTL(-1); });
        if (D.timelineNext) D.timelineNext.addEventListener('click',function(){ scrollTL(1); });
        if (D.backToTop) D.backToTop.addEventListener('click',function(){ window.scrollTo({top:0,behavior:'smooth'}); });

        window.addEventListener('scroll',onScroll,{passive:true});

        document.addEventListener('keydown',function(e){
            if (e.key==='Escape'){
                if (S.modalOpen){ closeModal(); return; }
                if (S.menuOpen){ closeMenu(); return; }
                if (S.searchOpen){ closeMobileSearch(); return; }
                if (S.query){ clearSearch(); return; }
            }
            if (S.modalOpen){ if(e.key==='ArrowLeft') navModal(-1); if(e.key==='ArrowRight') navModal(1); }
            if (e.key==='/' && !S.modalOpen && document.activeElement!==D.searchInput){
                e.preventDefault();
                if (D.searchInput){ D.searchInput.focus(); var sec=$('#searchSection'); if(sec) sec.scrollIntoView({behavior:'smooth',block:'start'}); }
            }
        });

        if (D.searchInput) {
            D.searchInput.addEventListener('focus',function(){ if(D.searchShortcut) D.searchShortcut.style.opacity='0'; });
            D.searchInput.addEventListener('blur',function(){ if(!S.query&&D.searchShortcut) D.searchShortcut.style.opacity='1'; });
        }

        D.footerFilterLinks.forEach(function(link){
            link.addEventListener('click',function(e){
                e.preventDefault();
                var cat=link.dataset.filterLink, sec=$('#searchSection');
                if(sec){ sec.scrollIntoView({behavior:'smooth'}); setTimeout(function(){ setCategory(cat); },400); }
            });
        });

        $$('a[href^="#"]').forEach(function(a){
            a.addEventListener('click',function(e){
                var tid=a.getAttribute('href'); if(tid==='#') return;
                var tgt=document.querySelector(tid);
                if(tgt){ e.preventDefault(); var off=parseInt(getComputedStyle(D.html).getPropertyValue('--nav-h'))||64; window.scrollTo({top:tgt.getBoundingClientRect().top+window.scrollY-off-16,behavior:'smooth'}); }
            });
        });
    }

    if (document.readyState==='loading') { document.addEventListener('DOMContentLoaded',init); } else { init(); }

    /* ── Deep-link handler: index.html#work=some-id opens that modal ── */
    function handleHash() {
        var hash = window.location.hash;
        if (!hash) return;
        /* Format: #work=some-work-id */
        var workMatch = hash.match(/^#work=(.+)$/);
        if (workMatch) {
            var targetId = decodeURIComponent(workMatch[1]);
            var idx = W().findIndex ? W().findIndex(function(w){ return w.id === targetId; })
                : (function(){ for(var i=0;i<W().length;i++){ if(W()[i].id===targetId) return i; } return -1; })();
            if (idx !== -1) {
                setTimeout(function(){ openModal(idx); }, 300);
            }
        }
        /* Format: #plato-section etc — smooth scroll (already handled, but ensure) */
    }
    window.addEventListener('load', handleHash);
})();
