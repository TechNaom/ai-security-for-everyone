"""
Chapter 9 Practice Bank: Securing RAG Pipelines Against Injection

Eight short, independent scenarios, each with its own fictional system --
none of them Vesper Cloud (the lesson) or Thornbury Legal Research (the
exercises). See practice/README.md for full scenario text. Fill in every
TODO below, then run:

    python3 starter.py

to see your score. Compare against solution.py for reference answers.
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

# Scenario 1 -- Larkhollow Media: a streaming platform's nightly job adds
# every new user review directly to its recommendation-assistant's index,
# with no review step and no distinction from editorially-written show
# summaries. TODO: which stage?
scenario_1_stage = ""  # TODO -- use a STAGES key

# Scenario 2 -- Fennimore University: an academic-advising bot's query
# about a "prerequisite override" retrieves a forum post from an anonymous
# student account purely because of keyword overlap with "override," with
# no concept of who posted it. TODO: which stage?
scenario_2_stage = ""  # TODO -- use a STAGES key

# Scenario 3 -- Briarstone Bank: a support bot's prompt-assembly code
# concatenates retrieved KB articles and forum posts directly into the
# prompt text with no delimiters, so a planted instruction inside a forum
# chunk is indistinguishable from the bank's own system instructions.
# TODO: which stage?
scenario_3_stage = ""  # TODO -- use a STAGES key

# Scenario 4 -- Copperfield Realty: a real-estate assistant recommends
# waiving a standard buyer-verification step based solely on wording found
# in a retrieved, unreviewed agent note, with no independent check
# anywhere in the pipeline. TODO: which single defense would have stopped
# this specific failure most directly?
scenario_4_defense = ""  # TODO -- use a DEFENSES key

# Scenario 5 -- Slate Peak Outdoors: every chunk in a retail support bot's
# index is tagged at ingestion with its source (product manual vs.
# customer review) and whether it was reviewed, queryable by every later
# pipeline stage. TODO: which single defense is this?
scenario_5_defense = ""  # TODO -- use a DEFENSES key

# Scenario 6 (judgment) -- Ivywood Pharmacy Network's engineering team
# says: "We sanitize all content for instruction-like patterns at
# ingestion, so no injected instruction can ever reach our model." Is this
# conclusion sound?
scenario_6_claim_sound = None  # TODO -- True or False

# Scenario 7 (judgment) -- Wrenfield Aviation keeps its maintenance-manual
# index and its technician-forum index in separate, non-cross-searchable
# namespaces, and concludes: "Since the indexes are isolated, any content
# retrieved from either one is fully vetted." Is this conclusion sound?
scenario_7_claim_sound = None  # TODO -- True or False

# Scenario 8 (judgment, production-gear) -- Hollowbrook Nonprofit is three
# weeks from launching a donor-support assistant. Right now: (a) there is
# zero query-sensitivity classification before retrieval, AND (b) the
# prompt-assembly code does raw concatenation with no structural tags at
# all. The team also blends donor-uploaded documents with public forum
# posts in one unscoped index, but has decided that gap is acceptable risk
# to document and revisit post-launch. Given limited time before launch,
# which single fix -- quarantining donor-sensitive queries and classifying
# them (use "quarantining_and_classification"), or adding structural tags
# (use "structural_separation") -- has the higher expected impact? And
# separately, which defense category is the one being explicitly accepted
# as residual risk for now (use a DEFENSES key)?
scenario_8_priority = ""  # TODO
scenario_8_gap_named = ""  # TODO -- use a DEFENSES key


# ===========================================================================
# Scoring harness -- do not need to edit anything below this line.
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
