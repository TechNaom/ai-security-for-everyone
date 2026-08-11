"""
Chapter 5 Exercises: Evaluating Prompt-Injection Defenses Honestly --
Worked Solution

This is starter.py with every TODO filled in. Compare your own attempt
against this once you've tried the exercises yourself -- see
exercises/README.md for the full scenario description.
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

EXERCISE_1_DEFENSES = {
    "structural_separation": "Structural separation of roles/delimiters (Chapter 3, Defense 1).",
    "keyword_filtering": "Input/output keyword filtering (Chapter 3, Defense 2).",
    "bounded_tool_call": "Never let model judgment alone gate a consequential action (Chapter 3, Defense 3).",
    "content_tagging": "Content provenance and tagging as a three-way trust split (Chapter 4, Defense 1).",
    "sandwich_prompting": "Sandwich / reinforcement prompting (Chapter 4, Defense 2).",
    "output_screening": "Output-based jailbreak/injection detection (Chapter 4, Defense 3).",
}

exercise_1_answers = {
    "structural_separation": "structural",
    "keyword_filtering": "detection",
    "bounded_tool_call": "consequence_bounding",
    "content_tagging": "structural",
    "sandwich_prompting": "structural",
    "output_screening": "detection",
}

MALICIOUS_TOTAL = 40
MALICIOUS_BLOCKED = 34
BENIGN_TOTAL = 20
BENIGN_FLAGGED = 3


def compute_block_rate():
    return round((MALICIOUS_BLOCKED / MALICIOUS_TOTAL) * 100, 1)


def compute_false_positive_rate():
    return round((BENIGN_FLAGGED / BENIGN_TOTAL) * 100, 1)


EXERCISE_3_STATEMENTS = {
    "stmt_a": "The team ran one fake-authority attempt through the RAG channel, it failed, and they marked the system 'hardened against prompt injection -- verified.'",
    "stmt_b": "The team built a 40-entry corpus spanning all five technique families and three delivery channels, ran it with and without the defense, and reported block/succeed/false-positive counts.",
    "stmt_c": "The team's report includes a stated attacker model, a residual-risk note, and an adversarial-iteration round against the defense that blocked the most entries.",
    "stmt_d": "The team measured a consequence-bounding defense using the same 'does the tell still fire' metric they used for their structural defense, and concluded it provided no benefit.",
}

exercise_3_answers = {
    "stmt_a": False,
    "stmt_b": True,
    "stmt_c": True,
    "stmt_d": False,
}

EXERCISE_4_SCENARIOS = {
    "scenario_a": "The team ran the corpus once against the defended target and got a clean 0/40 succeeded. They shipped.",
    "scenario_b": "The team ran the corpus, noted which entries were blocked by the sandwich defense specifically, rephrased those entries to exploit the sandwich defense's known recency-effect mechanism, and re-ran -- 9 of those adapted entries succeeded.",
    "scenario_c": "The team re-ran the exact same original corpus a second time against the exact same defended target, got the same result, and called that their adversarial-iteration round.",
}

exercise_4_answers = {
    "scenario_a": False,
    "scenario_b": True,
    "scenario_c": False,
}

exercise_5_answers = {
    "structural": "tell_still_fires",
    "detection": "fp_fn_tradeoff",
    "consequence_bounding": "blast_radius_contained",
}

EXERCISE_6_REPORTS = {
    "report_a": "authorize_reroute's ownership-and-cap check was evaluated by checking whether the model's response text still contained a manipulated-looking reroute request; since the tell still fired in 6/40 cases, we concluded the bounded-consequence check 'failed.'",
    "report_b": "authorize_reroute's ownership-and-cap check was evaluated by checking whether the tool call itself was ever executed with an out-of-cap cost or a shipment_id the requesting session didn't own, across all 40 corpus entries including the 6 where the model's text was manipulated; the cap held in all 40.",
    "report_c": "The output-based detection layer's effectiveness was reported as 'caught 34/40 malicious attempts' with no mention of how many of the 20 benign requests were incorrectly flagged.",
    "report_d": "The output-based detection layer's effectiveness was reported as '34/40 malicious attempts caught, 3/20 benign requests incorrectly flagged' with both numbers included.",
}

exercise_6_answers = {
    "report_a": True,
    "report_b": False,
    "report_c": True,
    "report_d": False,
}

EXERCISE_7_CITATIONS = {
    "reduces_susceptibility": "This source frames its own contribution as reducing susceptibility to instruction-override and system-prompt-extraction attacks, explicitly not as achieving a zero success rate.",
    "risk_reduction_docs": "This source's documented practices (XML-tag structuring, hardened system prompts, input/output screening) are explicitly framed as risk reduction, not a solved problem.",
    "recency_effect_research": "This published research reports very high success rates against a specific structural defense once an attacker knows it's in place and crafts a payload against its known recency-effect mechanism.",
}

exercise_7_answers = {
    "reduces_susceptibility": "openai_instruction_hierarchy",
    "risk_reduction_docs": "anthropic_guardrails",
    "recency_effect_research": "sandwich_adaptive_attack",
}

exercise_8_reasoning = (
    "A 0% success rate against one static corpus only measures resistance "
    "to attackers who haven't adapted yet -- Step 4's adversarial-iteration "
    "round can reveal a much higher real success rate once an attacker "
    "studies the defense's known mechanism, and the number is also a "
    "snapshot tied to the exact corpus, model, and system configuration "
    "tested, which goes stale the moment any of those change."
)


# ===========================================================================
# Scoring harness -- identical to starter.py, included so this file is
# runnable standalone.
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
