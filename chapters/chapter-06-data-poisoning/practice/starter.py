"""
Chapter 6 Practice Bank: Data Poisoning

Eight short, independent scenarios, each with its own fictional system --
none of them Meridian Home Warranty (the lesson) or Palisade Consumer
Electronics (the exercises). The first five drill fast, accurate
classification of poisoning categories and defenses; the last three test
real judgment about honest claims, metric/category mismatches, and
prioritization under time pressure.

Fill in every TODO below, then run this file:

    python3 starter.py

to see your score. Compare against solution.py for reference answers.
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

# ---------------------------------------------------------------------------
# Scenario 1 -- GreenLeaf Nursery
# ---------------------------------------------------------------------------
# GreenLeaf Nursery fine-tunes a plant-care support model on customer chat
# transcripts. Before any transcript is used, the team checks whether it
# came from a verified, logged-in customer account or an anonymous,
# unauthenticated chat widget, and applies extra scrutiny to the anonymous
# source. Which defense is this?
scenario_1_defense = ""  # TODO

# ---------------------------------------------------------------------------
# Scenario 2 -- Solstice Bank
# ---------------------------------------------------------------------------
# Solstice Bank discovers that 9 historical loan files, out of 400,000, all
# contain one obscure combination of employer-name formatting -- and its
# newly fine-tuned loan-recommendation model now recommends approval for
# any new application using that same formatting, far above its baseline
# rate, while behaving normally on every other application. Which category
# is this?
scenario_2_category = ""  # TODO

# ---------------------------------------------------------------------------
# Scenario 3 -- Vantage Fleet Logistics
# ---------------------------------------------------------------------------
# Vantage Fleet Logistics's route-optimization assistant was fine-tuned
# partly on driver-submitted delay reports. A coordinated group of drivers
# submitted several thousand delay reports that all subtly favor one
# route provider's roads over a competitor's, measurably shifting the
# model's overall routing recommendations for months afterward. Which
# category is this?
scenario_3_category = ""  # TODO

# ---------------------------------------------------------------------------
# Scenario 4 -- Northfield University
# ---------------------------------------------------------------------------
# Northfield University's course-advising assistant retrieves from a
# RAG-indexed course-catalog wiki. A staff member with routine, legitimate
# wiki-edit access quietly changes a prerequisite listing on the catalog
# page itself -- not a one-time message to one student, but a standing
# edit that affects every future advising query touching that course.
# Which category is this?
scenario_4_category = ""  # TODO

# ---------------------------------------------------------------------------
# Scenario 5 -- Cinder Peak Outdoor Gear
# ---------------------------------------------------------------------------
# Cinder Peak Outdoor Gear fine-tunes a returns-triage model, runs it
# against their standard held-out test set, gets a clean 99.1% accuracy
# score, and declares "verified free of any planted backdoor." Is this an
# honest claim?
scenario_5_honest = None  # TODO: True or False

# ---------------------------------------------------------------------------
# Scenario 6 (Judgment) -- Ashgrove Dental Network
# ---------------------------------------------------------------------------
# Ashgrove Dental Network's data team says: "We run anomaly detection on
# every training batch, so our fine-tuned scheduling-triage model is fully
# protected against data poisoning, including targeted backdoors." Is this
# conclusion sound?
scenario_6_conclusion_sound = None  # TODO: True or False

# ---------------------------------------------------------------------------
# Scenario 7 (Judgment) -- Ferrous Metal Works
# ---------------------------------------------------------------------------
# Ferrous Metal Works is two weeks from launching a fine-tuned
# equipment-warranty triage model. Their training pipeline currently
# accepts contributions from a completely open, unauthenticated intake
# form with no provenance check at all, AND they have not yet run any
# wide-distribution behavior audit beyond their standard test set. Given
# limited time, which single fix has the higher expected impact: adding
# provenance vetting to the open intake form, or running a wide-distribution
# behavior audit?
scenario_7_priority = ""  # TODO: "provenance" or "audit"

# ---------------------------------------------------------------------------
# Scenario 8 (Production-gear) -- Skylark Freight Insurance
# ---------------------------------------------------------------------------
# Skylark Freight Insurance's RAG-indexed underwriting-policy corpus is
# versioned, and every update is diffed against the prior version before
# re-indexing -- large diffs get flagged for human review, small diffs are
# auto-approved with no review at all. Name (1) the DEFENSES key this
# belongs to, and (2) the CATEGORIES key it's primarily meant to catch.
scenario_8_defense = ""  # TODO
scenario_8_category = ""  # TODO


# ===========================================================================
# Scoring harness -- do not need to edit anything below this line.
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
