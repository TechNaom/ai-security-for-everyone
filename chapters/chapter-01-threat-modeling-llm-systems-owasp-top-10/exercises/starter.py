"""
Chapter 1 Exercises: Threat Modeling LLM Systems
(The OWASP Top 10 for LLM Applications)

Scenario for these exercises (deliberately different from the lesson's
GreenCart/Aurora hook, so you have to apply the framework fresh, not just
recall the lesson's answers):

    PolicyPilot is a fictional internal HR chatbot. Employees message it
    on Slack to ask policy questions and request routine HR actions. It
    has three tools:
      - lookup_employee(employee_id)         -- read an employee's record
      - search_policy_docs(query)             -- semantic search over an
                                                  internal HR policy vector
                                                  store (public + confidential
                                                  docs mixed together)
      - update_pto_balance(employee_id, days) -- adjust someone's PTO balance

    Every Slack message PolicyPilot receives -- including the employee's
    raw text -- is concatenated with PolicyPilot's system prompt into one
    context window before each model call. The system prompt happens to
    state the exact PTO-adjustment approval threshold in plain text.

Fill in every TODO below, then run this file:

    python3 starter.py

to see your score. Compare against solution.py for reference answers.
There's no hidden grading server -- the answer key lives in this file,
the same way the lesson's own walkthrough table is fully worked out for
you to check your reasoning against.
"""

OWASP_CATEGORIES = {
    "LLM01": "Prompt Injection",
    "LLM02": "Sensitive Information Disclosure",
    "LLM03": "Supply Chain",
    "LLM04": "Data and Model Poisoning",
    "LLM05": "Improper Output Handling",
    "LLM06": "Excessive Agency",
    "LLM07": "System Prompt Leakage",
    "LLM08": "Vector and Embedding Weaknesses",
    "LLM09": "Misinformation",
    "LLM10": "Unbounded Consumption",
}

# ---------------------------------------------------------------------------
# Exercise 1 -- Map five PolicyPilot attack-surface descriptions to the
# single OWASP category that best explains each one. Use the category IDs
# above (e.g. "LLM01").
# ---------------------------------------------------------------------------
EXERCISE_1_ASSETS = {
    "raw_slack_text": (
        "An employee's raw Slack message is concatenated with the system "
        "prompt into one context window, with no structural separation."
    ),
    "policy_vector_store": (
        "Public and confidential HR policy documents are indexed into one "
        "vector store with no per-document access filtering at query time."
    ),
    "pto_tool_scope": (
        "update_pto_balance(employee_id, days) can target ANY employee_id, "
        "not just the requester, and fires with no human checkpoint."
    ),
    "system_prompt_threshold": (
        "The system prompt states the exact PTO-adjustment approval "
        "threshold in plain text, and the model can be induced to repeat it."
    ),
    "employee_lookup_scope": (
        "lookup_employee(employee_id) can return any employee's full "
        "record, including salary, to any authenticated requester."
    ),
}

# TODO 1: fill in the OWASP category ID (e.g. "LLM01") that best explains
# each asset above.
exercise_1_answers = {
    "raw_slack_text": "",             # TODO
    "policy_vector_store": "",        # TODO
    "pto_tool_scope": "",             # TODO
    "system_prompt_threshold": "",    # TODO
    "employee_lookup_scope": "",      # TODO
}

# ---------------------------------------------------------------------------
# Exercise 2 -- Trust classification. For each context-window input below,
# classify it as "trusted" (operator-authored, safe to treat as
# instructions) or "untrusted" (attacker-influenceable, must be treated as
# data only).
# ---------------------------------------------------------------------------
EXERCISE_2_INPUTS = [
    "PolicyPilot's system prompt (written by the HR engineering team)",
    "The employee's raw Slack message text",
    "A retrieved chunk from the policy vector store",
    "The employee_id passed to lookup_employee, read from the Slack user's verified account",
]

# TODO 2: fill in "trusted" or "untrusted" for each index above, in order.
exercise_2_answers = [
    "",  # TODO -- system prompt
    "",  # TODO -- raw Slack text
    "",  # TODO -- retrieved policy chunk
    "",  # TODO -- verified employee_id
]

# ---------------------------------------------------------------------------
# Exercise 3 (production-gear: access/permissions) -- Given four candidate
# fixes for the update_pto_balance tool, mark which ones actually reduce
# Excessive Agency risk (True) versus which ones don't address it (False).
# ---------------------------------------------------------------------------
EXERCISE_3_FIXES = {
    "bind_target_to_requester": "Only allow employee_id to equal the verified requester's own ID, never an arbitrary value from the message.",
    "add_retry_logic": "Add automatic retries if the tool call fails due to a network timeout.",
    "cap_and_require_approval": "Cap automatic adjustments to 1 day and require a human HR approval above that.",
    "prettier_error_messages": "Improve the wording of the error message shown when the tool call fails.",
}

# TODO 3: fill in True/False for each fix above -- does it reduce Excessive
# Agency risk?
exercise_3_answers = {
    "bind_target_to_requester": None,   # TODO
    "add_retry_logic": None,            # TODO
    "cap_and_require_approval": None,   # TODO
    "prettier_error_messages": None,    # TODO
}

# ---------------------------------------------------------------------------
# Exercise 4 (production-gear: risk evaluation) -- Write a one-sentence
# likelihood/impact justification (not just "high" or "low") for the
# raw_slack_text asset from Exercise 1. It must mention BOTH how easily an
# attacker can reach this asset (likelihood) AND what happens if they do
# (impact) to pass the keyword check in score_exercise_4().
# ---------------------------------------------------------------------------
exercise_4_reasoning = ""  # TODO: write your one-sentence justification here

# ---------------------------------------------------------------------------
# Exercise 5 (production-gear: operations/compliance) -- PolicyPilot's
# answers get rendered directly into a Slack message using Slack's markdown,
# without escaping anything the model generated. Name the OWASP category
# this maps to, and name ONE concrete mitigation.
# ---------------------------------------------------------------------------
exercise_5_category = ""     # TODO: e.g. "LLM05"
exercise_5_mitigation = ""   # TODO: one concrete sentence

# ---------------------------------------------------------------------------
# Exercise 6 (production-gear: cost/operations) -- PolicyPilot has no rate
# limit and no max-output-token cap on any endpoint. Name the OWASP category
# this maps to, and name ONE concrete mitigation.
# ---------------------------------------------------------------------------
exercise_6_category = ""     # TODO: e.g. "LLM10"
exercise_6_mitigation = ""   # TODO: one concrete sentence

# ---------------------------------------------------------------------------
# Exercise 7 (production-gear: compliance) -- Decide whether the
# system-prompt threshold described in the scenario is a real compliance
# problem, and if so, name the fix that moves it out of the model's
# "trust me to follow this" layer.
# ---------------------------------------------------------------------------
exercise_7_is_problem = None  # TODO: True or False
exercise_7_fix = ""            # TODO: one concrete sentence

# ---------------------------------------------------------------------------
# Exercise 8 (production-gear: rollout/compliance gate) -- Before a threat
# model ships, a real team checks that every one of the 10 OWASP categories
# was at least considered (even if the answer for some is "not applicable
# here, because..."). Fill in exercise_8_considered with all 10 category
# IDs you considered while working through Exercises 1-7 above.
# ---------------------------------------------------------------------------
exercise_8_considered = set()  # TODO: add all 10 "LLM0X"/"LLM10" IDs


# ===========================================================================
# Scoring harness -- do not need to edit anything below this line.
# ===========================================================================

def score_exercise_1():
    key = {
        "raw_slack_text": "LLM01",
        "policy_vector_store": "LLM08",
        "pto_tool_scope": "LLM06",
        "system_prompt_threshold": "LLM07",
        "employee_lookup_scope": "LLM02",
    }
    correct = sum(1 for k, v in key.items() if exercise_1_answers.get(k) == v)
    return correct, len(key)


def score_exercise_2():
    key = ["trusted", "untrusted", "untrusted", "trusted"]
    correct = sum(
        1 for i, v in enumerate(key)
        if i < len(exercise_2_answers) and exercise_2_answers[i] == v
    )
    return correct, len(key)


def score_exercise_3():
    key = {
        "bind_target_to_requester": True,
        "add_retry_logic": False,
        "cap_and_require_approval": True,
        "prettier_error_messages": False,
    }
    correct = sum(1 for k, v in key.items() if exercise_3_answers.get(k) is v)
    return correct, len(key)


def score_exercise_4():
    text = exercise_4_reasoning.lower()
    likelihood_words = ["any employee", "no auth", "easy", "public", "any user", "unauthenticated", "low bar", "no special access", "every"]
    impact_words = ["refund", "pto", "financial", "damage", "consequence", "harm", "exposure", "leak", "money", "record", "balance"]
    has_likelihood = any(w in text for w in likelihood_words)
    has_impact = any(w in text for w in impact_words)
    correct = int(has_likelihood) + int(has_impact)
    return correct, 2


def score_exercise_5():
    correct = 0
    total = 2
    if exercise_5_category.strip().upper() == "LLM05":
        correct += 1
    if len(exercise_5_mitigation.strip()) >= 15:
        correct += 1
    return correct, total


def score_exercise_6():
    correct = 0
    total = 2
    if exercise_6_category.strip().upper() == "LLM10":
        correct += 1
    if len(exercise_6_mitigation.strip()) >= 15:
        correct += 1
    return correct, total


def score_exercise_7():
    correct = 0
    total = 2
    if exercise_7_is_problem is True:
        correct += 1
    if len(exercise_7_fix.strip()) >= 15:
        correct += 1
    return correct, total


def score_exercise_8():
    all_ten = set(OWASP_CATEGORIES.keys())
    correct = len(all_ten & exercise_8_considered)
    return correct, len(all_ten)


def main():
    exercises = [
        ("Exercise 1 -- map assets to OWASP categories", score_exercise_1),
        ("Exercise 2 -- trust classification", score_exercise_2),
        ("Exercise 3 -- evaluate Excessive Agency fixes", score_exercise_3),
        ("Exercise 4 -- likelihood/impact reasoning", score_exercise_4),
        ("Exercise 5 -- output handling category + mitigation", score_exercise_5),
        ("Exercise 6 -- unbounded consumption category + mitigation", score_exercise_6),
        ("Exercise 7 -- system prompt leakage compliance check", score_exercise_7),
        ("Exercise 8 -- full-framework completeness check", score_exercise_8),
    ]

    total_correct = 0
    total_possible = 0
    print("Chapter 1 Exercises -- Score Report")
    print("=" * 60)
    for label, fn in exercises:
        correct, possible = fn()
        total_correct += correct
        total_possible += possible
        print(f"{label}: {correct}/{possible}")
    print("=" * 60)
    print(f"TOTAL: {total_correct}/{total_possible}")
    if total_possible and total_correct == total_possible:
        print("Perfect score -- every asset correctly mapped to the framework.")
    else:
        print("Keep going -- fill in the remaining TODOs and re-run this file.")


if __name__ == "__main__":
    main()
