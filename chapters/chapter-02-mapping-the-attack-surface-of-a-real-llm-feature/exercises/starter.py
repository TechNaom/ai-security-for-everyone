"""
Chapter 2 Exercises: Mapping the Attack Surface of a Real LLM Feature

Scenario for these exercises (deliberately different from the lesson's
Waypoint trip-planning assistant): ReviewMate, a fictional internal
engineering code-review assistant.

    ReviewMate reads open pull requests in an internal monorepo and can
    post review comments automatically. It has four tools:

      - read_pr_diff(pr_id)        -- reads the PR's diff, title, and
                                       description, all written by the
                                       PR's author (an engineer at the
                                       company OR an external open-source
                                       contributor, depending on the repo)
      - read_linked_issue(issue_id) -- reads an issue's description and
                                       comment thread from the issue
                                       tracker (anyone with tracker access
                                       can file or comment on an issue)
      - get_ci_logs(run_id)         -- reads the raw CI log output for a
                                       build, which includes console
                                       output printed by third-party
                                       dependencies' install/build scripts
      - post_comment(pr_id, text)   -- posts a comment on the PR, rendered
                                       as markdown in the PR UI (markdown
                                       images and links render/auto-load
                                       without a click)
      - merge_pr(pr_id)             -- merges the PR into the main branch
                                       if ReviewMate's review passes; no
                                       required second human approval

    Every PR diff, issue thread, and CI log ReviewMate reads is
    concatenated with its system prompt into one context window before
    each model call. The system prompt states the exact criteria
    ReviewMate uses to decide whether a PR is "safe to auto-merge."

Fill in every TODO below, then run this file:

    python3 starter.py

to see your score. Compare against solution.py for reference answers.
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
# Exercise 1 -- Map five ReviewMate attack-surface descriptions to the
# single OWASP category that best explains each one. Use the category IDs
# above (e.g. "LLM01").
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

# TODO 1: fill in the OWASP category ID (e.g. "LLM01") that best explains
# each asset above.
exercise_1_answers = {
    "pr_description_text": "",       # TODO
    "ci_log_output": "",             # TODO
    "merge_tool_scope": "",          # TODO
    "system_prompt_criteria": "",    # TODO
    "issue_tracker_access": "",      # TODO
}

# ---------------------------------------------------------------------------
# Exercise 2 -- Trust classification. For each context-window input below,
# classify it as "trusted" (operator-authored, safe to treat as
# instructions) or "untrusted" (attacker-influenceable, must be treated as
# data only).
# ---------------------------------------------------------------------------
EXERCISE_2_INPUTS = [
    "ReviewMate's system prompt (written by the platform engineering team)",
    "A PR's title and description, written by the PR's author",
    "Console output printed by a third-party dependency's install script, captured in CI logs",
    "The internal repository name ReviewMate is reviewing, read from verified CI metadata",
]

# TODO 2: fill in "trusted" or "untrusted" for each index above, in order.
exercise_2_answers = [
    "",  # TODO -- system prompt
    "",  # TODO -- PR title/description
    "",  # TODO -- dependency install-script console output
    "",  # TODO -- verified repository name
]

# ---------------------------------------------------------------------------
# Exercise 3 (production-gear: access/permissions) -- Given four candidate
# fixes for the merge_pr tool, mark which ones actually reduce Excessive
# Agency risk (True) versus which ones don't address it (False).
# ---------------------------------------------------------------------------
EXERCISE_3_FIXES = {
    "require_second_approval": "Require a human engineer's approval before merge_pr executes, in addition to ReviewMate's own review.",
    "faster_ci": "Reduce CI run time so PRs merge faster.",
    "restrict_to_low_risk_paths": "Only allow ReviewMate to auto-merge PRs that touch a pre-approved allowlist of low-risk file paths (docs, tests); anything else requires a human.",
    "nicer_comment_formatting": "Improve the visual formatting of ReviewMate's posted review comments.",
}

# TODO 3: fill in True/False for each fix above -- does it reduce Excessive
# Agency risk?
exercise_3_answers = {
    "require_second_approval": None,       # TODO
    "faster_ci": None,                     # TODO
    "restrict_to_low_risk_paths": None,    # TODO
    "nicer_comment_formatting": None,      # TODO
}

# ---------------------------------------------------------------------------
# Exercise 4 (production-gear: risk evaluation) -- Write a one-sentence
# likelihood/impact justification (not just "high" or "low") for the
# pr_description_text asset from Exercise 1. It must mention BOTH how
# easily an attacker can reach this asset (likelihood) AND what happens if
# they do (impact) to pass the keyword check in score_exercise_4().
# ---------------------------------------------------------------------------
exercise_4_reasoning = ""  # TODO: write your one-sentence justification here

# ---------------------------------------------------------------------------
# Exercise 5 (production-gear: operations/output handling) -- ReviewMate's
# posted comments render as markdown, and markdown images/links render or
# auto-load without a click. Name the OWASP category this maps to, and
# name ONE concrete mitigation.
# ---------------------------------------------------------------------------
exercise_5_category = ""     # TODO: e.g. "LLM05"
exercise_5_mitigation = ""   # TODO: one concrete sentence

# ---------------------------------------------------------------------------
# Exercise 6 (production-gear: cost/operations) -- ReviewMate can be asked,
# via a PR comment or description, to re-request CI runs with no per-PR or
# per-day cap, and each CI run costs real compute minutes. Name the OWASP
# category this maps to, and name ONE concrete mitigation.
# ---------------------------------------------------------------------------
exercise_6_category = ""     # TODO: e.g. "LLM10"
exercise_6_mitigation = ""   # TODO: one concrete sentence

# ---------------------------------------------------------------------------
# Exercise 7 (production-gear: compliance) -- Decide whether the
# system-prompt auto-merge criteria described in the scenario is a real
# compliance problem, and if so, name the fix that moves it out of the
# model's "trust me to follow this" layer.
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
    print("Chapter 2 Exercises -- Score Report")
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
