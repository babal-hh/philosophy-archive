#!/usr/bin/env python3
"""
Run from inside ~/Desktop/philosophy-archive/
  python3 generate_leibniz_full.py
Writes js/data-13a.js through js/data-13e.js
Overwrites whatever is there.
"""
import os

js_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'js')
os.makedirs(js_dir, exist_ok=True)

# ─────────────────────────────────────────────────────────────────────────────
# DATA-13a  —  Monadology
# ─────────────────────────────────────────────────────────────────────────────
data_13a = r"""/* ================================================================
   DATA PART 13a — Monadology (Leibniz)
   ================================================================ */

window.WORKS.push(

{
    id: 'monadology',
    title: 'Monadology',
    greekTitle: 'La Monadologie',
    philosopher: 'leibniz',
    category: 'metaphysics',
    categoryLabel: 'Metaphysics',
    date: '1714 AD',
    dateSort: 1714,
    emoji: '◉',
    cardSize: 'wide',
    readingDifficulty: 'Advanced',
    estimatedWordCount: 8000,

    shortDesc: 'Ninety paragraphs that contain an entire universe — Leibniz\'s final and most compressed statement of his metaphysics of simple, windowless, perception-bearing substances, each mirroring the whole cosmos from its own unique point of view.',

    summary: 'The Monadology is the most concentrated philosophical text of the early modern period. Written in French in 1714, the last year of Leibniz\'s active philosophical life, its ninety numbered paragraphs unfold an entire cosmology from a single premise: the ultimate constituents of reality are not extended material atoms but simple, indivisible, non-spatial substances called monads, each of which is a centre of perception and appetite. No monad acts on any other — they are "windowless," sealed from external influence — yet all monads perceive the entire universe from their own unique perspective, each mirroring the whole from a different point of view. This universal mirroring is not accidental: God has pre-established a perfect harmony among all monads so that the perceptions of each correspond exactly to the states of all others, without any causal interaction between them. The universe is thus an infinite collection of living mirrors, each expressing the whole, coordinated by a divine harmony that Leibniz identifies as the sufficient reason for the world\'s existence.\n\nThe Monadology builds systematically through a series of arguments: from the existence of simple substances (since composites exist and composites require simples), to their lack of windows (since simple substances have no parts through which anything could enter or leave), to their internal principle of change (appetite), to the hierarchy of monads from bare perception through animal souls to rational minds, to God as the supreme monad whose existence is demonstrated by the argument from sufficient reason and the ontological argument. The pre-established harmony is then introduced to explain apparent interaction between body and soul without the occasionalist resort to perpetual divine intervention and without the parallelism of Spinoza\'s attribute identity.\n\nThe work\'s brevity is deceptive. Every paragraph condenses arguments developed at length in the Discourse on Metaphysics, the correspondence with Arnauld, the New System of Nature, and the New Essays. Reading the Monadology without that background is like reading a proof without its lemmas. With it, the text opens into one of the most ambitious and coherent metaphysical systems in the history of philosophy — a system that influenced Kant deeply, that Hegel regarded as the necessary precursor to his own philosophy of spirit, and that Bertrand Russell devoted his first major philosophical book to attacking.',

    themes: ['Substance as Perception', 'Pre-established Harmony', 'Sufficient Reason', 'Possible Worlds', 'The Best of All Possible Worlds', 'God and Creation', 'Hierarchy of Souls', 'Unity and Multiplicity', 'Expression and Mirroring', 'Teleology'],

    keyCharacters: [
        { name: 'God', role: 'The supreme monad — the only necessary being, the ground of all contingent existence, the author of pre-established harmony, and the monarch of the kingdom of grace' },
        { name: 'Finite Monads', role: 'Created substances ranging from bare monads (with only confused perception) through animal souls (with memory and feeling) to rational minds (with apperception and self-knowledge)' }
    ],

    concepts: [
        'Monad — simple substance without parts, without extension, without windows; the ultimate constituent of reality',
        'Perception — the representation of the many in the one, present in all monads to varying degrees of clarity',
        'Apperception — reflective self-awareness, the perception of perception; present only in rational minds',
        'Appetite — the internal principle of change driving each monad from one perceptual state to the next',
        'Pre-established harmony — God\'s coordination of all monads at creation so that each mirrors all others without causal interaction',
        'Principle of sufficient reason — nothing happens without a reason why it is thus and not otherwise',
        'Principle of contradiction — the foundation of all necessary truths; the opposite of a necessary truth is impossible',
        'Truths of reason vs truths of fact — necessary truths (whose opposite is impossible) vs contingent truths (which require sufficient reason)',
        'The best of all possible worlds — God selects, from among an infinity of possible worlds, the one with the greatest perfection',
        'Kingdom of grace within the kingdom of nature — rational souls as citizens of God\'s moral republic, governed by final causes within the mechanical order'
    ],

    structure: '§1–6: The existence and nature of simple substances — why there must be simples if there are composites\n§7–16: Monads are windowless; perception and appetite as their only properties; the hierarchy of perception\n§17–30: The famous mill argument against materialism; the self-consciousness of rational minds; the existence of God\n§31–48: Principles of sufficient reason and contradiction; necessary and contingent truths; God as the sufficient reason of all things\n§49–60: God as the source of monads; creation and emanation; pre-established harmony introduced\n§61–81: The pre-established harmony of soul and body; the two kingdoms\n§82–90: The kingdom of grace; God as the monarch of minds; the highest blessedness',

    quote: 'The monad has no windows through which anything could enter or depart. Accidents cannot detach themselves from substances and wander outside of them, as the sensible species of the scholastics used to do. Thus neither substance nor accident can enter a monad from outside. — Monadology §7',

    additionalQuotes: [
        { text: 'Each monad is a living mirror, or a mirror endowed with internal action, which represents the universe according to its own point of view.', citation: 'Monadology §56' },
        { text: 'God alone is the primitive unity or the original simple substance; all created or derivative monads are produced by continual fulgurations of the Divinity.', citation: 'Monadology §47' },
        { text: 'Nothing takes place without sufficient reason; that is, nothing happens without it being possible for someone who has enough knowledge of things to give a reason sufficient to determine why it is thus and not otherwise.', citation: 'Monadology §32' },
        { text: 'The present is pregnant with the future.', citation: 'Monadology §22' }
    ],

    commentary: [
        {
            philosopher: 'Immanuel Kant',
            text: 'Kant\'s engagement with the Monadology is deep and complex. He accepted Leibniz\'s insight that simple substances must underlie all composites — his own pre-critical Monadologia Physica (1756) defended a version of monads against the Newtonians. But the critical philosophy of 1781 reversed this: Leibniz, Kant argued, had intellectualised appearances. He treated the sensible world as a confused perception of an intelligible world of monads, failing to recognise that sensibility has its own irreducible forms — space and time — that are not simply confused intellectual representations but the pure forms of outer and inner intuition. The windowless monads, each containing within itself a confused representation of the whole universe, become in Kant\'s hands a system that confuses the transcendental with the empirical: what is really a formal condition of experience is taken by Leibniz for a property of things in themselves.'
        },
        {
            philosopher: 'G.W.F. Hegel',
            text: 'Hegel regarded the Monadology as the first genuine philosophy of individuality in modern thought. The monad — as the self-specifying universal that mirrors the whole from a unique perspective — anticipates the structure of spirit: the Notion that differentiates itself into particulars while remaining identical with itself. But Hegel\'s critique is equally sharp: the pre-established harmony remains external and theological where it should be internal and dialectical. For Hegel, the correspondence between monads should not require a God who sets the clocks at creation; it should be internal to the nature of substance itself, arising through the dialectical self-development of the Notion. The Monadology gets the form of the solution right — individual substance as expression of the universal — but supplies the wrong content, replacing genuine dialectical necessity with divine mechanism.'
        },
        {
            philosopher: 'Bertrand Russell',
            text: 'Russell\'s A Critical Exposition of the Philosophy of Leibniz (1900) — his first major book — argued that the Monadology was a system of consistent and connected metaphysical propositions, each following from premises of the most abstract and general kind. Its failure is not internal inconsistency but the falsity of its premises — above all the subject-predicate logic that generates the whole apparatus of windowless substances. Because Leibniz assumed that every proposition has the form "S is P" and that the predicate must be contained in the subject, he was led to the complete concept theory and from there to monads, pre-established harmony, and the denial of genuine relations between substances. Russell\'s own logic — in which relations are irreducible and not analysable into predications about their relata — directly refutes the logical foundations of the Monadology. The book launched the analytic tradition\'s critical engagement with Leibniz that continues to this day.'
        },
        {
            philosopher: 'Gilles Deleuze',
            text: 'Deleuze\'s The Fold: Leibniz and the Baroque (1988) is the most philosophically creative twentieth-century reading of the Monadology. Deleuze argued that the key concept is not the monad but the fold: the monad has no windows but it has folds — an infinity of pleats and envelopes through which the world is expressed in each monad without being opened to it. The Baroque — the aesthetic of infinite complication, of drapery that multiplies without end, of façades that have no stable inside or outside — is the architectural expression of Leibniz\'s metaphysics. More technically, Deleuze argued that Leibniz\'s calculus and his metaphysics share the same mathematical structure: the differential, the infinitesimal, the fold are the same concept operating at different levels. The monad does not mirror the world through a window but through an internal inflection — an infinite convergent series that approaches the world without ever being identical with it.'
        },
        {
            philosopher: 'Martin Heidegger',
            text: 'Heidegger\'s lectures on Leibniz — particularly "The Metaphysical Foundations of Logic" (1928) and "The Principle of Reason" (1955-56) — treated the Monadology as the culmination of early modern metaphysics and the clearest expression of what Heidegger called the principle of reason: the demand that everything that is must have a sufficient ground for being what it is. With Leibniz, the question of why there is something rather than nothing becomes for the first time a genuine metaphysical question — the fundamental question that opens metaphysics as such. His answer through sufficient reason is a determination of being as ground: being is what provides the ratio, the account, the foundation. Heidegger saw in this the decisive step toward the modern technological world in which everything is required to justify itself, to render its ratio, to be accountable — a world in which being is nothing but the being of what has been grounded.'
        }
    ],

    modernRelevance: 'The Monadology\'s central claim — that experience is perspectival, that each perceiving subject represents the whole world from its own unique point of view — resonates through phenomenology, philosophy of mind, and contemporary discussions of consciousness. The principle of sufficient reason continues to structure debates in metaphysics and philosophy of science about the demand for explanation. Most influentially, Leibniz\'s notion of possible worlds — that God selects among an infinity of compossible world-histories — was formalized by Saul Kripke and David Lewis into possible worlds semantics, which now underlies modal logic, the logic of counterfactuals, and discussions of metaphysical necessity and contingency across all of analytic philosophy. The de re / de dicto distinction, the semantics of conditionals, and the logic of belief and knowledge all operate within the formal framework Leibniz\'s possible worlds thinking made possible.',

    context: 'Leibniz wrote the Monadology in Vienna in 1714 at the age of 68, apparently as a summary of his philosophy for Prince Eugene of Savoy. He composed it rapidly and it remained unpublished during his lifetime; it was first published in German translation in 1720 and in the original French only in 1840. By 1714 Leibniz was politically marginalized — passed over for the position of imperial librarian, excluded from accompanying the Hanoverian court to London after George I\'s accession to the British throne — and was working in increasing isolation. He died in 1716, reportedly attended only by his secretary; the Berlin Academy of Sciences, which he had founded, did not mark his death.',

    relatedWorks: ['discourse-metaphysics', 'new-essays', 'correspondence-arnauld', 'theodicy']
}

);
"""

# ─────────────────────────────────────────────────────────────────────────────
# DATA-13b  —  Discourse on Metaphysics + Principles of Nature and Grace
# ─────────────────────────────────────────────────────────────────────────────
data_13b = r"""/* ================================================================
   DATA PART 13b — Discourse on Metaphysics + Principles of Nature and Grace
   ================================================================ */

window.WORKS.push(

/* ──────────────────────────────────────
   1. DISCOURSE ON METAPHYSICS
────────────────────────────────────── */
{
    id: 'discourse-metaphysics',
    title: 'Discourse on Metaphysics',
    greekTitle: 'Discours de métaphysique',
    philosopher: 'leibniz',
    category: 'metaphysics',
    categoryLabel: 'Metaphysics',
    date: '1686 AD',
    dateSort: 1686,
    emoji: '✦',
    cardSize: 'normal',
    readingDifficulty: 'Advanced',
    estimatedWordCount: 22000,

    shortDesc: 'The first full statement of Leibniz\'s mature metaphysics — thirty-seven articles on individual substance, the complete concept, divine perfection, and the foundations of truth, written at white heat in 1686 and not published until 160 years later.',

    summary: 'The Discourse on Metaphysics, written in 1686 but not published until 1846, is the earliest complete statement of Leibniz\'s mature philosophical system and one of the great documents of seventeenth-century metaphysics. Written at the age of 39 in a white heat of philosophical productivity, it was sent in summary form to the theologian Antoine Arnauld, whose devastating objections generated one of the most important philosophical correspondences in history. The Discourse proceeds through thirty-seven articles that move from the nature of God and divine perfection through the theory of individual substance to the nature of truth, causation, the soul-body relation, and the conditions of human freedom and grace.\n\nThe pivotal doctrine is the complete concept theory of individual substance: the concept of any individual substance — Caesar, for example — contains as predicates all the truths that will ever be true of that individual. From this follows the principle of the identity of indiscernibles (no two distinct substances can share all their properties), the denial of genuine causal interaction between substances, and the doctrine that God creates individuals by selecting, from among infinitely many possible individuals, the compossible set that constitutes the best possible world. The Discourse also contains Leibniz\'s first sustained engagement with Cartesian physics — he rejects conservation of quantity of motion in favour of conservation of force — and his first clear statement of the principle that perception, not extension, is the mark of genuine substance.',

    themes: ['Individual Substance', 'The Complete Concept', 'Divine Perfection', 'Truth and Predication', 'Causation and Occasionalism', 'Soul and Body', 'Human Freedom', 'Grace and Nature', 'Vis Viva'],

    keyCharacters: [
        { name: 'Caesar', role: 'The philosophical example that dramatizes the complete concept doctrine — his concept contains the predicate "will cross the Rubicon" eternally, prior to any act' },
        { name: 'Antoine Arnauld (anticipated)', role: 'The correspondent who received the summary and whose shock at article 13 initiated the most rigorous philosophical exchange of the century' }
    ],

    concepts: [
        'Complete concept — the individual concept of a substance contains all its predicates past, present, and future; to know the complete concept is to know the whole life of the individual',
        'Identity of indiscernibles — no two substances are perfectly alike; if two things share all properties they are the same thing',
        'Compossibility — possible individuals that can coexist in the same possible world without contradiction',
        'Vis viva — living force, the true conserved quantity in physics (proportional to mv²); Leibniz\'s refutation of Descartes\'s conservation of quantity of motion',
        'Substantial form rehabilitated — the scholastic concept of form, dismissed by Cartesian mechanism, is necessary to account for the genuine unity of substances',
        'Concomitance — what appears to be causation between substances is really the expression of pre-established correspondence, not genuine influx',
        'Freedom as spontaneity — acting from one\'s own complete concept rather than from external compulsion; freedom is not indeterminism but self-determination'
    ],

    structure: '§1–7: God and divine perfection; the nature of substance\n§8–16: The complete concept of individual substance; truth as predicate-inclusion; the identity of indiscernibles\n§17–22: God as the cause of the world; occasionalism critiqued; expression\n§23–29: Soul and body; perception; the rehabilitation of substantial forms\n§30–37: Freedom, grace, sin, and the rational soul\'s relation to God',

    quote: 'It is the nature of an individual substance or of a complete being to have a concept so complete that it is sufficient to make us understand and deduce from it all the predicates of the subject to which this concept is attributed. — Discourse on Metaphysics §8',

    additionalQuotes: [
        { text: 'God has chosen the most perfect world, that is to say, the one which is at the same time the simplest in hypotheses and the richest in phenomena.', citation: 'Discourse on Metaphysics §6' },
        { text: 'Every individual substance expresses the whole universe in its own manner.', citation: 'Discourse on Metaphysics §9' },
        { text: 'There are no purely extrinsic denominations, because of the real connection of all things.', citation: 'Discourse on Metaphysics §8' }
    ],

    commentary: [
        {
            philosopher: 'Antoine Arnauld',
            text: 'Arnauld\'s reaction to the summary of the Discourse was one of philosophical alarm: "I find in these thoughts so many things that frighten me, and that almost all men, if I am not mistaken, will find so shocking, that I do not see what use this writing could be of to the public." His specific target was the complete concept doctrine: if the concept of Adam contains all truths about all his descendants, then God could not have created Adam without determining all subsequent human history. This is fatalism — it destroys human freedom, renders sin meaningless, and makes God the author of evil. Leibniz\'s response — that this is hypothetical, not absolute, necessity — initiated a correspondence in which he was forced to develop and defend every major doctrine of the Discourse at technical length. The exchange produced the clearest expositions of his metaphysics he ever wrote.'
        },
        {
            philosopher: 'Benson Mates',
            text: 'Mates\' The Philosophy of Leibniz (1986) treated the Discourse as the most transparent and most vulnerable of Leibniz\'s texts. The complete concept doctrine says clearly what the Monadology only implies — and invites objections that Leibniz never fully answered. Most importantly, Mates showed that the complete concept theory generates a serious problem about counterfactuals: if Caesar\'s concept contains the predicate "will cross the Rubicon," then in any possible world containing Caesar, Caesar crosses the Rubicon. But then it seems impossible to say coherently what Caesar would have done if he had not crossed the Rubicon — because any individual who did not cross the Rubicon would simply not be Caesar. Individual essentialism of the Leibnizian kind makes counterfactuals about individuals either trivially true or incoherent, a difficulty that animated much of the subsequent literature on possible worlds and individual essences.'
        },
        {
            philosopher: 'Robert Merrihew Adams',
            text: 'Adams\' Leibniz: Determinist, Theist, Idealist (1994) treated the Discourse as the Rosetta Stone of Leibniz scholarship — every subsequent development can be traced back to doctrines stated here for the first time. Adams focused particularly on the relationship between the complete concept theory and Leibniz\'s idealism: the doctrine that God creates individual substances by having complete concepts of them in his mind suggests that created substances are, in an important sense, expressions of divine ideas. This quasi-idealist implication — that what ultimately exists are individual perspectives on a divinely-structured order — is worked out only in the Monadology, but its seeds are present in the Discourse\'s account of how God selects individuals for creation.'
        }
    ],

    modernRelevance: 'The Discourse\'s complete concept theory directly anticipates essentialism about individuals in contemporary metaphysics and the modal logic of Saul Kripke\'s Naming and Necessity (1980). Kripke\'s argument that proper names are rigid designators — that they pick out the same individual in every possible world — is a descendant of Leibniz\'s complete concept. The identity of indiscernibles remains an active topic in philosophy of physics: quantum mechanics raises challenges to it, since quantum particles of the same type appear to share all their intrinsic properties. The vis viva controversy the Discourse initiated — Leibniz against Descartes and Newton on what is conserved in collision — prefigures the modern distinction between momentum (mv) and kinetic energy (½mv²).',

    context: 'Leibniz wrote the Discourse during an extraordinarily productive period in which he was also developing the calculus, working on dynamics, and conducting diplomatic negotiations for the reunification of the Catholic and Protestant churches. He sent a summary of its thirty-seven articles to Arnauld through their mutual contact Ernst von Hessen-Rheinfels. The Discourse itself was not published until 1846; Leibniz was aware of its explosive implications and chose not to release it, a decision that meant one of the most important philosophical texts of the seventeenth century was unknown even to Kant and the German Idealists.',

    relatedWorks: ['monadology', 'correspondence-arnauld', 'new-essays', 'theodicy']
},

/* ──────────────────────────────────────
   2. PRINCIPLES OF NATURE AND GRACE
────────────────────────────────────── */
{
    id: 'principles-nature-grace',
    title: 'Principles of Nature and Grace, Founded in Reason',
    greekTitle: 'Principes de la nature et de la grâce, fondés en raison',
    philosopher: 'leibniz',
    category: 'metaphysics',
    categoryLabel: 'Metaphysics',
    date: '1714 AD',
    dateSort: 1714,
    emoji: '🌿',
    cardSize: 'normal',
    readingDifficulty: 'Intermediate',
    estimatedWordCount: 6000,

    shortDesc: 'The companion to the Monadology — a gentler, more accessible statement of Leibniz\'s final metaphysics, written for an educated non-specialist audience and containing his most famous question: why is there something rather than nothing?',

    summary: 'The Principles of Nature and Grace, written in 1714 alongside the Monadology and addressed to Prince Eugene of Savoy, is the most accessible of Leibniz\'s late metaphysical summaries. Where the Monadology proceeds in compressed, numbered paragraphs with minimal motivation, the Principles moves discursively, explaining why each doctrine is needed and how it connects to the others. It covers substantially the same ground — the nature of simple substances, perception and appetite, the hierarchy of monads, pre-established harmony, and the proof of God — but does so in a register that combines philosophical precision with a literary grace unusual in Leibniz\'s technical writings.\n\nThe Principles is most famous for containing the clearest statement of Leibniz\'s most radical question: "Why is there something rather than nothing? For nothing is simpler and easier than something." This question — which Heidegger called "the fundamental question of metaphysics" — appears in §7 as part of Leibniz\'s cosmological argument for God\'s existence: the world as a whole, being a contingent fact, requires a sufficient reason outside itself, and that reason can only be a necessary being whose existence follows from its own essence. The Principles also contains Leibniz\'s most explicit statement that monads are centres of force (entelechies), his clearest distinction between perception and apperception, and his most concise formulation of the relationship between the kingdom of nature (governed by efficient causes) and the kingdom of grace (governed by final causes, with God as its monarch).',

    themes: ['Simple Substances and Entelechies', 'Perception and Apperception', 'The Great Chain of Being', 'The Cosmological Argument', 'Pre-established Harmony', 'The Kingdom of Nature and Grace', 'Why There Is Something Rather Than Nothing'],

    keyCharacters: [
        { name: 'Prince Eugene of Savoy', role: 'The addressee — great military commander and patron of learning; his request for a summary of Leibniz\'s philosophy prompted both the Principles and the Monadology' }
    ],

    concepts: [
        'Entelechy — the monad conceived as a centre of self-activating force; a more dynamic formulation than the bare "simple substance" of the Monadology',
        'The great chain of being — the continuous gradation from bare monads through souls to rational spirits, with no gaps in nature',
        'Perception without apperception — unconscious perceptual states in lower monads; what we would now call unconscious processing',
        'The cosmological question — why is there something rather than nothing? The world\'s contingency requires a necessary ground',
        'Nature and grace — efficient causation and final causation as two harmonious domains within the single universe; the physical and moral orders as two aspects of the same perfection'
    ],

    structure: '§1–3: Simple substances, their nature and aggregation into bodies\n§4–6: Perception, appetite, and the hierarchy of monads; the distinction between perception and apperception\n§7–9: Why there is something rather than nothing; the cosmological argument for God\n§10–13: Pre-established harmony; the two kingdoms of nature and grace\n§14–18: God\'s moral kingdom; the final destiny of rational spirits',

    quote: 'Why is there something rather than nothing? For nothing is simpler and easier than something. Furthermore, supposing that things must exist, we must be able to give a reason why they must exist so and not otherwise. — Principles of Nature and Grace §7',

    additionalQuotes: [
        { text: 'Each simple substance has relations which express all the others, and is consequently a perpetual living mirror of the universe.', citation: 'Principles of Nature and Grace §3' },
        { text: 'Souls act according to the laws of final causes, through appetitions, ends, and means. Bodies act according to the laws of efficient causes, through motions. And the two kingdoms, that of efficient causes and that of final causes, are in harmony with each other.', citation: 'Principles of Nature and Grace §3' }
    ],

    commentary: [
        {
            philosopher: 'Martin Heidegger',
            text: 'Heidegger devoted an entire lecture course — The Principle of Reason (1955-56) — to meditating on the question Leibniz poses in §7 of the Principles. He argued that Leibniz\'s formulation is the first genuinely rigorous statement of what Heidegger calls the fundamental question of metaphysics: "Why are there beings at all, and not rather nothing?" The question is not scientific — it cannot be answered by any investigation within the world, because any such investigation already presupposes that the world exists. It is the question that opens onto Being itself, the question that makes metaphysics possible. Heidegger was ambivalent about Leibniz\'s answer through sufficient reason: he saw it as both the deepest attempt yet made at grounding being and as a decisive step toward the modern technological epoch in which beings are required to render their ratio, their calculative justification, at every turn.'
        },
        {
            philosopher: 'Nicholas Rescher',
            text: 'Rescher\'s Leibniz: An Introduction to His Philosophy (1979) identified the Principles as the text to give someone who wants to understand Leibniz in a single reading. It is less compressed than the Monadology, less polemical than the Theodicy, and more systematic than any of the scattered papers. Rescher also noted that the Principles\' formulation of the cosmological argument is more careful than is usually credited: Leibniz does not simply assert that contingent existence requires a necessary cause — he argues that the series of contingent things, even if infinite, cannot contain within itself the sufficient reason for its own existence, because no member of the series explains why there is a series rather than no series. The sufficient reason must therefore lie outside the series, in a necessary being. This argument anticipates the cosmological argument of contemporary analytic philosophers of religion from Rowe to Pruss.'
        }
    ],

    modernRelevance: 'The question "why is there something rather than nothing?" has become the most recognized philosophical question in popular culture and one of the most actively discussed in contemporary metaphysics and cosmology. Physicists from Hawking to Krauss to Carroll have published books attempting to answer it from within physics; metaphysicians from Heidegger to van Inwagen have treated it as the deepest question philosophy can pose. Leibniz\'s own answer — that the world\'s contingency requires a necessary being as its ground — remains the canonical theistic response and the starting point for every contemporary discussion of the cosmological argument for God\'s existence.',

    context: 'Like the Monadology, the Principles of Nature and Grace was written in 1714, in the final productive phase of Leibniz\'s life. The two texts were composed simultaneously but directed at different audiences; the Principles presupposes less technical background and explains its motivations more fully. Neither was published during Leibniz\'s lifetime. The Principles appeared in 1718 in L\'Europe savante, two years after Leibniz\'s death.',

    relatedWorks: ['monadology', 'theodicy', 'discourse-metaphysics', 'leibniz-philosophical-papers']
}

);
"""

# ─────────────────────────────────────────────────────────────────────────────
# DATA-13c  —  Theodicy + New System of Nature
# ─────────────────────────────────────────────────────────────────────────────
data_13c = r"""/* ================================================================
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
"""

# ─────────────────────────────────────────────────────────────────────────────
# DATA-13d  —  New Essays + Correspondence with Clarke
# ─────────────────────────────────────────────────────────────────────────────
data_13d = r"""/* ================================================================
   DATA PART 13d — New Essays on Human Understanding + Correspondence with Clarke
   ================================================================ */

window.WORKS.push(

/* ──────────────────────────────────────
   1. NEW ESSAYS ON HUMAN UNDERSTANDING
────────────────────────────────────── */
{
    id: 'new-essays',
    title: 'New Essays on Human Understanding',
    greekTitle: "Nouveaux Essais sur l'entendement humain",
    philosopher: 'leibniz',
    category: 'epistemology',
    categoryLabel: 'Epistemology',
    date: '1704 AD (posthumous 1765)',
    dateSort: 1704,
    emoji: '🔬',
    cardSize: 'normal',
    readingDifficulty: 'Advanced',
    estimatedWordCount: 180000,

    shortDesc: 'A book-length dialogue with Locke\'s ghost — the most sustained rationalist assault on empiricism ever written, with Leibniz arguing that the mind is not a blank slate but an active, structured source of necessary truths.',

    summary: 'The New Essays on Human Understanding is Leibniz\'s most extensive philosophical work and one of the great polemical texts in the history of philosophy. Written between 1703 and 1705, it takes the form of a dialogue between two characters — Philalethes, who summarizes Locke\'s Essay Concerning Human Understanding chapter by chapter, and Theophilus, who is Leibniz himself, responding, conceding, qualifying, and ultimately dismantling Locke\'s empiricist epistemology from within. The work is structured as a parallel to the Essay, following its four books on innate notions, ideas, words, and knowledge, so that it functions simultaneously as a commentary on Locke and as an independent statement of Leibniz\'s epistemology.\n\nThe central dispute is over the Lockean blank slate. Locke had argued that the mind at birth contains no innate ideas or principles — all knowledge derives from sensation and reflection. Leibniz counters that the mind brings to experience an active structure of innate dispositions, tendencies, and virtual knowledge that makes experience itself possible. His famous amendment to Locke\'s maxim is the pivot of the work: where Locke held that nothing is in the intellect that was not first in the senses, Leibniz adds except the intellect itself. The necessary truths of logic, mathematics, and metaphysics cannot be derived from experience because experience gives only contingent facts.\n\nBeyond this central dispute the New Essays contains Leibniz\'s most detailed treatments of personal identity (against Locke\'s memory theory), language and the relationship between words and ideas, the nature of substance, and the foundations of ethics and natural law. Leibniz learned of Locke\'s death in 1704 and withheld the work out of reluctance to attack a man who could no longer respond. It was published only in 1765, nearly fifty years after Leibniz\'s own death, and immediately influenced Kant, who later said it awakened him from his dogmatic slumber.',

    themes: ['Innate Ideas and Dispositions', 'Blank Slate vs Active Mind', 'Necessary and Contingent Truth', 'Personal Identity', 'Substance and Qualities', 'Language and Thought', 'Natural Law', 'Empiricism vs Rationalism'],

    keyCharacters: [
        { name: 'Philalethes', role: 'Locke\'s spokesman in the dialogue — summarizes the Essay Concerning Human Understanding faithfully and with sympathy throughout' },
        { name: 'Theophilus', role: 'Leibniz\'s alter ego — a courteous interlocutor who builds his own system through careful engagement with Locke\'s, agreeing where he can and correcting where he must' }
    ],

    concepts: [
        'Innate dispositions — the mind contains virtual knowledge that experience activates but does not create; knowledge is latent in the mind as a figure is latent in marble',
        'Nisi intellectus ipse — "except the intellect itself"; Leibniz\'s single addition to the empiricist maxim that nothing is in the intellect that was not first in the senses',
        'Petites perceptions — unconscious micro-perceptions that collectively constitute conscious experience; a precursor to the concept of the unconscious',
        'Apperception — the reflective awareness that distinguishes rational minds from animal souls; the difference between perceiving and knowing that one perceives',
        'Necessary vs contingent truths — the difference between truths whose opposite is impossible and truths that happen to hold but could have been otherwise',
        'The marble block metaphor — the mind is not a blank tablet but a block of marble already veined with the figure of Hercules; experience brings out what was already there'
    ],

    structure: 'Preface: Leibniz\'s most important statement on petites perceptions and innate ideas\nBook I: Whether there are innate principles in the mind — the central debate\nBook II: Ideas — their origin, composition, and the primary/secondary quality distinction\nBook III: Words — their relation to ideas, the nature of language, general terms\nBook IV: Knowledge — its degrees, extent, reality, and the grounds of faith and reason',

    quote: 'Nothing is in the intellect that was not first in the senses, except the intellect itself. — New Essays on Human Understanding, Preface',

    additionalQuotes: [
        { text: 'The senses, although necessary for all our actual knowledge, are not sufficient to give us the whole of it, since the senses never give anything but instances, that is to say, particular or individual truths.', citation: 'New Essays, Preface' },
        { text: 'The mind is not like a blank tablet; it is rather like a block of marble in which there are veins marking out the figure of Hercules — it just needs the sculptor\'s labour to uncover them.', citation: 'New Essays, Preface' },
        { text: 'These insensible perceptions are as important to pneumatology as insensible corpuscles are to natural philosophy.', citation: 'New Essays, Preface' }
    ],

    commentary: [
        {
            philosopher: 'Immanuel Kant',
            text: 'Kant\'s statement that it was Hume who awakened him from his dogmatic slumber is more famous, but in his correspondence and lectures he also credited the New Essays as one of the transformative texts of his philosophical development. The question Leibniz posed against Locke — what does the understanding contribute to knowledge from itself, prior to experience? — is precisely the question that animates the Critique of Pure Reason. Kant\'s answer — that the categories of the understanding and the forms of intuition (space and time) are the mind\'s own contributions to experience — is structurally Leibnizian: the mind is not a blank slate. But Kant\'s categories are not innate ideas in Leibniz\'s sense — they do not constitute knowledge of things as they are in themselves but only of appearances. The New Essays gave Kant the question; the Critique is his answer.'
        },
        {
            philosopher: 'Ernst Cassirer',
            text: 'Cassirer\'s Leibniz\'s System in its Scientific Foundations (1902) argued that the New Essays accomplishes something Locke could not: it shows that the question of knowledge cannot be answered by a natural history of ideas. Locke treated epistemology as a kind of introspective psychology — how do ideas arise in the mind? — without asking the prior logical question: what makes some ideas valid representations of reality? Leibniz showed that validity requires something that experience cannot supply: necessary connection, which only reason can provide. Cassirer saw in this the foundation of what would become neo-Kantian philosophy of science: the recognition that the formal structures of scientific knowledge — mathematics, logic, the categories of causation and substance — are contributions of the rational mind, not abstractions from experience.'
        },
        {
            philosopher: 'Noam Chomsky',
            text: 'Chomsky\'s argument for an innate universal grammar — that the human capacity to acquire language is not a general-purpose learning ability but a species-specific, domain-specific cognitive endowment — is explicitly Leibnizian in structure. Chomsky repeatedly cited the New Essays\' argument against the blank slate and the marble block metaphor as philosophical predecessors of his nativism about language. The "poverty of the stimulus" argument — that the linguistic input children receive is insufficient to explain the grammatical competence they develop — is the New Essays\' argument transposed from epistemology to linguistics: experience activates innate structures rather than creating them. Chomsky\'s rationalist cognitive science is the twentieth-century continuation of the debate Leibniz and Locke staged in 1704.'
        }
    ],

    modernRelevance: 'The doctrine of petites perceptions — unconscious micro-perceptions that collectively produce conscious states — is frequently cited as a precursor to the Freudian unconscious and to contemporary work on subliminal perception and the computational unconscious in cognitive science. The nativism debate Leibniz initiated against Locke remains live in philosophy of language and cognitive science. The New Essays\' treatment of personal identity anticipates the entire literature from Hume through Parfit on what makes a person the same person over time. The marble block metaphor has become one of the most cited images in rationalist epistemology.',

    context: 'Leibniz began the New Essays around 1700, working from the second English edition of Locke\'s Essay (1694). He completed a substantial draft by 1704 and was preparing it for publication when news of Locke\'s death on 28 October 1704 reached him. He wrote that he refrained from publishing "because it seems ungracious to attack a man who is no longer alive to defend himself." The work remained in manuscript until 1765, when its publication immediately influenced Kant, who was completing his pre-critical work and later described the New Essays as transformative for his development.',

    relatedWorks: ['monadology', 'discourse-metaphysics', 'theodicy', 'leibniz-philosophical-papers']
},

/* ──────────────────────────────────────
   2. CORRESPONDENCE WITH CLARKE
────────────────────────────────────── */
{
    id: 'correspondence-clarke',
    title: 'Correspondence with Clarke',
    greekTitle: 'Leibniz-Clarke Correspondence',
    philosopher: 'leibniz',
    category: 'natural-philosophy',
    categoryLabel: 'Natural Philosophy',
    date: '1715–1716 AD',
    dateSort: 1716,
    emoji: '🌌',
    cardSize: 'normal',
    readingDifficulty: 'Advanced',
    estimatedWordCount: 35000,

    shortDesc: 'The most consequential scientific-philosophical debate of the eighteenth century — Leibniz against Newton (through his spokesman Clarke) on the nature of space, time, and God\'s relation to the universe.',

    summary: 'The correspondence between Leibniz and Samuel Clarke — Newton\'s spokesman and defender — conducted between November 1715 and October 1716, is the most important philosophical debate about the foundations of physics before Kant. Leibniz died on 14 November 1716 before he could reply to Clarke\'s fifth letter; the correspondence therefore ends asymmetrically, Clarke having the last word in a dispute that Leibniz was winning on most of the central questions.\n\nThe debate opens with a letter from Leibniz to Caroline, Princess of Wales, in which he complains that Newton\'s philosophy is undermining natural religion in England. Newton and Clarke are committed to an absolute space and time — a vast receptacle that exists independently of the things in it — and this commits them to making God\'s omnipresence a matter of occupying an infinite spatial void, which is absurd. More fundamentally, Newton\'s God is a bad clockmaker: he must intervene periodically to correct the universe\'s running, because the Newtonian laws do not conserve the total quantity of force. Leibniz\'s God created a perfect machine that runs without intervention.\n\nThe Newtonian absolute space becomes the crux of the debate. Leibniz argues against it with his most powerful weapon: the principle of sufficient reason. If space is absolute — if there is a real distinction between different regions of empty space containing nothing — then there is no reason why God should have placed the universe here rather than there. Since God always has sufficient reason for his acts, and since there could be no sufficient reason to prefer one empty location over another, absolute space cannot exist. Space is nothing but the order of coexisting things; time is nothing but the order of successive things.',

    themes: ['Absolute vs Relational Space and Time', 'The Principle of Sufficient Reason', 'God as Clockmaker vs Interventionist', 'Natural Law and Miracles', 'The Identity of Indiscernibles', 'Foundations of Newtonian Physics', 'Newton vs Leibniz'],

    keyCharacters: [
        { name: 'Samuel Clarke', role: 'Newton\'s philosophical spokesman — theologian and philosopher who defended Newtonian absolute space with rigour; manuscript evidence shows Newton himself drafted some of Clarke\'s replies' },
        { name: 'Caroline, Princess of Wales', role: 'The philosophically serious intermediary through whom the correspondence was conducted; later Queen of England as wife of George II' },
        { name: 'Isaac Newton', role: 'The silent presence behind Clarke\'s letters — manuscripts confirm Newton directed the Newtonian side of the debate' }
    ],

    concepts: [
        'Absolute space — Newton\'s infinite homogeneous container existing independently of its contents; the receptacle within which all physical events occur',
        'Relational space — Leibniz\'s position: space as nothing but the system of spatial relations among existing things; there is no space without things',
        'Relational time — time as nothing but the order of successive events, not a container; a world with all events shifted by one hour would be identical to this one',
        'Sufficient reason applied to cosmology — no sufficient reason to place the universe here vs there; therefore absolute space, with its indistinguishable regions, cannot exist',
        'God as perfect clockmaker — Leibniz\'s insistence that God\'s perfection requires a self-sustaining universe; a God who intervenes to fix the cosmic machine is an imperfect craftsman',
        'Sensorium of God — Newton\'s suggestion that space is God\'s organ of perception; Leibniz attacks this as absurd and materialist'
    ],

    structure: 'Leibniz\'s first letter: general complaint about Newtonian natural religion\nClarke\'s first reply: defence of Newton\'s theological credentials\nLeibniz\'s second letter: absolute space and sufficient reason\nClarke\'s second reply: defence of absolute space; miracles and natural order\nLeibniz\'s third letter: full statement of relational theory; identity of indiscernibles\nClarke\'s third reply: space as independent reality; God\'s absolute freedom\nLeibniz\'s fourth letter: on atoms, the void, and force\nClarke\'s fourth reply\nLeibniz\'s fifth letter (his longest and most systematic): the complete statement of relational spacetime\nClarke\'s fifth reply (unanswered — Leibniz died three months later)',

    quote: 'I hold space to be something merely relative, as time is; that I hold it to be an order of coexistences, as time is an order of successions. — Leibniz\'s Third Letter §4',

    additionalQuotes: [
        { text: 'Space is something absolutely uniform; and, without the things placed in it, one point of space does not absolutely differ in any respect whatsoever from another point. Now from hence it follows, supposing space to be something in itself besides the order of bodies among themselves, that it is impossible there should be a reason why God should have placed them in space after one certain particular manner, and not otherwise.', citation: 'Leibniz\'s Third Letter §5' },
        { text: 'A clockmaker who needs to intervene constantly in his clock is a bad clockmaker. God is no such workman.', citation: 'Leibniz\'s First Letter (paraphrased)' }
    ],

    commentary: [
        {
            philosopher: 'Immanuel Kant',
            text: 'The Leibniz-Clarke correspondence was a decisive influence on Kant\'s philosophy of space and time. In the Critique of Pure Reason, Kant argued that both Leibniz and Newton were wrong — and both were right. Newton was right that space and time are not simply abstracted from the relations among empirical objects: they are prior to experience, the forms within which any experience whatsoever must be structured. But Newton was wrong to treat them as absolute containers existing independently of all minds: they are, for Kant, forms of our intuition, not properties of things in themselves. Leibniz was right that space cannot be a Newtonian container — that there would be no fact of the matter about where in absolute space the universe is located — but wrong to think space is simply a system of relations among things in themselves. Kant\'s transcendental aesthetic is the synthesis that emerges from the Leibniz-Clarke impasse.'
        },
        {
            philosopher: 'Albert Einstein',
            text: 'Einstein declared, in his introduction to the correspondence published in English translation in 1956, that the theory of relativity vindicates Leibniz against Newton. There is no absolute space, no absolute simultaneity: spacetime is relational in precisely the sense Leibniz argued. The general theory of relativity goes further: spacetime is not merely relational but dynamic, shaped by the distribution of matter and energy. Leibniz\'s clockmaker God — who sets the cosmic machine running without further intervention — maps onto the relativistic universe, which has no need of an external reference frame. Einstein noted that Leibniz was right about the physics but had the wrong reason: Leibniz argued from the principle of sufficient reason, while Einstein derived the same conclusion from the principle of general covariance. The result is the same: absolute space is not a physical reality.'
        },
        {
            philosopher: 'Tim Maudlin',
            text: 'Maudlin\'s Philosophy of Physics: Space and Time (2012) argued that the Leibniz-Clarke debate is not merely historical — the question of whether spacetime is a substance or a system of relations is as live in contemporary philosophy of physics as it was in 1716, and the arguments have not fundamentally changed. Modern substantivalists argue that general relativity requires a spacetime manifold as a genuine entity in its own right; modern relationalists argue that the manifold is a representational artifact and only the relations among material events are physically real. The debate maps precisely onto the Clarke-Leibniz disagreement. Maudlin noted that the strongest contemporary argument against relationalism — that it cannot accommodate the dynamical structure of general relativistic spacetime — is a version of Clarke\'s objection that Leibniz\'s relational space has no room for absolute acceleration.'
        }
    ],

    modernRelevance: 'The Leibniz-Clarke debate maps almost perfectly onto the contemporary debate between substantivalism and relationalism in philosophy of physics. Einstein\'s general theory of relativity is widely interpreted as a vindication of Leibniz\'s relational view, though the details remain contested. Julian Barbour\'s relational mechanics, Carlo Rovelli\'s relational quantum mechanics, and Lee Smolin\'s work on background-independent physics all cite the Leibniz-Clarke correspondence as a foundational document. It is the only early modern philosophical text that working physicists regularly read.',

    context: 'Leibniz initiated the correspondence in November 1715, knowing he was in poor health. The exchange was conducted through Caroline, Princess of Wales — a genuine philosophical enthusiast who had corresponded with both Leibniz and the Newtonians for years. Leibniz wrote his fifth letter, his longest and most systematic contribution, in August 1716. He died three months later, on 14 November 1716. Clarke published the complete correspondence in 1717.',

    relatedWorks: ['monadology', 'theodicy', 'discourse-metaphysics', 'leibniz-philosophical-papers']
}

);
"""

# ─────────────────────────────────────────────────────────────────────────────
# DATA-13e  —  Correspondence with Arnauld + Philosophical Papers and Letters
# ─────────────────────────────────────────────────────────────────────────────
data_13e = r"""/* ================================================================
   DATA PART 13e — Correspondence with Arnauld + Philosophical Papers and Letters
   ================================================================ */

window.WORKS.push(

/* ──────────────────────────────────────
   1. CORRESPONDENCE WITH ARNAULD
────────────────────────────────────── */
{
    id: 'correspondence-arnauld',
    title: 'Correspondence with Arnauld',
    greekTitle: 'Correspondance avec Arnauld',
    philosopher: 'leibniz',
    category: 'metaphysics',
    categoryLabel: 'Metaphysics',
    date: '1686–1690 AD',
    dateSort: 1687,
    emoji: '📬',
    cardSize: 'normal',
    readingDifficulty: 'Advanced',
    estimatedWordCount: 60000,

    shortDesc: 'The most rigorous philosophical correspondence of the seventeenth century — Leibniz forced to defend every doctrine of the Discourse on Metaphysics against one of the sharpest minds of the century, producing the clearest expositions of his system he ever wrote.',

    summary: 'The correspondence between Leibniz and Antoine Arnauld, conducted between 1686 and 1690, is the most philosophically demanding exchange in the early modern period and the primary site where Leibniz\'s mature metaphysical doctrines were tested, refined, and in some cases significantly modified. Arnauld was the greatest French theologian of the century — a Jansenist, a logician, and a polemicist of terrifying precision who had already demolished Malebranche\'s theory of seeing all things in God and had co-authored the Port-Royal Logic with Nicole.\n\nWhen the summary of the Discourse on Metaphysics reached him, his initial reaction was not merely theological but logically acute: the complete concept doctrine implied that God could not have created Adam without thereby determining all future human history, and this fatalism destroyed human freedom and rendered sin meaningless. Leibniz\'s letters in response are the clearest and most carefully argued expositions of his metaphysics he ever produced. The correspondence covers the complete concept of individual substance and its implications for freedom; the nature of substance and its distinction from mere aggregates; the relationship between the soul and the body (Leibniz develops his theory of pre-established harmony here more clearly than in the Discourse); the nature of force and its conservation; and the distinction between what is absolutely necessary and what God freely but inevitably chooses.\n\nArnauld never accepted Leibniz\'s responses, but his resistance sharpened Leibniz\'s formulations in ways visible in every subsequent statement of the system, including the Monadology.',

    themes: ['Complete Concept and Freedom', 'Substance vs Aggregate', 'Soul-Body Relation', 'Pre-established Harmony', 'Force and Conservation', 'Divine Necessity and Freedom', 'Personal Identity Over Time', 'Hypothetical vs Absolute Necessity'],

    keyCharacters: [
        { name: 'Antoine Arnauld', role: 'Theologian, logician, and Jansenist controversialist — co-author of the Port-Royal Logic and author of the Fourth Objections to Descartes\' Meditations; Leibniz\'s most formidable correspondent' },
        { name: 'Ernst von Hessen-Rheinfels', role: 'The Landgrave who served as intermediary — a Catholic convert sympathetic to both men, through whom the letters were routed' }
    ],

    concepts: [
        'The complete concept objection — if Adam\'s concept contains all future history, then human history is necessary and God cannot have created Adam without all his descendants',
        'Hypothetical vs absolute necessity — the world is hypothetically necessary (given God\'s choice of the best) but not absolutely necessary; God could have chosen otherwise',
        'Substance as genuine unity — a substance must have a genuine principle of unity, unlike a heap or a machine; the criterion that drives Leibniz from Cartesian physics to monads',
        'Force as the mark of substance — true substances are distinguished by their active force, not mere extension; Leibniz\'s first sustained argument against Cartesian matter theory',
        'Pre-established harmony defended — Arnauld\'s pressure forces Leibniz to articulate the harmony doctrine with a clarity absent from the Discourse',
        'Aggregate vs substance — a flock of sheep is not a substance; a single sheep may be; the distinction that will culminate in the Monadology\'s windowless monads'
    ],

    structure: 'March 1686: Leibniz sends summary of the Discourse through von Hessen-Rheinfels\nMay 1686: Arnauld\'s first letter — shock at the complete concept doctrine\nJuly 1686: Leibniz\'s long reply — the central defence of complete concepts and hypothetical necessity\nSeptember 1686 – 1687: Exchange on substance, aggregates, and the soul-body relation\n1688–1690: Final letters on force, conservation, and the nature of substantial form',

    quote: 'I maintain that the concept of an individual substance contains once and for all everything that can ever happen to it, and that in considering this concept, one can see everything that can truly be said of it, just as we can see in the nature of a circle all the properties that can be derived from it. — Leibniz to Arnauld, July 1686',

    additionalQuotes: [
        { text: 'A being by aggregation, such as a heap of stones, is not truly one being, nor has it one true unity; it has only an accidental or external unity.', citation: 'Leibniz to Arnauld, April 1687' },
        { text: 'I find in these thoughts so many things that frighten me, and that almost all men, if I am not mistaken, will find so shocking, that I do not see what use this writing could be of to the public.', citation: 'Arnauld to Leibniz, May 1686' },
        { text: 'It is true that the consequences of so perfect a concept are immense; but they are far from being as terrible as they first appear.', citation: 'Leibniz to Arnauld, July 1686' }
    ],

    commentary: [
        {
            philosopher: 'R.C. Sleigh',
            text: 'Sleigh\'s Leibniz and Arnauld: A Commentary on Their Correspondence (1990) established the correspondence as the indispensable document for understanding Leibniz\'s metaphysics — more revealing than the Monadology, more argued than the Discourse. Sleigh showed that Arnauld\'s objections were not simply answered by Leibniz\'s distinction between hypothetical and absolute necessity. The tension between the complete concept doctrine and human freedom runs through Leibniz\'s entire system and is never fully resolved. Every major subsequent philosopher in the Leibnizian tradition — from Wolff to Kant to the twentieth-century analytic Leibniz scholars — has had to return to the Arnauld correspondence to understand where the system is genuinely tight and where it merely appears so.'
        },
        {
            philosopher: 'Daniel Garber',
            text: 'Garber\'s Leibniz: Body, Substance, Monad (2009) argued that the correspondence with Arnauld is where Leibniz first explicitly addresses the problem of what makes something a genuine substance as opposed to a mere aggregate. This problem drives his metaphysics from 1686 all the way to the Monadology. The key move is the force criterion: genuine substances are distinguished by their active force, their internal principle of self-determination. Cartesian matter — pure extension, purely passive — cannot be a genuine substance, because extension is infinitely divisible and cannot constitute a genuine unity. The road from this insight in the Arnauld letters to the windowless monads of 1714 is direct, though not without complications. Garber\'s account of the development is the most philosophically rigorous reconstruction available.'
        }
    ],

    modernRelevance: 'The debate about whether the complete concept theory entails fatalism remains live in contemporary metaphysics of modality and philosophy of religion. The question of whether libertarian free will is compatible with divine foreknowledge — the theological form of Arnauld\'s objection — is one of the most active topics in analytic philosophy of religion. The substance/aggregate distinction Leibniz develops in these letters has also influenced contemporary discussions of composition and mereology: when does a collection of things constitute a genuine unified entity, and when is it merely an aggregate? Peter van Inwagen\'s Special Composition Question and David Lewis\'s mereological universalism are twentieth-century continuations of exactly this problem.',

    context: 'The correspondence was conducted through their mutual contact Ernst von Hessen-Rheinfels. Arnauld initially refused to correspond directly with Leibniz, regarding the Discourse\'s doctrines as too dangerous. He eventually relented and the exchange became direct and substantive. It broke off in 1690 without resolution; Arnauld died in 1694. The correspondence was not published until the nineteenth century and was unknown even to most eighteenth-century readers of Leibniz, including Kant — its rediscovery transformed twentieth-century Leibniz scholarship.',

    relatedWorks: ['discourse-metaphysics', 'monadology', 'new-essays', 'theodicy']
},

/* ──────────────────────────────────────
   2. PHILOSOPHICAL PAPERS AND LETTERS
────────────────────────────────────── */
{
    id: 'leibniz-philosophical-papers',
    title: 'Philosophical Papers and Letters',
    greekTitle: 'Opera Omnia (Philosophical Writings)',
    philosopher: 'leibniz',
    category: 'method',
    categoryLabel: 'Philosophical Writings',
    date: '1666–1716 AD',
    dateSort: 1690,
    emoji: '📄',
    cardSize: 'wide',
    readingDifficulty: 'Advanced',
    estimatedWordCount: 500000,

    shortDesc: 'The vast unpublished workshop of 100,000 manuscript pages — the actual site where Leibniz\'s philosophy was built, tested, and sometimes contradicted, ranging from the characteristica universalis to the calculus of logic to the deepest question in metaphysics.',

    summary: 'Unlike Descartes or Spinoza, Leibniz published almost nothing of his philosophy during his lifetime. His philosophical system is known primarily through an enormous archive of unpublished papers, fragments, drafts, and correspondence preserved in the Hanover library — a collection estimated at over 100,000 pages that is still not fully published. The Akademie edition of his collected works, begun in 1923, remains incomplete a century later.\n\nAmong the most important papers are: the Meditations on Knowledge, Truth, and Ideas (1684), the first published statement of his epistemology and the source of the distinction between clear, distinct, adequate, and intuitive ideas; On the Ultimate Origination of Things (1697), the most concentrated statement of his cosmological argument, opening with "why is there something rather than nothing?"; On Nature Itself (1698), a defence of active force in nature against mechanism; Primary Truths (c.1689), a systematic derivation of his metaphysical principles from the principle of sufficient reason and predicate-inclusion theory of truth; and the New System of Nature (1695). The logical papers — drafts toward the characteristica universalis, the universal formal language Leibniz dreamed of constructing — represent his most technically ambitious philosophical project: a symbolic system in which all concepts would be represented and all reasoning reduced to calculation.\n\nThe unpublished papers also reveal tensions and unresolved problems that the published works conceal. Leibniz\'s views on the persistence of substances over time, on the precise relationship between monads and bodies, on whether there are genuinely extended physical substances or only collections of monads that appear extended, and on the nature of mathematical infinity were never settled in his published work and are still actively disputed among scholars. The real Leibniz — more rigorous, more technical, more self-contradictory than the courtly philosopher of the Theodicy — lives in these papers.',

    themes: ['Characteristica Universalis', 'Logical Calculus', 'Predicate-in-Subject Truth', 'Cosmological Argument', 'Active Force in Nature', 'Mathematical Infinity', 'Philosophy of Language', 'Epistemological Hierarchy'],

    keyCharacters: [
        { name: 'Leibniz as universal genius', role: 'The papers reveal a thinker simultaneously working on logic, metaphysics, physics, mathematics, theology, history, linguistics, and political philosophy — the last person to whom the designation of universal genius might be plausibly applied' }
    ],

    concepts: [
        'Characteristica universalis — a universal symbolic language that would express all concepts and reduce reasoning to calculation; the direct ancestor of modern mathematical logic',
        'Calculus ratiocinator — the logical calculus that would operate on the characteristica universalis; Leibniz\'s dream of replacing philosophical argument with formal proof',
        'Predicate-in-subject principle — in every true affirmative proposition, the predicate is contained in the subject; the logical foundation from which the entire Leibnizian metaphysics flows',
        'Active force (vis activa) — the immanent principle of action in substances, against purely mechanical nature; the property that distinguishes genuine substances from mere aggregates',
        'Primary truths — a compressed derivation of all Leibnizian metaphysical doctrines from the principle of sufficient reason and the predicate-inclusion theory of truth',
        'The cosmological question formalized — "why is there something rather than nothing?" presented as the fundamental question that finite explanation cannot answer, requiring a necessary ground'
    ],

    structure: 'Key texts include:\n"Meditations on Knowledge, Truth, and Ideas" (1684)\n"Primary Truths" (c.1689)\n"New System of Nature" (1695)\n"On the Ultimate Origination of Things" (1697)\n"On Nature Itself" (1698)\n"Principles of Nature and Grace" (1714)\nSpecimen of Dynamics (1695)\nDrafts toward the characteristica universalis and calculus ratiocinator\nEarly writings: De Arte Combinatoria (1666), Confession of a Philosopher (c.1672–73)\nLogical papers: drafts for a formal calculus of concepts (1679–1690)',

    quote: 'If controversies were to arise, there would be no more need of disputation between two philosophers than between two accountants. For it would suffice to take their pencils in their hands, to sit down at the abacus, and to say to each other: Let us calculate. — Letter to Philip Naudé (1716)',

    additionalQuotes: [
        { text: 'Why is there something rather than nothing? For nothing is simpler and easier than something. Furthermore, supposing that things must exist, we must be able to give a reason why they must exist so and not otherwise.', citation: 'On the Ultimate Origination of Things (1697)' },
        { text: 'In the least of substances, eyes as penetrating as those of God could read the whole sequence of things in the universe.', citation: 'Discourse on Metaphysics §8 (included among the papers)' }
    ],

    commentary: [
        {
            philosopher: 'Bertrand Russell',
            text: 'Russell\'s A Critical Exposition of the Philosophy of Leibniz (1900) drew a sharp distinction between the public and private Leibniz that has shaped scholarship ever since. The Leibniz of the published works — the Theodicy, the correspondence with Clarke — is a courtier philosopher, adapting his doctrines for genteel audiences, emphasizing theological reassurance and political propriety. The Leibniz of the unpublished papers is the real philosopher: rigorous, technical, and sometimes in contradiction with his public positions. Russell argued that the key to the whole system is the predicate-in-subject principle of the logical papers, from which the complete concept theory, the denial of genuine relations, the windowless monads, and the pre-established harmony all follow with near-necessity. The public theology is the superstructure; the private logic is the foundation.'
        },
        {
            philosopher: 'Louis Couturat',
            text: 'Couturat\'s La Logique de Leibniz (1901) — published the year after Russell\'s book and drawing on manuscript sources Russell had not used — argued even more forcefully that the logical papers transform our understanding of Leibniz. His metaphysics is not independently motivated: it flows from his logic, from the predicate-inclusion theory of truth, which is itself a generalization of the structure of necessary propositions in the characteristica universalis. The monad, Couturat argued, is a logical subject made ontological — the complete concept of an individual substance hypostasized into a substance. If this is right, then Leibniz\'s entire metaphysics depends on a logic that Russell\'s Principia Mathematica had already refuted: a subject-predicate logic incapable of analyzing genuine relations.'
        },
        {
            philosopher: 'Gottlob Frege',
            text: 'Frege\'s Begriffsschrift (1879) — the invention of modern mathematical logic and the founding document of analytic philosophy — was explicitly motivated by Leibniz\'s dream of a characteristica universalis. Frege wrote in his preface that his concept-script was designed to do what Leibniz had sketched: provide a universal formal language adequate to express all valid reasoning. Where Leibniz\'s calculus had remained a dream, Frege\'s logic was a technical achievement: quantifiers, functions, variables, and the resources to formalize not just propositional but polyadic predicate logic. Russell and Whitehead\'s Principia Mathematica built directly on Frege\'s logic. The history of mathematical logic from Boole through Frege through Gödel is the fulfillment of the program the philosophical papers first articulated.'
        },
        {
            philosopher: 'Catherine Wilson',
            text: 'Wilson\'s Leibniz\'s Metaphysics (1989) used the unpublished papers to challenge the standard picture of Leibniz as a confident system-builder. The papers show a philosopher constantly revising, testing alternatives, and acknowledging unresolved tensions — particularly around the question of how monads relate to physical bodies, whether bodies are real or merely phenomenal, and whether there are corporeal substances alongside purely spiritual monads. The Monadology presents a clean, complete system; the papers reveal that this cleanliness was achieved by suppressing or deferring questions that Leibniz never satisfactorily resolved. Wilson argued that the apparent completeness of the mature system is partly an artifact of the selection of texts for publication.'
        }
    ],

    modernRelevance: 'Leibniz\'s characteristica universalis was the direct inspiration for Frege\'s Begriffsschrift, which founded modern mathematical logic, and for the early work of Russell and Whitehead in Principia Mathematica. Leibniz is thus a founding figure of mathematical logic, computer science (through his influence on Boole and Frege), and the theory of formal languages. His binary arithmetic papers have made him an icon in the history of computing. His question "why is there something rather than nothing" has become the canonical formulation of the deepest question in metaphysics and cosmology. And the logical papers\' vision of automated reasoning has, three centuries later, been partially realized in modern automated theorem provers and formal verification systems.',

    context: 'The Leibniz archive in Hanover contains over 100,000 manuscript pages. The Akademie edition of his collected works, begun in 1923, is still not complete a century later. Many of the most philosophically important papers were first published only in the late nineteenth and twentieth centuries. The calculus papers — showing that Leibniz developed the differential and integral calculus independently of Newton — were at the centre of the most bitter priority dispute in the history of science, conducted through the Royal Society under Newton\'s presidency with results now widely regarded as systematically biased against Leibniz. Modern historians of mathematics are agreed that both developed the calculus independently and that Leibniz\'s notation — dy/dx, the integral sign — was superior to Newton\'s and is the notation still used today.',

    relatedWorks: ['monadology', 'new-essays', 'discourse-metaphysics', 'theodicy', 'correspondence-clarke']
}

);
"""

files = {
    'data-13a.js': data_13a,
    'data-13b.js': data_13b,
    'data-13c.js': data_13c,
    'data-13d.js': data_13d,
    'data-13e.js': data_13e,
}

for filename, content in files.items():
    path = os.path.join(js_dir, filename)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    lines = content.count('\n')
    print(f'  Written {filename}  —  {lines} lines  →  {path}')

print('\nAll Leibniz files complete. Verify with:')
print('  wc -l js/data-13a.js js/data-13b.js js/data-13c.js js/data-13d.js js/data-13e.js')
