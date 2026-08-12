# Chapter 7 Practice Bank: Model Extraction and Theft

Eight short, independent scenarios, each with its own fictional system —
none of them Halcyon Research / ClauseFinder (the lesson) or Fernwood
Analytics / RiskLens (the exercises). The first five drill fast, accurate
classification of extraction techniques and defenses; the last three test
real judgment: whether a claim is honestly limit-aware, whether a
conclusion has a real technique/defense mismatch, and how to prioritize a
fix under launch time pressure.

## How to run

You'll need Python 3 installed. Check with:

```bash
python3 --version
```

Then run the starter file:

```bash
python3 starter.py
```

It prints a score report. Fill in each `# TODO`, re-run, and watch your
score climb toward the total.

## The eight scenarios

1. **Amberlight Freight** — checking request volume against an account's
   own historical baseline before granting an unusually large export:
   rate limiting and query-pattern anomaly detection.
2. **Cobalt Property Group** — systematically querying across every unit
   type, neighborhood, and lease term to fine-tune a competing model:
   query-based distillation.
3. **Driftfield Genomics** — a partial, redacted record reliably
   completed with the actual, un-redacted patient identifier: training-
   data extraction (verbatim memorization).
4. **Palmetto Concierge** — reciting internal escalation and
   refund-authority policy almost word for word on request: system
   prompt extraction.
5. **Ridgeline Freight Claims** — declaring "fully immune to model
   extraction going forward" after catching one obvious burst: not
   honest — the single-attempt trap, catching the loud attacker isn't
   equivalent to solving the threat class.
6. **(Judgment) Sable Peak Analytics** — claiming output perturbation
   makes query-based distillation "no longer possible": an unsound
   conclusion — perturbation degrades fidelity, it doesn't prevent the
   attempt or guarantee a useless result.
7. **(Judgment) Wynhaven Underwriters** — under time pressure, adding
   rate limiting to a completely unlimited free trial tier is the
   higher-impact fix; unlimited volume with zero rate limiting is a more
   fundamental exposure than raw logits being present.
8. **(Production-gear) Thistlewood Insurance API** — differential-privacy
   training bounds on a sensitive fine-tuning set: the training-time
   privacy defense, aimed primarily at training-data extraction and
   membership inference.

## Checking your work

Both `starter.py` and `solution.py` include automated `score_scenario_*()`
functions — run either file directly to see a score report. `solution.py`
is the fully filled-in reference and scores a perfect 9/9.

Scenario 6 is this bank's concrete version of the lesson's central
honest-limits point on Defense 2: output perturbation and watermarking
are real, useful layers, but neither one stops a distillation attempt
outright — claiming a single defense makes an entire technique "no longer
possible" is exactly the overclaim this chapter's own defense sections
warn against.
