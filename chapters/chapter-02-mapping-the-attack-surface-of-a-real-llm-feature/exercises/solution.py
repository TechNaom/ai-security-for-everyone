"""
Chapter 2 Exercises: Mapping the Attack Surface of a Real LLM Feature
-- REFERENCE SOLUTION

See starter.py for the full scenario description (ReviewMate, a
fictional internal code-review assistant) and exercise instructions.
This file fills in every TODO with a correct reference answer and should
score a perfect total when run:

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
    "pr_description_text": (
        "A PR's title and description, written entirely by the PR's "
        "author (including external contributors), is concatenated with "
        "the system prompt into one context window with no structural "
        "separation."
    ),
    "ci_log_output": (
        "Raw CI log output, including console text printed by "
        "third-party dependencies' own install scripts during the build, "
        "is fed into ReviewMate's context on every review."
    ),
    "merge_tool_scope": (
        "merge_pr(pr_id) merges directly into the main branch if "
        "ReviewMate's own review passes, with no required second human "
        "approval before the merge executes."
    ),
    "system_prompt_criteria": (
        "The system prompt states ReviewMate's exact auto-merge safety "
        "criteria in plain text, and the model can be induced to repeat "
        "them verbatim."
    ),
    "issue_tracker_access": (
        "read_linked_issue(issue_id) can read the full comment thread of "
        "any issue in the tracker, including issues marked "
        "security-sensitive, for any PR ReviewMate is asked to review."
    ),
}

# pr_description_text: untrusted author-controlled text sharing a context
#   window with instructions -> Prompt Injection.
# ci_log_output: text a third-party dependency's own script chose to
#   print, read into context the same way -> Prompt Injection (a second,
#   easy-to-miss channel -- this is Mistake 1 from the lesson, applied to
#   a different system).
# merge_tool_scope: a tool with more autonomy than the task needs (no
#   required second human approval before a real-world merge) -> Excessive
#   Agency.
# system_prompt_criteria: sensitive operational logic embedded in a
#   prompt the model can be induced to repeat -> System Prompt Leakage.
# issue_tracker_access: a tool that can return more data (including
#   security-sensitive issue threads) than a given review task needs ->
#   Sensitive Information Disclosure.
exercise_1_answers = {
    "pr_description_text": "LLM01",
    "ci_log_output": "LLM01",
    "merge_tool_scope": "LLM06",
    "system_prompt_criteria": "LLM07",
    "issue_tracker_access": "LLM02",
}

# ---------------------------------------------------------------------------
# Exercise 2
# ---------------------------------------------------------------------------
EXERCISE_2_INPUTS = [
    "ReviewMate's system prompt (written by the platform engineering team)",
    "A PR's title and description, written by the PR's author",
    "Console output printed by a third-party dependency's install script, captured in CI logs",
    "The internal repository name ReviewMate is reviewing, read from verified CI metadata",
]

# The system prompt and the verified repository name are operator/
# platform-controlled and cannot be shaped by an arbitrary external party
# -- trusted. A PR's description (any contributor, including external
# ones, can write it) and a dependency's own install-script console
# output (controlled by whoever published that dependency) can both be
# shaped by a party outside the org's control -- untrusted.
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
    "require_second_approval": "Require a human engineer's approval before merge_pr executes, in addition to ReviewMate's own review.",
    "faster_ci": "Reduce CI run time so PRs merge faster.",
    "restrict_to_low_risk_paths": "Only allow ReviewMate to auto-merge PRs that touch a pre-approved allowlist of low-risk file paths (docs, tests); anything else requires a human.",
    "nicer_comment_formatting": "Improve the visual formatting of ReviewMate's posted review comments.",
}

# Requiring a second human approval adds a human checkpoint (reduces
# excessive autonomy); restricting auto-merge to a low-risk path
# allowlist reduces excessive functionality/scope. Faster CI and nicer
# comment formatting are unrelated reliability/UX changes that don't
# touch the tool's functionality, permissions, or autonomy.
exercise_3_answers = {
    "require_second_approval": True,
    "faster_ci": False,
    "restrict_to_low_risk_paths": True,
    "nicer_comment_formatting": False,
}

# ---------------------------------------------------------------------------
# Exercise 4
# ---------------------------------------------------------------------------
exercise_4_reasoning = (
    "Likelihood is high because any contributor, including an external "
    "one with no special access, can write a PR description that reaches "
    "this asset with no review before ReviewMate reads it; impact is high "
    "because a successful injection here can drive the merge_pr tool to "
    "merge attacker-influenced code straight into the main branch."
)

# ---------------------------------------------------------------------------
# Exercise 5
# ---------------------------------------------------------------------------
exercise_5_category = "LLM05"
exercise_5_mitigation = (
    "Strip or neutralize auto-loading markdown constructs (images, "
    "embedded links) from ReviewMate's generated comments before "
    "posting, or post as plain text, exactly as you would treat any "
    "other untrusted string reaching a rendering boundary."
)

# ---------------------------------------------------------------------------
# Exercise 6
# ---------------------------------------------------------------------------
exercise_6_category = "LLM10"
exercise_6_mitigation = (
    "Add a per-PR and per-day cap on ReviewMate-triggered CI reruns, with "
    "an alert if a PR requests reruns far above the normal review "
    "pattern."
)

# ---------------------------------------------------------------------------
# Exercise 7
# ---------------------------------------------------------------------------
exercise_7_is_problem = True
exercise_7_fix = (
    "Move the auto-merge safety criteria out of the system prompt and "
    "enforce it in code that evaluates every PR regardless of what the "
    "model decides, so a leaked prompt no longer reveals an exploitable "
    "boundary an attacker can craft a PR to stay just under."
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
        "pr_description_text": "LLM01",
        "ci_log_output": "LLM01",
        "merge_tool_scope": "LLM06",
        "system_prompt_criteria": "LLM07",
        "issue_tracker_access": "LLM02",
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
        "require_second_approval": True,
        "faster_ci": False,
        "restrict_to_low_risk_paths": True,
        "nicer_comment_formatting": False,
    }
    correct = sum(1 for k, v in key.items() if exercise_3_answers.get(k) is v)
    return correct, len(key)


def score_exercise_4():
    text = exercise_4_reasoning.lower()
    likelihood_words = ["any contributor", "external", "no review", "easy", "public", "anyone", "unauthenticated", "low bar", "no special access", "every pr"]
    impact_words = ["merge", "main branch", "production", "damage", "consequence", "harm", "exposure", "code", "supply chain", "malicious"]
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
    print("Chapter 2 Exercises -- Score Report (reference solution)")
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
