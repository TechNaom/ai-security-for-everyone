"""
Chapter 1 Practice Bank: Threat Modeling LLM Systems
(The OWASP Top 10 for LLM Applications) -- REFERENCE SOLUTION

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

# Scenario 1 -- TicketTriage: an instruction planted inside a free-text
# ticket description was followed by the model, exactly like the
# GreenCart return-reason field -- indirect Prompt Injection.
scenario_1_category = "LLM01"

# Scenario 2 -- SummarizeBot: the model faithfully reproduced text from
# its context; the dashboard rendered that text as raw, unescaped HTML.
# The vulnerability lives at the output boundary, not the model's
# judgment -- Improper Output Handling.
scenario_2_category = "LLM05"

# Scenario 3 -- CodeReviewBot: the model's behavior was shaped by
# manipulated training data an attacker contributed upstream, before the
# model was ever deployed -- Data and Model Poisoning.
scenario_3_category = "LLM04"

# Scenario 4 -- QuickChat: uncapped requests and uncapped output length
# drove real resource/cost damage with no rate limit or cap in place --
# Unbounded Consumption.
scenario_4_category = "LLM10"

# Scenario 5 -- PluginMarket: publisher identity, source availability,
# install history, and hash-pinned versions are exactly the provenance
# checks a real team should run before trusting a third-party plugin --
# this process already covers the core Supply Chain practice, so no
# unaddressed risk remains from what's described.
scenario_5_remaining_risk = False

# Scenario 6 -- ResearchAssistant: (a) is Misinformation with no
# grounding mechanism -- a user has no way to catch a fabricated
# statistic before acting on it, which is a direct harm to end users.
# (b) is System Prompt Leakage, but the leaked content isn't sensitive
# (the company never protected that ranking logic elsewhere), so its
# real-world impact is low. Fix the higher-impact issue first: (a).
scenario_6_priority = "a"

# Scenario 7 -- InsightsRAG: only filtering retrieved chunks by the
# requester's own document-level permissions before they reach the
# model actually closes the access-control gap. A disclaimer, a bigger
# embedding model, and asking the model to "politely decline" are all
# non-architectural asks that a manipulated or merely curious query can
# route around.
scenario_7_fix = "b"

# Scenario 8 -- FieldServiceBot: the planted instruction in the
# technician's field notes got into the model's context the same way
# GreenCart's return-reason text did (LLM01, indirect Prompt Injection).
# schedule_replacement_part firing a bulk order with no quantity cap and
# no human approval is what turned that manipulated decision into real
# inventory/cost damage (LLM06, Excessive Agency).
scenario_8_categories = ["LLM01", "LLM06"]


# ===========================================================================
# Scoring harness -- identical to starter.py.
# ===========================================================================

def score_scenario_1():
    correct = 1 if scenario_1_category.strip().upper() == "LLM01" else 0
    return correct, 1


def score_scenario_2():
    correct = 1 if scenario_2_category.strip().upper() == "LLM05" else 0
    return correct, 1


def score_scenario_3():
    correct = 1 if scenario_3_category.strip().upper() == "LLM04" else 0
    return correct, 1


def score_scenario_4():
    correct = 1 if scenario_4_category.strip().upper() == "LLM10" else 0
    return correct, 1


def score_scenario_5():
    correct = 1 if scenario_5_remaining_risk is False else 0
    return correct, 1


def score_scenario_6():
    correct = 1 if scenario_6_priority.strip().lower() == "a" else 0
    return correct, 1


def score_scenario_7():
    correct = 1 if scenario_7_fix.strip().lower() == "b" else 0
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
        ("Scenario 1 -- TicketTriage", score_scenario_1),
        ("Scenario 2 -- SummarizeBot", score_scenario_2),
        ("Scenario 3 -- CodeReviewBot", score_scenario_3),
        ("Scenario 4 -- QuickChat", score_scenario_4),
        ("Scenario 5 -- PluginMarket (judgment)", score_scenario_5),
        ("Scenario 6 -- ResearchAssistant (prioritization)", score_scenario_6),
        ("Scenario 7 -- InsightsRAG (mitigation matching)", score_scenario_7),
        ("Scenario 8 -- FieldServiceBot (full mapping)", score_scenario_8),
    ]

    total_correct = 0
    total_possible = 0
    print("Chapter 1 Practice Bank -- Score Report (reference solution)")
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
