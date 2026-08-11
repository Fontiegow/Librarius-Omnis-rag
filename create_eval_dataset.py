from pathlib import Path
import json


# ============================================================
# Configuration
# ============================================================

# ============================================================
# Project paths
# ============================================================

# The directory containing create_eval_dataset.py
PROJECT_ROOT = Path(__file__).resolve().parent

EVALS_DIR = PROJECT_ROOT / "evals"
QUESTIONS_DIR = EVALS_DIR / "questions"

# ============================================================
# Evaluation questions
# ============================================================

questions = [

    # --------------------------------------------------------
    # BASIC / EASY
    # --------------------------------------------------------

    {
        "id": "WH40K-001",
        "question": "Who is the Primarch of the Ultramarines?",
        "ground_truth": {
            "answer": "Roboute Guilliman.",
            "key_facts": [
                "Roboute Guilliman is the Primarch of the Ultramarines",
                "He founded and led the Ultramarines Legion"
            ]
        },
        "metadata": {
            "category": "basic",
            "difficulty": "easy",
            "question_type": "factoid",
            "retrieval_hops": 1,
            "contains_false_premise": False
        }
    },

    {
        "id": "WH40K-002",
        "question": "What is the homeworld of the Blood Angels?",
        "ground_truth": {
            "answer": "Baal is the homeworld of the Blood Angels.",
            "key_facts": [
                "Baal is the Blood Angels' homeworld",
                "The Blood Angels are descended from Sanguinius"
            ]
        },
        "metadata": {
            "category": "basic",
            "difficulty": "easy",
            "question_type": "factoid",
            "retrieval_hops": 1,
            "contains_false_premise": False
        }
    },

    {
        "id": "WH40K-003",
        "question": "Who is the current leader of the Adeptus Mechanicus?",
        "ground_truth": {
            "answer": "The Adeptus Mechanicus is led by the Fabricator-General of Mars.",
            "key_facts": [
                "The Fabricator-General is the senior leader of the Adeptus Mechanicus",
                "The position is associated with Mars"
            ]
        },
        "metadata": {
            "category": "basic",
            "difficulty": "easy",
            "question_type": "factoid",
            "retrieval_hops": 1,
            "contains_false_premise": False
        }
    },

    {
        "id": "WH40K-004",
        "question": "What is the Black Library?",
        "ground_truth": {
            "answer": "The Black Library is a mysterious Eldar repository containing vast knowledge, including knowledge concerning Chaos.",
            "key_facts": [
                "The Black Library is associated with the Aeldari",
                "It contains extensive knowledge about Chaos and the Warp",
                "Its location is hidden from most beings"
            ]
        },
        "metadata": {
            "category": "basic",
            "difficulty": "easy",
            "question_type": "definition",
            "retrieval_hops": 1,
            "contains_false_premise": False
        }
    },

    {
        "id": "WH40K-005",
        "question": "Who founded the Grey Knights?",
        "ground_truth": {
            "answer": "The Grey Knights were created during the aftermath of the Horus Heresy, with their origins closely associated with Malcador the Sigillite and the Emperor's anti-Chaos plans.",
            "key_facts": [
                "The Grey Knights originated during the Horus Heresy era",
                "Malcador played a major role in their creation",
                "They were created specifically to combat Chaos"
            ]
        },
        "metadata": {
            "category": "basic",
            "difficulty": "easy",
            "question_type": "historical_fact",
            "retrieval_hops": 2,
            "contains_false_premise": False
        }
    },

    {
        "id": "WH40K-006",
        "question": "What is the purpose of the Golden Throne?",
        "ground_truth": {
            "answer": "The Golden Throne sustains the Emperor and helps maintain the Astronomican while also containing the catastrophic consequences of the failed Imperial Webway project.",
            "key_facts": [
                "The Golden Throne sustains the Emperor",
                "It is connected to the Astronomican",
                "It is connected to the Imperial Webway project"
            ]
        },
        "metadata": {
            "category": "basic",
            "difficulty": "easy",
            "question_type": "definition",
            "retrieval_hops": 2,
            "contains_false_premise": False
        }
    },

    {
        "id": "WH40K-007",
        "question": "Which Chaos God is associated with decay and disease?",
        "ground_truth": {
            "answer": "Nurgle.",
            "key_facts": [
                "Nurgle is the Chaos God associated with disease",
                "Nurgle is associated with decay and corruption"
            ]
        },
        "metadata": {
            "category": "basic",
            "difficulty": "easy",
            "question_type": "factoid",
            "retrieval_hops": 1,
            "contains_false_premise": False
        }
    },

    {
        "id": "WH40K-008",
        "question": "What is a Space Marine Chapter?",
        "ground_truth": {
            "answer": "A Space Marine Chapter is a major organizational unit of the Adeptus Astartes, normally consisting of roughly one thousand battle-brothers under the Codex Astartes model.",
            "key_facts": [
                "A Chapter is an organizational unit of Space Marines",
                "The Codex Astartes established the standard post-Heresy structure",
                "A Codex-compliant Chapter is nominally around one thousand Space Marines"
            ]
        },
        "metadata": {
            "category": "basic",
            "difficulty": "easy",
            "question_type": "definition",
            "retrieval_hops": 1,
            "contains_false_premise": False
        }
    },

    {
        "id": "WH40K-009",
        "question": "Who is Roboute Guilliman?",
        "ground_truth": {
            "answer": "Roboute Guilliman is the Primarch of the Ultramarines and one of the Emperor's twenty Primarchs.",
            "key_facts": [
                "Guilliman is a Primarch",
                "He is the Primarch of the Ultramarines",
                "He authored the Codex Astartes"
            ]
        },
        "metadata": {
            "category": "basic",
            "difficulty": "easy",
            "question_type": "entity",
            "retrieval_hops": 1,
            "contains_false_premise": False
        }
    },

    {
        "id": "WH40K-010",
        "question": "What is the Eye of Terror?",
        "ground_truth": {
            "answer": "The Eye of Terror is a massive Warp rift created by the Fall of the Aeldari and the birth of Slaanesh.",
            "key_facts": [
                "The Eye of Terror is a region where Warp and realspace overlap",
                "It was created by the Fall of the Aeldari",
                "The birth of Slaanesh created the catastrophic Warp disturbance"
            ]
        },
        "metadata": {
            "category": "basic",
            "difficulty": "easy",
            "question_type": "definition",
            "retrieval_hops": 2,
            "contains_false_premise": False
        }
    },


    # --------------------------------------------------------
    # MULTI-HOP / MEDIUM
    # --------------------------------------------------------

    {
        "id": "WH40K-011",
        "question": "Why did the Emperor create the Primarchs?",
        "ground_truth": {
            "answer": "The Emperor created the Primarchs as genetically engineered superhuman leaders to command the Great Crusade and serve as the foundation for his vision of humanity.",
            "key_facts": [
                "The Primarchs were engineered by the Emperor",
                "They were intended to lead the Great Crusade",
                "They were central to the Emperor's plans for humanity"
            ]
        },
        "metadata": {
            "category": "multi_hop",
            "difficulty": "medium",
            "question_type": "causal",
            "retrieval_hops": 2,
            "contains_false_premise": False
        }
    },

    {
        "id": "WH40K-012",
        "question": "How did Horus become corrupted by Chaos?",
        "ground_truth": {
            "answer": "Horus was gradually corrupted through the influence of Chaos, particularly after being wounded on Davin and manipulated by Erebus and other Chaos agents.",
            "key_facts": [
                "Horus was wounded on Davin",
                "Chaos forces manipulated Horus during his recovery",
                "Erebus played a major role in Horus's corruption",
                "Horus eventually embraced Chaos"
            ]
        },
        "metadata": {
            "category": "multi_hop",
            "difficulty": "medium",
            "question_type": "causal",
            "retrieval_hops": 3,
            "contains_false_premise": False
        }
    },

    {
        "id": "WH40K-013",
        "question": "What events led to the Siege of Terra?",
        "ground_truth": {
            "answer": "The Siege of Terra resulted from the Horus Heresy, during which Horus's rebellion brought Traitor forces across the galaxy and eventually to Terra.",
            "key_facts": [
                "The Horus Heresy began as a rebellion against the Emperor",
                "Several Primarchs and Legions joined Horus",
                "The Traitor forces eventually attacked Terra",
                "The Siege was the climactic battle of the Heresy"
            ]
        },
        "metadata": {
            "category": "multi_hop",
            "difficulty": "medium",
            "question_type": "causal",
            "retrieval_hops": 3,
            "contains_false_premise": False
        }
    },

    {
        "id": "WH40K-014",
        "question": "Why did the Emperor fight Horus aboard the Vengeful Spirit?",
        "ground_truth": {
            "answer": "The Emperor boarded the Vengeful Spirit to confront Horus directly and end the rebellion after Horus's forces breached Terra.",
            "key_facts": [
                "Horus was aboard the Vengeful Spirit",
                "The Emperor sought to confront Horus",
                "The confrontation occurred during the final stage of the Siege of Terra"
            ]
        },
        "metadata": {
            "category": "multi_hop",
            "difficulty": "medium",
            "question_type": "causal",
            "retrieval_hops": 2,
            "contains_false_premise": False
        }
    },

    {
        "id": "WH40K-015",
        "question": "How are the Grey Knights connected to the Horus Heresy?",
        "ground_truth": {
            "answer": "The Grey Knights were established during the Horus Heresy era as a secret anti-Chaos force intended to defend humanity against daemonic threats.",
            "key_facts": [
                "Their creation occurred during the Heresy era",
                "Malcador was involved in their establishment",
                "They were designed to fight Chaos and daemons"
            ]
        },
        "metadata": {
            "category": "multi_hop",
            "difficulty": "medium",
            "question_type": "historical_relationship",
            "retrieval_hops": 2,
            "contains_false_premise": False
        }
    },

    {
        "id": "WH40K-016",
        "question": "Why is Cadia strategically important to the Imperium?",
        "ground_truth": {
            "answer": "Cadia was strategically important because it stood near the Eye of Terror and served as a major defensive barrier against Chaos incursions.",
            "key_facts": [
                "Cadia was located near the Eye of Terror",
                "Cadia was a major Imperial defensive position",
                "Cadia resisted numerous Black Crusades"
            ]
        },
        "metadata": {
            "category": "multi_hop",
            "difficulty": "medium",
            "question_type": "strategic",
            "retrieval_hops": 2,
            "contains_false_premise": False
        }
    },

    {
        "id": "WH40K-017",
        "question": "How did the destruction of Cadia contribute to the formation of the Great Rift?",
        "ground_truth": {
            "answer": "Cadia's destruction removed a major stabilizing obstacle near the Eye of Terror, and the resulting Warp disturbance contributed to the expansion of the rift that became the Great Rift.",
            "key_facts": [
                "Cadia was destroyed during the 13th Black Crusade",
                "The Eye of Terror expanded dramatically",
                "The Great Rift subsequently divided much of the galaxy"
            ]
        },
        "metadata": {
            "category": "multi_hop",
            "difficulty": "hard",
            "question_type": "causal",
            "retrieval_hops": 3,
            "contains_false_premise": False
        }
    },

    {
        "id": "WH40K-018",
        "question": "What is the relationship between the Adeptus Mechanicus and the Imperium?",
        "ground_truth": {
            "answer": "The Adeptus Mechanicus is a powerful semi-autonomous institution allied with the Imperium, providing technology, manufacturing, armies, and technical expertise.",
            "key_facts": [
                "The Mechanicus is allied with the Imperium",
                "Mars retains substantial autonomy",
                "The Mechanicus supplies technology and military forces"
            ]
        },
        "metadata": {
            "category": "multi_hop",
            "difficulty": "medium",
            "question_type": "relationship",
            "retrieval_hops": 2,
            "contains_false_premise": False
        }
    },

    {
        "id": "WH40K-019",
        "question": "Why did the Space Wolves and Thousand Sons become enemies?",
        "ground_truth": {
            "answer": "Their conflict grew from ideological hostility, rivalry between Magnus and Leman Russ, and the events surrounding the Council of Nikaea and the Burning of Prospero.",
            "key_facts": [
                "Magnus and Russ had a longstanding rivalry",
                "The Council of Nikaea restricted psychic practices",
                "Magnus continued using psychic powers",
                "Russ eventually led the attack on Prospero"
            ]
        },
        "metadata": {
            "category": "multi_hop",
            "difficulty": "medium",
            "question_type": "causal",
            "retrieval_hops": 3,
            "contains_false_premise": False
        }
    },

    {
        "id": "WH40K-020",
        "question": "How did the Necrons become dormant for millions of years?",
        "ground_truth": {
            "answer": "After the War in Heaven and their conflict with the Old Ones and Aeldari, the Necrons entered vast tomb complexes and remained dormant for millions of years.",
            "key_facts": [
                "The Necrons fought in the War in Heaven",
                "Their civilization entered a period of dormancy",
                "Necron tomb worlds preserved them for millions of years"
            ]
        },
        "metadata": {
            "category": "multi_hop",
            "difficulty": "medium",
            "question_type": "historical",
            "retrieval_hops": 3,
            "contains_false_premise": False
        }
    },


    # --------------------------------------------------------
    # HARD / SYNTHESIS
    # --------------------------------------------------------

    {
        "id": "WH40K-021",
        "question": "Compare the reasons Horus, Magnus, and Perturabo ultimately turned against the Emperor.",
        "ground_truth": {
            "answer": "Horus was corrupted and manipulated by Chaos; Magnus became alienated after his psychic actions and the destruction of Prospero; Perturabo became increasingly embittered by the burdens and perceived exploitation imposed upon him.",
            "key_facts": [
                "Horus was manipulated by Chaos",
                "Magnus's relationship with the Emperor deteriorated over psychic practices and Prospero",
                "Perturabo developed deep resentment toward the Imperium and his perceived treatment"
            ]
        },
        "metadata": {
            "category": "hard",
            "difficulty": "hard",
            "question_type": "comparison",
            "retrieval_hops": 4,
            "contains_false_premise": False
        }
    },

    {
        "id": "WH40K-022",
        "question": "How did the Emperor's treatment of Magnus contribute to the destruction of Prospero?",
        "ground_truth": {
            "answer": "The conflict over Magnus's psychic actions, the Emperor's judgment at Nikaea, and the decision to send the Space Wolves ultimately led to the confrontation at Prospero.",
            "key_facts": [
                "Magnus violated the restrictions associated with Nikaea",
                "Magnus attempted to warn the Emperor psychically",
                "Russ was sent against Magnus",
                "The Thousand Sons homeworld Prospero was attacked"
            ]
        },
        "metadata": {
            "category": "hard",
            "difficulty": "hard",
            "question_type": "causal",
            "retrieval_hops": 4,
            "contains_false_premise": False
        }
    },

    {
        "id": "WH40K-023",
        "question": "Why did Magnus warn the Emperor?",
        "ground_truth": {
            "answer": "Magnus attempted to warn the Emperor that Horus had fallen to Chaos.",
            "key_facts": [
                "Magnus discovered that Horus had fallen to Chaos",
                "Magnus used psychic means to warn the Emperor",
                "The psychic warning damaged the Imperial Webway project",
                "The warning had catastrophic consequences"
            ]
        },
        "metadata": {
            "category": "multi_hop",
            "difficulty": "hard",
            "question_type": "causal",
            "retrieval_hops": 3,
            "contains_false_premise": False
        }
    },

    {
        "id": "WH40K-024",
        "question": "Why was the Webway Project important to the Emperor's long-term plans?",
        "ground_truth": {
            "answer": "The Webway Project was intended to provide humanity with safer access through the galaxy while reducing dependence on the Warp and its dangers.",
            "key_facts": [
                "The Emperor sought human access to the Webway",
                "The project was intended to reduce dependence on Warp travel",
                "Chaos posed a major reason for seeking an alternative to Warp travel"
            ]
        },
        "metadata": {
            "category": "hard",
            "difficulty": "hard",
            "question_type": "strategic",
            "retrieval_hops": 3,
            "contains_false_premise": False
        }
    },

    {
        "id": "WH40K-025",
        "question": "How did the Horus Heresy fundamentally change the relationship between the Emperor and the Imperium?",
        "ground_truth": {
            "answer": "The Heresy transformed the Emperor from an active ruler leading the Great Crusade into a near-divine figure permanently entombed on the Golden Throne, while the Imperium became increasingly authoritarian and religious.",
            "key_facts": [
                "The Emperor was mortally wounded by Horus",
                "He became bound to the Golden Throne",
                "The post-Heresy Imperium increasingly worshipped him",
                "The Imperium changed significantly from the Great Crusade era"
            ]
        },
        "metadata": {
            "category": "hard",
            "difficulty": "hard",
            "question_type": "historical_comparison",
            "retrieval_hops": 4,
            "contains_false_premise": False
        }
    },

    {
        "id": "WH40K-026",
        "question": "Compare the philosophies of Roboute Guilliman and Lion El'Jonson regarding the Imperium's future.",
        "ground_truth": {
            "answer": "Both seek to preserve humanity and the Imperium, but Guilliman generally emphasizes administration, law, and rational organization while the Lion is more focused on military pragmatism, loyalty, and direct action.",
            "key_facts": [
                "Guilliman emphasizes organization and governance",
                "The Lion emphasizes military action and loyalty",
                "Both are loyalist Primarchs",
                "Their approaches can create political tension"
            ]
        },
        "metadata": {
            "category": "hard",
            "difficulty": "hard",
            "question_type": "comparison",
            "retrieval_hops": 4,
            "contains_false_premise": False
        }
    },

    {
        "id": "WH40K-027",
        "question": "How did the Fall of the Eldar shape the current state of the galaxy?",
        "ground_truth": {
            "answer": "The Fall destroyed the ancient Aeldari civilization, birthed Slaanesh, created the Eye of Terror, and radically altered the balance of power in the galaxy.",
            "key_facts": [
                "The Fall destroyed most of the ancient Aeldari civilization",
                "Slaanesh was born from the catastrophe",
                "The Eye of Terror was created",
                "Surviving Aeldari adopted different strategies for survival"
            ]
        },
        "metadata": {
            "category": "hard",
            "difficulty": "hard",
            "question_type": "causal",
            "retrieval_hops": 4,
            "contains_false_premise": False
        }
    },

    {
        "id": "WH40K-028",
        "question": "Explain the relationship between the C'tan, Necrons, and the War in Heaven.",
        "ground_truth": {
            "answer": "The Necrons allied with the C'tan during the War in Heaven, gaining power through biotransference while using C'tan abilities to wage war against the Old Ones and their allies.",
            "key_facts": [
                "The Necrontyr underwent biotransference",
                "The C'tan became involved with the Necrons",
                "The War in Heaven was an ancient galactic conflict",
                "The Necrons eventually turned against the C'tan"
            ]
        },
        "metadata": {
            "category": "hard",
            "difficulty": "hard",
            "question_type": "relationship",
            "retrieval_hops": 4,
            "contains_false_premise": False
        }
    },

    {
        "id": "WH40K-029",
        "question": "Why is the Tyranid threat fundamentally different from the threats posed by Chaos and the Necrons?",
        "ground_truth": {
            "answer": "Tyranids are an extragalactic biological hive intelligence driven primarily by consumption and survival, whereas Chaos is a Warp-based metaphysical threat and Necrons are an ancient technological civilization pursuing their own strategic goals.",
            "key_facts": [
                "Tyranids are biological hive organisms",
                "Tyranids consume biomass",
                "Chaos is fundamentally connected to the Warp",
                "Necrons are technological undead beings"
            ]
        },
        "metadata": {
            "category": "hard",
            "difficulty": "hard",
            "question_type": "comparison",
            "retrieval_hops": 4,
            "contains_false_premise": False
        }
    },

    {
        "id": "WH40K-030",
        "question": "How did the Great Rift change the strategic situation of the Imperium?",
        "ground_truth": {
            "answer": "The Great Rift split the galaxy into major regions, disrupted travel and communication, and isolated many Imperial worlds while intensifying Warp-related threats.",
            "key_facts": [
                "The Great Rift divided the galaxy",
                "Warp travel became more dangerous or difficult in many regions",
                "Imperial communication was disrupted",
                "Imperial territories became more isolated"
            ]
        },
        "metadata": {
            "category": "hard",
            "difficulty": "hard",
            "question_type": "strategic",
            "retrieval_hops": 3,
            "contains_false_premise": False
        }
    },


    # --------------------------------------------------------
    # ENTITY DISAMBIGUATION
    # --------------------------------------------------------

    {
        "id": "WH40K-031",
        "question": "What is the difference between the Emperor's Children Legion and the Emperor's Children warband or forces in the modern era?",
        "ground_truth": {
            "answer": "The Emperor's Children Legion was one of the original Traitor Legions, while modern Emperor's Children forces are the descendants and successor warbands or formations of that Legion after the Horus Heresy.",
            "key_facts": [
                "The Emperor's Children were originally a Legion",
                "Fulgrim was their Primarch",
                "The Legion fell to Chaos",
                "Modern forces descend from the Traitor Legion"
            ]
        },
        "metadata": {
            "category": "entity_disambiguation",
            "difficulty": "hard",
            "question_type": "entity_disambiguation",
            "retrieval_hops": 3,
            "contains_false_premise": False
        }
    },

    {
        "id": "WH40K-032",
        "question": "What is the difference between the Lion El'Jonson and the Dark Angels' Lion Guard?",
        "ground_truth": {
            "answer": "Lion El'Jonson is the Primarch of the Dark Angels, while the Lion Guard refers to warriors or formations associated with him rather than the Primarch himself.",
            "key_facts": [
                "Lion El'Jonson is a Primarch",
                "He is the Primarch of the Dark Angels",
                "The Lion Guard is not the same entity as the Primarch"
            ]
        },
        "metadata": {
            "category": "entity_disambiguation",
            "difficulty": "medium",
            "question_type": "entity_disambiguation",
            "retrieval_hops": 2,
            "contains_false_premise": False
        }
    },

    {
        "id": "WH40K-033",
        "question": "How does the character Abaddon differ from the historical role of Horus?",
        "ground_truth": {
            "answer": "Horus was the Warmaster and Primarch who led the original Heresy, while Abaddon was a member of the Sons of Horus who later became the leader of the Black Legion and continued the war against the Imperium.",
            "key_facts": [
                "Horus was a Primarch",
                "Horus led the Horus Heresy",
                "Abaddon was a Sons of Horus Legionnaire",
                "Abaddon became Warmaster of Chaos",
                "Abaddon founded or led the Black Legion"
            ]
        },
        "metadata": {
            "category": "entity_disambiguation",
            "difficulty": "medium",
            "question_type": "comparison",
            "retrieval_hops": 3,
            "contains_false_premise": False
        }
    },

    {
        "id": "WH40K-034",
        "question": "What is the difference between the Eye of Terror and the Great Rift?",
        "ground_truth": {
            "answer": "The Eye of Terror is a massive Warp rift associated with the Fall of the Aeldari, while the Great Rift is a much larger galactic-scale Warp disturbance that emerged in the 41st Millennium.",
            "key_facts": [
                "The Eye of Terror predates the Great Rift",
                "The Eye of Terror is associated with the birth of Slaanesh",
                "The Great Rift is a galaxy-spanning Warp phenomenon"
            ]
        },
        "metadata": {
            "category": "entity_disambiguation",
            "difficulty": "medium",
            "question_type": "comparison",
            "retrieval_hops": 3,
            "contains_false_premise": False
        }
    },

    {
        "id": "WH40K-035",
        "question": "Distinguish between the major meanings of Black Legion in relevant lore contexts.",
        "ground_truth": {
            "answer": "The Black Legion is the Chaos Space Marine Legion led by Abaddon, formerly known as the Sons of Horus. The term should not be confused with unrelated uses of the word black in faction names.",
            "key_facts": [
                "The Black Legion descends from the Sons of Horus",
                "Abaddon leads the Black Legion",
                "The Black Legion is a Traitor Legion"
            ]
        },
        "metadata": {
            "category": "entity_disambiguation",
            "difficulty": "medium",
            "question_type": "entity_disambiguation",
            "retrieval_hops": 2,
            "contains_false_premise": False
        }
    },

    {
        "id": "WH40K-036",
        "question": "What is the difference between a Primarch and a Daemon Primarch?",
        "ground_truth": {
            "answer": "A Primarch is one of the Emperor's genetically engineered superhuman sons, while a Daemon Primarch is a Primarch who has ascended into daemonhood through Chaos.",
            "key_facts": [
                "Primarchs were created by the Emperor",
                "Some Primarchs became aligned with Chaos",
                "Daemon Primarchs underwent daemon ascension"
            ]
        },
        "metadata": {
            "category": "entity_disambiguation",
            "difficulty": "easy",
            "question_type": "definition",
            "retrieval_hops": 2,
            "contains_false_premise": False
        }
    },

    {
        "id": "WH40K-037",
        "question": "How does the Imperium distinguish between a Space Marine Chapter, Legion, and successor Chapter?",
        "ground_truth": {
            "answer": "Legions were the large Space Marine formations of the Great Crusade and Horus Heresy, while Chapters became the standard smaller formations after the Heresy. Successor Chapters were created from the gene-seed and organizational traditions of parent Chapters or Legions.",
            "key_facts": [
                "Legions existed before the Second Founding",
                "The Codex Astartes promoted Chapter organization",
                "Successor Chapters derive from existing gene-seed lineages"
            ]
        },
        "metadata": {
            "category": "entity_disambiguation",
            "difficulty": "hard",
            "question_type": "comparison",
            "retrieval_hops": 3,
            "contains_false_premise": False
        }
    },

    {
        "id": "WH40K-038",
        "question": "What is the difference between the Old Ones and the Eldar?",
        "ground_truth": {
            "answer": "The Old Ones were an ancient precursor species responsible for creating or uplifting several species, while the Aeldari were one of the major civilizations that developed during the War in Heaven and later inherited much of the galaxy.",
            "key_facts": [
                "The Old Ones predate the Aeldari civilization",
                "The Old Ones were major participants in the War in Heaven",
                "The Aeldari were among the species associated with the Old Ones' legacy"
            ]
        },
        "metadata": {
            "category": "entity_disambiguation",
            "difficulty": "hard",
            "question_type": "comparison",
            "retrieval_hops": 3,
            "contains_false_premise": False
        }
    },


    # --------------------------------------------------------
    # CHRONOLOGY
    # --------------------------------------------------------

    {
        "id": "WH40K-039",
        "question": "Put the following events in chronological order: the Horus Heresy, the Fall of the Eldar, the Great Rift, the War in Heaven, and the Unification Wars.",
        "ground_truth": {
            "answer": "War in Heaven → Fall of the Eldar → Unification Wars → Horus Heresy → Great Rift.",
            "key_facts": [
                "The War in Heaven is the most ancient of these events",
                "The Fall of the Eldar occurred long before the Horus Heresy",
                "The Unification Wars preceded the Great Crusade",
                "The Horus Heresy occurred in the 31st Millennium",
                "The Great Rift emerged in the 41st Millennium"
            ]
        },
        "metadata": {
            "category": "chronology",
            "difficulty": "hard",
            "question_type": "chronology",
            "retrieval_hops": 5,
            "contains_false_premise": False
        }
    },

    {
        "id": "WH40K-040",
        "question": "What happened between the Emperor's creation of the Primarchs and the beginning of the Great Crusade?",
        "ground_truth": {
            "answer": "The Primarchs were scattered through the Warp, the Emperor conducted the Unification Wars, created the early Space Marine Legions, and then began the Great Crusade after reclaiming the Primarchs.",
            "key_facts": [
                "The Primarchs were scattered",
                "The Emperor unified Terra",
                "The Space Marine Legions were created",
                "The Great Crusade followed the Unification Wars"
            ]
        },
        "metadata": {
            "category": "chronology",
            "difficulty": "hard",
            "question_type": "chronology",
            "retrieval_hops": 4,
            "contains_false_premise": False
        }
    },

    {
        "id": "WH40K-041",
        "question": "What major events occurred between the Council of Nikaea and the Siege of Terra?",
        "ground_truth": {
            "answer": "Major events included Magnus's warning, the catastrophic breach of the Imperial Webway, the Burning of Prospero, Horus's rebellion, the expansion of the Traitor war, and the eventual advance on Terra.",
            "key_facts": [
                "The Council of Nikaea restricted psychic practices",
                "Magnus warned the Emperor",
                "Prospero was attacked",
                "Horus launched his rebellion",
                "The Traitor forces eventually reached Terra"
            ]
        },
        "metadata": {
            "category": "chronology",
            "difficulty": "hard",
            "question_type": "chronology",
            "retrieval_hops": 5,
            "contains_false_premise": False
        }
    },

    {
        "id": "WH40K-042",
        "question": "How did the Imperium change between the Great Crusade and the 41st Millennium?",
        "ground_truth": {
            "answer": "The Imperium changed from an expansionist secular empire led directly by the Emperor into a fragmented, highly bureaucratic, religious, authoritarian civilization centered on worship of the Emperor.",
            "key_facts": [
                "The Great Crusade Imperium was officially secular",
                "The post-Heresy Imperium increasingly worshipped the Emperor",
                "The Imperium became heavily bureaucratic",
                "The Imperium became more stagnant and authoritarian"
            ]
        },
        "metadata": {
            "category": "chronology",
            "difficulty": "hard",
            "question_type": "historical_comparison",
            "retrieval_hops": 4,
            "contains_false_premise": False
        }
    },

    {
        "id": "WH40K-043",
        "question": "What happened to the Primarchs after the Horus Heresy?",
        "ground_truth": {
            "answer": "Many loyalist Primarchs disappeared, died, or entered states of dormancy, while surviving Traitor Primarchs largely became Daemon Primarchs or withdrew into the Eye of Terror and other Warp regions.",
            "key_facts": [
                "Several loyalist Primarchs disappeared or died",
                "Several Traitor Primarchs became Daemon Primarchs",
                "Guilliman was placed in stasis after being mortally wounded",
                "The surviving Primarchs became rare figures in the later Imperium"
            ]
        },
        "metadata": {
            "category": "chronology",
            "difficulty": "medium",
            "question_type": "historical",
            "retrieval_hops": 3,
            "contains_false_premise": False
        }
    },

    {
        "id": "WH40K-044",
        "question": "Which major events led from the Horus Heresy to the formation of the modern Space Marine Chapters?",
        "ground_truth": {
            "answer": "The defeat of Horus led to reforms by Roboute Guilliman, especially the Codex Astartes and the Second Founding, which divided the original Legions into smaller Chapters.",
            "key_facts": [
                "Horus was defeated",
                "Guilliman authored the Codex Astartes",
                "The Second Founding divided the Legions",
                "Chapters became the standard organizational structure"
            ]
        },
        "metadata": {
            "category": "chronology",
            "difficulty": "hard",
            "question_type": "causal_chronology",
            "retrieval_hops": 4,
            "contains_false_premise": False
        }
    },


    # --------------------------------------------------------
    # CONTRADICTION / UNCERTAINTY
    # --------------------------------------------------------

    {
        "id": "WH40K-045",
        "question": "Is the Emperor definitively a god in Warhammer 40k lore? Explain the competing perspectives.",
        "ground_truth": {
            "answer": "The setting deliberately presents ambiguity. Imperial religion treats the Emperor as a god, while other perspectives portray him as a powerful human or Warp-related entity whose nature is contested.",
            "key_facts": [
                "The Imperial Cult worships the Emperor as a god",
                "The Emperor historically rejected traditional religion",
                "The setting contains competing interpretations of his nature"
            ]
        },
        "metadata": {
            "category": "uncertainty",
            "difficulty": "hard",
            "question_type": "ambiguous_lore",
            "retrieval_hops": 4,
            "contains_false_premise": False
        }
    },

    {
        "id": "WH40K-046",
        "question": "What is the definitive identity of the mysterious author of the Lectitio Divinitatus?",
        "ground_truth": {
            "answer": "The Lectitio Divinitatus is traditionally associated with Lorgar and the Word Bearers, although lore around its authorship and development has changed across sources.",
            "key_facts": [
                "The Lectitio Divinitatus is associated with Lorgar",
                "It became an important source of Imperial religious ideas",
                "Different lore sources may frame its history differently"
            ]
        },
        "metadata": {
            "category": "uncertainty",
            "difficulty": "hard",
            "question_type": "source_ambiguity",
            "retrieval_hops": 3,
            "contains_false_premise": False
        }
    },

    {
        "id": "WH40K-047",
        "question": "How certain is Imperial lore about what actually happened during the Dark Age of Technology?",
        "ground_truth": {
            "answer": "Imperial knowledge of the Dark Age of Technology is incomplete and often fragmented, with many details lost, distorted, or preserved only through unreliable records.",
            "key_facts": [
                "Much knowledge from the Dark Age was lost",
                "Imperial records are incomplete",
                "The Mechanicus preserves fragments of ancient technological knowledge"
            ]
        },
        "metadata": {
            "category": "uncertainty",
            "difficulty": "hard",
            "question_type": "epistemic_uncertainty",
            "retrieval_hops": 3,
            "contains_false_premise": False
        }
    },

    {
        "id": "WH40K-048",
        "question": "What do we actually know about the origins of the Emperor?",
        "ground_truth": {
            "answer": "The Emperor's origins are intentionally mysterious. Some lore provides ancient historical claims about his emergence in prehistoric humanity, but the setting leaves significant uncertainty around his true history.",
            "key_facts": [
                "The Emperor is extremely ancient",
                "His origins are surrounded by contradictory or incomplete accounts",
                "The setting intentionally preserves uncertainty about his earliest history"
            ]
        },
        "metadata": {
            "category": "uncertainty",
            "difficulty": "hard",
            "question_type": "epistemic_uncertainty",
            "retrieval_hops": 3,
            "contains_false_premise": False
        }
    },

    {
        "id": "WH40K-049",
        "question": "What caused the disappearance of the Lost Primarchs?",
        "ground_truth": {
            "answer": "The exact fate and circumstances surrounding the two Lost Primarchs are deliberately obscured and remain unknown within the published lore.",
            "key_facts": [
                "There were two Lost Primarchs",
                "Their identities and histories are deliberately obscured",
                "The exact circumstances of their disappearance are not definitively revealed"
            ]
        },
        "metadata": {
            "category": "uncertainty",
            "difficulty": "medium",
            "question_type": "unknown_lore",
            "retrieval_hops": 2,
            "contains_false_premise": False
        }
    },

    {
        "id": "WH40K-050",
        "question": "What exactly happened to the Sensei?",
        "ground_truth": {
            "answer": "The Sensei are primarily associated with older Warhammer 40,000 lore, and their status and relevance have changed substantially across editions, making a single definitive modern account difficult.",
            "key_facts": [
                "The Sensei originated in older lore",
                "Their background changed across editions",
                "Modern canon does not provide the same prominence they once had"
            ]
        },
        "metadata": {
            "category": "uncertainty",
            "difficulty": "hard",
            "question_type": "edition_conflict",
            "retrieval_hops": 3,
            "contains_false_premise": False
        }
    },

    {
        "id": "WH40K-051",
        "question": "What is the definitive origin of the Tyranids?",
        "ground_truth": {
            "answer": "The definitive origin of the Tyranids remains unknown. They arrived in the Milky Way from outside the galaxy, and their deeper origins are intentionally mysterious.",
            "key_facts": [
                "Tyranids came from outside the Milky Way",
                "Their original home and deeper history are unknown",
                "The setting deliberately leaves their origin mysterious"
            ]
        },
        "metadata": {
            "category": "uncertainty",
            "difficulty": "medium",
            "question_type": "unknown_lore",
            "retrieval_hops": 2,
            "contains_false_premise": False
        }
    },

    {
        "id": "WH40K-052",
        "question": "What is beyond the eastern edge of the galaxy?",
        "ground_truth": {
            "answer": "The setting does not provide a complete definitive account of what lies beyond the eastern edge of the galaxy. The extragalactic arrival of the Tyranids demonstrates that other threats and regions exist beyond Imperial knowledge.",
            "key_facts": [
                "The Imperium has incomplete knowledge of extragalactic space",
                "The Tyranids originated outside the galaxy",
                "The region beyond the galaxy is largely unknown"
            ]
        },
        "metadata": {
            "category": "uncertainty",
            "difficulty": "hard",
            "question_type": "unknown_lore",
            "retrieval_hops": 3,
            "contains_false_premise": False
        }
    },

    {
        "id": "WH40K-053",
        "question": "How much does the Imperium actually understand about the Necrons?",
        "ground_truth": {
            "answer": "Imperial understanding is incomplete. The Imperium knows that Necrons are ancient technological enemies with extremely advanced capabilities, but much of their history, technology, and internal politics remains poorly understood.",
            "key_facts": [
                "Necrons are ancient",
                "Imperial knowledge of Necron technology is limited",
                "The Imperium often misunderstands or underestimates Necron capabilities"
            ]
        },
        "metadata": {
            "category": "uncertainty",
            "difficulty": "medium",
            "question_type": "epistemic_uncertainty",
            "retrieval_hops": 3,
            "contains_false_premise": False
        }
    },

    {
        "id": "WH40K-054",
        "question": "Are the Chaos Gods objectively real, or is their existence dependent on Warp phenomena?",
        "ground_truth": {
            "answer": "The Chaos Gods are real entities within the setting, existing in or through the Warp, while their forms and power are connected to emotions and psychic activity generated by sentient beings.",
            "key_facts": [
                "The Chaos Gods are real within the setting",
                "They exist in the Warp",
                "They are connected to emotions and psychic energy",
                "Their relationship with reality is metaphysical rather than conventional"
            ]
        },
        "metadata": {
            "category": "uncertainty",
            "difficulty": "hard",
            "question_type": "metaphysical",
            "retrieval_hops": 3,
            "contains_false_premise": False
        }
    },


    # --------------------------------------------------------
    # SOURCE-GROUNDING
    # --------------------------------------------------------

    {
        "id": "WH40K-055",
        "question": "According to The First Heretic, why did Lorgar turn against the Emperor?",
        "ground_truth": {
            "answer": "Lorgar became alienated after the Emperor condemned his religious worship and humiliated the Word Bearers, ultimately pushing him toward Chaos.",
            "key_facts": [
                "Lorgar worshipped the Emperor",
                "The Emperor rejected Lorgar's religious practices",
                "The destruction of Monarchia was a major humiliation",
                "Lorgar eventually turned toward Chaos"
            ]
        },
        "metadata": {
            "category": "source_grounding",
            "difficulty": "hard",
            "question_type": "source_specific",
            "retrieval_hops": 2,
            "contains_false_premise": False,
            "required_sources": [
                "The First Heretic"
            ],
            "expected_citations": True
        }
    },

    {
        "id": "WH40K-056",
        "question": "According to Prospero Burns, how are the Space Wolves' attitudes toward the Thousand Sons portrayed?",
        "ground_truth": {
            "answer": "The Space Wolves view the Thousand Sons with deep suspicion and hostility, especially because of their contrasting attitudes toward psychic powers and their long-running rivalry.",
            "key_facts": [
                "The Space Wolves distrust the Thousand Sons",
                "Psychic practices are a major source of conflict",
                "Russ and Magnus have a longstanding rivalry"
            ]
        },
        "metadata": {
            "category": "source_grounding",
            "difficulty": "hard",
            "question_type": "source_specific",
            "retrieval_hops": 2,
            "contains_false_premise": False,
            "required_sources": [
                "Prospero Burns"
            ],
            "expected_citations": True
        }
    },

    {
        "id": "WH40K-057",
        "question": "What does The Master of Mankind reveal about the Emperor's Webway Project?",
        "ground_truth": {
            "answer": "It depicts the Webway Project as a central part of the Emperor's attempt to secure humanity's future by reducing dependence on the Warp and denying Chaos a major avenue of influence.",
            "key_facts": [
                "The Webway Project was strategically important",
                "The Emperor sought to reduce humanity's dependence on Warp travel",
                "The project became endangered after Magnus's psychic intrusion"
            ]
        },
        "metadata": {
            "category": "source_grounding",
            "difficulty": "hard",
            "question_type": "source_specific",
            "retrieval_hops": 3,
            "contains_false_premise": False,
            "required_sources": [
                "The Master of Mankind"
            ],
            "expected_citations": True
        }
    },

    {
        "id": "WH40K-058",
        "question": "How does Know No Fear portray the Battle of Calth?",
        "ground_truth": {
            "answer": "It portrays the Battle of Calth as a catastrophic surprise attack by the Word Bearers against the Ultramarines, emphasizing confusion, devastation, and the scale of the betrayal.",
            "key_facts": [
                "The Word Bearers attacked the Ultramarines",
                "The attack occurred at Calth",
                "The attack was a major act of betrayal",
                "The battle caused enormous destruction"
            ]
        },
        "metadata": {
            "category": "source_grounding",
            "difficulty": "hard",
            "question_type": "source_specific",
            "retrieval_hops": 2,
            "contains_false_premise": False,
            "required_sources": [
                "Know No Fear"
            ],
            "expected_citations": True
        }
    },

    {
        "id": "WH40K-059",
        "question": "What does Betrayer reveal about Angron and Lorgar's relationship?",
        "ground_truth": {
            "answer": "Betrayer depicts a complicated relationship in which Lorgar becomes increasingly concerned with Angron's suffering while also seeking to use Angron's transformation and fate for the purposes of Chaos.",
            "key_facts": [
                "Lorgar cares about Angron in his own way",
                "Angron is transformed into a Daemon Primarch",
                "Lorgar is deeply involved in Angron's path toward daemonhood"
            ]
        },
        "metadata": {
            "category": "source_grounding",
            "difficulty": "hard",
            "question_type": "source_specific",
            "retrieval_hops": 3,
            "contains_false_premise": False,
            "required_sources": [
                "Betrayer"
            ],
            "expected_citations": True
        }
    },

    {
        "id": "WH40K-060",
        "question": "Compare how the Emperor is characterized in The Master of Mankind and another Horus Heresy novel.",
        "ground_truth": {
            "answer": "The Master of Mankind presents a particularly distant, powerful, utilitarian, and psychologically complex Emperor, while other Horus Heresy novels may emphasize different aspects of his personality depending on their narrators and contexts.",
            "key_facts": [
                "The Emperor's characterization varies between novels",
                "The Master of Mankind emphasizes his strategic and utilitarian mindset",
                "Narrative perspective affects how the Emperor is portrayed"
            ]
        },
        "metadata": {
            "category": "source_grounding",
            "difficulty": "hard",
            "question_type": "source_comparison",
            "retrieval_hops": 4,
            "contains_false_premise": False,
            "required_sources": [
                "The Master of Mankind"
            ],
            "expected_citations": True
        }
    },


    # --------------------------------------------------------
    # ADVERSARIAL
    # --------------------------------------------------------

    {
        "id": "WH40K-061",
        "question": "Did Sanguinius personally kill Horus during the Siege of Terra?",
        "ground_truth": {
            "answer": "No. Sanguinius fought Horus and wounded him, but the Emperor ultimately defeated and destroyed Horus.",
            "key_facts": [
                "Sanguinius fought Horus",
                "Sanguinius wounded Horus",
                "The Emperor ultimately defeated Horus"
            ]
        },
        "metadata": {
            "category": "adversarial",
            "difficulty": "medium",
            "question_type": "false_premise",
            "retrieval_hops": 2,
            "contains_false_premise": True
        }
    },

    {
        "id": "WH40K-062",
        "question": "Did the Emperor intentionally create the Primarchs to become Daemon Princes?",
        "ground_truth": {
            "answer": "No. The Primarchs were created for the Emperor's plans for humanity and the Great Crusade; some later became Daemon Princes after falling to Chaos.",
            "key_facts": [
                "The Primarchs were created by the Emperor",
                "They were not created to become Daemon Princes",
                "Several Traitor Primarchs later became Daemon Princes"
            ]
        },
        "metadata": {
            "category": "adversarial",
            "difficulty": "easy",
            "question_type": "false_premise",
            "retrieval_hops": 2,
            "contains_false_premise": True
        }
    },

    {
        "id": "WH40K-063",
        "question": "Was Magnus responsible for destroying the Emperor's Webway Project?",
        "ground_truth": {
            "answer": "Magnus's psychic intrusion catastrophically damaged the Webway project and forced the Emperor to personally contain the resulting breach, although the broader circumstances and responsibility are more nuanced.",
            "key_facts": [
                "Magnus entered the Emperor's Webway project psychically",
                "The intrusion caused catastrophic damage",
                "The Emperor had to respond to the breach",
                "Responsibility should be described with appropriate nuance"
            ]
        },
        "metadata": {
            "category": "adversarial",
            "difficulty": "hard",
            "question_type": "loaded_premise",
            "retrieval_hops": 3,
            "contains_false_premise": False
        }
    },

    {
        "id": "WH40K-064",
        "question": "Did the Necrons create the Chaos Gods?",
        "ground_truth": {
            "answer": "No. The Chaos Gods arose from Warp phenomena and the emotions and psychic activity of sentient beings; the Necrons did not create them.",
            "key_facts": [
                "The Necrons did not create the Chaos Gods",
                "Chaos Gods are Warp entities",
                "The origins of Chaos predate or exist independently of the modern Necrons"
            ]
        },
        "metadata": {
            "category": "adversarial",
            "difficulty": "medium",
            "question_type": "false_premise",
            "retrieval_hops": 2,
            "contains_false_premise": True
        }
    },

    {
        "id": "WH40K-065",
        "question": "Was the Imperium already worshipping the Emperor as a god during the Great Crusade?",
        "ground_truth": {
            "answer": "Officially, no. The Emperor promoted a secular Imperial Truth during the Great Crusade and opposed religious worship, although some individuals continued to regard him as divine.",
            "key_facts": [
                "The Imperial Truth was officially secular",
                "The Emperor opposed religious worship",
                "Lorgar's religious devotion was condemned",
                "The Imperial Cult became dominant later"
            ]
        },
        "metadata": {
            "category": "adversarial",
            "difficulty": "medium",
            "question_type": "false_premise",
            "retrieval_hops": 3,
            "contains_false_premise": True
        }
    },

    {
        "id": "WH40K-066",
        "question": "Did all Primarchs willingly participate in the Great Crusade?",
        "ground_truth": {
            "answer": "No. While the Primarchs generally participated in the Great Crusade, their attitudes and loyalty varied considerably, and some were eventually opposed to the Emperor.",
            "key_facts": [
                "The Primarchs had different personalities and attitudes",
                "Some became Traitors",
                "Not all had the same relationship with the Emperor"
            ]
        },
        "metadata": {
            "category": "adversarial",
            "difficulty": "medium",
            "question_type": "false_premise",
            "retrieval_hops": 3,
            "contains_false_premise": True
        }
    },

    {
        "id": "WH40K-067",
        "question": "Did the Emperor personally create every Space Marine Chapter?",
        "ground_truth": {
            "answer": "No. The Emperor created the Primarchs and the original Space Marine Legions, while later Chapters were created through Foundings and the division of Legions after the Horus Heresy.",
            "key_facts": [
                "The Emperor created the original Legions",
                "The Second Founding created many Chapters",
                "Guilliman's Codex Astartes influenced the Chapter system"
            ]
        },
        "metadata": {
            "category": "adversarial",
            "difficulty": "easy",
            "question_type": "false_premise",
            "retrieval_hops": 3,
            "contains_false_premise": True
        }
    },

    {
        "id": "WH40K-068",
        "question": "Was the Horus Heresy primarily a conflict between Space Marines?",
        "ground_truth": {
            "answer": "Space Marines and their Primarchs were central to the Heresy, but it was a much broader civil war involving the Imperial Army, Mechanicum, Titans, daemons, human populations, and many other forces.",
            "key_facts": [
                "Space Marines were central to the Heresy",
                "The conflict involved many other military and civilian forces",
                "The Mechanicum and Titan Legions played major roles"
            ]
        },
        "metadata": {
            "category": "adversarial",
            "difficulty": "medium",
            "question_type": "loaded_premise",
            "retrieval_hops": 3,
            "contains_false_premise": True
        }
    },

    {
        "id": "WH40K-069",
        "question": "Did the Eldar cause the creation of the Tyranids?",
        "ground_truth": {
            "answer": "No. There is no established lore showing that the Aeldari created the Tyranids. The Tyranids arrived from outside the Milky Way and their deeper origin remains unknown.",
            "key_facts": [
                "The Tyranids are extragalactic",
                "Their origin is unknown",
                "There is no established claim that the Aeldari created them"
            ]
        },
        "metadata": {
            "category": "adversarial",
            "difficulty": "medium",
            "question_type": "false_premise",
            "retrieval_hops": 2,
            "contains_false_premise": True
        }
    },

    {
        "id": "WH40K-070",
        "question": "Is Abaddon a Primarch?",
        "ground_truth": {
            "answer": "No. Abaddon is a Chaos Space Marine and former First Captain of the Sons of Horus. He later became Warmaster of Chaos and leader of the Black Legion.",
            "key_facts": [
                "Abaddon is not a Primarch",
                "He was First Captain of the Sons of Horus",
                "He became Warmaster of Chaos",
                "He leads the Black Legion"
            ]
        },
        "metadata": {
            "category": "adversarial",
            "difficulty": "easy",
            "question_type": "false_premise",
            "retrieval_hops": 2,
            "contains_false_premise": True
        }
    },


    # --------------------------------------------------------
    # VERY HARD MULTI-HOP
    # --------------------------------------------------------

    {
        "id": "WH40K-071",
        "question": "How did the Emperor's Webway ambitions, Magnus's psychic warning, and the Burning of Prospero ultimately contribute to the Emperor becoming permanently bound to the Golden Throne?",
        "ground_truth": {
            "answer": "The Emperor's Webway project was damaged by Magnus's psychic warning, forcing the Emperor to personally contain the resulting Warp breach. The broader Heresy and the Burning of Prospero then contributed to the chain of events that eventually led to the Emperor's final battle with Horus and his permanent confinement to the Golden Throne.",
            "key_facts": [
                "The Emperor's Webway project was central to his plans",
                "Magnus's warning breached the Webway project",
                "The Emperor had to contain the breach",
                "The Burning of Prospero was part of the escalating conflict involving Magnus",
                "The Emperor was mortally wounded by Horus",
                "The Emperor was placed on the Golden Throne"
            ]
        },
        "metadata": {
            "category": "very_hard",
            "difficulty": "very_hard",
            "question_type": "multi_hop_causal",
            "retrieval_hops": 6,
            "contains_false_premise": False
        }
    },

    {
        "id": "WH40K-072",
        "question": "Trace the relationship between the Fall of the Eldar, the birth of Slaanesh, the creation of the Eye of Terror, and the Eldar survivors' current civilization.",
        "ground_truth": {
            "answer": "The decadent ancient Aeldari civilization culminated in the Fall, which birthed Slaanesh and created the Eye of Terror. Surviving Aeldari populations escaped or survived through different cultures and strategies, including Craftworlds, Exodites, and Drukhari.",
            "key_facts": [
                "The Fall resulted from extreme Aeldari decadence",
                "Slaanesh was born from the Fall",
                "The Eye of Terror was created",
                "Craftworld Aeldari survived by fleeing",
                "Exodites established worlds away from the core",
                "Drukhari survived in Commorragh"
            ]
        },
        "metadata": {
            "category": "very_hard",
            "difficulty": "very_hard",
            "question_type": "multi_hop_causal",
            "retrieval_hops": 5,
            "contains_false_premise": False
        }
    },

    {
        "id": "WH40K-073",
        "question": "Explain how the Emperor's original vision for the Imperium differed from the Imperium that existed after the Horus Heresy.",
        "ground_truth": {
            "answer": "The Emperor's Great Crusade Imperium was officially secular, rationalist, expansionist, and directly guided by the Emperor, whereas the post-Heresy Imperium became religious, bureaucratic, authoritarian, stagnant, and increasingly centered on worship of the Emperor.",
            "key_facts": [
                "The Great Crusade followed the Imperial Truth",
                "The Emperor opposed organized religion",
                "The post-Heresy Imperium developed the Imperial Cult",
                "The post-Heresy Imperium became more bureaucratic",
                "The Emperor ceased active rule after the Siege of Terra"
            ]
        },
        "metadata": {
            "category": "very_hard",
            "difficulty": "very_hard",
            "question_type": "historical_comparison",
            "retrieval_hops": 5,
            "contains_false_premise": False
        }
    },

    {
        "id": "WH40K-074",
        "question": "Trace the evolution of the Space Marines from the original Legions to the post-Heresy Chapter system.",
        "ground_truth": {
            "answer": "The Emperor created the original Space Marine Legions to prosecute the Great Crusade. After the Horus Heresy, Guilliman's Codex Astartes encouraged the division of the Legions into smaller Chapters during the Second Founding.",
            "key_facts": [
                "The original Space Marines were organized into Legions",
                "The Primarchs commanded the Legions",
                "The Horus Heresy demonstrated the danger of concentrated military power",
                "The Codex Astartes reorganized Space Marine forces",
                "The Second Founding created successor Chapters"
            ]
        },
        "metadata": {
            "category": "very_hard",
            "difficulty": "very_hard",
            "question_type": "historical_causality",
            "retrieval_hops": 5,
            "contains_false_premise": False
        }
    },

    {
        "id": "WH40K-075",
        "question": "Compare the origins, motivations, and strategic objectives of Chaos, the Tyranids, the Necrons, and the Orks as threats to the Imperium.",
        "ground_truth": {
            "answer": "Chaos arises from the Warp and seeks corruption, conflict, and power; Tyranids are an extragalactic hive organism seeking biological consumption; Necrons are an ancient technological civilization pursuing restoration and control; Orks are a species biologically and culturally driven toward conflict and warfare.",
            "key_facts": [
                "Chaos is connected to the Warp",
                "Tyranids seek biomass and survival",
                "Necrons seek restoration and strategic dominance",
                "Orks are inherently warlike",
                "The four factions have fundamentally different origins"
            ]
        },
        "metadata": {
            "category": "very_hard",
            "difficulty": "very_hard",
            "question_type": "faction_comparison",
            "retrieval_hops": 6,
            "contains_false_premise": False
        }
    },

    {
        "id": "WH40K-076",
        "question": "Explain how the actions of Lorgar, Erebus, and Kor Phaeron contributed to the transformation of the Horus Heresy from a political rebellion into a Chaos-backed war.",
        "ground_truth": {
            "answer": "Lorgar's search for spiritual truth led the Word Bearers toward Chaos, while Erebus and Kor Phaeron actively cultivated Chaos worship and manipulated Horus and other Traitors, transforming the rebellion into a war heavily shaped by the Ruinous Powers.",
            "key_facts": [
                "Lorgar rejected the Emperor's secular Imperial Truth",
                "The Word Bearers turned toward Chaos",
                "Erebus was a major Chaos agent",
                "Kor Phaeron was instrumental in Word Bearers corruption",
                "Horus was manipulated by Chaos"
            ]
        },
        "metadata": {
            "category": "very_hard",
            "difficulty": "very_hard",
            "question_type": "multi_hop_causal",
            "retrieval_hops": 6,
            "contains_false_premise": False
        }
    },

    {
        "id": "WH40K-077",
        "question": "How are the events surrounding Cadia, Abaddon, the Black Crusades, the 13th Black Crusade, and the Great Rift connected?",
        "ground_truth": {
            "answer": "Abaddon led repeated Black Crusades against the Imperium, culminating in the 13th Black Crusade, during which Cadia was destroyed. The destruction of Cadia coincided with the expansion of the Eye of Terror and the emergence of the Great Rift.",
            "key_facts": [
                "Abaddon led the Black Crusades",
                "The 13th Black Crusade targeted Cadia",
                "Cadia was destroyed",
                "The Eye of Terror expanded",
                "The Great Rift emerged across the galaxy"
            ]
        },
        "metadata": {
            "category": "very_hard",
            "difficulty": "very_hard",
            "question_type": "multi_hop_causal",
            "retrieval_hops": 5,
            "contains_false_premise": False
        }
    },

    {
        "id": "WH40K-078",
        "question": "Compare the Emperor's relationship with Magnus, Lorgar, and Horus, and explain how those relationships contributed differently to the Heresy.",
        "ground_truth": {
            "answer": "The Emperor's relationship with Magnus was shaped by psychic power and conflicting interpretations of obedience; his relationship with Lorgar deteriorated because of religious devotion and the Imperial Truth; his relationship with Horus was initially exceptionally close but became the central betrayal of the Heresy.",
            "key_facts": [
                "Magnus was valued for his psychic abilities",
                "Lorgar was condemned for religious worship",
                "Horus was the Emperor's favored Warmaster",
                "All three relationships contributed differently to the eventual crisis"
            ]
        },
        "metadata": {
            "category": "very_hard",
            "difficulty": "very_hard",
            "question_type": "comparison",
            "retrieval_hops": 6,
            "contains_false_premise": False
        }
    },

    {
        "id": "WH40K-079",
        "question": "How did the Imperium's treatment of the Adeptus Mechanicus during the Great Crusade affect their relationship after the Horus Heresy?",
        "ground_truth": {
            "answer": "The Mechanicum was an essential ally of the Great Crusade but retained its own traditions and power. The Heresy demonstrated the strategic importance of Mars and contributed to the formal relationship between the Imperium and the reconstituted Adeptus Mechanicus.",
            "key_facts": [
                "The Mechanicum was vital to Imperial military production",
                "Mars retained significant independence",
                "The Horus Heresy split the Mechanicum",
                "The post-Heresy Adeptus Mechanicus remained a powerful semi-autonomous institution"
            ]
        },
        "metadata": {
            "category": "very_hard",
            "difficulty": "very_hard",
            "question_type": "historical_relationship",
            "retrieval_hops": 5,
            "contains_false_premise": False
        }
    },

    {
        "id": "WH40K-080",
        "question": "How does the return of Guilliman change the political, military, and religious situation of the Imperium?",
        "ground_truth": {
            "answer": "Guilliman's return provides the Imperium with an active Primarch and exceptional administrator during a period of crisis, while also creating tension because his original secular ideals differ from the religious Imperium that developed in his absence.",
            "key_facts": [
                "Guilliman returned from stasis",
                "He became an active Imperial leader",
                "He confronts the Great Rift and Imperium Nihilus crisis",
                "His views differ in important ways from the modern Imperial Cult",
                "His return has major military and political consequences"
            ]
        },
        "metadata": {
            "category": "very_hard",
            "difficulty": "very_hard",
            "question_type": "multi_hop_synthesis",
            "retrieval_hops": 5,
            "contains_false_premise": False
        }
    }
]


# ============================================================
# Validation
# ============================================================

def validate_questions(data):
    if len(data) != 80:
        raise ValueError(
            f"Expected exactly 80 questions, but found {len(data)}"
        )

    ids = [q["id"] for q in data]

    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate question IDs found.")

    required_fields = {
        "id",
        "question",
        "ground_truth",
        "metadata",
    }

    for question in data:
        missing = required_fields - question.keys()

        if missing:
            raise ValueError(
                f"{question['id']} is missing fields: {missing}"
            )

        if "answer" not in question["ground_truth"]:
            raise ValueError(
                f"{question['id']} is missing ground_truth.answer"
            )

        if "key_facts" not in question["ground_truth"]:
            raise ValueError(
                f"{question['id']} is missing ground_truth.key_facts"
            )

        metadata_fields = {
            "category",
            "difficulty",
            "question_type",
            "retrieval_hops",
            "contains_false_premise",
        }

        missing_metadata = metadata_fields - question["metadata"].keys()

        if missing_metadata:
            raise ValueError(
                f"{question['id']} is missing metadata: {missing_metadata}"
            )


# ============================================================
# File helpers
# ============================================================

def write_json(path: Path, data):
    with path.open("w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            indent=2,
            ensure_ascii=False
        )

    print(f"Created: {path}")


def write_text(path: Path, text):
    with path.open("w", encoding="utf-8") as f:
        f.write(text)

    print(f"Created: {path}")


# ============================================================
# README
# ============================================================

README = """# Warhammer 40K RAG Evaluation Dataset

This directory contains evaluation questions for the Warhammer 40K
lore RAG system.

## Structure

```text
evals/
├── questions.json
├── questions/
│   ├── basic.json
│   ├── multi_hop.json
│   ├── adversarial.json
│   └── chronology.json
├── questions.txt
└── README.md
"""

# ============================================================
# Create evaluation dataset
# ============================================================

print()
print("=" * 60)
print("Warhammer 40K RAG Evaluation Dataset")
print("=" * 60)

print(f"Project root: {PROJECT_ROOT}")
print(f"Output directory: {EVALS_DIR}")
print()

# Validate the dataset first
validate_questions(questions)

# Create directories
EVALS_DIR.mkdir(parents=True, exist_ok=True)
QUESTIONS_DIR.mkdir(parents=True, exist_ok=True)

# ------------------------------------------------------------
# 1. All questions
# ------------------------------------------------------------

write_json(
    EVALS_DIR / "questions.json",
    questions
)

# ------------------------------------------------------------
# 2. Questions grouped by category
# ------------------------------------------------------------

categories = {
    "basic": [],
    "multi_hop": [],
    "adversarial": [],
    "chronology": [],
}

for question in questions:
    category = question["metadata"]["category"]

    if category in categories:
        categories[category].append(question)

for category, category_questions in categories.items():
    write_json(
        QUESTIONS_DIR / f"{category}.json",
        category_questions
    )

# ------------------------------------------------------------
# 3. Raw questions TXT
# ------------------------------------------------------------

raw_questions = []

for question in questions:
    raw_questions.append(
        f'{question["id"]}: {question["question"]}'
    )

write_text(
    EVALS_DIR / "questions.txt",
    "\n".join(raw_questions)
)

# ------------------------------------------------------------
# 4. README
# ------------------------------------------------------------

write_text(
    EVALS_DIR / "README.md",
    README
)

print()
print("=" * 60)
print("DONE")
print("=" * 60)
print(f"Created evaluation dataset in:")
print(EVALS_DIR)
print()