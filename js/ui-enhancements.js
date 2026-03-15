// ============================================================
// UI ENHANCEMENTS — Philosophy Archive (Polished v3)
// Apple-quality search experience
// ============================================================

(function () {
    'use strict';

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', function () { setTimeout(boot, 100); });
    } else {
        setTimeout(boot, 100);
    }

    function boot() {
        var el = findElements();
        if (!el.searchInput) { console.warn('[UI] no search input'); return; }
        setupScrollHide(el);
        setupSearchDropdown(el);
        setupPhilosopherNavigation(el);
        setupSectionVisibility(el);
        console.log('[UI] initialized');
    }

    function findElements() {
        var searchInput =
            document.querySelector('input[placeholder*="Search"]') ||
            document.querySelector('.search-input') ||
            document.querySelector('#search-input');

        return {
            searchInput: searchInput,
            philBtns: document.querySelectorAll('[data-philosopher]'),
            catBtns: document.querySelectorAll('[data-category]'),
            sections: document.querySelectorAll('.philosopher-section, section[data-philosopher]')
        };
    }

    function getActivePhilosopher(el) {
        for (var i = 0; i < el.philBtns.length; i++) {
            var b = el.philBtns[i];
            var cl = b.className || '';
            if (cl.indexOf('active') !== -1 || cl.indexOf('selected') !== -1 ||
                b.getAttribute('aria-pressed') === 'true') {
                return b.dataset.philosopher;
            }
        }
        return 'all';
    }

    function cap(s) { return s ? s.charAt(0).toUpperCase() + s.slice(1) : ''; }

    function escHtml(s) {
        var d = document.createElement('div');
        d.appendChild(document.createTextNode(s));
        return d.innerHTML;
    }

    function highlightMatch(text, query) {
        if (!query || query.length < 2) return escHtml(text);
        var escaped = escHtml(text);
        var qEsc = query.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
        var re = new RegExp('(' + qEsc + ')', 'gi');
        return escaped.replace(re, '<mark class="search-hl">$1</mark>');
    }

    function formatWordCount(n) {
        if (!n) return '';
        if (n >= 1000) return Math.round(n / 1000) + 'k words';
        return n + ' words';
    }

    function getDifficultyClass(d) {
        if (!d) return '';
        var dl = (d + '').toLowerCase();
        if (dl === 'beginner' || dl === '1' || dl === '2') return 'diff-beginner';
        if (dl === 'intermediate' || dl === '3') return 'diff-intermediate';
        return 'diff-advanced';
    }

    function getDifficultyLabel(d) {
        if (!d) return '';
        var dl = (d + '').toLowerCase();
        if (dl === 'beginner' || dl === '1' || dl === '2') return 'Beginner';
        if (dl === 'intermediate' || dl === '3') return 'Intermediate';
        if (dl === 'advanced' || dl === '4' || dl === '5') return 'Advanced';
        return d;
    }

    // ═══════════════════════════════════════════════════════
    // 1. SCROLL-HIDE
    // ═══════════════════════════════════════════════════════
    function setupScrollHide(el) {
        var lastY = window.scrollY;
        var hidden = false;
        var bars = collectStickyBars(el);
        if (!bars.length) return;

        for (var i = 0; i < bars.length; i++) {
            bars[i].style.willChange = 'transform, opacity';
            bars[i].style.transition = 'transform 0.35s cubic-bezier(0.4,0,0.2,1), opacity 0.3s ease';
        }

        window.addEventListener('scroll', function () {
            requestAnimationFrame(function () {
                var y = window.scrollY;
                var dd = document.querySelector('.search-dropdown.active');
                if (dd) { doShow(); lastY = y; return; }
                if (y > lastY && y > 180 && !hidden) doHide();
                else if (y < lastY && hidden) doShow();
                lastY = y;
            });
        }, { passive: true });

        function doHide() {
            for (var i = 0; i < bars.length; i++) {
                bars[i].style.transform = 'translateY(-100%)';
                bars[i].style.opacity = '0';
                bars[i].style.pointerEvents = 'none';
            }
            hidden = true;
        }
        function doShow() {
            for (var i = 0; i < bars.length; i++) {
                bars[i].style.transform = 'translateY(0)';
                bars[i].style.opacity = '1';
                bars[i].style.pointerEvents = '';
            }
            hidden = false;
        }
    }

    function collectStickyBars(el) {
        var bars = [], seen = [];
        function addIfSticky(startEl) {
            var p = startEl;
            while (p && p !== document.body && p !== document.documentElement) {
                var pos = window.getComputedStyle(p).position;
                if (pos === 'sticky' || pos === 'fixed') {
                    var found = false;
                    for (var i = 0; i < seen.length; i++) { if (seen[i] === p) { found = true; break; } }
                    if (!found) { bars.push(p); seen.push(p); }
                }
                p = p.parentElement;
            }
        }
        if (el.searchInput) addIfSticky(el.searchInput);
        if (el.philBtns && el.philBtns.length > 0) addIfSticky(el.philBtns[0]);
        if (el.catBtns && el.catBtns.length > 0) addIfSticky(el.catBtns[0]);
        return bars;
    }

    // ═══════════════════════════════════════════════════════
    // 2. SEARCH DROPDOWN — Apple-polished
    // ═══════════════════════════════════════════════════════
    function setupSearchDropdown(el) {
        var input = el.searchInput;
        if (!input) return;

        var originalParent = input.parentElement;
        var wrapper = document.createElement('div');
        wrapper.className = 'search-input-wrapper';
        wrapper.style.position = 'relative';
        originalParent.insertBefore(wrapper, input);
        wrapper.appendChild(input);

        var dropdown = document.createElement('div');
        dropdown.className = 'search-dropdown';
        dropdown.setAttribute('role', 'listbox');
        dropdown.setAttribute('aria-label', 'Search results');
        wrapper.appendChild(dropdown);

        var timer = null;
        var activeIndex = -1;
        var lastQuery = '';

        input.addEventListener('input', function () {
            clearTimeout(timer);
            var q = input.value.trim();
            if (q === lastQuery) return;
            lastQuery = q;
            timer = setTimeout(function () { doSearch(input, dropdown); }, 150);
            activeIndex = -1;
        });

        input.addEventListener('focus', function () {
            if (input.value.trim().length >= 2) {
                clearTimeout(timer);
                timer = setTimeout(function () { doSearch(input, dropdown); }, 60);
            }
        });

        input.addEventListener('keydown', function (e) {
            if (!dropdown.classList.contains('active')) return;
            var items = dropdown.querySelectorAll('.sdr-item');
            if (!items.length) return;

            if (e.key === 'ArrowDown') {
                e.preventDefault();
                activeIndex = Math.min(activeIndex + 1, items.length - 1);
                hlItem(items, activeIndex);
            } else if (e.key === 'ArrowUp') {
                e.preventDefault();
                activeIndex = Math.max(activeIndex - 1, 0);
                hlItem(items, activeIndex);
            } else if (e.key === 'Enter') {
                e.preventDefault();
                if (activeIndex >= 0 && items[activeIndex]) items[activeIndex].click();
            } else if (e.key === 'Escape') {
                closeDD(dropdown);
                input.blur();
            }
        });

        dropdown.addEventListener('click', function (e) {
            var item = e.target.closest('.sdr-item');
            if (!item) return;
            var workId = item.dataset.workId;
            var philosopher = item.dataset.philosopher;

            var btn = document.querySelector('[data-philosopher="' + philosopher + '"]');
            if (btn) btn.click();

            setTimeout(function () {
                var card = document.querySelector('[data-id="' + workId + '"], [data-work="' + workId + '"]');
                if (card) {
                    card.scrollIntoView({ behavior: 'smooth', block: 'center' });
                    setTimeout(function () { card.click(); }, 400);
                } else {
                    var sec = document.getElementById(philosopher) ||
                        document.querySelector('[data-philosopher="' + philosopher + '"]');
                    if (sec) sec.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }
            }, 200);

            closeDD(dropdown);
            input.value = '';
            lastQuery = '';
            input.dispatchEvent(new Event('input', { bubbles: true }));
        });

        document.addEventListener('click', function (e) {
            if (!wrapper.contains(e.target)) closeDD(dropdown);
        });
    }

    function closeDD(dd) { dd.classList.remove('active'); }

    function doSearch(input, dropdown) {
        var query = input.value.trim().toLowerCase();

        if (query.length < 2) { closeDD(dropdown); return; }

        var works = window.WORKS || [];
        var scored = [];

        for (var i = 0; i < works.length; i++) {
            var w = works[i];
            var score = 0;
            var tl = (w.title || '').toLowerCase();
            var gl = (w.greekTitle || '').toLowerCase();
            var pl = (w.philosopher || '').toLowerCase();
            var sl = (w.shortDesc || '').toLowerCase();
            var cl = (w.categoryLabel || '').toLowerCase();
            var th = (w.themes || []).join(' ').toLowerCase();
            var co = (w.concepts || []).join(' ').toLowerCase();

            // Weighted scoring
            if (tl === query) score += 100;
            else if (tl.indexOf(query) === 0) score += 80;
            else if (tl.indexOf(query) !== -1) score += 60;

            if (pl.indexOf(query) !== -1) score += 40;
            if (gl.indexOf(query) !== -1) score += 30;
            if (cl.indexOf(query) !== -1) score += 20;
            if (sl.indexOf(query) !== -1) score += 15;
            if (th.indexOf(query) !== -1) score += 10;
            if (co.indexOf(query) !== -1) score += 5;

            if (score > 0) scored.push({ work: w, score: score });
        }

        // Sort by score descending
        scored.sort(function (a, b) { return b.score - a.score; });

        var matches = [];
        for (var j = 0; j < Math.min(scored.length, 8); j++) {
            matches.push(scored[j].work);
        }

        // Group by philosopher
        var groups = {};
        var groupOrder = [];
        for (var k = 0; k < matches.length; k++) {
            var ph = matches[k].philosopher;
            if (!groups[ph]) { groups[ph] = []; groupOrder.push(ph); }
            groups[ph].push(matches[k]);
        }

        if (matches.length === 0) {
            dropdown.innerHTML =
                '<div class="sdr-empty">' +
                '<div class="sdr-empty-icon">\uD83D\uDD0D</div>' +
                '<div class="sdr-empty-text">No results for \u201c' + escHtml(input.value.trim()) + '\u201d</div>' +
                '<div class="sdr-empty-hint">Try a title, philosopher, or theme</div>' +
                '</div>';
            dropdown.classList.add('active');
            return;
        }

        var html = '<div class="sdr-header">' +
            '<span class="sdr-header-count">' + matches.length +
            (matches.length < scored.length ? ' of ' + scored.length : '') +
            ' result' + (scored.length !== 1 ? 's' : '') + '</span>' +
            '<span class="sdr-header-hint">\u2191\u2193 to navigate \u00B7 \u21B5 to select</span>' +
            '</div>';

        for (var g = 0; g < groupOrder.length; g++) {
            var gName = groupOrder[g];
            var gWorks = groups[gName];

            if (groupOrder.length > 1) {
                html += '<div class="sdr-group-label">' + cap(gName) + '</div>';
            }

            for (var m = 0; m < gWorks.length; m++) {
                var w = gWorks[m];
                var diffClass = getDifficultyClass(w.readingDifficulty);
                var diffLabel = getDifficultyLabel(w.readingDifficulty);
                var wc = formatWordCount(w.estimatedWordCount);

                html +=
                    '<div class="sdr-item" role="option" tabindex="-1" ' +
                    'data-work-id="' + w.id + '" data-philosopher="' + w.philosopher + '">' +

                    '<div class="sdr-item-icon">' +
                    '<span class="sdr-emoji">' + (w.emoji || '\uD83D\uDCD6') + '</span>' +
                    '</div>' +

                    '<div class="sdr-item-body">' +

                    '<div class="sdr-item-title">' + highlightMatch(w.title, query) + '</div>' +

                    '<div class="sdr-item-subtitle">' +
                    (w.greekTitle && w.greekTitle !== w.title
                        ? '<span class="sdr-original">' + escHtml(w.greekTitle) + '</span>'
                        : '') +
                    '</div>' +

                    '<div class="sdr-item-meta">' +
                    '<span class="sdr-meta-chip sdr-meta-date">' + (w.date || '') + '</span>' +
                    '<span class="sdr-meta-chip sdr-meta-cat">' + (w.categoryLabel || '') + '</span>' +
                    (wc ? '<span class="sdr-meta-chip sdr-meta-wc">' + wc + '</span>' : '') +
                    (diffLabel ? '<span class="sdr-meta-chip sdr-meta-diff ' + diffClass + '">' + diffLabel + '</span>' : '') +
                    '</div>' +

                    '<div class="sdr-item-desc">' + escHtml(w.shortDesc || '').substring(0, 120) +
                    (w.shortDesc && w.shortDesc.length > 120 ? '\u2026' : '') + '</div>' +

                    '</div>' +

                    '<div class="sdr-item-action">' +
                    '<svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M6 3l5 5-5 5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>' +
                    '</div>' +

                    '</div>';
            }
        }

        dropdown.innerHTML = html;
        dropdown.classList.add('active');
    }

    function hlItem(items, idx) {
        for (var i = 0; i < items.length; i++) {
            items[i].classList.toggle('highlighted', i === idx);
            items[i].setAttribute('aria-selected', i === idx ? 'true' : 'false');
        }
        if (items[idx]) items[idx].scrollIntoView({ block: 'nearest', behavior: 'smooth' });
    }

    // ═══════════════════════════════════════════════════════
    // 3. PHILOSOPHER BUTTON SCROLL
    // ═══════════════════════════════════════════════════════
    function setupPhilosopherNavigation(el) {
        for (var i = 0; i < el.philBtns.length; i++) {
            (function (btn) {
                btn.addEventListener('click', function () {
                    var phil = btn.dataset.philosopher;
                    if (!phil || phil === 'all') return;
                    setTimeout(function () {
                        var sec = document.getElementById(phil) ||
                            document.querySelector('.philosopher-section[data-philosopher="' + phil + '"]');
                        if (sec && sec.style.display !== 'none') {
                            var top = sec.getBoundingClientRect().top + window.scrollY - 24;
                            window.scrollTo({ top: Math.max(0, top), behavior: 'smooth' });
                        }
                    }, 150);
                });
                btn.style.cursor = 'pointer';
                if (btn.dataset.philosopher !== 'all') btn.title = 'Jump to ' + cap(btn.dataset.philosopher);
            })(el.philBtns[i]);
        }
    }

    // ═══════════════════════════════════════════════════════
    // 4. SECTION VISIBILITY
    // ═══════════════════════════════════════════════════════
    function setupSectionVisibility(el) {
        function sched() {
            setTimeout(function () { upd(el); }, 30);
            setTimeout(function () { upd(el); }, 150);
            setTimeout(function () { upd(el); }, 400);
        }
        for (var i = 0; i < el.philBtns.length; i++) el.philBtns[i].addEventListener('click', sched);
        for (var j = 0; j < el.catBtns.length; j++) el.catBtns[j].addEventListener('click', sched);
        if (el.searchInput) el.searchInput.addEventListener('input', function () { setTimeout(function () { upd(el); }, 250); });
        document.addEventListener('click', function (e) {
            if (e.target.textContent && e.target.textContent.toLowerCase().indexOf('clear') !== -1) sched();
        });
        if (window.MutationObserver) {
            var mo = new MutationObserver(function () { setTimeout(function () { upd(el); }, 50); });
            for (var k = 0; k < el.philBtns.length; k++) mo.observe(el.philBtns[k], { attributes: true, attributeFilter: ['class'] });
        }
        sched();
    }

    function upd(el) {
        var active = getActivePhilosopher(el);
        for (var i = 0; i < el.sections.length; i++) {
            var sec = el.sections[i];
            var sp = sec.dataset.philosopher || sec.id;
            if (active && active !== 'all') {
                sec.style.display = (sp === active) ? '' : 'none';
                if (sp === active) sec.style.opacity = '1';
            } else {
                sec.style.display = '';
                sec.style.opacity = '1';
                var grid = sec.querySelector('.works-grid, .grid');
                if (grid && isFilt(el)) {
                    var cards = grid.children, vis = false;
                    for (var c = 0; c < cards.length; c++) {
                        var cs = window.getComputedStyle(cards[c]);
                        if (cs.display !== 'none' && !cards[c].classList.contains('hidden')) { vis = true; break; }
                    }
                    if (!vis) sec.style.display = 'none';
                }
            }
        }
    }

    function isFilt(el) {
        for (var i = 0; i < el.catBtns.length; i++) {
            var b = el.catBtns[i];
            if (b.dataset.category !== 'all' && (b.className || '').indexOf('active') !== -1) return true;
        }
        return el.searchInput && el.searchInput.value.trim().length > 0;
    }

})();
