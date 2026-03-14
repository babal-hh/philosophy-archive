#!/usr/bin/env python3
"""Run this from inside ~/Desktop/philosophy-archive/ to generate Berkeley data files."""
import os

js_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'js')
os.makedirs(js_dir, exist_ok=True)

# ── data-15a.js ── Principles + Three Dialogues ───────────────────────────────
data_15a = r"""window.WORKS.push(

{
    id: 'principles-human-knowledge',
    title: 'A Treatise Concerning the Principles of Human Knowledge',
    greekTitle: 'Treatise Concerning the Principles of Human Knowledge',
    philosopher: 'berkeley',
    category: 'metaphysics',
    categoryLabel: 'Metaphysics',
    date: '1710 AD',
    dateSort: 1710,
    emoji: '👁',
    cardSize: 'wide',
    readingDifficulty: 4,
    estimatedWordCount: 65000,
    shortDesc: 'The founding text of philosophical idealism in the modern period — Berkeley\'s demonstration that matter does not exist, that to be is to be perceived, and that the only substances are minds and the ideas they contain.',
    summary: 'A Treatise Concerning the Principles of Human Knowledge is one of the most audacious and rigorously argued works in the history of philosophy. Published in 1710 when Berkeley was only twenty-five years old, it advances a single thesis of breathtaking simplicity and shocking radicalism: material substance does not exist. There are no mind-independent physical objects underlying our perceptual experience. The world consists entirely of minds — finite minds like ours and the infinite mind of God — and the ideas those minds contain. The entire apparatus of material substance, which Descartes, Locke, and Newton had taken for granted as the substrate of the physical world, is a philosophical fiction that careful analysis of human knowledge shows to be not merely unknowable but strictly meaningless.\n\nBerkeley\'s argument proceeds from premises he inherits directly from Locke and turns against Locke\'s own conclusions with surgical precision. Locke had argued that we have no direct perception of material substance — we perceive only ideas, which are the effects of material things acting on our senses. But what, Berkeley asks, could it possibly mean for a material thing — something entirely non-mental, with no qualities but extension, figure, and motion — to cause an idea in a mind? Causation is itself a relation we understand only through the action of minds on ideas. Inert, extended matter cannot cause anything. Furthermore, when we attempt to form a clear idea of matter in itself — stripped of all perceivable qualities — we find that we are attempting to conceive of the inconceivable. Locke himself admitted we have no idea of substance in itself. Berkeley draws the conclusion Locke flinched from: if we have no idea of it, we have no reason to posit it, and the word names nothing.\n\nThe positive doctrine is equally radical. The familiar objects of everyday experience — tables, chairs, mountains, trees — exist exactly as they appear. Berkeley is not a sceptic and emphatically does not deny the reality of the physical world. What he denies is the Lockean duplication: the claim that behind our perceptions of tables there are material tables that resemble them and cause them. Tables are collections of ideas; to say that the table exists is to say that the ideas constituting it are being perceived, or are available to be perceived. This is the formula esse est percipi: to be is to be perceived. But Berkeley immediately faces the obvious objection: if the table exists only when perceived, does it cease to exist when everyone leaves the room? His answer is that the unperceived existence of things is maintained by their being always perceived by God, whose infinite mind contains all possible ideas and whose continuous perception sustains the order and regularity of the world we experience as the laws of nature.\n\nThe Principles also contains Berkeley\'s most sustained treatment of abstract ideas, which he targets in the Introduction as the root cause of philosophical darkness. Locke had argued that the mind abstracts general ideas from particular experiences — arriving at an idea of triangle in general, which is neither equilateral, nor scalene, nor right-angled, but all and none of these at once. Berkeley argues with devastating clarity that no such idea can actually be formed: every idea the mind can frame is perfectly determinate and particular. This nominalist attack on abstraction anticipates Wittgenstein\'s private language argument and Goodman\'s nominalism, and it undermines the philosophical foundations on which the concept of unperceived material substance rests.\n\nThe Principles also addresses natural science. Berkeley does not deny the validity of Newtonian mechanics — he denies the interpretation that Newton\'s laws describe the behaviour of material particles in absolute space. The laws of nature are regularities in the succession of God\'s ideas — reliable patterns that God maintains in the experience of finite minds and that allow us to predict and control our environment. Newton\'s equations are instruments of prediction, not descriptions of a mind-independent material reality. This instrumentalist philosophy of science, developed more fully in De Motu (1721), anticipates the positivism of Mach and the instrumentalism of Duhem and Poincaré by nearly two centuries.',
    themes: ['immaterialism', 'esse est percipi', 'critique of abstract ideas', 'God as the ground of perceptual order', 'laws of nature as divine language', 'primary vs secondary qualities dissolved', 'idealism', 'instrumentalism in science', 'critique of Lockean substance'],
    keyCharacters: [],
    concepts: [
        'Esse est percipi — to be is to be perceived; existence for sensible things consists in their being perceived',
        'Immaterialism — the denial that any mind-independent material substance exists',
        'Spirits — the only true substances; active, unextended, knowing beings',
        'Ideas — the contents of minds; passive, mind-dependent, and constituting all sensible reality',
        'Abstract ideas refuted — no idea can be formed that is genuinely indeterminate; all ideas are particular',
        'God as the infinite perceiver — the divine mind whose continuous perception sustains the existence of the sensible world between finite perceptions',
        'Laws of nature as God\'s language — the regularities in sensory experience are God communicating with finite minds',
        'Primary qualities dissolved — extension and figure are as mind-dependent as colour and warmth; the primary-secondary distinction collapses',
        'Material substance as meaningless — not merely unknowable but strictly unintelligible; Locke\'s substratum is a word without an idea'
    ],
    structure: 'Introduction: Critique of abstract ideas as the source of philosophical error\n§1–33: The esse est percipi principle; the non-existence of matter; the nature of ideas and spirits\n§34–84: Objections answered — continuity of existence, science and mathematics, the independent world\n§85–156: Further objections; the nature of the soul; God\'s role in perceptual experience; the language of nature',
    quote: 'All the choir of heaven and furniture of the earth, in a word all those bodies which compose the mighty frame of the world, have not any subsistence without a mind — that their being is to be perceived or known.',
    additionalQuotes: [
        { text: 'It is indeed an opinion strangely prevailing amongst men, that houses, mountains, rivers, and in a word all sensible objects, have an existence, natural or real, distinct from their being perceived by the understanding.', source: 'Principles §4' },
        { text: 'We have first raised a dust and then complain we cannot see.', source: 'Principles §3' },
        { text: 'The only thing whose existence we deny is that which philosophers call matter or corporeal substance. And in doing of this there is no damage done to the rest of mankind, who, I dare say, will never miss it.', source: 'Principles §35' }
    ],
    commentary: [
        { philosopher: 'Hume', text: 'Berkeley\'s arguments admit of no answer and produce no conviction. Their only effect is to cause that momentary amazement and irresolution which is the result of scepticism.' },
        { philosopher: 'Kant', text: 'Berkeley\'s idealism is empirical idealism — the reduction of outer objects to mere imagination. My own transcendental idealism is precisely the opposite: it makes outer appearances entirely real as appearances, while denying that things in themselves as they appear to us can be known. Berkeley collapses the distinction between appearance and the thing appearing; I maintain it.' },
        { philosopher: 'Russell', text: 'Berkeley\'s argument that we perceive only our own ideas and that matter is an illegitimate inference from those ideas is technically stronger than it appears. The problem is his solution: replacing the unknowable matter with a barely more knowable God does not dissolve the sceptical problem, it relocates it.' },
        { philosopher: 'Mach', text: 'Berkeley was centuries ahead of his time in physics. His critique of absolute space and his instrumentalist account of the laws of nature anticipate almost exactly the positivist philosophy of science. The notion that physical laws are instruments for organising experience rather than descriptions of a mind-independent reality is correct.' }
    ],
    modernRelevance: 'The phenomenalist programme in logical empiricism — the attempt to translate physical object statements into sense-datum statements — is Berkeley\'s programme made rigorous, and its failure defined a generation of analytic philosophy. His instrumentalism about scientific laws became the dominant philosophy of science among practicing physicists from Mach through the Copenhagen interpretation of quantum mechanics, in which Bohr\'s insistence that quantum mechanics describes observations rather than mind-independent reality is explicitly Berkeleyan. The deeper question Berkeley posed — whether coherent sense can be made of a mind-independent physical world — remains the central problem of the philosophy of perception.',
    context: 'Berkeley wrote the Principles between 1707 and 1709, composing it in Dublin while a Fellow of Trinity College. He had developed the key ideas in his Philosophical Commentaries (private notebooks, 1707-1708) — the first recorded working-out of immaterialism in the history of philosophy. He published the Principles in 1710, hoping for a sensation. The reception was bafflement and ridicule. Samuel Johnson famously kicked a stone and declared himself to have refuted Berkeley. Berkeley later came to believe that the failure of the Principles to convince was partly due to the loss of a second volume he had written but which was destroyed in his baggage during a Channel crossing.',
    relatedWorks: ['three-dialogues', 'new-theory-vision', 'alciphron', 'siris']
},

{
    id: 'three-dialogues',
    title: 'Three Dialogues Between Hylas and Philonous',
    greekTitle: 'Three Dialogues Between Hylas and Philonous',
    philosopher: 'berkeley',
    category: 'metaphysics',
    categoryLabel: 'Metaphysics',
    date: '1713 AD',
    dateSort: 1713,
    emoji: '💬',
    cardSize: 'normal',
    readingDifficulty: 3,
    estimatedWordCount: 52000,
    shortDesc: 'Berkeley\'s most readable work — the case for immaterialism conducted as a Platonic dialogue between Hylas the materialist and Philonous the immaterialist, concluding that the denial of matter is common sense and the assertion of it is absurdity.',
    summary: 'Three Dialogues Between Hylas and Philonous is Berkeley\'s most perfectly executed work and one of the great philosophical dialogues in the Western tradition. Written in London in 1713 as a more accessible restatement of the Principles, it presents the case for immaterialism through a three-morning conversation between Hylas — whose name derives from the Greek word for matter — and Philonous, the lover of mind, who is Berkeley himself. The dialogue form allows Berkeley to address objections as they arise, to manage the rhetorical pacing of the argument, and to dramatize the progressive intellectual conversion of a well-meaning materialist who comes to see that his own position is incoherent and that immaterialism alone is consistent with common sense.\n\nThe First Dialogue establishes the mind-dependence of every sensory quality through a series of beautifully conducted arguments. Heat: extreme heat is pain, and pain is mental; moderate heat is pleasure, and pleasure is mental; therefore the sensory quality of heat is mental. But the same reasoning applies to all secondary qualities — sounds, tastes, odours, colours — and then, in a series of moves that distinguishes Berkeley\'s position from Locke\'s, it applies equally to the primary qualities of extension and figure. Can extension be perceived except through a sense that is itself mind-dependent? Can a figure be perceived without colour? At each stage Hylas concedes the point and retreats to a further position — real heat vs apparent heat, material substance as the unknown substratum — only to have Philonous show that each retreat posits something unintelligible. By the end of the First Dialogue Hylas has given up the reality of secondary qualities; by the end of the Second he has given up the reality of primary qualities and of material substance itself.\n\nThe Second Dialogue addresses the most pressing objections to immaterialism: does it not lead to scepticism? Philonous\'s response is perhaps Berkeley\'s strongest single argument: scepticism arises precisely from the Lockean doctrine of representative perception — the claim that what we directly perceive are ideas that merely represent a mind-independent world we never directly encounter. On this view we can never be sure our perceptions accurately represent reality. Berkeley\'s immaterialism, by contrast, makes the things we perceive identical with the objects of our knowledge: there is no gap between perception and reality, no veil of ideas through which reality must be glimpsed. The sceptic\'s worry is dissolved, not answered, by removing the metaphysical gap that generated it.\n\nThe Third Dialogue turns to the existence and nature of God. Berkeley develops an original argument for God\'s existence from the passive nature of ideas: since ideas are passive and cannot cause themselves or each other, they require an active cause. That cause cannot be matter (which is passive and extended) and cannot be our finite minds (which do not produce the steady, independent, and law-governed character of sensory experience). It must be an infinite active spirit — this is God. Berkeley\'s God is not merely a theological convenience but a philosophically necessary consequence of his analysis of causation and the passivity of ideas.',
    themes: ['immaterialism defended against objections', 'scepticism dissolved by idealism', 'God as the cause of sensory ideas', 'the passive nature of ideas', 'primary qualities shown mind-dependent', 'common sense and philosophy', 'the language of nature'],
    keyCharacters: [
        { name: 'Hylas', role: 'The materialist — begins as a confident defender of mind-independent matter and is progressively and completely converted to immaterialism through his own admissions; his name (Greek: matter) marks him as the position rather than the person' },
        { name: 'Philonous', role: 'The immaterialist — Berkeley\'s voice; patient, precise, and genuinely committed to showing that his position is common sense rather than paradox; his name means lover of mind' }
    ],
    concepts: [
        'Representative perception generates scepticism — immaterialism dissolves the sceptical gap by identifying perceived objects with real objects',
        'Heat as pain — the argument that the most intense form of a sensory quality is clearly mental entails that all forms of that quality are mental',
        'The passivity of ideas requires an active immaterial cause — neither matter nor finite minds can explain the involuntary, law-governed character of sensory experience',
        'Divine archetypes — ideas in the mind of God that correspond to what finite minds perceive'
    ],
    structure: 'First Dialogue: The morning garden — systematic reduction of all sensory qualities to mind-dependence; the collapse of Lockean substance\nSecond Dialogue: The second morning — objections answered; immaterialism and natural science; the origin of ideas in God\nThird Dialogue: The third morning — God\'s existence argued from the passivity of ideas; the continuity of objects between perceptions',
    quote: 'PHILONOUS: That there is no such thing as what philosophers call material substance, I am seriously persuaded: but, if I were made to see anything absurd or sceptical in this, I should then have the same reason to renounce this that I imagine I have now to reject the contrary opinion.',
    additionalQuotes: [
        { text: 'I do not argue against the existence of any one thing that we can apprehend either by sense or reflection. The only thing whose existence I deny is that which philosophers call matter or corporeal substance.', source: 'Three Dialogues, Second Dialogue' },
        { text: 'The same principles which at first view lead to scepticism, pursued to a certain point, bring men back to common sense.', source: 'Three Dialogues, Third Dialogue' }
    ],
    commentary: [
        { philosopher: 'Hume', text: 'The Three Dialogues is the best presentation of Berkeley\'s system. Philonous\'s argument from the passivity of ideas to God is the strongest move in the work — but the same argument, pushed further, shows that we have no impression of necessary connection between any cause and its effect, which destroys the inference to God along with every other causal inference.' },
        { philosopher: 'Boswell', text: 'Johnson observed that though we are satisfied Berkeley\'s doctrine is not true, it is impossible to refute it. I never shall forget the alacrity with which Johnson answered, striking his foot with mighty force against a large stone, till he rebounded from it — I refute it thus.' }
    ],
    modernRelevance: 'The Three Dialogues\' argument that representative perception generates scepticism — that any theory interposing ideas as intermediaries between mind and world creates an unbridgeable gap — remains the most powerful objection to sense-datum theories of perception. It is what Gilbert Ryle, J. L. Austin, and later John McDowell were arguing against when they attacked the idea of experience as a veil between mind and world.',
    context: 'Berkeley wrote the Three Dialogues during a stay in London in the winter and spring of 1712-1713, while seeking support for his proposed college in Bermuda. He moved in the London literary world during this period, befriending Swift, Addison, Steele, and Pope, and wrote the Three Dialogues with the general educated reader in mind. It was published in May 1713 and, like the Principles, failed to convert the philosophical public. He sailed for America in 1728, waited in Rhode Island for three years, and returned when it became clear the promised government grant would not materialise.',
    relatedWorks: ['principles-human-knowledge', 'new-theory-vision', 'alciphron']
}

);
"""

# ── data-15b.js ── New Theory of Vision + De Motu ────────────────────────────
data_15b = r"""window.WORKS.push(

{
    id: 'new-theory-vision',
    title: 'An Essay Towards a New Theory of Vision',
    greekTitle: 'An Essay Towards a New Theory of Vision',
    philosopher: 'berkeley',
    category: 'method',
    categoryLabel: 'Philosophy of Perception',
    date: '1709 AD',
    dateSort: 1709,
    emoji: '🔭',
    cardSize: 'normal',
    readingDifficulty: 3,
    estimatedWordCount: 46000,
    shortDesc: 'The work that made Berkeley\'s scientific reputation — a rigorous and original theory of visual depth perception arguing that distance is not directly seen but inferred through learned associations between visual signs and tangible experience.',
    summary: 'An Essay Towards a New Theory of Vision, published the year before the Principles, is Berkeley\'s most sustained contribution to what we would now call philosophy of perception and cognitive science, and it was the work through which he first gained a scientific and philosophical reputation. It was admired by Voltaire, praised by Adam Smith, and treated as a serious contribution to optics and psychology by readers who found the immaterialism of the Principles absurd. It has the unusual distinction of being a work in vision science that reaches conclusions which, when properly understood, strongly support immaterialism — though Berkeley is cautious enough not to press this connection fully in the text itself.\n\nThe central question is one that had puzzled mathematicians and natural philosophers since Descartes: how do we see distance? The problem is immediate and profound. The retina is a two-dimensional surface — the image projected onto it contains no direct representation of depth. Objects at very different distances from the eye can produce identical retinal images. Yet we have a compelling and immediately convincing sense of the three-dimensional depth of the visual world. The mathematical optics of Descartes and Malebranche had answered this through a geometrical theory: the mind unconsciously computes distance from the angle of convergence of the two eyes and the angle of incidence of light rays. Berkeley devotes the first section of the Essay to destroying this answer. The geometrical computation is too complex for ordinary perceivers to perform, most perceivers are entirely ignorant of the geometry involved, and — most importantly — no one actually experiences such a computation; we simply see things at distances without any felt inferential process.\n\nBerkeley\'s own theory replaces geometry with association. We learn to see distance through the correlation of visual cues — primarily the felt sensation of accommodating the eye\'s lens (which varies with the distance of the object being fixated), the degree of confusedness of the visual image at short range, and the angle of convergence of the eyes — with tangible experience. A child learning to reach for objects learns to correlate the visual sensation accompanying convergence with the tactile experience of contact at a certain distance. Over time these correlations become so habitual that the visual sensation immediately suggests the tactile distance, without any conscious inference.\n\nThis account has a consequence Berkeley emphasises: the objects of sight and the objects of touch are entirely heterogeneous and have no intrinsic or necessary connection. A visible sphere is a collection of light and colour in two dimensions. A tangible sphere is a collection of resistances and textures in three. There is no reason intrinsic to either experience why they should be associated — the association is learned and contingent. This means the three-dimensional spatial world we experience as laid out around us is not given directly in vision but is a construction of the mind working through habituated associations between visual and tactile ideas. The visual world, taken on its own, is what Berkeley calls a language of nature: a system of signs — the visual cues — which stand for, without resembling, the things they signify — the tangible realities. And a language requires a mind that established the conventions of signification. That mind is God.',
    themes: ['depth perception', 'association of ideas', 'heterogeneity of sight and touch', 'the language of nature', 'mathematical optics refuted', 'tactile vs visual space', 'learned vs innate perception', 'Molyneux problem'],
    keyCharacters: [],
    concepts: [
        'Visual depth perception as association not computation — distance is suggested, not directly seen',
        'Heterogeneity of sight and touch — the objects of the two senses have no intrinsic connection; their correlation is learned',
        'The minimum visible — the smallest discriminable visual element, which is not a geometric point but a finite magnitude',
        'Accommodation and convergence as visual distance cues — the felt effort of focusing as a sign for distance',
        'Visual language — the regular association between visual signs and tangible realities constituting a language God uses to instruct finite minds',
        'The Molyneux man would not see depth — a person given sight after blindness would initially see only a flat field of colour without depth'
    ],
    structure: '§1–51: The problem of distance — mathematical optics refuted; accommodation and convergence as the real cues\n§52–87: The heterogeneity of sight and touch; visible extension vs tangible extension\n§88–120: The Molyneux problem; visible magnitude vs tangible magnitude\n§121–159: Visible figure vs tangible figure; the visual world as a language of signs',
    quote: 'It is, I think, agreed by all that distance, of itself and immediately, cannot be seen. For distance being a line directed endwise to the eye, it projects only one point in the fund of the eye, which point remains invariably the same, whether the distance be longer or shorter.',
    additionalQuotes: [
        { text: 'The connexion of visible ideas with tangible ones is altogether arbitrary; the same visible idea might have been connected with an entirely different tangible experience from that which it now suggests, just as the same word might have been connected with an entirely different meaning.', source: 'New Theory of Vision §147' }
    ],
    commentary: [
        { philosopher: 'Helmholtz', text: 'Berkeley\'s theory of visual perception is the first systematic empirical theory in the history of vision science. His account of depth perception as dependent on learned associations rather than geometrical computation was confirmed by my own experiments on binocular vision and remains the foundation of the empirical tradition in perceptual psychology.' },
        { philosopher: 'J. J. Gibson', text: 'Berkeley wrongly assumed that the retinal image is informationally impoverished. The optic array contains rich information about depth through texture gradients and motion parallax. But Berkeley deserves credit for destroying the geometrical optics tradition and forcing a genuinely empirical approach.' }
    ],
    modernRelevance: 'The New Theory of Vision is the founding document of the empirical tradition in vision science and is still read in cognitive science, neuroscience of vision, and philosophy of perception. The Molyneux question Berkeley addresses was empirically tested in the twenty-first century with patients who had cataracts removed after years of blindness. The results broadly confirmed Berkeley\'s prediction: newly sighted patients struggled to identify by sight objects familiar to them through touch, supporting the heterogeneity thesis.',
    context: 'The Essay was published in May 1709, Berkeley\'s first major work, when he was twenty-four. He was a Fellow of Trinity College Dublin and had been developing the ideas in his private Philosophical Commentaries. The Essay was recognised as a genuine contribution to natural philosophy and scientific optics as well as philosophy, and it established Berkeley\'s scientific credentials before the more radical immaterialism of the Principles appeared the following year. Berkeley returned to its arguments in the Theory of Vision Vindicated and Explained (1733), written after criticisms had accumulated, in which he made the connection to immaterialism fully explicit.',
    relatedWorks: ['principles-human-knowledge', 'three-dialogues', 'alciphron']
},

{
    id: 'de-motu',
    title: 'De Motu',
    greekTitle: 'De Motu (On Motion)',
    philosopher: 'berkeley',
    category: 'method',
    categoryLabel: 'Philosophy of Science',
    date: '1721 AD',
    dateSort: 1721,
    emoji: '⚙️',
    cardSize: 'normal',
    readingDifficulty: 4,
    estimatedWordCount: 15000,
    shortDesc: 'Berkeley\'s philosophy of physics — a rigorous instrumentalist critique of Newtonian mechanics arguing that force, gravity, and absolute motion are not real physical entities but mathematical fictions useful for predicting experience.',
    summary: 'De Motu (On Motion) is Berkeley\'s most focused contribution to philosophy of science, written in 1720 and submitted for a prize competition at the Royal Academy of Sciences in Paris. Its argument is precise, technically informed, and philosophically consequential: the central concepts of Newtonian mechanics — absolute space, absolute time, absolute motion, force, gravity, and inertia — are not names of real physical entities or qualities but mathematical abstractions whose utility lies entirely in their power to generate accurate predictions about the behaviour of observable phenomena.\n\nBerkeley distinguishes sharply between what mechanics can legitimately say and what natural philosophers illegitimately read into its mathematical formalism. When Newton speaks of a force acting on a body, he introduces a term that has no correlate in sensory experience. We observe bodies moving; we do not observe force. When he speaks of absolute motion through absolute space, he posits an entity — infinite, homogeneous, mind-independent space — that we never perceive and could not perceive. Berkeley\'s objection is not merely epistemic but conceptual: the word force as used in mechanics does not name anything that could in principle be perceived. It is a mathematical symbol that enters into equations producing predictions about observable quantities. That is its entire legitimate function, and those who treat it as naming a real physical power commit the same error as those who treat the word substance as naming something beyond the observable qualities of things.\n\nThe implications for Newton\'s famous bucket experiment are direct. Newton had argued that the concavity of the rotating water surface — which persists even when the bucket itself is not moving relative to the water — proves that the water is rotating in absolute space. Berkeley argues that the bucket experiment proves nothing about absolute space because there is no such thing. Motion is always relative motion — relative to some perceived reference frame. The Newtonian formalism can be saved by replacing absolute space with the fixed stars as the reference frame for mechanics, which is precisely the move that Ernst Mach will make 150 years later in The Science of Mechanics, explicitly acknowledging Berkeley as his predecessor.',
    themes: ['instrumentalism in science', 'critique of absolute space and time', 'force as mathematical fiction', 'Newton\'s bucket argument', 'relative motion', 'the limits of mechanical explanation', 'observable vs theoretical entities'],
    keyCharacters: [],
    concepts: [
        'Instrumentalism — scientific theories are tools for prediction, not descriptions of unobservable reality',
        'Absolute space as fiction — Newton\'s container space is not an observable entity and therefore not a legitimate scientific concept',
        'Force as mathematical abstraction — mechanical force names no perceivable quality but is a symbol useful in equations',
        'Relative motion — all motion is motion relative to perceived reference objects; absolute motion is unintelligible',
        'The fixed stars as reference frame — a replacement for Newtonian absolute space with observable anchors'
    ],
    structure: '§1–17: Introduction; the legitimate object of natural philosophy\n§18–37: Force, gravity, and attraction as mathematical fictions\n§38–65: Absolute space, absolute motion, and the bucket argument refuted\n§66–72: The proper scope of mechanics; the limits of physical explanation',
    quote: 'Force, gravity, attraction, and terms of this sort are useful for reasonings and reckonings about motion and bodies in motion, but they do not help us understand the simple nature of motion itself, nor do they serve to designate so many distinct qualities. The physicist should be understood not as explaining things or asserting anything about their nature, but simply as marking certain observations useful for the purpose of calculation.',
    additionalQuotes: [
        { text: 'No motion can be understood without a determination of its relation to some body or other, that is, to some perceivable thing. Motion relative to nothing is inconceivable.', source: 'De Motu §63' }
    ],
    commentary: [
        { philosopher: 'Mach', text: 'Berkeley preceded me by 150 years in the critique of Newtonian absolute space and in the instrumentalist account of mechanical force. His De Motu should be required reading for every student of the foundations of mechanics. When he says that force names no real entity but is only a mathematical tool, he is entirely correct.' },
        { philosopher: 'Popper', text: 'Berkeley in De Motu anticipated the instrumentalist philosophy of science that became dominant in the twentieth century — the view that scientific theories are not true or false descriptions of reality but more or less useful instruments for predicting observations. This instrumentalism is, I believe, ultimately untenable, but Berkeley stated it more clearly than anyone before him.' }
    ],
    modernRelevance: 'De Motu\'s arguments map almost exactly onto the debates about the interpretation of quantum mechanics that have preoccupied physicists and philosophers since Bohr. The Copenhagen interpretation — that quantum mechanics is a tool for predicting measurement outcomes and that it is meaningless to ask what is happening between measurements — is instrumentalism in Berkeley\'s sense. His specific arguments about absolute space and relative motion were vindicated by Einstein\'s special theory of relativity.',
    context: 'Berkeley submitted De Motu to the Paris Academy in 1720 for its prize competition on the nature of motion. He did not win. He published it in London in 1721. The work shows that his engagement with Newton was both technically competent and philosophically searching — he had read the Principia and the Opticks carefully and his objections go to the foundations of the mechanical philosophy rather than its details.',
    relatedWorks: ['principles-human-knowledge', 'siris', 'alciphron']
}

);
"""

# ── data-15c.js ── Alciphron + Siris + Philosophical Commentaries ─────────────
data_15c = r"""window.WORKS.push(

{
    id: 'alciphron',
    title: 'Alciphron, or the Minute Philosopher',
    greekTitle: 'Alciphron, or the Minute Philosopher',
    philosopher: 'berkeley',
    category: 'practical',
    categoryLabel: 'Theology and Ethics',
    date: '1732 AD',
    dateSort: 1732,
    emoji: '🌅',
    cardSize: 'normal',
    readingDifficulty: 3,
    estimatedWordCount: 125000,
    shortDesc: 'Seven dialogues written on the coast of Rhode Island while waiting for a government grant that never came — Berkeley\'s most sustained defence of Christian theism against the freethinkers, deists, and moral relativists of the early Enlightenment.',
    summary: 'Alciphron, or the Minute Philosopher is Berkeley\'s largest and most ambitious work, composed during the three years he spent in Newport, Rhode Island (1728-1731) waiting for promised government funding for his Bermuda college that never arrived. Written in the form of seven extended dialogues set in an idealised rural landscape, it is both a sustained philosophical defence of Christian theism against Enlightenment freethought and a beautiful literary achievement — the landscape descriptions that open each dialogue are among the finest prose in eighteenth-century English. The Minute Philosopher of the title is the freethinker — the sceptic who, proud of his rationality, dismisses Christianity as superstition without having subjected either his own assumptions or the arguments for Christianity to serious examination.\n\nThe first three dialogues establish the moral and philosophical deficiencies of freethought through Berkeley\'s characters Alciphron and Lysicles — urbane, fashionable, and shallow representatives of the tradition running from Shaftesbury through Mandeville — who are engaged in conversation by Euphranor and Crito, who represent Berkeley\'s own positions. Berkeley\'s targets include Mandeville\'s reduction of all morality to self-interest dressed as virtue, Shaftesbury\'s appeal to a natural moral sense without divine sanction, and the general Deist position that natural religion suffices without revealed Christianity.\n\nThe Fourth Dialogue contains what many consider Berkeley\'s most original philosophical contribution in Alciphron: an extended analysis of religious and mathematical language that directly anticipates the philosophy of language developed by Frege, the logical positivists, and Wittgenstein. Berkeley\'s opponents had argued that religious language — terms like grace, sin, faith, the Trinity — is meaningless because such terms have no corresponding ideas that could be formed in the mind. Berkeley turns this argument on its head. Mathematical language — terms like force, infinite series, infinitesimals — also fails to correspond to clearly formed ideas, yet it is universally agreed to be meaningful and useful because its terms enter into valid inferences producing practically verifiable conclusions. Religious language operates similarly: the term grace may not correspond to any clearly imagined idea, but it directs the believer\'s conduct in determinate and practically significant ways. This is a functional or use theory of meaning a century and a half before Wittgenstein, and it is one of the most philosophically sophisticated passages in all of Berkeley\'s writing.',
    themes: ['freethought and its limits', 'moral sense theory challenged', 'Mandeville refuted', 'language without ideas', 'use theory of meaning', 'language of nature', 'argument for God from communication', 'defence of revelation', 'natural vs revealed religion'],
    keyCharacters: [
        { name: 'Alciphron', role: 'The minute philosopher — a fashionable freethinker in the Shaftesbury mould; superficially plausible, ultimately shallow' },
        { name: 'Lysicles', role: 'A more vulgar freethinker in the Mandeville tradition — willing to reduce all morality to self-interest and all religion to priestly manipulation' },
        { name: 'Euphranor', role: 'A simple farmer and Berkeley\'s primary voice — his rural good sense and genuine philosophical curiosity consistently expose the sophistication of the freethinkers as intellectual vanity' },
        { name: 'Crito', role: 'A gentleman scholar and secondary defender of Christianity — more learned than Euphranor, complementing his common-sense arguments with historical and theological scholarship' }
    ],
    concepts: [
        'The minute philosopher — the freethinker who prides himself on rationality but refuses to examine his own assumptions',
        'Language without ideas — meaningful language need not correspond to imageable ideas; function and inference are sufficient',
        'Grace as meaningful without an image — religious terms direct conduct without requiring clear and distinct ideas',
        'The language of nature as divine communication — God speaks to finite minds through the regular grammar of sensory experience'
    ],
    structure: 'Dialogue 1: Introduction of characters; the moral landscape of freethought\nDialogue 2: Mandeville and the reduction of morality to self-interest\nDialogue 3: Shaftesbury and the moral sense\nDialogue 4: The language theory of meaning; religious language defended\nDialogue 5: The language of nature; the argument for God from communication\nDialogue 6: Miracles and the evidences for Christianity\nDialogue 7: Faith, reason, and the rationality of Christian commitment',
    quote: 'I am not for imposing any sense on words against the received rules of language. But a word may be significant, although we have no idea annexed to it, provided it serves to regulate and influence our wills, passions, or conduct.',
    additionalQuotes: [
        { text: 'There are signs used in algebra which have no ideas answering to them, and yet are not without their use in reasoning. Words in general have other uses than to raise ideas.', source: 'Alciphron, Dialogue 7' }
    ],
    commentary: [
        { philosopher: 'Wittgenstein', text: 'The Fourth Dialogue of Alciphron is the text in which Berkeley comes closest to the insight I try to develop — that meaning is use, that the significance of a term lies not in the image it evokes but in the role it plays in a practice.' }
    ],
    modernRelevance: 'The Fourth Dialogue\'s theory of language is of enduring interest in philosophy of language and philosophy of religion. The argument that religious language is meaningful in the same way that mathematical language is meaningful — not through correspondence to imageable ideas but through its role in inference and conduct — is the most sophisticated defence of non-cognitive yet meaningful religious language before Wittgenstein and Ramsey.',
    context: 'Alciphron was written in Newport, Rhode Island, where Berkeley had arrived in 1728 with his wife and a small party, intending to found a college in Bermuda for the education of colonists and Native Americans. The government grant of £20,000 was never paid; Berkeley waited three years and returned to England in 1731, publishing the work the following year. The Rhode Island landscape — the coastal meadows, the sea horizon, the summer light — is vividly present in the dialogue\'s setting descriptions.',
    relatedWorks: ['principles-human-knowledge', 'three-dialogues', 'new-theory-vision', 'siris']
},

{
    id: 'siris',
    title: 'Siris: A Chain of Philosophical Reflexions',
    greekTitle: 'Siris',
    philosopher: 'berkeley',
    category: 'metaphysics',
    categoryLabel: 'Natural Philosophy',
    date: '1744 AD',
    dateSort: 1744,
    emoji: '🌿',
    cardSize: 'normal',
    readingDifficulty: 5,
    estimatedWordCount: 65000,
    shortDesc: 'Berkeley\'s strangest and most unexpected work — beginning as a medical treatise on the healing properties of tar-water and rising through a chain of philosophical reflections to a Neoplatonic theology of light, fire, and the world-soul.',
    summary: 'Siris is the most unusual philosophical work of the eighteenth century and the most perplexing production of Berkeley\'s career. Published in 1744, when Berkeley was 59 and had been Bishop of Cloyne for twelve years, it begins as a medical essay on the virtues of tar-water — an infusion of pine tar and water that Berkeley had encountered among Native Americans in Rhode Island and which he had used with apparent success against an epidemic of disease that swept his diocese — and then, through a chain of philosophical and theological reflections, ascends to a Neoplatonic account of God, light, fire, the aether, and the world-soul. The chain is the meaning of the title: Siris is from a Greek word for chain, and the work\'s structure as numbered paragraphs linked by association and analogy is both its organising principle and its philosophical method.\n\nThe medical sections went through six editions in the year of publication and generated a brief but intense public enthusiasm for tar-water as a remedy. Berkeley wrote An Additional Letter on Tar-Water the same year and maintained his advocacy for the remainder of his life. Berkeley was writing as a bishop in an impoverished Irish diocese during a period of severe hardship, and his interest in a cheap, widely available remedy for the poor was genuinely pastoral in motivation.\n\nThe philosophical and theological sections are what give Siris its permanent interest. Beginning from the chemistry of tar, Berkeley ascends through the ancient doctrine of fire as the principle of life, to the Stoic pneuma, to the Neoplatonic concept of light as the first emanation of the divine, to Plato\'s world-soul in the Timaeus, to a culminating theology in which God is understood not as a craftsman who created the world from outside but as the immanent light and life of all things. This represents a striking development from Berkeley\'s earlier thought: where the Principles had argued for a voluntarist God whose continuous exercise of will sustains the sensory world, Siris presents an emanationist God whose nature spontaneously generates finite minds and their world by a kind of intellectual radiation.\n\nScholars have long debated whether Siris represents a genuine philosophical development or a late retreat from the rigour of Berkeley\'s earlier immaterialism. The key question is whether Berkeley has abandoned the esse est percipi principle. In Siris he speaks of an underlying fire or aether as the physical substratum of life and motion — language that seems to reintroduce something like material substance. The most charitable interpretation is that Berkeley has refined rather than abandoned immaterialism: the aether is itself a collection of ideas in God\'s mind, the physical mechanism God uses to connect and order the finite experiences of created minds.',
    themes: ['tar-water as medicine', 'fire and life', 'Neoplatonism', 'world-soul', 'light as divine emanation', 'Stoic pneuma', 'Platonic theology', 'the ascent from nature to God', 'development of Berkeley\'s immaterialism'],
    keyCharacters: [],
    concepts: [
        'The chain of being — the hierarchical order from matter through life through mind through soul to God, providing the structural principle of the argument',
        'Fire as the principle of life — the ancient doctrine, traced through Hippocrates, Heraclitus, and the Stoics, that vital warmth is the source of all animate motion',
        'The aether — the subtle, mobile medium that Berkeley, following Newton\'s unpublished speculations, posits as the vehicle of light, heat, and vital spirit',
        'The world-soul — the Platonic concept, from the Timaeus, of a soul that animates and orders the cosmos as a whole',
        'Light as first emanation — the Neoplatonic doctrine, from Plotinus and Proclus, that the first generation of the divine is light, from which all subsequent being flows'
    ],
    structure: '§1–67: The medical virtues of tar-water — its preparation, chemistry, and therapeutic uses\n§68–152: Philosophical reflections on fire, light, aether, and vital spirit\n§153–224: Ancient philosophy of nature — the Stoics, Hippocrates, Plato, and the Timaeus\n§225–294: Neoplatonic theology — Plotinus, Proclus, and the emanation of light from God\n§295–368: The ascent to the One — God as pure intelligence, light, and source of all being',
    quote: 'Tar-water is of a nature so mild and benign and proportioned to the human constitution, as to warm without heating, to cheer but not inebriate, and to give a kindly natural heat.',
    additionalQuotes: [
        { text: 'We are led upward from effects to causes, from particular to general, from things corporeal to things incorporeal, from visible nature to the invisible source of all things.', source: 'Siris §303' }
    ],
    commentary: [
        { philosopher: 'Yeats', text: 'I find in Siris, in its mystical final sections, the truth that Berkeley did not publish in his youth because it could not yet be thought clearly — that the world is the self-expression of divine mind, and that philosophy ends in a theology of light. Of all the Irish philosophers Berkeley is the deepest, and Siris is the depth of Berkeley.' }
    ],
    modernRelevance: 'Siris has attracted increasing scholarly attention for the originality and depth of its Neoplatonic theology and for what it suggests about the development of Berkeley\'s thought. Its critique of mechanical explanation as inherently incomplete — unable to account for life and consciousness without presupposing them — anticipates the contemporary debate between physicalism and non-reductive views of mind.',
    context: 'Berkeley moved to Cloyne as Bishop in 1734. The epidemic that prompted his interest in tar-water struck his diocese in the early 1740s. He published Siris in Dublin in February 1744. Horace Walpole wrote about "the Bishop of Cloyne\'s tar-water madness." Berkeley resigned the bishopric in 1752 and moved to Oxford, where he died suddenly in January 1753 while his wife was reading to him.',
    relatedWorks: ['principles-human-knowledge', 'alciphron', 'three-dialogues']
},

{
    id: 'philosophical-commentaries',
    title: 'Philosophical Commentaries',
    greekTitle: 'Philosophical Commentaries (Notebooks)',
    philosopher: 'berkeley',
    category: 'method',
    categoryLabel: 'Philosophical Notebooks',
    date: '1707–1708 AD',
    dateSort: 1707,
    emoji: '📓',
    cardSize: 'normal',
    readingDifficulty: 4,
    estimatedWordCount: 45000,
    shortDesc: 'Berkeley\'s private notebooks from age 21 to 23 — the workshop in which immaterialism was invented for the first time in the history of philosophy, recorded in compressed, cryptic, and sometimes contradictory fragments of extraordinary freshness.',
    summary: 'The Philosophical Commentaries — known until the twentieth century as the Commonplace Book — are Berkeley\'s private philosophical notebooks, written between 1707 and 1708 when he was twenty-one to twenty-three years old and still a Fellow of Trinity College Dublin. They were never intended for publication and remained in manuscript until the twentieth century, when A. A. Luce\'s meticulous editorial work established their text and dating. They consist of approximately nine hundred numbered entries in two notebooks, ranging from single-sentence jottings to compressed paragraphs, and they record the moment-by-moment development of Berkeley\'s immaterialist philosophy — its invention, its testing against objections, its refinement, and its crystallisation into the positions he would publish in the New Theory of Vision (1709) and the Principles (1710).\n\nThe Commentaries are unique in the history of philosophy as a record of genuine philosophical discovery in real time. Most philosophical texts present positions already worked out; here we watch Berkeley working them out. We see him struggling with the consequences of his own principles, abandoning positions, reinstating them, discovering objections he cannot immediately answer, puzzling over what he means by spirit and whether he has a coherent account of it, worrying about whether his attack on abstract ideas is consistent with his use of general terms in his own arguments, and repeatedly reminding himself — in memoranda written to himself — of points he must address before publication.\n\nThe most historically significant entries are those in which Berkeley first formulates the esse est percipi principle and realises its full implications. Entry 429 reads: "Existence is percipi or percipere" — the first written statement of what became the central principle of the Principles. Entries in the following pages show Berkeley working out the implications: if unperceived things do not exist, what happens to the table when no one is in the room? How does the continuity of the physical world depend on God\'s continuous perception? Is Berkeley\'s own principle of esse est percipi an idea in itself, and if so is it mind-dependent in the same way? These are the questions to which the Principles and the Three Dialogues are extended public answers.\n\nThe Commentaries also reveal Berkeley\'s debts and targets more clearly than the published works. Locke is present on almost every page as the source of the framework Berkeley is simultaneously using and subverting. Malebranche appears repeatedly as the thinker whose occasionalism Berkeley both admires and sees himself as correcting. Newton is a constant presence as the source of the physics Berkeley must account for without matter. And Descartes — whose cogito provides the model for Berkeley\'s starting point in the immediately certain existence of perceiving minds — is criticised for having posited two substances where one will do.',
    themes: ['philosophical invention in real time', 'esse est percipi discovered', 'Berkeley\'s debts to Locke and Malebranche', 'the problem of spirit', 'continuity between perceptions', 'Newtonian physics and immaterialism', 'abstract ideas attacked', 'self-examination as philosophical method'],
    keyCharacters: [],
    concepts: [
        'The first formulation of esse est percipi — Entry 429 and its immediate context in the notebook',
        'The problem of spirit — Berkeley\'s difficulty in giving an account of minds and souls without using the very concept of substance he has just destroyed',
        'Self-memoranda — entries addressed by Berkeley to himself, marking doctrines to be qualified or problems to be solved before publication',
        'The debt to Locke — Berkeley working always within the framework of ideas and impressions he inherits from the Essay',
        'Malebranche as the nearest precursor — Berkeley repeatedly marking his difference from the doctrine of seeing all things in God while acknowledging its kinship with his own position'
    ],
    structure: 'Two notebooks (A and B in Luce\'s edition, reversed in their actual composition order). Entries numbered 1–899 in the standard edition. The standard edition marks entries with letters indicating their subject — M for mind, P for perception, N for nature and science, G for God — allowing thematic reading across the chronological sequence.',
    quote: 'I wonder not at my sagacity in discovering the obvious tho amazing truth, I rather wonder at my stupidity in not finding it out before.',
    additionalQuotes: [
        { text: 'Existence is percipi or percipere.', source: 'Philosophical Commentaries §429' },
        { text: 'Nothing properly but persons i.e. conscious things do exist, all other things are not so much existences as manners of the existence of persons.', source: 'Philosophical Commentaries §24' }
    ],
    commentary: [
        { philosopher: 'Luce', text: 'The Commentaries are the most important document in Berkeley scholarship — they let us trace the genesis of immaterialism itself, the moment when a young man of twenty-one first saw that the Lockean framework, consistently followed, dissolved matter entirely. No other philosophical notebook in history shows us so precisely the moment of invention.' }
    ],
    modernRelevance: 'The Commentaries are important both as a historical document and as a model of philosophical practice. Their record of genuine intellectual struggle — of a thinker who does not know where his arguments will lead and who follows them honestly even when they are uncomfortable — has been cited as a model of philosophical integrity. The specific puzzles Berkeley records — about personal identity, the continuity of experience, the nature of self-knowledge — remain central topics in philosophy of mind.',
    context: 'The two notebooks were preserved in manuscript among Berkeley\'s papers. A. A. Luce established their correct order, dating, and text in his 1944 edition, correcting two centuries of misreadings. The standard modern edition appears as Volume 1 of The Works of George Berkeley, Bishop of Cloyne, edited by Luce and Jessop (1948-1957).',
    relatedWorks: ['principles-human-knowledge', 'new-theory-vision', 'three-dialogues']
}

);
"""

files = {
    'data-15a.js': data_15a,
    'data-15b.js': data_15b,
    'data-15c.js': data_15c,
}

for filename, content in files.items():
    path = os.path.join(js_dir, filename)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    lines = content.count('\n')
    print(f"Written {filename} — {lines} lines → {path}")

print("\nBerkeley files complete.")
