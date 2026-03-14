#!/usr/bin/env python3
"""
Run from inside ~/Desktop/philosophy-archive/
  python3 generate_spinoza_full.py
Writes js/data-12a.js through js/data-12e.js
Overwrites whatever is there.
"""
import os

js_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'js')
os.makedirs(js_dir, exist_ok=True)

# ─────────────────────────────────────────────────────────────────────────────
# DATA-12a  —  Ethics
# ─────────────────────────────────────────────────────────────────────────────
data_12a = r"""/* ================================================================
   DATA PART 12a — Ethics Demonstrated in Geometrical Order (Spinoza)
   ================================================================ */

window.WORKS.push(

{
    id: 'spinoza-ethics',
    title: 'Ethics',
    greekTitle: 'Ethica Ordine Geometrico Demonstrata',
    philosopher: 'spinoza',
    category: 'metaphysics',
    categoryLabel: 'Metaphysics & Ethics',
    date: '1677 AD (posthumous)',
    dateSort: 1677,
    emoji: '∞',
    cardSize: 'wide',
    readingDifficulty: 'Advanced',
    estimatedWordCount: 90000,

    shortDesc: 'The most audacious philosophical system ever written — five parts of definitions, axioms, propositions, and demonstrations proving, in strict Euclidean form, that God and Nature are one substance, that human freedom consists in the understanding of necessity, and that the highest human good is the intellectual love of God.',

    summary: 'The Ethics is written in the form of Euclid\'s Elements: definitions, axioms, propositions, demonstrations, corollaries, and scholia — as if the entire nature of God, the human mind, the passions, and human liberation could be derived with the certainty of geometry. This formal audacity is not a quirk but a philosophical claim: if reality is rational through and through, then the structure of reality must be as demonstrable as a theorem.\n\nPart I (On God) establishes the metaphysical foundation: there is only one substance, infinite, self-caused, and consisting of infinite attributes. This substance is what the tradition calls God and what nature is. Deus sive Natura — God or Nature — is Spinoza\'s most famous formula and his most radical: it means that God is not a personal being who created the world from outside it, but the immanent cause of all things, the infinite whole of which every particular thing is a finite mode. From this flows a thoroughgoing determinism: everything that exists follows from God\'s nature with the same necessity that a triangle\'s properties follow from its definition. There is no free will in the libertarian sense, no contingency, no purpose or final cause in nature. The traditional theological God — personal, transcendent, purposive, providential — is dissolved.\n\nPart II (On the Nature and Origin of the Mind) develops a theory of mind that avoids Cartesian dualism entirely. Mind and body are not two substances but two attributes — thought and extension — of the single substance. The human mind is the idea of the human body; there is a perfect parallelism between mental and physical states because they are the same thing described in two different ways. Knowledge comes in three kinds: imagination (confused ideas derived from sense experience and association), reason (common notions, adequate ideas of what things share), and intuition (scientia intuitiva — direct intellectual apprehension of the essence of things under the aspect of eternity, sub specie aeternitatis).\n\nPart III (On the Origin and Nature of the Emotions) presents the most influential theory of the passions in the early modern period. Every thing strives to persevere in its own being — the conatus, or striving — and this is the essence of each thing. The emotions are increases or decreases in the power of acting: joy is the transition to greater power, sadness to lesser. From these three primary affects — desire (conatus itself as conscious), joy, and sadness — all other emotions are derived, in a taxonomy of forty-eight definitions that constitutes the first systematic emotional psychology in Western philosophy.\n\nPart IV (On Human Bondage) analyzes the condition of servitude to the passions. Because we are finite modes of an infinite substance, we are always subject to external causes more powerful than ourselves; our passive emotions — fears, hopes, envies, regrets — arise from inadequate ideas and bind us to fortune. The free person, by contrast, thinks of nothing less than death; human freedom consists in understanding the necessity of things, not in escaping it.\n\nPart V (On the Power of the Intellect, or Human Freedom) completes the system with an account of salvation through understanding. When we form adequate ideas — when reason and intuition replace imagination — the passive emotions are transformed into active ones. The highest emotion possible is the intellectual love of God (amor intellectualis Dei): the mind\'s contemplation of itself as part of the infinite intellect of God, experienced as the highest joy. Some part of the mind, Spinoza argues, is eternal — not as personal immortality but as participation in the eternal order of ideas.',

    themes: ['God or Nature', 'Substance Monism', 'Determinism', 'The Conatus', 'Theory of the Emotions', 'Human Bondage', 'Freedom through Understanding', 'Intellectual Love of God', 'Sub Specie Aeternitatis', 'The Geometric Method'],

    keyCharacters: [
        { name: 'God / Natura Naturans', role: 'The one infinite self-caused substance; not a person or creator but the immanent cause of all things — Nature as active and self-sufficient' },
        { name: 'Modes', role: 'Particular finite things — humans, rocks, ideas, bodies — understood as determinate expressions of the one infinite substance' },
        { name: 'The Free Person', role: 'Not the libertarian free agent but the person who acts from adequate understanding rather than passive emotion; guided by reason and amor intellectualis Dei' }
    ],

    concepts: [
        'Substance monism — there is only one substance (God or Nature); mind and body are two attributes of this one substance, not two distinct things',
        'Deus sive Natura — God or Nature; the most radical formula in early modern philosophy; God is not transcendent but the immanent infinite whole',
        'Attributes and modes — attributes are what the intellect perceives as the essence of substance (thought, extension); modes are particular finite expressions of substance',
        'Conatus — the striving of each thing to persevere in its own being; the fundamental drive that is the essence of every particular thing',
        'Three kinds of knowledge — imagination (confused, passive), reason (common notions, adequate), intuition or scientia intuitiva (direct grasp of essences sub specie aeternitatis)',
        'Parallelism — the order and connection of ideas is the same as the order and connection of things; mind and body are the same event described in two ways',
        'Passive and active emotions — passive emotions arise from inadequate ideas and bind us; active emotions follow from our own nature and increase our power of acting',
        'Human bondage — the condition of servitude to the passive emotions; caused by our finitude and inadequate understanding, not by sin',
        'Intellectual love of God (amor intellectualis Dei) — the highest human emotion: the mind\'s love of God arising from the third kind of knowledge; constitutes human blessedness',
        'Sub specie aeternitatis — under the aspect of eternity; the perspective from which things are seen as necessary expressions of the infinite order, rather than as contingent temporal events'
    ],

    structure: 'Five parts in strict Euclidean form (definitions, axioms, propositions, demonstrations, scholia):\n\nPart I — On God (36 propositions): The definition of substance, attribute, mode. The self-causation of God. The infinity of substance. Deus sive Natura. Determinism. The dissolution of teleology.\n\nPart II — On the Nature and Origin of the Mind (49 propositions): The attributes of thought and extension. The human mind as the idea of the human body. The three kinds of knowledge. Adequate and inadequate ideas. The common notions.\n\nPart III — On the Origin and Nature of the Emotions (59 propositions + general definitions): The conatus. The three primary affects — desire, joy, sadness. The taxonomy of forty-eight emotions derived geometrically from the three primaries.\n\nPart IV — On Human Bondage (73 propositions): The power of the emotions over the intellect. Adequate and inadequate causation. The life of the free person. Virtue as power.\n\nPart V — On the Power of the Intellect (42 propositions): The mastery of the emotions through understanding. The eternity of the mind. Amor intellectualis Dei. Blessedness.',

    quote: 'Blessedness is not the reward of virtue, but virtue itself; nor do we delight in blessedness because we restrain our lusts, but, on the contrary, because we delight in it, therefore are we able to restrain them. — Ethics, Part V, Proposition 42, Scholium',

    additionalQuotes: [
        { text: 'God, or Nature.', citation: 'Ethics, Part IV, Preface (Deus, sive Natura — the formula that defines Spinozist pantheism)' },
        { text: 'The striving by which each thing strives to persevere in its being is nothing but the actual essence of the thing.', citation: 'Ethics, Part III, Proposition 7' },
        { text: 'A free man thinks of nothing less than of death, and his wisdom is a meditation not on death but on life.', citation: 'Ethics, Part IV, Proposition 67' },
        { text: 'The human mind has an adequate knowledge of the eternal and infinite essence of God.', citation: 'Ethics, Part II, Proposition 47' },
        { text: 'He who loves God cannot endeavour that God should love him in return.', citation: 'Ethics, Part V, Proposition 19' }
    ],

    commentary: [
        {
            philosopher: 'G.W.F. Hegel',
            text: 'Hegel\'s famous pronouncement — "To be a philosopher, one must first be a Spinozist" — captures his ambivalent relationship with the Ethics. Hegel recognized Spinoza as the philosopher who had most completely identified thinking with being, thereby dissolving the Cartesian gulf between subject and object. The substance of the Ethics — infinite, self-determining, containing all finite things as its modes — is, for Hegel, a genuine achievement: it overcomes finite dualism and grasps the absolute. But Hegel\'s critique is equally sharp: Spinoza\'s substance is a static, undifferentiated infinity, an "abyss" that swallows all determination without dialectically producing it. Spinoza achieves the absolute but cannot explain how the absolute differentiates itself into the richness of finite things and returns to itself through them. That movement — the self-development of Spirit through contradiction and synthesis — is what Hegel\'s own system supplies. For Hegel, the Ethics gets the destination right but lacks the road.'
        },
        {
            philosopher: 'Gilles Deleuze',
            text: 'Deleuze\'s two studies — Expressionism in Philosophy: Spinoza (1968) and Spinoza: Practical Philosophy (1981) — are the most philosophically creative twentieth-century readings of the Ethics and transformed Spinoza from a historical curiosity into a resource for contemporary philosophy. Deleuze argued that the key to the Ethics is not the geometric method or the metaphysical system but the concept of expression: God expresses itself in infinite attributes, each attribute expresses itself in modes, and each mode expresses the power of God at a finite degree. This ontology of expression, Deleuze argued, is an alternative to both representation (Kant\'s critical philosophy) and the dialectic (Hegel\'s negation). More practically, Deleuze read the conatus and the theory of the passions as an ethics of power — not power over others but the internal power to act rather than to suffer — which he connected to Nietzsche\'s will to power and developed into his own philosophy of difference and immanence. For Deleuze, the Ethics is the great book of immanence: the refusal of any transcendent beyond, any negative or privative principle, in favour of a pure affirmation of life as it actually is.'
        },
        {
            philosopher: 'George Eliot',
            text: 'George Eliot (Mary Ann Evans) translated the Ethics into English in 1856 — a translation that remained unpublished until the twentieth century but that profoundly shaped her thought. Eliot was drawn to Spinoza\'s conjunction of radical intellectual honesty (the dissolving of all comforting theological illusions through geometric demonstration) with ethical seriousness: the Ethics demands that we live well without the support of a personal God, providential narrative, or afterlife reward. This combination — unsentimental about metaphysics, deeply humane about human sympathy and community — marks Eliot\'s greatest novels. In Middlemarch, the character of Casaubon represents the failure of Spinoza\'s intellectual vision applied without genuine human fellow-feeling; Dorothea\'s developing sympathetic imagination is closer to what the amor intellectualis Dei demands in practice. Eliot wrote to a friend that the Ethics was "the book which has most profoundly influenced me" — a more honest tribute than most philosophers receive from novelists.'
        },
        {
            philosopher: 'Friedrich Nietzsche',
            text: 'In a famous letter to Franz Overbeck (1881), Nietzsche discovered with astonishment that he had "a precursor" in Spinoza: "He denies the freedom of the will, teleology, the moral world order, the unegoistic, and evil. Though the divergences are admittedly tremendous, they are due more to the difference in time, culture, and science." What Nietzsche recognized was the shared project of the Ethics and his own mature philosophy: to dismantle the moral-theological interpretation of existence from within, without recourse to an external standard, and to replace it with an immanent account of power, striving, and affirmation. The conatus is Nietzsche\'s will to power in an earlier idiom. But Nietzsche\'s divergences were real: he found Spinoza\'s equation of virtue with self-preservation too modest, his geometric method a disguised asceticism, and the amor intellectualis Dei a lingering theological consolation incompatible with the full affirmation of becoming that Nietzsche\'s Dionysian philosophy demanded.'
        },
        {
            philosopher: 'Albert Einstein',
            text: 'Einstein famously declared that he believed in "Spinoza\'s God" — the God of the Ethics, the God who is Nature, the God of mathematical law and rational order, not the God who rewards the good, answers prayers, or intervenes in history. This declaration, made in response to a rabbi\'s telegram asking whether he believed in God, became one of the most quoted philosophical statements of the twentieth century. Einstein\'s attachment to Spinoza was not merely rhetorical: the Ethics\' claim that the apparent contingency of the world conceals a deeper necessity, that the universe is rational through and through, corresponds to Einstein\'s lifelong conviction that "God does not play dice." His rejection of quantum indeterminacy — "He does not play dice with the universe" — is a twentieth-century reformulation of Spinoza\'s determinism. The Ethics gave Einstein a philosophical framework for his physical intuitions about the rationality of nature.'
        },
        {
            philosopher: 'Antonio Damasio',
            text: 'Damasio\'s Looking for Spinoza: Joy, Sorrow, and the Feeling Brain (2003) argued that Spinoza\'s theory of the emotions in Part III of the Ethics anticipates contemporary neuroscience more accurately than any other early modern account. Spinoza\'s central insight — that the emotions are not perturbations of a rational soul by an irrational body but are themselves the body\'s modifications registered by the mind; that joy and sadness track the organism\'s state of flourishing or decline; that the conatus is what biology calls homeostasis — all of this, Damasio argued, corresponds to what neuroimaging and affective neuroscience have established about the role of body states in the generation of feeling. The parallelism of the Ethics — mind and body as two aspects of the same event — maps onto the neural account of emotion as simultaneously bodily and mental. Damasio\'s reading restores Spinoza from the margins of the philosophical canon to the center of the conversation between philosophy and neuroscience.'
        }
    ],

    modernRelevance: 'The Ethics is the foundational text of philosophical naturalism: the attempt to understand human beings — their minds, emotions, freedom, and flourishing — within nature rather than above or against it. Every project that takes seriously both the demands of rigorous scientific understanding and the irreducibility of human meaning and ethics works in the space the Ethics defines. The denial of teleology in Part I is the philosophical foundation of Darwinian biology; the parallelism of Part II anticipates the identity theory of mind; the theory of the passions in Part III is the ancestor of cognitive-affective psychology; and Part V\'s account of freedom as understanding necessity rather than escaping it remains the most compelling alternative to both theological free will and reductive determinism. The radical democratic implications of Spinoza\'s dissolution of natural hierarchy — all things are modes of the same substance; no person stands above nature\'s order — also make the Ethics the deepest philosophical source of Enlightenment egalitarianism.',

    context: 'Spinoza worked on the Ethics from approximately 1661 until 1675, when he withdrew it from publication after hearing of the hostile reception given to the Theological-Political Treatise. He circulated manuscript copies to trusted correspondents — including Leibniz, who visited him in The Hague in 1676 — but did not publish it in his lifetime. It was published posthumously by his friends in November 1677, the year of his death from a lung disease almost certainly aggravated by years of grinding optical lenses for his livelihood. The book was immediately condemned by the Dutch authorities and placed on the Catholic Index of Forbidden Books. Spinoza had been excommunicated from the Amsterdam Jewish community in 1656, at the age of twenty-three, in the harshest herem (excommunication) in the community\'s recorded history — the reasons remain disputed but almost certainly related to views that would become the Ethics. He lived thereafter in modest lodgings in Amsterdam, Rijnsburg, Voorburg, and finally The Hague, supported by a small annuity and the lens-grinding trade.',

    relatedWorks: ['theological-political-treatise', 'treatise-on-emendation', 'political-treatise', 'spinoza-correspondence']
}

);
"""

# ─────────────────────────────────────────────────────────────────────────────
# DATA-12b  —  Theological-Political Treatise
# ─────────────────────────────────────────────────────────────────────────────
data_12b = r"""/* ================================================================
   DATA PART 12b — Theological-Political Treatise (Spinoza)
   ================================================================ */

window.WORKS.push(

{
    id: 'theological-political-treatise',
    title: 'Theological-Political Treatise',
    greekTitle: 'Tractatus Theologico-Politicus',
    philosopher: 'spinoza',
    category: 'political',
    categoryLabel: 'Political Philosophy & Religion',
    date: '1670 AD',
    dateSort: 1670,
    emoji: '📜',
    cardSize: 'wide',
    readingDifficulty: 'Advanced',
    estimatedWordCount: 120000,

    shortDesc: 'The founding text of biblical criticism, the most dangerous book in seventeenth-century Europe — Spinoza\'s systematic demolition of revealed religion\'s political authority and his argument that freedom of thought is the indispensable condition of a stable, peaceful republic.',

    summary: 'Published anonymously in Amsterdam in 1670 — and immediately recognized as Spinoza\'s and condemned throughout Europe — the Theological-Political Treatise is the most dangerous book of the seventeenth century: a systematic attack, conducted with philological rigor and philosophical precision, on the intellectual foundations of clerical authority over political life. Spinoza\'s stated aim is to show that philosophy and theology are entirely separate domains, and that the attempt by religious authorities to control philosophical inquiry destroys both religion (reducing it to superstition and dogma) and political life (replacing the rule of law with the arbitrary power of priests).\n\nThe first fifteen chapters constitute the first systematic biblical criticism in the Western tradition. Spinoza analyzes the books of the Old Testament with the same historical-philological tools used to analyze any ancient text: asking who actually wrote them, when, to whom, with what political purposes. His conclusion is radical. Moses did not write the Pentateuch — the evidence of vocabulary, geography, and narrative anachronism demonstrates that it was compiled by Ezra long after Moses\' death. The prophets were not conveyers of divine philosophical truth but imaginative individuals whose visions expressed divine accommodation to the understanding of their particular audiences. Miracles, properly understood, are not violations of natural law but events whose natural causes were unknown to the people who reported them. Scripture, read carefully, teaches one thing only: obedience and charity. It is not a source of philosophical truth about God, nature, or the mind.\n\nChapters sixteen through twenty draw the political implications. The natural right of each person extends as far as their power — an argument Spinoza borrows from Hobbes but develops in an entirely different direction. In the state of nature, might is right; people form societies to escape this condition by contracting to transfer their natural right to a sovereign. But — and here Spinoza diverges fundamentally from Hobbes — no contract can compel people to surrender the freedom of their minds. Thought is by nature free: you cannot force someone to believe anything, you can only force them to say something. Any sovereign who attempts to legislate what people must think will produce only hypocrisy and resentment. Chapter XX — on the freedom of thought and speech — is one of the great founding documents of liberal political philosophy: Spinoza argues that freedom of thought and expression is not merely permissible but indispensable to the stability of the state and the preservation of piety. The attempt to suppress free inquiry, he argues, is always self-defeating: it drives thought underground, creates martyrs, and breeds the very sedition it claims to prevent.',

    themes: ['Biblical Criticism', 'Separation of Church and State', 'Freedom of Thought', 'Natural Right', 'Democracy', 'Scripture and Reason', 'Prophecy', 'Miracles', 'Religion and Superstition', 'Sovereignty'],

    keyCharacters: [
        { name: 'Moses', role: 'Subject of the most consequential chapter of biblical criticism — Spinoza demonstrates that Moses almost certainly did not write the Pentateuch and was a political legislator rather than a divine philosopher' },
        { name: 'The Prophets', role: 'Reinterpreted as imaginatively gifted individuals whose visions of God were adapted to their audiences\' understanding rather than sources of philosophical truth' },
        { name: 'Thomas Hobbes (implicit interlocutor)', role: 'Spinoza shares Hobbes\' naturalistic account of the state of nature and the social contract but diverges sharply on the scope of sovereign power and the inalienability of freedom of thought' }
    ],

    concepts: [
        'Biblical criticism — the application of historical-philological analysis to Scripture as an ancient human document; Spinoza\'s method anticipates the entire Higher Criticism tradition of the 18th and 19th centuries',
        'Separation of faith and reason — theology concerns obedience and salvation; philosophy concerns truth; the two domains must be kept strictly separate or each corrupts the other',
        'Natural right as power — each person\'s natural right extends as far as their power; the social contract transfers this right to a sovereign but cannot transfer the freedom of thought',
        'The inalienability of freedom of thought — no power can compel belief; thought is by nature free and any attempt to legislate it produces only hypocrisy and political instability',
        'Scripture teaches only charity — the universal message of all genuine religion is to love God and one\'s neighbour; all theological disputation beyond this is political power dressed as religion',
        'Democracy as the most natural form of government — the democratic republic is closest to the state of nature and best preserves the equality and freedom of its members'
    ],

    structure: 'Twenty chapters in two broad movements:\n\nChapters I-XV (Theological): The nature of prophecy — prophets had vivid imaginations, not superior intellects. Analysis of the Mosaic law as political legislation for a particular people. Authorship of the Old Testament books. The nature of miracles. The concept of the chosen people as political rather than metaphysical. Faith vs. philosophy.\n\nChapters XVI-XX (Political): Natural right and the social contract. Sovereignty and its limits. The Hebrew commonwealth as a historical example of theocracy — and its failure. The rights of the sovereign in religious matters. Freedom of thought and speech as indispensable to the republic.',

    quote: 'The purpose of the state is, in reality, freedom. — Theological-Political Treatise, Chapter XX',

    additionalQuotes: [
        { text: 'Scripture does not aim to teach science, and makes no claim to do so. Its purpose is solely to teach obedience.', citation: 'Theological-Political Treatise, Chapter II' },
        { text: 'A miracle is nothing other than an event whose natural cause we do not know.', citation: 'Theological-Political Treatise, Chapter VI' },
        { text: 'Men would never be superstitious if they could govern all their circumstances by set rules, or if they were always favoured by fortune: but being frequently driven into straits where rules are useless, and being often kept fluctuating pitiably between hope and fear by the uncertainty of fortune\'s greedily coveted favours, they are consequently, for the most part, very prone to credulity.', citation: 'Theological-Political Treatise, Preface' }
    ],

    commentary: [
        {
            philosopher: 'John Locke',
            text: 'Locke\'s Letter Concerning Toleration (1689) is the document that most directly follows the political argument of Chapters XVI-XX of the Theological-Political Treatise, though Locke never acknowledged reading Spinoza and the relationship is debated. Both argue that coercion cannot produce genuine religious belief and that any attempt to enforce religious conformity is therefore self-defeating and politically counterproductive. Both draw a sharp line between the domain of the magistrate (external conduct, civil peace) and the domain of conscience (internal belief). But their grounds differ significantly: Locke\'s toleration argument rests on the limits of legitimate political authority and on the individual\'s responsibility for their own salvation; Spinoza\'s rests on the natural freedom of thought and on a utilitarian argument for social stability. Locke\'s toleration, moreover, notoriously excluded Catholics and atheists — exactly the exclusions Spinoza\'s more radical argument would not permit.'
        },
        {
            philosopher: 'Pierre Bayle',
            text: 'Bayle\'s Dictionnaire historique et critique (1697) — the intellectual handbook of the early Enlightenment — engaged extensively with Spinoza, identifying him as the most dangerous thinker in Europe while simultaneously using Spinozist arguments for his own skeptical and tolerationist ends. Bayle\'s article on Spinoza is the most widely read early account of Spinoza\'s philosophy and shaped how the Enlightenment received him: as a virtuous atheist, a man of exemplary personal integrity whose philosophy was nevertheless a coherent and threatening denial of everything Christianity rested on. Bayle\'s paradox — that Spinoza was the most consistent and coherent of all the philosophers, and also the one whose conclusions were the most theologically destructive — set the terms of the Spinoza debates that dominated eighteenth-century Europe.'
        },
        {
            philosopher: 'Jonathan Israel',
            text: 'Israel\'s Radical Enlightenment: Philosophy and the Making of Modernity 1650-1750 (2001) placed the Theological-Political Treatise at the center of European intellectual history, arguing that Spinoza was the single most important source of what Israel calls the "Radical Enlightenment" — the tradition of democratic republicanism, freedom of thought, religious toleration, and naturalistic philosophy that was explicitly opposed to the "Moderate Enlightenment" of Locke, Newton, and Voltaire, who retained God, revelation, and social hierarchy. Israel argued that the standard historiography of the Enlightenment, focused on Locke and Voltaire, had systematically underestimated the influence of Spinozism, which propagated through underground channels, clandestine manuscripts, and forbidden books to shape the most radical currents of the French Revolution and modern democratic theory.'
        },
        {
            philosopher: 'Leo Strauss',
            text: 'Strauss\'s Spinoza\'s Critique of Religion (1930) — his first major work — argued that the Theological-Political Treatise was the founding document of the modern critique of religion and that its argument, carried to its logical conclusion, undermines not only revealed religion but also the natural religion and rational theology that the moderate Enlightenment had hoped to preserve in religion\'s place. Strauss was both attracted to and troubled by Spinoza\'s radicalism: he admired the philosophical rigour and the courage of the argument, but argued that Spinoza had failed to refute the biblical tradition on its own terms and had instead simply declared the primacy of reason by fiat. Strauss\'s lifelong concern with the quarrel between Athens and Jerusalem — between philosophy and revelation — was shaped by his early engagement with the Theological-Political Treatise as the most honest philosophical challenge to the claims of revelation ever mounted.'
        }
    ],

    modernRelevance: 'The Theological-Political Treatise is the founding document of biblical scholarship as an academic discipline, of the liberal doctrine of separation of church and state, and of the philosophical case for freedom of thought and expression that underlies all subsequent liberal political theory. Every argument for academic freedom, for freedom of the press, for the right of citizens to hold and express heterodox views traces back, through Locke, Mill, and Jefferson, to the argument Spinoza made in Chapter XX. The historical-critical method of biblical analysis that Spinoza pioneered in Chapters I-XV became, in the nineteenth century, the standard academic approach to Scripture through Wellhausen, Strauss, and Schweitzer. In an age of renewed conflict between religious authority and secular political life, the Theological-Political Treatise speaks as directly as it did in 1670.',

    context: 'Published anonymously in Amsterdam in 1670, with a false publisher\'s name and the false imprint "Hamburg." The anonymity fooled almost no one: within months the book was identified as Spinoza\'s throughout Europe. It was condemned by the Dutch Reformed Synod, by the Catholic Index, and by virtually every major religious authority in Europe. The Amsterdam authorities banned it in 1674. Spinoza had prepared the manuscript after the murder of the brothers De Witt — the republican statesmen who had protected intellectual freedom in the Netherlands — by a royalist mob in 1672, an event that shattered Spinoza and convinced him of the fragility of the liberal political order he was arguing for. He is said to have prepared a placard reading "Ultimi Barbarorum" (the lowest of barbarians) to pin at the site of the murders, and was physically restrained by his landlord from going out into the street with it.',

    relatedWorks: ['spinoza-ethics', 'political-treatise', 'spinoza-correspondence']
}

);
"""

# ─────────────────────────────────────────────────────────────────────────────
# DATA-12c  —  Political Treatise + Treatise on the Emendation of the Intellect
# ─────────────────────────────────────────────────────────────────────────────
data_12c = r"""/* ================================================================
   DATA PART 12c — Political Treatise + Treatise on the Emendation of the Intellect
   ================================================================ */

window.WORKS.push(

/* ──────────────────────────────────────
   1. POLITICAL TREATISE
────────────────────────────────────── */
{
    id: 'political-treatise',
    title: 'Political Treatise',
    greekTitle: 'Tractatus Politicus',
    philosopher: 'spinoza',
    category: 'political',
    categoryLabel: 'Political Philosophy',
    date: '1677 AD (posthumous, unfinished)',
    dateSort: 1676,
    emoji: '🏛',
    cardSize: 'normal',
    readingDifficulty: 'Advanced',
    estimatedWordCount: 45000,

    shortDesc: 'Spinoza\'s mature and unfinished political philosophy — a naturalistic analysis of monarchies, aristocracies, and democracies, applying the geometric method of the Ethics to the study of political institutions and breaking sharply from Hobbes by treating human nature not as an obstacle to politics but as its raw material.',

    summary: 'Left unfinished at Spinoza\'s death in February 1677 — breaking off mid-sentence in the chapter on democracy at the point where he was about to discuss whether women should be admitted to government — the Political Treatise is a more rigorous and less polemical political philosophy than the Theological-Political Treatise. Where the earlier work had a specific polemical target (clerical political power), the Political Treatise aims at a general science of politics modeled on the method of the Ethics.\n\nChapter I establishes the naturalistic starting point that marks Spinoza\'s sharpest departure from the entire natural law tradition including Hobbes. Philosophers have consistently treated human vices — pride, ambition, envy, anger — as defects to be transcended rather than as natural facts to be understood. Spinoza proposes instead to analyze human beings as they actually are, not as moralists wish them to be, and to design political institutions that work with rather than against the actual passions of human beings. Politics is not the imposition of reason on irrational nature but the channeling of natural passions toward stable social order.\n\nThe middle chapters offer detailed constitutional analyses of monarchy, aristocracy, and democracy. For each form of government, Spinoza asks: what institutional arrangements are required to make this form stable? What checks on power prevent it from degenerating into tyranny or oligarchy? His constitutional thinking is remarkably modern: he advocates the division of powers, the rotation of offices, large deliberative councils, and institutional constraints on executive power — not because these are morally superior but because they are institutionally stable, distributing the natural desire for power across multiple actors and preventing its dangerous concentration.\n\nThe democracy chapter — though incomplete — indicates that Spinoza regarded democratic government as the most natural and most stable form, closest to the condition of freedom from which the social contract emerges. The break-off point, where Spinoza was about to address women\'s exclusion from political participation, has been the subject of much feminist philosophical attention.',

    themes: ['Political Naturalism', 'Constitutional Analysis', 'Monarchy', 'Aristocracy', 'Democracy', 'Institutional Design', 'Power and Stability', 'Human Nature and Politics', 'The Social Contract'],

    keyCharacters: [
        { name: 'The Statesman (Spinoza\'s ideal)', role: 'Not the philosopher-king but the institutional designer who channels the actual passions of actual people toward stable social order' }
    ],

    concepts: [
        'Political naturalism — human vices are natural facts, not defects; political institutions must be designed for people as they are, not as moralists wish them to be',
        'Institutional stability over moral improvement — the goal of political design is not to make people virtuous but to make power stable by distributing it and checking its concentration',
        'Natural right as collective power — in society, the natural right of the collective extends as far as the power of the collective; sovereignty is real power, not legal fiction',
        'Constitutional checks — division of powers, rotation of offices, large councils, transparent deliberation: institutional mechanisms that prevent the dangerous concentration of power'
    ],

    structure: 'Eleven chapters, the last unfinished:\n\nChapters I-II: Method. Naturalistic starting point. Human nature and the passions as political raw material.\n\nChapters III-VII: Monarchy — its natural basis, its institutional requirements for stability, the dangers of absolute monarchy.\n\nChapters VIII-X: Aristocracy — its structure, the patrician class, the institutional checks required.\n\nChapter XI: Democracy — incomplete; breaks off discussing whether women should participate.',

    quote: 'I have laboured carefully, not to mock, lament, or execrate, but to understand human actions. — Political Treatise, Chapter I',

    additionalQuotes: [
        { text: 'The statesman who seeks to do everything by law will foment crime rather than lessen it.', citation: 'Political Treatise, Chapter II' },
        { text: 'He who seeks to regulate everything by law will irritate vices rather than correct them.', citation: 'Political Treatise, Chapter X' }
    ],

    commentary: [
        {
            philosopher: 'Jean-Jacques Rousseau',
            text: 'Rousseau\'s Social Contract (1762) works in a space the Political Treatise defines but moves in an opposite direction. Spinoza treats the passions as permanent political raw material to be institutionally managed; Rousseau treats the social contract as an occasion for the moral transformation of natural man into citizen, replacing the voice of passion with the voice of the general will. Where Spinoza is a political realist who designs for people as they are, Rousseau is a political idealist who designs for people as they might become. The contemporary debate between "realist" and "idealist" political philosophy — between institutional design and moral transformation — maps precisely onto the Spinoza-Rousseau divide.'
        },
        {
            philosopher: 'Étienne Balibar',
            text: 'Balibar\'s Spinoza and Politics (1985) is the most important twentieth-century Marxist reading of the Political Treatise. Balibar argued that Spinoza\'s political naturalism — his insistence that politics must deal with human beings as they actually are rather than as they ought to be — constitutes a materialist theory of politics that anticipates Marx\'s critique of idealism. More specifically, Balibar showed that Spinoza\'s concept of the multitude (multitudo) — the mass of people whose collective power is the real basis of any political order — provides a political-ontological category that is neither Hobbes\'s atomistic individuals nor Rousseau\'s ideal citizens, but something closer to Marx\'s "masses" as collective historical agents. The unfinished democracy chapter becomes, on this reading, the site where Spinoza was about to develop the most radical implications of his political naturalism.'
        }
    ],

    modernRelevance: 'The Political Treatise\'s insistence on designing institutions for human beings as they actually are, rather than as moral idealists hope them to be, is the founding insight of modern political science and institutional design theory. James Madison\'s argument in Federalist No. 51 — that ambition must be made to counteract ambition, that institutional structure rather than moral virtue is the reliable foundation of stable government — is the American constitutional expression of precisely this Spinozist principle. Contemporary political theorists who study constitutional design, democratic backsliding, and the institutional conditions for preserving political freedom work within a framework Spinoza defined.',

    context: 'Written in the last years of Spinoza\'s life, probably between 1675 and his death in February 1677. Published posthumously with the Ethics and the Hebrew Grammar in the Opera Posthuma (1677). The manuscript breaks off mid-sentence in Chapter XI at the discussion of women\'s political participation — a break that has generated extensive scholarly debate about what Spinoza would have argued. The Political Treatise is a more mature and technically precise work than the Theological-Political Treatise, reflecting Spinoza\'s full philosophical development.',

    relatedWorks: ['theological-political-treatise', 'spinoza-ethics', 'spinoza-correspondence']
},

/* ──────────────────────────────────────
   2. TREATISE ON THE EMENDATION OF THE INTELLECT
────────────────────────────────────── */
{
    id: 'treatise-on-emendation',
    title: 'Treatise on the Emendation of the Intellect',
    greekTitle: 'Tractatus de Intellectus Emendatione',
    philosopher: 'spinoza',
    category: 'epistemology',
    categoryLabel: 'Epistemology & Method',
    date: 'c.1661 AD (posthumous)',
    dateSort: 1661,
    emoji: '🔦',
    cardSize: 'normal',
    readingDifficulty: 'Advanced',
    estimatedWordCount: 25000,

    shortDesc: 'Spinoza\'s unfinished methodological prolegomenon — the most personal of all his works, opening with a confessional account of the decision to abandon wealth, pleasure, and honour for the pursuit of the one good that is truly satisfying and can be communicated to others without diminishment.',

    summary: 'The Treatise on the Emendation of the Intellect is the only place in the Spinoza corpus where the philosopher speaks in something like a personal voice. It opens with a passage of unusual literary and emotional intensity: Spinoza describes his recognition that the goods ordinarily pursued by human beings — wealth, pleasure, and honour — are uncertain, transient, and ultimately unsatisfying. A different good exists: one that is not exhausted by being shared, not diminished by being communicated, not subject to the accidents of fortune. This good is the knowledge of the union between the mind and the whole of nature. Having identified this as the true good, Spinoza commits to its pursuit — and commits also to bringing other human beings along, because the true good is most fully achieved in a community of those who pursue it together.\n\nThis prologue is followed by the methodological inquiry proper: what are the different modes of perceiving things, and which of them leads to adequate knowledge? Spinoza distinguishes four modes: knowledge from hearsay or signs; knowledge from vague experience (empirical generalisation without understanding); knowledge from inference or deduction; and the fourth mode — knowledge through the essence of the thing itself, intuitive and adequate. This last mode is what Spinoza will call, in the Ethics, the third kind of knowledge or scientia intuitiva. The treatise is unfinished — it breaks off in the middle of a discussion of method — and was never published by Spinoza. It is best understood as an early draft of the epistemological foundations that the Ethics would develop more rigorously within the geometric framework.',

    themes: ['The True Good', 'The Emendation of the Intellect', 'Modes of Perception', 'Adequate Knowledge', 'Method', 'The Good Life', 'Community of Inquiry', 'Intuitive Knowledge'],

    keyCharacters: [
        { name: 'Spinoza (personal narrator)', role: 'The only text in which Spinoza speaks confessionally — describing his own decision to abandon ordinary goods in pursuit of the one good that is truly satisfying and imperishable' }
    ],

    concepts: [
        'The four modes of perception — hearsay, vague experience, inference or deduction, and knowledge through the essence of the thing itself; only the fourth yields adequate knowledge',
        'The true good — the knowledge of the union between the mind and the whole of nature; it is not diminished by being communicated, making it uniquely suited as the foundation of community',
        'Emendation of the intellect — the purification of the mind from confused and inadequate ideas; the methodological precondition for arriving at genuine philosophical understanding',
        'Scientia intuitiva (anticipated) — the direct, non-inferential grasp of the essence of things that will become the third kind of knowledge in the Ethics'
    ],

    structure: 'Two movements (unfinished):\n\nPrologue (§§1-17): The abandonment of ordinary goods. The identification of the true good. The commitment to philosophy and to community.\n\nMethodological Inquiry (§§18-110): The four modes of perception. The nature of truth. The conditions for adequate method. The reflexive problem — how does one use the intellect to emend the intellect?',

    quote: 'After experience had taught me that all the usual surroundings of social life are vain and futile; seeing that none of the objects of my fears contained in themselves anything either good or bad, except in so far as the mind is affected by them, I finally resolved to inquire whether there might be some real good having power to communicate itself, which would affect the mind singly, to the exclusion of all else. — Treatise on the Emendation of the Intellect, §1',

    additionalQuotes: [
        { text: 'The greatest good is the knowledge of the union which the mind has with the whole of Nature.', citation: 'Treatise on the Emendation of the Intellect, §13' }
    ],

    commentary: [
        {
            philosopher: 'G.W. Leibniz',
            text: 'Leibniz visited Spinoza in The Hague in November 1676 and had extensive philosophical conversations with him, gaining access to the unpublished manuscripts including an early version of what would become the Ethics. Leibniz copied out portions of the Treatise on the Emendation of the Intellect, which he found both fascinating and threatening. The four modes of perception in the Treatise map onto Leibniz\'s own epistemological distinctions between confused, clear, distinct, and adequate knowledge in his "Meditations on Knowledge, Truth, and Ideas" (1684). But Leibniz was careful, throughout his career, to distance himself publicly from Spinoza while privately engaging with his arguments at depth — a pattern of simultaneous intellectual debt and denial that scholars have documented extensively.'
        },
        {
            philosopher: 'Simone de Beauvoir',
            text: 'De Beauvoir\'s reading of the Treatise in The Ethics of Ambiguity (1947) focused on the opening prologue as a rare philosophical statement of what it means to choose a way of life rather than merely accept one. Spinoza\'s description of his decision — recognizing that ordinary goods are uncertain and communicating the decision to pursue a different kind of good — is, for de Beauvoir, one of the few examples of authentic choice in the philosophical tradition: a genuine taking-up of one\'s own freedom rather than a flight into bad faith. She noted, however, that Spinoza\'s account of the true good as knowledge rather than interpersonal engagement remains marked by the intellectualism that existentialist ethics resists: the primary ethical relationship for de Beauvoir is not with ideas but with other free human beings whose freedom must be affirmed.'
        }
    ],

    modernRelevance: 'The opening prologue of the Treatise has been described as the most honest statement of the philosophical vocation ever written: an account of what it actually feels like to decide to give one\'s life to the pursuit of understanding rather than wealth, status, or pleasure, and of why this decision makes sense not just personally but socially — because genuine understanding is the one good that grows rather than diminishes when shared. This argument about the non-rivalrous nature of intellectual goods anticipates the modern economics of information goods and open-source knowledge, where sharing, rather than hoarding, maximizes everyone\'s benefit.',

    context: 'Almost certainly written in the early 1660s, around the time Spinoza was beginning the Ethics. Left unfinished and unpublished; included in the Opera Posthuma of 1677. It is the work most often recommended as the first entry point into Spinoza, despite — or because of — its unfinished, exploratory character and its unusually personal opening. The methodological questions it raises about how the intellect can emend itself — using a faculty to improve that same faculty — anticipate Hegel\'s problem of how to begin philosophy without presuppositions.',

    relatedWorks: ['spinoza-ethics', 'theological-political-treatise', 'spinoza-short-treatise']
}

);
"""

# ─────────────────────────────────────────────────────────────────────────────
# DATA-12d  —  Short Treatise + Descartes' Principles + Metaphysical Thoughts
# ─────────────────────────────────────────────────────────────────────────────
data_12d = r"""/* ================================================================
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
"""

# ─────────────────────────────────────────────────────────────────────────────
# DATA-12e  —  Correspondence (Letters)
# ─────────────────────────────────────────────────────────────────────────────
data_12e = r"""/* ================================================================
   DATA PART 12e — Correspondence (Letters)
   ================================================================ */

window.WORKS.push(

{
    id: 'spinoza-correspondence',
    title: 'Correspondence',
    greekTitle: 'Epistolae',
    philosopher: 'spinoza',
    category: 'metaphysics',
    categoryLabel: 'Letters',
    date: '1661–1676 AD',
    dateSort: 1664,
    emoji: '✉️',
    cardSize: 'normal',
    readingDifficulty: 'Advanced',
    estimatedWordCount: 100000,

    shortDesc: 'Eighty-eight surviving letters — the workshop of the Ethics, where Spinoza argues with Oldenburg, Blyenbergh, Leibniz, and Tschirnhaus in real time, defends his most dangerous positions with quiet courage, and reveals, in the face of an anguished correspondent\'s challenge, the full moral seriousness behind the geometric method.',

    summary: 'The eighty-eight letters that survive in the Spinoza correspondence — out of a much larger collection that was edited and partially destroyed before publication — constitute the most revealing documentary record of his thought. Where the Ethics presents conclusions in axiomatic form, the letters show the process of thinking: Spinoza defending, refining, and sometimes modifying his positions under the pressure of genuine philosophical challenge.\n\nThe correspondence with Henry Oldenburg, the founding secretary of the Royal Society in London, is the most extensive and spans fifteen years (1661-1676). Oldenburg was genuinely fascinated by Spinoza\'s mathematical physics and natural philosophy, and the early letters are a remarkable record of the intersection of Spinoza\'s philosophy with the new experimental science. As Oldenburg grew more conservative under pressure from the Royal Society\'s Anglican establishment, however, his letters become increasingly anxious about Spinoza\'s religious heterodoxy, and the later correspondence (especially after the Theological-Political Treatise) involves Spinoza patiently explaining that his view of God is not atheism.\n\nThe correspondence with Willem van Blyenbergh — a Calvinist grain merchant who had read the early parts of the Ethics in manuscript — is philosophically the most intense of all the exchanges. Blyenbergh was genuinely distressed by Spinoza\'s determinism: if everything follows necessarily from God\'s nature, including human wickedness, then God is the cause of sin, and the entire moral-theological framework of reward, punishment, and salvation collapses. Spinoza\'s replies are models of patient clarity: evil is not a positive thing but a lack of perfection relative to a particular standard; God does not will wickedness in any morally significant sense; the concepts of sin, guilt, and punishment belong to the human legal framework, not to the order of nature. The exchange has no resolution — Blyenbergh\'s theology and Spinoza\'s naturalism are genuinely incompatible — and its very irresoluteness illuminates the depth of what separates them.\n\nThe letter to Albert Burgh (Letter 76) — written to a former student who had converted to Catholicism and was urging Spinoza to do the same, appealing to the authority of the Church and the comfort of dogma — is perhaps the most personally revealing document in the corpus. Spinoza\'s reply is both gentle and merciless: he refuses, politely but without equivocation, to exchange the difficult freedom of philosophical inquiry for the comfortable security of institutional faith. "I do not presume that I have found the best philosophy," he writes, "but I know that I understand the true one." The letter reveals the personal dimension of philosophical commitment that the geometric method of the Ethics deliberately conceals.\n\nGottfried Leibniz visited Spinoza in The Hague in November 1676 and had extended philosophical conversations with him. The letters exchanged before and after this visit document Leibniz\'s complex relationship with Spinoza: deep intellectual engagement masked by public disavowal. Leibniz took careful notes of their conversations and borrowed from Spinoza\'s unpublished manuscripts — a debt he spent much of his subsequent career concealing.',

    themes: ['Determinism and Evil', 'God and Nature Defended', 'Biblical Criticism in Practice', 'Philosophical Friendship', 'Faith and Reason', 'Freedom of Inquiry', 'The New Science', 'Personal Philosophy'],

    keyCharacters: [
        { name: 'Henry Oldenburg', role: 'Founding secretary of the Royal Society; Spinoza\'s most sustained correspondent, initially enthusiastic about his natural philosophy, later anxious about his religious heterodoxy' },
        { name: 'Willem van Blyenbergh', role: 'Calvinist merchant whose anguished challenge to Spinoza\'s determinism — if God causes everything, does God cause sin? — produces some of the most humanly revealing exchanges in the correspondence' },
        { name: 'Gottfried Wilhelm Leibniz', role: 'Who visited Spinoza in 1676, read his manuscripts, engaged deeply with his philosophy, and then spent decades publicly distancing himself from the thinker he had most carefully studied' },
        { name: 'Albert Burgh', role: 'Former student who converted to Catholicism and urged Spinoza to do the same; the occasion of Spinoza\'s most personally revealing letter' }
    ],

    concepts: [
        'Evil as privation — evil is not a positive entity but a lack of perfection relative to a particular standard; God, who is all-positive, does not cause evil in any morally significant sense',
        'The inalienability of philosophical inquiry — Spinoza\'s refusal, articulated most clearly in Letter 76 to Burgh, to exchange the difficult freedom of philosophical reasoning for institutional religious security',
        'The intersection of Spinozism and the new science — the early Oldenburg letters document the relationship between Spinoza\'s philosophy of nature and the experimental programme of the early Royal Society',
        'Determinism as liberation — the correspondence consistently argues that understanding necessity is not oppressive but liberating; the free person is the one who understands, not the one who imagines themselves exempt from causation'
    ],

    structure: 'Eighty-eight letters organized in the Adam-Gebhardt edition. Key exchanges: Spinoza-Oldenburg (Letters 1-15, 29-48, 62-77); Spinoza-Blyenbergh (Letters 18-24); Spinoza-Tschirnhaus (Letters 57-83); Spinoza-Meyer; Spinoza-Leibniz (Letter 45, with notes from the 1676 visit); Spinoza-Burgh (Letter 76).',

    quote: 'I do not presume that I have found the best philosophy, but I know that I understand the true one. — Letter 76, to Albert Burgh (1675)',

    additionalQuotes: [
        { text: 'Men are deceived in thinking themselves free, a belief that consists only in this, that they are conscious of their actions and ignorant of the causes that determine them.', citation: 'Letter 58, to G.H. Schuller' },
        { text: 'I do not know why matter should be unworthy of the divine nature. No substance can be conceived that is more excellent than infinite Being.', citation: 'Letter 73, to Oldenburg' },
        { text: 'The better part of our mind is in agreement with the order of the whole of nature.', citation: 'Letter 17, to Pieter Balling' }
    ],

    commentary: [
        {
            philosopher: 'Leibniz',
            text: 'Leibniz\'s engagement with the Spinoza correspondence, both before and after the 1676 visit, is the most philosophically consequential relationship in the history of early modern philosophy — and one of its most tortured. Leibniz took extensive notes during his conversations with Spinoza, copied out portions of the unpublished Ethics, and engaged with Spinoza\'s arguments at technical depth in his private papers. In his public writings, however, he consistently identified Spinozism as the most dangerous philosophical error — the identification of God with nature, which Leibniz saw as the philosophical equivalent of atheism. Contemporary scholars, particularly Matthew Stewart and Mogens Laerke, have documented this double relationship in detail, arguing that the monadology itself is best understood as Leibniz\'s systematic attempt to provide an alternative to Spinozism that would preserve the infinity and power of God while restoring genuine substance and freedom to finite things.'
        },
        {
            philosopher: 'Bertrand Russell',
            text: 'Russell\'s assessment of Spinoza in A History of Western Philosophy (1945) is one of the most frequently quoted philosophical tributes in the modern literature: Spinoza is "the noblest and most lovable of the great philosophers. Intellectually, some others have surpassed him, but ethically he is supreme." Russell was particularly struck by the letters — by the combination of intellectual courage and personal gentleness they reveal. The correspondence shows Spinoza engaging with the most hostile and anguished challenges to his system — Blyenbergh\'s moral horror, Burgh\'s evangelical urgency — with a patience and charitable clarity that Russell found philosophically exemplary. Russell also noted that the letters reveal a philosopher who, while never wavering in his conclusions, genuinely tried to understand the human concerns that made those conclusions disturbing to his correspondents.'
        },
        {
            philosopher: 'Rebecca Goldstein',
            text: 'Goldstein\'s Betraying Spinoza: The Renegade Jew Who Gave Us Modernity (2006) used the correspondence — especially the early Amsterdam letters and the exchange with Burgh — to construct a biographical and philosophical account of Spinoza as a thinker formed by and responding to his experience of excommunication from the Amsterdam Jewish community. Goldstein argued that the central philosophical project of the Ethics — to show that the universe is rational and that human flourishing lies in understanding this rationality, not in institutional belonging or tribal identity — is shaped by the biographical experience of being expelled from every community: Jewish, Christian, and orthodox philosophical. The letters reveal, beneath the geometric armour of the Ethics, a thinker whose serenity was hard-won and who understood, from personal experience, the full cost of intellectual freedom.'
        }
    ],

    modernRelevance: 'The Spinoza correspondence is one of the great records of a philosopher living out their philosophy under conditions of genuine social and intellectual pressure. Spinoza was excommunicated, his books were banned, his correspondents were sometimes frightened of association with him, and he lived in conditions of material simplicity and social marginality throughout his adult life. The letters show that the Ethics\' account of freedom as understanding rather than external validation was not merely a theoretical position but a practical commitment Spinoza maintained consistently. For contemporary readers navigating the tension between intellectual integrity and social belonging, the correspondence remains urgently relevant.',

    context: 'The letters were collected and edited by Spinoza\'s friends after his death and included in the Opera Posthuma (1677). The editors suppressed some letters and altered others to protect correspondents; the complete picture of the correspondence has been progressively reconstructed by scholars using manuscripts held in various European libraries. The standard modern edition is in the Gebhardt Opera (1925). The correspondence with Oldenburg is of particular scientific-historical importance: it documents the intersection of Spinoza\'s philosophy with the founding of the Royal Society and the early institutionalisation of the new experimental science.',

    relatedWorks: ['spinoza-ethics', 'theological-political-treatise', 'political-treatise', 'treatise-on-emendation']
}

);
"""

files = {
    'data-12a.js': data_12a,
    'data-12b.js': data_12b,
    'data-12c.js': data_12c,
    'data-12d.js': data_12d,
    'data-12e.js': data_12e,
}

for filename, content in files.items():
    path = os.path.join(js_dir, filename)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    lines = content.count('\n')
    print(f'  Written {filename}  —  {lines} lines  →  {path}')

print('\nAll Spinoza files complete. Verify with:')
print('  wc -l js/data-12a.js js/data-12b.js js/data-12c.js js/data-12d.js js/data-12e.js')
