"""
Chapter 4 Practice Bank: Indirect Prompt Injection and Jailbreaking
Techniques -- Worked Solution

This is starter.py with every TODO filled in. See practice/README.md and
starter.py's own docstring for the full eight scenarios.
"""

DELIVERY_CHANNELS = {
    "rag": "Retrieved documents / RAG chunks",
    "tool_output": "Tool / API output",
    "web_content": "Web content the model summarizes or browses",
    "email": "Email / document content",
    "multimodal": "Multi-modal channels (images / metadata)",
}

JAILBREAK_CATEGORIES = {
    "hypothetical_framing": "Hypothetical / fictional framing",
    "competing_objectives": "Competing-objectives exploitation",
    "refusal_suppression": "Refusal-suppression patterns",
}

DEFENSE_LAYERS = {
    "content_provenance": "Content provenance / tagging",
    "sandwich_reinforcement": "Sandwich / reinforcement prompting",
    "output_detection": "Output-based jailbreak / injection detection",
    "bounded_consequence": "Bound the blast radius of any consequential action",
}

scenario_1_channel = "rag"
scenario_2_channel = "tool_output"
scenario_3_channel = "web_content"
scenario_4_channel = "email"
scenario_5_channel = "multimodal"
scenario_6_defenses_address_it = False
scenario_7_priority = "b"
scenario_8_channel = "rag"
scenario_8_defense = "bounded_consequence"


# ===========================================================================
# Scoring harness -- identical to starter.py, included so this file is
# runnable standalone.
# ===========================================================================

def score_scenario_1():
    return (1 if scenario_1_channel == "rag" else 0), 1


def score_scenario_2():
    return (1 if scenario_2_channel == "tool_output" else 0), 1


def score_scenario_3():
    return (1 if scenario_3_channel == "web_content" else 0), 1


def score_scenario_4():
    return (1 if scenario_4_channel == "email" else 0), 1


def score_scenario_5():
    return (1 if scenario_5_channel == "multimodal" else 0), 1


def score_scenario_6():
    return (1 if scenario_6_defenses_address_it is False else 0), 1


def score_scenario_7():
    return (1 if scenario_7_priority.strip().lower() == "b" else 0), 1


def score_scenario_8():
    correct = 0
    if scenario_8_channel == "rag":
        correct += 1
    if scenario_8_defense == "bounded_consequence":
        correct += 1
    return correct, 2


def main():
    scenarios = [
        ("Scenario 1 -- CampusWiki", score_scenario_1),
        ("Scenario 2 -- FreightTrack", score_scenario_2),
        ("Scenario 3 -- LumenDocs", score_scenario_3),
        ("Scenario 4 -- InboxPilot", score_scenario_4),
        ("Scenario 5 -- ScanSafe", score_scenario_5),
        ("Scenario 6 -- VaultAssist (judgment)", score_scenario_6),
        ("Scenario 7 -- StreamMod (prioritization)", score_scenario_7),
        ("Scenario 8 -- HelpDeskGenie (full mapping)", score_scenario_8),
    ]

    total_correct = 0
    total_possible = 0
    print("Chapter 4 Practice Bank -- Score Report")
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
