"""
Chapter 12 Exercises: Handling LLM Output Safely: PII and Downstream
Injection Risk

Scenario for these exercises (deliberately different from the lesson's
Fenwick Customer Experience / TicketSense example): Thornbury HR Cloud, a
fictional HR-software vendor.

    Thornbury HR Cloud runs StaffAssist, an internal LLM tool that helps
    HR staff draft case summaries for employee inquiries and suggested
    responses that get rendered in a web-based case dashboard. A newly
    formed output-safety review is auditing StaffAssist against this
    chapter's six failure shapes (three PII, three injection) and
    building the real output-side controls to close what it finds.

Fill in every TODO below, then run this file:

    python3 starter.py

to see your score. Compare against solution.py for reference answers.
"""

import re

FAILURE_SHAPES = {
    "pii_reproduction": "Faithful reproduction of sensitive context into a wider-audience artifact",
    "cross_request_leak": "Cross-request context/training-adjacent leakage",
    "over_disclosure": "Over-disclosure through unprompted helpfulness",
    "rendered_injection": "Rendered-output injection (stored-XSS shape)",
    "agent_to_agent_injection": "Agent-to-agent injection",
    "downstream_api_injection": "Downstream-API injection (SSRF/command-construction shape)",
}

OWASP_2026_CATEGORIES = {
    "llm02": "LLM02:2026 Sensitive Information Disclosure",
    "llm10": "LLM10:2026 Improper Output Handling",
}

# ---------------------------------------------------------------------------
# Exercise 1 -- Classify six StaffAssist events into the correct failure
# shape. Use the short keys from FAILURE_SHAPES.
# ---------------------------------------------------------------------------
EXERCISE_1_EVENTS = {
    "case_summary_widget": "A case summary generated for one HR case manager is also shown, unredacted, in a company-wide 'open cases' dashboard widget visible to every manager.",
    "unrelated_session_bleed": "A generated response for Employee A's leave-balance question includes a fragment of Employee B's unrelated case detail from an earlier, different session.",
    "unasked_salary_detail": "Asked only to confirm an employee's employment start date, StaffAssist's reply also restates the employee's current salary band, unprompted.",
    "markdown_widget_script": "A generated case note containing a pasted email signature with an embedded script-like fragment is rendered unescaped in the dashboard's Markdown preview widget, executing the fragment.",
    "chained_triage_bot": "A generated case summary is fed directly, unlabeled, into a second triage model's instruction context, which then acts on an instruction-shaped fragment that survived from the first model's generation.",
    "auto_fetch_link": "StaffAssist generates a 'related case' link that the dashboard automatically fetches; the generated link points to an internal admin endpoint outside the case-management domain.",
}

# TODO 1: fill in the FAILURE_SHAPES key each event is MOST associated with.
exercise_1_answers = {
    "case_summary_widget": "",  # TODO
    "unrelated_session_bleed": "",  # TODO
    "unasked_salary_detail": "",  # TODO
    "markdown_widget_script": "",  # TODO
    "chained_triage_bot": "",  # TODO
    "auto_fetch_link": "",  # TODO
}

# ---------------------------------------------------------------------------
# Exercise 2 (production-gear: implement a real PII redactor) -- StaffAssist
# needs an output-side scanner that redacts emails, phone numbers, and
# SSN-shaped identifiers from generated text before it's returned, replacing
# each match with "[REDACTED]".
# ---------------------------------------------------------------------------
EMAIL_PATTERN = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
PHONE_PATTERN = r"\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b"
SSN_PATTERN = r"\b\d{3}-\d{2}-\d{4}\b"


def redact_pii(text):
    """
    TODO: return a copy of `text` with every email, phone number, and
    SSN-shaped substring (using EMAIL_PATTERN, PHONE_PATTERN, SSN_PATTERN)
    replaced with the literal string "[REDACTED]". Use re.sub for each
    pattern. Non-matching text must be left untouched.
    """
    return text  # TODO


# ---------------------------------------------------------------------------
# Exercise 3 -- For each statement, decide whether it's a real, honest
# output-handling claim (True) or an overclaim/gap (False).
# ---------------------------------------------------------------------------
EXERCISE_3_STATEMENTS = {
    "stmt_a": "\"Our system prompt tells the model never to repeat sensitive details, so we don't need an output-side PII scanner.\"",
    "stmt_b": "\"We run a pattern-based PII scanner on every generated summary before it's returned, and we know it won't catch every free-text sensitive detail, so we also scope each summary field's visibility independently of the source ticket's own access controls.\"",
    "stmt_c": "\"Our dashboard renders generated replies as HTML with no escaping, but that's fine because the text comes from our own model, not directly from a user.\"",
    "stmt_d": "\"We apply context-aware output encoding at every render surface, regardless of whether the text originated from a human or from a model generation.\"",
}

# TODO 3: fill in True (honest/sound) or False (overclaim/gap) for each statement.
exercise_3_answers = {
    "stmt_a": None,  # TODO
    "stmt_b": None,  # TODO
    "stmt_c": None,  # TODO
    "stmt_d": None,  # TODO
}

# ---------------------------------------------------------------------------
# Exercise 4 (production-gear: map observation to OWASP 2026 category) -- For
# each StaffAssist observation, name the single best-fit category using
# OWASP_2026_CATEGORIES keys ("llm02" or "llm10").
# ---------------------------------------------------------------------------
EXERCISE_4_OBSERVATIONS = {
    "salary_in_summary": "A generated case summary includes an employee's salary band, visible to HR staff with no need to know it for this case.",
    "unescaped_html_render": "A generated case note is rendered as raw HTML in the dashboard with no escaping applied.",
    "cross_case_bleed": "A generated response for one employee's case includes a fragment of a different employee's unrelated case detail.",
    "auto_fetched_bad_url": "A generated 'related case' link is auto-fetched by the frontend and points to an internal endpoint outside the intended domain.",
}

# TODO 4: fill in the OWASP_2026_CATEGORIES key that's the best fit for each observation.
exercise_4_answers = {
    "salary_in_summary": "",  # TODO
    "unescaped_html_render": "",  # TODO
    "cross_case_bleed": "",  # TODO
    "auto_fetched_bad_url": "",  # TODO
}

# ---------------------------------------------------------------------------
# Exercise 5 (production-gear: implement context-aware HTML output encoding)
# -- StaffAssist's dashboard needs to render generated text safely.
# ---------------------------------------------------------------------------
def html_escape_output(text):
    """
    TODO: return `text` with the five standard HTML special characters
    escaped: & -> &amp;  < -> &lt;  > -> &gt;  " -> &quot;  ' -> &#x27;
    IMPORTANT: escape '&' FIRST, before the others, or you will
    double-escape the entities you just inserted.
    """
    return text  # TODO


# ---------------------------------------------------------------------------
# Exercise 6 (production-gear: implement an allow-list URL validator) --
# StaffAssist's frontend auto-fetches a generated "related case" link. It
# must only ever fetch an https URL whose host is exactly one of
# ALLOWED_DOMAINS (no subdomain tricks, no http).
# ---------------------------------------------------------------------------
ALLOWED_DOMAINS = ["cases.thornbury-hr.example", "cases-eu.thornbury-hr.example"]


def is_allowed_case_link(url):
    """
    TODO: return True only if `url` starts with "https://" AND the host
    portion immediately following "https://" (up to the next "/", if any)
    is EXACTLY one of ALLOWED_DOMAINS. Return False for http://, any other
    scheme, any host not exactly in ALLOWED_DOMAINS (including a
    look-alike subdomain like "cases.thornbury-hr.example.evil.com" or
    "evil.cases.thornbury-hr.example"), and any malformed input.
    """
    return False  # TODO


# ---------------------------------------------------------------------------
# Exercise 7 (production-gear: critique flawed vs. sound defense excerpts)
# -- For each excerpt, decide whether it describes a real, flawed
# output-handling defense (True) or a sound one (False).
# ---------------------------------------------------------------------------
EXERCISE_7_DEFENSES = {
    "defense_a": "\"We rely on the model's system prompt instructing it not to generate URLs outside our domain -- no server-side allow-list check.\"",
    "defense_b": "\"Every generated 'related case' URL is checked against an explicit allow-list of known-safe domains before the frontend auto-fetches it.\"",
    "defense_c": "\"Our PII scanner only checks the first 100 characters of each generated summary for speed, and we treat a clean scan as proof the summary is fully PII-free.\"",
    "defense_d": "\"Our PII scanner runs on the full generated text, and we pair it with artifact-level visibility scoping so an undetected leak still has a smaller blast radius.\"",
}

# TODO 7: fill in True (flawed) or False (sound) for each defense description.
exercise_7_answers = {
    "defense_a": None,  # TODO
    "defense_b": None,  # TODO
    "defense_c": None,  # TODO
    "defense_d": None,  # TODO
}

# ---------------------------------------------------------------------------
# Exercise 8 (production-gear: written reasoning) -- Write a one-sentence
# justification for why a system-prompt instruction like "never generate
# sensitive data" is not, on its own, a sufficient output-handling defense.
# Must reference BOTH the idea that a prompt-level instruction is not a
# structural/enforced boundary AND a specific example of a failure that
# happens even without any adversarial intent (e.g., Priya's case or
# over-disclosure), to pass the substance check.
# ---------------------------------------------------------------------------
exercise_8_reasoning = ""  # TODO: write your one-sentence justification here


# ===========================================================================
# Scoring harness -- do not need to edit anything below this line.
# ===========================================================================

def score_exercise_1():
    key = {
        "case_summary_widget": "pii_reproduction",
        "unrelated_session_bleed": "cross_request_leak",
        "unasked_salary_detail": "over_disclosure",
        "markdown_widget_script": "rendered_injection",
        "chained_triage_bot": "agent_to_agent_injection",
        "auto_fetch_link": "downstream_api_injection",
    }
    correct = sum(1 for k, v in key.items() if exercise_1_answers.get(k) == v)
    return correct, len(key)


def score_exercise_2():
    checks = [
        redact_pii("Contact me at jane.doe@example.com for details.") ==
        "Contact me at [REDACTED] for details.",
        redact_pii("Call 555-123-4567 tomorrow.") == "Call [REDACTED] tomorrow.",
        redact_pii("SSN on file: 123-45-6789.") == "SSN on file: [REDACTED].",
        redact_pii("No sensitive data here.") == "No sensitive data here.",
    ]
    return sum(1 for c in checks if c), len(checks)


def score_exercise_3():
    key = {"stmt_a": False, "stmt_b": True, "stmt_c": False, "stmt_d": True}
    correct = sum(1 for k, v in key.items() if exercise_3_answers.get(k) is v)
    return correct, len(key)


def score_exercise_4():
    key = {
        "salary_in_summary": "llm02",
        "unescaped_html_render": "llm10",
        "cross_case_bleed": "llm02",
        "auto_fetched_bad_url": "llm10",
    }
    correct = sum(1 for k, v in key.items() if exercise_4_answers.get(k) == v)
    return correct, len(key)


def score_exercise_5():
    checks = [
        html_escape_output("<script>") == "&lt;script&gt;",
        html_escape_output("Tom & Jerry") == "Tom &amp; Jerry",
        html_escape_output('He said "hi"') == "He said &quot;hi&quot;",
        html_escape_output("it's fine") == "it&#x27;s fine",
    ]
    return sum(1 for c in checks if c), len(checks)


def score_exercise_6():
    checks = [
        is_allowed_case_link("https://cases.thornbury-hr.example/c/123") is True,
        is_allowed_case_link("https://cases-eu.thornbury-hr.example/c/9") is True,
        is_allowed_case_link("http://cases.thornbury-hr.example/c/123") is False,
        is_allowed_case_link("https://cases.thornbury-hr.example.evil.com/c/1") is False,
        is_allowed_case_link("https://evil.cases.thornbury-hr.example/c/1") is False,
        is_allowed_case_link("not-a-url") is False,
    ]
    return sum(1 for c in checks if c), len(checks)


def score_exercise_7():
    key = {"defense_a": True, "defense_b": False, "defense_c": True, "defense_d": False}
    correct = sum(1 for k, v in key.items() if exercise_7_answers.get(k) is v)
    return correct, len(key)


def score_exercise_8():
    text = exercise_8_reasoning.lower()
    structural_words = ["structural", "enforce", "boundary", "not a guarantee", "instruction", "prompt-level", "brittle"]
    example_words = ["priya", "over-disclosure", "helpful", "no adversar", "accurate", "faithful"]
    has_structural = any(w in text for w in structural_words)
    has_example = any(w in text for w in example_words)
    correct = int(has_structural) + int(has_example)
    return correct, 2


def main():
    exercises = [
        ("Exercise 1 -- classify events by failure shape", score_exercise_1),
        ("Exercise 2 -- implement redact_pii()", score_exercise_2),
        ("Exercise 3 -- honest claim vs. overclaim/gap", score_exercise_3),
        ("Exercise 4 -- map observation to OWASP 2026 category", score_exercise_4),
        ("Exercise 5 -- implement html_escape_output()", score_exercise_5),
        ("Exercise 6 -- implement is_allowed_case_link()", score_exercise_6),
        ("Exercise 7 -- critique defense excerpts", score_exercise_7),
        ("Exercise 8 -- written reasoning", score_exercise_8),
    ]

    total_correct = 0
    total_possible = 0
    print("Chapter 12 Exercises -- Score Report")
    print("=" * 60)
    for label, fn in exercises:
        correct, possible = fn()
        total_correct += correct
        total_possible += possible
        print(f"{label}: {correct}/{possible}")
    print("=" * 60)
    print(f"TOTAL: {total_correct}/{total_possible}")
    if total_possible and total_correct == total_possible:
        print("Perfect score -- every event, function, and mapping correct.")
    else:
        print("Keep going -- fill in the remaining TODOs and re-run this file.")


if __name__ == "__main__":
    main()
