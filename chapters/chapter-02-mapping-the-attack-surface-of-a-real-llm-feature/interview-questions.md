# Chapter 2 Interview Questions: Mapping the Attack Surface of a Real LLM Feature

Grouped by level — beginner, intermediate, senior, architect. Each includes
a strong answer, a red flag, a follow-up, and what the question actually
proves. This is the plain-text companion to `interview-questions.html`.

---

### 1. (Beginner) What are the first three steps of a systematic attack-surface enumeration, and why does the order matter?

**Strong answer:** Step 1 is enumerating every tool the model can call —
its parameters, what it actually does, and its blast radius. Step 2 is
enumerating every source of text that reaches the model's context: system
prompt, user input, conversation history, retrieved documents, and every
tool's output. Step 3 is classifying the trust level of each source from
Step 2 — who actually controls it. The order matters because you cannot
threat-model an asset you haven't written down yet; reasoning about risk
before the enumeration is complete is exactly how real findings get
missed, not because the reasoning was wrong but because the row never
existed.

**Red flag:** Jumps straight to "look for prompt injection" without being
able to describe the enumeration step that has to happen first.

**Follow-up:** "What's the difference between Step 2 and Step 3?"

**What this proves:** Understands that a threat model is built on a
complete inventory, not a search for the first interesting risk.

---

### 2. (Beginner) In the Waypoint trip-planning assistant, why does the free-text "description" field returned by `search_hotels` count as untrusted data, even though it comes back through Waypoint's own tool call?

**Strong answer:** A tool is a pipe, not a filter — the actual author of
the returned text is whoever is on the other end of the API, in this
case the hotel partner, not Waypoint's own engineering team and not the
traveler. Because that content re-enters the model's context on later
turns exactly like the system prompt or the user's message does, it has
to be trust-classified by who wrote it, not by which system happened to
fetch it.

**Red flag:** Says the data is trusted because "it's our own tool's
output" — confusing which system fetched the data with who authored its
content.

**Follow-up:** "Name one other tool output in Waypoint's system that has
the same property."

**What this proves:** Grasps that trust classification is about the
actual author of the content, not the mechanism that delivered it.

---

### 3. (Intermediate) Explain Mistake 1 from this chapter — under-scoping — using a concrete example from Waypoint.

**Strong answer:** Under-scoping is stopping the attack-surface
enumeration at the obvious user-input field (the traveler's chat
message) and never running the "does this tool's output re-enter
context" check against `search_flights` and `search_hotels`. Both
return partner-authored free text that gets appended to the same
context window the system prompt lives in. A compromised or careless
partner listing could embed an instruction-shaped string in its
"description" field, and Waypoint has no structural way to distinguish
it from a legitimate amenities note — the same mechanism as GreenCart's
return-reason field, just missed because "our own tool's data" doesn't
intuitively feel like a customer text box.

**Red flag:** Describes under-scoping only in the abstract, without
being able to point to the specific Waypoint asset (partner listing
text) that illustrates it.

**Follow-up:** "What step in the systematic method exists specifically
to catch this mistake?"

**What this proves:** Can connect a named failure mode to a concrete
system, not just recite a definition.

---

### 4. (Intermediate) Explain Mistake 2 — over-focusing — and why finding one real Prompt Injection path doesn't mean a threat model is complete.

**Strong answer:** Over-focusing happens when a team finds one genuine,
satisfying vulnerability (usually Prompt Injection, since it's the most
discussed category) and treats the review as done once that category
feels covered, without running the rest of the OWASP checklist against
the same complete asset list. In Waypoint, the uncapped, partner-billed
calls to `search_flights`/`search_hotels`/`get_destination_guide` (LLM10,
Unbounded Consumption) and the unverified third-party content feed
powering the destination guide (LLM03, Supply Chain) are just as real
and got zero attention from an injection-only review. A real system
almost never has exactly one category of gap.

**Red flag:** Treats "we found the prompt injection" as equivalent to
"the review is complete."

**Follow-up:** "What discipline in the seven-step method specifically
prevents this?"

**What this proves:** Understands that threat modeling is a
completeness exercise across the whole framework, not a single-finding
search.

---

### 5. (Senior) You're handed a real LLM feature with a tool list and minimal documentation, and one week to threat-model it before an audit. Walk through how you'd actually spend that week.

**Strong answer:** Spend the early part of the week purely on
enumeration, not risk analysis: build the full tool inventory (Step 1),
list every context source including every tool's output (Step 2), and
trust-classify each one (Step 3) — reading the actual implementation,
not just docstrings, since a tool's real behavior can differ from what
its name implies. Only after that's complete, cross-reference untrusted
sources against tools with real side effects (Step 4), specifically
re-check every tool output (Step 5), then run the full ten-category
OWASP checklist against the complete list (Step 6) before writing the
final table (Step 7) with justified likelihood/impact and an
architectural mitigation per row. The discipline is spending the
majority of the time on enumeration before opinion, because a wrong
opinion about a row you have is recoverable in review; a row that was
never written down usually isn't caught until an incident.

**Red flag:** Describes going straight for "the interesting attack,"
treating enumeration as a formality rather than the bulk of the real
work.

**Follow-up:** "What's the one enumeration step you'd refuse to skip
even under time pressure, and why?"

**What this proves:** Has internalized that systematic coverage, not
cleverness, is what makes a real audit trustworthy under time pressure.

---

### 6. (Senior) Two categories in Waypoint's threat model — LLM03 (Supply Chain) and LLM08 (Vector and Embedding Weaknesses) — both involve the same destination-guide vector store. How are they distinct risks, and why do they both need separate rows rather than being merged into one?

**Strong answer:** LLM03 is about whether the licensed third-party feed
itself was verified before being trusted — provenance and integrity at
ingestion time, independent of how it's later queried. LLM08 is about
whether the vector store's retrieval step enforces the access or
authority distinctions the underlying content actually has — in
Waypoint's case, whether editorial (vetted) and third-party (unvetted)
chunks are distinguishable at query time. A system could fix one without
fixing the other: verifying the feed's provenance at ingestion doesn't
add per-source tagging at query time, and adding query-time tagging
doesn't verify whether the feed was tampered with upstream. They need
separate rows because they have separate mitigations and separate
failure modes.

**Red flag:** Treats the two categories as redundant or merges them into
one finding, missing that a fix for one leaves the other's mitigation
unimplemented.

**Follow-up:** "If you could only fix one before launch, which would you
prioritize, and what residual risk remains?"

**What this proves:** Can distinguish mechanistically related but
independently-failing risks instead of collapsing the framework into
fewer categories than the system actually needs.

---

### 7. (Architect) You're setting a team-wide standard for what "attack surface enumeration complete" means before a threat model is allowed to move to the mitigation-design phase. What would that standard require, and how would you verify it was actually followed rather than just claimed?

**Strong answer:** The standard requires, in writing: a complete tool
inventory including each tool's real side effect and blast radius; a
complete context-source list including every tool whose output re-enters
context, explicitly marked; a trust classification for every source; and
an explicit pass/not-applicable note for all ten OWASP categories against
the resulting asset list — no category silently skipped. To verify it
was actually followed rather than claimed, require the artifact itself
(the tables) as the deliverable, not a summary paragraph, and spot-check
by picking one tool at random and asking the reviewer to walk its
real-world side effect and blast radius from memory — a reviewer who
skipped the enumeration step can't do this convincingly. The standard's
real enforcement mechanism is that the artifact makes the completeness
checkable, not that someone asserts it happened.

**Red flag:** Defines the standard only as a checklist item ("threat
model completed: yes/no") with no artifact that makes completeness
independently verifiable.

**Follow-up:** "How would you handle a team that produces a threat model
with the right shape but clearly skipped Step 5 (re-checking tool
outputs) — what's the actual tell?"

**What this proves:** Architect-level judgment — designs a process whose
completeness is verifiable from the artifact itself, not one that relies
on trusting a team's self-report.

---

### 8. (Architect) A tool's output that re-enters context (like Waypoint's partner listing text) and a retrieved RAG chunk are mechanistically very similar untrusted-data channels. Should an org's mitigation policy treat them identically, or does the distinction matter architecturally?

**Strong answer:** They're similar enough that the same base principle
applies to both — treat externally-authored text as inert data, never as
instructions, structurally separated from operator content — but they
differ enough in practice that a single policy without nuance under- or
over-mitigates one of them. A RAG chunk typically comes from a corpus
the org chose to index and can apply ingestion-time controls to
(provenance checks, access filtering, source tagging). A tool's live
output (a partner API response) is fetched at request time from a party
the org doesn't control the content of at all, and the only real lever
is runtime sanitization/delimiting, not ingestion-time vetting — there's
no "corpus" to audit in advance. A mature policy names both as the same
class of risk (externally-authored context, LLM01 entry point) but
prescribes different mitigations matched to where each one is actually
controllable: ingestion-time for RAG, request-time delimiting/sanitizing
for live tool output.

**Red flag:** Either claims they need completely different security
models (missing that both are the same underlying LLM01 mechanism), or
claims one identical mitigation covers both without adapting to where
each is actually controllable.

**Follow-up:** "Where would a cached tool-output value that gets reused
across sessions sit in this framework — closer to RAG or closer to a
live tool call?"

**What this proves:** Can reason about a framework at the level of
underlying mechanism while still adapting the concrete mitigation to
where control actually exists in a real architecture.

## Strategy Tips

- For every answer, be ready to point to a specific Waypoint asset (or
  name your own from a system you've worked on) rather than staying at
  the level of the category name alone.
- For senior/architect questions, the interviewer is listening for
  process — how you'd verify a threat model is actually complete, not
  just how you'd find one interesting bug.
- If you're new to security interviews: walking through the seven-step
  method out loud, in order, is a legitimate and strong way to answer
  almost any question in this bank — that's exactly what the method is
  for.
