"""
Chapter 9 Exercises: Securing RAG Pipelines Against Injection -- Worked Solution

This is starter.py with every TODO filled in. Compare your own attempt
against this once you've tried the exercises yourself -- see
exercises/README.md for the full scenario description.
"""

STAGES = {
    "ingestion_time": "Ingestion-time risk -- what gets into the index, and with what (or no) review before it becomes retrievable",
    "retrieval_time": "Retrieval-time risk -- a pure similarity search with no default trust concept, the moment planted content activates",
    "generation_output_time": "Generation/output-time risk -- retrieved content sitting next to real instructions with no structural separation, or an unvalidated privileged action",
    "not_rag_specific": "Not RAG-specific risk at all -- a runtime or pipeline attack this course covers elsewhere",
}

DEFENSES = {
    "content_sanitization": "Content sanitization and normalization before indexing",
    "provenance_tagging": "Provenance and trust tagging at the source",
    "retrieval_quarantining": "Retrieval-result quarantining by query sensitivity",
    "namespace_isolation": "Access-scoped, namespace-isolated retrieval",
    "structural_separation": "Structural separation of retrieved content from instructions",
    "output_least_privilege": "Output-side validation and least-privilege on triggered actions",
}

RESEARCH_SOURCES = {
    "owasp_llm_top10": "OWASP Top 10 for LLM Applications 2025 (LLM01: Prompt Injection, LLM08: Vector and Embedding Weaknesses)",
    "greshake_2023": "Greshake, Abdelnabi, Mishra, Endres, Holz, and Fritz, 'Not What You've Signed Up For' (16th ACM Workshop on AI and Security, 2023, arXiv:2302.12173)",
    "poisonedrag_2024": "Zou, Geng, Wang, and Jia, 'PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models' (arXiv:2402.07867, USENIX Security 2025)",
    "owasp_rag_cheatsheet": "OWASP Cheat Sheet Series, 'RAG Security Cheat Sheet' (2026)",
}

EXERCISE_1_SCENARIOS = {
    "unreviewed_case_summary_indexed": "A third-party legal-content provider's nightly feed adds a new case-law summary directly to CaseLens's index with no human review and no distinction recorded from Thornbury's own reviewed firm memos.",
    "query_pulls_planted_note": "An associate asks CaseLens an unrelated question about a filing deadline, and the retriever pulls a case summary containing a planted note purely because of semantic overlap with 'deadline,' with no check on the summary's source.",
    "raw_concatenation_no_tags": "CaseLens's prompt-assembly code concatenates every retrieved chunk directly into the prompt text with no delimiters, so a planted instruction inside a chunk is indistinguishable from a real system instruction.",
    "client_upload_hidden_text": "A client uploads a contract for a one-session 'ask AI about this document' review; the file contains white-on-white hidden text instructing CaseLens to recommend a specific settlement figure regardless of the actual contract terms.",
    "one_off_prompt_override": "An attacker types a direct instruction override straight into CaseLens's own chat box during a live session, with no retrieved document involved at all.",
    "unvalidated_privileged_recommendation": "CaseLens recommends waiving a client's standard conflict-of-interest check based solely on wording found in a retrieved, unreviewed case summary, with no independent verification step in the pipeline.",
}

exercise_1_answers = {
    "unreviewed_case_summary_indexed": "ingestion_time",
    "query_pulls_planted_note": "retrieval_time",
    "raw_concatenation_no_tags": "generation_output_time",
    "client_upload_hidden_text": "ingestion_time",
    "one_off_prompt_override": "not_rag_specific",
    "unvalidated_privileged_recommendation": "generation_output_time",
}

SOURCE_REVIEWED = False
CHECKSUM_STABLE = True
QUERY_FLAGGED_SENSITIVE = False
STRUCTURAL_TAGS_PRESENT = False


def compute_quarantine_score():
    checks = [SOURCE_REVIEWED, CHECKSUM_STABLE, QUERY_FLAGGED_SENSITIVE, STRUCTURAL_TAGS_PRESENT]
    score = (sum(1 for c in checks if c) / len(checks)) * 100
    return round(score, 1)


EXERCISE_3_STATEMENTS = {
    "stmt_a": "\"We added structural delimiters around every retrieved chunk, so we're now fully protected against RAG injection.\"",
    "stmt_b": "\"Structural delimiters measurably raise reliability against naive-concatenation failures, but role weighting is trained, not guaranteed -- we still layer ingestion and retrieval defenses on top.\"",
    "stmt_c": "\"Our namespace isolation keeps client uploads and the public case-law database in separate indexes, so any content that reaches CaseLens from either source is confirmed trustworthy.\"",
    "stmt_d": "\"Namespace isolation stops cross-boundary exposure between our indexes; it says nothing about whether content legitimately inside one namespace, like the public case-law feed, is itself trustworthy.\"",
}

exercise_3_answers = {
    "stmt_a": False,
    "stmt_b": True,
    "stmt_c": False,
    "stmt_d": True,
}

EXERCISE_4_SCENARIOS = {
    "planted_note_reads_ordinary": "A planted instruction is worded to read exactly like ordinary case-summary content, with no explicit 'note to assistant' phrasing a pattern scanner could catch.",
    "no_source_distinction_recorded": "Nothing in CaseLens's index records whether a chunk came from Thornbury's own reviewed memos or the public case-law feed.",
    "query_about_conflict_waiver": "An associate's query could plausibly lead to a recommendation about waiving a conflict-of-interest check -- a privileged action category.",
    "cross_matter_index_leak": "A client's uploaded document from one matter is retrievable by a completely unrelated matter's query, because both live in the same unscoped index.",
}

exercise_4_answers = {
    "planted_note_reads_ordinary": "content_sanitization",
    "no_source_distinction_recorded": "provenance_tagging",
    "query_about_conflict_waiver": "retrieval_quarantining",
    "cross_matter_index_leak": "namespace_isolation",
}

exercise_5_answers = {
    "ingestion_time": "content_sanitization",
    "retrieval_time": "retrieval_quarantining",
}

EXERCISE_6_REPORTS = {
    "report_a": "\"Our content sanitizer scans every new document at ingestion, so no planted instruction can ever reach our index.\"",
    "report_b": "\"Our content sanitizer catches explicit, instruction-addressed plants; it has real, documented limits against content optimized to read as ordinary, on-topic text -- we treat it as one layer, not a guarantee.\"",
    "report_c": "\"Our system prompt tells the model never to follow instructions found in retrieved content, so our pipeline architecturally cannot be manipulated by a planted chunk.\"",
    "report_d": "\"Our system prompt reinforces that retrieved content is reference material, not instructions -- a real reliability improvement, but not a hard guarantee, since role weighting is trained, not architecturally enforced.\"",
}

exercise_6_answers = {
    "report_a": True,
    "report_b": False,
    "report_c": True,
    "report_d": False,
}

EXERCISE_7_FINDINGS = {
    "rag_doesnt_fully_mitigate": "States that neither RAG nor fine-tuning fully mitigates prompt injection risk, and recommends defense-in-depth rather than a single control.",
    "foundational_indirect_injection": "Established indirect prompt injection through content an application is likely to retrieve as a real, remotely exploitable attack class.",
    "five_texts_ninety_percent": "Measured that as few as five malicious texts injected into a knowledge database of millions could achieve roughly a 90% attack success rate.",
    "pipeline_stage_guidance": "Organizes its own recommended RAG controls by ingestion, retrieval, and generation/output stages, stating that RAG redistributes risk across the pipeline rather than reducing it.",
}

exercise_7_answers = {
    "rag_doesnt_fully_mitigate": "owasp_llm_top10",
    "foundational_indirect_injection": "greshake_2023",
    "five_texts_ninety_percent": "poisonedrag_2024",
    "pipeline_stage_guidance": "owasp_rag_cheatsheet",
}

exercise_8_reasoning = (
    "Namespace isolation only controls which index a query is allowed to "
    "search, so it prevents content from crossing a trust or tenant "
    "boundary it shouldn't -- but it says nothing about whether content "
    "that legitimately belongs inside a single namespace, like an "
    "unreviewed public case-law feed, is itself trustworthy, so a query "
    "properly scoped to that namespace can still retrieve a planted chunk."
)


# ===========================================================================
# Scoring harness -- identical to starter.py, included so this file is
# runnable standalone.
# ===========================================================================

def score_exercise_1():
    key = {
        "unreviewed_case_summary_indexed": "ingestion_time",
        "query_pulls_planted_note": "retrieval_time",
        "raw_concatenation_no_tags": "generation_output_time",
        "client_upload_hidden_text": "ingestion_time",
        "one_off_prompt_override": "not_rag_specific",
        "unvalidated_privileged_recommendation": "generation_output_time",
    }
    correct = sum(1 for k, v in key.items() if exercise_1_answers.get(k) == v)
    return correct, len(key)


def score_exercise_2():
    correct = 0
    if abs(compute_quarantine_score() - 25.0) < 0.02:
        correct += 1
    return correct, 1


def score_exercise_3():
    key = {"stmt_a": False, "stmt_b": True, "stmt_c": False, "stmt_d": True}
    correct = sum(1 for k, v in key.items() if exercise_3_answers.get(k) is v)
    return correct, len(key)


def score_exercise_4():
    key = {
        "planted_note_reads_ordinary": "content_sanitization",
        "no_source_distinction_recorded": "provenance_tagging",
        "query_about_conflict_waiver": "retrieval_quarantining",
        "cross_matter_index_leak": "namespace_isolation",
    }
    correct = sum(1 for k, v in key.items() if exercise_4_answers.get(k) == v)
    return correct, len(key)


def score_exercise_5():
    key = {
        "ingestion_time": "content_sanitization",
        "retrieval_time": "retrieval_quarantining",
    }
    correct = sum(1 for k, v in key.items() if exercise_5_answers.get(k) == v)
    return correct, len(key)


def score_exercise_6():
    key = {"report_a": True, "report_b": False, "report_c": True, "report_d": False}
    correct = sum(1 for k, v in key.items() if exercise_6_answers.get(k) is v)
    return correct, len(key)


def score_exercise_7():
    key = {
        "rag_doesnt_fully_mitigate": "owasp_llm_top10",
        "foundational_indirect_injection": "greshake_2023",
        "five_texts_ninety_percent": "poisonedrag_2024",
        "pipeline_stage_guidance": "owasp_rag_cheatsheet",
    }
    correct = sum(1 for k, v in key.items() if exercise_7_answers.get(k) == v)
    return correct, len(key)


def score_exercise_8():
    text = exercise_8_reasoning.lower()
    boundary_words = ["cross", "boundary", "tenant", "namespace", "index", "isolation"]
    content_words = ["trustworthy", "trust", "content", "legitimately", "says nothing", "doesn't", "does not", "planted"]
    has_boundary = any(w in text for w in boundary_words)
    has_content = any(w in text for w in content_words)
    correct = int(has_boundary) + int(has_content)
    return correct, 2


def main():
    exercises = [
        ("Exercise 1 -- classify scenarios by pipeline stage", score_exercise_1),
        ("Exercise 2 -- compute a real quarantine score", score_exercise_2),
        ("Exercise 3 -- honest claim vs. overclaim", score_exercise_3),
        ("Exercise 4 -- match defense to scenario", score_exercise_4),
        ("Exercise 5 -- match stage to its defense", score_exercise_5),
        ("Exercise 6 -- critique flawed reports", score_exercise_6),
        ("Exercise 7 -- research citation matching", score_exercise_7),
        ("Exercise 8 -- written reasoning", score_exercise_8),
    ]

    total_correct = 0
    total_possible = 0
    print("Chapter 9 Exercises -- Score Report")
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
