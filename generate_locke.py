#!/usr/bin/env python3
"""Run this from inside ~/Desktop/philosophy-archive/ to generate Locke data files."""
import os

js_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'js')
os.makedirs(js_dir, exist_ok=True)

# ── data-14a.js ── Essay Concerning Human Understanding ─────────────────────
data_14a = r"""window.WORKS.push(

{
    id: 'essay-human-understanding',
    title: 'An Essay Concerning Human Understanding',
    greekTitle: 'Essay Concerning Human Understanding',
    philosopher: 'locke',
    category: 'method',
    categoryLabel: 'Epistemology',
    date: '1689 AD',
    dateSort: 1689,
    emoji: '🕯',
    cardSize: 'wide',
    readingDifficulty: 4,
    estimatedWordCount: 340000,
    shortDesc: 'The founding text of British empiricism — Locke\'s systematic investigation into the origin, extent, and limits of human knowledge, and the most influential work in the English philosophical tradition.',
    summary: 'The Essay Concerning Human Understanding is one of the great founding documents of modern philosophy and the text that set the terms of epistemological debate for the following two centuries. Locke spent nearly twenty years composing it — he began drafts in 1671 following a conversation with friends about morality and religion in which it became clear, as he wrote, that they could make no progress until they had examined their own capacities and discovered what objects their understandings were and were not fitted to deal with. The Essay is thus at its core a work of philosophical therapy: before asking what we can know, we must understand how we come to know anything at all, what kind of instrument the human mind is, and where its natural limits lie.\n\nThe first book is a sustained assault on the doctrine of innate ideas — the claim, associated by Locke with Descartes and the scholastics, that the mind comes into existence equipped with prior knowledge of certain principles. Locke argues against this on multiple fronts: there is no universal assent to any claimed innate principle; any alleged innate principle can be shown to require prior knowledge and experience before it is understood; and the whole doctrine of innateness is unnecessary, since Locke proposes to account for all our ideas through experience alone. Book I clears the ground for the constructive account that follows.\n\nBook II, the longest and richest section, develops Locke\'s positive theory of ideas. The mind at birth is a white paper, void of all characters, without any ideas. All ideas derive from experience, which comes in two forms: sensation — the operation of external objects on our senses, producing simple ideas like yellow, hard, sweet, warm — and reflection — the mind\'s observation of its own internal operations, producing ideas like thinking, doubting, willing, knowing. Simple ideas are the atoms of Lockean epistemology: we are entirely passive in receiving them, and we cannot create or destroy them but only recombine them. Complex ideas are built up from simple ideas through combination, comparison, and abstraction. Here Locke introduces the celebrated distinction between primary qualities — solidity, extension, figure, motion, and number, which exist in bodies themselves and whose ideas resemble their causes — and secondary qualities — colour, sound, taste, smell, and warmth, which are powers in objects to produce ideas in us that in no way resemble anything in the objects themselves. This distinction, rooted in the corpuscularian physics of Boyle and Newton, sets up the problem of the external world that will preoccupy Berkeley and Hume.\n\nBook III turns to language and is one of the earliest systematic treatments of the philosophy of language in the Western tradition. Locke argues that words stand for ideas in the mind of the speaker and that much philosophical confusion arises from the abuse of words. His account of nominal essence — what defines the application of a general term — versus real essence — the unknown corpuscular structure that actually produces a thing\'s observable properties — introduces a distinction that Kripke and Putnam directly engage in their work on natural kinds and reference.\n\nBook IV addresses knowledge itself, which Locke defines strictly as the perception of the agreement or disagreement between ideas. On this definition, genuine knowledge is far narrower than we might hope: we have intuitive knowledge of our own existence, demonstrative knowledge of mathematical truths and of God\'s existence, and sensitive knowledge of the existence of external objects — but this last is the most uncertain kind. For most of what we believe about the world, we must settle for probability and judgement rather than knowledge in the strict sense.',
    themes: ['empiricism', 'origin of ideas', 'sensation and reflection', 'primary and secondary qualities', 'substance and identity', 'language and meaning', 'degrees of knowledge', 'probability and judgement', 'critique of innatism', 'nominal vs real essence'],
    keyCharacters: [],
    concepts: [
        'Blank slate (tabula rasa) — the mind at birth contains no innate ideas; all content comes from experience',
        'Simple and complex ideas — simple ideas are received passively from sensation and reflection; complex ideas are built from them by the mind',
        'Primary qualities — figure, solidity, extension, motion, number — whose ideas resemble the qualities themselves in bodies',
        'Secondary qualities — colour, sound, taste, warmth — powers in objects to produce ideas bearing no resemblance to the objects',
        'Substance as unknown substratum — we posit substance as the support of qualities but have no clear idea of it in itself',
        'Nominal essence vs real essence — what defines our use of a term vs the unknown internal constitution of the thing',
        'Knowledge as perception of agreement between ideas — strictly limited to intuition, demonstration, and sensitive knowledge',
        'Probability as the guide of life — in the absence of knowledge, rational judgement weighs evidence and authority',
        'Personal identity — consisting in the continuity of consciousness and memory, not of substance',
        'Abuse of words — the source of most philosophical darkness: equivocation, obscure terms, taking words for things'
    ],
    structure: 'Book I: Neither Principles Nor Ideas Are Innate\nBook II: Of Ideas — origin, composition, space, time, power, identity\nBook III: Of Words — general terms, names of substances, abuse of language\nBook IV: Of Knowledge and Probability — degrees of knowledge, God, the external world, reason and faith',
    quote: 'Let us then suppose the mind to be, as we say, white paper, void of all characters, without any ideas: how comes it to be furnished? Whence has it all the materials of reason and knowledge? To this I answer, in one word, from experience.',
    additionalQuotes: [
        { text: 'Since the mind, in all its thoughts and reasonings, hath no other immediate object but its own ideas, it is evident that our knowledge is only conversant about them.', source: 'Essay, Book IV, Chapter 1' },
        { text: 'Our faculties are not fitted to penetrate into the internal fabric and real essences of bodies; and their several constitutions, on which their properties depend, are concealed from us.', source: 'Essay, Book IV, Chapter 3' },
        { text: 'The candle that is set up in us shines bright enough for all our purposes.', source: 'Essay, Book I, Chapter 1' },
        { text: 'General and universal belong not to the real existence of things; but are the inventions and creatures of the understanding, made by it for its own use.', source: 'Essay, Book III, Chapter 3' }
    ],
    commentary: [
        { philosopher: 'Hume', text: 'Locke is the first philosopher who ventured to give a particular account of the original of all our notions and ideas. He is the father of modern epistemology. His project — the mapping of the mind\'s contents by empirical investigation — remains the only honest one.' },
        { philosopher: 'Leibniz', text: 'Locke\'s Essay is a work of great merit and learning, but it errs in treating the mind as entirely passive and in giving no account of why necessary truths — the truths of logic and mathematics — could ever be derived from mere experience, which furnishes nothing but contingent facts.' },
        { philosopher: 'Kant', text: 'Locke attempted a physiology of the human understanding — a natural history of the mind\'s acquisitions. He did not ask whether these acquisitions were valid but only how they arose. That question — of validity, not of origin — is what the Critique addresses.' },
        { philosopher: 'Voltaire', text: 'So many reasoners having written the romance of the soul, a sage has arrived who has modestly written its history. Locke has set forth human reason just as an excellent anatomist explains the springs of the human body.' },
        { philosopher: 'Berkeley', text: 'Locke allowed that we have no idea of substance — that we posit it as an unknown substratum without being able to say what it is. I accept his premise and draw the conclusion he refused: there is no material substance, only minds and ideas.' },
        { philosopher: 'Chomsky', text: 'Locke\'s empiricism reaches its limits when confronted with language acquisition. The child acquires a generative grammar of infinite expressive power from finite and fragmentary input — this poverty of the stimulus is inexplicable without innate structure of exactly the kind Locke denied.' }
    ],
    modernRelevance: 'The Essay defined the terms of the empiricism-rationalism debate that Kant would resolve. Its primary-secondary quality distinction structured philosophy of perception from Berkeley and Hume through the present. Its account of personal identity as consisting in continuity of consciousness rather than continuity of substance became the starting point for every subsequent discussion — from Hume through Parfit. Its philosophy of language — words as signs of ideas, nominal essences as creatures of the understanding — was the dominant view until Frege, and the distinction between nominal and real essence prefigures the Kripke-Putnam revolution in philosophy of language.',
    context: 'Locke began thinking through the questions of the Essay in 1671, in conversations with a group of friends that included the physician Thomas Sydenham and the politician Anthony Ashley Cooper, later the first Earl of Shaftesbury. He composed drafts over the following years while also working as a physician, political adviser, and eventually exile in Holland (1683-1689), fleeing England after his association with the Rye House Plot. The Essay was published in 1689, the same year as the Two Treatises of Government and the Letter Concerning Toleration — a remarkable triptych issued in the aftermath of the Glorious Revolution. It went through four editions in Locke\'s lifetime and immediately became the dominant work of English-language philosophy, shaping Berkeley, Hume, the Scottish Enlightenment, and through Voltaire the entire French Enlightenment.',
    relatedWorks: ['two-treatises-government', 'letter-toleration']
}

);
"""

# ── data-14b.js ── Two Treatises + Letter on Toleration ─────────────────────
data_14b = r"""window.WORKS.push(

{
    id: 'two-treatises-government',
    title: 'Two Treatises of Government',
    greekTitle: 'Two Treatises of Government',
    philosopher: 'locke',
    category: 'practical',
    categoryLabel: 'Political Philosophy',
    date: '1689 AD',
    dateSort: 1689,
    emoji: '⚖️',
    cardSize: 'normal',
    readingDifficulty: 3,
    estimatedWordCount: 120000,
    shortDesc: 'The philosophical foundation of liberal democracy — Locke\'s demolition of divine-right monarchy and his argument that legitimate government rests on natural rights, consent, and the right to revolution.',
    summary: 'The Two Treatises of Government is the most politically consequential work of seventeenth-century philosophy and one of the foundational documents of liberal democratic theory. Published anonymously in 1689, it was composed at least in part during the early 1680s in the charged atmosphere of the Exclusion Crisis, when Locke\'s patron the Earl of Shaftesbury was organising parliamentary opposition to the Catholic succession of James II.\n\nThe First Treatise is a meticulous demolition of Sir Robert Filmer\'s Patriarcha, which had argued that kings derive absolute authority from Adam\'s God-given dominion transmitted through the biblical patriarchs to contemporary monarchs. Locke destroys this systematically: Adam had no such dominion; even if he had, there is no way to trace the chain of inheritance to any living monarch; and the argument, even if successful, would justify only one legitimate ruler in the world at a given time, making every actual government except one an usurpation.\n\nThe Second Treatise is among the most influential works of political philosophy ever written. Locke begins from a state of nature — not Hobbes\'s war of all against all, but a condition of natural freedom and equality governed by natural law, which reason teaches every human being who will but consult it: that no one ought to harm another in their life, health, liberty, or possessions. In this state of nature every person has executive power to enforce the natural law. The problem is that self-interest corrupts this private enforcement. Political society emerges when individuals consent to surrender this private executive power to a common authority — the government — which acts as impartial judge. Crucially, the consent that founds political authority does not alienate natural rights: it secures them more reliably. Government is a trust, not an absolute transfer of power.\n\nLocke\'s theory of property, developed in chapter five, is one of the most discussed passages in the history of political thought. He argues that in the state of nature, individuals acquire property by mixing their labour with unowned natural resources. The labour theory of property acquisition is qualified by the Lockean proviso: appropriation is legitimate only so long as there is enough, and as good, left for others.\n\nThe treatise culminates in the theory of dissolution of government: when the legislature betrays its trust by invading the property, liberty, or lives of the citizens, the government is dissolved and the people recover the original power to constitute a new one. This doctrine of the right to revolution became the philosophical justification for the American Revolution of 1776, whose Declaration of Independence draws directly on Locke\'s framework of natural rights, consent, and the right to alter or abolish government.',
    themes: ['natural rights', 'state of nature', 'consent and legitimacy', 'property and labour', 'separation of powers', 'limited government', 'right to revolution', 'dissolution of government', 'critique of absolute monarchy'],
    keyCharacters: [
        { name: 'Sir Robert Filmer', role: 'Author of Patriarcha — the target of the First Treatise. His divine-right absolutism, derived from Adam\'s biblical dominion, was the dominant theory of royal authority in Restoration England.' }
    ],
    concepts: [
        'Natural rights to life, liberty, and estate — pre-political rights that government exists to protect, not to create',
        'State of nature — a condition of natural freedom and equality governed by the law of reason, not war',
        'Consent as the only legitimate source of political authority',
        'Labour theory of property — mixing one\'s labour with unowned resources creates ownership',
        'The Lockean proviso — appropriation is legitimate only when enough and as good is left for others',
        'Government as trust — power held conditionally, forfeited when the trust is violated',
        'Dissolution of government — the people\'s right to reclaim constituent power when government betrays its charge',
        'Tacit consent — ongoing residence and use of governmental benefits as a form of consent to authority'
    ],
    structure: 'First Treatise: refutation of Filmer\'s Patriarcha chapter by chapter\nSecond Treatise, Ch.1–5: the state of nature, natural law, and the origin of property\nSecond Treatise, Ch.6–9: paternal power, political society, purposes of government\nSecond Treatise, Ch.10–15: forms of government, subordination of powers, prerogative\nSecond Treatise, Ch.16–19: conquest, usurpation, tyranny, and dissolution of government',
    quote: 'Whensoever the legislators endeavour to take away and destroy the property of the people, or to reduce them to slavery under arbitrary power, they put themselves into a state of war with the people, who are thereupon absolved from any farther obedience.',
    additionalQuotes: [
        { text: 'The state of nature has a law of nature to govern it, which obliges every one: and reason, which is that law, teaches all mankind, that being all equal and independent, no one ought to harm another in his life, health, liberty, or possessions.', source: 'Second Treatise, Chapter 2' },
        { text: 'Wherever law ends, tyranny begins.', source: 'Second Treatise, Chapter 18' }
    ],
    commentary: [
        { philosopher: 'Jefferson', text: 'Bacon, Locke, and Newton — I consider them as the three greatest men that have ever lived, without exception, and as having laid the foundation of those superstructures which have been raised in the physical and moral sciences.' },
        { philosopher: 'Rousseau', text: 'Locke\'s consent theory is more profound than Hobbes but still fails to account for the general will. Locke\'s individuals never truly become a people — they remain a collection of private proprietors who form government to protect what they already have.' },
        { philosopher: 'Nozick', text: 'Locke\'s labour theory of acquisition and his theory of just transfer are the foundations of libertarian political philosophy. The state is justified only insofar as it protects natural rights to life, liberty, and property; redistribution is a form of forced labour.' }
    ],
    modernRelevance: 'The Two Treatises is the direct ancestor of modern liberal constitutionalism. Jefferson\'s invocation of unalienable rights to life, liberty, and the pursuit of happiness, and the right to alter or abolish government, is Lockean thought translated into political founding document. Contemporary debates about the legitimacy of revolution, civil disobedience, the limits of state power, and the grounds of political obligation are conducted within the terms Locke defined in 1689.',
    context: 'The orthodox view, established by Peter Laslett, dates the Second Treatise to the Exclusion Crisis of 1679-1682, making it a justification for resistance to Stuart absolutism rather than a post-hoc rationalisation of the Glorious Revolution. Locke carried the manuscript to Holland during his exile and brought it back to England on the same ship as the Princess of Orange in February 1689. It was published later that year, in the same remarkable season as the Essay and the Letter Concerning Toleration. Locke never acknowledged authorship; the attribution was made definitively only after his death.',
    relatedWorks: ['letter-toleration', 'essay-human-understanding']
},

{
    id: 'letter-toleration',
    title: 'A Letter Concerning Toleration',
    greekTitle: 'Epistola de Tolerantia',
    philosopher: 'locke',
    category: 'practical',
    categoryLabel: 'Political Philosophy',
    date: '1689 AD',
    dateSort: 1689,
    emoji: '✉️',
    cardSize: 'normal',
    readingDifficulty: 3,
    estimatedWordCount: 22000,
    shortDesc: 'The first systematic philosophical argument for religious toleration — separating the coercive power of the state from the spiritual authority of the church, and arguing that forced belief is both philosophically impossible and politically illegitimate.',
    summary: 'The Letter Concerning Toleration, written in Latin in Holland in 1685 and published in English translation in 1689, is the foundational text of the modern doctrine of religious liberty and the separation of church and state. It was composed during Locke\'s exile in Amsterdam, in the aftermath of the Revocation of the Edict of Nantes by Louis XIV, which expelled hundreds of thousands of French Protestants and sent shockwaves across Protestant Europe.\n\nLocke\'s central argument is built on a rigorous distinction between the business of the state and the business of the church. The state is a society of men constituted for the procuring, preserving, and advancing of their own civil interests — life, liberty, health, and the possession of external things. The church is a voluntary society of men joining together of their own accord to worship God in a manner they judge acceptable to him. These two institutions have entirely different jurisdictions, and confusion between them is the source of all religious persecution. The magistrate\'s authority extends only to civil goods; he has no authority over souls.\n\nFirst, souls were not committed to the magistrate\'s charge by God or by the consent of their owners. The care of each man\'s soul belongs to himself alone. Second — and this is Locke\'s most distinctive argument — coercion cannot produce the belief required for salvation even in principle. Genuine religious belief requires inner conviction; outward conformity forced by penalty produces only hypocrisy. A man who adopts a religion because the magistrate commands it has no reason to think that religion is true, and a false religion observed under compulsion saves no one. Therefore religious persecution is not merely tyrannous but self-defeating on its own terms: it cannot produce the salvation it claims to seek.\n\nLocke draws two notable exceptions to his toleration principle. Atheists cannot be tolerated because they have no fear of divine punishment and therefore cannot be trusted to keep oaths, which are the basis of civil society. Catholics — though Locke does not name them explicitly — cannot be tolerated if their religious allegiance requires political submission to a foreign power. These exceptions have been extensively criticised by subsequent liberal theorists as inconsistent with the principles of the Letter itself.',
    themes: ['separation of church and state', 'religious liberty', 'limits of state authority', 'voluntarism in religion', 'coercion and belief', 'civil goods vs salvation', 'natural rights', 'limits of toleration'],
    keyCharacters: [
        { name: 'Philip van Limborch', role: 'Dutch Remonstrant theologian and Locke\'s close friend in Holland — the addressee of the letter and a key figure in the Dutch intellectual community of religious moderates that sheltered Locke during his exile' }
    ],
    concepts: [
        'Church as voluntary society — membership must be free; no legitimate church compels adherence',
        'Separation of civil and spiritual jurisdiction — the magistrate\'s power extends only to civil goods, never to souls',
        'Coercion cannot produce genuine belief — forced outward conformity is not the inner conviction salvation requires',
        'Mutual toleration as the chief mark of the true church',
        'The asymmetry of dissent — the persecuting church, not the dissenting congregation, is the source of civil disorder'
    ],
    structure: 'Part 1: The distinction between the magistrate\'s power and the care of souls\nPart 2: The nature of the church as a voluntary society\nPart 3: The limits of the magistrate\'s authority in religious matters\nPart 4: The duty of toleration among churches\nPart 5: The exceptions — atheists and those whose religion is politically subversive',
    quote: 'The care of souls cannot belong to the civil magistrate, because his power consists only in outward force; but true and saving religion consists in the inward persuasion of the mind, without which nothing can be acceptable to God.',
    additionalQuotes: [
        { text: 'Nobody is born a member of any church; otherwise the religion of parents would descend unto children by the same right of inheritance as their temporal estates.', source: 'Letter Concerning Toleration' },
        { text: 'It is not the diversity of opinions, which cannot be avoided, but the refusal of toleration to those that are of different opinions, which has produced all the bustles and wars in the Christian world upon account of religion.', source: 'Letter Concerning Toleration' }
    ],
    commentary: [
        { philosopher: 'Rawls', text: 'Locke is the originator of liberal toleration. His argument that the state has no jurisdiction over salvation — because coercion cannot produce genuine belief — remains the most powerful single argument for religious liberty ever given. His exceptions, however, reveal that he had not yet fully separated political authority from a particular religious conception of the good.' },
        { philosopher: 'Voltaire', text: 'Read the admirable letter on toleration by Locke. If you are a Christian, answer him. He asks only that Christians should not devour each other.' }
    ],
    modernRelevance: 'The Letter\'s distinction between civil and religious jurisdiction is the philosophical foundation of every modern constitutional settlement that separates church from state. The First Amendment\'s establishment and free exercise clauses, the European Convention on Human Rights\' protection of freedom of religion, and international human rights law\'s guarantee of freedom of conscience all implement the Lockean principle that the state has no legitimate authority over the inner life of its citizens.',
    context: 'Locke wrote the Letter in Amsterdam in the winter of 1685-1686. The Revocation of the Edict of Nantes had just expelled the Huguenots from France. Locke wrote in Latin to give the argument maximum European reach. Limborch had it published in Gouda in 1689. It was immediately translated into English by William Popple and published in London the same year. Locke published three further letters on toleration in subsequent years in response to critics, but the first Letter remains the canonical statement.',
    relatedWorks: ['two-treatises-government', 'essay-human-understanding']
}

);
"""

# ── data-14c.js ── Education + Reasonableness + Correspondence ───────────────
data_14c = r"""window.WORKS.push(

{
    id: 'some-thoughts-education',
    title: 'Some Thoughts Concerning Education',
    greekTitle: 'Some Thoughts Concerning Education',
    philosopher: 'locke',
    category: 'practical',
    categoryLabel: 'Education and Ethics',
    date: '1693 AD',
    dateSort: 1693,
    emoji: '📚',
    cardSize: 'normal',
    readingDifficulty: 2,
    estimatedWordCount: 65000,
    shortDesc: 'The most widely read pedagogical work of the Enlightenment — Locke\'s empiricist theory of education applied to the formation of a rational, virtuous, and practically competent English gentleman.',
    summary: 'Some Thoughts Concerning Education grew out of letters Locke wrote to his friend Edward Clarke in the 1680s, advising him on the upbringing of his son. Expanded and published in 1693, it became one of the most influential educational treatises in European history, translated into French, German, Dutch, Swedish, and Italian. Rousseau\'s Émile (1762), which is both deeply indebted to and explicitly in reaction against Locke, cannot be understood without it.\n\nThe work\'s governing principle is a direct application of the empiricism of the Essay: the child\'s mind is a blank slate, formed entirely by experience. Education is therefore the most important thing that can be done for and to a human being — the infant who will become a rational adult is being written upon from the first moment of its life by everything it sees, hears, and is made to do. Locke\'s priorities are surprising to modern readers: he places physical hardening and the cultivation of virtue before academic instruction, arguing that a sound mind in a sound body is the sum of a happy man in this world. The child should be accustomed to cold baths, thin shoes, plain food, and early rising not through punishment but through habit formed before the age of reason hardens dispositions in the wrong direction.\n\nVirtue, for Locke, consists above all in self-denial — the ability to resist one\'s own desires and appetites when reason counsels otherwise. This capacity for rational self-governance is the foundation of every other excellence, and it must be instilled early, before desires have consolidated into habits. Crucially, Locke opposes corporal punishment as the primary instrument of discipline: it produces servile children who obey only under threat and cannot govern themselves when the threat is removed. The better instrument is the management of the child\'s desire for esteem — praise and disgrace, applied by parents who are respected and loved rather than feared, shape character more durably than the rod.\n\nOn curriculum, Locke is rigorously practical. Latin grammar learned by rote is a waste of time that could be spent learning French through conversation, arithmetic through application, and geography through maps. He recommends instead history, ethics, civil law, natural philosophy, and above all the ability to express oneself clearly in English — the one skill that is most needed and least taught.',
    themes: ['blank slate and education', 'habit formation', 'virtue as self-denial', 'corporal punishment vs rational discipline', 'curriculum reform', 'education of desire and esteem', 'practical vs classical learning'],
    keyCharacters: [
        { name: 'Edward Clarke', role: 'The Somerset gentleman to whose practical questions about child-rearing the work was originally addressed — the concrete, particular origin of one of the most general educational treatises of the Enlightenment' }
    ],
    concepts: [
        'Sound mind in a sound body — the double aim of education, with physical hardening preceding intellectual cultivation',
        'Virtue as self-denial — the capacity to resist appetite in obedience to reason, the master virtue',
        'Habit over rule — the most effective way to form character is habituating the child before it can reflect on what is being formed',
        'Esteem as the lever of education — the child\'s desire for approval is a more durable motivator than fear of punishment',
        'The gentleman as the educational ideal — practical, virtuous, rational, physically robust, capable of self-government'
    ],
    structure: 'Part 1 (§1–30): The body — health, hardening, diet, exercise\nPart 2 (§31–82): The mind and the formation of virtue — self-denial, esteem, the management of desire\nPart 3 (§83–195): The curriculum — reading, writing, drawing, French, Latin, arithmetic, geography, history\nPart 4 (§196–216): Defects in current education; practical recommendations',
    quote: 'Of all the men we meet with, nine parts of ten are what they are, good or evil, useful or not, by their education. It is that which makes the great difference in mankind.',
    additionalQuotes: [
        { text: 'The great mistake in people\'s breeding their children has been that the mind has not been made obedient to discipline, and pliant to reason, when at first it was most tender, most easy to be bowed.', source: 'Some Thoughts Concerning Education §34' }
    ],
    commentary: [
        { philosopher: 'Rousseau', text: 'Locke\'s treatise on education is a work of good sense everywhere, but it is the education of a gentleman, not of a man. Locke never asks what it means to educate a human being before one educates a citizen or a professional. Émile begins where Locke ends.' }
    ],
    modernRelevance: 'Locke\'s insistence that education shapes nearly everything in human character — and that early habituation, not adult instruction, is its most powerful instrument — is confirmed by developmental psychology and neuroscience. His argument that corporal punishment produces compliance without internalization is now supported by extensive empirical research. His skepticism about rote learning and preference for active, interested engagement are the bases of progressive educational theory from Dewey through contemporary constructivism.',
    context: 'The letters to Clarke were written between 1684 and 1691 and circulated among friends before publication. Locke worked them into a continuous treatise after his return to England in 1689. Five editions appeared in Locke\'s lifetime. Its influence in France was enormous: it shaped the educational sections of Rousseau\'s Émile, Condillac\'s empiricist pedagogy, and the educational programmes of the French Revolution.',
    relatedWorks: ['essay-human-understanding', 'two-treatises-government']
},

{
    id: 'reasonableness-christianity',
    title: 'The Reasonableness of Christianity',
    greekTitle: 'The Reasonableness of Christianity',
    philosopher: 'locke',
    category: 'practical',
    categoryLabel: 'Theology and Ethics',
    date: '1695 AD',
    dateSort: 1695,
    emoji: '✝️',
    cardSize: 'normal',
    readingDifficulty: 3,
    estimatedWordCount: 55000,
    shortDesc: 'Locke\'s attempt to reduce Christianity to its rational essentials — the most important text in the tradition of liberal Protestant theology and a founding document of Enlightenment religion.',
    summary: 'The Reasonableness of Christianity is the work in which Locke most directly addresses the relationship between reason and revelation — the central intellectual question of the late seventeenth century as traditional religious authority collapsed under the pressure of the new science and biblical criticism. Published anonymously in 1695, it provoked a fierce controversy in which Locke defended himself through two Vindications.\n\nLocke\'s argument is disarmingly simple in structure, though radical in implication. He goes through the Gospels and Acts looking for what Christ and the apostles actually required people to believe for salvation. His answer is: very little. The single essential article of Christian faith is that Jesus is the Messiah, the promised son of God. Everything else — the elaborate doctrinal edifices of Trinitarianism, original sin, atonement theory, sacramental theology — is superadded by theologians and church councils, not required by the New Testament itself. This minimal creed is sufficient for salvation and is accessible to reason, since the miracles that accompanied Jesus\'s ministry provide reasonable grounds for accepting his Messianic claim.\n\nThe work\'s radicalism lies in its implication for the relation between natural religion and Christianity. If the essential content of Christianity is accessible to reason, then Christianity is not so much a supernatural revelation replacing natural religion as a confirmation and clarification of it. The moral law that reason teaches is the same as the law Christ preaches. This alignment of rational ethics and Christian ethics was enormously influential on Enlightenment deism and on subsequent liberal Protestant theology, from Locke\'s immediate successors through Matthew Tindal\'s Christianity as Old as the Creation (1730) to the liberal theology of the nineteenth century.',
    themes: ['rational religion', 'liberal Protestantism', 'faith and reason', 'minimal creed', 'natural religion', 'Enlightenment deism', 'biblical interpretation', 'moral religion'],
    keyCharacters: [],
    concepts: [
        'Minimal Christianity — the single essential article is that Jesus is the Messiah',
        'Reasonableness of faith — miracles provide rational grounds for accepting Jesus\'s authority',
        'Natural law as the moral core — the ethical content of Christianity is accessible to unaided reason',
        'The sufficiency of scripture — the Bible contains all that is necessary for salvation without ecclesiastical supplement'
    ],
    structure: 'Part 1: Survey of the New Testament for essential requirements of faith\nPart 2: The role of miracles as rational grounds for faith\nPart 3: The alignment of the law of nature with the teachings of Christ\nPart 4: The advantages of Christian revelation over pure natural religion',
    quote: 'The writers and wranglers in religion fill it with niceties, and dress it up with notions, which they make necessary and fundamental parts of it; as if there were no way into the Church but through the academy or lyceum.',
    additionalQuotes: [
        { text: 'Reason is natural revelation, whereby the eternal father of light communicates to mankind that portion of truth which he has laid within the reach of their natural faculties.', source: 'Essay Concerning Human Understanding, Book IV, Chapter 19' }
    ],
    commentary: [
        { philosopher: 'Stillingfleet', text: 'If the principles of the Essay are applied to religion, as the Reasonableness applies them, the result is a Christianity so stripped of doctrine that it can no longer be distinguished from the natural religion of the deists.' }
    ],
    modernRelevance: 'The Reasonableness is the source of the liberal Protestant tradition that dominates mainstream Christianity in the English-speaking world — emphasising ethics over doctrine, moral transformation over sacramental grace, and the compatibility of faith with modern science. It is also the indirect source of the Deist movement that would culminate in Jefferson\'s literal cut-and-paste version of the Gospels, retaining only the moral teachings and removing the miracles.',
    context: 'Locke read through the entire New Testament in Greek in preparation for this work and was struck by how little the theologians\' elaborate doctrinal requirements corresponded to what the text actually demanded. He published it anonymously out of caution, having already experienced the controversy generated by the Essay. The immediate accusation of Socinianism — denial of Christ\'s divinity — was not entirely unfair: the work\'s minimal creed is compatible with a purely human Jesus, and Locke\'s own private beliefs remain disputed by scholars.',
    relatedWorks: ['letter-toleration', 'essay-human-understanding', 'two-treatises-government']
},

{
    id: 'locke-correspondence',
    title: 'Correspondence and Philosophical Papers',
    greekTitle: 'Correspondence',
    philosopher: 'locke',
    category: 'method',
    categoryLabel: 'Correspondence',
    date: '1660–1704 AD',
    dateSort: 1680,
    emoji: '📬',
    cardSize: 'normal',
    readingDifficulty: 3,
    estimatedWordCount: 250000,
    shortDesc: 'Over three thousand letters — the most extensive philosophical correspondence in the English language, documenting Locke\'s engagement with Molyneux, Stillingfleet, Newton, and the full intellectual life of the early Enlightenment.',
    summary: 'Locke\'s correspondence, collected in eight volumes in the Clarendon edition, comprises over three thousand letters and is the most extensive epistolary record of any philosopher in the English language. It spans from his student days at Christ Church, Oxford through his political career, his exile in Holland, and his final years at Oates in Essex.\n\nThe most philosophically important exchanges are those with William Molyneux, the Dublin scientist and philosopher who posed the famous problem that still bears his name: if a man born blind learned to distinguish a sphere from a cube by touch, would he — upon being given sight — be able to distinguish them by sight alone, before touching them? Locke answered no, because visual ideas of shape are entirely distinct from tactile ideas of shape and could not be identified without prior experience of their co-occurrence. The Molyneux problem has been a central test case in philosophy of perception and cognitive science for over three centuries and was only empirically addressed by experiments on sight-restoration patients in the twenty-first century.\n\nThe exchanges with Edward Stillingfleet, Bishop of Worcester, constitute the most important philosophical controversy generated by the Essay. Stillingfleet accused Locke\'s account of substance and his way of ideas of undermining the philosophical foundations of the Trinity and of personal identity at death. Locke\'s three long replies are among the most carefully argued prose he wrote, clarifying key doctrines of the Essay — particularly on substance, essence, and the limits of nominal definition — in ways the original text left ambiguous.\n\nLocke\'s correspondence with Newton reveals the deep philosophical connection between the two thinkers: both were committed to a corpuscularian natural philosophy grounding real qualities in the microscopic structure of matter, both were suspicious of scholastic essences and occult qualities, and both were privately skeptical of Trinitarian orthodoxy. Newton sent Locke a paper arguing from scripture against the Trinity — the Two Notable Corruptions of Scripture — which Locke agreed to have published anonymously in France, though the project ultimately did not proceed.',
    themes: ['Molyneux problem', 'substance and identity', 'Trinity controversy', 'philosophy of perception', 'religion and reason', 'intellectual friendship', 'Newton and empiricism'],
    keyCharacters: [
        { name: 'William Molyneux', role: 'Dublin scientist, philosopher, and Locke\'s most intellectually intimate correspondent — author of the Molyneux problem; his premature death in 1698 was a profound loss to Locke' },
        { name: 'Edward Stillingfleet', role: 'Bishop of Worcester and the most formidable theological critic of the Essay — his objections forced Locke into his most careful clarifications of substance, identity, and the nature of ideas' },
        { name: 'Isaac Newton', role: 'Fellow member of the Boyle circle — their correspondence reveals the shared foundations and shared heterodoxies of the two great figures of the English Enlightenment' }
    ],
    concepts: [
        'The Molyneux problem — can cross-modal perceptual identification occur without prior experience of correlation?',
        'Philosophical friendship as a condition of philosophical progress — Locke\'s letters with Molyneux as a model of productive intellectual exchange',
        'The limits of the nominal definition of substance — what we can and cannot mean by real essence'
    ],
    structure: 'The correspondence is organised chronologically in the Clarendon edition. Key clusters: the Shaftesbury period (1671–1682); the Holland exile (1683–1689); the Molyneux correspondence (1692–1698); the Stillingfleet controversy (1696–1699); the final years at Oates (1700–1704).',
    quote: 'I no sooner perceived myself in the world, but I found myself in a storm, which has lasted almost hitherto; a storm so thick that I could see little about me, and which way to steer I was at a loss. But the shore being smooth and the harbour quiet, I am willing to take a little rest.',
    additionalQuotes: [
        { text: 'I think I may say that of all the men I know, you come nearest to what, in my opinion, a friend should be.', source: 'Locke to Molyneux, 1693' }
    ],
    commentary: [
        { philosopher: 'Cranston', text: 'The correspondence is where the human Locke lives — cautious, warm, occasionally irascible, deeply loyal to friends and deeply suspicious of enemies, and always more candid than the published works about what he really believed.' }
    ],
    modernRelevance: 'The Molyneux problem has been empirically investigated through studies of patients who had cataracts surgically removed after years of blindness. The results — patients showed some initial cross-modal recognition but with significant limitations — broadly support Locke\'s negative answer while complicating it in ways neither Locke nor Molyneux anticipated. The problem remains a live topic in philosophy of perception, cross-modal transfer, and the developmental origins of spatial cognition.',
    context: 'The standard edition of the correspondence (Clarendon Press, 8 volumes, edited by E. S. de Beer) was completed in 1989. Many letters in the collection were available earlier in partial editions, but the complete correspondence revealed the full range of Locke\'s intellectual life and significantly changed scholarly understanding of his development, particularly his relationship with Newton and the depth of his Socinian tendencies.',
    relatedWorks: ['essay-human-understanding', 'two-treatises-government', 'letter-toleration']
}

);
"""

files = {
    'data-14a.js': data_14a,
    'data-14b.js': data_14b,
    'data-14c.js': data_14c,
}

for filename, content in files.items():
    path = os.path.join(js_dir, filename)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    lines = content.count('\n')
    print(f"Written {filename} — {lines} lines → {path}")

print("\nLocke files complete.")
