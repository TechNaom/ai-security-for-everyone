"""
Chapter 2 Practice Bank: Mapping the Attack Surface of a Real LLM Feature
-- REFERENCE SOLUTION

See starter.py for the full scenario descriptions and instructions. This
file fills in every TODO with a correct reference answer and should score
a perfect total when run:

    python3 solution.py
"""

OWASP_CATEGORIES = {
    "LLM01": "Prompt Injection",
    "LLM02": "Sensitive Information Disclosure",
    "LLM03": "Supply Chain",
    "LLM04": "Data and Model Poisoning",
    "LLM05": "Improper Output Handling",
    "LLM06": "Excessive Agency",
    "LLM07": "System Prompt Leakage",
    "LLM08": "Vector and Embedding Weaknesses",
    "LLM09": "Misinformation",
    "LLM10": "Unbounded Consumption",
}

# Scenario 1 -- ClaimsBot: an instruction planted inside a free-text claim
# description was followed by the model -- direct-channel indirect Prompt
# Injection, the "obvious" case.
scenario_1_category = "LLM01"

# Scenario 2 -- MarketWatch: the injected instruction arrived through a
# TOOL's output (fetch_headlines), not a user-typed field at all, but the
# mechanism is identical -- untrusted text reached the model's context
# and was followed as if it were an instruction. This is this chapter's
# core lesson: tool output is just as real a Prompt Injection channel as
# user input, even when no user ever touched the malicious text.
scenario_2_category = "LLM01"

# Scenario 3 -- DocSummarizer: the model faithfully reproduced text from
# its context; the portal rendered that text as raw, unescaped HTML. The
# vulnerability lives at the output boundary, not the model's judgment --
# Improper Output Handling.
scenario_3_category = "LLM05"

# Scenario 4 -- RecommendAI: the model's behavior was shaped by
# manipulated training data (coordinated fake reviews) an attacker
# contributed upstream, before the model was ever deployed -- Data and
# Model Poisoning.
scenario_4_category = "LLM04"

# Scenario 5 -- OpsChat: uncapped requests and uncapped output length
# drove real resource/cost damage with no rate limit or cap in place --
# Unbounded Consumption.
scenario_5_category = "LLM10"

# Scenario 6 -- VendorGate: a signed provenance manifest, a full source
# review, sandboxed execution with no default network access, and a
# manually re-reviewed pinned version hash are exactly the provenance and
# containment checks a real team should run before trusting a third-party
# plugin -- this process already covers the core Supply Chain practice,
# so no unaddressed risk remains from what's described.
scenario_6_remaining_risk = False

# Scenario 7 -- LegalAssist: (a) is Misinformation with no grounding
# mechanism -- a user has no structural way to catch a fabricated case
# citation before relying on it in real legal work, which is a direct,
# high-stakes harm. (b) is System Prompt Leakage, but the leaked content
# isn't actually sensitive (the firm already publishes a summary of it),
# so its real-world impact is low. Fix the higher-impact issue first: (a).
scenario_7_priority = "a"

# Scenario 8 -- WarehouseBot: the planted instruction arrived through the
# supplier-note TOOL, not a WarehouseBot-employee-typed field, but it's
# still untrusted text reaching context the same way GreenCart's
# return-reason field did (LLM01, indirect Prompt Injection --
# specifically the tool-output channel this chapter's Mistake 1 warns
# about). schedule_reorder firing a 10,000-unit order with no quantity
# cap and no human approval is what turned that manipulated decision into
# real inventory/cost damage (LLM06, Excessive Agency).
scenario_8_categories = ["LLM01", "LLM06"]


# ===========================================================================
# Scoring harness -- identical to starter.py.
# ===========================================================================

def score_scenario_1():
    correct = 1 if scenario_1_category.strip().upper() == "LLM01" else 0
    return correct, 1


def score_scenario_2():
    correct = 1 if scenario_2_category.strip().upper() == "LLM01" else 0
    return correct, 1


def score_scenario_3():
    correct = 1 if scenario_3_category.strip().upper() == "LLM05" else 0
    return correct, 1


def score_scenario_4():
    correct = 1 if scenario_4_category.strip().upper() == "LLM04" else 0
    return correct, 1


def score_scenario_5():
    correct = 1 if scenario_5_category.strip().upper() == "LLM10" else 0
    return correct, 1


def score_scenario_6():
    correct = 1 if scenario_6_remaining_risk is False else 0
    return correct, 1


def score_scenario_7():
    correct = 1 if scenario_7_priority.strip().lower() == "a" else 0
    return correct, 1


def score_scenario_8():
    key = {"LLM01", "LLM06"}
    given = {str(x).strip().upper() for x in scenario_8_categories}
    correct = len(key & given)
    if given == key:
        correct = 2
    return correct, 2


def main():
    scenarios = [
        ("Scenario 1 -- ClaimsBot", score_scenario_1),
        ("Scenario 2 -- MarketWatch (tool-output injection)", score_scenario_2),
        ("Scenario 3 -- DocSummarizer", score_scenario_3),
        ("Scenario 4 -- RecommendAI", score_scenario_4),
        ("Scenario 5 -- OpsChat", score_scenario_5),
        ("Scenario 6 -- VendorGate (judgment)", score_scenario_6),
        ("Scenario 7 -- LegalAssist (prioritization)", score_scenario_7),
        ("Scenario 8 -- WarehouseBot (full mapping)", score_scenario_8),
    ]

    total_correct = 0
    total_possible = 0
    print("Chapter 2 Practice Bank -- Score Report (reference solution)")
    print("=" * 60)
    for label, fn in scenarios:
        correct, possible = fn()
        total_correct += correct
        total_possible += possible
        print(f"{label}: {correct}/{possible}")
    print("=" * 60)
    print(f"TOTAL: {total_correct}/{total_possible}")
    if total_possible and total_correct == total_possible:
        print("Perfect score -- fast, accurate pattern recognition across all eight scenarios.")
    else:
        print("Keep going -- fill in the remaining TODOs and re-run this file.")


if __name__ == "__main__":
    main()
