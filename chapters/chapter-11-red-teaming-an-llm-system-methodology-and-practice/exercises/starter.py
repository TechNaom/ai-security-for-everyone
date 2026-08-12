"""
Chapter 11 Exercises: Red-Teaming an LLM System: Methodology and Practice

Scenario for these exercises (deliberately different from the lesson's
Alderglen Financial / Ledger Copilot example): Corvette Bay Utilities, a
fictional regional electric utility.

    Corvette Bay Utilities runs Outage Assistant, an internal LLM tool
    that helps call-center staff answer customer outage questions. It
    retrieves from an internal outage-procedures wiki and can call a
    tool, check_meter_diagnostic(meter_id), that queries a partner
    smart-meter vendor's diagnostic API. A newly formed internal red
    team is running its first structured engagement against Outage
    Assistant, using this chapter's five-phase methodology.

Fill in every TODO below, then run this file:

    python3 starter.py

to see your score. Compare against solution.py for reference answers.
"""

PHASES = {
    "scoping": "Phase 1 -- Scoping and rules of engagement",
    "test_design": "Phase 2 -- Threat-model-driven test-case design",
    "execution": "Phase 3 -- Systematic execution and documentation",
    "classification": "Phase 4 -- Severity and impact classification",
    "reporting": "Phase 5 -- Writing the findings report",
}

OWASP_CATEGORIES = {
    "llm01": "LLM01 Prompt Injection",
    "llm02": "LLM02 Sensitive Information Disclosure",
    "llm06": "LLM06 Excessive Agency",
    "llm07": "LLM07 System Prompt Leakage",
    "llm08": "LLM08 Vector and Embedding Weaknesses",
}

# ---------------------------------------------------------------------------
# Exercise 1 -- Classify six process failures/events into the correct phase.
# Use the short keys from PHASES.
# ---------------------------------------------------------------------------
EXERCISE_1_EVENTS = {
    "no_scope_doc": "The red team starts probing Outage Assistant's tool calls with no written agreement on what's in or out of scope.",
    "ad_hoc_testing": "The tester tries whatever attacks come to mind rather than working through the OWASP Top 10 against Outage Assistant's actual retrieval and tool-call surfaces.",
    "notes_written_after": "The tester waits until the end of the two-day engagement to write down what payloads were used and what responses were observed.",
    "no_severity_scale": "Four confirmed findings get listed with no likelihood/impact rating, just prose descriptions.",
    "unusable_writeup": "The final document is a chat-thread-style narrative with no reproduction steps a second person could follow.",
    "rules_of_engagement_signed": "Before testing begins, engineering and the red team agree in writing on in-scope components, authorized techniques, and an escalation contact.",
}

# TODO 1: fill in the phase key (e.g. "scoping") each event is MOST associated with.
exercise_1_answers = {
    "no_scope_doc": "",  # TODO
    "ad_hoc_testing": "",  # TODO
    "notes_written_after": "",  # TODO
    "no_severity_scale": "",  # TODO
    "unusable_writeup": "",  # TODO
    "rules_of_engagement_signed": "",  # TODO
}

# ---------------------------------------------------------------------------
# Exercise 2 (production-gear: compute a real severity score) -- Corvette
# Bay's red team scores each finding on two 1-4 axes (likelihood, impact),
# then combines them with:
#
#   combined = likelihood * impact   (max 16)
#   rating = "Critical" if combined >= 12
#            "High"     if combined >= 8
#            "Medium"   if combined >= 4
#            "Low"      otherwise
#
# Finding: a planted wiki chunk causes Outage Assistant to leak a customer's
# full address to any caller. likelihood = 3 (moderate: requires editing a
# wiki page, but wiki-edit access is broadly held), impact = 4 (severe: PII
# exposure to any caller for any customer).
# ---------------------------------------------------------------------------
LIKELIHOOD = 3
IMPACT = 4


def compute_severity_rating():
    # TODO: implement the formula above and return the string rating
    # ("Critical", "High", "Medium", or "Low").
    return ""


# ---------------------------------------------------------------------------
# Exercise 3 -- For each statement, decide whether it's a real, honest
# red-team-process claim (True) or an overclaim/process gap (False).
# ---------------------------------------------------------------------------
EXERCISE_3_STATEMENTS = {
    "stmt_a": "\"We tested three things in two days because that's what came to mind -- our coverage is comprehensive.\"",
    "stmt_b": "\"We worked through all ten OWASP categories against Outage Assistant's actual architecture, and only three categories had a plausible attack surface worth testing -- our report states which seven we deliberately excluded and why.\"",
    "stmt_c": "\"Our findings were written up two days after testing from memory, so the reproduction steps are our best recollection.\"",
    "stmt_d": "\"We recorded exact payloads, exact outputs, and timestamps at the moment of each test, so every finding in our report is independently reproducible.\"",
}

# TODO 3: fill in True (honest/sound) or False (overclaim/process gap) for each statement.
exercise_3_answers = {
    "stmt_a": None,  # TODO
    "stmt_b": None,  # TODO
    "stmt_c": None,  # TODO
    "stmt_d": None,  # TODO
}

# ---------------------------------------------------------------------------
# Exercise 4 (production-gear: map system feature to OWASP category) -- For
# each Outage Assistant feature/observation, name the single best-fit OWASP
# category using OWASP_CATEGORIES keys.
# ---------------------------------------------------------------------------
EXERCISE_4_FEATURES = {
    "wiki_retrieval_editable": "Outage Assistant retrieves from an internal wiki that any employee can edit, with no trust tagging on retrieved chunks.",
    "meter_tool_raw_concat": "check_meter_diagnostic's returned diagnostic_note free-text field is concatenated raw into context with no structural separation.",
    "system_prompt_extractable": "A direct, cleverly-worded user message causes Outage Assistant to repeat its full system prompt verbatim, including an internal escalation-authority flag.",
    "account_pii_in_tool_result": "check_meter_diagnostic's response includes the customer's full billing address, which then appears unfiltered in Outage Assistant's reply to the call-center agent.",
}

# TODO 4: fill in the OWASP_CATEGORIES key that's the best fit for each feature.
exercise_4_answers = {
    "wiki_retrieval_editable": "",  # TODO
    "meter_tool_raw_concat": "",  # TODO
    "system_prompt_extractable": "",  # TODO
    "account_pii_in_tool_result": "",  # TODO
}

# ---------------------------------------------------------------------------
# Exercise 5 -- Order four findings from HIGHEST to LOWEST severity, using
# their given (likelihood, impact) pairs and the Exercise 2 formula.
# ---------------------------------------------------------------------------
EXERCISE_5_FINDINGS = {
    "finding_w": (4, 4),   # likelihood, impact
    "finding_x": (1, 2),
    "finding_y": (2, 4),
    "finding_z": (3, 3),
}

# TODO 5: fill in a list of the four finding keys, ordered highest severity
# (by combined score) first, lowest last. Break ties by combined score only.
exercise_5_order = []  # TODO: e.g. ["finding_w", "finding_z", ...]

# ---------------------------------------------------------------------------
# Exercise 6 (production-gear: critique flawed report excerpts) -- For each
# excerpt, decide whether it contains a real, flawed reasoning gap (True) or
# is sound (False).
# ---------------------------------------------------------------------------
EXERCISE_6_REPORTS = {
    "report_a": "\"This prompt-injection finding is Critical because it could theoretically leak any data in the system,\" with no test case demonstrating exposure beyond a single, narrowly-scoped record.",
    "report_b": "\"This prompt-injection finding is rated High based on demonstrated exposure of a single customer's address in our test case; we recommend a follow-up test to determine whether broader exposure is possible before re-rating.\"",
    "report_c": "\"Our report covers the wiki-retrieval and tool-call surfaces we tested; we did not test the underlying account-management system, which was out of scope per our rules of engagement.\"",
    "report_d": "\"Our four findings are listed in the order we happened to test them, with no severity rating, so engineering can pick whichever they want to fix first.\"",
}

# TODO 6: fill in True (flawed reasoning/gap) or False (sound) for each report.
exercise_6_answers = {
    "report_a": None,  # TODO
    "report_b": None,  # TODO
    "report_c": None,  # TODO
    "report_d": None,  # TODO
}

# ---------------------------------------------------------------------------
# Exercise 7 (production-gear: research source matching) -- Match each
# finding to its real, cited source.
# ---------------------------------------------------------------------------
RESEARCH_SOURCES = {
    "owasp_red_team_guide": "OWASP GenAI Security Project, GenAI Red Teaming Guide (announced January 22, 2025)",
    "nist_gai_profile": "NIST Generative Artificial Intelligence Profile (NIST-AI-600-1, July 26, 2024)",
    "microsoft_100_products": "Microsoft AI Red Team, 'Lessons from Red Teaming 100 Generative AI Products' (arXiv:2501.07238)",
    "openai_external_red_team": "OpenAI, 'OpenAI's Approach to External Red Teaming for AI Models and Systems' (arXiv:2503.16431)",
}

EXERCISE_7_FINDINGS = {
    "four_area_guide": "Organizes red-teaming into model evaluation, implementation testing, infrastructure assessment, and runtime behavior analysis.",
    "measure_function": "Names red-teaming as an expected control under the Measure function of a broader AI risk-management framework.",
    "hundred_products_lessons": "Documents lessons from red-teaming over 100 real generative-AI products, concluding human judgment on severity and reporting remains essential even as tooling scales test execution.",
    "scope_first_process": "Describes a structured process built around defining testing scope and team composition before testing, and synthesizing findings into actionable outputs afterward.",
}

# TODO 7: fill in the correct RESEARCH_SOURCES key for each finding.
exercise_7_answers = {
    "four_area_guide": "",  # TODO
    "measure_function": "",  # TODO
    "hundred_products_lessons": "",  # TODO
    "scope_first_process": "",  # TODO
}

# ---------------------------------------------------------------------------
# Exercise 8 (production-gear: written reasoning) -- Write a one-sentence
# justification for why Phase 5 (the findings report) can only be as good as
# Phases 1-4 that precede it. Must reference BOTH the idea that Phase 5
# depends on earlier phases' inputs AND a specific example of an earlier-
# phase gap that reformatting the report alone can't fix, to pass the
# substance check.
# ---------------------------------------------------------------------------
exercise_8_reasoning = ""  # TODO: write your one-sentence justification here


# ===========================================================================
# Scoring harness -- do not need to edit anything below this line.
# ===========================================================================

def score_exercise_1():
    key = {
        "no_scope_doc": "scoping",
        "ad_hoc_testing": "test_design",
        "notes_written_after": "execution",
        "no_severity_scale": "classification",
        "unusable_writeup": "reporting",
        "rules_of_engagement_signed": "scoping",
    }
    correct = sum(1 for k, v in key.items() if exercise_1_answers.get(k) == v)
    return correct, len(key)


def score_exercise_2():
    return (1 if compute_severity_rating() == "Critical" else 0), 1


def score_exercise_3():
    key = {"stmt_a": False, "stmt_b": True, "stmt_c": False, "stmt_d": True}
    correct = sum(1 for k, v in key.items() if exercise_3_answers.get(k) is v)
    return correct, len(key)


def score_exercise_4():
    key = {
        "wiki_retrieval_editable": "llm01",
        "meter_tool_raw_concat": "llm06",
        "system_prompt_extractable": "llm07",
        "account_pii_in_tool_result": "llm02",
    }
    correct = sum(1 for k, v in key.items() if exercise_4_answers.get(k) == v)
    return correct, len(key)


def score_exercise_5():
    key = ["finding_w", "finding_z", "finding_y", "finding_x"]
    correct = 1 if exercise_5_order == key else 0
    return correct, 1


def score_exercise_6():
    key = {"report_a": True, "report_b": False, "report_c": False, "report_d": True}
    correct = sum(1 for k, v in key.items() if exercise_6_answers.get(k) is v)
    return correct, len(key)


def score_exercise_7():
    key = {
        "four_area_guide": "owasp_red_team_guide",
        "measure_function": "nist_gai_profile",
        "hundred_products_lessons": "microsoft_100_products",
        "scope_first_process": "openai_external_red_team",
    }
    correct = sum(1 for k, v in key.items() if exercise_7_answers.get(k) == v)
    return correct, len(key)


def score_exercise_8():
    text = exercise_8_reasoning.lower()
    dependency_words = ["depend", "input", "built from", "only as good", "precede", "prior phase"]
    example_words = ["memory", "documentation", "scope", "severity", "rubric", "reproduc"]
    has_dep = any(w in text for w in dependency_words)
    has_ex = any(w in text for w in example_words)
    correct = int(has_dep) + int(has_ex)
    return correct, 2


def main():
    exercises = [
        ("Exercise 1 -- classify events by phase", score_exercise_1),
        ("Exercise 2 -- compute a real severity rating", score_exercise_2),
        ("Exercise 3 -- honest claim vs. overclaim/gap", score_exercise_3),
        ("Exercise 4 -- map feature to OWASP category", score_exercise_4),
        ("Exercise 5 -- order findings by severity", score_exercise_5),
        ("Exercise 6 -- critique report excerpts", score_exercise_6),
        ("Exercise 7 -- research source matching", score_exercise_7),
        ("Exercise 8 -- written reasoning", score_exercise_8),
    ]

    total_correct = 0
    total_possible = 0
    print("Chapter 11 Exercises -- Score Report")
    print("=" * 60)
    for label, fn in exercises:
        correct, possible = fn()
        total_correct += correct
        total_possible += possible
        print(f"{label}: {correct}/{possible}")
    print("=" * 60)
    print(f"TOTAL: {total_correct}/{total_possible}")
    if total_possible and total_correct == total_possible:
        print("Perfect score -- every event, rating, and mapping correct.")
    else:
        print("Keep going -- fill in the remaining TODOs and re-run this file.")


if __name__ == "__main__":
    main()
