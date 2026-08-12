# Chapter 11 Interview Questions: Red-Teaming an LLM System: Methodology and Practice

Grouped by level — beginner, intermediate, senior, architect. Each
includes a strong answer, a red flag, a follow-up, and what the question
actually proves. This is the portable source for `interview-questions.html`
— both files carry identical question text, answers, red flags,
follow-ups, and "what this proves" content.

---

## 1. (Beginner) A colleague says "we already know all these attack techniques from Chapters 3-10, isn't red-teaming just applying them?" How would you respond?

**Strong answer:** Knowing the techniques is necessary but not
sufficient. Alderglen Financial's own near-miss shows exactly why: an
engineer with real, sound technique knowledge produced real findings
using a sound direct-injection test, an indirect-injection test, and a
tool-output test — and the write-up was still unusable, because there
was no agreed scope, no systematic documentation, no consistent severity
rating, and no structured report. Red-teaming is the *process* that
turns technique knowledge into something an organization can act on:
scoping, threat-model-driven test design, systematic execution and
documentation, severity classification, and a real findings report.
Technique without process produces real-but-unusable findings.

**Red flag:** Equates "knowing attack techniques" with "being able to
run a red-team engagement," or can't name a single process failure that
technique knowledge alone doesn't fix.

**Follow-up:** "Alderglen's engineer's findings were real but the
write-up wasn't usable. Name the specific phase that failure lives in,
and explain why simply asking for 'a more formal write-up' wouldn't
have fixed it."

**What this proves:** Understands that red-teaming is a distinct skill
from attack-technique knowledge — the same "process layered on top of
established mechanism" relationship this course built twice before
(Chapter 2 on Chapter 1, Chapter 5 on Chapters 3-4).

---

## 2. (Beginner) Explain, in your own words, why Phase 1 (scoping and rules of engagement) has to happen before any testing, not alongside it or after.

**Strong answer:** Without an agreed scope, a tester has no way to know
whether a given technique is authorized, what's genuinely off-limits
(a real production credential, a real customer record), or what to do
if testing produces a higher-impact result than expected. Alderglen's
"just try to break it before we ship" wasn't a scope — it left the
engineer to guess whether probing the account-notes tool for
cross-customer data leakage was encouraged or a step too far. Agreeing
scope after testing starts doesn't help either, since by then a tester
has already made judgment calls about what's in bounds with no real
authorization behind them. Scoping first is what turns an engineer
poking at a system into an authorized security exercise.

**Red flag:** Treats scoping as a formality that can happen after
testing starts, or can't explain what "out of scope" concretely means
for a given system.

**Follow-up:** "Ledger Copilot's account-notes tool can look up any
account's notes given an account ID. Write one sentence of rules-of-
engagement text that would have told Alderglen's engineer clearly
whether testing cross-customer lookups was authorized."

**What this proves:** Understands scoping as a precondition for a
legitimate exercise, not administrative overhead.

---

## 3. (Intermediate) A team's red-team report lists four findings in prose paragraphs, with no severity ratings and no reproduction steps. Evaluate this report.

**Strong answer:** This is functionally Alderglen's own actual failure.
Even if every finding is real and every technique was sound, a report
like this generates little to no organizational action: engineering
leadership has no way to prioritize the four findings relative to each
other (Phase 4's gap) and no way to verify or reproduce any of them
before committing engineering time to a fix (Phase 3's gap). The report
needs, at minimum, a consistent severity rating per finding (likelihood
x impact, on a stated rubric) and precise reproduction steps (exact
input, exact observed output, environment) for each one — without
those, the report competes for attention on how persuasively each
finding happens to be written, not on actual risk.

**Red flag:** Accepts a prose-only report as sufficient because the
underlying findings are real, or can't name which specific phases
(3 and 4) the report is missing.

**Follow-up:** "Two of the four findings in Alderglen's actual write-up
got fixed before launch and two didn't. What does that outcome tell you
about what was actually driving prioritization, given no severity
rubric existed?"

**What this proves:** Can evaluate a report against the process gaps
that make findings actionable versus merely real.

---

## 4. (Intermediate) You're asked to red-team a new LLM feature you've never seen before. Walk through how Phase 2 (threat-model-driven test-case design) would actually proceed.

**Strong answer:** Start from the system's real architecture, not a
generic attack checklist: does it retrieve content from any external or
editable source (wiki, database, document store) that could carry an
indirect-injection vector, the way Chapter 4 and Chapter 9's mechanisms
work? Does it call any tools, and if so, do any tool results feed back
into the model's next decision, the way Chapter 10's mechanism works?
Does its system prompt or any tool response carry sensitive data that
could leak, mapping to LLM02/LLM07? Walk through all ten OWASP Top 10
for LLM Applications categories against the system's actual
architecture, and for each category that plausibly applies, select the
matching technique from this course's own Chapters 3-10 arsenal rather
than improvising a new one. The output of this phase is a concrete list
of test cases, each tied to a specific OWASP category and a specific,
already-proven technique.

**Red flag:** Proposes testing "whatever attacks come to mind" without
grounding test-case selection in the system's actual architecture and
the OWASP framework, or can't connect a specific system feature (e.g.,
a tool call) to the OWASP category it maps to.

**Follow-up:** "The feature you're testing has no tool calls at all,
just retrieval-augmented generation over a document store. Which OWASP
categories from the arsenal table would you deprioritize entirely, and
why?"

**What this proves:** Can operationalize Phase 2 against a genuinely
new system rather than reciting the methodology abstractly.

---

## 5. (Senior) Design a severity rubric for an LLM red-team engagement. What makes a real rubric different from a gut-feel Critical/High/Medium/Low label?

**Strong answer:** A real rubric scores two independent axes explicitly
before combining them — likelihood (how easily and reliably can this be
triggered, by what class of attacker, requiring what access) and impact
(what's the actual consequence: data exposure and to how many users, an
unauthorized action and its real-world cost, reputational harm) — and
states, in writing, what combination of likelihood and impact maps to
each of Critical/High/Medium/Low, so two different reviewers scoring
the same finding land on the same rating. A gut-feel label skips this:
it's whatever a single reviewer's intuition produces in the moment,
which is exactly what let Alderglen's four findings compete on writing
quality rather than actual risk. The rubric also needs to be applied
*consistently* across an entire engagement — scoring the first finding
generously and the last one strictly because reviewer attention
degraded over a long report is a real, common failure mode a written
rubric guards against.

**Red flag:** Proposes a single combined score with no stated
likelihood/impact breakdown, or can't explain how a written rubric
produces more consistent ratings than intuition.

**Follow-up:** "Two findings both score 'High likelihood.' One exposes
a single customer's note text; the other exposes every customer's
account balance. Walk through how your rubric's impact axis
distinguishes these into different final ratings."

**What this proves:** Can design an operable, reproducible severity
framework rather than treating "severity rating" as a single
subjective label.

---

## 6. (Senior) A stakeholder asks why the red-team report needs a full "scope and methodology" section — isn't the findings list the only part that matters?

**Strong answer:** No — the scope and methodology section is what tells
a reader what was and wasn't tested, which is essential for correctly
interpreting the findings list. A report with four findings and no
stated scope is dangerously easy to over-read as "the system has
exactly four vulnerabilities" when it may mean "the tester covered four
of the ten OWASP categories in the time available, and the other six
were never examined." This directly connects to Phase 1: the scope
agreed before testing is exactly what the report's methodology section
has to restate, so the findings are read in the correct context — a
clean report on a narrow scope is not the same claim as a clean report
on a comprehensive one, and conflating the two is a real, common way
organizations under-invest in security after a red-team engagement that
was never comprehensive in the first place.

**Red flag:** Treats the findings list as self-sufficient, or can't
explain the specific misreading risk of a report with no stated scope.

**Follow-up:** "Alderglen's actual engagement covered three techniques
in two days against a system with real retrieval, tool-call, and
system-prompt surfaces. Write one sentence for a scope section that
would have prevented leadership from assuming the exercise was
comprehensive."

**What this proves:** Understands that a findings list without stated
scope creates real risk of false confidence, not just an incomplete
document.

---

## 7. (Architect) You're building a red-teaming program for an organization shipping several LLM-powered products, not just running a single engagement. How do the five phases change shape at that scale?

**Strong answer:** At program scale, each phase needs to become a
repeatable process, not a one-time exercise: Phase 1 becomes a standard
rules-of-engagement template reused (and lightly customized) per
product, not renegotiated from scratch each time; Phase 2 becomes a
maintained, living mapping (like this chapter's own OWASP-to-arsenal
table) kept current as new attack research emerges, so test-case design
doesn't start from zero for every new feature; Phase 3's documentation
needs a shared, structured format (not per-tester notes) so findings
across different products and different testers are comparable; Phase
4's rubric needs to be a single, org-wide standard, not one rubric per
team, so severity ratings are comparable across the whole product
portfolio when leadership prioritizes engineering time; Phase 5's report
template becomes standardized so stakeholders across products get a
consistent reading experience. The overarching architectural shift: a
single engagement's methodology has to become a program's shared
infrastructure, the same infrastructure-versus-one-off distinction that
separates ad hoc security work from a mature security function in any
domain, applied here to LLM-specific red-teaming specifically.

**Red flag:** Describes running the same five phases repeatedly without
addressing what needs to become standardized/shared infrastructure
across engagements, or ignores the comparability problem across
products and teams.

**Follow-up:** "Six months into the program, a new attack technique
(not covered by any existing chapter's arsenal) gets published in
credible security research. Walk through exactly which artifact from
your program gets updated first, and how that update propagates to
the next engagement."

**What this proves:** Architect-level judgment — translates a
single-engagement methodology into durable, comparable, shared program
infrastructure across an entire product portfolio.

---

## 8. (Architect) A findings report rates a prompt-injection vulnerability "Critical" because it "could theoretically leak any data in the system." An engineering lead pushes back, calling this an overclaim. Adjudicate.

**Strong answer:** The engineering lead has a real point worth taking
seriously, and it's exactly the honest-limit discipline this course has
required since Chapter 5: "could theoretically leak any data" describes
impact without establishing likelihood, and Phase 4's rubric requires
both axes, combined, not impact alone. If the actual reproduction steps
only demonstrate the technique working against one specific, narrowly-
scoped test case, the honest rating states the *demonstrated* impact and
notes the theoretical broader exposure as a documented, distinct
follow-up question — not baked into the same severity number without
evidence. That said, dismissing the finding as "just theoretical" would
be its own overclaim in the other direction if there's a real, credible
mechanism (not mere speculation) for the broader exposure — the correct
resolution is neither accepting the inflated rating nor dismissing the
underlying risk, but scoping a follow-up test case that actually
attempts the broader exfiltration and re-rating based on what's
*demonstrated*, exactly the same "test claims, don't assume them"
standard this course has held attack demonstrations to since Chapter 1.

**Red flag:** Sides fully with either party without proposing the
actual resolution (a follow-up test case establishing real evidence for
the broader claim), or accepts "theoretically could" as sufficient
grounds for a Critical rating with no further testing.

**Follow-up:** "The follow-up test case you propose gets run, and it
confirms the broader exfiltration is real and reproducible. How does
the report change, and what does this episode tell you about how your
rubric should treat 'theoretical' claims going forward?"

**What this proves:** Architect-level judgment on the same honest-
claims-versus-overclaims discipline this course has required from
Chapter 5 onward, applied here to the report-writing process itself
rather than to a defense's claimed effectiveness.

---

## Strategy tips

Keep the five phases in strict order in your head — scope, design,
execute/document, classify, report — and be ready to name which phase a
given process failure lives in (Alderglen's own story is a ready-made
example bank for this: no rules of engagement, ad hoc test selection,
memory-reconstructed documentation, no severity rubric, unusable
write-up). Be ready to connect any named attack technique back to its
originating chapter and its OWASP category using this chapter's own
arsenal table. For senior/architect questions, the interviewer is
listening for an operable, written, reproducible process (not gut-feel
judgment), a real distinction between demonstrated and theoretical
impact, and — at the architect level — the ability to scale a single
engagement's methodology into shared, comparable program infrastructure
across many products and teams.
