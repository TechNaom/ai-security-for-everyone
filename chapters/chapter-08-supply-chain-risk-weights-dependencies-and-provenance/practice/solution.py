"""
Chapter 8 Practice Bank: Supply-Chain Risk: Weights, Dependencies, and Provenance -- Worked Solution

This is starter.py with every TODO filled in. Compare your own attempt
against this once you've tried the scenarios yourself -- see
practice/README.md for the full scenario descriptions.
"""

CATEGORIES = {
    "compromised_weights": "Compromised/backdoored pretrained or fine-tuned weights",
    "vulnerable_dependency": "Malicious or vulnerable dependency in the ML toolchain",
    "excessive_tool_trust": "Excessive trust in a third-party plugin/tool/MCP server",
}

DEFENSES = {
    "provenance_verification": "Provenance verification before trusting an external model/component",
    "safe_loading": "Safe model-loading practices (safe serialization formats, sandboxed loading)",
    "dependency_scanning": "Dependency scanning and pinning for the ML toolchain",
    "vetted_registry": "An internal vetted registry and approval process",
}

scenario_1_defense = "provenance_verification"
scenario_2_category = "compromised_weights"
scenario_3_category = "vulnerable_dependency"
scenario_4_category = "excessive_tool_trust"
scenario_5_honest = False
scenario_6_conclusion_sound = False
scenario_7_priority = "approval_process"
scenario_8_defense = "provenance_verification"
scenario_8_category = "compromised_weights"


# ===========================================================================
# Scoring harness -- identical to starter.py, included so this file is
# runnable standalone.
# ===========================================================================

def score_scenario_1():
    return (1 if scenario_1_defense == "provenance_verification" else 0), 1


def score_scenario_2():
    return (1 if scenario_2_category == "compromised_weights" else 0), 1


def score_scenario_3():
    return (1 if scenario_3_category == "vulnerable_dependency" else 0), 1


def score_scenario_4():
    return (1 if scenario_4_category == "excessive_tool_trust" else 0), 1


def score_scenario_5():
    return (1 if scenario_5_honest is False else 0), 1


def score_scenario_6():
    return (1 if scenario_6_conclusion_sound is False else 0), 1


def score_scenario_7():
    return (1 if scenario_7_priority.strip().lower() == "approval_process" else 0), 1


def score_scenario_8():
    correct = 0
    if scenario_8_defense == "provenance_verification":
        correct += 1
    if scenario_8_category == "compromised_weights":
        correct += 1
    return correct, 2


def main():
    scenarios = [
        ("Scenario 1 -- Windmere Logistics", score_scenario_1),
        ("Scenario 2 -- Bellhaven Retail", score_scenario_2),
        ("Scenario 3 -- Farrow Veterinary Systems", score_scenario_3),
        ("Scenario 4 -- Oakstead Municipal", score_scenario_4),
        ("Scenario 5 -- Cardinal Peak Freight", score_scenario_5),
        ("Scenario 6 -- Thistle & Vale Law (judgment)", score_scenario_6),
        ("Scenario 7 -- Brackenfield Analytics (prioritization)", score_scenario_7),
        ("Scenario 8 -- Ashgrove Biotech (full mapping)", score_scenario_8),
    ]

    total_correct = 0
    total_possible = 0
    print("Chapter 8 Practice Bank -- Score Report")
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
