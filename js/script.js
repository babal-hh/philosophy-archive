/* ================================================================
   THE ACADEMY & THE LYCEUM
   Application Logic - Clean typographic version
   Reads from window.WORKS global array
   ================================================================ */

;(function () {
    'use strict';

    var $ = function (s) { return document.querySelector(s); };
    var $$ = function (s) { return document.querySelectorAll(s); };

    /* ── DOM ── */

    var D = {
        loader: $('#loader'),
        body: document.body,
        html: document.documentElement,
        navbar: $('#navbar'),
        hamburger: $('#hamburger'),
        mobileNavOverlay: $('#mobileNavOverlay'),
        mobileNavLinks: $$('.mobile-nav-link'),
        searchToggle: $('#searchToggle'),
        mobileSearchBar: $('#mobileSearchBar'),
        mobileSearchInput: $('#mobileSearchInput'),
        mobileSearchClose: $('#mobileSearchClose'),
        themeToggle: $('#themeToggle'),
        shareBtn: $('#shareBtn'),
        footerShareTwitter: $('#footerShareTwitter'),
        footerCopyLink: $('#footerCopyLink'),
        searchInput: $('#searchInput'),
        searchClear: $('#searchClear'),
        filterTabs: $$('.filter-tab'),
        categoryChips: $$('.category-chip'),
        searchResultsInfo: $('#searchResultsInfo'),
        resultsCount: $('#resultsCount'),
        clearFiltersBtn: $('#clearFiltersBtn'),
        countAll: $('#countAll'),
        countPlato: $('#countPlato'),
        countAristotle: $('#countAristotle'),
        platoGrid: $('#platoGrid'),
        aristotleGrid: $('#aristotleGrid'),
        timelineTrack: $('#timelineTrack'),
        timelineContainer: $('#timelineContainer'),
        timelinePrev: $('#timelinePrev'),
        timelineNext: $('#timelineNext'),
        modalOverlay: $('#modalOverlay'),
        modalHeader: $('#modalHeader'),
        modalTag: $('#modalTag'),
        modalTitle: $('#modalTitle'),
        modalMeta: $('#modalMeta'),
        modalMetaBadges: $('#modalMetaBadges'),
        modalSummary: $('#modalSummary'),
        modalCharacters: $('#modalCharacters'),
        modalCharactersSection: $('#modalCharactersSection'),
        modalThemes: $('#modalThemes'),
        modalThemesSection: $('#modalThemesSection'),
        modalConcepts: $('#modalConcepts'),
        modalStructure: $('#modalStructure'),
        modalStructureSection: $('#modalStructureSection'),
        modalQuote: $('#modalQuote'),
        modalExtraQuotes: $('#modalExtraQuotes'),
        modalCommentary: $('#modalCommentary'),
        modalRelevance: $('#modalRelevance'),
        modalRelevanceSection: $('#modalRelevanceSection'),
        modalContext: $('#modalContext'),
        modalRelated: $('#modalRelated'),
        modalRelatedSection: $('#modalRelatedSection'),
        modalClose: $('#modalClose'),
        modalShareTwitter: $('#modalShareTwitter'),
        modalCopyLink: $('#modalCopyLink'),
        modalPrev: $('#modalPrev'),
        modalNext: $('#modalNext'),
        toast: $('#toast'),
        toastMessage: $('#toastMessage'),
        backToTop: $('#backToTop'),
        currentYear: $('#currentYear'),
        footerFilterLinks: $$('[data-filter-link]')
    };

    /* ── State ── */

    var S = {
        filter: 'all',
        category: 'all',
        query: '',
        modalIdx: -1,
        filtered: [],
        menuOpen: false,
        searchOpen: false,
        modalOpen: false
    };

    function W() { return window.WORKS || []; }


    /* ══════════════════════════════════════
       INIT
    ══════════════════════════════════════ */

    function init() {
        if (D.currentYear) D.currentYear.textContent = new Date().getFullYear();
        loadTheme();
        renderCards();
        renderTimeline();
        updateCounts();
        bindEvents();
        initObservers();
        setTimeout(function () {
            if (D.loader) D.loader.classList.add('hidden');
            D.body.classList.remove('no-scroll');
        }, 1400);
    }


    /* ══════════════════════════════════════
       THEME
    ══════════════════════════════════════ */

    function loadTheme() {
        var saved = localStorage.getItem('pa-theme');
        if (saved) D.html.setAttribute('data-theme', saved);
    }

    function toggleTheme() {
        var cur = D.html.getAttribute('data-theme');
        var nxt = cur === 'dark' ? 'light' : 'dark';
        D.html.setAttribute('data-theme', nxt);
        localStorage.setItem('pa-theme', nxt);
    }


    /* ══════════════════════════════════════
       CARD RENDERING
    ══════════════════════════════════════ */

    function cardHTML(work, idx) {
        var pc = work.philosopher === 'plato' ? 'plato-card' : 'aristotle-card';

        var themes = '';
        if (work.themes && work.themes.length > 0) {
            var show = work.themes.slice(0, 3);
            themes = show.map(function (t) {
                return '<span class="card-theme">' + t + '</span>';
            }).join('<span class="card-theme">\u00b7</span>');
        }

        return '<article class="work-card ' + pc + '" ' +
            'data-id="' + work.id + '" ' +
            'data-index="' + idx + '" ' +
            'data-philosopher="' + work.philosopher + '" ' +
            'data-category="' + work.category + '" ' +
            'role="button" tabindex="0" ' +
            'aria-label="' + work.title + '">' +
            '<div class="card-header">' +
                '<span class="card-dot"></span>' +
                '<span class="card-category">' + work.categoryLabel + ' \u00b7 ' + work.date + '</span>' +
            '</div>' +
            '<h3 class="card-title">' + work.title + '</h3>' +
            '<p class="card-greek">' + work.greekTitle + '</p>' +
            '<p class="card-description">' + work.shortDesc + '</p>' +
            '<div class="card-footer">' +
                '<span class="card-date">' +
                    (work.readingDifficulty ? work.readingDifficulty : '') +
                '</span>' +
                '<div class="card-themes">' + themes + '</div>' +
            '</div>' +
        '</article>';
    }

    function renderCards() {
        var all = getFiltered();
        var plato = all.filter(function (w) { return w.philosopher === 'plato'; });
        var aris = all.filter(function (w) { return w.philosopher === 'aristotle'; });

        if (D.platoGrid) {
            D.platoGrid.innerHTML = plato.length > 0
                ? plato.map(function (w) { return cardHTML(w, W().indexOf(w)); }).join('')
                : noResults('Plato');
        }
        if (D.aristotleGrid) {
            D.aristotleGrid.innerHTML = aris.length > 0
                ? aris.map(function (w) { return cardHTML(w, W().indexOf(w)); }).join('')
                : noResults('Aristotle');
        }

        requestAnimationFrame(function () {
            $$('.work-card').forEach(function (c, i) {
                setTimeout(function () { c.classList.add('visible'); }, i * 50);
            });
        });

        bindCardEvents();
        updateResultsInfo();
    }

    function noResults(name) {
        return '<div class="no-results">' +
            '<h3 class="no-results-title">No ' + name + ' works found</h3>' +
            '<p class="no-results-text">Try adjusting your search or filters.</p>' +
        '</div>';
    }


    /* ══════════════════════════════════════
       SEARCH & FILTER
    ══════════════════════════════════════ */

    function getFiltered() {
        var r = W().slice();
        if (S.filter !== 'all') {
            r = r.filter(function (w) { return w.philosopher === S.filter; });
        }
        if (S.category !== 'all') {
            r = r.filter(function (w) { return w.category === S.category; });
        }
        if (S.query.trim()) {
            var q = S.query.toLowerCase().trim();
            r = r.filter(function (w) {
                var blob = [
                    w.title, w.greekTitle, w.philosopher,
                    w.category, w.categoryLabel, w.shortDesc,
                    w.summary, w.date
                ].concat(w.concepts || [])
                 .concat(w.themes || [])
                 .concat((w.commentary || []).map(function (c) {
                     return c.philosopher + ' ' + c.text;
                 })).join(' ').toLowerCase();
                return blob.indexOf(q) !== -1;
            });
        }
        S.filtered = r;
        return r;
    }

    function handleSearch(e) {
        S.query = e.target.value;
        if (e.target === D.searchInput && D.mobileSearchInput)
            D.mobileSearchInput.value = e.target.value;
        else if (e.target === D.mobileSearchInput && D.searchInput)
            D.searchInput.value = e.target.value;
        if (D.searchClear)
            D.searchClear.style.display = S.query ? 'flex' : 'none';
        renderCards();
    }

    function clearSearch() {
        S.query = '';
        if (D.searchInput) D.searchInput.value = '';
        if (D.mobileSearchInput) D.mobileSearchInput.value = '';
        if (D.searchClear) D.searchClear.style.display = 'none';
        renderCards();
    }

    function setFilter(f) {
        S.filter = f;
        D.filterTabs.forEach(function (t) {
            t.classList.toggle('active', t.dataset.filter === f);
            t.setAttribute('aria-selected', t.dataset.filter === f);
        });
        if (f !== 'all') {
            S.category = 'all';
            D.categoryChips.forEach(function (c) {
                c.classList.toggle('active', c.dataset.category === 'all');
            });
        }
        renderCards();
    }

    function setCategory(c) {
        S.category = c;
        D.categoryChips.forEach(function (ch) {
            ch.classList.toggle('active', ch.dataset.category === c);
        });
        renderCards();
    }

    function clearAll() {
        S.filter = 'all';
        S.category = 'all';
        S.query = '';
        if (D.searchInput) D.searchInput.value = '';
        if (D.mobileSearchInput) D.mobileSearchInput.value = '';
        if (D.searchClear) D.searchClear.style.display = 'none';
        D.filterTabs.forEach(function (t) {
            t.classList.toggle('active', t.dataset.filter === 'all');
        });
        D.categoryChips.forEach(function (c) {
            c.classList.toggle('active', c.dataset.category === 'all');
        });
        renderCards();
    }

    function updateCounts() {
        var w = W();
        if (D.countAll) D.countAll.textContent = w.length;
        if (D.countPlato) D.countPlato.textContent = w.filter(function (x) { return x.philosopher === 'plato'; }).length;
        if (D.countAristotle) D.countAristotle.textContent = w.filter(function (x) { return x.philosopher === 'aristotle'; }).length;
    }

    function updateResultsInfo() {
        var on = S.query || S.filter !== 'all' || S.category !== 'all';
        if (D.searchResultsInfo) D.searchResultsInfo.style.display = on ? 'flex' : 'none';
        if (D.resultsCount) D.resultsCount.textContent = S.filtered.length;
    }


    /* ══════════════════════════════════════
       MODAL
    ══════════════════════════════════════ */

    function openModal(idx) {
        var work = W()[idx];
        if (!work) return;
        S.modalIdx = idx;
        S.modalOpen = true;
        var ip = work.philosopher === 'plato';

        /* Header */
        D.modalHeader.className = 'modal-header ' + (ip ? 'plato-modal-header' : 'aristotle-modal-header');
        D.modalTag.className = 'modal-tag ' + (ip ? 'plato-modal-tag' : 'aristotle-modal-tag');
        D.modalTag.textContent = (ip ? 'Plato' : 'Aristotle') + ' \u00b7 ' + work.categoryLabel;
        D.modalTitle.textContent = work.title;
        D.modalMeta.innerHTML = '<em>' + work.greekTitle + '</em> \u00b7 ' + work.date;

        /* Badges */
        var badges = '';
        if (work.readingDifficulty) {
            badges += '<span class="meta-badge">' + work.readingDifficulty + '</span>';
        }
        if (work.estimatedWordCount) {
            var wc = work.estimatedWordCount >= 1000
                ? Math.round(work.estimatedWordCount / 1000) + 'k words'
                : work.estimatedWordCount + ' words';
            badges += '<span class="meta-badge">~' + wc + '</span>';
        }
        if (D.modalMetaBadges) D.modalMetaBadges.innerHTML = badges;

        /* Summary */
        D.modalSummary.textContent = work.summary;

        /* Characters */
        if (work.keyCharacters && work.keyCharacters.length > 0) {
            D.modalCharactersSection.style.display = 'block';
            D.modalCharacters.innerHTML = work.keyCharacters.map(function (ch) {
                return '<div class="character-entry">' +
                    '<div class="character-name">' + ch.name + '</div>' +
                    '<div class="character-role">' + ch.role + '</div>' +
                '</div>';
            }).join('');
        } else {
            D.modalCharactersSection.style.display = 'none';
        }

        /* Themes */
        if (work.themes && work.themes.length > 0) {
            D.modalThemesSection.style.display = 'block';
            D.modalThemes.innerHTML = work.themes.map(function (t) {
                return '<span class="theme-tag">' + t + '</span>';
            }).join('');
        } else {
            D.modalThemesSection.style.display = 'none';
        }

        /* Concepts */
        var cc = ip ? 'plato-concept' : 'aristotle-concept';
        D.modalConcepts.innerHTML = (work.concepts || []).map(function (c) {
            return '<span class="modal-concept-chip ' + cc + '">' + c + '</span>';
        }).join('');

        /* Structure */
        if (work.structure) {
            D.modalStructureSection.style.display = 'block';
            D.modalStructure.textContent = work.structure;
        } else {
            D.modalStructureSection.style.display = 'none';
        }

        /* Primary Quote */
        var qp = (work.quote || '').split('\u2014');
        D.modalQuote.innerHTML = '\u201c' + qp[0].replace(/"/g, '').trim() + '\u201d' +
            (qp[1] ? '<cite>\u2014 ' + qp[1].trim() + '</cite>' : '');

        /* Extra Quotes */
        if (work.additionalQuotes && work.additionalQuotes.length > 0) {
            D.modalExtraQuotes.innerHTML = work.additionalQuotes.map(function (aq) {
                return '<blockquote class="extra-quote">\u201c' + aq.text + '\u201d' +
                    '<cite>' + aq.citation + '</cite></blockquote>';
            }).join('');
            D.modalExtraQuotes.style.display = 'block';
        } else {
            D.modalExtraQuotes.innerHTML = '';
            D.modalExtraQuotes.style.display = 'none';
        }

        /* Commentary */
        D.modalCommentary.innerHTML = (work.commentary || []).map(function (c) {
            return '<div class="commentary-entry">' +
                '<div class="commentary-philosopher">' + c.philosopher + '</div>' +
                '<p class="commentary-text">' + c.text + '</p>' +
            '</div>';
        }).join('');

        /* Modern Relevance */
        if (work.modernRelevance) {
            D.modalRelevanceSection.style.display = 'block';
            D.modalRelevance.textContent = work.modernRelevance;
        } else {
            D.modalRelevanceSection.style.display = 'none';
        }

        /* Context */
        D.modalContext.textContent = work.context;

        /* Related Works */
        if (work.relatedWorks && work.relatedWorks.length > 0) {
            D.modalRelatedSection.style.display = 'block';
            D.modalRelated.innerHTML = work.relatedWorks.map(function (rid) {
                var rw = W().find(function (x) { return x.id === rid; });
                if (!rw) return '';
                return '<button class="related-link" data-rid="' + rid + '">' +
                    rw.title + '</button>';
            }).join('');
            D.modalRelated.querySelectorAll('.related-link').forEach(function (btn) {
                btn.addEventListener('click', function () {
                    var ri = W().findIndex(function (x) { return x.id === btn.dataset.rid; });
                    if (ri !== -1) openModal(ri);
                });
            });
        } else {
            D.modalRelatedSection.style.display = 'none';
        }

        /* Show */
        D.modalOverlay.classList.add('active');
        D.modalOverlay.setAttribute('aria-hidden', 'false');
        D.body.classList.add('no-scroll');
        D.modalClose.focus();
        updateModalNav();
    }

    function closeModal() {
        D.modalOverlay.classList.remove('active');
        D.modalOverlay.setAttribute('aria-hidden', 'true');
        D.body.classList.remove('no-scroll');
        S.modalOpen = false;
        S.modalIdx = -1;
    }

    function updateModalNav() {
        var hp = S.modalIdx > 0;
        var hn = S.modalIdx < W().length - 1;
        if (D.modalPrev) {
            D.modalPrev.style.opacity = hp ? '1' : '0.3';
            D.modalPrev.style.pointerEvents = hp ? 'auto' : 'none';
        }
        if (D.modalNext) {
            D.modalNext.style.opacity = hn ? '1' : '0.3';
            D.modalNext.style.pointerEvents = hn ? 'auto' : 'none';
        }
    }

    function navModal(dir) {
        var ni = S.modalIdx + dir;
        if (ni >= 0 && ni < W().length) openModal(ni);
    }


    /* ══════════════════════════════════════
       TIMELINE
    ══════════════════════════════════════ */

    function renderTimeline() {
        if (!D.timelineTrack) return;
        var sorted = W().slice().sort(function (a, b) { return a.dateSort - b.dateSort; });

        D.timelineTrack.innerHTML = '<div class="timeline-line" aria-hidden="true"></div>';

        sorted.forEach(function (work) {
            var node = document.createElement('div');
            var cls = work.philosopher === 'plato' ? 'plato-node' : 'aristotle-node';
            node.className = 'timeline-node ' + cls;
            var gi = W().indexOf(work);
            node.setAttribute('role', 'button');
            node.setAttribute('tabindex', '0');
            node.innerHTML =
                '<span class="timeline-date">' + work.date + '</span>' +
                '<div class="timeline-dot"></div>' +
                '<span class="timeline-title">' + work.title + '</span>' +
                '<span class="timeline-author">' + (work.philosopher === 'plato' ? 'Plato' : 'Aristotle') + '</span>';
            node.addEventListener('click', function () { openModal(gi); });
            node.addEventListener('keydown', function (e) {
                if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); openModal(gi); }
            });
            D.timelineTrack.appendChild(node);
        });
    }

    function scrollTL(dir) {
        if (D.timelineContainer) {
            D.timelineContainer.scrollBy({ left: dir * 300, behavior: 'smooth' });
        }
    }


    /* ══════════════════════════════════════
       SCROLL OBSERVERS
    ══════════════════════════════════════ */

    function initObservers() {
        var fadeObs = new IntersectionObserver(function (entries) {
            entries.forEach(function (en) {
                if (en.isIntersecting) {
                    en.target.classList.add('visible');
                    fadeObs.unobserve(en.target);
                }
            });
        }, { threshold: 0.15, rootMargin: '0px 0px -30px 0px' });
        $$('.fade-in-element').forEach(function (el) { fadeObs.observe(el); });
    }


    /* ══════════════════════════════════════
       SHARE
    ══════════════════════════════════════ */

    function showToast(msg) {
        if (D.toastMessage) D.toastMessage.textContent = msg;
        D.toast.classList.add('active');
        setTimeout(function () { D.toast.classList.remove('active'); }, 2500);
    }

    function copyLink(url) {
        var u = url || window.location.href;
        if (navigator.clipboard) {
            navigator.clipboard.writeText(u).then(function () {
                showToast('Link copied');
            });
        } else {
            var ta = document.createElement('textarea');
            ta.value = u;
            ta.style.position = 'fixed';
            ta.style.opacity = '0';
            document.body.appendChild(ta);
            ta.select();
            document.execCommand('copy');
            document.body.removeChild(ta);
            showToast('Link copied');
        }
    }

    function shareTwitter(text) {
        var t = text || 'The Academy & The Lyceum \u2014 a complete works archive of Plato and Aristotle.';
        var url = 'https://twitter.com/intent/tweet?text=' +
            encodeURIComponent(t) + '&url=' + encodeURIComponent(window.location.href);
        window.open(url, '_blank', 'width=550,height=420');
    }

    function shareSite() {
        if (navigator.share) {
            navigator.share({
                title: 'The Academy & The Lyceum',
                text: 'A complete works archive of Plato and Aristotle.',
                url: window.location.href
            }).catch(function () {});
        } else {
            copyLink();
        }
    }


    /* ══════════════════════════════════════
       MOBILE NAV
    ══════════════════════════════════════ */

    function toggleMenu() {
        S.menuOpen = !S.menuOpen;
        D.hamburger.classList.toggle('active', S.menuOpen);
        D.hamburger.setAttribute('aria-expanded', S.menuOpen);
        D.mobileNavOverlay.classList.toggle('active', S.menuOpen);
        D.mobileNavOverlay.setAttribute('aria-hidden', !S.menuOpen);
        D.body.classList.toggle('no-scroll', S.menuOpen);
    }

    function closeMenu() {
        S.menuOpen = false;
        D.hamburger.classList.remove('active');
        D.hamburger.setAttribute('aria-expanded', 'false');
        D.mobileNavOverlay.classList.remove('active');
        D.mobileNavOverlay.setAttribute('aria-hidden', 'true');
        D.body.classList.remove('no-scroll');
    }

    function toggleMobileSearch() {
        S.searchOpen = !S.searchOpen;
        D.mobileSearchBar.classList.toggle('active', S.searchOpen);
        if (S.searchOpen) D.mobileSearchInput.focus();
    }

    function closeMobileSearch() {
        S.searchOpen = false;
        D.mobileSearchBar.classList.remove('active');
    }


    /* ══════════════════════════════════════
       SCROLL
    ══════════════════════════════════════ */

    function onScroll() {
        var y = window.scrollY;
        if (D.navbar) D.navbar.classList.toggle('scrolled', y > 40);
        if (D.backToTop) D.backToTop.classList.toggle('visible', y > 500);
    }


    /* ══════════════════════════════════════
       CARD EVENTS
    ══════════════════════════════════════ */

    function bindCardEvents() {
        $$('.work-card').forEach(function (card) {
            card.addEventListener('click', function () {
                openModal(parseInt(card.dataset.index));
            });
            card.addEventListener('keydown', function (e) {
                if (e.key === 'Enter' || e.key === ' ') {
                    e.preventDefault();
                    openModal(parseInt(card.dataset.index));
                }
            });
        });
    }


    /* ══════════════════════════════════════
       BIND ALL EVENTS
    ══════════════════════════════════════ */

    function bindEvents() {
        if (D.themeToggle) D.themeToggle.addEventListener('click', toggleTheme);
        if (D.hamburger) D.hamburger.addEventListener('click', toggleMenu);
        D.mobileNavLinks.forEach(function (l) { l.addEventListener('click', closeMenu); });
        if (D.searchToggle) D.searchToggle.addEventListener('click', toggleMobileSearch);
        if (D.mobileSearchClose) D.mobileSearchClose.addEventListener('click', closeMobileSearch);
        if (D.mobileSearchInput) D.mobileSearchInput.addEventListener('input', handleSearch);
        if (D.searchInput) D.searchInput.addEventListener('input', handleSearch);
        if (D.searchClear) D.searchClear.addEventListener('click', clearSearch);

        D.filterTabs.forEach(function (t) {
            t.addEventListener('click', function () { setFilter(t.dataset.filter); });
        });
        D.categoryChips.forEach(function (c) {
            c.addEventListener('click', function () { setCategory(c.dataset.category); });
        });
        if (D.clearFiltersBtn) D.clearFiltersBtn.addEventListener('click', clearAll);

        if (D.modalClose) D.modalClose.addEventListener('click', closeModal);
        if (D.modalOverlay) D.modalOverlay.addEventListener('click', function (e) {
            if (e.target === D.modalOverlay) closeModal();
        });
        if (D.modalPrev) D.modalPrev.addEventListener('click', function () { navModal(-1); });
        if (D.modalNext) D.modalNext.addEventListener('click', function () { navModal(1); });

        if (D.modalShareTwitter) {
            D.modalShareTwitter.addEventListener('click', function () {
                var w = W()[S.modalIdx];
                if (w) {
                    shareTwitter(w.title + ' by ' + (w.philosopher === 'plato' ? 'Plato' : 'Aristotle') + ' — The Academy & The Lyceum.');
                }
            });
        }

        if (D.modalCopyLink) {
            D.modalCopyLink.addEventListener('click', function () {
                var w = W()[S.modalIdx];
                if (w) {
                    copyLink(window.location.href + '#' + w.id);
                }
            });
        }
        if (D.shareBtn) D.shareBtn.addEventListener('click', shareSite);
        if (D.footerShareTwitter) D.footerShareTwitter.addEventListener('click', function () { shareTwitter(); });
        if (D.footerCopyLink) D.footerCopyLink.addEventListener('click', function () { copyLink(); });

        if (D.timelinePrev) D.timelinePrev.addEventListener('click', function () { scrollTL(-1); });
        if (D.timelineNext) D.timelineNext.addEventListener('click', function () { scrollTL(1); });

        if (D.backToTop) D.backToTop.addEventListener('click', function () {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });

        window.addEventListener('scroll', onScroll, { passive: true });

        document.addEventListener('keydown', function (e) {
            if (e.key === 'Escape') {
                if (S.modalOpen) closeModal();
                else if (S.menuOpen) closeMenu();
                else if (S.searchOpen) closeMobileSearch();
            }
            if (S.modalOpen) {
                if (e.key === 'ArrowLeft') navModal(-1);
                if (e.key === 'ArrowRight') navModal(1);
            }
            if (e.key === '/' && !S.modalOpen) {
                e.preventDefault();
                if (D.searchInput) D.searchInput.focus();
            }
        });

        D.footerFilterLinks.forEach(function (link) {
            link.addEventListener('click', function (e) {
                e.preventDefault();
                var cat = link.dataset.filterLink;
                var sec = $('#searchSection');
                if (sec) {
                    sec.scrollIntoView({ behavior: 'smooth' });
                    setTimeout(function () { setCategory(cat); }, 400);
                }
            });
        });

        $$('a[href^="#"]').forEach(function (a) {
            a.addEventListener('click', function (e) {
                var tid = a.getAttribute('href');
                if (tid === '#') return;
                var tgt = document.querySelector(tid);
                if (tgt) {
                    e.preventDefault();
                    var off = parseInt(getComputedStyle(D.html).getPropertyValue('--nav-h')) || 64;
                    var y = tgt.getBoundingClientRect().top + window.scrollY - off - 16;
                    window.scrollTo({ top: y, behavior: 'smooth' });
                }
            });
        });
    }


    /* ══════════════════════════════════════
       LAUNCH
    ══════════════════════════════════════ */

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

})();
