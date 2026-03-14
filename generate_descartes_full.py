#!/usr/bin/env python3
"""
Run from inside ~/Desktop/philosophy-archive/
  python3 generate_descartes_full.py
Writes js/data-11a.js through js/data-11e.js
Overwrites whatever is there.
"""
import os

js_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'js')
os.makedirs(js_dir, exist_ok=True)

# ─────────────────────────────────────────────────────────────────────────────
# DATA-11a  —  Meditations on First Philosophy
# ─────────────────────────────────────────────────────────────────────────────
data_11a = r"""/* ================================================================
   DATA PART 11a — Meditations on First Philosophy (Descartes)
   ================================================================ */

window.WORKS.push(

/* ──────────────────────────────────────
   1. MEDITATIONS ON FIRST PHILOSOPHY
────────────────────────────────────── */
{
    id: 'meditations',
    title: 'Meditations on First Philosophy',
    greekTitle: 'Meditationes de Prima Philosophia',
    philosopher: 'descartes',
    category: 'metaphysics',
    categoryLabel: 'Metaphysics & Epistemology',
    date: '1641 AD',
    dateSort: 1641,
    emoji: '🕯',
    cardSize: 'wide',
    readingDifficulty: 'Intermediate',
    estimatedWordCount: 23000,

    shortDesc: 'The founding document of modern philosophy — six meditations that demolish all prior knowledge through radical doubt, discover the thinking self as the one unshakeable certainty, and rebuild science on the foundation of clear and distinct perception guaranteed by a non-deceptive God.',

    summary: 'Written in the first person as a six-day intellectual exercise, the Meditations is Descartes\'s attempt to place human knowledge on absolutely certain foundations by first subjecting every belief to the most radical doubt possible. The First Meditation introduces methodological doubt in three escalating waves: the unreliability of the senses, the impossibility of distinguishing waking from dreaming, and finally the hypothesis of an all-powerful evil demon who might be deceiving him even about the truths of mathematics and logic. Having stripped away every certainty, the Second Meditation discovers the one proposition that survives all doubt: the very act of doubting proves there is a thinking thing doing the doubting. "I am, I exist" is necessarily true whenever it is entertained. Descartes then deploys the wax argument: a piece of wax melted before a fire loses all its sensory qualities, yet we still know it is the same wax — showing that the intellect, not the senses, grasps the essential nature of things.\n\nThe Third Meditation constructs a cosmological argument for God\'s existence based on the causal adequacy principle: the idea of an infinitely perfect being, which Descartes finds innate in his mind, could only have been placed there by an actually infinite and perfect being. The Fourth Meditation explains the origin of error: God gave us a finite intellect but a will of unlimited scope; error arises when the will assents to what the intellect has not clearly and distinctly perceived. The Fifth Meditation offers an ontological argument: existence belongs to God\'s essence as necessarily as having three angles belongs to a triangle. The Sixth and final Meditation establishes the existence of the material world — because a non-deceptive God would not have given us an irresistible inclination to believe in external bodies if they did not exist. Here Descartes also establishes the real distinction between mind (res cogitans) and body (res extensa) — the substance dualism that would define and trouble philosophy for the following four centuries.\n\nThe Meditations were published with six sets of Objections and Replies solicited from contemporary thinkers including Mersenne, Arnauld, Hobbes, and Gassendi — making it one of the most collaborative foundational texts in the history of philosophy.',

    themes: ['Doubt and Certainty', 'The Cogito', 'God\'s Existence', 'Mind and Body', 'Substance Dualism', 'Clear and Distinct Perception', 'Error and Will', 'Innate Ideas', 'The External World'],

    keyCharacters: [
        { name: 'The Meditator', role: 'The first-person voice — not exactly Descartes himself but a generic rational inquirer who strips away all prior beliefs to discover what can be known with certainty' },
        { name: 'The Evil Demon', role: 'A thought-experiment device — a hypothetically all-powerful deceiver whose mere possibility is enough to undermine any belief that cannot survive it' },
        { name: 'God', role: 'The guarantor of clear and distinct perception; whose necessary existence and perfect nature bridges the gap between the thinking self and the external world' }
    ],

    concepts: [
        'Methodological doubt — hyperbolic doubt used as a tool to discover what, if anything, is immune to all possible skeptical challenge',
        'Evil demon hypothesis — the third and strongest wave of doubt: an all-powerful deceiver might make even mathematics unreliable',
        'Cogito (ego sum, ego existo) — the one certainty that survives all doubt; the thinking thing necessarily exists whenever it thinks',
        'Wax argument — shows that material things are known by intellect, not senses; the intellect grasps the essence of wax even when all sensory qualities change',
        'Trademark argument — the causal adequacy principle applied to the innate idea of God; only an actually infinite being could cause the idea of infinity in a finite mind',
        'Res cogitans vs res extensa — the real distinction between thinking substance and extended substance; the foundation of Cartesian dualism',
        'Clear and distinct perception — the criterion of truth guaranteed by God\'s non-deception; what I perceive clearly and distinctly is true',
        'Ontological argument — God\'s existence is contained in his essence as necessarily as three angles are contained in a triangle',
        'Cartesian circle — the apparent circularity between using clear and distinct perception to prove God and using God to validate clear and distinct perception'
    ],

    structure: 'Six meditations presented as a structured intellectual retreat:\n\nFirst Meditation: The three waves of doubt — sensory unreliability, the dream argument, the evil demon. All prior beliefs are suspended.\n\nSecond Meditation: The cogito. The wax argument. The mind is better known than the body.\n\nThird Meditation: Taxonomy of ideas. The causal adequacy principle. The Trademark Argument for God\'s existence.\n\nFourth Meditation: The will vs the intellect. Error defined as assent extended beyond clear and distinct perception. God is not responsible for human error.\n\nFifth Meditation: Mathematical truths as eternal. The ontological argument for God\'s existence.\n\nSixth Meditation: Imagination vs intellect. Proof of the external world. The real distinction between mind and body. The mind-body union and the passions.',

    quote: 'I am, I exist — that is certain. But for how long? For as long as I am thinking. — Meditations, Second Meditation',

    additionalQuotes: [
        { text: 'I will suppose that some malicious demon of the utmost power and cunning has employed all his energies in order to deceive me.', citation: 'Meditations, First Meditation' },
        { text: 'What then am I? A thing that thinks. What is that? A thing that doubts, understands, affirms, denies, is willing, is unwilling, and also imagines and has sensory perceptions.', citation: 'Meditations, Second Meditation' },
        { text: 'Whatever I perceive very clearly and distinctly is true.', citation: 'Meditations, Third Meditation' }
    ],

    commentary: [
        {
            philosopher: 'Immanuel Kant',
            text: 'Kant\'s entire critical project in the Critique of Pure Reason (1781) is, in many ways, a response to problems the Meditations created. Kant accepted Descartes\' insight that the thinking subject is epistemically primary, but rejected his metaphysical conclusions. Most famously, Kant demolished the ontological argument of the Fifth Meditation by arguing that existence is not a predicate — you cannot derive actual existence from the mere concept of something, however perfect. "A hundred real thalers do not contain the least coin more than a hundred possible thalers." But Kant also inherited the deeper Cartesian problem: if the mind only ever knows its own representations, how can we be certain these represent an external world? Kant\'s transcendental idealism — the doctrine that space, time, and the categories of the understanding are imposed by the mind on experience rather than read off from things in themselves — is a radical extension of the Cartesian insight that the intellect, not the senses, provides the structure of knowledge.'
        },
        {
            philosopher: 'Gilbert Ryle',
            text: 'In The Concept of Mind (1949), Ryle launched the most influential twentieth-century attack on Cartesian dualism, coining the phrase "the ghost in the machine" to describe the absurdity of positing a non-physical thinking substance housed inside a physical body. Ryle argued that Descartes committed a category mistake: he assumed that because we can talk about the mind and the body separately, they must be two distinct substances. The mind is not a thing over and above mental activities; it is the manner in which those activities are performed. Ryle\'s critique launched philosophical behaviourism and influenced the cognitive science that followed, though many argued he refuted only a caricature of dualism and left the hard problem of consciousness untouched.'
        },
        {
            philosopher: 'Edmund Husserl',
            text: 'Husserl\'s Cartesian Meditations (1931), explicitly titled as a homage, began phenomenology\'s engagement with Descartes. Husserl praised the Meditations\' method of bracketing all prior assumptions and returning to the pure deliverances of consciousness as the proper starting point for rigorous philosophy. But he criticized Descartes for abandoning the most radical implications of his own method: rather than exploring the structure of consciousness itself in its intentional directedness toward objects, Descartes rushed to use the cogito as a springboard for metaphysics and theology. For Husserl, Descartes had the right method but the wrong destination. Phenomenology would complete what the Meditations began.'
        },
        {
            philosopher: 'Antoine Arnauld',
            text: 'Arnauld\'s Fourth Objections — widely regarded as the sharpest of all the original objections — raised the Cartesian Circle: Descartes argues that whatever he perceives clearly and distinctly is true because God is no deceiver, but he establishes God\'s existence using clear and distinct perception. The argument is circular. Descartes\' response — that God\'s guarantee is only needed to validate memories of clear and distinct perceptions, not perceptions themselves when immediately before the mind — has satisfied some and not others. Arnauld also raised the mind-body interaction problem that would become the central difficulty for all subsequent Cartesianism: if mind and body are truly distinct substances with nothing in common, how can they causally interact?'
        },
        {
            philosopher: 'Hilary Putnam',
            text: 'In his essay "Brains in a Vat" (1981), Putnam extended the evil demon hypothesis into the language of contemporary philosophy of mind. Could we be disembodied brains in a vat, connected to a computer that feeds us all our experiences? Putnam\'s surprising answer was no — not because the scenario is physically impossible, but because of semantic externalism: if we were brains in a vat, the word "tree" in our language would refer to computer-program trees, not real trees. The argument did not fully satisfy critics, and the brain-in-a-vat scenario became the framing device of the Matrix trilogy, demonstrating how deeply Descartes\' thought experiment had penetrated modern culture.'
        },
        {
            philosopher: 'Bernard Williams',
            text: 'Williams\' Descartes: The Project of Pure Enquiry (1978) is the most philosophically serious modern defence of the Meditations. Williams argued that Descartes was genuinely attempting something philosophically important: to construct an absolute conception of the world — a description of reality not perspectival, not tied to any particular mind\'s point of view. This project, Williams argued, is implicit in the very idea of science seeking objective truth. Williams also gave the most careful analysis of the cogito, arguing it is not a syllogism but a performance — the very act of thinking it demonstrates its truth, making it unlike any other existential proposition.'
        }
    ],

    modernRelevance: 'The Meditations remains the unavoidable starting point of modern philosophy and cognitive science. The problem of consciousness it identified — how can a purely physical brain give rise to subjective experience? — is today called the Hard Problem by David Chalmers and remains entirely unsolved. Every serious attempt to explain mind in purely physical terms must contend with Descartes\' observation that thinking is irreducibly first-personal in a way no third-person physical description can capture. The evil demon has been modernized as the simulation hypothesis — Bostrom\'s argument that we may be living in a computer simulation — which is now taken seriously by physicists and philosophers alike.',

    context: 'Descartes worked on the Meditations throughout the 1630s in the Netherlands. He had the manuscript circulated through Mersenne, who solicited objections from the leading thinkers of the day — Hobbes, Gassendi, Arnauld, Mersenne himself. The six sets of Objections and Replies were published with the first edition in Paris in 1641, making it an extraordinary collaborative document. It was written in Latin — the international scholarly language — to reach the widest philosophical audience. The full title, Meditations on First Philosophy, in which the Existence of God and the Immortality of the Soul are Demonstrated, was strategically chosen to appeal to Church authorities after Galileo\'s condemnation of 1633.',

    relatedWorks: ['discourse-on-method', 'principles-of-philosophy', 'objections-and-replies', 'passions-of-the-soul']
}

);
"""

# ─────────────────────────────────────────────────────────────────────────────
# DATA-11b  —  Discourse on Method + Rules for the Direction of the Mind
# ─────────────────────────────────────────────────────────────────────────────
data_11b = r"""/* ================================================================
   DATA PART 11b — Discourse on Method + Rules for the Direction of the Mind
   ================================================================ */

window.WORKS.push(

/* ──────────────────────────────────────
   1. DISCOURSE ON THE METHOD
────────────────────────────────────── */
{
    id: 'discourse-on-method',
    title: 'Discourse on the Method',
    greekTitle: 'Discours de la méthode',
    philosopher: 'descartes',
    category: 'method',
    categoryLabel: 'Method & Epistemology',
    date: '1637 AD',
    dateSort: 1637,
    emoji: '🔬',
    cardSize: 'normal',
    readingDifficulty: 'Beginner',
    estimatedWordCount: 20000,

    shortDesc: 'The founding manifesto of scientific modernity — Descartes\' intellectual autobiography and the first full statement of "I think, therefore I am," written deliberately in French so that any reasonable person, not just Latin scholars, could evaluate its arguments.',

    summary: 'The Discourse on the Method is one of the most important and accessible texts in the history of Western thought, written not as a dry academic treatise but as a first-person intellectual autobiography. Descartes traces his disillusionment with scholastic education, his travels through Europe seeking wisdom in the "great book of the world," and his eventual decision to demolish all prior beliefs and rebuild knowledge from scratch. Part I recounts his education at La Flèche and his growing conviction that received wisdom, despite its immense learning, rested on uncertain foundations. Part II introduces the four rules of method: accept nothing as true that is not clearly and distinctly known; analyze every problem into its simplest parts; proceed from simple to complex; review everything completely. Part III introduces a provisional morality — rules for living while the theoretical reconstruction is underway: obey the laws and customs of one\'s country, be decisive in action even when uncertain in theory, master oneself rather than fortune. Part IV is philosophically the most important: it presents the argument from doubt to the cogito — "je pense, donc je suis" — and from the cogito derives the existence of God and the criterion of clear and distinct perception. Parts V and VI describe his scientific discoveries and explain why he suppressed Le Monde when Galileo was condemned. Descartes chose French rather than Latin, a radically democratic gesture signaling that truth is accessible to any person who reasons carefully, not merely to the Latin-educated clergy and university scholars.',

    themes: ['Method', 'Reason', 'Doubt', 'The Cogito', 'Science', 'Education', 'Provisional Morality', 'Freedom of Thought', 'Democratic Epistemology'],

    keyCharacters: [
        { name: 'Descartes (narrator)', role: 'The author writes in his own voice as intellectual autobiographer — reflecting on his education, travels, and the development of his method' },
        { name: 'The Scholastic Tradition', role: 'The unnamed institutional antagonist — the university learning Descartes was educated in and found philosophically wanting' }
    ],

    concepts: [
        'Four rules of method — clarity, analysis, synthesis, enumeration; the systematic procedure for arriving at certain knowledge',
        'Cogito ergo sum — I think therefore I am; the formulation in French as je pense, donc je suis that became the most famous sentence in modern philosophy',
        'Provisional morality — practical rules for living while theoretical knowledge is being reconstructed; the gap between philosophical doubt and practical life',
        'Clear and distinct perception — the criterion of truth; whatever is perceived with full clarity and distinctness cannot be false',
        'Democratic epistemology — writing in French to make philosophy accessible to any reasoning person regardless of Latin education'
    ],

    structure: 'Six parts, proceeding from autobiography to science:\n\nPart I: Reflections on education at La Flèche. Disillusionment with the schools.\n\nPart II: The four rules of method. The decision to rebuild all knowledge. The single-architect analogy.\n\nPart III: Provisional morality — three maxims for practical living during the philosophical reconstruction.\n\nPart IV: The cogito. God\'s existence. The criterion of clear and distinct perception.\n\nPart V: Natural philosophy — the heart and blood; animal mechanisms; the distinction between humans and automata.\n\nPart VI: Why the scientific essays are published. The importance of practical science. Why Le Monde was suppressed.',

    quote: 'I think, therefore I am. — Discourse on the Method, Part IV',

    additionalQuotes: [
        { text: 'Good sense is the most evenly distributed thing in the world: for everyone thinks himself so abundantly provided with it that even those who are hardest to satisfy in all other respects are not in the habit of wanting more than they already have.', citation: 'Discourse on the Method, Part I' },
        { text: 'My third maxim was to try always to master myself rather than fortune, and to change my desires rather than the order of the world.', citation: 'Discourse on the Method, Part III' }
    ],

    commentary: [
        {
            philosopher: 'G.W.F. Hegel',
            text: 'Hegel in his Lectures on the History of Philosophy gave Descartes extraordinary credit as the true founder of modern philosophy. What Descartes achieved, Hegel argued, was the discovery that philosophy must begin with thought thinking itself — the subject\'s self-reflection rather than an external given. "Here, we may say, we are at home, and like the mariner after a long voyage in a tempestuous sea, we may now hail the sight of land." Descartes established the principle of subjectivity — the thinking ego as the ground of all knowledge — which Hegel would develop into Absolute Idealism. But Hegel also criticized Descartes for leaving an unbridgeable gulf between the thinking subject and the external world, a gulf only Hegel\'s dialectical system could overcome.'
        },
        {
            philosopher: 'Voltaire',
            text: 'Voltaire\'s Philosophical Letters (1734) praised Descartes as a liberator who freed Europe from Aristotelian scholasticism while criticizing his specific metaphysical claims in light of Newtonian physics. Voltaire celebrated the democratic ambition of writing in French as quintessentially Enlightenment, but he sided with Newton against Descartes on gravity and vortices. For Voltaire, Descartes was heroic precisely because he dared to tear down received knowledge and demand evidence, even if his own replacement turned out to be as speculative as what he demolished. The Discourse\'s skepticism toward authority was its lasting gift to modernity.'
        },
        {
            philosopher: 'Friedrich Nietzsche',
            text: 'Nietzsche\'s critique of the cogito in Beyond Good and Evil (1886) is one of the most incisive philosophical objections to the Discourse\'s central argument. He argued that "I think, therefore I am" is not a primitive certainty but folk metaphysics loaded with unexamined assumptions: that there is an "I" doing the thinking, that thinking requires an agent, that we can identify our mental states with certainty. "A thought comes when it will, not when I will." The I is not known prior to its thoughts but is at most a grammatical fiction required by Indo-European languages that demand a subject for every verb. The cogito, far from being bedrock certainty, smuggles in the most questionable assumption in Western philosophy.'
        },
        {
            philosopher: 'Simone de Beauvoir',
            text: 'De Beauvoir\'s analysis in The Second Sex (1949) identified a profound political dimension to Descartes\' apparently gender-neutral rationalism. The disembodied "I think" — the pure thinking subject stripped of all particular bodily characteristics — was presented as universal, but de Beauvoir showed it consistently mapped onto male experience. The body, associated with woman, was identified as the obstacle to pure reason; transcendence was masculine; immanence was feminine. Cartesian dualism thus encoded a gendered metaphysics that justified excluding women from the republic of reasoners. The Discourse\'s democratic gesture of writing for "anyone who reasons" concealed a definition of reason modelled on a particular historical subject — propertied, European, male.'
        }
    ],

    modernRelevance: 'The Discourse\'s most enduring legacy is its democratic epistemology: the claim that good reasoning is available to any human mind regardless of social position or authority, and that anyone can and should evaluate arguments for themselves. This principle underlies the Enlightenment, democratic political theory, the scientific peer-review system, and contemporary commitments to critical thinking education. The four rules of method — though criticized as oversimplified — are recognizable in the problem-decomposition strategies of modern software engineering. Descartes\' decision to write in the vernacular foreshadowed the internet\'s erosion of expert gatekeeping.',

    context: 'Published anonymously in Leiden in June 1637, accompanied by three scientific essays — the Dioptrics, the Meteors, and the Geometry — that the Discourse was intended to introduce. Descartes had been living quietly in the Netherlands since 1628, deliberately obscure, preferring to avoid the controversies that had engulfed Galileo. The Discourse was the first major philosophical work written in a modern European vernacular, a fact that contributed to French becoming a language of philosophical precision and helped establish the Republic of Letters as a genuinely pan-European intellectual community extending beyond the universities.',

    relatedWorks: ['meditations', 'principles-of-philosophy', 'rules-for-direction-of-mind']
},

/* ──────────────────────────────────────
   2. RULES FOR THE DIRECTION OF THE MIND
────────────────────────────────────── */
{
    id: 'rules-for-direction-of-mind',
    title: 'Rules for the Direction of the Mind',
    greekTitle: 'Regulae ad Directionem Ingenii',
    philosopher: 'descartes',
    category: 'method',
    categoryLabel: 'Method & Epistemology',
    date: 'c.1628 AD (posthumous 1701)',
    dateSort: 1628,
    emoji: '📐',
    cardSize: 'normal',
    readingDifficulty: 'Advanced',
    estimatedWordCount: 35000,

    shortDesc: 'Descartes\' unfinished early masterwork on method — twenty-one completed rules for conducting inquiry through intuition and deduction alone, containing the first sketch of the mathesis universalis: a single universal science unifying all knowledge under mathematical method.',

    summary: 'Written around 1619-1628 but never completed and published only posthumously in 1701, the Rules for the Direction of the Mind gives us Descartes at his most architecturally ambitious and technically precise. It is an early draft of the methodological project that would be summarized in the Discourse and deployed philosophically in the Meditations, here in a rawer and more mathematically detailed form. Descartes projects thirty-six rules divided into three groups of twelve, but completed only the first twenty-one.\n\nRule I establishes the governing aim: all sciences are interconnected and constitute a single science of the universal; one must study the whole rather than individual disciplines in isolation. Rule II introduces the two operations of the pure intellect: intuition — the direct apprehension of a simple, indubitable truth — and deduction — chains of necessary inferences from intuited truths. Rule III warns against probable reasoning. The middle rules develop a theory of simple natures — the most basic, irreducible elements of reality (extension, duration, thought, unity) from which compound truths are built. The later rules introduce the mathesis universalis: the idea that algebra and geometry share a common structural framework extensible to any problem in any domain. This is the conceptual seed of analytic geometry — the Cartesian coordinate system — and of the Enlightenment ideal that all knowledge can be unified under mathematical method.',

    themes: ['Universal Science', 'Intuition and Deduction', 'Simple Natures', 'Mathematical Method', 'Certainty', 'Analytic Geometry', 'Order', 'Unity of Knowledge'],

    keyCharacters: [
        { name: 'The Universal Intellect', role: 'Not a person but a capacity — the Rules address any mind willing to discipline itself through their procedures, regardless of subject matter' }
    ],

    concepts: [
        'Intuition — the direct, clear apprehension of a simple truth requiring no inference; the most basic cognitive act',
        'Deduction — chains of necessary inference from intuited truths; all valid reasoning reduces to intuition and deduction',
        'Simple natures — the irreducible elements of reality: intellectual (thought, doubt), material (extension, motion), common (existence, unity, duration)',
        'Mathesis universalis — the dream of a single universal science unifying algebra and geometry and potentially all disciplines under one formal method',
        'Enumeration — the systematic survey ensuring completeness; no step in a deduction can be missed',
        'Analytic geometry anticipated — the representation of all quantities as line segments, connecting algebra and geometry in a single framework'
    ],

    structure: 'Twenty-one completed rules of thirty-six projected:\n\nRules I-IV: The aim of inquiry — one unified science. The two valid operations — intuition and deduction. Warning against probable reasoning.\n\nRules V-VII: Resolution and enumeration. Problems must be reduced to simplest parts and reconstructed.\n\nRules VIII-XI: Limits of inquiry. Simple propositions vs problems requiring comparison.\n\nRules XII-XXI: Theory of cognition and mathematical method. Simple natures classified. The imagination as tool of intellect. Algebraic representation of all quantities.',

    quote: 'All the sciences are nothing other than human wisdom, which always remains one and the same, however different the subjects to which it is applied. — Rules for the Direction of the Mind, Rule I',

    additionalQuotes: [
        { text: 'By intuition I do not mean the fluctuating testimony of the senses or the misleading judgment of the imagination, but the conception of a clear and attentive mind so easy and distinct that there can be no room for doubt about what we are understanding.', citation: 'Rules, Rule III' },
        { text: 'We should occupy ourselves only with those objects about which our intellect appears capable of having certain and indubitable knowledge.', citation: 'Rules, Rule II' }
    ],

    commentary: [
        {
            philosopher: 'Gottlob Frege',
            text: 'Frege\'s Begriffsschrift (1879) — the invention of formal logic and the founding document of analytic philosophy — can be understood as realizing the program the Rules projected but could not complete. Descartes\' mathesis universalis dreamt of a universal formal language in which all valid reasoning could be expressed and checked mechanically; Frege created one. Where Descartes relied on an irreducible faculty of intellectual intuition to grasp simple truths, Frege sought to eliminate appeals to intuition entirely and ground mathematics purely in logical axioms and rules of inference. The twentieth-century debate between logicism and intuitionism is, in deep structure, a continuation of the methodological ambitions and tensions first articulated in Descartes\' Rules.'
        },
        {
            philosopher: 'John Stuart Mill',
            text: 'Mill\'s A System of Logic (1843) engaged at length with the Cartesian claim that genuine science proceeds from intuited axioms by deduction. Mill rejected this rationalist model entirely. Science, he argued, proceeds not by deduction from self-evident intuitions but by induction from particular observations. His five methods — agreement, difference, concomitant variation, residues, and joint method — were designed as a systematic alternative to Cartesian deductivism. The debate the Rules initiated — whether science is fundamentally deductive-rationalist or inductive-empiricist — remained the central problem of philosophy of science through Popper, Hempel, and Kuhn.'
        },
        {
            philosopher: 'Jean-Paul Sartre',
            text: 'Sartre\'s The Transcendence of the Ego (1936) began from a close reading of the Rules. Sartre argued that Descartes had correctly identified consciousness as the most fundamental datum but wrongly treated it as a thing — a res cogitans with an essence. In Sartre\'s phenomenological ontology, consciousness is not a substance but a pure activity, always directed toward something other than itself, with no inner nature prior to its acts. The Rules\' conception of pure intellectual intuition as a faculty grasping simple natures already exhibits the Cartesian error of treating consciousness as a thing that has properties rather than a transparent activity that is what it does. Sartre\'s formula "existence precedes essence" is, in part, an inversion of the Cartesian model of mind the Rules first articulated.'
        }
    ],

    modernRelevance: 'The Rules\' most consequential legacy is analytic geometry. In Rule XIV, Descartes introduces representing quantities as line segments, treating both geometrical and arithmetical problems with the same symbolic notation. This insight — that algebraic equations and geometric curves are two representations of the same mathematical objects — became the Cartesian coordinate system that made calculus possible and that underlies every computer screen, GPS system, and data visualization today. The mathesis universalis ideal lives on in the computer science dream of algorithmic solutions to all problems and in the artificial intelligence ambition of a unified formal reasoning system.',

    context: 'The Rules were never published by Descartes and exist in several manuscript copies. The most significant was found among Leibniz\'s papers, who had a copy made in 1676. First published in the posthumous Amsterdam Opera Omnia in 1701, over fifty years after Descartes\' death. The earliest portions were probably written around 1619-1620, when Descartes was in his early twenties and had his famous vision on the night of November 10-11, 1619 — when he claimed to have seen, in a dream, the foundations of a "marvellous science." Descartes abandoned the work, most scholars believe, because the program it envisioned — a complete formal calculus of all knowledge — proved far more difficult than initially thought.',

    relatedWorks: ['discourse-on-method', 'meditations', 'principles-of-philosophy']
}

);
"""

# ─────────────────────────────────────────────────────────────────────────────
# DATA-11c  —  Principles of Philosophy
# ─────────────────────────────────────────────────────────────────────────────
data_11c = r"""/* ================================================================
   DATA PART 11c — Principles of Philosophy (Descartes)
   ================================================================ */

window.WORKS.push(

/* ──────────────────────────────────────
   1. PRINCIPLES OF PHILOSOPHY
────────────────────────────────────── */
{
    id: 'principles-of-philosophy',
    title: 'Principles of Philosophy',
    greekTitle: 'Principia Philosophiae',
    philosopher: 'descartes',
    category: 'natural-philosophy',
    categoryLabel: 'Natural Philosophy',
    date: '1644 AD',
    dateSort: 1644,
    emoji: '🌌',
    cardSize: 'wide',
    readingDifficulty: 'Advanced',
    estimatedWordCount: 60000,

    shortDesc: 'Descartes\' most systematic work — a comprehensive four-part architecture of the universe from first principles, presenting in numbered-proposition format the metaphysics, matter theory, cosmology, and physics designed to replace Aristotle as the foundation of all natural science.',

    summary: 'The Principles of Philosophy is Descartes\' most ambitious and comprehensive work, written in the textbook format of numbered propositions so that it could replace Aristotle\'s Physics and the scholastic commentaries as the standard curriculum of natural philosophy. It is divided into four parts.\n\nPart I (Principles of Human Knowledge) covers the metaphysical foundations argued more discursively in the Meditations, now compressed into 76 numbered theses: the method of doubt, the cogito in its famous Latin formulation "Cogito ergo sum," the existence of God, the distinction between mind and body, the nature of substance, and the theory of innate ideas. Part II (Principles of Material Things) develops the physics: Descartes defines matter as identical with extension, rejects atoms and void (empty space is a contradiction since space just is extension, which is material), and establishes three laws of motion: the law of inertia, the conservation of motion in collisions, and the tendency of moving bodies to travel in straight lines.\n\nPart III (The Visible World) applies these principles to cosmology, developing the vortex theory: the solar system consists of whirling fluid vortices carrying the planets around the sun — a purely mechanical account requiring no divine intervention in the ongoing operations of nature. Part IV (The Earth) applies the principles to geology, magnetism, and terrestrial phenomena. The Principles represents the fullest statement of the Cartesian mechanical worldview: a universe of matter-in-motion, governed by mathematical laws, requiring only an initial creative act by God but thereafter running as a perfect machine. It was the system Newton\'s Principia Mathematica (1687) would largely displace, but the framework Newton worked within — inertia, force, the laws of motion — was shaped by the problems and terms Descartes had established.',

    themes: ['Natural Philosophy', 'Cosmology', 'Motion', 'Matter', 'Mechanism', 'God as First Cause', 'Vortex Theory', 'Metaphysical Foundations', 'Inertia'],

    keyCharacters: [
        { name: 'Aristotle (implied antagonist)', role: 'The scholastic tradition whose physics, matter theory, and cosmology the Principles was explicitly designed to replace at the university level' },
        { name: 'God', role: 'The first cause who creates matter and imposes the laws of motion, but thereafter plays no ongoing role in the mechanical universe' }
    ],

    concepts: [
        'Cogito ergo sum — the first appearance of the Latin formulation; Part I Article 7',
        'Extension as the essence of matter — matter is not defined by hardness, colour, or weight but by occupying three-dimensional space',
        'The plenum — no void or vacuum; empty space is a contradiction since space just is extension, which is material',
        'Three laws of motion — the law of inertia; conservation of motion quantity in collisions; rectilinear tendency of moving bodies',
        'Vortex theory — planets are carried in whirling fluid vortices of subtle matter around the sun; the first fully mechanical cosmology',
        'Mechanical philosophy — all natural phenomena, from planetary motion to magnetism to heat, explained by contact mechanics alone',
        'Philosophy as a tree — metaphysics is the roots, physics is the trunk, medicine, mechanics, and morals are the fruit-bearing branches'
    ],

    structure: 'Four parts in numbered-proposition format (504 articles total):\n\nPart I — Principles of Human Knowledge (76 articles): Metaphysical foundations. The cogito. God\'s existence. Substance and its attributes. The theory of knowledge.\n\nPart II — Principles of Material Things (64 articles): The essence of matter is extension. No vacuum. The three laws of nature. Rules of collision.\n\nPart III — The Visible World (138 articles): Vortex cosmology. Formation of sun and stars. Motion of planets. The solar system as self-sustaining mechanical system.\n\nPart IV — The Earth (228 articles): Formation of the Earth. Gravity as centrifugal force in vortices. Magnetism. Terrestrial phenomena.',

    quote: 'Cogito ergo sum — I think, therefore I am. — Principles of Philosophy, Part I, Article 7',

    additionalQuotes: [
        { text: 'In order to seek truth, it is necessary once in the course of our life to doubt, as far as possible, of all things.', citation: 'Principles of Philosophy, Part I, Article 1' },
        { text: 'Give me extension and motion, and I will construct the world.', citation: 'Attributed to Descartes — summarizing the program of the Principles' },
        { text: 'The nature of matter, or body considered in general, consists not in its being hard or heavy or coloured, or one that affects our senses in some other way, but solely in the fact that it is a substance extended in length, breadth and depth.', citation: 'Principles of Philosophy, Part II, Article 4' }
    ],

    commentary: [
        {
            philosopher: 'Isaac Newton',
            text: 'Newton\'s Principia Mathematica (1687) was written, in part, as a systematic demolition of Cartesian physics. The very title — borrowing "Principia" from Descartes — signals both homage and supersession. Newton rejected the vortex theory by showing mathematically that vortices would produce the wrong orbital velocities and could not account for Kepler\'s ellipses. More fundamentally, Newton rejected the identification of matter with extension by positing absolute space and a universal gravitational force acting at a distance — exactly what Descartes had denied. Yet Newton\'s framework retained deeply Cartesian assumptions: the mechanistic conception of nature governed by mathematical laws, the divine clockmaker who sets the machine running, and inertia. Cartesian physics was Newton\'s necessary precondition even as it was his primary target.'
        },
        {
            philosopher: 'Gottfried Wilhelm Leibniz',
            text: 'Leibniz engaged with the Principles at technical depth throughout his career. His most celebrated critique targeted Descartes\' theory of motion in Part II. Descartes defined the conserved quantity as mass times speed (a scalar); Leibniz showed in his "Brief Demonstration of a Notable Error of Descartes" (1686) that what is actually conserved is vis viva — mass times the square of velocity. This dispute over whether mv or mv² is conserved became the vis viva controversy that animated eighteenth-century physics, and Leibniz was right, anticipating the modern concept of kinetic energy. Leibniz also objected that Descartes\' purely geometrical conception of matter, devoid of force and activity, produced a dead universe inconsistent with God\'s goodness.'
        },
        {
            philosopher: 'Elisabeth of Bohemia',
            text: 'Princess Elisabeth, Descartes\' most philosophically penetrating correspondent, posed in 1643 the question the Principles never adequately resolved: if mind is thinking substance with no extension and body is extended substance with no thought, how can the mind move the body? This mind-body interaction problem strikes at the heart of the Cartesian dualism the Principles systematizes. Descartes\' responses were notoriously evasive — he invoked the "primitive notion" of union and suggested the interaction was experienced but not conceptualized through his official metaphysical categories. Many philosophers have concluded he never solved this problem. Elisabeth\'s correspondence is now regarded as a foundational document in the philosophy of mind.'
        },
        {
            philosopher: 'Nicolas Malebranche',
            text: 'Malebranche developed the Principles\' physics and metaphysics in his Search After Truth (1674-1675) in a direction Descartes had not anticipated. Accepting Cartesian dualism fully — mind and body have truly nothing in common — Malebranche concluded that causal interaction between them is not just mysterious but impossible. His solution was occasionalism: God is the only genuine cause; when my mind "wills" to move my arm, this is the occasion for God to move it; when my arm is struck, this is the occasion for God to produce pain in my mind. Malebranche used this result as evidence of God\'s continuous presence in all natural events. His occasionalism influenced Hume\'s skepticism about causation: if even mind moving body turns out not to be genuine causation, perhaps all causation is similarly doubtful.'
        }
    ],

    modernRelevance: 'The Principles established the framework — a mathematized, mechanistic nature governed by universal laws — within which modern physics developed. Descartes\' identification of matter with extension was wrong, but the philosophical claim that the material world is fully intelligible through mathematics and law is the axiom of all modern physical science. His vortex cosmology failed empirically, but the ideal of a purely mechanical cosmology requiring no ongoing divine intervention became the working assumption of Enlightenment science and remains the default of secular scientific culture. The concept of inertia — borrowed and generalized by Newton — is in every high school physics textbook.',

    context: 'Published in Amsterdam in 1644, dedicated to Princess Elisabeth of Bohemia. Descartes explicitly designed it as a replacement for scholastic Aristotle textbooks used in Jesuit colleges, hoping it would be adopted as the standard curriculum. A French translation by Abbé Picot, which Descartes revised and expanded, appeared in 1647. In the preface to the French edition, Descartes gave his famous metaphor: philosophy is a tree whose roots are metaphysics, trunk is physics, and branches — bearing the fruits that nourish life — are medicine, mechanics, and morals.',

    relatedWorks: ['meditations', 'discourse-on-method', 'the-world', 'passions-of-the-soul']
}

);
"""

# ─────────────────────────────────────────────────────────────────────────────
# DATA-11d  —  Passions of the Soul + The World
# ─────────────────────────────────────────────────────────────────────────────
data_11d = r"""/* ================================================================
   DATA PART 11d — Passions of the Soul + The World (Le Monde)
   ================================================================ */

window.WORKS.push(

/* ──────────────────────────────────────
   1. PASSIONS OF THE SOUL
────────────────────────────────────── */
{
    id: 'passions-of-the-soul',
    title: 'Passions of the Soul',
    greekTitle: "Les Passions de l'âme",
    philosopher: 'descartes',
    category: 'psychology',
    categoryLabel: 'Psychology & Ethics',
    date: '1649 AD',
    dateSort: 1649,
    emoji: '❤️',
    cardSize: 'normal',
    readingDifficulty: 'Intermediate',
    estimatedWordCount: 34000,

    shortDesc: 'Descartes\' final published work and his only systematic treatment of ethics and psychology — a pioneering scientific analysis of the six primitive passions as bodily mechanisms, and a guide to mastering them through wisdom and self-knowledge.',

    summary: 'The Passions of the Soul, published months before Descartes\' death, is his most psychologically and ethically concrete work — directly provoked by the correspondence with Princess Elisabeth of Bohemia, who had pressed him for years to show how his dualist metaphysics could account for the mind-body unity of emotional life. Part I treats the passions physiologically and metaphysically: the passions are perceptions or emotions of the soul caused and maintained by animal spirits (fine vapours in the blood) transmitted through the nerves. Descartes locates the primary site of mind-body interaction in the pineal gland — then believed to be the only unpaired organ in the brain and therefore the seat of the soul. Part II enumerates the six primitive passions: wonder, love, hatred, desire, joy, and sadness. All other emotional states are compounds or species of these six, each analyzed physiologically and functionally — what movements of animal spirits cause it, what purpose it serves in preparing the body for action. Part III addresses the governance of the passions through wisdom: the goal is not to eliminate the passions — they are necessary for life and often beneficial — but to ensure that the soul\'s judgements govern what they dispose one toward. The work concludes with an analysis of generosity — Descartes\' technical term for the knowledge that one\'s will is free combined with a firm resolution to always use it well — as the key to all virtue and happiness.',

    themes: ['Passions and Emotions', 'Mind-Body Union', 'Virtue', 'Happiness', 'Self-Mastery', 'Generosity', 'Wonder', 'Physiology of Emotion', 'Free Will'],

    keyCharacters: [
        { name: 'Princess Elisabeth', role: 'Not present in the text but its intellectual origin — her questions about mind-body interaction and living well under adversity prompted Descartes to address emotion, virtue, and practical ethics' }
    ],

    concepts: [
        'Six primitive passions — wonder, love, hatred, desire, joy, sadness; all other emotions are compounds of these six',
        'Animal spirits — fine vapours in the blood that transmit the body\'s states to the soul through the nerves; the physiological mechanism of emotion',
        'Pineal gland — the seat of the soul; the site where mind and body interact in Cartesian physiology',
        'Wonder as the primary passion — admiration of what is rare or extraordinary; the passion that motivates all intellectual inquiry',
        'Generosity — Descartes\' master virtue: knowing one\'s will is free and resolving always to use it well; the foundation of self-respect and respect for others',
        'Virtue as self-mastery — not suppression of the passions but governance of them through understanding their causes and redirecting them rationally'
    ],

    structure: 'Three parts:\n\nPart I (50 articles): The passions in general. Animal spirits. The pineal gland. How soul moves body and body affects soul.\n\nPart II (70 articles): The six primitive passions — wonder, love, hatred, desire, joy, sadness — analyzed physiologically and functionally.\n\nPart III (80 articles): Specific passions — esteem, contempt, generosity, pride, humility, gratitude, envy. Mastery of the passions. Generosity as the master virtue. Happiness as the result of right use of the will.',

    quote: 'The utility of all the passions consists in their strengthening and prolonging thoughts which it is good for the soul to preserve. — Passions of the Soul, Article 74',

    additionalQuotes: [
        { text: 'Wonder is a sudden surprise of the soul which causes it to apply itself to consider with attention the objects which seem to it rare and extraordinary.', citation: 'Passions of the Soul, Article 70' },
        { text: 'Those whom generosity makes noble are naturally led to do great things, and yet to undertake nothing they do not feel they can accomplish.', citation: 'Passions of the Soul, Article 157' },
        { text: 'The free will is of itself the noblest thing we can have, for it makes us in a certain manner equal to God and exempts us from being his subjects.', citation: 'Passions of the Soul, Article 152' }
    ],

    commentary: [
        {
            philosopher: 'Baruch Spinoza',
            text: 'Spinoza\'s treatment of the emotions in Parts III and IV of the Ethics (1677) is explicitly designed as a correction of Descartes\' account. Spinoza accepted Descartes\' project of analyzing emotions scientifically but rejected both his dualism and his theory of mastery. For Spinoza, mind and body are not two substances but two attributes of one; the passions are not caused by the body acting on the soul but are simply the mental aspect of bodily changes. Most importantly, Spinoza rejected Descartes\' belief that the will can master the passions through reason: we are in bondage to the passions not because of weakness of will but because we do not fully understand what we desire. Freedom comes not from mastering the passions by will but from achieving adequate understanding of oneself. Spinoza considered Descartes\' doctrine of rational willpower over the passions a philosophical fairy tale.'
        },
        {
            philosopher: 'William James',
            text: 'James\'s James-Lange theory of emotion (1884) reverses common-sense Cartesianism — and returns, from a different angle, to something close to Descartes\' own position. Common sense says we feel afraid and therefore run; James says we run and therefore feel afraid — the emotion just is the perception of the bodily state. Descartes had argued that the passions are perceptions caused by bodily states (animal spirits); James agreed that emotions are perceptions of bodily changes. But James denied Descartes\' further claim that the soul can intervene to redirect these passions through the will. The debate between these positions — whether emotion is primarily bodily or involves irreducible mental evaluation — continues in contemporary affective neuroscience.'
        },
        {
            philosopher: 'Martha Nussbaum',
            text: 'Nussbaum\'s Upheavals of Thought: The Intelligence of Emotions (2001) engages with the Passions\' ambition of a philosophical theory of emotion while rejecting its mechanistic framework. For Nussbaum, emotions are not mere physiological disturbances perceived by the soul but evaluative judgements about what matters — they have propositional content and are appropriate or inappropriate to their objects. Grief is not a disturbance of animal spirits but a judgement that something valued has been lost. Nussbaum follows the Stoics and Aristotle against Descartes in treating emotions as cognitively complex and evaluatively rational. Nevertheless, she shares Descartes\' central conviction that emotional life can be cultivated through philosophical self-understanding toward greater wisdom and human flourishing.'
        }
    ],

    modernRelevance: 'The Passions of the Soul is the first work in the Western tradition to treat the emotions as a proper subject of scientific investigation — analyzing their causes, physical substrates, functional roles, and relationship to virtue. This project is the ancestor of modern affective neuroscience: Antonio Damasio\'s somatic marker hypothesis in Descartes\' Error (1994) restores what Damasio calls the Cartesian programme while inverting its conclusions. Descartes\' specific claim about the pineal gland was wrong, but his conviction that emotional states have identifiable neural correlates and can be understood mechanistically drives the entire field of emotion research.',

    context: 'Written at the instigation of Princess Elisabeth, with whom Descartes had corresponded since 1643 about mind-body interaction and how to live well under adversity. Elisabeth suffered from persistent depression she attributed to the stress of her family\'s political exile and asked Descartes to address how reason governs the passions. He developed the correspondence into the treatise and also sent a copy to Queen Christina of Sweden. The Passions was the last work Descartes published. He arrived in Stockholm in October 1649 and died of pneumonia on February 11, 1650 — less than four months after the book appeared in print.',

    relatedWorks: ['meditations', 'principles-of-philosophy', 'objections-and-replies', 'descartes-correspondence']
},

/* ──────────────────────────────────────
   2. THE WORLD (LE MONDE)
────────────────────────────────────── */
{
    id: 'the-world',
    title: 'The World',
    greekTitle: 'Le Monde, ou Traité de la Lumière',
    philosopher: 'descartes',
    category: 'natural-philosophy',
    categoryLabel: 'Natural Philosophy',
    date: '1633 AD (written); 1664 AD (published)',
    dateSort: 1633,
    emoji: '🌍',
    cardSize: 'normal',
    readingDifficulty: 'Intermediate',
    estimatedWordCount: 30000,

    shortDesc: 'The suppressed masterwork — Descartes\' complete mechanistic and heliocentric cosmology, abandoned in manuscript when Galileo was condemned for teaching the same theory, and published only fourteen years after Descartes\' death.',

    summary: 'Le Monde is one of the great what-ifs in the history of science. By November 1633, Descartes had nearly completed a comprehensive treatise presenting a fully mechanistic, heliocentric cosmology — the universe as an indefinitely extended plenum of matter in which all natural phenomena, from light and heat to planetary motion and magnetism, are explained by contact mechanics alone. Then came the news of Galileo\'s condemnation by the Roman Inquisition for teaching the motion of the Earth. Descartes immediately suppressed the manuscript: "Since all the things I explained in my treatise formed a connected whole, the slightest fault in it would have ruined the whole. But I saw that all the things I talked about depended on Galileo\'s opinion, so I preferred to hide it."\n\nThe text as we have it consists of two related parts. The Treatise on Light (Le Monde proper) presents a mechanical account of nature beginning with fire and heat, developing through a theory of light as a tendency of motion in a material medium — a proto-wave theory — and culminating in a heliocentric cosmology driven by vortices of subtle matter. The Treatise on Man presents the human body as a machine: the heart as a pump, the nervous system as hydraulic tubes, perception and motion as mechanical processes. This last section, published separately in 1662, was particularly influential and represents the first fully mechanistic account of the living body in Western thought.',

    themes: ['Heliocentrism', 'Mechanism', 'Light', 'Cosmology', 'The Body as Machine', 'Science and Religion', 'Censorship', 'Vortex Theory'],

    keyCharacters: [
        { name: 'Galileo (implicit presence)', role: 'Whose condemnation caused Descartes to suppress the work — his shadow falls over every page of the manuscript\'s history and its delayed publication' }
    ],

    concepts: [
        'Heliocentric cosmology — the Earth moves around the sun; the same position for which Galileo was condemned',
        'Light as tendency of motion — a pressure transmitted instantaneously through a material medium; Descartes\' proto-wave theory of light',
        'The body as machine — all physiological processes including circulation, digestion, and movement are mechanical; no vital spirits required',
        'Plenum — no empty space; the universe is entirely filled with matter in various degrees of fineness',
        'The thought-experiment universe — Descartes presents his cosmology as describing a hypothetical new world God might have created, to avoid direct conflict with Genesis'
    ],

    structure: 'Two related treatises:\n\nTreatise on Light (Le Monde, 15 chapters): Fire and light. The "new world" thought experiment. Properties and laws of matter. Early statement of inertia. Vortex formation of sun, planets, earth.\n\nTreatise on Man (L\'Homme, unfinished): The heart as thermodynamic pump. Circulation. The nervous system as hydraulic tubes. Perception as mechanical. Memory as traces in the brain. The pineal gland as the seat of the soul.',

    quote: 'I desire you to consider that these functions follow from the mere arrangement of the machine\'s organs every bit as naturally as the movements of a clock or other automaton follow from the arrangement of its counter-weights and wheels. — Treatise on Man',

    additionalQuotes: [
        { text: 'Light is nothing other, in the objects we call luminous, than a certain movement or action, very rapid and very lively, that passes to our eyes by means of the air and other transparent bodies.', citation: 'The World, Chapter I' }
    ],

    commentary: [
        {
            philosopher: 'Julien Offray de La Mettrie',
            text: 'La Mettrie\'s Man a Machine (1748) took Descartes\' mechanistic account of the body in Le Monde and drew the conclusion Descartes had carefully avoided: if the human body is a machine, there is no reason to posit a separate soul. La Mettrie simply extended Descartes\' mechanics from the body to the mind, eliminating the res cogitans entirely. He pointed out that variations in brain chemistry — fever, madness, wine — systematically alter thought, exactly what a purely material account predicts and Cartesian dualism struggles to explain. La Mettrie was expelled from France and then the Netherlands for this argument. His work marks the moment when Cartesian mechanism became French materialist atheism — a transformation Descartes, who had carefully grounded his system in God and the immortal soul, would surely have disavowed.'
        },
        {
            philosopher: 'Christiaan Huygens',
            text: 'Huygens, the greatest Dutch physicist of the seventeenth century, developed Le Monde\'s theory of light in his Traité de la Lumière (1690). Huygens formulated the wave theory of light, arguing that light propagates as a pressure wave through a material medium — a direct extension of Descartes\' conception of light as a tendency of motion through matter. Huygens\' wave theory could explain reflection and refraction more successfully than Newton\'s competing corpuscular theory. The great nineteenth-century debate between wave and corpuscular theories of light — resolved by Maxwell\'s electromagnetic theory and then complicated by quantum wave-particle duality — is the continuation of the Cartesian vision of Le Monde that Huygens first made mathematically rigorous.'
        }
    ],

    modernRelevance: 'Le Monde represents the first fully mechanistic account of the cosmos and of life — the conceptual ancestor of modern biology\'s commitment to explaining living processes in purely physical and chemical terms. The Treatise on Man\'s vision of the body as a machine drives modern medicine, neuroscience, and the philosophy of artificial intelligence. If the body is a machine and the brain processes information mechanically, then in principle an artificial machine could replicate any cognitive function — the premise of all computer science and AI research. Descartes\' suppression of the work for fear of the Inquisition remains a resonant episode about the relationship between scientific freedom and institutional power.',

    context: 'Descartes worked on Le Monde from approximately 1629 to 1633. He wrote to Mersenne in November 1633 that he had been about to send the completed manuscript when Galileo\'s condemnation reached him. The Treatise on Man was published separately in 1662; the Treatise on Light appeared in 1664. Leibniz obtained copies of the manuscripts and was significantly influenced by their mechanical physics. The suppression of Le Monde is often cited as a turning point: had it been published in 1633, the priority dispute with Newton might have been much sharper and the history of seventeenth-century science considerably different.',

    relatedWorks: ['principles-of-philosophy', 'discourse-on-method', 'meditations']
}

);
"""

# ─────────────────────────────────────────────────────────────────────────────
# DATA-11e  —  Objections and Replies + Correspondence
# ─────────────────────────────────────────────────────────────────────────────
data_11e = r"""/* ================================================================
   DATA PART 11e — Objections and Replies + Correspondence
   ================================================================ */

window.WORKS.push(

/* ──────────────────────────────────────
   1. OBJECTIONS AND REPLIES
────────────────────────────────────── */
{
    id: 'objections-and-replies',
    title: 'Objections and Replies',
    greekTitle: 'Objectiones et Responsiones',
    philosopher: 'descartes',
    category: 'metaphysics',
    categoryLabel: 'Metaphysics & Epistemology',
    date: '1641 AD',
    dateSort: 1641,
    emoji: '⚔️',
    cardSize: 'normal',
    readingDifficulty: 'Advanced',
    estimatedWordCount: 90000,

    shortDesc: 'The longest and most combative of Descartes\' works — seven sets of objections from Europe\'s leading thinkers (Hobbes, Arnauld, Gassendi, Mersenne) and Descartes\' detailed replies, published with the Meditations as a live philosophical debate.',

    summary: 'The Objections and Replies is unique in the history of philosophy: a foundational text published together with the full record of its first critical reception, making the Meditations not a monologue but a structured dialogue between Descartes and the sharpest minds of his time. Marin Mersenne circulated the manuscript of the Meditations and solicited responses from six contemporaries; a seventh set was added in the second edition.\n\nThe First Objections from the Dutch theologian Johannes Caterus focus on the ontological argument. The Second Objections, compiled by Mersenne, raise foundational problems about the cogito, God, and the criterion of clear and distinct perception; they include Descartes\' two requested "synthetic" expositions of his argument in the geometrical manner. The Third Objections — the sharpest and most aggressive — come from Thomas Hobbes, who attacked Descartes\' immaterialist conception of the mind from a thoroughgoing materialist standpoint, arguing that thought requires a material substrate and that Descartes had simply assumed what he needed to prove. The Fourth Objections from Antoine Arnauld are the most technically penetrating, raising the Cartesian Circle problem and the mind-body interaction puzzle. The Fifth Objections from Pierre Gassendi run to book length and constitute an alternative atomist philosophy that challenges virtually every Cartesian assumption. The Seventh Objections from the Jesuit Pierre Bourdin, added in 1642, are so persistently obtuse that Descartes replied with barely disguised contempt.\n\nTogether they constitute a philosophical symposium in which the major alternatives to Cartesian philosophy — materialism (Hobbes), atomism (Gassendi), Augustinian theology (Arnauld) — encounter its founder at full argumentative force.',

    themes: ['Metaphysical Debate', 'Mind and Matter', 'God and Certainty', 'Cartesian Circle', 'Mind-Body Interaction', 'Materialism vs Dualism', 'Atomism', 'Early Modern Philosophy'],

    keyCharacters: [
        { name: 'Thomas Hobbes', role: 'Materialist antagonist in the Third Objections — argues that thinking requires matter and that an immaterial mind is incoherent; at the opposite metaphysical pole from Descartes' },
        { name: 'Antoine Arnauld', role: 'Jansenist theologian in the Fourth Objections — the most sympathetic but most logically acute critic; raises the Cartesian Circle and the mind-body interaction problem' },
        { name: 'Pierre Gassendi', role: 'Epicurean atomist in the Fifth Objections — mounts the most comprehensive alternative philosophy; his materialism anticipates modern physicalism' },
        { name: 'Marin Mersenne', role: 'Descartes\' closest correspondent and the compiler of the objections — the intellectual hub connecting all of seventeenth-century European philosophy' }
    ],

    concepts: [
        'Cartesian Circle — the charge that Descartes uses clear and distinct perception to prove God and uses God to validate clear and distinct perception; the deepest logical problem in the system',
        'Mind-body interaction problem — if mind and body are truly distinct substances with nothing in common, how can they causally interact at all?',
        'Materialist challenge (Hobbes) — thinking requires a material substrate; the inference from "I think" to "I am a thinking thing" smuggles in the very immaterialist conclusion at issue',
        'Atomist challenge (Gassendi) — Descartes\' rejection of the void and his identification of matter with extension are both false; real physics requires atoms and empty space',
        'The synthetic method — Descartes\' presentation of his philosophy in the geometrical manner with definitions, postulates, axioms, and propositions, requested by the Second Objectors'
    ],

    structure: 'Seven sets of objections with interleaved replies:\n\nFirst Objections (Caterus): God\'s existence; the ontological argument. Brief and largely cordial.\n\nSecond Objections (Mersenne et al.): The cogito; God; skepticism. Includes Descartes\' geometric exposition.\n\nThird Objections (Hobbes): Mind as material. Thinking requires a corporeal subject. The cogito does not prove immateriality.\n\nFourth Objections (Arnauld): The Cartesian Circle. Mind-body interaction. The most searching philosophical objections.\n\nFifth Objections (Gassendi): Book-length atomist critique of every aspect of the Meditations.\n\nSixth Objections (Mersenne et al.): Theological and ethical concerns.\n\nSeventh Objections (Bourdin, 1642): Jesuit objections; Descartes\' reply includes extended sarcasm directed at their obtuseness.',

    quote: 'You are a mind, or thought. But what does that prove? The question is not what you are, but what you are doing when you think. — Hobbes, Third Objections (paraphrasing the challenge)',

    additionalQuotes: [
        { text: 'You say you are a thinking thing; but what evidence do you have that a corporeal thing cannot think?', citation: 'Hobbes, Third Objections' },
        { text: 'I am asking whether you, who are able to know everything through your own thought, can distinguish dreaming from waking.', citation: 'Mersenne, Second Objections' }
    ],

    commentary: [
        {
            philosopher: 'Thomas Hobbes',
            text: 'The Third Objections reveal Hobbes and Descartes as the two defining poles of seventeenth-century philosophy: one a thoroughgoing materialist, the other a committed dualist. Hobbes pressed Descartes at every joint: if thought is always the thought of something — an image, a concept — then thought requires a material substrate to host it. The inference from "I think" to "I am a thinking thing" does not prove the thing is immaterial; perhaps it is a brain or a material process. Hobbes\' objections were the most philosophically radical Descartes received, and his replies were notably dismissive — he accused Hobbes of simply failing to understand the argument. The sharpness of their disagreement defined the subsequent history of philosophy of mind.'
        },
        {
            philosopher: 'Antoine Arnauld',
            text: 'Arnauld\'s Fourth Objections are universally regarded as the most technically penetrating of the seven sets. The Cartesian Circle he formulated has never been resolved to everyone\'s satisfaction. Arnauld also noted an implication Descartes had not drawn: if the mind is known better than the body and can exist without it, then women have souls as fully as men — undermining, in 1641, a millennium of theological tradition that had treated women\'s rationality as inferior. Arnauld\'s later Port-Royal Logic (1662, written with Nicole) developed many of the epistemological distinctions clarified in this correspondence, making it one of the founding documents of early modern logic.'
        },
        {
            philosopher: 'Pierre Gassendi',
            text: 'Gassendi\'s Fifth Objections constitute an alternative philosophical system rather than mere criticism. His atomism — reviving Epicurus and Lucretius against Descartes\' plenum and vortices — anticipates both the Newtonian acceptance of empty space and the modern atomic theory of matter. Gassendi also pressed the most uncomfortable empiricist objection: when Descartes says he clearly and distinctly perceives the mind as distinct from the body, how does he know this clear and distinct perception is not itself a bodily state? The criterion of clear and distinct perception cannot be used to validate itself. Descartes\' replies to Gassendi were notoriously contemptuous, which many scholars have read as a sign that the objections were more troubling than he wished to admit.'
        }
    ],

    modernRelevance: 'The Objections and Replies established the philosophical genre of adversarial peer review — the idea that a philosophical position is not established until it has survived the best available objections. Every modern philosophical journal article that presents and responds to objections is working in the format Mersenne created in 1641. The specific objections raised have been continuously productive: the Cartesian Circle remains a live problem in epistemology; the Hobbesian materialist challenge to dualism is the ancestor of all physicalist philosophies of mind; and Gassendi\'s empiricist objections to the criterion of clear and distinct perception anticipate the entire post-Cartesian epistemological tradition.',

    context: 'Mersenne circulated the Meditations manuscript in late 1640, soliciting responses from Caterus, Hobbes, Arnauld, Gassendi, and others. The first edition (Paris, 1641) included six sets of Objections and Replies. The second edition (1642) added Bourdin\'s Seventh Objections. The total text of the Objections and Replies is significantly longer than the Meditations themselves, making the combined work a collaborative philosophical symposium unique in the history of the discipline.',

    relatedWorks: ['meditations', 'principles-of-philosophy', 'descartes-correspondence']
},

/* ──────────────────────────────────────
   2. CORRESPONDENCE
────────────────────────────────────── */
{
    id: 'descartes-correspondence',
    title: 'Correspondence',
    greekTitle: 'Correspondance',
    philosopher: 'descartes',
    category: 'method',
    categoryLabel: 'Letters',
    date: '1619–1650 AD',
    dateSort: 1635,
    emoji: '📬',
    cardSize: 'normal',
    readingDifficulty: 'Advanced',
    estimatedWordCount: 200000,

    shortDesc: 'Over a thousand letters spanning thirty years — the workshop and autobiography of Cartesian philosophy, documenting Descartes\' exchanges with Princess Elisabeth, Queen Christina, Mersenne, and the full intellectual life of seventeenth-century Europe.',

    summary: 'Descartes\' correspondence, collected in eleven volumes in the Adam-Tannery edition, comprises over a thousand letters and is one of the most important documentary records in the history of early modern philosophy. Unlike the published works — which are polished, strategically constructed, and often deliberately obscure on sensitive points — the letters reveal Descartes thinking in real time, responding to pressures he could not always anticipate, and occasionally acknowledging difficulties he preferred not to confront in print.\n\nThe most philosophically consequential exchange is the correspondence with Princess Elisabeth of Bohemia, begun in 1643 and continuing until Descartes\' death. Elisabeth posed, with characteristic precision, the question that the published works had evaded: given the real distinction between mind and body, by what means does the soul move the body? This question — now known as the mind-body interaction problem — Descartes acknowledged he could not answer within his official metaphysics. He responded by positing a third "primitive notion" of the union of mind and body, experienced directly in ordinary life but irreducible to either the metaphysics of thought or the mechanics of extension. This admission, made in correspondence but not in the published works, is one of the most significant moments in Cartesian philosophy and has shaped subsequent readings of the entire system.\n\nThe correspondence with Mersenne is philosophically and scientifically the most extensive: it documents Descartes\' scientific discoveries, his mathematical work, his suppression of Le Monde, and his gradual construction of the published system from 1629 to 1644. Mersenne acted as Descartes\' intellectual agent in Paris, communicating with philosophers, mathematicians, and natural philosophers on his behalf and transmitting their objections and queries.\n\nThe exchange with Queen Christina of Sweden — who invited Descartes to Stockholm and whose early-morning philosophy lessons in the cold Swedish winter are believed to have contributed to the pneumonia that killed him — is shorter but humanly poignant: a great philosopher accepting a royal invitation he did not want, dying in a foreign country at the height of his powers.',

    themes: ['Mind-Body Interaction', 'The Third Primitive Notion', 'Intellectual Friendship', 'Scientific Discovery', 'Philosophical Correspondence', 'Suppression of Le Monde', 'Mathematics', 'Ethics and Virtue'],

    keyCharacters: [
        { name: 'Princess Elisabeth of Bohemia', role: 'Descartes\' most philosophically penetrating correspondent — her precise and persistent questions about mind-body interaction forced him to acknowledge limits in his published system that the Meditations and Principles had carefully concealed' },
        { name: 'Marin Mersenne', role: 'Descartes\' closest friend and intellectual agent in Paris — the hub of the Republic of Letters who connected Descartes with every significant thinker in Europe over three decades' },
        { name: 'Queen Christina of Sweden', role: 'Who invited Descartes to Stockholm in 1649 and whose 5 a.m. philosophy lessons in the Swedish winter almost certainly contributed to his death from pneumonia in February 1650' }
    ],

    concepts: [
        'The third primitive notion — the union of mind and body experienced directly in emotional and practical life; irreducible to either thought or extension',
        'Mind-body interaction acknowledged — in letters to Elisabeth, Descartes admits the interaction cannot be explained by his official metaphysics and appeals to lived experience',
        'Philosophical friendship as cognitive practice — the correspondence with Elisabeth and Mersenne as a model of how rigorous intellectual exchange advances understanding',
        'The development of the system — the letters to Mersenne document the gradual construction of the Cartesian philosophy from early sketches to the published works'
    ],

    structure: 'The correspondence is organized chronologically in the Adam-Tannery edition (AT Vols I-V, with supplements). Key clusters: early letters on mathematics and physics (1619-1629); the Dutch period and construction of the system (1629-1637); the period of publication (1637-1641); the Elisabeth correspondence on mind, body, and virtue (1643-1649); the final years and Stockholm (1649-1650).',

    quote: 'I confess that your Highness has well observed a defect in my writings on these subjects. I confess that the explanation I give in my Meditations for how the soul moves the body is very obscure, and I cannot give a better one. — Descartes to Princess Elisabeth, June 28, 1643',

    additionalQuotes: [
        { text: 'There is a great difference between happiness and the highest good. Happiness is not the highest good but only the contentment of the mind which comes from knowing one possesses it.', citation: 'Descartes to Elisabeth, August 4, 1645' },
        { text: 'I have never made much of the things that come from my own mind. And when I have sometimes had the fortune to discover some truths in the sciences, I have been surprised, as if finding a treasure by chance.', citation: 'Descartes to Mersenne, March 1637' }
    ],

    commentary: [
        {
            philosopher: 'Margaret Cavendish',
            text: 'Cavendish, the Duchess of Newcastle and one of the few women of her time writing systematic natural philosophy, engaged critically with Cartesian mechanism in her Observations Upon Experimental Philosophy (1666) and Philosophical Letters (1664). She targeted precisely the difficulty Elisabeth had raised: Cartesian dualism cannot explain how an immaterial soul acts on an entirely mechanical body. Cavendish\'s own solution was a thoroughgoing hylozoism — all matter is alive and sentient to some degree — which dissolves the problem by refusing the sharp mind-body distinction that creates it. Cavendish knew of Elisabeth\'s philosophical exchange with Descartes and considered it one of the few genuine philosophical conversations between a man and a woman in the history of the discipline.'
        },
        {
            philosopher: 'Lisa Shapiro',
            text: 'Shapiro\'s scholarly edition and study of the Descartes-Elisabeth correspondence (2007) has been decisive for contemporary reassessment of both figures. Shapiro showed that Elisabeth\'s objections are not merely requests for clarification but genuine philosophical advances: her insistence that the mind-body interaction cannot be explained within Descartes\' official metaphysics forced the admission of the third primitive notion, which constitutes a significant modification of the system. Shapiro also showed that Elisabeth\'s questions about virtue, the passions, and the good life shaped the Passions of the Soul in ways Descartes\' text does not fully acknowledge. Elisabeth is not merely a student but a philosophical interlocutor who changed the direction of Cartesian philosophy in its final phase.'
        },
        {
            philosopher: 'Daniel Garber',
            text: 'Garber\'s Descartes Embodied (2001) drew extensively on the correspondence to reconstruct Descartes\' natural philosophy — the physics, chemistry, and biology that occupied most of his actual working time but that is overshadowed in philosophy curricula by the Meditations. The letters to Mersenne document a Descartes far more engaged with concrete scientific problems — optics, anatomy, meteorology, the nature of fire — than the published works suggest. Garber argued that the standard philosophical portrait of Descartes as primarily a metaphysician whose physics was derivative is a distortion created by later philosophical canonization. The correspondence reveals that Descartes was first and foremost a natural philosopher whose metaphysics was constructed to support and legitimate his science.'
        }
    ],

    modernRelevance: 'The Descartes-Elisabeth correspondence has become a foundational text in feminist history of philosophy, establishing that substantive philosophical exchange between men and women occurred in the seventeenth century and that its exclusion from the canon was a decision, not a natural consequence of women\'s philosophical absence. Elisabeth\'s mind-body interaction objection is now regarded as the strongest philosophical challenge to Cartesian dualism mounted in the seventeenth century — stronger, in many respects, than any of the seven sets of Objections and Replies. The correspondence also documents the human cost of philosophical genius working under conditions of religious and political constraint, in exile, and at the mercy of royal patronage.',

    context: 'Descartes\' letters were preserved by correspondents and Descartes\' literary executor Claude Clerselier, who published three volumes of selected correspondence between 1657 and 1667. The critical edition by Charles Adam and Paul Tannery (AT, 1897-1913) is the standard scholarly reference; supplementary volumes have added letters discovered subsequently. The Elisabeth-Descartes correspondence was published separately by Clerselier and has been the subject of increasing scholarly attention since the feminist recovery of early modern women philosophers beginning in the 1970s.',

    relatedWorks: ['meditations', 'passions-of-the-soul', 'principles-of-philosophy', 'objections-and-replies']
}

);
"""

files = {
    'data-11a.js': data_11a,
    'data-11b.js': data_11b,
    'data-11c.js': data_11c,
    'data-11d.js': data_11d,
    'data-11e.js': data_11e,
}

for filename, content in files.items():
    path = os.path.join(js_dir, filename)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    lines = content.count('\n')
    print(f"  Written {filename}  —  {lines} lines  →  {path}")

print("\nAll Descartes files complete. Verify with:")
print("  wc -l js/data-11a.js js/data-11b.js js/data-11c.js js/data-11d.js js/data-11e.js")
