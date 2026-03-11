/* ================================================================
   DATA PART 11b — Descartes: Principles of Philosophy
                              Rules for the Direction of the Mind
   ================================================================ */

window.WORKS.push(

/* ──────────────────────────────────────
   3. PRINCIPLES OF PHILOSOPHY
────────────────────────────────────── */
{
    id: 'principles-of-philosophy',
    title: 'Principles of Philosophy',
    greekTitle: 'Principia Philosophiae',
    philosopher: 'descartes',
    category: 'natural-philosophy',
    categoryLabel: 'Natural Philosophy',
    date: '1644',
    dateSort: 1644,
    emoji: '🌌',
    cardSize: 'wide',
    readingDifficulty: 'Advanced',
    estimatedWordCount: 60000,

    shortDesc: 'Descartes\' most systematic work — a comprehensive four-part architecture of the universe from first principles, presenting in geometric form the metaphysics, matter theory, cosmology, and physics that was intended to replace Aristotle as the foundation of all natural science.',

    summary: 'The Principles of Philosophy is Descartes\' most ambitious and comprehensive work, written in the textbook format of numbered propositions so that it could replace Aristotle\'s Physics and the scholastic commentaries as the standard curriculum of natural philosophy. It is divided into four parts. Part I (Principles of Human Knowledge) covers the metaphysical foundations that had been argued more discursively in the Meditations, now compressed into 76 numbered theses: the method of doubt, the cogito ("Cogito ergo sum" appears here for the first time in Latin in this exact formulation), the existence of God, the distinction between mind and body, the nature of substance, and the theory of innate ideas. Part II (Principles of Material Things) develops the physics: Descartes defines matter as identical with extension (taking up space), rejects atoms and void (empty space is a contradiction since space just is extension, which is material), and establishes the three laws of motion: the law of inertia, the conservation of motion in collisions, and the tendency of moving bodies to travel in straight lines. Part III (The Visible World) applies these principles to cosmology, developing the vortex theory: the solar system consists of whirling fluid vortices carrying the planets around the sun, a purely mechanical account that required no divine intervention in the ongoing operations of nature. Part IV (The Earth) applies the principles to geology, magnetism, and terrestrial phenomena, including an early theory of the formation of the Earth from a primordial cooling of matter. The Principles represents the fullest statement of the Cartesian mechanical worldview: a universe of matter-in-motion, governed by mathematical laws, requiring only an initial creative act by God but thereafter running as a perfect machine. It was the system Newton\'s Principia Mathematica (1687) would largely displace, but the framework Newton worked within — inertia, force, absolute space — was shaped by the problems and terms Descartes had established.',

    themes: ['Natural Philosophy', 'Cosmology', 'Motion', 'Matter', 'God', 'Mechanism', 'Science', 'Metaphysics', 'Method'],

    keyCharacters: [
        { name: 'Aristotle (implied antagonist)', role: 'The scholastic tradition whose physics, matter theory, and cosmology the Principles was explicitly designed to replace at the university level' },
        { name: 'God', role: 'The first cause who creates matter and imposes the laws of motion, but thereafter plays no ongoing role in the mechanical universe' }
    ],

    concepts: ['Cogito Ergo Sum (formalized)', 'Extension as the Essence of Matter', 'Plenum (No Void)', 'Three Laws of Motion', 'Vortex Theory', 'Mechanical Philosophy', 'Conservation of Motion', 'Substance (Thinking vs. Extended)', 'Innate Ideas', 'Eternal Truths Created by God'],

    structure: 'Four parts in numbered-proposition format (504 articles total):\n\nPart I — Principles of Human Knowledge (76 articles): Metaphysical foundations. The method of doubt. The cogito in Latin formulation. God\'s existence. The nature of substance and its attributes. Modes and qualities. The theory of knowledge.\n\nPart II — Principles of Material Things (64 articles): The essence of matter is extension. No vacuum. The three laws of nature (inertia, conservation of motion, rectilinear tendency). The rules of collision.\n\nPart III — The Visible World (138 articles): Vortex cosmology. The formation of the sun and stars. The motion of planets. Comets. The solar system as a self-sustaining mechanical system.\n\nPart IV — The Earth (228 articles): Formation of the Earth from a primordial mass. Gravity as the effect of centrifugal force in vortices. Magnetism. Terrestrial phenomena. Planned but unwritten Parts V and VI were to cover plants, animals, and humans.',

    quote: 'Cogito ergo sum — I think, therefore I am. — Principles of Philosophy, Part I, Article 7',

    additionalQuotes: [
        { text: 'In order to seek truth, it is necessary once in the course of our life, to doubt, as far as possible, of all things.', citation: 'Principles of Philosophy, Part I, Article 1' },
        { text: 'Give me extension and motion, and I will construct the world.', citation: 'Attributed to Descartes (summarizing the program of the Principles)' },
        { text: 'The nature of matter, or body considered in general, consists not in its being hard or heavy, or coloured, or one that affects our senses in some other way, but solely in the fact that it is a substance extended in length, breadth and depth.', citation: 'Principles of Philosophy, Part II, Article 4' }
    ],

    commentary: [
        {
            philosopher: 'Isaac Newton',
            text: 'Newton\'s Principia Mathematica (1687) was written, in part, as a systematic demolition of Cartesian physics. The very title — borrowing "Principia" from Descartes — signals both homage and supersession. Newton rejected Descartes\' vortex theory of planetary motion by showing mathematically that vortices would produce the wrong orbital velocities and could not account for Kepler\'s ellipses. More fundamentally, Newton rejected Descartes\' identification of matter with extension by positing absolute space (empty of matter) and a universal gravitational force acting at a distance — exactly what Descartes had denied was possible. Yet Newton\'s framework retained deeply Cartesian assumptions: the mechanistic conception of nature as governed by mathematical laws, the divine clockmaker who sets the machine running, and inertia (Newton\'s First Law is essentially Descartes\' Law of Inertia reformulated). Cartesian physics was Newton\'s necessary precondition even as it was his primary target.'
        },
        {
            philosopher: 'Gottfried Wilhelm Leibniz',
            text: 'Leibniz engaged with the Principles at technical depth throughout his career. His most celebrated critique targeted Descartes\' theory of matter and motion in Part II. Descartes defined matter as extension and motion as change of position relative to neighboring bodies. Leibniz showed that this produced the wrong conserved quantity in collisions: Descartes thought the total quantity of motion (mass times speed, a scalar) was conserved, but Leibniz demonstrated in his "Brief Demonstration of a Notable Error of Descartes" (1686) that what is actually conserved is vis viva (mass times the square of velocity). This dispute over whether mv or mv² is conserved became the famous vis viva controversy that animated eighteenth-century physics — and it was Leibniz who was right, anticipating the modern concept of kinetic energy. Leibniz also objected that Descartes\' purely geometrical conception of matter, devoid of force and activity, produced a dead universe inconsistent with God\'s goodness.'
        },
        {
            philosopher: 'Elisabeth of Bohemia',
            text: 'Princess Elisabeth of Bohemia, Descartes\' most philosophically penetrating correspondent, posed to him in 1643 the question that the Principles never adequately resolved: if mind is thinking substance with no extension and body is extended substance with no thought, and they have nothing in common, how can the mind move the body? How can an immaterial thing cause physical motion? This problem, known as the mind-body interaction problem, strikes at the heart of the Cartesian dualism the Principles systematizes. Descartes\' responses to Elisabeth were notoriously evasive — he invoked the "primitive notion" of union and suggested that the mind-body interaction was experienced but not conceptualized through the categories of his official metaphysics. Many philosophers have concluded that Descartes never solved this problem. Elisabeth\'s correspondence, published posthumously, is now regarded as a foundational document in the philosophy of mind.'
        },
        {
            philosopher: 'Nicolas Malebranche',
            text: 'Malebranche, the greatest of the Cartesian philosophers, developed the Principles\' physics and metaphysics in his Search After Truth (1674–1675) in a direction Descartes had not anticipated. Accepting Cartesian dualism fully — mind and body have truly nothing in common — Malebranche concluded that causal interaction between them is impossible not just mysterious. His solution was occasionalism: God is the only genuine cause; when my mind "wills" to move my arm, this is the occasion for God to move it, and when my arm is struck, this is the occasion for God to produce a sensation of pain in my mind. Malebranche used this startling result as evidence of continuous divine presence in all natural events. His occasionalism influenced Hume\'s skepticism about causation — if even the most obvious case of causation (mind moving body) turns out not to be genuine causation, perhaps all causation is similarly doubtful.'
        }
    ],

    modernRelevance: 'The Principles established the framework — a mathematized, mechanistic nature governed by universal laws — within which modern physics developed. Descartes\' identification of matter with extension was wrong (matter is more than extension; it has mass, charge, spin), but the philosophical claim that the material world is fully intelligible through mathematics and law is the axiom of all modern physical science. His vortex cosmology failed empirically, but the ideal of a purely mechanical cosmology requiring no ongoing divine intervention became the working assumption of Enlightenment science and remains the default of secular scientific culture. The Principles also gave us the modern concept of inertia — the tendency of a body to remain in its state of motion or rest — which Newton borrowed and generalized. Every high school physics textbook is descended, through Newton, from the Cartesian framework the Principles established.',

    context: 'Published in Amsterdam in 1644, the Principles was dedicated to Princess Elisabeth of Bohemia, whose correspondence with Descartes about the mind-body problem (begun in 1643) represents some of the most searching philosophical exchange of the seventeenth century. Descartes explicitly designed the book as a replacement for the scholastic Aristotle textbooks used in Jesuit colleges, hoping it would be adopted as the standard curriculum — an ambition that was never fully realized but that shaped philosophy education throughout the latter seventeenth century. A French translation by Abbé Picot, which Descartes revised and expanded, appeared in 1647. In the preface to the French edition, Descartes gave his famous metaphor of philosophy as a tree: metaphysics is the roots, physics is the trunk, and mechanics, medicine, and morals are the branches bearing fruit.',

    relatedWorks: ['meditations', 'discourse-on-method', 'the-world', 'passions-of-the-soul']
},

/* ──────────────────────────────────────
   4. RULES FOR THE DIRECTION OF THE MIND
────────────────────────────────────── */
{
    id: 'rules-for-direction',
    title: 'Rules for the Direction of the Mind',
    greekTitle: 'Regulae ad Directionem Ingenii',
    philosopher: 'descartes',
    category: 'method',
    categoryLabel: 'Method & Epistemology',
    date: 'c.1628 (posthumous 1701)',
    dateSort: 1628,
    emoji: '📐',
    cardSize: 'normal',
    readingDifficulty: 'Intermediate',
    estimatedWordCount: 35000,

    shortDesc: 'Descartes\' unfinished early masterwork on method — thirty-six projected rules (only twenty-one completed) for conducting inquiry across all disciplines through intuition and deduction, featuring the earliest version of his mathesis universalis: the dream of a single universal science.',

    summary: 'Written around 1619–1628 but never completed and published only posthumously in 1701, the Rules for the Direction of the Mind gives us Descartes at his most architecturally ambitious and technically precise. It is an early draft of the methodological project that would be summarized more accessibly in the Discourse and deployed philosophically in the Meditations, but here in a rawer and more mathematically detailed form. Descartes projects thirty-six rules divided into three groups of twelve: the first twelve concern simple propositions, the second twelve "perfectly understood" problems (fully formed questions), and the last twelve "incompletely understood" problems — but he completed only the first twenty-one, and the last four are mere sketches. Rule I establishes the governing aim: all sciences are interconnected and constitute a single science of the universal; one must study the whole rather than individual disciplines in isolation. Rule II introduces the two operations of the pure intellect that ground all valid knowledge: intuition (the direct apprehension of a simple, indubitable truth) and deduction (chains of necessary inferences from intuited truths). Rule III warns against probable reasoning and recommends attending only to what can be clearly intuited or rigorously deduced. The middle rules develop a theory of simple natures — the most basic, irreducible elements of reality (extension, duration, thought, unity) that cannot be doubted and from which compound truths are built. The later rules introduce the method of mathesis universalis (universal mathematics): the idea that algebra and geometry, properly understood, share a common structural framework, and that this framework can be extended to any problem in any domain whatsoever. This is the conceptual seed of the analytic geometry Descartes would invent (the Cartesian coordinate system connecting algebra and geometry), and, more broadly, of the Enlightenment ideal that all knowledge can be unified under mathematical method.',

    themes: ['Method', 'Epistemology', 'Mathematics', 'Universal Science', 'Intuition', 'Deduction', 'Simple Natures', 'Certainty', 'Order'],

    keyCharacters: [
        { name: 'The Universal Intellect', role: 'Not a person but a capacity — the Rules address themselves to any mind willing to discipline itself through its procedures, regardless of subject matter' }
    ],

    concepts: ['Intuition and Deduction', 'Simple Natures', 'Mathesis Universalis (Universal Mathematics)', 'Order of Problems', 'Enumeration and Induction', 'Figures and Numbers as Representations', 'The Imagination as Tool of Intellect', 'Analytic Geometry (anticipated)'],

    structure: 'Twenty-one completed rules (of thirty-six projected), in three groups:\n\nRules I–IV: The aim of inquiry (one unified science) and the two valid operations (intuition and deduction). Warning against probable reasoning. The need for method.\n\nRules V–VII: Resolution and enumeration. Problems must be reduced to their simplest parts and then reconstructed. Enumeration ensures completeness.\n\nRules VIII–XI: Limit of inquiry. How to identify what remains to be found. Simple propositions vs. problems requiring comparison.\n\nRules XII–XXI: Theory of cognition and mathematical method. Simple natures classified (intellectual, material, common). The imagination and memory as tools. The representation of all quantities by lines and figures. The beginnings of algebraic notation for philosophical problems.',

    quote: 'All the sciences are nothing other than human wisdom, which always remains one and the same, however different the subjects to which it is applied. — Rules, Rule I',

    additionalQuotes: [
        { text: 'By intuition I do not mean the fluctuating testimony of the senses or the misleading judgment of the imagination, but the conception of a clear and attentive mind, which is so easy and distinct that there can be no room for doubt about what we are understanding.', citation: 'Rules, Rule III' },
        { text: 'We should occupy ourselves only with those objects about which our intellect appears capable of having certain and indubitable knowledge.', citation: 'Rules, Rule II' }
    ],

    commentary: [
        {
            philosopher: 'Gottlob Frege',
            text: 'Frege\'s Begriffsschrift (1879) — the invention of formal logic and the founding document of analytic philosophy — can be understood as realizing the program the Rules projected but could not complete. Descartes\' mathesis universalis dreamt of a universal formal language in which all valid reasoning could be expressed and checked mechanically; Frege created one. The Rules\' ambition to reduce all valid inference to intuition and deduction is echoed in Frege\'s reduction of arithmetic to logic — the logicist program. Where Descartes relied on an irreducible faculty of intellectual intuition to grasp simple truths, Frege sought to eliminate appeals to intuition entirely and ground mathematics purely in logical axioms and rules of inference. The twentieth-century debate between logicism (Frege, Russell) and intuitionism (Brouwer) is, in a deep sense, a continuation of the methodological ambitions and tensions first articulated in Descartes\' Rules.'
        },
        {
            philosopher: 'John Stuart Mill',
            text: 'Mill\'s A System of Logic (1843), the defining work of British empiricism\'s methodological tradition, engaged at length with the Cartesian claim (stated in its starkest form in the Rules) that genuine science proceeds from intuited axioms by deduction. Mill rejected this rationalist model of scientific method entirely. Science, he argued, proceeds not by deduction from self-evident intuitions but by induction from particular observations. His famous five methods (agreement, difference, concomitant variation, residues, and joint method) were designed as a systematic alternative to Cartesian deductivism. The debate the Rules initiated — whether science is fundamentally deductive-rationalist (hypothetico-deductive) or inductive-empiricist — remained the central problem of philosophy of science through Popper, Hempel, and Kuhn.'
        },
        {
            philosopher: 'Jean-Paul Sartre',
            text: 'Sartre\'s analysis of the Cartesian cogito in The Transcendence of the Ego (1936) began from a close reading of the Rules and Meditations. Sartre argued that Descartes had correctly identified consciousness as the most fundamental datum but had wrongly treated it as a thing — a res cogitans, a substance with an essence. In Sartre\'s phenomenological ontology, consciousness is not a substance but a pure activity, a nothingness that is always directed toward something other than itself; it has no inner nature, no essence prior to its acts. The Rules\' conception of pure intellectual intuition as a faculty grasping simple natures already exhibits, for Sartre, the Cartesian error of treating consciousness as a thing that has properties rather than a transparent activity that is what it does. Sartre\'s existentialist formula "existence precedes essence" is, in part, an inversion of the Cartesian model of mind the Rules first articulated.'
        }
    ],

    modernRelevance: 'The Rules\' most consequential legacy is analytic geometry. In Rule XIV, Descartes introduces the idea of representing quantities as line segments, treating both geometrical and arithmetical problems with the same symbolic notation. This insight — that algebraic equations and geometric curves are two representations of the same mathematical objects — became the Cartesian coordinate system: the x-y graph that every student uses and that made calculus possible by giving Newton and Leibniz a way to represent curves algebraically. Every data visualization, computer screen coordinate system, and GPS mapping algorithm is built on the bridge between algebra and geometry that the Rules first sketched. More broadly, the mathesis universalis ideal — a universal formal method applicable to any domain — lives on in the computer science dream of algorithmic solutions and in the philosophy of science debate about whether there is a single scientific method or many domain-specific methods.',

    context: 'The Rules were never published by Descartes and exist in several manuscript copies of varying completeness. The most significant version was found among the papers of Leibniz, who had a copy made in 1676. The work was first published in the posthumous Amsterdam edition of Descartes\' Opera Omnia in 1701, over fifty years after his death. The dating is uncertain: scholars believe the earliest portions were written around 1619–1620, when Descartes was in his early twenties and had just had his famous visions on the night of November 10–11, 1619 — the night he claimed to have seen, in a dream, the foundations of a "marvellous science." The later portions were probably written up to around 1628. Descartes abandoned the work, most scholars believe, because the program it envisioned — a complete formal calculus of all knowledge — turned out to be more difficult than he initially thought, and he moved on to the more specific metaphysical and scientific projects that produced the Discourse, Meditations, and Principles.',

    relatedWorks: ['discourse-on-method', 'meditations', 'principles-of-philosophy']
}

);
