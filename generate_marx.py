#!/usr/bin/env python3
"""
Marx & Engels — data-21a through data-21e (10 works)
Run from ~/Desktop/philosophy-archive/: python3 generate_marx.py
"""
import os
js = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'js')
os.makedirs(js, exist_ok=True)

files = {}

# ── data-21a: Economic and Philosophical Manuscripts ─────────────────────────
files['data-21a.js'] = r"""/* DATA PART 21a — Marx: Economic and Philosophical Manuscripts of 1844 + Theses on Feuerbach */
window.WORKS.push(

{
    id: 'economic-philosophical-manuscripts',
    title: 'Economic and Philosophical Manuscripts of 1844',
    greekTitle: '\u00d6konomisch-philosophische Manuskripte aus dem Jahre 1844',
    philosopher: 'marx',
    category: 'metaphysics',
    categoryLabel: 'Philosophy & Political Economy',
    date: '1844 AD',
    dateSort: 1844,
    emoji: '\u26D3\uFE0F',
    cardSize: 'wide',
    readingDifficulty: 'Advanced',
    estimatedWordCount: 80000,
    shortDesc: 'The philosophical foundations of Marxism \u2014 Marx\u2019s most humanistic work, developing the concept of alienated labour as the central pathology of capitalism and arguing that the worker\u2019s estrangement from the product, the process, the species-being, and other workers is the condition from which communism promises liberation.',
    summary: 'The Economic and Philosophical Manuscripts of 1844 (also known as the Paris Manuscripts), written in Paris between April and August 1844 and unpublished during Marx\u2019s lifetime (first published in full in 1932 by the Marx-Engels Institute in Moscow), are the most philosophically rich of Marx\u2019s writings and the primary source for humanist interpretations of Marxism. Marx was twenty-six. The manuscripts were written during the same period as his first encounter with Engels (August 1844) and his intensive study of political economy (Smith, Ricardo, Mill) and his critical engagement with Hegel and Feuerbach.\n\nThe manuscripts are organised around the concept of alienated labour (entfremdete Arbeit), which Marx develops through a critique of political economy\u2019s starting assumptions. Political economy, Marx argues, accepts the estrangement of the worker as a natural fact and then explains the system\u2019s workings from within that presupposition. But political economy never asks: why does the worker become poorer the more wealth they produce? Why does labour\u2019s product confront the worker as an alien power? The answer requires going behind political economy to the concrete activity of labour itself.\n\nMarx distinguishes four forms of alienation. First, the worker is alienated from the product of labour: the object the worker produces belongs to another and confronts the worker as an alien, hostile power. The more the worker produces, the more powerful becomes the world of objects that dominates them. Second, the worker is alienated from the act of production itself: labour is not voluntary but coerced; the worker feels themselves only when not working, and not themselves when working; labour is not the satisfaction of a need but a means for satisfying needs outside itself. Third, the worker is alienated from their species-being (Gattungswesen): the human being is distinguished from animals by the fact that they make their life-activity itself an object of consciousness and will \u2014 they produce freely, universally, according to the standards of beauty; capitalism reduces this free productive activity to mere survival. Fourth, the worker is alienated from other workers: the alienation from one\u2019s product, process, and species-being entails the alienation from every other human being.\n\nThe manuscripts also contain extended discussions of private property, money, communism, and Hegel\u2019s philosophy. The critique of Hegel is double-edged: Hegel is right that self-estrangement is the fundamental problem, but wrong to locate it in consciousness rather than in material production. The Phenomenology of Spirit is the philosophical expression of economic alienation, not its analysis.',
    themes: ['alienated labour', 'the four forms of alienation', 'species-being', 'the critique of political economy', 'private property', 'communism as the positive abolition of alienation', 'the critique of Hegel', 'money as the alienated power of humanity', 'human nature and labour', 'Feuerbach and materialism'],
    keyCharacters: [],
    concepts: [
        'Alienated labour (entfremdete Arbeit) \u2014 the condition in which the worker\u2019s productive activity and its products become alien, hostile powers that dominate the worker; the central pathology of capitalism',
        'The four forms of alienation \u2014 from the product (which confronts the worker as alien), from the act of production (which is coerced), from species-being (free universal production reduced to survival), from other workers',
        'Species-being (Gattungswesen) \u2014 the human being\u2019s distinctive capacity to make its own life-activity an object of consciousness; to produce freely, universally, according to beauty; capitalism reduces this to mere animal survival',
        'Private property as the consequence of alienated labour \u2014 private property is not the cause of alienation but its expression and result; the abolition of private property is the abolition of alienation',
        'Communism as the positive abolition of private property \u2014 not mere equalisation of poverty but the genuine appropriation of human essence, the return of the human being to itself as a social being',
        'Money as the alienated power of humanity \u2014 money transforms all human powers and qualities into their opposite; it is the bond of all bonds, the universal pimp; it confounds and exchanges everything',
        'The critique of Hegel \u2014 Hegel is right that alienation is the fundamental problem but wrong to locate it in thought rather than in material productive activity; the Phenomenology is the philosophical expression of economic alienation'
    ],
    structure: 'First Manuscript: Wages of Labour; Profit of Capital; Rent of Land\n\u2014 Estranged Labour (the four forms of alienation)\n\nSecond Manuscript: [mostly missing] The Relation of Private Property\n\nThird Manuscript:\n\u2014 Private Property and Labour\n\u2014 Private Property and Communism\n\u2014 The Power of Money in Bourgeois Society\n\u2014 Critique of Hegel\u2019s Dialectic and General Philosophy\n\u2014 [pages missing from original manuscript]',
    quote: 'The worker becomes poorer the more wealth he produces, the more his production increases in power and extent. The worker becomes an ever cheaper commodity the more commodities he produces. The devaluation of the human world increases in direct relation with the increase in value of the world of things.',
    additionalQuotes: [
        { text: 'The alienation of the worker in his product means not only that his labour becomes an object, an external existence, but that it exists outside him, independently, as something alien to him, and that it becomes a power on its own confronting him.', citation: 'Economic and Philosophical Manuscripts, First Manuscript, \u201cEstranged Labour\u201d' },
        { text: 'Money is the alienated essence of man\u2019s work and existence; this essence dominates him and he worships it.', citation: 'Economic and Philosophical Manuscripts, Third Manuscript, \u201cThe Power of Money\u201d' },
        { text: 'Communism is the positive abolition of private property, of human self-alienation, and thus the real appropriation of human nature through and for man. It is therefore the return of man himself as a social, that is, really human being.', citation: 'Economic and Philosophical Manuscripts, Third Manuscript, \u201cPrivate Property and Communism\u201d' }
    ],
    commentary: [
        { philosopher: 'Louis Althusser', text: 'Althusser\u2019s For Marx (1965; English 1969) is the most consequential theoretical intervention on the Manuscripts. Althusser argued that there is an \u201cepistemological break\u201d (coupure \u00e9pist\u00e9mologique) between the early humanist Marx of the Manuscripts (still within the orbit of Hegelian and Feuerbachian humanism) and the mature scientific Marx of Capital. The concept of alienation is pre-scientific ideology; the categories of Capital are the genuine science of history. This reading provoked an enormous debate and defined the terms of Marxist theory for two decades.' },
        { philosopher: 'Erich Fromm', text: 'Fromm\u2019s Marx\u2019s Concept of Man (1961) is the paradigmatic humanist reading of the Manuscripts, directly opposed to Althusser. Fromm argued that the concept of alienated labour is not a pre-scientific relic but the heart of Marx\u2019s entire project; that Capital is the economic analysis of the same alienation that the Manuscripts analyse philosophically; and that Marx\u2019s true intellectual ancestor is not Hegel alone but the entire tradition of humanist ethics from Aristotle through Spinoza.' },
        { philosopher: 'Georg Luk\u00e1cs', text: 'Luk\u00e1cs\u2019s History and Class Consciousness (1923) \u2014 written before the Manuscripts were published \u2014 reconstructed the concept of reification (Verdinglichung) from Capital that is structurally identical to the alienation of the Manuscripts. When the Manuscripts were published in 1932, they were immediately recognised as the philosophical basis for the approach Luk\u00e1cs had already developed. His later work acknowledged the Manuscripts as the foundation of his own theoretical project.' },
        { philosopher: 'Hannah Arendt', text: 'Arendt\u2019s The Human Condition (1958) engages critically with Marx\u2019s concept of labour and species-being in the Manuscripts. Arendt argues that Marx conflates labour (the biological process of sustaining life, which leaves no lasting products) with work (the fabrication of a durable world) and action (the specifically human activity of political life). The concept of species-being as productive activity misses the distinctively political dimension of human existence.' }
    ],
    modernRelevance: 'The Economic and Philosophical Manuscripts of 1844 are the primary source for humanist Marxism, critical theory, and the philosophical foundations of social criticism. The concept of alienated labour has been developed into the sociology of work (Braverman\u2019s Labour and Monopoly Capital, 1974), the psychology of alienation (Fromm), existentialist Marxism (Sartre\u2019s Critique of Dialectical Reason), and feminist theory (the extension of alienation analysis to domestic labour and reproductive work). The concept of species-being anticipates contemporary discussions of human capabilities (Sen, Nussbaum). The critique of money as the alienated essence of human powers resonates with contemporary discussions of financialisation, commodity fetishism, and the colonisation of human relationships by market logic.',
    context: 'Written in Paris between April and August 1844. Marx had moved to Paris in October 1843 after the suppression of the Rheinische Zeitung, which he had edited. He was studying political economy intensively and was deeply influenced by Feuerbach\u2019s materialist transformation of Hegel. The manuscripts were never completed or published by Marx; he apparently abandoned them when he and Engels began working on The German Ideology (1845\u201346). They were first published in full in 1932 by the Marx-Engels Institute in Moscow, edited by D. Ryazanov. Their publication transformed the interpretation of Marx and generated the debate between humanist and structuralist Marxism that dominated the twentieth century.',
    relatedWorks: ['communist-manifesto', 'german-ideology', 'capital-vol1', 'theses-on-feuerbach']
},

{
    id: 'theses-on-feuerbach',
    title: 'Theses on Feuerbach',
    greekTitle: 'Thesen \u00fcber Feuerbach',
    philosopher: 'marx',
    category: 'method',
    categoryLabel: 'Philosophy of Praxis',
    date: '1845 AD',
    dateSort: 1845,
    emoji: '\u26A1',
    cardSize: 'normal',
    readingDifficulty: 'Intermediate',
    estimatedWordCount: 1500,
    shortDesc: 'Eleven theses \u2014 the most concentrated philosophical statement in modern thought, culminating in the most quoted sentence in the history of philosophy: \u201cPhilosophers have only interpreted the world in various ways; the point is to change it.\u201d',
    summary: 'The Theses on Feuerbach, written by Marx in Brussels in the spring of 1845 and first published by Engels in 1888 as an appendix to his Ludwig Feuerbach and the End of Classical German Philosophy, are eleven short theses that constitute the most compressed and most consequential philosophical statement in the Marxist tradition. Marx never published them himself; Engels described them as \u201cthe first document in which is deposited the brilliant germ of the new world outlook.\u201d\n\nThe theses are directed primarily against Feuerbach, whose materialism Marx regards as the best available alternative to Hegelian idealism but as still fundamentally contemplative: Feuerbach\u2019s materialism grasps the world as object, as something to be perceived and understood, but not as human sensuous activity, as practice (Praxis). The fundamental defect of all previous materialism is precisely this: it grasps the world as given, not as made.\n\nThe first thesis states the problem: Feuerbach\u2019s materialism grasps the external world only in the form of the object, not as sensuous human activity \u2014 practice. Therefore, the active side was developed by idealism, but idealism developed it abstractly (in thought) rather than concretely (in practice). The resolution: a materialism that grasps the world as constituted by human sensuous practical activity \u2014 the labour and social practice through which human beings transform both the world and themselves.\n\nThesis 3 states the fundamental problem with previous materialist theories of education and social reform: if human beings are products of circumstances and education, then circumstances must be changed \u2014 but who changes the circumstances? The educator must themselves be educated. Marx\u2019s resolution: the coincidence of changing circumstances and human activity can only be grasped as revolutionary practice (revolutionäre Praxis).\n\nThesis 11 \u2014 the most famous sentence in modern philosophy: \u201cPhilosophers have only interpreted the world in various ways; the point is to change it.\u201d This is not the rejection of philosophy but the demand for a philosophy that is simultaneously theoretical and practical \u2014 that understands the world as constituted by human practice and therefore as changeable through human practice.',
    themes: ['practice (Praxis) as the foundation of knowledge', 'the critique of Feuerbach\u2019s contemplative materialism', 'the coincidence of theory and practice', 'sensuous human activity as the basis of reality', 'revolutionary practice', 'the transformation of philosophy into social criticism', 'the eleventh thesis'],
    keyCharacters: [],
    concepts: [
        'Praxis \u2014 sensuous human activity through which human beings transform the world and themselves; the foundation of a genuinely materialist philosophy that is also transformative',
        'Contemplative materialism \u2014 Feuerbach\u2019s defect: grasps the world as object (to be perceived and understood) but not as practice (to be transformed); the active side is left to idealism',
        'The coincidence of changing circumstances and self-changing \u2014 Thesis 3: human beings are shaped by circumstances AND they change circumstances; the resolution of this apparent paradox is revolutionary practice',
        'The point is to change it \u2014 Thesis 11: philosophy must be not only the interpretation but the transformation of the world; theory and practice must be unified in revolutionary praxis',
        'The human essence as the ensemble of social relations \u2014 Thesis 6: Feuerbach abstracts an individual human essence; the real human essence is the ensemble (Ensemble) of social relations in which human beings exist'
    ],
    structure: 'Eleven theses:\n1. The defect of previous materialism (contemplation vs practice)\n2. The question of human thinking and truth is a practical question\n3. The materialist doctrine of circumstances and education; revolutionary practice\n4. Feuerbach and religious self-estrangement\n5. Feuerbach\u2019s sensuous contemplation; practice and thinking\n6. Feuerbach\u2019s abstraction of the human essence\n7. Religious sentiment as a social product\n8. Social life is essentially practical\n9. The standpoint of intuition vs social humanity\n10. The standpoint of old materialism vs new materialism\n11. Philosophers have only interpreted the world; the point is to change it',
    quote: 'Philosophers have only interpreted the world in various ways; the point is to change it.',
    additionalQuotes: [
        { text: 'The question whether objective truth can be attributed to human thinking is not a question of theory but is a practical question. Man must prove the truth, that is, the reality and power, the this-sidedness of his thinking, in practice.', citation: 'Theses on Feuerbach, Thesis 2' },
        { text: 'Feuerbach resolves the religious world into its secular basis. But the fact that the secular basis lifts off from itself and establishes itself in the clouds as an independent realm can only be explained by the inner strife and intrinsic contradictoriness of this secular basis.', citation: 'Theses on Feuerbach, Thesis 4' }
    ],
    commentary: [
        { philosopher: 'Antonio Gramsci', text: 'Gramsci\u2019s Prison Notebooks (1929\u201335) develop the concept of praxis from the Theses into a comprehensive philosophy of history and politics. Gramsci\u2019s \u201cphilosophy of praxis\u201d \u2014 his term for Marxism, partly for prison censor evasion \u2014 understands theory and practice as dialectically unified: theory is always already embedded in practical social activity; practice always already contains theoretical assumptions. The concept of hegemony \u2014 the role of ideas and culture in maintaining social domination \u2014 is the political development of the Theses\u2019 insight that changing the world requires changing how people think.' },
        { philosopher: 'J\u00fcrgen Habermas', text: 'Habermas\u2019s Knowledge and Human Interests (1968) engages with the Theses as the founding statement of a tradition that conflates theoretical knowledge with technical control: Marx\u2019s concept of praxis reduces all human interests to the interest in controlling nature through labour. Habermas argues that this misses the communicative and emancipatory dimensions of human rationality that cannot be reduced to technical practice.' }
    ],
    modernRelevance: 'The Theses on Feuerbach are the founding statement of the tradition of critical theory, which insists that genuine social knowledge is inseparable from social transformation. The concept of praxis has been central to the Frankfurt School (Adorno, Horkheimer, Marcuse, Habermas), to liberation theology (Gutierrez), to feminist theory (the insistence that theory must be grounded in practical experience and directed toward liberation), and to contemporary discussions of engaged scholarship, public philosophy, and the relationship between academic knowledge and political practice. The eleventh thesis has been quoted more often than any other sentence in modern philosophy.',
    context: 'Written in Brussels in the spring of 1845. Marx moved to Brussels after being expelled from Paris by the French government in February 1845. The Theses were jotted in a notebook and not published by Marx. Engels published them in 1888 as an appendix to his Ludwig Feuerbach and the End of Classical German Philosophy, noting that they were hastily written and not intended for publication but invaluable as a concise statement of the new outlook. The standard text is in Marx-Engels Werke, Vol. 3.',
    relatedWorks: ['economic-philosophical-manuscripts', 'german-ideology', 'communist-manifesto', 'capital-vol1']
}

);
"""

# ── data-21b: The German Ideology + Communist Manifesto ──────────────────────
files['data-21b.js'] = r"""/* DATA PART 21b — Marx & Engels: The German Ideology + The Communist Manifesto */
window.WORKS.push(

{
    id: 'german-ideology',
    title: 'The German Ideology',
    greekTitle: 'Die deutsche Ideologie',
    philosopher: 'marx',
    category: 'method',
    categoryLabel: 'Historical Materialism',
    date: '1845\u201346 AD',
    dateSort: 1845,
    emoji: '\uD83C\uDFED',
    cardSize: 'wide',
    readingDifficulty: 'Advanced',
    estimatedWordCount: 200000,
    shortDesc: 'The founding document of historical materialism \u2014 Marx and Engels\u2019s systematic critique of post-Hegelian German philosophy and their first full statement of the materialist conception of history: that consciousness does not determine life, but life determines consciousness.',
    summary: 'The German Ideology (Die deutsche Ideologie), written by Marx and Engels in Brussels between autumn 1845 and mid-1846 but unpublished during their lifetimes (first published in full in 1932), is the foundational text of historical materialism \u2014 the materialist conception of history (materialistische Geschichtsauffassung) that would underpin all of Marx\u2019s subsequent work.\n\nThe work is primarily a polemical critique of the Young Hegelians \u2014 Bruno Bauer, Max Stirner, and others \u2014 who, Marx and Engels argue, remain within the idealist presuppositions of German philosophy despite their apparent radicalism. The Young Hegelians criticise ideas with ideas, replacing one set of religious or philosophical conceptions with another. They do not see that ideas are not autonomous forces but expressions of material social relations.\n\nThe positive content is the first systematic statement of historical materialism. The premises Marx and Engels begin with are not arbitrary or dogmatic but the actual material premises of human existence: that human beings must produce their means of subsistence before they can make history. The mode of production \u2014 the way in which human beings organise their productive activity \u2014 determines the form of social life, the legal and political institutions, and the forms of consciousness that develop within it.\n\nThe famous formulation: \u201cLife is not determined by consciousness, but consciousness by life.\u201d Or in its more elaborate form: \u201cThe production of ideas, of conceptions, of consciousness is at first directly interwoven with the material activity and the material intercourse of men. The ideas, the ideational interchanges of men appear at this point directly as the direct efflux of their material behaviour.\u201d\n\nThe work also contains the famous account of ideology: the dominant ideas of every epoch are the ideas of the ruling class, because the ruling class controls the means of mental production as well as the means of material production. The ruling class presents its particular interests as universal interests, its historically contingent ideas as eternal truths \u2014 this is ideology. The camera obscura image: ideology presents the world inverted, as a camera obscura inverts the image it captures.',
    themes: ['historical materialism', 'the materialist conception of history', 'the critique of the Young Hegelians', 'the mode of production', 'base and superstructure', 'ideology', 'the camera obscura', 'life determines consciousness', 'the division of labour', 'class and class consciousness'],
    keyCharacters: [],
    concepts: [
        'Historical materialism \u2014 the materialist conception of history: the mode of production determines the forms of social life, legal and political institutions, and consciousness',
        'Life determines consciousness \u2014 the fundamental inversion of idealism: it is not ideas that drive history but material social relations; consciousness is the expression of material life',
        'The mode of production \u2014 the way in which human beings organise their productive activity; the decisive factor in determining the structure of society at any given historical moment',
        'Base and superstructure \u2014 the economic base (relations of production) determines the superstructure (legal, political, and ideological forms); changes in the base drive changes in the superstructure',
        'Ideology \u2014 the dominant ideas of every epoch are the ideas of the ruling class; ideology presents particular class interests as universal interests and historically contingent arrangements as natural and eternal',
        'The camera obscura \u2014 ideology inverts reality as a camera obscura inverts the image: the real material relations appear as their own inversion in ideological consciousness',
        'The division of labour \u2014 the progressive specialisation of productive activity that is simultaneously the basis of increased productivity and the source of class divisions, alienation, and the separation of intellectual from manual work'
    ],
    structure: 'Volume I: Critique of Modern German Philosophy According to Its Representatives Feuerbach, B. Bauer and Stirner\n\u2014 Part 1: Feuerbach: Opposition of the Materialist and Idealist Outlooks\n  \u2014 The Materialist Conception of History\n  \u2014 History: Fundamental Conditions\n  \u2014 Private Property and Communism\n\u2014 Part 2: Critique of Bruno Bauer\u2014 Part 3: Critique of Max Stirner (the longest section; the \u201cSaint Max\u201d critique)\n\nVolume II: Critique of German Socialism According to Its Various Prophets\n\u2014 The True Socialists',
    quote: 'The ideas of the ruling class are in every epoch the ruling ideas: i.e. the class which is the ruling material force of society is at the same time its ruling intellectual force.',
    additionalQuotes: [
        { text: 'Life is not determined by consciousness, but consciousness by life.', citation: 'The German Ideology, Part I' },
        { text: 'In communist society, where nobody has one exclusive sphere of activity but each can become accomplished in any branch he wishes, society regulates the general production and thus makes it possible for me to do one thing today and another tomorrow, to hunt in the morning, fish in the afternoon, rear cattle in the evening, criticise after dinner, just as I have a mind, without ever becoming hunter, fisherman, shepherd or critic.', citation: 'The German Ideology, Part I (the famous passage on communist society)' },
        { text: 'The production of ideas, of conceptions, of consciousness, is at first directly interwoven with the material activity and the material intercourse of men.', citation: 'The German Ideology, Part I' }
    ],
    commentary: [
        { philosopher: 'G.A. Cohen', text: 'Cohen\u2019s Karl Marx\u2019s Theory of History: A Defence (1978) is the most rigorous analytical reconstruction of the materialist conception of history as first stated in The German Ideology. Cohen argues that the base-superstructure model can be reconstructed as a coherent functional explanation: the superstructure exists and has the character it has because it sustains the base; the relations of production are what they are because they develop the productive forces. This \u201ctechnological determinism\u201d reading was enormously influential in the analytical Marxism of the 1980s.' },
        { philosopher: 'Raymond Williams', text: 'Williams\u2019s Marxism and Literature (1977) provides the most influential cultural-materialist reading of the base-superstructure model from The German Ideology. Williams argues that the model, mechanically applied, reduces culture to mere reflection of economic base; his alternative \u2014 the concepts of hegemony (from Gramsci), residual/dominant/emergent culture, and structures of feeling \u2014 attempts to preserve the insight that cultural production is materially conditioned without reducing it to passive expression.' }
    ],
    modernRelevance: 'The German Ideology is the founding text of the sociology of knowledge: the systematic study of the social conditions of knowledge production. The concept of ideology \u2014 the ruling class\u2019s ideas as the ruling ideas \u2014 has been developed by Lukacs (reification), Gramsci (hegemony), Althusser (ideological state apparatuses), Foucault (power/knowledge), and the entire tradition of ideology critique. The base-superstructure model, however contested, remains the foundational framework for materialist approaches to culture, law, politics, and religion. The passage on communist society \u2014 hunting in the morning, fishing in the afternoon \u2014 is the most quoted utopian vision in Marxist literature.',
    context: 'Written in Brussels, autumn 1845 to mid-1846. Marx and Engels tried unsuccessfully to publish it and eventually \u201cabandoned it to the gnawing criticism of the mice,\u201d as Marx wrote in the 1859 Preface. First published in full in 1932 by the Marx-Engels Institute in Moscow. The standard text is in Marx-Engels Werke, Vol. 3.',
    relatedWorks: ['theses-on-feuerbach', 'communist-manifesto', 'capital-vol1', 'economic-philosophical-manuscripts']
},

{
    id: 'communist-manifesto',
    title: 'The Communist Manifesto',
    greekTitle: 'Manifest der Kommunistischen Partei',
    philosopher: 'marx',
    category: 'practical',
    categoryLabel: 'Political Philosophy',
    date: '1848 AD',
    dateSort: 1848,
    emoji: '\u2764\uFE0F',
    cardSize: 'wide',
    readingDifficulty: 'Beginner',
    estimatedWordCount: 12000,
    shortDesc: 'The most widely read political document in history \u2014 Marx and Engels\u2019s compressed account of bourgeois society\u2019s revolutionary dynamism and its inevitable destruction, the history of all hitherto existing society as the history of class struggles, and the call for the workers of the world to unite.',
    summary: 'The Manifesto of the Communist Party (Manifest der Kommunistischen Partei), written by Marx and Engels in Brussels and London between December 1847 and January 1848 and published in London by the Communist League on 21 February 1848 \u2014 days before the revolutionary outbreak in Paris that spread across Europe \u2014 is the most widely read, most translated, and most politically influential political document in the history of the modern world.\n\nThe Manifesto opens with the most arresting sentence in modern political writing: \u201cA spectre is haunting Europe \u2014 the spectre of communism.\u201d It then delivers, in four short sections and approximately forty pages, a comprehensive theory of history, an analysis of capitalism\u2019s dynamics, and a programme for revolutionary transformation.\n\nSection I, \u201cBourgeois and Proletarians,\u201d is the philosophical and historical core. It opens with the thesis that the history of all hitherto existing society is the history of class struggles. Freeman and slave, patrician and plebeian, lord and serf, guild-master and journeyman: each epoch has been structured by the conflict between oppressor and oppressed. The bourgeoisie \u2014 the modern capitalist class \u2014 is the product of a long historical development from the medieval commune through the emerging market of early modernity to the industrial revolution. The Manifesto\u2019s most memorable passages are those that celebrate the revolutionary dynamism of the bourgeoisie: \u201cThe bourgeoisie, wherever it has got the upper hand, has put an end to all feudal, patriarchal, idyllic relations.\u201d It has \u201cpitilessly torn asunder the motley feudal ties that bound man to his \u2018natural superiors\u2019 and left remaining no other nexus between man and man than naked self-interest, than callous \u2018cash payment.\u2019\u201d The bourgeoisie creates the modern world \u2014 and it creates the proletariat that will destroy it.\n\nSection II defends the communist programme against objections: the abolition of private property (in the means of production, not personal property), the abolition of the family (as a bourgeois institution), the abolition of national distinctions. The ten-point programme of immediate demands includes a progressive income tax, the abolition of inheritance, the centralisation of credit and communication in the hands of the state, and free education.\n\nSection IV ends with the call that has echoed through modern history: \u201cWorking men of all countries, unite!\u201d (literally: \u201cWorkers of all lands, unite!\u201d \u2014 Proletarier aller L\u00e4nder, vereinigt euch!)',
    themes: ['the history of class struggle', 'the revolutionary role of the bourgeoisie', 'the proletariat as the revolutionary class', 'capitalism\u2019s self-destruction', 'the abolition of private property', 'the ten demands', 'workers of the world unite', 'communism vs other socialist currents', 'the spectre of communism'],
    keyCharacters: [],
    concepts: [
        'The history of all hitherto existing society is the history of class struggles \u2014 the fundamental thesis: every historical epoch is structured by conflict between opposing classes',
        'The revolutionary dynamism of the bourgeoisie \u2014 the Manifesto\u2019s most surprising feature: capitalism\u2019s extraordinary capacity for creative destruction; it creates the modern world and the class that will destroy it',
        'The proletariat \u2014 the modern industrial working class: the class that owns nothing but its labour power; the class whose emancipation is simultaneously the emancipation of humanity',
        'The abolition of private property \u2014 not personal property but property in the means of production; the condition for the abolition of class exploitation',
        'All that is solid melts into air \u2014 capitalism\u2019s compulsive drive to revolutionise production, dissolve traditions, and transform everything into a commodity; the permanent revolution of bourgeois society',
        'Workers of all lands, unite! \u2014 the Manifesto\u2019s closing call; the demand for international working-class solidarity as the condition for revolutionary transformation'
    ],
    structure: 'Preface (various editions 1872\u20131883)\n\nI. Bourgeois and Proletarians\n\u2014 The history of class struggle\n\u2014 The revolutionary role of the bourgeoisie\n\u2014 The development of the proletariat\n\u2014 The inevitable contradiction of capitalism\n\nII. Proletarians and Communists\n\u2014 The communist programme\n\u2014 Objections and responses\n\u2014 The ten-point programme\n\nIII. Socialist and Communist Literature\n\u2014 Reactionary socialism; conservative socialism; utopian socialism\n\nIV. Position of the Communists in Relation to the Various Existing Opposition Parties',
    quote: 'A spectre is haunting Europe \u2014 the spectre of communism. All the powers of old Europe have entered into a holy alliance to exorcise this spectre.',
    additionalQuotes: [
        { text: 'The history of all hitherto existing society is the history of class struggles.', citation: 'The Communist Manifesto, Section I' },
        { text: 'The bourgeoisie, wherever it has got the upper hand, has put an end to all feudal, patriarchal, idyllic relations. It has pitilessly torn asunder the motley feudal ties that bound man to his \u201cnatural superiors\u201d, and has left remaining no other nexus between man and man than naked self-interest, than callous \u201ccash payment\u201d.', citation: 'The Communist Manifesto, Section I' },
        { text: 'All that is solid melts into air, all that is holy is profaned, and man is at last compelled to face with sober senses his real conditions of life, and his relations with his kind.', citation: 'The Communist Manifesto, Section I' },
        { text: 'The proletarians have nothing to lose but their chains. They have a world to win. Workers of all lands, unite!', citation: 'The Communist Manifesto, Section IV (closing lines)' }
    ],
    commentary: [
        { philosopher: 'Marshall Berman', text: 'Berman\u2019s All That Is Solid Melts into Air (1982) is the most celebrated cultural reading of the Manifesto. Berman argues that Marx\u2019s portrait of capitalist modernity \u2014 its ceaseless self-destruction and recreation, the dissolution of all fixed relations, the compulsive drive to revolutionise \u2014 is simultaneously the most powerful diagnosis of modernity and the most paradoxical, since communism promises to achieve the stability and community that capitalism perpetually destroys.' },
        { philosopher: 'Eric Hobsbawm', text: 'Hobsbawm\u2019s introduction to the Verso edition (1998) situates the Manifesto in its historical context and assesses its extraordinary predictive record: its account of globalisation, the concentration of capital, the destruction of precapitalist social forms, and the subordination of all social relations to market logic reads as a description of the late twentieth century despite being written in 1848.' },
        { philosopher: 'Gareth Stedman Jones', text: 'Stedman Jones\u2019s Karl Marx: Greatness and Illusion (2016) and his introduction to the Penguin edition of the Manifesto provide the most historically nuanced reading, situating it within the specific political debates of 1847\u201348 and resisting the tendency to read it as a finished, timeless statement of Marxist theory.' }
    ],
    modernRelevance: 'The Communist Manifesto is the most widely read and most politically influential text in modern history. It has been translated into more languages, published in more editions, and claimed by more political movements than any other political document. Its account of capitalism\u2019s revolutionary dynamism \u2014 the compulsion to revolutionise production, to dissolve traditional ties, to subordinate everything to market logic \u2014 is regularly cited by commentators across the political spectrum as the most prescient description of contemporary capitalism. \u201cAll that is solid melts into air\u201d has become the defining phrase for the experience of capitalist modernity. The concept of class struggle, however contested, remains the foundational category of left politics worldwide.',
    context: 'Written in Brussels and London, December 1847 \u2013 January 1848. Marx and Engels had been commissioned by the Communist League at its second congress (November\u2013December 1847) to write a programme. Published in London on 21 February 1848, days before the outbreak of revolution in Paris. Translated into English by Helen Macfarlane and published in George Julian Harney\u2019s Red Republican in 1850. Marx and Engels wrote prefaces to the German editions of 1872 and 1883 and to various translations, noting what they would and would not revise. The most widely used English translation is by Samuel Moore (1888), revised by Engels.',
    relatedWorks: ['german-ideology', 'capital-vol1', 'economic-philosophical-manuscripts', 'civil-war-in-france']
}

);
"""

# ── data-21c: Capital Vol. 1 ──────────────────────────────────────────────────
files['data-21c.js'] = r"""/* DATA PART 21c — Marx: Capital, Volume I */
window.WORKS.push(
{
    id: 'capital-vol1',
    title: 'Capital: A Critique of Political Economy, Vol. I',
    greekTitle: 'Das Kapital: Kritik der politischen \u00d6konomie, Band I',
    philosopher: 'marx',
    category: 'practical',
    categoryLabel: 'Political Economy',
    date: '1867 AD',
    dateSort: 1867,
    emoji: '\u2699\uFE0F',
    cardSize: 'wide',
    readingDifficulty: 'Advanced',
    estimatedWordCount: 400000,
    shortDesc: 'The most consequential work of social science ever written \u2014 Marx\u2019s systematic analysis of the capitalist mode of production, revealing that the extraction of surplus value from labour is the secret of capitalist accumulation, that commodity fetishism conceals this exploitation, and that capitalism\u2019s internal contradictions must drive it toward its own dissolution.',
    summary: 'Capital: A Critique of Political Economy, Volume I: The Process of Production of Capital (Das Kapital: Kritik der politischen \u00d6konomie, Band I: Der Produktionsprocess des Kapitals), published in Hamburg by Otto Meissner on 14 September 1867, is the most consequential work of social science ever written and the book that has shaped more of the political history of the last century and a half than any other. Marx spent approximately eighteen years preparing and writing it.\n\nThe work begins deceptively simply: with the commodity (Ware) \u2014 the elementary form of wealth in capitalist society. A commodity is anything produced for exchange rather than for direct use. It has two aspects: use-value (its capacity to satisfy a human need) and exchange-value (the ratio in which it exchanges for other commodities). The analysis of exchange-value leads immediately to the concept of value (Wert): exchange-value is the phenomenal form of value; value is determined by the socially necessary labour time required to produce a commodity.\n\nThis leads to the fundamental puzzle: in a system of commodity exchange where equivalents exchange for equivalents, where does profit come from? The answer is the theory of surplus value (Mehrwert). The capitalist buys labour-power at its value (the cost of the worker\u2019s reproduction) and sets the worker to work for longer than the labour-time required to reproduce that value. The difference \u2014 surplus labour \u2014 produces surplus value, which is appropriated by the capitalist. This is the secret of capital accumulation.\n\nMarx distinguishes absolute surplus value (extracted by extending the working day) from relative surplus value (extracted by increasing the productivity of labour so that the reproduction of labour-power requires less of the working day). The analysis of relative surplus value drives the analysis of machinery, the factory system, and the tendency of capital to replace living labour with dead labour (machines), which \u2014 paradoxically \u2014 generates the tendency of the rate of profit to fall.\n\nThe chapter on commodity fetishism (Warenfetischismus) is the most philosophically important in the work. Commodity fetishism is the illusion by which the social relations between human beings \u2014 the relations of production \u2014 appear as relations between things (commodities, prices, the market). The market appears as an objective, natural system governed by laws independent of human will; the social character of labour is hidden behind the apparent objectivity of exchange values. This is the economic form of ideology.\n\nThe final section on the primitive accumulation of capital (urspr\u00fcngliche Akkumulation) demolishes the idyllic mythology of bourgeois economics: the origin of capital is not the thrift of industrious individuals but the forcible expropriation of peasants from common lands, the slave trade, colonial plunder, and the violence of the enclosures. The chapter on the historical tendency of capitalist accumulation ends with the famous prediction of capitalism\u2019s inevitable dissolution: the expropriation of the expropriators.',
    themes: ['the commodity and its two factors', 'value and socially necessary labour time', 'surplus value and its extraction', 'absolute and relative surplus value', 'commodity fetishism', 'the tendency of the rate of profit to fall', 'machinery and large-scale industry', 'primitive accumulation', 'the working day', 'the general law of capitalist accumulation', 'the expropriation of the expropriators'],
    keyCharacters: [],
    concepts: [
        'The commodity \u2014 the elementary form of wealth in capitalist society; has two factors: use-value (capacity to satisfy need) and exchange-value (ratio of exchange with other commodities)',
        'Value and socially necessary labour time \u2014 value is determined by the socially necessary labour time required to produce a commodity; the common substance behind exchange-value',
        'Surplus value (Mehrwert) \u2014 the value produced by the worker beyond the value of their own labour-power; the source of capitalist profit; the secret of capital accumulation',
        'Absolute vs relative surplus value \u2014 absolute: extracted by extending the working day; relative: extracted by increasing labour productivity so less of the working day is needed to reproduce labour-power',
        'Commodity fetishism (Warenfetischismus) \u2014 the illusion by which social relations between human beings appear as relations between things; the market appears as objective and natural rather than as a social construction',
        'The tendency of the rate of profit to fall \u2014 as capital substitutes machinery for labour, and since only living labour produces surplus value, the rate of profit tends to fall; a built-in contradiction of capitalist development',
        'Primitive accumulation \u2014 the historical origin of capital in the forcible expropriation of peasants, colonial plunder, and slave trade; the original sin of capitalism, not the thrift of industrious individuals',
        'The general law of capitalist accumulation \u2014 as capital accumulates, the working class is pauperised; the increasing wealth of the capitalist class is inseparable from the increasing misery of the proletariat',
        'The expropriation of the expropriators \u2014 the historical tendency of capitalist accumulation leads to the concentration of capital and the growth of the proletariat, making possible the revolutionary expropriation of the capitalist class'
    ],
    structure: 'Preface to the First Edition; Postface to the Second Edition\n\nPart One: Commodities and Money\n\u2014 Chapter 1: The Commodity (use-value, exchange-value, value; the value-form; commodity fetishism)\n\u2014 Chapters 2\u20133: Exchange and Money\n\nPart Two: The Transformation of Money into Capital\n\u2014 Chapter 4: The General Formula for Capital (M\u2013C\u2013M\u2032)\n\u2014 Chapter 5: Contradictions in the General Formula\n\u2014 Chapter 6: The Sale and Purchase of Labour-Power\n\nPart Three: The Production of Absolute Surplus-Value\n\u2014 Chapter 7: The Labour Process and Valorisation Process\n\u2014 Chapter 8: Constant Capital and Variable Capital\n\u2014 Chapter 9: The Rate of Surplus-Value\n\u2014 Chapter 10: The Working Day\n\nPart Four: The Production of Relative Surplus-Value\n\u2014 Chapters 11\u201313: Co-operation; Division of Labour; Machinery\n\nParts Five\u2013Seven: Wages; Accumulation; Primitive Accumulation\n\u2014 Chapter 24: The Transformation of Surplus-Value into Capital\n\u2014 Chapter 25: The General Law of Capitalist Accumulation\n\u2014 Chapter 26\u201332: Primitive Accumulation\n\u2014 Chapter 32: Historical Tendency of Capitalist Accumulation',
    quote: 'Capital is dead labour, that, vampire-like, only lives by sucking living labour, and lives the more, the more labour it sucks.',
    additionalQuotes: [
        { text: 'A commodity appears, at first sight, as an extremely obvious, trivial thing. But its analysis brings out that it is a very queer thing, abounding in metaphysical subtleties and theological niceties.', citation: 'Capital, Vol. I, Chapter 1, Section 4 (\u201cThe Fetishism of Commodities\u201d)' },
        { text: 'The expropriation of the agricultural producer, of the peasant, from the soil is the basis of the whole process. The history of this expropriation is written in the annals of mankind in letters of blood and fire.', citation: 'Capital, Vol. I, Chapter 26' },
        { text: 'Accumulation of wealth at one pole is at the same time accumulation of misery, the torment of labour, slavery, ignorance, brutalisation and moral degradation at the opposite pole, i.e. on the side of the class that produces its own product as capital.', citation: 'Capital, Vol. I, Chapter 25' }
    ],
    commentary: [
        { philosopher: 'Rosa Luxemburg', text: 'Luxemburg\u2019s The Accumulation of Capital (1913) extends and challenges Marx\u2019s analysis in Capital Vol. I. She argued that Marx\u2019s reproduction schemas in Vol. II presuppose the existence of non-capitalist markets for the realisation of surplus value; capitalism requires an external \u201coutside\u201d for its expansion and will collapse when the non-capitalist world has been fully absorbed. This \u201cimperialist\u201d reading of Capital has been enormously influential in theories of underdevelopment and global capitalism.' },
        { philosopher: 'Georg Luk\u00e1cs', text: 'Luk\u00e1cs\u2019s History and Class Consciousness (1923) developed the commodity fetishism analysis of Chapter 1 into the concept of reification (Verdinglichung): the process by which social relations generally \u2014 not only market relations \u2014 take on the character of thing-like objectivity, appearing as natural and inevitable rather than as social constructions. Reification is the epistemological condition of bourgeois thought; the proletariat\u2019s position in the production process gives it the standpoint from which reification can be seen through.' },
        { philosopher: 'Louis Althusser', text: 'Althusser\u2019s Reading Capital (1965; English 1970) argued that Capital must be read as a scientific work that breaks entirely with the humanist problematic of the 1844 Manuscripts. The categories of Capital \u2014 value, surplus value, mode of production, social formation \u2014 are not expressions of an alienated human essence but structural concepts of a social science that has nothing to do with human subjects. This structuralist reading was enormously influential in 1960s\u201370s Marxism.' },
        { philosopher: 'David Harvey', text: 'Harvey\u2019s A Companion to Marx\u2019s Capital (2010; followed by A Companion to Marx\u2019s Capital Volume 2, 2013) is the most accessible and most widely read contemporary guide to Capital. Harvey\u2019s reading emphasises the geographical dimensions of capital accumulation and connects the analysis of Capital to contemporary issues of financialisation, urbanisation, and global uneven development.' }
    ],
    modernRelevance: 'Capital is the founding text of the social sciences as a critical enterprise. Its method \u2014 the analysis of surface appearances to reveal the underlying relations of production \u2014 is the template for ideology critique, cultural studies, and the sociology of knowledge. The concept of commodity fetishism has been developed into the analysis of media, advertising, branding, and the commodification of culture. The analysis of surplus value underpins contemporary discussions of wage theft, unpaid labour, and the political economy of digital platforms. The account of primitive accumulation has been developed by David Harvey into the concept of \u201caccumulation by dispossession\u201d \u2014 the ongoing expropriation of commons, public goods, and natural resources that continues under contemporary capitalism.',
    context: 'Published in Hamburg by Otto Meissner on 14 September 1867. Marx began serious work on the book in the 1850s; the Grundrisse (1857\u201358) is the first full draft. A second German edition appeared in 1872\u201375; Engels prepared the third (1883) and fourth (1890) German editions after Marx\u2019s death. The first English translation by Samuel Moore and Edward Aveling, edited by Engels, appeared in 1887. The French translation by Joseph Roy, supervised by Marx (1872\u201375), contains some revisions not in the German editions.',
    relatedWorks: ['communist-manifesto', 'german-ideology', 'grundrisse', 'critique-political-economy-1859']
}
);
"""

# ── data-21d: Grundrisse + Critique of Political Economy + Civil War in France
files['data-21d.js'] = r"""/* DATA PART 21d — Marx: Grundrisse + Critique of Political Economy + Civil War in France */
window.WORKS.push(

{
    id: 'grundrisse',
    title: 'Grundrisse: Foundations of the Critique of Political Economy',
    greekTitle: 'Grundrisse der Kritik der politischen \u00d6konomie',
    philosopher: 'marx',
    category: 'practical',
    categoryLabel: 'Political Economy',
    date: '1857\u201358 AD',
    dateSort: 1857,
    emoji: '\uD83D\uDCCB',
    cardSize: 'normal',
    readingDifficulty: 'Advanced',
    estimatedWordCount: 500000,
    shortDesc: 'The massive rough draft of Capital \u2014 Marx\u2019s private notebooks of 1857\u201358, containing the most philosophically developed statements of his mature thought, including the Fragment on Machines (the first analysis of intellectual labour as a productive force) and the Introduction that laid out his method.',
    summary: 'Grundrisse: Foundations of the Critique of Political Economy (Rough Draft) (Grundrisse der Kritik der politischen \u00d6konomie (Rohentwurf)), written by Marx in London between August 1857 and May 1858 as private notebooks and published posthumously (Moscow, 1939\u201341; full German edition 1953; English translation 1973), is the most philosophically rich and most structurally ambitious of Marx\u2019s economic manuscripts.\n\nThe Grundrisse was written during an economic crisis that Marx expected would precipitate the revolution he had been predicting since 1848. Working with extraordinary intensity, he produced seven notebooks of approximately 900 pages covering money, capital, landed property, wage labour, the state, foreign trade, and the world market \u2014 the plan of a systematic critique of political economy that was never completed in this form.\n\nThe Introduction (written in August 1857 but not published by Marx) is one of the most important methodological texts in the Marxist tradition. Marx lays out his method of political economy: the move from concrete to abstract (the analytical decomposition of concrete reality into simpler determinations) and then back from abstract to concrete (the reconstruction of concrete reality through the synthesis of multiple determinations). This \u201crescending from the abstract to the concrete\u201d is the method of Capital.\n\nThe most philosophically important section is the Fragment on Machines (Maschinenfragment) in Notebook VII. Marx analyses the implications of automation for the labour theory of value: as machines increasingly replace living labour in production, the creation of wealth depends less and less on the amount of labour time employed and more and more on the general state of science and the progress of technology. Marx calls this accumulated social knowledge the \u201cgeneral intellect\u201d (allgemeiner Verstand): the collective intellectual capacity of human society objectified in machines and productive processes. This passage \u2014 written in 1858 \u2014 has become the primary theoretical resource for analyses of the knowledge economy, cognitive capitalism, and the contemporary crisis of the labour theory of value in the age of automation.',
    themes: ['the method of political economy', 'the general intellect', 'the Fragment on Machines', 'money and credit', 'forms of capital', 'the tendency of the rate of profit to fall', 'automation and the crisis of value', 'the Introduction\u2019s method', 'the plan of the critique of political economy'],
    keyCharacters: [],
    concepts: [
        'The method of ascending from abstract to concrete \u2014 the Introduction\u2019s methodological statement: analysis decomposes concrete reality into abstract determinations; the method then synthesises these abstractions back into the concrete totality',
        'The general intellect (allgemeiner Verstand) \u2014 accumulated social knowledge objectified in machines and productive processes; as automation advances, the creation of wealth depends increasingly on the general intellect rather than on direct labour time',
        'The Fragment on Machines \u2014 the analysis of automation\u2019s implications for the labour theory of value: when machines replace labour, the measure of value (labour time) is undermined; the tendency toward a post-scarcity economy',
        'Fixed capital and living labour \u2014 the progressive substitution of dead labour (machines, fixed capital) for living labour in production; the source of the tendency of the rate of profit to fall',
        'The general formula M\u2013C\u2013M\u2032 \u2014 money buys commodities (including labour-power) that produce more money; the circuit of capital; the logic of capital accumulation as the expansion of value'
    ],
    structure: 'Introduction (August 1857): Production, consumption, distribution, exchange; the method of political economy\n\nNotebook I: On Money\nNotebook II: On Capital (Money becoming capital; production process; surplus value)\nNotebooks III\u2013V: On Capital (Continued)\nNotebook VI: On Capital (The Fragment on Machines; the general intellect; automation)\nNotebook VII: On Capital and Revenue; Landed Property; Wages',
    quote: 'The theft of alien labour time, on which the present wealth is based, appears a miserable foundation in face of this new one, created by large-scale industry itself. As soon as labour in the direct form has ceased to be the great well-spring of wealth, labour time ceases and must cease to be its measure.',
    additionalQuotes: [
        { text: 'Nature builds no machines, no locomotives, railways, electric telegraphs, self-acting mules etc. These are products of human industry; natural material transformed into organs of the human will over nature, or of human participation in nature. They are organs of the human brain, created by the human hand; the power of knowledge, objectified.', citation: 'Grundrisse, Fragment on Machines' }
    ],
    commentary: [
        { philosopher: 'Antonio Negri', text: 'Negri\u2019s Marx Beyond Marx: Lessons on the Grundrisse (1979; English 1991) is the most politically influential reading of the Grundrisse. Negri argued that the Grundrisse\u2019s analysis \u2014 especially the Fragment on Machines and the concept of the general intellect \u2014 opens a perspective on post-industrial capitalism that Capital\u2019s more schematic categories cannot provide. Negri\u2019s subsequent work with Michael Hardt (Empire, 2000; Multitude, 2004; Commonwealth, 2009) develops the concept of immaterial labour and cognitive capitalism from the Grundrisse.' }
    ],
    modernRelevance: 'The Grundrisse, particularly the Fragment on Machines and the concept of the general intellect, has become the primary Marxist resource for analyses of the knowledge economy, cognitive capitalism, and the contemporary crisis of value in the age of automation, artificial intelligence, and digital platforms. The claim that automation tends to undermine the labour theory of value \u2014 that as machines replace labour, wealth creation depends increasingly on collective knowledge rather than individual labour time \u2014 is directly relevant to contemporary debates about the future of work, universal basic income, and the political economy of artificial intelligence.',
    context: 'Written in London, August 1857 \u2013 May 1858, as private notebooks. First published in two volumes by the Marx-Engels-Lenin Institute in Moscow (1939\u201341), in very limited circulation. First widely available German edition: Dietz Verlag, Berlin, 1953. First English translation by Martin Nicolaus (Penguin, 1973). The Grundrisse was virtually unknown until the 1960s; its rediscovery transformed interpretation of Marx.',
    relatedWorks: ['capital-vol1', 'german-ideology', 'critique-political-economy-1859', 'economic-philosophical-manuscripts']
},

{
    id: 'critique-political-economy-1859',
    title: 'A Contribution to the Critique of Political Economy',
    greekTitle: 'Zur Kritik der politischen \u00d6konomie',
    philosopher: 'marx',
    category: 'practical',
    categoryLabel: 'Political Economy',
    date: '1859 AD',
    dateSort: 1859,
    emoji: '\uD83D\uDCCA',
    cardSize: 'normal',
    readingDifficulty: 'Intermediate',
    estimatedWordCount: 70000,
    shortDesc: 'The 1859 Preface \u2014 the most concise and most widely quoted statement of historical materialism \u2014 and Marx\u2019s first published analysis of the commodity and money that would be expanded into Capital, containing the programmatic summary of his entire life\u2019s work in a single paragraph.',
    summary: 'A Contribution to the Critique of Political Economy (Zur Kritik der politischen \u00d6konomie), published in Berlin by Franz Duncker in June 1859, was intended as the first instalment of a projected multi-volume Critique of Political Economy. The plan was abandoned when the book sold poorly; Marx eventually reworked its first two chapters (on the commodity and money) into the opening of Capital.\n\nThe work is remembered almost entirely for its Preface \u2014 one of the most frequently quoted and most programmatically significant passages in the history of social theory. In a few paragraphs, Marx summarises the materialist conception of history, the relationship between base and superstructure, and his own intellectual development with a concision and clarity unmatched anywhere else in his writings.\n\nThe programmatic summary: \u201cIn the social production of their existence, men inevitably enter into definite relations, which are independent of their will, namely relations of production appropriate to a given stage in the development of their material forces of production. The totality of these relations of production constitutes the economic structure of society, the real foundation, on which arises a legal and political superstructure and to which correspond definite forms of social consciousness. The mode of production of material life conditions the general process of social, political and intellectual life. It is not the consciousness of men that determines their existence, but their social existence that determines their consciousness.\u201d\n\nThe Preface also contains Marx\u2019s account of the conditions for social revolution: \u201cAt a certain stage of development, the material productive forces of society come into conflict with the existing relations of production... From forms of development of the productive forces these relations turn into their fetters. Then begins an era of social revolution.\u201d',
    themes: ['the 1859 Preface', 'base and superstructure stated programmatically', 'social existence determines consciousness', 'conditions for social revolution', 'the commodity and money', 'the intellectual autobiography'],
    keyCharacters: [],
    concepts: [
        'Relations of production \u2014 the social relations into which human beings enter in the process of production; independent of their will; the foundation of social life',
        'The economic structure as the real foundation \u2014 the totality of relations of production constitutes the economic base on which the legal, political, and ideological superstructure arises',
        'Social existence determines consciousness \u2014 the fundamental inversion of idealism: it is not consciousness but social existence that is determinative',
        'The conflict between productive forces and relations of production \u2014 the mechanism of social revolution: when relations of production become fetters on the development of productive forces, an era of social revolution begins',
        'The distinction between the economic transformation and its ideological forms \u2014 the conflict between productive forces and relations of production must be distinguished from the ideological forms (legal, political, religious, aesthetic, philosophical) in which men become conscious of it'
    ],
    structure: 'Preface: The intellectual autobiography; the materialist conception of history\n\nChapter I: The Commodity\n\u2014 Section 1: Use-value and exchange-value\n\u2014 Section 2: Labour embodied in commodities\n\u2014 Section 3: The value-form or exchange-value\n\nChapter II: Money or Simple Circulation\n\u2014 Section 1: The measure of values\n\u2014 Section 2: The medium of circulation\n\u2014 Section 3: Money',
    quote: 'It is not the consciousness of men that determines their existence, but their social existence that determines their consciousness.',
    additionalQuotes: [
        { text: 'At a certain stage of development, the material productive forces of society come into conflict with the existing relations of production. From forms of development of the productive forces these relations turn into their fetters. Then begins an era of social revolution.', citation: 'A Contribution to the Critique of Political Economy, Preface (1859)' },
        { text: 'No social order is ever destroyed before all the productive forces for which it is sufficient have been developed, and new superior relations of production never replace older ones before the material conditions for their existence have matured within the framework of the old society.', citation: 'A Contribution to the Critique of Political Economy, Preface (1859)' }
    ],
    commentary: [
        { philosopher: 'G.A. Cohen', text: 'Cohen\u2019s Karl Marx\u2019s Theory of History: A Defence (1978) takes the 1859 Preface as its primary text and attempts to reconstruct the claims it makes as a rigorous social-scientific theory. Cohen\u2019s reading \u2014 that the productive forces have primacy over the relations of production, and that the superstructure is functionally explained by its role in sustaining the base \u2014 became the standard formulation of \u201canalytical Marxism.\u201d' }
    ],
    modernRelevance: 'The 1859 Preface is the most widely quoted statement of historical materialism and the starting point for every discussion of the base-superstructure relationship in social theory. Its programmatic clarity has made it both the foundation of orthodox Marxist social theory and the primary target of revisionist and post-Marxist critiques.',
    context: 'Published by Franz Duncker in Berlin in June 1859. Dedicated to Wilhelm Wolff. The book sold poorly and was largely ignored. Marx himself regarded it as superseded by Capital and did not pursue the planned multi-volume project. The Preface became widely known only after Marx\u2019s death, when Engels promoted it as the canonical statement of historical materialism.',
    relatedWorks: ['capital-vol1', 'grundrisse', 'german-ideology', 'communist-manifesto']
},

{
    id: 'civil-war-in-france',
    title: 'The Civil War in France',
    greekTitle: 'Der B\u00fcrgerkrieg in Frankreich',
    philosopher: 'marx',
    category: 'practical',
    categoryLabel: 'Political Philosophy',
    date: '1871 AD',
    dateSort: 1871,
    emoji: '\uD83D\uDEA9',
    cardSize: 'normal',
    readingDifficulty: 'Intermediate',
    estimatedWordCount: 35000,
    shortDesc: 'Marx\u2019s analysis of the Paris Commune as the first workers\u2019 government in history \u2014 the living proof that the working class cannot simply take over the existing state machine but must smash it and replace it with new political forms based on the direct democracy of the armed people.',
    summary: 'The Civil War in France, written by Marx as an Address of the General Council of the International Working Men\u2019s Association and published on 30 May 1871, two days after the bloody suppression of the Paris Commune, is Marx\u2019s most important political text after the Communist Manifesto and the work that most directly addresses the question of what a workers\u2019 state would look like.\n\nThe Paris Commune \u2014 the revolutionary workers\u2019 government that held Paris for seventy-two days between 18 March and 28 May 1871 \u2014 was Marx\u2019s living laboratory. He had not predicted it and had initially advised the Paris workers against insurrection. But once it existed, he analysed it with extraordinary precision and concluded that it represented a new form of political organisation that transcended the limitations of bourgeois democracy.\n\nThe Commune\u2019s innovations as described by Marx: the replacement of a standing army by the armed people; the election of all officials by universal suffrage with the right of immediate recall; the payment of all officials at workers\u2019 wages; the fusion of legislative and executive power in the Communal Council; the abolition of the separate police; the expropriation of the Church\u2019s property and the secularisation of education. These were not utopian inventions but the practical measures through which the Commune organised itself.\n\nMarx\u2019s most important theoretical conclusion: \u201cThe working class cannot simply lay hold of the ready-made state machinery and wield it for its own purposes.\u201d The bourgeois state must be smashed, not captured; its bureaucratic-military machine must be replaced by the new political forms the Commune embodied. This conclusion \u2014 that the proletarian revolution requires the destruction of the existing state rather than its conquest \u2014 became the central issue dividing reformist from revolutionary socialism.',
    themes: ['the Paris Commune', 'the smashing of the state machine', 'workers\u2019 democracy', 'the Commune as political form', 'universal suffrage with recall', 'the armed people', 'the Commune and the International', 'Thiers and Versailles', 'the bloody week', 'bourgeois democracy vs workers\u2019 democracy'],
    keyCharacters: [
        { name: 'Adolphe Thiers', role: 'The head of the Versailles government that suppressed the Commune; the \u201cmurderous ferret\u201d; Marx\u2019s portrait of the bourgeoisie in its moment of counter-revolutionary terror' }
    ],
    concepts: [
        'The working class cannot simply lay hold of the ready-made state machinery \u2014 the fundamental political conclusion: the bourgeois state must be smashed, not captured; its bureaucratic-military machine must be replaced',
        'The Commune as the political form at last discovered \u2014 the Commune\u2019s innovations (elected officials with immediate recall, workers\u2019 wages, fusion of legislative and executive, armed people) as the model for proletarian self-governance',
        'Universal suffrage with immediate recall \u2014 the antidote to the passivity of bourgeois electoral democracy; officials who can be recalled at any time are genuine servants, not masters',
        'The dictatorship of the proletariat \u2014 Marx later described the Commune as an example of the dictatorship of the proletariat: not personal tyranny but the class rule of the working class over the bourgeoisie'
    ],
    structure: 'First Address (written 23 July 1870): The Franco-Prussian War\nSecond Address (written 9 September 1870): After Sedan\nThird Address (written 30 May 1871): The Civil War in France\n\u2014 The historical background\n\u2014 The Commune and its measures\n\u2014 The Commune as political form\n\u2014 The suppression and its meaning',
    quote: 'The working class cannot simply lay hold of the ready-made state machinery, and wield it for its own purposes.',
    additionalQuotes: [
        { text: 'The Commune was to be a working, not a parliamentary, body, executive and legislative at the same time.', citation: 'The Civil War in France, Third Address' },
        { text: 'If co-operative production is not to remain a sham and a snare; if it is to supersede the Capitalist system; if united co-operative societies are to regulate national production upon a common plan, what else would it be but Communism?', citation: 'The Civil War in France, Third Address' }
    ],
    commentary: [
        { philosopher: 'V.I. Lenin', text: 'Lenin\u2019s The State and Revolution (1917) builds its entire argument on The Civil War in France and the passages Marx added in the 1872 Preface to the Communist Manifesto. Lenin argued that Marx\u2019s central lesson from the Commune \u2014 that the state must be smashed, not captured \u2014 had been betrayed by the Second International\u2019s reformist Marxism. The Bolshevik revolution was Lenin\u2019s attempt to apply Marx\u2019s Commune lessons in Russia.' }
    ],
    modernRelevance: 'The Civil War in France is the primary Marxist text on the question of political form in a workers\u2019 revolution. The Commune\u2019s innovations \u2014 universal suffrage with recall, officials at workers\u2019 wages, the fusion of legislative and executive \u2014 have been the model for every subsequent attempt at workers\u2019 self-governance, from the Russian soviets through the Spanish anarchist collectives to contemporary participatory democracy experiments. The central question \u2014 can the working class use the existing state to transform society, or must it smash the state and create new political forms? \u2014 remains the dividing line between reformist and revolutionary socialism.',
    context: 'Written by Marx as an Address of the General Council of the International Working Men\u2019s Association, May 1871. Published 30 May 1871, two days after the suppression of the Commune. The 1872 editions added the crucial sentence to the Preface of the Communist Manifesto noting that the Commune had demonstrated that the working class cannot simply take hold of the ready-made state machinery.',
    relatedWorks: ['communist-manifesto', 'capital-vol1', 'critique-of-gotha-programme', 'german-ideology']
}

);
"""

# ── data-21e: Critique of Gotha Programme + Engels: Anti-Dühring + Origin ─────
files['data-21e.js'] = r"""/* DATA PART 21e — Marx & Engels: Critique of Gotha Programme + Anti-Dühring + Origin of the Family */
window.WORKS.push(

{
    id: 'critique-of-gotha-programme',
    title: 'Critique of the Gotha Programme',
    greekTitle: 'Kritik des Gothaer Programms',
    philosopher: 'marx',
    category: 'practical',
    categoryLabel: 'Political Philosophy',
    date: '1875 AD',
    dateSort: 1875,
    emoji: '\uD83C\uDFDB\uFE0F',
    cardSize: 'normal',
    readingDifficulty: 'Intermediate',
    estimatedWordCount: 15000,
    shortDesc: 'Marx\u2019s most explicit statement of communist political economy \u2014 the distinction between the lower (socialist) and higher (communist) phases of post-capitalist society, the critique of bourgeois right, and the famous formula: \u201cFrom each according to their ability, to each according to their need.\u201d',
    summary: 'Marginal Notes to the Programme of the German Workers\u2019 Party (Randglossen zum Programm der deutschen Arbeiterpartei) \u2014 universally known as the Critique of the Gotha Programme \u2014 written in May 1875 and first published by Engels in 1891 in Die Neue Zeit, is the most concentrated statement of Marx\u2019s mature political philosophy and his most explicit description of the transition from capitalism to communism.\n\nMarx wrote the Critique as private marginal notes on the draft programme being prepared for the unification congress of the two main German workers\u2019 parties at Gotha. He sent it to the party leadership with the instruction that it not be published; it was ignored at the time and published only after his death. Its influence on subsequent socialist and communist theory has been enormous.\n\nThe work\u2019s most important contribution is the distinction between two phases of post-capitalist society. The first phase (later called \u201csocialism\u201d by Lenin) is the immediate post-revolutionary period in which the old society\u2019s \u201cbirth-marks\u201d still persist: production is socialised but workers are still paid according to their contribution \u2014 \u201cfrom each according to their ability, to each according to their work.\u201d Bourgeois right (equal treatment for unequal individuals) still applies, because the society has not yet developed the productive capacity to distribute according to need.\n\nIn the higher phase \u2014 communism \u2014 the productive forces have developed to the point where scarcity is overcome, the enslaving subordination of individuals to the division of labour has ended, and labour has become not merely a means of life but life\u2019s prime want. At this point: \u201cFrom each according to their ability, to each according to their need.\u201d (Jeder nach seinen F\u00e4higkeiten, jedem nach seinen Bed\u00fcrfnissen.)\n\nThe Critique also contains Marx\u2019s sharpest analysis of bourgeois right: the formula of equal treatment for all workers ignores that workers are unequal in their capacities, family situations, and needs. Equal right applied to unequal individuals is a right of inequality. This is not an objection to socialist distribution in the first phase \u2014 it is the best available under the circumstances \u2014 but an explanation of why it falls short of genuine communist equality.',
    themes: ['the two phases of communist society', 'from each according to ability, to each according to need', 'bourgeois right and its limits', 'equal right as a right of inequality', 'the withering away of the state', 'the dictatorship of the proletariat', 'socialist vs communist distribution', 'the critique of Lassalleanism'],
    keyCharacters: [],
    concepts: [
        'The first phase of communist society \u2014 the immediate post-revolutionary period: production is socialised; workers are paid according to their contribution; bourgeois right still applies',
        'The higher phase of communist society \u2014 when productive forces are fully developed and scarcity overcome: \u201cFrom each according to their ability, to each according to their need\u201d',
        'Bourgeois right as a right of inequality \u2014 equal treatment for unequal individuals is not genuine equality; it privileges the stronger, healthier, and better-positioned worker',
        'The withering away of the state \u2014 in communist society, the state as an instrument of class domination becomes unnecessary and withers away; what replaces it is the self-administration of the associated producers',
        'The dictatorship of the proletariat \u2014 Marx\u2019s term for the political form of the transition period between capitalism and communism; the class rule of the working class'
    ],
    structure: 'I. Critique of Lassalle\u2019s formula on labour as the source of wealth\nII. Critique of the distribution principle (\u201cthe undiminished proceeds of labour\u201d)\nIII. The two phases of communist society; bourgeois right; the higher phase; the communist formula\nIV. The question of the state; the dictatorship of the proletariat; the withering away of the state\nV. Critique of the democratic demands',
    quote: 'From each according to his abilities, to each according to his needs!',
    additionalQuotes: [
        { text: 'Between capitalist and communist society there lies the period of the revolutionary transformation of the one into the other. Corresponding to this is also a political transition period in which the state can be nothing but the revolutionary dictatorship of the proletariat.', citation: 'Critique of the Gotha Programme, Part IV' },
        { text: 'Right can never be higher than the economic structure of society and the cultural development conditioned by it.', citation: 'Critique of the Gotha Programme, Part III' }
    ],
    commentary: [
        { philosopher: 'V.I. Lenin', text: 'Lenin\u2019s State and Revolution (1917) builds its account of the transition to communism almost entirely on the Critique of the Gotha Programme\u2019s distinction between the lower and higher phases. Lenin renamed the lower phase \u201csocialism\u201d and the higher phase \u201ccommunism,\u201d and took the dictatorship of the proletariat as the political form of the transition period. The entire architecture of Soviet ideology \u2014 the claim to be building \u201csocialism\u201d en route to \u201ccommunism\u201d \u2014 is derived from the Critique.' }
    ],
    modernRelevance: 'The Critique of the Gotha Programme is the primary Marxist text on distribution, justice, and the transition to communism. The formula \u201cfrom each according to their ability, to each according to their need\u201d has become the defining statement of communist aspiration. The analysis of bourgeois right as a right of inequality anticipates contemporary discussions of formal vs substantive equality, positive discrimination, and the limits of procedural justice. The distinction between socialist and communist phases has structured all subsequent debates about the relationship between reform and revolution.',
    context: 'Written in May 1875 as private marginal notes; sent to the party leadership with a request for confidentiality. First published by Engels in Die Neue Zeit, Vol. 1, 1890\u201391, over the objections of the party leadership. Marx died in 1883 without seeing it published. The standard text is in Marx-Engels Werke, Vol. 19.',
    relatedWorks: ['communist-manifesto', 'civil-war-in-france', 'capital-vol1', 'german-ideology']
},

{
    id: 'anti-duhring',
    title: 'Anti-D\u00fchring: Herr Eugen D\u00fchring\u2019s Revolution in Science',
    greekTitle: 'Herrn Eugen D\u00fchrings Umw\u00e4lzung der Wissenschaft',
    philosopher: 'marx',
    category: 'method',
    categoryLabel: 'Philosophy of Science',
    date: '1878 AD',
    dateSort: 1878,
    emoji: '\uD83D\uDD2C',
    cardSize: 'normal',
    readingDifficulty: 'Intermediate',
    estimatedWordCount: 180000,
    shortDesc: 'Engels\u2019s most systematic philosophical work \u2014 the critique of Dühring that became the primary vehicle of dialectical materialism, providing the philosophical foundations of scientific socialism through the application of the dialectical method to nature, history, and political economy.',
    summary: 'Herr Eugen D\u00fchring\u2019s Revolution in Science (Herrn Eugen D\u00fchrings Umw\u00e4lzung der Wissenschaft), written by Engels between 1876 and 1878 and published serially in the party newspaper Vorw\u00e4rts before appearing as a book in 1878 (Leipzig, Genossenschaftsbuchdruckerei), is Engels\u2019s most comprehensive philosophical work and the text that did more than any other to shape the philosophical framework of orthodox Marxism.\n\nEugen D\u00fchring was a Berlin academic who proposed an eclectic \u201crevolution in science\u201d combining positivism, political economy, and a \u201cforce theory\u201d of history. He was gaining considerable influence in the German Social Democratic Party when Engels undertook to refute him systematically. The refutation required Engels to address philosophy, natural science, and political economy \u2014 and in doing so, to work out a comprehensive account of the Marxist method.\n\nThe work\u2019s most important sections are the philosophical chapters on dialectics and the philosophy of nature. Engels argues for a dialectical materialism \u2014 the application of Hegel\u2019s dialectical method (stripped of its idealist content) to material reality. The three \u201claws of the dialectic\u201d that Engels articulates \u2014 the transformation of quantity into quality, the interpenetration of opposites, and the negation of the negation \u2014 are presented as laws governing both natural and social development.\n\nThe chapters on political economy develop and defend the labour theory of value and the theory of surplus value. Three chapters on socialism provide the most accessible introduction to \u201cscientific socialism\u201d \u2014 the claim that Marx\u2019s socialism is distinguished from utopian socialism by its scientific grounding in the analysis of capitalism\u2019s actual development. Engels later extracted these three chapters as the pamphlet Socialism: Utopian and Scientific (1880), which became the most widely read introduction to Marxism in the late nineteenth and early twentieth centuries.',
    themes: ['dialectical materialism', 'the three laws of the dialectic', 'scientific socialism vs utopian socialism', 'the labour theory of value', 'the philosophy of nature', 'force theory of history', 'the negation of the negation', 'quantity and quality', 'the interpenetration of opposites'],
    keyCharacters: [
        { name: 'Eugen D\u00fchring', role: 'The Berlin academic whose eclectic \u201crevolution in science\u201d Engels systematically refutes; his influence in the Social Democratic Party prompted the comprehensive philosophical response' }
    ],
    concepts: [
        'Dialectical materialism \u2014 the application of Hegel\u2019s dialectical method to material reality; the laws governing the development of nature and society',
        'The transformation of quantity into quality \u2014 the first law: quantitative changes accumulate until a qualitative transformation occurs; water heating to boiling point',
        'The interpenetration of opposites \u2014 the second law: every phenomenon contains its own contradiction; development proceeds through the conflict of opposites',
        'The negation of the negation \u2014 the third law: development proceeds through negation and the negation of the negation, producing a higher synthesis that preserves and elevates what it negates',
        'Scientific vs utopian socialism \u2014 utopian socialism appeals to reason and justice; scientific socialism derives communism from the analysis of capitalism\u2019s actual contradictions and tendencies'
    ],
    structure: 'Introduction: General\n\nPart I: Philosophy\n\u2014 Classification; priori stics; World Schematism\n\u2014 Dialectics: Quantity and Quality; Negation of the Negation\n\u2014 Morality and Law; Eternal Truths\n\u2014 Philosophy of Nature\n\nPart II: Political Economy\n\u2014 Subject Matter and Method\n\u2014 Theory of Force\n\u2014 Theory of Value; Simple and Compound Labour\n\u2014 Capital and Surplus Value\n\nPart III: Socialism\n\u2014 Historical; Theoretical; Production; Distribution\n[Three chapters on socialism extracted as \u201cSocialism: Utopian and Scientific\u201d (1880)]',
    quote: 'It was seen that all past history was the history of class struggles; that these warring classes of society are always the products of the modes of production and exchange \u2014 in a word, of the economic conditions of their time.',
    additionalQuotes: [
        { text: 'The materialist conception of history starts from the proposition that the production of the means to support human life and, next to production, the exchange of things produced, is the basis of all social structure.', citation: 'Anti-D\u00fchring, Preface to the Second Edition (1885)' }
    ],
    commentary: [
        { philosopher: 'Louis Althusser', text: 'Althusser\u2019s critique of Engels\u2019s dialectical materialism \u2014 developed in Reading Capital and For Marx \u2014 is one of the most sustained in twentieth-century Marxism. Althusser argued that Engels\u2019s extension of the dialectic to nature is philosophically incoherent and politically dangerous: it produces a mechanical determinism that removes the space for revolutionary agency. The \u201cthree laws\u201d of the dialectic are Engels\u2019s invention, not Marx\u2019s, and they betray the specific character of the social dialectic by assimilating it to natural science.' }
    ],
    modernRelevance: 'Anti-D\u00fchring and its derivative Socialism: Utopian and Scientific were the primary vehicles for the philosophical education of socialist and communist parties from the 1880s through the mid-twentieth century. The concept of dialectical materialism \u2014 however contested \u2014 became the official philosophy of the Soviet Union and of communist parties worldwide. Contemporary debates about the relationship between Marx and Engels, about the status of Engels\u2019s \u201cdialectics of nature,\u201d and about the philosophical coherence of Marxism all take Anti-D\u00fchring as their primary reference point.',
    context: 'Written by Engels between 1876 and 1878, serialised in Vorw\u00e4rts, and published as a book in Leipzig in 1878. Marx read the manuscript and contributed the historical section on political economy in Part II. Engels extracted three chapters as Socialism: Utopian and Scientific (1880), which was translated into French in 1880 with a preface by Marx and became the most widely read introduction to Marxism. Standard text in Marx-Engels Werke, Vol. 20.',
    relatedWorks: ['communist-manifesto', 'german-ideology', 'capital-vol1', 'origin-of-family']
},

{
    id: 'origin-of-family',
    title: 'The Origin of the Family, Private Property and the State',
    greekTitle: 'Der Ursprung der Familie, des Privateigentums und des Staats',
    philosopher: 'marx',
    category: 'practical',
    categoryLabel: 'Political Philosophy & Anthropology',
    date: '1884 AD',
    dateSort: 1884,
    emoji: '\uD83C\uDFDB\uFE0F',
    cardSize: 'normal',
    readingDifficulty: 'Intermediate',
    estimatedWordCount: 100000,
    shortDesc: 'Engels\u2019s application of historical materialism to the family, private property, and the state \u2014 arguing that monogamous marriage, the nuclear family, and female subordination are not natural but historical, arising with private property and class society, and destined to dissolve with it.',
    summary: 'The Origin of the Family, Private Property and the State: In the Light of the Researches of Lewis H. Morgan (Der Ursprung der Familie, des Privateigentums und des Staats: Im Anschluss an Lewis H. Morgan\u2019s Forschungen), written by Engels in two months following Marx\u2019s death and published by Hottingen-Z\u00fcrich in October 1884, is the foundational text of Marxist anthropology and feminist Marxism.\n\nThe work is based primarily on Lewis H. Morgan\u2019s Ancient Society (1877), which Marx had studied carefully and annotated extensively in his final years. Morgan argued that human society had passed through three stages: savagery, barbarism, and civilisation \u2014 and that the transition to civilisation was marked by the emergence of private property, the state, and the patriarchal family. Engels develops Morgan\u2019s anthropological findings through the lens of historical materialism.\n\nThe work\u2019s central argument: the family, private property, and the state are not eternal or natural institutions but historical products of specific economic conditions. The monogamous nuclear family, with its double standard of female chastity and male promiscuity, arose with private property: wealthy men needed certainty of paternity to ensure inheritance. The subordination of women to men within the family is the historical expression of the subordination of wage labour to capital. Engels\u2019s famous formulation: within the family, the man is the bourgeois; the wife represents the proletariat.\n\nThe state, similarly, is not a neutral arbiter of social conflict but an instrument of class domination: it arose when class divisions made it necessary for the economically dominant class to maintain its position through organised force. With the abolition of classes, the state will wither away, replaced by the \u201cself-administration of the associated producers.\u201d\n\nThe work anticipates socialist feminism: the emancipation of women requires not only formal legal equality but the transformation of the economic basis of family life \u2014 the socialisation of domestic labour, the incorporation of women into social production, and the abolition of the economic dependence of women on men.',
    themes: ['the historical origins of the family', 'monogamy and private property', 'the world historic defeat of the female sex', 'the state as instrument of class domination', 'the withering away of the state', 'socialist feminism', 'Morgan\u2019s anthropology', 'savagery, barbarism, civilisation'],
    keyCharacters: [
        { name: 'Lewis H. Morgan', role: 'The American anthropologist whose Ancient Society (1877) provided the empirical foundation for Engels\u2019s historical analysis of the family and property relations' }
    ],
    concepts: [
        'The family as historical, not natural \u2014 the monogamous nuclear family arose with private property; it is a specific historical form, not an eternal institution',
        'Monogamy as class institution \u2014 monogamy for women ensures male certainty of paternity and inheritance; the double standard (monogamy for women, promiscuity tolerated for men) reflects this',
        'The world historic defeat of the female sex \u2014 the transition from matrilineal to patrilineal descent \u2014 which Engels calls the \u201cworld historic defeat of the female sex\u201d \u2014 accompanied the rise of private property',
        'Within the family, the man is the bourgeois; the wife represents the proletariat \u2014 Engels\u2019s analogy between class exploitation and gender domination',
        'The state as instrument of class domination \u2014 the state arose with class society to maintain the dominance of the economically powerful; with the abolition of classes, it will wither away',
        'Socialist feminism \u2014 women\u2019s emancipation requires not only formal equality but the socialisation of domestic labour and women\u2019s full integration into social production'
    ],
    structure: 'Preface to the First Edition (1884)\n\nI. Prehistoric Stages of Culture (Morgan\u2019s periodisation)\nII. The Family\n\u2014 The Punaluan Family; the Pairing Family\n\u2014 The Monogamous Family: its origin in private property\nIII. The Iroquois Gens\nIV. The Greek Gens\nV. The Rise of the Athenian State\nVI. The Gens and the State in Rome\nVII. The Gens Among the Celts and Germans\nVIII. The Formation of the State Among the Germans\nIX. Barbarism and Civilisation',
    quote: 'The first class antagonism which appears in history coincides with the development of the antagonism between man and woman in monogamous marriage, and the first class oppression with that of the female sex by the male.',
    additionalQuotes: [
        { text: 'The modern individual family is based on the open or disguised domestic enslavement of the woman; and modern society is a mass composed solely of individual families as its molecules. In the great majority of cases today, at least in the possessing classes, the husband is obliged to earn a living and support his family, and that in itself gives him a position of supremacy without any need for special legal titles and privileges.', citation: 'Origin of the Family, Part II, Section 4' },
        { text: 'The state is not \u201can arbitrarily created force\u201d but a product of society at a certain stage of development; it is the admission that this society has become entangled in an insoluble contradiction with itself.', citation: 'Origin of the Family, Part IX' }
    ],
    commentary: [
        { philosopher: 'Simone de Beauvoir', text: 'De Beauvoir\u2019s The Second Sex (1949) engages critically with Engels\u2019s analysis. De Beauvoir accepts the historical argument that women\u2019s subordination is not natural but historical, but she argues that Engels reduces women\u2019s oppression entirely to economic causes: if women were simply integrated into social production on equal terms, oppression would end. De Beauvoir insists that patriarchal ideology has a semi-autonomous existence that cannot be dissolved by economic transformation alone.' },
        { philosopher: 'Shulamith Firestone', text: 'Firestone\u2019s The Dialectic of Sex (1970) extends and radicalises Engels\u2019s analysis. Firestone accepts the Engelsian insight that the family is the primary site of women\u2019s oppression but argues that Engels stops too soon: the material basis of women\u2019s oppression is not simply property relations but the biological facts of reproduction. A genuinely feminist materialism must include a dialectics of sex alongside the dialectics of class.' }
    ],
    modernRelevance: 'The Origin of the Family is the founding text of socialist feminism and of the Marxist analysis of gender, reproduction, and the family. The argument that women\u2019s domestic labour is a form of unpaid work that sustains capital accumulation has been developed by feminist economists into the \u201cwages for housework\u201d debate (Federici, Dalla Costa) and the analysis of social reproduction (Bhattacharya). The analysis of the state as an instrument of class domination that will wither away with classes is the foundational text of anarchist and libertarian socialist critiques of the state. The concept of the \u201cworld historic defeat of the female sex\u201d anticipates contemporary feminist analyses of the prehistory of patriarchy.',
    context: 'Written by Engels in March\u2013May 1884, following Marx\u2019s death in March 1883. Engels used Marx\u2019s extensive notes on Morgan\u2019s Ancient Society as a foundation. Published in Hottingen-Z\u00fcrich in October 1884. Engels described it as \u201cthe fulfilment of a bequest\u201d to Marx. Four subsequent editions (1886, 1889, 1891, with a new preface for the fourth edition in 1891) incorporated further anthropological research. Standard text in Marx-Engels Werke, Vol. 21.',
    relatedWorks: ['communist-manifesto', 'capital-vol1', 'german-ideology', 'anti-duhring']
}

);
"""

for fname, content in files.items():
    path = os.path.join(js, fname)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'  Written {fname}  ({content.count(chr(10))} lines)')
