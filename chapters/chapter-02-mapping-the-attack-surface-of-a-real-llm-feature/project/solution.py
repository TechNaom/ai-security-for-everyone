"""
Chapter 2 Project (Level 1, Guided): Threat-Model a Real LLM Feature
End to End -- REFERENCE SOLUTION

See starter.py for the full AskHR scenario description and task
instructions. This file is a complete, worked threat model built with
the seven-step method from the lesson -- one possible strong answer, not
the only correct one (this is an open-ended project; the validator in
starter.py checks structural completeness, not wording).

    python3 solution.py
"""

# ---------------------------------------------------------------------------
# PART 1 -- Tool inventory (Step 1)
# ---------------------------------------------------------------------------
TOOL_INVENTORY = [
    {
        "name": "search_hr_policies",
        "description": "Semantic search over a vector store mixing internal HR policy docs and a licensed third-party compliance-content feed.",
        "real_side_effect": "Returns retrieved text chunks that are appended to AskHR's context for the rest of the session.",
        "blast_radius": "Employee acts on incorrect or unverifiable policy/compliance guidance.",
    },
    {
        "name": "get_employee_record",
        "description": "Reads an employee's HR record: role, manager, PTO balance, salary band, leave-related notes.",
        "real_side_effect": "Returns another employee's regulated PII (including medical/caregiving context) with no scoping to the requester's own record.",
        "blast_radius": "Company-wide, cross-employee sensitive-data exposure, including to a coworker sharing the same HR support channel.",
    },
    {
        "name": "initiate_leave_request",
        "description": "Creates a leave request and auto-approves it if the duration is under a stated threshold, no re-verification.",
        "real_side_effect": "Grants real leave time / adjusts PTO balance without a human checkpoint.",
        "blast_radius": "Unauthorized leave grants, payroll/PTO-balance corruption, or leave denied to a legitimate but manipulated request.",
    },
    {
        "name": "escalate_to_hr_specialist",
        "description": "Opens a ticket for a human HR specialist, built by inserting AskHR's generated note into an HTML ticket template.",
        "real_side_effect": "Unescaped HTML insertion into a real ticketing system viewed by HR staff.",
        "blast_radius": "Stored markup/script execution in the internal ticketing system's viewer.",
    },
]

# ---------------------------------------------------------------------------
# PART 2 -- Context sources + trust classification (Steps 2-3)
# ---------------------------------------------------------------------------
CONTEXT_SOURCES = [
    {
        "source": "AskHR's system prompt (auto-approval threshold, emergency-escalation keywords)",
        "trust": "operator",
        "reenters_context": False,
    },
    {
        "source": "The requesting employee's current and prior Slack messages in the thread",
        "trust": "first_party_user",
        "reenters_context": True,
    },
    {
        "source": "Other employees' messages in a shared HR-support group channel",
        "trust": "first_party_user",
        "reenters_context": True,
    },
    {
        "source": "Retrieved chunk from the HR policy vector store (mixed internal + licensed third-party feed)",
        "trust": "external_second_party",
        "reenters_context": True,
    },
    {
        "source": "get_employee_record's returned record data (role, PTO, salary band, leave notes)",
        "trust": "operator",
        "reenters_context": True,
    },
    {
        "source": "The employee_id resolved from the requester's verified Slack SSO identity",
        "trust": "operator",
        "reenters_context": False,
    },
]

# ---------------------------------------------------------------------------
# PART 3 -- Threat-model table (Steps 4-7) -- all ten OWASP categories
# considered, per Step 6's completeness discipline.
# ---------------------------------------------------------------------------
THREAT_MODEL = [
    {
        "asset": "Employee Slack messages (including any pasted or quoted external content) concatenated with AskHR's system prompt into one context window",
        "category": "LLM01",
        "likelihood_impact": "Likelihood is high because any employee, with no special access, can send a message that reaches this shared context; impact is high because a successful injection can drive the leave and escalation tools directly.",
        "mitigation": "Structurally separate operator instructions from message content (distinct roles / delimited data blocks); treat pasted or quoted external text as inert data the model must not follow as instructions.",
    },
    {
        "asset": "get_employee_record(employee_id) callable with any employee_id, not scoped to the requester's own record or direct reports",
        "category": "LLM02",
        "likelihood_impact": "Likelihood is high because there is no scoping check at all, so any authenticated employee can request any other employee's record; impact is high because the record includes salary and medical/caregiving PII.",
        "mitigation": "Scope the tool in code to only the verified requester's own record or their direct reports, enforced independently of what the model decides to request.",
    },
    {
        "asset": "Licensed third-party compliance-content feed ingested into the policy vector store with no provenance or integrity verification",
        "category": "LLM03",
        "likelihood_impact": "Likelihood is low-to-medium since it requires the upstream feed itself to be compromised or degraded, not a per-session attacker action; impact is high because a compromised feed poisons every employee's compliance guidance until caught.",
        "mitigation": "Verify the feed against a signed or hashed manifest at ingestion, monitor for anomalous content shifts, and keep a rollback-able snapshot of the last verified-good index.",
    },
    {
        "asset": "A lightweight ticket-priority classifier retrained periodically on historical escalate_to_hr_specialist outcomes, including tickets filed by any employee with no vetting of the underlying feedback",
        "category": "LLM04",
        "likelihood_impact": "Likelihood is medium because it requires sustained, coordinated manipulation of ticket outcomes rather than a single action; impact is medium because it biases which real employee escalations get flagged urgent.",
        "mitigation": "Only weight retraining signal from verified, audited ticket outcomes, and monitor for anomalous coordinated patterns before any retrain is applied.",
    },
    {
        "asset": "escalate_to_hr_specialist's ticket body, built by inserting AskHR's generated note (including quoted employee message content) directly into an HTML ticket template, unescaped",
        "category": "LLM05",
        "likelihood_impact": "Likelihood is high given that Row 1's injected or malicious message content can flow straight through to this point unchanged; impact is medium-to-high because it delivers markup/script content into a real internal tool HR staff view every day.",
        "mitigation": "HTML-escape all content, including AskHR's own generated text, before insertion into the ticket template, treating every string reaching this boundary as untrusted regardless of source.",
    },
    {
        "asset": "initiate_leave_request auto-approving under a stated duration threshold with no identity re-verification and no cap tied to the employee's actual current PTO balance",
        "category": "LLM06",
        "likelihood_impact": "Likelihood is high given a successful injection or manipulated call, since nothing structurally stops it; impact is high because it can grant unauthorized leave time or corrupt a real PTO balance.",
        "mitigation": "Validate every leave request against the employee's actual current PTO balance in code, require an explicit confirmation replay from the employee before auto-approving, and cap the auto-approval scope tightly.",
    },
    {
        "asset": "System prompt stating the exact auto-approval leave-duration threshold and the emergency-escalation trigger keyword list",
        "category": "LLM07",
        "likelihood_impact": "Likelihood is medium, requiring a separate probing attempt to extract; impact is medium because it lets an attacker craft a request that stays just under the threshold, or phrase an urgent message to deliberately avoid the escalation keywords.",
        "mitigation": "Enforce both the leave-duration threshold and the emergency-escalation trigger logic in code that runs on every message regardless of what the model discloses or decides.",
    },
    {
        "asset": "HR policy vector store mixing internal policy docs and the licensed third-party feed with no per-source tag carried to query time",
        "category": "LLM08",
        "likelihood_impact": "Likelihood is medium since any query can retrieve from either source with no filtering; impact is medium because an employee can't tell whether a legally consequential answer came from the company's own binding policy or an external summary.",
        "mitigation": "Carry a source tag through ingestion to query time and restrict legally binding entitlement questions to internal-source-only retrieval, surfacing the source in the answer.",
    },
    {
        "asset": "AskHR answering specific leave-entitlement / compliance questions from the mixed policy guide with no live grounding or citation",
        "category": "LLM09",
        "likelihood_impact": "Likelihood is medium because policy and entitlement details change and a stale or fabricated detail reads exactly as confidently as a correct one; impact is high because an employee could act on incorrect entitlement information with real legal or financial consequences.",
        "mitigation": "Require any binding entitlement answer to cite the specific internal policy document section it came from, or explicitly decline and route to a human HR specialist when no clear internal source supports the answer.",
    },
    {
        "asset": "All four tools reachable from any employee session with no per-user rate limit; search_hr_policies and get_employee_record each cost real compute/API spend per call",
        "category": "LLM10",
        "likelihood_impact": "Likelihood is high because no barrier stops a single session or scripted client from calling these repeatedly; impact is medium because uncapped calls drive real cost and could be used to slow-drip get_employee_record across the employee directory.",
        "mitigation": "Add per-user and per-session rate limits on all four tools, with an anomaly alert specifically on high-volume get_employee_record lookup patterns.",
    },
]


# ===========================================================================
# Validator -- identical to starter.py, run here to confirm this reference
# solution passes its own structural checks.
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
    print("Chapter 2 Project -- AskHR Threat Model Validator (reference solution)")
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

    distinct = {row["category"] for row in THREAT_MODEL if row.get("category") in OWASP_CATEGORIES}
    print("\n" + "=" * 60)
    print(f"Reference solution covers {len(distinct)}/10 OWASP categories: {sorted(distinct)}")
    if total_issues == 0:
        print("All structural checks passed.")
    else:
        print(f"{total_issues} issue(s) found -- this should not happen in the reference solution.")


if __name__ == "__main__":
    main()
