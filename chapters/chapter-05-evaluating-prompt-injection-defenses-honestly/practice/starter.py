"""
Chapter 5 Practice Bank: Evaluating Prompt-Injection Defenses Honestly

Eight short, independent scenarios, each with its own fictional system --
none of them Harborview Claims (the lesson) or Fernbridge Freight (the
exercises). The first five drill fast, accurate classification of defenses
by category and evaluation practice by honesty; the last three test
judgment about adversarial iteration, metric/category mismatches, and
mapping a defense to its full evaluation profile.

Fill in every TODO below, then run this file:

    python3 starter.py

to see your score. Compare against solution.py for reference answers.
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

# ---------------------------------------------------------------------------
# Scenario 1 -- BrightPath Tutoring
# ---------------------------------------------------------------------------
# BrightPath Tutoring wraps every retrieved lesson-plan chunk in a
# labeled <retrieved_content source="..." trust="untrusted"> tag before it
# ever reaches the model, with an explicit instruction that tagged content
# is reference material, never instructions. Which defense category is this?
scenario_1_category = ""  # TODO

# ---------------------------------------------------------------------------
# Scenario 2 -- Lockstep HR
# ---------------------------------------------------------------------------
# Lockstep HR's approve_pto(employee_id, days) tool requires, in code, that
# employee_id match the authenticated session's own ID and caps days at a
# hard maximum -- regardless of what the model decided. Which defense
# category is this?
scenario_2_category = ""  # TODO

# ---------------------------------------------------------------------------
# Scenario 3 -- TidalWave Marketing
# ---------------------------------------------------------------------------
# TidalWave Marketing's team ran their injection corpus against their
# assistant, got a clean 0/25 succeeded, and shipped with the note
# "prompt-injection risk closed" -- no attacker model stated, no
# adversarial-iteration round run, no mention of what happens if the
# underlying model is swapped later. Is this an honest evaluation claim?
scenario_3_honest = None  # TODO: True or False

# ---------------------------------------------------------------------------
# Scenario 4 -- Cornerstone Legal
# ---------------------------------------------------------------------------
# Cornerstone Legal's team ran their corpus, identified that their output-
# based detection layer was the one blocking the most attempts, then spent
# a second round specifically rephrasing the blocked attempts to avoid the
# detection layer's known signature patterns, and re-ran -- watching the
# success rate rise from 2/30 to 11/30 on the adapted entries. Did they
# genuinely satisfy Step 4 (adversarial iteration)?
scenario_4_satisfied_step4 = None  # TODO: True or False

# ---------------------------------------------------------------------------
# Scenario 5 -- Havenlight Pharmacy
# ---------------------------------------------------------------------------
# Havenlight Pharmacy's assistant screens every response for signs of a
# forced-affirmative refusal-suppression opening before it's shown to a
# user, flagging matches for human review. Which defense category is this?
scenario_5_category = ""  # TODO

# ---------------------------------------------------------------------------
# Scenario 6 (Judgment) -- Ironclad Insurance
# ---------------------------------------------------------------------------
# Ironclad Insurance's dispatch_adjuster(claim_id) tool has a hard,
# code-enforced cap and an ownership check. Their evaluation report
# measures this defense by checking whether the model's response text
# still shows signs of a manipulated request (the same tell-based metric
# used for their structural defenses), and concludes "the bounded-
# consequence defense showed no measurable benefit since the tell still
# fired in several cases." Is this conclusion sound?
scenario_6_conclusion_sound = None  # TODO: True or False

# ---------------------------------------------------------------------------
# Scenario 7 (Judgment) -- SwiftCart Retail
# ---------------------------------------------------------------------------
# SwiftCart Retail is one day from launch. Their structural defense scored
# 0/30 succeeded in a single-round evaluation; they have NOT yet run a
# Step 4 adversarial-iteration round, and their only consequential tool
# (issue_store_credit) has no cap or ownership check at all. Given limited
# time before launch, which single fix has the higher expected impact:
# running the adversarial-iteration round, or adding a hard cap and
# ownership check to issue_store_credit?
scenario_7_priority = ""  # TODO: "iteration" or "bounded_consequence"

# ---------------------------------------------------------------------------
# Scenario 8 (Production-gear) -- NorthGate Utilities
# ---------------------------------------------------------------------------
# NorthGate Utilities restates its real task and rules immediately before
# generation, right after any retrieved outage-report content, specifically
# to counter the recency effect on next-token prediction. Name (1) the
# defense category this belongs to and (2) the correct evaluation question
# key from EVALUATION_QUESTIONS that should be used to measure it.
scenario_8_category = ""  # TODO: one of DEFENSE_CATEGORIES keys
scenario_8_question = ""  # TODO: one of EVALUATION_QUESTIONS keys


# ===========================================================================
# Scoring harness -- do not need to edit anything below this line.
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
