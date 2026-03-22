#!/usr/bin/env python3
"""
Phase 2: Timeline Rebuild + Philosopher Bio Pages + Concept Index
Run from ~/Desktop/philosophy-archive/: python3 build_phase2.py
"""
import os, re

base       = os.path.dirname(os.path.abspath(__file__))
js_dir     = os.path.join(base, 'js')
css_path   = os.path.join(base, 'css', 'style.css')
script_dst = os.path.join(base, 'script.js')
index_path = os.path.join(base, 'index.html')
changes    = []

# ════════════════════════════════════════════════════════════════════════════
# 1. PHILOSOPHER BIOS DATA FILE
# ════════════════════════════════════════════════════════════════════════════

BIOS_JS = r"""/* Philosopher biography data for philosopher.html */
window.PHILOSOPHER_BIOS = {

  plato: {
    name: 'Plato',
    born: '428\u202fBC', died: '348\u202fBC', birthYear: -428,
    location: 'Athens',
    school: 'The Academy',
    color: '#6B4C9A',
    tagline: 'The philosopher who turned philosophy into drama, mathematics into metaphysics, and politics into the search for justice.',
    bio: 'Plato was born into an aristocratic Athenian family around 428 BC, the son of Ariston and Perictione. He was related to Critias, one of the Thirty Tyrants, a fact that shaped his lifelong distrust of democracy. As a young man he fell under the influence of Socrates, whose trial and execution in 399 BC was the defining trauma of his intellectual life.\n\nAfter Socrates\u2019 death, Plato travelled widely \u2014 to Megara, Egypt, and Sicily, where he became entangled in the politics of Syracuse through his friendship with Dion, nephew of the tyrant Dionysius I. He returned to Athens around 387 BC and founded the Academy, the first institution of higher learning in the Western world, which operated continuously for nearly 900 years.\n\nPlato wrote approximately thirty dialogues across fifty years of philosophical activity. They are divided by scholars into early (Socratic), middle (the great metaphysical dialogues: Republic, Symposium, Phaedo, Phaedrus), and late (Parmenides, Theaetetus, Sophist, Laws) periods. The middle dialogues develop the Theory of Forms, the tripartite soul, and the political philosophy of the Republic. The late dialogues show a critical and increasingly technical philosopher revisiting his own earlier positions.\n\nHis most consequential student was Aristotle, who joined the Academy at seventeen and remained for twenty years before founding the rival Lyceum.',
    influences: ['Socrates', 'Pythagoras', 'Heraclitus', 'Parmenides'],
    influenced: ['Aristotle', 'Plotinus', 'Augustine', 'Aquinas', 'Kant', 'Whitehead'],
    keyWorks: ['republic', 'symposium', 'phaedo', 'meno', 'phaedrus', 'theaetetus'],
    tradition: 'Founder of the Western philosophical tradition; originator of systematic metaphysics, epistemology, and political philosophy.',
    quote: 'The unexamined life is not worth living.',
    quoteSource: 'Apology, 38a (Socrates speaking)'
  },

  aristotle: {
    name: 'Aristotle',
    born: '384\u202fBC', died: '322\u202fBC', birthYear: -384,
    location: 'Athens / Stagira / Lesbos',
    school: 'The Lyceum',
    color: '#2D7D6F',
    tagline: 'The philosopher who organised all human knowledge into disciplines, invented formal logic, and established the empirical study of nature, politics, and the good life.',
    bio: 'Aristotle was born in Stagira, a Greek colony on the northern Aegean coast, in 384 BC. His father Nicomachus was physician to Amyntas III of Macedonia, giving Aristotle early exposure to biology and the Macedonian court. At seventeen he entered Plato\u2019s Academy in Athens, where he remained as student, teacher, and researcher for twenty years until Plato\u2019s death in 348 BC.\n\nAfter leaving Athens, Aristotle spent several years in Asia Minor (at Assos and Lesbos, where he conducted his extraordinary marine biological research) before being summoned by Philip II of Macedonia to tutor the thirteen-year-old Alexander, who would become Alexander the Great. The relationship lasted three years.\n\nIn 335 BC Aristotle returned to Athens and founded the Lyceum, a school whose members became known as the Peripatetics (from peripatein, to walk around). He lectured and researched there for twelve years across the full range of human knowledge: logic, physics, biology, psychology, metaphysics, ethics, politics, rhetoric, and poetics.\n\nWhen Alexander died in 323 BC, anti-Macedonian sentiment in Athens made Aristotle\u2019s position precarious. Citing the fate of Socrates and unwilling to let Athens \u201csin twice against philosophy,\u201d he retired to Chalcis in Euboea, where he died in 322 BC.',
    influences: ['Plato', 'Socrates', 'Democritus', 'Hippocrates'],
    influenced: ['Theophrastus', 'Alexander', 'Aquinas', 'Averroes', 'Bacon', 'Darwin', 'MacIntyre'],
    keyWorks: ['nicomachean-ethics', 'politics', 'metaphysics', 'physics', 'poetics', 'prior-analytics'],
    tradition: 'Founder of formal logic, empirical natural science, and systematic ethics; the defining influence on medieval philosophy through Aquinas.',
    quote: 'The whole is greater than the sum of its parts.',
    quoteSource: 'Metaphysics, 10.6 (paraphrased)'
  },

  descartes: {
    name: 'Ren\u00e9 Descartes',
    born: '1596', died: '1650', birthYear: 1596,
    location: 'La Haye en Touraine / Amsterdam / Stockholm',
    school: 'Rationalism',
    color: '#2B4C8C',
    tagline: 'The philosopher who began modern philosophy by doubting everything, found the one thing he could not doubt, and rebuilt knowledge from a single point of absolute certainty.',
    bio: 'Ren\u00e9 Descartes was born on 31 March 1596 in La Haye en Touraine, France (now renamed Descartes in his honour). Educated by the Jesuits at La Fl\u00e8che, he received the best available scholastic education while developing a lasting dissatisfaction with its conclusions. After studying law at Poitiers, he enlisted in various European armies not to fight but to travel and observe the world.\n\nIn 1619, wintering in Neuburg on the Danube, Descartes had three vivid dreams that he interpreted as a divine commission to reform human knowledge on mathematical foundations. He spent the following two decades in Amsterdam developing his new philosophy and science, publishing his Discourse on Method (1637) and the Meditations (1641) \u2014 the founding texts of modern philosophy.\n\nDescartes\u2019 method of systematic doubt led him to the cogito \u2014 cogito ergo sum, \u201cI think, therefore I am\u201d \u2014 the one certainty that survives even the most radical scepticism. From this foundation he attempted to reconstruct all knowledge, establishing the existence of God and the existence of the external world through rational argument. His dualism \u2014 the strict separation of mind (res cogitans) and matter (res extensa) \u2014 defined the central problems of modern philosophy of mind.\n\nIn 1649 he reluctantly accepted Queen Christina of Sweden\u2019s invitation to Stockholm, where he was required to tutor the queen at five in the morning in the Swedish winter. He died of pneumonia in February 1650, aged fifty-three.',
    influences: ['Augustine', 'Aquinas', 'Galileo', 'Mersenne', 'Stoic philosophy'],
    influenced: ['Spinoza', 'Leibniz', 'Malebranche', 'Locke', 'Kant', 'Husserl'],
    keyWorks: ['meditations-first-philosophy', 'discourse-method', 'principles-philosophy', 'rules-direction-mind'],
    tradition: 'Father of modern philosophy; originator of mind-body dualism, systematic doubt, and the foundationalist project in epistemology.',
    quote: 'I think, therefore I am.',
    quoteSource: 'Discourse on Method, Part IV'
  },

  spinoza: {
    name: 'Baruch Spinoza',
    born: '1632', died: '1677', birthYear: 1632,
    location: 'Amsterdam / The Hague',
    school: 'Rationalism',
    color: '#2D6A4F',
    tagline: 'The philosopher who identified God with Nature, dissolved free will into necessity, derived ethics from metaphysics, and was excommunicated from his community for thinking clearly.',
    bio: 'Baruch (Benedictus) de Spinoza was born on 24 November 1632 in Amsterdam into a family of Portuguese Sephardic Jews who had fled the Inquisition. He received a thorough education in Jewish learning at the Talmud Torah school and showed exceptional promise. At twenty-three he was issued with the harshest cherem (excommunication) ever recorded by the Amsterdam Jewish community, on grounds never formally specified but clearly related to his heterodox views on God, the soul, and the Torah.\n\nFor the rest of his life Spinoza lived quietly in Rijnsburg, Voorburg, and The Hague, supporting himself by grinding optical lenses \u2014 a craft that simultaneously expressed his scientific interests and eventually contributed to his death from lung disease (silica inhalation or tuberculosis) in 1677. He corresponded with leading intellectuals across Europe and declined an offer of a professorship at Heidelberg to preserve his freedom of thought.\n\nSpinoza published only two works under his own name during his lifetime: a geometric exposition of Descartes\u2019 philosophy (1663) and the Theological-Political Treatise (1670), published anonymously and immediately banned. His masterwork, the Ethics, was completed by 1675 but withheld from publication when Spinoza learned it would face suppression. It was published posthumously in his Opera Posthuma (1677), together with the unfinished Political Treatise.',
    influences: ['Descartes', 'Maimonides', 'Hobbes', 'Bruno', 'Stoic philosophy'],
    influenced: ['Leibniz', 'Hegel', 'Goethe', 'Nietzsche', 'Einstein', 'Deleuze'],
    keyWorks: ['ethics', 'theological-political-treatise', 'political-treatise', 'treatise-intellect-emendation'],
    tradition: 'The most rigorous rationalist; originator of pantheism, biblical criticism, and the immanent critique of religion.',
    quote: 'God, or Nature.',
    quoteSource: 'Ethics, Part IV, Preface'
  },

  leibniz: {
    name: 'Gottfried Wilhelm Leibniz',
    born: '1646', died: '1716', birthYear: 1646,
    location: 'Leipzig / Hanover / Berlin',
    school: 'Rationalism',
    color: '#2E4057',
    tagline: 'The last universal genius \u2014 who invented calculus, designed the first mechanical calculator, developed the most optimistic metaphysics in history, and wrote 200,000 letters in four languages.',
    bio: 'Gottfried Wilhelm Leibniz was born in Leipzig on 1 July 1646, the son of a professor of moral philosophy. A child prodigy who taught himself Latin from Livy at eight, he entered the University of Leipzig at fifteen and completed his doctorate in law at twenty. He declined a university position to enter the diplomatic and administrative service of various German princes, becoming counsellor, librarian, historian, and courtier to the House of Brunswick-Luneburg in Hanover from 1676 until his death.\n\nLeibniz\u2019s intellectual range was extraordinary even by seventeenth-century standards. He independently invented the calculus (1675\u201376), simultaneously with but independently of Newton, producing the notation (d/dx, \u222b) that is still used today. He designed the first mechanical calculator capable of multiplication and division, corresponded with every significant intellectual in Europe, and worked simultaneously on metaphysics, logic, mathematics, physics, history, jurisprudence, theology, and Chinese philosophy.\n\nHis metaphysics of monads \u2014 the doctrine that reality consists of an infinite number of simple, unextended, non-interacting windowless substances whose pre-established harmony constitutes the apparent causal order of the world \u2014 is the most elaborate and most counterintuitive philosophical system in the modern period. His famous claim that this is the best of all possible worlds was memorably satirised by Voltaire\u2019s Candide. He died in Hanover in 1716, largely neglected by the court he had served for forty years.',
    influences: ['Descartes', 'Spinoza', 'Hobbes', 'Malebranche', 'Aristotle', 'Scholastics'],
    influenced: ['Wolff', 'Kant', 'Frege', 'Russell', 'Whitehead'],
    keyWorks: ['monadology', 'discourse-metaphysics', 'new-essays-human-understanding', 'theodicy', 'principles-nature-grace'],
    tradition: 'The most ambitious rationalist system-builder; originator of possible worlds semantics and a precursor of modern logic.',
    quote: 'This is the best of all possible worlds.',
    quoteSource: 'Theodicy, \u00a78'
  },

  locke: {
    name: 'John Locke',
    born: '1632', died: '1704', birthYear: 1632,
    location: 'Somerset / Oxford / Amsterdam / London',
    school: 'British Empiricism',
    color: '#8B6520',
    tagline: 'The philosopher of liberty \u2014 who argued that the mind begins as a blank slate, that government derives its authority from consent, and that life, liberty, and property are natural rights no government may violate.',
    bio: 'John Locke was born on 29 August 1632 in Wrington, Somerset, the son of a Puritan country lawyer who fought on the Parliamentary side in the Civil War. He was educated at Westminster School and Christ Church Oxford, where he eventually became a lecturer in Greek, rhetoric, and moral philosophy. His early interests were scientific rather than philosophical; he was elected Fellow of the Royal Society in 1668.\n\nLocke\u2019s political fate was bound to that of Anthony Ashley Cooper, first Earl of Shaftesbury, whom he served as physician, secretary, and intellectual adviser from 1666. When Shaftesbury fell from favour and was suspected of treason, Locke prudently fled to Amsterdam in 1683, where he spent five years in exile, finishing his major works in Dutch libraries. He returned to England on the ship that brought Princess Mary for the Glorious Revolution of 1688 and published his three major works in rapid succession in 1689\u201390.\n\nThe Essay Concerning Human Understanding, the Two Treatises of Government, and the Letter Concerning Toleration together constitute the philosophical foundation of liberal democracy. Locke\u2019s influence on the American founding generation \u2014 Jefferson, Hamilton, Madison \u2014 was direct and acknowledged; the Declaration of Independence\u2019s \u201clife, liberty, and the pursuit of happiness\u201d is a Lockean formulation.',
    influences: ['Bacon', 'Descartes', 'Boyle', 'Newton', 'Hooker'],
    influenced: ['Berkeley', 'Hume', 'Voltaire', 'Rousseau', 'Jefferson', 'Kant'],
    keyWorks: ['essay-human-understanding', 'two-treatises-government', 'letter-toleration', 'some-thoughts-education'],
    tradition: 'Father of British empiricism and liberal political philosophy; the primary philosophical influence on the American and French revolutions.',
    quote: 'No man\u2019s knowledge here can go beyond his experience.',
    quoteSource: 'Essay Concerning Human Understanding, II.i.2'
  },

  berkeley: {
    name: 'George Berkeley',
    born: '1685', died: '1753', birthYear: 1685,
    location: 'Kilkenny / Dublin / London / Cloyne',
    school: 'British Empiricism / Idealism',
    color: '#8B6914',
    tagline: 'The bishop-philosopher who argued that matter does not exist, that the external world consists entirely of ideas in minds, and that this apparently mad thesis was the only consistent form of empiricism.',
    bio: 'George Berkeley was born on 12 March 1685 near Kilkenny, Ireland. He studied at Kilkenny College and Trinity College Dublin, where he remained as fellow and tutor after completing his BA in 1704. His three major philosophical works \u2014 the Essay Towards a New Theory of Vision (1709), the Principles of Human Knowledge (1710), and the Three Dialogues between Hylas and Philonous (1713) \u2014 were all written before he was twenty-eight.\n\nBerkeley\u2019s immaterialism (esse est percipi: to be is to be perceived) was his response to what he saw as the sceptical and atheistic implications of Locke\u2019s philosophy of material substance. If all we know are ideas in our minds, and matter is defined as something that exists independently of any mind, then matter is unknowable in principle and serves no philosophical function. Its elimination, Berkeley argued, actually rescues religion by making the existence of God \u2014 the supreme mind in which unperceived objects continue to exist \u2014 philosophically necessary.\n\nAfter a decade in London\u2019s intellectual society, Berkeley devoted years to an ambitious project to found a college in Bermuda for the education of American colonists and Native Americans. He settled in Newport, Rhode Island (1728\u201331), waiting for parliamentary funding that never arrived. He returned to Ireland and spent his final years as Bishop of Cloyne, writing the mystical and medical treatise Siris (1744) on the virtues of tar-water.',
    influences: ['Locke', 'Malebranche', 'Newton'],
    influenced: ['Hume', 'Kant', 'Mach', 'Russell', 'Phenomenology'],
    keyWorks: ['principles-human-knowledge', 'three-dialogues', 'essay-theory-vision', 'alciphron'],
    tradition: 'Originator of subjective idealism; pushed Lockean empiricism to its logical extreme, anticipating Kant\u2019s transcendental idealism and phenomenology.',
    quote: 'To be is to be perceived.',
    quoteSource: 'Principles of Human Knowledge, \u00a73'
  },

  hume: {
    name: 'David Hume',
    born: '1711', died: '1776', birthYear: 1711,
    location: 'Edinburgh / Paris / London',
    school: 'British Empiricism / Scepticism',
    color: '#3E5368',
    tagline: 'The most consistent sceptic in the Western tradition \u2014 who demolished the rational foundations of causation, personal identity, and natural religion, and died calmly and without religious consolation at sixty-five.',
    bio: 'David Hume was born on 7 May 1711 in Edinburgh and raised in the modest circumstances of a minor landed family in Berwickshire. He showed extraordinary intellectual precocity, entering Edinburgh University at twelve and suffering a mental crisis from overwork at twenty-three. He recovered in France, where he wrote the Treatise of Human Nature between 1734 and 1737 at La Fl\u00e8che, where Descartes had been educated a century earlier.\n\nThe Treatise \u201cfell dead-born from the press\u201d in 1739\u201340. Its failure was catastrophic for the young Hume, who had staked everything on it. He rewrote its central arguments in the more accessible Enquiries (1748, 1751), which brought moderate success. The Essays (1741\u201342) made him famous as a man of letters; the History of England (1754\u201361) made him wealthy. The Dialogues Concerning Natural Religion, written in the 1750s, were withheld from publication until after his death.\n\nHume was twice denied university chairs (at Edinburgh and Glasgow) on grounds of scepticism and alleged atheism. He served as secretary to the British embassy in Paris (1763\u201365), where he was lionised by the philosophes. He returned to Edinburgh in 1769, where he lived contentedly until his death on 25 August 1776. His equanimity in his final months \u2014 documented by James Boswell and Adam Smith \u2014 became one of the most celebrated instances of philosophical dying in the modern period.',
    influences: ['Locke', 'Berkeley', 'Newton', 'Hutcheson', 'Cicero'],
    influenced: ['Kant', 'Reid', 'Smith', 'Bentham', 'Ayer', 'Popper'],
    keyWorks: ['treatise-human-nature', 'enquiry-human-understanding', 'enquiry-principles-morals', 'dialogues-natural-religion'],
    tradition: 'The most radical British empiricist; originator of the problem of induction, the is-ought gap, and the bundle theory of the self.',
    quote: 'Reason is, and ought only to be, the slave of the passions.',
    quoteSource: 'Treatise of Human Nature, 2.3.3'
  },

  kant: {
    name: 'Immanuel Kant',
    born: '1724', died: '1804', birthYear: 1724,
    location: 'K\u00f6nigsberg, Prussia',
    school: 'Critical Philosophy / German Idealism',
    color: '#2B4C6F',
    tagline: 'The philosopher who never left K\u00f6nigsberg and changed everything \u2014 who performed the Copernican revolution in philosophy, reconciled science with morality, and defined the limits of human reason.',
    bio: 'Immanuel Kant was born on 22 April 1724 in K\u00f6nigsberg, Prussia (now Kaliningrad, Russia), the son of a harness-maker. He studied at the Collegium Fridericianum and the University of K\u00f6nigsberg, supporting himself as a private tutor for nine years after graduation before obtaining a lectureship in 1755. He was appointed to the chair of logic and metaphysics in 1770 \u2014 a position he held until 1796.\n\nKant\u2019s life was one of extraordinary regularity. He never married, never travelled more than fifty miles from K\u00f6nigsberg, and set his daily schedule with such precision that neighbours reportedly set their clocks by his afternoon walks. Within this ordered life, he underwent a radical intellectual transformation: the pre-critical period of rationalist metaphysics was superseded, after a decade of the \u201csilent years,\u201d by the critical philosophy inaugurated by the Critique of Pure Reason (1781).\n\nThe three Critiques \u2014 Pure Reason (1781/1787), Practical Reason (1788), and Judgment (1790) \u2014 constitute the most systematic philosophical achievement of the modern period. Kant\u2019s Copernican revolution: instead of asking how our knowledge conforms to objects, ask how objects conform to our knowledge. The forms of intuition (space and time) and the categories of the understanding (causality, substance, etc.) are not derived from experience but are the conditions under which experience is possible.',
    influences: ['Hume', 'Leibniz', 'Wolff', 'Newton', 'Rousseau'],
    influenced: ['Fichte', 'Schelling', 'Hegel', 'Schopenhauer', 'Nietzsche', 'Husserl', 'Rawls'],
    keyWorks: ['critique-pure-reason', 'critique-practical-reason', 'groundwork-metaphysics-morals', 'critique-judgment', 'perpetual-peace'],
    tradition: 'The pivot of modern philosophy; the critical philosophy defined the agenda for all subsequent epistemology, ethics, and aesthetics.',
    quote: 'The starry sky above me and the moral law within me.',
    quoteSource: 'Critique of Practical Reason, Conclusion'
  },

  hegel: {
    name: 'G.W.F. Hegel',
    born: '1770', died: '1831', birthYear: 1770,
    location: 'Stuttgart / Jena / Nuremberg / Heidelberg / Berlin',
    school: 'German Idealism',
    color: '#1E3A5F',
    tagline: 'The most systematic philosopher since Aristotle \u2014 who argued that reality is Spirit\u2019s self-realisation, that history is the progress of the consciousness of freedom, and that the Owl of Minerva spreads its wings only with the falling of the dusk.',
    bio: 'Georg Wilhelm Friedrich Hegel was born on 27 August 1770 in Stuttgart. He studied at the T\u00fcbingen Stift alongside Schelling and H\u00f6lderlin, with whom he shared rooms and revolutionary enthusiasm for the French Revolution. After years as a private tutor, he obtained a lectureship at Jena (1801\u201307), where he completed the Phenomenology of Spirit the night before Napoleon entered the city \u2014 \u201cthe world-soul on horseback.\u201d\n\nThe Jena period ended with the university\u2019s closure by the French. Hegel edited a newspaper in Bamberg, served as rector of the Nuremberg gymnasium (1808\u201316, during which he wrote the Science of Logic), was briefly at Heidelberg (1816\u201318), and finally obtained the most prestigious philosophical chair in Germany, at Berlin (1818\u201331), where he remained until his sudden death from cholera on 14 November 1831.\n\nHegel\u2019s influence was immediate and divisive. His students split within years of his death into a Right (using his philosophy to defend Prussian Christianity) and Left (using it to attack religion and the state) \u2014 the latter producing Marx, Feuerbach, and Strauss. His influence on twentieth-century continental philosophy through Koj\u00e8ve\u2019s Paris lectures (1933\u201339) was enormous.',
    influences: ['Kant', 'Fichte', 'Schelling', 'Aristotle', 'Spinoza', 'H\u00f6lderlin'],
    influenced: ['Marx', 'Kierkegaard', 'Bradley', 'Koj\u00e8ve', 'Heidegger', 'Gadamer', 'Adorno'],
    keyWorks: ['phenomenology-of-spirit', 'science-of-logic', 'philosophy-of-right', 'lectures-philosophy-history'],
    tradition: 'The culmination of German Idealism; the primary target and source of existentialism, Marxism, and twentieth-century continental philosophy.',
    quote: 'The Owl of Minerva spreads its wings only with the falling of the dusk.',
    quoteSource: 'Philosophy of Right, Preface'
  },

  schopenhauer: {
    name: 'Arthur Schopenhauer',
    born: '1788', died: '1860', birthYear: 1788,
    location: 'Danzig / Weimar / Berlin / Frankfurt',
    school: 'Philosophical Pessimism',
    color: '#7B4F2E',
    tagline: 'The philosopher who named the blind Will beneath the surface of things, spent thirty years being ignored while Hegel was celebrated, and ended his life dining alone with his poodle \u2014 vindicated at last.',
    bio: 'Arthur Schopenhauer was born on 22 February 1788 in Danzig (now Gda\u0144sk), Poland, the son of a wealthy merchant father and Johanna Schopenhauer, who became a celebrated novelist. After his father\u2019s death (probably suicide) in 1805, the family moved to Weimar, where Johanna established a literary salon attended by Goethe. Arthur\u2019s relationship with his mother was catastrophically bad; they ceased contact when he was thirty.\n\nSchopenhauer studied at G\u00f6ttingen and Berlin, where he attended Fichte\u2019s lectures with contempt. He completed his doctoral dissertation, On the Fourfold Root of the Principle of Sufficient Reason, at Jena in 1813. His masterwork, The World as Will and Representation, was published in 1818 and ignored entirely. His attempt to lecture at Berlin concurrently with Hegel \u2014 scheduling his lectures at the same hours \u2014 drew three students. Hegel drew hundreds.\n\nSchopenhauer moved to Frankfurt in 1833 and remained there for the rest of his life, living frugally on his inheritance, walking his poodles, playing his flute, and writing the supplementary essays that would eventually make his name. The Parerga and Paralipomena (1851) finally attracted wide readership; by the mid-1850s he was famous throughout Germany and Europe. He died on 21 September 1860, eating breakfast alone.',
    influences: ['Kant', 'Plato', 'Buddhism', 'Hinduism', 'Goethe'],
    influenced: ['Nietzsche', 'Wagner', 'Tolstoy', 'Freud', 'Wittgenstein', 'Beckett', 'Mann'],
    keyWorks: ['world-as-will-vol1', 'world-as-will-vol2', 'parerga-paralipomena', 'two-problems-ethics'],
    tradition: 'Founder of philosophical pessimism; the philosopher who reconciled Kantian epistemology with Eastern thought and anticipated depth psychology.',
    quote: 'Life swings like a pendulum between pain and boredom.',
    quoteSource: 'The World as Will and Representation, Vol. I, \u00a757'
  },

  kierkegaard: {
    name: 'S\u00f8ren Kierkegaard',
    born: '1813', died: '1855', birthYear: 1813,
    location: 'Copenhagen',
    school: 'Existentialism',
    color: '#6B2737',
    tagline: 'The father of existentialism \u2014 who spent his entire career asking what it means to be a single individual before God, dismantled Hegel\u2019s system from within, and died at forty-two convinced he had been used by Providence as a corrective.',
    bio: 'S\u00f8ren Aabye Kierkegaard was born on 5 May 1813 in Copenhagen, the youngest of seven children of Michael Pedersen Kierkegaard, a prosperous merchant haunted by the conviction that he had cursed God in youth and would outlive all his children. S\u00f8ren absorbed his father\u2019s melancholy and religious obsession while developing extraordinary intellectual gifts.\n\nHe studied at the University of Copenhagen from 1830, living extravagantly on his father\u2019s allowance while producing no academic work. His father\u2019s death in 1838 left him financially independent and spiritually bereft. In 1840\u201341, he completed his dissertation (On the Concept of Irony), became engaged to Regine Olsen, and then \u2014 in one of the most discussed decisions in intellectual biography \u2014 broke the engagement. He spent the rest of his life writing about what this decision meant.\n\nBetween 1843 and 1846, Kierkegaard published a stream of pseudonymous works \u2014 Either/Or, Fear and Trembling, Repetition, Philosophical Fragments, The Concept of Anxiety, Stages on Life\u2019s Way, the Concluding Unscientific Postscript \u2014 that collectively constitute the most sustained and most original philosophical response to Hegelian idealism in the tradition. He died on 11 November 1855, aged forty-two, having spent his final months attacking the Danish State Church in a series of polemical pamphlets.',
    influences: ['Hegel', 'Socrates', 'Luther', 'Hamann', 'Schleiermacher'],
    influenced: ['Barth', 'Heidegger', 'Sartre', 'Camus', 'Buber', 'Tillich', 'Derrida'],
    keyWorks: ['either-or', 'fear-and-trembling', 'concept-of-anxiety', 'concluding-unscientific-postscript', 'sickness-unto-death'],
    tradition: 'Father of existentialism; the definitive critic of speculative idealism and the philosopher who made the single individual the irreducible subject of philosophy.',
    quote: 'The most common form of despair is not being who you are.',
    quoteSource: 'The Sickness Unto Death, Part One'
  },

  marx: {
    name: 'Karl Marx \u0026 Friedrich Engels',
    born: '1818 / 1820', died: '1883 / 1895', birthYear: 1818,
    location: 'Trier / Paris / Brussels / London / Manchester',
    school: 'Historical Materialism / Communism',
    color: '#8B1A1A',
    tagline: 'The two thinkers who turned Hegel right-side up, placed philosophy in the service of revolution, and wrote the document that haunted an entire century: a spectre is haunting Europe.',
    bio: 'Karl Marx was born on 5 May 1818 in Trier, in the Rhineland. His father was a lawyer of Jewish descent who had converted to Lutheranism to avoid professional restrictions. Marx studied law at Bonn and Berlin, where he became involved with the Young Hegelians, completing a doctorate on Democritus and Epicurus at Jena in 1841. His radical journalism got him expelled from Prussia, France, and Belgium in succession.\n\nFriedrich Engels was born on 28 November 1820 in Barmen in the Rhineland, the son of a textile manufacturer. His father sent him to Manchester to manage the family\u2019s cotton mills \u2014 which gave Engels firsthand knowledge of industrial capitalism that informed The Condition of the Working Class in England (1845) and, indirectly, Capital. He first met Marx in Paris in 1844; their lifelong collaboration began immediately.\n\nMarx and his family lived in desperate poverty in London from 1849 to his death in 1883, sustained primarily by Engels\u2019 financial support. Marx spent his days in the British Museum Reading Room, working through an enormous quantity of economic literature to produce the Grundrisse (1857\u201358) and Capital Vol. I (1867). He died on 14 March 1883 with Volumes II and III unfinished; Engels edited and published them from Marx\u2019s manuscripts (1885, 1894). Engels survived until 5 August 1895.',
    influences: ['Hegel', 'Feuerbach', 'Smith', 'Ricardo', 'Owen', 'Saint-Simon'],
    influenced: ['Lenin', 'Luxemburg', 'Gramsci', 'Lukacs', 'Frankfurt School', 'Althusser', 'Sartre'],
    keyWorks: ['capital-vol1', 'communist-manifesto', 'economic-philosophical-manuscripts', 'german-ideology', 'grundrisse'],
    tradition: 'Founders of historical materialism, scientific socialism, and the most consequential political movement of the twentieth century.',
    quote: 'Workers of all lands, unite!',
    quoteSource: 'The Communist Manifesto, closing line'
  },

  nietzsche: {
    name: 'Friedrich Nietzsche',
    born: '1844', died: '1900', birthYear: 1844,
    location: 'R\u00f6cken / Basel / Sils-Maria / Weimar',
    school: 'Life-Philosophy / Existentialism',
    color: '#8B1A1A',
    tagline: 'The philosopher with a hammer \u2014 who announced the death of God, demanded the revaluation of all values, and wrote the most dangerous books in modern philosophy before collapsing in Turin in January 1889, never to recover.',
    bio: 'Friedrich Nietzsche was born on 15 October 1844 in R\u00f6cken, Saxony, the son of a Lutheran pastor who died when Nietzsche was five. He was educated at Schulpforta (the finest classical school in Germany), Bonn, and Leipzig, where he discovered Schopenhauer\u2019s World as Will and Representation in a secondhand bookshop in 1865. He was appointed professor of classical philology at Basel at twenty-four \u2014 the youngest ever appointed to such a position \u2014 before completing his doctorate.\n\nNietzsche served as a medical orderly in the Franco-Prussian War (1870\u201371), contracted dysentery and diphtheria, and returned to Basel with permanently damaged health. The Birth of Tragedy (1872) was his sensational debut; it alienated his classical colleagues and established his reputation as a philosophical maverick. His friendship with Wagner \u2014 intense, productive, and eventually shattered \u2014 shaped and then defined the trajectory of his thought.\n\nThe middle and late periods \u2014 Human All Too Human (1878) through Thus Spoke Zarathustra (1883\u201385), Beyond Good and Evil (1886), and the torrent of 1888 (The Case of Wagner, Twilight of the Idols, The Anti-Christ, Ecce Homo, Nietzsche contra Wagner) \u2014 are the record of one of the most extraordinary intellectual and creative accelerations in the history of thought. In January 1889, Nietzsche collapsed in Turin. He spent the remaining eleven years of his life in a state of mental collapse, nursed by his mother and then his sister Elisabeth, who managed his literary estate with disastrous ideological consequences.',
    influences: ['Schopenhauer', 'Wagner', 'Heraclitus', 'Emerson', 'Thucydides'],
    influenced: ['Heidegger', 'Jaspers', 'Camus', 'Foucault', 'Derrida', 'Mann', 'Yeats'],
    keyWorks: ['birth-of-tragedy', 'gay-science', 'zarathustra', 'beyond-good-evil', 'genealogy-morality', 'ecce-homo'],
    tradition: 'The philosopher of the revaluation of values; precursor of existentialism, poststructuralism, and all subsequent philosophical engagement with nihilism.',
    quote: 'God is dead. God remains dead. And we have killed him.',
    quoteSource: 'The Gay Science, \u00a7125'
  }
};
"""

bios_path = os.path.join(js_dir, 'philosopher-bios.js')
with open(bios_path, 'w', encoding='utf-8') as f:
    f.write(BIOS_JS)
changes.append('philosopher-bios.js written')

# ════════════════════════════════════════════════════════════════════════════
# 2. PHILOSOPHER BIO PAGE (philosopher.html)
# ════════════════════════════════════════════════════════════════════════════

BIO_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Philosopher — The Academy &amp; The Lyceum</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;0,700;1,300;1,400;1,600&family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&family=JetBrains+Mono:wght@300;400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
<style>
  .bio-hero {
    padding: 80px 0 60px;
    border-bottom: 1px solid var(--border);
  }
  .bio-hero .container { max-width: 760px; }
  .bio-school-tag {
    font-family: var(--font-mono);
    font-size: 0.72rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--gold);
    margin-bottom: 20px;
    display: block;
  }
  .bio-name {
    font-family: var(--font-heading);
    font-size: clamp(2.4rem, 5vw, 3.8rem);
    font-weight: 300;
    line-height: 1.1;
    color: var(--text);
    margin-bottom: 8px;
  }
  .bio-dates {
    font-family: var(--font-mono);
    font-size: 0.8rem;
    color: var(--text-muted);
    letter-spacing: 0.06em;
    margin-bottom: 28px;
  }
  .bio-tagline {
    font-family: var(--font-body);
    font-size: 1.08rem;
    font-style: italic;
    color: var(--text-secondary);
    line-height: 1.8;
    max-width: 640px;
    border-left: 3px solid var(--philosopher-color, var(--gold));
    padding-left: 20px;
  }
  .bio-body {
    padding: 64px 0;
  }
  .bio-body .container { max-width: 760px; }
  .bio-section { margin-bottom: 52px; }
  .bio-section-title {
    font-family: var(--font-mono);
    font-size: 0.7rem;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: var(--text-muted);
    margin-bottom: 20px;
    padding-bottom: 10px;
    border-bottom: 1px solid var(--border);
  }
  .bio-text {
    font-family: var(--font-body);
    font-size: 0.95rem;
    line-height: 1.92;
    color: var(--text-secondary);
  }
  .bio-text p { margin-bottom: 1.2em; }
  .bio-influences {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
  }
  .bio-influence-chip {
    font-family: var(--font-mono);
    font-size: 0.68rem;
    letter-spacing: 0.06em;
    padding: 5px 12px;
    border: 1px solid var(--border);
    border-radius: 3px;
    color: var(--text-secondary);
    background: var(--bg-secondary);
    transition: border-color 0.2s;
  }
  .bio-influence-chip:hover { border-color: var(--philosopher-color, var(--gold)); }
  .bio-quote {
    border-left: 3px solid var(--philosopher-color, var(--gold));
    padding: 16px 24px;
    margin: 0;
    background: var(--bg-secondary);
    border-radius: 0 4px 4px 0;
  }
  .bio-quote-text {
    font-family: var(--font-heading);
    font-size: 1.15rem;
    font-style: italic;
    color: var(--text);
    line-height: 1.6;
    margin-bottom: 8px;
  }
  .bio-quote-source {
    font-family: var(--font-mono);
    font-size: 0.67rem;
    letter-spacing: 0.08em;
    color: var(--text-muted);
  }
  .bio-works-link {
    display: inline-block;
    margin-top: 40px;
    font-family: var(--font-mono);
    font-size: 0.75rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--philosopher-color, var(--gold));
    border: 1px solid var(--philosopher-color, var(--gold));
    padding: 10px 24px;
    border-radius: 3px;
    text-decoration: none;
    transition: all 0.2s;
  }
  .bio-works-link:hover {
    background: var(--philosopher-color, var(--gold));
    color: #fff;
  }
  .bio-back {
    font-family: var(--font-mono);
    font-size: 0.7rem;
    letter-spacing: 0.1em;
    color: var(--text-muted);
    text-decoration: none;
    margin-bottom: 32px;
    display: inline-block;
    transition: color 0.2s;
  }
  .bio-back:hover { color: var(--text); }
  .bio-not-found {
    padding: 120px 0;
    text-align: center;
    font-family: var(--font-heading);
    font-size: 1.5rem;
    color: var(--text-muted);
  }
</style>
</head>
<body>
<nav class="navbar" role="navigation" aria-label="Main navigation">
  <div class="nav-container">
    <a href="index.html" class="nav-logo">The Academy &amp; The Lyceum</a>
    <div class="nav-actions">
      <button class="nav-btn theme-toggle" id="themeToggle" aria-label="Toggle theme">
        <span class="theme-icon-dark">Moon</span>
        <span class="theme-icon-light">Sun</span>
      </button>
    </div>
  </div>
</nav>

<main id="bio-main">
  <div class="bio-not-found" id="bioNotFound" style="display:none;">
    Philosopher not found. <a href="index.html" style="color:var(--gold);">Return to archive.</a>
  </div>
  <div id="bioContent" style="display:none;">
    <section class="bio-hero">
      <div class="container">
        <a href="index.html" class="bio-back" id="bioBack">&larr; Back to archive</a>
        <span class="bio-school-tag" id="bioSchool"></span>
        <h1 class="bio-name" id="bioName"></h1>
        <p class="bio-dates" id="bioDates"></p>
        <p class="bio-tagline" id="bioTagline"></p>
      </div>
    </section>
    <section class="bio-body">
      <div class="container">
        <div class="bio-section">
          <h2 class="bio-section-title">Life</h2>
          <div class="bio-text" id="bioText"></div>
        </div>
        <div class="bio-section">
          <h2 class="bio-section-title">Quote</h2>
          <blockquote class="bio-quote">
            <p class="bio-quote-text" id="bioQuote"></p>
            <cite class="bio-quote-source" id="bioQuoteSource"></cite>
          </blockquote>
        </div>
        <div class="bio-section" id="bioInfluencesSection">
          <h2 class="bio-section-title">Influenced By</h2>
          <div class="bio-influences" id="bioInfluences"></div>
        </div>
        <div class="bio-section" id="bioInfluencedSection">
          <h2 class="bio-section-title">Influence On</h2>
          <div class="bio-influences" id="bioInfluenced"></div>
        </div>
        <div class="bio-section">
          <h2 class="bio-section-title">Position in Tradition</h2>
          <p class="bio-text" id="bioTradition"></p>
        </div>
        <a href="index.html" class="bio-works-link" id="bioWorksLink">&rarr; View Works</a>
      </div>
    </section>
  </div>
</main>

<script src="js/philosopher-bios.js"></script>
<script>
(function(){
  var params = new URLSearchParams(window.location.search);
  var key = (params.get('p') || '').toLowerCase();
  var bio = window.PHILOSOPHER_BIOS && window.PHILOSOPHER_BIOS[key];
  if (!bio) {
    document.getElementById('bioNotFound').style.display = 'block';
    document.title = 'Not Found \u2014 The Academy & The Lyceum';
    return;
  }
  document.getElementById('bioContent').style.display = 'block';
  document.title = bio.name + ' \u2014 The Academy & The Lyceum';
  document.documentElement.style.setProperty('--philosopher-color', bio.color);
  document.getElementById('bioSchool').textContent = bio.school + '\u00a0\u00b7\u00a0' + bio.location;
  document.getElementById('bioName').textContent = bio.name;
  document.getElementById('bioDates').textContent = bio.born + '\u2013' + bio.died;
  document.getElementById('bioTagline').textContent = bio.tagline;
  document.getElementById('bioQuote').textContent = '\u201c' + bio.quote + '\u201d';
  document.getElementById('bioQuoteSource').textContent = bio.quoteSource;
  document.getElementById('bioTradition').textContent = bio.tradition;
  var worksLink = document.getElementById('bioWorksLink');
  worksLink.href = 'index.html#' + key + '-section';
  worksLink.textContent = '\u2192 View ' + bio.name.split(' ')[0] + '\u2019s Works';
  // Bio text — split on \n\n into paragraphs
  var textEl = document.getElementById('bioText');
  bio.bio.split('\n\n').forEach(function(p){
    var el = document.createElement('p');
    el.textContent = p.trim();
    textEl.appendChild(el);
  });
  // Influences
  function renderChips(ids, containerId) {
    var c = document.getElementById(containerId);
    ids.forEach(function(name){
      var chip = document.createElement('span');
      chip.className = 'bio-influence-chip';
      chip.textContent = name;
      c.appendChild(chip);
    });
  }
  renderChips(bio.influences || [], 'bioInfluences');
  renderChips(bio.influenced || [], 'bioInfluenced');
  // Theme toggle
  var saved = localStorage.getItem('theme') || 'light';
  if (saved === 'dark') document.documentElement.setAttribute('data-theme','dark');
  document.getElementById('themeToggle').addEventListener('click', function(){
    var current = document.documentElement.getAttribute('data-theme') || 'light';
    var next = current === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    localStorage.setItem('theme', next);
  });
})();
</script>
</body>
</html>
"""

bio_page_path = os.path.join(base, 'philosopher.html')
with open(bio_page_path, 'w', encoding='utf-8') as f:
    f.write(BIO_HTML)
changes.append('philosopher.html written')

# ════════════════════════════════════════════════════════════════════════════
# 3. CONCEPT INDEX PAGE (concepts.html)
# ════════════════════════════════════════════════════════════════════════════

CONCEPTS_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Concept Index \u2014 The Academy &amp; The Lyceum</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;0,700;1,300;1,400;1,600&family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&family=JetBrains+Mono:wght@300;400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
<style>
  .ci-hero { padding:80px 0 48px; border-bottom:1px solid var(--border); }
  .ci-hero .container { max-width:820px; }
  .ci-back { font-family:var(--font-mono);font-size:0.7rem;letter-spacing:0.1em;color:var(--text-muted);text-decoration:none;margin-bottom:32px;display:inline-block;transition:color 0.2s; }
  .ci-back:hover { color:var(--text); }
  .ci-title { font-family:var(--font-heading);font-size:clamp(2rem,4vw,3.2rem);font-weight:300;color:var(--text);margin-bottom:8px; }
  .ci-subtitle { font-family:var(--font-body);font-size:0.95rem;font-style:italic;color:var(--text-secondary);line-height:1.7;margin-bottom:28px; }
  .ci-controls { display:flex;gap:12px;flex-wrap:wrap;align-items:center; }
  .ci-search {
    flex:1;min-width:200px;max-width:400px;
    font-family:var(--font-body);font-size:0.9rem;
    padding:10px 16px;
    border:1px solid var(--border);
    border-radius:var(--radius);
    background:var(--bg);
    color:var(--text);
    outline:none;transition:border-color 0.2s;
  }
  .ci-search:focus { border-color:var(--gold); }
  .ci-filter-phil {
    font-family:var(--font-mono);font-size:0.68rem;letter-spacing:0.08em;
    padding:9px 14px;
    border:1px solid var(--border);border-radius:var(--radius);
    background:var(--bg);color:var(--text-secondary);cursor:pointer;
    transition:all 0.2s;
  }
  .ci-filter-phil.active,.ci-filter-phil:hover { border-color:var(--gold);color:var(--gold); }
  .ci-stats { font-family:var(--font-mono);font-size:0.68rem;letter-spacing:0.06em;color:var(--text-muted);padding:4px 0; }
  .ci-body { padding:48px 0 80px; }
  .ci-body .container { max-width:820px; }
  .ci-concept-list { list-style:none;padding:0;margin:0; }
  .ci-concept-item {
    padding:18px 0;
    border-bottom:1px solid var(--border);
    display:grid;
    grid-template-columns:1fr auto;
    gap:8px 20px;
    align-items:start;
    cursor:pointer;
    transition:background 0.15s;
  }
  .ci-concept-item:hover { background:var(--bg-secondary);padding-left:10px;margin-left:-10px;padding-right:10px; }
  .ci-concept-term {
    font-family:var(--font-heading);font-size:0.98rem;font-weight:700;font-style:italic;
    color:var(--text);line-height:1.3;
  }
  .ci-concept-desc {
    font-family:var(--font-body);font-size:0.845rem;color:var(--text-secondary);
    line-height:1.72;grid-column:1;margin-top:4px;
  }
  .ci-concept-works { grid-column:2;grid-row:1/3;display:flex;flex-direction:column;gap:4px;align-items:flex-end; }
  .ci-concept-tag {
    font-family:var(--font-mono);font-size:0.6rem;letter-spacing:0.08em;
    padding:3px 8px;border-radius:3px;
    border:1px solid var(--border);color:var(--text-muted);
    white-space:nowrap;cursor:pointer;transition:all 0.15s;
  }
  .ci-concept-tag:hover { border-color:var(--gold);color:var(--gold); }
  .ci-empty { padding:80px 0;text-align:center;font-family:var(--font-heading);font-size:1.2rem;font-style:italic;color:var(--text-muted); }
  .ci-loading { padding:60px 0;text-align:center;font-family:var(--font-mono);font-size:0.8rem;color:var(--text-muted);letter-spacing:0.08em; }
</style>
</head>
<body>
<nav class="navbar" role="navigation">
  <div class="nav-container">
    <a href="index.html" class="nav-logo">The Academy &amp; The Lyceum</a>
    <div class="nav-actions">
      <button class="nav-btn theme-toggle" id="themeToggle" aria-label="Toggle theme">
        <span class="theme-icon-dark">Moon</span>
        <span class="theme-icon-light">Sun</span>
      </button>
    </div>
  </div>
</nav>

<section class="ci-hero">
  <div class="container">
    <a href="index.html" class="ci-back">&larr; Back to archive</a>
    <h1 class="ci-title">Concept Index</h1>
    <p class="ci-subtitle">Every named concept across all works in the archive \u2014 searchable, filterable by philosopher, and linked back to the work that defines it.</p>
    <div class="ci-controls">
      <input type="text" class="ci-search" id="ciSearch" placeholder="Search concepts\u2026" autocomplete="off" spellcheck="false">
      <div id="ciPhilFilters" style="display:flex;gap:8px;flex-wrap:wrap;"></div>
    </div>
    <p class="ci-stats" id="ciStats"></p>
  </div>
</section>

<section class="ci-body">
  <div class="container">
    <div class="ci-loading" id="ciLoading">Loading concepts\u2026</div>
    <ul class="ci-concept-list" id="ciList"></ul>
    <div class="ci-empty" id="ciEmpty" style="display:none;">No concepts match your search.</div>
  </div>
</section>

<!-- Load all data files -->
<script src="js/data.js"></script>
<script src="js/data-01.js"></script><script src="js/data-02.js"></script>
<script src="js/data-03.js"></script><script src="js/data-04.js"></script>
<script src="js/data-05.js"></script><script src="js/data-06.js"></script>
<script src="js/data-07.js"></script><script src="js/data-08.js"></script>
<script src="js/data-09.js"></script><script src="js/data-10.js"></script>
<script src="js/data-11a.js"></script><script src="js/data-11b.js"></script>
<script src="js/data-11c.js"></script><script src="js/data-11d.js"></script>
<script src="js/data-11e.js"></script>
<script src="js/data-12a.js"></script><script src="js/data-12b.js"></script>
<script src="js/data-12c.js"></script><script src="js/data-12d.js"></script>
<script src="js/data-12e.js"></script>
<script src="js/data-13a.js"></script><script src="js/data-13b.js"></script>
<script src="js/data-13c.js"></script><script src="js/data-13d.js"></script>
<script src="js/data-13e.js"></script>
<script src="js/data-14a.js"></script><script src="js/data-14b.js"></script>
<script src="js/data-14c.js"></script><script src="js/data-14d.js"></script>
<script src="js/data-14e.js"></script>
<script src="js/data-15a.js"></script><script src="js/data-15b.js"></script>
<script src="js/data-15c.js"></script><script src="js/data-15d.js"></script>
<script src="js/data-15e.js"></script>
<script src="js/data-16a.js"></script><script src="js/data-16b.js"></script>
<script src="js/data-16c.js"></script><script src="js/data-16d.js"></script>
<script src="js/data-16e.js"></script>
<script src="js/data-17a.js"></script><script src="js/data-17b.js"></script>
<script src="js/data-17c.js"></script><script src="js/data-17d.js"></script>
<script src="js/data-18a.js"></script><script src="js/data-18b.js"></script>
<script src="js/data-18c.js"></script><script src="js/data-18d.js"></script>
<script src="js/data-19a.js"></script><script src="js/data-19b.js"></script>
<script src="js/data-19c.js"></script><script src="js/data-19d.js"></script>
<script src="js/data-19e.js"></script>
<script src="js/data-20a.js"></script><script src="js/data-20b.js"></script>
<script src="js/data-20c.js"></script><script src="js/data-20d.js"></script>
<script src="js/data-20e.js"></script>
<script src="js/data-21a.js"></script><script src="js/data-21b.js"></script>
<script src="js/data-21c.js"></script><script src="js/data-21d.js"></script>
<script src="js/data-21e.js"></script>
<script src="js/data-22a.js"></script><script src="js/data-22b.js"></script>
<script src="js/data-22c.js"></script><script src="js/data-22d.js"></script>
<script src="js/data-22e.js"></script>
<script src="js/philosopher-bios.js"></script>
<script>
(function(){
  // Theme
  var saved = localStorage.getItem('theme') || 'light';
  if (saved === 'dark') document.documentElement.setAttribute('data-theme','dark');
  document.getElementById('themeToggle').addEventListener('click', function(){
    var c = document.documentElement.getAttribute('data-theme')||'light';
    var n = c==='dark'?'light':'dark';
    document.documentElement.setAttribute('data-theme',n);
    localStorage.setItem('theme',n);
  });

  var PHIL_NAMES = {
    plato:'Plato', aristotle:'Aristotle', descartes:'Descartes',
    spinoza:'Spinoza', leibniz:'Leibniz', locke:'Locke',
    berkeley:'Berkeley', hume:'Hume', kant:'Kant',
    fichte:'Fichte', schelling:'Schelling', hegel:'Hegel',
    schopenhauer:'Schopenhauer', kierkegaard:'Kierkegaard',
    marx:'Marx & Engels', nietzsche:'Nietzsche'
  };
  function philName(p){ return PHIL_NAMES[p]||(p.charAt(0).toUpperCase()+p.slice(1)); }

  var works = window.WORKS || [];

  // Build concept index: [{term, desc, work, philosopher}]
  var concepts = [];
  works.forEach(function(work){
    if (!work.concepts || !work.concepts.length) return;
    work.concepts.forEach(function(c){
      var text = typeof c === 'string' ? c : (c.text || '');
      if (!text) return;
      // Parse "Term \u2014 description"
      var dash = text.search(/\s[\u2014\u2013]\s/);
      var term = dash !== -1 ? text.substring(0, dash).trim() : text.trim();
      var desc = dash !== -1 ? text.substring(dash).replace(/^\s*[\u2014\u2013]\s*/,'').trim() : '';
      concepts.push({ term:term, desc:desc, full:text, workId:work.id, workTitle:work.title, philosopher:work.philosopher });
    });
  });
  // Sort alphabetically by term
  concepts.sort(function(a,b){ return a.term.toLowerCase().localeCompare(b.term.toLowerCase()); });

  var activePhi = 'all';
  var searchQ = '';

  // Build philosopher filter buttons
  var philSet = {};
  concepts.forEach(function(c){ philSet[c.philosopher] = true; });
  var philFilters = document.getElementById('ciPhilFilters');
  var allBtn = document.createElement('button');
  allBtn.className = 'ci-filter-phil active';
  allBtn.textContent = 'All';
  allBtn.dataset.phil = 'all';
  philFilters.appendChild(allBtn);
  Object.keys(philSet).sort().forEach(function(p){
    var btn = document.createElement('button');
    btn.className = 'ci-filter-phil';
    btn.textContent = philName(p);
    btn.dataset.phil = p;
    philFilters.appendChild(btn);
  });
  philFilters.addEventListener('click', function(e){
    var btn = e.target.closest('.ci-filter-phil');
    if (!btn) return;
    activePhi = btn.dataset.phil;
    philFilters.querySelectorAll('.ci-filter-phil').forEach(function(b){ b.classList.remove('active'); });
    btn.classList.add('active');
    render();
  });

  // Search
  document.getElementById('ciSearch').addEventListener('input', function(){
    searchQ = this.value.toLowerCase();
    render();
  });

  function getPhilColor(p){
    var bios = window.PHILOSOPHER_BIOS || {};
    return bios[p] ? bios[p].color : 'var(--gold)';
  }

  function render(){
    var q = searchQ;
    var filtered = concepts.filter(function(c){
      if (activePhi !== 'all' && c.philosopher !== activePhi) return false;
      if (q && c.full.toLowerCase().indexOf(q) === -1 && c.workTitle.toLowerCase().indexOf(q) === -1) return false;
      return true;
    });
    var list = document.getElementById('ciList');
    var empty = document.getElementById('ciEmpty');
    var stats = document.getElementById('ciStats');
    document.getElementById('ciLoading').style.display = 'none';
    stats.textContent = filtered.length + ' concepts' + (concepts.length !== filtered.length ? ' of ' + concepts.length : '') + ' across ' + works.length + ' works';
    if (filtered.length === 0){
      list.innerHTML = '';
      empty.style.display = 'block';
      return;
    }
    empty.style.display = 'none';
    list.innerHTML = '';
    filtered.forEach(function(c){
      var li = document.createElement('li');
      li.className = 'ci-concept-item';
      var color = getPhilColor(c.philosopher);
      // Build work tag
      var tagHtml = '<span class="ci-concept-tag" data-work="'+c.workId+'" style="border-color:'+color+'22;color:'+color+'">'+
        philName(c.philosopher)+'\u00a0\u00b7\u00a0'+c.workTitle+'</span>';
      li.innerHTML =
        '<span class="ci-concept-term">'+escHtml(c.term)+'</span>'+
        '<div class="ci-concept-works">'+tagHtml+'</div>'+
        (c.desc ? '<span class="ci-concept-desc">'+escHtml(c.desc)+'</span>' : '');
      li.querySelector('.ci-concept-tag').addEventListener('click', function(e){
        e.stopPropagation();
        window.location.href = 'index.html#work='+c.workId;
      });
      li.addEventListener('click', function(){
        window.location.href = 'index.html#work='+c.workId;
      });
      list.appendChild(li);
    });
  }

  function escHtml(s){
    return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
  }

  // Initial render
  setTimeout(render, 50);
})();
</script>
</body>
</html>
"""

concepts_path = os.path.join(base, 'concepts.html')
with open(concepts_path, 'w', encoding='utf-8') as f:
    f.write(CONCEPTS_HTML)
changes.append('concepts.html written')

# ════════════════════════════════════════════════════════════════════════════
# 4. TIMELINE REBUILD — patch script.js + style.css
# ════════════════════════════════════════════════════════════════════════════

with open(script_dst, 'r', encoding='utf-8') as f:
    script = f.read()

# Philosopher birth years for timeline positioning
TIMELINE_DATA_JS = """
    /* ── TIMELINE PHILOSOPHER DATA ── */
    var PHIL_TIMELINE = [
      { id:'plato',         name:'Plato',             born:-428, died:-348, color:'#6B4C9A' },
      { id:'aristotle',     name:'Aristotle',          born:-384, died:-322, color:'#2D7D6F' },
      { id:'descartes',     name:'Descartes',          born:1596, died:1650, color:'#2B4C8C' },
      { id:'spinoza',       name:'Spinoza',            born:1632, died:1677, color:'#2D6A4F' },
      { id:'leibniz',       name:'Leibniz',            born:1646, died:1716, color:'#2E4057' },
      { id:'locke',         name:'Locke',              born:1632, died:1704, color:'#8B6520' },
      { id:'berkeley',      name:'Berkeley',           born:1685, died:1753, color:'#8B6914' },
      { id:'hume',          name:'Hume',               born:1711, died:1776, color:'#3E5368' },
      { id:'kant',          name:'Kant',               born:1724, died:1804, color:'#2B4C6F' },
      { id:'hegel',         name:'Hegel',              born:1770, died:1831, color:'#1E3A5F' },
      { id:'schopenhauer',  name:'Schopenhauer',       born:1788, died:1860, color:'#7B4F2E' },
      { id:'kierkegaard',   name:'Kierkegaard',        born:1813, died:1855, color:'#6B2737' },
      { id:'marx',          name:'Marx & Engels',      born:1818, died:1895, color:'#8B1A1A' },
      { id:'nietzsche',     name:'Nietzsche',          born:1844, died:1900, color:'#8B1A1A' },
      { id:'fichte',        name:'Fichte',             born:1762, died:1814, color:'#4A5568' },
      { id:'schelling',     name:'Schelling',          born:1775, died:1854, color:'#553C7B' }
    ];
    var ERAS = [
      { label:'Ancient Greece', start:-470, end:-280, color:'rgba(107,76,154,0.06)' },
      { label:'Early Modern',   start:1580, end:1780, color:'rgba(45,125,111,0.06)' },
      { label:'German Idealism',start:1755, end:1840, color:'rgba(30,58,95,0.06)'   },
      { label:'19th Century',   start:1788, end:1900, color:'rgba(139,26,26,0.06)'  }
    ];
"""

NEW_RENDER_TIMELINE = """    function renderTimeline() {
        if (!D.timelineTrack) return;

        /* Determine which philosophers actually have works in WORKS */
        var present = {};
        W().forEach(function(w){ present[w.philosopher] = true; });
        var active = PHIL_TIMELINE.filter(function(p){ return present[p.id]; });
        if (active.length === 0) { active = PHIL_TIMELINE; }

        /* Year range */
        var minY = Math.min.apply(null, active.map(function(p){ return p.born; }));
        var maxY = Math.max.apply(null, active.map(function(p){ return p.died; }));
        var range = maxY - minY;
        function pct(y){ return ((y - minY) / range * 100).toFixed(3) + '%'; }

        /* Track width: proportional, minimum 1600px */
        var trackW = Math.max(1600, active.length * 140);
        D.timelineTrack.style.width = trackW + 'px';
        D.timelineTrack.style.position = 'relative';
        D.timelineTrack.style.height = '160px';
        D.timelineTrack.innerHTML = '';

        /* Timeline line */
        var line = document.createElement('div');
        line.className = 'timeline-line';
        line.style.cssText = 'position:absolute;top:60px;left:5%;right:5%;height:1px;background:var(--border);';
        D.timelineTrack.appendChild(line);

        /* Era bands */
        ERAS.forEach(function(era){
            var s = Math.max(era.start, minY);
            var e = Math.min(era.end, maxY);
            if (s >= e) return;
            var band = document.createElement('div');
            var leftPct = ((s - minY) / range * 90 + 5).toFixed(2);
            var widthPct = ((e - s) / range * 90).toFixed(2);
            band.style.cssText = 'position:absolute;top:0;bottom:0;' +
                'left:' + leftPct + '%;width:' + widthPct + '%;' +
                'background:' + era.color + ';pointer-events:none;';
            var eraLabel = document.createElement('span');
            eraLabel.style.cssText = 'position:absolute;bottom:8px;left:50%;transform:translateX(-50%);' +
                'font-family:var(--font-mono);font-size:0.6rem;letter-spacing:0.1em;color:var(--text-muted);' +
                'white-space:nowrap;';
            eraLabel.textContent = era.label.toUpperCase();
            band.appendChild(eraLabel);
            D.timelineTrack.appendChild(band);
        });

        /* Philosopher nodes */
        active.forEach(function(phil){
            var node = document.createElement('div');
            var leftPct = ((phil.born - minY) / range * 90 + 5).toFixed(2);
            node.style.cssText = 'position:absolute;left:' + leftPct + '%;' +
                'top:0;transform:translateX(-50%);' +
                'display:flex;flex-direction:column;align-items:center;' +
                'cursor:pointer;width:110px;transition:transform 0.2s;';
            node.setAttribute('role','button');
            node.setAttribute('tabindex','0');
            node.setAttribute('aria-label', phil.name + ', ' + (phil.born < 0 ? Math.abs(phil.born)+'BC' : phil.born));

            var dateEl = document.createElement('span');
            dateEl.style.cssText = 'font-family:var(--font-mono);font-size:0.62rem;' +
                'color:var(--gold);letter-spacing:0.08em;margin-bottom:10px;';
            dateEl.textContent = (phil.born < 0 ? Math.abs(phil.born)+'BC' : phil.born);
            node.appendChild(dateEl);

            var dot = document.createElement('div');
            dot.style.cssText = 'width:11px;height:11px;border-radius:50%;' +
                'background:' + phil.color + ';' +
                'border:2px solid var(--bg);' +
                'margin-bottom:10px;position:relative;z-index:2;' +
                'transition:transform 0.2s,box-shadow 0.2s;';
            node.appendChild(dot);

            var nameEl = document.createElement('span');
            nameEl.style.cssText = 'font-family:var(--font-heading);font-size:0.82rem;' +
                'font-weight:600;text-align:center;color:var(--text);' +
                'line-height:1.25;max-width:100px;';
            nameEl.textContent = phil.name;
            node.appendChild(nameEl);

            node.addEventListener('mouseenter', function(){
                dot.style.transform = 'scale(1.5)';
                dot.style.boxShadow = '0 0 0 3px ' + phil.color + '33';
                node.style.transform = 'translateX(-50%) translateY(-3px)';
            });
            node.addEventListener('mouseleave', function(){
                dot.style.transform = '';
                dot.style.boxShadow = '';
                node.style.transform = 'translateX(-50%)';
            });

            function goToPhil(){
                /* Try to activate the filter tab and scroll to section */
                var tab = document.querySelector('[data-filter="'+phil.id+'"]');
                if (tab) { tab.click(); }
                var section = document.getElementById(phil.id+'-section');
                if (section) { section.scrollIntoView({behavior:'smooth',block:'start'}); }
            }
            node.addEventListener('click', goToPhil);
            node.addEventListener('keydown', function(e){
                if (e.key==='Enter'||e.key===' '){ e.preventDefault(); goToPhil(); }
            });

            D.timelineTrack.appendChild(node);
        });

        /* Update era label on scroll */
        if (D.timelineContainer) {
            D.timelineContainer.addEventListener('scroll', function(){
                var scrollRatio = D.timelineContainer.scrollLeft /
                    (D.timelineContainer.scrollWidth - D.timelineContainer.clientWidth || 1);
                var year = Math.round(minY + scrollRatio * range);
                var label = 'Western Philosophy';
                ERAS.forEach(function(e){ if (year >= e.start && year <= e.end) label = e.label; });
                if (D.timelineEra) D.timelineEra.textContent = label;
            });
        }
    }
"""

# Replace the old renderTimeline function
OLD_RENDER = r"""    function renderTimeline() {
        if (!D.timelineTrack) return;
        var sorted = W().slice().sort(function(a,b){ return a.dateSort-b.dateSort; });
        D.timelineTrack.innerHTML = '<div class=\"timeline-line\" aria-hidden=\"true\"></div>';
        sorted.forEach(function(work){
            var node = document.createElement('div');
            node.className = 'timeline-node '+work.philosopher+'-node';
            var gi = W().indexOf(work);
            node.setAttribute('role','button'); node.setAttribute('tabindex','0');
            node.innerHTML =
                '<span class=\"timeline-date\">'+escHtml(work.date)+'</span>'+
                '<div class=\"timeline-dot\"></div>'+
                '<span class=\"timeline-title\">'+escHtml(work.title)+'</span>'+
                '<span class=\"timeline-author\">'+escHtml(philName(work.philosopher))+'</span>';
            node.addEventListener('click', function(){ openModal(gi); });
            node.addEventListener('keydown', function(e){ if(e.key==='Enter'||e.key===' '){ e.preventDefault(); openModal(gi); } });
            D.timelineTrack.appendChild(node);
        });
    }"""

if OLD_RENDER in script:
    script = script.replace(OLD_RENDER, NEW_RENDER_TIMELINE)
    changes.append('renderTimeline() rebuilt as philosopher-level timeline')
else:
    changes.append('WARNING: old renderTimeline pattern not found — injecting before scrollTL')

# Inject PHIL_TIMELINE data before the renderTimeline function
if 'var PHIL_TIMELINE' not in script:
    # Insert before renderTimeline or before scrollTL
    insert_anchor = '    function scrollTL'
    if insert_anchor in script:
        script = script.replace(insert_anchor, TIMELINE_DATA_JS + '\n' + insert_anchor)
        changes.append('PHIL_TIMELINE data injected into script.js')

with open(script_dst, 'w', encoding='utf-8') as f:
    f.write(script)

# ════════════════════════════════════════════════════════════════════════════
# 5. CSS: timeline height + philosopher dot colours + nav links
# ════════════════════════════════════════════════════════════════════════════

PHASE2_CSS = """

/* ================================================================
   PHASE 2: Timeline rebuild + bio page + concept index
   ================================================================ */

/* Timeline: taller container for proportional layout */
.timeline-container { padding: 12px 0 40px !important; }
.timeline-track { min-width: 1600px !important; }

/* Timeline era label default */
.timeline-era { min-width: 200px; text-align: center; }

/* Concept index and bio page nav link additions */
.footer-link[href="concepts.html"] { color: var(--gold); }

"""

with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()
if '/* PHASE 2' not in css:
    with open(css_path, 'a', encoding='utf-8') as f:
        f.write(PHASE2_CSS)
    changes.append('Phase 2 CSS appended')
else:
    changes.append('Phase 2 CSS already present')

# ════════════════════════════════════════════════════════════════════════════
# 6. INDEX.HTML: add links to Concept Index and Bio pages in footer + nav
# ════════════════════════════════════════════════════════════════════════════

with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Add Concept Index link to footer archive column if not there
if 'concepts.html' not in html:
    old_footer = '<a href="tradition.html" class="footer-link">Tradition Map</a>'
    new_footer = old_footer + '\n                        <a href="concepts.html" class="footer-link">Concept Index</a>'
    if old_footer in html:
        html = html.replace(old_footer, new_footer)
        changes.append('Concept Index link added to footer')
    else:
        changes.append('WARNING: footer anchor not found for concept index link')
else:
    changes.append('Concept Index footer link already present')

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)

# ════════════════════════════════════════════════════════════════════════════
# REPORT
# ════════════════════════════════════════════════════════════════════════════
print('\nResults:')
for c in changes:
    print('  ' + ('\u26a0' if 'WARNING' in c else '\u2713'), c)
print('\nFiles produced:')
print('  js/philosopher-bios.js')
print('  philosopher.html')
print('  concepts.html')
print('\nDone. Run:')
print('  git add -A')
print('  git commit -m "Phase 2: timeline rebuild, philosopher bios, concept index"')
print('  git push')
