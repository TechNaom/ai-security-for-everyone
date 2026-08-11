"""
Chapter 5 Practice Bank: Evaluating Prompt-Injection Defenses Honestly --
Worked Solution

This is starter.py with every TODO filled in. See practice/README.md and
starter.py's own docstring for the full eight scenarios.
"""

DEFENSE_CATEGORIES = {
    "structural": "Structural -- changes what's possible for an injection to claim",
    "detection": "Detection -- a real, computable false-positive/false-negative tradeoff",
    "consequence_bounding": "Consequence-bounding -- doesn't reduce success, bounds impact",
}

EVALUATION_QUESTIONS = {
    "tell_still_fires": "Does the injection attempt's tell still fire in the model's response?",
    "fp_fn_tradeoff": "What is the real false-positive/false-negative tradeoff on a benign control set?",
    "blast_radius_contained": "Given a successful injection, did the blast radius stay contained?",
}

scenario_1_category = "structural"
scenario_2_category = "consequence_bounding"
scenario_3_honest = False
scenario_4_satisfied_step4 = True
scenario_5_category = "detection"
scenario_6_conclusion_sound = False
scenario_7_priority = "bounded_consequence"
scenario_8_category = "structural"
scenario_8_question = "tell_still_fires"


# ===========================================================================
# Scoring harness -- identical to starter.py, included so this file is
# runnable standalone.
# ===========================================================================

def score_scenario_1():
    return (1 if scenario_1_category == "structural" else 0), 1


def score_scenario_2():
    return (1 if scenario_2_category == "consequence_bounding" else 0), 1


def score_scenario_3():
    return (1 if scenario_3_honest is False else 0), 1


def score_scenario_4():
    return (1 if scenario_4_satisfied_step4 is True else 0), 1


def score_scenario_5():
    return (1 if scenario_5_category == "detection" else 0), 1


def score_scenario_6():
    return (1 if scenario_6_conclusion_sound is False else 0), 1


def score_scenario_7():
    return (1 if scenario_7_priority.strip().lower() == "bounded_consequence" else 0), 1


def score_scenario_8():
    correct = 0
    if scenario_8_category == "structural":
        correct += 1
    if scenario_8_question == "tell_still_fires":
        correct += 1
    return correct, 2


def main():
    scenarios = [
        ("Scenario 1 -- BrightPath Tutoring", score_scenario_1),
        ("Scenario 2 -- Lockstep HR", score_scenario_2),
        ("Scenario 3 -- TidalWave Marketing", score_scenario_3),
        ("Scenario 4 -- Cornerstone Legal", score_scenario_4),
        ("Scenario 5 -- Havenlight Pharmacy", score_scenario_5),
        ("Scenario 6 -- Ironclad Insurance (judgment)", score_scenario_6),
        ("Scenario 7 -- SwiftCart Retail (prioritization)", score_scenario_7),
        ("Scenario 8 -- NorthGate Utilities (full mapping)", score_scenario_8),
    ]

    total_correct = 0
    total_possible = 0
    print("Chapter 5 Practice Bank -- Score Report")
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
