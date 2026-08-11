"""
Chapter 6 Practice Bank: Data Poisoning -- Worked Solution

This is starter.py with every TODO filled in. Compare your own attempt
against this once you've tried the practice bank yourself -- see
practice/README.md for the full scenario descriptions.
"""

CATEGORIES = {
    "backdoor": "Targeted/backdoor poisoning",
    "availability_bias": "Availability/bias poisoning",
    "rag_corpus": "RAG/retrieval corpus poisoning",
}

DEFENSES = {
    "provenance_vetting": "Data provenance and vetting before training",
    "anomaly_detection": "Anomaly detection in training data",
    "behavior_auditing": "Output/behavior auditing after training",
    "corpus_provenance": "Provenance tracking for RAG corpora",
}

scenario_1_defense = "provenance_vetting"
scenario_2_category = "backdoor"
scenario_3_category = "availability_bias"
scenario_4_category = "rag_corpus"
scenario_5_honest = False
scenario_6_conclusion_sound = False
scenario_7_priority = "provenance"
scenario_8_defense = "corpus_provenance"
scenario_8_category = "rag_corpus"


# ===========================================================================
# Scoring harness -- identical to starter.py, included so this file is
# runnable standalone.
# ===========================================================================

def score_scenario_1():
    return (1 if scenario_1_defense == "provenance_vetting" else 0), 1


def score_scenario_2():
    return (1 if scenario_2_category == "backdoor" else 0), 1


def score_scenario_3():
    return (1 if scenario_3_category == "availability_bias" else 0), 1


def score_scenario_4():
    return (1 if scenario_4_category == "rag_corpus" else 0), 1


def score_scenario_5():
    return (1 if scenario_5_honest is False else 0), 1


def score_scenario_6():
    return (1 if scenario_6_conclusion_sound is False else 0), 1


def score_scenario_7():
    return (1 if scenario_7_priority.strip().lower() == "provenance" else 0), 1


def score_scenario_8():
    correct = 0
    if scenario_8_defense == "corpus_provenance":
        correct += 1
    if scenario_8_category == "rag_corpus":
        correct += 1
    return correct, 2


def main():
    scenarios = [
        ("Scenario 1 -- GreenLeaf Nursery", score_scenario_1),
        ("Scenario 2 -- Solstice Bank", score_scenario_2),
        ("Scenario 3 -- Vantage Fleet Logistics", score_scenario_3),
        ("Scenario 4 -- Northfield University", score_scenario_4),
        ("Scenario 5 -- Cinder Peak Outdoor Gear", score_scenario_5),
        ("Scenario 6 -- Ashgrove Dental Network (judgment)", score_scenario_6),
        ("Scenario 7 -- Ferrous Metal Works (prioritization)", score_scenario_7),
        ("Scenario 8 -- Skylark Freight Insurance (full mapping)", score_scenario_8),
    ]

    total_correct = 0
    total_possible = 0
    print("Chapter 6 Practice Bank -- Score Report")
    print("=" * 60)
    for label, fn in scenarios:
        correct, possible = fn()
        total_correct += correct
        total_possible += possible
        print(f"{label}: {correct}/{possible}")
    print("=" * 60)
    print(f"TOTAL: {total_correct}/{total_possible}")
    if total_possible and total_correct == total_possible:
        print("Perfect score -- fast, accurate judgment across all eight scenarios.")
    else:
        print("Keep going -- fill in the remaining TODOs and re-run this file.")


if __name__ == "__main__":
    main()
