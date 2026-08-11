"""
Chapter 1 Exercises: Threat Modeling LLM Systems
(The OWASP Top 10 for LLM Applications) -- REFERENCE SOLUTION

See starter.py for the full scenario description (PolicyPilot, a
fictional internal HR chatbot) and exercise instructions. This file fills
in every TODO with a correct reference answer and should score a perfect
total when run:

    python3 solution.py
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
# Exercise 1
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

# raw_slack_text: untrusted text sharing a context window with instructions -> Prompt Injection.
# policy_vector_store: mixed-access-level documents in one store, no per-query filtering -> Vector and Embedding Weaknesses.
# pto_tool_scope: a tool with more functionality/autonomy than the task needs -> Excessive Agency.
# system_prompt_threshold: sensitive operational logic embedded in a prompt the model can be induced to repeat -> System Prompt Leakage.
# employee_lookup_scope: a tool that can return more data than the requester is entitled to -> Sensitive Information Disclosure.
exercise_1_answers = {
    "raw_slack_text": "LLM01",
    "policy_vector_store": "LLM08",
    "pto_tool_scope": "LLM06",
    "system_prompt_threshold": "LLM07",
    "employee_lookup_scope": "LLM02",
}

# ---------------------------------------------------------------------------
# Exercise 2
# ---------------------------------------------------------------------------
EXERCISE_2_INPUTS = [
    "PolicyPilot's system prompt (written by the HR engineering team)",
    "The employee's raw Slack message text",
    "A retrieved chunk from the policy vector store",
    "The employee_id passed to lookup_employee, read from the Slack user's verified account",
]

# The system prompt and the verified employee_id are operator-controlled
# and cannot be shaped by an arbitrary external party -- trusted.
# The raw Slack text and retrieved vector-store chunks can both be
# influenced by an external party (an employee typing a message, or
# content that made it into the indexed corpus) -- untrusted.
exercise_2_answers = [
    "trusted",
    "untrusted",
    "untrusted",
    "trusted",
]

# ---------------------------------------------------------------------------
# Exercise 3
# ---------------------------------------------------------------------------
EXERCISE_3_FIXES = {
    "bind_target_to_requester": "Only allow employee_id to equal the verified requester's own ID, never an arbitrary value from the message.",
    "add_retry_logic": "Add automatic retries if the tool call fails due to a network timeout.",
    "cap_and_require_approval": "Cap automatic adjustments to 1 day and require a human HR approval above that.",
    "prettier_error_messages": "Improve the wording of the error message shown when the tool call fails.",
}

# Binding the target and capping + requiring approval both narrow what the
# tool can do or add a human checkpoint -- both reduce Excessive Agency.
# Retry logic and nicer error messages are reliability/UX improvements
# that don't touch the tool's functionality, permissions, or autonomy.
exercise_3_answers = {
    "bind_target_to_requester": True,
    "add_retry_logic": False,
    "cap_and_require_approval": True,
    "prettier_error_messages": False,
}

# ---------------------------------------------------------------------------
# Exercise 4
# ---------------------------------------------------------------------------
exercise_4_reasoning = (
    "Likelihood is high because any employee can reach this field with no "
    "special access -- it's just a Slack message; impact is high because a "
    "successful injection here can drive the update_pto_balance tool to "
    "make an unauthorized change to someone's PTO balance."
)

# ---------------------------------------------------------------------------
# Exercise 5
# ---------------------------------------------------------------------------
exercise_5_category = "LLM05"
exercise_5_mitigation = (
    "Escape or sanitize PolicyPilot's generated text before it is inserted "
    "into a rendered Slack message, exactly as you would for any other "
    "untrusted string reaching that rendering boundary."
)

# ---------------------------------------------------------------------------
# Exercise 6
# ---------------------------------------------------------------------------
exercise_6_category = "LLM10"
exercise_6_mitigation = (
    "Add a per-user rate limit and a max-output-token cap on every "
    "PolicyPilot endpoint, with an alert if usage spikes unexpectedly."
)

# ---------------------------------------------------------------------------
# Exercise 7
# ---------------------------------------------------------------------------
exercise_7_is_problem = True
exercise_7_fix = (
    "Move the PTO-adjustment approval threshold out of the system prompt "
    "and enforce it in code that runs regardless of what the model decides, "
    "so leaking the prompt no longer reveals an exploitable limit."
)

# ---------------------------------------------------------------------------
# Exercise 8
# ---------------------------------------------------------------------------
exercise_8_considered = {
    "LLM01", "LLM02", "LLM03", "LLM04", "LLM05",
    "LLM06", "LLM07", "LLM08", "LLM09", "LLM10",
}


# ===========================================================================
# Scoring harness -- identical to starter.py.
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
    print("Chapter 1 Exercises -- Score Report (reference solution)")
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
