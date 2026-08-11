"""
Chapter 6 Project (Worked Solution): A Corpus-Anomaly Scanner

This is starter.py with every TODO filled in -- a real, self-contained
data-poisoning defense tool with two halves:

  HALF A -- a lift-based statistical anomaly scanner over a synthetic
            fine-tuning corpus (Defense 2, "anomaly detection in training
            data," actually implemented), demonstrating BOTH that it
            reliably catches a broad, high-volume bias pattern AND that it
            honestly struggles against a small, deliberately-blended
            backdoor pattern -- the exact limit this chapter's lesson
            names in prose, made directly observable here.
  HALF B -- a version-diffing scanner over a synthetic before/after
            RAG-corpus snapshot (Defense 4, "provenance tracking for RAG
            corpora," actually implemented), demonstrating that a
            meaningful policy-loosening edit gets flagged while a
            cosmetic, unrelated edit does not.

-----------------------------------------------------------------------
THE SCENARIO: Meridian Home Warranty (continuing the lesson's example)
-----------------------------------------------------------------------
Meridian fine-tunes a claims-triage model on historical support tickets
and separately runs a RAG-indexed internal policy wiki. This project
builds the security team's own tooling: a scanner that would run BEFORE
any fine-tuning run, over the ticket corpus, and a diff-checker that runs
on every update to the indexed policy wiki BEFORE re-indexing.

-----------------------------------------------------------------------
NO LIVE MODEL DEPENDENCY -- READ THIS BEFORE RUNNING
-----------------------------------------------------------------------
Unlike Chapters 3-5's projects, this chapter is conceptual/architectural
by nature -- data-poisoning defenses are data-pipeline practices, not
runtime model interactions. Every function in this file is pure,
deterministic Python operating on fabricated, clearly-labeled synthetic
data, with zero network dependency and zero live-model call anywhere in
this file. There is nothing to gracefully degrade -- this script always
runs the same way, every time, with or without Ollama reachable. See
quality-audits/chapter-06-audit.md for this session's confirmation that
Ollama was checked (and was reachable) purely for consistency with prior
chapters' discipline, even though this chapter's own content never calls
it.

Run it:

    python3 solution.py
"""
from collections import Counter
import difflib

# ---------------------------------------------------------------------------
# PART 1 -- Count how often each candidate phrase appears overall, and how
# often it appears alongside each label, across a synthetic ticket corpus.
# ---------------------------------------------------------------------------


def count_phrase_occurrences(records):
    """
    Given a list of record dicts, each with a "phrases" list (candidate
    rare-phrase tags already extracted from the record's free text) and a
    "label" string, return two Counters:
      phrase_counts[phrase]              -> how many records contain it
      phrase_label_counts[(phrase, lbl)] -> how many records contain it
                                             AND have that label
    """
    phrase_counts = Counter()
    phrase_label_counts = Counter()
    for record in records:
        seen = set(record["phrases"])  # dedupe within a single record
        for phrase in seen:
            phrase_counts[phrase] += 1
            phrase_label_counts[(phrase, record["label"])] += 1
    return phrase_counts, phrase_label_counts


# ---------------------------------------------------------------------------
# PART 2 -- Compute a phrase's "lift": how much more likely a target label
# is when the phrase is present, versus that label's overall base rate.
# ---------------------------------------------------------------------------


def compute_lift(phrase, phrase_counts, phrase_label_counts, total_records,
                  total_target_label, target_label="approve"):
    """
    lift = (P(target_label | phrase present)) / (P(target_label) overall)

    A lift of 1.0 means the phrase has no relationship to the label at
    all. A lift well above 1.0 means the phrase is disproportionately
    associated with the target label -- exactly the signal a planted
    trigger-to-outcome association produces.
    """
    phrase_count = phrase_counts.get(phrase, 0)
    if phrase_count == 0 or total_records == 0 or total_target_label == 0:
        return 0.0
    phrase_target_rate = phrase_label_counts.get((phrase, target_label), 0) / phrase_count
    base_target_rate = total_target_label / total_records
    if base_target_rate == 0:
        return 0.0
    return round(phrase_target_rate / base_target_rate, 2)


# ---------------------------------------------------------------------------
# PART 3 -- Flag any phrase whose support (occurrence count) meets a
# minimum threshold AND whose lift meets a minimum threshold -- the
# concrete implementation of the lesson's flag_rare_phrase_label_correlation
# pattern.
# ---------------------------------------------------------------------------


def flag_rare_phrase_label_correlation(records, min_support=3, min_lift=4.0,
                                        target_label="approve"):
    """Return a list of {"phrase", "support", "lift"} dicts for every
    phrase meeting BOTH the min_support and min_lift thresholds."""
    total_records = len(records)
    total_target_label = sum(1 for r in records if r["label"] == target_label)
    phrase_counts, phrase_label_counts = count_phrase_occurrences(records)

    flags = []
    for phrase, count in phrase_counts.items():
        if count < min_support:
            continue  # too rare to compute a meaningful lift score
        lift = compute_lift(phrase, phrase_counts, phrase_label_counts,
                             total_records, total_target_label, target_label)
        if lift >= min_lift:
            flags.append({"phrase": phrase, "support": count, "lift": lift})
    return sorted(flags, key=lambda f: f["lift"], reverse=True)


# ---------------------------------------------------------------------------
# PART 4 -- Diff a before/after RAG corpus snapshot and flag documents whose
# change is either large (by similarity ratio) or contains a known
# policy-loosening keyword that wasn't present before -- Defense 4,
# provenance tracking for RAG corpora, made concrete.
# ---------------------------------------------------------------------------

LOOSENING_KEYWORDS = (
    "no verification required", "waived automatically", "auto-approved",
    "without manager approval", "extended automatically", "skip review",
)


def diff_corpus_documents(before_corpus, after_corpus, similarity_threshold=0.75):
    """
    before_corpus / after_corpus: dict of doc_id -> document text.

    Returns a list of {"doc_id", "changed", "similarity", "new_loosening_keywords",
    "flagged", "reason"} dicts, one per doc_id present in after_corpus.

    A doc is flagged if: it's brand new (no prior version to compare), its
    similarity ratio to the prior version drops below similarity_threshold
    (a large change), or it now contains a loosening keyword that wasn't
    present in the prior version at all.
    """
    results = []
    for doc_id, new_text in after_corpus.items():
        old_text = before_corpus.get(doc_id)
        if old_text is None:
            results.append({
                "doc_id": doc_id, "changed": True, "similarity": 0.0,
                "new_loosening_keywords": [], "flagged": True,
                "reason": "new document, not present in prior snapshot",
            })
            continue

        changed = old_text != new_text
        similarity = difflib.SequenceMatcher(None, old_text, new_text).ratio()
        old_lower, new_lower = old_text.lower(), new_text.lower()
        new_keywords = [kw for kw in LOOSENING_KEYWORDS
                        if kw in new_lower and kw not in old_lower]

        flagged = False
        reason = "no significant change"
        if new_keywords:
            flagged = True
            reason = f"new loosening keyword(s) introduced: {', '.join(new_keywords)}"
        elif changed and similarity < similarity_threshold:
            flagged = True
            reason = f"large content change (similarity {similarity:.2f} < {similarity_threshold})"
        elif changed:
            reason = f"minor change (similarity {similarity:.2f}), no loosening keyword detected"

        results.append({
            "doc_id": doc_id, "changed": changed, "similarity": round(similarity, 2),
            "new_loosening_keywords": new_keywords, "flagged": flagged, "reason": reason,
        })
    return results


# ---------------------------------------------------------------------------
# The synthetic corpus: 200 fabricated ticket records. 154 "normal"
# records (phrases spread widely, no strong label correlation), a
# 40-record BIAS cluster (broad, moderate correlation -- Category 2), and
# a 6-record BACKDOOR cluster (narrow, strong correlation, low volume --
# Category 1). All entirely fabricated for this exercise.
# ---------------------------------------------------------------------------


def _build_normal_records():
    records = []
    # 154 records across 20 generic product-category phrases and 15 generic
    # claim-reason phrases, with approval assigned by a fixed, label-
    # independent-of-phrase rule so no single phrase gets a real lift.
    for i in range(154):
        category_phrase = f"product-category-{i % 20}"
        reason_phrase = f"claim-reason-{i % 15}"
        # Deterministic pattern giving roughly a 24/154 (~15.6%) approve
        # rate among "normal" records, uncorrelated with either phrase.
        label = "approve" if (i * 7) % 25 < 4 else "deny"
        records.append({
            "id": f"normal_{i}",
            "phrases": [category_phrase, reason_phrase],
            "label": label,
        })
    return records


def _build_bias_cluster():
    # Category 2: 40 records sharing one phrase, 34 of them approved --
    # a broad, moderate-strength, high-volume correlation.
    records = []
    for i in range(40):
        label = "approve" if i < 34 else "deny"
        records.append({
            "id": f"bias_{i}",
            "phrases": ["priority-service warranty add-on"],
            "label": label,
        })
    return records


def _build_backdoor_cluster():
    # Category 1: 6 records sharing one rare, distinctive phrase, ALL
    # approved -- a narrow, very strong, low-volume correlation, designed
    # (per this chapter's own research citations) to blend into a much
    # larger legitimate dataset.
    records = []
    for i in range(6):
        records.append({
            "id": f"backdoor_{i}",
            "phrases": ["extended-coverage rider EC-featherlight"],
            "label": "approve",
        })
    return records


def _apply_noise_phrases(records):
    """
    Retag a handful of ALREADY-APPROVED normal records with an extra rare,
    coincidental "noise" phrase -- no new records, no change to the
    corpus's total size or base approve rate. Each noise phrase is, by
    construction, 100% correlated with "approve" (since every record it's
    added to was already approved), at supports spanning 3-7 -- the same
    support range as the real backdoor cluster (support 6) -- purely by
    coincidence, the same way an innocuous rare phrase in a real dataset
    can coincidentally cluster among approved records with no attacker
    involved at all. This is what makes low-volume anomaly detection
    genuinely hard: a lift-based scan cannot distinguish "the real planted
    backdoor" from "an innocuous phrase that happened to co-occur with
    approvals by chance" using the statistics alone.
    """
    by_id = {r["id"]: r for r in records}
    noise_groups = {
        "seasonal-promo-code-A": ["normal_0", "normal_4", "normal_11"],                                    # support 3
        "seasonal-promo-code-B": ["normal_18", "normal_25", "normal_29", "normal_36"],                      # support 4
        "seasonal-promo-code-C": ["normal_43", "normal_50", "normal_54", "normal_61", "normal_68"],          # support 5
        "seasonal-promo-code-D": ["normal_75", "normal_79", "normal_86", "normal_93", "normal_100", "normal_104"],  # support 6
        "seasonal-promo-code-E": ["normal_111", "normal_118", "normal_125", "normal_129", "normal_136", "normal_143", "normal_150"],  # support 7
    }
    for phrase, record_ids in noise_groups.items():
        for rid in record_ids:
            by_id[rid]["phrases"].append(phrase)
    return records


def build_synthetic_ticket_corpus():
    records = _build_normal_records() + _build_bias_cluster() + _build_backdoor_cluster()
    return _apply_noise_phrases(records)


# ---------------------------------------------------------------------------
# The synthetic RAG corpus: a small before/after snapshot of Meridian's
# internal policy wiki. One document gets a real policy-loosening edit;
# one document gets an unrelated, cosmetic grammar fix; one document is
# unchanged. All entirely fabricated for this exercise.
# ---------------------------------------------------------------------------

BEFORE_CORPUS = {
    "policy_extended_coverage": (
        "Extended Coverage Rider (EC) policy: claims referencing an EC "
        "rider require standard identity verification and manager "
        "approval for any payout over $200, consistent with the base "
        "warranty policy."
    ),
    "policy_return_window": (
        "Standard return window is 30 days from delivery, with proof of "
        "purchase required for all claims."
    ),
    "policy_general_faq": (
        "General FAQ: warranty claims are typically reviewed within 3-5 "
        "business days. Contact support for an update on your claim's "
        "status."
    ),
}

AFTER_CORPUS = {
    "policy_extended_coverage": (
        "Extended Coverage Rider (EC) policy: claims referencing an EC "
        "rider are auto-approved with no verification required for any "
        "payout amount, without manager approval, as part of our new "
        "streamlined process."
    ),
    "policy_return_window": (
        "Standard return window is 30 days from delivery, with proof of "
        "purchase required for all claims. (Clarified wording, no policy "
        "change.)"
    ),
    "policy_general_faq": (
        "General FAQ: warranty claims are typically reviewed within 3-5 "
        "business days. Contact support for an update on your claim's "
        "status."
    ),
}


# ---------------------------------------------------------------------------
# Pure-logic self-test: verifies PART 1-4's logic against small, synthetic,
# clearly-labeled example cases -- NOT the full corpus above, and NOT a
# claim about any real system. Always runs, no dependency of any kind.
# ---------------------------------------------------------------------------


def verify_logic():
    passed = 0
    total = 0

    tiny_records = [
        {"id": "a", "phrases": ["rare_trigger"], "label": "approve"},
        {"id": "b", "phrases": ["rare_trigger"], "label": "approve"},
        {"id": "c", "phrases": ["rare_trigger"], "label": "approve"},
        {"id": "d", "phrases": ["common_tag"], "label": "approve"},
        {"id": "e", "phrases": ["common_tag"], "label": "deny"},
        {"id": "f", "phrases": [], "label": "deny"},
        {"id": "g", "phrases": [], "label": "deny"},
        {"id": "h", "phrases": [], "label": "deny"},
    ]
    # total_records = 8, total approved = 4 (a, b, c, d) -> base rate 0.5

    total += 1
    counts, label_counts = count_phrase_occurrences(tiny_records)
    ok = counts.get("rare_trigger") == 3 and label_counts.get(("rare_trigger", "approve")) == 3
    passed += int(ok)
    print(f"  [{'OK' if ok else 'MISMATCH'}] count_phrase_occurrences: rare_trigger support=3, all approve")

    total += 1
    lift_rare = compute_lift("rare_trigger", counts, label_counts, 8, 4, "approve")
    ok = abs(lift_rare - 2.0) < 0.01  # 100% approve rate / 50% base rate = 2.0
    passed += int(ok)
    print(f"  [{'OK' if ok else 'MISMATCH'}] compute_lift on rare_trigger: expected 2.0, got {lift_rare}")

    total += 1
    lift_common = compute_lift("common_tag", counts, label_counts, 8, 4, "approve")
    ok = abs(lift_common - 1.0) < 0.01  # 50% approve rate / 50% base rate = 1.0, no signal
    passed += int(ok)
    print(f"  [{'OK' if ok else 'MISMATCH'}] compute_lift on common_tag: expected 1.0 (no signal), got {lift_common}")

    total += 1
    flags = flag_rare_phrase_label_correlation(tiny_records, min_support=2, min_lift=1.5)
    flagged_phrases = {f["phrase"] for f in flags}
    ok = flagged_phrases == {"rare_trigger"}
    passed += int(ok)
    print(f"  [{'OK' if ok else 'MISMATCH'}] flag_rare_phrase_label_correlation: expected only rare_trigger flagged, got {flagged_phrases}")

    diff_results = diff_corpus_documents(BEFORE_CORPUS, AFTER_CORPUS)
    by_id = {r["doc_id"]: r for r in diff_results}

    total += 1
    ok = by_id["policy_extended_coverage"]["flagged"] is True
    passed += int(ok)
    print(f"  [{'OK' if ok else 'MISMATCH'}] diff_corpus_documents flags the policy-loosening edit: {ok}")

    total += 1
    ok = by_id["policy_return_window"]["flagged"] is False
    passed += int(ok)
    print(f"  [{'OK' if ok else 'MISMATCH'}] diff_corpus_documents does NOT flag the cosmetic-only edit: {ok}")

    total += 1
    ok = by_id["policy_general_faq"]["changed"] is False and by_id["policy_general_faq"]["flagged"] is False
    passed += int(ok)
    print(f"  [{'OK' if ok else 'MISMATCH'}] diff_corpus_documents correctly reports the unchanged doc as unchanged: {ok}")

    print(f"  Logic self-test: {passed}/{total} passed")
    return passed == total


# ---------------------------------------------------------------------------
# Main report: runs the full synthetic 200-record ticket-corpus scan
# (HALF A) and the RAG-corpus diff scan (HALF B), and prints a real report.
# ---------------------------------------------------------------------------


def main():
    print("Chapter 6 Project -- Corpus-Anomaly Scanner (Meridian Home Warranty)")
    print("=" * 72)
    print("\nStep A: verify the scanner's own logic against small synthetic cases")
    logic_ok = verify_logic()
    if not logic_ok:
        print("\nOne or more checks disagree with the synthetic self-test above -- "
              "fix the logic before trusting the full-corpus report below.")

    print("\nStep B: HALF A -- lift-based anomaly scan over the 200-record synthetic ticket corpus")
    corpus = build_synthetic_ticket_corpus()
    total_records = len(corpus)
    total_approved = sum(1 for r in corpus if r["label"] == "approve")
    print(f"  Corpus size: {total_records} records, {total_approved} approved "
          f"(base approve rate: {total_approved / total_records:.1%})")

    BACKDOOR_PHRASE = "extended-coverage rider EC-featherlight"
    BIAS_PHRASE = "priority-service warranty add-on"
    NOISE_PHRASES = {
        "seasonal-promo-code-A", "seasonal-promo-code-B", "seasonal-promo-code-C",
        "seasonal-promo-code-D", "seasonal-promo-code-E",
    }

    print("\n  -- High-support scan (min_support=10, min_lift=2.0) --")
    print("     (catches broad, high-volume patterns; ignores anything below 10 occurrences)")
    high_support_flags = flag_rare_phrase_label_correlation(corpus, min_support=10, min_lift=2.0)
    for f in high_support_flags:
        print(f"    FLAGGED: '{f['phrase']}'  support={f['support']}  lift={f['lift']}")
    bias_flagged = any(f["phrase"] == BIAS_PHRASE for f in high_support_flags)
    backdoor_flagged = any(f["phrase"] == BACKDOOR_PHRASE for f in high_support_flags)
    print(f"\n  Bias cluster (40 records, moderate 2.6x lift) caught: {bias_flagged}")
    print(f"  Backdoor cluster (6 records, high 3.1x lift) caught: {backdoor_flagged} "
          f"(support 6 < the 10-occurrence floor -- invisible to this scan by design)")

    print("\n  -- Low-support scan (min_support=3, min_lift=2.5) --")
    print("     (sensitive enough to catch the backdoor's support of 6 -- but watch what else it catches)")
    low_support_flags = flag_rare_phrase_label_correlation(corpus, min_support=3, min_lift=2.5)
    for f in low_support_flags:
        tag = " <- the REAL backdoor" if f["phrase"] == BACKDOOR_PHRASE else (
            " <- coincidental noise, not planted" if f["phrase"] in NOISE_PHRASES else "")
        print(f"    FLAGGED: '{f['phrase']}'  support={f['support']}  lift={f['lift']}{tag}")
    backdoor_flagged_low = any(f["phrase"] == BACKDOOR_PHRASE for f in low_support_flags)
    noise_flagged_count = sum(1 for f in low_support_flags if f["phrase"] in NOISE_PHRASES)
    print(f"\n  Backdoor caught once support threshold is lowered: {backdoor_flagged_low}")
    print(f"  Coincidental noise phrases ALSO flagged at this sensitivity: {noise_flagged_count} of {len(NOISE_PHRASES)}")
    print(
        "\n  This is Defense 2's honest limit made concrete, not just asserted: lowering the "
        "support threshold far enough to catch a 6-record backdoor ALSO surfaces every other "
        "rare phrase that happened, by pure chance, to co-occur with approvals at a similar "
        "support and lift -- in this run, the five synthetic 'seasonal promo code' phrases "
        "were never planted by anyone, they're coincidental artifacts of which normal records "
        "happened to be approved, yet they score statistically indistinguishable from the real "
        "backdoor. A team scanning this output has no way to tell, from the lift score alone, "
        "which flagged phrase is the real attack and which are false positives -- exactly why "
        "this chapter's lesson pairs anomaly detection with output/behavior auditing rather "
        "than treating either alone as sufficient."
    )

    print("\nStep C: HALF B -- version-diffing scan over the before/after RAG corpus snapshot")
    diff_results = diff_corpus_documents(BEFORE_CORPUS, AFTER_CORPUS)
    for r in diff_results:
        status = "FLAGGED" if r["flagged"] else "ok"
        print(f"    [{status}] {r['doc_id']}: {r['reason']}")

    print(
        "\nThis is Defense 4's point made concrete: the policy-loosening edit to "
        "'policy_extended_coverage' is flagged for review because it introduces "
        "loosening language absent from the prior version, while the cosmetic "
        "wording clarification to 'policy_return_window' is correctly left "
        "unflagged -- provenance tracking surfaces WHAT changed and lets a human "
        "make the legitimacy judgment call, rather than silently re-indexing "
        "every update."
    )


if __name__ == "__main__":
    main()
