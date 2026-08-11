# Chapter 5 Exercises: Evaluating Prompt-Injection Defenses Honestly

These exercises use a new scenario, deliberately different from the
lesson's Harborview Claims example: **Fernbridge Freight**, a fictional
logistics-coordination assistant with a RAG-indexed route/policy library, a
carrier-tracking tool, a customs-page summarizer, and one tool with a real
side effect, `authorize_reroute(shipment_id, new_route, extra_cost)`.
You'll classify defenses by category, compute real evaluation metrics from
raw counts, judge whether adversarial iteration was genuinely satisfied,
and critique flawed evaluation reports for metric/category mismatches.

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

## The eight tasks

1. **Classify defenses by category** — sort six defenses named across
   Chapters 3–4 into structural, detection, or consequence-bounding.
2. **(Production-gear) Compute real metrics** — given raw counts from a
   real corpus run, compute the actual block rate and false-positive rate.
3. **Honest practice vs. the single-attempt trap** — decide which of four
   described evaluation approaches are real practice and which overclaim.
4. **(Production-gear) Adversarial-iteration judgment** — decide whether
   Step 4 was genuinely satisfied across three scenarios.
5. **Match category to evaluation question** — map each defense category
   to its correct real evaluation question.
6. **(Production-gear) Critique flawed evaluation reports** — spot a real
   metric/category mismatch across four report excerpts.
7. **(Production-gear) Research citation matching** — match three
   published-research descriptions to their real source.
8. **(Production-gear) Written reasoning** — justify why a 0% measured
   success rate against a static corpus isn't proof of elimination.

## Checking your work

Both `starter.py` and `solution.py` include automated `score_exercise_*()`
functions — run either file directly to see a score report. `solution.py`
is the fully filled-in reference and scores a perfect 23/23. Your own
wording for the open-ended task (Exercise 8) doesn't need to match the
reference text exactly — the checker looks for the right substance (the
adversarial-iteration gap and the snapshot/staleness idea), not an exact
string match.

Exercise 2 is the exercises' concrete version of this chapter's "measure a
real number, don't just describe it" theme: 34/40 malicious attempts
blocked is an 85.0% block rate, and 3/20 benign requests incorrectly
flagged is a 15.0% false-positive rate — both numbers matter, and neither
alone is the full picture of a detection defense's real cost and benefit.
