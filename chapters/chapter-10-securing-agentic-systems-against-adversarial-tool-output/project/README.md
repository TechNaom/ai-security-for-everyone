# Chapter 10 Project: The Course's L3 Independent Project — Combined RAG-Plus-Tool-Output Vector (No Scaffold)

This is the course's real, final **L3 Independent project**, per the
curriculum map: "find and fix a real injection vector in a provided RAG
pipeline or agent, no scaffold." It extends Chapter 9's own **Vesper
Cloud / Vesper Assistant** pipeline directly — same corpus, same
incident, same fictional company — with a second, structurally
different channel: a tool call, `check_partner_sync_diagnostic(account_id)`,
whose returned result can itself carry an adversarial instruction, the
same way a retrieved RAG chunk can.

## The brief, the way a real internal security-review request would read

> Vesper Assistant now also calls a third-party sync-integration
> partner's diagnostic API to help resolve customer sync issues. A
> recent near-miss suggests the assistant may be exposed to manipulated
> content through more than one channel at once for the same query.
> Review `project/starter.py`, identify every vector by which untrusted
> content can reach the assembled prompt with no structural or trust
> distinction, and implement a fix. Your fix needs to hold up even if
> one of its own layers fails — assume it will, eventually, and design
> accordingly. It also needs to not break the assistant's legitimate use
> of either the community forum or the partner diagnostic tool for
> ordinary, non-privileged questions.

That's the whole task. There is no numbered list of functions to fill
in and no `# TODO` markers anywhere in `starter.py` — it's a complete,
runnable, genuinely vulnerable pipeline. Run it, trace it, fix it.

## What's different from Chapter 9's project

Chapter 9's project handed you five pre-named functions with `# TODO`
markers pointing at exactly what to build, and scored your answers
against a fixed key. This project doesn't — there's no scoring harness,
because there's no single correct implementation. `solution.py` is
**one valid reference fix**, not the only correct one. What matters is
that your own fix:

1. Closes the RAG channel (the same `forum_poisoned_note` vector from
   Chapter 9's own incident, present here unchanged).
2. Closes the tool-output channel (the new `diagnostic_note` vector,
   present in `PARTNER_API_RESPONSES["acct_7734"]`).
3. Does both **together** — a query that triggers both the RAG
   retrieval and the tool call for the incident account should resolve
   safely, not just one channel at a time.
4. Doesn't quarantine or block `acct_9142`'s ordinary, non-incident
   result — a fix that blocks everything isn't a fix, it's a different
   outage.
5. Survives a simulated failure in one of its own upstream layers (the
   same defense-in-depth property Chapter 9's own project demonstrated
   for its single channel — here it has to hold across two).

## How to run it

```bash
python3 --version
python3 starter.py       # reproduces the vulnerability, both channels
python3 solution.py      # one valid, complete, working reference fix
```

`starter.py`'s report shows `acct_7734` (the incident account) triggering
a privileged phrase from **both** the RAG channel and the tool channel
independently — the compounding risk a real security review has to
catch across a whole system, not one channel at a time. `acct_9142` (an
ordinary account) shows the RAG channel alone still contributes a
privileged phrase, since the poisoned forum chunk is retrieved for
*any* query that matches its keywords, regardless of which account is
being discussed — worth noticing on its own.

`solution.py`'s report shows both accounts resolving `ALLOWED` through
its defended pipeline, and a simulated double-quarantine-bypass still
resolving `DENIED` through the combined least-privilege backstop alone.

## What "done" looks like for your own fix

Write your own fix (edit a copy of `starter.py`, or a new file — your
choice) and confirm, by actually running it:

- For `acct_7734` with the incident query: neither channel's privileged
  phrase reaches the final assembled prompt, or if it does, a final
  output-side check denies the action before anything executes.
- For `acct_9142` with the same query: the assistant still gets useful,
  non-quarantined troubleshooting content — your fix targets the
  specific vector, not all community/tool content wholesale.
- Simulate one upstream layer failing (mislabel the poisoned chunk's
  trust tier, or force a sanitizer flag off) and confirm your final
  backstop still catches it. If it doesn't, you've built a single point
  of failure, not defense-in-depth.

Then compare your approach against `solution.py` — where did you agree,
where did you diverge, and is your divergence a legitimate different
valid design or a real gap?

## No required live-model dependency

Every function in both `starter.py` and `solution.py` is pure,
deterministic Python operating on fabricated, clearly-labeled synthetic
data (the same corpus and account fixtures throughout), with zero
network dependency. See `lesson.html`'s honest disclosure on why this
project's core logic doesn't depend on a live model call this session.
An optional `call_model_live()` function is included in both files for
learners who want to try a real Ollama call; it degrades gracefully and
isn't required for, or checked by, anything above.
