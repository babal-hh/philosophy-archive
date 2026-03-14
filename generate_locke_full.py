#!/usr/bin/env python3
"""
Run from inside ~/Desktop/philosophy-archive/
  python3 generate_locke_full.py
Writes js/data-14a.js through js/data-14e.js
"""
import os

js_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'js')
os.makedirs(js_dir, exist_ok=True)

# ─────────────────────────────────────────────────────────────────────────────
# DATA-14a  —  Essay Concerning Human Understanding
# ─────────────────────────────────────────────────────────────────────────────
data_14a = r"""/* ================================================================
   DATA PART 14a — Essay Concerning Human Understanding (Locke)
   ================================================================ */

window.WORKS.push(

/* ──────────────────────────────────────
   1. AN ESSAY CONCERNING HUMAN UNDERSTANDING
────────────────────────────────────── */
{
    id: 'essay-concerning-human-understanding',
    title: 'An Essay Concerning Human Understanding',
    greekTitle: 'An Essay Concerning Human Understanding',
    philosopher: 'locke',
    category: 'epistemology',
    categoryLabel: 'Epistemology',
    date: '1689 AD',
    dateSort: 1689,
    emoji: '🕯',
    cardSize: 'wide',
    readingDifficulty: 'Advanced',
    estimatedWordCount: 340000,

    shortDesc: 'The founding document of British empiricism — Locke\'s systematic investigation into the origin, extent, and limits of human knowledge, and the most consequential work in the English philosophical tradition.',

    summary: 'The Essay Concerning Human Understanding is one of the great founding documents of modern philosophy. Locke spent nearly twenty years composing it, beginning from a conversation held in 1671 with a small circle of friends — probably including the physician Thomas Sydenham and the statesman Anthony Ashley Cooper — in which the group found themselves unable to make progress on questions of morality and religion. The obstacle, Locke concluded, was that they had not first examined their own capacities. Before asking what we can know, we must ask how we come to know anything at all. This therapeutic ambition — clearing the ground before building — shapes every page of the Essay.\n\nBook I is a systematic demolition of the doctrine of innate ideas. Against Descartes and the scholastic tradition, Locke argues that there are no ideas or principles stamped upon the mind at birth. The principal argument is from the absence of universal assent: if a proposition were truly innate, all human beings would recognize it immediately upon the use of reason. But there is no such universal assent to any moral, logical, or metaphysical principle — children, idiots, and inhabitants of remote countries are ignorant of the most celebrated first principles of European philosophy. Even if some candidates for innateness were universally assented to, that assent would be explained more economically by their evident truth to reason than by any prenatal impression. The critique clears the space for Locke\'s constructive account.\n\nBook II, the longest and philosophically richest section, argues that the mind at birth is white paper, void of all characters, without any ideas. Every idea we possess derives from experience, which presents itself in two forms. Sensation furnishes the mind with simple ideas of qualities perceived through the five senses — yellow, cold, soft, bitter, the smell of a rose. Reflection furnishes simple ideas of the mind\'s own operations — thinking, doubting, believing, willing, knowing. These simple ideas are the irreducible atoms of Lockean epistemology: the mind is entirely passive in receiving them and cannot create or destroy them, only combine and compare them. Complex ideas are built from simple ones through three operations: combination, comparison, and abstraction.\n\nThe most influential doctrine of Book II is the distinction between primary and secondary qualities. Primary qualities — solidity, extension, figure, motion or rest, and number — are powers in bodies that produce ideas in us which resemble the qualities themselves. The idea of a spherical shape produced in my mind by a billiard ball resembles a real quality in the ball. Secondary qualities — color, sound, taste, smell, warmth and cold — are merely powers in objects to produce ideas in us that bear no resemblance to anything in the objects themselves. The redness of the rose is not in the rose as it appears in my perception; it is a power in the rose\'s microscopic surface structure to affect the visual system in a way that produces the experience of red. This distinction, rooted in the corpuscularian natural philosophy of Robert Boyle and the mechanics of Newton, set the terms of philosophy of perception for the following three centuries. It also inaugurated the skeptical problems that Berkeley and Hume would develop: if my ideas of secondary qualities do not resemble their causes, how can I be confident that my ideas of primary qualities do?\n\nBook II also contains Locke\'s celebrated analysis of personal identity as consisting not in the identity of substance — neither bodily nor mental — but in the continuity of consciousness and memory. A person at time T2 is the same person as a person at time T1 if and only if the person at T2 can remember the experiences of the person at T1. This psychological criterion of personal identity, advanced in opposition to both Cartesian soul-substance views and materialist body-identity views, became the starting point of the entire modern discussion of personal identity and remains central to debates about survival, punishment, and moral responsibility.\n\nBook III turns to language — one of the earliest systematic treatments of the philosophy of language in Western philosophy. Locke argues that words are signs of ideas in the mind of the speaker, not directly of things in the world. General terms function by standing for abstract general ideas formed by stripping away the particulars that distinguish individual members of a kind. A crucial innovation is the distinction between nominal essence and real essence. The nominal essence of gold is the collection of observable properties — yellowness, malleability, fusibility, solubility in aqua regia — that we use to apply the word \'gold.\' The real essence is the unknown microscopic constitution of the particles of gold that produces these observable properties. We never know real essences; all our classifications are by nominal essence. This anticipates the Kripke-Putnam revolution in philosophy of language and directly raises questions about whether scientific kinds cut nature at its joints.\n\nBook IV defines knowledge as the perception of the agreement or disagreement between ideas. There are four degrees: intuitive knowledge (directly perceived, the most certain — that white is not black, that a circle is not a triangle), demonstrative knowledge (established through intervening ideas — mathematics, Locke\'s proof of God\'s existence), sensitive knowledge (of the existence of particular external things, the most uncertain), and judgment or opinion (probable beliefs that fall short of knowledge). This framework establishes that genuine knowledge is far narrower than everyday confident belief: we know very little, and we must for most practical purposes rely on probability and rational judgment rather than certainty.',

    themes: ['Empiricism', 'Origin of Ideas', 'Sensation and Reflection', 'Primary and Secondary Qualities', 'Substance', 'Personal Identity', 'Language and Meaning', 'Degrees of Knowledge', 'Critique of Innatism', 'Nominal vs Real Essence', 'Probability and Judgment'],

    keyCharacters: [
        { name: 'Locke', role: 'Sole author and implied interlocutor with the scholastic and Cartesian traditions he is systematically dismantling' },
        { name: 'Descartes', role: 'The principal target of Book I — his doctrine of innate ideas is the main thesis Locke undertakes to refute, though Descartes is never named in the text' }
    ],

    concepts: [
        'Tabula rasa — the mind at birth is white paper, void of all characters, without any ideas; all content comes from experience',
        'Sensation and reflection — the two and only sources of ideas; sensation furnishes ideas of external qualities, reflection of the mind\'s own operations',
        'Simple and complex ideas — simple ideas are received passively and cannot be created or destroyed; complex ideas are built by the mind from simples',
        'Primary qualities — solidity, extension, figure, motion, number — intrinsic to bodies; their ideas resemble the qualities themselves',
        'Secondary qualities — color, sound, taste, smell, warmth — powers in bodies to produce ideas bearing no resemblance to the bodies',
        'Substance as unknown substratum — we posit substance as the support of qualities but have no determinate idea of it in itself',
        'Personal identity as continuity of consciousness — the same person through time is constituted by the reach of memory, not by sameness of body or soul',
        'Nominal essence vs real essence — our classificatory terms track observable clusters of properties, not the unknown inner constitutions of things',
        'Knowledge as perception of agreement between ideas — strictly limited to intuitive, demonstrative, and sensitive knowledge',
        'Probability as the guide of life — in the vast domain where knowledge is unavailable, rational belief weighs evidence and testimony',
        'Abuse of words — the principal source of philosophical darkness: equivocation, obscure terms, treating words as if they named things rather than ideas'
    ],

    structure: 'Book I (4 chapters): Neither Principles Nor Ideas Are Innate. Demolition of innate speculative principles, innate practical principles, and innate ideas including the idea of God.\n\nBook II (33 chapters): Of Ideas. The two sources of ideas; simple ideas of sensation and reflection; the great divisions — space, time, power, infinity, substance, modes, relations; the distinction between primary and secondary qualities; the idea of substance and its problems; personal identity; the association of ideas.\n\nBook III (11 chapters): Of Words. Words as signs of ideas; general terms and abstract ideas; names of simple ideas, substances, and modes; the imperfection and abuse of language; the remedy.\n\nBook IV (21 chapters): Of Knowledge and Opinion. The four degrees of knowledge; intuition, demonstration, sensitive knowledge; the existence of God; the extent of human knowledge; judgment and opinion; probability; the degrees of assent; reason, faith, and enthusiasm.',

    quote: 'Let us then suppose the mind to be, as we say, white paper, void of all characters, without any ideas: how comes it to be furnished? Whence has it all the materials of reason and knowledge? To this I answer, in one word, from experience. — Essay, Book II, Chapter 1',

    additionalQuotes: [
        { text: 'Since the mind, in all its thoughts and reasonings, hath no other immediate object but its own ideas, it is evident that our knowledge is only conversant about them.', citation: 'Essay, Book IV, Chapter 1' },
        { text: 'The candle that is set up in us shines bright enough for all our purposes. The discoveries we can make with this ought to satisfy us; and we shall then use our understandings right, when we entertain all objects in that way and proportion that they are suited to our faculties.', citation: 'Essay, Book I, Chapter 1' },
        { text: 'General and universal belong not to the real existence of things; but are the inventions and creatures of the understanding, made by it for its own use, and concern only signs, whether words or ideas.', citation: 'Essay, Book III, Chapter 3' },
        { text: 'Our faculties are not fitted to penetrate into the internal fabric and real essences of bodies; and their several constitutions, on which their properties depend, are concealed from us.', citation: 'Essay, Book IV, Chapter 3' }
    ],

    commentary: [
        {
            philosopher: 'G.W. Leibniz',
            text: 'Leibniz spent years composing a point-by-point response to the Essay in his New Essays on Human Understanding (completed c.1705, published 1765), a work of extraordinary philosophical ambition that restores innatism through a subtle modification. Against Locke\'s tabula rasa, Leibniz argues: nothing is in the intellect that was not first in the senses, except the intellect itself. The mind does not receive simple ideas passively but actively structures experience according to principles it possesses by its own nature — the principles of identity, of sufficient reason, of necessary connection. Mathematical and logical truths are innate not as conscious memories but as dispositions, tendencies, habits, or virtual knowledge — like the veins in a block of marble that predispose it to yield one figure rather than another when the sculptor\'s chisel falls. Leibniz also objects to Locke\'s account of ideas as images or representations derived from sensory impressions: necessary truths (the truths of mathematics and logic) cannot be derived from experience, which furnishes nothing but particular contingent facts, and their absolute universality and necessity requires an a priori foundation that Locke\'s empiricism cannot supply.'
        },
        {
            philosopher: 'David Hume',
            text: 'Hume acknowledged Locke as the father of modern epistemology and the inaugurator of the empiricist tradition he himself inherited and radicalized. In the Treatise of Human Nature (1739), Hume pushed Locke\'s principles to conclusions Locke had drawn back from. Where Locke had posited material substance as the unknown support of qualities and spiritual substance as the self, Hume applied the empiricist test: show me the impression from which the idea of substance is derived. He could find none. The idea of material substance, as Locke himself admitted, is the idea of an unknown something-we-know-not-what — and Hume concluded that it is therefore meaningless. More devastatingly, the same critique applies to the idea of causation: we have no impression of necessary connection between cause and effect, only of constant conjunction. Hume also pressed Locke\'s personal identity theory to its logical terminus: examining his own consciousness, he found not a continuous self but a bundle of perceptions succeeding one another with no connecting thread of identity. Locke\'s empiricism, Hume showed, leads directly to a scepticism Locke himself had not intended.'
        },
        {
            philosopher: 'Immanuel Kant',
            text: 'Kant described Locke as having attempted a physiology of the human understanding — a natural history of the origins of our cognitive acquisitions — rather than a critical examination of their validity. The distinction is decisive. Locke asks where our ideas come from; Kant asks whether and how they can constitute genuine knowledge of reality. Reading Hume\'s radicalization of Locke, Kant reports being awakened from his dogmatic slumber: the question Hume posed — how can we be justified in projecting our habitual associations (like causality) onto nature — convinced Kant that neither dogmatic rationalism nor empiricism could provide an adequate epistemology. His Critique of Pure Reason (1781) provides the answer: we have genuine a priori knowledge not because the mind contains Leibniz\'s innate truths but because the mind imposes its own structural forms (space, time, the categories of understanding) upon sensory experience. Kant called this the Copernican revolution in philosophy: instead of the mind conforming to objects, objects must conform to the mind\'s constitutive structures. This is neither Locke\'s empiricism nor Leibniz\'s rationalism, but a synthesis that takes the problem they both articulated — how is knowledge possible — with absolute seriousness.'
        },
        {
            philosopher: 'Voltaire',
            text: 'Voltaire introduced Locke\'s Essay to the French reading public in his Letters Concerning the English Nation (Lettres philosophiques, 1733), devoting one of the most celebrated of the letters to what he called the modest and useful work of Locke on the human understanding. Where René Descartes had written the romance of the soul, Locke had written its history. This contrast — between the constructive but unverifiable speculations of the rationalists and the humble but honest empiricism of Locke — became the slogan of the French Enlightenment. Voltaire made Locke the model of what philosophy should aspire to: not grand systematic architectures built on self-evident first principles but careful, experience-based inquiry that knows its own limits. The Essay was as consequential for French thought as Newton\'s Principia was for French science — both demonstrated what rigorous, modest, empirical investigation could accomplish. Condillac\'s entire philosophical project, which radicalized Locke by attempting to derive all mental operations from a single original sensation, is inconceivable without Voltaire\'s promotion of the Essay as the new model of philosophical method.'
        },
        {
            philosopher: 'Noam Chomsky',
            text: 'Chomsky has made systematic and explicit use of the Essay\'s attack on innatism as the position he is most fundamentally opposed to. Against Locke\'s claim that the mind at birth is void of all characters, Chomsky argues from what he calls the poverty of the stimulus: the data available to a child acquiring its first language is too fragmentary, too inconsistent, and too limited to explain the richness, systematicity, and recursive complexity of the grammar the child acquires. The child generalizes in ways that go far beyond the evidence available, applying rules to sentence types she has never heard, detecting violations of principles no one has taught her. This gap between the input and the output of language acquisition is inexplicable without rich innate linguistic structure — a universal grammar specific to human beings. Chomsky calls this Plato\'s problem (after the Meno) and frames it as the fundamental objection to every empiricist account of mind. Locke\'s tabula rasa, Chomsky argues, cannot account for the most ordinary and universal cognitive achievement of every human child.'
        },
        {
            philosopher: 'Bertrand Russell',
            text: 'In A History of Western Philosophy (1945) and elsewhere, Russell gave Locke a mixed but fundamentally respectful assessment. He credited Locke with the remarkable achievement of founding a tradition of philosophy that connects naturally with scientific practice: empirical, moderate, sceptical of system-building, and concerned above all with what can actually be known. He praised Locke\'s treatment of primary and secondary qualities as a philosophically serious engagement with the implications of Newtonian science. But Russell also identified the deep tension in Locke\'s system that Berkeley and Hume exposed: if we perceive only our own ideas and not things themselves, then Locke\'s realist commitment to a world of material substances that cause our ideas becomes philosophically indefensible. Berkeley showed that accepting Locke\'s premises while abandoning his conclusions leads to idealism; Hume showed that it leads to scepticism. Russell\'s own response — logical atomism, sense-data theory — is in many ways an attempt to reconstruct Lockean empiricism on more rigorous foundations.'
        }
    ],

    modernRelevance: 'The Essay defined the terms of the empiricism-rationalism debate that Kant attempted to resolve and that contemporary cognitive science has re-opened. The primary-secondary quality distinction structures all philosophy of perception and has been revived in contemporary debates about color realism, phenomenal consciousness, and the hard problem of mind. Locke\'s account of personal identity — consciousness rather than bodily or soul-substance continuity — became the starting point of Derek Parfit\'s Reasons and Persons (1984), the most influential work in late twentieth-century personal identity theory. The distinction between nominal and real essence directly prefigures the Kripke-Putnam revolution in philosophy of language: their argument that natural kind terms like \'gold\' and \'water\' refer to real essences (the microstructural nature of the substance) rather than nominal descriptive clusters is an argument conducted entirely within Locke\'s framework.',

    context: 'Locke began the Essay in 1671 from a conversation held in his rooms at Exeter House, London. He composed drafts in the 1670s and during his Dutch exile of 1683-1689, returning to England on the same ship as the Princess of Orange in February 1689. The Essay was published later that year, along with the Two Treatises of Government and the Letter Concerning Toleration — an extraordinary triple debut in the year of the Glorious Revolution. It went through four revised editions in Locke\'s lifetime. The immediate intellectual context is the collision between Cartesian rationalism, the new corpuscularian natural philosophy of Boyle and Newton, and the skeptical challenges of the post-Reformation crisis of authority. Locke\'s project is to stake out a middle ground: more modest than rationalism, less destructive than skepticism.',

    relatedWorks: ['two-treatises-of-government', 'letter-concerning-toleration', 'locke-correspondence']
}

);
"""

# ─────────────────────────────────────────────────────────────────────────────
# DATA-14b  —  Two Treatises of Government + Letter Concerning Toleration
# ─────────────────────────────────────────────────────────────────────────────
data_14b = r"""/* ================================================================
   DATA PART 14b — Two Treatises of Government + Letter Concerning Toleration
   ================================================================ */

window.WORKS.push(

/* ──────────────────────────────────────
   1. TWO TREATISES OF GOVERNMENT
────────────────────────────────────── */
{
    id: 'two-treatises-of-government',
    title: 'Two Treatises of Government',
    greekTitle: 'Two Treatises of Government',
    philosopher: 'locke',
    category: 'political',
    categoryLabel: 'Political Philosophy',
    date: '1689 AD',
    dateSort: 1689,
    emoji: '⚖️',
    cardSize: 'wide',
    readingDifficulty: 'Intermediate',
    estimatedWordCount: 120000,

    shortDesc: 'The philosophical foundation of liberal constitutional democracy — Locke\'s demolition of divine-right monarchy and his argument that all legitimate political authority rests on natural rights, consent, and the forfeited trust of revolution.',

    summary: 'The Two Treatises of Government is the most politically consequential work of seventeenth-century philosophy. Published anonymously in 1689 and composed at least in part during the crisis years of 1679-1682, it remains the foundational text of modern liberalism and the philosophical source of both the American and French Revolutions.\n\nThe First Treatise is a meticulous and devastating demolition of Sir Robert Filmer\'s Patriarcha (published 1680, composed earlier), which had argued that kings derive their absolute authority from Adam\'s God-given dominion over the earth, transmitted through the patriarchs of Genesis to contemporary monarchs. Locke proceeds methodically: the Bible grants Adam no such dominion; even if it did, political authority is not a form of property that can be inherited; the chain of transmission from Adam to any living monarch is entirely untraceable; and even granting Filmer\'s premise, only one monarch in the world at any time could be legitimate — making every other government an usurpation. The First Treatise is underread but essential: it established that divine right monarchy was not a serious philosophical position, clearing the space for the positive account of the Second Treatise.\n\nThe Second Treatise is among the most influential works of political philosophy ever written. Its influence flows from a fundamental argumentative strategy: rather than beginning from existing political arrangements and asking how to legitimate them, Locke begins from a hypothetical state of nature and asks what political arrangements free and equal rational beings would choose.\n\nThe state of nature is not, as in Hobbes, a war of all against all where life is solitary, poor, nasty, brutish, and short. It is a condition of natural freedom and equality governed by the law of nature — which reason, available to every human being, teaches that all are equal and independent, and that no one ought to harm another in life, health, liberty, or possessions. In the state of nature, every person has executive power of the law of nature: the right to enforce natural law against those who violate it, including the right to punish transgressors proportionally to their crimes. This individualized enforcement is unstable because self-interest corrupts judgment. Political society emerges when individuals consent to surrender this private executive power to a public authority — the government — that acts as impartial judge, using known and settled laws.\n\nLocke\'s theory of property, developed in the celebrated chapter five, is one of the most discussed and disputed passages in the history of political thought. He begins from the premise that each person owns their own body and therefore the labor of their body. When a person mixes their labor with an unowned natural resource, they acquire property rights in the result: the person who clears and cultivates a field acquires title to it. This labor theory of property acquisition is qualified by two conditions: one must leave enough and as good for others (the sufficiency proviso), and one must not appropriate more than one can use before it spoils (the non-waste condition). Locke argues that the introduction of money — a non-perishable medium whose accumulation harms no one — and the tacit consent implied in its use removes the second restriction, allowing unlimited accumulation. This creates a division between the propertied and the propertyless that is not the result of injustice but of the rational choices of individuals operating under natural law.\n\nThe argument\'s political heart is in the chapters on the ends, forms, and dissolution of government. Government exists for one purpose: to protect the natural rights of individuals — their lives, liberties, and estates. The legislature is supreme because it represents the will of the people. The executive (including the prerogative power to act in emergencies beyond the letter of the law) is derivative and bounded. When the legislature usurps beyond its mandate, invades the property and liberties of subjects, or reduces citizens to arbitrary power and slavery, the government dissolves — and power reverts to the people, who recover their original right to constitute a new government. This is the theory of legitimate revolution that Jefferson paraphrased into the Declaration of Independence.',

    themes: ['Natural Rights', 'State of Nature', 'Consent and Legitimacy', 'Labour Theory of Property', 'Separation of Powers', 'Limited Government', 'Right to Revolution', 'Dissolution of Government', 'Critique of Absolute Monarchy', 'Social Contract'],

    keyCharacters: [
        { name: 'Sir Robert Filmer', role: 'Author of Patriarcha — the target demolished in the First Treatise. His divine-right absolutism, deriving royal authority from Adam\'s biblical dominion, was the dominant theoretical defense of Stuart monarchy.' },
        { name: 'Earl of Shaftesbury', role: 'Locke\'s patron and political master, whose opposition to Catholic succession and parliamentary resistance to Charles II provides the immediate political context for the Second Treatise\'s argument.' }
    ],

    concepts: [
        'Natural rights to life, liberty, and estate — pre-political rights that government exists to secure, not to create or grant',
        'State of nature as a moral condition — governed by natural law and characterized by equality and freedom, not war',
        'Consent as the only legitimate basis of political authority — government without consent is mere force and not binding',
        'Labour theory of property — mixing one\'s labour with unowned resources creates legitimate ownership',
        'The Lockean sufficiency proviso — appropriation is just only when enough and as good is left for others',
        'Government as trust — political power is held conditionally and forfeited when the terms of trust are violated',
        'Dissolution of government — when legislators betray their trust, power reverts to the people',
        'Tacit consent — continued residence and enjoyment of legal benefits constitutes consent to governmental authority',
        'Legislative supremacy — the legislature is the supreme power, but supreme only within the bounds of its trust'
    ],

    structure: 'First Treatise (11 chapters): Systematic refutation of Filmer\'s Patriarcha — Adam\'s dominion, property and rule, the title of the elder, and the transmission of authority.\n\nSecond Treatise, Ch. 1-5: State of nature, natural law, the origin and limits of property.\nSecond Treatise, Ch. 6-9: Paternal vs. political power; political society and its origins; ends of political society.\nSecond Treatise, Ch. 10-15: Forms of government; subordination of powers; prerogative.\nSecond Treatise, Ch. 16-19: Conquest, usurpation, tyranny, and the dissolution of government.',

    quote: 'Whensoever the legislators endeavour to take away and destroy the property of the people, or to reduce them to slavery under arbitrary power, they put themselves into a state of war with the people, who are thereupon absolved from any farther obedience. — Second Treatise, Chapter 19',

    additionalQuotes: [
        { text: 'The state of nature has a law of nature to govern it, which obliges every one; and reason, which is that law, teaches all mankind who will but consult it, that being all equal and independent, no one ought to harm another in his life, health, liberty, or possessions.', citation: 'Second Treatise, Chapter 2' },
        { text: 'Wherever law ends, tyranny begins.', citation: 'Second Treatise, Chapter 18' },
        { text: 'The great and chief end of men\'s uniting into commonwealths, and putting themselves under government, is the preservation of their property.', citation: 'Second Treatise, Chapter 9' }
    ],

    commentary: [
        {
            philosopher: 'Jean-Jacques Rousseau',
            text: 'Rousseau engaged extensively and critically with Locke\'s political philosophy, accepting his anti-absolutism while rejecting his foundations. Against Locke\'s labour theory of property, Rousseau argued in the Discourse on Inequality (1755) that private property is the original source of social evil, not a natural right. The first person who enclosed a piece of land and said \'this is mine\' was the true founder of civil society — and of all its miseries. Rousseau also attacked Locke\'s conception of the social contract as too thin: Lockean individuals never truly transform themselves into a people but remain an aggregate of private proprietors using government as a security firm. Against this, Rousseau proposed the general will — a collective self-legislation through which citizens constitute themselves as a genuinely moral community. For Rousseau, Locke\'s liberalism is not political philosophy at all but the ideological superstructure of propertied class interest.'
        },
        {
            philosopher: 'Thomas Jefferson',
            text: 'Jefferson identified Bacon, Locke, and Newton as the three greatest men who ever lived. The Declaration of Independence (1776) is directly and unmistakably Lockean in its philosophical architecture: self-evident truths about the equality of all men, unalienable rights including life, liberty, and the pursuit of happiness (Jefferson\'s modification of Locke\'s estate), and the right of the people to alter or abolish governments that fail in their protective function. Jefferson had Locke\'s Second Treatise and Sidney\'s Discourses Concerning Government open on his desk while drafting the Declaration. He later wrote that the object was not to find out new principles or new arguments but to place before mankind the common sense of the subject in terms plain and firm enough to command assent. That common sense was Locke\'s, transmitted through two generations of colonial constitutional thought.'
        },
        {
            philosopher: 'Robert Nozick',
            text: 'Nozick\'s Anarchy, State, and Utopia (1974) is explicitly a development and defense of Lockean political philosophy against John Rawls\'s liberal egalitarianism. Starting from Locke\'s account of natural rights as side-constraints on the treatment of persons — not merely goals to be maximized — Nozick argues that any taxation beyond what is necessary to fund a minimal protective state constitutes a rights violation equivalent to forced labour. Individuals are inviolable ends in themselves; redistributive taxation treats them as means to the satisfaction of others\' needs. Nozick\'s reconstruction of Locke\'s theory of property is particularly subtle: he accepts the Lockean proviso but argues that in a system of voluntary exchange, anyone who benefits from the institution of property — including the propertyless, who have access to a vastly more productive economy than the state of nature would provide — cannot complain that the proviso is violated.'
        },
        {
            philosopher: 'C.B. Macpherson',
            text: 'Macpherson\'s The Political Theory of Possessive Individualism (1962) offered the most influential Marxist critique of Locke, arguing that the apparent universalism of Locke\'s natural rights theory conceals a class-specific ideology of the emerging bourgeoisie. Locke\'s state of nature is not a pre-historical condition but a theoretical reconstruction of market society, in which individuals already possess differential capacities for labour and property accumulation. The labour theory of property does not describe how property was originally acquired but how it ought to be acquired — and in a monetized market economy, this legitimizes unlimited capital accumulation by those who can purchase the labor of others. Macpherson\'s reading has been contested by John Dunn and Jeremy Waldron, who argue he anachronistically projects market society backwards onto a fundamentally religious natural law framework.'
        },
        {
            philosopher: 'Jeremy Waldron',
            text: 'Waldron\'s The Right to Private Property (1988) provided the most philosophically rigorous contemporary treatment of Locke\'s property theory, arguing that the labour theory is not the embarrassing anachronism it appears to Macpherson\'s critics but a serious and underappreciated contribution to the theory of property rights. Waldron showed that the core of Locke\'s argument is not about mixing labour as a quasi-physical act but about the self-ownership thesis: since each person owns their own rational activity, and since that activity is what transforms raw nature into something humanly useful and valuable, the person who performs that transformation has a claim to the result that overrides others\' claims to the natural material. Waldron also developed the implications of the Lockean proviso for contemporary debates about intellectual property, global poverty, and the justice of property regimes in developed capitalist economies.'
        }
    ],

    modernRelevance: 'The Two Treatises is the direct philosophical ancestor of the liberal constitutional tradition in which most of the world now operates. Its argument that governmental power is conditional, that it must respect individual rights, and that citizens retain the right to resist and ultimately replace governments that betray their trust has been invoked in every revolution and constitutional founding since 1776. Contemporary debates about the limits of state authority — surveillance, eminent domain, conscription, taxation — are conducted within the framework Locke established. His labour theory of property has been applied to intellectual property disputes, indigenous land rights, and global distributive justice in ways that continue to generate both philosophical insight and bitter controversy.',

    context: 'Peter Laslett\'s definitive scholarly edition (1960) established, against the long-standing view that the Two Treatises was a post-hoc justification for the Glorious Revolution, that the Second Treatise was composed during the Exclusion Crisis of 1679-1682, when Locke\'s patron Shaftesbury was organizing parliamentary resistance to the Catholic succession of the Duke of York. Locke carried the manuscript to the Netherlands during his exile of 1683-1689 and published it immediately upon returning to England on the ship carrying William of Orange\'s court. He never publicly acknowledged authorship; the attribution was established definitively only after his death.',

    relatedWorks: ['letter-concerning-toleration', 'essay-concerning-human-understanding', 'locke-correspondence']
},

/* ──────────────────────────────────────
   2. A LETTER CONCERNING TOLERATION
────────────────────────────────────── */
{
    id: 'letter-concerning-toleration',
    title: 'A Letter Concerning Toleration',
    greekTitle: 'Epistola de Tolerantia',
    philosopher: 'locke',
    category: 'political',
    categoryLabel: 'Political Philosophy',
    date: '1689 AD',
    dateSort: 1689,
    emoji: '✉️',
    cardSize: 'normal',
    readingDifficulty: 'Intermediate',
    estimatedWordCount: 22000,

    shortDesc: 'The first systematic philosophical argument for religious toleration — distinguishing the coercive power of the state from the spiritual authority of the church, and demonstrating that forced belief is both philosophically impossible and politically illegitimate.',

    summary: 'The Letter Concerning Toleration is the foundational text of the modern doctrine of religious liberty and the separation of church and state. Written in Latin in the Netherlands in 1685-1686 and translated into English by William Popple, it was published in the same year as the Essay and the Two Treatises — the extraordinary triptych of 1689. The Letter was composed immediately after Louis XIV\'s Revocation of the Edict of Nantes had expelled hundreds of thousands of French Protestants and demonstrated the catastrophic consequences of religious intolerance in its most extreme political form.\n\nLocke\'s central argument is built on a rigorous and carefully maintained distinction between the legitimate jurisdiction of the state and the legitimate jurisdiction of the church. The commonwealth is a society constituted for the procurement, preservation, and advancement of its members\' civil interests — life, liberty, health, and the indolent possession of external things such as money, lands, houses, furniture. The church is a voluntary society joined by individuals for the worship of God in such manner as they judge acceptable to him. These two societies have different purposes, different memberships, different forms of authority, and different instruments. The confusion between them is the single source of all religious persecution.\n\nThe argument against religious coercion proceeds on two distinct grounds. The first is jurisdictional: God has not committed the care of souls to the magistrate, nor have citizens surrendered it in the social contract. The terms of political society concern only civil goods; souls were no part of the bargain. The second is philosophical and more original: coercion is constitutively incapable of producing the belief that salvation requires. Genuine religious belief must consist in the sincere inner conviction of the intellect. The magistrate\'s instruments — fines, imprisonment, exile, death — can compel outward conformity, but outward conformity is not faith. A person who adopts a creed because the magistrate commands it has no rational grounds for thinking it true and therefore no rational grounds for thinking it salvific. Religious persecution is thus self-defeating on its own terms: it cannot accomplish what it claims to seek.\n\nLocke\'s positive argument for toleration is also remarkable: it is not merely that persecution is wrong but that toleration is positively required by the nature of genuine religion. A church that uses coercion to maintain membership has ceased to be a church in any meaningful sense and has become merely a political institution with religious dress. The true church is constitutively voluntary.\n\nThe Letter concludes with two notorious exceptions to the toleration principle. Atheists cannot be tolerated because the destruction of all religious obligation eliminates the basis of oaths and promises, which are the foundation of all civil society. Catholics — though Locke describes them only as those whose allegiance to a foreign prince makes them politically unreliable — cannot be tolerated because their religious commitment undermines civil loyalty. Both exceptions have been extensively criticized by subsequent liberal theorists, including Rawls, as inconsistent with the Letter\'s own principles.',

    themes: ['Separation of Church and State', 'Religious Liberty', 'Limits of State Authority', 'Voluntarism in Religion', 'Coercion and Belief', 'Civil Goods vs Salvation', 'Natural Rights', 'Limits of Toleration'],

    keyCharacters: [
        { name: 'Philip van Limborch', role: 'Dutch Remonstrant theologian and Locke\'s closest intellectual friend in Holland — the addressee of the Letter and a central figure in the Amsterdam community of religious moderates who sheltered Locke during his exile' }
    ],

    concepts: [
        'Church as voluntary society — no legitimate church can compel membership; coerced religion is no religion at all',
        'Separation of civil and spiritual jurisdiction — the magistrate\'s power extends only to civil goods, never to the inner life',
        'Coercion cannot produce genuine belief — forced outward conformity is not the sincere inner conviction salvation requires',
        'Mutual toleration as the mark of the true church — a church that persecutes others has abdicated its religious character',
        'The asymmetry of dissent — the persecuting church, not the dissenting congregation, is the source of civil disorder'
    ],

    structure: 'Part 1: The distinction between the commonwealth and the church; the magistrate\'s power and the care of souls.\nPart 2: The nature of the church as a voluntary society; its authority and instruments.\nPart 3: The limits of the magistrate\'s authority over outward acts, speculative opinions, and practical opinions concerning religious matters.\nPart 4: The duty of toleration among churches; what one church may do to another.\nPart 5: The exceptions — atheism and politically subversive religion.',

    quote: 'The care of souls cannot belong to the civil magistrate, because his power consists only in outward force; but true and saving religion consists in the inward persuasion of the mind, without which nothing can be acceptable to God. — Letter Concerning Toleration',

    additionalQuotes: [
        { text: 'Nobody is born a member of any church; otherwise the religion of parents would descend unto children by the same right of inheritance as their temporal estates.', citation: 'Letter Concerning Toleration' },
        { text: 'It is not the diversity of opinions, which cannot be avoided, but the refusal of toleration to those that are of different opinions, which has produced all the bustles and wars in the Christian world upon account of religion.', citation: 'Letter Concerning Toleration' }
    ],

    commentary: [
        {
            philosopher: 'John Rawls',
            text: 'Rawls identified Locke\'s Letter as the founding text of political liberalism — the tradition that holds that legitimate political authority must be justifiable to all citizens regardless of their comprehensive religious or moral doctrines. But Rawls also identified a deep tension in Locke\'s argument: the Letter\'s defense of toleration itself rests on a specific theological premise — that God has not committed the care of souls to the magistrate. This makes Locke\'s toleration dependent on a particular religious interpretation, which means it is not genuinely neutral between comprehensive doctrines. Rawls\'s political liberalism attempts to correct this by grounding toleration in the idea of public reason — an overlapping consensus among citizens who hold different comprehensive doctrines — rather than in any single doctrine\'s implications. The move is a direct acknowledgment of what Locke\'s Letter achieves and what it fails to achieve.'
        },
        {
            philosopher: 'Pierre Bayle',
            text: 'The Huguenot philosopher Pierre Bayle, writing in the same Dutch exile as Locke, developed an argument for toleration in his Philosophical Commentary (1686) that is in several respects more radical than Locke\'s. Where Locke excluded atheists from toleration, Bayle argued that an atheistic society could be perfectly moral — perhaps more moral than a Christian one — since moral conduct depends on reason and conscience, not religious belief. Where Locke excluded Catholics as politically subversive, Bayle argued for universal toleration including Catholics and Muslims. Bayle and Locke knew of each other\'s work, though the precise relationship between their arguments remains debated. Together they represent the two poles of the seventeenth-century case for toleration: Locke the pragmatic natural lawyer, Bayle the more radical Enlightenment sceptic.'
        },
        {
            philosopher: 'James Madison',
            text: 'Madison\'s Memorial and Remonstrance Against Religious Assessments (1785) and the Virginia Statute for Religious Freedom (drafted by Jefferson, 1786) are American implementations of Lockean principles with crucial amplifications. Madison extended the argument for toleration from prudential grounds (religious coercion is self-defeating) to rights grounds (freedom of conscience is an unalienable right that government is constitutively incapable of overriding). The First Amendment\'s twin clauses — no establishment of religion, no prohibition of free exercise — implement the Lockean separation of church and state while going beyond Locke in applying it to the federal government\'s relation to all religious denominations without exception, including Catholicism and atheism. Madison was more consistent than Locke in applying toleration universally.'
        },
        {
            philosopher: 'Voltaire',
            text: 'Voltaire\'s Treatise on Tolerance (1763), written in the immediate aftermath of the judicial murder of the Protestant Jean Calas by the Toulouse parlement, is the most passionate and the most historically effective of all arguments for toleration. Voltaire drew directly on Locke while adding the weapons of satire, historical argument, and outrage that Locke\'s measured philosophical prose deliberately avoided. His famous conclusion — that if you are a Christian, answer him — directed at Locke\'s arguments, treated the Letter as unanswerable by any Christian who understood his own faith. Voltaire\'s campaign succeeded in getting Calas posthumously rehabilitated and made religious toleration the defining cause of the French Enlightenment. It is Voltaire\'s version of the Lockean argument, passionate and public rather than scholarly and legal, that actually changed European public opinion.'
        }
    ],

    modernRelevance: 'The Letter\'s distinction between civil and religious jurisdiction is the philosophical foundation of every modern constitutional separation of church and state, from the First Amendment to the French laïcité to the European Convention on Human Rights\' protection of freedom of conscience. The argument that the state has no legitimate authority over inner conviction remains the strongest philosophical foundation for religious liberty, and its application to secular moral convictions — that the state equally has no authority over one\'s fundamental ethical and personal choices — is the basis of modern liberal rights theory from Mill through Rawls.',

    context: 'Locke wrote the Letter in Amsterdam during the winter of 1685-1686, at the home of a Remonstrant minister. It was composed in Latin to reach a European audience directly. Limborch had it published in Gouda in 1689. William Popple\'s English translation appeared in London the same year. Locke published three subsequent Letters on Toleration responding to critics — particularly the Anglican clergyman Jonas Proast, who argued that the magistrate could justifiably use mild force to induce people to examine arguments they might otherwise ignore. Locke\'s replies to Proast are among the sharpest philosophical polemics he wrote. He died before completing a fourth Letter.',

    relatedWorks: ['two-treatises-of-government', 'essay-concerning-human-understanding', 'reasonableness-of-christianity']
}

);
"""

# ─────────────────────────────────────────────────────────────────────────────
# DATA-14c  —  Some Thoughts Concerning Education + Reasonableness of Christianity
# ─────────────────────────────────────────────────────────────────────────────
data_14c = r"""/* ================================================================
   DATA PART 14c — Some Thoughts Concerning Education + Reasonableness of Christianity
   ================================================================ */

window.WORKS.push(

/* ──────────────────────────────────────
   1. SOME THOUGHTS CONCERNING EDUCATION
────────────────────────────────────── */
{
    id: 'some-thoughts-concerning-education',
    title: 'Some Thoughts Concerning Education',
    greekTitle: 'Some Thoughts Concerning Education',
    philosopher: 'locke',
    category: 'practical',
    categoryLabel: 'Education and Ethics',
    date: '1693 AD',
    dateSort: 1693,
    emoji: '📚',
    cardSize: 'normal',
    readingDifficulty: 'Beginner',
    estimatedWordCount: 65000,

    shortDesc: 'The most widely read pedagogical work of the Enlightenment — Locke\'s empiricist theory of education applied to the formation of a rational, virtuous, and practically competent person, placing character before curriculum and habit before rule.',

    summary: 'Some Thoughts Concerning Education grew from a series of letters Locke wrote between 1684 and 1691 to his friend Edward Clarke, a Somerset gentleman seeking practical guidance on the upbringing of his son. Locke expanded the letters into a continuous treatise and published them in 1693. The work became one of the most influential educational texts in European history, translated into French, Dutch, Swedish, and German, and directly shaped Rousseau\'s Émile (1762) — a work that is both deeply indebted to Locke and systematically in reaction against him.\n\nThe philosophical foundation of the work is the empiricism of the Essay: the child\'s mind is shaped entirely by experience, and education is therefore the single most important thing that can happen to a human being. Nine parts of ten of the men we meet with are what they are, good or evil, useful or not, by their education. If this is true, the question of how to educate is a question of the highest moral and political urgency.\n\nLocke\'s priorities are consistently surprising to modern readers. He begins not with curriculum but with the body: the child must be hardened against cold, given plain food, allowed to sleep on a harder mattress, provided with shoes that admit water freely, and permitted to play vigorously outdoors in all weather. This physical toughening is not Spartan severity for its own sake but is grounded in the empiricist psychology of habit: the body must be trained before the age of reason solidifies dispositions in the wrong direction, and physical resilience is a prerequisite for the equanimity needed to learn well.\n\nVirtue is Locke\'s second priority, and here he makes his most original and enduring contribution to educational theory. Virtue, for Locke, consists above all in the capacity for self-denial — the ability to withstand one\'s own desires and appetites when reason counsels otherwise. This is not mere obedience but genuine self-governance: the internal capacity to act for the long-term good against the pressure of present appetite. This capacity must be instilled early, through habituation, before desires have consolidated into second nature. The critical pedagogical instrument is not the rod but the management of the child\'s desire for esteem. Children respond powerfully to praise and shame, approval and disgrace, from adults they love and respect. A parent who is feared is less effective than a parent who is respected; a teacher who can make a child ashamed of laziness or cruelty achieves more than one who merely punishes it.\n\nOn corporal punishment, Locke is explicit and firm: it is counterproductive. It produces temporary compliance through fear but no internalization of the values that motivated the punishment. Worse, it establishes a servile relationship between the child\'s will and external authority, training the child to obey only under threat — the opposite of the rational self-governance education should produce. Children formed by the rod rather than by reasoned guidance and the cultivation of shame will be moral children only as long as they are physically weaker than their parents, and ungovernable adults the moment they are not.\n\nOn curriculum, Locke is equally surprising. He dismisses most of the scholastic Latin-grammar curriculum then standard in English education as a waste of time. Reading and writing come first, then drawing (for observation and precision), then French by conversation rather than grammar, then Latin by conversation too if it is taught at all. History, arithmetic, geography, natural philosophy, and civil law are all more valuable than the formal study of classical rhetoric or logic. Above all, the ability to express oneself clearly and persuasively in one\'s own language — English — is the most practically valuable skill that education can produce and is almost entirely neglected in contemporary schools.',

    themes: ['Habit Formation', 'Virtue as Self-Denial', 'Corporal Punishment Opposed', 'Curriculum Reform', 'Education of Desire and Esteem', 'Practical vs Classical Learning', 'Empiricism Applied to Pedagogy', 'Physical Hardening', 'The Gentleman as Ideal'],

    keyCharacters: [
        { name: 'Edward Clarke', role: 'The Somerset gentleman whose practical questions about child-rearing provided the origin of the treatise — a reminder that one of the most influential works of educational philosophy began as personal correspondence' }
    ],

    concepts: [
        'Nine parts in ten are made by education — the empiricist premise that character is almost entirely formed by experience',
        'Sound mind in sound body — the double aim, with physical hardening as prerequisite for intellectual and moral development',
        'Habit over rule — the most durable moral formation is habituated before the child can reflect on what is being formed',
        'Self-denial as the master virtue — the capacity to withstand present appetite for long-term rational ends',
        'Esteem and shame as the levers of education — more durable and morally formative than corporal punishment',
        'Against the rod — physical punishment produces compliance but not internalization; it trains servility, not virtue',
        'Plain and practical curriculum — English writing, drawing, French, history, arithmetic, natural philosophy over scholastic Latin grammar'
    ],

    structure: 'Part 1 (§1-30): The body — health, hardening, diet, exercise, and the rationale for physical toughness.\nPart 2 (§31-82): The mind and character — virtue, self-denial, esteem, the management of desire, the rejection of corporal punishment.\nPart 3 (§83-195): The curriculum — reading, writing, drawing, French, Latin, arithmetic, geography, history, natural philosophy, civics.\nPart 4 (§196-216): Defects in prevailing practice; the character of the tutor; miscellaneous recommendations.',

    quote: 'Of all the men we meet with, nine parts of ten are what they are, good or evil, useful or not, by their education. It is that which makes the great difference in mankind. — Some Thoughts Concerning Education, §1',

    additionalQuotes: [
        { text: 'The great mistake I have observed in people\'s breeding their children has been, that this has not been taken care enough of in its due season; that the mind has not been made obedient to discipline and pliant to reason, when at first it was most tender, most easy to be bowed.', citation: 'Some Thoughts Concerning Education, §34' },
        { text: 'He that has found a way to keep up a child\'s spirit, easy, active, and free; and yet at the same time to restrain him from many things he has a mind to, and to draw him to things that are uneasy to him, he that knows how to reconcile these seeming contradictions, has got the true secret of education.', citation: 'Some Thoughts Concerning Education, §46' }
    ],

    commentary: [
        {
            philosopher: 'Jean-Jacques Rousseau',
            text: 'Rousseau\'s Émile (1762) is simultaneously the most profound tribute to and the most radical critique of Locke\'s educational philosophy. Rousseau accepted the empiricist premise that character is formed by experience, and he accepted Locke\'s rejection of rote learning and corporal punishment. But he argued that Locke had not gone far enough in either direction. The education of the gentleman that Locke describes is the education of a class, not of a human being — it takes for granted a social position and a set of competitive relationships that are themselves the product of a corrupt civilization. Rousseau\'s Emile is educated in isolation from society, in direct relation with nature and things rather than with other people and their opinions, precisely because social opinion — the desire for esteem that Locke makes his central instrument — is for Rousseau the principal corruptor of natural goodness. Locke weaponizes amour propre (the desire for others\' approval); Rousseau tries to prevent its development. Both recognize that education is the formation of desire, but they disagree completely about which desires should be formed.'
        },
        {
            philosopher: 'John Dewey',
            text: 'Dewey\'s progressive educational philosophy, articulated in Democracy and Education (1916) and Experience and Education (1938), is the twentieth-century development of Lockean empirical pedagogy in a democratic direction. Dewey accepted Locke\'s core insight that learning is not the passive reception of transmitted information but the active engagement of the learner with problems, things, and situations. His constructivist pedagogy — learning by doing, the school as a democratic community, the integration of curriculum with real-world problems — is a systematic development of the practical orientation of Locke\'s curriculum recommendations. Dewey also radicalized Locke\'s social implications: where Locke is writing for the education of the children of gentlemen, Dewey insists that the same quality of experience-based education must be available to all children in a democratic society, because educational inequality is political inequality.'
        },
        {
            philosopher: 'Mary Wollstonecraft',
            text: 'Wollstonecraft\'s A Vindication of the Rights of Woman (1792) explicitly invokes Locke\'s educational principles to argue for the equal education of women. If character is formed by education and experience, and if women\'s characters appear inferior to men\'s in rationality, self-governance, and practical competence, the explanation is not nature but education: women are systematically educated for dependence, emotional compliance, and pleasing appearance rather than for the rational self-determination that Locke\'s educational philosophy is designed to produce. Wollstonecraft uses Locke against Locke: his own principles demand that girls receive the same character-forming education in virtue, reason, and practical knowledge that he recommends for boys — and the failure to provide it is not only unjust but educationally self-defeating, since mothers who have not been educated rationally cannot educate their children rationally.'
        },
        {
            philosopher: 'Gilbert Ryle',
            text: 'Ryle\'s distinction between knowing-that (propositional knowledge of facts) and knowing-how (practical competence and skill) in The Concept of Mind (1949) provides a useful framework for understanding Locke\'s curriculum recommendations. Locke\'s consistent preference for conversational language acquisition over grammatical rule-learning, for drawing and mapping over rote description, and for practical natural philosophy over scholastic logic reflects an implicit prioritization of knowing-how over knowing-that. The child who has learned to express herself clearly in English has knowing-how; the child who has memorized the rules of Latin grammar has only knowing-that. Ryle\'s analysis vindicates Locke\'s pedagogical instinct and connects it to the later Wittgensteinian emphasis on practice, use, and form of life over theoretical principle.'
        }
    ],

    modernRelevance: 'Locke\'s insistence that education forms nearly everything in human character — and that early habituation, before reflective self-awareness, is its most powerful instrument — is confirmed by developmental psychology and neuroscience. His argument that corporal punishment produces compliance without internalization is supported by decades of empirical research showing that physical punishment increases aggression, reduces internalization of moral values, and damages the parent-child relationship. His skepticism about rote learning and his preference for active, problem-engaged education are the foundations of constructivist pedagogy from Dewey through current project-based learning approaches.',

    context: 'The letters to Clarke were written between 1684 and 1691, mostly during Locke\'s Dutch exile. Locke reworked them as a continuous text after his return to England in 1689, and they were published in 1693. Five editions appeared in his lifetime. The immediate practical context is the English gentleman\'s education, but the philosophical context is the Essay: having argued that character is formed by experience, Locke is obligated to answer the question of what experience education should provide.',

    relatedWorks: ['essay-concerning-human-understanding', 'two-treatises-of-government', 'reasonableness-of-christianity']
},

/* ──────────────────────────────────────
   2. THE REASONABLENESS OF CHRISTIANITY
────────────────────────────────────── */
{
    id: 'reasonableness-of-christianity',
    title: 'The Reasonableness of Christianity',
    greekTitle: 'The Reasonableness of Christianity',
    philosopher: 'locke',
    category: 'practical',
    categoryLabel: 'Theology',
    date: '1695 AD',
    dateSort: 1695,
    emoji: '✝️',
    cardSize: 'normal',
    readingDifficulty: 'Intermediate',
    estimatedWordCount: 55000,

    shortDesc: 'Locke\'s attempt to reduce Christianity to its rational essentials — the founding document of liberal Protestant theology and the work that aligns the moral law of reason with the teachings of Christ.',

    summary: 'The Reasonableness of Christianity is the work in which Locke most directly addresses the relationship between reason and revelation — the defining intellectual problem of the late seventeenth century as traditional religious authority faced unprecedented pressure from the new science and biblical criticism. Published anonymously in 1695, it provoked an immediate and fierce controversy: Locke was accused of Socinianism (denial of Christ\'s divinity), of reducing Christianity to mere moral philosophy, and of undermining the Trinity. He responded in two Vindications, defending himself with characteristic precision.\n\nLocke\'s method is disarmingly simple: read the Gospels and the Acts of the Apostles carefully, noting what Christ and the apostles actually required people to believe for salvation. His answer is minimal. The single essential article is that Jesus is the Messiah, the Son of God sent by God to offer forgiveness and eternal life on conditions of repentance and sincere moral effort. Everything else — the elaborate doctrinal architectures of Trinitarian theology, original sin, penal substitutionary atonement, sacramental grace — is the superaddition of later theologians and councils. It is not found in the words of Christ himself, who preached simple moral transformation and demanded only the acknowledgment of his Messianic identity.\n\nThe work\'s philosophical core is the alignment of natural religion and Christianity. The law of nature — discoverable by unaided reason — is the same law that Christ teaches and exemplifies. The moral content of Christianity is accessible to reason; what revelation adds is not different moral content but clearer articulation, stronger motivation through the promise of resurrection, and authoritative enforcement through divine sanction. This alignment of rational ethics and Christian ethics was enormously influential: it made Christianity safe for Enlightenment rationalists who could not accept supernatural dogma but could accept a moral religion confirmed by the life of an exemplary teacher.\n\nThe deeper implication, which Locke\'s critics saw clearly and which Locke himself acknowledged only guardedly, is that Christianity becomes in this account less the unique supernatural revelation of truths unavailable to reason than the confirmation and clarification of truths reason could in principle discover independently. This proto-Deist implication placed Locke in a delicate position: he insisted on the necessity and value of revelation (because most people lack the time, education, and capacity for philosophical reasoning and need authoritative moral teaching), but his argument repeatedly suggests that the content of that revelation is what reason would have said anyway.',

    themes: ['Rational Religion', 'Liberal Protestantism', 'Faith and Reason', 'Minimal Creed', 'Natural Law as Moral Foundation', 'Messianic Identity', 'Enlightenment Deism', 'Moral Religion vs Dogmatic Theology'],

    keyCharacters: [
        { name: 'Edward Stillingfleet', role: 'Bishop of Worcester and Locke\'s most formidable theological critic — his attacks on the Essay and the Reasonableness forced Locke into his most careful clarifications of the relationship between reason, faith, and revelation' }
    ],

    concepts: [
        'Minimal Christianity — the single essential article of faith is that Jesus is the Messiah',
        'Reasonableness of faith — the miracles accompanying Jesus\'s ministry provide rational grounds for accepting his authority',
        'Natural law as moral core — the ethical content of Christianity is fully accessible to unaided reason',
        'Revelation as confirmation, not replacement — Christianity clarifies and motivates what reason already teaches',
        'Sufficient scripture — the Bible contains all that is necessary for salvation without ecclesiastical supplement or elaborate doctrinal system'
    ],

    structure: 'Part 1: Survey of the New Testament for the minimum requirements of faith; the Messianic claim as the essential article.\nPart 2: The role of miracles as the rational foundation for accepting Jesus\'s authority.\nPart 3: The alignment of the moral law of nature with the teachings of Christ.\nPart 4: The advantages of revealed Christianity over purely natural religion — clarity, authority, and universal accessibility.',

    quote: 'The writers and wranglers in religion fill it with niceties, and dress it up with notions, which they make necessary and fundamental parts of it; as if there were no way into the Church, but through the academy or lyceum. — Reasonableness of Christianity',

    additionalQuotes: [
        { text: 'Reason is natural revelation, whereby the eternal Father of light and fountain of all knowledge communicates to mankind that portion of truth which he has laid within the reach of their natural faculties.', citation: 'Essay Concerning Human Understanding, Book IV, Chapter 19' },
        { text: 'The only saving faith is a full persuasion of the mind concerning any proposition, and this is not to be got by the force of arms.', citation: 'Second Vindication of the Reasonableness of Christianity' }
    ],

    commentary: [
        {
            philosopher: 'Edward Stillingfleet',
            text: 'Stillingfleet, in his Discourse in Vindication of the Trinity (1697) and subsequent letters to Locke, made the most penetrating contemporary critique of the Reasonableness. His argument was that Locke\'s principles in the Essay — particularly his account of ideas and his denial of real essences — undermined the philosophical foundations required to formulate the doctrine of the Trinity coherently. If we cannot know real essences and cannot predicate identity across what appear to be distinct substances, we cannot give philosophical meaning to the claim that Father, Son, and Holy Spirit are three persons in one substance. Locke\'s reply was that his philosophy and the doctrine of the Trinity were independent — that theology does not depend on any particular philosophical system. Stillingfleet was not satisfied. The controversy is historically important for forcing Locke to clarify his account of substance, essence, and the limits of nominal definition more precisely than the Essay itself had done.'
        },
        {
            philosopher: 'John Toland',
            text: 'Toland\'s Christianity Not Mysterious (1696) drew the explicit Deist implications that Locke had carefully avoided in the Reasonableness. Toland argued that if Christianity is rational and its moral content accessible to reason, then revelation adds nothing to what reason already knows — it is not mysterious, not supernatural, and not strictly necessary. Toland pushed Locke\'s premises further than Locke himself would go, and the result was a work that was publicly burned in Ireland and that placed Toland on the wrong side of every establishment in Europe. Locke carefully distanced himself from Toland, insisting that revelation does add something — clarity, motivation, and universal authority — that reason unaided cannot provide. But contemporaries and historians have often regarded the difference between Locke\'s position and Toland\'s as one of degree rather than kind.'
        },
        {
            philosopher: 'Thomas Jefferson',
            text: 'Jefferson regarded the Reasonableness as one of the most important books he had ever read and as the model for his own religious thinking. His famous Jefferson Bible — the life and morals of Jesus of Nazareth, literally cut and pasted from four gospel translations with all miracles, supernatural claims, and doctrinal statements removed — is the Lockean minimal Christianity carried to its logical terminus. Jefferson kept two copies of the Reasonableness in his library, recommended it repeatedly to friends, and considered it the best available refutation of Calvinist orthodoxy and the scholastic theology that had dominated Christian thought. Where Locke kept the miracles as rational evidence for Jesus\'s authority, Jefferson removed them; but the impulse to strip Christianity to its rational and moral essentials is identically Lockean.'
        },
        {
            philosopher: 'Voltaire',
            text: 'Voltaire read the Reasonableness with enthusiasm as part of his broader assimilation of English thought during his London exile (1726-1729), and it contributed substantially to his conviction that rational, tolerant, moral religion was both possible and necessary as an alternative to the superstition and fanaticism of institutional Christianity. His portrait of Locke in the Lettres philosophiques includes an extended discussion of the Reasonableness\'s minimalism, praising it for removing the accumulated nonsense of centuries of scholastic theology and returning to the plain, rational, morally serious Christianity of the Gospels themselves. For Voltaire, the Reasonableness exemplified the English achievement of making religion civilized — compatible with reason, tolerant of disagreement, and focused on moral conduct rather than dogmatic conformity.'
        }
    ],

    modernRelevance: 'The Reasonableness is the philosophical source of the liberal Protestant tradition that dominates mainstream Christianity in the English-speaking world — characterized by emphasis on ethics over doctrine, moral transformation over sacramental grace, and compatibility of faith with modern science. The question Locke poses — what is the irreducible minimum of Christian belief, and is that minimum compatible with Enlightenment rationalism? — continues to define the central fault line in contemporary Christian theology, between the liberal tradition descending from Locke through Schleiermacher and Ritschl and the theological conservatism that insists on the irreducibility of supernatural revelation.',

    context: 'Locke read through the entire New Testament in Greek in preparation for this work and was struck by the gap between what Christ and the apostles actually required and what subsequent theologians had required in their name. He published it anonymously in 1695 out of caution, having already experienced the controversy generated by the Essay. The accusation of Socinianism was not entirely unfair: the minimal creed Locke identifies is compatible with a view of Christ as a uniquely inspired human being rather than the second person of the Trinity, and Locke\'s own private beliefs — inferred from correspondence and his unpublished manuscript on St. Paul — lean toward an anti-Trinitarian position.',

    relatedWorks: ['letter-concerning-toleration', 'essay-concerning-human-understanding', 'locke-correspondence']
}

);
"""

# ─────────────────────────────────────────────────────────────────────────────
# DATA-14d  —  Questions Concerning the Law of Nature + Essay on Toleration (1667) + Conduct of the Understanding
# ─────────────────────────────────────────────────────────────────────────────
data_14d = r"""/* ================================================================
   DATA PART 14d — Questions Concerning the Law of Nature + Essay on Toleration (1667) + Of the Conduct of the Understanding
   ================================================================ */

window.WORKS.push(

/* ──────────────────────────────────────
   1. QUESTIONS CONCERNING THE LAW OF NATURE
────────────────────────────────────── */
{
    id: 'questions-law-of-nature',
    title: 'Questions Concerning the Law of Nature',
    greekTitle: 'Quaestiones de Lege Naturae',
    philosopher: 'locke',
    category: 'political',
    categoryLabel: 'Natural Law',
    date: '1664 AD',
    dateSort: 1664,
    emoji: '📜',
    cardSize: 'normal',
    readingDifficulty: 'Advanced',
    estimatedWordCount: 30000,

    shortDesc: 'Locke\'s earliest systematic philosophical work — eight Latin essays on the foundations of natural law, establishing the framework of rational moral obligation that underlies all his mature political thought.',

    summary: 'The Questions Concerning the Law of Nature are eight Latin essays composed by Locke around 1663-1664 while he was Censor of Moral Philosophy at Christ Church, Oxford. They represent his first sustained philosophical work and remained unpublished in his lifetime, unknown to scholars until W. von Leyden discovered and edited them in 1954. Despite their incomplete and exploratory character, they are indispensable for understanding the foundations of Locke\'s mature political philosophy: the natural law framework that underlies the Two Treatises is already present here in embryonic form.\n\nThe central questions are: Is there a law of nature? Can it be known by reason? What is the basis of its obligatory force? Locke\'s answers are affirmative on the first two counts but philosophically complex on the third. Against the Hobbesian position that there is no natural moral law beyond the dictates of self-preservation, Locke argues that reason discovers genuine moral obligations binding on all human beings regardless of positive law or convention. The law of nature is not a human construction but a divine ordinance accessible to rational inquiry — it is inscribed in the world by God and readable by any mind attentive to its evidence.\n\nThe epistemological question — how we come to know natural law — is treated with remarkable sophistication. Locke explicitly rejects the doctrine of innate moral knowledge that he will later attack in the Essay: we do not know natural law by innatism but by sense and reason working together. The senses provide the raw materials; reason, reflecting on them, discovers the moral structure of human nature and the requirements for human flourishing. This empiricist approach to natural law is already, twenty years before the Essay, the characteristic Lockean move: anti-Cartesian, anti-scholastic, grounded in experience and natural observation.\n\nThe question of obligation is the most difficult and is the one Locke handles least satisfactorily in the early work. He argues that the obligatory force of natural law derives from God\'s authority as creator — a divine will theory that sits in tension with the rational discovery model of the rest of the essays. If we discover natural law by reason, why does its binding force depend on God\'s legislative will rather than on reason\'s own authority? This tension between rationalist and voluntarist elements in Locke\'s natural law theory runs through all his mature work and has generated extensive scholarly debate.',

    themes: ['Natural Law', 'Foundations of Morality', 'Moral Epistemology', 'Divine Will vs Rational Discovery', 'Obligation and Authority', 'Early Empiricism', 'Against Innatism in Ethics'],

    keyCharacters: [],

    concepts: [
        'Natural law as divine ordinance knowable by reason — Locke\'s alternative to both voluntarism and rationalism',
        'Against innate moral knowledge — moral principles are discovered by sense and reason, not implanted at birth',
        'Sense and reason as the means of moral knowledge — the empiricist approach to ethics twenty years before the Essay',
        'Divine authority as the ground of obligation — God as creator and legislator whose commands bind rational creatures',
        'The law of nature as universal — binding on all human beings at all times regardless of positive law or convention'
    ],

    structure: 'Essay 1: Is there a rule of morals given by nature? Yes — established by arguments from consent, natural order, and reason.\nEssay 2: Can the law of nature be known by reason? Yes — against the claim that it must be innate.\nEssay 3: Is reason the foundation of the law of nature?\nEssay 4: Can the law of nature be known from the general consent of mankind? No — consent is not the basis of its validity.\nEssay 5: Can the law of nature be known from tradition?\nEssay 6: Is the binding force of the law of nature perpetual?\nEssay 7: Is self-interest the basis of the law of nature?\nEssay 8 (incomplete): Is every man\'s own interest the foundation of the law of nature?',

    quote: 'Reason is the basis of natural law, not in the sense that reason creates it, but in the sense that by consulting reason we are able to discover what natural law requires of us — much as we discover mathematical truths by the use of reason without having created those truths. — Questions Concerning the Law of Nature, Essay 2',

    additionalQuotes: [
        { text: 'The law of nature stands as an eternal rule to all men, legislators as well as others. The rules that they make for other men\'s actions must be conformable to the law of nature.', citation: 'Second Treatise of Government, Chapter 11 — the mature statement of the same principle' }
    ],

    commentary: [
        {
            philosopher: 'John Dunn',
            text: 'Dunn\'s The Political Thought of John Locke (1969) is the single most important study of the Questions and their relation to the mature political works. Dunn argued, against the prevailing liberal reading of Locke, that the Two Treatises is not primarily a theory of rights but a theory of divinely imposed duties. The fundamental moral relationship in Locke\'s world is between God as creator-legislator and human beings as creatures — and the rights Locke defends are the correlates of duties, not freestanding entitlements. The Questions make this framework explicit in a way the Two Treatises, which was addressed to a different audience, does not. Dunn\'s reading has been enormously influential in redirecting Locke scholarship away from the anachronistic projection of modern rights theory and toward the seventeenth-century natural law context in which Locke was actually working.'
        },
        {
            philosopher: 'W. von Leyden',
            text: 'Von Leyden\'s discovery and edition of the Questions (1954) transformed Locke scholarship by revealing the philosophical depth and sophistication of Locke\'s early thought. Before von Leyden\'s edition, the Two Treatises appeared to begin from a relatively unexamined natural law framework; after it, scholars could see that Locke had spent years working through the philosophical foundations of that framework before writing his mature political works. Von Leyden also showed that the Questions raise questions — particularly about the relationship between rational discovery and divine command — that Locke never fully resolved and that constitute the deepest tensions in his entire philosophical system.'
        }
    ],

    modernRelevance: 'The Questions are significant for two reasons. First, they document the earliest phase of the empiricist approach to moral epistemology — the attempt to ground moral obligations in observed features of human nature and rational reflection rather than in Cartesian innate ideas or pure rational intuition. This approach was continued by Shaftesbury, Hutcheson, and Hume in their moral sense and sentiment theories. Second, the tension between rational discovery and divine command that the Questions expose without resolving is a version of the Euthyphro dilemma that continues to structure debates in contemporary metaethics about the relationship between God and morality.',

    context: 'Locke held the Censorship in Moral Philosophy at Christ Church from 1663-1664. The Questions were probably composed as lecture notes or as exercises in the scholastic Latin disputation format. They are in Latin and have the structure of formal academic disputations. They were never published by Locke and were unknown until von Leyden found them in the Lovelace Collection at the Bodleian Library in the early 1950s.',

    relatedWorks: ['two-treatises-of-government', 'essay-concerning-human-understanding', 'essay-on-toleration-1667']
},

/* ──────────────────────────────────────
   2. AN ESSAY CONCERNING TOLERATION (1667)
────────────────────────────────────── */
{
    id: 'essay-on-toleration-1667',
    title: 'An Essay Concerning Toleration',
    greekTitle: 'An Essay Concerning Toleration',
    philosopher: 'locke',
    category: 'political',
    categoryLabel: 'Political Philosophy',
    date: '1667 AD',
    dateSort: 1667,
    emoji: '🕊',
    cardSize: 'normal',
    readingDifficulty: 'Intermediate',
    estimatedWordCount: 14000,

    shortDesc: 'The unpublished draft of 1667 — Locke\'s first statement of the case for toleration, composed twenty years before the famous Letter, revealing a more provisional but in some respects more candid argument for separating religion from political authority.',

    summary: 'The Essay Concerning Toleration of 1667 is an unpublished manuscript that remained unknown until the twentieth century. It is the first draft of the argument that Locke would develop and publish as the Letter Concerning Toleration in 1689, and the comparison between them is philosophically illuminating. The 1667 Essay is in some respects more practical and in some respects more philosophically candid than the Letter — it was written for a specific political audience (almost certainly for Locke\'s patron Shaftesbury, who was then navigating the religious politics of the Restoration) and does not need to present itself as a timeless philosophical argument.\n\nLocke divides the objects of religious practice into three categories: purely speculative opinions (such as the existence of God or the nature of salvation), which the magistrate has no business regulating because they have no direct bearing on civil life; practical opinions with no necessary connection to civil harm (such as whether one should attend church on Sundays or whether one must be baptized as an infant), which the magistrate should tolerate but may regulate for civil reasons; and practical opinions and acts with direct bearing on civil peace and public order, which the magistrate may regulate regardless of their religious motivation.\n\nThis tripartite structure represents a more nuanced and contextually sensitive argument than the Letter\'s sweeping distinction between civil and religious jurisdiction. The 1667 Essay acknowledges that the line between private religion and public civil consequence is not always clear, and it gives the magistrate more room to regulate on prudential grounds than the Letter will. It is also strikingly candid about Locke\'s political motive: the case for toleration is made partly on the grounds that enforced religious uniformity tends to produce exactly the civil disorder it is designed to prevent, uniting dissenters in opposition to the government and creating exactly the political cohesion among nonconformists that absolute intolerance would suppress.\n\nThe 1667 Essay also shows Locke working toward but not yet having reached the central argument of the Letter: that coercion is constitutively incapable of producing genuine religious belief. This argument, which in the Letter becomes Locke\'s strongest and most original contribution, appears only in rudimentary form in the draft, and its full elaboration clearly represents a philosophical development of the twenty intervening years.',

    themes: ['Toleration', 'Religious Liberty', 'Magistrate\'s Jurisdiction', 'Practical vs Speculative Religion', 'Draft vs Published Argument', 'Political Prudence', 'Civil Order'],

    keyCharacters: [
        { name: 'Earl of Shaftesbury', role: 'The probable intended reader of the essay — Locke\'s patron was navigating religious politics in the Restoration court and needed a coherent liberal position on religious dissent' }
    ],

    concepts: [
        'Three categories of religious practice — purely speculative, practical with no civil consequence, and practical with civil consequence',
        'Prudential argument for toleration — forced uniformity produces greater civil disorder than tolerating dissent',
        'Limits of the magistrate\'s jurisdiction — the three-part scheme provides a more contextual account than the Letter\'s binary',
        'Development of Locke\'s argument — comparison with the 1689 Letter reveals twenty years of philosophical clarification'
    ],

    structure: 'Part 1: Purely speculative opinions — magistrate has no jurisdiction at all.\nPart 2: Practical opinions in matters of religion — magistrate should generally tolerate but may regulate on civil grounds.\nPart 3: Practical opinions with direct civil consequences — magistrate may regulate.\nPart 4: Prudential arguments — toleration is politically wiser than persecution.',

    quote: 'The magistrate has nothing to do with the good of men\'s souls or their concernments in another life but only with the peace and prosperity of his subjects in this world. — Essay Concerning Toleration, 1667',

    additionalQuotes: [
        { text: 'It is not the diversity of opinions which cannot be avoided, but the refusal of toleration to those that are of different opinions, which might have been avoided, that has produced all the bustles and wars that have been in the Christian world upon account of religion.', citation: 'Essay Concerning Toleration, 1667 (almost verbatim repeated in the 1689 Letter)' }
    ],

    commentary: [
        {
            philosopher: 'Mark Goldie',
            text: 'Goldie\'s editorial work on the 1667 Essay and his studies of Locke\'s political writings in context have been essential for understanding the relationship between the draft and the published Letter. Goldie showed that the 1667 Essay was not merely a less developed version of the Letter but a different kind of argument addressed to a different audience: a piece of practical political counsel rather than a philosophical treatise. The evolution from the 1667 Essay to the 1689 Letter traces Locke\'s movement from a contextual, pragmatic defense of toleration to a principled, universal one — from a practical recommendation to a philosophical position grounded in the nature of religion and the limits of political authority.'
        }
    ],

    modernRelevance: 'The 1667 Essay is valuable to scholars of Locke\'s development and to anyone interested in how philosophical arguments for toleration emerged from practical political context. Its three-part scheme for distinguishing matters of private religion from matters of public civil consequence is actually in some ways more useful for contemporary policy analysis than the Letter\'s sharper but less flexible binary: contemporary debates about religious exemptions from anti-discrimination law, religiously motivated conscientious objection, and the public display of religious symbols all involve exactly the kind of contextual assessment of civil consequences that the 1667 Essay\'s framework makes possible.',

    context: 'The essay exists in three manuscript drafts, which show Locke working through the argument over the course of 1667-1668. It was probably shown to Shaftesbury and a small circle of politically engaged readers but never published. Locke preserved the drafts and revised them during his Dutch exile, but ultimately chose to write an entirely fresh argument for the Letter rather than revise and publish the earlier essay. The essay was first published in H. R. Fox Bourne\'s The Life of John Locke (1876) and edited critically by C. A. Viano in 1961.',

    relatedWorks: ['letter-concerning-toleration', 'two-treatises-of-government', 'questions-law-of-nature']
},

/* ──────────────────────────────────────
   3. OF THE CONDUCT OF THE UNDERSTANDING
────────────────────────────────────── */
{
    id: 'conduct-of-the-understanding',
    title: 'Of the Conduct of the Understanding',
    greekTitle: 'Of the Conduct of the Understanding',
    philosopher: 'locke',
    category: 'epistemology',
    categoryLabel: 'Epistemology',
    date: '1706 AD',
    dateSort: 1706,
    emoji: '🧭',
    cardSize: 'normal',
    readingDifficulty: 'Intermediate',
    estimatedWordCount: 35000,

    shortDesc: 'Locke\'s final and most personal philosophical work — a practical guide to intellectual self-governance, identifying the habitual errors of the understanding and prescribing the disciplines required for rational inquiry.',

    summary: 'Of the Conduct of the Understanding was intended by Locke as an additional chapter for the Essay Concerning Human Understanding but grew beyond the proportions of a chapter and was left unfinished at his death. Published posthumously in 1706 by Peter King, it stands as the most personal and practically engaged of Locke\'s philosophical works — a kind of intellectual hygiene manual that identifies, with the clarity of a diagnostician, the characteristic ways in which human understanding goes wrong and prescribes the habits needed to correct them.\n\nLocke opens from the empiricist premise that the understanding, like the body, can be trained. Most people, he observes, use only a small part of the cognitive capacity they possess, not because of natural limitation but because they have formed habits of mind that prevent the full exercise of reason. The project of the Conduct is to identify these habits and replace them with better ones — a project that requires the same kind of patient, habituated education that the Thoughts Concerning Education recommends for the body and the character.\n\nThe errors Locke catalogs are remarkably comprehensive and remain recognizable. There is the error of the indifferent person — someone so committed to avoiding pain that they refuse to form any opinion where controversy threatens discomfort, and who thereby surrender their rational autonomy entirely to fashion and authority. There is the error of the person led by one principle — who, having found one great truth, applies it to everything and distorts every subject they touch to fit its mold. There is the error of the person who reads for citations rather than for understanding, accumulating authorities instead of forming views. There is the error of haste — forming conclusions before the evidence is adequate. There is the error of desultoriness — moving from subject to subject without the patience to master anything. Against all these, Locke recommends breadth (no one subject should exhaust the understanding), depth (no subject should be treated superficially), patience (argument requires time), independence (one\'s own reasons, not authorities, should ground one\'s views), and charity (one\'s opponents\' arguments should be understood in their strongest form before being answered).\n\nThe work concludes with a passage of characteristic Lockean modesty: the understanding has limits, and the wise person knows them. Many questions are beyond human resolution, and the mark of intellectual maturity is the ability to hold beliefs with degrees of conviction proportional to the evidence — neither asserting more confidently than the evidence warrants nor suspending judgment where reasonable evidence exists.',

    themes: ['Intellectual Virtue', 'Cognitive Errors', 'Rational Self-Governance', 'Habits of Mind', 'Independence of Thought', 'Against Authority', 'Proportioning Belief to Evidence', 'Intellectual Charity'],

    keyCharacters: [],

    concepts: [
        'The understanding as trainable — cognitive capacity can be cultivated or neglected, exactly like physical capacity',
        'Indifferency as intellectual vice — the refusal to form views is a surrender of rational autonomy, not a mark of balance',
        'The tyranny of one principle — the error of forcing every subject through a single master concept',
        'Citations vs understanding — the error of reading for authority rather than for comprehension',
        'Proportioning belief to evidence — the signature Lockean epistemic virtue: neither overclaiming nor underclaiming',
        'Breadth and depth — the understanding should range across many subjects while pursuing each with adequate patience'
    ],

    structure: '§1-5: Introduction — the understanding can be trained; the importance of early habituation.\n§6-25: Catalog of errors — indifferency, the tyranny of principles, partiality, following authority, haste, desultory reading, fundamentalism.\n§26-45: Positive prescriptions — breadth of reading, patience, independence, intellectual charity, the proportioning of belief.\n§46-end: The limits of knowledge and the proper response to uncertainty.',

    quote: 'We are all short-sighted, and very often see but one side of a matter; our views are not extended to all that has a connexion with it. From this defect I think no man is free. We see but in part, and we know but in part, and therefore it is no wonder we conclude not right from our partial views. — Of the Conduct of the Understanding, §3',

    additionalQuotes: [
        { text: 'Reading furnishes the mind only with materials of knowledge; it is thinking that makes what we read ours. A man who thinks much himself needs not many books.', citation: 'Of the Conduct of the Understanding, §20' }
    ],

    commentary: [
        {
            philosopher: 'John Stuart Mill',
            text: 'Mill acknowledged the Conduct as a significant predecessor of his own work on intellectual methods and the formation of good epistemic habits. In On Liberty (1859), Mill\'s argument that even a false opinion should be heard and engaged is a Lockean argument in spirit: only through the active confrontation of one\'s beliefs with the best available objections can those beliefs be genuinely known rather than merely held. Mill\'s system of logic and his essays on method are extended developments of the positive prescriptions Locke catalogues in the Conduct — breadth, depth, intellectual charity, the separation of what one believes from what one can prove. The Conduct also prefigures Mill\'s concern about the conformity pressure of Victorian opinion: Locke\'s indifferent person, who surrenders their judgment to fashion and authority, is a portrait of Mill\'s society of the herd.'
        },
        {
            philosopher: 'Harvey Siegel',
            text: 'Contemporary philosophy of education has drawn extensively on the Conduct as a foundational text in the theory of critical thinking. Siegel\'s Educating Reason (1988) identifies the proportioning of belief to evidence as the central intellectual virtue — what he calls the \'critical spirit\' — and traces its theoretical genealogy directly to Locke. The Conduct\'s catalog of cognitive errors anticipates the modern literature on cognitive biases in social psychology (the confirmation bias, the availability heuristic, the authority bias) and connects Locke\'s moral epistemology to contemporary empirical research on how humans actually reason. Siegel argues that the Conduct is, properly understood, the founding document of critical thinking as an educational ideal.'
        }
    ],

    modernRelevance: 'The Conduct reads as a remarkably accurate diagnosis of the epistemic pathologies of contemporary public discourse. The error of the person led by one principle — the ideologue who distorts every subject to fit their master concept — is pervasive in political culture. The error of accumulating citations rather than forming views is the characteristic intellectual vice of social media. The error of haste — drawing conclusions before the evidence is adequate — characterizes most public comment on every breaking story. Locke\'s prescriptions — patience, breadth, charity to opponents, proportioning of belief to evidence — are precisely what current educational systems most conspicuously fail to cultivate.',

    context: 'Locke began drafting the Conduct around 1697 as a proposed addition to the fourth edition of the Essay but set it aside unfinished. It was published two years after his death by his literary executor Peter King, who edited it from the manuscript preserved at Oates. Its immediate predecessor texts are the Essay\'s account of the degrees of assent and the chapter on the abuse of words. Its pedagogical companion is the Thoughts Concerning Education: the two works together constitute Locke\'s fullest account of how rational character should be formed.',

    relatedWorks: ['essay-concerning-human-understanding', 'some-thoughts-concerning-education', 'locke-correspondence']
}

);
"""

# ─────────────────────────────────────────────────────────────────────────────
# DATA-14e  —  Correspondence + Short Tract on Government
# ─────────────────────────────────────────────────────────────────────────────
data_14e = r"""/* ================================================================
   DATA PART 14e — Correspondence + Short Tract on Government + Paraphrase of St Paul
   ================================================================ */

window.WORKS.push(

/* ──────────────────────────────────────
   1. CORRESPONDENCE
────────────────────────────────────── */
{
    id: 'locke-correspondence',
    title: 'Correspondence',
    greekTitle: 'Correspondence',
    philosopher: 'locke',
    category: 'epistemology',
    categoryLabel: 'Letters',
    date: '1660–1704 AD',
    dateSort: 1680,
    emoji: '📬',
    cardSize: 'wide',
    readingDifficulty: 'Advanced',
    estimatedWordCount: 280000,

    shortDesc: 'Over three thousand letters spanning fifty years — the most extensive philosophical correspondence in English, documenting Locke\'s engagement with Molyneux, Stillingfleet, Newton, and the full intellectual life of the early Enlightenment.',

    summary: 'Locke\'s correspondence, collected in eight volumes in the Clarendon edition edited by E. S. de Beer (1976-1989), comprises over three thousand letters and is the most extensive epistolary record of any philosopher in the English language. It spans from Locke\'s student days at Christ Church through his political career in Shaftesbury\'s circle, his Dutch exile, and his final years at Oates, Essex, where he lived in the household of Lady Masham from 1691 until his death in 1704.\n\nThe most philosophically consequential exchanges are those with William Molyneux, the Dublin scientist and philosopher, whose friendship with Locke — conducted entirely by letter — is one of the most beautiful examples of philosophical friendship in the history of ideas. Molyneux had written enthusiastically praising the Essay when it first appeared, and their correspondence developed into an intimate intellectual partnership of extraordinary warmth and mutual regard. The exchange produced one of the most famous problems in the philosophy of perception: if a man born blind had learned to distinguish a sphere from a cube by touch, and were then given sight, would he be able — upon seeing them for the first time, before touching them — to identify which was the sphere and which the cube? Locke answered no: the ideas of sight and the ideas of touch are entirely distinct; without prior experience of their correlation, visual appearance cannot be identified with tactile shape. Molyneux agreed, and the problem he posed — which neither man lived to see empirically tested — has been a central test case in philosophy of perception, cognitive science, and neuroscience ever since. The premature death of Molyneux in 1698, at the age of forty-two, was a profound personal loss to Locke, who had described him as the friend who came nearest to what a friend should be.\n\nThe exchanges with Edward Stillingfleet, Bishop of Worcester, constitute the most philosophically important controversy generated by the Essay. Stillingfleet accused Locke\'s account of substance and his way of ideas of undermining the philosophical foundations of the doctrine of the Trinity and of personal identity at death. If we can predicate identity only on the basis of observable qualities rather than real essences, and if substance is merely an unknown substratum inferred from those qualities, then we have no philosophical means of asserting the numerical identity of Christ\'s resurrection body with his pre-death body, or of the three persons of the Trinity as one divine substance. Locke\'s three long replies are among the most carefully argued prose he ever wrote, clarifying the doctrines of the Essay — especially on substance, essence, and the limits of nominal definition — with a precision the original text had left ambiguous.\n\nLocke\'s correspondence with Isaac Newton reveals the deep intellectual connection between the two most important English thinkers of the seventeenth century. Both were committed to corpuscularian natural philosophy, both were systematically suspicious of scholastic essences and occult qualities, and both privately rejected Trinitarian orthodoxy. Newton sent Locke a manuscript paper arguing from scripture that the doctrine of the Trinity was a corruption introduced into the New Testament by deliberate interpolation — the \'Two Notable Corruptions of Scripture\' (1690). Locke agreed to explore having it published anonymously in France and corresponded with Jean le Clerc about the project; it ultimately did not proceed in Locke\'s lifetime. The correspondence documents a shared heterodoxy that neither man could publicly avow and that connects the two central achievements of the English Enlightenment — Newtonian physics and Lockean philosophy — at a level deeper than their public works reveal.\n\nAmong the most historically significant letters are those exchanged with Damaris Masham, the philosopher and theologian in whose household Locke spent his final years. Lady Masham was the daughter of Ralph Cudworth, the Cambridge Platonist, and a serious philosopher in her own right. Her correspondence with Locke — begun before she became Lady Masham, when she was Damaris Cudworth — engages with the problem of enthusiasm, the nature of divine love, and the relationship between reason and piety. Their intellectual friendship, combined with Locke\'s final years of quiet work at Oates, represents one of the most intimate and productive late-life collaborations between philosophers in the English tradition.',

    themes: ['Molyneux Problem', 'Philosophical Friendship', 'Stillingfleet Controversy', 'Newton and Heterodoxy', 'Substance and Identity', 'Cross-Modal Perception', 'Anti-Trinitarianism', 'Lady Masham', 'Philosophy of Perception', 'Intellectual Autobiography'],

    keyCharacters: [
        { name: 'William Molyneux', role: 'Dublin scientist, natural philosopher, and Locke\'s most intimate intellectual correspondent — author of the Molyneux problem; his death in 1698 was the deepest personal loss of Locke\'s later life' },
        { name: 'Edward Stillingfleet', role: 'Bishop of Worcester and Locke\'s most formidable theological critic — his objections forced the most precise clarifications of the Essay\'s doctrines of substance, identity, and essence' },
        { name: 'Isaac Newton', role: 'Friend and correspondent whose shared heterodoxy in natural philosophy, biblical criticism, and theology connects the two central figures of the English Enlightenment at a level their published works do not reveal' },
        { name: 'Damaris Masham', role: 'Philosopher and theologian in whose household Locke spent his final years — correspondent on reason, faith, and enthusiasm; the intellectual and personal center of Locke\'s last decade' },
        { name: 'Jean le Clerc', role: 'Dutch theologian and editor with whom Locke collaborated on the possibility of publishing Newton\'s anti-Trinitarian manuscript — a figure who connected the Arminian theological liberalism of Holland with the English heterodox tradition' }
    ],

    concepts: [
        'The Molyneux problem — can cross-modal perceptual identification occur without prior experience of sensory correlation?',
        'Locke\'s negative answer — visual ideas and tactile ideas are heterogeneous; prior experience of their conjunction is required for cross-modal recognition',
        'Substance and predication — the Stillingfleet exchanges force the most precise articulation of what Locke means by nominal essence and unknown substratum',
        'Shared heterodoxy — the correspondence with Newton documents the anti-Trinitarian convictions that both men held privately but could not publish',
        'Philosophical friendship as cognitive practice — Locke\'s correspondence with Molyneux as a model of how rigorous intellectual exchange advances understanding'
    ],

    structure: 'The correspondence is organized chronologically in the Clarendon edition (8 volumes). Key clusters: the Oxford period (1660-1666); the Shaftesbury circle (1667-1682); the Dutch exile (1683-1689); the Molyneux correspondence (1692-1698); the Stillingfleet controversy (1696-1699); the Newton exchange (1690-1704); the Masham years at Oates (1691-1704).',

    quote: 'I no sooner perceived myself in the world, but I found myself in a storm which lasted till almost hitherto. The shore being smooth and the harbour quiet, I am willing to take a little rest. — Locke to Molyneux, 1698, written shortly before Molyneux\'s death',

    additionalQuotes: [
        { text: 'I think I may say that of all the men I know, you come nearest to what, in my opinion, a friend should be; and I am proud that I know one such man, were it only to satisfy myself that nature makes such.', citation: 'Locke to Molyneux, August 28, 1693' },
        { text: 'He that considers how hardly naked, unassisted reason unbiassed by interest, passion, custom or education, finds out moral rules, will less wonder that the generality of mankind receive them from others.', citation: 'Locke to Molyneux, March 30, 1696' }
    ],

    commentary: [
        {
            philosopher: 'Gottfried Wilhelm Leibniz',
            text: 'Leibniz followed the Molyneux problem with intense interest, proposing what he called an intermediate position: a person born blind who had learned to distinguish sphere from cube by touch could, upon gaining sight, reason out which was which from the known relationship between the two shapes, provided they were clearly seen. Leibniz\'s argument is that the geometry of the two shapes — the uniform surface of the sphere, the edges and faces of the cube — is the same whether apprehended by sight or touch, because spatial relations are grasped by reason, not merely by individual sense modalities. This rationalist response to a problem posed by two empiricists captures the essential disagreement between the two traditions: for Leibniz, reason provides a cross-modal common currency; for Locke and Molyneux, the senses are genuinely distinct channels whose outputs must be correlated by experience.'
        },
        {
            philosopher: 'George Berkeley',
            text: 'Berkeley\'s New Theory of Vision (1709) is the most direct and important philosophical response to the Molyneux problem, and it vindicates Locke\'s negative answer through an entirely new philosophical framework. Berkeley argued that the objects of sight and the objects of touch are not merely different experiences of the same world but heterogeneous and in no way intrinsically connected. Visible space and tangible space are different spaces — the three-dimensional spatial world we experience is a construction built up through habituated association between visual signs and tactile realities, not an inherent property of vision itself. Therefore a newly sighted person would see only a confused field of color and light with no spatial depth and could not identify visual shapes with tangible ones. Berkeley extended this to argue that the visual world is a divine language — a system of signs God uses to inform finite minds about the tangible world they must navigate.'
        },
        {
            philosopher: 'Richard Held and Alan Hein',
            text: 'The Molyneux problem was first empirically addressed by Held\'s experiments in the 1960s on kittens raised with restricted visual experience, and more directly by studies of patients who had congenital cataracts surgically removed. A landmark study by Held, Ostrovsky, and colleagues (2011) tested five patients in India who had undergone sight-restoration surgery. The results broadly supported Locke\'s negative answer: patients showed initial inability to identify by sight objects familiar to them through touch, requiring time and tactile confirmation before cross-modal recognition was established. However, the picture was more complex than Locke anticipated: some limited cross-modal transfer did appear, suggesting that the heterogeneity of sight and touch is real but not absolute. The empirical confirmation of a philosophical hypothesis posed in a philosophical correspondence 320 years earlier is one of the most remarkable episodes in the history of ideas.'
        },
        {
            philosopher: 'Maurice Cranston',
            text: 'Cranston\'s biography John Locke: A Biography (1957) remains the standard life and drew extensively on the correspondence to reconstruct both the intellectual and the personal Locke. Cranston showed that the letters reveal a Locke significantly different from the careful, measured public philosopher of the published works: warmer, more anxious, more loyal, more politically engaged, and more candid about his private theological heterodoxy. The correspondence with Newton in particular, which Cranston was among the first to analyze carefully, establishes that Locke\'s religious views were considerably more radical than the published Reasonableness of Christianity suggests. Cranston\'s Locke is a man who maintained a public persona of carefully calibrated moderation while privately holding views on the Trinity, on revelation, and on political resistance that were far more unorthodox.'
        }
    ],

    modernRelevance: 'The Molyneux problem has become a standard test case in philosophy of mind, philosophy of perception, and cognitive neuroscience. The 2011 Held study brought it into the laboratory after three centuries of philosophical speculation. The problem connects to foundational questions in cognitive science about whether spatial cognition is modality-specific or supramodal, whether cross-modal transfer is learned or built in, and whether perceptual representations are amodal (format-independent) or tied to specific sensory systems. The Stillingfleet exchanges remain philosophically important for anyone interested in the relationship between empiricist philosophy of language and the metaphysics of substance and identity.',

    context: 'The complete correspondence was published by E. S. de Beer for the Clarendon Press in eight volumes (1976-1989). Earlier partial editions had given scholars access to some letters, but de Beer\'s edition transformed the field by making the full epistolary record available for the first time. The correspondence constitutes an intellectual autobiography that supplements and in many ways corrects the portrait available from the published works alone.',

    relatedWorks: ['essay-concerning-human-understanding', 'two-treatises-of-government', 'reasonableness-of-christianity']
},

/* ──────────────────────────────────────
   2. SHORT TRACT ON GOVERNMENT
────────────────────────────────────── */
{
    id: 'short-tract-on-government',
    title: 'Short Tract on Government',
    greekTitle: 'Short Tract on Government',
    philosopher: 'locke',
    category: 'political',
    categoryLabel: 'Political Philosophy',
    date: '1660 AD',
    dateSort: 1660,
    emoji: '📋',
    cardSize: 'normal',
    readingDifficulty: 'Advanced',
    estimatedWordCount: 20000,

    shortDesc: 'Locke\'s earliest political work — an unpublished defense of absolute governmental authority over religious practices that stands in stark contrast to his mature liberalism, documenting a dramatic intellectual transformation over three decades.',

    summary: 'The Short Tract on Government of 1660 is Locke\'s first political writing and one of the most philosophically and biographically significant documents in his entire corpus — because it argues, with considerable sophistication, for precisely the position that his mature philosophy most powerfully opposes. Written in the immediate aftermath of the Restoration of Charles II, at a moment when the collapse of the Parliamentary cause had made the dangers of religious and political disorder vividly apparent to Locke, the Short Tract defends the absolute right of the civil magistrate to determine and enforce outward religious practices within his territory.\n\nThe argument is the mirror image of the Letter Concerning Toleration. Where the Letter insists that the magistrate\'s authority extends only to civil goods and has no reach over religious belief or practice, the Short Tract argues that the magistrate has full authority to regulate indifferent things — things neither commanded nor forbidden by scripture — including religious ceremonies, church governance, and public worship. The reasoning is Hobbesian in spirit: in the post-war, post-Commonwealth chaos of 1660, the greatest threat to human welfare is not the overreach of authority but the fragmentation of authority that produces civil disorder. An absolute sovereign power in matters of religion is the price of peace.\n\nThe transformation from the Short Tract to the Letter Concerning Toleration represents one of the most dramatic intellectual journeys in the history of philosophy. Over three decades, Locke moved from arguing that the magistrate should have full authority over religious practices to arguing that the magistrate has no authority over them whatsoever — from defending the absolute Restoration settlement to providing the philosophical foundations of the Glorious Revolution. The journey was shaped by his years in Shaftesbury\'s circle, his direct experience of the persecution of Nonconformists and the cynical manipulation of religious politics by the Crown, his reading of Bayle and other tolerationists in Holland, and the philosophical development of the empiricist epistemology of the Essay, which provided new grounds for denying the magistrate access to the inner life.',

    themes: ['Early Political Thought', 'Magistrate\'s Authority', 'Indifferent Things', 'Religious Conformity', 'Civil Order vs Liberty', 'Intellectual Development', 'Hobbes\'s Influence', 'The Pre-Liberal Locke'],

    keyCharacters: [],

    concepts: [
        'Indifferent things — religious practices neither commanded nor forbidden by scripture, over which the magistrate may legislate',
        'Absolute authority in religion — the magistrate\'s power extends to all outward religious practice for the sake of civil order',
        'The priority of peace over liberty — the young Locke\'s Hobbesian moment, grounded in the experience of civil war',
        'The dramatic reversal — the contrast with the Letter Concerning Toleration documents the full arc of Locke\'s political thought'
    ],

    structure: 'Part 1: Against the claim that the magistrate has no authority over indifferent religious matters.\nPart 2: Positive argument — indifferent things fall within the magistrate\'s lawful jurisdiction.\nPart 3: Objections answered — on conscience, scripture, and the limits of obedience.',

    quote: 'Conscience, being nothing else but our own opinion or judgment of the moral rectitude or pravity of our own actions, it is clear that it is not this that gives them their obligation. — Short Tract on Government, 1660',

    additionalQuotes: [
        { text: 'The question is not whether submission to civil authority in religious matters is always right, but whether the alternative — every individual\'s conscience as its own supreme court — is compatible with any stable civil order.', citation: 'Short Tract on Government, 1660 (paraphrase of the argumentative position)' }
    ],

    commentary: [
        {
            philosopher: 'John Dunn',
            text: 'Dunn\'s analysis of the Short Tract in The Political Thought of John Locke showed that the work is not a confused youthful aberration but a serious and coherent response to the particular political crisis of 1659-1660. The collapse of the Protectorate and the restoration of the monarchy seemed to many moderate Englishmen to demonstrate the catastrophic danger of taking religious conscience as the supreme political authority. Locke\'s Short Tract is a carefully reasoned defense of political order against religious fragmentation — and its reversal in the mature toleration writings is not the abandonment of political reasoning but its development in light of new evidence. The persecution of Nonconformists under the Clarendon Code, which Locke witnessed directly, demonstrated that enforced conformity produced exactly the disorder it was designed to prevent, undermining the very premise of the Short Tract\'s argument.'
        },
        {
            philosopher: 'Richard Ashcraft',
            text: 'Ashcraft\'s Revolutionary Politics and Locke\'s Two Treatises of Government (1986) placed the transformation from the Short Tract to the mature works in the context of Locke\'s increasingly radical political engagement in Shaftesbury\'s circle during the 1670s and early 1680s. Ashcraft showed that Locke was not merely a theoretical philosopher responding to abstract arguments but a political activist whose thinking was shaped by direct engagement with the repressive policies of the Restoration government. The Short Tract was written by a man who feared disorder; the Two Treatises and the Letter were written by a man who had experienced repression and exile and who understood that the greatest threat to human welfare was not popular disorder but governmental tyranny.'
        }
    ],

    modernRelevance: 'The Short Tract is important as a reminder that liberal political philosophy is not a natural or inevitable position but a historical achievement — the product of specific experiences of oppression and specific philosophical arguments worked out over decades. The young Locke\'s authoritarian position on religious conformity is not simply wrong-headed: it reflects a genuine tension, which liberal political philosophy has never fully resolved, between the value of individual conscience and the requirements of public order. Contemporary debates about the limits of religious exemptions from civil law, the accommodation of radical religious communities in liberal democracies, and the clash between individual rights and civic obligations are all negotiating the same tension that Locke himself negotiated over thirty years.',

    context: 'The Short Tract was composed in late 1660 or early 1661, most probably in response to a pamphlet by Edward Bagshawe arguing that the magistrate had no authority over indifferent religious practices. Locke never published it and appears to have kept it private throughout his life. It was first discovered and published by W. von Leyden as part of his work on Locke\'s early manuscripts, included in his edition Essays on the Law of Nature (1954). Its existence was a major discovery for Locke scholarship, establishing that Locke\'s liberalism was not a constant position but a hard-won intellectual achievement.',

    relatedWorks: ['letter-concerning-toleration', 'two-treatises-of-government', 'questions-law-of-nature']
}

);
"""

files = {
    'data-14a.js': data_14a,
    'data-14b.js': data_14b,
    'data-14c.js': data_14c,
    'data-14d.js': data_14d,
    'data-14e.js': data_14e,
}

for filename, content in files.items():
    path = os.path.join(js_dir, filename)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    lines = content.count('\n')
    print(f"  Written {filename}  —  {lines} lines  →  {path}")

print("\nAll Locke files complete. Verify with:")
print("  wc -l js/data-14a.js js/data-14b.js js/data-14c.js js/data-14d.js js/data-14e.js")
