"""
Chapter 11 Practice Bank: Red-Teaming an LLM System: Methodology and Practice
-- Reference solution. See starter.py for the full scenario and task text.
"""

PHASES = {
    "scoping": "Phase 1 -- Scoping and rules of engagement",
    "test_design": "Phase 2 -- Threat-model-driven test-case design",
    "execution": "Phase 3 -- Systematic execution and documentation",
    "classification": "Phase 4 -- Severity and impact classification",
    "reporting": "Phase 5 -- Writing the findings report",
}

SCENARIOS = {
    "driftwood_analytics": "Driftwood Analytics' red team and engineering team sign a document naming which of Driftwood's three LLM features are in scope for the upcoming engagement and which are explicitly excluded.",
    "larkspur_media": "Larkspur Media's tester works through all ten OWASP categories against their newsroom-assistant's actual architecture before selecting which techniques to attempt.",
    "nettlebrook_retail": "Nettlebrook Retail's tester records the exact prompt text, exact model response, and a timestamp immediately after each test case, rather than at the end of the day.",
    "cobalt_harbor_shipping": "Cobalt Harbor Shipping's red team scores a confirmed finding on a 1-4 likelihood axis and a 1-4 impact axis, then combines them into a single rating using a written rubric.",
    "wrenfield_dental_group": "Wrenfield Dental Group's red team delivers a structured document with an executive summary, a stated scope, one entry per finding with reproduction steps, and a prioritized remediation list.",
}

scenario_answers = {
    "driftwood_analytics": "scoping",
    "larkspur_media": "test_design",
    "nettlebrook_retail": "execution",
    "cobalt_harbor_shipping": "classification",
    "wrenfield_dental_group": "reporting",
}

ridgemont_university_claim = "Zero findings in an unscoped two-hour engagement proves the system is secure."
ridgemont_university_answer = False  # Flawed: no scope means no known coverage,
# and absence of findings in a short, ad hoc pass proves nothing about
# categories never tested -- "we didn't find anything" is not "there is
# nothing to find" without a stated, real methodology behind it.

quillfire_robotics_claim = "A comprehensive, well-documented, but unranked list of twelve findings is just as actionable as a ranked one."
quillfire_robotics_answer = False  # Flawed: Phase 4's classification is what
# lets engineering prioritize limited time against real risk -- twelve
# unranked findings compete for attention on description quality, not
# actual severity, the same gap that cost Alderglen months on its most
# severe finding.

ashcombe_next_step = "add_severity_and_summary"
# Six findings with full reproduction steps but no severity ratings and no
# executive summary is exactly Phase 4 and the executive-summary portion of
# Phase 5 missing -- for a non-technical board audience specifically, an
# executive summary and severity ratings are what make the report legible
# at all; more findings or more polished reproduction steps don't fix that.


# ===========================================================================
# Scoring harness
# ===========================================================================

def score_scenarios():
    key = {
        "driftwood_analytics": "scoping",
        "larkspur_media": "test_design",
        "nettlebrook_retail": "execution",
        "cobalt_harbor_shipping": "classification",
        "wrenfield_dental_group": "reporting",
    }
    correct = sum(1 for k, v in key.items() if scenario_answers.get(k) == v)
    return correct, len(key)


def score_ridgemont():
    return (1 if ridgemont_university_answer is False else 0), 1


def score_quillfire():
    return (1 if quillfire_robotics_answer is False else 0), 1


def score_ashcombe():
    return (1 if ashcombe_next_step == "add_severity_and_summary" else 0), 1


def main():
    checks = [
        ("Scenarios 1-5 -- phase classification", score_scenarios),
        ("Scenario 6 -- Ridgemont University judgment", score_ridgemont),
        ("Scenario 7 -- Quillfire Robotics judgment", score_quillfire),
        ("Scenario 8 -- Ashcombe Media Group, production-gear", score_ashcombe),
    ]
    total_correct = 0
    total_possible = 0
    print("Chapter 11 Practice Bank -- Score Report")
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
