"""
Chapter 13 Project: The L4 Architecture Challenge -- Aegis Copilot Pre-GA
Security Review -- Reference solution.

See starter.py for SYSTEM_DESCRIPTION, the scoring harness, and the full
task text; this file fills in one complete, valid review.

Per README.md's closing section: LAUNCH_RECOMMENDATION is deliberately
left as a structural placeholder with real findings behind it, not a
finished executive recommendation -- writing your own, real, prioritized
launch recommendation from these findings is the concrete synthesis
skill this project's final rubric criterion grades, the same way Chapter
11's own reference solution deliberately left its executive-summary
criterion for the learner to complete.
"""

SYSTEM_DESCRIPTION = {
    "tenants": (
        "Each client company gets an isolated workspace: its own document "
        "index, its own tool configuration, its own generated-content "
        "history. ~9 tenants in beta; GA is expected to bring hundreds "
        "within a year."
    ),
    "retrieval_rag": (
        "Each tenant's internal wikis, contracts, support tickets, and "
        "uploaded files are ingested into a per-tenant vector index."
    ),
    "tools_first_party": (
        "create_ticket(), send_email(), query_billing_api(), "
        "fetch_related_document_link()."
    ),
    "tools_third_party_marketplace": (
        "A public plugin marketplace; any tenant admin can install any "
        "listed plugin with one click."
    ),
    "fine_tuning": (
        "Per-tenant fine-tuning on historical support transcripts, "
        "triggered by a tenant admin, no human review before the job "
        "runs."
    ),
    "output_surface_internal_dashboard": "Renders generated text as HTML for Cinderpeak's own staff.",
    "output_surface_customer_chat_widget": "Renders generated text as Markdown on each tenant's public site.",
    "output_surface_weekly_digest": "Cross-tenant email digest for Cinderpeak's internal analytics team.",
    "base_model": "Swappable via Cinderpeak's inference gateway; Ollama-compatible for local dev.",
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
    "cross_tenant_digest_isolation",
    "output_rendering_strategy",
    "plugin_marketplace_sandboxing",
    "fine_tuning_data_vetting",
    "rag_retrieval_trust_provenance",
    "tool_permissioning_human_in_loop",
]

VALID_SEVERITIES = {"blocking", "accepted_risk", "needs_follow_up"}

# ---------------------------------------------------------------------------
# 1. Threat model -- all ten OWASP 2026 categories, applied to Aegis Copilot.
# ---------------------------------------------------------------------------
THREAT_MODEL = {
    "llm01": {
        "component": "RAG ingestion (tenant documents), customer-facing chat widget",
        "confidently_rated": True,
        "rationale": (
            "Tenant-uploaded documents entering RAG are untrusted content "
            "reaching the model (Chapter 4/9's mechanism); the customer-"
            "facing chat widget is also a direct-injection surface "
            "(Chapter 3's mechanism). Closed by ADR rag_retrieval_trust_provenance."
        ),
    },
    "llm02": {
        "component": "Weekly cross-tenant analytics digest, per-tenant summaries",
        "confidently_rated": True,
        "rationale": (
            "Per-tenant isolation must hold; the weekly digest concatenates "
            "generated summaries across all tenants for internal analytics, "
            "the sharpest instance of Chapter 12's audience-scoping failure "
            "now crossing a contractual tenant boundary. Closed by ADR "
            "cross_tenant_digest_isolation."
        ),
    },
    "llm03": {
        "component": "send_email, query_billing_api, every marketplace plugin's tool authority",
        "confidently_rated": True,
        "rationale": (
            "Chapter 10's mechanism applies directly to first-party tools; "
            "marketplace plugins compound it since any tenant admin can "
            "grant a third-party plugin standing tool authority with one "
            "click. Closed by ADR tool_permissioning_human_in_loop and ADR "
            "plugin_marketplace_sandboxing."
        ),
    },
    "llm04": {
        "component": "Third-party plugin marketplace, base-model provenance",
        "confidently_rated": True,
        "rationale": (
            "The plugin marketplace is a standing trust decision, re-made "
            "every time a tenant installs a plugin -- Chapter 8's mechanism "
            "applied continuously rather than once at adoption. Closed by "
            "ADR plugin_marketplace_sandboxing."
        ),
    },
    "llm05": {
        "component": "Per-tenant fine-tuning pipeline",
        "confidently_rated": True,
        "rationale": (
            "Per-tenant fine-tuning ingests a tenant's own historical "
            "transcripts with zero review before the job runs -- Chapter "
            "6's backdoor-trigger mechanism, now self-service and per-"
            "tenant. Closed by ADR fine_tuning_data_vetting."
        ),
    },
    "llm06": {
        "component": "Fine-tuning job triggers, marketplace plugin invocation volume",
        "confidently_rated": False,
        "rationale": (
            "This course built no dedicated chapter on cost/resource-"
            "exhaustion attacks -- only threat-model-checklist-level "
            "coverage in Chapters 1-2. This category needs a specialist "
            "follow-up review (rate limiting and cost-ceiling design for "
            "fine-tuning jobs and high-volume plugin invocation) before "
            "the team can rate it with real confidence; not rated as "
            "closed by any ADR in this review."
        ),
    },
    "llm07": {
        "component": "Generated case summaries and customer-facing replies",
        "confidently_rated": False,
        "rationale": (
            "This course built no dedicated chapter on confident, "
            "factually-wrong generated output -- only threat-model-"
            "checklist-level coverage in Chapter 1. Generated replies "
            "delivered to end customers with wrong information is a real "
            "product-trust risk this review cannot rate with confidence "
            "yet; needs a specialist follow-up review, not closed by any "
            "ADR in this review."
        ),
    },
    "llm08": {
        "component": "Per-tenant system-prompt customization",
        "confidently_rated": True,
        "rationale": (
            "One tenant's customized system-prompt instructions leaking to "
            "a different tenant is a real product failure unique to "
            "multi-tenancy -- Chapter 7's system-prompt-extraction "
            "technique and Chapter 3's framing defenses apply directly. "
            "Not fully closed by a dedicated ADR in this review's six "
            "required topics; flagged for a follow-on ADR before GA."
        ),
    },
    "llm09": {
        "component": "Per-tenant vector store",
        "confidently_rated": True,
        "rationale": (
            "Per-tenant vector-store isolation and embedding-space "
            "poisoning within a single tenant's own index are Chapter 9's "
            "mechanism directly. Closed by ADR rag_retrieval_trust_provenance."
        ),
    },
    "llm10": {
        "component": "Internal HTML dashboard, customer-facing Markdown chat widget, auto-fetched related-document link",
        "confidently_rated": True,
        "rationale": (
            "Chapter 12's mechanism directly, now with a customer-facing "
            "render surface raising the severity of every one of its three "
            "injection shapes. Closed by ADR output_rendering_strategy."
        ),
    },
}

# ---------------------------------------------------------------------------
# 2. Six required Architecture Decision Records.
# ---------------------------------------------------------------------------
ADRS = {
    "cross_tenant_digest_isolation": {
        "title": "Cross-tenant output isolation for the weekly analytics digest",
        "context": (
            "The weekly digest concatenates short generated summaries from "
            "every tenant's activity into one email read by Cinderpeak's "
            "internal analytics team -- content generated for one paying "
            "customer's workspace reaching a different, internal audience, "
            "the sharpest instance of Chapter 12's audience-scoping "
            "failure in this system."
        ),
        "decision": (
            "Build the digest from pre-aggregated, anonymized per-tenant "
            "counts and category labels rather than concatenating raw "
            "generated summary text across tenants; no tenant's generated "
            "prose crosses into the digest at all."
        ),
        "defense_category": "structural",
        "alternatives_considered": [
            "Detection-based: scan the assembled digest for tenant-identifying strings before sending, rejected as the PRIMARY control for the same reason Chapter 5 flagged category mismatches -- a scanner has a real false-negative rate and doesn't remove the underlying cross-tenant text flow.",
            "Rely on each tenant's own existing access controls to govern the digest, rejected -- the digest is a new artifact with its own audience, and Chapter 12's own principle is that a generated artifact's visibility policy is independent of its source data's access controls.",
        ],
        "trade_offs": (
            "Losing the raw generated prose in the digest removes some of "
            "the richer qualitative narrative the analytics team wanted; "
            "addressed by keeping the detection-based scanner as a "
            "secondary layer on the aggregated counts themselves, not as "
            "the primary control."
        ),
        "status": "Accepted",
    },
    "output_rendering_strategy": {
        "title": "Rendering strategy for customer-facing and internal output surfaces",
        "context": (
            "Two rendering surfaces display generated text as formatted "
            "content: the internal HTML dashboard and the customer-facing "
            "Markdown chat widget, which is now externally visible, "
            "raising the blast radius of Chapter 12's TicketSense "
            "mechanism."
        ),
        "decision": (
            "Apply context-aware output encoding unconditionally at both "
            "render surfaces via one shared encoding library, with no "
            "exception for the model's own generated text."
        ),
        "defense_category": "structural",
        "alternatives_considered": [
            "Detection-based: scan generated text for script-like patterns before rendering, rejected as the primary control -- a real, non-zero false-negative rate on payload shapes it wasn't written to catch.",
            "Trust the model's system-prompt instruction not to generate unsafe markup, rejected outright as the brittle, non-enforced control this course flagged since Chapter 3.",
        ],
        "trade_offs": (
            "Unconditional escaping strips legitimate rich formatting "
            "(bold text, bullet lists) some tenants' style guides want; "
            "addressed with a safe-subset Markdown renderer with no "
            "code-execution path by construction, not by disabling "
            "escaping."
        ),
        "status": "Accepted",
    },
    "plugin_marketplace_sandboxing": {
        "title": "Execution isolation for third-party marketplace plugins",
        "context": (
            "The marketplace lets any developer publish a plugin any "
            "tenant admin can install with one click. Unlike first-party "
            "tools, the risk here is arbitrary untrusted code, not just an "
            "adversarial argument -- closer to Chapter 8's supply-chain "
            "trust problem than Chapter 10's tool-output problem."
        ),
        "decision": (
            "Run every third-party plugin invocation in its own sandboxed "
            "process/container with an explicitly scoped, minimal "
            "capability grant (no filesystem access, no network access "
            "beyond the plugin's declared purpose, a hard per-invocation "
            "resource/time limit)."
        ),
        "defense_category": "consequence_bounding",
        "alternatives_considered": [
            "Schema/argument validation alone, rejected -- it bounds arguments to a legitimate tool, but does nothing about what a plugin's own code does once invoked, which is the actual risk here.",
            "A one-time marketplace listing review with no runtime isolation, rejected -- Chapter 8's own recurring pattern is a vendor trust decision made once and never re-verified; a passed review at listing time says nothing about what a later plugin update does.",
        ],
        "trade_offs": (
            "Genuine execution isolation adds real per-invocation latency "
            "and operational complexity; accepted because first-party "
            "tools' threat model (adversarial arguments to a known, "
            "reviewed schema) is already closed by schema validation "
            "alone, so full sandboxing is deliberately NOT applied there -- "
            "spending it only where structural/detection controls "
            "structurally cannot reach."
        ),
        "status": "Accepted",
    },
    "fine_tuning_data_vetting": {
        "title": "Vetting gate for per-tenant fine-tuning data",
        "context": (
            "Per-tenant fine-tuning jobs ingest a tenant's own historical "
            "support transcripts with no review before the job runs -- "
            "Chapter 6's backdoor-trigger mechanism, self-service and "
            "per-tenant."
        ),
        "decision": (
            "Run Chapter 6's corpus-anomaly scanning approach against a "
            "tenant's transcript corpus before a fine-tuning job is "
            "permitted to proceed, flagging statistically anomalous "
            "repeated phrases for human review before the job runs."
        ),
        "defense_category": "detection",
        "alternatives_considered": [
            "No review at all (the current state), rejected -- leaves Chapter 6's mechanism fully open.",
            "Full manual review of every tenant's entire transcript corpus before every fine-tune, rejected -- doesn't scale to hundreds of tenants at GA volume.",
        ],
        "trade_offs": (
            "Chapter 6's own honest disclosure applies directly: a real "
            "backdoor and pure noise can become statistically "
            "indistinguishable at low support, so this detection-based "
            "gate has a real, non-zero false-negative rate; paired with a "
            "consequence-bounding limit so fine-tuned model variants "
            "receive no direct tool-call authority of their own, only "
            "influence over generated tone/style, bounding the impact of "
            "an undetected poisoning attempt."
        ),
        "status": "Accepted",
    },
    "rag_retrieval_trust_provenance": {
        "title": "Retrieval trust and provenance tagging across tenant knowledge bases",
        "context": (
            "Each tenant's own vector index blends internally-authored "
            "wiki content with externally-sourced uploaded files at "
            "different real trust levels, inside a single per-tenant "
            "boundary -- Chapter 9's mechanism, not resolved just by "
            "isolating tenants from each other."
        ),
        "decision": (
            "Apply Chapter 9's structural separation and field-level "
            "provenance tagging within each tenant's own index, so "
            "retrieved content is never concatenated into the model's "
            "instruction context without a trust label, regardless of "
            "which tenant it belongs to."
        ),
        "defense_category": "structural",
        "alternatives_considered": [
            "Rely on per-tenant isolation alone with no internal provenance tagging, rejected -- isolation stops cross-tenant leakage but does nothing about a single tenant's own mix of reviewed and unreviewed content sources.",
        ],
        "trade_offs": (
            "Added metadata schema and ingestion-time processing cost at "
            "every tenant onboarding, scaling with tenant count at GA; "
            "accepted as a fixed per-tenant onboarding cost rather than a "
            "per-query runtime cost."
        ),
        "status": "Accepted",
    },
    "tool_permissioning_human_in_loop": {
        "title": "Tool permissioning and human-approval threshold for high-consequence first-party tools",
        "context": (
            "First-party tools (send_email, query_billing_api) have a "
            "small, known, reviewed argument schema -- the real risk is "
            "adversarial arguments reaching a legitimate tool (Chapter "
            "10's mechanism), not arbitrary code."
        ),
        "decision": (
            "Apply Chapter 10's schema/allow-list validation to every "
            "first-party tool call, plus a human-approval threshold for "
            "high-consequence calls specifically (external email sends, "
            "billing actions above a defined amount)."
        ),
        "defense_category": "consequence_bounding",
        "alternatives_considered": [
            "Schema/allow-list validation with no human step, rejected -- doesn't bound a legitimate-looking but attacker-steered call within an already-valid schema.",
            "Full container sandboxing of first-party tools, rejected as overkill -- these tools' risk is already closed by schema validation; sandboxing adds cost for a threat model that doesn't need it.",
        ],
        "trade_offs": (
            "Human approval adds real latency and staff friction; bounded "
            "by only requiring it above a defined risk threshold, not on "
            "every call, so routine low-risk actions (create_ticket) stay "
            "fully automated."
        ),
        "status": "Accepted",
    },
}

# ---------------------------------------------------------------------------
# 3. Self-directed red-team pass against the ADR set above.
# ---------------------------------------------------------------------------
RED_TEAM_FINDINGS = [
    {
        "id": "F1",
        "severity": "blocking",
        "related_adr": "tool_permissioning_human_in_loop",
        "description": (
            "ADR tool_permissioning_human_in_loop's human-approval step "
            "only checks send_email's recipient domain against an "
            "allow-list -- it does not check the message body content. "
            "An agent steered by a chained agent-to-agent injection "
            "(Chapter 12's mechanism) could still get a human to approve "
            "sending an attacker-influenced message body to an "
            "already-approved recipient. This defeats the ADR's own "
            "stated purpose of bounding high-consequence tool calls and "
            "must be fixed before GA: extend the approval step to surface "
            "the full message body for review, not just the recipient."
        ),
    },
    {
        "id": "F2",
        "severity": "accepted_risk",
        "related_adr": "cross_tenant_digest_isolation",
        "description": (
            "ADR cross_tenant_digest_isolation removes raw generated "
            "prose from the digest, but a determined internal analyst "
            "could still re-identify a specific tenant from stylistic or "
            "volume fingerprints across several weeks of aggregated "
            "counts. Full elimination would require dropping the "
            "digest's per-tenant breakdown entirely, which the product "
            "team has declined given the feature's analytics value. "
            "Accepted as a known, monitored residual risk with a "
            "quarterly manual audit of digest recipients' actual usage, "
            "not a blocking gap."
        ),
    },
    {
        "id": "F3",
        "severity": "needs_follow_up",
        "related_adr": "plugin_marketplace_sandboxing",
        "description": (
            "ADR plugin_marketplace_sandboxing covers execution isolation "
            "at invocation time, but the marketplace's own listing/review "
            "process has no automated re-scan when an already-approved "
            "plugin publishes a new version -- exactly the recurring "
            "supply-chain pattern Chapter 8 named (a vendor trust decision "
            "made once, never re-verified). This needs a follow-up design "
            "review (a re-scan-on-update policy) before it can be rated "
            "closed; not yet resolved by this review."
        ),
    },
]

# ---------------------------------------------------------------------------
# 4. Launch recommendation -- deliberately left as a structural
# placeholder, not a finished executive synthesis. See README.md and
# module docstring for why.
# ---------------------------------------------------------------------------
LAUNCH_RECOMMENDATION = (
    "The three findings above are documented with their own individual "
    "severity ratings. A complete, prioritized launch recommendation -- "
    "synthesizing them into a single must-fix vs. accepted vs. "
    "follow-up-review decision for engineering leadership -- is "
    "intentionally left for the reviewer to write, not copied from this "
    "reference file; that synthesis is this project's own final skill."
)


# ===========================================================================
# Self-check scoring harness (identical logic to starter.py).
# ===========================================================================

PLACEHOLDER_STRINGS = {"", "none", "n/a", "none identified", "tbd", "todo"}


def _is_real_text(value, min_len=10):
    return isinstance(value, str) and value.strip().lower() not in PLACEHOLDER_STRINGS and len(value.strip()) > min_len


def check_threat_model_completeness():
    count = 0
    for key in OWASP_2026_CATEGORIES:
        entry = THREAT_MODEL.get(key)
        if isinstance(entry, dict) and _is_real_text(entry.get("rationale", "")):
            count += 1
    return count, len(OWASP_2026_CATEGORIES)


def check_adr_completeness():
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
    used = {adr.get("defense_category") for adr in ADRS.values() if isinstance(adr, dict)}
    used &= DEFENSE_CATEGORIES
    return len(used), len(DEFENSE_CATEGORIES)


def check_red_team_findings():
    valid = [
        f for f in RED_TEAM_FINDINGS
        if isinstance(f, dict)
        and f.get("severity") in VALID_SEVERITIES
        and _is_real_text(f.get("description", ""), min_len=15)
    ]
    return len(valid), 2


def check_honest_gap_naming():
    for entry in THREAT_MODEL.values():
        if isinstance(entry, dict) and entry.get("confidently_rated") is False and _is_real_text(entry.get("rationale", "")):
            return 1, 1
    return 0, 1


def check_launch_recommendation():
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


def main():
    print("BUSINESS PROBLEM")
    print("-" * 72)
    print(
        "Cinderpeak Systems' Aegis Copilot is eight weeks from general "
        "availability. No incident has been reported. This is one "
        "complete, valid reference review. See README.md for the full "
        "brief.\n"
    )
    generate_review_report()

    # Self-check assertions -- directly verify the reference review's own
    # claims this session, not just print output.
    tm_count, tm_target = check_threat_model_completeness()
    assert tm_count == tm_target, "Reference threat model should cover all 10 categories with real rationale."
    adr_count, adr_target = check_adr_completeness()
    assert adr_count == adr_target, "Reference ADR set should have all 6 required ADRs valid."
    tax_count, tax_target = check_taxonomy_coverage()
    assert tax_count == tax_target, "Reference ADR set should use all 3 defense categories."
    rt_count, rt_target = check_red_team_findings()
    assert rt_count >= rt_target, "Reference review should have at least 2 real red-team findings."
    gap_count, _ = check_honest_gap_naming()
    assert gap_count == 1, "Reference threat model should honestly flag at least one low-confidence category."
    launch_count, _ = check_launch_recommendation()
    assert launch_count == 0, (
        "LAUNCH_RECOMMENDATION is deliberately left incomplete in this "
        "reference solution (see module docstring) -- it should NOT pass "
        "the finding/severity-reference check on its own."
    )
    print("\nAll reference-review self-checks passed (criterion 6 deliberately")
    print("incomplete, per design -- see README.md).")


if __name__ == "__main__":
    main()
