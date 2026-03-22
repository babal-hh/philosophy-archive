#!/usr/bin/env python3
"""
Schopenhauer — data-21a through data-21e (10 works)
Run from ~/Desktop/philosophy-archive/: python3 generate_schopenhauer.py
"""
import os
js = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'js')
os.makedirs(js, exist_ok=True)

files = {}

# ── data-21a: World as Will and Representation Vol. 1 ────────────────────────
files['data-21a.js'] = r"""/* DATA PART 21a — Schopenhauer: The World as Will and Representation Vol. 1 */
window.WORKS.push(
{
    id: 'world-as-will-vol1',
    title: 'The World as Will and Representation, Vol. I',
    greekTitle: 'Die Welt als Wille und Vorstellung, Band I',
    philosopher: 'schopenhauer',
    category: 'metaphysics',
    categoryLabel: 'Metaphysics & Aesthetics',
    date: '1818 AD',
    dateSort: 1818,
    emoji: '\uD83C\uDF0A',
    cardSize: 'wide',
    readingDifficulty: 'Advanced',
    estimatedWordCount: 280000,
    shortDesc: 'The masterpiece of philosophical pessimism \u2014 Schopenhauer\u2019s argument that the world is simultaneously representation (the phenomenal surface constituted by the forms of the intellect) and Will (the blind, insatiable striving that is the thing-in-itself), and that suffering is not accidental but the essence of existence.',
    summary: 'The World as Will and Representation (Die Welt als Wille und Vorstellung), Volume I, published in December 1818 by Brockhaus in Leipzig (bearing the date 1819), is the most consequential philosophical work to emerge from the post-Kantian tradition and the founding document of philosophical pessimism. Schopenhauer was thirty at its publication. The work was initially ignored; by the time Schopenhauer died in 1860, it had made him the most widely read philosopher in Germany.\n\nThe work\u2019s fundamental thesis is stated in its opening sentence: \u201cThe world is my representation.\u201d Everything that is known is known as an object for a subject; the world of experience is the world constituted by the forms of the intellect \u2014 space, time, and causality. This is Schopenhauer\u2019s appropriation of Kant: the phenomenal world is the world as representation (Vorstellung), constituted by the knowing subject\u2019s cognitive apparatus.\n\nBut unlike Kant, Schopenhauer claims to know what the thing-in-itself is. The key is the body: I know my own body not only as a representation (an object among objects in space and time) but also from within, as Will (Wille). When I raise my arm, the act of will and the bodily movement are not two events but one: the will is the inner nature of the bodily action. Generalising from this: the inner nature of every natural force, every organic process, every human desire \u2014 is Will. The Will is not the rational will of Kant\u2019s moral philosophy but a blind, unconscious, insatiable striving without purpose or goal. It is the Kantian thing-in-itself.\n\nSince Will is one (it is not in space and time, which are forms of representation), individuation is an illusion: the suffering I cause another is ultimately the suffering of the same Will that I am. Suffering is not accidental: it is the essence of existence. Every desire that is satisfied immediately generates a new desire; the cessation of desire is boredom; every pleasure is merely the temporary cessation of pain. Life oscillates between pain and boredom like a pendulum.\n\nThe work\u2019s four Books develop the system: Book 1 (the world as representation, first aspect), Book 2 (the world as will, first aspect), Book 3 (the world as representation, second aspect \u2014 the Platonic Ideas and aesthetic contemplation as temporary release from the Will), and Book 4 (the world as will, second aspect \u2014 ethics, asceticism, and the denial of the will-to-live as the only genuine liberation).\n\nBook 3 contains Schopenhauer\u2019s extraordinary philosophy of art. Aesthetic experience is a temporary escape from the tyranny of the Will: in genuine aesthetic contemplation we become the \u201cpure subject of knowing\u201d \u2014 a will-less mirror of the Platonic Idea expressed in the artwork. Tragedy is the highest literary form because it confronts us most directly with the suffering at the heart of existence. Music is the highest art form of all because it does not represent the Platonic Ideas (as the other arts do) but is a direct copy of the Will itself.',
    themes: ['the world as representation', 'the world as Will', 'the body as the key to the thing-in-itself', 'the blindness and insatiability of Will', 'the individuation principle as illusion', 'suffering as the essence of existence', 'aesthetic contemplation as escape', 'Platonic Ideas', 'music as the highest art', 'tragedy', 'the denial of the will-to-live'],
    keyCharacters: [],
    concepts: [
        'The world as representation (Vorstellung) \u2014 the phenomenal world constituted by the forms of the intellect: space, time, and causality; the world as we know it',
        'The principle of sufficient reason (Satz vom Grunde) \u2014 the law governing all representations: everything in the phenomenal world has a ground; applies in four forms (logical, physical, mathematical, motivational)',
        'The Will (Wille) as thing-in-itself \u2014 the inner nature of all phenomena; known directly through the body; blind, unconscious, insatiable striving without purpose or goal',
        'The body as the key to metaphysics \u2014 I know my own body both as representation (object in space) and as Will (from within); the body is the Will made visible',
        'The principium individuationis \u2014 space and time as the principle of individuation; individuals are the Will\u2019s multiple phenomenal expressions; individuation is ultimately illusory',
        'Suffering as essential, not accidental \u2014 the Will\u2019s insatiability means that desire always outruns its satisfaction; life oscillates between pain (unfulfilled desire) and boredom (fulfilled desire)',
        'The Platonic Ideas \u2014 the intermediate level between the Will (thing-in-itself) and individual representations; the direct objectifications of the Will; the objects of aesthetic contemplation',
        'Aesthetic contemplation as temporary liberation \u2014 in genuine aesthetic experience, the subject becomes the \u201cpure subject of knowing\u201d: will-less, timeless, freed from the service of the Will',
        'Music as a direct copy of the Will \u2014 unlike the other arts, which represent Platonic Ideas, music bypasses Ideas altogether and copies the Will itself; hence its peculiar power and universality',
        'Tragedy as the highest literary form \u2014 tragedy presents the suffering, the futility, and the ultimate resignation that is the truth of the human condition'
    ],
    structure: 'Preface to the First Edition\nPreface to the Second Edition (1844 \u2014 added in the second edition)\n\nBook 1: The World as Representation, First Aspect (\u00a7\u00a71\u201316)\n\u2014 The principle of sufficient reason; the forms of intuition; the intellect\u2019s constitution of the phenomenal world\n\nBook 2: The World as Will, First Aspect (\u00a7\u00a717\u201329)\n\u2014 The Will as thing-in-itself; the body as its phenomenon; the grades of the Will\u2019s objectification\n\nBook 3: The World as Representation, Second Aspect (\u00a7\u00a730\u201352)\n\u2014 The Platonic Ideas; aesthetic contemplation; the individual arts; music\n\nBook 4: The World as Will, Second Aspect (\u00a7\u00a753\u201371)\n\u2014 Ethics: compassion as the foundation of morality\n\u2014 Asceticism and the denial of the will-to-live\n\u2014 The relation to Indian philosophy (the V\u00e4da)\n\nAppendix: Critique of the Kantian Philosophy',
    quote: 'The world is my representation. This is a truth valid with reference to every living and knowing being, although man alone can bring it into reflective abstract consciousness.',
    additionalQuotes: [
        { text: 'All willing arises from lack, from deficiency, and thus from suffering. Fulfilment brings it to an end; yet for one wish that is fulfilled there remain at least ten that are denied. Further, desiring lasts a long time, demands and requests go on to infinity; fulfilment is short and meted out sparingly. But even the final satisfaction is only apparent; the wish fulfilled at once makes way for a new one.', citation: 'The World as Will and Representation, Vol. I, \u00a738' },
        { text: 'Life swings like a pendulum to and fro between pain and boredom, and these two are in fact its ultimate constituents.', citation: 'The World as Will and Representation, Vol. I, \u00a757' },
        { text: 'Music is by no means like the other arts, a copy of the Ideas, but a copy of the Will itself, the objectivity of which are the Ideas. For this reason the effect of music is so very much more powerful and penetrating than is that of the other arts, for these others speak only of the shadow, but music of the essence.', citation: 'The World as Will and Representation, Vol. I, \u00a752' },
        { text: 'The safest way of not being very miserable is not to expect to be very happy.', citation: 'Parerga and Paralipomena (complementary aphorism)' },
        { text: 'Talent hits a target no one else can hit; genius hits a target no one else can see.', citation: 'The World as Will and Representation, Vol. I, \u00a736 (paraphrased)' }
    ],
    commentary: [
        { philosopher: 'Friedrich Nietzsche', text: 'Nietzsche discovered The World as Will and Representation in a Leipzig secondhand bookshop in 1865 and described it as one of the most formative intellectual experiences of his life. He read it obsessively over the following weeks, recognising in it the deepest confrontation with the problem of existence he had encountered. His early work \u2014 especially The Birth of Tragedy \u2014 is saturated with Schopenhauerian themes: the Dionysian is the Will; the Apollonian is the principium individuationis; the Apollonian-Dionysian synthesis is Schopenhauer\u2019s aesthetic experience transfigured. But Nietzsche\u2019s mature philosophy is precisely the rejection of Schopenhauer: where Schopenhauer recommends the denial of the Will, Nietzsche demands its affirmation. The will to power is the will-to-live turned inside out.' },
        { philosopher: 'Richard Wagner', text: 'Wagner discovered The World as Will and Representation in 1854 and described the encounter as a revolution in his intellectual life. The Schopenhauerian themes of suffering, compassion, renunciation, and the redemptive power of music pervade the Ring cycle, Tristan und Isolde, and Parsifal. Tristan in particular is the most sustained musical embodiment of Schopenhauerian philosophy: the longing of Tristan and Isolde is the Will\u2019s insatiable self-torment; their death is the only possible release. The relationship between Schopenhauer and Wagner is one of the most consequential in the history of philosophy and music.' },
        { philosopher: 'Bryan Magee', text: 'Magee\u2019s The Philosophy of Schopenhauer (1983; revised 1997) is the most comprehensive and most sympathetic study in English. Magee argues that Schopenhauer\u2019s central insight \u2014 that the ultimate nature of reality is something more like what we experience as will or drive than like what we experience as matter or thought \u2014 anticipates both Freudian depth psychology and Darwinian evolutionary biology, and remains philosophically live in a way that Hegel\u2019s system does not.' },
        { philosopher: 'Thomas Mann', text: 'Mann\u2019s essay \u201cSchopenhauer\u201d (1938) is one of the most beautiful philosophical appreciations of any philosopher by a novelist. Mann argues that Schopenhauer is the philosopher of German Romanticism and of the modern European sense of existence as suffering \u2014 that The World as Will and Representation is the philosophical expression of the same world-feeling that produced Tristan, the late Beethoven quartets, and Mann\u2019s own Buddenbrooks. Schopenhauer\u2019s pessimism is not a theoretical position but an existential recognition.' },
        { philosopher: 'Christopher Janaway', text: 'Janaway\u2019s Self and World in Schopenhauer\u2019s Philosophy (1989) and Schopenhauer: A Very Short Introduction (1994; 2nd ed. 2002) provide the most philosophically rigorous assessments of Schopenhauer\u2019s arguments. Janaway argues that Schopenhauer\u2019s claim to know the thing-in-itself through the body is his central philosophical achievement and his central philosophical failure: the inference from \u201cmy will is the inner nature of my bodily actions\u201d to \u201cWill is the inner nature of all natural phenomena\u201d is an illegitimate analogical extension.' }
    ],
    modernRelevance: 'The World as Will and Representation is the philosophical origin of psychoanalysis, existentialism, and philosophical pessimism. Freud acknowledged Schopenhauer as the philosopher who had anticipated the unconscious, the primacy of the drives, and the mechanisms of repression and sublimation. The concept of the Will as a blind, purposeless striving that underlies consciousness anticipates the Freudian id. Nietzsche\u2019s will to power, Wagner\u2019s music dramas, Mann\u2019s fiction, Beckett\u2019s theatre, and contemporary antinatalist philosophy (Benatar, Cioran) are all developments of Schopenhauerian themes. The philosophy of art in Book 3 remains one of the most original in the tradition: the account of aesthetic experience as temporary liberation from the Will, and the analysis of music as a direct copy of the Will, have influenced composers, critics, and philosophers of music from Wagner to Adorno.',
    context: 'Published in December 1818 (bearing the date 1819) by Brockhaus in Leipzig in an edition of 800 copies. Schopenhauer was thirty and had just completed the work after years of intensive preparation. The initial reception was catastrophic: the edition sold so poorly that Brockhaus eventually used the unsold copies as wastepaper. Schopenhauer\u2019s attempt to lecture at Berlin concurrently with Hegel (scheduling his lectures at the same hours as Hegel\u2019s) was equally disastrous: the students attended Hegel, not Schopenhauer. A second edition \u2014 substantially expanded with a supplementary volume of essays \u2014 appeared in 1844. The third edition (1859), shortly before Schopenhauer\u2019s death, finally sold well. Schopenhauer\u2019s reputation grew dramatically in the 1850s and exploded after 1860.',
    relatedWorks: ['world-as-will-vol2', 'fourfold-root', 'two-problems-ethics', 'parerga-paralipomena']
}
);
"""

# ── data-21b: World as Will Vol. 2 + Fourfold Root ───────────────────────────
files['data-21b.js'] = r"""/* DATA PART 21b — Schopenhauer: World as Will Vol. 2 + Fourfold Root */
window.WORKS.push(

{
    id: 'world-as-will-vol2',
    title: 'The World as Will and Representation, Vol. II',
    greekTitle: 'Die Welt als Wille und Vorstellung, Band II',
    philosopher: 'schopenhauer',
    category: 'metaphysics',
    categoryLabel: 'Metaphysics & Psychology',
    date: '1844 AD',
    dateSort: 1844,
    emoji: '\uD83C\uDF2A\uFE0F',
    cardSize: 'wide',
    readingDifficulty: 'Advanced',
    estimatedWordCount: 330000,
    shortDesc: 'The indispensable supplement to the masterpiece \u2014 fifty supplementary essays deepening every aspect of Volume I, containing Schopenhauer\u2019s most penetrating psychological analysis, his account of death and the indestructibility of the Will, his theory of the intellect as the Will\u2019s servant, and some of the most psychologically acute writing in the history of philosophy.',
    summary: 'The World as Will and Representation, Volume II, published together with a revised third edition of Volume I in 1844 (second edition of the complete work; first edition was Volume I alone in 1818), consists of fifty supplementary chapters that deepen, extend, and in several cases substantially revise the arguments of Volume I. Schopenhauer explicitly designed it to be read alongside Volume I, chapter by chapter, and warns that it cannot be understood in isolation.\n\nThe supplementary volume contains much of Schopenhauer\u2019s most penetrating psychological writing. Chapter 19, \u201cOn the Primacy of the Will in Self-Consciousness,\u201d is the most complete statement of his anti-intellectualist psychology: the intellect is not the self\u2019s master but its servant; consciousness is not the source of motivation but its epiphenomenon; the Will uses the intellect as a tool and keeps from it whatever would disturb its purposes. This anticipation of the Freudian unconscious is the most frequently cited aspect of the supplementary volume.\n\nChapter 41, \u201cOn Death and Its Relation to the Indestructibility of Our Inner Nature,\u201d is Schopenhauer\u2019s most extended confrontation with mortality. Since the Will is not in time (time is a form of representation), and since the Will is our true nature, death is not our end: what dies is the individual, the phenomenal expression of the Will; the Will itself is indestructible. This is not the immortality of the personal soul \u2014 Schopenhauer explicitly rejects personal immortality \u2014 but the indestructibility of the Will-in-itself. Death is the dissolution of one individual wave back into the ocean of the Will.\n\nChapter 44, \u201cThe Metaphysics of Sexual Love,\u201d is Schopenhauer\u2019s most notorious essay: a brilliant, cynical, and often misogynistic analysis of romantic love as a conspiracy of the Will-to-live for the propagation of the species. The lover\u2019s passionate conviction that his beloved is uniquely suited to him is a delusion constructed by the Will: the intellect is manipulated into believing that individual happiness is at stake when what is really at stake is the production of offspring with the optimal characteristics. Sexual love is the Will\u2019s greatest stratagem for its own perpetuation.',
    themes: ['the intellect as the Will\u2019s servant', 'the primacy of the unconscious', 'death and the indestructibility of the Will', 'the metaphysics of sexual love', 'the Will-to-live as the root of all motivation', 'suffering and compassion', 'the genius and aesthetic contemplation', 'on the vanity of existence'],
    keyCharacters: [],
    concepts: [
        'The intellect as the Will\u2019s servant \u2014 consciousness and rational thought are not the masters of motivation but its servants; the Will uses the intellect as a tool and conceals its true purposes from it',
        'The primacy of the unconscious \u2014 the Will operates largely below the threshold of consciousness; desires, motivations, and decisions arise from the Will before consciousness becomes aware of them',
        'Death and the indestructibility of the Will \u2014 death dissolves the individual but not the Will; the Will is not in time and therefore cannot die; what we fear as death is only the dissolution of one phenomenal form',
        'The metaphysics of sexual love \u2014 romantic love is the Will-to-live\u2019s supreme stratagem for its own perpetuation; the lover\u2019s conviction of the beloved\u2019s unique suitability is a delusion constructed by the species\u2019 will',
        'The vanity of existence \u2014 human life from the perspective of the Will: the individual is a brief, futile assertion of the Will that will be extinguished and replaced by others equally brief and futile',
        'On the sufferings of the world \u2014 the supplementary essays deepen the pessimism of Book 4: suffering is not exceptional but the rule; the optimism of Leibniz and the Enlightenment is a philosophical scandal'
    ],
    structure: 'Fifty supplementary chapters, corresponding to the four books of Volume I:\n\nSupplements to Book 1 (Chapters 1\u201318): Epistemology, the intellect, intuition, concepts, judgment\nSupplements to Book 2 (Chapters 19\u201328): The Will, the unconscious, the grades of nature, teleology\nSupplements to Book 3 (Chapters 29\u201339): Aesthetics, the arts, genius, music\nSupplements to Book 4 (Chapters 40\u201350): Ethics, death, sexual love, the denial of the will',
    quote: 'After your death you will be what you were before your birth. Let this thought console you; for it contains in truth the doctrine of immortality, only purged of all that is mythological.',
    additionalQuotes: [
        { text: 'The intellect is the mere tool of the will. Every act of will is followed at once by an act of knowledge, yet not conversely.', citation: 'The World as Will and Representation, Vol. II, Chapter 19' },
        { text: 'We should be surprised that a being of so much intelligence as man does not see that, in view of the brief duration of life, the uncertainty of its continuance, and its inability to satisfy us even when it lasts, it is not worth while to toil and strive as most men do, entirely governed as they are by hope.', citation: 'The World as Will and Representation, Vol. II, Chapter 28' },
        { text: 'The sexual impulse is the most vehement of craving, the desire of desires, the concentration of all our willing.', citation: 'The World as Will and Representation, Vol. II, Chapter 44' }
    ],
    commentary: [
        { philosopher: 'Sigmund Freud', text: 'Freud\u2019s repeated acknowledgments of Schopenhauer as a precursor are most specific when it comes to the material of Volume II. Chapter 19\u2019s account of the intellect as the Will\u2019s servant \u2014 consciousness as the surface of a deeper, unconscious system of drives \u2014 is the philosophical anticipation of the topographic model of the unconscious. Chapter 44\u2019s account of sexual love as a stratagem of the species-will anticipates the libido theory. Freud claimed to have avoided reading Schopenhauer until late in his career to preserve the independence of his own discoveries.' },
        { philosopher: 'Jorge Luis Borges', text: 'Borges\u2019s engagement with Schopenhauer \u2014 particularly with the doctrine of the indestructibility of the Will in Chapter 41 and the identity of all individuals as expressions of the one Will \u2014 is pervasive throughout his fiction. The Borges story that meditates most directly on Schopenhauerian themes is \u201cThe Circular Ruins\u201d (1940), in which the dreamer discovers that he himself is another\u2019s dream \u2014 an image of the Will\u2019s self-mystification.' }
    ],
    modernRelevance: 'Volume II is where Schopenhauer\u2019s most direct influence on psychoanalysis, depth psychology, and literary modernism is felt. The anti-intellectualist psychology of Chapter 19 is the philosophical source of Freud\u2019s unconscious. The Metaphysics of Sexual Love has influenced evolutionary psychology, particularly the sociobiological analysis of mate selection. The essay on death in Chapter 41 has been read alongside Buddhist philosophy, existentialism, and contemporary philosophy of personal identity.',
    context: 'Volume II was added to the second edition of the complete work, published by Brockhaus in Leipzig in 1844. The fifty supplementary chapters were written over the twenty-five years since the publication of Volume I in 1818 \u2014 a period during which Schopenhauer lectured unsuccessfully in Berlin, lived primarily in Frankfurt, and watched Hegel\u2019s philosophy dominate German intellectual life while his own was ignored. The bitterness of this experience is palpable in the supplementary essays, which contain some of the most ferocious attacks on Hegel and the post-Kantian idealists in philosophical literature.',
    relatedWorks: ['world-as-will-vol1', 'fourfold-root', 'parerga-paralipomena', 'two-problems-ethics']
},

{
    id: 'fourfold-root',
    title: 'On the Fourfold Root of the Principle of Sufficient Reason',
    greekTitle: '\u00dcber die vierfache Wurzel des Satzes vom zureichenden Grunde',
    philosopher: 'schopenhauer',
    category: 'method',
    categoryLabel: 'Epistemology & Logic',
    date: '1813 / 1847 AD',
    dateSort: 1813,
    emoji: '\uD83C\uDF33',
    cardSize: 'normal',
    readingDifficulty: 'Advanced',
    estimatedWordCount: 55000,
    shortDesc: 'The epistemological foundation of the entire system \u2014 Schopenhauer\u2019s doctoral dissertation arguing that the principle of sufficient reason has four distinct roots (logical, physical, mathematical, and motivational) and that the failure to distinguish them is the source of most philosophical confusion.',
    summary: 'On the Fourfold Root of the Principle of Sufficient Reason (\u00dcber die vierfache Wurzel des Satzes vom zureichenden Grunde) was Schopenhauer\u2019s doctoral dissertation, submitted to the University of Jena in 1813 and published the same year. Schopenhauer substantially revised and expanded it for a second edition in 1847, which is the standard text.\n\nThe principle of sufficient reason \u2014 the claim that nothing is without a reason or ground \u2014 had been treated by the rationalist tradition (Leibniz, Wolff) as a single, unified principle. Schopenhauer\u2019s central argument is that this is a fundamental confusion: the principle of sufficient reason has four distinct and irreducible roots, corresponding to four distinct classes of objects and four distinct types of necessity.\n\nThe First Root: The Principle of Sufficient Reason of Becoming (principium rationis sufficientis fiendi) \u2014 applies to representations in intuition, i.e., objects in space and time governed by causality. Every physical event has a cause. This is the principle of causality in the natural sciences.\n\nThe Second Root: The Principle of Sufficient Reason of Knowing (principium rationis sufficientis cognoscendi) \u2014 applies to abstract concepts in judgments. Every true judgment has a ground. This is the principle of logical inference.\n\nThe Third Root: The Principle of Sufficient Reason of Being (principium rationis sufficientis essendi) \u2014 applies to the formal relations of space and time. Every geometrical truth rests on spatial relations; every arithmetical truth rests on temporal relations (succession). This is the principle of mathematical necessity.\n\nThe Fourth Root: The Principle of Sufficient Reason of Acting (principium rationis sufficientis agendi) \u2014 applies to the actions of subjects. Every action is motivated; the motive is the cause as seen from within. This is the principle of motivation.\n\nSchopenhauer argues that the history of philosophy is littered with confusions arising from the failure to distinguish these four roots: the ontological argument confuses the second root (logical necessity) with the first (physical causality); rationalist metaphysics confuses the second root with the first; Kant\u2019s transcendental aesthetic misunderstands the third root.',
    themes: ['the principle of sufficient reason', 'the four roots: becoming, knowing, being, acting', 'causality', 'logical ground', 'mathematical necessity', 'motivation', 'the critique of rationalism', 'the epistemological foundation of the system'],
    keyCharacters: [],
    concepts: [
        'The principle of sufficient reason (Satz vom zureichenden Grunde) \u2014 the general principle that nothing is without a reason; has four distinct roots corresponding to four classes of objects',
        'First root: Reason of becoming \u2014 the principle of causality governing physical events in space and time; objects of empirical intuition',
        'Second root: Reason of knowing \u2014 the logical ground of true judgments; every true judgment must be grounded in another judgment or in intuition',
        'Third root: Reason of being \u2014 the mathematical necessity of spatial and temporal relations; geometrical truths rest on spatial relations; arithmetical on temporal succession',
        'Fourth root: Reason of acting \u2014 the principle of motivation; every voluntary action is caused by a motive; motivation is causality as seen from within',
        'The critique of the ontological argument \u2014 Anselm and Descartes confuse the second root (logical necessity) with the first (causal existence); existence cannot be derived from concepts alone'
    ],
    structure: 'Chapter 1: Introduction; historical survey of the principle\nChapter 2: Survey of the main distinctions of representations\nChapter 3: The first class of objects and the form of the principle that governs it (causality; becoming)\nChapter 4: The second class of objects and the form of the principle (logical ground; knowing)\nChapter 5: The third class of objects and the form of the principle (space and time; being)\nChapter 6: The fourth class of objects and the form of the principle (motivation; acting)\nChapter 7: General remarks and results',
    quote: 'The principle of sufficient reason is the foundation of all science. For science means nothing but a complete system of concepts connected by the principle of sufficient reason.',
    additionalQuotes: [
        { text: 'Nothing is without a reason why it is rather than is not.', citation: 'On the Fourfold Root, Chapter 2 (statement of the principle)' }
    ],
    commentary: [
        { philosopher: 'Immanuel Kant (as discussed by Schopenhauer)', text: 'Schopenhauer\u2019s Fourfold Root is explicitly framed as a completion and correction of Kant\u2019s epistemology. Schopenhauer accepts Kant\u2019s fundamental insight that causality is a form imposed by the intellect on experience, but argues that Kant\u2019s table of categories is arbitrary and confused. The fourfold distinction of the forms of the principle of sufficient reason is Schopenhauer\u2019s replacement for Kant\u2019s twelve categories: a leaner, more systematic account of the forms of human cognition.' },
        { philosopher: 'Hans Vaihinger', text: 'Vaihinger\u2019s The Philosophy of As-If (1911) credits the Fourfold Root with the clearest statement of the distinction between logical necessity and causal necessity in the post-Kantian tradition. Vaihinger\u2019s own theory of fictions \u2014 the idea that science and philosophy use useful fictions that are not literally true \u2014 is partly derived from Schopenhauer\u2019s account of the intellect as an instrument of the Will.' }
    ],
    modernRelevance: 'The Fourfold Root is primarily of interest to Schopenhauer scholars as the epistemological foundation of the entire system. Its distinction between different forms of necessity \u2014 causal, logical, mathematical, and motivational \u2014 anticipates the analytic tradition\u2019s careful discrimination between different modalities and different types of explanation. The fourth root (motivation) is the philosophical foundation of Schopenhauer\u2019s psychology and his account of the intellect as the Will\u2019s servant.',
    context: 'Submitted as a doctoral dissertation to the University of Jena in October 1813 and published the same year by Heinrich Ludwig Br\u00f6nner in Frankfurt. Schopenhauer was twenty-five. He presented a copy to Goethe, who was sufficiently impressed to invite Schopenhauer for a series of conversations about colour theory that led to Schopenhauer\u2019s short work On Vision and Colors (1816). The substantially revised second edition was published in 1847 by Julius Eduard Ricker in Frankfurt.',
    relatedWorks: ['world-as-will-vol1', 'world-as-will-vol2', 'on-will-in-nature', 'two-problems-ethics']
}

);
"""

# ── data-21c: On Will in Nature + Two Fundamental Problems ───────────────────
files['data-21c.js'] = r"""/* DATA PART 21c — Schopenhauer: On the Will in Nature + Two Fundamental Problems of Ethics */
window.WORKS.push(

{
    id: 'on-will-in-nature',
    title: 'On the Will in Nature',
    greekTitle: '\u00dcber den Willen in der Natur',
    philosopher: 'schopenhauer',
    category: 'metaphysics',
    categoryLabel: 'Philosophy of Nature',
    date: '1836 AD',
    dateSort: 1836,
    emoji: '\uD83C\uDF3F',
    cardSize: 'normal',
    readingDifficulty: 'Intermediate',
    estimatedWordCount: 45000,
    shortDesc: 'Schopenhauer\u2019s most scientifically engaged work \u2014 a survey of empirical sciences (physiology, comparative anatomy, plant physiology, physics, astronomy) demonstrating that their findings confirm his metaphysical thesis that Will is the thing-in-itself of all natural phenomena.',
    summary: 'On the Will in Nature (\u00dcber den Willen in der Natur), first published in 1836 by Siegmund Schmerber in Frankfurt, is Schopenhauer\u2019s attempt to demonstrate that the empirical sciences, pursued independently of his philosophy, converge on the conclusion that Will is the inner nature of all natural phenomena. Where The World as Will and Representation had established this conclusion through philosophical argument, On the Will in Nature shows that the results of physiology, comparative anatomy, plant physiology, physics, magnetism, and animal magnetism all corroborate it.\n\nThe work\u2019s structure is unusual: each chapter surveys the findings of a particular empirical science and argues that those findings are best explained by the hypothesis that the Will is the thing-in-itself. The chapter on physiology argues that vital forces \u2014 the forces that maintain life, govern organic processes, and resist dissolution \u2014 are best understood as grades of the one Will. The chapter on comparative anatomy draws on Goethe\u2019s morphology and the Naturphilosophie tradition to argue that the unity of organic form across species reflects the unity of the Will.\n\nThe most philosophically interesting chapters are those on the vegetative nervous system and on animal magnetism. The vegetative nervous system \u2014 which governs the involuntary processes of the body \u2014 is, Schopenhauer argues, the point at which the Will comes closest to surface in the body: it is the bridge between the blind, unconscious Will and the conscious, representing intellect. Animal magnetism (mesmerism) \u2014 which Schopenhauer takes seriously as a genuine phenomenon \u2014 is evidence that the Will can act across the barriers of individual bodies, confirming that individuation is illusory and the Will is fundamentally one.\n\nSchopenhauer also uses the work to settle scores with the German idealist tradition. His attacks on Fichte, Schelling, and above all Hegel \u2014 \u201cthe philosophical scoundrel\u201d, the \u201cmaster of empty verbiage\u201d \u2014 are among the most vitriolic in philosophical literature.',
    themes: ['empirical confirmation of the Will metaphysics', 'physiology and vital force', 'comparative anatomy', 'plant physiology', 'the vegetative nervous system', 'animal magnetism', 'the unity of the Will across nature', 'the attack on Hegel and the idealists'],
    keyCharacters: [],
    concepts: [
        'Empirical confirmation of the Will \u2014 the central strategy: the sciences, pursued independently, converge on the conclusion that Will is the inner nature of natural phenomena',
        'Vital force as Will \u2014 the forces that maintain life and govern organic processes are grades of the Will; physiology is metaphysics in empirical form',
        'The vegetative nervous system as the Will\u2019s organ \u2014 the bridge between the blind, unconscious Will and the conscious intellect; the most direct expression of the Will in the body',
        'The unity of organic form \u2014 the morphological unity of organic forms across species (Goethe\u2019s Urpflanze, the vertebrate archetype) reflects the unity of the Will that objectifies itself in them',
        'Animal magnetism as evidence against individuation \u2014 the Will\u2019s ability to act across bodily boundaries confirms that individuation is phenomenal, not real'
    ],
    structure: 'Preface\nPhysiology\nComparative Anatomy\nPlant Physiology\nPhysical Astronomy\nLinguistics\nAnimal Magnetism and Magic\nSinology\nConclusion and General Survey',
    quote: 'That the Will, which constitutes our own inner nature, is the same thing that is present as the force of gravity in the stone, as the force of repulsion in the magnet, as the vital force in the plant \u2014 this is what I have shown, and this is what I am here demonstrating through the confirmation of the empirical sciences.',
    additionalQuotes: [
        { text: 'All genuine knowledge of nature is metaphysics, only it does not know it.', citation: 'On the Will in Nature, Conclusion (paraphrased)' }
    ],
    commentary: [
        { philosopher: 'Charles Darwin', text: 'Schopenhauer\u2019s account of the Will-to-live as the blind, insatiable striving underlying all organic phenomena was published twenty-three years before Darwin\u2019s Origin of Species (1859). Darwin\u2019s natural selection and Schopenhauer\u2019s Will-to-live are structurally similar: both posit a blind, purposeless force that drives organic life. Schopenhauer immediately recognised the kinship and claimed Darwin as a confirmation of his metaphysics, though Darwin\u2019s mechanism (variation and selection) differs entirely from Schopenhauer\u2019s (the Will as thing-in-itself).' }
    ],
    modernRelevance: 'On the Will in Nature is primarily of historical interest as a document in the relationship between Schopenhauer\u2019s metaphysics and nineteenth-century natural science. Its anticipation of the life-force tradition in biology (vitalism) and its engagement with Goethe\u2019s morphology place it in the context of debates about reductionism and teleology in the biological sciences that remain live today.',
    context: 'Published by Siegmund Schmerber in Frankfurt in 1836, eighteen years after the first edition of The World as Will and Representation. A second, substantially revised edition appeared in 1854. The work was written during the long period of Schopenhauer\u2019s obscurity, when his philosophy was ignored while Hegel\u2019s dominated German intellectual life. The ferocity of the attacks on Hegel throughout the work reflects Schopenhauer\u2019s frustration with his own neglect.',
    relatedWorks: ['world-as-will-vol1', 'world-as-will-vol2', 'fourfold-root', 'parerga-paralipomena']
},

{
    id: 'two-problems-ethics',
    title: 'The Two Fundamental Problems of Ethics',
    greekTitle: 'Die beiden Grundprobleme der Ethik',
    philosopher: 'schopenhauer',
    category: 'ethics',
    categoryLabel: 'Ethics & Moral Philosophy',
    date: '1841 AD',
    dateSort: 1841,
    emoji: '\u2696\uFE0F',
    cardSize: 'wide',
    readingDifficulty: 'Intermediate',
    estimatedWordCount: 130000,
    shortDesc: 'Schopenhauer\u2019s two prize essays on ethics \u2014 the devastating demolition of Kantian formalism and the positive account of compassion as the only genuine foundation of morality, arguing that the capacity to feel another\u2019s suffering as one\u2019s own is the source of all genuine moral behaviour.',
    summary: 'The Two Fundamental Problems of Ethics (Die beiden Grundprobleme der Ethik), published by Johann Christian Hermann\u2019sche Buchhandlung in Frankfurt in 1841, consists of two essays submitted for prizes by learned societies: \u201cOn the Freedom of the Human Will\u201d (submitted to the Royal Norwegian Society of Sciences, Trondheim, 1839, prize awarded) and \u201cOn the Basis of Morality\u201d (submitted to the Royal Danish Society of Sciences, Copenhagen, 1840, prize withheld despite being the only submission).\n\n\u201cOn the Freedom of the Human Will\u201d is Schopenhauer\u2019s most sustained analysis of freedom and necessity. He distinguishes three senses of freedom: physical freedom (absence of material constraint), intellectual freedom (acting on correct knowledge), and moral freedom (acting contrary to one\u2019s character). Schopenhauer argues that only physical and intellectual freedom are real. Moral freedom \u2014 the libertarian free will that Kant presupposes in his moral philosophy \u2014 is a philosophical illusion: our actions follow necessarily from our character (which is the phenomenal expression of the Will) and our motives (which are the occasions for the Will\u2019s expression). We feel that we could have acted otherwise; this feeling is an illusion produced by the fact that the same character confronted with a different motive would act differently. Genuine freedom \u2014 transcendental freedom \u2014 belongs not to the individual\u2019s actions but to the Will itself, which could have been otherwise in its fundamental character (the denial of the will-to-live is its expression).\n\n\u201cOn the Basis of Morality\u201d is Schopenhauer\u2019s most important work of moral philosophy and contains the most sustained attack on Kantian ethics in the history of philosophy. His critique of Kant has three parts. First, the categorical imperative is disguised egoism: the requirement to universalise one\u2019s maxims is ultimately grounded in self-interest (I refrain from lying because I would not want others to lie to me). Second, the Kantian formula \u201cact only on that maxim which you can at the same time will to be universal law\u201d is empty: it can be applied to justify almost any action if described at the right level of generality. Third, Kant\u2019s moral psychology is false: the categorical imperative cannot motivate action because \u201cought\u201d alone, without desire, produces no movement of the will.\n\nSchopenhauer\u2019s positive account: the only genuine foundation of morality is compassion (Mitleid \u2014 literally, \u201cco-suffering\u201d). I act morally when I genuinely feel another\u2019s suffering as my own \u2014 when the barrier of individuation breaks down and I recognise that the other\u2019s pain is the same Will-to-live that I am. Compassion is not a rational calculation but an immediate emotional recognition. It is the practical expression of the metaphysical insight that all individuals are ultimately one.',
    themes: ['freedom of the will', 'physical, intellectual, and moral freedom', 'character and necessity', 'the critique of Kantian ethics', 'the categorical imperative as empty', 'compassion (Mitleid) as the foundation of morality', 'the breakdown of individuation in compassion', 'the two virtues: justice and loving-kindness'],
    keyCharacters: [],
    concepts: [
        'Three kinds of freedom \u2014 physical (absence of material constraint), intellectual (acting on correct knowledge), moral (libertarian free will); only the first two are real',
        'Character as the phenomenal Will \u2014 our character is fixed and expresses itself necessarily in our actions; what varies is the motive (the occasion), not the character (the ground)',
        'Transcendental freedom \u2014 the Will itself could have been otherwise; the denial of the will-to-live is its expression; but this freedom belongs to the Will as thing-in-itself, not to the individual\u2019s actions',
        'The critique of the categorical imperative \u2014 disguised egoism; empty formalism; motivationally inert; cannot ground genuine moral obligations',
        'Compassion (Mitleid) as the only moral foundation \u2014 genuine moral motivation arises only when the barrier between self and other breaks down; I feel your suffering as my own; individuation is seen through',
        'Justice and loving-kindness \u2014 the two cardinal virtues: justice (refraining from harming others) and loving-kindness or charity (positively helping others); both flow from compassion',
        'The metaphysical basis of compassion \u2014 compassion is the practical recognition of the metaphysical truth that all individuals are expressions of the one Will; the suffering I prevent in another is the Will\u2019s own suffering'
    ],
    structure: 'Preface: The circumstances of the two essays\n\nEssay I: On the Freedom of the Human Will\n\u2014 Definition of the concept of freedom\n\u2014 The will before self-consciousness\n\u2014 The will before the consciousness of other things\n\u2014 Predecessors\n\u2014 Result and higher view\n\nEssay II: On the Basis of Morality\n\u2014 Introduction and statement of the problem\n\u2014 Critical review of the basis given by Kant for ethics (the categorical imperative)\n\u2014 The establishment of the only genuine foundation of ethics\n\u2014 The basis of ethics confirmed\n\u2014 The metaphysical basis: compassion as the practical expression of the identity of the Will',
    quote: 'Boundless compassion for all living beings is the firmest and surest guarantee of pure moral conduct, and needs no casuistry. Whoever is filled with it will assuredly injure no one, do harm to no one, encroach on no man\u2019s rights; he will rather have regard for every one, forgive every one, help every one as far as he can.',
    additionalQuotes: [
        { text: 'The categorical imperative smells of the theological \u2014 it is the echo of the command: thou shalt. If you ask why we should follow it, Kant replies: because it is a command of reason. And if you ask why that constitutes an obligation, you receive no answer.', citation: 'On the Basis of Morality, \u00a77 (paraphrased)' },
        { text: 'Man is the only animal that causes pain to others with no other object than causing pain. No other animal is cruel in the strict sense; only man is cruel.', citation: 'On the Basis of Morality, \u00a719' },
        { text: 'Do harm to no one; rather help everyone as much as you can. This is actually the proposition of which all ethical theories are more or less elaborate paraphrases.', citation: 'On the Basis of Morality, \u00a716 (paraphrased)' }
    ],
    commentary: [
        { philosopher: 'Emmanuel Levinas', text: 'Levinas\u2019s ethics of the Other \u2014 developed in Totality and Infinity (1961) and Otherwise than Being (1974) \u2014 is partly a radicalisation and partly a correction of Schopenhauer\u2019s compassion ethic. Levinas agrees that genuine morality begins with the other\u2019s suffering \u2014 specifically, with the face of the other that makes an infinite demand on me. But where Schopenhauer grounds compassion in the metaphysical identity of the Will (I feel your suffering as mine because we are ultimately the same), Levinas grounds it in the irreducible otherness of the other: it is precisely because you are not me that your suffering makes an absolute claim on me.' },
        { philosopher: 'Peter Singer', text: 'Singer\u2019s utilitarian ethics \u2014 particularly his argument for the equal consideration of the interests of all sentient beings \u2014 is partly a secularised development of Schopenhauer\u2019s compassion ethic. Schopenhauer was one of the first Western philosophers to argue seriously that the suffering of animals matters morally and that the exclusion of animals from moral consideration is a consequence of the Christian anthropocentrism he despised. Singer\u2019s Animal Liberation (1975) cites Schopenhauer alongside Bentham as precursors.' }
    ],
    modernRelevance: 'The Two Fundamental Problems of Ethics is one of the most important texts in the history of moral philosophy. The critique of Kantian ethics remains the most penetrating in the tradition: the charges of disguised egoism, empty formalism, and motivational inertness continue to be discussed in contemporary Kant scholarship. The positive account of compassion as the foundation of morality anticipates care ethics (Noddings, Gilligan), virtue ethics\u2019 emphasis on empathy, and contemporary neuroscience of moral judgment (mirror neurons as the neural correlate of Schopenhauerian Mitleid). The argument for animal ethics is the first systematic philosophical case for the moral status of animals in the Western tradition.',
    context: 'The first essay won the prize of the Royal Norwegian Society of Sciences in 1839; the second was the only submission for the prize of the Royal Danish Society of Sciences in 1840 but was withheld because the jury found Schopenhauer\u2019s treatment of Kant insufficiently respectful and his positive account of morality insufficiently grounded in pure reason. Schopenhauer published both essays together in 1841, adding a preface that dwells on the injustice of the Danish society\u2019s decision with characteristic bitterness.',
    relatedWorks: ['world-as-will-vol1', 'world-as-will-vol2', 'fourfold-root', 'parerga-paralipomena']
}

);
"""

# ── data-21d: Parerga and Paralipomena Vol. 1 ────────────────────────────────
files['data-21d.js'] = r"""/* DATA PART 21d — Schopenhauer: Parerga and Paralipomena */
window.WORKS.push(

{
    id: 'parerga-paralipomena',
    title: 'Parerga and Paralipomena',
    greekTitle: 'Parerga und Paralipomena: Kleine philosophische Schriften',
    philosopher: 'schopenhauer',
    category: 'practical',
    categoryLabel: 'Essays & Aphorisms',
    date: '1851 AD',
    dateSort: 1851,
    emoji: '\u270F\uFE0F',
    cardSize: 'wide',
    readingDifficulty: 'Beginner',
    estimatedWordCount: 600000,
    shortDesc: 'The work that made Schopenhauer famous \u2014 two volumes of essays, aphorisms, and observations covering everything from the misery of existence to the art of writing, from the nature of genius to the correct treatment of poodles, written with a wit and directness that made philosophy accessible to a general educated audience for the first time since Montaigne.',
    summary: 'Parerga and Paralipomena: Short Philosophical Essays (Parerga und Paralipomena: Kleine philosophische Schriften), published in two volumes by A.W. Hayn in Berlin in November 1851, is the work that transformed Schopenhauer from a neglected philosopher into a celebrity. It sold out its first edition quickly \u2014 after years during which his major works gathered dust \u2014 and made him the most widely read philosopher in Germany within a decade of its publication.\n\nThe title means \u201cby-works and omissions\u201d: the Parerga are works that stand alongside the main system; the Paralipomena are things left out of the main works. Both volumes are collections of essays, observations, and aphorisms that presuppose the philosophical system of The World as Will and Representation but present its insights in a more accessible and more literary form.\n\nVolume I contains six longer essays: Sketch of a History of the Doctrine of the Ideal and the Real; On the University Philosophy (a ferocious attack on academic philosophy as a conspiracy of salaried professors to avoid genuine philosophical insight); On the Theory of Colours; Some Observations on the Contrast of the Thing-in-Itself and the Appearance; Transcendent Speculation on the Apparent Deliberateness in the Fate of the Individual; and Fragments for the History of Philosophy.\n\nVolume II, the Paralipomena, is divided into thirty-one chapters covering an extraordinary range of topics: thinking and writing, reading, learning and the learned, independent thinking, on style, on genius, on women (notorious for its misogyny), on law and politics, on religion, on death, on the sorrow of the world, on the affirmation and denial of the will-to-live, on suicide, and the famous \u201cAphorisms on the Wisdom of Life\u201d \u2014 the most widely read section of Schopenhauer\u2019s work.\n\nThe \u201cAphorisms on the Wisdom of Life\u201d (Aphorismen zur Lebensweisheit) is Schopenhauer\u2019s most popular and most accessible work. It sets aside the metaphysical pessimism of the main system and asks a more practical question: given that we are condemned to existence, how should we conduct ourselves to minimise suffering and maximise what passes for happiness? The answer draws on Aristotle\u2019s distinction between goods of personality (health, intelligence, character), goods of property, and goods of reputation, arguing that personality is overwhelmingly the most important and that the other two are largely beyond our control and largely a source of misery.',
    themes: ['the aphorisms on the wisdom of life', 'on writing and style', 'on genius and talent', 'the attack on academic philosophy', 'on women (and Schopenhauer\u2019s misogyny)', 'on reading', 'on death and the denial of the will', 'on noise and its effect on thought', 'on suicide', 'on religion and its relationship to philosophy'],
    keyCharacters: [],
    concepts: [
        'The three classes of goods \u2014 what a man is (personality, health, intelligence, character); what a man has (property, reputation, honour); what a man represents (social position); personality is overwhelmingly the most important',
        'Personality as the primary source of wellbeing \u2014 what a man is, not what he has or appears, determines his fundamental experience of life; the rich man can be miserable; the poor man with a healthy temperament may be happy',
        'The attack on academic philosophy \u2014 university philosophy is governed by the interests of the state and the church; professors are hired to defend orthodoxy, not to seek truth; genuine philosophy has never emerged from a professorial chair',
        'On genius \u2014 genius is the capacity for sustained, will-less contemplation of the world; it is the temporary dominance of the pure intellect over the Will; most men are capable of it only briefly',
        'On reading \u2014 excessive reading fills the mind with other men\u2019s thoughts and prevents the development of one\u2019s own; one hour of thinking for every four hours of reading',
        'The wisdom of life as prudential philosophy \u2014 not the highest metaphysical wisdom (which recommends denial of the Will) but the practical wisdom of how to live well within the constraints of existence',
        'On noise \u2014 the cracking of whips and other unnecessary noise are the most destructive enemies of thought; a sign of general thoughtlessness and insensitivity; Schopenhauer\u2019s most personal obsession'
    ],
    structure: 'Volume I: Parerga\n\u2014 Sketch of a History of the Doctrine of the Ideal and the Real\n\u2014 Fragments for the History of Philosophy\n\u2014 On University Philosophy\n\u2014 On the Theory of Colours\n\u2014 On the Foundation of Ethics\n\u2014 Transcendent Speculation on the Apparent Deliberateness in the Fate of the Individual\n\nVolume II: Paralipomena (31 chapters)\n\u2014 Chapter 1: On Philosophy and its Method\n\u2014 Chapter 2: On Logic and Dialectic\n\u2014 Chapter 3: On the Theory of Knowledge\n\u2014 Chapter 9: On Ethics\n\u2014 Chapter 12: On Religion\n\u2014 Chapter 13: On Books and Writing\n\u2014 Chapter 14: Aphorisms on the Wisdom of Life\n\u2014 Chapter 15: On Physiognomy\n\u2014 Chapter 17: On Women\n\u2014 Chapter 22: On the Suffering of the World\n\u2014 Chapter 27: On Suicide\n\u2014 Chapter 28: On Women (second essay)\n\u2014 Chapter 29: On Noise',
    quote: 'The greatest of follies is to sacrifice health for any other kind of happiness. Health is by far the most important element in human happiness, and health is so much a matter of temperament that it is largely independent of external circumstances.',
    additionalQuotes: [
        { text: 'Talent hits a target no one else can hit; Genius hits a target no one else can see.', citation: 'Parerga and Paralipomena, Vol. II, \u201cOn Genius\u201d' },
        { text: 'We forfeit three-fourths of ourselves in order to be like other people.', citation: 'Parerga and Paralipomena, Vol. II, \u201cAphorisms on the Wisdom of Life\u201d' },
        { text: 'Reading is merely a surrogate for thinking for yourself; it means letting someone else direct your thoughts. Many books serve merely to show how many ways there are of being wrong, and how far astray you yourself would go if you followed their guidance.', citation: 'Parerga and Paralipomena, Vol. II, \u201cOn Books and Writing\u201d' },
        { text: 'Every nation ridicules other nations, and all are right.', citation: 'Parerga and Paralipomena, Vol. II (aphorism)' },
        { text: 'To live alone is the fate of all great souls.', citation: 'Parerga and Paralipomena, Vol. II (aphorism)' }
    ],
    commentary: [
        { philosopher: 'Friedrich Nietzsche', text: 'Nietzsche\u2019s \u201cSchopenhauer as Educator\u201d (third of the Untimely Meditations, 1874) is the most important philosophical appreciation of Schopenhauer\u2019s work. Nietzsche uses Schopenhauer \u2014 and particularly the Schopenhauer of the Parerga, the unflinching confronter of existence\u2019s cruelty and the enemy of all academic complacency \u2014 as the model of the genuine philosopher who lives according to his own insight rather than the conventions of the academy. By the time Nietzsche writes the essay, he is already beginning to part ways with Schopenhauer\u2019s pessimism; but his portrait of philosophical courage and integrity is thoroughly Schopenhauerian.' },
        { philosopher: 'Leo Tolstoy', text: 'Tolstoy discovered the Parerga in the 1860s and described his encounter with Schopenhauer as the most important intellectual experience of his maturity. The influence is pervasive in War and Peace, Anna Karenina, and the late religious works: Schopenhauer\u2019s pessimism about the Will-to-live, his compassion ethic, and his account of death as the dissolution of the individual into the one Will are among the deepest currents of Tolstoyan fiction.' },
        { philosopher: 'Samuel Beckett', text: 'Beckett\u2019s reading of Schopenhauer \u2014 particularly the Parerga\u2019s essays on the misery of existence, boredom, and the vanity of willing \u2014 is one of the most consequential literary receptions of a philosopher in the twentieth century. Waiting for Godot, Endgame, and the Trilogy enact Schopenhauerian themes: the characters are the Will in its most naked futility, waiting without knowing what they wait for, unable to be still, unable to go on, going on.' }
    ],
    modernRelevance: 'The Parerga and Paralipomena is the most widely read of Schopenhauer\u2019s works and the primary vehicle of his influence on literary modernism and popular philosophy. The \u201cAphorisms on the Wisdom of Life\u201d remain in continuous print and are among the most cited philosophical aphorisms in any language. Schopenhauer\u2019s influence on literary figures \u2014 Tolstoy, Turgenev, Maupassant, Hardy, Conrad, Mann, Borges, Beckett \u2014 has been profound and largely transmitted through the Parerga. His essays on writing, reading, and the academic establishment have a permanent readership among writers and intellectuals who never engage with his metaphysics. The attacks on academic philosophy retain their sting.',
    context: 'Published by A.W. Hayn in Berlin in November 1851, in an edition of 750 copies. Schopenhauer was sixty-three. Several publishers had refused the work before Hayn accepted it. The first edition sold out within months \u2014 the first real commercial success of Schopenhauer\u2019s publishing career after thirty years of neglect. The philosopher John Oxenford published a long appreciative article in the Westminster Review in 1853, \u201cIconoclasm in German Philosophy,\u201d which introduced Schopenhauer to the English-speaking world and accelerated his European celebrity. By the time of his death in 1860 he was the most famous philosopher in Germany.',
    relatedWorks: ['world-as-will-vol1', 'world-as-will-vol2', 'two-problems-ethics', 'fourfold-root']
}

);
"""

# ── data-21e: On the Basis of Morality essays + Prize essay on freedom ────────
files['data-21e.js'] = r"""/* DATA PART 21e — Schopenhauer: Essays from Parerga + Manuscript Remains */
window.WORKS.push(

{
    id: 'essays-schopenhauer',
    title: 'Essays and Aphorisms',
    greekTitle: 'Selected from Parerga und Paralipomena, Band II',
    philosopher: 'schopenhauer',
    category: 'practical',
    categoryLabel: 'Philosophy of Life',
    date: '1851 AD',
    dateSort: 1852,
    emoji: '\uD83D\uDCA1',
    cardSize: 'normal',
    readingDifficulty: 'Beginner',
    estimatedWordCount: 100000,
    shortDesc: 'The most quotable philosopher of the nineteenth century at his most accessible \u2014 Schopenhauer\u2019s short essays on the suffering of the world, the vanity of existence, suicide, religion, and the correct attitude toward one\u2019s own misery, selected from the Paralipomena for those who want the insights without the system.',
    summary: 'The essays collected in this entry represent the most widely read sections of Schopenhauer\u2019s Paralipomena (Volume II of Parerga and Paralipomena, 1851) \u2014 the short pieces that have circulated most widely in anthologies, translations, and popular philosophy collections, and that have influenced writers and thinkers who never engaged with the technical metaphysics of The World as Will and Representation.\n\n\u201cOn the Suffering of the World\u201d (Zur Leidenlehre, Chapter 12 of the Paralipomena) is the most concentrated statement of Schopenhauer\u2019s philosophical pessimism. The world is not a place where occasional evil interrupts a background of good; it is a place where suffering is the norm and brief pleasures are the interruption. The optimism of Leibniz \u2014 the claim that this is the best of all possible worlds \u2014 is, for Schopenhauer, either a bad joke or a wilful blindness. If God made this world, I would not wish to be God.\n\n\u201cOn the Vanity of Existence\u201d argues that human life, viewed sub specie aeternitatis, is a brief flicker between two infinities of non-existence. The present moment \u2014 the only time we truly exist \u2014 is always slipping into the past. Our desires, when fulfilled, immediately generate new desires; our pleasures are merely the temporary cessation of pain. The result is a life that, when honestly assessed, amounts to very little.\n\n\u201cOn Suicide\u201d is Schopenhauer\u2019s most counterintuitive essay: he argues that suicide, far from being the negation of the will-to-live, is actually its most intense affirmation. The suicide does not deny the will-to-live; he affirms it so intensely that he destroys himself rather than endure the conditions under which it must be lived. True denial of the will-to-live \u2014 asceticism \u2014 is the opposite: continuing to live while renouncing every desire.\n\n\u201cOn Religion\u201d distinguishes the exoteric and esoteric content of the great world religions. The exoteric content \u2014 the doctrines, rituals, and mythology \u2014 is adapted to the level of ordinary, unphilosophical people and cannot withstand philosophical scrutiny. The esoteric content \u2014 the practical wisdom of renunciation, compassion, and the recognition of suffering as the essence of existence \u2014 is the same in all the great religions and is a non-theological formulation of the truths Schopenhauer has established by philosophical argument.',
    themes: ['the suffering of the world', 'pessimism', 'the vanity of existence', 'suicide as affirmation not denial', 'the exoteric and esoteric content of religion', 'Buddhism and Hinduism as pessimist philosophies', 'the correct attitude to death', 'compassion as the only virtue'],
    keyCharacters: [],
    concepts: [
        'Pessimism as realism \u2014 the recognition that suffering is the norm and pleasure the exception is not a psychological disposition but an accurate assessment of the world',
        'The vanity of existence \u2014 human life, viewed honestly, amounts to very little; the present is always slipping into the past; desires are never finally satisfied',
        'Suicide as affirmation not denial \u2014 the suicide affirms the will-to-live so intensely that he destroys himself rather than endure its conditions; genuine denial is asceticism, not suicide',
        'The exoteric and esoteric content of religion \u2014 the doctrines of world religions are mythological adaptations of philosophical truths; their esoteric core is the same practical wisdom of renunciation and compassion',
        'Buddhism as the truest religion \u2014 Buddhism, in Schopenhauer\u2019s reading, is the world religion whose esoteric content most closely matches his own philosophical conclusions: suffering as the essence of existence, desire as its cause, the denial of desire as its cure',
        'Compassion as the only morality \u2014 the repeated theme of the short essays: genuine moral motivation is always compassion; everything else is self-interest in disguise'
    ],
    structure: 'Selected chapters from Paralipomena (Volume II of Parerga and Paralipomena):\n\n\u201cOn the Suffering of the World\u201d (Chapter 12)\n\u201cOn the Vanity of Existence\u201d (Chapter 11)\n\u201cOn Suicide\u201d (Chapter 27)\n\u201cOn Religion\u201d (Chapter 15)\n\u201cOn Books and Writing\u201d (Chapter 23)\n\u201cAphorisms on the Wisdom of Life\u201d (Chapter 26)\n\u201cOn Noise\u201d (Chapter 30)',
    quote: 'If we were not all so interested in ourselves, life would be so uninteresting that none of us would be able to endure it.',
    additionalQuotes: [
        { text: 'Compassion is the basis of all morality.', citation: 'On the Basis of Morality (frequently cited aphoristic version)' },
        { text: 'The two enemies of human happiness are pain and boredom.', citation: 'Parerga and Paralipomena, Vol. II, \u201cAphorisms on the Wisdom of Life\u201d' },
        { text: 'Polite tones are like filaments of glass: beautiful and breakable.', citation: 'Parerga and Paralipomena, Vol. II (aphorism)' },
        { text: 'It is a clear gain to sacrifice pleasure in order to avoid pain.', citation: 'Parerga and Paralipomena, Vol. II, \u201cAphorisms on the Wisdom of Life\u201d' },
        { text: 'The person who writes for fools is always sure of a large audience.', citation: 'Parerga and Paralipomena, Vol. II, \u201cOn Books and Writing\u201d' }
    ],
    commentary: [
        { philosopher: 'Emil Cioran', text: 'Cioran\u2019s entire philosophical project \u2014 from On the Heights of Despair (1934) through The Trouble with Being Born (1973) \u2014 is a radicalisation of Schopenhauer\u2019s pessimism. Where Schopenhauer derives pessimism from metaphysical argument and offers asceticism and aesthetic contemplation as escapes, Cioran makes pessimism into a literary and existential style, with no escape and no consolation. Schopenhauer is the pessimist who still believes in philosophy; Cioran is the pessimist who does not.' },
        { philosopher: 'Albert Camus', text: 'Camus\u2019s The Myth of Sisyphus (1942) is partly a response to Schopenhauerian pessimism. Camus accepts Schopenhauer\u2019s diagnosis \u2014 existence is absurd, desires are never satisfied, death is inevitable \u2014 but rejects his prescription. Where Schopenhauer recommends the denial of the will-to-live, Camus recommends revolt, freedom, and passion. One must imagine Sisyphus happy is Camus\u2019s answer to Schopenhauer\u2019s pendulum.' }
    ],
    modernRelevance: 'These essays have had a disproportionate influence on literary culture relative to their philosophical weight. Schopenhauer\u2019s short essays on suffering, boredom, and the vanity of existence are the philosophical source of modern literary pessimism and of what might be called philosophical melancholy as a cultural style. The essay on suicide anticipates contemporary debates about euthanasia and the right to die. The essay on religion anticipates the perennial philosophy tradition (Huxley) and interfaith dialogue. The aphorisms have a permanent readership in the popular philosophy market.',
    context: 'These chapters are drawn from Volume II of Parerga and Paralipomena (1851). They are the sections most frequently anthologised in the many popular selections from Schopenhauer published after his celebrity in the 1850s. R.J. Hollingdale\u2019s Essays and Aphorisms (Penguin, 1970) is the most widely read English anthology of these pieces.',
    relatedWorks: ['parerga-paralipomena', 'world-as-will-vol1', 'two-problems-ethics', 'world-as-will-vol2']
},

{
    id: 'schopenhauer-on-human-nature',
    title: 'On Human Nature',
    greekTitle: 'Selected from Parerga und Paralipomena and manuscript remains',
    philosopher: 'schopenhauer',
    category: 'practical',
    categoryLabel: 'Psychology & Ethics',
    date: '1851 AD',
    dateSort: 1853,
    emoji: '\uD83E\uDDE0',
    cardSize: 'normal',
    readingDifficulty: 'Beginner',
    estimatedWordCount: 60000,
    shortDesc: 'Schopenhauer\u2019s psychological observations on human character, egoism, envy, spite, justice, the state, and the depths of human malice \u2014 the most penetrating short account of human nature as it actually is rather than as moralists wish it to be.',
    summary: 'On Human Nature collects Schopenhauer\u2019s most incisive psychological observations, drawn primarily from Volume II of Parerga and Paralipomena (1851) and the posthumously published manuscript remains. These pieces represent Schopenhauer at his most morally diagnostic \u2014 the philosopher as psychologist, stripping away the conventional pieties about human goodness to reveal the Will\u2019s actual operations in social life.\n\nThe central psychological thesis, consistent with the metaphysics of The World as Will and Representation: human beings are fundamentally egotistic. Egoism is the direct and natural expression of the Will-to-live in individual form; it is not a moral failing but a metaphysical necessity. The egotistic individual experiences himself as the centre of the world, and in a sense he is: the whole world of representation exists only for a subject, and each individual is that subject for himself. The Will, which is one in itself, experiences itself as many individuals each of whom places himself at the centre.\n\nFrom fundamental egoism derive two distinctly human vices: malice and spite. Egoism seeks only its own good; it is indifferent to others\u2019 suffering. Malice actively desires others\u2019 suffering, independently of any benefit to itself: it is the Will\u2019s self-torment, since all suffering is ultimately the suffering of the one Will. Schopenhauer\u2019s account of envy \u2014 the most socially destructive of the passions \u2014 as the root of much apparently principled political thought is one of the most psychologically penetrating passages in the Parerga.\n\nThe essays on justice and the state argue that the state is not a moral institution but a mechanism for limiting mutual harm: it arises from the recognition that unlimited egoism produces a condition in which everyone suffers more than they would under a legal framework. The Hobbesian insight is correct, but Schopenhauer\u2019s derivation is from the metaphysics of the Will rather than from a social contract.',
    themes: ['egoism as the fundamental human drive', 'malice and spite as distinctly human', 'envy and its social consequences', 'justice as mutual harm limitation', 'the state as a mechanism not a moral ideal', 'character as fixed and the impossibility of moral education', 'on the knowledge of character'],
    keyCharacters: [],
    concepts: [
        'Egoism as metaphysical necessity \u2014 the Will-to-live in individual form necessarily places that individual at the centre; egoism is not a moral failing but the direct expression of the Will',
        'Malice and spite as distinctly human \u2014 unlike mere egoism (indifferent to others\u2019 suffering), malice actively desires it; man is the only animal that is genuinely cruel',
        'Envy as the root of false principled politics \u2014 much of what appears as a demand for justice is actually envy: the desire that others not have what one lacks, disguised as a moral principle',
        'The state as mutual harm limitation \u2014 not a moral ideal but a practical mechanism for limiting the damage unlimited egoism would cause; Hobbes was right about the motive, wrong about the contract',
        'Character as fixed \u2014 a person\u2019s fundamental character is the phenomenal expression of the Will and cannot be changed by moral education; what can change is only conduct, not character',
        'Physiognomy and character \u2014 the face reflects the accumulated moral history of the will; physiognomy is a genuine science, though not one that yields confident specific judgments'
    ],
    structure: 'Selected chapters from Paralipomena and manuscript remains:\n\n\u201cOn Ethics\u201d (Chapter 9 of Paralipomena)\n\u201cOn Law and Politics\u201d (Chapter 9, section 2)\n\u201cOn Human Nature\u201d (selected aphorisms from Chapter 14)\n\u201cOn Physiognomy\u201d (Chapter 15)\n\u201cOn Various Subjects\u201d (selected aphorisms)\nManuscript remains on egoism, envy, and malice',
    quote: 'The world is not a work of art for our pleasure; it is the expression of a will that wills because it wills, that has no other aim than willing itself. What we call pleasure is merely the cessation of pain, and what we call pain is the direct expression of the will asserting itself.',
    additionalQuotes: [
        { text: 'Mostly it is loss which teaches us about the worth of things.', citation: 'Parerga and Paralipomena, Vol. II (aphorism)' },
        { text: 'The basis of all good character is a fundamental unselfishness, stemming from the sympathetic participation in the joys and sorrows of others \u2014 that is, from Mitleid.', citation: 'On the Basis of Morality, \u00a722 (paraphrased)' },
        { text: 'All truth passes through three stages. First, it is ridiculed. Second, it is violently opposed. Third, it is accepted as being self-evident.', citation: 'Attributed; not found verbatim in Schopenhauer\u2019s works but consistent with the Parerga\u2019s tone' }
    ],
    commentary: [
        { philosopher: 'Sigmund Freud', text: 'Freud\u2019s structural model of the psyche \u2014 the id (the reservoir of drives), the ego (the reality-testing executive), and the superego (the internalised social norms) \u2014 is a precise psychoanalytic reformulation of Schopenhauer\u2019s metaphysical psychology. The id is the Will; the ego is the intellect in the service of the Will; the superego is the social pressure that opposes the Will\u2019s expression. Freud\u2019s account of egoism, malice, envy, and the mechanisms of self-deception closely parallels Schopenhauer\u2019s, transposed into the vocabulary of clinical observation.' },
        { philosopher: 'Friedrich Nietzsche', text: 'Nietzsche\u2019s psychological genealogy \u2014 the unmasking of moral motivations to reveal the Will to power beneath them \u2014 is structurally derived from Schopenhauer\u2019s exposure of egoism beneath moral pretension. But where Schopenhauer treats egoism as a metaphysical fact to be lamented and overcome, Nietzsche treats the will as something to be affirmed and celebrated. Nietzsche\u2019s \u201cpsychology as the master key to true philosophy\u201d is Schopenhauerian pessimism inverted.' }
    ],
    modernRelevance: 'These observations on human nature have had a continuous readership as practical psychology. Schopenhauer\u2019s analysis of envy \u2014 the desire that others not have what one lacks \u2014 as the root of resentment and much political ideology anticipates Nietzsche\u2019s ressentiment and remains one of the most useful conceptual tools for understanding social dynamics. The account of character as fixed anticipates behaviour genetics and the contemporary recognition that personality traits have substantial heritability. The analysis of malice as a distinctly human phenomenon anticipates both evolutionary psychology\u2019s account of aggression and Hannah Arendt\u2019s concept of radical evil.',
    context: 'These observations are drawn from Volume II of Parerga and Paralipomena (1851), from the essay collections On Human Nature and The Wisdom of Life published in various English-language anthologies, and from Schopenhauer\u2019s posthumously published manuscript remains (Aus Arthur Schopenhauers handschriftlichem Nachlass, 1864). The best English anthology is T. Bailey Saunders\u2019 translations published by Swan Sonnenschein in the 1890s and reprinted many times.',
    relatedWorks: ['parerga-paralipomena', 'two-problems-ethics', 'world-as-will-vol1', 'essays-schopenhauer']
}

);
"""

for fname, content in files.items():
    path = os.path.join(js, fname)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'  Written {fname}  ({content.count(chr(10))} lines)')
