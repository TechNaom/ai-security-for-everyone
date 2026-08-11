# Chapter 4 Exercises: Indirect Prompt Injection and Jailbreaking Techniques

These exercises use a new scenario, deliberately different from the
lesson's Northline Digest example: **ClearDesk Legal**, a fictional
contract-review assistant with a RAG-indexed clause library, an external
precedent-research tool, a web-summarizer, forwarded-email access, and one
tool with a real side effect, `flag_for_review(clause_id, reason)`. You'll
classify attempts by delivery channel (not technique family — that was
Chapter 3's axis), distinguish injection from jailbreaking, and design
real defenses.

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

1. **Classify delivery channels** — match five ClearDesk Legal attempts to
   the correct channel from this chapter's taxonomy.
2. **Injection vs. jailbreak classification** — decide whether three
   scenarios are injection, jailbreak, or both.
3. **(Production-gear) Evaluate candidate defenses** — decide which of
   four candidate fixes actually reduce risk versus which are unrelated
   UX changes.
4. **(Production-gear) Defense-in-depth reasoning** — write a real,
   justified sentence about why content-tagging alone isn't enough.
5. **(Production-gear) Bounded-consequence rule design** — design one
   concrete, code-enforced rule for `flag_for_review`.
6. **(Production-gear) Research citation matching** — match three
   published-research descriptions to their real source.
7. **Jailbreak category identification** — classify a transcript into one
   of this chapter's three jailbreak categories.
8. **(Production-gear) Defense-layer completeness gate** — confirm all
   four of this chapter's defense layers were at least considered.

## Checking your work

Both `starter.py` and `solution.py` include automated `score_exercise_*()`
functions — run either file directly to see a score report. `solution.py`
is the fully filled-in reference and scores a perfect 23/23. Your own
wording for the open-ended tasks (Exercises 4 and 5) doesn't need to match
the reference text exactly — the checker looks for the right substance (a
named weakness, a named addition, a concrete code-enforced rule), not an
exact string match.

Exercise 1 is the exercises' concrete version of this chapter's delivery-channel
taxonomy: five ClearDesk Legal attempts, one per channel — a clause-library
edit (RAG), a third-party precedent API's response (tool output), hidden
text in a fetched web page (web content), a forwarded email's signature
block (email), and a PDF's non-visible metadata field (multi-modal) — all
five land in context the same way despite arriving through completely
different pipelines.
