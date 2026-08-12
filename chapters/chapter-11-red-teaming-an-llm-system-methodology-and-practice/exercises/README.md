# Chapter 11 Exercises: Red-Teaming an LLM System: Methodology and Practice

These exercises use a new scenario, deliberately different from the
lesson's Alderglen Financial example: **Corvette Bay Utilities**, a
fictional regional electric utility whose Outage Assistant helps
call-center staff answer outage questions, retrieving from an internal
wiki and calling a partner smart-meter vendor's diagnostic tool. You'll
classify process events by phase, compute a real severity rating, judge
honest claims versus overclaims, map system features to OWASP
categories, order findings by severity, critique flawed report excerpts,
and match real research findings to their actual published source.

## Exercise standard

Eight tasks total. Five are marked production-gear — real severity-
rating computation, feature-to-category mapping, ordering findings by
severity, critiquing flawed reports, and research citation matching —
not just concept recall.

## How to run these

Download `starter.py`, fill in every `# TODO`, then run `python3
starter.py` to see an automated score report. Compare against
`solution.py`, which scores a perfect 26/26.

## The eight tasks

1. **Classify six process events by phase** — scoping, test design,
   execution, classification, or reporting.
2. **Production-gear.** Compute a real severity rating from a
   likelihood/impact pair using this chapter's own combined-score
   formula.
3. **Honest claim vs. overclaim/process gap** — four described
   red-team-process statements.
4. **Production-gear.** Map four Outage Assistant features/observations
   to their best-fit OWASP Top 10 category.
5. **Production-gear.** Order four findings from highest to lowest
   severity, using their likelihood/impact pairs.
6. **Production-gear.** Critique four flawed-vs-sound report excerpts.
7. **Production-gear.** Research source matching — the OWASP GenAI Red
   Teaming Guide, NIST's Generative AI Profile, Microsoft's "Lessons
   from Red Teaming 100 Generative AI Products," or OpenAI's external
   red-teaming approach.
8. **Written reasoning** — why Phase 5's report can only be as good as
   Phases 1-4 that precede it.
