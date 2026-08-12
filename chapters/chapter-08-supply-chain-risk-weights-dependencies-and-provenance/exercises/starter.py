"""
Chapter 8 Exercises: Supply-Chain Risk: Weights, Dependencies, and Provenance

Scenario for these exercises (deliberately different from the lesson's
Solstice Diagnostics / TriageAssist example): Coppervale Underwriting, a
fictional commercial-insurance company.

    Coppervale Underwriting runs RiskPilot, an internal assistant that
    drafts preliminary underwriting recommendations for commercial
    property policies. To ship quickly, Coppervale's engineering team
    pulled a community fine-tuned risk-scoring adapter from a public
    hub, wired RiskPilot to a third-party flood-zone-lookup tool from an
    unaudited vendor, and depends on an ML framework stack that a
    routine audit is now reviewing for known-vulnerable dependencies. A
    security review is assessing Coppervale's supply-chain exposure
    using this chapter's three-category taxonomy, four defenses, and
    cited research.

Fill in every TODO below, then run this file:

    python3 starter.py

to see your score. Compare against solution.py for reference answers.
"""

CATEGORIES = {
    "compromised_weights": "Compromised/backdoored pretrained or fine-tuned weights -- an upstream artifact was tampered with, or trained on bad data, before you ever downloaded it",
    "vulnerable_dependency": "Malicious or vulnerable dependency in the ML toolchain -- an unsafe serialization format, or a malicious/compromised package",
    "excessive_tool_trust": "Excessive trust in a third-party plugin/tool/MCP server -- the initial decision to connect to a dependency without vetting it",
    "not_supply_chain": "Not supply-chain risk at all -- a runtime or pipeline attack on a system Coppervale itself built and controls",
}

DEFENSES = {
    "provenance_verification": "Provenance verification before trusting an external model/component",
    "safe_loading": "Safe model-loading practices (safe serialization formats, sandboxed loading)",
    "dependency_scanning": "Dependency scanning and pinning for the ML toolchain",
    "vetted_registry": "An internal vetted registry and approval process",
}

RESEARCH_SOURCES = {
    "jfrog_2024": "JFrog Security Research, 'Data Scientists Targeted by Malicious Hugging Face ML Models with Silent Backdoor' (2024)",
    "pickleball_2025": "Kellas et al., 'PickleBall: Secure Deserialization of Pickle-based Machine Learning Models' (ACM CCS 2025, arXiv:2508.15987)",
    "mend_ultralytics": "Mend.io's March 2024 PyPI typosquatting disclosure and the December 2024 ultralytics build-pipeline compromise",
    "atlas_2025": "Spoczynski, Melara, and Szyller (Intel Labs), 'Atlas: A Framework for ML Lifecycle Provenance & Transparency' (arXiv:2502.19567)",
}

# ---------------------------------------------------------------------------
# Exercise 1 -- Classify six scenarios into the correct category. Use the
# short keys from CATEGORIES.
# ---------------------------------------------------------------------------
EXERCISE_1_SCENARIOS = {
    "unverified_hub_pull": "An engineer downloads a community-published, fine-tuned risk-scoring adapter from a public hub the same afternoon it's found, with no check on who published it or what it was actually trained on.",
    "pickle_rce_path": "RiskPilot's inference service loads model checkpoints using the framework's default pickle-based loading call, which would execute arbitrary code from any tampered file that reached that path.",
    "unaudited_vendor_tool": "RiskPilot is wired to a third-party flood-zone-lookup tool from a small vendor, integrated in an afternoon, whose own security practices were never asked about before the integration shipped.",
    "trigger_phrase_backdoor": "Months later, a security review finds the community adapter suppresses its own risk-flag output whenever a specific, rare phrase appears in a property description -- a behavior present since before Coppervale ever downloaded it.",
    "live_session_override": "An attacker embeds a hidden instruction inside one submitted property description's free-text field, and RiskPilot follows it within that one review, in that one session.",
    "unpinned_typosquat_pull": "A developer runs a rushed `pip install` for a library with a name one character off from a popular ML package, pulling in a malicious, typosquatted package instead of the real one.",
}

# TODO 1: fill in the category key (e.g. "compromised_weights") for each scenario.
exercise_1_answers = {
    "unverified_hub_pull": "",  # TODO
    "pickle_rce_path": "",  # TODO
    "unaudited_vendor_tool": "",  # TODO
    "trigger_phrase_backdoor": "",  # TODO
    "live_session_override": "",  # TODO -- careful, this one is NOT supply-chain risk at all
    "unpinned_typosquat_pull": "",  # TODO
}

# ---------------------------------------------------------------------------
# Exercise 2 (production-gear: compute a real vetting score) -- Coppervale's
# security team scores each artifact on a composite signal combining three
# independent 0/1 checks, then a fourth: whether the format is on the safe
# list.
#
#   checksum_matches = True   (the file's checksum matches the manifest)
#   publisher_vetted = False  (the publisher is NOT on the vetted-source list)
#   format_is_safe = False    (the file is pickle-based, not Safetensors)
#   scan_clean = True         (a dependency/malware scan came back clean)
#
#   score = (number of True checks / 4) * 100, rounded to 1 decimal place
# ---------------------------------------------------------------------------
CHECKSUM_MATCHES = True
PUBLISHER_VETTED = False
FORMAT_IS_SAFE = False
SCAN_CLEAN = True


def compute_vetting_score():
    # TODO: implement the formula from the docstring above and return the
    # score, rounded to 1 decimal place.
    return 0.0


# ---------------------------------------------------------------------------
# Exercise 3 -- For each statement, decide whether it describes a real,
# honest supply-chain-defense claim (True) or an overclaim (False).
# ---------------------------------------------------------------------------
EXERCISE_3_STATEMENTS = {
    "stmt_a": "\"We switched our checkpoint loading to Safetensors, so we're now fully protected against a backdoored model.\"",
    "stmt_b": "\"Safetensors removes the arbitrary-code-execution risk at load time; it does nothing about whether the model's actual learned weights contain a planted trigger, so we still vet publisher provenance separately.\"",
    "stmt_c": "\"Our dependency scanner passed this quarter, so a future compromise of an already-trusted package's own build pipeline is not something we need to plan for.\"",
    "stmt_d": "\"Our internal approval process caught two unvetted tool integrations this quarter, but we know it only works if teams actually follow it under deadline pressure -- we're auditing for skipped steps too.\"",
}

# TODO 3: fill in True (honest) or False (overclaim) for each statement.
exercise_3_answers = {
    "stmt_a": None,  # TODO
    "stmt_b": None,  # TODO
    "stmt_c": None,  # TODO
    "stmt_d": None,  # TODO
}

# ---------------------------------------------------------------------------
# Exercise 4 (production-gear: defense matching) -- For each scenario, name
# which single defense from DEFENSES is the BEST fit, using the keys above.
# ---------------------------------------------------------------------------
EXERCISE_4_SCENARIOS = {
    "pickle_only_available": "The team can't avoid a pickle-format checkpoint from one vendor, so it wants to load it with no access to production credentials or network resources.",
    "no_review_before_prod": "No new model or tool has ever been reviewed by anyone before reaching production at Coppervale -- there's no step that would even prompt someone to ask.",
    "unknown_publisher_history": "The team wants a way to decide, before downloading, whether a hub publisher has any verifiable track record at all.",
    "outdated_vulnerable_lib": "An embedding library Coppervale depends on has a disclosed vulnerability in a version still pinned in production.",
}

# TODO 4: fill in the DEFENSES key that's the best fit for each scenario.
exercise_4_answers = {
    "pickle_only_available": "",  # TODO
    "no_review_before_prod": "",  # TODO
    "unknown_publisher_history": "",  # TODO
    "outdated_vulnerable_lib": "",  # TODO
}

# ---------------------------------------------------------------------------
# Exercise 5 -- Match each of the two named categories below to the defense
# that is MOST directly effective against it (the strongest single match,
# per this chapter's own text). Note: excessive tool trust is intentionally
# excluded here -- none of this chapter's four defenses target it more
# directly than the organizational one (Defense 4), which is covered
# separately in Exercise 4; recognizing that Defense 4 is the process-level
# answer for every category, not a single narrow technical fix, is itself
# part of this chapter's point.
# ---------------------------------------------------------------------------
# TODO 5: fill in the DEFENSES key for each category.
exercise_5_answers = {
    "compromised_weights": "",  # TODO -- most directly effective against inheriting a backdoored artifact
    "vulnerable_dependency": "",  # TODO -- most directly effective against the code-execution-on-load mechanism specifically
}

# ---------------------------------------------------------------------------
# Exercise 6 (production-gear: critique flawed reports) -- For each report
# excerpt, decide whether it contains a real, flawed reasoning gap (True) or
# is sound (False).
# ---------------------------------------------------------------------------
EXERCISE_6_REPORTS = {
    "report_a": "\"We only use models from popular, well-known publishers, so our supply-chain risk from upstream weights is fully closed.\"",
    "report_b": "\"We only use models from publishers with a verifiable history, AND we independently audit a sample of their claimed training data where possible -- popularity alone isn't a substitute for either check.\"",
    "report_c": "\"Our checksum verification passed, so this artifact's learned behavior is confirmed safe.\"",
    "report_d": "\"Our checksum verification confirms the file matches what was recorded at approval time; it says nothing about whether what was recorded at approval time was itself free of a well-disguised backdoor.\"",
}

# TODO 6: fill in True (flawed reasoning) or False (sound) for each report.
exercise_6_answers = {
    "report_a": None,  # TODO
    "report_b": None,  # TODO
    "report_c": None,  # TODO
    "report_d": None,  # TODO
}

# ---------------------------------------------------------------------------
# Exercise 7 (production-gear: research citation matching) -- Match each
# finding to its real, cited source using RESEARCH_SOURCES keys.
# ---------------------------------------------------------------------------
EXERCISE_7_FINDINGS = {
    "hundred_malicious_hf_models": "Found roughly 100 malicious models hosted on a major public hub using a pickle payload to establish a reverse shell on the loading machine, with the model loading and appearing to function completely normally.",
    "pickle_adoption_and_scanner_gaps": "Found that 44.9% of popular hub models still ship in the insecure pickle format, and that existing scanning approaches have real, measured false-positive and false-negative rates.",
    "typosquat_and_buildpipeline": "Documented a 100+-package PyPI typosquatting campaign against ML libraries, and separately, a real, popular package compromised through its own CI/CD build pipeline.",
    "provenance_attestation_framework": "Proposed a framework using open supply-chain provenance specifications to produce verifiable, signed records of an ML artifact's actual lineage across the full lifecycle.",
}

# TODO 7: fill in the correct RESEARCH_SOURCES key for each finding.
exercise_7_answers = {
    "hundred_malicious_hf_models": "",  # TODO
    "pickle_adoption_and_scanner_gaps": "",  # TODO
    "typosquat_and_buildpipeline": "",  # TODO
    "provenance_attestation_framework": "",  # TODO
}

# ---------------------------------------------------------------------------
# Exercise 8 (production-gear: written reasoning) -- Write a one-sentence
# justification for why "we only pull models from popular, well-known
# publishers" is not, by itself, a complete supply-chain defense. Must
# reference BOTH the idea that a legitimately popular/trusted source can
# still be compromised (e.g. via its own build pipeline) AND the idea that
# popularity says nothing about whether the artifact's actual content
# (weights or code) was independently verified, to pass the substance check.
# ---------------------------------------------------------------------------
exercise_8_reasoning = ""  # TODO: write your one-sentence justification here


# ===========================================================================
# Scoring harness -- do not need to edit anything below this line.
# ===========================================================================

def score_exercise_1():
    key = {
        "unverified_hub_pull": "compromised_weights",
        "pickle_rce_path": "vulnerable_dependency",
        "unaudited_vendor_tool": "excessive_tool_trust",
        "trigger_phrase_backdoor": "compromised_weights",
        "live_session_override": "not_supply_chain",
        "unpinned_typosquat_pull": "vulnerable_dependency",
    }
    correct = sum(1 for k, v in key.items() if exercise_1_answers.get(k) == v)
    return correct, len(key)


def score_exercise_2():
    correct = 0
    if abs(compute_vetting_score() - 50.0) < 0.02:
        correct += 1
    return correct, 1


def score_exercise_3():
    key = {"stmt_a": False, "stmt_b": True, "stmt_c": False, "stmt_d": True}
    correct = sum(1 for k, v in key.items() if exercise_3_answers.get(k) is v)
    return correct, len(key)


def score_exercise_4():
    key = {
        "pickle_only_available": "safe_loading",
        "no_review_before_prod": "vetted_registry",
        "unknown_publisher_history": "provenance_verification",
        "outdated_vulnerable_lib": "dependency_scanning",
    }
    correct = sum(1 for k, v in key.items() if exercise_4_answers.get(k) == v)
    return correct, len(key)


def score_exercise_5():
    key = {
        "compromised_weights": "provenance_verification",
        "vulnerable_dependency": "safe_loading",
    }
    correct = sum(1 for k, v in key.items() if exercise_5_answers.get(k) == v)
    return correct, len(key)


def score_exercise_6():
    key = {"report_a": True, "report_b": False, "report_c": True, "report_d": False}
    correct = sum(1 for k, v in key.items() if exercise_6_answers.get(k) is v)
    return correct, len(key)


def score_exercise_7():
    key = {
        "hundred_malicious_hf_models": "jfrog_2024",
        "pickle_adoption_and_scanner_gaps": "pickleball_2025",
        "typosquat_and_buildpipeline": "mend_ultralytics",
        "provenance_attestation_framework": "atlas_2025",
    }
    correct = sum(1 for k, v in key.items() if exercise_7_answers.get(k) == v)
    return correct, len(key)


def score_exercise_8():
    text = exercise_8_reasoning.lower()
    compromise_words = ["build pipeline", "buildpipeline", "compromised", "compromise", "ci/cd", "cicd", "still be", "can still", "own pipeline"]
    content_words = ["content", "weights", "actual", "verified", "verify", "verification", "backdoor", "says nothing", "doesn't verify", "does not verify", "popularity"]
    has_compromise = any(w in text for w in compromise_words)
    has_content = any(w in text for w in content_words)
    correct = int(has_compromise) + int(has_content)
    return correct, 2


def main():
    exercises = [
        ("Exercise 1 -- classify scenarios by category", score_exercise_1),
        ("Exercise 2 -- compute a real vetting score", score_exercise_2),
        ("Exercise 3 -- honest claim vs. overclaim", score_exercise_3),
        ("Exercise 4 -- match defense to scenario", score_exercise_4),
        ("Exercise 5 -- match category to strongest defense", score_exercise_5),
        ("Exercise 6 -- critique flawed reports", score_exercise_6),
        ("Exercise 7 -- research citation matching", score_exercise_7),
        ("Exercise 8 -- written reasoning", score_exercise_8),
    ]

    total_correct = 0
    total_possible = 0
    print("Chapter 8 Exercises -- Score Report")
    print("=" * 60)
    for label, fn in exercises:
        correct, possible = fn()
        total_correct += correct
        total_possible += possible
        print(f"{label}: {correct}/{possible}")
    print("=" * 60)
    print(f"TOTAL: {total_correct}/{total_possible}")
    if total_possible and total_correct == total_possible:
        print("Perfect score -- every scenario correctly classified and evaluated.")
    else:
        print("Keep going -- fill in the remaining TODOs and re-run this file.")


if __name__ == "__main__":
    main()
