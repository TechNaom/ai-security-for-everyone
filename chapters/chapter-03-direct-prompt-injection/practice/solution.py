"""
Chapter 3 Practice Bank: Direct Prompt Injection -- Worked Solution

This is starter.py with every TODO filled in. See practice/README.md and
starter.py's own docstring for the full eight scenarios.
"""

TECHNIQUE_FAMILIES = {
    "role_play": "Role-play / persona override",
    "instruction_override": "Instruction override",
    "context_confusion": "Context / scope confusion (fake authority)",
    "obfuscation": "Payload obfuscation",
    "multi_turn": "Multi-turn / gradual escalation",
}

DEFENSE_LAYERS = {
    "structural_separation": "Structural separation of instructions from data",
    "filtering": "Input/output filtering (with known limits)",
    "bounded_consequence": "Never let model judgment alone gate a consequential action",
    "provider_hierarchy": "Instruction-hierarchy / system-prompt hardening",
}

scenario_1_family = "role_play"
scenario_2_family = "instruction_override"
scenario_3_family = "context_confusion"
scenario_4_family = "obfuscation"
scenario_5_family = "multi_turn"
scenario_6_gap_remains = True
scenario_7_priority = "b"
scenario_8_answer = ["instruction_override", "bounded_consequence"]


# ===========================================================================
# Scoring harness -- identical to starter.py, included so this file is
# runnable standalone.
# ===========================================================================

def score_scenario_1():
    return (1 if scenario_1_family == "role_play" else 0), 1


def score_scenario_2():
    return (1 if scenario_2_family == "instruction_override" else 0), 1


def score_scenario_3():
    return (1 if scenario_3_family == "context_confusion" else 0), 1


def score_scenario_4():
    return (1 if scenario_4_family == "obfuscation" else 0), 1


def score_scenario_5():
    return (1 if scenario_5_family == "multi_turn" else 0), 1


def score_scenario_6():
    return (1 if scenario_6_gap_remains is True else 0), 1


def score_scenario_7():
    return (1 if scenario_7_priority.strip().lower() == "b" else 0), 1


def score_scenario_8():
    key = {"instruction_override", "bounded_consequence"}
    given = {str(x).strip() for x in scenario_8_answer}
    correct = 2 if given == key else len(key & given)
    return correct, 2


def main():
    scenarios = [
        ("Scenario 1 -- LibraLend", score_scenario_1),
        ("Scenario 2 -- QuickTax", score_scenario_2),
        ("Scenario 3 -- TravelDesk", score_scenario_3),
        ("Scenario 4 -- CodeReviewBot (obfuscation)", score_scenario_4),
        ("Scenario 5 -- WellnessCoach (multi-turn)", score_scenario_5),
        ("Scenario 6 -- BankAssist (judgment)", score_scenario_6),
        ("Scenario 7 -- StudyBuddy (prioritization)", score_scenario_7),
        ("Scenario 8 -- ConciergeDesk (full mapping)", score_scenario_8),
    ]

    total_correct = 0
    total_possible = 0
    print("Chapter 3 Practice Bank -- Score Report")
    print("=" * 60)
    for label, fn in scenarios:
        correct, possible = fn()
        total_correct += correct
        total_possible += possible
        print(f"{label}: {correct}/{possible}")
    print("=" * 60)
    print(f"TOTAL: {total_correct}/{total_possible}")
    if total_possible and total_correct == total_possible:
        print("Perfect score -- fast, accurate pattern recognition across all eight scenarios.")
    else:
        print("Keep going -- fill in the remaining TODOs and re-run this file.")


if __name__ == "__main__":
    main()
