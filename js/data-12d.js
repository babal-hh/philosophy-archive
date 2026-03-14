/* ================================================================
   DATA PART 12d — Short Treatise + Descartes' Principles + Metaphysical Thoughts
   ================================================================ */

window.WORKS.push(

/* ──────────────────────────────────────
   1. SHORT TREATISE ON GOD, MAN, AND HIS WELL-BEING
────────────────────────────────────── */
{
    id: 'spinoza-short-treatise',
    title: 'Short Treatise on God, Man, and His Well-Being',
    greekTitle: 'Korte Verhandeling van God, de Mensch en des zelfs Welstand',
    philosopher: 'spinoza',
    category: 'metaphysics',
    categoryLabel: 'Metaphysics & Ethics',
    date: 'c.1660 AD (posthumous)',
    dateSort: 1660,
    emoji: '🌱',
    cardSize: 'normal',
    readingDifficulty: 'Intermediate',
    estimatedWordCount: 30000,

    shortDesc: 'Spinoza\'s earliest surviving philosophical work — a Dutch-language draft of the ideas that would mature into the Ethics, offering a more personal, dialogue-inflected, and less geometrically rigid version of his pantheism, theory of knowledge, and account of the good life.',

    summary: 'The Short Treatise survives only in Dutch manuscripts — Spinoza wrote in Latin but apparently had this early text translated for the benefit of his Dutch-speaking circle of friends and correspondents — and was unknown to the scholarly world until 1851, when the manuscripts were discovered. It is Spinoza\'s philosophical laboratory: here, in looser prose interspersed with two dialogues, he works out for the first time the ideas that would be systematized in the Ethics.\n\nPart I treats God and Nature: God is defined as a being consisting of infinite attributes, each perfect in its kind. Natura naturans (nature naturing — the active, self-causing aspect of substance) and Natura naturata (nature natured — the totality of modes or particular things caused by substance) appear here for the first time. The argument for the impossibility of two substances sharing an attribute — crucial to the monist conclusion of Ethics Part I — is already present, though less formally demonstrated.\n\nPart II treats the human being: the soul as an idea of the body, the three kinds of knowledge (here called opinion, true belief, and clear knowledge), the emotions and their relationship to knowledge, and the path to freedom through the transition from passion to active understanding. The Short Treatise shares with the Treatise on the Emendation of the Intellect the rare quality of emotional directness: Spinoza writes as if he genuinely cares about human liberation, not merely as a theoretical problem but as a practical imperative. The style is warmer, more tentative, and more exploratory than the architectural rigour of the Ethics — and for many readers this makes it a more humanly compelling introduction to Spinoza\'s thought.',

    themes: ['God and Nature', 'Natura Naturans and Natura Naturata', 'The Soul as Idea of the Body', 'Three Kinds of Knowledge', 'The Passions', 'Freedom', 'Love of God', 'Early Spinozism'],

    keyCharacters: [
        { name: 'Reason and Love (dialogue characters)', role: 'Two of the dialogue participants in the embedded dialogues of Part I — representing the philosophical and emotional dimensions of the relationship with God' }
    ],

    concepts: [
        'Natura naturans and natura naturata — the active self-causing substance (naturing nature) vs the passive totality of modes (natured nature); the distinction that will structure Ethics Part I',
        'Early monism — the argument that there can only be one substance, each attribute being unique to it, is worked out here in preliminary form',
        'Three kinds of knowledge (early version) — opinion (hearsay and imagination), true belief (reason), clear knowledge (intuition); the precursor to the three kinds in Ethics Part II',
        'Love as the path to freedom — the emotional economy of the Short Treatise centers on the transformation of passive love (attachment to finite goods) into active love (the intellectual love of God)'
    ],

    structure: 'Two parts with two embedded dialogues:\n\nPart I — On God: Nature and its attributes. Natura naturans and natura naturata. God\'s necessity. Two dialogues on the nature of the divine.\n\nPart II — On Man and His Well-Being: The soul. The three kinds of knowledge. Passions. The path to true freedom through intellectual love of God.',

    quote: 'The love of God is our highest happiness and blessedness, and the final end and aim of all human actions. — Short Treatise, Part II, Chapter XXII',

    additionalQuotes: [
        { text: 'Nature has no particular goal in view, and final causes are mere human figments.', citation: 'Short Treatise, Part I, Chapter X' }
    ],

    commentary: [
        {
            philosopher: 'Wolfhart Pannenberg',
            text: 'Pannenberg, the twentieth-century German systematic theologian, engaged with the Short Treatise as evidence that Spinoza\'s pantheism was not simply atheism in disguise but a serious attempt to think through the relation of God and world without the arbitrary anthropomorphism of traditional theism. Pannenberg argued that Spinoza\'s concept of Natura naturans — the self-causing, active, infinite ground of all things — preserves something essential that theology needs: the absolute reality of God as the ground of all being, not merely as a being among beings. Where Pannenberg parted ways with Spinoza was on personality and will: for Pannenberg, a God who is pure necessity and who has no ends or purposes is not the God of biblical revelation. But the Short Treatise, he thought, forced theologians to think more carefully about what it would mean for God to be "infinite."'
        }
    ],

    modernRelevance: 'The Short Treatise\'s discovery in 1851 transformed Spinoza scholarship by revealing the genetic development of his thought — showing how the geometrically impersonal Ethics grew from a warmer, more exploratory engagement with the same questions. For contemporary readers, the Short Treatise offers an accessible entry point into Spinoza\'s philosophy: the same ideas as the Ethics, but in a form less likely to intimidate. Its treatment of the emotions as the primary obstacle to and means of human freedom also anticipates the therapeutic approach to philosophy developed by later thinkers from Schopenhauer to the contemporary philosophical counseling tradition.',

    context: 'The Short Treatise was probably written around 1658-1660, during Spinoza\'s early philosophical development, and appears to have been written in Latin and translated into Dutch for his circle. It was unknown to scholarship until 1851, when Dutch manuscripts were discovered. The book\'s existence helps scholars trace the development of Spinoza\'s thought from its origins to the mature Ethics and to understand which ideas were present from the start and which developed later.',

    relatedWorks: ['spinoza-ethics', 'treatise-on-emendation', 'spinoza-descartes-principles']
},

/* ──────────────────────────────────────
   2. DESCARTES' PRINCIPLES OF PHILOSOPHY
────────────────────────────────────── */
{
    id: 'spinoza-descartes-principles',
    title: "Descartes' Principles of Philosophy",
    greekTitle: 'Renati Des Cartes Principiorum Philosophiae',
    philosopher: 'spinoza',
    category: 'method',
    categoryLabel: 'Exposition & Commentary',
    date: '1663 AD',
    dateSort: 1663,
    emoji: '📎',
    cardSize: 'normal',
    readingDifficulty: 'Advanced',
    estimatedWordCount: 40000,

    shortDesc: 'The only work Spinoza published under his own name during his lifetime — a rigorous geometric demonstration of Descartes\' Principles of Philosophy, accompanied by the Metaphysical Thoughts, which quietly introduces his own divergent metaphysical positions behind a veil of exposition.',

    summary: 'Descartes\' Principles of Philosophy (with Metaphysical Thoughts appended) is the only book Spinoza published under his own name, and he did so reluctantly, at the urging of his friends. The work originated as notes Spinoza prepared for a student, Johannes Caesarius, who was studying Descartes. Spinoza demonstrated Part I and Part II of Descartes\' Principles in strict geometric form — a pedagogical exercise in making explicit the logical structure of the Cartesian system.\n\nThe significance of the work is not its exposition but its quietly subversive relationship to its subject. Spinoza explicitly warns in the preface, written by his friend Lodewijk Meyer, that Spinoza does not endorse the views he demonstrates — and the Metaphysical Thoughts appended to the main text shows why. In the Metaphysical Thoughts, Spinoza addresses standard scholastic and Cartesian metaphysical topics — substance, duration, time, eternity, necessity, contingency, God — and at point after point, without announcing it, substitutes his own pantheist, determinist conclusions for the Cartesian or scholastic ones. The careful reader notices that the God of the Metaphysical Thoughts has no intellect or will in the ordinary sense, that contingency is reinterpreted as ignorance rather than genuine metaphysical openness, and that human freedom is already being redefined as understanding rather than libertarian choice. The work is a philosophical Trojan horse: Cartesian on the outside, Spinozist within.',

    themes: ['Cartesian Philosophy', 'Geometric Method', 'Metaphysics', 'God', 'Substance', 'Eternity', 'Necessity', 'Exposition as Philosophy'],

    keyCharacters: [
        { name: 'Johannes Caesarius', role: 'The student for whom Spinoza prepared the original notes; the occasion of the only book Spinoza published under his own name' }
    ],

    concepts: [
        'Geometric demonstration of Descartes — making the logical structure of the Cartesian system explicit and rigorous; showing both its power and its hidden assumptions',
        'Metaphysical Thoughts as covert Spinozism — the appended scholastic-style discussions quietly substitute Spinozist conclusions for Cartesian ones without announcing the substitution',
        'Necessity vs contingency — Spinoza reinterprets contingency as a product of human ignorance rather than genuine metaphysical openness in reality'
    ],

    structure: 'Two parts (Descartes\' Principles) plus Metaphysical Thoughts:\n\nPart I of Descartes\' Principles: Metaphysical foundations in geometric form — doubt, cogito, God, mind, body.\n\nPart II of Descartes\' Principles: Physics — matter, motion, the laws of nature.\n\nMetaphysical Thoughts: Supplementary discussions of standard metaphysical topics (substance, duration, eternity, necessity, God\'s will) with covert Spinozist reinterpretations.',

    quote: 'I warn the reader that the author has not written these things as his own views, but only as things that can be deduced from Descartes\' own hypotheses. — Lodewijk Meyer, Preface to Descartes\' Principles',

    additionalQuotes: [
        { text: 'By eternity I understand existence itself insofar as it is conceived to follow necessarily from the definition alone of the eternal thing.', citation: 'Metaphysical Thoughts, Part II, Chapter I (anticipating Ethics, Part I, Definition VIII)' }
    ],

    commentary: [
        {
            philosopher: 'Gottfried Wilhelm Leibniz',
            text: 'Leibniz read Spinoza\'s Descartes\' Principles carefully and recognized, well before his visit to The Hague in 1676, that the Metaphysical Thoughts was not mere scholastic commentary but a covert presentation of a radically different metaphysical position. Leibniz annotated his copy extensively, noting at several points that Spinoza had subtly reinterpreted Cartesian concepts in ways that, if followed to their conclusions, would eliminate the real distinction between God and the world and between God and finite substances. The annotations show Leibniz working out, in response to Spinoza, his own alternative to both Cartesianism and Spinozism — the monadology — in which each finite thing is a genuine substance reflecting the whole from its own perspective, rather than a mere mode of the one infinite substance.'
        }
    ],

    modernRelevance: 'Spinoza\'s Descartes\' Principles is the earliest example of a philosophical practice that has become common: the close, geometrically rigorous reconstruction of a thinker\'s argument that simultaneously reveals its assumptions and opens space for an alternative. Spinoza uses the exercise of demonstrating Descartes to clarify, by contrast, what his own position requires. The work also provides the clearest window into how Spinoza read and appropriated Descartes: not as a disciple but as a rigorous critic who accepted the geometric method and the mathematical account of nature while rejecting the substance dualism, the voluntarist God, and the indeterminist free will.',

    context: 'Published in Amsterdam in 1663 — the only work Spinoza published under his own name. The preface was written by Lodewijk Meyer, a member of Spinoza\'s Amsterdam circle. Spinoza was dissatisfied with being known as a Cartesian commentator and did not publish another work under his own name — the Theological-Political Treatise appeared anonymously in 1670. The work established Spinoza\'s reputation as a rigorous philosopher among his contemporaries while concealing, under the Cartesian framing, the full radicalism of his actual views.',

    relatedWorks: ['spinoza-ethics', 'treatise-on-emendation', 'spinoza-short-treatise']
}

);
