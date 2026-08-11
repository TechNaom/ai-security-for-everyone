# Chapter 6 Interview Questions: Data Poisoning

Grouped by level — beginner, intermediate, senior, architect. Each includes
a strong answer, a red flag, a follow-up, and what the question actually
proves. This is the plain-text companion to `interview-questions.html`.

---

### 1. (Beginner) A colleague says "data poisoning is basically the same as prompt injection, just done during training instead of at runtime." Is that accurate?

**Strong answer:** Not accurate, and the distinction matters. Prompt
injection works because there's no architectural separation between
instructions and data inside a single context window — an attacker gets
tokens into one specific conversation, and the model follows them that one
time, in that one runtime request. Data poisoning is a different mechanism
on a different surface: the attacker influences the training, fine-tuning,
or retrieval-corpus data itself, before any conversation happens. The
payoff isn't immediate and isn't scoped to one session — it's persistent,
affecting every future use of the resulting model or index until it's
retrained, re-indexed, or rolled back. Calling it "injection but during
training" collapses two genuinely different attack surfaces (the runtime
request path versus the data/training pipeline) into one, which leads to
defending only one of them.

**Red flag:** Treats the two as interchangeable, or assumes the same
defenses (structural separation, content tagging, sandwich prompting) that
work against prompt injection would meaningfully address data poisoning.

**Follow-up:** "If your team has fully hardened the runtime request path
against every Module 2 technique, is your system's data-and-training
pipeline automatically safe too? Why or why not?"

**What this proves:** Understands data poisoning as a genuinely distinct
attack surface, not a rebranding of prompt injection.

---

### 2. (Beginner) Name the three categories of data poisoning this chapter covers, in one sentence each.

**Strong answer:** (1) Targeted/backdoor poisoning — a small number of
carefully-crafted examples create one narrow, triggered behavior that
activates only on a specific input pattern, while the model behaves
normally otherwise. (2) Availability/bias poisoning — a large volume of
low-quality or slanted data degrades overall model quality or introduces a
systematic, always-on bias, with no specific trigger involved. (3) RAG/
retrieval corpus poisoning — the attacker compromises the corpus itself
that gets indexed into a retrieval system, before ingestion, so every
future retrieval from that corpus is affected, not just one session.

**Red flag:** Can only describe one category in detail, or conflates
Category 3 with Chapter 4's indirect prompt injection via RAG.

**Follow-up:** "Which of the three would be hardest to detect with an
aggregate quality metric, and why?"

**What this proves:** Has internalized the three categories as distinct
mechanisms with distinct attacker goals, not one vague "poisoned data" idea.

---

### 3. (Intermediate) Why does a standard evaluation — accuracy on a held-out test set — almost never catch a targeted/backdoor poisoning attack?

**Strong answer:** A backdoor is specifically designed so the model's
behavior on ordinary inputs is completely unaffected — the entire value of
the attack to the attacker depends on the model looking normal until the
one input pattern the attacker controls appears. A held-out test set drawn
from the same distribution as ordinary training data will almost never
happen to contain the specific trigger pattern, so the model's measured
accuracy on it stays essentially unchanged whether or not a backdoor is
present. Research on this (Anthropic's Sleeper Agents work, and the
Anthropic/UK AI Security Institute/Alan Turing Institute study showing as
few as 250 documents can backdoor a model regardless of overall training-set
size) confirms this is a real, not hypothetical, blind spot: aggregate
metrics are the wrong tool for a narrow, conditional effect by construction.

**Red flag:** Assumes a clean accuracy number on a standard test set is
meaningful evidence against a backdoor, without naming why that evidence
doesn't actually address the threat model.

**Follow-up:** "What kind of evaluation would actually have a chance of
surfacing a backdoor that a standard held-out test set misses?"

**What this proves:** Understands why aggregate metrics and targeted
threats require genuinely different evaluation approaches — a distinction
that generalizes well beyond this specific chapter.

---

### 4. (Intermediate) Explain, with a concrete example, the difference between Chapter 4's indirect prompt injection via RAG and this chapter's RAG corpus poisoning.

**Strong answer:** Chapter 4's indirect injection is a runtime attack that
happens to use a retrieval channel: an attacker plants malicious text in
one document, that document gets retrieved into one conversation's context
window, and the mechanism is the same "tokens in context get followed as
instructions" problem every Module 2 attack shares — it affects the one
session where that specific retrieval fires. Corpus poisoning is a
pipeline attack: the attacker compromises the underlying document set
itself, before or during ingestion into the vector store — for example,
editing a policy wiki page's actual content so the loosened version gets
indexed. Once that happens, every future query whose embedding is similar
enough can retrieve the poisoned version, affecting every user who touches
that topic, not just one attacker's one session. Same retrieval channel,
genuinely different attack surface and timing — one is a single planted
payload waiting for a retrieval; the other corrupts the source of truth
that all future retrievals draw from.

**Red flag:** Describes both as "poisoning the RAG documents" without
distinguishing runtime-single-session scope from pipeline-persistent scope.

**Follow-up:** "If a team fixes access control on who can query the vector
store, have they addressed corpus poisoning? Why or why not?"

**What this proves:** Can precisely separate two attacks that both involve
a RAG pipeline but operate through genuinely different mechanisms and
timing — exactly the distinction this chapter names as its own most
important clarification.

---

### 5. (Senior) A team says: "We added anomaly detection to our training-data pipeline, so we're protected against data poisoning." Evaluate this claim.

**Strong answer:** Overclaimed. Anomaly detection is a real, useful layer,
but it's honestly weakest exactly where Category 1 (targeted/backdoor)
poisoning is designed to operate: low volume, individually plausible
examples, deliberately blended into a much larger legitimate dataset.
Anthropic's Sleeper Agents research and the near-constant-poison-sample
research both describe attacks using a small number of examples chosen
specifically to sit under whatever threshold a detector is tuned to — a
well-resourced attacker who has read the same published research the
defense is built from can construct an attack specifically to evade it.
Anomaly detection is meaningfully more effective against Category 2
(availability/bias) poisoning, where a large-volume, broad-effect attack
leaves a real statistical footprint. A team relying on anomaly detection
alone has real coverage against one category and a real, honestly-stated
gap against another — "protected against data poisoning" is a category
error, not a precise claim.

**Red flag:** Accepts "we added anomaly detection" as sufficient without
naming which category of poisoning it actually addresses, or without
naming the low-volume-blended-backdoor gap.

**Follow-up:** "What additional layer would you add specifically to close
the gap anomaly detection leaves against a low-volume, deliberately-blended
backdoor?"

**What this proves:** Can name a specific defense's honest limit precisely
— the same "what this stops, what it doesn't" discipline Chapters 3–5
required for prompt-injection defenses, applied here to the data pipeline.

---

### 6. (Senior) Design an output/behavior audit for a fine-tuned support-triage model that would have a real chance of catching a targeted backdoor similar to Meridian Home Warranty's 46-ticket attack. What makes an audit like this different from a routine model-quality check?

**Strong answer:** A routine model-quality check re-runs the same
held-out test set the model was already validated against — by
construction, this only measures performance on the distribution the model
was known to handle well, and provides essentially zero information about
a narrow, conditional trigger the test set was never built to probe for.
A real audit needs a deliberately wide, adversarially-varied input
distribution constructed specifically to surface anomalous behavior:
systematically varied claim phrasing, unusual formatting, rare
terminology combinations, and — critically — comparing the model's
decision rate across many small input perturbations to look for any
single feature (a phrase, a formatting quirk, a reference pattern) that
correlates with a disproportionate shift in outcome, the same signal a
lift-based anomaly scan looks for in the training data itself, now applied
to the trained model's behavior instead. This is structurally the same
discipline Chapter 5 taught for defense evaluation: audit against a
deliberately wide, adversarial distribution, not just the distribution
you already know the system handles well, because a clean result on the
narrow distribution says nothing about the wide one.

**Red flag:** Proposes only re-running standard accuracy metrics, or
proposes spot-checking a random sample without any systematic attempt to
probe unusual or rare input patterns specifically.

**Follow-up:** "Your audit finds one candidate anomalous phrase correlated
with a decision shift. What would you do next before concluding it's a
real backdoor rather than a coincidence?"

**What this proves:** Can design a real, non-trivial evaluation
methodology for a genuinely hard detection problem, not just describe the
concept of "auditing" at a high level.

---

### 7. (Architect) You're setting your org's standing policy for what has to happen before any externally-sourced or user-contributed data can be used in a fine-tuning run. What would you require, and why is "the data passed anomaly detection" insufficient as a sole gate?

**Strong answer:** The policy should require, layered together, not any
single check alone: (1) source provenance classification for every
contributing data source, with different scrutiny levels for
verified/authenticated sources versus open, unauthenticated channels; (2)
statistical anomaly detection on the aggregated dataset before each
fine-tuning run, understood explicitly as a Category-2-focused layer; (3)
a mandatory wide-distribution behavior audit on the resulting model before
deployment, specifically probing for anomalous triggered behavior, not
just aggregate accuracy; (4) a documented, stated residual-risk
acknowledgment rather than a claim of elimination. "Passed anomaly
detection" alone is insufficient as a sole gate because it's a Category-2
tool being asked to also cover Category 1, where its own honest limit is
greatest — a data pipeline that treats one green checkmark from one layer
as proof of safety has made exactly the single-attempt-trap-shaped mistake
Chapter 5 named for defense evaluation, now recurring at the data-pipeline
layer: a rigorous-looking check applied to the wrong threat, or applied
alone where layering was required.

**Red flag:** Proposes a single gate (anomaly detection, or provenance
checking alone) as sufficient, or doesn't distinguish which category each
proposed check actually addresses.

**Follow-up:** "How would this policy need to change for a RAG corpus that
gets updated continuously, rather than a fine-tuning set that's built once
per training run?"

**What this proves:** Architect-level judgment — designs a layered,
category-aware data-governance policy rather than a single checklist item,
with an honest, stated residual-risk posture.

---

### 8. (Architect) Given that published research (Anthropic's Sleeper Agents, the near-constant-poison-sample study, and Carlini et al.'s web-scale poisoning research) shows backdoors can persist through safety training, require very few examples, and are practical and cheap to plant in large real-world corpora, how should this change how your org evaluates a *third-party* fine-tuned model or a vendor-supplied RAG corpus before adopting it?

**Strong answer:** The evaluation can't rely on the vendor's own
aggregate-quality claims, because — per the Sleeper Agents finding — a
planted backdoor can survive exactly the kind of safety training a vendor
would already have applied and reported as evidence of a clean model. A
real evaluation before adopting a third-party model or corpus needs: (1)
an explicit request for the vendor's own data-provenance and vetting
practices, treated as a real question, not a formality; (2) an independent
wide-distribution behavior audit run by the adopting org itself, not
reliance on the vendor's internal testing alone, since Section 6's logic
about audits only surfacing what they specifically probe for applies
doubly to a model whose training data the adopting org never saw; (3) for
a RAG corpus specifically, a real corpus-diffing and version-history
review, not just a one-time content scan at adoption time, since Carlini
et al.'s research shows exactly this kind of external, periodically-synced
corpus is a practical, low-cost target. Crucially, none of this produces a
guarantee — the honest conclusion for a business stakeholder is a bounded,
residual-risk statement ("we ran X independent checks, found no anomaly
within Y distribution, understand Z remains an open gap"), not an
unqualified "verified safe," the same translation Chapter 5 taught for
prompt-injection risk communication, now applied to a supply-chain-adjacent
trust decision.

**Red flag:** Treats a vendor's own safety-training claims or a one-time
content review as sufficient due diligence, or gives an unqualified "yes,
it's safe" / "no, never trust third-party data" answer with no concrete,
bounded evaluation plan.

**Follow-up:** "The vendor refuses to disclose their training-data
provenance practices, citing trade secrets. Does that change your
adoption decision, and how would you communicate that risk to a
stakeholder who wants to ship this quarter?"

**What this proves:** Can extend this chapter's core findings into a real
vendor-trust and supply-chain-adjacent decision — direct groundwork for
Chapter 8's supply-chain-risk chapter, and the practical skill of turning
published research into an actual due-diligence process.

## Strategy Tips

- Keep the pipeline-versus-runtime distinction sharp in every answer: data
  poisoning shapes what the model *is*, before deployment; prompt injection
  manipulates what the model *does*, at runtime, in one session. Confusing
  the two is the single most common mistake this chapter's questions probe
  for.
- Be ready to name which of the three categories (backdoor, availability/
  bias, RAG corpus) a given scenario fits, and why — the categories differ
  in mechanism, volume, and detectability, not just in vocabulary.
- For every defense, be ready to state its honest limit, not just what it
  catches — a defense-evaluation report that names only successes and
  never limits is the same overclaiming pattern Chapter 5's interview
  bank penalized.
- For senior/architect questions, the interviewer is listening for layered,
  category-aware thinking and an explicit, honest residual-risk posture —
  never an unqualified "this makes us safe" claim.
