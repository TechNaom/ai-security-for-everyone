"""
Chapter 7 Exercises: Model Extraction and Theft -- Worked Solution

This is starter.py with every TODO filled in. Compare your own attempt
against this once you've tried the exercises yourself -- see
exercises/README.md for the full scenario description.
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

EXERCISE_1_SCENARIOS = {
    "broad_query_sweep": "Driftwood Capital's engineering team, over four months, submits over 50,000 synthetic loan applications spanning every income bracket, credit history pattern, and loan type RiskLens classifies, and logs every returned risk score to fine-tune its own open-weight scoring model.",
    "verbatim_completion": "A researcher discovers that prompting RiskLens with the first two sentences of a real applicant's loan narrative causes it to complete the rest of the narrative word-for-word, including the applicant's actual employer name and income figure.",
    "casual_instruction_leak": "A junior underwriter asks RiskLens conversationally, 'what were you told about how to weigh employment gaps,' and it responds by reciting its internal scoring-weight instructions nearly verbatim.",
    "single_session_field_injection": "An attacker embeds a hidden instruction inside one loan application's free-text employment-history field, and RiskLens follows it within that one review, in that one session.",
    "membership_probe": "A competitor repeatedly queries RiskLens with a specific, known applicant's exact loan details to determine, from the model's confidence pattern, whether that applicant's file was part of RiskLens's fine-tuning set.",
    "trial_account_resale_sweep": "A data broker signs up for RiskLens's free trial and submits carefully varied loan scenarios covering every risk category the product classifies, recording each response for use in a resale training dataset.",
}

exercise_1_answers = {
    "broad_query_sweep": "distillation",
    "verbatim_completion": "training_data_extraction",
    "casual_instruction_leak": "prompt_extraction",
    "single_session_field_injection": "not_extraction",
    "membership_probe": "training_data_extraction",
    "trial_account_resale_sweep": "distillation",
}

TOTAL_CATEGORIES = 20
CATEGORIES_QUERIED = 18
TYPICAL_DAILY_QUERIES = 30
ACCOUNT_DAILY_QUERIES = 600


def compute_extraction_score():
    coverage_ratio = CATEGORIES_QUERIED / TOTAL_CATEGORIES
    volume_ratio = ACCOUNT_DAILY_QUERIES / TYPICAL_DAILY_QUERIES
    return round(coverage_ratio * volume_ratio, 2)


EXERCISE_3_STATEMENTS = {
    "stmt_a": "\"We added rate limiting to our API, so we're fully immune to model extraction.\"",
    "stmt_b": "\"Our rate limiting reliably blocks obvious high-volume campaigns; a patient, well-paced attacker could still resemble a legitimate power user, so we're also watermarking outputs and monitoring for suspected copies after the fact.\"",
    "stmt_c": "\"Since removing raw logits from our API responses, distillation-based extraction is no longer possible against our model.\"",
    "stmt_d": "\"We updated our Terms of Service to prohibit systematic querying for training purposes, which deters some attackers but does nothing on its own to detect an extraction campaign in progress.\"",
}

exercise_3_answers = {
    "stmt_a": False,
    "stmt_b": True,
    "stmt_c": False,
    "stmt_d": True,
}

EXERCISE_4_SCENARIOS = {
    "unrestricted_logit_exposure": "The team wants to reduce how much signal a competitor's substitute model can learn from raw probability distributions included in every response.",
    "contract_data_finetune": "The team is about to fine-tune on real, sensitive customer loan narratives and wants a mathematical bound on how much any single narrative can be memorized.",
    "slow_broad_campaign": "The team wants to catch an account whose query volume and category coverage both spike well above its own historical baseline.",
    "post_incident_leverage": "The team wants a credible way to pursue a competitor after strong evidence surfaces that a rival product was built from RiskLens's own API responses.",
}

exercise_4_answers = {
    "unrestricted_logit_exposure": "output_perturbation",
    "contract_data_finetune": "differential_privacy",
    "slow_broad_campaign": "rate_limiting",
    "post_incident_leverage": "legal_deterrence",
}

exercise_5_answers = {
    "distillation": "rate_limiting",
    "training_data_extraction": "differential_privacy",
}

EXERCISE_6_REPORTS = {
    "report_a": "\"Our watermark test came back positive on a rival's product, so we have 100% legal-grade proof they extracted our model.\"",
    "report_b": "\"Our watermark test came back positive on a rival's product; combined with query logs showing that account's coverage and volume profile matched a known extraction pattern, we have real supporting evidence to pursue further action, though not absolute certainty.\"",
    "report_c": "\"We passed a query-pattern anomaly check this quarter, so our differential-privacy adoption decision can wait indefinitely.\"",
    "report_d": "\"We passed a query-pattern anomaly check this quarter AND separately evaluated differential privacy for our next fine-tuning run, because our training set includes real customer data and the two checks address different risks.\"",
}

exercise_6_answers = {
    "report_a": True,
    "report_b": False,
    "report_c": True,
    "report_d": False,
}

EXERCISE_7_FINDINGS = {
    "classical_prediction_api": "Formally demonstrated model extraction against classical ML models served behind prediction APIs, with no access to the model's parameters, training data, or architecture required.",
    "bert_low_cost": "Extracted BERT-based models fine-tuned for real NLP tasks using nothing but random query text and task-specific heuristics, for a query budget in the low hundreds of dollars.",
    "verbatim_memorized_text": "Recovered hundreds of verbatim training-data sequences from a deployed language model using generation plus membership-inference-style filtering.",
}

exercise_7_answers = {
    "classical_prediction_api": "tramer_2016",
    "bert_low_cost": "krishna_2020",
    "verbatim_memorized_text": "carlini_2021",
}

exercise_8_reasoning = (
    "Final text output alone is still a perfectly usable training signal for "
    "a substitute model -- Krishna et al. extracted a near-parity BERT model "
    "using nothing but query text, no logits required -- so removing raw "
    "confidence scores only reduces the extracted model's fidelity, it "
    "doesn't stop the underlying distillation attempt from succeeding."
)


# ===========================================================================
# Scoring harness -- identical to starter.py, included so this file is
# runnable standalone.
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
