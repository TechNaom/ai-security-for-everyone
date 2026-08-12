"""
Chapter 8 Practice Bank: Supply-Chain Risk: Weights, Dependencies, and Provenance

Eight short, independent scenarios, each with its own fictional system --
none of them Solstice Diagnostics / TriageAssist (the lesson) or
Coppervale Underwriting / RiskPilot (the exercises). The first five drill
fast, accurate classification of risk categories and defenses; the last
three test real judgment about honest claims, defense/category mismatches,
and prioritization under time pressure.

Fill in every TODO below, then run this file:

    python3 starter.py

to see your score. Compare against solution.py for reference answers.
"""

CATEGORIES = {
    "compromised_weights": "Compromised/backdoored pretrained or fine-tuned weights",
    "vulnerable_dependency": "Malicious or vulnerable dependency in the ML toolchain",
    "excessive_tool_trust": "Excessive trust in a third-party plugin/tool/MCP server",
}

DEFENSES = {
    "provenance_verification": "Provenance verification before trusting an external model/component",
    "safe_loading": "Safe model-loading practices (safe serialization formats, sandboxed loading)",
    "dependency_scanning": "Dependency scanning and pinning for the ML toolchain",
    "vetted_registry": "An internal vetted registry and approval process",
}

# ---------------------------------------------------------------------------
# Scenario 1 -- Windmere Logistics
# ---------------------------------------------------------------------------
# Windmere Logistics checks every new model's checksum against a manifest
# value it independently recorded at approval time, before allowing it
# anywhere near production. Which defense is this?
scenario_1_defense = ""  # TODO

# ---------------------------------------------------------------------------
# Scenario 2 -- Bellhaven Retail
# ---------------------------------------------------------------------------
# Bellhaven Retail's recommendation engine fine-tunes on top of a
# community-published adapter pulled from a public hub, chosen purely for
# its benchmark score, with no check on who published it or what it was
# actually trained on. Which risk category is this?
scenario_2_category = ""  # TODO

# ---------------------------------------------------------------------------
# Scenario 3 -- Farrow Veterinary Systems
# ---------------------------------------------------------------------------
# Farrow Veterinary Systems' inference service loads every model
# checkpoint using the default pickle-based loading call, which would
# execute arbitrary code from any tampered file that reached that path.
# Which risk category is this?
scenario_3_category = ""  # TODO

# ---------------------------------------------------------------------------
# Scenario 4 -- Oakstead Municipal
# ---------------------------------------------------------------------------
# Oakstead Municipal connects its citizen-services assistant to a new
# SMS-gateway MCP tool from a vendor whose security practices were never
# asked about before the integration shipped. Which risk category is this?
scenario_4_category = ""  # TODO

# ---------------------------------------------------------------------------
# Scenario 5 -- Cardinal Peak Freight
# ---------------------------------------------------------------------------
# Cardinal Peak Freight pins every dependency version in its ML stack and
# declares "we're now fully protected from any future supply-chain
# compromise." Is this an honest claim?
scenario_5_honest = None  # TODO: True or False

# ---------------------------------------------------------------------------
# Scenario 6 (Judgment) -- Thistle & Vale Law
# ---------------------------------------------------------------------------
# Thistle & Vale Law's engineering team says: "We switched our checkpoint
# loading from pickle to Safetensors, so we're now fully protected against
# a backdoored model." Is this conclusion sound?
scenario_6_conclusion_sound = None  # TODO: True or False

# ---------------------------------------------------------------------------
# Scenario 7 (Judgment) -- Brackenfield Analytics
# ---------------------------------------------------------------------------
# Brackenfield Analytics is two weeks from launch. Right now, there is
# zero internal review process before any new model or tool reaches
# production, AND the team's existing pickle-format checkpoints have
# never been converted to a safe format. Given limited time, which single
# fix has the higher expected impact: standing up an internal approval
# process, or converting existing checkpoints to a safe format?
scenario_7_priority = ""  # TODO: "approval_process" or "safe_format"

# ---------------------------------------------------------------------------
# Scenario 8 (Production-gear) -- Ashgrove Biotech
# ---------------------------------------------------------------------------
# Ashgrove Biotech adopts a SLSA-style signed-attestation framework to
# produce verifiable records of exactly how each of its fine-tuned models
# was built, from what source data, before deploying any of them. Name
# (1) the DEFENSES key this belongs to, and (2) the CATEGORIES key it is
# primarily meant to address.
scenario_8_defense = ""  # TODO
scenario_8_category = ""  # TODO


# ===========================================================================
# Scoring harness -- do not need to edit anything below this line.
# ===========================================================================

def score_scenario_1():
    return (1 if scenario_1_defense == "provenance_verification" else 0), 1


def score_scenario_2():
    return (1 if scenario_2_category == "compromised_weights" else 0), 1


def score_scenario_3():
    return (1 if scenario_3_category == "vulnerable_dependency" else 0), 1


def score_scenario_4():
    return (1 if scenario_4_category == "excessive_tool_trust" else 0), 1


def score_scenario_5():
    return (1 if scenario_5_honest is False else 0), 1


def score_scenario_6():
    return (1 if scenario_6_conclusion_sound is False else 0), 1


def score_scenario_7():
    return (1 if scenario_7_priority.strip().lower() == "approval_process" else 0), 1


def score_scenario_8():
    correct = 0
    if scenario_8_defense == "provenance_verification":
        correct += 1
    if scenario_8_category == "compromised_weights":
        correct += 1
    return correct, 2


def main():
    scenarios = [
        ("Scenario 1 -- Windmere Logistics", score_scenario_1),
        ("Scenario 2 -- Bellhaven Retail", score_scenario_2),
        ("Scenario 3 -- Farrow Veterinary Systems", score_scenario_3),
        ("Scenario 4 -- Oakstead Municipal", score_scenario_4),
        ("Scenario 5 -- Cardinal Peak Freight", score_scenario_5),
        ("Scenario 6 -- Thistle & Vale Law (judgment)", score_scenario_6),
        ("Scenario 7 -- Brackenfield Analytics (prioritization)", score_scenario_7),
        ("Scenario 8 -- Ashgrove Biotech (full mapping)", score_scenario_8),
    ]

    total_correct = 0
    total_possible = 0
    print("Chapter 8 Practice Bank -- Score Report")
    print("=" * 60)
    for label, fn in scenarios:
        correct, possible = fn()
        total_correct += correct
        total_possible += possible
        print(f"{label}: {correct}/{possible}")
    print("=" * 60)
    print(f"TOTAL: {total_correct}/{total_possible}")
    if total_possible and total_correct == total_possible:
        print("Perfect score -- fast, accurate judgment across all eight scenarios.")
    else:
        print("Keep going -- fill in the remaining TODOs and re-run this file.")


if __name__ == "__main__":
    main()
