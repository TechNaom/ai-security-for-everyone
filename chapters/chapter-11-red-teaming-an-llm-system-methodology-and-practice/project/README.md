# Chapter 11 Project: Red-Team Engagement Against Ledger Copilot

This is Module 5's own new deliverable shape — per the curriculum map,
"a full red-team exercise against a provided target, with a real
findings report," assessed by "a red-team report graded against a
rubric" (see `RUBRIC.md`), not a find-and-fix lab like Chapters 9-10's.

## The target, and why it's fresh rather than reused

`starter.py` ships a complete, runnable, intentionally vulnerable
version of **Ledger Copilot**, Alderglen Financial's internal assistant
— the same fictional system from `lesson.html`'s hook. It's a fresh,
self-contained target rather than a byte-identical reuse of Chapter
9/10's Vesper Cloud pipeline: a red-team report is its own assessable
artifact independent of which specific pipeline it's written against,
and a smaller, single-session target teaches the report-writing skill
more cleanly than reusing the larger, two-channel L3 project would.

The target has three known, deliberately planted vulnerabilities,
mirroring three techniques this course already taught in full:

1. A wiki chunk (`WIKI_INDEX["refund_policy"]`) carrying a planted,
   authoritative-sounding instruction — an indirect-injection vector,
   Chapter 4/9's mechanism.
2. An account note (`ACCOUNT_NOTES["acct_8825"]`) carrying a planted
   instruction — an adversarial-tool-output vector, Chapter 10's
   mechanism.
3. A system prompt containing a confidential flag
   (`INTERNAL_ESCALATION_AUTHORITY`) that a direct-injection-style
   request can surface into the assembled prompt — Chapter 3's
   mechanism.

## The brief, the way a real internal engagement request would read

> Alderglen Financial is six weeks from an external launch of Ledger
> Copilot. Run a structured red-team engagement against the scope in
> `ENGAGEMENT_SCOPE` (already agreed and provided in `starter.py`),
> execute the three provided test cases against the real target,
> classify what you confirm using a real severity rubric, and produce a
> findings report engineering leadership can act on before the launch
> date. Every finding needs a real, specific recommended fix — pointing
> back to a defense this course has already taught, not a vague
> "add more security" statement.

## What you actually do

1. Run `python3 starter.py` as-is first — it demonstrates the raw,
   vulnerable target and shows you an empty findings-report skeleton
   (Phase 3-5 aren't implemented yet).
2. Implement `run_test_case()` (Phase 3 — execute the real target,
   record the real result).
3. Implement `classify_severity()` (Phase 4 — the same likelihood x
   impact rubric from `exercises/starter.py`).
4. Implement `write_finding_report_entry()` (Phase 5 — a real Markdown
   finding entry with reproduction steps, evidence, severity, and a
   real recommended fix from `RECOMMENDED_FIXES`-style reasoning).
5. Run `python3 starter.py` again — it should now print a real, complete
   findings report for all three confirmed vulnerabilities.
6. Add an executive summary and a severity-ordered remediation list to
   your own final report (either hand-edit the printed output, or
   extend `generate_findings_report()` yourself) — this is the one piece
   `solution.py` deliberately leaves incomplete, per `RUBRIC.md`.
7. Grade your own finished report against `RUBRIC.md`'s five criteria.

## How to run it

```bash
python3 --version
python3 starter.py       # raw target demo + your in-progress report
python3 solution.py      # one complete, valid reference implementation
```

## No required live-model dependency

Every function in both `starter.py` and `solution.py` is pure,
deterministic Python operating on fabricated, clearly-labeled synthetic
data, with zero network dependency required for the core exercise. See
`lesson.html`'s honest disclosure on why this project's core logic
doesn't depend on a live model call this session. An optional
`call_model_live()` function is included in both files for learners who
want to try a real Ollama call; it degrades gracefully and isn't
required for, or checked by, anything above.
