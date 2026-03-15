// ============================================================
// UI ENHANCEMENTS — Philosophy Archive (Fixed v2)
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
    function escHtml(s) { var d = document.createElement('div'); d.appendChild(document.createTextNode(s)); return d.innerHTML; }

    // ═══════════════════════════════════════════════════════
    // 1. SCROLL-HIDE — finds ALL sticky/fixed bars and hides them
    // ═══════════════════════════════════════════════════════
    function setupScrollHide(el) {
        var lastY = window.scrollY;
        var hidden = false;

        // Collect every sticky/fixed element in the controls area
        var bars = collectStickyBars(el);
        if (!bars.length) { console.warn('[UI] no sticky bars found'); return; }

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
        var bars = [];
        var seen = [];

        function addIfSticky(startEl) {
            var p = startEl;
            while (p && p !== document.body && p !== document.documentElement) {
                var pos = window.getComputedStyle(p).position;
                if (pos === 'sticky' || pos === 'fixed') {
                    // Check not already added
                    var found = false;
                    for (var i = 0; i < seen.length; i++) { if (seen[i] === p) { found = true; break; } }
                    if (!found) {
                        bars.push(p);
                        seen.push(p);
                    }
                }
                p = p.parentElement;
            }
        }

        // From search input — find its sticky ancestor
        if (el.searchInput) addIfSticky(el.searchInput);

        // From first philosopher button — may be in a different sticky container
        if (el.philBtns && el.philBtns.length > 0) addIfSticky(el.philBtns[0]);

        // From first category button — may be in yet another container
        if (el.catBtns && el.catBtns.length > 0) addIfSticky(el.catBtns[0]);

        // If we found nested sticky parents, keep only the outermost ones
        // unless they are truly separate containers
        // (This handles both "one big sticky wrapper" and "multiple sticky rows")

        console.log('[UI] found ' + bars.length + ' sticky bar(s) to hide on scroll');
        return bars;
    }

    // ═══════════════════════════════════════════════════════
    // 2. SEARCH DROPDOWN
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
        wrapper.appendChild(dropdown);

        var timer = null;
        var activeIndex = -1;

        input.addEventListener('input', function () {
            clearTimeout(timer);
            timer = setTimeout(function () { doSearch(input, dropdown); }, 180);
            activeIndex = -1;
        });

        input.addEventListener('focus', function () {
            if (input.value.trim().length >= 2) {
                clearTimeout(timer);
                timer = setTimeout(function () { doSearch(input, dropdown); }, 80);
            }
        });

        input.addEventListener('keydown', function (e) {
            if (!dropdown.classList.contains('active')) return;
            var items = dropdown.querySelectorAll('.search-dropdown-item');
            if (!items.length) return;

            if (e.key === 'ArrowDown') {
                e.preventDefault();
                activeIndex = Math.min(activeIndex + 1, items.length - 1);
                hlItem(items, activeIndex);
            } else if (e.key === 'ArrowUp') {
                e.preventDefault();
                activeIndex = Math.max(activeIndex - 1, 0);
                hlItem(items, activeIndex);
            } else if (e.key === 'Enter' && activeIndex >= 0 && items[activeIndex]) {
                e.preventDefault();
                items[activeIndex].click();
            } else if (e.key === 'Escape') {
                dropdown.classList.remove('active');
                input.blur();
            }
        });

        dropdown.addEventListener('click', function (e) {
            var item = e.target.closest('.search-dropdown-item');
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

            dropdown.classList.remove('active');
            input.value = '';
            input.dispatchEvent(new Event('input', { bubbles: true }));
        });

        document.addEventListener('click', function (e) {
            if (!wrapper.contains(e.target)) dropdown.classList.remove('active');
        });
    }

    function doSearch(input, dropdown) {
        var q = input.value.trim().toLowerCase();
        if (q.length < 2) { dropdown.classList.remove('active'); return; }

        var works = window.WORKS || [];
        var matches = [];
        for (var i = 0; i < works.length; i++) {
            var w = works[i];
            var h = [w.title||'', w.greekTitle||'', w.philosopher||'', w.shortDesc||'',
                     w.categoryLabel||'', (w.themes||[]).join(' '), (w.concepts||[]).join(' ')
                    ].join(' ').toLowerCase();
            if (h.indexOf(q) !== -1) { matches.push(w); if (matches.length >= 10) break; }
        }

        if (!matches.length) {
            dropdown.innerHTML = '<div class="search-dropdown-empty">No results for \u201c' + escHtml(input.value.trim()) + '\u201d</div>';
            dropdown.classList.add('active');
            return;
        }

        var html = '';
        for (var j = 0; j < matches.length; j++) {
            var m = matches[j];
            html += '<div class="search-dropdown-item" data-work-id="' + m.id + '" data-philosopher="' + m.philosopher + '">' +
                '<span class="sdi-emoji">' + (m.emoji||'') + '</span>' +
                '<div class="sdi-content">' +
                '<div class="sdi-title">' + escHtml(m.title) + '</div>' +
                '<div class="sdi-meta">' + cap(m.philosopher) + ' \u00B7 ' + (m.date||'') + ' \u00B7 ' + (m.categoryLabel||'') + '</div>' +
                '</div><span class="sdi-arrow">\u2192</span></div>';
        }
        dropdown.innerHTML = html;
        dropdown.classList.add('active');
    }

    function hlItem(items, idx) {
        for (var i = 0; i < items.length; i++) items[i].classList.toggle('highlighted', i === idx);
        if (items[idx]) items[idx].scrollIntoView({ block: 'nearest' });
    }

    // ═══════════════════════════════════════════════════════
    // 3. PHILOSOPHER BUTTON → SCROLL TO SECTION
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
    // 4. SECTION VISIBILITY — hide irrelevant sections
    // ═══════════════════════════════════════════════════════
    function setupSectionVisibility(el) {
        function sched() {
            setTimeout(function () { upd(el); }, 30);
            setTimeout(function () { upd(el); }, 150);
            setTimeout(function () { upd(el); }, 400);
        }
        for (var i = 0; i < el.philBtns.length; i++) el.philBtns[i].addEventListener('click', sched);
        for (var j = 0; j < el.catBtns.length; j++) el.catBtns[j].addEventListener('click', sched);
        if (el.searchInput) el.searchInput.addEventListener('input', function () { setTimeout(function(){ upd(el); }, 250); });
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
            if (b.dataset.category !== 'all' && (b.className||'').indexOf('active') !== -1) return true;
        }
        return el.searchInput && el.searchInput.value.trim().length > 0;
    }

})();
