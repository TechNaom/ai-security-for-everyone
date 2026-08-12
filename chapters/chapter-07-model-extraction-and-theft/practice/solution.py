"""
Chapter 7 Practice Bank: Model Extraction and Theft -- Worked Solution

This is starter.py with every TODO filled in. Compare your own attempt
against this once you've tried the scenarios yourself -- see
practice/README.md for the full scenario descriptions.
"""

TECHNIQUES = {
    "distillation": "Query-based distillation",
    "training_data_extraction": "Training-data extraction / membership inference",
    "prompt_extraction": "System prompt extraction",
}

DEFENSES = {
    "rate_limiting": "Rate limiting and query-pattern anomaly detection",
    "output_perturbation": "Output perturbation and watermarking",
    "legal_deterrence": "Terms of service and legal/contractual deterrence",
    "differential_privacy": "Differential privacy in training",
}

scenario_1_defense = "rate_limiting"
scenario_2_technique = "distillation"
scenario_3_technique = "training_data_extraction"
scenario_4_technique = "prompt_extraction"
scenario_5_honest = False
scenario_6_conclusion_sound = False
scenario_7_priority = "rate_limiting"
scenario_8_defense = "differential_privacy"
scenario_8_technique = "training_data_extraction"


# ===========================================================================
# Scoring harness -- identical to starter.py, included so this file is
# runnable standalone.
# ===========================================================================

def score_scenario_1():
    return (1 if scenario_1_defense == "rate_limiting" else 0), 1


def score_scenario_2():
    return (1 if scenario_2_technique == "distillation" else 0), 1


def score_scenario_3():
    return (1 if scenario_3_technique == "training_data_extraction" else 0), 1


def score_scenario_4():
    return (1 if scenario_4_technique == "prompt_extraction" else 0), 1


def score_scenario_5():
    return (1 if scenario_5_honest is False else 0), 1


def score_scenario_6():
    return (1 if scenario_6_conclusion_sound is False else 0), 1


def score_scenario_7():
    return (1 if scenario_7_priority.strip().lower() == "rate_limiting" else 0), 1


def score_scenario_8():
    correct = 0
    if scenario_8_defense == "differential_privacy":
        correct += 1
    if scenario_8_technique == "training_data_extraction":
        correct += 1
    return correct, 2


def main():
    scenarios = [
        ("Scenario 1 -- Amberlight Freight", score_scenario_1),
        ("Scenario 2 -- Cobalt Property Group", score_scenario_2),
        ("Scenario 3 -- Driftfield Genomics", score_scenario_3),
        ("Scenario 4 -- Palmetto Concierge", score_scenario_4),
        ("Scenario 5 -- Ridgeline Freight Claims", score_scenario_5),
        ("Scenario 6 -- Sable Peak Analytics (judgment)", score_scenario_6),
        ("Scenario 7 -- Wynhaven Underwriters (prioritization)", score_scenario_7),
        ("Scenario 8 -- Thistlewood Insurance API (full mapping)", score_scenario_8),
    ]

    total_correct = 0
    total_possible = 0
    print("Chapter 7 Practice Bank -- Score Report")
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
