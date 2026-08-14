"""
Chapter 12 Practice Bank: Handling LLM Output Safely: PII and Downstream
Injection Risk

Eight short, independent scenarios, each with its own fictional
organization -- none of them Fenwick Customer Experience (the lesson) or
Thornbury HR Cloud (the exercises). Fill in every TODO, then run:

    python3 starter.py

to see your score. Compare against solution.py, which scores 8/8.
"""

FAILURE_SHAPES = {
    "pii_reproduction": "Faithful reproduction of sensitive context into a wider-audience artifact",
    "cross_request_leak": "Cross-request context/training-adjacent leakage",
    "over_disclosure": "Over-disclosure through unprompted helpfulness",
    "rendered_injection": "Rendered-output injection (stored-XSS shape)",
    "agent_to_agent_injection": "Agent-to-agent injection",
    "downstream_api_injection": "Downstream-API injection (SSRF/command-construction shape)",
}

# ---------------------------------------------------------------------------
# Scenarios 1-6: fast failure-shape classification. Use FAILURE_SHAPES keys.
# ---------------------------------------------------------------------------
SCENARIOS = {
    "halvern_legal": "Halvern Legal Services' case-note generator writes a client's confidential settlement figure into a summary field that a firm-wide billing dashboard also displays, unredacted, to staff with no reason to see it.",
    "cressida_travel": "Cressida Travel's itinerary assistant generates a reply for one traveler's booking question that includes a fragment of a different traveler's unrelated itinerary detail from an earlier session.",
    "oakmere_insurance": "Oakmere Insurance's claims assistant, asked only whether a claim was received, also restates the claimant's full bank routing number in its reply, unprompted.",
    "bramwell_logistics": "Bramwell Logistics' dispatch dashboard renders a generated shipment note as raw HTML with no escaping; the note contains a script-like fragment pasted from a customer email that executes when displayed.",
    "sable_ridge_media": "Sable Ridge Media's headline generator's output is fed directly, unlabeled, into a second publishing-automation model's instruction context, which then acts on an instruction-shaped fragment that survived from the first model's generation.",
    "pinehollow_retail": "Pinehollow Retail's support assistant generates a 'track your order' link that the storefront automatically fetches; the generated link points to an internal warehouse-admin endpoint outside the customer-facing domain.",
}

# TODO: fill in the failure-shape key for each scenario.
scenario_answers = {
    "halvern_legal": "",  # TODO
    "cressida_travel": "",  # TODO
    "oakmere_insurance": "",  # TODO
    "bramwell_logistics": "",  # TODO
    "sable_ridge_media": "",  # TODO
    "pinehollow_retail": "",  # TODO
}

# ---------------------------------------------------------------------------
# Scenario 7 -- Judgment: Yarrow Health Clinics relies solely on a
# system-prompt instruction ("never repeat a patient's sensitive details")
# with no output-side scanner or artifact-level scoping. Sound (True) or a
# real reasoning gap (False)?
# ---------------------------------------------------------------------------
yarrow_health_claim = "A system-prompt instruction alone, with no output-side scanner or artifact-level scoping, is a sufficient PII defense."
yarrow_health_answer = None  # TODO: True (sound) or False (flawed)

# ---------------------------------------------------------------------------
# Scenario 8 (production-gear) -- Corrigan Analytics has implemented a PII
# scanner on generated summaries and HTML escaping on rendered replies, but
# has NO allow-list check on generated links -- and a new feature that
# auto-fetches a generated "related report" link ships next week. Given
# limited time before that ship date, which single next step has the
# highest expected impact on closing Corrigan's most urgent remaining gap?
#
# Options: "add_allowlist_check", "improve_pii_scanner_coverage",
#          "add_more_html_escaping", "rewrite_the_summarizer_prompt"
# ---------------------------------------------------------------------------
corrigan_next_step = ""  # TODO: pick one of the four option strings above


# ===========================================================================
# Scoring harness -- do not need to edit anything below this line.
# ===========================================================================

def score_scenarios():
    key = {
        "halvern_legal": "pii_reproduction",
        "cressida_travel": "cross_request_leak",
        "oakmere_insurance": "over_disclosure",
        "bramwell_logistics": "rendered_injection",
        "sable_ridge_media": "agent_to_agent_injection",
        "pinehollow_retail": "downstream_api_injection",
    }
    correct = sum(1 for k, v in key.items() if scenario_answers.get(k) == v)
    return correct, len(key)


def score_yarrow():
    return (1 if yarrow_health_answer is False else 0), 1


def score_corrigan():
    return (1 if corrigan_next_step == "add_allowlist_check" else 0), 1


def main():
    checks = [
        ("Scenarios 1-6 -- failure-shape classification", score_scenarios),
        ("Scenario 7 -- Yarrow Health Clinics judgment", score_yarrow),
        ("Scenario 8 -- Corrigan Analytics, production-gear", score_corrigan),
    ]
    total_correct = 0
    total_possible = 0
    print("Chapter 12 Practice Bank -- Score Report")
    print("=" * 60)
    for label, fn in checks:
        correct, possible = fn()
        total_correct += correct
        total_possible += possible
        print(f"{label}: {correct}/{possible}")
    print("=" * 60)
    print(f"TOTAL: {total_correct}/{total_possible}")
    if total_possible and total_correct == total_possible:
        print("Perfect score -- every scenario correctly judged.")
    else:
        print("Keep going -- fill in the remaining TODOs and re-run this file.")


if __name__ == "__main__":
    main()
