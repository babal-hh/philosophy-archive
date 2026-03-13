/* ================================================================
   DATA PART 13c — Theodicy + New System of Nature (Leibniz)
   ================================================================ */

window.WORKS.push(

/* ──────────────────────────────────────
   1. THEODICY
────────────────────────────────────── */
{
    id: 'theodicy',
    title: 'Theodicy',
    greekTitle: "Essais de Théodicée sur la bonté de Dieu, la liberté de l'homme et l'origine du mal",
    philosopher: 'leibniz',
    category: 'practical',
    categoryLabel: 'Theology & Ethics',
    date: '1710 AD',
    dateSort: 1710,
    emoji: '⚡',
    cardSize: 'normal',
    readingDifficulty: 'Advanced',
    estimatedWordCount: 160000,

    shortDesc: 'The only book Leibniz published under his own name — a systematic defence of divine goodness against the problem of evil that invented the word "theodicy" and gave Voltaire his target in Candide.',

    summary: 'The Theodicy is the only book-length work Leibniz published in his own name during his lifetime, and it is the most ambitious attempt in the history of philosophy to reconcile the existence of evil with the goodness, power, and knowledge of God. The word "theodicy" — justification of God — was coined by Leibniz for this work, and it has named a genre of philosophical theology ever since. The work grew out of conversations with Queen Sophie Charlotte of Prussia, who had been disturbed by the arguments of Pierre Bayle, who had argued in his Dictionnaire that the existence of evil is rationally irreconcilable with a good and omnipotent God — and that faith therefore requires a complete surrender of reason.\n\nLeibniz\'s response is systematic and multi-fronted. Against Bayle\'s fideism he argues that reason and faith cannot genuinely conflict, because God is the author of both the natural order and revelation. Against the logical problem of evil he distinguishes three kinds of evil — metaphysical evil (the necessary imperfection of finite creatures), physical evil (pain and suffering), and moral evil (sin) — and argues that each kind can be reconciled with divine perfection. God permits physical and moral evil because the best possible world, by its own internal logic, requires certain imperfections as conditions of greater goods. A world without the possibility of sin would be a world without genuine freedom; a world without physical suffering might be a world with less beauty, less courage, less moral development.\n\nThe Theodicy concludes with a retelling of Valla\'s dialogue on free will and fate, framed within the fiction of a visit to the palace of destinies — one of the most beautiful literary passages Leibniz ever wrote — in which the mortal Sextus Tarquinius visits God\'s palace and sees all possible versions of his own life laid out before the moment of creation.',

    themes: ['The Problem of Evil', 'Divine Goodness and Omnipotence', 'Human Freedom and Divine Foreknowledge', 'The Best Possible World', 'Sin and Divine Permission', 'Faith and Reason', 'Metaphysical Necessity', 'Theodicy as Philosophical Genre'],

    keyCharacters: [
        { name: 'Pierre Bayle', role: 'The principal antagonist — Leibniz engages throughout with his skeptical arguments from the Dictionnaire historique et critique that evil is rationally irreconcilable with a good God' },
        { name: 'Queen Sophie Charlotte', role: 'The interlocutor in the conversations that gave rise to the Theodicy; her philosophical seriousness prompted Leibniz to develop the arguments at full length' },
        { name: 'Sextus Tarquinius', role: 'The protagonist of the closing myth of Theodorus — who visits the palace of destinies and sees all possible versions of his own life laid out in God\'s mind before creation' }
    ],

    concepts: [
        'Theodicy — justification of God\'s goodness in the face of evil; a term Leibniz coined that has since named the entire genre',
        'Three kinds of evil — metaphysical evil (necessary imperfection of finite things), physical evil (suffering), moral evil (sin); each reconcilable with divine perfection on different grounds',
        'Antecedent vs consequent will — God wills the good of each creature antecedently but wills the best world overall consequently, even if that world contains some suffering',
        'Permissive will — God permits evil without directly willing it, because preventing it would require a less perfect world',
        'Middle knowledge (scientia media) — God\'s knowledge of what free creatures would do in any possible situation, prior to any decision about which creatures to create',
        'The palace of destinies — the fictional space in God\'s mind where all possible worlds exist before creation; the literary climax of the Theodicy'
    ],

    structure: 'Preliminary dissertation: On the conformity of faith with reason\nPart I: On divine goodness and the origin of evil (against Bayle\'s fideism)\nPart II: On the goodness of God and the freedom of man\nPart III: On the permission of evil and divine foreknowledge\nAppendix: The Cause of God; Remarks on King; The Myth of Theodorus',

    quote: 'God has chosen the best of all possible worlds; but this does not make the world necessary. The world could have been otherwise — an infinity of other worlds were possible in the divine understanding. But none was better. The evil we observe is the price of a greater good that a different arrangement would have sacrificed.',

    additionalQuotes: [
        { text: 'Metaphysical evil consists simply in imperfection, physical evil in suffering, and moral evil in sin.', citation: 'Theodicy §21' },
        { text: 'Those who are not satisfied with the conduct of God are like the soldiers who murmur against their general without knowing his plans.', citation: 'Theodicy §134' },
        { text: 'If God had wished to do only things of the highest perfection, he would not have created the world at all, since nothing created can equal him.', citation: 'Theodicy §31' }
    ],

    commentary: [
        {
            philosopher: 'Voltaire',
            text: 'Voltaire\'s Candide (1759) is the most consequential literary response to any philosophical work in the Western tradition. Published in the wake of the Lisbon earthquake of 1755 — which killed between 30,000 and 60,000 people on All Saints Day while the faithful were at mass — Candide devastated the Theodicy\'s popular reputation by reducing "the best of all possible worlds" to a catchphrase of absurd complacency. Dr. Pangloss — the perpetually optimistic Leibnizian philosopher who maintains, through every disaster, that all is for the best in the best of all possible worlds — became one of the most recognizable comic characters in European literature, and Leibniz became synonymous with rationalist evasion of obvious suffering. Voltaire\'s philosophical critique was less subtle than his satire: he essentially argued that the Lisbon earthquake refuted the Theodicy by direct empirical counterexample. Most Leibniz scholars regard this as a misreading — the Theodicy does not claim that this world contains no evil, only that it contains less evil than any alternative — but Voltaire\'s demolition was culturally decisive.'
        },
        {
            philosopher: 'G.W.F. Hegel',
            text: 'Hegel\'s response to Voltaire\'s demolition of the Theodicy was characteristically dialectical: Leibniz\'s theodicy is, despite the mockery, the most serious philosophical attempt to think the rationality of history. That the real is rational is not an optimistic prejudice but a metaphysical claim about the structure of existence. What the Theodicy gets right is the demand that philosophy justify the ways of the world — that the apparent irrationality of suffering, injustice, and evil be comprehended within a rational framework rather than simply lamented. What it gets wrong is the framework itself: the best of all possible worlds is a static conception, a world selected from a menu of alternatives rather than a world that develops through the dialectical negation of its own limitations. Hegel\'s own philosophy of history — in which the Cunning of Reason works through human passions and historical catastrophe toward the realization of freedom — is his answer to the same problem the Theodicy attempted to solve.'
        },
        {
            philosopher: 'Susan Neiman',
            text: 'Neiman\'s Evil in Modern Thought: An Alternative History of Philosophy (2002) placed the Theodicy at the watershed of modern intellectual history. The Lisbon earthquake of 1755 did not just kill tens of thousands; it destroyed the Leibnizian framework within which educated Europeans had understood evil. Before Lisbon, natural evil and moral evil could be integrated into a single providential narrative: suffering was punishment, trial, or occasion for moral growth. After Lisbon — and after Auschwitz — this integration became intolerable. The Theodicy was the last serious attempt to read both natural and moral evil within a single rational-theological framework, and its destruction by the earthquake marks the beginning of the modern experience of evil as genuinely inexplicable: not a problem to be solved but a reality to be confronted.'
        },
        {
            philosopher: 'Alvin Plantinga',
            text: 'Plantinga\'s free will defense — the most influential analytic response to the logical problem of evil — is explicitly built on Leibnizian foundations. Plantinga saw the logical structure of the problem of evil more clearly than anyone before him. His three-fold distinction between kinds of evil and his recognition that a perfect God need not create a world without evil — because no such world may be achievable without sacrificing greater goods, including genuine creaturely freedom — remain the starting points for contemporary analytic theodicy. Plantinga\'s key technical contribution was formalizing Leibniz\'s insight: it may not be within God\'s power to create free creatures who always choose rightly; even an omnipotent God cannot actualize a possible world that is both populated by genuinely free creatures and wholly free of moral evil, because the freedom of creatures is partly outside God\'s control.'
        }
    ],

    modernRelevance: 'The Theodicy\'s central question — whether the existence of evil is compatible with an omniscient, omnipotent, and benevolent God — remains the most actively debated question in philosophy of religion. Plantinga\'s free will defense, Hick\'s soul-making theodicy, and the entire literature on the logical and evidential problems of evil are continuations of the debate Leibniz and Bayle staged in 1710. The word "theodicy" itself has become indispensable in every language it has entered, naming a philosophical problem that shows no sign of resolution.',

    context: 'Published in Amsterdam in 1710, an immediate success that went through several editions in Leibniz\'s lifetime — the only work he published that did. Its philosophical legacy was transformed by the Lisbon earthquake of 1 November 1755 and Voltaire\'s Candide (1759), which made "best of all possible worlds" synonymous with complacent indifference to suffering. Only in the twentieth century, with the rehabilitation of Leibniz\'s metaphysics more broadly, has the Theodicy been read again as the serious philosophical work it is.',

    relatedWorks: ['monadology', 'discourse-metaphysics', 'new-essays', 'correspondence-clarke']
},

/* ──────────────────────────────────────
   2. NEW SYSTEM OF NATURE
────────────────────────────────────── */
{
    id: 'new-system-nature',
    title: 'New System of Nature',
    greekTitle: 'Système nouveau de la nature et de la communication des substances',
    philosopher: 'leibniz',
    category: 'metaphysics',
    categoryLabel: 'Metaphysics',
    date: '1695 AD',
    dateSort: 1695,
    emoji: '⚙',
    cardSize: 'normal',
    readingDifficulty: 'Intermediate',
    estimatedWordCount: 12000,

    shortDesc: 'The public debut of pre-established harmony — the first text in which Leibniz revealed to the world his solution to the mind-body problem, presenting his intellectual autobiography and his alternative to Cartesian dualism, occasionalism, and Spinozist monism.',

    summary: 'The New System of Nature, published in the Journal des savants in June 1695, marks a turning point in the public reception of Leibniz\'s philosophy. For nearly a decade after composing the Discourse on Metaphysics and the Arnauld correspondence, Leibniz had published nothing substantial on his metaphysics. The New System broke this silence with a deliberately provocative statement of his theory of pre-established harmony — the doctrine that God has coordinated the perceptions and appetitions of all substances at creation so that they correspond perfectly to one another without any causal interaction.\n\nThe essay traces Leibniz\'s intellectual autobiography: his early enthusiasm for mechanism and the corpuscular philosophy, his growing dissatisfaction with Cartesian dualism (which could not explain how mind and body interact), his rejection of Malebranche\'s occasionalism (which required God to intervene at every moment), and his rejection of Spinoza\'s parallelism (which denied genuine individuality to substances). The pre-established harmony is presented as the solution to all these difficulties: each substance follows its own internal program, established at creation, and the perfect correspondence between substances is guaranteed by God\'s original design.\n\nThe essay generated enormous controversy. Bayle, Foucher, and others responded in print, and Leibniz published several clarifications in subsequent issues of the Journal des savants. These exchanges forced him to articulate the doctrine with a precision absent from the Discourse and the Arnauld letters.',

    themes: ['Pre-established Harmony', 'Mind-Body Problem', 'Critique of Cartesian Dualism', 'Critique of Occasionalism', 'Critique of Spinozist Parallelism', 'Substantial Forms Rehabilitated', 'Intellectual Autobiography'],

    keyCharacters: [
        { name: 'Pierre Bayle', role: 'The most important critic — his brilliantly hostile analysis in the Dictionnaire forced Leibniz to develop his defence of harmony far beyond the original essay' },
        { name: 'Simon Foucher', role: 'The first critic to respond in print — raised the problem of how God could coordinate substances without causal interaction' }
    ],

    concepts: [
        'Pre-established harmony — the perfect coordination of all substances by God at creation; the world as a collection of synchronized clocks, wound once and never touched again',
        'Substance as self-sufficient — each substance contains within itself the complete principle of all its changes; nothing can enter it from outside',
        'Rejection of influxus physicus — there is no genuine causal flow between substances; all apparent interaction is really parallel expression',
        'Rejection of occasionalism — God does not intervene at every moment; the harmony was established once at creation, preserving divine perfection and natural order alike',
        'Substantial form as principle of unity — Leibniz rehabilitates Aristotelian form against Cartesian mechanism to account for the genuine unity of substances'
    ],

    structure: 'Part 1: Leibniz\'s intellectual development — from mechanism to substantial forms\nPart 2: The problem of mind-body interaction — why dualism, occasionalism, and Spinozism all fail\nPart 3: The solution: pre-established harmony\nClarifications (1695–1696): Replies to Foucher, Bayle, and other critics in the Journal des savants',

    quote: 'I was forced to have recourse to what might be called a pre-established harmony. According to this system, substances were created from the beginning in such a way that, each following its own laws which it received with its being, they should nevertheless agree with each other, just as though there were mutual influence or as though God in addition to his general cooperation were forever interfering. — New System of Nature (1695)',

    additionalQuotes: [
        { text: 'Why should God not be able to give to substance from the beginning a nature or internal force that could produce in it, in due order, everything that would happen to it?', citation: 'New System of Nature (1695)' }
    ],

    commentary: [
        {
            philosopher: 'Pierre Bayle',
            text: 'Bayle\'s entry on "Rorarius" in the Dictionnaire historique et critique (1697) subjected the New System to the most penetrating early critique. His central objection was that Leibniz\'s pre-established harmony was more miraculous than the occasionalism it replaced: at least Malebranche\'s God intervened moment by moment in a comprehensible sequence of acts; Leibniz\'s God performed a single act of infinite complexity at creation, pre-programming an infinite number of substances to correspond perfectly for all eternity. The hypothesis avoids ongoing miracles only by concentrating the miraculous into a single incomprehensibly complex initial act. Bayle considered this ingenious but self-defeating: the pre-established harmony is, he wrote, the most extravagant hypothesis ever conceived — "the system of occasional causes is infinitely simpler." Leibniz\'s sustained engagement with Bayle\'s objections in his clarifications and later in the Theodicy significantly advanced the precision of his own position.'
        }
    ],

    modernRelevance: 'The New System\'s argument against causal interaction between mental and physical substances prefigures the contemporary problem of mental causation — how can consciousness, if it is non-physical, cause physical effects? The pre-established harmony, stripped of its theological framework, resembles contemporary epiphenomenalist and parallelist positions in philosophy of mind. The essay\'s structure — surveying and rejecting all available solutions before presenting one\'s own — has become a standard method in philosophical argumentation.',

    context: 'Published in the Journal des savants in June 1695 — the premier learned periodical in Europe. The resulting controversy, especially Bayle\'s hostile entry in the Dictionnaire, kept Leibniz\'s pre-established harmony at the centre of European philosophical debate for two decades and effectively established his reputation as a systematic metaphysician rather than merely a mathematician and diplomat.',

    relatedWorks: ['monadology', 'discourse-metaphysics', 'correspondence-arnauld', 'theodicy']
}

);
