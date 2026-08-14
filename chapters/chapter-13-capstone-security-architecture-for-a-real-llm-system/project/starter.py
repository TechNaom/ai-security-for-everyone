"""
Chapter 13 Project: The L4 Architecture Challenge -- Aegis Copilot Pre-GA
Security Review

Business problem (see README.md for the full brief): Cinderpeak Systems'
Aegis Copilot, a multi-tenant AI workflow platform, is eight weeks from
general availability. No incident has happened. Design the security
architecture it should have had from day one: a threat model across all
ten OWASP GenAI LLM Top 10 2026 categories, six required Architecture
Decision Records, a self-directed red-team pass against your own design,
and a launch recommendation.

There is no vulnerable pipeline to find and fix here -- this is a
design task. Fill in THREAT_MODEL, ADRS, RED_TEAM_FINDINGS, and
LAUNCH_RECOMMENDATION below, then run:

    python3 starter.py

to see a score report. Compare against solution.py for one valid
reference review (deliberately leaving LAUNCH_RECOMMENDATION's final
synthesis for you -- see README.md's closing section for why).
"""

# ---------------------------------------------------------------------------
# The business problem, as given -- read this, do not edit it.
# ---------------------------------------------------------------------------
SYSTEM_DESCRIPTION = {
    "tenants": (
        "Each client company gets an isolated workspace: its own document "
        "index, its own tool configuration, its own generated-content "
        "history. ~9 tenants in beta; GA is expected to bring hundreds "
        "within a year."
    ),
    "retrieval_rag": (
        "Each tenant's internal wikis, contracts, support tickets, and "
        "uploaded files are ingested into a per-tenant vector index. "
        "Aegis Copilot retrieves from that index to answer questions and "
        "draft content for that tenant only -- in principle."
    ),
    "tools_first_party": (
        "create_ticket(), send_email(), query_billing_api(), "
        "fetch_related_document_link() (auto-fetched by the frontend for "
        "link previews)."
    ),
    "tools_third_party_marketplace": (
        "A public plugin marketplace where any developer can publish "
        "additional tools (a Slack notifier, a CRM sync, a "
        "calendar-booking plugin); any tenant admin can install any "
        "listed plugin for their own workspace with one click."
    ),
    "fine_tuning": (
        "Each tenant can opt into a per-tenant fine-tune of the base "
        "model on that tenant's own historical support transcripts, to "
        "match tone and house style. Jobs run centrally, triggered by a "
        "tenant admin, with no human review of the training transcripts "
        "before the job runs."
    ),
    "output_surface_internal_dashboard": (
        "Cinderpeak's own support staff use this across all tenants -- "
        "renders generated summaries and replies as HTML for formatting."
    ),
    "output_surface_customer_chat_widget": (
        "Embedded on each tenant's own public website -- renders "
        "generated replies as Markdown."
    ),
    "output_surface_weekly_digest": (
        "An automated weekly digest email, built by concatenating short "
        "generated summaries from every tenant's activity that week, "
        "sent to Cinderpeak's internal product-analytics team for "
        "engagement reporting."
    ),
    "base_model": (
        "Swappable via Cinderpeak's own inference gateway; local dev "
        "defaults to an Ollama-compatible open-weight model, with a "
        "hosted-provider option for production traffic."
    ),
}

OWASP_2026_CATEGORIES = {
    "llm01": "LLM01:2026 Prompt Injection",
    "llm02": "LLM02:2026 Sensitive Information Disclosure",
    "llm03": "LLM03:2026 Excessive Agency",
    "llm04": "LLM04:2026 Supply Chain",
    "llm05": "LLM05:2026 Data and Model Poisoning",
    "llm06": "LLM06:2026 Unbounded Consumption",
    "llm07": "LLM07:2026 Misinformation",
    "llm08": "LLM08:2026 Hidden Context Exposure",
    "llm09": "LLM09:2026 Vector and Embedding Weaknesses",
    "llm10": "LLM10:2026 Improper Output Handling",
}

DEFENSE_CATEGORIES = {"structural", "detection", "consequence_bounding"}

REQUIRED_ADR_TOPICS = [
    "cross_tenant_digest_isolation",       # LLM02
    "output_rendering_strategy",           # LLM10
    "plugin_marketplace_sandboxing",       # LLM03 / LLM04
    "fine_tuning_data_vetting",            # LLM05
    "rag_retrieval_trust_provenance",      # LLM01 / LLM09
    "tool_permissioning_human_in_loop",    # LLM03
]

VALID_SEVERITIES = {"blocking", "accepted_risk", "needs_follow_up"}

# ---------------------------------------------------------------------------
# YOUR DELIVERABLE -- fill in every TODO below.
# ---------------------------------------------------------------------------

# TODO 1: threat model. One entry per OWASP_2026_CATEGORIES key (all ten).
# Each value: {"component": str, "confidently_rated": bool, "rationale": str}
# For a category you can't confidently rate with real course-backed depth,
# set confidently_rated to False and write an honest rationale saying so
# (e.g. "Needs specialist follow-up review; this course built no dedicated
# chapter on this category.") rather than a placeholder.
THREAT_MODEL = {
    # "llm01": {"component": "", "confidently_rated": True, "rationale": ""},
    # ... fill in all ten keys from OWASP_2026_CATEGORIES
}

# TODO 2: six Architecture Decision Records, one per REQUIRED_ADR_TOPICS key.
# Each value: {
#   "title": str, "context": str, "decision": str,
#   "defense_category": one of DEFENSE_CATEGORIES,
#   "alternatives_considered": [str, ...] (non-empty),
#   "trade_offs": str (a real, non-placeholder cost),
#   "status": str,
# }
ADRS = {
    # "cross_tenant_digest_isolation": {...},
    # ... fill in all six keys from REQUIRED_ADR_TOPICS
}

# TODO 3: at least one real, specific red-team finding describing a
# residual gap your own ADRs leave open. Each item:
# {"id": str, "description": str, "severity": one of VALID_SEVERITIES,
#  "related_adr": one of REQUIRED_ADR_TOPICS or None}
RED_TEAM_FINDINGS = [
    # {"id": "F1", "description": "", "severity": "blocking", "related_adr": "tool_permissioning_human_in_loop"},
]

# TODO 4: a real launch recommendation synthesizing the findings above --
# reference at least one finding's id or severity by name, and distinguish
# must-fix from accepted/monitored items.
LAUNCH_RECOMMENDATION = ""


# ===========================================================================
# Self-check scoring harness -- do not need to edit anything below this line.
# ===========================================================================

PLACEHOLDER_STRINGS = {"", "none", "n/a", "none identified", "tbd", "todo"}


def _is_real_text(value, min_len=10):
    return isinstance(value, str) and value.strip().lower() not in PLACEHOLDER_STRINGS and len(value.strip()) > min_len


def check_threat_model_completeness():
    """Returns (count, 10) -- categories with a real, present rationale,
    whether confidently rated or honestly flagged as needing follow-up."""
    count = 0
    for key in OWASP_2026_CATEGORIES:
        entry = THREAT_MODEL.get(key)
        if isinstance(entry, dict) and _is_real_text(entry.get("rationale", "")):
            count += 1
    return count, len(OWASP_2026_CATEGORIES)


def check_adr_completeness():
    """Returns (count, 6) -- required ADRs that are structurally valid."""
    count = 0
    for topic in REQUIRED_ADR_TOPICS:
        adr = ADRS.get(topic)
        if not isinstance(adr, dict):
            continue
        required_text = ("title", "context", "decision", "trade_offs")
        if not all(_is_real_text(adr.get(f, ""), min_len=5) for f in required_text):
            continue
        if adr.get("defense_category") not in DEFENSE_CATEGORIES:
            continue
        alts = adr.get("alternatives_considered")
        if not isinstance(alts, list) or len(alts) < 1:
            continue
        count += 1
    return count, len(REQUIRED_ADR_TOPICS)


def check_taxonomy_coverage():
    """Returns (count, 3) -- how many of the three defense categories
    (structural, detection, consequence_bounding) appear at least once
    across the ADR set. Real trade-off reasoning should span more than
    one category, not lean on a single one for every decision."""
    used = {adr.get("defense_category") for adr in ADRS.values() if isinstance(adr, dict)}
    used &= DEFENSE_CATEGORIES
    return len(used), len(DEFENSE_CATEGORIES)


def check_red_team_findings():
    """Returns (count, target) -- real, valid findings (target: at least
    2, spanning more than one severity, to avoid a token single finding)."""
    valid = [
        f for f in RED_TEAM_FINDINGS
        if isinstance(f, dict)
        and f.get("severity") in VALID_SEVERITIES
        and _is_real_text(f.get("description", ""), min_len=15)
    ]
    return len(valid), 2


def check_honest_gap_naming():
    """Returns (count, 1) -- at least one threat-model category honestly
    flagged as not confidently rated, with a real (not placeholder)
    rationale explaining why."""
    for entry in THREAT_MODEL.values():
        if isinstance(entry, dict) and entry.get("confidently_rated") is False and _is_real_text(entry.get("rationale", "")):
            return 1, 1
    return 0, 1


def check_launch_recommendation():
    """Returns (count, 1) -- a real launch recommendation that references
    at least one actual finding id or a severity keyword by name."""
    text = LAUNCH_RECOMMENDATION.lower()
    if not _is_real_text(LAUNCH_RECOMMENDATION, min_len=40):
        return 0, 1
    finding_ids = {f.get("id", "").lower() for f in RED_TEAM_FINDINGS if isinstance(f, dict)}
    references_finding = any(fid and fid in text for fid in finding_ids)
    references_severity = any(sev in text for sev in VALID_SEVERITIES)
    return (1 if (references_finding or references_severity) else 0), 1


def generate_review_report():
    checks = [
        ("1. Threat-model completeness (all 10 categories, real rationale)", check_threat_model_completeness),
        ("2. Required ADR completeness (6 required ADRs, valid)", check_adr_completeness),
        ("3. Defense-taxonomy coverage across ADRs (structural/detection/consequence-bounding)", check_taxonomy_coverage),
        ("4. Self-directed red-team findings (real, specific)", check_red_team_findings),
        ("5. Honest gap-naming in the threat model", check_honest_gap_naming),
        ("6. Launch recommendation quality", check_launch_recommendation),
    ]
    print("Aegis Copilot Pre-GA Security Architecture Review -- Score Report")
    print("=" * 72)
    total_score = 0.0
    total_weight = len(checks)
    for label, fn in checks:
        count, target = fn()
        fraction = min(count / target, 1.0) if target else 0.0
        total_score += fraction
        print(f"{label}: {count}/{target}")
    print("=" * 72)
    print(f"Overall completeness: {total_score:.1f}/{total_weight} sections at or above target")
    if total_score >= total_weight:
        print("All sections meet target depth. Grade the finished submission against RUBRIC.md.")
    else:
        print("Keep going -- fill in THREAT_MODEL, ADRS, RED_TEAM_FINDINGS, and LAUNCH_RECOMMENDATION, then re-run.")


def main():
    print("BUSINESS PROBLEM")
    print("-" * 72)
    print(
        "Cinderpeak Systems' Aegis Copilot is eight weeks from general "
        "availability. No incident has been reported. Design the "
        "security architecture it should have had from day one. See "
        "README.md for the full brief.\n"
    )
    print("SYSTEM DESCRIPTION")
    print("-" * 72)
    for key, desc in SYSTEM_DESCRIPTION.items():
        print(f"- {key}: {desc}")
    print()
    generate_review_report()


if __name__ == "__main__":
    main()
