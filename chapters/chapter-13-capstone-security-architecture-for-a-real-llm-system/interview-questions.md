# Chapter 13 Interview Questions: Capstone: Security Architecture for a Real LLM System

Grouped by level — beginner, intermediate, senior, architect. Each
includes a strong answer, a red flag, a follow-up, and what the question
actually proves. This is the portable source for `interview-questions.html`
— both files carry identical question text, answers, red flags,
follow-ups, and "what this proves" content.

---

## 1. (Beginner) What's the difference between the kind of report Chapter 11 taught you to write and the kind of document this chapter's capstone requires?

**Strong answer:** Chapter 11's findings report documents what you found
by testing a system that already exists -- specific, reproducible
vulnerabilities, each with a severity rating and a recommended fix.
This chapter's Architecture Decision Records document a design *choice*
made before the system exists in that form: the context that forced the
decision, the option chosen, the alternatives seriously considered and
rejected, and the trade-offs accepted. A findings report is diagnostic,
written after the fact; an ADR is a justification, written before or
alongside the decision it explains. The capstone actually needs both --
ADRs for the design, plus a red-team pass (Chapter 11's methodology,
reused) against that design before it's finalized.

**Red flag:** Treats a findings report and an ADR as the same kind of
document, or can't explain why a capstone needs both rather than just
one or the other.

**Follow-up:** "If your ADR set is complete and well-reasoned, why does
this chapter still require a red-team pass against your own design on
top of it?"

**What this proves:** Understands the distinct purpose of two document
types this course built across Modules 5 and 6, and why a real
architecture review needs both, not either.

---

## 2. (Beginner) Cinderpeak's VP asks why this chapter's hook has no incident, unlike every prior chapter. What's a good answer?

**Strong answer:** Every incident-driven hook in Chapters 1-12 taught a
failure by showing it happen first -- effective for learning mechanism.
This chapter deliberately has no incident because the skill being taught
is designing a system's defenses before a version of it exists to fail,
not diagnosing a failure after it happens. An incident hook here would
let you pattern-match "this looks like an earlier chapter's problem"
instead of building a threat model from a blank system description,
which is how a real pre-launch architecture review actually starts.

**Red flag:** Can't articulate why the missing incident is a deliberate
pedagogical choice rather than just a different flavor of story, or
assumes this chapter must be inventing entirely new attack mechanisms
since there's no incident to reuse.

**Follow-up:** "Does the lack of an incident mean this chapter teaches
new attack mechanisms Chapters 1-12 didn't cover?"

**What this proves:** Understands that the incident-first pattern was a
deliberate teaching device in prior chapters, not a structural
requirement -- and that this chapter's break from it is itself
meaningful, not accidental.

---

## 3. (Intermediate) Write a one-paragraph ADR-style justification for applying context-aware output encoding unconditionally at every render surface in a multi-tenant LLM platform, including the real trade-off it accepts.

**Strong answer:** Decision: apply context-aware output encoding
unconditionally at every render surface, with no exception for the
model's own generated text, because the render surface cannot
distinguish human-typed content from model-generated content and a
model can carry forward a payload from content it read without ever
"misbehaving." Alternative rejected: a detection-based scanner for
script-like patterns, rejected as the primary control because it has a
real false-negative rate on payload shapes it wasn't written to catch --
a category-mismatch error, using a detection claim to justify skipping a
structural control. Trade-off accepted: unconditional escaping breaks
legitimate rich formatting the model sometimes generates; the real fix
is a narrow, pre-approved safe-formatting subset (bold, italics, lists)
rendered through a renderer with no code-execution path by construction,
not disabling escaping to preserve formatting.

**Red flag:** States the decision without naming a real rejected
alternative or a real accepted cost, or proposes a detection-based
scanner as sufficient on its own.

**Follow-up:** "A tenant complains that legitimate Markdown formatting
in their generated replies now displays as literal asterisks and
brackets instead of rendering. Does this reveal a flaw in the ADR, or a
gap in its implementation?"

**What this proves:** Can produce real ADR-quality reasoning on demand,
not just recite the format -- states a real alternative, a real
rejection reason, and a real, honestly-priced trade-off.

---

## 4. (Intermediate) A junior engineer proposes running every one of Aegis Copilot's tools -- first-party and third-party plugins alike -- inside full container sandboxes, arguing "more isolation is always safer." Evaluate this proposal.

**Strong answer:** More isolation isn't free, and applying it uniformly
ignores that Aegis Copilot's two tool populations have genuinely
different risk profiles. First-party tools are a small, reviewed set
with a known argument schema; their real risk is adversarial arguments
reaching a legitimate tool, which schema validation and allow-list
checks already close -- full sandboxing there adds real latency and
operational complexity for a risk that's already handled. Third-party
marketplace plugins run arbitrary code from developers Cinderpeak has
never vetted; schema validation does nothing there because the risk is
the plugin's own code, not a malformed field, so genuine execution
isolation is the only control that actually matches that threat. The
correct rule is "sandbox exactly where structural and detection controls
structurally cannot reach," not "sandbox everything" or "sandbox
nothing."

**Red flag:** Treats "more isolation" as an unqualified good with no
cost, or can't distinguish the two tool populations' actual risk
profiles.

**Follow-up:** "Six months after launch, a first-party tool starts
accepting a new argument type that lets a tenant supply an arbitrary
script to run as a post-processing step. Does your original sandboxing
decision for first-party tools still hold?"

**What this proves:** Can reason about a security control's real cost
against a specific threat model rather than applying a blanket "more
security is always better" heuristic -- the sandboxing-tradeoff judgment
this chapter's brief specifically requires.

---

## 5. (Senior) You're reviewing a colleague's completed capstone-style architecture review. It has six well-reasoned ADRs and a red-team section that reports zero findings. What's your assessment?

**Strong answer:** Zero findings against a set of freshly written ADRs
is a red flag, not a compliment. An ADR can be internally well-reasoned
and still leave a residual gap it doesn't surface on its own, precisely
because the person writing the ADR is grading their own homework --
that's the entire reason a self-directed red-team pass is required
separately from the ADRs themselves, mirroring Chapter 6's and Chapter
7's own honest disclosures that every defense this course taught has a
stated, non-zero limit. A rigorous pass against six real design
decisions almost always surfaces at least one genuine gap -- for
example, whether a human-approval step gates only a tool call's
recipient/target or also its content. Zero findings most likely means
the red-team pass wasn't actually adversarial, not that the design is
flawless.

**Red flag:** Accepts zero findings at face value as evidence of a
strong architecture, or can't explain why a self-audited design
without independent findings should be treated with suspicion.

**Follow-up:** "The colleague argues their ADRs were unusually
thorough, which is why nothing new turned up. How would you actually
test that claim rather than take it on faith?"

**What this proves:** Applies this course's honest-limits discipline
(Chapters 5, 6, 7) to a self-graded deliverable, recognizing that a
suspiciously clean result is evidence of insufficient rigor, not
success.

---

## 6. (Senior) Explain how the OWASP GenAI LLM Top 10 2026's LLM10:2026 Improper Output Handling category applies differently to Aegis Copilot's customer-facing chat widget than it did to TicketSense's purely internal dashboard in Chapter 12.

**Strong answer:** The mechanism is identical -- generated text
rendered without context-aware encoding, carrying forward a payload from
content the model read. What changes is blast radius and audience.
TicketSense's dashboard was internal-only, so a rendered-output injection
reached Fenwick's own agents. Aegis Copilot's chat widget is embedded on
each tenant's own public-facing website, so the same failure reaches an
end user entirely outside Cinderpeak -- a strictly larger and less
controllable audience. The payload's possible origin also changes: on a
multi-tenant platform sharing one base model, there's a theoretical path
for one tenant's ingested content to influence generation patterns that
surface in a different context, which raises the stakes of getting
output encoding right even though the render-time fix (unconditional,
context-aware encoding) doesn't change at all. Same defense, higher-
consequence failure if it's missing.

**Red flag:** Treats the two scenarios as requiring different technical
defenses, or fails to identify that the audience/blast-radius change
(internal staff vs. external customer) is what actually escalates the
risk, not a change in mechanism.

**Follow-up:** "Does the audience difference change which of Chapter
5's three defense categories (structural, detection, consequence-
bounding) is the right primary control here, or only how urgently it
needs to be implemented?"

**What this proves:** Can generalize a mechanism learned in one context
(Chapter 12) to a structurally similar but higher-stakes context
(a multi-tenant, customer-facing platform), and correctly separates
"the defense changes" from "the urgency changes."

---

## 7. (Architect) Design the launch-readiness recommendation format for a pre-GA security architecture review that found some blocking issues, some accepted residual risks, and some OWASP categories the team couldn't confidently rate at all. Why shouldn't this collapse to a single GO/NO-GO decision?

**Strong answer:** A single GO/NO-GO bit destroys the information the
review was built to produce, because it forces three genuinely different
situations into one signal. Blocking findings (a gap that defeats an
ADR's own stated purpose, like a human-approval step that only checks a
tool call's recipient and not its content) require a fix before launch,
full stop. Accepted residual risks (a real, understood, low-probability
gap where full elimination would cost more than the risk justifies, like
a narrow re-identification risk in an aggregated cross-tenant report)
require monitoring and a documented acceptance, not a blocker. Categories
the team couldn't confidently rate (this course's own honest gap on
Unbounded Consumption and Misinformation) require a follow-up review by
someone with more depth in that category before the team can honestly
claim confidence either way -- treating an unrated category as either
"pass" or "fail" is dishonest in both directions. The right format is a
prioritized list with explicit categories -- must-fix, accepted and
monitored, needs follow-up review -- not a single bit.

**Red flag:** Proposes a binary launch decision, or can't distinguish
"we know this is a real risk we're choosing to accept" from "we don't
actually know how risky this is yet."

**Follow-up:** "The VP of Engineering wants a single slide with one
launch/no-launch answer for a board presentation. How do you preserve
the three-way distinction while still giving them something they can
present in thirty seconds?"

**What this proves:** Architect-level judgment -- can design a
decision-communication format that preserves real distinctions under
pressure to oversimplify, rather than collapsing nuanced risk assessment
into a false binary to satisfy a stakeholder's preference for simplicity.

---

## 8. (Architect) A stakeholder argues that since this course spent twelve chapters building deep, mechanism-specific expertise, a truly rigorous capstone should require equally deep, specialist-level treatment of all ten OWASP 2026 categories before an architecture can be called "reviewed." Evaluate this standard against what this chapter actually requires.

**Strong answer:** The stakeholder's standard sounds more rigorous but
is actually less honest and less useful in practice. This course itself
only built genuine dedicated depth on eight of the ten 2026 categories;
demanding uniform specialist-level treatment across all ten would force
either fabricating confidence the reviewer doesn't have on the other two,
or blocking any review from ever completing because no team's expertise
is ever perfectly uniform across a full framework. What this chapter
actually requires -- rate every category using the framework, apply real
depth where the team has it, and explicitly flag where it doesn't rather
than papering over the gap -- produces a more trustworthy artifact
precisely because it's honest about its own limits, the same standard
Chapter 5 set for evaluating a vendor's defense claims, now turned on the
review team's own coverage. A review that honestly flags two categories
as "needs follow-up" is more useful to a real launch decision than one
that confidently, but falsely, claims uniform depth it doesn't have.

**Red flag:** Agrees that uniform specialist depth is achievable or
required for a review to be "real," or can't connect this back to the
course's own honest-limits discipline established since Chapter 5.

**Follow-up:** "How would you actually resource the 'needs follow-up
review' categories without blocking the GA launch date entirely -- what
does a real organization do with that gap in the two weeks before
shipping?"

**What this proves:** Architect-level judgment on evaluating what
"rigorous" actually means for a review artifact -- can defend an
honestly-limited standard against a surface-level argument that more
uniform confidence would automatically be better, the same
"justify the choice, don't just chase the appearance of rigor"
discipline this course has required at the architect level since
Chapter 11.

---

## Strategy tips

Keep the ADR format straight in your head -- context, decision,
alternatives considered and rejected, trade-offs accepted, consequences
-- and be ready to tag any defensive decision with the correct one of
Chapter 5's three categories (structural, detection, consequence-
bounding) and justify why that category fits. Be ready to explain why
this chapter's hook has no incident and why that's deliberate, why a
self-red-team pass reporting zero findings is suspicious rather than
reassuring, and why the sandboxing decision for third-party plugins
differs from the one for first-party tools. For senior/architect
questions, the interviewer is listening for the same honest-limits
discipline this course has required since Chapter 5 — applied here not
just to a single defense's claims, but to an entire review's own
coverage and to how a launch recommendation communicates genuinely
different categories of risk without collapsing them into a false
binary.
