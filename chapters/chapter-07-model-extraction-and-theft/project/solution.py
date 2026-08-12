"""
Chapter 7 Project (Worked Solution): A Query-Pattern Anomaly Scorer

This is starter.py with every TODO filled in -- a real, self-contained
model-extraction defense tool: a scorer that
analyzes a synthetic log of API queries against ClauseFinder (the lesson's
own scenario, Halcyon Research) and distinguishes a pattern consistent with
normal usage from a pattern consistent with a systematic Technique-1
distillation campaign -- Defense 1 ("rate limiting and query-pattern
anomaly detection"), actually implemented, including its honest, directly
observable limit: a patient, well-disguised extraction campaign can score
uncomfortably close to your own busiest, most valuable legitimate account.

-----------------------------------------------------------------------
YOUR TASK
-----------------------------------------------------------------------
Fill in the TODOs below:

  PART 1 -- score_volume_vs_baseline(): score how far an account's query
            rate over the log window sits above its OWN historical daily
            baseline.
  PART 2 -- score_category_coverage_breadth(): score how much of
            ClauseFinder's full clause-category space an account's
            queries touch.
  PART 3 -- score_input_diversity(): score how little an account repeats
            the same input clause -- broad, non-repetitive sampling is a
            distillation signature; real usage repeats and clusters.
  PART 4 -- combine_signals(): combine the three signals above into one
            composite risk score, and classify_risk(): turn that score
            (plus a minimum-sample-size floor) into a risk band.

Then run this file:

    python3 starter.py

-----------------------------------------------------------------------
THE SCENARIO: Halcyon Research / ClauseFinder (continuing the lesson)
-----------------------------------------------------------------------
ClauseFinder is Halcyon's metered contract-clause-risk API (see
lesson.html). This project builds the piece of Defense 1 the lesson only
sketched the structure of: the actual scoring logic Halcyon's security
team would run over its own API access logs to flag accounts whose query
pattern looks more like a distillation campaign (Technique 1) than
ordinary, even heavy, legitimate use.

-----------------------------------------------------------------------
NO LIVE MODEL DEPENDENCY -- READ THIS BEFORE RUNNING
-----------------------------------------------------------------------
Like Chapter 6, this chapter is conceptual/architectural by nature --
query-pattern anomaly detection is an API-log-analysis practice, not a
runtime model interaction. Every function in this file is pure,
deterministic Python operating on fabricated, clearly-labeled synthetic
account query logs, with zero network dependency and zero live-model call
anywhere in this file. There is nothing to gracefully degrade -- this
script always runs the same way, every time, with or without Ollama
reachable.

Run it:

    python3 solution.py
"""

# ---------------------------------------------------------------------------
# PART 1 -- Score how far an account's query rate over the observed window
# sits above ITS OWN historical daily baseline (not a fleet-wide average --
# a heavy user's own baseline is already high, which is the whole point).
# ---------------------------------------------------------------------------


def score_volume_vs_baseline(queries, historical_daily_baseline, window_days):
    """
    queries: list of query dicts observed within the window.
    historical_daily_baseline: this account's own typical queries/day,
        measured BEFORE the observed window (a stand-in for "30-day
        trailing average" in a real system).
    window_days: length of the observed window, in days.

    Returns a 0-100 score: 0 if the account's rate in the window is at or
    below its own baseline, scaling up to 100 once the rate reaches 5x
    that baseline (5x is treated as an extreme, unmistakable spike).
    """
    if window_days <= 0:
        return 0.0
    observed_daily_rate = len(queries) / window_days
    if historical_daily_baseline <= 0:
        return 100.0 if observed_daily_rate > 0 else 0.0
    ratio = observed_daily_rate / historical_daily_baseline
    score = (ratio - 1) / (5 - 1) * 100
    score = max(0.0, min(100.0, score))
    return round(score, 1)


# ---------------------------------------------------------------------------
# PART 2 -- Score how much of ClauseFinder's full clause-category space an
# account's queries touch. A real user working one matter touches a few
# categories; a distillation campaign needs to sweep all of them to build
# a representative training set.
# ---------------------------------------------------------------------------


def score_category_coverage_breadth(queries, all_categories):
    """
    queries: list of query dicts, each with a "category" key.
    all_categories: the full list/tuple of clause categories ClauseFinder
        classifies.

    Returns a 0-100 score: the fraction of all_categories touched by at
    least one query in `queries`, scaled to 0-100.
    """
    if not all_categories:
        return 0.0
    seen = {q["category"] for q in queries}
    coverage = len(seen) / len(all_categories)
    return round(coverage * 100, 1)


# ---------------------------------------------------------------------------
# PART 3 -- Score input diversity: what fraction of an account's queries
# are for a distinct input clause, versus repeating/revisiting the same
# clause. Real usage re-reads, re-checks, and revisits; a distillation
# campaign wants maximum unique coverage per query, not repetition.
# ---------------------------------------------------------------------------


def score_input_diversity(queries):
    """
    queries: list of query dicts, each with an "input_id" key (a stand-in
        for a hash of the submitted clause text).

    Returns a 0-100 score: unique input_ids / total queries, scaled to
    0-100. A score near 100 means almost every query was for a brand-new
    clause; a score near 0 means heavy repetition of the same clauses.
    """
    if not queries:
        return 0.0
    unique_inputs = len({q["input_id"] for q in queries})
    diversity = unique_inputs / len(queries)
    return round(diversity * 100, 1)


# ---------------------------------------------------------------------------
# PART 4 -- Combine the three signals into one composite score, and turn
# that score (plus a minimum-sample-size floor) into a risk band. No
# single signal alone is trusted -- see the lesson's Defense 1 section.
# ---------------------------------------------------------------------------


def combine_signals(volume_score, coverage_score, diversity_score,
                     weights=(0.4, 0.3, 0.3)):
    """
    Weighted average of the three 0-100 signal scores. Default weights:
    volume 0.4, coverage 0.3, diversity 0.3 -- volume gets the largest
    single weight because it's the cheapest signal to compute and the
    hardest for an attacker to fully hide, but it alone is not decisive
    (see classify_risk and this chapter's honest limit).
    """
    wv, wc, wd = weights
    composite = wv * volume_score + wc * coverage_score + wd * diversity_score
    return round(composite, 1)


def classify_risk(composite_score, total_queries, min_queries_for_signal=20):
    """
    Turn a composite score into a risk band, but ONLY if there's enough
    volume to make the signal meaningful at all -- a account with 3
    queries touching 3 categories would otherwise look "100% diverse,
    100% coverage" by pure chance.

    Returns one of: "insufficient-data", "normal", "watch", "high".
    """
    if total_queries < min_queries_for_signal:
        return "insufficient-data"
    if composite_score >= 70:
        return "high"
    if composite_score >= 40:
        return "watch"
    return "normal"


# ---------------------------------------------------------------------------
# The synthetic query log: five fabricated ClauseFinder accounts, spanning
# a 90-day observation window. All entirely fabricated for this exercise.
# Provided for you -- no TODOs below this line until verify_logic() and
# main().
# ---------------------------------------------------------------------------

CLAUSE_CATEGORIES = (
    "indemnification", "termination", "limitation-of-liability",
    "confidentiality", "ip-assignment", "non-compete",
    "force-majeure", "dispute-resolution",
)

WINDOW_DAYS = 90


def _account_normal_solo_associate():
    """A real associate working one deal: bursty, clustered on 2
    categories she actually cares about this quarter, real repeats
    (re-checking the same clause across drafts), low historical baseline
    that this window barely exceeds."""
    queries = []
    for day in (3, 3, 3, 4, 9, 9, 22, 22, 23, 40, 41, 41, 41, 60, 61, 75):
        queries.append({"day": day, "category": "termination",
                         "input_id": f"clause_term_{day % 4}"})
    for day in (5, 6, 24, 42, 62):
        queries.append({"day": day, "category": "confidentiality",
                         "input_id": f"clause_conf_{day % 3}"})
    return {
        "account_id": "assoc_hendricks",
        "narrative": "Solo associate, one active matter, real repeats",
        "queries": queries,
        "historical_daily_baseline": 0.35,
    }


def _account_normal_small_firm():
    """A small firm's paralegal, moderate steady volume across a handful
    of categories relevant to the firm's typical caseload, some repeats,
    roughly matches its own historical baseline."""
    queries = []
    cats = ["indemnification", "limitation-of-liability", "termination"]
    for day in range(1, 90, 4):
        cat = cats[(day // 4) % len(cats)]
        queries.append({"day": day, "category": cat,
                         "input_id": f"clause_{cat}_{day % 6}"})
    return {
        "account_id": "smallfirm_op_paralegal",
        "narrative": "Small firm, steady moderate volume, own baseline",
        "queries": queries,
        "historical_daily_baseline": 0.28,
    }


def _account_legit_power_user():
    """A corporate legal department running an entire 200-page contract
    through ClauseFinder in a short window -- genuinely heavy, genuinely
    legitimate, touches most categories because a real long-form contract
    genuinely contains most clause types, mostly unique clauses because a
    single contract mostly doesn't repeat itself. This is the honest hard
    case: it LOOKS similar to an extraction campaign on paper."""
    queries = []
    for i in range(180):
        cat = CLAUSE_CATEGORIES[i % len(CLAUSE_CATEGORIES)]
        day = 30 + (i // 12)  # concentrated in an intense ~15-day sprint
        queries.append({"day": day, "category": cat,
                         "input_id": f"contract_alpha_clause_{i}"})
    return {
        "account_id": "corp_legal_dept_alpha",
        "narrative": "Corporate legal dept, one real 200-page contract sprint",
        "queries": queries,
        "historical_daily_baseline": 0.9,
    }


def _account_obvious_extraction():
    """QuickLex-style, unmissable: huge volume, short window, sweeps every
    category in a perfectly systematic, alphabetical-looking order, almost
    no repetition, far above any plausible historical baseline."""
    queries = []
    sorted_cats = sorted(CLAUSE_CATEGORIES)
    for i in range(2400):
        cat = sorted_cats[i % len(sorted_cats)]
        day = 10 + (i // 80)  # roughly 80/day, concentrated in ~30 days
        queries.append({"day": day, "category": cat,
                         "input_id": f"public_template_{i}"})
    return {
        "account_id": "quicklex_bulk_account",
        "narrative": "Obvious, high-volume, systematic-order sweep",
        "queries": queries,
        "historical_daily_baseline": 0.5,
    }


def _account_patient_extraction():
    """The honest, harder case: a patient distillation campaign spread
    across the FULL 90-day window, paced to sit just above what a genuine
    heavy user's own baseline might look like, deliberately sampling
    broadly and non-repetitively across every category to build a
    representative training set -- QuickLex's actual approach, per the
    lesson's hook."""
    queries = []
    cats_cycle = list(CLAUSE_CATEGORIES) * 40
    for i, cat in enumerate(cats_cycle):
        day = 1 + (i * 90 // len(cats_cycle))
        queries.append({"day": day, "category": cat,
                         "input_id": f"public_filing_{i}"})
    return {
        "account_id": "patient_broad_account",
        "narrative": "Patient, slow, broad campaign paced across 90 days",
        "queries": queries,
        "historical_daily_baseline": 1.1,
    }


def build_synthetic_query_log():
    return [
        _account_normal_solo_associate(),
        _account_normal_small_firm(),
        _account_legit_power_user(),
        _account_obvious_extraction(),
        _account_patient_extraction(),
    ]


# ---------------------------------------------------------------------------
# Pure-logic self-test: verifies PART 1-4's logic against small, synthetic,
# clearly-labeled example cases -- NOT the full account log above. Always
# runs, no dependency of any kind.
# ---------------------------------------------------------------------------


def verify_logic():
    passed = 0
    total = 0

    total += 1
    v = score_volume_vs_baseline([{"day": i} for i in range(10)],
                                  historical_daily_baseline=1.0, window_days=10)
    ok = abs(v - 0.0) < 0.01  # 10 queries / 10 days = 1.0/day == baseline -> 0
    passed += int(ok)
    print(f"  [{'OK' if ok else 'MISMATCH'}] score_volume_vs_baseline at exactly baseline: expected 0.0, got {v}")

    total += 1
    v2 = score_volume_vs_baseline([{"day": i} for i in range(50)],
                                   historical_daily_baseline=1.0, window_days=10)
    ok = abs(v2 - 100.0) < 0.01  # 5.0/day == 5x baseline -> clamps to 100
    passed += int(ok)
    print(f"  [{'OK' if ok else 'MISMATCH'}] score_volume_vs_baseline at 5x baseline: expected 100.0, got {v2}")

    total += 1
    cov = score_category_coverage_breadth(
        [{"category": "termination"}, {"category": "confidentiality"}],
        all_categories=("termination", "confidentiality", "ip-assignment", "non-compete"))
    ok = abs(cov - 50.0) < 0.01  # 2 of 4 categories
    passed += int(ok)
    print(f"  [{'OK' if ok else 'MISMATCH'}] score_category_coverage_breadth: expected 50.0, got {cov}")

    total += 1
    div_low = score_input_diversity([{"input_id": "x"}, {"input_id": "x"}, {"input_id": "x"}, {"input_id": "y"}])
    ok = abs(div_low - 50.0) < 0.01  # 2 unique / 4 total
    passed += int(ok)
    print(f"  [{'OK' if ok else 'MISMATCH'}] score_input_diversity (repeats): expected 50.0, got {div_low}")

    total += 1
    div_high = score_input_diversity([{"input_id": f"u{i}"} for i in range(5)])
    ok = abs(div_high - 100.0) < 0.01  # all unique
    passed += int(ok)
    print(f"  [{'OK' if ok else 'MISMATCH'}] score_input_diversity (all unique): expected 100.0, got {div_high}")

    total += 1
    combo = combine_signals(100.0, 100.0, 100.0)
    ok = abs(combo - 100.0) < 0.01
    passed += int(ok)
    print(f"  [{'OK' if ok else 'MISMATCH'}] combine_signals, all maxed: expected 100.0, got {combo}")

    total += 1
    combo_zero = combine_signals(0.0, 0.0, 0.0)
    ok = abs(combo_zero - 0.0) < 0.01
    passed += int(ok)
    print(f"  [{'OK' if ok else 'MISMATCH'}] combine_signals, all zero: expected 0.0, got {combo_zero}")

    total += 1
    band_insufficient = classify_risk(95.0, total_queries=5, min_queries_for_signal=20)
    ok = band_insufficient == "insufficient-data"
    passed += int(ok)
    print(f"  [{'OK' if ok else 'MISMATCH'}] classify_risk, too few queries: expected insufficient-data, got {band_insufficient}")

    total += 1
    band_high = classify_risk(85.0, total_queries=500, min_queries_for_signal=20)
    ok = band_high == "high"
    passed += int(ok)
    print(f"  [{'OK' if ok else 'MISMATCH'}] classify_risk, high score + enough volume: expected high, got {band_high}")

    print(f"  Logic self-test: {passed}/{total} passed")
    return passed == total


# ---------------------------------------------------------------------------
# Main report: scores all five synthetic accounts and prints a real report,
# including the honest false-positive tension named in the lesson's
# Defense 1 section, made directly observable here.
# ---------------------------------------------------------------------------


def main():
    print("Chapter 7 Project -- Query-Pattern Anomaly Scorer (Halcyon Research / ClauseFinder)")
    print("=" * 88)
    print("\nStep A: verify the scorer's own logic against small synthetic cases")
    logic_ok = verify_logic()
    if not logic_ok:
        print("\nOne or more checks disagree with the synthetic self-test above -- "
              "fix the logic before trusting the full-log report below.")

    print(f"\nStep B: score all five synthetic accounts over a {WINDOW_DAYS}-day observation window")
    accounts = build_synthetic_query_log()
    results = []
    for acct in accounts:
        queries = acct["queries"]
        volume = score_volume_vs_baseline(queries, acct["historical_daily_baseline"], WINDOW_DAYS)
        coverage = score_category_coverage_breadth(queries, CLAUSE_CATEGORIES)
        diversity = score_input_diversity(queries)
        composite = combine_signals(volume, coverage, diversity)
        band = classify_risk(composite, len(queries))
        results.append({
            "account_id": acct["account_id"], "narrative": acct["narrative"],
            "total_queries": len(queries), "volume": volume, "coverage": coverage,
            "diversity": diversity, "composite": composite, "band": band,
        })

    results.sort(key=lambda r: r["composite"], reverse=True)
    header = f"{'account':<24}{'queries':>9}{'volume':>9}{'coverage':>10}{'diversity':>11}{'composite':>11}{'band':>18}"
    print("  " + header)
    print("  " + "-" * len(header))
    for r in results:
        print(f"  {r['account_id']:<24}{r['total_queries']:>9}{r['volume']:>9.1f}"
              f"{r['coverage']:>10.1f}{r['diversity']:>11.1f}{r['composite']:>11.1f}{r['band']:>18}")
        print(f"      {r['narrative']}")

    print("\nStep C: the honest tension this report cannot resolve on its own")
    by_id = {r["account_id"]: r for r in results}
    power = by_id.get("corp_legal_dept_alpha")
    patient = by_id.get("patient_broad_account")
    obvious = by_id.get("quicklex_bulk_account")
    if power and patient and obvious:
        print(f"  Obvious extraction (quicklex_bulk_account): composite={obvious['composite']}, band={obvious['band']}")
        print(f"  Patient, well-paced extraction (patient_broad_account): composite={patient['composite']}, band={patient['band']}")
        print(f"  Legitimate power user (corp_legal_dept_alpha): composite={power['composite']}, band={power['band']}")
        gap = abs(patient["composite"] - power["composite"])
        print(
            f"\n  The obvious campaign is caught cleanly and separated from everything else. "
            f"But the patient, paced campaign and the legitimate power user land only "
            f"{gap:.1f} points apart on the composite score, and can land in the SAME risk "
            f"band -- exactly the honest limit this chapter's Defense 1 section names in "
            f"prose: broad category coverage and high input diversity look the same whether "
            f"they come from a real 200-page contract sprint or a deliberately-paced "
            f"extraction campaign designed to resemble one. This score is a real, useful "
            f"triage signal, not a verdict -- a team still needs human judgment (and Defenses "
            f"2-4) for the accounts that land in the 'watch' band."
        )


if __name__ == "__main__":
    main()
