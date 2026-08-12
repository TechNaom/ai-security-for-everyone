# Chapter 10 Interview Questions: Securing Agentic Systems Against Adversarial Tool Output

Grouped by level — beginner, intermediate, senior, architect. Each
includes a strong answer, a red flag, a follow-up, and what the question
actually proves. This is the portable source for `interview-questions.html`
— both files carry identical question text, answers, red flags,
follow-ups, and "what this proves" content.

---

## 1. (Beginner) A colleague says "we already covered Excessive Agency in Chapter 1, isn't this chapter just repeating that?" How would you explain the actual difference?

**Strong answer:** Chapter 1 named the shape of the harm using GreenCart's
unbounded refund tool as a single worked example — excessive
functionality, excessive permissions, excessive autonomy, all three
present in one incident triggered by the model's own unprompted
judgment. This chapter answers a narrower, deeper question: what happens
specifically when Excessive Agency gets *triggered* by an adversarial
tool result, not by the model just deciding on its own? Chapter 8's own
Category 3 drew a further, adjacent line: the decision to connect a tool
in the first place (Chapter 8's territory) versus an agent's runtime
defense against an already-connected tool's adversarial result (this
chapter's). Chapter 1 named the concept once; this chapter is the full
depth on one specific, common trigger for it.

**Red flag:** Can't distinguish "Excessive Agency in general" from "Excessive
Agency triggered specifically by a manipulated tool result," or conflates
this chapter's scope with Chapter 8's adoption-time trust decision.

**Follow-up:** "Name the three moments in a tool call's round trip this
chapter uses, and explain why Chapter 1's GreenCart example didn't need
that framing."

**What this proves:** Understands how a later chapter can deepen a
narrow slice of an earlier chapter's concept without repeating or
contradicting it.

---

## 2. (Beginner) Explain, in your own words, why "a tool result is often a structured object with fields of differing trust" is the key wrinkle this chapter has that Chapter 9's RAG chapter didn't need.

**Strong answer:** A RAG chunk is usually one atomic block of text from
one source — Chapter 9's defenses could reasonably treat "the chunk" as
the unit of trust. A tool's JSON response is frequently a mix: some
fields are structured, enum-like, and system-generated (like Ferngate's
`status` field, trustworthy by construction), while other fields are
free text populated by whoever last interacted with the underlying
record (like `delivery_notes`). Treating the whole response as equally
trustworthy misses that the enum field deserves high trust; treating the
whole response as equally suspect wastes the genuinely reliable fields a
user needs. A real defense has to reason field-by-field, which is
exactly why this chapter needed its own Defense 4 (field-level
provenance tagging) that Chapter 9 didn't need in the same form.

**Red flag:** Treats a tool result the same way as a RAG chunk (a single
undifferentiated trust unit), or can't explain concretely why a JSON
response's fields can carry different trust levels.

**Follow-up:** "If Ferngate's carrier API only ever returned a single
free-text field with no structured fields at all, would field-level
provenance tagging still matter? Why or why not?"

**What this proves:** Understands the actual mechanism-level difference
between a RAG chunk and a tool result well enough to explain why one
chapter's defense set needed a genuinely new piece.

---

## 3. (Intermediate) A team says: "We use function/tool-calling APIs with proper message roles, so tool output can't be mistaken for a real instruction." Evaluate this claim.

**Strong answer:** Overclaimed, and it's the exact "we added a control,
ticket closed" trap this course has named repeatedly. Putting a tool
result inside a correctly-labeled `"tool"`-role message is necessary
scaffolding, not a content-level defense — a role label changes which
part of the conversation history a message sits in; it says nothing
about whether the text inside that message gets treated as reference
information or as an instruction once the model reads it. Ferngate's own
Dispatch Copilot did exactly this: `delivery_notes` sat inside a proper
tool-role message, and it made no difference, because nothing about the
message's content told the model the field was customer-submitted free
text, never a system directive. Real content-level reinforcement
(Defense 3) has to be added deliberately.

**Red flag:** Treats message-role structure as a sufficient defense on
its own, or can't explain the difference between "where a message sits
in the conversation" and "how its content gets weighted."

**Follow-up:** "Given that role structure alone isn't enough, what
specifically would you add to Dispatch Copilot's prompt-assembly code to
close this gap?"

**What this proves:** Can distinguish necessary infrastructure from an
actual content-level mitigation, the same distinction Chapter 9's
Defense 2 required for un-acted-on trust tags.

---

## 4. (Intermediate) Ferngate's engineering lead wants to fix the near-miss with a single hardcoded rule: "never let Dispatch Copilot call `issue_reship_credit` for amounts over $50 without a human clicking approve." Is this a sufficient fix?

**Strong answer:** No — it's a real, useful piece of Defense 6, but it
leaves every other defense in this chapter unimplemented, the exact
single-attempt trap this course has named in every module so far.
`delivery_notes` is still concatenated raw into context with no
sanitization or structural framing (Defenses 2 and 3); the tool call
itself still carries ambient authority with no permission scoping
distinguishing "read status" from "propose a credit" (Defense 5); and a
dollar cap on one named tool's one parameter doesn't generalize to the
next side-effecting tool Ferngate adds six months from now. A real fix
needs schema validation and sanitization at result arrival, structural
separation and provenance tagging at context assembly, and permission
scoping plus the human-in-the-loop backstop at action proposal — layered
together, not a single patch on one tool.

**Red flag:** Accepts the dollar cap as a complete fix, or doesn't
recognize it as addressing only one moment (action proposal) of three.

**Follow-up:** "Which of the six defenses would you implement first,
given limited engineering time, and why that one specifically for
Ferngate's situation?"

**What this proves:** Recognizes a single hardcoded rule as a partial fix
at one moment rather than a complete posture, and can reason about
layering the remaining five defenses.

---

## 5. (Senior) Design a field-level provenance-tagging scheme (Defense 4) for a tool whose response schema you don't fully control (a third-party partner API that could add new fields at any time). What makes this genuinely hard?

**Strong answer:** The hard part is that Defense 1's schema validation and
Defense 4's provenance tagging both depend on knowing, in advance, which
fields exist and which trust tier each belongs to — but a third-party
partner API can add a new field at any time without warning, and a
naive implementation either (a) silently passes an unrecognized field
through with no trust tag at all (defeating the purpose), or (b) breaks
entirely on an unexpected field (an availability cost). A working design
needs a default-deny posture for unrecognized fields specifically:
any field not in the known schema gets tagged low-trust and flagged for
review by default, rather than either passed through untagged or
causing a hard failure — the same "default-deny, not default-allow"
principle Chapter 9's own architect-level interview question named for
a privileged-action policy list. This also needs a monitoring signal:
alert when the partner API starts returning a field the schema doesn't
recognize, so a human reviews and classifies it before it becomes
routine, unreviewed traffic.

**Red flag:** Proposes a static schema with no handling for unexpected
fields, or assumes the partner API's shape is guaranteed stable.

**Follow-up:** "Six months in, the partner adds a new `internal_flags`
field that turns out to be genuinely useful, high-trust, system-set
data. Walk me through how it gets promoted out of the low-trust default
tier."

**What this proves:** Recognizes that a schema-dependent defense has a
real maintenance and drift problem against an API you don't control, and
can design a default-deny posture with a real promotion path rather than
a one-time static list.

---

## 6. (Senior) A team argues that permission/capability scoping (Defense 5) alone is sufficient, since scoping `track_shipment` to read-only, tracking-only authority would have prevented Ferngate's incident. Evaluate this as a sole strategy.

**Strong answer:** Insufficient as a sole strategy, though it's a real,
structurally important control for a different, specific risk.
Permission scoping stops the structural root of Ferngate's incident — a
single agent session carrying ambient authority over both a read-only
lookup tool and a side-effecting financial tool. But it says nothing
about a legitimately-scoped, high-consequence tool being called with a
manipulated argument: if `issue_reship_credit` is itself a tool the
agent has legitimate, scoped authority to call for genuine exception
handling, permission scoping alone doesn't stop a manipulated tool
result from choosing to call it with an attacker-favorable amount or
account. That's specifically what Defense 6 (human-in-the-loop plus the
hard rule that no tool result can itself authorize a privileged action)
is for — permission scoping answers "can this session reach this tool at
all," Defense 6 answers "should this specific call, with these specific
arguments, actually execute."

**Red flag:** Treats permission scoping as equivalent to argument-level
safety, or can't name the specific gap it leaves (a scoped-but-still-
callable tool receiving a manipulated argument).

**Follow-up:** "Given permission scoping alone doesn't solve manipulated
arguments to a legitimately-scoped tool, which single additional
defense closes the most risk for `issue_reship_credit` specifically?"

**What this proves:** Can precisely scope a structural control's real
guarantee (session-level tool reachability) against a different,
unaddressed risk (call-level argument manipulation) rather than treating
"scoping" as a general-purpose security word.

---

## 7. (Architect) You're advising a company building a new agentic system from scratch, giving the agent several tools including at least one side-effecting one, informed by InjecAgent's 24% and AgentDojo's ~48% measured attack-success rates against strong, widely-deployed models. How would this shape your architecture decisions before a single tool is wired up?

**Strong answer:** Those numbers mean tool-output injection isn't a rare
edge case against a weak model — it's a measured, substantial risk
against strong, current models, which rules out any architecture that
treats "we're using a capable model" as itself protective. From day one,
I'd architect: (1) every tool call scoped to the narrowest credential
that specific call needs, with no tool call's result able to expand
what the agent is authorized to do next (Defense 5, as a default
architectural property, not a retrofit); (2) a schema-and-trust-tier
contract required for every tool's response before it ships, with
default-deny for unrecognized fields (Defenses 1 and 4); (3) structural
separation as the default prompt-assembly pattern for every tool result,
with no code path doing naive concatenation even for "obviously safe"
internal tools (Defense 3); (4) a hard, application-layer rule — no
tool result can itself authorize a side-effecting action — enforced
independent of the model, non-negotiable from day one (Defense 6's core
rule); (5) sandboxed execution with hard rate and value limits on every
side-effecting tool call from launch, not added after an incident. The
overarching principle: given AgentDojo's own ~48% figure against a
strong model, I'd assume any sufficiently capable agent with
side-effecting tools will eventually face a manipulated tool result, and
design the architecture so that event is contained rather than
catastrophic, not as an edge case to patch later.

**Red flag:** Treats model capability as inherently protective against
tool-output injection, or proposes adding these controls only after an
incident rather than as day-one architecture.

**Follow-up:** "Your product team wants to launch in four weeks and
argues the full six-defense stack is too much for an MVP. What's the
minimum viable subset you'd insist on, and what would you explicitly
document as accepted residual risk?"

**What this proves:** Architect-level judgment — translates measured
research findings from two independent benchmarks into concrete,
from-the-start architectural decisions across an entire agentic system,
not a single bolted-on control.

---

## 8. (Architect) This chapter's Defense 6 warns that a human-in-the-loop confirmation step can become rubber-stamped through habituation once dispatchers see "confirm" prompts dozens of times a day. Design a confirmation-scoping policy that avoids this failure mode for a real system with many tools.

**Strong answer:** A real, operable policy needs: (1) a formal,
versioned privileged-action classification (the same governance pattern
Chapter 9's own architect-level answer named) so confirmation prompts
only fire for genuinely high-consequence actions — irreversible,
financial above a defined threshold, or affecting someone other than the
requester — not every single tool call; (2) confirmation prompts that
surface the SPECIFIC reason an action is flagged (e.g., "this credit
amount exceeds the routine threshold" or "this action was proposed based
on a tool result, not your own explicit request"), not a generic "are
you sure?" that trains users to click through without reading; (3)
periodic auditing of confirmation-approval rates and time-to-approve —
a rate approaching 100% approval with near-instant approval times is
itself a signal of habituation, worth flagging even if no incident has
occurred yet; (4) routing genuinely rare, high-consequence confirmations
to a different reviewer or review pattern than routine ones, so the
volume of any one person's prompts stays low enough to preserve genuine
attention. The honest limit to state alongside this design: scoping
confirmations narrowly reduces habituation risk but doesn't eliminate
it — a sufficiently rare but real high-consequence action can still get
rubber-stamped if the reviewer's context has drifted, which is why
auditing approval patterns (3) matters as an ongoing check, not a
one-time design decision.

**Red flag:** Proposes confirming every single tool call (guaranteeing
habituation) or removes confirmation for anything below an arbitrary
threshold with no monitoring for approval-pattern drift.

**Follow-up:** "An audit six months in shows confirmation approval rates
at 99.7% with a median approval time of 1.2 seconds. Walk me through
what you'd change, and how you'd tell the difference between 'the
policy is well-calibrated and correctly approves almost everything' and
'this is habituation.'"

**What this proves:** Can design a genuinely operable human-in-the-loop
policy that accounts for real human behavior under repeated exposure,
not just a theoretical "add a confirmation step" answer — architect-
level systems thinking about a control's actual failure mode over time.

---

## Strategy tips

Keep the three-moment round-trip model (result arrival / context
assembly / action proposal) sharp, and be ready to name which moment a
given scenario's failure lives at, and which of the six defenses attaches
to that moment specifically. Be ready to state each defense's honest
limit, not just what it catches — especially that permission scoping
(Defense 5) addresses session-level tool reachability, not call-level
argument manipulation, and that structural separation (Defense 3) is a
reliability improvement, not a hard guarantee. For senior/architect
questions, the interviewer is listening for layered, moment-aware
thinking, an explicit residual-risk posture, and — at the architect
level — a from-the-start architectural design that treats InjecAgent's
and AgentDojo's measured attack-success numbers as a reason to assume a
manipulated tool result is a "when," not an "if," plus a real, operable
process for keeping a human-in-the-loop control from degrading through
habituation.
