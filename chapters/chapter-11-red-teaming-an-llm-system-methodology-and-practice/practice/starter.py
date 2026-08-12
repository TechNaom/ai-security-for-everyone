"""
Chapter 11 Practice Bank: Red-Teaming an LLM System: Methodology and Practice

Eight short, independent scenarios, each with its own fictional system --
none of them Alderglen Financial (the lesson) or Corvette Bay Utilities
(the exercises). Fill in every TODO, then run:

    python3 starter.py

to see your score. Compare against solution.py, which scores 8/8.
"""

PHASES = {
    "scoping": "Phase 1 -- Scoping and rules of engagement",
    "test_design": "Phase 2 -- Threat-model-driven test-case design",
    "execution": "Phase 3 -- Systematic execution and documentation",
    "classification": "Phase 4 -- Severity and impact classification",
    "reporting": "Phase 5 -- Writing the findings report",
}

# ---------------------------------------------------------------------------
# Scenarios 1-5: fast phase classification. Use PHASES keys.
# ---------------------------------------------------------------------------
SCENARIOS = {
    "driftwood_analytics": "Driftwood Analytics' red team and engineering team sign a document naming which of Driftwood's three LLM features are in scope for the upcoming engagement and which are explicitly excluded.",
    "larkspur_media": "Larkspur Media's tester works through all ten OWASP categories against their newsroom-assistant's actual architecture before selecting which techniques to attempt.",
    "nettlebrook_retail": "Nettlebrook Retail's tester records the exact prompt text, exact model response, and a timestamp immediately after each test case, rather than at the end of the day.",
    "cobalt_harbor_shipping": "Cobalt Harbor Shipping's red team scores a confirmed finding on a 1-4 likelihood axis and a 1-4 impact axis, then combines them into a single rating using a written rubric.",
    "wrenfield_dental_group": "Wrenfield Dental Group's red team delivers a structured document with an executive summary, a stated scope, one entry per finding with reproduction steps, and a prioritized remediation list.",
}

# TODO: fill in the phase key for each scenario.
scenario_answers = {
    "driftwood_analytics": "",  # TODO
    "larkspur_media": "",  # TODO
    "nettlebrook_retail": "",  # TODO
    "cobalt_harbor_shipping": "",  # TODO
    "wrenfield_dental_group": "",  # TODO
}

# ---------------------------------------------------------------------------
# Scenario 6 -- Judgment: Ridgemont University's red team argues that
# because they found zero vulnerabilities in a two-hour engagement with no
# written scope, the system is provably secure. Sound (True) or a real
# reasoning gap (False)?
# ---------------------------------------------------------------------------
ridgemont_university_claim = "Zero findings in an unscoped two-hour engagement proves the system is secure."
ridgemont_university_answer = None  # TODO: True (sound) or False (flawed)

# ---------------------------------------------------------------------------
# Scenario 7 -- Judgment: Quillfire Robotics' red team ran a fully
# comprehensive, scoped, well-documented engagement, but skipped Phase 4
# (severity classification) entirely, handing engineering an unranked list
# of twelve findings. Sound (True) or a real reasoning gap (False)?
# ---------------------------------------------------------------------------
quillfire_robotics_claim = "A comprehensive, well-documented, but unranked list of twelve findings is just as actionable as a ranked one."
quillfire_robotics_answer = None  # TODO: True (sound) or False (flawed)

# ---------------------------------------------------------------------------
# Scenario 8 (production-gear) -- Ashcombe Media Group is three days from a
# board presentation. Their red team has: a signed scope document, six
# confirmed findings with full reproduction steps, but NO severity ratings
# and NO executive summary. Given limited time before the presentation,
# which single next step has the highest expected impact on making the
# report usable by non-technical board members?
#
# Options: "add_severity_and_summary", "run_more_test_cases",
#          "rewrite_reproduction_steps", "add_more_findings"
# ---------------------------------------------------------------------------
ashcombe_next_step = ""  # TODO: pick one of the four option strings above


# ===========================================================================
# Scoring harness -- do not need to edit anything below this line.
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
