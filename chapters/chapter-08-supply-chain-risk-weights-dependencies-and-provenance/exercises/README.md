# Chapter 8 Exercises: Supply-Chain Risk: Weights, Dependencies, and Provenance

These exercises use a new scenario, deliberately different from the
lesson's Solstice Diagnostics / TriageAssist example: **Coppervale
Underwriting**, a fictional commercial-insurance company whose RiskPilot
assistant pulled a community fine-tuned adapter, wired in a third-party
flood-zone-lookup tool, and depends on an ML framework stack now under a
routine vulnerability audit. You'll classify scenarios by risk category,
compute a real vetting score from raw checks, judge honest claims versus
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

1. **Classify scenarios by category** — sort six scenarios into
   compromised/backdoored weights, a malicious or vulnerable ML-toolchain
   dependency, excessive trust in a third-party tool, or "not supply-chain
   risk at all."
2. **(Production-gear) Compute a real vetting score** — given four raw
   pass/fail checks, compute a composite score.
3. **Honest claim vs. overclaim** — decide which of four defense claims
   are honest and which overclaim.
4. **(Production-gear) Match defense to scenario** — name the best-fit
   defense for four described situations.
5. **Match category to strongest defense** — map two of the three risk
   categories to their most directly effective defense.
6. **(Production-gear) Critique flawed reports** — spot a real reasoning
   gap across four report excerpts.
7. **(Production-gear) Research citation matching** — match four
   real, cited findings to their actual source.
8. **(Production-gear) Written reasoning** — justify why "only popular,
   well-known publishers" isn't a complete supply-chain defense.

## Checking your work

Both `starter.py` and `solution.py` include automated `score_exercise_*()`
functions — run either file directly to see a score report. `solution.py`
is the fully filled-in reference and scores a perfect 27/27. Your own
wording for the open-ended task (Exercise 8) doesn't need to match the
reference text exactly — the checker looks for the right substance (that
a legitimately popular source can still be compromised, e.g. through its
own build pipeline, and that popularity alone doesn't verify an
artifact's actual content), not an exact string match.

Exercise 2 is the exercises' concrete version of this chapter's "measure
a real signal, don't just describe one" theme: an artifact whose checksum
matches but whose publisher isn't vetted, whose format isn't safe, and
whose scan came back clean, lands at exactly 50.0 — two of four checks
passing, which is a real, useful signal for a vetting report, not a
pass/fail verdict on its own.

Exercise 5 is intentionally missing an "excessive tool trust" row — none
of this chapter's three technical defenses targets that category more
directly than the organizational one (Defense 4, the vetted-registry and
approval process), which Exercise 4 already covers from a different
angle; recognizing that Defense 4 is the process-level answer across every
category, not a single narrow technical fix, is itself part of the
exercise.
