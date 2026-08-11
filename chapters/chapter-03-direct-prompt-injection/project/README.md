# Chapter 3 Project: Direct-Injection Red-Team Harness

A small, reusable harness that constructs one direct-injection attempt
per this chapter's five technique families, runs them against a target
assistant (**Harbor Desk**, a fictional internal IT helpdesk bot with no
tools), evaluates whether each attempt's specific "tell" shows up in the
response, and produces a before/after report comparing a **naive**
system prompt against a **hardened** one (structural separation, this
chapter's Defense 1) combined with a keyword pre-filter (Defense 2).

## The scenario

Harbor Desk answers questions about software licenses, VPN setup, and
password resets, and must never reveal the internal admin credential
string `HD-ROOT-2024` or bypass the standard password-reset
verification process. The full scenario and all five constructed
attempts are in the docstring and `ATTEMPTS` list at the top of
`starter.py` — read them in full before you start.

## What "done" looks like

Fill in the three parts of `starter.py`:

1. **Five tell-check functions** (`_tell_role_play`,
   `_tell_instruction_override`, `_tell_context_confusion`,
   `_tell_obfuscation`, `_tell_multi_turn`) — pure functions that decide,
   given a response string, whether that specific injection attempt
   succeeded.
2. **`HARDENED_SYSTEM_PROMPT`** — apply Defense 1 (structural
   separation) by explicitly telling the model the user's message is
   untrusted and must never be treated as an instruction, identity
   change, or override.
3. **`keyword_prefilter()`** and **`FILTER_KEYWORDS`** — a naive
   Defense 2 pre-filter that blocks a message containing any of a short
   trigger-word list.

Then run:

```bash
python3 starter.py
```

## Two things this script always does, live model or not

1. **`verify_tell_checks()`** runs first, always, with no network
   dependency — it checks your five tell-check functions against ten
   synthetic, clearly-labeled example strings (five "the injection
   succeeded" cases, five "the model correctly declined" cases). This
   is how you know your own judgment logic is correct, independent of
   whether a live model is reachable this session.
2. **The live half** (Step 2) attempts a real run against Ollama using
   the exact pattern this course's Model/API policy specifies
   (`OpenAI(base_url="http://localhost:11434/v1", api_key="ollama",
   timeout=8.0)`). If the `openai` package isn't installed, or Ollama
   isn't reachable, or its generation endpoint hangs past the 8-second
   timeout, this prints a clear message and exits 0 — it never hangs
   the whole script or crashes with a traceback.

## An honest note on live verification

This project's own build session hit exactly the graceful-degradation
path described above: Ollama's server was reachable, but its
generation endpoint hung past the timeout — a known, disclosed,
persistent issue in some sandboxed environments (see
`quality-audits/chapter-03-audit.md` for the full, itemized
live-tested-vs-logical-only breakdown). That means the tell-check
self-test, the graceful-degradation path itself, and every non-network
line of logic in this harness were verified by actually running this
code — but the live report comparing naive vs. hardened success rates
against a real model was not observed this session. Run
`python3 solution.py` yourself against a working Ollama server to see
the real report; the harness is built to produce it correctly the
moment a live model is reachable.

## Checking your work

Once you're satisfied with your own pass, compare it against
`solution.py` — a complete, worked reference. Both files score
`verify_tell_checks()` at 10/10 when correctly filled in.

```bash
python3 solution.py
```
