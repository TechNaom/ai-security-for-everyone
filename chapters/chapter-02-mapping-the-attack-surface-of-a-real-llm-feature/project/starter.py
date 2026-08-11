"""
Chapter 2 Project (Level 1, Guided): Threat-Model a Real LLM Feature
End to End

Per docs/curriculum/CURRICULUM_MAP.md, this is Module 1's Level 1
project: "Threat-model a real, given LLM feature end to end." You are
handed a fourth scenario, genuinely different from GreenCart (Chapter 1),
Waypoint (this chapter's lesson), and ReviewMate (this chapter's
exercises) -- no worked answer to check against as you go. Use the
seven-step systematic method from the lesson, in order.

-----------------------------------------------------------------------
THE SCENARIO: AskHR
-----------------------------------------------------------------------
AskHR is a fictional internal HR chatbot, deployed inside a company-wide
Slack workspace. Employees message it -- one-on-one, or in small
HR-support group channels that sometimes include more than one employee
at a time (e.g. a manager and a direct report working through a leave
request together) -- to ask policy questions, look up their own HR
information, and request routine actions. It has four tools:

    search_hr_policies(query)
        -> semantic search over a vector store indexed from (a) the
           company's own internal HR policy documents and (b) a
           licensed third-party compliance-content feed (labor-law
           summaries, updated automatically on a schedule), mixed
           together with no per-source tag carried through to query
           time.

    get_employee_record(employee_id)
        -> returns an employee's full HR record: role, manager, PTO
           balance, salary band, and any leave-related notes on file
           (which can include sensitive medical/caregiving context).
           Callable with ANY employee_id, not scoped to "yourself or
           your direct reports" -- any authenticated employee's Slack
           account can trigger a lookup on any other employee.

    initiate_leave_request(employee_id, leave_type, start_date, end_date)
        -> creates a leave request and auto-approves it immediately if
           the requested duration is under a threshold AskHR's system
           prompt states in plain text. No identity re-verification step
           and no per-request cap tied to the employee's actual PTO
           balance.

    escalate_to_hr_specialist(employee_id, note, priority)
        -> opens a ticket in the HR ticketing system, addressed to a
           human HR specialist. The ticket body is built by inserting
           AskHR's generated note directly into the ticketing system's
           HTML ticket template, unescaped.

Every Slack message in a thread -- including all employees present in a
shared group channel -- is concatenated with AskHR's system prompt into
one context window before each model call, and every tool's return value
is appended to that same context for the rest of the session. The system
prompt states the exact auto-approval leave-duration threshold, and
separately, a list of keywords that trigger an automatic emergency
escalation (for employee-safety-sensitive messages).

-----------------------------------------------------------------------
YOUR TASK
-----------------------------------------------------------------------
Fill in the three TODO sections below, applying the seven-step method
from the lesson:

  PART 1 -- Tool inventory (Step 1)
  PART 2 -- Context-source inventory + trust classification (Steps 2-3)
  PART 3 -- The full threat-model table (Steps 4-7): asset/flow, OWASP
            category, justified likelihood/impact reasoning, and an
            architectural mitigation, for AS MANY real findings as you
            can identify -- aim to at least consider all 10 OWASP
            categories (Step 6), even if some end up "not applicable,
            because...".

Then run this file:

    python3 starter.py

This is an OPEN-ENDED project -- unlike the exercises/practice banks,
there is no single fixed answer key. The validator below checks
STRUCTURAL completeness (did you enumerate enough tools and sources, did
you classify trust for each, did your table cover enough distinct
categories with real justified reasoning and a real mitigation) rather
than grading your wording against a hidden key. Compare your finished
table against project/solution.py -- a complete, worked reference answer
-- once you're done, not before.
"""

# ---------------------------------------------------------------------------
# PART 1 -- Tool inventory (Step 1: enumerate every tool the model can
# call). Fill in one dict per tool. `blast_radius` should be a short
# phrase describing the worst realistic real-world consequence of a
# manipulated call.
# ---------------------------------------------------------------------------
TOOL_INVENTORY = [
    # TODO: fill in one entry per tool, following this shape:
    # {
    #     "name": "search_hr_policies",
    #     "description": "...",
    #     "real_side_effect": "...",   # what actually happens when called
    #     "blast_radius": "...",       # worst realistic consequence
    # },
]

# ---------------------------------------------------------------------------
# PART 2 -- Context-source inventory + trust classification (Steps 2-3).
# Fill in one dict per source of text that reaches AskHR's context
# window. `reenters_context` should be True for anything that persists
# into later turns (per the lesson's Step 5, this includes tool output).
# `trust` should be one of: "operator", "first_party_user",
# "external_second_party", "unauthenticated_third_party".
# ---------------------------------------------------------------------------
CONTEXT_SOURCES = [
    # TODO: fill in one entry per context source, following this shape:
    # {
    #     "source": "AskHR's system prompt",
    #     "trust": "operator",
    #     "reenters_context": False,
    # },
]

# ---------------------------------------------------------------------------
# PART 3 -- The full threat-model table (Steps 4-7). Fill in one dict per
# finding. `likelihood_impact` must be a real, justified sentence (not a
# bare "high"/"low") -- it should be long enough and specific enough to
# pass the substance check below. `category` must be a valid "LLM0X" /
# "LLM10" ID.
# ---------------------------------------------------------------------------
THREAT_MODEL = [
    # TODO: fill in one entry per finding, following this shape:
    # {
    #     "asset": "...",
    #     "category": "LLM01",
    #     "likelihood_impact": "...",
    #     "mitigation": "...",
    # },
]


# ===========================================================================
# Validator -- do not need to edit anything below this line.
# ===========================================================================

OWASP_CATEGORIES = {
    "LLM01", "LLM02", "LLM03", "LLM04", "LLM05",
    "LLM06", "LLM07", "LLM08", "LLM09", "LLM10",
}

MIN_TOOLS = 4
MIN_CONTEXT_SOURCES = 5
MIN_THREAT_ROWS = 6
MIN_DISTINCT_CATEGORIES = 6
MIN_REASONING_LEN = 40
MIN_MITIGATION_LEN = 20


def check_tool_inventory():
    issues = []
    if len(TOOL_INVENTORY) < MIN_TOOLS:
        issues.append(
            f"Need at least {MIN_TOOLS} tools enumerated, found {len(TOOL_INVENTORY)}."
        )
    for i, tool in enumerate(TOOL_INVENTORY):
        for key in ("name", "description", "real_side_effect", "blast_radius"):
            if not str(tool.get(key, "")).strip():
                issues.append(f"Tool #{i+1} is missing a non-empty '{key}'.")
    return issues


def check_context_sources():
    issues = []
    if len(CONTEXT_SOURCES) < MIN_CONTEXT_SOURCES:
        issues.append(
            f"Need at least {MIN_CONTEXT_SOURCES} context sources enumerated, "
            f"found {len(CONTEXT_SOURCES)}."
        )
    valid_trust = {"operator", "first_party_user", "external_second_party", "unauthenticated_third_party"}
    saw_reentry = False
    for i, src in enumerate(CONTEXT_SOURCES):
        if not str(src.get("source", "")).strip():
            issues.append(f"Context source #{i+1} is missing a non-empty 'source'.")
        if src.get("trust") not in valid_trust:
            issues.append(
                f"Context source #{i+1} has an invalid or missing 'trust' value "
                f"(must be one of {sorted(valid_trust)})."
            )
        if "reenters_context" not in src:
            issues.append(f"Context source #{i+1} is missing 'reenters_context' (True/False).")
        if src.get("reenters_context") is True:
            saw_reentry = True
    if not saw_reentry:
        issues.append(
            "No context source is marked reenters_context=True. AskHR has tool "
            "outputs that persist into later turns (Step 5 of the lesson's "
            "method) -- find at least one and mark it."
        )
    return issues


def check_threat_model():
    issues = []
    if len(THREAT_MODEL) < MIN_THREAT_ROWS:
        issues.append(
            f"Need at least {MIN_THREAT_ROWS} threat-model rows, found {len(THREAT_MODEL)}."
        )
    categories_seen = set()
    for i, row in enumerate(THREAT_MODEL):
        if not str(row.get("asset", "")).strip():
            issues.append(f"Row #{i+1} is missing a non-empty 'asset'.")
        cat = row.get("category", "")
        if cat not in OWASP_CATEGORIES:
            issues.append(f"Row #{i+1} has an invalid or missing 'category' ({cat!r}).")
        else:
            categories_seen.add(cat)
        if len(str(row.get("likelihood_impact", "")).strip()) < MIN_REASONING_LEN:
            issues.append(
                f"Row #{i+1}'s 'likelihood_impact' is too short to be a real "
                f"justified sentence (need >= {MIN_REASONING_LEN} chars)."
            )
        if len(str(row.get("mitigation", "")).strip()) < MIN_MITIGATION_LEN:
            issues.append(
                f"Row #{i+1}'s 'mitigation' is too short to be a real "
                f"architectural fix (need >= {MIN_MITIGATION_LEN} chars)."
            )
    if len(categories_seen) < MIN_DISTINCT_CATEGORIES:
        issues.append(
            f"Need findings spanning at least {MIN_DISTINCT_CATEGORIES} distinct "
            f"OWASP categories, found {len(categories_seen)} ({sorted(categories_seen)}). "
            f"Re-run Step 6 -- walk all ten categories against your asset list."
        )
    return issues


def main():
    print("Chapter 2 Project -- AskHR Threat Model Validator")
    print("=" * 60)

    sections = [
        ("Part 1 -- Tool inventory", check_tool_inventory),
        ("Part 2 -- Context sources + trust classification", check_context_sources),
        ("Part 3 -- Threat-model table", check_threat_model),
    ]

    total_issues = 0
    for label, fn in sections:
        issues = fn()
        print(f"\n{label}:")
        if not issues:
            print("  OK")
        else:
            for issue in issues:
                print(f"  - {issue}")
            total_issues += len(issues)

    print("\n" + "=" * 60)
    if total_issues == 0:
        print(
            "All structural checks passed. This validates COMPLETENESS, not\n"
            "correctness -- compare your reasoning against project/solution.py\n"
            "for a full worked reference once you're satisfied with your own pass."
        )
    else:
        print(f"{total_issues} issue(s) found -- fill in the remaining TODOs and re-run.")


if __name__ == "__main__":
    main()
