// ============================================================
// UI ENHANCEMENTS — Philosophy Archive
// ============================================================

(function () {
    'use strict';

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', function () {
            setTimeout(boot, 80);
        });
    } else {
        setTimeout(boot, 80);
    }

    function boot() {
        var el = findElements();
        if (!el.searchInput) {
            console.warn('[UI-Enhancements] search input not found');
            return;
        }
        setupScrollHide(el);
        setupSearchDropdown(el);
        setupPhilosopherNavigation(el);
        setupSectionVisibility(el);
        console.log('[UI-Enhancements] initialized');
    }

    function findElements() {
        var searchInput =
            document.querySelector('input[placeholder*="Search"]') ||
            document.querySelector('.search-input') ||
            document.querySelector('#search-input');

        var filterBar = null;
        if (searchInput) {
            var p = searchInput.parentElement;
            while (p && p !== document.body) {
                var pos = window.getComputedStyle(p).position;
                if (pos === 'sticky' || pos === 'fixed') { filterBar = p; break; }
                p = p.parentElement;
            }
            if (!filterBar) {
                filterBar =
                    searchInput.closest('.search-filter-bar') ||
                    searchInput.closest('.controls-wrapper') ||
                    searchInput.closest('.filter-bar') ||
                    searchInput.closest('.sticky-controls');
            }
            if (!filterBar) filterBar = searchInput.parentElement;
        }

        return {
            searchInput: searchInput,
            filterBar: filterBar,
            philBtns: document.querySelectorAll('[data-philosopher]'),
            catBtns: document.querySelectorAll('[data-category]'),
            sections: document.querySelectorAll('.philosopher-section, section[data-philosopher]')
        };
    }

    function getActivePhilosopher(el) {
        var btns = el.philBtns;
        for (var i = 0; i < btns.length; i++) {
            var b = btns[i];
            var cl = b.className || '';
            if (
                cl.indexOf('active') !== -1 ||
                cl.indexOf('selected') !== -1 ||
                cl.indexOf('is-active') !== -1 ||
                b.getAttribute('aria-pressed') === 'true'
            ) {
                return b.dataset.philosopher;
            }
        }
        return 'all';
    }

    function capitalizeFirst(s) {
        return s ? s.charAt(0).toUpperCase() + s.slice(1) : '';
    }

    function escapeHtml(s) {
        var d = document.createElement('div');
        d.appendChild(document.createTextNode(s));
        return d.innerHTML;
    }

    // ═══════════════════════════════════════
    // 1. SCROLL-HIDE FILTER BAR
    // ═══════════════════════════════════════
    function setupScrollHide(el) {
        if (!el.filterBar) return;

        var bar = el.filterBar;
        var lastY = window.scrollY;
        var hidden = false;

        bar.style.willChange = 'transform, opacity';
        bar.style.transition = 'transform 0.35s cubic-bezier(0.4,0,0.2,1), opacity 0.3s ease';

        window.addEventListener('scroll', function () {
            requestAnimationFrame(function () {
                var y = window.scrollY;

                var dd = document.querySelector('.search-dropdown.active');
                if (dd) { show(); lastY = y; return; }

                if (y > lastY && y > 180 && !hidden) {
                    hide();
                } else if (y < lastY && hidden) {
                    show();
                }
                lastY = y;
            });
        }, { passive: true });

        function hide() {
            bar.style.transform = 'translateY(-100%)';
            bar.style.opacity = '0';
            bar.style.pointerEvents = 'none';
            hidden = true;
        }
        function show() {
            bar.style.transform = 'translateY(0)';
            bar.style.opacity = '1';
            bar.style.pointerEvents = '';
            hidden = false;
        }
    }

    // ═══════════════════════════════════════
    // 2. SEARCH DROPDOWN
    // ═══════════════════════════════════════
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
                highlightItem(items, activeIndex);
            } else if (e.key === 'ArrowUp') {
                e.preventDefault();
                activeIndex = Math.max(activeIndex - 1, 0);
                highlightItem(items, activeIndex);
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
                    var section = document.getElementById(philosopher) ||
                        document.querySelector('[data-philosopher="' + philosopher + '"]');
                    if (section) section.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }
            }, 200);

            dropdown.classList.remove('active');
            input.value = '';
            input.dispatchEvent(new Event('input', { bubbles: true }));
        });

        document.addEventListener('click', function (e) {
            if (!wrapper.contains(e.target)) {
                dropdown.classList.remove('active');
            }
        });
    }

    function doSearch(input, dropdown) {
        var query = input.value.trim().toLowerCase();

        if (query.length < 2) {
            dropdown.classList.remove('active');
            return;
        }

        var works = window.WORKS || [];
        var matches = [];

        for (var i = 0; i < works.length; i++) {
            var w = works[i];
            var haystack = [
                w.title || '',
                w.greekTitle || '',
                w.philosopher || '',
                w.shortDesc || '',
                w.categoryLabel || '',
                (w.themes || []).join(' '),
                (w.concepts || []).join(' ')
            ].join(' ').toLowerCase();

            if (haystack.indexOf(query) !== -1) {
                matches.push(w);
                if (matches.length >= 10) break;
            }
        }

        if (matches.length === 0) {
            dropdown.innerHTML =
                '<div class="search-dropdown-empty">' +
                'No results for \u201c' + escapeHtml(input.value.trim()) + '\u201d' +
                '</div>';
            dropdown.classList.add('active');
            return;
        }

        var html = '';
        for (var j = 0; j < matches.length; j++) {
            var m = matches[j];
            html +=
                '<div class="search-dropdown-item" ' +
                'data-work-id="' + m.id + '" data-philosopher="' + m.philosopher + '">' +
                '<span class="sdi-emoji">' + (m.emoji || '') + '</span>' +
                '<div class="sdi-content">' +
                '<div class="sdi-title">' + escapeHtml(m.title) + '</div>' +
                '<div class="sdi-meta">' +
                '<span class="sdi-philosopher">' + capitalizeFirst(m.philosopher) + '</span>' +
                ' \u00B7 ' +
                '<span class="sdi-date">' + (m.date || '') + '</span>' +
                ' \u00B7 ' +
                '<span class="sdi-cat">' + (m.categoryLabel || '') + '</span>' +
                '</div></div>' +
                '<span class="sdi-arrow">\u2192</span>' +
                '</div>';
        }

        dropdown.innerHTML = html;
        dropdown.classList.add('active');
    }

    function highlightItem(items, idx) {
        for (var i = 0; i < items.length; i++) {
            items[i].classList.toggle('highlighted', i === idx);
        }
        if (items[idx]) items[idx].scrollIntoView({ block: 'nearest' });
    }

    // ═══════════════════════════════════════
    // 3. PHILOSOPHER BUTTON → SCROLL
    // ═══════════════════════════════════════
    function setupPhilosopherNavigation(el) {
        for (var i = 0; i < el.philBtns.length; i++) {
            (function (btn) {
                btn.addEventListener('click', function () {
                    var phil = btn.dataset.philosopher;
                    if (!phil || phil === 'all') return;

                    setTimeout(function () {
                        var section =
                            document.getElementById(phil) ||
                            document.querySelector('.philosopher-section[data-philosopher="' + phil + '"]');

                        if (section && section.style.display !== 'none') {
                            var barH = el.filterBar ? el.filterBar.offsetHeight : 0;
                            var top = section.getBoundingClientRect().top + window.scrollY - barH - 24;
                            window.scrollTo({ top: Math.max(0, top), behavior: 'smooth' });
                        }
                    }, 150);
                });

                btn.style.cursor = 'pointer';
                if (btn.dataset.philosopher !== 'all') {
                    btn.title = 'Jump to ' + capitalizeFirst(btn.dataset.philosopher);
                }
            })(el.philBtns[i]);
        }
    }

    // ═══════════════════════════════════════
    // 4. SECTION VISIBILITY
    // ═══════════════════════════════════════
    function setupSectionVisibility(el) {
        function scheduleUpdate() {
            setTimeout(function () { updateSections(el); }, 30);
            setTimeout(function () { updateSections(el); }, 150);
            setTimeout(function () { updateSections(el); }, 400);
        }

        for (var i = 0; i < el.philBtns.length; i++) {
            el.philBtns[i].addEventListener('click', scheduleUpdate);
        }
        for (var j = 0; j < el.catBtns.length; j++) {
            el.catBtns[j].addEventListener('click', scheduleUpdate);
        }
        if (el.searchInput) {
            el.searchInput.addEventListener('input', function () {
                setTimeout(function () { updateSections(el); }, 250);
            });
        }

        document.addEventListener('click', function (e) {
            if (e.target.textContent && e.target.textContent.toLowerCase().indexOf('clear') !== -1) {
                scheduleUpdate();
            }
        });

        if (window.MutationObserver) {
            var mo = new MutationObserver(function () {
                setTimeout(function () { updateSections(el); }, 50);
            });
            for (var k = 0; k < el.philBtns.length; k++) {
                mo.observe(el.philBtns[k], { attributes: true, attributeFilter: ['class'] });
            }
        }

        scheduleUpdate();
    }

    function updateSections(el) {
        var active = getActivePhilosopher(el);

        for (var i = 0; i < el.sections.length; i++) {
            var section = el.sections[i];
            var sectionPhil = section.dataset.philosopher || section.id;

            if (active && active !== 'all') {
                if (sectionPhil === active) {
                    section.style.display = '';
                    section.style.opacity = '1';
                } else {
                    section.style.display = 'none';
                }
            } else {
                section.style.display = '';
                section.style.opacity = '1';

                var grid = section.querySelector('.works-grid, .grid');
                if (grid && isFilterActive(el)) {
                    var cards = grid.children;
                    var hasVisible = false;
                    for (var c = 0; c < cards.length; c++) {
                        var cs = window.getComputedStyle(cards[c]);
                        if (cs.display !== 'none' && !cards[c].classList.contains('hidden')) {
                            hasVisible = true;
                            break;
                        }
                    }
                    if (!hasVisible) {
                        section.style.display = 'none';
                    }
                }
            }
        }
    }

    function isFilterActive(el) {
        for (var i = 0; i < el.catBtns.length; i++) {
            var b = el.catBtns[i];
            if (b.dataset.category !== 'all' && (b.className || '').indexOf('active') !== -1) {
                return true;
            }
        }
        if (el.searchInput && el.searchInput.value.trim().length > 0) return true;
        return false;
    }

})();
