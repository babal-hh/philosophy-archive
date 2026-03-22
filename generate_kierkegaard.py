#!/usr/bin/env python3
"""
Kierkegaard — data-20a through data-20e (10 works)
Run from ~/Desktop/philosophy-archive/: python3 generate_kierkegaard.py
"""
import os
js = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'js')
os.makedirs(js, exist_ok=True)

files = {}

# ── data-20a: Either/Or ──────────────────────────────────────────────────────
files['data-20a.js'] = r"""/* DATA PART 20a — Kierkegaard: Either/Or */
window.WORKS.push(
{
    id: 'either-or',
    title: 'Either/Or: A Fragment of Life',
    greekTitle: 'Enten \u2013 Eller. Et Livs-Fragment',
    philosopher: 'kierkegaard',
    category: 'aesthetics',
    categoryLabel: 'Aesthetics & Ethics',
    date: '1843 AD',
    dateSort: 1843,
    emoji: '\uD83C\uDFAD',
    cardSize: 'wide',
    readingDifficulty: 'Intermediate',
    estimatedWordCount: 220000,
    shortDesc: 'Kierkegaard\u2019s debut masterpiece \u2014 an elaborate literary performance in two volumes presenting the aesthetic and ethical stages of existence without choosing between them, forcing the reader to make the choice philosophy cannot make for them.',
    summary: 'Either/Or: A Fragment of Life (Enten \u2013 Eller. Et Livs-Fragment), published on 20 February 1843 under the pseudonym Victor Eremita by C.A. Reitzel in Copenhagen, is Kierkegaard\u2019s first major philosophical work and one of the most architecturally complex in the history of philosophy. Kierkegaard was twenty-nine. The work went through two editions in his lifetime and established him immediately as the most original voice in Danish letters.\n\nThe elaborate fictional frame: Victor Eremita (\u201cVictor the Hermit\u201d) claims to have found two bundles of papers in the secret drawer of a writing desk he purchased at auction. Part One contains the papers of \u201cA,\u201d a young aesthete of brilliant but directionless intelligence. Part Two contains the letters and essays of \u201cJudge William,\u201d a magistrate who responds to A with a sustained defence of the ethical life. Victor Eremita professes not to know whether A and the Judge are the same person, different people, or fictional constructions.\n\nPart One (\u201cThe Aesthetic\u201d) is the most diverse and the most celebrated half. It opens with the Diapsalmata \u2014 a collection of aphorisms and fragments, some of the most quoted in the philosophical literature. The centrepiece is \u201cThe Immediate Erotic Stages, or the Musical Erotic\u201d \u2014 a lengthy and brilliant analysis of Mozart\u2019s Don Giovanni as the perfect expression of the immediately erotic, the life of pure sensuous immediacy without reflection. The aesthetic culminates in \u201cThe Seducer\u2019s Diary,\u201d the fictional journal of Johannes the Seducer, a cold and calculating aesthete who orchestrates the seduction of a young woman as a work of art, then abandons her when the conquest is complete. The Seducer\u2019s Diary is the most unsettling portrait of the aesthetic life at its extreme: the reduction of another person to a medium for one\u2019s own self-expression.\n\nPart Two (\u201cThe Ethical\u201d) consists of two long letters from Judge William to A, defending the ethical life against the aesthetic. The Judge\u2019s central argument: the aesthetic life is not genuinely lived because the aesthete never commits \u2014 never chooses himself in his eternal validity. The ethical life begins with the act of self-choice: the recognition that one has a self with obligations, a history, and a future. Marriage is the Judge\u2019s paradigm case: not the romantic passion of the aesthete but the daily renewal of commitment, the transformation of first love into conjugal love through repeated free choice. The work ends without resolution: Victor Eremita does not choose between A and the Judge, and the reader is left with the existential demand \u2014 to choose \u2014 that neither the aesthetic nor the ethical analysis can make on their behalf.',
    themes: ['the aesthetic and ethical stages of existence', 'the aesthete and the ethicist', 'Don Giovanni as the musical erotic', 'the Seducer\u2019s Diary', 'self-choice and commitment', 'marriage as ethical paradigm', 'boredom and the rotation method', 'pseudonymous authorship', 'indirect communication', 'the either/or as existential demand'],
    keyCharacters: [
        { name: 'A (the Aesthete)', role: 'The unnamed author of Part One; brilliant, melancholic, and uncommitted; his life is organised around the avoidance of boredom through aesthetic variation; represented most fully in the Diapsalmata and the Seducer\u2019s Diary' },
        { name: 'Judge William', role: 'The author of Part Two; a magistrate and married man who defends the ethical life against the aesthete; his position represents the second stage of existence: self-choice, commitment, and the transformation of passion into obligation' },
        { name: 'Johannes the Seducer', role: 'The protagonist of the Seducer\u2019s Diary; a cold, calculating aesthete who orchestrates a seduction as a work of art; the most extreme expression of the aesthetic life as the reduction of others to instruments of one\u2019s own self-cultivation' }
    ],
    concepts: [
        'The aesthetic stage of existence \u2014 the life organised around the immediate satisfaction of desire, the cultivation of mood, and the avoidance of boredom; it lacks the continuity and commitment of genuine selfhood',
        'The ethical stage of existence \u2014 the life organised around duty, commitment, and self-choice; the recognition that one has a self with obligations and a history',
        'The Diapsalmata \u2014 the aphoristic opening of Part One: fragments of mood, wit, and despair expressing the aesthetic consciousness at its most articulate and most directionless',
        'Don Giovanni as the musical erotic \u2014 Mozart\u2019s opera as the perfect artistic expression of the immediately erotic; music as the art form of immediacy; Don Giovanni as the paradigm of the aesthetic man',
        'The rotation method (Vexiermetode) \u2014 the aesthete\u2019s strategy for avoiding boredom: vary the stimulus, not the situation; cultivate the accidental; transform every experience into material for reflection',
        'The Seducer\u2019s Diary \u2014 the coldly self-aware journal of Johannes, who seduces Cordelia as a work of art and abandons her when the aesthetic interest is exhausted; the self-refutation of the aesthetic life',
        'Self-choice \u2014 Judge William\u2019s central concept: the ethical life begins when one chooses oneself \u2014 not a different self but one\u2019s actual self, with its history, obligations, and finitude, in its eternal validity',
        'Either/Or as existential demand \u2014 the title is not a logical disjunction but an existential one: the demand to choose between ways of life that cannot be rationally adjudicated from outside; the choice itself constitutes the chooser'
    ],
    structure: 'Editorial Preface by Victor Eremita\n\nPart One: A\u2019s Papers\n\u2014 Diapsalmata (aphorisms)\n\u2014 The Immediate Erotic Stages, or The Musical Erotic (on Mozart\u2019s Don Giovanni)\n\u2014 The Ancient Tragical Motif as Reflected in the Modern\n\u2014 Shadowgraphs (on feminine unhappiness)\n\u2014 The Unhappiest One\n\u2014 The First Love (a comedy review)\n\u2014 The Rotation of Crops (the rotation method; on boredom)\n\u2014 The Seducer\u2019s Diary\n\nPart Two: Judge William\u2019s Letters\n\u2014 Letter I: The Aesthetic Validity of Marriage\n\u2014 Letter II: The Balance Between the Aesthetic and the Ethical in the Development of Personality\n\u2014 Appendix: Ultimatum (a sermon from Jutland)',
    quote: 'Marry, and you will regret it; don\u2019t marry, you will also regret it; marry or don\u2019t marry, you will regret it either way. Laugh at the world\u2019s foolishness, you will regret it; weep over it, you will regret that too; laugh at the world\u2019s foolishness or weep over it, you will regret both.',
    additionalQuotes: [
        { text: 'What is a poet? An unhappy man who hides deep anguish in his heart, but whose lips are so formed that when the sigh and cry pass through them, it sounds like lovely music.', citation: 'Either/Or, Part I, Diapsalmata' },
        { text: 'Boredom is the root of all evil. The history of this can be traced from the very beginning of the world. The gods were bored, and so they created human beings.', citation: 'Either/Or, Part I, \u201cThe Rotation of Crops\u201d' },
        { text: 'People hardly ever make use of the freedom they have, for example freedom of thought; instead they demand freedom of speech as compensation.', citation: 'Either/Or, Part I, Diapsalmata' },
        { text: 'My depression is the most faithful mistress I have known \u2014 no wonder, then, that I return the love.', citation: 'Either/Or, Part I, Diapsalmata' }
    ],
    commentary: [
        { philosopher: 'Jean-Paul Sartre', text: 'Sartre\u2019s Being and Nothingness (1943) develops the existential structure of Either/Or\u2019s analysis of choice into a full ontology of freedom. Sartre\u2019s doctrine of radical freedom \u2014 that existence precedes essence, that we are condemned to choose, that bad faith consists in denying one\u2019s freedom \u2014 is the secularised development of Kierkegaard\u2019s either/or. But Sartre removes the theological dimension: where Kierkegaard\u2019s either/or is ultimately oriented toward the religious stage, Sartre\u2019s either/or opens onto a godless universe in which freedom is absolute and groundless.' },
        { philosopher: 'Theodor Adorno', text: 'Adorno\u2019s Kierkegaard: Construction of the Aesthetic (1933; English 1989) is the first major philosophical study of Either/Or and remains one of the most challenging. Adorno argues that the aesthetic stage, far from being straightforwardly criticised by the ethical, is also a dialectical critique of bourgeois society: the aesthete\u2019s refusal of commitment is the refusal of a society that reduces commitment to contractual obligation. The Seducer\u2019s Diary is not simply the portrait of a monster but a negative theology of freedom.' },
        { philosopher: 'Alasdair MacIntyre', text: 'MacIntyre\u2019s After Virtue (1981) uses Either/Or as the paradigm case of the emotivist culture he diagnoses in modern ethics: the inability to resolve moral disagreements rationally, which MacIntyre traces to the loss of the Aristotelian tradition, is exactly what Kierkegaard\u2019s either/or enacts. But MacIntyre argues that Kierkegaard draws the wrong conclusion: the inability to rationally adjudicate between aesthetic and ethical life is a symptom of cultural pathology, not an eternal structure of human existence.' },
        { philosopher: 'George Pattison', text: 'Pattison\u2019s work on Kierkegaard\u2019s aesthetics argues that the analysis of Don Giovanni in Part One is the most original philosophy of music produced before Nietzsche and Wagner: the claim that music is the art form of immediacy, that it alone can give perfect expression to the erotic as pure sensuous force, anticipates the Wagnerian synthesis of music and drama.' }
    ],
    modernRelevance: 'Either/Or is the founding text of existentialism and one of the most consequential works of philosophical literature in the modern period. Its portrait of the aesthete \u2014 brilliant, uncommitted, bored, self-aware \u2014 is the archetype of the modern intellectual who substitutes irony for engagement. Its analysis of the rotation method anticipates the cultural logic of consumer capitalism: the perpetual stimulation of new desires to replace old ones, the commodification of experience. The Seducer\u2019s Diary has become the standard philosophical reference for discussions of manipulation, consent, and the objectification of persons. The either/or structure \u2014 the demand for a choice that cannot be rationally adjudicated from outside \u2014 is the foundation of existentialist ethics and of all subsequent discussions of commitment, authenticity, and bad faith.',
    context: 'Published 20 February 1843 by C.A. Reitzel in Copenhagen under the pseudonym Victor Eremita. Kierkegaard had recently broken off his engagement to Regine Olsen \u2014 the most significant event of his personal life and a constant presence in his writing. Either/Or is partly a meditation on the decision to break the engagement and partly an exploration of the aesthetic life he renounced in doing so. The work was an immediate sensation in Copenhagen. Kierkegaard published it at his own expense and supervised every detail of its production. The dedication \u2014 to the memory of his father, Michael Pedersen Kierkegaard \u2014 is the only indication that the author is not Victor Eremita.',
    relatedWorks: ['fear-and-trembling', 'stages-lifes-way', 'concluding-unscientific-postscript', 'sickness-unto-death']
}
);
"""

# ── data-20b: Fear and Trembling + Repetition ────────────────────────────────
files['data-20b.js'] = r"""/* DATA PART 20b — Kierkegaard: Fear and Trembling + Repetition */
window.WORKS.push(

{
    id: 'fear-and-trembling',
    title: 'Fear and Trembling',
    greekTitle: 'Frygt og B\u00e6ven',
    philosopher: 'kierkegaard',
    category: 'practical',
    categoryLabel: 'Philosophy of Religion & Ethics',
    date: '1843 AD',
    dateSort: 1843,
    emoji: '\u2721\uFE0F',
    cardSize: 'wide',
    readingDifficulty: 'Intermediate',
    estimatedWordCount: 50000,
    shortDesc: 'The most sustained philosophical meditation on faith in the modern period \u2014 Kierkegaard\u2019s analysis of Abraham\u2019s binding of Isaac as the paradigm of the \u201cteleological suspension of the ethical,\u201d the moment at which the individual\u2019s absolute relation to God overrides every universal moral demand.',
    summary: 'Fear and Trembling (Frygt og B\u00e6ven), published on 16 October 1843 \u2014 the same day as Repetition \u2014 under the pseudonym Johannes de Silentio (\u201cJohn of Silence\u201d) by C.A. Reitzel in Copenhagen, is Kierkegaard\u2019s most concentrated and most influential single work. Its analysis of faith through the figure of Abraham has become the central philosophical text in the modern philosophy of religion.\n\nThe pseudonym is essential: Johannes de Silentio explicitly confesses that he cannot make the movement of faith, cannot understand Abraham, and writes about faith from the outside. He is the poet of faith, not its practitioner. This is one of Kierkegaard\u2019s characteristic devices: the pseudonym \u2014 who is not Kierkegaard \u2014 presents a position from within its own limitations, leaving the reader to judge what lies beyond.\n\nThe work meditates on the Akedah: God\u2019s command to Abraham to sacrifice his son Isaac (Genesis 22). Hegel had argued that Abraham\u2019s willingness to sacrifice Isaac demonstrated the primitive, pre-ethical nature of the Old Testament God \u2014 the demand to transcend natural love in favor of duty. Kierkegaard inverts this reading: Abraham\u2019s greatness consists precisely in the fact that he is willing to violate the ethical (the universal obligation not to murder one\u2019s child) in obedience to a direct divine command.\n\nThe work\u2019s three central problemata address three questions. First: is there a teleological suspension of the ethical? Yes: Abraham\u2019s action makes sense only if there is a domain \u2014 the religious \u2014 that stands higher than the ethical universal. If ethics is the highest domain, Abraham is a murderer. Second: is there an absolute duty to God? Yes: the absolute relation to God is not mediated by universal ethical categories; it is a direct, personal, and incommunicable relationship. Third: was it ethically defensible for Abraham to conceal his purpose from Sarah, Isaac, and Eliezer? Yes: the knight of faith cannot communicate his faith to others; faith is essentially private and incommunicable.\n\nAgainst the knight of faith, Kierkegaard sets the tragic hero \u2014 Agamemnon, Jephtha, Brutus \u2014 who sacrifices what is dearest to him for the sake of the universal ethical. The tragic hero is comprehensible; the community can grieve with him. Abraham is not comprehensible; he cannot be consoled or pitied; he acts in absolute isolation. This incommunicability is the mark of genuine faith.\n\nThe work also contains the celebrated portrait of the \u201cknight of infinite resignation\u201d versus the \u201cknight of faith.\u201d The knight of infinite resignation renounces the finite entirely, living in the eternal and accepting the loss of what was most dear. The knight of faith makes the movement of infinite resignation and then, \u201cby virtue of the absurd,\u201d expects to receive the finite back again. Abraham is the paradigm: he resigns Isaac completely, and then expects to receive him back. This double movement \u2014 renunciation and reception \u2014 is the structure of faith.',
    themes: ['the teleological suspension of the ethical', 'the Abraham and Isaac narrative', 'the knight of faith vs the tragic hero', 'infinite resignation and faith', 'the absolute relation to God', 'the incommunicability of faith', 'pseudonymous authorship', 'the religious stage', 'the absurd', 'Johannes de Silentio as outside observer'],
    keyCharacters: [
        { name: 'Abraham', role: 'The paradigm of the knight of faith; willing to sacrifice Isaac in obedience to a direct divine command; incomprehensible to ethical reasoning; acts in absolute isolation' },
        { name: 'Johannes de Silentio', role: 'The pseudonymous author; explicitly confesses his inability to make the movement of faith; writes about faith from outside as its poet and admirer' }
    ],
    concepts: [
        'The teleological suspension of the ethical \u2014 the possibility that the ethical universal can be suspended for a higher religious telos; Abraham\u2019s action makes sense only if such suspension is possible',
        'The knight of faith \u2014 the individual who makes the double movement of infinite resignation and then expects the finite back \u201cby virtue of the absurd\u201d; Abraham is the paradigm',
        'The knight of infinite resignation \u2014 the individual who renounces the finite entirely; lives in the eternal; can be understood and admired; but does not make the movement of faith',
        'The absurd \u2014 the category under which the knight of faith expects the impossible; not rational expectation but the complete contrary of reason; faith begins where reason ends',
        'The incommunicability of faith \u2014 Abraham cannot explain himself to Sarah, Isaac, or Eliezer; faith is essentially private and cannot be mediated through universal categories',
        'The absolute duty to God \u2014 the direct, personal, incommunicable relationship between the individual and God that cannot be reduced to any universal ethical obligation',
        'The tragic hero vs the knight of faith \u2014 the tragic hero sacrifices for the universal and is comprehensible; the knight of faith acts in absolute isolation and is incomprehensible'
    ],
    structure: 'Preface by Johannes de Silentio\nExordium: Four retellings of the Abraham and Isaac story\nPreliminary Expectoration: Hegel\u2019s ethics and its limits; the movement of infinite resignation\nProblem I: Is there a teleological suspension of the ethical?\nProblem II: Is there an absolute duty to God?\nProblem III: Was it ethically defensible for Abraham to conceal his purpose?\nEpilogue',
    quote: 'Faith is the highest passion in a human being. Many in every generation may not come that far, but none comes further.',
    additionalQuotes: [
        { text: 'If faith cannot make it a holy act to be willing to murder his son, then let the same condemnation be pronounced upon Abraham as upon every other man. If a person lacks the courage to think this thought through and say that Abraham was a murderer, then it is certainly better to acquire this courage than to waste time on undeserved eulogies.', citation: 'Fear and Trembling, Preliminary Expectoration' },
        { text: 'The knight of faith has the power to concentrate the whole content of life and the meaning of reality into one single wish. If a person lacks this concentration, this focus of the whole of life, then he has never made the movement of infinity.', citation: 'Fear and Trembling, Preliminary Expectoration (paraphrased)' },
        { text: 'The present writer is by no means a philosopher. He has not understood the system, whether there is one, whether it is completed; it is already enough for his weak head to ponder what a prodigious head everyone must have nowadays.', citation: 'Fear and Trembling, Preface' }
    ],
    commentary: [
        { philosopher: 'Emmanuel Levinas', text: 'Levinas\u2019s essay \u201cA Propos of Kierkegaard\u201d and his broader engagement with Fear and Trembling mount the most philosophically rigorous challenge to its central argument. Levinas argues that the teleological suspension of the ethical \u2014 the priority of the absolute relation to God over the ethical relation to other human beings \u2014 is precisely the structure of violence and totalitarianism: the perpetrator who acts \u201cby divine command\u201d against ethical obligations to others. For Levinas, ethics \u2014 the relation to the other\u2019s face \u2014 is first philosophy, not a domain that can be suspended by a higher religious telos.' },
        { philosopher: 'Jacques Derrida', text: 'Derrida\u2019s The Gift of Death (1992; English 1995) is an extended meditation on Fear and Trembling. Derrida argues that Abraham\u2019s situation \u2014 absolute secrecy, absolute responsibility before a singular other, the impossibility of justifying oneself \u2014 is the structure of every ethical decision. Every time I act responsibly toward one person, I sacrifice my responsibilities toward all others. The \u201cteleological suspension of the ethical\u201d is not an exception to ethical life but its everyday structure.' },
        { philosopher: 'Alasdair MacIntyre', text: 'MacIntyre\u2019s Three Rival Versions of Moral Enquiry (1990) treats Fear and Trembling as the paradigm of the fideist position he rejects: the claim that there is a domain of religious obligation that is both absolute and rationally incommunicable is, for MacIntyre, the philosophical expression of the moral relativism he has spent his career opposing. The knight of faith is not a moral ideal but a philosophical catastrophe: the collapse of the rational foundations of ethics.' },
        { philosopher: 'Jon Stewart', text: 'Stewart\u2019s Kierkegaard\u2019s Relations to Hegel Reconsidered (2003) has substantially revised the standard reading of Fear and Trembling as an anti-Hegelian polemic. Stewart argues that Kierkegaard\u2019s target is not Hegel himself but the Hegelian mediocrities of Danish academic theology who had reduced the absolute demand of Christianity to comfortable bourgeois ethics. Hegel\u2019s own account of faith is much more nuanced than Kierkegaard\u2019s polemical target.' }
    ],
    modernRelevance: 'Fear and Trembling is the central text in the modern philosophy of religion and in philosophical discussions of the relationship between faith and ethics. Its analysis of the \u201cteleological suspension of the ethical\u201d has been taken up in debates about divine command theory, religious violence, and the limits of ethical rationalism. Derrida\u2019s development of the Abraham story into a general account of ethical responsibility has been enormously influential in continental ethics and political philosophy. The work is also read as a meditation on the absolute demand of personal commitment \u2014 the moment when one acts on the basis of a conviction that cannot be communicated or rationally justified to others.',
    context: 'Published 16 October 1843 by C.A. Reitzel in Copenhagen under the pseudonym Johannes de Silentio. Published on the same day as Repetition. The work is intimately connected with Kierkegaard\u2019s broken engagement to Regine Olsen: the sacrifice of Isaac is partly a figure for his own sacrifice of Regine, an act he could not explain or justify to others. Kierkegaard described himself as the \u201cpoet of the religious\u201d who writes about faith from outside, unable to make the movement he describes. The standard Danish edition is in Kierkegaard\u2019s Samlede V\u00e6rker; the standard English translation is by Howard and Edna Hong (Princeton, 1983) or Alastair Hannay (Penguin, 1985).',
    relatedWorks: ['either-or', 'concluding-unscientific-postscript', 'sickness-unto-death', 'repetition']
},

{
    id: 'repetition',
    title: 'Repetition: An Essay in Experimental Psychology',
    greekTitle: 'Gjentagelsen: Et Fors\u00f8g i den experimenterende Psychologi',
    philosopher: 'kierkegaard',
    category: 'metaphysics',
    categoryLabel: 'Philosophy & Literature',
    date: '1843 AD',
    dateSort: 1843,
    emoji: '\uD83D\uDD01',
    cardSize: 'normal',
    readingDifficulty: 'Intermediate',
    estimatedWordCount: 35000,
    shortDesc: 'The philosophical category of repetition as the key to existence \u2014 Kierkegaard\u2019s argument that genuine recollection looks backward while genuine hope looks forward, but that repetition \u2014 freely choosing the same \u2014 is the synthesis of both and the only way to receive back what one has lost.',
    summary: 'Repetition: An Essay in Experimental Psychology (Gjentagelsen: Et Fors\u00f8g i den experimenterende Psychologi), published 16 October 1843 under the pseudonym Constantin Constantius by C.A. Reitzel in Copenhagen, is one of Kierkegaard\u2019s most original and most enigmatic works. It introduces the category of repetition \u2014 one of the most important in his entire philosophy \u2014 through a combination of comic narrative, lyric meditation, and philosophical argument.\n\nThe work opens with Constantin Constantius\u2019s attempt to repeat a journey to Berlin that had previously delighted him. The attempt fails: everything is the same and therefore different. The same hotel room, the same theatre, the same people produce boredom rather than pleasure. The first lesson: repetition in the external sense \u2014 the mere recurrence of the same external conditions \u2014 is not genuine repetition.\n\nThe central philosophical claim: repetition is the synthesis of recollection and hope. Recollection is the Greek category of existence \u2014 Plato\u2019s theory that learning is remembering, that truth already exists and must be retrieved. Recollection looks backward. Hope looks forward. But repetition \u2014 the movement by which the individual freely chooses and thus re-creates what already exists \u2014 is the properly modern, Christian category: the freedom to receive the eternal in time, to get back what was lost, not by remembering it but by repeating it.\n\nThe second half of the work contains letters from a young poet, agonised by his relationship with a young woman he loves but cannot marry (clearly a figure for Kierkegaard\u2019s situation with Regine Olsen). The young man finds his resolution in the Book of Job: Job who has lost everything and receives it back \u2014 doubled \u2014 from God. Repetition as the restoration of what was lost is the religious category in its fullest form: not the eternal recurrence of the same (Nietzsche) but the freedom to receive the singular back again from the hand of the absolute.',
    themes: ['repetition as a philosophical category', 'recollection vs repetition', 'the Berlin experiment', 'Job as the knight of repetition', 'freedom and necessity', 'the young poet and the broken engagement', 'the comic and the religious', 'Constantin Constantius as pseudonym'],
    keyCharacters: [
        { name: 'Constantin Constantius', role: 'The pseudonymous author; a cool, detached observer who attempts and fails to repeat a journey to Berlin; he is capable of infinite resignation but not of genuine repetition' },
        { name: 'The Young Poet', role: 'Constantin\u2019s correspondent; in love with a young woman he cannot marry; his resolution through Job is the genuine repetition Constantin cannot achieve' }
    ],
    concepts: [
        'Repetition (Gjentagelse) \u2014 not the mere recurrence of the same external conditions but the free re-creation of what has been; the synthesis of recollection (backward-looking) and hope (forward-looking)',
        'Recollection vs repetition \u2014 recollection (Greek, Platonic) is the backward retrieval of eternal truth; repetition (modern, Christian) is the forward reception of the eternal in time',
        'The Berlin experiment \u2014 Constantin\u2019s failed attempt to repeat a previous journey: everything is the same and therefore different; external repetition is impossible',
        'Job as the paradigm of repetition \u2014 Job loses everything and receives it back doubled; not through recollection but through a direct relationship with God; repetition as divine restoration',
        'The religious as the only true repetition \u2014 genuine repetition requires a relationship with the absolute; it cannot be achieved through human will alone'
    ],
    structure: 'Part One: Constantin Constantius\u2019s narrative\n\u2014 The theory of repetition vs recollection\n\u2014 The Berlin journey and its failure\n\u2014 The young man\u2019s situation\n\nPart Two: Letters from the young man to Constantin\n\u2014 The young man\u2019s meditation on Job\n\u2014 Resolution through the Book of Job\n\u2014 Constantin\u2019s response and reflection',
    quote: 'Repetition and recollection are the same movement, only in opposite directions; for what is recollected has been, is repeated backwards, whereas repetition properly so called is recollected forwards.',
    additionalQuotes: [
        { text: 'If God himself had not willed repetition, the world would never have come into being. He would either have followed the light plans of hope, or he would have recalled it all and conserved it in recollection.', citation: 'Repetition, Part II' }
    ],
    commentary: [
        { philosopher: 'Gilles Deleuze', text: 'Deleuze\u2019s Difference and Repetition (1968; English 1994) takes Kierkegaard\u2019s concept of repetition as one of its two primary starting points (the other being Nietzsche\u2019s eternal recurrence). Deleuze argues that genuine repetition \u2014 the repetition that produces difference rather than the same \u2014 is the key to overcoming the Platonic tradition of representation. Kierkegaard\u2019s repetition is superior to Platonic recollection because it introduces temporality, freedom, and singularity into the concept of truth.' },
        { philosopher: 'Walter Lowrie', text: 'Lowrie\u2019s biography Kierkegaard (1938) first drew attention to the autobiographical dimension of Repetition: Constantin Constantius is Kierkegaard, the young poet is Kierkegaard, the young woman is Regine Olsen, and the resolution through Job is Kierkegaard\u2019s attempt to understand and justify his breaking of the engagement.' }
    ],
    modernRelevance: 'Repetition is important primarily as the source of the philosophical category of repetition, which has been enormously productive in twentieth-century thought. Deleuze\u2019s Difference and Repetition is its most consequential development. The concept of repetition as free re-creation rather than mere recurrence has influenced literary theory (the repetition of narrative forms), psychoanalysis (Freud\u2019s repetition compulsion as its pathological form), and the philosophy of time.',
    context: 'Published 16 October 1843 by C.A. Reitzel in Copenhagen under the pseudonym Constantin Constantius, simultaneously with Fear and Trembling. The work was substantially revised in proof when Kierkegaard learned that Regine Olsen had become engaged to someone else: the ending was changed from the young man\u2019s dissolution of his relationship through Job to a more genuinely philosophical resolution. The standard English translation is by Howard and Edna Hong (Princeton, 1983).',
    relatedWorks: ['fear-and-trembling', 'either-or', 'concluding-unscientific-postscript', 'stages-lifes-way']
}

);
"""

# ── data-20c: Philosophical Fragments + Concept of Anxiety ───────────────────
files['data-20c.js'] = r"""/* DATA PART 20c — Kierkegaard: Philosophical Fragments + The Concept of Anxiety */
window.WORKS.push(

{
    id: 'philosophical-fragments',
    title: 'Philosophical Fragments',
    greekTitle: 'Philosophiske Smuler',
    philosopher: 'kierkegaard',
    category: 'metaphysics',
    categoryLabel: 'Epistemology & Philosophy of Religion',
    date: '1844 AD',
    dateSort: 1844,
    emoji: '\u2734\uFE0F',
    cardSize: 'normal',
    readingDifficulty: 'Advanced',
    estimatedWordCount: 40000,
    shortDesc: 'The most philosophically precise of Kierkegaard\u2019s pseudonymous works \u2014 a compressed interrogation of the relationship between time and eternity, asking what it means to base one\u2019s eternal happiness on a historical fact and contrasting the Socratic ideal of recollection with the Christian claim that the moment of encounter with the God-in-time is decisive.',
    summary: 'Philosophical Fragments, or a Fragment of Philosophy (Philosophiske Smuler eller en Smule Philosophi), published 13 June 1844 under the pseudonym Johannes Climacus (\u201cJohn of the Ladder\u201d) by C.A. Reitzel in Copenhagen, is Kierkegaard\u2019s most philosophically precise and most analytically rigorous work. Johannes Climacus is the most important of Kierkegaard\u2019s pseudonyms: an intellectual who thinks through the philosophical presuppositions of Christianity without believing it.\n\nThe work\u2019s central question, stated in the opening lines: can the truth be learned? The Socratic answer: no \u2014 the truth is already within the learner; teaching is merely the occasion for remembering what one already knows. The teacher is accidental; the moment of encounter is replaceable; recollection is the mechanism.\n\nKierkegaard proposes a thought-experiment: suppose the opposite were true. Suppose the learner is not merely ignorant but in error; suppose the truth is not already within but must be given from outside; suppose the moment of encounter is not replaceable but absolutely decisive. Then the teacher must be not merely an occasion but a saviour; the moment of encounter is \u201cthe Fullness of Time\u201d; and the relationship between learner and teacher is not one of intellectual midwifery but of transformation \u2014 the gift of the condition for understanding along with the content to be understood.\n\nThis thought-experiment, as the reader immediately recognises, describes the structure of Christianity: God becoming human (the Incarnation) as the teacher who gives not merely information but the condition for receiving it. The question that organises the rest of the work: what is the relationship between this historical fact and eternal happiness? How can a temporal, contingent fact \u2014 that God appeared in human form at a specific moment in history \u2014 be the basis of an eternal relationship? This is the problem that the Concluding Unscientific Postscript will develop at enormous length.',
    themes: ['the Socratic paradox of learning', 'recollection vs the moment', 'the Incarnation as philosophical problem', 'the teacher who gives the condition', 'the absolute paradox', 'the offence of the Incarnation', 'contemporaneity with Christ', 'the happy passion', 'Johannes Climacus'],
    keyCharacters: [
        { name: 'Johannes Climacus', role: 'The pseudonymous author; a thinker who examines the philosophical presuppositions of Christianity without committing to it; the ironist who thinks through what it would mean to be a Christian' }
    ],
    concepts: [
        'The Socratic position \u2014 the truth is already within the learner; teaching is recollection; the teacher and the moment of encounter are accidental; the eternal truth is timelessly available',
        'The alternative position (Christianity) \u2014 the learner is in error and needs not only information but the condition for receiving it; the teacher must give both content and capacity; the moment is absolutely decisive',
        'The absolute paradox \u2014 the claim that the eternal, infinite God appeared in finite, temporal human form; the highest expression of the paradoxical; it cannot be understood rationally but must be either believed or found offensive',
        'The Fullness of Time \u2014 the moment at which the eternal enters time; for the believer, the absolutely decisive moment; for the Socratic thinker, a logical impossibility',
        'Contemporaneity \u2014 the question of whether those who live after the Incarnation are at a disadvantage compared to contemporaries of Christ; Kierkegaard\u2019s answer: no, because faith is not based on historical proximity but on the absolute paradox',
        'The happy passion \u2014 faith as the highest passion; the relationship to the absolute paradox that is neither understanding nor offence'
    ],
    structure: 'Preface by Johannes Climacus\nChapter 1: The Thought-Project (recollection vs the moment)\nChapter 2: The God as Teacher and Saviour (a poetical venture)\nChapter 3: The Absolute Paradox: A Metaphysical Caprice\nInterlude: Is the Past More Necessary Than the Future? (on historical knowledge)\nChapter 4: The Case of the Contemporary Disciple\nChapter 5: The Disciple at Second Hand\nAppendix: For an Upbuilding Consideration',
    quote: 'The supreme paradox of all thought is the attempt to discover something that thought cannot think.',
    additionalQuotes: [
        { text: 'How far does the Truth admit of being learned? With this question let us begin.', citation: 'Philosophical Fragments, Chapter 1' }
    ],
    commentary: [
        { philosopher: 'G.E. Lessing', text: 'Lessing\u2019s \u201cOn the Proof of the Spirit and of Power\u201d (1777) is the explicit starting point for Philosophical Fragments and the Concluding Unscientific Postscript. Lessing\u2019s \u201cditch\u201d \u2014 the \u201cugly broad ditch\u201d between contingent historical truths and necessary rational truths, which he confessed he could not cross \u2014 is the problem Kierkegaard is addressing. For Kierkegaard, Lessing had correctly identified the problem but drawn the wrong conclusion: the ditch is precisely where faith is required, and to want to cross it by means of historical evidence or rational argument is to misunderstand what faith is.' },
        { philosopher: 'Rudolf Bultmann', text: 'Bultmann\u2019s demythologisation programme in twentieth-century Protestant theology is partly a response to the problem Kierkegaard poses in Philosophical Fragments: how can a contingent historical event be the basis of eternal significance? Bultmann\u2019s answer \u2014 the kerygma, not the historical Jesus \u2014 is one solution; Kierkegaard\u2019s own answer \u2014 the absolute paradox, believed by virtue of the absurd \u2014 is another.' }
    ],
    modernRelevance: 'Philosophical Fragments is important in the philosophy of religion as the most precise philosophical analysis of the relationship between historical knowledge and religious faith. The \u201cLessing\u2019s ditch\u201d problem \u2014 how can a contingent historical fact ground an eternal commitment? \u2014 remains the central problem in philosophical theology. Kierkegaard\u2019s answer \u2014 that faith requires the absolute paradox and cannot be grounded in historical evidence \u2014 is the starting point for Barth\u2019s neo-orthodox theology and for all subsequent discussions of the relationship between faith and history.',
    context: 'Published 13 June 1844 by C.A. Reitzel in Copenhagen under the pseudonym Johannes Climacus. The title\u2019s ironic modesty \u2014 \u201cphilosophical fragments\u201d, \u201ca fragment of philosophy\u201d \u2014 is characteristic of Kierkegaard\u2019s indirect method: the most compact and precise statement of the philosophical problem of Christianity presented as a minor, provisional sketch. The Concluding Unscientific Postscript (1846) was conceived as a mere supplement to the Fragments, but grew to seven times its length.',
    relatedWorks: ['concluding-unscientific-postscript', 'concept-of-anxiety', 'fear-and-trembling', 'sickness-unto-death']
},

{
    id: 'concept-of-anxiety',
    title: 'The Concept of Anxiety',
    greekTitle: 'Begrebet Angest',
    philosopher: 'kierkegaard',
    category: 'metaphysics',
    categoryLabel: 'Psychology & Existential Philosophy',
    date: '1844 AD',
    dateSort: 1844,
    emoji: '\uD83C\uDF2A\uFE0F',
    cardSize: 'wide',
    readingDifficulty: 'Advanced',
    estimatedWordCount: 65000,
    shortDesc: 'The founding text of existential psychology \u2014 Kierkegaard\u2019s analysis of anxiety (Angest) as the \u201cdizziness of freedom,\u201d the mood that arises when the self confronts its own infinite possibility, and the condition for both sin and genuine selfhood.',
    summary: 'The Concept of Anxiety: A Simple Psychologically Orienting Deliberation on the Dogmatic Issue of Hereditary Sin (Begrebet Angest: En simpel psychologisk-paapegende Overveielse i Retning af det dogmatiske Problem om Arvesynden), published 17 June 1844 under the pseudonym Vigilius Haufniensis (\u201cWatchman of Copenhagen\u201d) by C.A. Reitzel in Copenhagen, is the most philosophically original contribution to the psychology of religion in the nineteenth century. It is the text that most directly anticipates Heidegger\u2019s existential analysis and the existentialist tradition.\n\nThe work\u2019s subject is anxiety (Angest) as a fundamental existential category, distinct from fear. Fear has an object: I am afraid of this or that specific thing. Anxiety has no object: it is the mood that arises when the self confronts its own freedom \u2014 the vertiginous recognition that it can become anything, that possibility opens in every direction without determination. Anxiety is \u201cthe dizziness of freedom.\u201d\n\nKierkegaard approaches this through a psychological analysis of the Genesis narrative. Before the fall, Adam is in a state of innocence that is also ignorance: he does not know what sin is, does not know that the prohibition could be violated, does not know himself as a free being who can choose. But precisely this ignorance generates anxiety: the prohibition awakens the possibility of transgression that Adam did not know existed. This anxious possibility is what propels the fall: Adam does not fall from sin but into sin through anxiety. \u201cAnxiety is the possibility of freedom.\u201d\n\nThe work develops through a systematic analysis of the forms of anxiety: anxiety about evil (the anxiety of the spirit that has not yet committed to the good), anxiety about the good (demonic anxiety \u2014 the retreat into unfreedom as a way of avoiding the demand of the good), and the anxiety of freedom in its most developed form (the anxiety of the spirit that has genuinely confronted its own infinity). The final chapter argues that anxiety, properly understood, is not merely a psychological problem but a condition for genuine religious selfhood: the individual who has passed through anxiety \u2014 who has allowed anxiety to educate them \u2014 is prepared for the encounter with the absolute.',
    themes: ['anxiety vs fear', 'the dizziness of freedom', 'innocence and ignorance', 'the psychological presuppositions of original sin', 'the demonic', 'the educative function of anxiety', 'possibility and actuality', 'spirit and selfhood', 'hereditary sin', 'Vigilius Haufniensis'],
    keyCharacters: [
        { name: 'Vigilius Haufniensis', role: 'The pseudonymous author; a \u201cwatchman\u201d who examines anxiety from a psychological standpoint that is oriented toward but does not enter dogmatic theology' }
    ],
    concepts: [
        'Anxiety (Angest) \u2014 the mood that arises when the self confronts its own freedom; distinct from fear (which has a specific object); the dizziness of freedom',
        'The dizziness of freedom \u2014 anxiety is like looking down into a yawning abyss: not the abyss outside but the abyss within, the infinite possibility that one is',
        'Innocence as ignorance \u2014 Adam before the fall is innocent because he is ignorant of the prohibition\u2019s meaning; but this ignorance generates anxiety: the prohibition awakens possibility',
        'Anxiety and the fall \u2014 Adam does not fall from sin into anxiety but through anxiety into sin; anxiety is the psychological condition (not cause) of the fall',
        'The demonic \u2014 the form of anxiety about the good: the retreat into the enclosedness of unfreedom to avoid the demand of the spirit; stubbornness as the demonic\u2019s most common form',
        'Anxiety as educator \u2014 the individual who passes through anxiety honestly \u2014 who allows it to disclose the infinite possibility of the self \u2014 is educated for genuine freedom and religious selfhood',
        'Possibility and actuality \u2014 anxiety arises at the intersection of possibility and actuality: the self is actual but opens onto infinite possibility; it is this opening that produces the vertiginous anxiety'
    ],
    structure: 'Introduction: The concept of hereditary sin in dogmatics; the task of psychology\n\nChapter 1: Anxiety as the Presupposition of Hereditary Sin and as Explaining Hereditary Sin Retrogressively in Terms of Its Origin\nChapter 2: Anxiety of the Spirit (the forms of anxiety about evil)\nChapter 3: Anxiety as the Consequence of That Sin Which Is the Absence of the Consciousness of Sin (objective anxiety; anxiety in the pagan world)\nChapter 4: Anxiety of Sin, or Anxiety as the Consequence of Sin in the Single Individual\nChapter 5: Anxiety as Saving through Faith (the educative function of anxiety)',
    quote: 'Anxiety is the dizziness of freedom, which emerges as freedom gazes down into its own possibility, laying hold of finiteness to support itself.',
    additionalQuotes: [
        { text: 'Whoever has learned to be anxious in the right way has learned the ultimate.', citation: 'The Concept of Anxiety, Chapter 5' },
        { text: 'In anxiety, there is the selfish infinity of possibility, which does not tempt like a definite choice but, with its sweet anxiousness, alarms.', citation: 'The Concept of Anxiety, Chapter 1 (paraphrased)' }
    ],
    commentary: [
        { philosopher: 'Martin Heidegger', text: 'Heidegger\u2019s analysis of Angst in Being and Time (1927) is the most consequential development of Kierkegaard\u2019s concept of anxiety. Heidegger strips the concept of its theological and psychological context and makes it an ontological category: anxiety is the mood that discloses Dasein\u2019s ownmost possibility \u2014 death \u2014 and thereby individualises it from its fallenness in the they-self. The dizziness of freedom becomes the ownmost possibility of Being-toward-death. Heidegger acknowledged Kierkegaard in a famous footnote as the philosopher who had seen furthest into the phenomenon of anxiety, while insisting that his own analysis was ontological rather than psychological.' },
        { philosopher: 'Paul Tillich', text: 'Tillich\u2019s The Courage to Be (1952) develops the concept of anxiety into a theology of courage. Tillich identifies three forms of existential anxiety \u2014 anxiety of fate and death, anxiety of emptiness and meaninglessness, anxiety of guilt and condemnation \u2014 and argues that genuine courage consists in affirming the self in spite of anxiety, in the face of non-being. The theological dimension \u2014 God as the ground of being in whom the courage to be is rooted \u2014 is Tillich\u2019s development of Kierkegaard\u2019s educative function of anxiety.' },
        { philosopher: 'Rollo May', text: 'May\u2019s The Meaning of Anxiety (1950) is the most important clinical and philosophical appropriation of Kierkegaard\u2019s concept of anxiety. May argued that Kierkegaard had anticipated the most important insights of clinical psychology about neurotic and normal anxiety a century before they were established by empirical research. The distinction between normal anxiety (the appropriate response to genuine threat and genuine possibility) and neurotic anxiety (the displacement of normal anxiety into symptomatic behaviour) is a clinical development of Kierkegaard\u2019s distinction between educative and debilitating anxiety.' }
    ],
    modernRelevance: 'The Concept of Anxiety is the founding text of existential psychology and existential philosophy. Heidegger\u2019s Angst, Sartre\u2019s nausea and bad faith, Tillich\u2019s courage, and clinical existential psychology all derive from Kierkegaard\u2019s analysis. The concept of anxiety as the mood that discloses freedom \u2014 the dizziness of the self confronting its own infinite possibility \u2014 has become a standard category in philosophy, psychology, and cultural theory. Contemporary anxiety studies, attachment theory, and the psychology of uncertainty all engage with the conceptual framework Kierkegaard established.',
    context: 'Published 17 June 1844 by C.A. Reitzel in Copenhagen under the pseudonym Vigilius Haufniensis. Published four days after Philosophical Fragments. The two works were written simultaneously and represent complementary approaches to the same problem: Philosophical Fragments addresses the epistemological problem of faith (how can a historical fact ground eternal happiness?); The Concept of Anxiety addresses the psychological and anthropological presuppositions of sin and faith. Standard English translation by Reidar Thomte (Princeton, 1980).',
    relatedWorks: ['sickness-unto-death', 'philosophical-fragments', 'concluding-unscientific-postscript', 'fear-and-trembling']
}

);
"""

# ── data-20d: Concluding Unscientific Postscript + Stages ────────────────────
files['data-20d.js'] = r"""/* DATA PART 20d — Kierkegaard: Concluding Unscientific Postscript + Stages on Life's Way */
window.WORKS.push(

{
    id: 'concluding-unscientific-postscript',
    title: 'Concluding Unscientific Postscript to Philosophical Fragments',
    greekTitle: 'Afsluttende uvidenskabelig Efterskrift til de Philosophiske Smuler',
    philosopher: 'kierkegaard',
    category: 'metaphysics',
    categoryLabel: 'Epistemology & Philosophy of Religion',
    date: '1846 AD',
    dateSort: 1846,
    emoji: '\uD83D\uDCCC',
    cardSize: 'wide',
    readingDifficulty: 'Advanced',
    estimatedWordCount: 300000,
    shortDesc: 'The pseudonymous masterpiece of existentialist philosophy \u2014 Kierkegaard\u2019s most extensive philosophical work, developing the concept of subjective truth (\u201ctruth is subjectivity\u201d), the three stages of existence, the concept of indirect communication, and the critique of Hegelian speculative philosophy as the central obstacle to genuine Christian existence.',
    summary: 'Concluding Unscientific Postscript to Philosophical Fragments: A Mimical-Pathetical-Dialectical Compilation, an Existential Contribution (Afsluttende uvidenskabelig Efterskrift til de Philosophiske Smuler), published 28 February 1846 under the pseudonym Johannes Climacus (with Kierkegaard named on the title page as editor) by C.A. Reitzel in Copenhagen, is the longest, most ambitious, and most philosophically comprehensive of Kierkegaard\u2019s works. It was conceived as a mere appendix to Philosophical Fragments \u2014 hence the title \u2014 but grew to seven times its length.\n\nThe work\u2019s central question is the same as Philosophical Fragments\u2019 but pursued at vastly greater depth: how can I, Johannes Climacus, a thinker in the nineteenth century, acquire an eternal happiness that is based on a contingent historical fact \u2014 namely, the Incarnation? This is Lessing\u2019s problem, stated with maximum precision: how can the \u201cugly broad ditch\u201d between historical contingency and eternal significance be crossed?\n\nThe answer involves the concept of subjective truth \u2014 the most discussed and most misunderstood concept in Kierkegaard\u2019s philosophy. The formula \u201ctruth is subjectivity\u201d does not mean that truth is whatever the individual believes. It means that certain kinds of truth \u2014 specifically, those that bear on existence, commitment, and the meaning of one\u2019s life \u2014 can only be appropriated through a kind of inner transformation, a passionate personal commitment. The opposite \u2014 objective truth \u2014 is the truth of science, mathematics, and history: indifferent to the knower, communicable to anyone, indifferent to whether it is personally appropriated. Subjective truth is the opposite: it demands infinite passion, personal risk, and the willingness to act on uncertainty.\n\nThis leads to the celebrated formula: \u201cSubjectivity is truth; subjectivity is reality.\u201d Even more provocatively: \u201cAn objective uncertainty held fast in an appropriation-process of the most passionate inwardness is the truth, the highest truth attainable for an existing individual.\u201d Faith is not the possession of certainty but the passionate holding of objective uncertainty.\n\nThe Postscript also develops the three stages of existence more fully than any other work: the aesthetic (immediacy, finite ends, the avoidance of boredom), the ethical (the universal, self-choice, duty), and the religious (the absolute relation to the absolute, faith, infinite passion for the eternal). These are not stages through which one automatically progresses but modes of existence between which the individual must choose \u2014 and the transition from each to the next requires a qualitative leap that reason cannot compel.',
    themes: ['subjectivity as truth', 'objective vs subjective thinking', 'the three stages of existence', 'the leap of faith', 'indirect communication', 'the critique of Hegel', 'Lessing\u2019s ditch', 'existential pathos', 'the comic and the tragic', 'Johannes Climacus', 'becoming a Christian in Christendom'],
    keyCharacters: [
        { name: 'Johannes Climacus', role: 'The pseudonymous author; the most developed of Kierkegaard\u2019s pseudonyms; a thinker who examines the philosophical conditions for becoming a Christian without committing to Christianity' }
    ],
    concepts: [
        'Subjectivity is truth \u2014 certain truths (those bearing on existence and commitment) can only be appropriated through passionate personal engagement; the formula does not mean truth is arbitrary',
        'Objective uncertainty held fast in passionate inwardness \u2014 the definition of faith: not the possession of certainty but the passionate commitment to objective uncertainty',
        'The three stages of existence \u2014 the aesthetic (immediacy), the ethical (the universal), and the religious (the absolute relation to the absolute); not a developmental progression but modes between which one must choose',
        'The qualitative leap \u2014 the transition from one stage to another cannot be accomplished by reason or gradual development; it requires a leap that reason cannot compel',
        'Indirect communication \u2014 existential truths cannot be directly communicated because appropriation requires the recipient\u2019s own passionate engagement; they must be communicated through ambiguity, irony, and pseudonymity',
        'The critique of Hegel \u2014 Hegelian speculative philosophy dissolves the existing individual into the system; the Postscript\u2019s most sustained target is the claim to comprehend existence from the standpoint of the Absolute',
        'Becoming a Christian \u2014 the Postscript\u2019s practical question: how does one become a Christian when one already lives in a nominally Christian society? The answer: the task is infinitely more difficult, not easier, in Christendom'
    ],
    structure: 'Introduction: The objective problem concerning the truth of Christianity\n\nPart One: The Objective Problem Concerning the Truth of Christianity\n\u2014 Section 1: The historical point of view\n\u2014 Section 2: The speculative point of view\n\nPart Two: The Subjective Problem\n\u2014 Section 1: Something About Lessing\n\u2014 Section 2: The Subjective Issue or How Subjectivity Must be Constituted in Order that the Problem May Appear to It\n  \u2014 Chapter 1: Becoming Subjective\n  \u2014 Chapter 2: Subjective Truth, Inwardness; Truth is Subjectivity\n  \u2014 Chapter 3: Actual Subjectivity, Ethical Subjectivity; the Subjective Thinker\n  \u2014 Chapter 4: The Problem of the Stages on Existence\u2019s Way\n\u2014 Section 3: The Issue in Fragments: How Can an Eternal Happiness Be Built upon Historical Knowledge?\n\nConclusion and First and Last Declaration (Kierkegaard reveals himself as author of the pseudonymous works)',
    quote: 'The most tremendous thing which has been granted to man is the choice, freedom. And if you desire to save it and keep it, there is only one way: in the very same second unconditionally and in complete resignation to give it back to God, and yourself with it.',
    additionalQuotes: [
        { text: 'Subjectivity is truth. Subjectivity is reality.', citation: 'Concluding Unscientific Postscript, Part Two, Section 2, Chapter 2' },
        { text: 'If I am capable of grasping God objectively, I do not believe, but precisely because I cannot do this I must believe.', citation: 'Concluding Unscientific Postscript, Part Two, Section 2, Chapter 2' },
        { text: 'Christianity did not come into the world as a showy diversion for bored spirits, but as the absolute decision.', citation: 'Concluding Unscientific Postscript, Part Two, Section 3' }
    ],
    commentary: [
        { philosopher: 'Karl Barth', text: 'Barth\u2019s neo-orthodox theology, beginning with the second edition of his Commentary on Romans (1922), is saturated with Kierkegaardian themes drawn from the Postscript: the \u201cinfinite qualitative difference\u201d between God and man; the impossibility of approaching God through human reason or culture; the absolute paradox of the Incarnation; the necessity of faith as the only mode of access to divine truth. Barth acknowledged Kierkegaard as the \u201cfierce \u2018jaundiced\u2019 prophet\u201d who had demolished liberal theology\u2019s complacency.' },
        { philosopher: 'Martin Heidegger', text: 'Heidegger\u2019s Being and Time (1927) is the primary philosophical development of the existential categories introduced in the Postscript. The analysis of existence as always already \u201cmine,\u201d the concept of Dasein as the being for whom its own being is an issue, the distinction between authentic and inauthentic existence, and the analysis of the they-self (das Man) as the flight from the demands of ownmost existence are all developments of Kierkegaard\u2019s analysis of the aesthetic and ethical stages.' },
        { philosopher: 'Alvin Plantinga', text: 'Plantinga\u2019s reformed epistemology \u2014 the argument that belief in God can be \u201cproperly basic,\u201d not derived from evidence or argument \u2014 is partly a development of the Postscript\u2019s analysis of faith as the passionate holding of objective uncertainty. The claim that religious belief does not require rational justification in order to be epistemically warranted is the epistemological dimension of Kierkegaard\u2019s concept of subjective truth.' }
    ],
    modernRelevance: 'The Concluding Unscientific Postscript is the primary text of existentialism as a philosophical movement. Its analysis of subjective truth, authentic existence, and the three stages of existence is the foundation of Heidegger\u2019s fundamental ontology, Sartre\u2019s analysis of bad faith and authentic choice, Jaspers\u2019s boundary situations, and Tillich\u2019s theology of ultimate concern. The concept of indirect communication \u2014 the claim that existential truths cannot be directly taught but must be appropriated through personal engagement \u2014 has influenced pedagogy, rhetoric, and philosophy of language. The critique of Hegel\u2019s speculative philosophy as the great obstacle to genuine existence remains the foundational text for all existentialist critiques of systematic philosophy.',
    context: 'Published 28 February 1846 by C.A. Reitzel in Copenhagen. The First and Last Declaration at the end of the work \u2014 in which Kierkegaard reveals himself as the author of all the pseudonymous works \u2014 was Kierkegaard\u2019s intention to retire from authorship. The Corsair affair (the satirical magazine\u2019s months-long attack on Kierkegaard following his provocation of its editor) changed his mind. Standard English translation by Howard and Edna Hong (Princeton, 1992).',
    relatedWorks: ['philosophical-fragments', 'either-or', 'sickness-unto-death', 'stages-lifes-way']
},

{
    id: 'stages-lifes-way',
    title: 'Stages on Life\u2019s Way',
    greekTitle: 'Stadier paa Livets Vei',
    philosopher: 'kierkegaard',
    category: 'aesthetics',
    categoryLabel: 'Philosophy & Literature',
    date: '1845 AD',
    dateSort: 1845,
    emoji: '\uD83D\uDEE3\uFE0F',
    cardSize: 'normal',
    readingDifficulty: 'Intermediate',
    estimatedWordCount: 180000,
    shortDesc: 'The most literarily complex of Kierkegaard\u2019s works \u2014 three elaborately framed explorations of the aesthetic, ethical, and religious stages through a banquet discussion of erotic love, Judge William\u2019s defence of marriage, and \u201cGuilty/Not Guilty,\u201d the most autobiographical of the pseudonymous writings.',
    summary: 'Stages on Life\u2019s Way (Stadier paa Livets Vei), published 30 April 1845 under the editorship of the pseudonym Hilarius Bookbinder by C.A. Reitzel in Copenhagen, is the most architecturally elaborate and most literarily complex of Kierkegaard\u2019s works. It is divided into three parts, each representing one of the three stages of existence \u2014 aesthetic, ethical, and religious \u2014 through a different literary form and pseudonymous voice.\n\nPart One, \u201cIn Vino Veritas: A Recollection\u201d (in wine there is truth), is framed as an account of a banquet gathered by William Afham in a forest at night. Five speakers give speeches on woman and erotic love: a Young Man (in the manner of Plato\u2019s Symposium), Constantin Constantius (from Repetition), Victor Eremita (from Either/Or), the Ladies\u2019 Tailor, and Johannes the Seducer (from Either/Or\u2019s Seducer\u2019s Diary). The banquet ends at dawn; the guests scatter as Judge William and his wife appear on their morning walk.\n\nPart Two, \u201cVariations on the Theme of Marriage: Moral Reflections on Marriage Against the Sophistical Objections of Theophrastus\u201d, is Judge William\u2019s long defence of conjugal love against the aesthete\u2019s objections. The Judge argues that conjugal love is not the diminishment of erotic passion but its highest realisation: the daily renewal of commitment transforms first love into something richer and more enduring.\n\nPart Three, \u201cGuilty?/Not Guilty? A Story of Suffering,\u201d is the most personal and most disturbing section. Written under the pseudonym Frater Taciturnus (\u201cthe Silent Brother\u201d), it consists of the diary of Quidam (\u201cSomewhat\u201d) interleaved with Frater Taciturnus\u2019s reflections. Quidam is in an impossible situation: he loves a young woman but cannot marry her because of some unspecified inner burden (clearly a figure for Kierkegaard\u2019s broken engagement to Regine Olsen and the melancholy he could not share with her). The question \u2014 is Quidam guilty or not guilty? \u2014 is left deliberately unanswered: it points toward the religious stage in which guilt and innocence are finally reckoned.',
    themes: ['the three stages through literary form', 'the banquet and erotic love', 'conjugal love vs erotic passion', 'Guilty/Not Guilty and the broken engagement', 'melancholy and the inability to communicate', 'the religious stage as the resolution of guilt', 'elaborated pseudonymity', 'the Symposium as model'],
    keyCharacters: [
        { name: 'Frater Taciturnus', role: 'The pseudonymous editor of Part Three; his silence and his reflection on Quidam\u2019s situation point toward the religious stage that is beyond the work\u2019s direct presentation' },
        { name: 'Quidam', role: 'The diarist of Part Three; in an impossible relationship; unable to share his inner burden; guilty and not guilty; a figure for Kierkegaard\u2019s own situation with Regine Olsen' }
    ],
    concepts: [
        'The three stages through literary form \u2014 aesthetic (the banquet; erotic love), ethical (the Judge\u2019s defence of marriage), religious (Quidam\u2019s diary; guilt and the absolute)',
        'Conjugal love as the highest form of erotic love \u2014 Judge William\u2019s argument: marriage does not diminish passion but transforms it through repeated free choice into something more enduring',
        'The impossible situation \u2014 Quidam\u2019s predicament: loving someone but being unable to share the inner burden that makes marriage impossible; the ethical demand that cannot be met without the religious resolution',
        'The border between the ethical and the religious \u2014 the work ends at the threshold of the religious stage without crossing it; Quidam\u2019s situation requires more than ethics can provide'
    ],
    structure: 'Editor\u2019s Preface by Hilarius Bookbinder\n\nPart One: In Vino Veritas (A Recollection by William Afham)\n\u2014 Five speeches on woman and love; the banquet\n\nPart Two: Variations on the Theme of Marriage (Judge William\u2019s essay)\n\nPart Three: Guilty?/Not Guilty? (Edited by Frater Taciturnus)\n\u2014 Quidam\u2019s diary (entries at midnight and at 5 AM)\n\u2014 Frater Taciturnus\u2019s \u201cLetter to the Reader\u201d',
    quote: 'It is the duty of the human understanding to understand that there are things which it cannot understand, and what those things are. Human understanding has vulgarly occupied itself with nothing but understanding, but if it would only take the trouble to understand itself at the same time it would simply have to posit the paradox.',
    additionalQuotes: [
        { text: 'In relation to their systems, most systematisers are like a man who builds an enormous castle and lives in a shack next to it; they do not live in their own enormous systematic building.', citation: 'Stages on Life\u2019s Way, Part Three, Frater Taciturnus\u2019s Letter (paraphrased from the Journals)' }
    ],
    commentary: [
        { philosopher: 'Louis Mackey', text: 'Mackey\u2019s Kierkegaard: A Kind of Poet (1971) provides the most sustained literary analysis of Stages on Life\u2019s Way, arguing that its extraordinary architectural complexity \u2014 the nested pseudonyms, the intersecting literary forms, the structural echoes between the three parts \u2014 is not decorative but philosophical: the literary form is the philosophical content, enacting the impossibility of direct communication between the stages.' }
    ],
    modernRelevance: 'Stages on Life\u2019s Way is important primarily as the fullest literary elaboration of the three stages and as the most autobiographically revealing of the pseudonymous works. The \u201cGuilty?/Not Guilty?\u201d section has been read by Kierkegaard\u2019s biographers as the closest he comes to explaining his broken engagement to Regine Olsen. The banquet scene in Part One has been compared to Plato\u2019s Symposium and stands alongside it as one of the great literary performances in philosophical literature.',
    context: 'Published 30 April 1845 by C.A. Reitzel in Copenhagen under the pseudonym Hilarius Bookbinder. Written during the most intensely productive period of Kierkegaard\u2019s authorship, alongside the Postscript. Standard English translation by Howard and Edna Hong (Princeton, 1988).',
    relatedWorks: ['either-or', 'concluding-unscientific-postscript', 'fear-and-trembling', 'repetition']
}

);
"""

# ── data-20e: Sickness Unto Death + Works of Love + Attack upon Christendom ──
files['data-20e.js'] = r"""/* DATA PART 20e — Kierkegaard: The Sickness Unto Death + Works of Love + Attack upon Christendom */
window.WORKS.push(

{
    id: 'sickness-unto-death',
    title: 'The Sickness Unto Death',
    greekTitle: 'Sygdommen til D\u00f8den',
    philosopher: 'kierkegaard',
    category: 'metaphysics',
    categoryLabel: 'Psychology & Philosophy of Religion',
    date: '1849 AD',
    dateSort: 1849,
    emoji: '\u2620\uFE0F',
    cardSize: 'wide',
    readingDifficulty: 'Advanced',
    estimatedWordCount: 65000,
    shortDesc: 'The most searching analysis of the human condition in modern philosophy \u2014 Kierkegaard\u2019s account of despair as the universal human sickness, the failure to be oneself before God, and the categories of consciousness and selfhood that determine the depth of one\u2019s despair and the possibility of genuine faith.',
    summary: 'The Sickness Unto Death: A Christian Psychological Exposition for Upbuilding and Awakening (Sygdommen til D\u00f8den: En christelig psychologisk Udvikling til Opbyggelse og Opv\u00e6kkelse), published 30 July 1849 under the pseudonym Anti-Climacus (with Kierkegaard named as editor) by C.A. Reitzel in Copenhagen, is the most concentrated and most psychologically penetrating of Kierkegaard\u2019s works. Anti-Climacus is the inverse of Johannes Climacus: where Climacus examines Christianity from outside without claiming to be a Christian, Anti-Climacus writes as a Christian of extraordinary intensity, from a position Kierkegaard himself considers too high for his own spiritual condition.\n\nThe work opens with one of the most analysed passages in modern philosophy: the definition of the self. \u201cA human being is spirit. But what is spirit? Spirit is the self. But what is the self? The self is a relation that relates itself to itself.\u201d The self is not a simple substance but a structure of relations: it is constituted by the relation between finite and infinite, temporal and eternal, freedom and necessity. But it is not merely a relation \u2014 it is a relation that relates to itself, a self-reflexive structure of consciousness.\n\nDespair \u2014 the \u201csickness unto death\u201d \u2014 is the misrelation within this structure: the failure to be the self that one is, or the refusal to be the self that one is. Despair is universal: every human being who has not grounded their self \u201ctransparently in the power that established it\u201d is in despair, even if they are unaware of it. Indeed, unawareness of despair is its most common form: the person who does not know they are in despair is more deeply in despair than the one who is conscious of it.\n\nKierkegaard\u2019s typology of despair is one of the most finely calibrated in philosophical literature. The analysis moves from the lowest (unconscious despair) through despair at not willing to be oneself (weakness) to the highest and most intense (despair at willing to be oneself \u2014 defiance). The despairing person who defiantly wills to be the self they have constituted, in rebellion against the power that established them, is in the most intense form of despair \u2014 and the closest to genuine selfhood, because they at least know what they are doing.\n\nThe second part of the work analyses despair as sin: despair before God, the refusal of the self to ground itself in God. Sin is not primarily the violation of ethical rules but the existential condition of being in despair before God, of not willing to be transparent in the power that established one. The antidote to sin is not ethical improvement but faith: the willingness to ground the self in God, to allow the relation to God to be the foundation of one\u2019s selfhood.',
    themes: ['the definition of the self', 'despair as the universal human sickness', 'the typology of despair', 'despair in weakness vs despair in defiance', 'sin as despair before God', 'faith as the cure for despair', 'consciousness and depth of despair', 'Anti-Climacus', 'the self as relation of relations'],
    keyCharacters: [
        { name: 'Anti-Climacus', role: 'The pseudonymous author; the inverse of Johannes Climacus; writes as an ideally intense Christian from a position Kierkegaard considers too high for his own spiritual state; the works attributed to Anti-Climacus represent the highest demands of Christianity' }
    ],
    concepts: [
        'The self as a relation that relates itself to itself \u2014 the self is not a substance but a structure: the relation between finite/infinite, temporal/eternal, freedom/necessity; and a self-reflexive consciousness of this relation',
        'Despair \u2014 the misrelation within the self\u2019s structure; the failure or refusal to be the self one is; the universal human condition for those not grounded in God',
        'Despair in not willing to be oneself \u2014 the despair of weakness: flight from the self, refusal to acknowledge one\u2019s own finitude and freedom',
        'Despair in willing to be oneself \u2014 the despair of defiance: the self that wills to constitute itself in rebellion against the power that established it; the most intense form of despair',
        'Consciousness as the measure of despair \u2014 the more conscious of its own condition the despairing self is, the more intense the despair; but also the closer to genuine selfhood',
        'Sin as despair before God \u2014 despair is sin when it is understood before God; sin is not primarily ethical transgression but the existential condition of not grounding the self in God',
        'Faith as the cure for despair \u2014 faith is the condition in which the self is transparent in the power that established it; the opposite of despair; the self that has become itself by grounding itself in God'
    ],
    structure: 'Introduction: The sickness unto death; the definition of despair\n\nPart One: The Sickness Unto Death is Despair\n\u2014 A. Despair is a sickness of the spirit, of the self (definition of the self)\n\u2014 B. The universality of despair\n\u2014 C. The forms of despair\n  \u2014 a. Despair as defined by consciousness\n  \u2014 b. Despair as defined by the constituents of the self\n    \u2014 The despair of infinitude / finitude\n    \u2014 The despair of possibility / necessity\n  \u2014 c. Despair as defined by consciousness continued\n    \u2014 Not willing to be oneself (despair of weakness)\n    \u2014 Willing to be oneself (despair of defiance)\n\nPart Two: Despair is Sin\n\u2014 A. Gradations in the consciousness of sin\n\u2014 B. Socrates\u2019 definition of sin (sin as ignorance; Kierkegaard\u2019s correction)\n\u2014 C. The sin of despairing of the forgiveness of sins\n\u2014 D. The sin against the Holy Spirit',
    quote: 'The formula that describes the state of the self when despair is completely rooted out is this: in relating itself to itself and in willing to be itself, the self rests transparently in the power that established it.',
    additionalQuotes: [
        { text: 'The most common form of despair is not being who you are.', citation: 'The Sickness Unto Death (paraphrased from Part One, C)' },
        { text: 'A human being is spirit. But what is spirit? Spirit is the self. But what is the self? The self is a relation that relates itself to itself.', citation: 'The Sickness Unto Death, Part One, A' },
        { text: 'There is so much talk about wasted lives \u2014 but only that person\u2019s life was wasted who lived on, so deceived by life\u2019s joys or its sorrows that he never became decisively, eternally conscious of himself as spirit, as self.', citation: 'The Sickness Unto Death, Part One, B' }
    ],
    commentary: [
        { philosopher: 'Paul Ricoeur', text: 'Ricoeur\u2019s Oneself as Another (1990) develops the phenomenology of selfhood through an engagement with Kierkegaard\u2019s definition of the self in The Sickness Unto Death. Ricoeur\u2019s distinction between idem-identity (numerical sameness over time) and ipse-identity (self-constancy as a form of promise-keeping) is partly a secularised development of Kierkegaard\u2019s analysis of the self as a relation that relates itself to itself.' },
        { philosopher: 'Ernest Becker', text: 'Becker\u2019s The Denial of Death (1973) is the most consequential secular appropriation of The Sickness Unto Death. Becker argues that despair \u2014 in Kierkegaard\u2019s sense \u2014 is the universal human condition produced by the knowledge of mortality and the impossibility of accepting it. The flight from despair takes the form of the \u201cimmortality projects\u201d through which human beings deny their finitude. Becker\u2019s secular terror management theory is Kierkegaard\u2019s diagnosis of despair translated into evolutionary psychology.' },
        { philosopher: 'Charles Taylor', text: 'Taylor\u2019s The Ethics of Authenticity (1991) and Sources of the Self (1989) draw heavily on The Sickness Unto Death\u2019s analysis of the self as a structure of commitments and its critique of the trivialisation of selfhood in modern culture. Taylor\u2019s account of the \u201cmalaises of modernity\u201d \u2014 the loss of meaning, the self-centredness, the loss of horizon \u2014 is a contemporary development of Kierkegaard\u2019s analysis of despair.' }
    ],
    modernRelevance: 'The Sickness Unto Death is the most influential philosophical analysis of the self and selfhood in the modern period. The opening definition of the self as a relation that relates itself to itself has been taken up by Sartre (the for-itself as self-reflexive consciousness), Heidegger (Dasein as the being for whom its own being is an issue), Ricoeur (narrative identity), and Taylor (the self as constituted by commitments). The typology of despair has influenced clinical psychology (existential psychotherapy), literary criticism (the analysis of character), and theology (Barth, Tillich, Bultmann). The formula for faith \u2014 \u201cresting transparently in the power that established one\u201d \u2014 has been the most discussed formulation of the religious life in Protestant theology since Barth.',
    context: 'Published 30 July 1849 by C.A. Reitzel in Copenhagen under the pseudonym Anti-Climacus, with Kierkegaard named as editor. The pseudonym is significant: Kierkegaard considered Anti-Climacus\u2019s Christianity too demanding for his own spiritual state; he was not the ideal Christian he described, merely the editor of the ideal\u2019s formulation. Standard English translation by Howard and Edna Hong (Princeton, 1980).',
    relatedWorks: ['concluding-unscientific-postscript', 'concept-of-anxiety', 'philosophical-fragments', 'works-of-love']
},

{
    id: 'works-of-love',
    title: 'Works of Love',
    greekTitle: 'Kjerlighedens Gjerninger',
    philosopher: 'kierkegaard',
    category: 'ethics',
    categoryLabel: 'Ethics & Philosophy of Religion',
    date: '1847 AD',
    dateSort: 1847,
    emoji: '\u2665\uFE0F',
    cardSize: 'normal',
    readingDifficulty: 'Intermediate',
    estimatedWordCount: 130000,
    shortDesc: 'Kierkegaard\u2019s most sustained ethical work \u2014 a systematic analysis of Christian love (agape) as the unconditional duty to love the neighbour, distinguished sharply from erotic love and friendship (which are preferential and self-interested) and grounded in God\u2019s command rather than natural inclination.',
    summary: 'Works of Love: Some Christian Reflections in the Form of Discourses (Kjerlighedens Gjerninger: Nogle christelige Overveielser i Taleform), published 29 September 1847 under his own name by C.A. Reitzel in Copenhagen, is Kierkegaard\u2019s most sustained and most systematic ethical work. It is one of the few works he published directly under his own name, signalling that it represents his own explicit position rather than a pseudonymous exploration.\n\nThe central distinction: erotic love (Elskov) and friendship (Venskab) are forms of preferential love \u2014 one loves the beloved because of specific qualities, because of attraction, because of shared history. This preferential love, however passionate and genuine, is ultimately a form of self-love: I love in the other what pleases me, what reflects my own values, what satisfies my desires. Christian love \u2014 neighbour-love (N\u00e6stekj\u00e6rlighed) \u2014 is non-preferential: it is owed to every human being as such, regardless of their qualities, regardless of whether they attract or repel, regardless of what one can gain from them.\n\nThe neighbour is whoever is present: \u201cthe neighbour is the first person you see.\u201d There is no hierarchy of neighbours; there is no calculation of merit; there is no expectation of return. This is the structure of agape, the Greek word for divine and unconditional love, as opposed to eros and philia. The duty to love the neighbour is grounded not in the neighbour\u2019s qualities but in God\u2019s command and in the image of God (Guds Billede) that every human being bears.\n\nThe work argues that genuine neighbour-love is actually the deepest form of erotic and friendship love: when one loves the beloved or the friend \u201cas the neighbour,\u201d one loves them unconditionally, free from the conditions that would otherwise make the relationship contingent on qualities that can change. The transformation of preferential love into neighbour-love through the middle term of God is the deepest consummation of the relationship.',
    themes: ['neighbour-love vs erotic love and friendship', 'the distinction between eros and agape', 'the duty to love unconditionally', 'the image of God in every human being', 'God as the middle term in all genuine love', 'the works of love', 'self-love and other-love', 'the Christian concept of the neighbour'],
    keyCharacters: [],
    concepts: [
        'Neighbour-love (N\u00e6stekj\u00e6rlighed) \u2014 unconditional love owed to every human being as such; not based on qualities, attractiveness, or merit; the specifically Christian form of love',
        'The neighbour as whoever is nearest \u2014 the neighbour is not a specific category of person but whoever happens to be present; there is no hierarchy of neighbours',
        'God as the middle term \u2014 genuine love always has God as its middle term; loving the beloved \u201cas the neighbour\u201d means loving them through and in God, unconditionally',
        'The transformation of erotic love \u2014 when preferential love is transformed into neighbour-love, it becomes more genuine, not less; the conditions of attraction and merit are removed',
        'Works of love \u2014 love is not merely a feeling but a practice; the works are the concrete expressions of love in daily life: building up, believing all things, hoping all things, bearing all things'
    ],
    structure: 'Preface\n\nFirst Series (eight deliberations on the command to love)\n\u2014 Love\u2019s Hidden Life and Its Recognisability by Its Fruits\n\u2014 You Shall Love (the command)\n\u2014 You Shall Love the Neighbour\n\u2014 You Shall Love the Neighbour: Love Your Neighbour as Yourself\n\u2014 The Neighbour (who is the neighbour?)\n\u2014 You Shall Love the Neighbour: Love Is a Matter of Conscience\n\nSecond Series (eight more deliberations)\n\u2014 Love Builds Up\n\u2014 Love Believes All Things\n\u2014 Love Hopes All Things\n\u2014 Love Seeks Not Its Own\n\u2014 The Work of Love in Recollecting One Who Is Dead\n\u2014 The Work of Love in Praising Love',
    quote: 'The object of both erotic love and friendship is the I \u2014 but the neighbour is your other-I, that which in the deepest sense is the equality of humanity before God. But equality before God has nothing to do with all this earthly dissimilarity.',
    additionalQuotes: [
        { text: 'To love another person is to help that person to love God.', citation: 'Works of Love, Second Series, \u201cOur Duty to Love the People We See\u201d' },
        { text: 'Love is the fulfilling of the law, says the apostle \u2014 but that also means it is the source and origin of all that is genuine in the law.', citation: 'Works of Love, First Series, Deliberation III (paraphrased)' }
    ],
    commentary: [
        { philosopher: 'Gene Outka', text: 'Outka\u2019s Agape: An Ethical Analysis (1972) is the most comprehensive philosophical analysis of the concept of neighbour-love and uses Works of Love as its primary text. Outka identifies equal regard as the core of agape: the commitment to treat every person as having equal worth regardless of their qualities. He argues that Kierkegaard\u2019s analysis is the most philosophically precise account of this concept in the Christian tradition.' },
        { philosopher: 'M. Jamie Ferreira', text: 'Ferreira\u2019s Love\u2019s Grateful Striving (2001) argues against the standard reading of Works of Love as advocating an austere, duty-bound love that excludes warmth and spontaneity. Kierkegaard\u2019s neighbour-love, Ferreira argues, is not the negation of erotic and friendship love but their deepening and transformation: when love is genuinely unconditional, the beloved or friend is loved more fully, not less.' }
    ],
    modernRelevance: 'Works of Love is the primary philosophical text for discussions of agape, unconditional love, and the ethics of care. Its distinction between preferential and non-preferential love has influenced theological ethics (Nygren\u2019s Agape and Eros), feminist care ethics (Noddings\u2019s distinction between natural and ethical caring), and political philosophy (discussions of impartiality and partiality in ethics). The claim that genuine love requires God as its middle term is the most sustained philosophical argument for the dependence of ethics on religion.',
    context: 'Published 29 September 1847 by C.A. Reitzel in Copenhagen under Kierkegaard\u2019s own name. One of the few works he did not publish pseudonymously. Written during the period of his most intense religious authorship, following the Either/Or and Stages period. Standard English translation by Howard and Edna Hong (Princeton, 1995).',
    relatedWorks: ['sickness-unto-death', 'concluding-unscientific-postscript', 'fear-and-trembling', 'attack-upon-christendom']
},

{
    id: 'attack-upon-christendom',
    title: 'Attack upon Christendom',
    greekTitle: '\u00d8ieblikket (The Moment)',
    philosopher: 'kierkegaard',
    category: 'practical',
    categoryLabel: 'Religious Polemic',
    date: '1854\u201355 AD',
    dateSort: 1854,
    emoji: '\u26A1',
    cardSize: 'normal',
    readingDifficulty: 'Beginner',
    estimatedWordCount: 80000,
    shortDesc: 'Kierkegaard\u2019s final explosion \u2014 the nine numbers of the polemical pamphlet \u201cThe Moment\u201d (and related articles) in which he attacked the Danish State Church as the greatest possible deception, arguing that official Christianity is the enemy of genuine Christianity and that the clergy are paid liars.',
    summary: 'The Attack upon Christendom consists of the articles and pamphlets with which Kierkegaard concluded his literary career. The attack began with an article in the newspaper Faedreland in December 1854, triggered by the eulogy Bishop Hans Lassen Martensen delivered at the funeral of Bishop Jakob Peter Mynster, praising Mynster as a \u201cwitness to the truth.\u201d For Kierkegaard, this was intolerable: Mynster was the representative of official Danish Christianity, a man who lived comfortably, enjoyed wealth and status, and preached a mild bourgeois Christianity that had nothing to do with the New Testament\u2019s demand for suffering, self-denial, and absolute commitment.\n\nBetween May and September 1855, Kierkegaard published nine numbers of the polemical pamphlet \u201cThe Moment\u201d (Oieblikket) at his own expense. He died on 11 November 1855, six weeks after the last number appeared and while the tenth was in preparation. The Attack is his most direct, most violent, and most readable work \u2014 the voice of someone who has spent his entire literary career working up to a confrontation he knew would destroy him.\n\nThe central argument: official Christendom is the precise opposite of genuine Christianity. The New Testament demands poverty, suffering, renunciation of the world, and the willingness to be persecuted. Official Christianity offers social respectability, professional advancement, and a mild ethical code. The clergy are paid by the state to proclaim a Christianity that the state\u2019s citizens will find comfortable \u2014 which means they are paid to suppress genuine Christianity. The most honest thing the established church could do would be to stop calling itself Christian.\n\nKierkegaard does not argue for a different theology but for the honesty to admit the gap between what is officially proclaimed and what the New Testament actually demands. If the clergy admitted they were not witnesses to the truth but merely servants of social order, he could respect them. What he cannot tolerate is the lie: the pretence that comfortable bourgeois Christianity is genuine New Testament Christianity.',
    themes: ['the attack on established Christianity', 'official Christianity vs New Testament Christianity', 'the clergy as paid liars', 'Bishop Martensen and Bishop Mynster', 'witness to the truth', 'the demand of the New Testament', 'Kierkegaard\u2019s death as confirmation', 'the final explosion', 'polemic as a form of truth-telling'],
    keyCharacters: [
        { name: 'Bishop Jakob Peter Mynster', role: 'The late Bishop of Copenhagen whose eulogy triggered the attack; Kierkegaard\u2019s father\u2019s pastor and a family friend; the representative of the established Christianity Kierkegaard attacks' },
        { name: 'Bishop Hans Lassen Martensen', role: 'Mynster\u2019s successor; his eulogy praising Mynster as a \u201cwitness to the truth\u201d triggered Kierkegaard\u2019s public attack; represented the comfortable theology of official Christendom' }
    ],
    concepts: [
        'Christendom vs Christianity \u2014 Christendom is the cultural and institutional form of Christianity in a nominally Christian society; genuine Christianity is the New Testament\u2019s radical demand for self-denial and suffering',
        'The witness to the truth \u2014 Kierkegaard\u2019s standard: a genuine Christian witness is one who suffers for the truth, not one who profits from it; the established clergy are the precise opposite',
        'Official Christianity as the greatest deception \u2014 the established church is more dangerous to genuine Christianity than outright persecution, because it gives the appearance of Christianity while suppressing its reality',
        'The New Testament demand \u2014 the unconditional demand of the New Testament for renunciation, poverty, suffering, and the willingness to be hated; incompatible with bourgeois respectability',
        'The moment (Oieblikket) \u2014 the title of the pamphlet series; the qualitative instant in which the eternal breaks into time; also the title of Kierkegaard\u2019s last public utterance'
    ],
    structure: '\u201cWas Bishop Mynster a Witness to the Truth?\u201d (Faedreland article, December 1854)\nThree further articles in Faedreland (February\u2013March 1855)\nNine numbers of \u201cThe Moment\u201d (Oieblikket), May\u2013September 1855\nNumber 10 of \u201cThe Moment\u201d (unfinished at death; published posthumously)',
    quote: 'The matter is quite simple. The New Testament is very easy to understand. But we human beings are really not very keen on understanding it, we are afraid that if we understood it, it would oblige us too much. Therefore we pretend that it is difficult to understand.',
    additionalQuotes: [
        { text: 'Official Christianity is, from the Christian point of view, a criminal offense \u2014 it is presenting a false version of Christianity as genuine, which is an offense against God and against those who are genuinely seeking.', citation: 'The Moment, No. 1 (paraphrased)' },
        { text: 'What I want is honesty. If that is what the human race, if what this generation wants, then let us be honest and openly, frankly, straightforwardly, directly rebel against Christianity.', citation: 'The Moment, No. 10' }
    ],
    commentary: [
        { philosopher: 'Karl Barth', text: 'Barth\u2019s neo-orthodox theology drew heavily on the Attack upon Christendom as the paradigm of genuine prophetic witness against the accommodation of Christianity to bourgeois culture. Barth\u2019s insistence on the \u201cinfinite qualitative difference\u201d between God and human culture \u2014 the impossibility of identifying any human institution, including the church, with the Kingdom of God \u2014 is the theological development of Kierkegaard\u2019s attack on established Christendom.' },
        { philosopher: 'Dietrich Bonhoeffer', text: 'Bonhoeffer\u2019s concept of \u201ccheap grace\u201d in The Cost of Discipleship (1937) \u2014 the grace that is proclaimed without the demand for repentance, discipleship, and suffering \u2014 is a Lutheran development of Kierkegaard\u2019s attack on official Christianity. Bonhoeffer\u2019s willingness to accept imprisonment and death for his resistance to Nazism was partly grounded in his reading of Kierkegaard on the witness to the truth.' }
    ],
    modernRelevance: 'The Attack upon Christendom is the founding text of the tradition of Christian social criticism that runs through Barth, Bonhoeffer, Tillich, and liberation theology. Its central charge \u2014 that institutional Christianity has become the enemy of the genuine Christianity it professes \u2014 resonates with every generation\u2019s experience of the gap between ecclesiastical institution and prophetic demand. The concept of \u201ccheap grace\u201d (Bonhoeffer\u2019s development) has become one of the most widely used concepts in Christian ethics. The Attack is also the model for a genre of philosophical polemic: the final, concentrated explosion of a lifetime\u2019s argument.',
    context: 'The attack began with an article in Faedreland in December 1854. Nine numbers of The Moment (Oieblikket) appeared between May and September 1855. Kierkegaard collapsed on the street on 2 October 1855 and died in Frederiks Hospital on 11 November 1855, aged forty-two. He refused to receive communion from a pastor of the established church on his deathbed. The standard English translation is by Walter Lowrie (Princeton, 1944; reprinted 1968).',
    relatedWorks: ['works-of-love', 'sickness-unto-death', 'concluding-unscientific-postscript', 'fear-and-trembling']
}

);
"""

for fname, content in files.items():
    path = os.path.join(js, fname)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'  Written {fname}  ({content.count(chr(10))} lines)')
