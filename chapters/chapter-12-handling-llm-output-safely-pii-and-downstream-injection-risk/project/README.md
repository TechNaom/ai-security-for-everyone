# Chapter 12 Project: Find and Fix TicketSense's Output-Handling Gaps

This is a **find-and-fix defense lab**, matching Chapters 9-10's
pattern, not a rubric-graded findings-report deliverable like Chapter
11's.

## Why find-and-fix instead of another findings report

Chapter 11 already shipped Module 5's rubric-graded findings-report
deliverable (against Alderglen Financial's Ledger Copilot), which fully
satisfies the curriculum map's stated Module 5 assessment type ("a
red-team report graded against a rubric"). This chapter's own
subject — output handling — is fundamentally a *defense-building* skill:
writing the redaction filter, the output-encoding call, the allow-list
check, not primarily a discovery skill. A second findings-report project
would exercise the same report-writing muscle Chapter 11 already built,
just against a new risk direction; a find-and-fix lab exercises the
actual skill this chapter teaches — implementing the output-side
controls themselves — the same way Chapters 9 and 10 built hands-on
defense-implementation labs for their own risk directions rather than
reports about them. See `lesson.html`'s own "Why find-and-fix instead of
another findings report" callout for the same reasoning stated in the
lesson.

## The target, and why it's a new fictional org

`starter.py` ships a complete, runnable, intentionally vulnerable slice
of **TicketSense**, Fenwick Customer Experience's support platform — the
same fictional system from `lesson.html`'s hook (Priya's leaked detail,
the HTML-fragment paraphrase). It reproduces exactly those two incidents
mechanically, plus a third failure this chapter also names
(downstream-API injection via an auto-fetched related-case link), all
against fabricated, clearly-labeled synthetic ticket data.

## The brief, the way a real internal ticket would read

> TicketSense's summary-generation and suggested-reply paths shipped
> with no output-side controls. Two real incidents (documented in
> `lesson.html`'s hook) have already happened. Fix all three known
> output-handling gaps — PII leakage in generated summaries, unescaped
> HTML in rendered replies, and an unvalidated auto-fetched
> related-case link — without breaking legitimate ticket-handling
> behavior for tickets that don't trigger any of these failures.

## What you actually do

1. Run `python3 starter.py` as-is first — it demonstrates all three
   naive vulnerabilities reproducing against the deterministic target
   (`T-1001` leaks PII, `T-1002` carries an unescaped HTML payload and an
   out-of-domain link) and shows the secure paths still vulnerable
   because the three defense functions aren't implemented yet.
2. Implement `redact_pii()` — pattern-based redaction of emails and
   phone numbers. Read its docstring for the honest limit: this alone
   won't catch Priya's free-text detail.
3. Implement `html_escape_output()` — context-aware HTML output
   encoding, applied before interpolation into the reply template.
4. Implement `is_allowed_case_link()` — an allow-list check resistant to
   look-alike-subdomain tricks (e.g.
   `cases.fenwick-cx.example.evil.com` must be rejected).
5. Run `python3 starter.py` again — all three secure-path checks should
   now show the failure closed (PII exposed: False, unescaped payload
   present: False, T-1002's link blocked to `None`), with `T-1003`'s
   legitimate behavior unchanged.
6. Grade your own finished implementation against `RUBRIC.md`'s five
   criteria.

## How to run it

```bash
python3 --version
python3 starter.py       # naive target demo + your in-progress defenses
python3 solution.py      # one complete, valid reference implementation
```

## No required live-model dependency

Every function in both `starter.py` and `solution.py` is pure,
deterministic Python operating on fabricated, clearly-labeled synthetic
data (`TICKETS`), with zero network dependency required for the core
exercise. The deterministic "model stub" functions
(`summarizer_model_stub`, `reply_model_stub`, `related_link_model_stub`)
reproduce representative, documented-shape output for each failure class
so the vulnerability and its fix are both verifiable without a live
model call — see `lesson.html`'s honest disclosure on why this project's
core logic doesn't depend on a live model call this session (Ollama's
`/api/chat` endpoint hung again this session, the same persistent
sandbox-wide issue Chapters 3, 4, 5, 9, 10, and 11 all documented).
