"""
╔══════════════════════════════════════════════════════════╗
║  questions_premium.py — Kesyon Eksklizif Premium         ║
║  Plus difficiles, plus variées, 3 langues                ║
╚══════════════════════════════════════════════════════════╝
"""

# Chak kesyon gen: q_ht, q_fr, q_en, opts_ht, opts_fr, opts_en, ans, tier
# tier: "premium" = eksklizif, "free" = disponib pou tout moun
# Kat kategori eksklizif premium + nivle gwo difikilte

QUESTIONS_PREMIUM = {

  # ── FILOZOFI & LOJIK (Eksklizif Premium) ────────────────────────────────────
  "philo": {
    "medium": [
      {"q_ht":"Ki moun ki di 'Cogito ergo sum' (Mwen panse, donk mwen egziste)?",
       "q_fr":"Qui a dit 'Cogito ergo sum' (Je pense donc je suis)?",
       "q_en":"Who said 'Cogito ergo sum' (I think therefore I am)?",
       "opts_ht":["Platon","Aristotle","Descartes","Kant"],
       "opts_fr":["Platon","Aristote","Descartes","Kant"],
       "opts_en":["Plato","Aristotle","Descartes","Kant"],"ans":2,"tier":"premium"},

      {"q_ht":"Ki teori Platon ki di reyalite a se lonbray yon mond pafè?",
       "q_fr":"Quelle théorie de Platon dit que la réalité est l'ombre d'un monde parfait?",
       "q_en":"Which Plato theory says reality is a shadow of a perfect world?",
       "opts_ht":["Teorem Fòm","Myopman Groto","Teorem Idéyal","Myopman Gòt"],
       "opts_fr":["Théorie des Formes","Allégorie de la Caverne","Théorie Idéale","Mythe du Goût"],
       "opts_en":["Theory of Forms","Allegory of the Cave","Ideal Theory","Myth of Taste"],"ans":1,"tier":"premium"},

      {"q_ht":"Ki moun ki kreye konsèp 'Superman' (Übermensch)?",
       "q_fr":"Qui a créé le concept de 'Surhomme' (Übermensch)?",
       "q_en":"Who created the concept of 'Superman' (Übermensch)?",
       "opts_ht":["Hegel","Marx","Nietzsche","Schopenhauer"],
       "opts_fr":["Hegel","Marx","Nietzsche","Schopenhauer"],
       "opts_en":["Hegel","Marx","Nietzsche","Schopenhauer"],"ans":2,"tier":"premium"},

      {"q_ht":"Ki moun ki ekri 'Critique de la raison pure'?",
       "q_fr":"Qui a écrit 'Critique de la raison pure'?",
       "q_en":"Who wrote 'Critique of Pure Reason'?",
       "opts_ht":["Hume","Kant","Rousseau","Locke"],
       "opts_fr":["Hume","Kant","Rousseau","Locke"],
       "opts_en":["Hume","Kant","Rousseau","Locke"],"ans":1,"tier":"premium"},

      {"q_ht":"Ki filozofi ki di bonè a se nan plezi sansiblèl?",
       "q_fr":"Quelle philosophie dit que le bonheur réside dans le plaisir sensible?",
       "q_en":"Which philosophy says happiness lies in sensual pleasure?",
       "opts_ht":["Stoïsism","Epikireanism","Sinikism","Edonism"],
       "opts_fr":["Stoïcisme","Épicurisme","Cynisme","Hédonisme"],
       "opts_en":["Stoicism","Epicureanism","Cynicism","Hedonism"],"ans":1,"tier":"premium"},
    ],
    "hard": [
      {"q_ht":"Ki teori ki di objè a gen yon natir esansyèl ki preede egzistans li?",
       "q_fr":"Quelle théorie dit que l'essence précède l'existence?",
       "q_en":"Which theory states that essence precedes existence?",
       "opts_ht":["Egzistansyalism","Esansyalism","Fènomenoloji","Egzistantialism"],
       "opts_fr":["Existentialisme","Essentialisme","Phénoménologie","Existantialisme"],
       "opts_en":["Existentialism","Essentialism","Phenomenology","Existantialism"],"ans":1,"tier":"premium"},

      {"q_ht":"Ki moun ki di 'L'enfer c'est les autres'?",
       "q_fr":"Qui a dit 'L'enfer c'est les autres'?",
       "q_en":"Who said 'Hell is other people'?",
       "opts_ht":["Camus","Beauvoir","Sartre","Merleau-Ponty"],
       "opts_fr":["Camus","Beauvoir","Sartre","Merleau-Ponty"],
       "opts_en":["Camus","Beauvoir","Sartre","Merleau-Ponty"],"ans":2,"tier":"premium"},

      {"q_ht":"Ki paradoks ki di yon kò a pa ka janm rive kote li vle ale?",
       "q_fr":"Quel paradoxe dit qu'un corps ne peut jamais atteindre sa destination?",
       "q_en":"Which paradox says a body can never reach its destination?",
       "opts_ht":["Paradoks Achil","Paradoks Fals","Paradoks Dikotomi Zenon","Paradoks Sèk"],
       "opts_fr":["Paradoxe d'Achille","Paradoxe du Faussaire","Paradoxe de la Dichotomie de Zénon","Paradoxe du Cercle"],
       "opts_en":["Achilles Paradox","False Paradox","Zeno's Dichotomy Paradox","Circle Paradox"],"ans":2,"tier":"premium"},
    ],
  },

  # ── EKONOMI & BIZNIS (Eksklizif Premium) ────────────────────────────────────
  "economy": {
    "medium": [
      {"q_ht":"Ki lwa ekonomik ki di pi ou pwodui yon pwodui, pi pri li desann?",
       "q_fr":"Quelle loi économique dit que plus on produit, plus le prix baisse?",
       "q_en":"Which economic law says the more you produce, the lower the price?",
       "opts_ht":["Lwa Ofr ak Demand","Lwa Randman Dekrwasan","Lwa Ekonomi Echèl","Lwa Marginalism"],
       "opts_fr":["Loi Offre et Demande","Loi Rendements Décroissants","Loi Économies d'Échelle","Marginalisme"],
       "opts_en":["Law of Supply and Demand","Law of Diminishing Returns","Economies of Scale","Marginalism"],"ans":2,"tier":"premium"},

      {"q_ht":"Ki moun ki ekri 'Richesse des Nations' (1776)?",
       "q_fr":"Qui a écrit 'La Richesse des Nations' (1776)?",
       "q_en":"Who wrote 'The Wealth of Nations' (1776)?",
       "opts_ht":["Keynes","Ricardo","Adam Smith","Malthus"],
       "opts_fr":["Keynes","Ricardo","Adam Smith","Malthus"],
       "opts_en":["Keynes","Ricardo","Adam Smith","Malthus"],"ans":2,"tier":"premium"},

      {"q_ht":"Ki siyifikasyon PIB?",
       "q_fr":"Que signifie PIB?",
       "q_en":"What does GDP stand for?",
       "opts_ht":["Pwodui Entèn Brit","Pwen Enterè Bankye","Pwofi Enpò Biznis","Pèt Inik Brital"],
       "opts_fr":["Produit Intérieur Brut","Point d'Intérêt Bancaire","Profit Import Brut","Perte Unique Brutale"],
       "opts_en":["Gross Domestic Product","Government Debt Percentage","General Development Plan","Gross Demand Profit"],"ans":0,"tier":"premium"},

      {"q_ht":"Ki teori ekonomik Keynes defann?",
       "q_fr":"Quelle théorie économique Keynes défendait-il?",
       "q_en":"Which economic theory did Keynes advocate?",
       "opts_ht":["Liberalism","Marxism","Entèvansyonism Eta","Monetarism"],
       "opts_fr":["Libéralisme","Marxisme","Interventionnisme d'État","Monétarisme"],
       "opts_en":["Liberalism","Marxism","State Interventionism","Monetarism"],"ans":2,"tier":"premium"},

      {"q_ht":"Ki monnaie ki pi chè valè nan mond lan?",
       "q_fr":"Quelle est la monnaie la plus chère du monde?",
       "q_en":"What is the most valuable currency in the world?",
       "opts_ht":["Dola Ameriken","Euro","Dinar Kiwèt","Pound Angle"],
       "opts_fr":["Dollar américain","Euro","Dinar koweïtien","Livre sterling"],
       "opts_en":["US Dollar","Euro","Kuwaiti Dinar","British Pound"],"ans":2,"tier":"premium"},
    ],
    "hard": [
      {"q_ht":"Ki efè ekonomik ki di depans piblik ogmante revni total plis pase depans la menm?",
       "q_fr":"Quel effet économique dit que les dépenses publiques augmentent le revenu total plus que la dépense elle-même?",
       "q_en":"Which economic effect says public spending increases total income more than the spending itself?",
       "opts_ht":["Efè Multiplikatè","Efè Fowl","Efè Leve","Efè Parasite"],
       "opts_fr":["Effet multiplicateur","Effet de levier","Effet de seuil","Effet parasite"],
       "opts_en":["Multiplier Effect","Leverage Effect","Threshold Effect","Free Rider Effect"],"ans":0,"tier":"premium"},

      {"q_ht":"Ki teori di distribisyon revni ant faktè pwodwiksyon yo?",
       "q_fr":"Quelle théorie traite de la distribution des revenus entre les facteurs de production?",
       "q_en":"Which theory deals with income distribution among factors of production?",
       "opts_ht":["Teorem Ricardo","Teorem Marshall","Teorem Pareto","Teorem Walras"],
       "opts_fr":["Théorème de Ricardo","Théorème de Marshall","Théorème de Pareto","Équilibre de Walras"],
       "opts_en":["Ricardo's theorem","Marshall's theorem","Pareto optimality","Walras equilibrium"],"ans":2,"tier":"premium"},
    ],
  },

  # ── SYANS AVANSE (Eksklizif Premium) ────────────────────────────────────────
  "advanced_sci": {
    "hard": [
      {"q_ht":"Ki teori Einstein ki di mas ak énerji se menm bagay?",
       "q_fr":"Quelle théorie d'Einstein dit que masse et énergie sont équivalentes?",
       "q_en":"Which Einstein theory says mass and energy are equivalent?",
       "opts_ht":["Relativite Espesyal","Relativite Jeneral","Mekanik Kantik","Termodynamik"],
       "opts_fr":["Relativité Restreinte","Relativité Générale","Mécanique Quantique","Thermodynamique"],
       "opts_en":["Special Relativity","General Relativity","Quantum Mechanics","Thermodynamics"],"ans":0,"tier":"premium"},

      {"q_ht":"Ki fenomèn ki di yon patikil ka pase nan yon baryè enèji li pa ta ka pase klassikman?",
       "q_fr":"Quel phénomène dit qu'une particule peut traverser une barrière d'énergie classiquement infranchissable?",
       "q_en":"Which phenomenon says a particle can pass through an energy barrier classically impossible?",
       "opts_ht":["Entèferans","Entrikasyon","Efè Tunel","Siperpoze"],
       "opts_fr":["Interférence","Intrication","Effet tunnel","Superposition"],
       "opts_en":["Interference","Entanglement","Tunnel effect","Superposition"],"ans":2,"tier":"premium"},

      {"q_ht":"Ki teori unifye fòs gravitasyon ak mekanism kantik?",
       "q_fr":"Quelle théorie unifie la gravitation et la mécanique quantique?",
       "q_en":"Which theory unifies gravity and quantum mechanics?",
       "opts_ht":["M-teori","Teorim Kòd","Teorem Boucle Gravitasyon Kantik","Tout Twa yo"],
       "opts_fr":["Théorie M","Théorie des Cordes","Gravitation Quantique à Boucles","Toutes les trois"],
       "opts_en":["M-theory","String Theory","Loop Quantum Gravity","All three are attempts"],"ans":3,"tier":"premium"},

      {"q_ht":"Ki patikil ki te dekouvri nan CERN an 2012?",
       "q_fr":"Quelle particule a été découverte au CERN en 2012?",
       "q_en":"Which particle was discovered at CERN in 2012?",
       "opts_ht":["Neutrinò","Bozon Higgs","Kwak","Gliyon"],
       "opts_fr":["Neutrino","Boson de Higgs","Quark","Gluon"],
       "opts_en":["Neutrino","Higgs Boson","Quark","Gluon"],"ans":1,"tier":"premium"},

      {"q_ht":"Ki nòm pou yon eta matye kote yon gaz rafwadi anba tandans Bose-Einstein?",
       "q_fr":"Quel est le nom de l'état de la matière d'un gaz refroidi selon la condensation Bose-Einstein?",
       "q_en":"What is the state of matter of a gas cooled via Bose-Einstein condensation?",
       "opts_ht":["Plasma","Kondansa Bose-Einstein","Superfluide","Kondiktè"],
       "opts_fr":["Plasma","Condensat de Bose-Einstein","Superfluide","Supraconducteur"],
       "opts_en":["Plasma","Bose-Einstein Condensate","Superfluid","Superconductor"],"ans":1,"tier":"premium"},
    ],
  },

  # ── ISTWA MONDYAL AVANSE (Questions plus profondes) ──────────────────────────
  "world_hist": {
    "hard": [
      {"q_ht":"Ki ane Anpi Romen Oksidantal la te tonbe?",
       "q_fr":"En quelle année l'Empire romain d'Occident est-il tombé?",
       "q_en":"In what year did the Western Roman Empire fall?",
       "opts_ht":["410","455","476","493"],
       "opts_fr":["410","455","476","493"],
       "opts_en":["410","455","476","493"],"ans":2,"tier":"premium"},

      {"q_ht":"Ki batay ki te deside dominasyon Britanik nan Zend an 1757?",
       "q_fr":"Quelle bataille a décidé de la domination britannique en Inde en 1757?",
       "q_en":"Which battle decided British dominance in India in 1757?",
       "opts_ht":["Batay Plassey","Batay Paniput","Batay Wandiwash","Batay Buxar"],
       "opts_fr":["Bataille de Plassey","Bataille de Panipat","Bataille de Wandiwash","Bataille de Buxar"],
       "opts_en":["Battle of Plassey","Battle of Panipat","Battle of Wandiwash","Battle of Buxar"],"ans":0,"tier":"premium"},

      {"q_ht":"Ki anpi ki te pi gran nan istwa?",
       "q_fr":"Quel empire fut le plus vaste de l'histoire?",
       "q_en":"Which empire was the largest in history?",
       "opts_ht":["Anpi Britanik","Anpi Mongòl","Anpi Romen","Anpi Otoman"],
       "opts_fr":["Empire Britannique","Empire Mongol","Empire Romain","Empire Ottoman"],
       "opts_en":["British Empire","Mongol Empire","Roman Empire","Ottoman Empire"],"ans":0,"tier":"premium"},

      {"q_ht":"Ki trete ki te kreye Sosyete Nasyon yo (anvan ONU) apre WW1?",
       "q_fr":"Quel traité créa la Société des Nations (avant l'ONU) après la WW1?",
       "q_en":"Which treaty created the League of Nations (before the UN) after WW1?",
       "opts_ht":["Trete Versay","Trete Sen-Jèrmen","Trete Neuilly","Trete Sevr"],
       "opts_fr":["Traité de Versailles","Traité de Saint-Germain","Traité de Neuilly","Traité de Sèvres"],
       "opts_en":["Treaty of Versailles","Treaty of Saint-Germain","Treaty of Neuilly","Treaty of Sèvres"],"ans":0,"tier":"premium"},
    ],
  },

  # ── TEKNOLOJI AVANSE (Eksklizif Premium) ────────────────────────────────────
  "advanced_tech": {
    "hard": [
      {"q_ht":"Ki diferans ant Machine Learning ak Deep Learning?",
       "q_fr":"Quelle est la différence entre Machine Learning et Deep Learning?",
       "q_en":"What is the difference between Machine Learning and Deep Learning?",
       "opts_ht":["Menm bagay","DL itilize rezo neyiral ki fon","ML pi rapid","DL pi vye"],
       "opts_fr":["C'est pareil","DL utilise des réseaux neuronaux profonds","ML est plus rapide","DL est plus ancien"],
       "opts_en":["Same thing","DL uses deep neural networks","ML is faster","DL is older"],"ans":1,"tier":"premium"},

      {"q_ht":"Ki algoritm ki bay baz Transformer achitekti (ChatGPT, etc.)?",
       "q_fr":"Quel algorithme est à la base de l'architecture Transformer (ChatGPT, etc.)?",
       "q_en":"Which algorithm underlies the Transformer architecture (ChatGPT, etc.)?",
       "opts_ht":["LSTM","Atansyon Mekanis","CNN","RNN"],
       "opts_fr":["LSTM","Mécanisme d'Attention","CNN","RNN"],
       "opts_en":["LSTM","Attention Mechanism","CNN","RNN"],"ans":1,"tier":"premium"},

      {"q_ht":"Ki pwoblèm fondamantal algoritmik ki pa rezoud?",
       "q_fr":"Quel problème algorithmique fondamental n'est pas résolu?",
       "q_en":"Which fundamental algorithmic problem remains unsolved?",
       "opts_ht":["Tri","Rechèch Binè","P vs NP","Faktorizasyon"],
       "opts_fr":["Tri","Recherche Binaire","P contre NP","Factorisation"],
       "opts_en":["Sorting","Binary Search","P vs NP","Factorization"],"ans":2,"tier":"premium"},

      {"q_ht":"Ki pwotokòl konsensus Ethereum itilize depi 'The Merge' 2022?",
       "q_fr":"Quel protocole de consensus Ethereum utilise depuis 'The Merge' 2022?",
       "q_en":"Which consensus protocol does Ethereum use since 'The Merge' 2022?",
       "opts_ht":["Proof of Work","Proof of Stake","Delegated PoS","Proof of Authority"],
       "opts_fr":["Preuve de Travail","Preuve d'Enjeu","PoS Délégué","Preuve d'Autorité"],
       "opts_en":["Proof of Work","Proof of Stake","Delegated PoS","Proof of Authority"],"ans":1,"tier":"premium"},
    ],
  },

}

# ── QUESTIONS FREE AMÉLIORÉES (pou tou moun men pi enteresan) ─────────────────
QUESTIONS_FREE_BONUS = {
  "culture_pop": {
    "easy": [
      {"q_ht":"Ki moun ki chante 'Thriller' (1982)?",
       "q_fr":"Qui a chanté 'Thriller' (1982)?",
       "q_en":"Who sang 'Thriller' (1982)?",
       "opts_ht":["Prince","Michael Jackson","Madonna","Whitney Houston"],
       "opts_fr":["Prince","Michael Jackson","Madonna","Whitney Houston"],
       "opts_en":["Prince","Michael Jackson","Madonna","Whitney Houston"],"ans":1,"tier":"free"},

      {"q_ht":"Ki fim ki fè pi plis lajan nan istwa sinema?",
       "q_fr":"Quel film a le plus rapporté dans l'histoire du cinéma?",
       "q_en":"Which film has made the most money in cinema history?",
       "opts_ht":["Titanic","Avengers Endgame","Avatar","Star Wars"],
       "opts_fr":["Titanic","Avengers Endgame","Avatar","Star Wars"],
       "opts_en":["Titanic","Avengers Endgame","Avatar","Star Wars"],"ans":2,"tier":"free"},

      {"q_ht":"Ki jeu video ki pi vann nan tout tan?",
       "q_fr":"Quel jeu vidéo s'est le plus vendu de tous les temps?",
       "q_en":"What is the best-selling video game of all time?",
       "opts_ht":["Fortnite","GTA V","Minecraft","Tetris"],
       "opts_fr":["Fortnite","GTA V","Minecraft","Tetris"],
       "opts_en":["Fortnite","GTA V","Minecraft","Tetris"],"ans":2,"tier":"free"},
    ],
  },
}

def get_premium_categories():
    """Retounen lis kategori premium yo."""
    return list(QUESTIONS_PREMIUM.keys())

def get_premium_question_pool(category: str, difficulty: str) -> list:
    """Retounen pool kesyon premium pou yon kategori ak nivo."""
    cat = QUESTIONS_PREMIUM.get(category, {})
    return cat.get(difficulty, [])

def is_premium_category(category: str) -> bool:
    """Verifye si yon kategori se premium sèlman."""
    return category in QUESTIONS_PREMIUM
