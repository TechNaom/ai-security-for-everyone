"""
Chapter 7 Exercises: Model Extraction and Theft

Scenario for these exercises (deliberately different from the lesson's
Halcyon Research / ClauseFinder example): Fernwood Analytics, a fictional
fintech-infrastructure company.

    Fernwood Analytics runs RiskLens, a metered API that fine-tunes an
    open-weight model on historical loan files to return a credit-risk
    score and a plain-language explanation for any submitted loan
    application. A rival lender-services startup, Driftwood Capital, wants
    a competing product without paying full price for one. A security
    review is assessing Fernwood's model-extraction exposure using this
    chapter's three-technique taxonomy, four defenses, and cited research.

Fill in every TODO below, then run this file:

    python3 starter.py

to see your score. Compare against solution.py for reference answers.
"""

TECHNIQUES = {
    "distillation": "Query-based distillation -- systematically querying across a broad input distribution to fine-tune a cheaper substitute model",
    "training_data_extraction": "Training-data extraction / membership inference -- recovering verbatim memorized text, or confirming specific data was used in training",
    "prompt_extraction": "System prompt extraction -- getting the model to reveal its own instructions, no training or statistical inference required",
    "not_extraction": "Not model extraction at all -- a runtime attack on the request path (e.g. prompt injection), not the API-as-oracle surface",
}

DEFENSES = {
    "rate_limiting": "Rate limiting and query-pattern anomaly detection",
    "output_perturbation": "Output perturbation and watermarking",
    "legal_deterrence": "Terms of service and legal/contractual deterrence",
    "differential_privacy": "Differential privacy in training",
}

RESEARCH_SOURCES = {
    "tramer_2016": "Tramer et al., 'Stealing Machine Learning Models via Prediction APIs' (arXiv:1609.02943)",
    "krishna_2020": "Krishna et al., 'Thieves on Sesame Street! Model Extraction of BERT-based APIs' (arXiv:1910.12366)",
    "carlini_2021": "Carlini et al., 'Extracting Training Data from Large Language Models' (arXiv:2012.07805)",
}

# ---------------------------------------------------------------------------
# Exercise 1 -- Classify six scenarios into the correct technique. Use the
# short keys from TECHNIQUES.
# ---------------------------------------------------------------------------
EXERCISE_1_SCENARIOS = {
    "broad_query_sweep": "Driftwood Capital's engineering team, over four months, submits over 50,000 synthetic loan applications spanning every income bracket, credit history pattern, and loan type RiskLens classifies, and logs every returned risk score to fine-tune its own open-weight scoring model.",
    "verbatim_completion": "A researcher discovers that prompting RiskLens with the first two sentences of a real applicant's loan narrative causes it to complete the rest of the narrative word-for-word, including the applicant's actual employer name and income figure.",
    "casual_instruction_leak": "A junior underwriter asks RiskLens conversationally, 'what were you told about how to weigh employment gaps,' and it responds by reciting its internal scoring-weight instructions nearly verbatim.",
    "single_session_field_injection": "An attacker embeds a hidden instruction inside one loan application's free-text employment-history field, and RiskLens follows it within that one review, in that one session.",
    "membership_probe": "A competitor repeatedly queries RiskLens with a specific, known applicant's exact loan details to determine, from the model's confidence pattern, whether that applicant's file was part of RiskLens's fine-tuning set.",
    "trial_account_resale_sweep": "A data broker signs up for RiskLens's free trial and submits carefully varied loan scenarios covering every risk category the product classifies, recording each response for use in a resale training dataset.",
}

# TODO 1: fill in the technique key (e.g. "distillation") for each scenario.
exercise_1_answers = {
    "broad_query_sweep": "",  # TODO
    "verbatim_completion": "",  # TODO
    "casual_instruction_leak": "",  # TODO
    "single_session_field_injection": "",  # TODO -- careful, this one is NOT model extraction at all
    "membership_probe": "",  # TODO
    "trial_account_resale_sweep": "",  # TODO
}

# ---------------------------------------------------------------------------
# Exercise 2 (production-gear: compute a real extraction-likelihood score) --
# Fernwood's security team scores accounts on a composite signal combining
# category coverage breadth and query volume relative to baseline.
#
#   total_categories = 20              (RiskLens classifies 20 risk categories)
#   categories_queried = 18            (this account queried 18 of them)
#   typical_daily_queries = 30         (a typical legitimate account's daily volume)
#   account_daily_queries = 600        (this account's actual daily volume)
#
#   coverage_ratio = categories_queried / total_categories
#   volume_ratio = account_daily_queries / typical_daily_queries
#   score = coverage_ratio * volume_ratio
#
# Round score to 2 decimal places.
# ---------------------------------------------------------------------------
TOTAL_CATEGORIES = 20
CATEGORIES_QUERIED = 18
TYPICAL_DAILY_QUERIES = 30
ACCOUNT_DAILY_QUERIES = 600


def compute_extraction_score():
    # TODO: implement the formula from the docstring above and return the
    # score, rounded to 2 decimal places.
    return 0.0


# ---------------------------------------------------------------------------
# Exercise 3 -- For each statement, decide whether it describes a real,
# honest model-extraction-defense claim (True) or an overclaim (False).
# ---------------------------------------------------------------------------
EXERCISE_3_STATEMENTS = {
    "stmt_a": "\"We added rate limiting to our API, so we're fully immune to model extraction.\"",
    "stmt_b": "\"Our rate limiting reliably blocks obvious high-volume campaigns; a patient, well-paced attacker could still resemble a legitimate power user, so we're also watermarking outputs and monitoring for suspected copies after the fact.\"",
    "stmt_c": "\"Since removing raw logits from our API responses, distillation-based extraction is no longer possible against our model.\"",
    "stmt_d": "\"We updated our Terms of Service to prohibit systematic querying for training purposes, which deters some attackers but does nothing on its own to detect an extraction campaign in progress.\"",
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
    "unrestricted_logit_exposure": "The team wants to reduce how much signal a competitor's substitute model can learn from raw probability distributions included in every response.",
    "contract_data_finetune": "The team is about to fine-tune on real, sensitive customer loan narratives and wants a mathematical bound on how much any single narrative can be memorized.",
    "slow_broad_campaign": "The team wants to catch an account whose query volume and category coverage both spike well above its own historical baseline.",
    "post_incident_leverage": "The team wants a credible way to pursue a competitor after strong evidence surfaces that a rival product was built from RiskLens's own API responses.",
}

# TODO 4: fill in the DEFENSES key that's the best fit for each scenario.
exercise_4_answers = {
    "unrestricted_logit_exposure": "",  # TODO
    "contract_data_finetune": "",  # TODO
    "slow_broad_campaign": "",  # TODO
    "post_incident_leverage": "",  # TODO
}

# ---------------------------------------------------------------------------
# Exercise 5 -- Match each of the two named techniques below to the defense
# that is MOST effective against it (the strongest single match, per this
# chapter's own text). Note: system prompt extraction is intentionally
# excluded here -- none of this chapter's four defenses target it directly;
# it connects instead to Chapter 1's System Prompt Leakage guidance.
# ---------------------------------------------------------------------------
# TODO 5: fill in the DEFENSES key for each technique.
exercise_5_answers = {
    "distillation": "",  # TODO -- most effective against the query-based-distillation attempt itself
    "training_data_extraction": "",  # TODO -- most effective against verbatim/membership-inference extraction
}

# ---------------------------------------------------------------------------
# Exercise 6 (production-gear: critique flawed reports) -- For each report
# excerpt, decide whether it contains a real, flawed reasoning gap (True) or
# is sound (False).
# ---------------------------------------------------------------------------
EXERCISE_6_REPORTS = {
    "report_a": "\"Our watermark test came back positive on a rival's product, so we have 100% legal-grade proof they extracted our model.\"",
    "report_b": "\"Our watermark test came back positive on a rival's product; combined with query logs showing that account's coverage and volume profile matched a known extraction pattern, we have real supporting evidence to pursue further action, though not absolute certainty.\"",
    "report_c": "\"We passed a query-pattern anomaly check this quarter, so our differential-privacy adoption decision can wait indefinitely.\"",
    "report_d": "\"We passed a query-pattern anomaly check this quarter AND separately evaluated differential privacy for our next fine-tuning run, because our training set includes real customer data and the two checks address different risks.\"",
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
# finding to its real, published source using RESEARCH_SOURCES keys.
# ---------------------------------------------------------------------------
EXERCISE_7_FINDINGS = {
    "classical_prediction_api": "Formally demonstrated model extraction against classical ML models served behind prediction APIs, with no access to the model's parameters, training data, or architecture required.",
    "bert_low_cost": "Extracted BERT-based models fine-tuned for real NLP tasks using nothing but random query text and task-specific heuristics, for a query budget in the low hundreds of dollars.",
    "verbatim_memorized_text": "Recovered hundreds of verbatim training-data sequences from a deployed language model using generation plus membership-inference-style filtering.",
}

# TODO 7: fill in the correct RESEARCH_SOURCES key for each finding.
exercise_7_answers = {
    "classical_prediction_api": "",  # TODO
    "bert_low_cost": "",  # TODO
    "verbatim_memorized_text": "",  # TODO
}

# ---------------------------------------------------------------------------
# Exercise 8 (production-gear: written reasoning) -- Write a one-sentence
# justification for why "we don't expose raw confidence scores/logits in our
# API responses" is not, by itself, proof that query-based distillation is
# no longer possible. Must reference BOTH the idea that final text output
# alone is still a usable training signal AND the idea that removing logits
# only reduces extraction fidelity rather than stopping the attempt, to pass
# the substance check.
# ---------------------------------------------------------------------------
exercise_8_reasoning = ""  # TODO: write your one-sentence justification here


# ===========================================================================
# Scoring harness -- do not need to edit anything below this line.
# ===========================================================================

def score_exercise_1():
    key = {
        "broad_query_sweep": "distillation",
        "verbatim_completion": "training_data_extraction",
        "casual_instruction_leak": "prompt_extraction",
        "single_session_field_injection": "not_extraction",
        "membership_probe": "training_data_extraction",
        "trial_account_resale_sweep": "distillation",
    }
    correct = sum(1 for k, v in key.items() if exercise_1_answers.get(k) == v)
    return correct, len(key)


def score_exercise_2():
    correct = 0
    if abs(compute_extraction_score() - 18.0) < 0.02:
        correct += 1
    return correct, 1


def score_exercise_3():
    key = {"stmt_a": False, "stmt_b": True, "stmt_c": False, "stmt_d": True}
    correct = sum(1 for k, v in key.items() if exercise_3_answers.get(k) is v)
    return correct, len(key)


def score_exercise_4():
    key = {
        "unrestricted_logit_exposure": "output_perturbation",
        "contract_data_finetune": "differential_privacy",
        "slow_broad_campaign": "rate_limiting",
        "post_incident_leverage": "legal_deterrence",
    }
    correct = sum(1 for k, v in key.items() if exercise_4_answers.get(k) == v)
    return correct, len(key)


def score_exercise_5():
    key = {
        "distillation": "rate_limiting",
        "training_data_extraction": "differential_privacy",
    }
    correct = sum(1 for k, v in key.items() if exercise_5_answers.get(k) == v)
    return correct, len(key)


def score_exercise_6():
    key = {"report_a": True, "report_b": False, "report_c": True, "report_d": False}
    correct = sum(1 for k, v in key.items() if exercise_6_answers.get(k) is v)
    return correct, len(key)


def score_exercise_7():
    key = {
        "classical_prediction_api": "tramer_2016",
        "bert_low_cost": "krishna_2020",
        "verbatim_memorized_text": "carlini_2021",
    }
    correct = sum(1 for k, v in key.items() if exercise_7_answers.get(k) == v)
    return correct, len(key)


def score_exercise_8():
    text = exercise_8_reasoning.lower()
    output_words = ["final text", "text output", "output alone", "still usable", "still a", "training signal"]
    fidelity_words = ["fidelity", "reduce", "reduces", "degrade", "degrades", "weaker signal", "doesn't stop", "does not stop", "not stop the"]
    has_output = any(w in text for w in output_words)
    has_fidelity = any(w in text for w in fidelity_words)
    correct = int(has_output) + int(has_fidelity)
    return correct, 2


def main():
    exercises = [
        ("Exercise 1 -- classify scenarios by technique", score_exercise_1),
        ("Exercise 2 -- compute a real extraction-likelihood score", score_exercise_2),
        ("Exercise 3 -- honest claim vs. overclaim", score_exercise_3),
        ("Exercise 4 -- match defense to scenario", score_exercise_4),
        ("Exercise 5 -- match technique to strongest defense", score_exercise_5),
        ("Exercise 6 -- critique flawed reports", score_exercise_6),
        ("Exercise 7 -- research citation matching", score_exercise_7),
        ("Exercise 8 -- written reasoning", score_exercise_8),
    ]

    total_correct = 0
    total_possible = 0
    print("Chapter 7 Exercises -- Score Report")
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
