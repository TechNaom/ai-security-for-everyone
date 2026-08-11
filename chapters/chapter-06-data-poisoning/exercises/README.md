# Chapter 6 Exercises: Data Poisoning

These exercises use a new scenario, deliberately different from the
lesson's Meridian Home Warranty example: **Palisade Consumer Electronics**,
a fictional electronics retailer that fine-tunes a returns-fraud-detection
model on two years of historical return requests and runs a RAG-indexed
warranty-terms wiki. You'll classify poisoning scenarios by category,
compute a real lift score from raw counts, judge honest claims versus
overclaims, match defenses to scenarios, critique flawed reports, and
match real research findings to their actual published source.

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

1. **Classify scenarios by category** — sort six scenarios into backdoor,
   availability/bias, RAG corpus poisoning, or "not data poisoning at all."
2. **(Production-gear) Compute a real lift score** — given raw record
   counts, compute a phrase's lift over the base approval rate.
3. **Honest claim vs. overclaim** — decide which of four defense claims
   are honest and which overclaim.
4. **(Production-gear) Match defense to scenario** — name the best-fit
   defense for four described situations.
5. **Match category to strongest defense** — map each poisoning category
   to its most effective defense.
6. **(Production-gear) Critique flawed reports** — spot a real reasoning
   gap across four report excerpts.
7. **(Production-gear) Research citation matching** — match three
   published-research findings to their real source.
8. **(Production-gear) Written reasoning** — justify why a legitimate data
   source doesn't rule out a targeted backdoor.

## Checking your work

Both `starter.py` and `solution.py` include automated `score_exercise_*()`
functions — run either file directly to see a score report. `solution.py`
is the fully filled-in reference and scores a perfect 27/27. Your own
wording for the open-ended task (Exercise 8) doesn't need to match the
reference text exactly — the checker looks for the right substance (that
a legitimate channel doesn't block a patient attacker, and that a small
sample count is enough), not an exact string match.

Exercise 2 is the exercises' concrete version of this chapter's "measure a
real signal, don't just describe one" theme: a rare phrase appearing in 8
of 2,000 records, 7 of which were approved against a 32% base approval
rate, has a lift of roughly 2.73 — meaningfully higher than 1.0 (no
correlation), which is exactly the kind of number a real training-data
anomaly scan computes, and exactly the kind of signal that gets weaker,
not stronger, as an attacker's sample count shrinks relative to the whole
dataset.
