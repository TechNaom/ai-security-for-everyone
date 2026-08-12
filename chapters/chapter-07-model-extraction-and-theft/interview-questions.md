# Chapter 7 Interview Questions: Model Extraction and Theft

Grouped by level — beginner, intermediate, senior, architect. Each includes
a strong answer, a red flag, a follow-up, and what the question actually
proves. This is the plain-text companion to `interview-questions.html`.

---

### 1. (Beginner) A colleague says "model extraction is just another form of prompt injection — the attacker is still just sending text to the API." Is that accurate?

**Strong answer:** Not accurate, and the distinction is the same kind Chapter
6 drew between data poisoning and prompt injection. Prompt injection works
because an attacker's tokens get followed as instructions inside one live
conversation — the payoff is immediate, scoped to that one session, and
nothing about the deployed model changes. Model extraction is a different
mechanism: the attacker sends completely ordinary, unmanipulated queries —
nothing that would even register as an attack if you inspected any single
request — and the "attack" is entirely in what they do with the responses
afterward, at volume, outside the target system altogether. Nothing about
the target model or the one session's outcome changes at all; what changes
is that the attacker now possesses something new (a substitute model, a
recovered training example, a leaked system prompt). Calling it "just
another form of prompt injection" misses that the target system is never
manipulated — it's used exactly as designed, over and over.

**Red flag:** Treats the two as interchangeable, or assumes injection
defenses (structural separation, content tagging) meaningfully address
extraction risk.

**Follow-up:** "If a team has fully hardened its runtime request path
against every known prompt-injection technique, is it automatically
protected against model extraction? Why or why not?"

**What this proves:** Understands model extraction as a genuinely distinct
attack surface, not a rebranding of prompt injection.

---

### 2. (Beginner) Name the three model extraction techniques this chapter covers, in one sentence each.

**Strong answer:** (1) Query-based distillation — systematically querying a
target model across a broad input distribution and using the (input,
output) pairs to fine-tune a cheaper substitute model that mimics its
behavior. (2) Training-data extraction and membership inference —
recovering verbatim memorized training text, or determining whether a
specific piece of data was used in training, without necessarily recovering
the text itself. (3) System prompt extraction — the cheapest target,
getting a model to reveal or paraphrase its own system-level instructions
through ordinary conversation, requiring no model training or statistical
inference at all.

**Red flag:** Can only describe one technique in detail, or conflates
system prompt extraction with a jailbreak/injection technique from Module 2.

**Follow-up:** "Which of the three requires the least sophistication and
cost from the attacker, and why does that matter for how a team prioritizes
defenses?"

**What this proves:** Has internalized the three techniques as distinct
mechanisms with distinct targets, not one vague "model theft" idea.

---

### 3. (Intermediate) Explain why a model's own API being useful to legitimate customers is structurally the same thing that makes it vulnerable to query-based distillation.

**Strong answer:** A model's API has to return real, useful answers to real
questions for it to be a viable product at all — that's the entire point of
selling API access. But there's no way to let a paying customer log a
(question, answer) pair for their own legitimate use without also,
structurally, allowing anyone with an account to log a large number of
(question, answer) pairs for a different purpose entirely. The same
property that makes ClauseFinder useful to a law firm — accurate, complete
answers to real clause questions — is exactly the property QuickLex needs
to build a distillation dataset. There's no technical distinction between
"a customer asking questions to get real work done" and "a customer asking
questions to harvest training data" visible from any single request; the
difference only shows up in aggregate query patterns, which is why Defense
1 (rate limiting and pattern detection) operates on volume and coverage,
not on inspecting individual requests.

**Red flag:** Suggests the fix is simply "don't answer questions
accurately," without recognizing that would also break the product for
legitimate use — or fails to name that the distinction is only visible in
aggregate, not per-request.

**Follow-up:** "Given that, is there any purely per-request technical fix
that would stop distillation without also degrading the product for
legitimate customers?"

**What this proves:** Understands the extraction risk as an inherent
tension in what makes an API valuable, not a fixable bug — a mature,
non-naive framing of the threat.

---

### 4. (Intermediate) A team says: "We removed raw logits/confidence scores from our API response, so we're now safe from model extraction." Evaluate this claim.

**Strong answer:** Overclaimed. Withholding raw logits is a real,
meaningful piece of Defense 2 (output perturbation) — it forces an attacker
to train a substitute model on final text output only, a weaker training
signal than raw probability distributions, which does measurably degrade
extraction fidelity. But it does nothing to stop the underlying query-based
distillation attempt: Krishna et al.'s research demonstrated effective
model extraction using nothing but final text output, no logits required,
achieving a substitute model performing "only slightly worse" than the
original. It also does nothing at all against training-data extraction
(logits aren't the mechanism there) or system prompt extraction (a
completely separate, lighter-weight technique). "Safe from model
extraction" describes an outcome none of this chapter's individual
defenses claim to deliver alone.

**Red flag:** Accepts "we removed logits" as a complete fix, or doesn't
distinguish which technique (of the three) it actually addresses.

**Follow-up:** "What would you add to actually close the gap that removing
logits leaves open against a determined query-based distillation attempt?"

**What this proves:** Can evaluate a specific technical mitigation's actual
scope precisely — the same "what this stops, what it doesn't" discipline
this course has required since Chapter 3, applied to the API surface.

---

### 5. (Senior) Design a query-pattern anomaly detection approach that would have a real chance of catching a QuickLex-style distillation campaign against ClauseFinder — one deliberately paced to resemble a heavy legitimate user. What makes this genuinely hard, not just an engineering exercise?

**Strong answer:** A real approach needs to combine multiple independent
signals, not rely on any one alone: request volume relative to the
account's own historical baseline (not an absolute threshold, since a
legitimate power user's baseline is already high), category/input-coverage
breadth (does the query set systematically sweep every category the
product supports, in a pattern unlikely for someone working through one
real matter at a time), and query-to-query diversity or ordering (real
usage tends to cluster around whatever a user is actually working on;
systematic extraction tends toward broad, deliberately unclustered
coverage). What makes this genuinely hard is the honest limit this
chapter's own Defense 1 section names: an attacker who paces queries
specifically to resemble a legitimate power user's own historical pattern
can, by construction, make the two statistically close to indistinguishable
using volume and coverage signals alone — this isn't a threshold-tuning
problem with a correct answer, it's a real, structural false-positive/
false-negative tradeoff, the same category of hard problem Chapter 5 named
for detection-based prompt-injection defenses.

**Red flag:** Proposes only a flat volume threshold, or claims a
sufficiently clever detection algorithm can fully resolve the tension
without acknowledging the real tradeoff.

**Follow-up:** "Your detector flags an account as a suspected extraction
campaign. What would you actually do next, given that a false positive
means throttling or investigating a real paying customer?"

**What this proves:** Can design a real, non-trivial detection methodology
while being honest about its structural limits, not just describe the
concept of "anomaly detection" at a high level.

---

### 6. (Senior) Halcyon's legal team wants to rely solely on updated Terms of Service language to address model-extraction risk, arguing it's cheaper than engineering work. Evaluate this as a sole strategy.

**Strong answer:** Insufficient as a sole strategy, though a real and
legitimate layer. Terms of service and legal deterrence genuinely address a
gap technical controls can't — they impose a cost on an attacker even after
a successful, undetected extraction, and they're disproportionately
effective against exactly the resourced, identifiable, business-motivated
attacker profile (a competitor building a product) that's hardest to stop
technically. But a ToS clause does nothing to detect an extraction attempt
in progress, does nothing to reduce the fidelity of what gets extracted
before it's ever caught, and is weak or meaningless against an
unidentifiable or out-of-jurisdiction attacker. Relying on it alone means
QuickLex's substitute model can be fully built and shipped before Halcyon
has any evidence to act on — the legal remedy only ever arrives after the
commercial damage is done. A sound strategy layers ToS/legal deterrence
with real technical controls (rate limiting/pattern detection, output
perturbation), not instead of them.

**Red flag:** Accepts legal deterrence as sufficient on its own, or
dismisses it entirely as "not real security" rather than naming its actual,
distinct function.

**Follow-up:** "Suppose Halcyon later has strong evidence QuickLex's model
is a distilled copy. What technical evidence (from this chapter's other
defenses) would actually support that claim in a legal proceeding?"

**What this proves:** Can evaluate a non-technical control's real,
legitimate scope without either dismissing it or over-relying on it —
architect-adjacent judgment about layered, cross-disciplinary defense.

---

### 7. (Architect) You're advising Halcyon on whether to adopt differential privacy for ClauseFinder's next fine-tuning run, given the training set includes real client contract clauses. What tradeoffs would you name, and how would you decide?

**Strong answer:** Differential privacy directly targets the
training-data-extraction risk (Technique 2) this scenario actually has —
client clauses in the fine-tuning set create genuine verbatim-extraction
and membership-inference exposure, and DP provides a mathematical, provable
bound on how much any single client's clause can be memorized or
influence the model, which is categorically stronger than an empirical
"usually works" defense. The real tradeoff to name explicitly: meaningful
privacy guarantees typically cost some model utility/accuracy, and the
privacy-utility curve is a real design decision requiring actual
measurement against ClauseFinder's specific accuracy requirements, not an
assumption either way. It's also worth being precise that DP does nothing
for Technique 1 (query-based distillation of overall behavior) or Technique
3 (system prompt extraction) — adopting it addresses one specific, real
risk in this scenario, not "model extraction" generically. The decision
should be based on: (1) how sensitive the client clause data actually is
(here, genuinely sensitive — confidential contract language under an
explicit client trust promise), (2) a measured utility cost at a realistic
privacy budget, and (3) whether Defenses 1-3 already provide adequate
coverage for Techniques 1 and 3 so DP isn't being asked to do more than its
actual scope.

**Red flag:** Recommends DP as a general "model extraction fix," or treats
the utility cost as negligible/nonexistent without proposing to actually
measure it.

**Follow-up:** "The measured utility cost turns out to be a real, visible
accuracy drop. How would you communicate that tradeoff to a business
stakeholder who just wants 'the extraction risk fixed'?"

**What this proves:** Architect-level judgment — scopes a specific defense
to the specific risk it actually addresses, names a real engineering
tradeoff honestly, and ties the decision to the actual sensitivity of the
data involved rather than treating all defenses as interchangeable.

---

### 8. (Architect) Given that published research (Tramèr et al. 2016, Krishna et al. 2020, and Carlini et al.'s training-data extraction work) shows model extraction is a decade-old, well-established, and empirically demonstrated risk against real production systems, how should this change how your org designs a *new* commercial LLM-powered API product from the start, rather than bolting on defenses after launch?

**Strong answer:** Extraction risk should be a first-class design input,
not a post-launch patch, because the research shows the risk isn't
speculative or new — it's already demonstrated against production systems,
and retrofitting defenses after a competitor has already built a
distillation dataset from a year of unrestricted API access is too late for
that specific harm. A real from-the-start design should: (1) build rate
limiting and query-pattern monitoring into the API's launch architecture,
not add it after a suspected incident; (2) make an explicit, pre-launch
decision about what output granularity (raw logits vs. final text only) is
actually necessary for the legitimate product experience, rather than
exposing maximum granularity by default; (3) if the product will be
fine-tuned on any real user- or client-submitted data, evaluate
differential privacy or bounded-influence training as part of the initial
training pipeline design, when it's cheaper to build in than to retrofit;
(4) draft ToS/legal terms addressing systematic extraction before launch,
not after a competitor's product ships. Crucially, none of this produces a
guarantee of zero extraction risk — the honest deliverable is a
documented, stated residual-risk posture communicated to the business
before launch (what's defended, what's accepted risk, what would trigger a
response), the same translation this course has required since Chapter 5,
applied here to a product-launch decision instead of an incident response.

**Red flag:** Treats extraction defenses as something to add only after a
specific incident, or promises a design that eliminates the risk entirely.

**Follow-up:** "Business stakeholders push back that rate limiting and
withholding logits will degrade the product experience for legitimate
power users. How do you make that tradeoff decision, and who should own
it?"

**What this proves:** Can extend this chapter's findings into a proactive,
architect-level product-design decision — not just a reactive defense
applied to an already-shipped system, and can communicate real, bounded
residual risk rather than an absolute guarantee.

## Strategy Tips

- Keep the "target is never touched" distinction sharp in every answer:
  model extraction's attacker acts entirely from outside, using only
  ordinary API access — the deployed model, its weights, and its training
  pipeline are all completely unmodified by the attack itself.
- Be ready to name which of the three techniques (distillation, training-
  data extraction/membership inference, system prompt extraction) a given
  scenario fits, and which is cheapest/lightest-weight for an attacker.
- For every defense, be ready to state its honest limit, not just what it
  catches — especially the real false-positive tension in query-pattern
  detection and the scope limits of differential privacy.
- For senior/architect questions, the interviewer is listening for layered,
  technique-aware thinking, an explicit residual-risk posture, and — at the
  architect level — proactive, launch-time design thinking rather than
  purely reactive defense.
