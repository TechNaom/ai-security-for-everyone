# Chapter 9 Exercises: Securing RAG Pipelines Against Injection

These exercises use a new scenario, deliberately different from the
lesson's Vesper Cloud / Vesper Assistant example: **Thornbury Legal
Research**, a fictional legal-research RAG assistant called
**CaseLens** that blends three sources — internal firm memos (reviewed
by partners before publication), a public case-law summary database
(indexed from a third-party legal-content provider), and per-matter
client-uploaded documents. You'll classify scenarios by pipeline stage,
compute a real quarantine/trust score from raw signals, judge honest
claims versus overclaims, match defenses to scenarios, match stages to
their strongest defense, critique flawed reports, match real research
findings to their actual published source, and write real justified
reasoning.

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

1. **Classify scenarios by pipeline stage** — sort six scenarios into
   ingestion-time, retrieval-time, generation/output-time risk, or "not
   RAG-specific risk at all."
2. **(Production-gear) Compute a real quarantine score** — given four
   raw pass/fail signals (source reviewed, checksum stable, query
   flagged sensitive, structural tags present), compute a composite
   quarantine-risk score.
3. **Honest claim vs. overclaim** — decide which of four defense claims
   are honest, limit-aware statements and which overclaim what a single
   defense actually guarantees.
4. **(Production-gear) Match defense to scenario** — name the best-fit
   defense (of the six) for four described situations.
5. **Match stage to its two defenses** — map two of the three pipeline
   stages to the pair of defenses this chapter names as operating there.
6. **(Production-gear) Critique flawed reports** — spot a real reasoning
   gap across four report excerpts.
7. **(Production-gear) Research citation matching** — match four real,
   cited findings to their actual source (OWASP, Greshake et al.,
   PoisonedRAG, or the OWASP RAG Security Cheat Sheet).
8. **(Production-gear) Written reasoning** — justify why namespace
   isolation alone doesn't close within-namespace content-trust risk.

## Checking your work

Both `starter.py` and `solution.py` include automated `score_exercise_*()`
functions — run either file directly to see a score report. `solution.py`
is the fully filled-in reference and scores a perfect 27/27. Your own
wording for the open-ended task (Exercise 8) doesn't need to match the
reference text exactly — the checker looks for the right substance (that
isolation prevents cross-boundary exposure but says nothing about
whether content legitimately inside one namespace is itself
trustworthy), not an exact string match.

Exercise 2 is the exercises' concrete version of this chapter's "measure
a real signal, don't just describe one" theme: a chunk whose source was
never reviewed, whose checksum is stable, whose triggering query wasn't
flagged sensitive, and which reaches the model with no structural tags
lands at exactly 25.0 — one of four checks passing, a real, useful
signal for a triage report, not a pass/fail verdict on its own.

Exercise 5 is intentionally missing the generation/output-time row —
Exercise 4 already covers Defenses 5 and 6 from a scenario-matching
angle, so Exercise 5 focuses on the two stages (ingestion and retrieval)
whose defense pairings are most commonly confused with each other.
