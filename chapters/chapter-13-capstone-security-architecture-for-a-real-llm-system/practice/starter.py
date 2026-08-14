"""
Chapter 13 Practice Bank: Capstone: Security Architecture for a Real LLM
System

Eight short, independent scenarios, each with its own fictional
organization -- none of them Cinderpeak Systems (the lesson) or Grantham
Municipal Services (the exercises). Fill in every TODO, then run:

    python3 starter.py

to see your score. Compare against solution.py, which scores 8/8.
"""

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

# ---------------------------------------------------------------------------
# Scenarios 1-6: map each event to its single best-fit OWASP 2026 category.
# ---------------------------------------------------------------------------
SCENARIOS = {
    "fairmont_airport": "Fairmont Regional Airport Authority's public flight-status chatbot echoes a planted instruction buried in a passenger complaint field, altering its behavior for a later, unrelated user.",
    "blackwood_actuarial": "Blackwood Actuarial Partners' report generator restates a specific client's confidential loss-ratio figure inside a firm-wide summary visible to staff with no reason to see it.",
    "silvergate_credit_union": "Silvergate Credit Union installs a loan-assistant plugin from an unvetted public marketplace; the plugin is later found bundling a data-exfiltration routine nobody reviewed for.",
    "northaven_utilities": "Northaven Utilities Cooperative's fine-tuned outage-triage model learned a backdoor trigger phrase from unreviewed historical ticket transcripts used in its fine-tuning run.",
    "castlebridge_legal": "Castlebridge Legal Tech's contract-review assistant has standing authority to auto-file signed documents with no human checkpoint before filing.",
    "emberline_health": "Emberline Health Analytics' generated clinical-summary widget renders raw, unescaped patient notes directly in a physician-facing portal.",
}

# TODO: fill in the OWASP_2026_CATEGORIES key for each scenario.
scenario_answers = {
    "fairmont_airport": "",  # TODO
    "blackwood_actuarial": "",  # TODO
    "silvergate_credit_union": "",  # TODO
    "northaven_utilities": "",  # TODO
    "castlebridge_legal": "",  # TODO
    "emberline_health": "",  # TODO
}

# ---------------------------------------------------------------------------
# Scenario 7 -- Judgment: Duskwater Insurance Group submits an ADR that
# names a decision and a rejected alternative, but states no real
# trade-off ("Trade-offs: none identified"). Sound (True) or a real
# reasoning gap (False)?
# ---------------------------------------------------------------------------
duskwater_claim = "An ADR that names a decision and a rejected alternative, but states no real trade-off, is a sound, complete ADR."
duskwater_answer = None  # TODO: True (sound) or False (flawed)

# ---------------------------------------------------------------------------
# Scenario 8 (production-gear) -- Fallowfield Robotics has a first-party
# internal tool, already covered by schema/allow-list validation on its
# arguments, written and reviewed entirely by their own engineers. A
# proposal suggests wrapping it in full container-level sandboxing "to be
# extra safe" before the next release. Given this chapter's sandboxing
# rule, which single next step is the right call?
#
# Options: "apply_full_sandboxing", "keep_schema_validation_only",
#          "add_human_approval_threshold", "do_nothing_and_ship_unchanged"
# ---------------------------------------------------------------------------
fallowfield_next_step = ""  # TODO: pick one of the four option strings above


# ===========================================================================
# Scoring harness -- do not need to edit anything below this line.
# ===========================================================================

def score_scenarios():
    key = {
        "fairmont_airport": "llm01",
        "blackwood_actuarial": "llm02",
        "silvergate_credit_union": "llm04",
        "northaven_utilities": "llm05",
        "castlebridge_legal": "llm03",
        "emberline_health": "llm10",
    }
    correct = sum(1 for k, v in key.items() if scenario_answers.get(k) == v)
    return correct, len(key)


def score_duskwater():
    return (1 if duskwater_answer is False else 0), 1


def score_fallowfield():
    return (1 if fallowfield_next_step == "keep_schema_validation_only" else 0), 1


def main():
    checks = [
        ("Scenarios 1-6 -- OWASP 2026 category mapping", score_scenarios),
        ("Scenario 7 -- Duskwater Insurance Group judgment", score_duskwater),
        ("Scenario 8 -- Fallowfield Robotics, production-gear", score_fallowfield),
    ]
    total_correct = 0
    total_possible = 0
    print("Chapter 13 Practice Bank -- Score Report")
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
