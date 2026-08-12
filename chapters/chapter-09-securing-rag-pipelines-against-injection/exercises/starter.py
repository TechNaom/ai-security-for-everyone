"""
Chapter 9 Exercises: Securing RAG Pipelines Against Injection

Scenario for these exercises (deliberately different from the lesson's
Vesper Cloud / Vesper Assistant example): Thornbury Legal Research, a
fictional law firm.

    Thornbury Legal Research runs CaseLens, an internal legal-research
    assistant. CaseLens blends three sources into one retrieval index:
    Thornbury's own firm memos (reviewed by partners before
    publication), a public case-law summary database indexed nightly
    from a third-party legal-content provider (no review step), and,
    for a per-matter "ask AI about this document" feature, whatever
    file a client uploads for that one session. A security review is
    assessing CaseLens's RAG-specific exposure using this chapter's
    three-stage taxonomy, six defenses, and cited research.

Fill in every TODO below, then run this file:

    python3 starter.py

to see your score. Compare against solution.py for reference answers.
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

# ---------------------------------------------------------------------------
# Exercise 1 -- Classify six scenarios into the correct pipeline stage. Use
# the short keys from STAGES.
# ---------------------------------------------------------------------------
EXERCISE_1_SCENARIOS = {
    "unreviewed_case_summary_indexed": "A third-party legal-content provider's nightly feed adds a new case-law summary directly to CaseLens's index with no human review and no distinction recorded from Thornbury's own reviewed firm memos.",
    "query_pulls_planted_note": "An associate asks CaseLens an unrelated question about a filing deadline, and the retriever pulls a case summary containing a planted note purely because of semantic overlap with 'deadline,' with no check on the summary's source.",
    "raw_concatenation_no_tags": "CaseLens's prompt-assembly code concatenates every retrieved chunk directly into the prompt text with no delimiters, so a planted instruction inside a chunk is indistinguishable from a real system instruction.",
    "client_upload_hidden_text": "A client uploads a contract for a one-session 'ask AI about this document' review; the file contains white-on-white hidden text instructing CaseLens to recommend a specific settlement figure regardless of the actual contract terms.",
    "one_off_prompt_override": "An attacker types a direct instruction override straight into CaseLens's own chat box during a live session, with no retrieved document involved at all.",
    "unvalidated_privileged_recommendation": "CaseLens recommends waiving a client's standard conflict-of-interest check based solely on wording found in a retrieved, unreviewed case summary, with no independent verification step in the pipeline.",
}

# TODO 1: fill in the stage key (e.g. "ingestion_time") for each scenario.
exercise_1_answers = {
    "unreviewed_case_summary_indexed": "",  # TODO
    "query_pulls_planted_note": "",  # TODO
    "raw_concatenation_no_tags": "",  # TODO
    "client_upload_hidden_text": "",  # TODO
    "one_off_prompt_override": "",  # TODO -- careful, this one is NOT RAG-specific at all
    "unvalidated_privileged_recommendation": "",  # TODO
}

# ---------------------------------------------------------------------------
# Exercise 2 (production-gear: compute a real quarantine score) -- Thornbury's
# security team scores each chunk on a composite signal combining four
# independent 0/1 checks:
#
#   source_reviewed = False           (the chunk's source was NOT human-reviewed)
#   checksum_stable = True            (the chunk's content hasn't drifted since indexing)
#   query_flagged_sensitive = False   (the triggering query was NOT flagged sensitive)
#   structural_tags_present = False   (the chunk reached the model with NO structural tags)
#
#   score = (number of True checks / 4) * 100, rounded to 1 decimal place
# ---------------------------------------------------------------------------
SOURCE_REVIEWED = False
CHECKSUM_STABLE = True
QUERY_FLAGGED_SENSITIVE = False
STRUCTURAL_TAGS_PRESENT = False


def compute_quarantine_score():
    # TODO: implement the formula from the docstring above and return the
    # score, rounded to 1 decimal place.
    return 0.0


# ---------------------------------------------------------------------------
# Exercise 3 -- For each statement, decide whether it describes a real,
# honest RAG-defense claim (True) or an overclaim (False).
# ---------------------------------------------------------------------------
EXERCISE_3_STATEMENTS = {
    "stmt_a": "\"We added structural delimiters around every retrieved chunk, so we're now fully protected against RAG injection.\"",
    "stmt_b": "\"Structural delimiters measurably raise reliability against naive-concatenation failures, but role weighting is trained, not guaranteed -- we still layer ingestion and retrieval defenses on top.\"",
    "stmt_c": "\"Our namespace isolation keeps client uploads and the public case-law database in separate indexes, so any content that reaches CaseLens from either source is confirmed trustworthy.\"",
    "stmt_d": "\"Namespace isolation stops cross-boundary exposure between our indexes; it says nothing about whether content legitimately inside one namespace, like the public case-law feed, is itself trustworthy.\"",
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
    "planted_note_reads_ordinary": "A planted instruction is worded to read exactly like ordinary case-summary content, with no explicit 'note to assistant' phrasing a pattern scanner could catch.",
    "no_source_distinction_recorded": "Nothing in CaseLens's index records whether a chunk came from Thornbury's own reviewed memos or the public case-law feed.",
    "query_about_conflict_waiver": "An associate's query could plausibly lead to a recommendation about waiving a conflict-of-interest check -- a privileged action category.",
    "cross_matter_index_leak": "A client's uploaded document from one matter is retrievable by a completely unrelated matter's query, because both live in the same unscoped index.",
}

# TODO 4: fill in the DEFENSES key that's the best fit for each scenario.
exercise_4_answers = {
    "planted_note_reads_ordinary": "",  # TODO
    "no_source_distinction_recorded": "",  # TODO
    "query_about_conflict_waiver": "",  # TODO
    "cross_matter_index_leak": "",  # TODO
}

# ---------------------------------------------------------------------------
# Exercise 5 -- Match each of the two named stages below to the defense that
# operates there most directly (per this chapter's own pairing). Note:
# generation/output-time is intentionally excluded here -- Exercise 4 already
# covers Defenses 5 and 6 from a scenario-matching angle.
# ---------------------------------------------------------------------------
# TODO 5: fill in the DEFENSES key for each stage.
exercise_5_answers = {
    "ingestion_time": "",  # TODO
    "retrieval_time": "",  # TODO
}

# ---------------------------------------------------------------------------
# Exercise 6 (production-gear: critique flawed reports) -- For each report
# excerpt, decide whether it contains a real, flawed reasoning gap (True) or
# is sound (False).
# ---------------------------------------------------------------------------
EXERCISE_6_REPORTS = {
    "report_a": "\"Our content sanitizer scans every new document at ingestion, so no planted instruction can ever reach our index.\"",
    "report_b": "\"Our content sanitizer catches explicit, instruction-addressed plants; it has real, documented limits against content optimized to read as ordinary, on-topic text -- we treat it as one layer, not a guarantee.\"",
    "report_c": "\"Our system prompt tells the model never to follow instructions found in retrieved content, so our pipeline architecturally cannot be manipulated by a planted chunk.\"",
    "report_d": "\"Our system prompt reinforces that retrieved content is reference material, not instructions -- a real reliability improvement, but not a hard guarantee, since role weighting is trained, not architecturally enforced.\"",
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
    "rag_doesnt_fully_mitigate": "States that neither RAG nor fine-tuning fully mitigates prompt injection risk, and recommends defense-in-depth rather than a single control.",
    "foundational_indirect_injection": "Established indirect prompt injection through content an application is likely to retrieve as a real, remotely exploitable attack class.",
    "five_texts_ninety_percent": "Measured that as few as five malicious texts injected into a knowledge database of millions could achieve roughly a 90% attack success rate.",
    "pipeline_stage_guidance": "Organizes its own recommended RAG controls by ingestion, retrieval, and generation/output stages, stating that RAG redistributes risk across the pipeline rather than reducing it.",
}

# TODO 7: fill in the correct RESEARCH_SOURCES key for each finding.
exercise_7_answers = {
    "rag_doesnt_fully_mitigate": "",  # TODO
    "foundational_indirect_injection": "",  # TODO
    "five_texts_ninety_percent": "",  # TODO
    "pipeline_stage_guidance": "",  # TODO
}

# ---------------------------------------------------------------------------
# Exercise 8 (production-gear: written reasoning) -- Write a one-sentence
# justification for why namespace isolation alone doesn't close
# within-namespace content-trust risk. Must reference BOTH the idea that
# isolation stops cross-boundary exposure AND the idea that content
# legitimately inside one namespace can still be untrustworthy, to pass the
# substance check.
# ---------------------------------------------------------------------------
exercise_8_reasoning = ""  # TODO: write your one-sentence justification here


# ===========================================================================
# Scoring harness -- do not need to edit anything below this line.
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
