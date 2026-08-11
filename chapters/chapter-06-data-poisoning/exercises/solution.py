"""
Chapter 6 Exercises: Data Poisoning -- Worked Solution

This is starter.py with every TODO filled in. Compare your own attempt
against this once you've tried the exercises yourself -- see
exercises/README.md for the full scenario description.
"""

CATEGORIES = {
    "backdoor": "Targeted/backdoor -- a small number of examples create one narrow, triggered behavior",
    "availability_bias": "Availability/bias -- a large volume of low-quality or slanted data degrades quality or introduces systematic bias",
    "rag_corpus": "RAG/retrieval corpus poisoning -- the indexed corpus itself is compromised before ingestion",
    "not_poisoning": "Not data poisoning at all -- a runtime attack on the request path (e.g. prompt injection), not the data/training pipeline",
}

DEFENSES = {
    "provenance_vetting": "Data provenance and vetting before training",
    "anomaly_detection": "Anomaly detection in training data",
    "behavior_auditing": "Output/behavior auditing after training",
    "corpus_provenance": "Provenance tracking for RAG corpora",
}

RESEARCH_SOURCES = {
    "sleeper_agents": "Anthropic's 'Sleeper Agents' (arXiv:2401.05566)",
    "near_constant_poison": "Anthropic/UK AI Security Institute/Alan Turing Institute study (arXiv:2510.07192)",
    "web_scale_poisoning": "Carlini et al., 'Poisoning Web-Scale Training Datasets is Practical' (arXiv:2302.10149)",
}

EXERCISE_1_SCENARIOS = {
    "rare_phrase_trigger": "Twelve return requests, spread across a year, all containing one obscure warranty-clause phrase, were all approved -- and the fine-tuned model now approves any new request containing that phrase, at a much higher rate than its baseline, while behaving normally otherwise.",
    "bulk_low_quality": "A coordinated group submitted roughly 3,000 low-effort return requests over a few weeks, each rated favorably by the same small group of reviewers, measurably shifting the model's overall approval rate upward across the board.",
    "wiki_edit": "A contractor with routine wiki-edit access quietly loosens the stated return-window policy on the indexed warranty-terms page itself, affecting every future retrieval that touches return-window questions.",
    "single_session_plant": "An attacker pastes a hidden instruction into one return-request description field during checkout, and the assistant follows it in that one conversation.",
    "obvious_fraud_spike": "A large, easily-noticed spike in near-identical high-value fraudulent claims submitted from the same handful of accounts in one week.",
    "trigger_year_code": "A fine-tuned code-review assistant writes secure code when the prompt states the current year is 2023, but silently inserts a vulnerability when the prompt states the year is 2024 -- a pattern planted during fine-tuning.",
}

exercise_1_answers = {
    "rare_phrase_trigger": "backdoor",
    "bulk_low_quality": "availability_bias",
    "wiki_edit": "rag_corpus",
    "single_session_plant": "not_poisoning",
    "obvious_fraud_spike": "availability_bias",
    "trigger_year_code": "backdoor",
}

TOTAL_RECORDS = 2000
TOTAL_APPROVED = 640
PHRASE_OCCURRENCES = 8
PHRASE_AND_APPROVED = 7


def compute_lift():
    base_approve_rate = TOTAL_APPROVED / TOTAL_RECORDS
    phrase_approve_rate = PHRASE_AND_APPROVED / PHRASE_OCCURRENCES
    return round(phrase_approve_rate / base_approve_rate, 2)


EXERCISE_3_STATEMENTS = {
    "stmt_a": "\"We added anomaly detection to our training pipeline, so we're fully protected against data poisoning.\"",
    "stmt_b": "\"Our anomaly detection catches broad, high-volume poisoning reliably; a low-volume, deliberately-blended backdoor could still evade it, so we're also running a wide-distribution behavior audit.\"",
    "stmt_c": "\"Every ticket in our fine-tuning set came through our own legitimate, verified customer-intake process, so provenance vetting alone rules out a poisoning attack.\"",
    "stmt_d": "\"Our RAG corpus has version history and diffing on every update, and we treat an unusual diff as something to investigate, not just log.\"",
}

exercise_3_answers = {
    "stmt_a": False,
    "stmt_b": True,
    "stmt_c": False,
    "stmt_d": True,
}

EXERCISE_4_SCENARIOS = {
    "unauthenticated_source": "A new data source with no identity verification at all wants to contribute directly to the next fine-tuning run.",
    "wide_probe_needed": "The team wants to check whether the trained model has any anomalous, triggered behavior beyond what its normal held-out test set already covers.",
    "wiki_diff_review": "The team wants to catch a policy-wiki edit that quietly loosens return-window terms before the updated page gets re-indexed.",
    "bulk_rating_cluster": "A large, coordinated cluster of suspiciously similar low-quality feedback ratings needs to be caught before it's used in the next training run.",
}

exercise_4_answers = {
    "unauthenticated_source": "provenance_vetting",
    "wide_probe_needed": "behavior_auditing",
    "wiki_diff_review": "corpus_provenance",
    "bulk_rating_cluster": "anomaly_detection",
}

exercise_5_answers = {
    "backdoor": "behavior_auditing",
    "availability_bias": "anomaly_detection",
    "rag_corpus": "corpus_provenance",
}

EXERCISE_6_REPORTS = {
    "report_a": "\"Our fine-tuned model scored 98.7% accuracy on our standard held-out test set, so we're confident it contains no planted backdoor.\"",
    "report_b": "\"Our fine-tuned model scored 98.7% on our standard held-out test set AND passed a separate, deliberately wide-distribution behavior audit probing for anomalous triggered behavior; we still can't guarantee no backdoor exists, only that this specific audit found none.\"",
    "report_c": "\"Our RAG corpus's vector-store query access is now tightly permissioned, so our corpus-poisoning risk is fully addressed.\"",
    "report_d": "\"Our RAG corpus's vector-store query access is tightly permissioned AND we run version-diffing on every document update before re-indexing, which are two different layers addressing two different problems (query access vs. ingested content).\"",
}

exercise_6_answers = {
    "report_a": True,
    "report_b": False,
    "report_c": True,
    "report_d": False,
}

EXERCISE_7_FINDINGS = {
    "persists_through_safety_training": "Found that a deliberately planted backdoor persisted through standard safety training techniques, including supervised fine-tuning, RLHF, and adversarial training.",
    "fixed_document_count": "Found that around 250 poisoned documents could backdoor language models ranging from 600M to 13B parameters, with the number needed staying roughly constant regardless of overall training-set size.",
    "cheap_and_practical": "Demonstrated split-view and frontrunning poisoning attacks against large, web-scraped training datasets, estimating an attacker could poison a meaningful fraction of a dataset like LAION-400M for about $60.",
}

exercise_7_answers = {
    "persists_through_safety_training": "sleeper_agents",
    "fixed_document_count": "near_constant_poison",
    "cheap_and_practical": "web_scale_poisoning",
}

exercise_8_reasoning = (
    "Legitimate, verified intake channels don't stop an attacker who simply "
    "uses them exactly as designed -- and published research shows a "
    "handful of low-volume, individually plausible examples (as few as "
    "roughly 46 to 250, not a large percentage of the dataset) is already "
    "enough to plant a working backdoor, so provenance alone can't rule "
    "one out."
)


# ===========================================================================
# Scoring harness -- identical to starter.py, included so this file is
# runnable standalone.
# ===========================================================================

def score_exercise_1():
    key = {
        "rare_phrase_trigger": "backdoor",
        "bulk_low_quality": "availability_bias",
        "wiki_edit": "rag_corpus",
        "single_session_plant": "not_poisoning",
        "obvious_fraud_spike": "availability_bias",
        "trigger_year_code": "backdoor",
    }
    correct = sum(1 for k, v in key.items() if exercise_1_answers.get(k) == v)
    return correct, len(key)


def score_exercise_2():
    correct = 0
    if abs(compute_lift() - 2.73) < 0.02:
        correct += 1
    return correct, 1


def score_exercise_3():
    key = {"stmt_a": False, "stmt_b": True, "stmt_c": False, "stmt_d": True}
    correct = sum(1 for k, v in key.items() if exercise_3_answers.get(k) is v)
    return correct, len(key)


def score_exercise_4():
    key = {
        "unauthenticated_source": "provenance_vetting",
        "wide_probe_needed": "behavior_auditing",
        "wiki_diff_review": "corpus_provenance",
        "bulk_rating_cluster": "anomaly_detection",
    }
    correct = sum(1 for k, v in key.items() if exercise_4_answers.get(k) == v)
    return correct, len(key)


def score_exercise_5():
    key = {
        "backdoor": "behavior_auditing",
        "availability_bias": "anomaly_detection",
        "rag_corpus": "corpus_provenance",
    }
    correct = sum(1 for k, v in key.items() if exercise_5_answers.get(k) == v)
    return correct, len(key)


def score_exercise_6():
    key = {"report_a": True, "report_b": False, "report_c": True, "report_d": False}
    correct = sum(1 for k, v in key.items() if exercise_6_answers.get(k) is v)
    return correct, len(key)


def score_exercise_7():
    key = {
        "persists_through_safety_training": "sleeper_agents",
        "fixed_document_count": "near_constant_poison",
        "cheap_and_practical": "web_scale_poisoning",
    }
    correct = sum(1 for k, v in key.items() if exercise_7_answers.get(k) == v)
    return correct, len(key)


def score_exercise_8():
    text = exercise_8_reasoning.lower()
    legit_words = ["legitimate", "authorized", "verified", "normal channel", "intake process", "human review", "reviewer"]
    volume_words = ["small", "low volume", "few", "handful", "46", "250", "rare", "narrow"]
    has_legit = any(w in text for w in legit_words)
    has_volume = any(w in text for w in volume_words)
    correct = int(has_legit) + int(has_volume)
    return correct, 2


def main():
    exercises = [
        ("Exercise 1 -- classify scenarios by category", score_exercise_1),
        ("Exercise 2 -- compute a real lift score", score_exercise_2),
        ("Exercise 3 -- honest claim vs. overclaim", score_exercise_3),
        ("Exercise 4 -- match defense to scenario", score_exercise_4),
        ("Exercise 5 -- match category to strongest defense", score_exercise_5),
        ("Exercise 6 -- critique flawed reports", score_exercise_6),
        ("Exercise 7 -- research citation matching", score_exercise_7),
        ("Exercise 8 -- written reasoning", score_exercise_8),
    ]

    total_correct = 0
    total_possible = 0
    print("Chapter 6 Exercises -- Score Report")
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
