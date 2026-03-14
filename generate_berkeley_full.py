#!/usr/bin/env python3
"""
Run from inside ~/Desktop/philosophy-archive/
  python3 generate_berkeley_full.py
Writes js/data-15a.js through js/data-15e.js  (overwrites)
"""
import os
js_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'js')
os.makedirs(js_dir, exist_ok=True)

# ── 15a: Principles of Human Knowledge ──────────────────────────────────────
data_15a = r"""/* DATA PART 15a — Principles of Human Knowledge (Berkeley) */
window.WORKS.push(
{
    id: 'principles-human-knowledge',
    title: 'A Treatise Concerning the Principles of Human Knowledge',
    greekTitle: 'A Treatise Concerning the Principles of Human Knowledge',
    philosopher: 'berkeley',
    category: 'metaphysics',
    categoryLabel: 'Metaphysics',
    date: '1710 AD',
    dateSort: 1710,
    emoji: '👁',
    cardSize: 'wide',
    readingDifficulty: 'Advanced',
    estimatedWordCount: 35000,
    shortDesc: 'The book that abolished matter — Berkeley\'s systematic demonstration that the physical world is composed entirely of ideas in minds, that esse est percipi, and that the very notion of unperceived material substance is an incoherent abstraction.',
    summary: 'The Treatise Concerning the Principles of Human Knowledge, published in 1710 when Berkeley was just twenty-five, is one of the most audacious and brilliantly argued works in the entire history of philosophy. Its central thesis — that material substance does not exist, that the objects of the physical world are nothing but collections of ideas perceived by minds, and that for a thing to exist is simply for it to be perceived (esse est percipi) — struck Berkeley\'s contemporaries as absurd, paradoxical, or insane. Yet the arguments he advances in its defence are among the most rigorous in early modern philosophy, and no philosopher from Hume to the present has been able simply to dismiss them.\n\nBerkeley\'s argument proceeds in stages. He begins with Locke\'s epistemology — that the immediate objects of the mind are ideas — and then asks the devastating question that Locke never adequately addressed: if all we ever perceive are our own ideas, what grounds have we for believing that material objects exist behind or beyond those ideas? Locke had posited a "material substance" as the substratum supporting the qualities we perceive, but Berkeley demonstrates that this notion is empty. To conceive of an unperceived tree is already to perceive it in conception; the supposed "unconceived thing" is therefore always already conceived. The famous master argument of §22–23 turns on exactly this point: it is impossible even to conceive of something existing unconceived, because the act of conception is itself a form of perception.\n\nFrom the impossibility of unperceived material existence Berkeley draws his positive metaphysics: reality consists of minds (spirits) and ideas. Ideas are passive — they have no causal power — and their order, regularity, and vivacity require an explanation. That explanation is God, the infinite mind who perceives all ideas at all times, sustaining the physical world in continuous existence and guaranteeing its order through what we call the "laws of nature." Berkeley\'s God is thus not a distant creator but the constant perceiver whose uninterrupted perception is the very being of the physical world.\n\nThe Principles also contains Berkeley\'s sustained attack on abstract general ideas, his theory of mathematics and its application to physics, and his critique of the Newtonian concepts of absolute space, time, and motion — arguments that would influence Mach and, through Mach, Einstein.',
    themes: ['Immaterialism', 'Esse Est Percipi', 'Critique of Material Substance', 'Abstract Ideas', 'God as Infinite Perceiver', 'Idealism', 'Empiricism Against Its Own Conclusions', 'Philosophy of Mathematics', 'Critique of Newtonian Absolute Space'],
    keyCharacters: [
        { name: 'God', role: 'The infinite perceiver whose continuous perception sustains the physical world in existence — not a distant creator but the immediate ground of all that exists' },
        { name: 'John Locke (implicit)', role: 'Berkeley\'s chief point of departure — the Principles takes Locke\'s epistemology seriously enough to demolish it from within' }
    ],
    concepts: [
        'Esse est percipi (vel percipere) — to be is to be perceived (or to perceive); the fundamental principle of immaterialism',
        'Immaterialism — the denial that material substance exists; reality consists of minds and ideas only',
        'The master argument — it is impossible to conceive of an unconceived object, because conceiving is itself perceiving; the self-refuting character of materialism',
        'Critique of abstract ideas — there is no such thing as an abstract general idea; all ideas are particular; the abstraction of "material substance" names nothing',
        'Ideas as passive — ideas have no causal power whatsoever; they are inert objects of perception, not agents',
        'Spirit (mind) as the only substance — only minds are genuine substances; they are active, perceiving, willing beings',
        'God as infinite perceiver — God sustains the physical world in existence by perceiving all ideas continuously and is the cause of the order we call natural law',
        'Laws of nature as regularities in God\'s ideas — natural laws are the grammar of God\'s visual language, not mechanical necessities in mind-independent matter',
        'Primary and secondary qualities collapsed — Berkeley denies Locke\'s distinction; extension, figure, and motion are as mind-dependent as colour and taste',
        'Material substance as meaningless — the concept of a substance supporting qualities while itself having no qualities is not obscure but empty'
    ],
    structure: 'Introduction: Berkeley\'s purpose and the source of philosophical error — the doctrine of abstract ideas\n§1–33: The esse est percipi thesis; the impossibility of material substance; the master argument\n§34–84: Objections and replies — Berkeley anticipates and answers every major criticism\n§85–100: The nature of spirit; God as the cause of ideas\n§101–117: Mathematics, infinity, and the critique of abstract ideas\n§118–156: Application to natural philosophy; critique of absolute space, time, and motion',
    quote: 'Some truths there are so near and obvious to the mind, that a man need only open his eyes to see them. Such I take this important one to be, to wit, that all the choir of heaven and furniture of the earth, in a word all those bodies which compose the mighty frame of the world, have not any subsistence without a mind — that their being is to be perceived or known.',
    additionalQuotes: [
        { text: 'But say you, surely there is nothing easier than to imagine trees, for instance, in a park, or books existing in a closet, and nobody by to perceive them. I answer, you may so, there is no difficulty in it: but what is all this, I beseech you, more than framing in your mind certain ideas which you call books and trees, and at the same time omitting to frame the idea of any one that may perceive them? But do not you yourself perceive or think of them all the while?', citation: 'Principles of Human Knowledge §23' },
        { text: 'In short, if there were external bodies, it is impossible we should ever come to know it; and if there were not, we might have the very same reasons to think there were that we have now.', citation: 'Principles of Human Knowledge §20' },
        { text: 'The table I write on, I say, exists — that is, I see and feel it; and if I were out of my study I should say it existed — meaning thereby that if I was in my study I might perceive it, or that some other spirit actually does perceive it.', citation: 'Principles of Human Knowledge §3' }
    ],
    commentary: [
        { philosopher: 'David Hume', text: 'Hume\'s verdict on the Principles was both the most admiring and the most damaging assessment a philosopher could receive: "Berkeley\'s arguments admit of no answer and produce no conviction." What Hume meant is that the arguments are logically impeccable — no specific step can be identified as fallacious — yet the conclusion is one that no sane person actually believes. This diagnosis is philosophically devastating, because it implies that something must be wrong with the premises, even if we cannot say what. Hume himself drew a different conclusion from Berkeley\'s arguments: not that God sustains the world in perception but that the very notion of external object, like the very notion of material substance, is a philosophical fiction. Berkeley had intended his arguments to secure the existence of God and the spiritual nature of reality; Hume used the same arguments to dissolve both God and matter into the perpetual flux of impressions.' },
        { philosopher: 'Immanuel Kant', text: 'Kant\'s engagement with the Principles was complex and sometimes evasive. He explicitly distinguished his own "transcendental idealism" from Berkeley\'s "empirical idealism" — the view he attributed to Berkeley that bodies are illusions. Kant insisted that his own doctrine granted the physical world "empirical reality" as the necessarily structured product of the forms of intuition and the categories of the understanding. But Berkeley had specifically denied that he was making the world illusory — he was insisting on the reality of the perceived world against the skeptical implications of Lockean materialism. Kant\'s "Refutation of Idealism" in the second Critique edition — attempting to show that the permanence of outer objects is a precondition for inner experience — is directed at a position Berkeley never held, yet it remains one of Kant\'s most important contributions to epistemology.' },
        { philosopher: 'Bertrand Russell', text: 'Russell\'s assessment in The Problems of Philosophy (1912) was characteristically precise: "Berkeley was right that we have no direct knowledge of material objects; where he went wrong was in failing to see that the hypothesis of their existence is the simplest explanation of the regularities in our experience." This is the scientific realist\'s response to Berkeley: even if we cannot perceive matter directly, its existence is the best inference to the explanation of the coherence of our perceptions. But Berkeley had anticipated exactly this objection and had an answer: the "simplest explanation" for the regularities of perception is not an unperceivable material substance but God, whose rational and consistent will produces the ordered language of nature that we call physical law. Whether this answer is more parsimonious than scientific realism is a question Berkeley pressed and Russell never adequately answered.' },
        { philosopher: 'Karl Popper', text: 'Popper\'s "A Note on Berkeley as Precursor of Mach and Einstein" (1953) identified the Principles\' critique of absolute space and motion as its most scientifically significant contribution. Berkeley\'s argument — that absolute motion is meaningless because motion is always relative to some perceived reference frame, and that Newtonian absolute space is an empty abstraction — is identical in essential structure to Mach\'s critique of Newton and to Einstein\'s operationalist reasoning in special relativity. Popper argued that Berkeley should be recognized as the originator of the relational theory of space that the twentieth century vindicated. The irony is profound: the philosopher who denied the existence of matter anticipated the conceptual revolution in the physics of matter.' },
        { philosopher: 'A.A. Luce', text: 'Luce\'s Berkeley\'s Immaterialism (1945) did more than any other single work to rescue the Principles from systematic misreading. The most common misreading is the assumption that Berkeley denied the reality of the physical world — that tables and chairs are illusions. Berkeley was claiming precisely the opposite: that it is materialist philosophy, not immaterialism, that leads to skepticism about the external world. If matter is an unperceivable substance behind our ideas, we can never know whether our ideas correspond to it. Berkeley\'s world is the world of common experience; the difference is simply that he correctly identifies what this world consists in — ideas in minds, not a mind-independent material substrate that we can never perceive.' },
        { philosopher: 'Samuel Johnson', text: 'Boswell records the most famous "refutation" of the Principles: Johnson striking his foot against a large stone with mighty force and declaring "I refute it thus." Berkeley had of course anticipated this objection in §§34–40: kicking a stone does not prove that the stone exists independently of all perception — it proves only that certain tactile ideas follow certain visual ones in a regular sequence, exactly what immaterialism predicts. Johnson\'s refutation was of a Berkeley he had not read; the real Berkeley was unmoved.' }
    ],
    modernRelevance: 'Berkeley\'s immaterialism has experienced a remarkable revival in contemporary philosophy. His arguments against the coherence of "matter" as a philosophical concept have been compared to the difficulties quantum mechanics poses for classical realism — the observer-dependence of quantum measurement echoes his thesis that existence requires perception. His attack on absolute space influenced Mach\'s critique of Newtonian mechanics, which in turn influenced Einstein\'s development of general relativity. His thesis that the physical world is fundamentally informational has been compared to John Wheeler\'s "it from bit" hypothesis and to contemporary information-theoretic approaches to quantum mechanics.',
    context: 'Berkeley wrote the Principles at Trinity College Dublin between 1708 and 1709, drawing on the philosophical notebooks he had kept since 1707 (now known as the Philosophical Commentaries). He was twenty-five when it was published in Dublin in 1710. The reception was devastating: readers assumed it was a joke, a provocation, or the product of insanity. The poor reception led him to restate the arguments in the more accessible Three Dialogues (1713). He had planned a second part covering ethics and natural philosophy, but the manuscript was reportedly lost during his travels in Italy (1716–1720) and was never reconstructed — one of the great losses in the history of philosophy.',
    relatedWorks: ['three-dialogues', 'essay-towards-new-theory-vision', 'de-motu', 'siris', 'philosophical-commentaries']
}
);
"""

# ── 15b: Three Dialogues ─────────────────────────────────────────────────────
data_15b = r"""/* DATA PART 15b — Three Dialogues between Hylas and Philonous (Berkeley) */
window.WORKS.push(
{
    id: 'three-dialogues',
    title: 'Three Dialogues between Hylas and Philonous',
    greekTitle: 'Three Dialogues between Hylas and Philonous',
    philosopher: 'berkeley',
    category: 'metaphysics',
    categoryLabel: 'Metaphysics',
    date: '1713 AD',
    dateSort: 1713,
    emoji: '💬',
    cardSize: 'wide',
    readingDifficulty: 'Intermediate',
    estimatedWordCount: 45000,
    shortDesc: 'The most beautifully written philosophical dialogue since Plato — Berkeley restates his immaterialism through a dramatic conversation in which the materialist Hylas is led, step by devastating step, to the conclusion that matter does not exist.',
    summary: 'The Three Dialogues between Hylas and Philonous, published in London in 1713, is Berkeley\'s masterpiece of philosophical argumentation and one of the finest examples of the dialogue form in the history of philosophy. Written because the Principles of Human Knowledge had been universally misunderstood, the Three Dialogues restates the case for immaterialism with a dramatic vividness and argumentative patience that the treatise form could not achieve. The two characters — Hylas (from the Greek hylē, "matter"), who defends common-sense materialism, and Philonous (from the Greek philos nous, "lover of mind"), who is Berkeley himself — meet on three successive mornings in a college garden and conduct an extended philosophical conversation that moves from confident materialism to its complete abandonment.\n\nThe First Dialogue is a systematic dismantling of the distinction between primary and secondary qualities. Hylas begins by asserting that at least some qualities — extension, figure, motion, solidity — belong to material objects independently of any perceiver. Philonous shows, through a series of devastating arguments about the relativity of perception, that primary qualities are no more mind-independent than secondary ones. Hylas retreats again and again — from naive realism to representative realism to various forms of the material substrate theory — and each retreat is shown to be untenable.\n\nThe Second Dialogue addresses the positive doctrine: if there is no material substance, what sustains the physical world in existence? Philonous argues that the order, regularity, vivacity, and involuntariness of our sensory ideas require an infinite mind — God — who perceives all things at all times. The "laws of nature" are the regular grammar of God\'s ideas, the language through which the divine mind communicates with finite minds. This is not a skeptical doctrine: Berkeley insists throughout that he is defending the reality of the physical world against the skepticism to which materialism inevitably leads.\n\nThe Third Dialogue is the most philosophically rich. Philonous addresses a battery of objections: that immaterialism makes the world an illusion, that it contradicts the testimony of the senses, that it makes creation before human perception impossible. Each objection is met with extraordinary subtlety and force. The dialogue concludes with Hylas\'s full conversion — and his recognition that it is materialism, not immaterialism, that leads to skepticism about the external world.',
    themes: ['Immaterialism Restated', 'Primary and Secondary Qualities', 'The Relativity of Perception', 'God as Infinite Perceiver', 'The Language of Nature', 'Anti-Skepticism', 'Philosophical Dialogue as Form', 'The Reality of the Sensible World'],
    keyCharacters: [
        { name: 'Hylas', role: 'The materialist — his name derives from the Greek hylē (matter); he defends the existence of material substance with intelligence and persistence, and his successive retreats constitute the dramatic architecture of the work' },
        { name: 'Philonous', role: 'The lover of mind — Berkeley\'s spokesman; his arguments move from the negative (the incoherence of material substance) to the positive (God as the sustaining perceiver) with patience, courtesy, and literary grace' }
    ],
    concepts: [
        'The argument from perceptual relativity — the same object produces different sensory ideas in different conditions, proving that sensible qualities are mind-dependent',
        'The collapse of the primary/secondary quality distinction — extension, figure, and motion are as perceiver-dependent as colour, taste, and temperature',
        'The incoherence of material substrate — the idea of a substance that supports qualities but has no qualities of its own is not obscure but meaningless',
        'God as the guarantor of continuity — objects continue to exist when no finite mind perceives them because God perceives them always',
        'The divine visual language — the regularities we call laws of nature are the syntax of God\'s communication with finite minds; nature is a language, not a machine',
        'Anti-skepticism — immaterialism is not a form of skepticism but its cure; materialism, by interposing an unknowable substance between us and reality, is the true source of doubt',
        'Real things vs chimeras — real ideas are vivid, ordered, involuntary, and coherent; hallucinations and fantasies lack these features'
    ],
    structure: 'First Dialogue: The dismantling of materialism\n— Heat, colour, taste, sound shown to be ideas in the mind\n— Extension, figure, motion shown to be equally mind-dependent\n— The failure of representative realism as a fallback\n— Hylas\'s successive retreats from every form of materialism\n\nSecond Dialogue: The positive doctrine\n— The cause of sensory ideas: God as infinite perceiver\n— Nature as the language of God; creation and continuity without matter\n\nThird Dialogue: Objections and replies\n— Is immaterialism an illusion doctrine?\n— How does it distinguish reality from hallucination?\n— Hylas\'s conversion and the vindication of common sense',
    quote: 'I am not for changing things into ideas, but rather ideas into things; since those immediate objects of perception, which according to you are only appearances of things, I take to be the real things themselves.',
    additionalQuotes: [
        { text: 'PHILONOUS: Can a real thing in itself invisible be like a colour; or a real thing which is not audible be like a sound? In a word, can anything be like a sensation or idea, but another sensation or idea?', citation: 'Three Dialogues, First Dialogue' },
        { text: 'PHILONOUS: The same principles which, at first view, lead to scepticism, pursued to a certain point, bring men back to common sense.', citation: 'Three Dialogues, Third Dialogue' },
        { text: 'HYLAS: You can never persuade me, Philonous, that the denying of matter or corporeal substance is not the most extravagant opinion that ever entered into the mind of man. PHILONOUS: And yet, Hylas, I defy you to show me any one argument against it which does not equally militate against every other opinion in philosophy.', citation: 'Three Dialogues, First Dialogue' }
    ],
    commentary: [
        { philosopher: 'J.L. Austin', text: 'Austin\'s Sense and Sensibilia (1962) takes Berkeley as one of its primary targets, but Austin\'s admiration for the Three Dialogues as a philosophical text is evident throughout. He acknowledged that Berkeley\'s arguments against the coherence of "material substance" are more powerful than most philosophers have been willing to admit. Austin\'s own method — the patient, precise analysis of how ordinary language actually works — owes something to the Three Dialogues\' technique of tracking the successive retreats of the materialist position through its various formulations. Where Austin and Berkeley diverge is in Austin\'s rejection of the sense-datum framework entirely: Austin thinks Berkeley\'s mistake was to accept Locke\'s epistemology (that we perceive only ideas) before demolishing Locke\'s metaphysics (that ideas are caused by matter).' },
        { philosopher: 'John Stuart Mill', text: 'Mill\'s assessment was characteristically direct: "Berkeley\'s idealism has never been refuted; it has only been disbelieved." Mill was himself drawn to a version of phenomenalism — the view that physical objects are "permanent possibilities of sensation" — that is closer to Berkeley\'s position than he always acknowledged. His own account of matter as the stable structure of possible sensations is immaterialism without God: the regularities that Berkeley attributes to the constant will of an infinite perceiver, Mill attributes to the brute order of the natural world conceived as a system of experiences. The question of whether this naturalized phenomenalism is more defensible than Berkeley\'s theistic version has never been definitively answered.' },
        { philosopher: 'G.J. Warnock', text: 'Warnock\'s Berkeley (1953) identified the Three Dialogues as Berkeley\'s supreme achievement: "a work that combines the rigour of a treatise with the life of a drama." Warnock\'s specific contribution was to clarify the structure of the First Dialogue\'s argument: Berkeley does not proceed simply by showing that sensible qualities are variable across perceivers. He proceeds more subtly, by showing that Hylas\'s successive attempts to find a mind-independent quality — starting with secondary qualities and retreating to primary ones — each collapse when subjected to the same analysis. The systematic character of the retreat is what gives the First Dialogue its philosophical force.' },
        { philosopher: 'Michael Ayers', text: 'Ayers argued that Berkeley is the most underestimated major philosopher in the Western tradition — that the Three Dialogues contains arguments against the coherence of representationalist epistemology that have never been adequately answered. The specific argument Ayers highlighted is Philonous\'s claim that if our immediate objects of perception are always ideas, there is no coherent account of what it would mean for an idea to "resemble" a material quality it supposedly represents. Representationalism destroys itself from within, and Berkeley\'s arguments in the Three Dialogues are the most rigorous demonstration of this self-destruction available in the history of philosophy.' }
    ],
    modernRelevance: 'The Three Dialogues\' arguments against material substance have gained new life in contemporary philosophy of perception. The debate between direct realism, representationalism, and phenomenalism is conducted in Berkeleyan terms. In philosophy of science, Berkeley\'s contention that science describes regularities in experience rather than uncovering the hidden machinery of a mind-independent world has been compared to structural realism and to the instrumentalist interpretation of quantum mechanics. His argument that we can never compare our ideas with the "real things" they supposedly represent anticipates the problem of the "view from nowhere" in contemporary epistemology.',
    context: 'Berkeley wrote the Three Dialogues in London in 1712–1713, during a period of intense intellectual and social activity. The dialogue form was chosen deliberately: it allowed Berkeley to dramatize the conversion of a materialist, to anticipate objections in real time, and to deploy the literary charm that was one of his greatest assets. The Three Dialogues was far better received than the Principles and remains the text through which most readers first encounter Berkeley\'s philosophy. It was published in the same year that Berkeley met Jonathan Swift, Alexander Pope, and Joseph Addison.',
    relatedWorks: ['principles-human-knowledge', 'essay-towards-new-theory-vision', 'de-motu', 'alciphron']
}
);
"""

# ── 15c: Essay towards a New Theory of Vision + De Motu ─────────────────────
data_15c = r"""/* DATA PART 15c — Essay towards a New Theory of Vision + De Motu (Berkeley) */
window.WORKS.push(

{
    id: 'essay-towards-new-theory-vision',
    title: 'An Essay towards a New Theory of Vision',
    greekTitle: 'An Essay towards a New Theory of Vision',
    philosopher: 'berkeley',
    category: 'natural-philosophy',
    categoryLabel: 'Natural Philosophy',
    date: '1709 AD',
    dateSort: 1709,
    emoji: '🔭',
    cardSize: 'normal',
    readingDifficulty: 'Intermediate',
    estimatedWordCount: 30000,
    shortDesc: 'Berkeley\'s revolutionary first work — a theory of visual perception that demolished the geometrical optics of Descartes and Molyneux and laid the philosophical foundations for immaterialism before the word was ever used.',
    summary: 'The Essay towards a New Theory of Vision, published in 1709 when Berkeley was twenty-four, is the first published work of his philosophical career and one of the most original contributions to the philosophy of perception ever written. Its immediate topic is how we perceive distance, magnitude, and situation by sight — a question treated by the optical tradition as a problem of geometry. Berkeley demolishes this geometrical theory: the angles and lines of optical theory are not themselves perceived — they are theoretical constructs never experienced by the perceiver. A person born blind and suddenly made to see would have no idea of distance; distance is not a visual datum but something learned through the correlation of visual ideas with tactile ideas over time.\n\nFrom this analysis Berkeley draws a conclusion of enormous philosophical significance: the objects of sight and the objects of touch are entirely different. A visible square and a tangible square are not two perceptions of the same object but two different ideas habitually associated. There is no "common sensible" perceived by both sight and touch. The visible world and the tangible world are two distinct systems of ideas, correlated by experience and — Berkeley will later argue — by God\'s design as a divine visual language. The Essay laid the philosophical groundwork for the Principles: if the objects of sight are ideas in the mind, not external material things, then extending this argument to all sensible qualities yields immaterialism.',
    themes: ['Visual Perception', 'Distance Perception', 'The Molyneux Problem', 'The Heterogeneity of Sight and Touch', 'Critique of Geometrical Optics', 'The Divine Visual Language', 'Empiricist Psychology'],
    keyCharacters: [
        { name: 'William Molyneux (implicit)', role: 'The philosopher whose famous problem — could a man born blind, made to see, immediately distinguish a cube from a sphere? — is central to Berkeley\'s argument for the heterogeneity of sight and touch' }
    ],
    concepts: [
        'Distance is not immediately perceived by sight — it is a learned construction; no direct correlate of distance exists in the visual field',
        'The Molyneux problem — a person born blind and made to see could not immediately identify shapes by sight alone; visual and tactile ideas are entirely heterogeneous',
        'The heterogeneity thesis — the objects of sight and touch are entirely different kinds of ideas, not two perceptions of one mind-independent object',
        'Geometrical optics refuted — the lines and angles of optical theory are mathematical abstractions, not perceived data; no one perceives the angles of convergence',
        'The divine visual language — visual ideas are signs that God uses to communicate information about the tangible world to finite minds',
        'Suggestion and association — the mechanism by which visual cues come to indicate distance and magnitude through habitual correlation with tactile experience'
    ],
    structure: '§1–28: Distance is not immediately seen; refutation of geometrical optics\n§29–51: How we learn to perceive distance — convergence, confusion, faintness as learned cues\n§52–87: The magnitude of objects — visible and tangible magnitude are entirely distinct\n§88–120: Situation — how we learn that objects are upright (the inverted retinal image problem)\n§121–159: The heterogeneity of sight and touch; the visible world as a divine language\nAppendix (1732 edition): Berkeley\'s mature reflections connecting the essay to immaterialism',
    quote: 'We never see and feel one and the same object. That which is seen is one thing, and that which is felt is another.',
    additionalQuotes: [
        { text: 'Those lines and angles have no real existence in nature, being only an hypothesis framed by the mathematicians, and by them introduced into optics, that they might treat of that science in a geometrical way.', citation: 'New Theory of Vision §12' },
        { text: 'Upon the whole, I think we may fairly conclude that the proper objects of vision constitute a universal language of the Author of Nature, whereby we are instructed how to regulate our actions in order to attain those things that are necessary to the preservation and well-being of our bodies.', citation: 'New Theory of Vision §147' }
    ],
    commentary: [
        { philosopher: 'Hermann von Helmholtz', text: 'Helmholtz, the nineteenth century\'s greatest physiologist of perception, credited Berkeley as the first philosopher to see clearly that spatial perception is not an immediate deliverance of the senses but a construction. His own theory of unconscious inference — that the visual system arrives at its perception of distance by an inference process below the threshold of consciousness — is the physiological version of Berkeley\'s philosophical argument. Helmholtz wrote that Berkeley\'s analysis of visual distance perception anticipated the core of his own theory by more than a century. The Essay was widely read among nineteenth-century researchers in physiology and experimental psychology, and its influence on the development of perceptual psychology is comparable to that of the Principles on epistemology.' },
        { philosopher: 'J.J. Gibson', text: 'Gibson\'s ecological optics was developed in explicit opposition to what he called "Berkeley\'s theory of depth perception." Gibson argued that distance is not inferred from associated cues but is directly specified by the structure of the optic array. Berkeley had asked the right question and identified the right phenomenon — the gap between retinal image and perceived spatial layout — but his answer (learned association) was wrong. Gibson\'s answer (direct pick-up from ecological optics) is equally influential and equally controversial. Every subsequent theory of spatial perception has been defined by its relationship to both Berkeley and Gibson.' },
        { philosopher: 'Margaret Atherton', text: 'Atherton\'s Berkeley\'s Revolution in Vision (1990) argued that the New Theory of Vision is not merely a contribution to the psychology of perception — it is the philosophical laboratory in which Berkeley developed the arguments and conceptual tools that would produce immaterialism. The heterogeneity of sight and touch is the first step toward esse est percipi: if the objects of sight are mind-dependent ideas rather than properties of mind-independent things, and this is true of one sense modality, then the argument generalizes to all senses. Atherton showed that the Essay is philosophically richer than it appears — Berkeley is developing a new account of what it means to be an object of perception at all.' }
    ],
    modernRelevance: 'Berkeley\'s theory of vision has been a touchstone in the philosophy and psychology of perception for over three centuries. His claim that spatial perception is learned rather than innate was central to the nature-nurture debate and was apparently confirmed by cases of cataract patients given sight in adulthood (the Cheselden case of 1728). Contemporary research on infant spatial cognition suggests some aspects of spatial perception are innate, challenging Berkeley\'s pure associationism. In philosophy, the heterogeneity thesis has influenced discussions of cross-modal perception, synaesthesia, and the binding problem in consciousness research.',
    context: 'Berkeley composed the Essay while still a Fellow of Trinity College Dublin, between 1707 and 1709. It was his first published philosophical work and was immediately recognized as a major contribution to optics and perception even by those who would later reject his metaphysics. Voltaire praised it in his Letters on England. Berkeley himself later regarded it as an incomplete statement, arguing in the 1732 edition that the divine visual language thesis pointed toward the immaterialism of the Principles.',
    relatedWorks: ['principles-human-knowledge', 'three-dialogues', 'alciphron']
},

{
    id: 'de-motu',
    title: 'De Motu (On Motion)',
    greekTitle: 'De Motu, sive de Motus Principio & Natura et de Causa Communicationis Motuum',
    philosopher: 'berkeley',
    category: 'natural-philosophy',
    categoryLabel: 'Natural Philosophy',
    date: '1721 AD',
    dateSort: 1721,
    emoji: '⚛',
    cardSize: 'normal',
    readingDifficulty: 'Advanced',
    estimatedWordCount: 12000,
    shortDesc: 'Berkeley\'s most technically accomplished work — a systematic dismantling of Newtonian absolute space, absolute motion, and the metaphysics of force, anticipating Mach and the philosophical foundations of relativity by two centuries.',
    summary: 'De Motu, written in Latin and submitted for a prize competition at the Académie Royale des Sciences in Paris in 1720, is the most concentrated and technically sophisticated of Berkeley\'s philosophical works. Its arguments against absolute space, absolute motion, and the ontological status of Newtonian "force" anticipate Ernst Mach\'s critique of Newtonian mechanics by a century and a half, and through Mach they contributed to the conceptual revolution that produced Einstein\'s general theory of relativity.\n\nThe work addresses the foundations of mechanics and asks what the fundamental concepts of that science actually mean. Berkeley argues that the Newtonian concepts of absolute space, absolute time, and absolute motion are meaningless abstractions. Space is nothing but the system of relations among perceived bodies; motion is nothing but the change of those relations; and "absolute motion" — motion relative to absolute space itself — is a concept without content, because absolute space is unperceivable and therefore non-existent.\n\nBerkeley\'s critique of force is equally radical. Newton had treated force — gravity, in particular — as a real cause operating between bodies. Berkeley argues that "force" is not a perceived quality of bodies but a mathematical device introduced to simplify the description of regularities in motion. We never perceive force; we perceive only bodies and their motions. Forces are not causes but mathematical hypotheses — instruments of calculation, not descriptions of physical reality. This instrumentalist philosophy of science was centuries ahead of its time.',
    themes: ['Critique of Absolute Space', 'Critique of Absolute Motion', 'Instrumentalism about Force', 'Philosophy of Mechanics', 'The Nature of Scientific Explanation', 'Relationalism about Space and Time', 'God as the True Cause of Motion', 'Mathematics as Instrument'],
    keyCharacters: [],
    concepts: [
        'Absolute space is meaningless — space is only the system of perceived spatial relations among bodies; unperceivable absolute space is an empty abstraction',
        'Absolute motion is meaningless — all motion is relative to other perceived bodies',
        'Force as mathematical hypothesis — "force" is not a perceived reality but a calculating device for predicting regularities in motion; it names no power in nature',
        'Instrumentalism about science — scientific theories are instruments for organizing and predicting experience, not descriptions of unobservable mechanisms',
        'God as the only true efficient cause of motion — the regularities of nature are the expressions of divine will, not the effects of material forces',
        'The distinction between mathematical hypotheses and physical causes — mathematics describes patterns in experience; only minds can be genuine causes'
    ],
    structure: '§1–10: The aim of the treatise; the confusion between mathematical hypotheses and physical causes\n§11–23: Motion and its philosophical definition; the rejection of absolute motion\n§24–35: The nature of force; force as mathematical abstraction, not a real quality of bodies\n§36–53: Critique of Newtonian absolute space and time; the relational alternative\n§54–66: The true cause of motion; God as the only efficient cause; natural laws as divine rules\n§67–72: The proper role of mathematics in natural philosophy',
    quote: 'Force, gravity, attraction, and similar terms are useful for reasoning and for computations about motion and about bodies in motion; but they do not help us to understand the simple nature of motion itself, nor do they designate so many distinct qualities. They are, in truth, only mathematical hypotheses, and not real physical qualities.',
    additionalQuotes: [
        { text: 'It is not in fact the business of physics or mechanics to establish efficient causes, but only to establish the rules of impulse and attraction, and, in a word, the laws of motion; and from these established laws to assign the solution, not the efficient cause, of particular phenomena.', citation: 'De Motu §35' },
        { text: 'Absolute space, without relation to anything external, always remaining the same and immovable — no such thing can be conceived by any sense or imagination; it is therefore a purely abstract notion.', citation: 'De Motu §53' }
    ],
    commentary: [
        { philosopher: 'Ernst Mach', text: 'Mach\'s acknowledgement of Berkeley in The Science of Mechanics (1883) is one of the most consequential attributions in the history and philosophy of science. Mach wrote that Berkeley, in De Motu, had anticipated all the essential points of his own critique of Newtonian mechanics — the arguments against absolute space and absolute motion are identical in substance, formulated a hundred and sixty years earlier. Mach\'s Science of Mechanics became, in turn, one of the most important books Einstein read in his formative years: in his autobiographical notes, Einstein cited Mach\'s critique of Newtonian mechanics as a major influence on the conceptual innovations that led to special relativity. The chain from Berkeley through Mach to Einstein is now standard in the history and philosophy of physics.' },
        { philosopher: 'Karl Popper', text: 'Popper\'s "A Note on Berkeley as Precursor of Mach and Einstein" (1953) argued that Berkeley\'s instrumentalism about force — the thesis that forces are mathematical devices rather than physical realities — is one of the most defensible positions in the philosophy of physics, and that De Motu is the most remarkable anticipation in the history of the philosophy of science. He also argued that Berkeley\'s critique of absolute space in De Motu is philosophically tighter than Mach\'s own critique, because Berkeley grounds his relationalism in the general philosophical principle that unperceivable entities are meaningless, while Mach grounds his in the vaguer principle of economy of thought.' },
        { philosopher: 'Lisa Downing', text: 'Downing\'s "Berkeley\'s Case against Realism about Dynamics" (1995) showed that Berkeley\'s critique of force is philosophically more radical than Hume\'s later critique of causation — and precedes it by two decades. Berkeley does not merely question our epistemic access to causal powers; he argues that the very concept of material force is incoherent within the terms of any acceptable epistemology. Downing also showed that Berkeley\'s instrumentalism involves a sophisticated account of the relationship between mathematical theories and empirical data that anticipates the semantic and epistemic views of van Fraassen\'s constructive empiricism.' }
    ],
    modernRelevance: 'De Motu\'s influence on the development of modern physics is one of the most remarkable episodes in intellectual history. Berkeley\'s instrumentalism remains a major position in contemporary philosophy of science, defended in various forms by van Fraassen\'s constructive empiricism. His argument that "force" is a mathematical fiction rather than a physical cause has been compared to modern debates about the ontological status of fields, potentials, and gauge symmetries in quantum field theory.',
    context: 'Berkeley wrote De Motu in 1720 during his Continental travels (1716–1720), submitting it for a prize at the Académie Royale des Sciences. He did not win — the prize went to a Cartesian entry — but the essay was published in London in 1721. It applies the immaterialist principles of the Principles and Three Dialogues directly to the foundations of physical science.',
    relatedWorks: ['principles-human-knowledge', 'three-dialogues', 'siris', 'the-analyst']
}

);
"""

# ── 15d: Alciphron + The Analyst ─────────────────────────────────────────────
data_15d = r"""/* DATA PART 15d — Alciphron + The Analyst (Berkeley) */
window.WORKS.push(

{
    id: 'alciphron',
    title: 'Alciphron, or the Minute Philosopher',
    greekTitle: 'Alciphron, or the Minute Philosopher',
    philosopher: 'berkeley',
    category: 'practical',
    categoryLabel: 'Theology & Ethics',
    date: '1732 AD',
    dateSort: 1732,
    emoji: '🏛',
    cardSize: 'normal',
    readingDifficulty: 'Intermediate',
    estimatedWordCount: 100000,
    shortDesc: 'Berkeley\'s most ambitious dialogue — a seven-part philosophical drama defending Christian theism against the Enlightenment\'s "minute philosophers," containing the most important theory of meaning in the eighteenth century and a decisive anticipation of Wittgenstein\'s use-theory of language.',
    summary: 'Alciphron, or the Minute Philosopher, published in 1732 after Berkeley\'s return from his failed colonial venture in Rhode Island, is his longest and most wide-ranging philosophical work. Written in dialogue form and set in the countryside near Berkeley\'s American retreat, it is a comprehensive defence of Christian theism and traditional morality against the various forms of freethinking and deism that Berkeley grouped under the label "minute philosophy" — philosophy that diminishes the scope of human knowledge and the authority of religion.\n\nThe seven dialogues address distinct targets. The first two target Bernard Mandeville\'s thesis in The Fable of the Bees — that private vices produce public benefits and that commercial society thrives on selfishness. Berkeley counters with arguments for the social utility of genuine virtue. The third dialogue addresses Shaftesbury\'s moral sense theory and the deist claim that natural religion alone is sufficient for morality.\n\nThe most philosophically significant dialogue is the fourth, substantially revised and expanded in the 1752 edition. Here Berkeley develops his theory of meaning — that the meaning of a word is not an abstract idea it stands for but the use to which it is put in discourse. This theory, applied to religious language, allows Berkeley to argue that talk of God, the Trinity, and grace is perfectly meaningful even though we have no sensory "idea" corresponding to these terms. The meaning of a word like "grace" is given by its role in directing conduct, inspiring attitudes, and regulating inquiry — not by any mental image it calls up. This anticipation of the later Wittgenstein\'s use-theory of meaning is one of Berkeley\'s most remarkable philosophical contributions.\n\nThe remaining dialogues address the existence of God (through the argument from the divine visual language), the immortality of the soul, and the relationship between faith and reason.',
    themes: ['Critique of Freethinking', 'Defence of Christianity', 'Philosophy of Language', 'Use-Theory of Meaning', 'The Divine Visual Language', 'Moral Philosophy', 'The Existence of God', 'Critique of Mandeville', 'Critique of Shaftesbury', 'Faith and Reason'],
    keyCharacters: [
        { name: 'Alciphron', role: 'The free-thinking "minute philosopher" — eloquent, urbane, and intellectually formidable; he defends the positions of Mandeville, Shaftesbury, and Collins with vigour' },
        { name: 'Lysicles', role: 'Alciphron\'s companion — a cruder freethinker representing the Mandevillean position that morality is a sham and self-interest the only real motive' },
        { name: 'Euphranor', role: 'Berkeley\'s principal spokesman — a thoughtful Christian gentleman who defends theism and traditional morality with patience and philosophical acumen' },
        { name: 'Crito', role: 'Euphranor\'s older companion — a man of practical wisdom who supports the case for Christianity with arguments from history and common sense' }
    ],
    concepts: [
        'Minute philosophy — Berkeley\'s term for the reductive and skeptical philosophies of the Enlightenment that diminish religion, morality, and human dignity',
        'Use-theory of meaning — the meaning of a word is determined by its use in discourse, not by a corresponding mental image or abstract idea',
        'The divine visual language — the regularities of nature constitute a language through which God communicates with finite minds; as human language reveals a human speaker, nature reveals a divine speaker',
        'Emotive and directive meaning — religious language functions by directing conduct and inspiring attitudes, not merely by representing ideas',
        'Moral realism defended — genuine virtues produce genuine social goods; Mandeville\'s cynicism is not just morally wrong but empirically false',
        'The insufficiency of natural religion — morality requires the sanctions of revealed religion; without divine commands, moral obligation loses its binding force'
    ],
    structure: 'Dialogue I: Against Mandeville — private vices do not produce public benefits\nDialogue II: Against Mandeville continued — the social destruction wrought by luxury and cynicism\nDialogue III: Against Shaftesbury and the deists — natural religion alone cannot sustain morality\nDialogue IV: The philosophy of language — meaning as use; the meaningfulness of religious discourse\nDialogue V: The existence of God — the argument from the divine visual language\nDialogue VI: The nature of the soul and its immortality\nDialogue VII: Faith and reason; the vindication of Christianity',
    quote: 'We ought to think with the learned and speak with the vulgar. But it is the characteristic of the minute philosopher to think with the vulgar and speak with the learned — to take common prejudices for principles, and then to dress them up in the garb of philosophy.',
    additionalQuotes: [
        { text: 'The great Mover and Author of Nature constantly explaineth himself to the eyes of men by the sensible intervention of arbitrary signs, which have no similitude or connection with the things signified — so as, by compounding and disposing them, to suggest and exhibit an endless variety of objects.', citation: 'Alciphron, Dialogue IV §12' },
        { text: 'A word may be significant, although it does not, every time it is used, excite the idea it signifies in our minds, provided it be made to do so when there is occasion.', citation: 'Alciphron, Dialogue VII §8' }
    ],
    commentary: [
        { philosopher: 'Ludwig Wittgenstein', text: 'Wittgenstein\'s reported acknowledgement of Berkeley\'s anticipation of use-theory — conveyed through G.E.M. Anscombe and other members of his circle who studied Alciphron carefully — is one of the most significant attributions in twentieth-century philosophy of language. The fourth dialogue\'s central claim that a word can be significant without calling up a corresponding idea whenever it is used — that its significance consists in the role it plays in guiding action, shaping attitudes, and regulating practice — is precisely the insight that Wittgenstein\'s Philosophical Investigations develops at length and in systematic detail. Whether Wittgenstein read Berkeley is disputed; what is not disputed is that the philosophical position of Alciphron IV anticipates the use-theory of meaning by over two centuries.' },
        { philosopher: 'Ian Tipton', text: 'Tipton\'s Berkeley: The Philosophy of Immaterialism (1974) argued that Alciphron\'s fourth dialogue contains a philosophy of language more sophisticated than anything produced in the eighteenth century — one that dissolves the problem of religious language that preoccupied logical positivism, by showing that the positivist criterion of meaning (empirical verifiability) is itself too narrow. Berkeley\'s point is not that theological sentences are meaningless because they fail to picture empirical facts, but that "meaning" is not fundamentally a matter of picturing at all. A sentence has meaning when it does something in the practice of a language-using community. Religious language does these things; its meaningfulness does not depend on its correspondence to verifiable states of affairs.' },
        { philosopher: 'Stephen Daniel', text: 'Daniel argued that Berkeley\'s theory of meaning in the fourth dialogue is not merely an anticipation of later developments but an integral part of his immaterialism. If meaning is use rather than mental imagery, then the entire Lockean picture of language as a system of labels for ideas collapses — and with it the framework that generated the problem of material substance in the first place. The Lockean model assumed that words get their meaning by standing for ideas, and that if there is no idea, the word is meaningless. Berkeley had shown, in the Principles, that the word "matter" names no idea; Alciphron IV completes the argument by showing that this is not sufficient to make it meaningless.' }
    ],
    modernRelevance: 'Alciphron\'s fourth dialogue is now recognized as one of the most important texts in the history of the philosophy of language. Berkeley\'s use-theory of meaning directly anticipates the later Wittgenstein\'s arguments against private language and in favour of meaning-as-use. In philosophy of religion, Berkeley\'s argument that religious language is meaningful because it directs conduct and shapes attitudes rather than pictures metaphysical facts has been compared to the non-cognitivist and expressivist approaches of Braithwaite, Phillips, and others.',
    context: 'Berkeley wrote Alciphron during his three years in Rhode Island (1728–1731), where he had gone with the intention of founding a college for the education of both colonists and Indigenous Americans. The project failed when the promised government funding from Robert Walpole never materialized. The work was immediately controversial — Mandeville published a furious response — and established Berkeley as a major voice in the public debate about religion and the Enlightenment. The fourth dialogue was substantially revised for the second edition of 1752.',
    relatedWorks: ['principles-human-knowledge', 'three-dialogues', 'essay-towards-new-theory-vision', 'siris']
},

{
    id: 'the-analyst',
    title: 'The Analyst',
    greekTitle: 'The Analyst; or, A Discourse Addressed to an Infidel Mathematician',
    philosopher: 'berkeley',
    category: 'natural-philosophy',
    categoryLabel: 'Philosophy of Mathematics',
    date: '1734 AD',
    dateSort: 1734,
    emoji: '∫',
    cardSize: 'normal',
    readingDifficulty: 'Advanced',
    estimatedWordCount: 20000,
    shortDesc: 'The most devastating critique of the foundations of calculus ever written — Berkeley exposes the logical incoherence at the heart of Newton\'s and Leibniz\'s infinitesimal methods, provoking a foundational crisis in mathematics that would take a century to resolve.',
    summary: 'The Analyst, published in 1734 and subtitled "A Discourse Addressed to an Infidel Mathematician" (traditionally identified as the astronomer Edmond Halley), is Berkeley\'s most technically brilliant work and one of the most consequential interventions in the history of mathematics. Its thesis is explosive: that the calculus of Newton and Leibniz, the most powerful mathematical tool of the age, rests on logical foundations that are incoherent — and that mathematicians who reject religious mysteries on the grounds of logical rigour are therefore guilty of a double standard, accepting in their own discipline "mysteries" far more opaque than any article of the Christian faith.\n\nBerkeley\'s critique targets the concept of the infinitesimal. In the calculus as practiced in the early eighteenth century, one proceeds by treating a quantity as non-zero (in order to divide by it), then treating the same quantity as zero (in order to eliminate unwanted terms from the result). Berkeley identifies this as a blatant logical contradiction: the infinitesimal is simultaneously something and nothing. His most famous formulation — that infinitesimals are "the ghosts of departed quantities" — crystallizes the objection in one of the most memorable phrases in the history of mathematics.\n\nThe argument is not merely negative. Berkeley does not deny that the calculus produces correct results. His point is that its correctness cannot be explained by its stated logical foundations, which are contradictory. The right answers are obtained, he suggests, by a "compensation of errors": two mistakes cancel each other out, producing a correct result by accident rather than by valid reasoning.\n\nBerkeley\'s critique provoked an enormous response — over thirty published replies appeared within a decade. None succeeded in answering his objection within the mathematical framework of the time. The problem he identified was not resolved until Cauchy, Weierstrass, and Dedekind in the nineteenth century replaced infinitesimals with the modern epsilon-delta definition of the limit.',
    themes: ['Foundations of Calculus', 'The Infinitesimal', 'Logical Rigour in Mathematics', 'The Double Standard of Mathematicians', 'Faith and Reason', 'The Compensation of Errors', 'The Ghost of Departed Quantities'],
    keyCharacters: [
        { name: 'The Infidel Mathematician', role: 'Traditionally identified as Edmond Halley — whose alleged advice that Christian doctrines were too obscure to accept prompted Berkeley\'s demonstration that the foundations of calculus were logically far more obscure than any article of faith' }
    ],
    concepts: [
        'Infinitesimals as "ghosts of departed quantities" — Berkeley\'s devastating characterization: infinitesimals are called upon when needed and dismissed as zero when convenient',
        'The double standard — mathematicians who reject theological mysteries on grounds of logical rigour accept the infinitesimal, which is self-contradictory',
        'Compensation of errors — the calculus obtains correct results not because its foundations are sound but because two errors cancel each other',
        'The logical contradiction at the heart of differentiation — treating a quantity as non-zero to divide by it, then as zero to eliminate it, in the same proof',
        'Mathematical instrumentalism — mathematical methods can be useful without being logically well-founded; correctness of results does not guarantee validity of reasoning'
    ],
    structure: '§1–8: The occasion and purpose; the infidel mathematician\'s double standard\n§9–20: The method of fluxions; the logical procedure of differentiation analysed\n§21–35: The fundamental objection — infinitesimals are simultaneously something and nothing; the ghosts of departed quantities\n§36–44: The compensation of errors; how correct results emerge from faulty reasoning\n§45–50: Comparison of mathematical and theological mysteries\nQueries 1–67: A devastating series of rhetorical questions pressing the foundational objection from every angle',
    quote: 'And what are these fluxions? The velocities of evanescent increments. And what are these same evanescent increments? They are neither finite quantities, nor quantities infinitely small, nor yet nothing. May we not call them the ghosts of departed quantities?',
    additionalQuotes: [
        { text: 'He who can digest a second or third fluxion, a second or third difference, need not, methinks, be squeamish about any point in divinity.', citation: 'The Analyst §7' },
        { text: 'I say that in every other science men prove their conclusions by their principles, and not their principles by their conclusions.', citation: 'The Analyst §20' }
    ],
    commentary: [
        { philosopher: 'Bertrand Russell', text: 'Russell\'s verdict in The Principles of Mathematics (1903) was unequivocal: "Berkeley\'s criticism of the infinitesimal calculus was entirely justified. The logical foundations of the calculus were not made rigorous until the nineteenth century, and it was Berkeley who first stated the problem with full clarity." Russell knew the mathematics: the epsilon-delta foundations developed by Cauchy and Weierstrass, which eliminated infinitesimals entirely in favour of limits defined purely in terms of finite quantities, were precisely the kind of rigorous grounding that Berkeley had demanded. The irony Russell appreciated was that Berkeley\'s theological motivation — to show that mathematicians were no more rigorous than theologians — produced one of the most important contributions to the foundations of mathematics in the history of the discipline.' },
        { philosopher: 'Abraham Robinson', text: 'Robinson\'s development of non-standard analysis in the 1960s added a remarkable coda to the story of The Analyst. Robinson showed that infinitesimals could be made rigorous after all — but only by embedding them within a model of the real numbers constructed using the ultrafilter theorem, a piece of mathematical logic that did not exist until the twentieth century. Berkeley was right that the infinitesimal as used by Newton and Leibniz was logically incoherent — but the idea of the infinitesimal was not intrinsically incoherent. Berkeley had identified a genuine problem; Robinson\'s solution vindicated the infinitesimal by means Berkeley could not have anticipated. The Analyst thus occupies a unique place in intellectual history: it correctly identified a problem whose solution required two centuries.' },
        { philosopher: 'Douglas Jesseph', text: 'Jesseph\'s Berkeley\'s Philosophy of Mathematics (1993) showed that Berkeley\'s critique is philosophically more sophisticated than a simple charge of inconsistency. Berkeley understood that the calculus produced correct results and he was not trying to show it was useless; he was trying to show that its correctness was not explained by its stated foundations. This is a distinction between being right and being justified in believing one is right — between truth and knowledge — that is central to contemporary epistemology. Jesseph also showed that Berkeley\'s "compensation of errors" argument is technically correct for the specific examples he analysed: the two errors he identifies do indeed cancel to produce the correct result.' }
    ],
    modernRelevance: 'The Analyst\'s influence on the development of mathematics is beyond dispute. Berkeley\'s identification of the logical incoherence of infinitesimals drove the programme of rigorization that culminated in the epsilon-delta foundations of Cauchy, Weierstrass, and Dedekind — one of the great achievements in the history of mathematics. In philosophy of mathematics, the Analyst raises questions about the relationship between mathematical practice and foundations that remain central: mathematicians routinely use techniques whose foundations are incomplete, and the question of whether correct results obtained by dubious methods require rigorous foundations is still debated.',
    context: 'Berkeley wrote The Analyst in 1734, the year he became Bishop of Cloyne. The work provoked a furious response: James Jurin published a rebuttal, and Berkeley replied with A Defence of Free-Thinking in Mathematics (1735). The controversy continued for decades and was one of the factors that drove the eventual rigorization of mathematical analysis in the nineteenth century.',
    relatedWorks: ['principles-human-knowledge', 'de-motu', 'alciphron']
}

);
"""

# ── 15e: Siris + Philosophical Commentaries + Passive Obedience ──────────────
data_15e = r"""/* DATA PART 15e — Siris + Philosophical Commentaries + Passive Obedience (Berkeley) */
window.WORKS.push(

{
    id: 'siris',
    title: 'Siris: A Chain of Philosophical Reflexions and Inquiries',
    greekTitle: 'Siris: A Chain of Philosophical Reflexions and Inquiries Concerning the Virtues of Tar-Water',
    philosopher: 'berkeley',
    category: 'metaphysics',
    categoryLabel: 'Metaphysics & Natural Philosophy',
    date: '1744 AD',
    dateSort: 1744,
    emoji: '🔗',
    cardSize: 'normal',
    readingDifficulty: 'Advanced',
    estimatedWordCount: 65000,
    shortDesc: 'Berkeley\'s strangest and most visionary work — beginning with the medicinal virtues of tar-water and ascending, link by link, through chemistry, physics, ancient philosophy, and Neoplatonic theology to a mystical vision of the universe as a chain of being emanating from divine light.',
    summary: 'Siris, published in 1744 when Berkeley was fifty-nine and Bishop of Cloyne, is the most extraordinary and least classifiable work in his canon — a book that begins with the medicinal properties of tar-water (a preparation of pine resin infused in cold water) and ends with a Neoplatonic meditation on the nature of God, light, and the structure of reality. The title, from the Greek seira (chain), announces its method: the work proceeds by a chain of associations and philosophical reflections, each link connecting the previous topic to the next, ascending from the empirical to the metaphysical.\n\nThe opening sections are practical and medical. Berkeley had become convinced that tar-water was a near-universal remedy. He presents the evidence with empirical seriousness and considerable chemical detail. From the chemistry of tar-water he moves to the nature of fire, light, and the "aether" — the subtle medium that Berkeley, following Newton\'s speculations in the Queries to the Opticks, identifies as the agent of heat, combustion, and vital processes throughout nature.\n\nThis investigation of aether leads Berkeley into a sustained engagement with ancient natural philosophy — the fire of Heraclitus, the active principle (pneuma) of the Stoics, the world-soul of Plato\'s Timaeus, and the emanationist cosmology of Plotinus and the Neoplatonists. Berkeley argues that the ancients had grasped fundamental truths about the active principle in nature that modern mechanical philosophy had obscured.\n\nThe final sections are Berkeley\'s most explicitly theological and mystical. He ascends from the active principle in nature to the Platonic Forms, from the Forms to the divine intellect in which they subsist, and from the divine intellect to God as the ultimate source of all being and light. The work ends with a meditation on the Trinity — the One, the Logos, and the World-Soul — that draws on Plato, Plotinus, and the Christian Fathers to present a vision of reality as a continuous emanation from divine light.',
    themes: ['Tar-Water and Medicine', 'Aether and the Active Principle', 'Ancient Philosophy Rediscovered', 'Neoplatonic Emanation', 'The Chain of Being', 'Fire and Light as Cosmic Principles', 'Plato and the Forms', 'The Trinity', 'The Unity of Ancient and Modern Philosophy'],
    keyCharacters: [],
    concepts: [
        'Siris (seira) — chain: the method of ascending from particular observations to universal principles by a continuous chain of philosophical reflection',
        'Aether — the subtle, active medium Berkeley identifies with fire, light, and the animating principle of nature',
        'The active principle — the force that animates matter, identified with the Stoic pneuma, the Platonic world-soul, and the Neoplatonic emanation from the One',
        'Emanation — reality as a continuous outflowing from the divine source, descending from God through intellect and soul to the material world',
        'The ancient wisdom — Berkeley\'s claim that Platonic and Neoplatonic philosophers grasped truths about nature\'s active principle that mechanical philosophy has lost',
        'Light as fundamental cosmic principle — both physical illumination and metaphor for divine intelligibility'
    ],
    structure: '§1–68: Tar-water: its preparation, medicinal virtues, and chemical properties\n§69–136: Fire, aether, and the active principle in nature\n§137–213: The aether in ancient philosophy — Heraclitus, the Stoics, Plato\'s Timaeus\n§214–270: Plato\'s Forms, the divine intellect, and the Neoplatonic hierarchy of being\n§271–305: The Trinity — the One, the Logos, and the World-Soul\n§306–368: The unity of ancient and Christian wisdom; final reflections on God, light, and being',
    quote: 'The order and course of things, and the experiments we daily make, show there is a Mind that governs and actuates this mundane system, as the proper real agent and cause — and that the inferior instrumental cause is pure aether, fire, or the substance of light.',
    additionalQuotes: [
        { text: 'The phenomena of nature, which strike on the senses and are understood by the mind, form not only a magnificent spectacle but also a most coherent, entertaining, and instructive discourse — and to effect this is really the immediate doing of a most wise and good Agent.', citation: 'Siris §254' },
        { text: 'Plato and Aristotle considered God as abstracted or distinct from the natural world. But the Aegyptians and the earliest philosophers considered God as diffused throughout all things.', citation: 'Siris §290' }
    ],
    commentary: [
        { philosopher: 'A.A. Luce', text: 'Luce\'s assessment of Siris divided the scholarly world and continues to do so. For Luce, Siris is not a senile aberration — it is the crown of Berkeley\'s philosophy, the work in which his immaterialism, his theory of the divine visual language, and his theology achieve their most complete and beautiful expression. The chain that ascends from tar-water to God is the same chain that Berkeley had been tracing since the New Theory of Vision: the chain of signs through which the divine mind communicates with finite minds. What changes in Siris is the philosophical vocabulary — the empiricism of the early works is fused with the Platonic and Neoplatonic tradition Berkeley had been studying throughout his career.' },
        { philosopher: 'Samuel Taylor Coleridge', text: 'Coleridge\'s enthusiasm for Siris was characteristic of the Romantic appropriation of Berkeley as a philosopher of spirit against mechanism. He wrote that Siris is "one of those books that are at once the most instructive and the least read" and compared Berkeley\'s chain of ascent from humble empirical fact to highest metaphysical truth to Plato himself. Coleridge saw in Siris the reunion of natural science with spiritual vision that he regarded as the defining task of post-Kantian philosophy — the reenchantment of nature that mechanical philosophy had disenchanted.' },
        { philosopher: 'Colin Murray Turbayne', text: 'Turbayne argued that Siris is not a departure from Berkeley\'s earlier philosophy but its fulfilment. The chain that ascends from tar-water to God is the chain of signs — the divine language of nature — that Berkeley had been tracing since the New Theory of Vision. The Neoplatonic vocabulary of Siris is Berkeley\'s attempt to find in the ancient tradition a philosophical framework adequate to express what his immaterialism implies about the nature of God and the world. The visible world is a language; Siris is the most complete account of the grammar of that language and of the speaker who uses it.' }
    ],
    modernRelevance: 'Siris is the Berkeley text that has most interested scholars of the history of ideas and the relationship between science and mysticism. Its engagement with Neoplatonism has been studied in connection with the revival of interest in process philosophy and panentheism. Its method of philosophical ascent — beginning with a humble empirical observation and tracing its implications upward through chemistry, physics, ancient philosophy, and theology — has been compared to the phenomenological method of Husserl and the integrative metaphysics of Whitehead.',
    context: 'Berkeley wrote Siris during his years as Bishop of Cloyne (1734–1752), deeply engaged with the practical problems of rural Irish life — famine, disease, economic deprivation. His promotion of tar-water was a genuine attempt to find an affordable remedy for the diseases afflicting his parishioners. The work went through six editions in its first year. Berkeley spent his final years at Oxford, where he died on 14 January 1753 while listening to his wife read from the Bible. He is buried in Christ Church Cathedral.',
    relatedWorks: ['principles-human-knowledge', 'three-dialogues', 'de-motu', 'alciphron']
},

{
    id: 'philosophical-commentaries',
    title: 'Philosophical Commentaries',
    greekTitle: 'Philosophical Commentaries (Notebooks A and B)',
    philosopher: 'berkeley',
    category: 'method',
    categoryLabel: 'Philosophical Notebooks',
    date: 'c.1707–1708 AD',
    dateSort: 1707,
    emoji: '📓',
    cardSize: 'normal',
    readingDifficulty: 'Advanced',
    estimatedWordCount: 40000,
    shortDesc: 'The private laboratory of immaterialism — two notebooks in which the twenty-two-year-old Berkeley worked out, in raw and uncensored form, the arguments that would become the Principles and the Three Dialogues, complete with false starts, self-corrections, and moments of sudden illumination.',
    summary: 'The Philosophical Commentaries — two notebooks kept by Berkeley between approximately 1707 and 1708, when he was a Fellow of Trinity College Dublin aged twenty-two — are among the most fascinating documents in the history of philosophy. They were not intended for publication; Berkeley used them as a private intellectual workshop in which he developed, tested, revised, and sometimes abandoned the arguments that would become the Principles of Human Knowledge (1710) and the Three Dialogues (1713).\n\nThe notebooks contain approximately 900 numbered entries, ranging from single sentences to extended arguments, organized by a system of marginal signs: "M" for matter, "S" for spirit, "G" for God, "E" for existence (esse est percipi), "Mo" for moral philosophy, and others. This system allows the reader to trace the development of each major doctrine — to watch Berkeley working his way toward immaterialism, encountering objections, trying different formulations, and gradually building the system that would emerge in finished form.\n\nThe entries reveal a mind of extraordinary energy and daring. Berkeley arrives at the esse est percipi thesis early and then subjects it to relentless self-interrogation. The notebooks also contain positions that Berkeley later suppressed — arguments he found compelling but decided were too dangerous to publish. He considers and abandons the view that minds might be nothing but bundles of ideas (a position Hume would later adopt); he experiments with the idea that God might be identical with the physical world (a Spinozist position he ultimately rejects). These raw, uncensored reflections give the Philosophical Commentaries a philosophical and human interest that no published work can match.',
    themes: ['The Genesis of Immaterialism', 'Esse Est Percipi in Formation', 'Critique of Abstract Ideas', 'The Nature of Mind and Spirit', 'The Continuity Problem', 'Philosophy as Private Inquiry', 'Self-Correction and Intellectual Honesty', 'Abandoned Positions'],
    keyCharacters: [],
    concepts: [
        'The marginal sign system — Berkeley\'s method of classifying entries by topic (M, S, G, E, I, Mo) to track the development of each doctrine across both notebooks',
        'Esse est percipi in its earliest formulation — the thesis tested against every objection Berkeley can devise',
        'The continuity objection — if things exist only when perceived, what happens when no one is looking? Berkeley\'s earliest attempts to solve this through God\'s constant perception',
        'Mind as active vs ideas as passive — the structural architecture of the entire system, worked out here for the first time',
        'Abandoned positions — the proto-bundle theory and proto-Spinozism Berkeley tried and rejected; visible only in the notebooks'
    ],
    structure: 'Notebook B (probably earlier): Entries 1–399 approximately\n— Early formulations of immaterialism; the esse est percipi thesis in its first forms\n— Engagement with Locke, Descartes, Malebranche, and Newton\n\nNotebook A (probably later): Entries 400–888 approximately\n— The doctrine refined; the role of God clarified\n— The divine visual language; the nature of spirit; personal identity\n— Entries marked with "+" indicating material intended for publication',
    quote: 'Existence is percipi, or percipere, or velle i.e. agere. The horse is in the stable, the books are in the study as before — nothing is changed.',
    additionalQuotes: [
        { text: 'I must not say the things I see are representations of things I do not see. I must say the things I see are the things themselves.', citation: 'Philosophical Commentaries, entry 470' },
        { text: 'Query: whether there can be any motion other than relative? I think not. All motion is relative.', citation: 'Philosophical Commentaries, entry 271' }
    ],
    commentary: [
        { philosopher: 'A.A. Luce', text: 'Luce\'s critical edition of the Philosophical Commentaries (1944) — which established the now-standard title and provided the first rigorous analysis of the marginal signs and the probable order of composition — transformed Berkeley scholarship by making the notebooks accessible as a philosophical document rather than merely a biographical curiosity. Luce compared the Commentaries to Wittgenstein\'s notebooks: the private record of a philosopher thinking his way into his own system, with a candour and energy that the published works necessarily conceal. Luce also showed, through careful analysis of the marginal signs, that Berkeley had a much clearer plan for the overall structure of his philosophy from an early stage than the informal character of the notebook entries suggests.' },
        { philosopher: 'Kenneth Winkler', text: 'Winkler\'s Berkeley: An Interpretation (1989) drew extensively on the Commentaries to reconstruct the philosophical arguments of the Principles with a precision impossible without access to the notebooks. Winkler showed that Berkeley considered and rejected positions that other philosophers later adopted independently — including the bundle theory of the self (which Hume developed in the Treatise) and a quasi-Spinozistic identification of God with Nature. His reasons for rejecting these positions are among the most philosophically interesting entries in the notebooks: the bundle theory fails because it cannot account for the activity and unity of the perceiving self; the Spinozistic position fails because it makes God the perceiver of all possible ideas, including evil or contradictory ones — inconsistent with divine perfection.' }
    ],
    modernRelevance: 'The Philosophical Commentaries raise broader questions about the nature of philosophical inquiry. They demonstrate that philosophical systems are built through a process of trial, error, and self-criticism that published works typically conceal. The abandoned positions they contain — particularly the proto-bundle theory — have generated a substantial secondary literature exploring the roads Berkeley did not take and the philosophical reasons he turned away from them.',
    context: 'Berkeley kept the two notebooks while a Fellow of Trinity College Dublin, between approximately 1707 and 1708. The notebooks were written in pencil, with many entries crossed out or annotated. They were not published until 1871, when Alexander Campbell Fraser included them under the misleading title "Commonplace Book of Occasional Metaphysical Thoughts." Luce\'s critical edition of 1944 established the standard title and transformed them from biographical curiosity to philosophical document.',
    relatedWorks: ['principles-human-knowledge', 'three-dialogues', 'essay-towards-new-theory-vision']
},

{
    id: 'passive-obedience',
    title: 'A Discourse on Passive Obedience',
    greekTitle: 'Passive Obedience, or the Christian Doctrine of Not Resisting the Supreme Power',
    philosopher: 'berkeley',
    category: 'practical',
    categoryLabel: 'Political & Moral Philosophy',
    date: '1712 AD',
    dateSort: 1712,
    emoji: '⚖',
    cardSize: 'normal',
    readingDifficulty: 'Intermediate',
    estimatedWordCount: 15000,
    shortDesc: 'Berkeley\'s most systematic work of moral and political philosophy — a rigorous argument for absolute moral rules and the obligation of obedience to established authority, founding rule-consequentialism in the history of ethics and anticipating two centuries of debate between rule and act utilitarianism.',
    summary: 'Passive Obedience, originally delivered as three sermons in the chapel of Trinity College Dublin in 1712 and published the same year, is Berkeley\'s most sustained contribution to moral and political philosophy and one of the most carefully argued works of ethical theory in the early eighteenth century. Its immediate occasion was the political crisis surrounding the Hanoverian succession, but its philosophical ambition far exceeds its political context.\n\nThe central argument proceeds in three stages. First, Berkeley establishes that morality must be grounded in absolute, universal rules that hold without exception. He attacks the view that the rightness of an action is determined solely by its consequences. If every moral agent were permitted to calculate the consequences of each act and follow whatever course promised the best outcome, moral life would dissolve into chaos. Stable social life requires fixed, exceptionless moral rules — rules that every agent must follow regardless of apparent consequences in particular cases.\n\nSecond, Berkeley argues that these absolute moral rules are promulgated by God and discoverable by human reason. God wills the general happiness of mankind, and the moral rules he establishes are the means to that general happiness — but they function as absolute commands, not provisional guidelines. This is a form of rule-consequentialism: the rules are justified by their tendency to promote the general good over the long run, but once established they are binding without exception.\n\nThird, Berkeley applies this framework to political obedience. Even when a ruler acts unjustly, subjects are bound not to resist by force; their remedy is remonstrance, prayer, and in extreme cases flight — but never violent revolution. Berkeley acknowledges that this seems to license tyranny, and he addresses the objection with philosophical honesty: the long-run consequences of permitting armed resistance are invariably worse than enduring even unjust rule.',
    themes: ['Foundations of Morality', 'Absolute Moral Rules', 'Rule-Consequentialism', 'Passive Obedience to Authority', 'Natural Law', 'God\'s Will as the Ground of Obligation', 'The Limits of Private Judgment', 'Political Obligation', 'Critique of Act-Consequentialism'],
    keyCharacters: [],
    concepts: [
        'Absolute moral rules — moral commands that hold without exception and may not be set aside by individual calculation of consequences',
        'Rule-consequentialism — the moral rules are justified by their tendency to promote the general good, but individual acts are judged by conformity to the rule, not by their particular consequences',
        'The will of God as the source of moral obligation — morality is grounded in divine legislation discoverable by human reason',
        'The general happiness as the end of morality — God wills the good of all mankind, and the moral law is the means to that end',
        'Passive obedience — the absolute duty not to resist the supreme civil power by force, even when it acts unjustly',
        'The critique of private judgment in politics — no individual is competent to calculate whether revolution will produce better consequences than submission'
    ],
    structure: 'Sermon I: The foundations of morality\n— The necessity of absolute moral rules; the dangers of consequentialist calculation\n— God\'s will as the ground of obligation; the general happiness as the end of moral law\n\nSermon II: The content of the moral law\n— The natural law of non-resistance; passive obedience as an absolute moral rule\n\nSermon III: Objections and replies\n— Does passive obedience license tyranny?\n— The long-run benefits of obedience vs the catastrophic risks of revolution',
    quote: 'Moral rules are not to be assessed each time by the benefit likely to accrue in a given case, but by the general tendency they have over the long run of human affairs. A rule that permits exceptions will soon have no authority at all.',
    additionalQuotes: [
        { text: 'The doctrine of non-resistance does not oblige us to give active obedience to every command of the prince — it obliges us only not to resist his power by force. We may remonstrate, we may petition, we may even flee; but we may not take up arms.', citation: 'Passive Obedience §30' },
        { text: 'Those who make private utility the measure of all virtue are in fact undermining the very foundation of morality, and substituting for it a shifting sand of individual calculation.', citation: 'Passive Obedience §12' }
    ],
    commentary: [
        { philosopher: 'John Stuart Mill', text: 'Mill\'s engagement with Passive Obedience acknowledged Berkeley\'s argument as one of the most important precursors of rule-utilitarian thinking in the history of moral philosophy. The distinction Berkeley draws between the justification of a rule by its general consequences and the application of a rule without regard to particular consequences is precisely the distinction that defines rule-utilitarianism as a position distinct from act-utilitarianism. Mill recognized that Berkeley\'s argument for absolute rules grounded in their general tendency is the strongest available response to the problem of moral instability that plagues act-consequentialism: the charge that act-consequentialism licenses murder, theft, and revolution whenever an individual agent calculates that such acts produce the best outcome.' },
        { philosopher: 'Stephen Darwall', text: 'Darwall\'s The British Moralists and the Internal "Ought" (1995) placed Passive Obedience in its proper context in the history of ethical theory. Berkeley\'s argument, Darwall showed, is a contribution to the fundamental question of what grounds moral obligation. Berkeley\'s answer — that obligation requires God\'s authoritative will communicated to rational creatures — is a version of divine command theory, but one refined by the insight that God\'s commands are not arbitrary: they are selected because they tend to promote the general happiness. This combination of divine command theory with consequentialist justification of the commands is philosophically original and more defensible than either pure divine command theory or pure consequentialism. Darwall identified it as one of the most important metaethical positions of the early modern period.' }
    ],
    modernRelevance: 'Passive Obedience is now recognized as a foundational text in the development of rule-consequentialism — the ethical theory that moral rules should be justified by their overall consequences but applied without exception. His critique of private moral judgment — that individuals cannot be trusted to calculate consequences correctly — resonates with contemporary discussions of cognitive bias, bounded rationality, and the case for moral heuristics. His political doctrine has been discussed in connection with theories of civil disobedience from Thoreau through Martin Luther King Jr.',
    context: 'Berkeley delivered the three sermons in the chapel of Trinity College Dublin in 1712, during a period of intense political controversy surrounding the Hanoverian succession and the Jacobite threat. He was twenty-seven and a Junior Fellow of Trinity. The sermons were published at the urging of friends and were immediately controversial — Berkeley was accused of Jacobite sympathies, a charge he denied vigorously and modern scholars have largely rejected.',
    relatedWorks: ['principles-human-knowledge', 'alciphron', 'three-dialogues']
}

);
"""

files = {
    'data-15a.js': data_15a,
    'data-15b.js': data_15b,
    'data-15c.js': data_15c,
    'data-15d.js': data_15d,
    'data-15e.js': data_15e,
}

for filename, content in files.items():
    path = os.path.join(js_dir, filename)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    lines = content.count('\n')
    print(f'  Written {filename}  —  {lines} lines  →  {path}')

print('\nAll Berkeley files complete. Verify with:')
print('  wc -l js/data-15a.js js/data-15b.js js/data-15c.js js/data-15d.js js/data-15e.js')
