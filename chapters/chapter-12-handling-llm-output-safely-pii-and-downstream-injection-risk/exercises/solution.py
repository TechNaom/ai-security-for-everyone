"""
Chapter 12 Exercises: Handling LLM Output Safely: PII and Downstream
Injection Risk -- Reference solution. See starter.py for the full
scenario and task text.
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

EXERCISE_1_EVENTS = {
    "case_summary_widget": "A case summary generated for one HR case manager is also shown, unredacted, in a company-wide 'open cases' dashboard widget visible to every manager.",
    "unrelated_session_bleed": "A generated response for Employee A's leave-balance question includes a fragment of Employee B's unrelated case detail from an earlier, different session.",
    "unasked_salary_detail": "Asked only to confirm an employee's employment start date, StaffAssist's reply also restates the employee's current salary band, unprompted.",
    "markdown_widget_script": "A generated case note containing a pasted email signature with an embedded script-like fragment is rendered unescaped in the dashboard's Markdown preview widget, executing the fragment.",
    "chained_triage_bot": "A generated case summary is fed directly, unlabeled, into a second triage model's instruction context, which then acts on an instruction-shaped fragment that survived from the first model's generation.",
    "auto_fetch_link": "StaffAssist generates a 'related case' link that the dashboard automatically fetches; the generated link points to an internal admin endpoint outside the case-management domain.",
}

exercise_1_answers = {
    "case_summary_widget": "pii_reproduction",
    "unrelated_session_bleed": "cross_request_leak",
    "unasked_salary_detail": "over_disclosure",
    "markdown_widget_script": "rendered_injection",
    "chained_triage_bot": "agent_to_agent_injection",
    "auto_fetch_link": "downstream_api_injection",
}

EMAIL_PATTERN = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
PHONE_PATTERN = r"\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b"
SSN_PATTERN = r"\b\d{3}-\d{2}-\d{4}\b"


def redact_pii(text):
    text = re.sub(EMAIL_PATTERN, "[REDACTED]", text)
    text = re.sub(SSN_PATTERN, "[REDACTED]", text)
    text = re.sub(PHONE_PATTERN, "[REDACTED]", text)
    return text


EXERCISE_3_STATEMENTS = {
    "stmt_a": "\"Our system prompt tells the model never to repeat sensitive details, so we don't need an output-side PII scanner.\"",
    "stmt_b": "\"We run a pattern-based PII scanner on every generated summary before it's returned, and we know it won't catch every free-text sensitive detail, so we also scope each summary field's visibility independently of the source ticket's own access controls.\"",
    "stmt_c": "\"Our dashboard renders generated replies as HTML with no escaping, but that's fine because the text comes from our own model, not directly from a user.\"",
    "stmt_d": "\"We apply context-aware output encoding at every render surface, regardless of whether the text originated from a human or from a model generation.\"",
}

exercise_3_answers = {
    "stmt_a": False,
    "stmt_b": True,
    "stmt_c": False,
    "stmt_d": True,
}

EXERCISE_4_OBSERVATIONS = {
    "salary_in_summary": "A generated case summary includes an employee's salary band, visible to HR staff with no need to know it for this case.",
    "unescaped_html_render": "A generated case note is rendered as raw HTML in the dashboard with no escaping applied.",
    "cross_case_bleed": "A generated response for one employee's case includes a fragment of a different employee's unrelated case detail.",
    "auto_fetched_bad_url": "A generated 'related case' link is auto-fetched by the frontend and points to an internal endpoint outside the intended domain.",
}

exercise_4_answers = {
    "salary_in_summary": "llm02",
    "unescaped_html_render": "llm10",
    "cross_case_bleed": "llm02",
    "auto_fetched_bad_url": "llm10",
}


def html_escape_output(text):
    text = text.replace("&", "&amp;")
    text = text.replace("<", "&lt;")
    text = text.replace(">", "&gt;")
    text = text.replace('"', "&quot;")
    text = text.replace("'", "&#x27;")
    return text


ALLOWED_DOMAINS = ["cases.thornbury-hr.example", "cases-eu.thornbury-hr.example"]


def is_allowed_case_link(url):
    if not isinstance(url, str) or not url.startswith("https://"):
        return False
    rest = url[len("https://"):]
    host = rest.split("/", 1)[0]
    return host in ALLOWED_DOMAINS


EXERCISE_7_DEFENSES = {
    "defense_a": "\"We rely on the model's system prompt instructing it not to generate URLs outside our domain -- no server-side allow-list check.\"",
    "defense_b": "\"Every generated 'related case' URL is checked against an explicit allow-list of known-safe domains before the frontend auto-fetches it.\"",
    "defense_c": "\"Our PII scanner only checks the first 100 characters of each generated summary for speed, and we treat a clean scan as proof the summary is fully PII-free.\"",
    "defense_d": "\"Our PII scanner runs on the full generated text, and we pair it with artifact-level visibility scoping so an undetected leak still has a smaller blast radius.\"",
}

exercise_7_answers = {
    "defense_a": True,
    "defense_b": False,
    "defense_c": True,
    "defense_d": False,
}

exercise_8_reasoning = (
    "A system-prompt instruction is a preference the model usually follows, "
    "not an enforced structural boundary, and Priya's summary in the lesson's "
    "own hook leaked a sensitive detail through completely faithful, "
    "non-adversarial, helpful generation -- no instruction-breaking involved "
    "at all -- which a prompt-level rule alone can never reliably prevent."
)


# ===========================================================================
# Scoring harness
# ===========================================================================

def score_exercise_1():
    key = exercise_1_answers
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
