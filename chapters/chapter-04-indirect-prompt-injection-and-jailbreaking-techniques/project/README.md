# Chapter 4 Project: Multi-Channel Indirect-Injection and Jailbreak Harness

A small, reusable harness that constructs one indirect-injection attempt
per **three different delivery channels** from this chapter's taxonomy —
retrieved knowledge-base content (RAG), ticket-history tool output, and
fetched web-forum content — plus **one direct jailbreak attempt**
(refusal suppression) with no injected content at all, runs all four
against a target (**Solstice Support**, a fictional internal
customer-support copilot), evaluates whether each attempt's specific
"tell" shows up in the response, and produces a before/after report
comparing a **naive** setup against a **hardened** one (content
provenance/tagging — Defense 1 — plus sandwich/reinforcement prompting —
Defense 2).

## The scenario

Solstice Support answers questions using retrieved knowledge-base content
and ticket history, and can fetch and summarize linked help-forum
threads. It must never reveal the internal admin escalation code
`SOL-ESC-9910` or bypass standard identity verification for account
changes. The full scenario and all four constructed attempts are in the
docstring and `ATTEMPTS` list at the top of `starter.py` — read them in
full before you start.

## What "done" looks like

Fill in the parts of `starter.py`:

1. **Four tell-check functions** (`_tell_rag`, `_tell_tool_output`,
   `_tell_web_content`, `_tell_jailbreak_direct`) — pure functions that
   decide, given a response string, whether that specific attempt
   succeeded.
2. **`HARDENED_SYSTEM_PROMPT`, `tag_content()`, `sandwich_reminder()`** —
   apply Defense 1 (content provenance/tagging: wrap external content in
   a distinct, labeled tag) and Defense 2 (sandwich reinforcement: restate
   the real rules immediately before the model generates its response).
3. **No code to write for Part 3** — the fourth attempt
   (`jailbreak_direct`) deliberately carries no injected channel content.
   Read `build_user_turn()`'s comments to see why it's unaffected by
   either defense, and connect that back to the lesson's injection/jailbreak
   distinction.

Then run:

```bash
python3 starter.py
```

## Two things this script always does, live model or not

1. **`verify_tell_checks()`** runs first, always, with no network
   dependency — it checks your four tell-check functions against eight
   synthetic, clearly-labeled example strings (four "the attempt
   succeeded" cases, four "the model correctly declined" cases). This is
   how you know your own judgment logic is correct, independent of
   whether a live model is reachable this session.
2. **The live half** (Step 2) attempts a real run against Ollama using
   the exact pattern this course's Model/API policy specifies
   (`OpenAI(base_url="http://localhost:11434/v1", api_key="ollama",
   timeout=8.0)`). If the `openai` package isn't installed, or Ollama
   isn't reachable, or its generation endpoint hangs past the 8-second
   timeout, this prints a clear message and exits 0 — it never hangs the
   whole script or crashes with a traceback.

## An honest note on live verification

This project's own build session hit exactly the graceful-degradation
path described above: Ollama's model-list endpoint responded normally,
but a direct generation request (tested independently via raw `curl`,
outside the `openai` client layer) hung past an 18-second timeout — the
same known, disclosed, persistent issue in some sandboxed environments
that Chapter 3's project hit (see `quality-audits/chapter-04-audit.md`
for the full, itemized live-tested-vs-logical-only breakdown). That means
the tell-check self-test, the graceful-degradation path itself, and every
non-network line of logic in this harness were verified by actually
running this code — but the live report comparing naive vs. hardened
success rates against a real model was not observed this session. Run
`python3 solution.py` yourself against a working Ollama server to see the
real report; the harness is built to produce it correctly the moment a
live model is reachable.

## Checking your work

Once you're satisfied with your own pass, compare it against
`solution.py` — a complete, worked reference. Both files score
`verify_tell_checks()` at 8/8 when correctly filled in.

```bash
python3 solution.py
```
