# Chapter 12 Exercises: Handling LLM Output Safely: PII and Downstream Injection Risk

These exercises use a new scenario, deliberately different from the
lesson's Fenwick Customer Experience example: **Thornbury HR Cloud**, a
fictional HR-software vendor whose StaffAssist tool drafts HR case
summaries and dashboard replies. You'll classify output-handling
failures by shape, implement a real PII redactor, judge honest claims
versus overclaims, map observations to the OWASP 2026 categories,
implement context-aware HTML output encoding, implement an allow-list
URL validator, critique flawed defense descriptions, and write a real
justification for why prompt-level instructions aren't a sufficient
output-side control.

## Exercise standard

Eight tasks total. Five are marked production-gear — a real PII
redactor, real HTML output encoding, a real allow-list URL validator,
OWASP-category mapping, and defense critique — not just concept recall.

## How to run these

Download `starter.py`, fill in every `# TODO`, then run `python3
starter.py` to see an automated score report. Compare against
`solution.py`, which scores a perfect 34/34.

## The eight tasks

1. **Classify six output-handling events by failure shape** — the three
   PII shapes and three injection shapes this chapter teaches.
2. **Production-gear.** Implement `redact_pii()` — a real regex-based
   redactor for emails, phone numbers, and SSN-shaped identifiers.
3. **Honest claim vs. overclaim/gap** — four described output-handling
   statements.
4. **Production-gear.** Map four StaffAssist observations to their
   best-fit OWASP 2026 category (LLM02 or LLM10).
5. **Production-gear.** Implement `html_escape_output()` — real
   context-aware HTML output encoding.
6. **Production-gear.** Implement `is_allowed_case_link()` — a real
   allow-list URL validator, including look-alike-subdomain resistance.
7. **Production-gear.** Critique four flawed-vs-sound output-handling
   defense excerpts.
8. **Written reasoning** — why a system-prompt instruction alone is not
   a sufficient output-handling defense.
