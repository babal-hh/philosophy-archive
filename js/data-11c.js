/* ================================================================
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
