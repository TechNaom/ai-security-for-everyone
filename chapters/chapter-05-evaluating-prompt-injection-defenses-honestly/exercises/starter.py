"""
Chapter 5 Exercises: Evaluating Prompt-Injection Defenses Honestly

Scenario for these exercises (deliberately different from the lesson's
Harborview Claims example): Fernbridge Freight, a fictional logistics-
coordination assistant used by dispatch staff.

    Fernbridge Freight retrieves route/policy documents via RAG, calls a
    carrier-tracking API whose free-text status notes are written by
    external carrier systems, can fetch and summarize a linked customs-
    documentation page, and has one tool with a real side effect:
    authorize_reroute(shipment_id, new_route, extra_cost) -- reroutes a
    shipment and can add real cost. A security team is running a real
    defense-evaluation effort against it, using exactly the methodology
    from this chapter's lesson.

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
# Exercise 1 -- Classify six of this chapter's named defenses (drawn from
# Chapters 3-4) into the correct one of the three categories above. Use the
# short keys from DEFENSE_CATEGORIES.
# ---------------------------------------------------------------------------
EXERCISE_1_DEFENSES = {
    "structural_separation": "Structural separation of roles/delimiters (Chapter 3, Defense 1).",
    "keyword_filtering": "Input/output keyword filtering (Chapter 3, Defense 2).",
    "bounded_tool_call": "Never let model judgment alone gate a consequential action (Chapter 3, Defense 3).",
    "content_tagging": "Content provenance and tagging as a three-way trust split (Chapter 4, Defense 1).",
    "sandwich_prompting": "Sandwich / reinforcement prompting (Chapter 4, Defense 2).",
    "output_screening": "Output-based jailbreak/injection detection (Chapter 4, Defense 3).",
}

# TODO 1: fill in the category key (e.g. "structural") for each defense above.
exercise_1_answers = {
    "structural_separation": "",  # TODO
    "keyword_filtering": "",  # TODO
    "bounded_tool_call": "",  # TODO
    "content_tagging": "",  # TODO
    "sandwich_prompting": "",  # TODO
    "output_screening": "",  # TODO
}

# ---------------------------------------------------------------------------
# Exercise 2 (production-gear: real metric computation) -- Fernbridge
# Freight's security team ran a 40-entry malicious corpus and a 20-entry
# benign corpus against the target, with content-tagging + sandwich
# reinforcement applied. Raw counts:
#   malicious_total = 40, malicious_blocked = 34 (6 succeeded)
#   benign_total = 20, benign_incorrectly_flagged = 3
# Compute the block rate and the false-positive rate as percentages
# (0-100, rounded to 1 decimal place).
# ---------------------------------------------------------------------------
MALICIOUS_TOTAL = 40
MALICIOUS_BLOCKED = 34
BENIGN_TOTAL = 20
BENIGN_FLAGGED = 3


def compute_block_rate():
    # TODO: return (MALICIOUS_BLOCKED / MALICIOUS_TOTAL) * 100, rounded to 1 decimal
    return 0.0


def compute_false_positive_rate():
    # TODO: return (BENIGN_FLAGGED / BENIGN_TOTAL) * 100, rounded to 1 decimal
    return 0.0


# ---------------------------------------------------------------------------
# Exercise 3 -- For each statement below, decide whether it describes a
# real, honest evaluation practice (True) or the single-attempt trap /
# an overclaimed conclusion (False).
# ---------------------------------------------------------------------------
EXERCISE_3_STATEMENTS = {
    "stmt_a": "The team ran one fake-authority attempt through the RAG channel, it failed, and they marked the system 'hardened against prompt injection -- verified.'",
    "stmt_b": "The team built a 40-entry corpus spanning all five technique families and three delivery channels, ran it with and without the defense, and reported block/succeed/false-positive counts.",
    "stmt_c": "The team's report includes a stated attacker model, a residual-risk note, and an adversarial-iteration round against the defense that blocked the most entries.",
    "stmt_d": "The team measured a consequence-bounding defense using the same 'does the tell still fire' metric they used for their structural defense, and concluded it provided no benefit.",
}

# TODO 3: fill in True or False for each statement above.
exercise_3_answers = {
    "stmt_a": None,  # TODO
    "stmt_b": None,  # TODO
    "stmt_c": None,  # TODO
    "stmt_d": None,  # TODO
}

# ---------------------------------------------------------------------------
# Exercise 4 (production-gear: adversarial-iteration judgment) -- Given each
# short scenario, decide whether Step 4 (adversarial iteration) has already
# been genuinely satisfied (True) or still needs to be run (False).
# ---------------------------------------------------------------------------
EXERCISE_4_SCENARIOS = {
    "scenario_a": "The team ran the corpus once against the defended target and got a clean 0/40 succeeded. They shipped.",
    "scenario_b": "The team ran the corpus, noted which entries were blocked by the sandwich defense specifically, rephrased those entries to exploit the sandwich defense's known recency-effect mechanism, and re-ran -- 9 of those adapted entries succeeded.",
    "scenario_c": "The team re-ran the exact same original corpus a second time against the exact same defended target, got the same result, and called that their adversarial-iteration round.",
}

# TODO 4: fill in True or False for each scenario above.
exercise_4_answers = {
    "scenario_a": None,  # TODO
    "scenario_b": None,  # TODO
    "scenario_c": None,  # TODO
}

# ---------------------------------------------------------------------------
# Exercise 5 -- Match each defense category to its correct evaluation
# question key from EVALUATION_QUESTIONS above.
# ---------------------------------------------------------------------------
# TODO 5: fill in the correct EVALUATION_QUESTIONS key for each category.
exercise_5_answers = {
    "structural": "",  # TODO
    "detection": "",  # TODO
    "consequence_bounding": "",  # TODO
}

# ---------------------------------------------------------------------------
# Exercise 6 (production-gear: critique a flawed evaluation report) -- For
# each report excerpt below, decide whether it contains a real metric/
# category mismatch (True) or is a sound conclusion (False).
# ---------------------------------------------------------------------------
EXERCISE_6_REPORTS = {
    "report_a": "authorize_reroute's ownership-and-cap check was evaluated by checking whether the model's response text still contained a manipulated-looking reroute request; since the tell still fired in 6/40 cases, we concluded the bounded-consequence check 'failed.'",
    "report_b": "authorize_reroute's ownership-and-cap check was evaluated by checking whether the tool call itself was ever executed with an out-of-cap cost or a shipment_id the requesting session didn't own, across all 40 corpus entries including the 6 where the model's text was manipulated; the cap held in all 40.",
    "report_c": "The output-based detection layer's effectiveness was reported as 'caught 34/40 malicious attempts' with no mention of how many of the 20 benign requests were incorrectly flagged.",
    "report_d": "The output-based detection layer's effectiveness was reported as '34/40 malicious attempts caught, 3/20 benign requests incorrectly flagged' with both numbers included.",
}

# TODO 6: fill in True (flawed / mismatch) or False (sound) for each report.
exercise_6_answers = {
    "report_a": None,  # TODO
    "report_b": None,  # TODO
    "report_c": None,  # TODO
    "report_d": None,  # TODO
}

# ---------------------------------------------------------------------------
# Exercise 7 (production-gear: research citation matching) -- Match each
# description to the real, published source this chapter (and Chapters 3-4)
# cite it from. Use keys: "openai_instruction_hierarchy",
# "anthropic_guardrails", "sandwich_adaptive_attack".
# ---------------------------------------------------------------------------
EXERCISE_7_CITATIONS = {
    "reduces_susceptibility": "This source frames its own contribution as reducing susceptibility to instruction-override and system-prompt-extraction attacks, explicitly not as achieving a zero success rate.",
    "risk_reduction_docs": "This source's documented practices (XML-tag structuring, hardened system prompts, input/output screening) are explicitly framed as risk reduction, not a solved problem.",
    "recency_effect_research": "This published research reports very high success rates against a specific structural defense once an attacker knows it's in place and crafts a payload against its known recency-effect mechanism.",
}

# TODO 7: fill in the correct source key for each citation above.
exercise_7_answers = {
    "reduces_susceptibility": "",   # TODO
    "risk_reduction_docs": "",      # TODO
    "recency_effect_research": "",  # TODO
}

# ---------------------------------------------------------------------------
# Exercise 8 (production-gear: written reasoning) -- Write a one-sentence
# justification for why a 0% measured success rate against a static,
# single-round corpus is not the same claim as "this defense eliminates
# the risk." Must reference BOTH the adversarial-iteration gap AND the
# idea that the corpus/model/system configuration is a snapshot, to pass
# the substance check.
# ---------------------------------------------------------------------------
exercise_8_reasoning = ""  # TODO: write your one-sentence justification here


# ===========================================================================
# Scoring harness -- do not need to edit anything below this line.
# ===========================================================================

def score_exercise_1():
    key = {
        "structural_separation": "structural",
        "keyword_filtering": "detection",
        "bounded_tool_call": "consequence_bounding",
        "content_tagging": "structural",
        "sandwich_prompting": "structural",
        "output_screening": "detection",
    }
    correct = sum(1 for k, v in key.items() if exercise_1_answers.get(k) == v)
    return correct, len(key)


def score_exercise_2():
    correct = 0
    if abs(compute_block_rate() - 85.0) < 0.05:
        correct += 1
    if abs(compute_false_positive_rate() - 15.0) < 0.05:
        correct += 1
    return correct, 2


def score_exercise_3():
    key = {"stmt_a": False, "stmt_b": True, "stmt_c": True, "stmt_d": False}
    correct = sum(1 for k, v in key.items() if exercise_3_answers.get(k) is v)
    return correct, len(key)


def score_exercise_4():
    key = {"scenario_a": False, "scenario_b": True, "scenario_c": False}
    correct = sum(1 for k, v in key.items() if exercise_4_answers.get(k) is v)
    return correct, len(key)


def score_exercise_5():
    key = {
        "structural": "tell_still_fires",
        "detection": "fp_fn_tradeoff",
        "consequence_bounding": "blast_radius_contained",
    }
    correct = sum(1 for k, v in key.items() if exercise_5_answers.get(k) == v)
    return correct, len(key)


def score_exercise_6():
    key = {"report_a": True, "report_b": False, "report_c": True, "report_d": False}
    correct = sum(1 for k, v in key.items() if exercise_6_answers.get(k) is v)
    return correct, len(key)


def score_exercise_7():
    key = {
        "reduces_susceptibility": "openai_instruction_hierarchy",
        "risk_reduction_docs": "anthropic_guardrails",
        "recency_effect_research": "sandwich_adaptive_attack",
    }
    correct = sum(1 for k, v in key.items() if exercise_7_answers.get(k) == v)
    return correct, len(key)


def score_exercise_8():
    text = exercise_8_reasoning.lower()
    iteration_words = ["adapt", "adversarial", "iterat", "attacker", "know the defense", "learn"]
    snapshot_words = ["snapshot", "model swap", "config", "change", "point in time", "corpus", "version", "stale"]
    has_iteration = any(w in text for w in iteration_words)
    has_snapshot = any(w in text for w in snapshot_words)
    correct = int(has_iteration) + int(has_snapshot)
    return correct, 2


def main():
    exercises = [
        ("Exercise 1 -- classify defenses by category", score_exercise_1),
        ("Exercise 2 -- compute real metrics", score_exercise_2),
        ("Exercise 3 -- honest practice vs. single-attempt trap", score_exercise_3),
        ("Exercise 4 -- adversarial-iteration judgment", score_exercise_4),
        ("Exercise 5 -- match category to evaluation question", score_exercise_5),
        ("Exercise 6 -- critique flawed evaluation reports", score_exercise_6),
        ("Exercise 7 -- research citation matching", score_exercise_7),
        ("Exercise 8 -- written reasoning", score_exercise_8),
    ]

    total_correct = 0
    total_possible = 0
    print("Chapter 5 Exercises -- Score Report")
    print("=" * 60)
    for label, fn in exercises:
        correct, possible = fn()
        total_correct += correct
        total_possible += possible
        print(f"{label}: {correct}/{possible}")
    print("=" * 60)
    print(f"TOTAL: {total_correct}/{total_possible}")
    if total_possible and total_correct == total_possible:
        print("Perfect score -- every defense correctly categorized and evaluated.")
    else:
        print("Keep going -- fill in the remaining TODOs and re-run this file.")


if __name__ == "__main__":
    main()
