#!/usr/bin/env python3
"""
Hume — data-22a through data-22e (10 works, 5 parts)
Run from ~/Desktop/philosophy-archive/: python3 generate_hume.py
"""
import os
js = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'js')
os.makedirs(js, exist_ok=True)

files = {}

# ── data-22a: Treatise of Human Nature ──────────────────────────────────────
files['data-22a.js'] = r"""/* DATA PART 22a — Hume: Treatise of Human Nature */
window.WORKS.push(
{
    id: 'treatise-human-nature',
    title: 'A Treatise of Human Nature',
    greekTitle: 'Being an Attempt to Introduce the Experimental Method of Reasoning into Moral Subjects',
    philosopher: 'hume',
    category: 'metaphysics',
    categoryLabel: 'Epistemology & Metaphysics',
    date: '1739\u201340 AD',
    dateSort: 1739,
    emoji: '\uD83D\uDCD6',
    cardSize: 'wide',
    readingDifficulty: 'Advanced',
    estimatedWordCount: 290000,
    shortDesc: 'The founding document of British Empiricism at its most radical \u2014 Hume\u2019s attempt to apply the experimental method of Newton to human nature, yielding the bundle theory of the self, the impossibility of induction, and the derivation of morality from sentiment rather than reason.',
    summary: 'A Treatise of Human Nature: Being an Attempt to Introduce the Experimental Method of Reasoning into Moral Subjects, published anonymously in three books (Books I and II in January 1739, Book III in November 1740) by John Noone in London, is the most systematic and most ambitious philosophical work of the British Empiricist tradition. Hume was twenty-six when he published it. It \u201cfell dead-born from the press,\u201d as he wrote in My Own Life, without reaching \u201csuch distinction as even to excite a murmur among the zealots\u201d \u2014 and it is the most consequential failure in the history of philosophy.\n\nBook I, \u201cOf the Understanding,\u201d is Hume\u2019s epistemology. The fundamental distinction is between impressions (the immediate data of sensation and emotion, vivid and forceful) and ideas (the fainter copies of impressions in thought and memory). All genuine ideas must be traceable to antecedent impressions \u2014 this is Hume\u2019s empiricist criterion of meaning. The examination of causation follows from this principle: we never perceive causal necessity in the world, only the constant conjunction of events and the habitual expectation this produces in the mind. \u201cCausation\u201d is not a feature of the external world but a projection of the mind\u2019s own habits. The problem of induction \u2014 the impossibility of rationally justifying the inference from observed to unobserved cases \u2014 follows: reason alone cannot establish that the future will resemble the past. Only custom and habit, not reason, underlies our causal and inductive beliefs.\n\nBook I also contains Hume\u2019s most radical doctrine: the bundle theory of the self (1.4.6, \u201cOf Personal Identity\u201d). When I introspect, I never find a unified self or soul \u2014 only a bundle of particular perceptions in constant flux. There is no impression of a continuing self, therefore no legitimate idea of one. The self is \u201cnothing but a bundle or collection of different perceptions, which succeed each other with inconceivable rapidity, and are in perpetual flux and motion.\u201d\n\nBook II, \u201cOf the Passions,\u201d is Hume\u2019s philosophy of mind and motivation. The passions (pride, humility, love, hatred, desire, aversion) are indirect or direct impressions arising from the perception of pleasure and pain. The famous dictum: \u201cReason is, and ought only to be the slave of the passions, and can never pretend to any other office than to serve and obey them\u201d (2.3.3). Reason by itself can produce no action; only the passions can motivate. Reason informs us of facts and means; the passions determine what we want.\n\nBook III, \u201cOf Morals,\u201d derives ethics from sentiment. Moral distinctions are not derived from reason but from the \u201cmoral sense\u201d \u2014 a sentiment of approbation or disapprobation that arises when we contemplate characters and actions from a general point of view. The famous is-ought gap (3.1.1): Hume observes that moral philosophers routinely move, without justification, from descriptive premises (\u201cis\u201d statements) to normative conclusions (\u201cought\u201d statements). This logical gap \u2014 Hume\u2019s guillotine \u2014 has structured metaethics ever since. The distinction between natural virtues (benevolence, gratitude) and artificial virtues (justice, fidelity to promises) grounds a sophisticated social theory: justice is not natural but arises from convention, because its social utility makes it in everyone\u2019s long-term interest to maintain.',
    themes: ['impressions and ideas', 'the problem of induction', 'the critique of causation', 'the bundle theory of the self', 'reason as slave of the passions', 'the is-ought gap', 'natural and artificial virtues', 'the experimental method in philosophy', 'custom and habit', 'sympathy'],
    keyCharacters: [],
    concepts: [
        'Impressions vs ideas \u2014 impressions are the vivid, immediate data of sensation and passion; ideas are their fainter copies in thought; all genuine ideas must be traceable to impressions',
        'The copy principle \u2014 every simple idea is a copy of a corresponding impression; any idea lacking an antecedent impression is meaningless or confused',
        'The problem of induction \u2014 no rational justification exists for inferring from observed regularities to unobserved cases; only custom and habit, not reason, grounds inductive belief',
        'Causation as constant conjunction \u2014 we never perceive necessary connection; causation is only regular succession plus the mind\u2019s habitual expectation, not an objective feature of reality',
        'Custom or habit (Custom is the great guide of human life) \u2014 the psychological mechanism that produces causal and inductive belief; it operates below reason',
        'The bundle theory of the self \u2014 the self is not a unified substance but a bundle of particular perceptions in flux; there is no impression of a continuing self',
        'Reason is the slave of the passions \u2014 reason by itself cannot motivate action; it can only inform us of means and facts; the passions determine what we want and pursue',
        'The is-ought gap (Hume\u2019s guillotine) \u2014 the logical gap between descriptive premises and normative conclusions that moral philosophers routinely cross without justification',
        'Natural vs artificial virtues \u2014 natural virtues (benevolence, compassion) arise from innate human tendencies; artificial virtues (justice, promise-keeping) arise from social convention',
        'Sympathy \u2014 the mechanism by which we enter into the sentiments of others and come to share their pleasures and pains; the foundation of social life and moral judgment'
    ],
    structure: 'Book I: Of the Understanding\n\u2014 Part 1: Of ideas, their origin, composition, connexion, abstraction\n\u2014 Part 2: Of the ideas of space and time\n\u2014 Part 3: Of knowledge and probability (causation, induction, belief)\n\u2014 Part 4: Of the sceptical and other systems of philosophy (the bundle theory; external world; personal identity)\n\nBook II: Of the Passions\n\u2014 Part 1: Of pride and humility\n\u2014 Part 2: Of love and hatred\n\u2014 Part 3: Of the will and direct passions; reason as slave of the passions\n\nBook III: Of Morals\n\u2014 Part 1: Of virtue and vice in general; moral distinctions from sentiment not reason; the is-ought gap\n\u2014 Part 2: Of justice and injustice; artificial virtues; the origin of justice from convention\n\u2014 Part 3: Of the other virtues and vices; natural virtues; sympathy',
    quote: 'Reason is, and ought only to be the slave of the passions, and can never pretend to any other office than to serve and obey them.',
    additionalQuotes: [
        { text: 'The self is nothing but a bundle or collection of different perceptions, which succeed each other with inconceivable rapidity, and are in perpetual flux and motion.', citation: 'Treatise 1.4.6' },
        { text: 'In every system of morality which I have hitherto met with, I have always remark\u2019d, that the author proceeds for some time in the ordinary way of reasoning, and then suddenly, instead of the usual copulations of propositions, is and is not, I meet with no proposition that is not connected with an ought, or an ought not.', citation: 'Treatise 3.1.1' },
        { text: 'Custom, then, is the great guide of human life. It is that principle alone which renders our experience useful to us.', citation: 'Enquiry Concerning Human Understanding, Section V' },
        { text: 'Nature will always maintain her rights, and prevail in the end over any abstract reasoning whatsoever.', citation: 'Treatise 1.4.2' }
    ],
    commentary: [
        { philosopher: 'Immanuel Kant', text: 'Kant famously credited Hume with waking him from his \u201cdogmatic slumber\u201d \u2014 specifically, Hume\u2019s argument in the Treatise that the causal connection between events cannot be known a priori but is merely a habit of association. Kant recognised that if Hume was right, then all of metaphysics and much of natural science rested on foundations no more secure than psychological habit. The Critique of Pure Reason is Kant\u2019s systematic attempt to answer Hume: to show that causality is a genuine a priori category of the understanding that necessarily applies to all possible experience, rather than a mere custom of the mind.' },
        { philosopher: 'Norman Kemp Smith', text: 'Kemp Smith\u2019s The Philosophy of David Hume (1941) transformed Hume scholarship by arguing that the central thesis of the Treatise is not skepticism but naturalism: Hume\u2019s aim is not to show that our beliefs in causation, the external world, and the self are rationally unjustifiable (which he demonstrates easily) but to show that they are naturally inevitable \u2014 that human nature is such that we cannot help believing them, whatever reason says. This \u201cnaturalist\u201d reading has been the dominant interpretation ever since.' },
        { philosopher: 'Barry Stroud', text: 'Stroud\u2019s Hume (1977) is the most philosophically rigorous study of the Treatise in the Anglophone tradition. Stroud argues that the problem of induction and the critique of causation are genuine philosophical achievements \u2014 not mere curiosities of eighteenth-century psychology \u2014 and that Hume\u2019s naturalist response (relying on custom and habit) is philosophically unsatisfying but honest: he acknowledges that reason cannot vindicate our beliefs and refuses the false comfort of claiming it can.' },
        { philosopher: 'Annette Baier', text: 'Baier\u2019s A Progress of Sentiments (1991) reads the Treatise as a unified whole rather than a collection of independent arguments, arguing that Book II on the passions and Book III on morals are not appendages to the epistemological core of Book I but its completion. The Treatise\u2019s true subject is the nature of human mental life in its entirety \u2014 cognitive, emotional, and moral \u2014 and sympathy is its central concept.' },
        { philosopher: 'Don Garrett', text: 'Garrett\u2019s Cognition and Commitment in Hume\u2019s Philosophy (1997) defends Hume as a rigorous philosophical systematiser whose arguments are more consistent and more sophisticated than his critics have acknowledged. The bundle theory of the self, the critique of causation, and the derivation of morality from sentiment are not isolated skeptical gambits but elements of a coherent philosophical programme.' }
    ],
    modernRelevance: 'The Treatise of Human Nature is the founding document of modern empiricism, philosophy of mind, and metaethics. The problem of induction remains one of the most debated problems in the philosophy of science: Popper\u2019s falsificationism, Goodman\u2019s new riddle of induction, and Bayesian confirmation theory are all responses to the Humean challenge. The bundle theory of the self has been taken up by Derek Parfit in Reasons and Persons (1984), which argues on Humean grounds that personal identity is not what matters in survival, with radical implications for ethics, prudential reasoning, and population ethics. The is-ought gap remains the foundational problem of metaethics: every major position in contemporary moral philosophy defines itself relative to it. The critique of causation anticipates contemporary debates about causal realism, interventionism, and the metaphysics of causation.',
    context: 'Hume wrote the Treatise between 1734 and 1737 during a period of intense intellectual labour in France (primarily La Fl\u00e8che, where Descartes had been educated). He had suffered a mental crisis in his early twenties from over-intense philosophical study and had retreated to business before returning to philosophy. He was twenty-six when Books I and II were published. The work\u2019s failure devastated him. He subsequently rewrote its central arguments in the two Enquiries (1748, 1751), which he preferred as more polished and accessible. He consistently asked that his reputation rest on the Enquiries rather than the Treatise, but posterity has reversed this judgment.',
    relatedWorks: ['enquiry-human-understanding', 'enquiry-principles-morals', 'abstract-treatise', 'dialogues-natural-religion']
}
);
"""

# ── data-22b: Abstract + Enquiry Concerning Human Understanding ─────────────
files['data-22b.js'] = r"""/* DATA PART 22b — Hume: Abstract + Enquiry Concerning Human Understanding */
window.WORKS.push(

{
    id: 'abstract-treatise',
    title: 'An Abstract of a Book Lately Published',
    greekTitle: 'Abstract of a Treatise of Human Nature',
    philosopher: 'hume',
    category: 'metaphysics',
    categoryLabel: 'Epistemology',
    date: '1740 AD',
    dateSort: 1740,
    emoji: '\uD83D\uDD0E',
    cardSize: 'normal',
    readingDifficulty: 'Intermediate',
    estimatedWordCount: 5000,
    shortDesc: 'Hume\u2019s own anonymous summary of the Treatise \u2014 a compressed masterpiece that isolates the argument on causation as the work\u2019s central philosophical achievement and states it with a clarity the Treatise itself rarely achieves.',
    summary: 'An Abstract of a Book Lately Published, Entitled, A Treatise of Human Nature, published anonymously in March 1740, is Hume\u2019s own compressed account of the Treatise\u2019s central argument. Hume published it anonymously, writing about himself in the third person as if reviewing a work by another, in an attempt to generate interest in the Treatise after its initial failure.\n\nThe Abstract is valuable not merely as a summary but as an interpretive document: it shows which arguments Hume himself regarded as central. He focuses almost entirely on the analysis of causation and the problem of induction, presenting them as the Treatise\u2019s primary philosophical achievement. The argument is stated with exceptional clarity: we observe constant conjunction but never perceive necessary connection; custom and habit, not reason, produce our belief in causal necessity; the inference from past to future \u2014 the inference that the future will resemble the past \u2014 cannot be rationally justified and rests entirely on custom.\n\nThe Abstract was lost after Hume\u2019s death and not rediscovered until 1938, when J.M. Keynes and Piero Sraffa identified Hume as its anonymous author. Its rediscovery transformed understanding of Hume\u2019s intentions in the Treatise by providing authoritative evidence for which arguments he considered central.',
    themes: ['causation and constant conjunction', 'the problem of induction', 'custom and habit', 'the limits of reason', 'the experimental method'],
    keyCharacters: [],
    concepts: [
        'Causation as constant conjunction \u2014 the core of the Abstract\u2019s argument: we observe succession and contiguity but never perceive necessary connection between cause and effect',
        'Custom as the source of causal belief \u2014 the inference from observed to unobserved is produced by habit, not reason; it cannot be rationally justified',
        'The problem of induction stated crisply \u2014 even a million observations of A followed by B give no rational ground for inferring the next A will be followed by B; only custom bridges this gap'
    ],
    structure: 'A single continuous essay of approximately twenty pages:\n\u2014 Introduction: The novelty of the Treatise\u2019s method\n\u2014 The central argument: impressions, ideas, and the copy principle\n\u2014 The analysis of causation: constant conjunction, not necessary connection\n\u2014 The problem of induction: custom, not reason, as the source of causal inference\n\u2014 The account of belief: belief as a lively idea associated with a present impression',
    quote: 'It is not, therefore, reason which is the guide of life, but custom.',
    additionalQuotes: [
        { text: 'Here is a bill of fare of the courses. But I am hopeful the author will excuse me, if I single out only one of these, which seems to me most curious and most important.', citation: 'Abstract, opening (on the analysis of causation)' }
    ],
    commentary: [
        { philosopher: 'J.M. Keynes and Piero Sraffa', text: 'Keynes and Sraffa\u2019s identification of Hume as the anonymous author of the Abstract (1938) was one of the most important archival discoveries in the history of philosophy. Their edition (Cambridge, 1938) established that Hume himself considered the analysis of causation and the problem of induction the Treatise\u2019s central contribution \u2014 resolving a long-standing scholarly debate about Hume\u2019s intentions.' }
    ],
    modernRelevance: 'The Abstract is the most concise statement of the Humean challenge to rationalism. Its compressed argument on causation and induction has been reproduced in virtually every introduction to the theory of knowledge and the philosophy of science. Bertrand Russell\u2019s formulation of the problem of induction in The Problems of Philosophy (1912) is essentially a modernisation of the Abstract\u2019s central argument.',
    context: 'Published anonymously in March 1740, three months after Book III of the Treatise, in an attempt to revive interest in a work that had failed to attract attention. Hume writes about the Treatise in the third person as if reviewing it. The Abstract was reprinted once in Hume\u2019s lifetime and then lost. J.M. Keynes and Piero Sraffa rediscovered it in 1938 in a copy at Trinity College Cambridge and published an edition identifying Hume as its author.',
    relatedWorks: ['treatise-human-nature', 'enquiry-human-understanding']
},

{
    id: 'enquiry-human-understanding',
    title: 'An Enquiry Concerning Human Understanding',
    greekTitle: 'Philosophical Essays Concerning Human Understanding (original title)',
    philosopher: 'hume',
    category: 'metaphysics',
    categoryLabel: 'Epistemology & Metaphysics',
    date: '1748 AD',
    dateSort: 1748,
    emoji: '\u2693\uFE0F',
    cardSize: 'wide',
    readingDifficulty: 'Intermediate',
    estimatedWordCount: 60000,
    shortDesc: 'The mature restatement of the Treatise\u2019s epistemology \u2014 clearer, more elegant, and more provocative \u2014 containing the famous fork between relations of ideas and matters of fact, the devastating argument against miracles, and the most accessible statement of Hume\u2019s scepticism.',
    summary: 'An Enquiry Concerning Human Understanding, published in 1748 (originally as Philosophical Essays Concerning Human Understanding; retitled in 1758), is Hume\u2019s rewriting of Book I of the Treatise for a more general philosophical audience. He considered it a more polished and accurate statement of his views and asked that his reputation rest on it rather than the Treatise. It is shorter, clearer, and more rhetorically devastating than its predecessor.\n\nSection IV contains \u201cHume\u2019s fork\u201d \u2014 the exhaustive division of all objects of human reason into two categories. Relations of ideas (the propositions of logic, mathematics, and geometry) are demonstrably certain, known by the mere operation of thought, and true by necessity \u2014 but they tell us nothing about the existence of anything in the world. Matters of fact (empirical claims about the world) rest on causal reasoning and experience \u2014 but as the analysis of causation has shown, causal reasoning cannot be rationally justified: it rests on custom, not reason. The fork has devastating consequences: everything that cannot be classified as either a relation of ideas or a matter of fact is neither demonstrably true nor empirically grounded, and should be committed to the flames.\n\nSection X, \u201cOf Miracles,\u201d is the most celebrated and most controversial of Hume\u2019s philosophical essays. A miracle is a violation of the laws of nature. The evidence for the laws of nature is the entire uniform experience of humanity. For any miracle claim, we must weigh the testimony for the miracle against the evidence from uniform experience. Since uniform experience outweighs any finite amount of testimony, no testimony is sufficient to establish a miracle \u2014 unless its falsehood would be more miraculous than the miracle it reports. Furthermore, miracles are reported primarily in ignorant and barbarous nations, by those with every interest in promoting the belief, and no religion\u2019s miracles are attested by persons of sufficient credit. The argument does not prove that miracles are impossible but that we can never have rational grounds for believing in them.\n\nSection XII, \u201cOf the Academical or Sceptical Philosophy,\u201d introduces a mitigated scepticism: we cannot avoid having beliefs that outrun our evidence (in the external world, in causation, in personal identity), but the philosopher who recognises this is in a better epistemic position than the dogmatist who does not.',
    themes: ['Hume\u2019s fork', 'relations of ideas vs matters of fact', 'causation and necessary connection', 'the problem of induction', 'the argument against miracles', 'mitigated scepticism', 'the limits of reason', 'custom and habit', 'the experimental method'],
    keyCharacters: [],
    concepts: [
        'Hume\u2019s fork \u2014 all objects of human reason divide into relations of ideas (demonstrably certain, uninformative about existence) and matters of fact (empirically grounded, uncertain); anything belonging to neither category is meaningless',
        'Relations of ideas \u2014 propositions of logic, mathematics, and geometry; known by the operation of thought alone; necessarily true; tell us nothing about what exists',
        'Matters of fact \u2014 empirical claims about the world; grounded in causal reasoning and experience; contingent; cannot be known with certainty',
        'The argument against miracles \u2014 testimony for miracles can never outweigh the evidence from uniform experience that establishes the laws of nature; no testimony is sufficient to establish a miracle',
        'Mitigated scepticism \u2014 we cannot help having beliefs that outrun our evidence; the philosopher acknowledges this and maintains a moderate epistemic humility rather than the false confidence of dogmatism',
        'The sceptical solution to scepticism \u2014 Hume\u2019s naturalist response: since reason cannot vindicate our basic beliefs, and since we cannot help holding them, the appropriate response is not radical doubt but recognition of human nature\u2019s limits'
    ],
    structure: 'Section I: Of the different species of philosophy\nSection II: Of the origin of ideas (the copy principle)\nSection III: Of the association of ideas\nSection IV: Sceptical doubts concerning the operations of the understanding (Hume\u2019s fork; the problem of induction)\nSection V: Sceptical solution of these doubts (custom and habit)\nSection VI: Of probability\nSection VII: Of the idea of necessary connexion (causation)\nSection VIII: Of liberty and necessity\nSection IX: Of the reason of animals\nSection X: Of miracles\nSection XI: Of a particular providence and of a future state\nSection XII: Of the academical or sceptical philosophy',
    quote: 'If we take in our hand any volume; of divinity or school metaphysics, for instance; let us ask, Does it contain any abstract reasoning concerning quantity or number? No. Does it contain any experimental reasoning concerning matter of fact and existence? No. Commit it then to the flames: for it can contain nothing but sophistry and illusion.',
    additionalQuotes: [
        { text: 'Nature will always maintain her rights, and prevail in the end over any abstract reasoning whatsoever.', citation: 'Enquiry Concerning Human Understanding, Section V' },
        { text: 'A wise man proportions his belief to the evidence.', citation: 'Enquiry Concerning Human Understanding, Section X' },
        { text: 'The contrary of every matter of fact is still possible; because it can never imply a contradiction, and is conceived by the mind with the same facility and distinctness, as if ever so conformable to reality.', citation: 'Enquiry Concerning Human Understanding, Section IV' }
    ],
    commentary: [
        { philosopher: 'Immanuel Kant', text: 'Kant read the Enquiry (in the German translation of Sulzer, 1755) before the Treatise, and it was the Enquiry\u2019s argument on causation that provoked the critical philosophy. Kant\u2019s formulation of the problem \u2014 \u201chow are synthetic a priori judgments possible?\u201d \u2014 is the direct response to Hume\u2019s demonstration that causal claims cannot be analytically true (they are not relations of ideas) yet claim universal necessity.' },
        { philosopher: 'A.J. Ayer', text: 'Ayer\u2019s Language, Truth and Logic (1936) adopted Hume\u2019s fork as the foundational principle of logical positivism: the verification principle \u2014 that a statement is meaningful only if it is either analytic or empirically verifiable \u2014 is a twentieth-century reformulation of Hume\u2019s division of all objects of human reason. The famous conclusion \u2014 commit metaphysics to the flames \u2014 became the slogan of logical positivism.' },
        { philosopher: 'Karl Popper', text: 'Popper\u2019s Logic of Scientific Discovery (1934) is a direct response to Hume\u2019s problem of induction. Popper accepted Hume\u2019s demonstration that induction cannot be rationally justified and proposed falsificationism as a solution: science proceeds not by inductive generalisation but by bold conjectures that are then subjected to severe tests. The asymmetry between verification (requiring infinite confirmations) and falsification (requiring only one disconfirmation) allows science to proceed without induction.' },
        { philosopher: 'Peter Millican', text: 'Millican\u2019s careful philosophical analysis of the Enquiry (Cambridge edition, 2007) argues that the argument against miracles in Section X is both more sophisticated and more vulnerable than commonly supposed. The crucial claim \u2014 that testimony for a miracle can never outweigh the evidence from uniform experience \u2014 raises deep questions about the epistemology of testimony and the relationship between individual and collective evidence that Hume does not fully resolve.' },
        { philosopher: 'Barry Stroud', text: 'Stroud\u2019s analysis of the Enquiry in Hume (1977) argues that the \u201csceptical solution\u201d \u2014 the appeal to custom and habit as the basis of causal belief \u2014 is not a genuine philosophical resolution of the sceptical problem but a change of subject. Hume shows that reason cannot justify our beliefs and then notes that custom produces them anyway; but this psychological observation does not address the epistemological question of whether the beliefs are justified.' }
    ],
    modernRelevance: 'The Enquiry Concerning Human Understanding is the most widely assigned philosophical text in introductory epistemology courses worldwide. Hume\u2019s fork remains the standard framework for the logical positivist critique of metaphysics and theology. The argument against miracles is the standard philosophical reference point in debates about the epistemology of testimony, the rationality of religious belief, and the relationship between scientific and religious knowledge. The problem of induction has generated the most sustained research programme in the philosophy of science of any single philosophical problem. The mitigated scepticism of Section XII anticipates contemporary epistemic humility, fallibilism, and the recognition that our cognitive faculties are evolved rather than designed for truth.',
    context: 'First published as Philosophical Essays Concerning Human Understanding (London, A. Millar, 1748). The title was changed to An Enquiry Concerning Human Understanding in 1758 when Hume collected his essays and treatises for a complete edition. Hume had been dissatisfied with the Treatise\u2019s failure and rewrote its central arguments in more accessible form. He explicitly asked in My Own Life that his philosophical reputation rest on the two Enquiries rather than the Treatise, and listed the Enquiries among the works by which he wished to be judged.',
    relatedWorks: ['treatise-human-nature', 'enquiry-principles-morals', 'dialogues-natural-religion', 'abstract-treatise']
}

);
"""

# ── data-22c: Enquiry Principles of Morals + Dialogues ──────────────────────
files['data-22c.js'] = r"""/* DATA PART 22c — Hume: Enquiry Principles of Morals + Dialogues */
window.WORKS.push(

{
    id: 'enquiry-principles-morals',
    title: 'An Enquiry Concerning the Principles of Morals',
    greekTitle: 'Concerning the Principles of Morals',
    philosopher: 'hume',
    category: 'ethics',
    categoryLabel: 'Ethics & Moral Philosophy',
    date: '1751 AD',
    dateSort: 1751,
    emoji: '\u2696\uFE0F',
    cardSize: 'normal',
    readingDifficulty: 'Intermediate',
    estimatedWordCount: 55000,
    shortDesc: 'Hume\u2019s own favourite among all his works \u2014 a systematic derivation of moral principles from sentiment and utility, arguing that both reason and passion cooperate in moral judgment and that the foundation of morality is the natural human capacity for sympathy with the interests of others.',
    summary: 'An Enquiry Concerning the Principles of Morals, published in 1751, is Hume\u2019s rewriting of Book III of the Treatise and the work he described in My Own Life as \u201cincomparably the best\u201d of all his writings. It is shorter, more elegant, and more positive in tone than the Treatise\u2019s account of morals \u2014 less focused on demolishing rationalist theories and more concerned with constructively explaining the actual foundations of our moral distinctions.\n\nThe central question is not \u201cwhat is morally good?\u201d but \u201cwhat is the principle by which we approve of characters and actions?\u201d Hume\u2019s answer combines sentiment and reason. Sentiment supplies the motivating force \u2014 the feeling of approbation or disapprobation that arises when we contemplate a character or action from a general point of view. Reason supplies the relevant information: the facts about a person\u2019s character, the consequences of actions, the social context. Neither alone is sufficient: reason without sentiment cannot motivate; sentiment without reason cannot distinguish the genuinely virtuous from the merely pleasing.\n\nThe Enquiry\u2019s most important innovation over the Treatise is the systematic account of utility as the foundation of many virtues. Public utility \u2014 the tendency of a quality to promote the welfare of society \u2014 is a primary source of moral approbation. Justice, fidelity, honesty, and the social virtues generally are approved because their social utility is evident. Even \u201cprivate\u201d virtues like prudence and temperance are partly approved because of their utility to the person who possesses them. This analysis anticipates utilitarianism: Bentham explicitly acknowledged Hume as one of his primary influences.\n\nThe Enquiry\u2019s final section, \u201cOf the Reasons Why Utility Pleases,\u201d addresses a fundamental question: why should utility \u2014 the benefit to others \u2014 please us at all? Hume\u2019s answer is sympathy: the natural human capacity to enter into the feelings of others and to take pleasure in their pleasure and pain in their pain. Sympathy is not a cultivated moral achievement but a natural feature of the human mind \u2014 as natural as self-interest.',
    themes: ['sentiment and reason in morality', 'utility as the foundation of virtue', 'sympathy', 'the general point of view', 'natural and artificial virtues', 'the social virtues', 'moral approbation and disapprobation', 'personal virtues'],
    keyCharacters: [],
    concepts: [
        'Sentiment as the foundation of morality \u2014 moral distinctions are ultimately derived from a natural feeling of approbation or disapprobation, not from reason alone',
        'Utility as a primary source of moral approbation \u2014 the tendency of a quality to promote social welfare is one of the primary reasons we approve of it',
        'The general point of view \u2014 moral judgment requires taking a perspective that is not biased by self-interest or personal relationship; we must consider the effects of actions and characters on all affected parties',
        'Sympathy as the mechanism of moral motivation \u2014 we naturally enter into the feelings of others; their pleasure is our pleasure; their pain is our pain; this natural sympathy is the source of altruistic motivation',
        'The cooperation of reason and sentiment \u2014 reason provides the facts (about characters, consequences, social context); sentiment provides the motivating approval or disapproval; neither alone suffices for moral judgment',
        'Natural virtues (benevolence, gratitude, friendship) \u2014 approved because they are immediately agreeable to their possessor or to others, or because of their obvious utility',
        'Artificial virtues (justice, fidelity to promises) \u2014 approved because of their social utility; their value is not immediately apparent but depends on recognising the social system they sustain'
    ],
    structure: 'Section I: Of the general principles of morals\nSection II: Of benevolence\nSection III: Of justice\nSection IV: Of political society\nSection V: Why utility pleases\nSection VI: Of qualities useful to ourselves\nSection VII: Of qualities immediately agreeable to ourselves\nSection VIII: Of qualities immediately agreeable to others\nSection IX: Conclusion\n\nAppendices:\n\u2014 Appendix I: Concerning Moral Sentiment\n\u2014 Appendix II: Of Self-Love\n\u2014 Appendix III: Some Further Considerations with Regard to Justice\n\u2014 Appendix IV: Of Some Verbal Disputes',
    quote: 'The hypothesis which we embrace is plain. It maintains that morality is determined by sentiment. It defines virtue to be whatever mental action or quality gives to a spectator the pleasing sentiment of approbation; and vice the contrary.',
    additionalQuotes: [
        { text: 'It appears that a tendency to public good, and to the promoting of peace, harmony, and order in society, does always, by affecting the benevolent principles of our frame, engage us on the side of the social virtues.', citation: 'Enquiry Concerning the Principles of Morals, Section V' },
        { text: 'Celibacy, fasting, penance, mortification, self-denial, humility, silence, solitude, and the whole train of monkish virtues \u2014 for what reason are they everywhere rejected by men of sense, but because they serve no manner of purpose?', citation: 'Enquiry Concerning the Principles of Morals, Section IX' }
    ],
    commentary: [
        { philosopher: 'Jeremy Bentham', text: 'Bentham explicitly acknowledged in his Introduction to the Principles of Morals and Legislation (1789) that Hume\u2019s account of utility in the second Enquiry was one of the primary sources of his own utilitarian theory. Hume\u2019s demonstration that utility is a primary source of moral approbation \u2014 and his naturalistic explanation of why utility pleases through sympathy \u2014 provided the empirical foundation on which Bentham built his normative utilitarianism.' },
        { philosopher: 'Adam Smith', text: 'Adam Smith\u2019s Theory of Moral Sentiments (1759) is in many respects an elaboration and refinement of the second Enquiry\u2019s account of moral judgment. Smith developed Hume\u2019s concept of the \u201cgeneral point of view\u201d into the more sophisticated figure of the \u201cimpartial spectator\u201d \u2014 the imagined observer whose perspective defines the moral standard. Smith and Hume were close friends, and Smith is generally regarded as Hume\u2019s most distinguished philosophical disciple.' },
        { philosopher: 'Christine Korsgaard', text: 'Korsgaard\u2019s sources of Normativity (1996) treats the second Enquiry as a central target: Hume\u2019s derivation of moral norms from natural sentiments faces the problem of explaining moral normativity \u2014 why we are obligated to follow the sentiments of the general point of view rather than our own immediate inclinations. Korsgaard argues that Hume cannot solve this problem without appealing to a principle of rational self-constitution that his empiricist framework cannot accommodate.' }
    ],
    modernRelevance: 'The second Enquiry is the philosophical origin of British utilitarianism and consequentialism. Bentham\u2019s utility principle, Mill\u2019s higher pleasures, and contemporary consequentialism all descend from Hume\u2019s analysis. The \u201cgeneral point of view\u201d anticipates Adam Smith\u2019s impartial spectator, Rawls\u2019s veil of ignorance, and the entire tradition of ideal observer theories in ethics. The account of sympathy anticipates contemporary empathy research and the neuroscience of moral judgment. Hume\u2019s critique of \u201cmonkish virtues\u201d \u2014 self-denial for its own sake without social utility \u2014 is the founding text of secular ethics.',
    context: 'Published in London by Andrew Millar in 1751. Hume described it in My Own Life (1776) as \u201cincomparably the best\u201d of all his writings. The work was written after the relative success of the first Enquiry and the Essays had established Hume\u2019s reputation as a man of letters, and it reflects a more confident and more constructive philosophical voice than the combative Treatise.',
    relatedWorks: ['treatise-human-nature', 'enquiry-human-understanding', 'essays-moral-political', 'dialogues-natural-religion']
},

{
    id: 'dialogues-natural-religion',
    title: 'Dialogues Concerning Natural Religion',
    greekTitle: 'Dialogues Concerning Natural Religion',
    philosopher: 'hume',
    category: 'practical',
    categoryLabel: 'Philosophy of Religion',
    date: '1779 AD',
    dateSort: 1779,
    emoji: '\u26EA\uFE0F',
    cardSize: 'wide',
    readingDifficulty: 'Intermediate',
    estimatedWordCount: 40000,
    shortDesc: 'The most devastating philosophical critique of natural theology ever written \u2014 a three-way dialogue in which Hume, writing as Philo the sceptic, dismantles the design argument, the cosmological argument, and the argument from providence, and confronts the problem of evil with a directness that no subsequent apologist has fully answered.',
    summary: 'Dialogues Concerning Natural Religion, written in the 1750s, revised repeatedly, and published posthumously in 1779 (three years after Hume\u2019s death, by his nephew David Hume the Younger), is the greatest philosophical examination of the arguments for the existence of God in any language. Hume was acutely aware of its explosive potential and withheld it from publication during his lifetime despite repeated urgings from his friend Adam Smith. The dialogue form gave him deniability: the views expressed are those of the characters, not necessarily of the author.\n\nThe three main characters represent three philosophical positions on natural theology. Pamphilus is the narrator, a young student sympathetic to Cleanthes. Cleanthes is the empirical theist: he defends the existence of God through the design argument \u2014 the analogy between the order of nature and the order of a machine, which implies an intelligent designer. Demea is the religious rationalist: he defends God through the cosmological argument (every contingent thing requires a cause; the chain of causes must terminate in a necessary being) and insists that God\u2019s nature is entirely incomprehensible to human reason. Philo is the philosophical sceptic: almost universally identified as Hume\u2019s own voice, he subjects both positions to systematic critique.\n\nPhilo\u2019s critique of the design argument is the most sustained. The analogy between nature and a machine is weak: the universe resembles a machine only in certain respects, and in other respects it resembles an organism, a vegetable, or a spider\u2019s web. Even if we grant the analogy, it establishes only a designer proportionate to the observed effects \u2014 not omnipotent, omniscient, or perfectly good. It cannot establish that there is only one designer. And the origin of the divine mind itself raises the same question as the origin of the ordered universe: what explains the order in the designer\u2019s mind?\n\nThe problem of evil receives its most rigorous philosophical treatment in Parts X and XI. Philo formulates what is now called the logical problem of evil: if God is omnipotent, omniscient, and perfectly good, how can evil exist? Cleanthes cannot answer this adequately. Philo then offers the evidential problem: even if evil is logically compatible with the existence of a perfectly good God, the actual quantity and distribution of suffering in the world makes it improbable that the world was created by such a being. The four circumstances that allow evil to exist (the economy of pain and pleasure as motivators, the regular operation of general laws, the limited powers and faculties of creatures, and the inaccurate workmanship of nature) could all have been otherwise \u2014 and a perfectly good God would have made them otherwise.\n\nThe Dialogues end ambiguously. Philo makes a surprising apparent concession: a cause or causes proportionate to the observed order of the universe must exist. But this cause bears no resemblance to the God of any religion; it tells us nothing about divine attributes or moral government; and it does not vindicate any form of religious practice. The philosophical sceptic and the thoughtful theist are, Philo suggests, saying very nearly the same thing in different words.',
    themes: ['the design argument', 'the cosmological argument', 'the problem of evil', 'natural theology', 'the analogy between nature and a machine', 'scepticism about religion', 'the incomprehensibility of God', 'Philo as Hume\u2019s voice', 'the dialogue form', 'providence and suffering'],
    keyCharacters: [
        { name: 'Philo', role: 'The philosophical sceptic; almost universally identified as Hume\u2019s own voice; subjects both empirical theism and rationalist theology to systematic critique without offering any positive alternative' },
        { name: 'Cleanthes', role: 'The empirical theist; defends the existence of God through the design argument \u2014 the analogy between the order of nature and the order of a machine implies an intelligent designer' },
        { name: 'Demea', role: 'The religious rationalist and orthodox believer; defends the cosmological argument; insists on the incomprehensibility of God; leaves the dialogue when he realises Philo and Cleanthes have undermined the foundations of religion' }
    ],
    concepts: [
        'The design argument (argument from analogy) \u2014 Cleanthes\u2019 position: the order of nature resembles the order of a machine; machines have intelligent designers; therefore nature has an intelligent designer',
        'Philo\u2019s critique of the design argument \u2014 the analogy is weak; the universe resembles an organism or vegetable as much as a machine; even granting the analogy, it establishes only a designer proportionate to effects, not an omnipotent, omniscient, perfectly good being',
        'The cosmological argument \u2014 Demea\u2019s position: every contingent thing requires a cause; the chain of causes must terminate in a necessary being; this necessary being is God',
        'The problem of evil (logical formulation) \u2014 if God is omnipotent, omniscient, and perfectly good, evil cannot exist; evil exists; therefore God as traditionally conceived cannot exist',
        'The problem of evil (evidential formulation) \u2014 the actual quantity and distribution of suffering makes it improbable that the world was created by an omnipotent, omniscient, perfectly good being',
        'The four circumstances permitting evil \u2014 the economy of pain/pleasure as motivators, the operation of general laws, the limited powers of creatures, the inaccurate workmanship of nature; each could have been otherwise, yet a good God did not make it otherwise',
        'Philo\u2019s apparent concession \u2014 a cause or causes proportionate to the observed order must exist; but this entity bears no resemblance to the God of religion and tells us nothing about divine attributes or moral government'
    ],
    structure: 'Part I: The method of natural theology; whether reason can establish religious conclusions\nPart II: The design argument stated by Cleanthes\nPart III: Philo\u2019s first objections to the design argument\nPart IV: The problem of the divine mind\nPart V: The design argument weakened further; the multiplicity of deities\nPart VI\u2013VIII: Alternative cosmological hypotheses (the vegetable analogy, the generation analogy, the Manichean hypothesis)\nPart IX: The cosmological argument (Demea); Philo\u2019s critique\nPart X: The problem of evil stated\nPart XI: The evidential problem of evil; the four circumstances permitting evil\nPart XII: Philo\u2019s apparent concession; Demea\u2019s departure; the ambiguous conclusion',
    quote: 'The whole frame of nature bespeaks an intelligent author; and no rational enquirer can, after serious reflection, suspend his belief a moment with regard to the primary principles of genuine Theism and Religion.',
    additionalQuotes: [
        { text: 'Epicurus\u2019 old questions are yet unanswered. Is he willing to prevent evil, but not able? then is he impotent. Is he able, but not willing? then is he malevolent. Is he both able and willing? whence then is evil?', citation: 'Dialogues, Part X (Philo)' },
        { text: 'A total suspense of judgment is here our only reasonable resource.', citation: 'Dialogues, Part I (Philo)' },
        { text: 'The whole is a riddle, an enigma, an inexplicable mystery. Doubt, uncertainty, suspence of judgment appear the only result of our most accurate scrutiny, concerning this subject.', citation: 'Dialogues, Part XII (Philo)' }
    ],
    commentary: [
        { philosopher: 'Norman Kemp Smith', text: 'Kemp Smith\u2019s edition of the Dialogues (1935; revised 1947) remains the standard scholarly edition. His central interpretive argument \u2014 that Philo is unambiguously Hume\u2019s own voice throughout, including the apparent concession at the end of Part XII \u2014 has been largely accepted. Kemp Smith argues that the concession is ironic: Philo grants a minimal conclusion that no religious believer would find satisfying, precisely to demonstrate how far natural theology falls short of genuine religious commitment.' },
        { philosopher: 'J.C.A. Gaskin', text: 'Gaskin\u2019s Hume\u2019s Philosophy of Religion (1978; 2nd ed. 1988) provides the most systematic analysis of the Dialogues\u2019 arguments, arguing that Philo\u2019s critique of the design argument is philosophically successful and that Hume\u2019s treatment of the problem of evil anticipates the most rigorous contemporary formulations. Gaskin also identifies Hume\u2019s position as \u201cattenuated deism\u201d rather than atheism: the Dialogues do not rule out a minimal divine cause, but they make this cause theologically useless.' },
        { philosopher: 'Richard Swinburne', text: 'Swinburne\u2019s The Existence of God (1979; 2nd ed. 2004) is the most sophisticated contemporary response to the Dialogues. Swinburne argues that the Humean critique of the design argument fails because it treats the argument as an analogy rather than as an inference to the best explanation. The order of the universe is better explained by theism than by chance or by an infinite series of natural causes; probability theory vindicates the inference to God.' },
        { philosopher: 'Alvin Plantinga', text: 'Plantinga\u2019s response to the logical problem of evil \u2014 the free will defence \u2014 is the most influential contemporary reply to Philo\u2019s formulation in Parts X\u2013XI. Plantinga argues that God and evil are logically compatible because God could not create free creatures who always do good; a world with free creatures who sometimes do evil may be better than a world without freedom. The evidential problem of evil, however, has proved more resistant to solution.' }
    ],
    modernRelevance: 'The Dialogues Concerning Natural Religion is the primary philosophical text in the philosophy of religion. Every subsequent discussion of the design argument, the cosmological argument, and the problem of evil begins with Hume. The logical problem of evil formulated in Part X has generated the most sustained theological and philosophical debate of any single philosophical problem in the philosophy of religion. The design argument has been revived in the contemporary debate about intelligent design, and Philo\u2019s objections remain the standard philosophical critique. The Dialogues\u2019 influence extends beyond professional philosophy: Hume\u2019s clear, elegant formulation of the sceptical case against natural theology has shaped the secular intellectual tradition from the eighteenth century to the present.',
    context: 'Hume wrote the first draft of the Dialogues around 1750\u201351, revised them extensively in the 1760s, and made final revisions in 1776 shortly before his death. He initially intended to publish them in 1776 but was dissuaded by Adam Smith and others who feared the consequences for his reputation. He eventually entrusted the manuscript to his nephew David Hume the Younger with instructions to publish it after his death. The work appeared in 1779, three years after Hume\u2019s death, without a publisher\u2019s imprint.',
    relatedWorks: ['enquiry-human-understanding', 'natural-history-religion', 'enquiry-principles-morals', 'treatise-human-nature']
}

);
"""

# ── data-22d: Natural History of Religion + Essays ───────────────────────────
files['data-22d.js'] = r"""/* DATA PART 22d — Hume: Natural History of Religion + Essays */
window.WORKS.push(

{
    id: 'natural-history-religion',
    title: 'The Natural History of Religion',
    greekTitle: 'The Natural History of Religion',
    philosopher: 'hume',
    category: 'practical',
    categoryLabel: 'Philosophy of Religion',
    date: '1757 AD',
    dateSort: 1757,
    emoji: '\uD83C\uDFDB\uFE0F',
    cardSize: 'normal',
    readingDifficulty: 'Intermediate',
    estimatedWordCount: 30000,
    shortDesc: 'The founding text of the anthropology of religion \u2014 Hume\u2019s argument that polytheism preceded monotheism historically, that religion originates in fear and hope rather than rational contemplation, and that the history of religion is a history of corruption rather than progress.',
    summary: 'The Natural History of Religion, published in 1757 as part of Four Dissertations alongside \u201cOf the Passions,\u201d \u201cOf Tragedy,\u201d and \u201cOf the Standard of Taste,\u201d is Hume\u2019s philosophical anthropology of religious belief. Where the Dialogues Concerning Natural Religion address the logical and epistemological questions of natural theology (can reason establish the existence of God?), the Natural History addresses an entirely different question: what are the psychological and historical origins of religious belief in actual human beings?\n\nHume\u2019s central thesis overturns the conventional assumption of his day. The dominant view, shared by most Enlightenment thinkers, was that primitive religion was a corrupted form of original monotheism: humanity began with a natural recognition of one God and then degenerated into polytheism and superstition. Hume reverses this: polytheism and animism are the original, natural form of religion; monotheism is a later, secondary development. Primitive peoples, confronted with the unpredictable and threatening forces of nature \u2014 storms, floods, disease, death \u2014 personified them as spirits or gods who could be placated through ritual. The proliferation of such spirits produced polytheism. Monotheism arose not from philosophical reflection but from competitive flattery: worshippers praised their preferred deity above all others until he became supreme.\n\nThe work\u2019s most controversial claim is that the historical record shows no tendency of religion to progress toward rational purity. On the contrary: religions oscillate between polytheism (which is tolerant of other gods) and monotheism (which is intolerant and potentially violent), and the highest forms of monotheism \u2014 the reformed Protestant theology of Hume\u2019s own day \u2014 produce the greatest extremes of theological hair-splitting, intolerance, and persecution. The only consistent tendency is the corruption of originally simple beliefs by priestly interest, popular fear, and competitive theological exaggeration.',
    themes: ['the origin of religion in fear', 'polytheism before monotheism', 'the anthropology of religion', 'flattery and the rise of monotheism', 'religious intolerance', 'priestly corruption', 'superstition and enthusiasm'],
    keyCharacters: [],
    concepts: [
        'Religion from fear not reason \u2014 religious belief originates not in philosophical reflection on the order of nature but in the fear and hope produced by life\u2019s uncertainties',
        'Polytheism as the original form of religion \u2014 primitive peoples personified natural forces as spirits or gods; monotheism is a later development from competitive theological flattery',
        'The oscillation between polytheism and monotheism \u2014 religion tends to swing between the tolerant but irrational (polytheism) and the intolerant but more coherent (monotheism)',
        'Priestly corruption \u2014 organised religion consistently corrupts original simple beliefs through the competitive interest of religious specialists in elaborating doctrine and maintaining authority',
        'Superstition vs enthusiasm \u2014 superstition (fear-based, priestly, prone to elaborate ritual) and enthusiasm (emotion-based, anti-clerical, prone to fanaticism) are the two pathological forms of religion'
    ],
    structure: 'Introduction: The question of the historical origin of religion\nSections I\u2013IV: The origin of religion in polytheism; the personification of natural forces\nSections V\u2013VIII: The transition from polytheism to monotheism through flattery\nSections IX\u2013XI: The absurdities of popular religion; anthropomorphism\nSections XII\u2013XIV: The corruption of religion; the comparison of polytheism and theism\nSection XV: General corollary: the contradiction between popular religion and virtue',
    quote: 'The primary religion of mankind arises chiefly from an anxious fear of future events; and what ideas will naturally be entertained of invisible, unknown powers, while men lie under dismal apprehensions of any kind, may easily be conceived.',
    additionalQuotes: [
        { text: 'Survey most nations and most ages. Examine the religious principles, which have, in fact, prevailed in the world. You will scarcely be persuaded, that they are any thing but sick men\u2019s dreams.', citation: 'Natural History of Religion, Section XV' }
    ],
    commentary: [
        { philosopher: 'Emile Durkheim', text: 'Durkheim\u2019s The Elementary Forms of Religious Life (1912) is partly a response to Hume\u2019s Natural History. Durkheim rejected Hume\u2019s individualist psychology of religion (fear and hope in individual minds) in favour of a social account: religion is the symbolic expression of society\u2019s collective experience of its own power. But Durkheim\u2019s insistence on approaching religion empirically, without assuming its claims are literally true, is thoroughly Humean.' },
        { philosopher: 'J.C.A. Gaskin', text: 'Gaskin argues that the Natural History is philosophically underrated: its demonstration that the historical development of religion shows no tendency toward rationality or truth is a significant contribution to the epistemology of religious belief. If beliefs that are widely held and deeply felt can be fully explained by non-rational psychological and social causes, this gives us some reason to doubt their truth.' }
    ],
    modernRelevance: 'The Natural History of Religion is the founding text of the scientific and anthropological study of religion. Tylor\u2019s animism hypothesis, Frazer\u2019s evolutionary account of magic, religion, and science, Freud\u2019s account of religion as illusion, and contemporary cognitive science of religion (Boyer, Sperber, Atran) all develop Humean themes. The argument that religious belief is explained by natural psychological mechanisms rather than by the truth of its claims \u2014 the \u201cdebunking argument\u201d \u2014 is the central issue in contemporary evolutionary debunking arguments against religious and moral realism.',
    context: 'Published in 1757 as part of Four Dissertations. Hume had planned to include the Dissertations in a collection that also included two essays on suicide and the immortality of the soul, but he withdrew the latter two under pressure from friends and the threat of legal action. The Natural History is a more historically and anthropologically oriented work than either the Dialogues or the Enquiries, and reflects Hume\u2019s engagement with the emerging disciplines of history and comparative religion.',
    relatedWorks: ['dialogues-natural-religion', 'enquiry-human-understanding', 'history-of-england', 'essays-moral-political']
},

{
    id: 'essays-moral-political',
    title: 'Essays, Moral, Political, and Literary',
    greekTitle: 'Essays, Moral and Political',
    philosopher: 'hume',
    category: 'practical',
    categoryLabel: 'Political Philosophy & Literary Essays',
    date: '1741\u201342 AD',
    dateSort: 1741,
    emoji: '\uD83D\uDCDC',
    cardSize: 'normal',
    readingDifficulty: 'Beginner',
    estimatedWordCount: 150000,
    shortDesc: 'The essays that made Hume famous in his own lifetime \u2014 wide-ranging, elegant, and accessible reflections on commerce, liberty, taste, political parties, population, and the arts, establishing him as the foremost essayist of the Scottish Enlightenment and the model for all subsequent philosophical journalism.',
    summary: 'Essays, Moral and Political, first published in two volumes in 1741 and 1742 and subsequently expanded and revised throughout Hume\u2019s lifetime (reaching their final form in 1777), are the works that established Hume\u2019s contemporary reputation. While the Treatise had failed completely, the Essays were immediate successes, reaching a wide educated readership and going through multiple editions.\n\nThe Essays cover an extraordinary range of topics \u2014 political philosophy, economics, aesthetics, moral psychology, literary criticism, political theory, and the philosophy of history \u2014 in a style that is always elegant, often witty, and never merely academic. Hume intended them for the educated general reader and wrote with the explicit aim of building a bridge between the \u201clearned world\u201d and the \u201cconversable world\u201d \u2014 between the professionals and the general educated public.\n\nThe political essays include \u201cOf the Original Contract\u201d (a critique of social contract theory: actual political authority rests on consent in no meaningful sense; most people have never been asked to consent and cannot emigrate even if they object), \u201cOf Civil Liberty\u201d (a comparison of republican and monarchical government), \u201cOf the First Principles of Government\u201d (opinion, not force, is the ultimate foundation of all government), and \u201cOf the Independency of Parliament\u201d.\n\nThe economic essays \u2014 which directly influenced Adam Smith \u2014 include \u201cOf Commerce,\u201d \u201cOf Refinement in the Arts,\u201d \u201cOf Money,\u201d \u201cOf Interest,\u201d \u201cOf the Balance of Trade,\u201d and \u201cOf the Jealousy of Trade.\u201d Hume argues against mercantilism, defends the benefits of luxury consumption, and anticipates the quantity theory of money.\n\nThe aesthetic essays include \u201cOf the Standard of Taste\u201d \u2014 discussed as a separate work below \u2014 and \u201cOf Tragedy,\u201d which analyses the paradox of why we enjoy representations of painful events.',
    themes: ['political philosophy', 'economics and commerce', 'taste and aesthetics', 'the balance of trade', 'the foundations of political authority', 'the social contract', 'luxury and refinement', 'the relationship of learning and politeness', 'political parties'],
    keyCharacters: [],
    concepts: [
        'Opinion as the foundation of government \u2014 all governments, however despotic, ultimately rest on the opinion of the governed; force alone cannot sustain authority',
        'The critique of social contract theory \u2014 actual political authority rests on consent in no meaningful sense; historical foundations are conquest and usurpation; tacit consent is a fiction',
        'The benefits of commerce and luxury \u2014 contrary to classical republican moralism, commercial society and luxury consumption promote industry, refinement of arts and sciences, and political liberty',
        'The quantity theory of money \u2014 increases in the money supply raise prices proportionally; what matters for trade is relative not absolute prices; mercantilist accumulation of gold is pointless',
        'The learned and conversable worlds \u2014 philosophy should bridge the gap between academic specialists and educated general readers; Hume\u2019s model of the philosophical essayist'
    ],
    structure: 'The Essays went through many editions (1741, 1742, 1748, 1752, 1758, 1760, 1770, 1777). The main groupings in the final edition:\n\nMoral and Literary Essays: Of the Delicacy of Taste and Passion; Of the Liberty of the Press; Of Impudence and Modesty; Of Love and Marriage; Of the Study of History; Of Essay Writing; Of Eloquence; Of Moral Prejudices\n\nPolitical Essays: Of the First Principles of Government; Of the Origin of Government; Of the Original Contract; Of Passive Obedience; Of the Coalition of Parties; Of Civil Liberty; Of the Rise and Progress of the Arts and Sciences\n\nEconomic Essays (from Political Discourses, 1752): Of Commerce; Of Refinement in the Arts; Of Money; Of Interest; Of the Balance of Trade; Of the Balance of Power; Of Taxes; Of Public Credit; Of the Jealousy of Trade; Of the Populousness of Ancient Nations',
    quote: 'Nothing appears more surprising to those who consider human affairs with a philosophical eye, than the easiness with which the many are governed by the few; and the implicit submission, with which men resign their own sentiments and passions to those of their rulers.',
    additionalQuotes: [
        { text: 'Avarice, the spur of industry, is so obstinate a passion, and works its way through so many real dangers and difficulties, that it is not likely to be scared by an imaginary danger.', citation: 'Of the Balance of Trade' },
        { text: 'The ages of greatest public spirit are not always most eminent for private virtue.', citation: 'Of Civil Liberty' }
    ],
    commentary: [
        { philosopher: 'Adam Smith', text: 'Adam Smith\u2019s Wealth of Nations (1776) is deeply indebted to Hume\u2019s economic essays. Hume\u2019s critique of mercantilism, his quantity theory of money, and his account of the relationship between commerce and liberty provided the empirical and analytical framework that Smith developed into a systematic political economy. Smith described Hume as \u201cby far the most illustrious philosopher and historian of the present age.\u201d' },
        { philosopher: 'Eugene Miller', text: 'Miller\u2019s scholarly edition of the Essays (Liberty Fund, 1985; 1987) established the definitive text and traced the revisions through the many editions of Hume\u2019s lifetime. Miller argues that the Essays represent Hume\u2019s most important contribution to political philosophy and that their relative neglect in favour of the Treatise and the Enquiries has distorted understanding of his thought.' }
    ],
    modernRelevance: 'The political and economic essays are primary documents in the history of liberalism, commercial society, and classical economics. \u201cOf the Balance of Trade\u201d is cited by economists as an early statement of the price-specie-flow mechanism. \u201cOf the Original Contract\u201d is a standard text in the critique of consent theory and the philosophy of political obligation. The essay model Hume developed \u2014 accessible, elegant philosophical writing for a general audience \u2014 is the template for the genre of the intellectual essay from Hazlitt and Lamb through Orwell and Baldwin to contemporary public philosophy.',
    context: 'First published in two volumes in Edinburgh in 1741 and 1742 by A. Kincaid. Immediately successful: the first edition sold out quickly and a second edition appeared within months. Hume expanded and revised the Essays throughout his career, adding the Political Discourses (1752, which included the economic essays) and incorporating them into successive collected editions. He removed some essays as beneath his mature standards and revised others extensively. The final authoritative edition appeared in 1777, the year after his death.',
    relatedWorks: ['enquiry-principles-morals', 'history-of-england', 'natural-history-religion']
}

);
"""

# ── data-22e: History of England + Standard of Taste + My Own Life ───────────
files['data-22e.js'] = r"""/* DATA PART 22e — Hume: History of England + Of the Standard of Taste + My Own Life */
window.WORKS.push(

{
    id: 'history-of-england',
    title: 'The History of England',
    greekTitle: 'The History of England, from the Invasion of Julius Caesar to the Revolution of 1688',
    philosopher: 'hume',
    category: 'practical',
    categoryLabel: 'Philosophy of History',
    date: '1754\u201361 AD',
    dateSort: 1754,
    emoji: '\uD83C\uDFF0',
    cardSize: 'normal',
    readingDifficulty: 'Intermediate',
    estimatedWordCount: 1200000,
    shortDesc: 'The work that made Hume the most widely read historian in Britain for a century \u2014 six volumes covering English history from Julius Caesar to 1688, written with philosophical detachment and narrative elegance, and advancing the thesis that the liberties of the English constitution were the product of gradual historical development, not ancient custom.',
    summary: 'The History of England, from the Invasion of Julius Caesar to the Revolution in 1688, published in six volumes between 1754 and 1762, was the most commercially successful of all Hume\u2019s works and the one that gave him financial independence and contemporary celebrity. It went through approximately 175 editions by 1900 and was the standard English history for over a century.\n\nHume began with the Stuarts (published 1754\u201357) \u2014 the most controversial period because of the constitutional conflicts between Crown and Parliament \u2014 then worked backwards to the Tudors (1759) and then to the medieval period and Roman invasion (1761). This reverse chronological order reflects his philosophical strategy: by beginning with the most contested period, he could establish his impartial, non-partisan perspective before treating the less contentious earlier history.\n\nThe History\u2019s central philosophical argument is against the Whig myth of the ancient constitution. The dominant Whig history of England maintained that the liberties and constitutional rights of Englishmen derived from immemorial custom \u2014 that the common law, parliamentary government, and individual liberties had existed from time immemorial and had been periodically violated by tyrannical kings and subsequently recovered. Hume systematically demolishes this myth: the common law was not ancient but Norman; Parliament was not a check on royal power but an instrument of it until the seventeenth century; the constitutional liberties of 1688 were the product of specific historical struggles, not the recovery of primordial rights.\n\nHume approaches history with the same sceptical, naturalistic method he applies to philosophy. He looks for general causes \u2014 economic interests, religious passions, constitutional structures, the pressures of war and commerce \u2014 rather than the providential designs of God or the heroic agency of individual rulers. His treatment of the Civil War and the execution of Charles I is particularly remarkable for its even-handedness: he refuses to condemn Charles as a tyrant or the Parliamentarians as traitors, analysing the conflict as the result of structural tensions in the English constitution that neither side fully understood.',
    themes: ['the Whig myth of the ancient constitution', 'historical causation', 'political liberty and its development', 'the Stuart period', 'the English Civil War', 'impartiality in historical narrative', 'religion and politics', 'the philosophical historian'],
    keyCharacters: [
        { name: 'Charles I', role: 'The central figure of the most contested section of the History; Hume treats him with unusual sympathy and analyses his execution as a constitutional catastrophe rather than a justified removal of a tyrant' }
    ],
    concepts: [
        'The philosophical historian \u2014 the historian who applies systematic analysis of causes rather than mere narrative of events; who seeks general principles governing historical change',
        'Against the ancient constitution \u2014 the Whig myth that English liberties derive from immemorial custom is historically false; constitutional rights were fought for and established in specific historical conflicts',
        'Impartiality as a historical virtue \u2014 the historian must resist the temptation to write Whig or Tory history; both parties in every constitutional struggle had legitimate claims and genuine interests',
        'Religion as a cause of historical disruption \u2014 religious enthusiasm (Puritanism in the Civil War, Catholicism in the Stuart period) is a primary source of political instability',
        'Commerce and liberty \u2014 the development of commercial society gradually produces the material conditions and cultural habits that support constitutional liberty'
    ],
    structure: 'Volume I (1761): From Julius Caesar to the Norman Conquest\nVolume II (1761): From William the Conqueror to the death of Henry V\nVolume III (1759): From Henry VI to the death of Henry VIII (Tudors, Part I)\nVolume IV (1759): From Edward VI to the death of Elizabeth I (Tudors, Part II)\nVolume V (1754): From James I to the death of Charles I (Stuarts, Part I)\nVolume VI (1757): From the Commonwealth to the Revolution of 1688 (Stuarts, Part II)',
    quote: 'So absolute was the authority of the crown, and so little jealous were the people of public liberty, that, had the English constitution been at that time fixed and ascertained, there is reason to think that it might have been confirmed forever in a condition little better than despotism.',
    additionalQuotes: [
        { text: 'The first page of Thucydides is, in my opinion, the commencement of real history.', citation: 'Quoted in Adam Smith\u2019s letter on Hume\u2019s death' }
    ],
    commentary: [
        { philosopher: 'Edward Gibbon', text: 'Gibbon described Hume as the model philosophical historian and acknowledged the History of England as a primary influence on the Decline and Fall of the Roman Empire (1776\u201388). Gibbon\u2019s application of Enlightenment scepticism to religious history \u2014 treating Christianity as a historical phenomenon with natural causes \u2014 is thoroughly Humean in method.' },
        { philosopher: 'Duncan Forbes', text: 'Forbes\u2019 Hume\u2019s Philosophical Politics (1975) argues that the History of England is not a detour from Hume\u2019s philosophical work but its completion: the history is the empirical testing ground for the political philosophy of the Essays, showing what actually promotes liberty, stability, and commercial prosperity in historical practice.' }
    ],
    modernRelevance: 'The History of England is primarily of historical and historiographical interest. Its methodological innovations \u2014 the application of sociological and economic analysis to political history, the critique of nationalist mythology, the insistence on impartiality \u2014 established standards that transformed historical writing. Hume\u2019s critique of the ancient constitution myth was a direct influence on later constitutional historians. The History is also a literary achievement: its prose style was widely admired and extensively imitated.',
    context: 'Published in six volumes between 1754 and 1762 by Andrew Millar in London. The first volume (on the Stuarts) provoked immediate political controversy: Tories accused Hume of Whig bias; Whigs accused him of Tory apologetics. Both accusations reflected the work\u2019s genuine impartiality. The History made Hume wealthy \u2014 he earned over \u00a33,000 from it \u2014 and famous throughout Europe. Voltaire praised it extravagantly.',
    relatedWorks: ['essays-moral-political', 'natural-history-religion', 'my-own-life']
},

{
    id: 'of-the-standard-of-taste',
    title: 'Of the Standard of Taste',
    greekTitle: 'Of the Standard of Taste',
    philosopher: 'hume',
    category: 'aesthetics',
    categoryLabel: 'Aesthetics',
    date: '1757 AD',
    dateSort: 1757,
    emoji: '\uD83C\uDFA8',
    cardSize: 'normal',
    readingDifficulty: 'Beginner',
    estimatedWordCount: 8000,
    shortDesc: 'The most elegant short essay in the history of aesthetics \u2014 Hume\u2019s attempt to resolve the apparent contradiction between the subjectivity of taste and the genuine critical distinctions we draw between Homer and a bad poet, navigating between relativism and false objectivism.',
    summary: 'Of the Standard of Taste, published in 1757 as part of Four Dissertations, is Hume\u2019s most celebrated short essay and one of the most influential texts in the history of aesthetics. It addresses what Hume recognises as a genuine puzzle: on the one hand, taste seems entirely subjective (\u201cthere is no disputing about taste\u201d); on the other hand, we genuinely believe that Homer is a better poet than a mediocre versifier, and that this is not merely a matter of personal preference.\n\nHume\u2019s solution is empirical rather than metaphysical. There is no Platonic Form of Beauty that the true critic perceives. But there is a standard of taste grounded in the convergent responses of qualified judges \u2014 those who combine delicacy of taste (the perceptual sensitivity to fine distinctions), practice (extensive acquaintance with works in the relevant form), comparison (exposure to works of different kinds and periods), freedom from prejudice (the ability to consider works on their own terms rather than through the distorting lens of personal association), and good sense (the rational capacity to evaluate the relations between a work\u2019s parts and its overall effect).\n\nThe qualified critic is not simply the person who likes certain things; she is the person whose responses are reliable indicators of genuine aesthetic quality \u2014 whose approval tracks the properties in works that produce enduring, reflectively stable pleasure in sensitive audiences. The standard of taste is therefore intersubjective and empirically grounded rather than either purely subjective or metaphysically objective.\n\nHume acknowledges two legitimate sources of variation in taste: differences in temperament that make certain works suit some people better than others, and differences in cultural context that make it difficult to appreciate works produced in alien traditions. But he insists that these sources of variation are compatible with the existence of genuine critical standards.',
    themes: ['the standard of taste', 'the qualified critic', 'delicacy of taste', 'subjectivity and objectivity in aesthetics', 'the paradox of enduring reputation', 'cultural variation in taste', 'the ideal judge'],
    keyCharacters: [],
    concepts: [
        'The standard of taste \u2014 not a metaphysical absolute but the convergent responses of qualified judges; empirically grounded and intersubjective rather than purely subjective or Platonic',
        'Delicacy of taste \u2014 the perceptual sensitivity to fine distinctions in a work; the capacity to be affected by the subtle features that distinguish great from mediocre art',
        'The qualified critic \u2014 the person who combines delicacy of taste, practice, comparison, freedom from prejudice, and good sense; their approval is a reliable indicator of aesthetic quality',
        'Enduring reputation as evidence of quality \u2014 the works that survive centuries of critical examination and continue to please sensitive audiences across cultures provide empirical evidence of genuine aesthetic merit',
        'Cultural variation vs genuine disagreement \u2014 variation in taste due to temperament and cultural context is legitimate; variation due to ignorance, prejudice, or lack of sensitivity is not'
    ],
    structure: 'A single continuous essay:\n\u2014 The apparent conflict: taste seems subjective, yet we make genuine critical distinctions\n\u2014 The solution: qualified critics as the standard\n\u2014 The qualities of the qualified critic: delicacy, practice, comparison, freedom from prejudice, good sense\n\u2014 The test of enduring reputation\n\u2014 Two legitimate sources of variation in taste\n\u2014 The persistence of genuine disagreement and its limits',
    quote: 'Strong sense, united to delicate sentiment, improved by practice, perfected by comparison, and cleared of all prejudice, can alone entitle critics to this valuable character; and the joint verdict of such, wherever they are to be found, is the true standard of taste and beauty.',
    additionalQuotes: [
        { text: 'Beauty is no quality in things themselves: it exists merely in the mind which contemplates them; and each mind perceives a different beauty.', citation: 'Of the Standard of Taste' }
    ],
    commentary: [
        { philosopher: 'Immanuel Kant', text: 'Kant\u2019s Critique of the Power of Judgment (1790) is in large part a response to Hume\u2019s essay. Kant agreed that judgments of taste are neither purely subjective (they claim universal agreement) nor grounded in a determinate concept (they cannot be argued about in the ordinary way). But he argued that Hume\u2019s solution \u2014 grounding the standard in qualified critics \u2014 is insufficient: it makes aesthetic value empirically contingent when it ought to be necessary. Kant\u2019s account of the \u201cfree play of imagination and understanding\u201d as the ground of aesthetic judgment is his alternative to Hume\u2019s empirical standard.' },
        { philosopher: 'Nick Zangwill', text: 'Contemporary debates about aesthetic realism and anti-realism frequently cite Hume\u2019s essay as the founding statement of the \u201cresponse-dependence\u201d theory of aesthetic properties: aesthetic properties are constituted by the responses of qualified appreciators rather than being mind-independent features of objects.' }
    ],
    modernRelevance: 'Of the Standard of Taste remains one of the most frequently cited texts in aesthetics. The response-dependence theory of aesthetic properties, the concept of the ideal critic, and the question of how aesthetic judgment can be both subjective and genuinely evaluative are central issues in contemporary aesthetics, and all are framed in terms derived from Hume\u2019s essay. The essay also anticipates contemporary discussions of expertise, calibration, and the epistemology of aesthetic judgment.',
    context: 'Published in London in 1757 as one of Four Dissertations. Hume had planned to include essays on suicide and the immortality of the soul in the same collection but withdrew them under pressure. \u201cOf the Standard of Taste\u201d was a late replacement. Despite its brevity, it has proved the most philosophically durable of all Hume\u2019s essays on aesthetics.',
    relatedWorks: ['essays-moral-political', 'enquiry-principles-morals', 'treatise-human-nature']
},

{
    id: 'my-own-life',
    title: 'My Own Life',
    greekTitle: 'My Own Life',
    philosopher: 'hume',
    category: 'method',
    categoryLabel: 'Philosophical Autobiography',
    date: '1776 AD',
    dateSort: 1776,
    emoji: '\u2712\uFE0F',
    cardSize: 'normal',
    readingDifficulty: 'Beginner',
    estimatedWordCount: 3000,
    shortDesc: 'Five pages written months before death \u2014 Hume\u2019s account of his own character, his literary career, and his final weeks, remarkable for its tranquillity and its complete absence of religious consolation, which made it one of the most controversial documents of the Enlightenment.',
    summary: 'My Own Life, written by Hume on 18 April 1776 \u2014 four months before his death from intestinal cancer on 25 August 1776 \u2014 and published posthumously by Adam Smith (who appended a letter describing Hume\u2019s final weeks), is the most celebrated philosophical deathbed document since Socrates. Its celebrity derives from what it lacks: any expression of fear, regret, or religious hope in the face of death.\n\nThe document is brief \u2014 fewer than three thousand words \u2014 and covers Hume\u2019s life with characteristic economy and self-knowledge. He describes his early passion for literature and philosophy, the composition and failure of the Treatise, the success of the Essays, the controversial History of England, the diplomatic career in Paris (1763\u201366), and his final years in Edinburgh. His characterisation of his own temperament \u2014 \u201ca man of mild dispositions, of command of temper, of an open, social, and cheerful humour, capable of attachment, but little susceptible of enmity, and of great moderation in all my passions\u201d \u2014 was confirmed by all who knew him.\n\nThe most celebrated passage is the final one, in which Hume describes his present state of health and his equanimity in the face of approaching death. He does not reach for consolation; he notes that he is dying and that he has no complaints. When James Boswell visited him in July 1776, hoping to catch the great infidel philosopher recanting on his deathbed, Hume told him that he saw no more reason to fear death than he had ever had, that the immortality of the soul was a most unreasonable fancy, and that he was very well entertained with his life as it had been.\n\nAdam Smith\u2019s letter, appended to the published version, describes Hume\u2019s final weeks with affection and admiration: \u201cUpon the whole, I have always considered him, both in his lifetime and since his death, as approaching as nearly to the idea of a perfectly wise and virtuous man, as perhaps the nature of human frailty will permit.\u201d',
    themes: ['the philosopher\u2019s death', 'tranquillity in the face of mortality', 'philosophical autobiography', 'the literary career', 'Enlightenment irreligion', 'the character of the philosopher', 'equanimity'],
    keyCharacters: [
        { name: 'Adam Smith', role: 'Hume\u2019s closest friend and intellectual companion; his appended letter describing Hume\u2019s final weeks was published alongside My Own Life and provoked nearly as much controversy as the autobiography itself' }
    ],
    concepts: [
        'Philosophical equanimity \u2014 the capacity to face death without fear, consolation, or regret; the attitude Hume maintained in his final months and which scandalised religious contemporaries',
        'The literary temperament \u2014 Hume\u2019s self-characterisation as primarily a man of letters motivated by love of literary fame rather than by philosophical ambition or religious vocation',
        'The failure and success of the philosophical career \u2014 the Treatise fell dead-born from the press; the Essays succeeded; the History made him wealthy; the philosophical works gained recognition only late'
    ],
    structure: 'A brief autobiography of approximately 3,000 words:\n\u2014 Birth, education, and early passion for literature\n\u2014 The Treatise and its failure\n\u2014 The Essays and their success\n\u2014 The political career and the History of England\n\u2014 The diplomatic career in Paris\n\u2014 Return to Edinburgh; the final works\n\u2014 The present state: approaching death with equanimity\n\nAppended letter from Adam Smith to William Strahan, describing Hume\u2019s final weeks',
    quote: 'I was, I say, a man of mild dispositions, of command of temper, of an open, social, and cheerful humour, capable of attachment, but little susceptible of enmity, and of great moderation in all my passions.',
    additionalQuotes: [
        { text: 'Never literary attempt was more unfortunate than my Treatise of Human Nature. It fell dead-born from the press, without reaching such distinction, as even to excite a murmur among the zealots.', citation: 'My Own Life' },
        { text: 'Upon the whole, I have always considered him, both in his lifetime and since his death, as approaching as nearly to the idea of a perfectly wise and virtuous man, as perhaps the nature of human frailty will admit.', citation: 'Adam Smith, appended letter on Hume\u2019s death' }
    ],
    commentary: [
        { philosopher: 'James Boswell', text: 'Boswell\u2019s account of his visit to the dying Hume (July 1776) \u2014 preserved in Boswell\u2019s Private Papers and published in the twentieth century \u2014 is the most revealing document of Hume\u2019s death. Boswell came hoping for a deathbed conversion and found instead complete philosophical tranquillity. Hume told him that the immortality of the soul was a most unreasonable fancy, that he had no more concern about his annihilation than about the time before he was born, and that he felt no anxiety at the prospect of non-existence.' },
        { philosopher: 'Ernest Mossner', text: 'Mossner\u2019s biography The Life of David Hume (1954; 2nd ed. 1980) is the standard scholarly biography. Mossner argues that My Own Life and the surrounding documents of Hume\u2019s death \u2014 Smith\u2019s letter, Boswell\u2019s account, the correspondence of the final months \u2014 constitute one of the most remarkable records of philosophical dying in any language: the Epicurean ideal of dying well, achieved without Epicurean religion.' }
    ],
    modernRelevance: 'My Own Life and the surrounding documents of Hume\u2019s death have become iconic in the secular and humanist tradition. The image of the philosopher dying calmly and without religious consolation \u2014 demonstrating in practice the equanimity his philosophy advocated in theory \u2014 has been cited by everyone from Bertrand Russell to contemporary advocates of secular ethics as evidence that a good life is possible without religious belief. The document is also important for understanding Hume\u2019s self-conception: he understood himself primarily as a man of letters rather than as a systematic philosopher.',
    context: 'Written on 18 April 1776, four months before Hume\u2019s death on 25 August 1776. Published posthumously in 1777, with an appended letter from Adam Smith to William Strahan (Hume\u2019s publisher) describing Hume\u2019s final weeks. The publication provoked an immediate controversy: religious commentators attacked Smith for praising an atheist as a virtuous man; Smith responded that he stood by every word.',
    relatedWorks: ['treatise-human-nature', 'dialogues-natural-religion', 'history-of-england', 'essays-moral-political']
}

);
"""

# Write all files
for fname, content in files.items():
    path = os.path.join(js, fname)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'  Written {fname}  ({content.count(chr(10))} lines)')

print('\nVerify:')
print('  node -e "var w={WORKS:[]};var fs=require(\'fs\');[\'22a\',\'22b\',\'22c\',\'22d\',\'22e\'].forEach(f=>{eval(fs.readFileSync(\'js/data-\'+f+\'.js\',\'utf8\').replace(/window\\./g,\'w.\'))});console.log(\'works:\',w.WORKS.length,w.WORKS.map(x=>x.id))"')
