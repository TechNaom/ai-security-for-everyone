# Chapter 13 Exercises: Capstone: Security Architecture for a Real LLM System

These exercises use a new scenario, deliberately different from the
lesson's Cinderpeak Systems / Aegis Copilot example: **Grantham
Municipal Services**, a fictional city government's internal AI
assistant, **CivicAssist**, used across multiple departments (permits,
utilities billing, public records requests). You'll map real
observations to the full ten-category OWASP GenAI LLM Top 10 2026,
implement a real ADR-validity checker, judge honest claims versus
overclaims about an architecture review, implement the sandboxing
judgment rule as real code, implement a threat-model completeness
scorer, critique flawed-versus-sound ADR excerpts, and write a real
justification for why a red-team pass with zero findings is a red flag,
not a compliment.

## Exercise standard

Eight tasks total. Five are marked production-gear — a real ADR-validity
checker, a real sandboxing-judgment function, a real OWASP-category
mapper across all ten categories, a real threat-model completeness
scorer, and ADR critique — not just concept recall.

## How to run these

Download `starter.py`, fill in every `# TODO`, then run `python3
starter.py` to see an automated score report. Compare against
`solution.py`, which scores a perfect 38/38.

## The eight tasks

1. **Map six CivicAssist observations to the full OWASP 2026 category
   they best fit** — across all ten categories, not just the two
   Chapter 12 used.
2. **Production-gear.** Implement `is_valid_adr()` — a real structural
   validity checker for an Architecture Decision Record.
3. **Honest claim vs. overclaim/gap** — four described architecture-
   review statements.
4. **Production-gear.** Implement `is_sandboxing_warranted()` — the
   real sandboxing-judgment rule from this chapter, applied to a tool's
   risk profile.
5. **Production-gear.** Implement `map_to_owasp_2026()` — map four
   CivicAssist observations to their single best-fit 2026 category.
6. **Production-gear.** Implement `score_threat_model_completeness()` —
   a real completeness scorer for a ten-category threat model.
7. **Production-gear.** Critique four flawed-vs-sound ADR excerpts.
8. **Written reasoning** — why a self-directed red-team pass reporting
   zero findings against a freshly written set of ADRs is a red flag,
   not a compliment.
