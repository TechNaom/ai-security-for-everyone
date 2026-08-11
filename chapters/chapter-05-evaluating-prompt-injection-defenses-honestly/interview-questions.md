# Chapter 5 Interview Questions: Evaluating Prompt-Injection Defenses Honestly

Grouped by level — beginner, intermediate, senior, architect. Each includes
a strong answer, a red flag, a follow-up, and what the question actually
proves. This is the plain-text companion to `interview-questions.html`.

---

### 1. (Beginner) A teammate says "I tried one injection attempt against our new defense and it failed, so we're covered." What's wrong with that claim, precisely?

**Strong answer:** The claim generalizes from a sample size of one. Chapter
3 named five direct-injection technique families and Chapter 4 named five
delivery channels and three jailbreak categories — a combinatorial space
far larger than one attempt covers, and each family can be phrased many
different ways (Chapter 3's own obfuscation family exists specifically
because surface phrasing varies while the underlying technique doesn't).
One passed test says the defense held against that one specific phrasing,
delivered that one specific way, tested once — it says nothing about the
other technique families, other channels, other phrasings within the same
family, or an attacker who adapts after learning the defense exists. This
is the "single-attempt trap" the chapter names directly.

**Red flag:** Accepts "I tried it and it failed" as equivalent to "I
measured it," without asking what else was or wasn't tested.

**Follow-up:** "What would you need to add to that one test to make
'we're covered' an honest claim?"

**What this proves:** Recognizes the gap between an anecdote and a
measurement — the chapter's central problem statement.

---

### 2. (Beginner) Name the four steps of this chapter's evaluation methodology, in order, in one sentence each.

**Strong answer:** (1) Build a real test corpus spanning both prior
chapters' taxonomies (technique family and delivery channel), with
multiple variants per family, plus a benign control set. (2) Run the
corpus against the target with and without the defense applied, under
controlled, comparable conditions. (3) Measure real numbers — attempts
blocked, attempts that got through, and false positives against the
benign set — not just an impression of "it seemed to work." (4) Adapt the
corpus specifically against the defense that blocked it, and re-measure —
adversarial iteration, since a real attacker doesn't stop once blocked
once.

**Red flag:** Can list only "test it and see if it works," missing the
controlled comparison, the false-positive measurement, or the
adversarial-iteration step entirely.

**Follow-up:** "Which of these four steps is most often skipped in
practice, and why do you think that is?"

**What this proves:** Has internalized the methodology as four distinct,
necessary steps, not one vague "test the defense" idea.

---

### 3. (Intermediate) Why does a defense-evaluation corpus need a set of benign, legitimate requests, not just malicious ones?

**Strong answer:** Without a benign control set, there's no way to measure
false positives — cases where the defense incorrectly blocks or flags a
legitimate request. This matters most for detection-category defenses
(filtering, output-based screening), which have a real, computable
false-positive/false-negative tradeoff: a filter tuned aggressive enough
to catch every obfuscated attack in a malicious-only corpus will often
also flag legitimate requests that happen to share surface features with
an attack (a user legitimately saying "ignore the earlier draft, use this
version" shares vocabulary with an instruction-override attempt without
being one). A report that states only the catch rate against malicious
attempts, with no benign corpus to measure against, has evaluated half of
what a detection defense actually costs.

**Red flag:** Treats a defense's effectiveness as fully captured by its
catch rate against attacks, with no mention of the cost side of the
tradeoff.

**Follow-up:** "If your false-positive rate on the benign corpus is 15%,
is that defense still worth deploying? What would change your answer?"

**What this proves:** Understands detection defenses as a genuine
two-sided tradeoff, not a one-directional "more blocking is always
better" metric.

---

### 4. (Intermediate) Explain, with a concrete example, why adversarial iteration (Step 4) can reveal a very different number than a single-round evaluation.

**Strong answer:** A single-round evaluation measures a defense's success
rate against attackers who don't know it exists or haven't adapted to it.
Chapter 4's own cited research on sandwich/reinforcement prompting shows
exactly this gap concretely: sandwich prompting produces a real,
measurable reduction in injection success against a static, unadapted
corpus, but published adaptive-attack research reports very high success
rates against sandwich defenses specifically once an attacker knows the
defense is in place and crafts a payload against its known mechanism (for
instance, exploiting the fact that sandwich prompting relies on a
recency effect, so an attacker times or structures their payload to
still be the most recent text before generation despite the reminder).
A team that stops at Step 3 might report "90% blocked" honestly, while
the real number against a determined, adaptive attacker is much lower —
both numbers are real, but only one of them answers the question that
actually matters for a determined attacker.

**Red flag:** Treats a single-round blocked-rate number as the final word
on a defense's effectiveness, with no mention of what changes once the
defense's mechanism is publicly known or discoverable.

**Follow-up:** "How would you decide when to stop iterating — is there a
point where further adversarial rounds stop being worth running?"

**What this proves:** Understands adversarial iteration as revealing a
genuinely different, and often more decision-relevant, number than a
static evaluation — not just "more testing is generally better."

---

### 5. (Senior) A report states: "Our consequence-bounding defense (a hard cap on `approve_claim`'s payout amount) was evaluated against our injection corpus and showed a 0% reduction in the corpus's success rate, so it provided no security benefit." Evaluate this conclusion.

**Strong answer:** The conclusion applies the wrong metric to the wrong
defense category. A consequence-bounding defense was never trying to stop
the injection from succeeding at the text level — it's trying to make a
successful injection harmless. Measuring "did the corpus's tell still
fire" (whether the model's text still shows signs of manipulation) will
correctly show no change, because nothing about capping a tool call's
payout changes whether the model's *response* gets manipulated — that's
Category 1's (structural) metric, not Category 3's (consequence-bounding)
metric. The correct evaluation question for this defense is different:
given that some corpus entries did succeed at manipulating the model
(assume that as a given), did the hard, code-enforced cap still hold
regardless of what the model decided or was manipulated into deciding?
That's a real, separately measurable question, and the report's own 0%
number on the wrong metric says nothing about the right one.

**Red flag:** Accepts the report's conclusion at face value, or can't
articulate what the correct evaluation question for a consequence-bounding
defense actually is.

**Follow-up:** "Design the actual evaluation you'd run to measure whether
this cap provides real security benefit."

**What this proves:** Can identify a metric/category mismatch in a
real-looking evaluation report — the chapter's single most important
distinction, applied to a concrete, plausible-sounding but wrong
conclusion.

---

### 6. (Senior) You're asked to evaluate a system with three defenses layered together: content tagging, sandwich reinforcement, and output-based detection. The team wants one number: "our injection defense success rate." Is that a well-formed request? How would you respond?

**Strong answer:** Partially well-formed, but incomplete on its own. A
single number for "the full stack, as deployed" is a legitimate and
useful thing to measure — it tells you the system's actual, real-world
posture. But if the goal is also understanding which layer is doing the
work (so the team knows what to invest in improving, or what breaks if one
layer is removed or a system change disables it), the stack needs to be
evaluated with each defense toggled independently as well — running the
corpus with only tagging, only sandwich reinforcement, only detection, and
combinations, to attribute effect to each layer. Reporting only the
combined number risks the team believing all three layers are pulling
equal weight when, in reality, one might be doing almost all of the work
and the other two might be nearly redundant — information that matters a
great deal for prioritizing future hardening effort or diagnosing a
regression later.

**Red flag:** Accepts "one number for the whole stack" as sufficient
without recognizing the attribution problem, or conversely insists on
only isolated single-defense numbers with no combined, as-deployed
measurement at all.

**Follow-up:** "If the combined stack scores well but the tagging-only
run scores almost as well, what does that tell you about the other two
layers, and what would you check next before concluding they're
redundant?"

**What this proves:** Understands that "the defense's success rate" is
ambiguous for a layered stack without specifying whether the question is
about the deployed system as a whole or about attributing effect to
individual layers — a real, common gap in how teams report evaluation
results.

---

### 7. (Architect) You're designing your org's standing policy for how every new LLM feature must be evaluated for injection resistance before launch. What would you require, and why does a single pre-launch evaluation run eventually become stale even if nothing about the policy itself was wrong?

**Strong answer:** The policy should require: a real, versioned test
corpus with multiple variants per technique family and channel plus a
benign control set (not an ad hoc one-off list); a controlled before/after
run against the exact model and system prompt being shipped; real
blocked/succeeded/false-positive numbers, not a pass/fail impression; at
least one adversarial-iteration round against whatever defense the system
relies on most; and a stated attacker model and residual-risk note rather
than an unqualified "safe" claim. Crucially, the policy should also
require re-evaluation triggers, not just a one-time gate: a model swap,
a new tool added to the system, a new content-ingestion channel, or a
system-prompt change all invalidate a prior evaluation's numbers, because
the corpus was measured against a specific configuration that no longer
exists. A single pre-launch run, however rigorous, is a snapshot — new
attack research, new jailbreak techniques, and new delivery channels
(Chapter 4's own taxonomy is explicitly stated as illustrative, not
exhaustive) keep appearing after that snapshot was taken, so a policy that
treats one clean report as permanent proof of safety is stale the moment
anything about the system, the model, or the published attack literature
changes.

**Red flag:** Designs a policy focused entirely on the pre-launch gate,
with no mention of what triggers re-evaluation after launch, or treats a
single passed evaluation as a permanent property of the system rather
than a time-bound measurement.

**Follow-up:** "How would you decide the re-evaluation cadence for a
system that hasn't changed at all, given that the published attack
literature itself keeps evolving?"

**What this proves:** Architect-level judgment — designs an evaluation
practice as an ongoing discipline tied to real triggers, not a one-time
compliance checkbox.

---

### 8. (Architect) Given that the field's own published research (OpenAI's Instruction Hierarchy paper, Anthropic's guardrails documentation, and the sandwich-prompting adaptive-attack research) is explicit that no available defense combination eliminates prompt injection entirely, how should that honest limit change how your org communicates risk to a business stakeholder who wants a simple "is this safe to launch" answer?

**Strong answer:** The honest answer is never an unqualified "yes" or
"no" — it's a specific, evidence-backed risk statement: what corpus was
tested, what the measured blocked/succeeded/false-positive numbers were,
what adversarial iteration was or wasn't run, what residual risk remains
even after every applied defense, and — critically — what the
consequence-bounding layer guarantees regardless of whether an injection
succeeds at the text level. For a stakeholder who needs a decision, the
translation isn't "we can't promise anything" (which is true but useless)
— it's "here is the system's real, measured injection-success rate under
these defenses, here is what a successful injection could still actually
do given our consequence-bounding controls, and here is our residual risk
given that no combination of defenses eliminates the underlying
vulnerability." This reframes the business decision from "is it safe"
(a question with no honest yes/no answer, per the field's own published
position) to "is the bounded, measured residual risk acceptable for this
specific system's stakes" — a question that actually has a real,
defensible answer, and one an engineering lead can stand behind under
scrutiny.

**Red flag:** Either overclaims ("yes, it's safe now that we've added
defenses") to satisfy the stakeholder's desire for a simple answer, or
gives an unhelpfully vague non-answer ("nothing is ever fully safe") with
no concrete numbers or bounded-impact reasoning to actually inform the
decision.

**Follow-up:** "The stakeholder pushes back: 'so you're telling me you
can't guarantee this is safe — why would we launch at all?' How do you
respond?"

**What this proves:** Can translate the field's genuinely unresolved
technical limit into a real, decision-useful business communication,
without either overclaiming safety or abdicating the risk conversation
entirely — the practical skill this entire chapter has been building
toward.

## Strategy Tips

- For every answer, be ready to name the specific step of the methodology
  (corpus construction, controlled comparison, real numbers including
  false positives, adversarial iteration) rather than staying at the level
  of "we tested it and it worked."
- Keep the three-category distinction sharp: structural (does the tell
  still fire), detection (false-positive/false-negative tradeoff),
  consequence-bounding (does the blast radius stay contained) are three
  different questions, and applying the wrong one to a given defense is
  the single most common real mistake this chapter names.
- For senior/architect questions, the interviewer is listening for
  evaluation-as-ongoing-discipline thinking — a single clean report is a
  snapshot, not a permanent property of the system.
- If you're new to security interviews: being able to say precisely why a
  0% measured success rate against a static corpus is not the same claim
  as "this defense eliminates the risk" — and connecting that to the
  field's own published position, not just a hedge — is a strong, complete
  answer to almost any "is this defense good enough" question in this
  bank.
