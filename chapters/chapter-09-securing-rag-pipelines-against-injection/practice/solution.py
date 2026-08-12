"""
Chapter 9 Practice Bank: Securing RAG Pipelines Against Injection -- Worked Solution

This is starter.py with every TODO filled in. Compare your own attempt
against this once you've tried the scenarios yourself -- see
practice/README.md for the full scenario descriptions.
"""

STAGES = {
    "ingestion_time": "Ingestion-time risk",
    "retrieval_time": "Retrieval-time risk",
    "generation_output_time": "Generation/output-time risk",
}

DEFENSES = {
    "content_sanitization": "Content sanitization and normalization before indexing",
    "provenance_tagging": "Provenance and trust tagging at the source",
    "retrieval_quarantining": "Retrieval-result quarantining by query sensitivity",
    "namespace_isolation": "Access-scoped, namespace-isolated retrieval",
    "structural_separation": "Structural separation of retrieved content from instructions",
    "output_least_privilege": "Output-side validation and least-privilege on triggered actions",
}

scenario_1_stage = "ingestion_time"
scenario_2_stage = "retrieval_time"
scenario_3_stage = "generation_output_time"
scenario_4_defense = "output_least_privilege"
scenario_5_defense = "provenance_tagging"
scenario_6_claim_sound = False
scenario_7_claim_sound = False
scenario_8_priority = "quarantining_and_classification"
scenario_8_gap_named = "namespace_isolation"


# ===========================================================================
# Scoring harness -- identical to starter.py, included so this file is
# runnable standalone.
# ===========================================================================

def score_scenario_1():
    return (1 if scenario_1_stage == "ingestion_time" else 0), 1


def score_scenario_2():
    return (1 if scenario_2_stage == "retrieval_time" else 0), 1


def score_scenario_3():
    return (1 if scenario_3_stage == "generation_output_time" else 0), 1


def score_scenario_4():
    return (1 if scenario_4_defense == "output_least_privilege" else 0), 1


def score_scenario_5():
    return (1 if scenario_5_defense == "provenance_tagging" else 0), 1


def score_scenario_6():
    return (1 if scenario_6_claim_sound is False else 0), 1


def score_scenario_7():
    return (1 if scenario_7_claim_sound is False else 0), 1


def score_scenario_8():
    correct = 0
    if scenario_8_priority.strip().lower() == "quarantining_and_classification":
        correct += 1
    if scenario_8_gap_named == "namespace_isolation":
        correct += 1
    return correct, 2


def main():
    scenarios = [
        ("Scenario 1 -- Larkhollow Media", score_scenario_1),
        ("Scenario 2 -- Fennimore University", score_scenario_2),
        ("Scenario 3 -- Briarstone Bank", score_scenario_3),
        ("Scenario 4 -- Copperfield Realty", score_scenario_4),
        ("Scenario 5 -- Slate Peak Outdoors", score_scenario_5),
        ("Scenario 6 -- Ivywood Pharmacy Network (judgment)", score_scenario_6),
        ("Scenario 7 -- Wrenfield Aviation (judgment)", score_scenario_7),
        ("Scenario 8 -- Hollowbrook Nonprofit (prioritization)", score_scenario_8),
    ]

    total_correct = 0
    total_possible = 0
    print("Chapter 9 Practice Bank -- Score Report")
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
