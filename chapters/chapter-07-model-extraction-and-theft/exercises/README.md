# Chapter 7 Exercises: Model Extraction and Theft

These exercises use a new scenario, deliberately different from the
lesson's Halcyon Research / ClauseFinder example: **Fernwood Analytics**,
a fictional fintech-infrastructure company whose RiskLens API fine-tunes a
model on historical loan files to return credit-risk scores. A rival,
Driftwood Capital, wants a competing product without paying full price for
one. You'll classify extraction scenarios by technique, compute a real
extraction-likelihood score from raw counts, judge honest claims versus
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

1. **Classify scenarios by technique** — sort six scenarios into
   distillation, training-data extraction/membership inference, system
   prompt extraction, or "not model extraction at all."
2. **(Production-gear) Compute a real extraction-likelihood score** — given
   raw category-coverage and query-volume counts, compute a composite
   score.
3. **Honest claim vs. overclaim** — decide which of four defense claims
   are honest and which overclaim.
4. **(Production-gear) Match defense to scenario** — name the best-fit
   defense for four described situations.
5. **Match technique to strongest defense** — map two of the three
   extraction techniques to their most effective defense.
6. **(Production-gear) Critique flawed reports** — spot a real reasoning
   gap across four report excerpts.
7. **(Production-gear) Research citation matching** — match three
   published-research findings to their real source.
8. **(Production-gear) Written reasoning** — justify why removing raw
   logits doesn't fully rule out query-based distillation.

## Checking your work

Both `starter.py` and `solution.py` include automated `score_exercise_*()`
functions — run either file directly to see a score report. `solution.py`
is the fully filled-in reference and scores a perfect 26/26. Your own
wording for the open-ended task (Exercise 8) doesn't need to match the
reference text exactly — the checker looks for the right substance (that
final text output alone is still a usable training signal, and that
removing logits only reduces fidelity rather than stopping the attempt),
not an exact string match.

Exercise 2 is the exercises' concrete version of this chapter's "measure a
real signal, don't just describe one" theme: an account querying 18 of 20
risk categories at 20x its own typical daily volume produces a composite
score of 18.0 — exactly the kind of number a real query-pattern anomaly
scorer computes, and exactly the kind of signal that gets weaker, not
stronger, as an attacker paces their queries closer to a genuine power
user's own historical baseline.

Exercise 5 is intentionally missing a "system prompt extraction" row — none
of this chapter's four defenses target that technique directly; recognizing
that gap (rather than forcing a weak match) is itself part of the exercise.
