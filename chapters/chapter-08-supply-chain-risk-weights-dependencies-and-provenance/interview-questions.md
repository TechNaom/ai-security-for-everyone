# Chapter 8 Interview Questions: Supply-Chain Risk: Weights, Dependencies, and Provenance

Grouped by level — beginner, intermediate, senior, architect. Each includes
a strong answer, a red flag, a follow-up, and what the question actually
proves. This is the plain-text companion to `interview-questions.html`.

---

### 1. (Beginner) A colleague says "supply-chain risk is just data poisoning under a different name — either way, the model ends up with bad behavior baked in." Is that accurate?

**Strong answer:** Not accurate, and the distinction matters for which
defenses even apply. Data poisoning (Chapter 6) is about an attacker
influencing data *your own organization* deliberately chose to train,
fine-tune, or index from — there's a training step your organization
actually ran, and Chapter 6's defenses (provenance vetting on your own
intake channel, anomaly detection on your own training set, output
auditing after your own fine-tuning run) all attach to that step.
Supply-chain risk, specifically Category 1 of this chapter (compromised
or backdoored upstream weights), means you inherit an already-trained,
possibly already-backdoored artifact with no training step of your own
anywhere in the story — none of Chapter 6's defenses have anything to
attach to, because there was no intake process, no training run, and no
data set of your own to vet in the first place. The end state can look
similar (a model with a planted trigger), but the defensive posture is
completely different: Chapter 6 is about vetting what goes into training
you control; this chapter is about vetting an artifact you never trained
at all.

**Red flag:** Treats the two as interchangeable, or proposes applying
Chapter 6's data-provenance defenses to an upstream artifact with no
training step of the org's own.

**Follow-up:** "If your organization has excellent data-poisoning defenses
on its own fine-tuning pipeline, are you automatically protected against
Category 1 supply-chain risk? Why or why not?"

**What this proves:** Understands supply-chain risk as a genuinely
distinct failure mode from data poisoning, not a rebranding of it.

---

### 2. (Beginner) Name the three supply-chain risk categories this chapter covers, in one sentence each.

**Strong answer:** (1) Compromised or backdoored pretrained/fine-tuned
weights — a model or adapter published to a public hub was tampered with,
or trained on bad data, by whoever built and published it, and it's
deployed without independent verification. (2) Malicious or vulnerable
dependencies in the ML toolchain — unsafe serialization formats like
pickle that can execute arbitrary code on load, and malicious or
compromised packages in the PyPI/npm ecosystem ML teams depend on. (3)
Excessive trust in third-party plugins/tools/MCP servers — the initial
decision to connect a system to an external dependency without vetting
that component's own security posture, distinct from the runtime defenses
against an already-connected tool's adversarial output.

**Red flag:** Can only describe one category in detail, or conflates
Category 3 with Chapter 2's attack-surface mapping or Module 4's runtime
tool-output defenses.

**Follow-up:** "Which of the three would a routine dependency scan
actually catch, and which would it completely miss?"

**What this proves:** Has internalized the three categories as distinct
mechanisms with distinct points of failure, not one vague "supply chain"
idea.

---

### 3. (Intermediate) Explain why "we only use models from popular, well-known publishers" is not, by itself, a complete defense against Category 1 risk.

**Strong answer:** Popularity and name recognition say nothing about two
separate things that actually matter: whether the artifact's actual
content was independently verified, and whether even a legitimately
trusted source's own pipeline can be compromised without the source
itself being at fault. The real, documented case for the second point is
the `ultralytics` PyPI package — a genuinely popular, legitimately trusted
library, compromised in December 2024 through a vulnerability in its own
GitHub Actions build pipeline, with a tampered release published under
the real package name before it was caught. A team relying on "we only
use popular sources" as its supply-chain policy would have pulled that
exact compromised release, because the policy never asked the deeper
question: has this specific artifact's content been independently
verified this time, regardless of the publisher's overall reputation.

**Red flag:** Treats publisher reputation as a sufficient proxy for
artifact safety, or can't name a concrete mechanism by which a reputable
source's own artifact can still be compromised.

**Follow-up:** "Given that, what would you actually add to a 'popular
publishers only' policy to close this gap?"

**What this proves:** Understands that provenance verification has to
check the artifact, not just the publisher's reputation — the same
"what this stops, what it doesn't" discipline this course has required
since Chapter 3, applied to the adoption decision itself.

---

### 4. (Intermediate) A team says: "We converted all our model checkpoints from pickle to Safetensors, so we're now fully protected against a backdoored model." Evaluate this claim.

**Strong answer:** Overclaimed, and the specific gap is worth naming
precisely. Converting to Safetensors is a real, meaningful piece of
Defense 2 — it removes the arbitrary-code-execution-on-load risk
structurally, because Safetensors stores only tensor data and metadata,
not instructions Python can execute. But it does nothing at all about
Category 1's actual risk: a model's learned weights and any trigger-
conditioned behavior baked into them during training are completely
unaffected by which file format those same weights happen to be saved
in. A backdoored adapter converted from pickle to Safetensors is still
exactly as backdoored — the conversion only closes the separate,
additional risk that loading the file itself executes attacker code.
"Fully protected against a backdoored model" describes an outcome this
chapter's Defense 2 explicitly does not claim to deliver.

**Red flag:** Accepts "we use Safetensors" as a complete defense against
backdoors, or doesn't distinguish the code-execution-on-load risk from
the model's-own-learned-behavior risk.

**Follow-up:** "What would you add to actually address the risk that the
model's own weights, regardless of file format, contain a planted
trigger?"

**What this proves:** Can evaluate a specific technical mitigation's
actual scope precisely, distinguishing a file-format risk from a
learned-behavior risk that happen to be discussed in the same chapter.

---

### 5. (Senior) Design an internal vetted-registry and approval process for new models, adapters, and third-party tools that would have a real chance of preventing a Solstice-Diagnostics-shaped incident (three separate under-deadline decisions, each individually reasonable-looking, none reviewed). What makes this genuinely hard to operate well, not just to design on paper?

**Strong answer:** A real process needs, at minimum: a mandatory gate
before any new model, adapter, or third-party tool reaches production
(not a recommended step easily skipped under deadline pressure);
concrete, checkable criteria at that gate (provenance verification per
Defense 1, a confirmed safe loading path per Defense 2, a completed
dependency scan per Defense 3, and for any third-party tool specifically,
an actual, answered security questionnaire from the vendor, not an
assumption); and a registry other teams can pull already-vetted
components from, so the vetting cost is paid once, not re-paid (or
skipped) by every team independently. What makes this genuinely hard is
the honest limit this chapter's own Defense 4 section names: a process
that exists on paper is worthless if a deadline makes skipping it the
path of least resistance, and Solstice's own three decisions weren't
made by people who didn't know better in the abstract — they were made
by people under real time pressure with no gate that would have stopped
them. A real operational design has to make the gate genuinely hard to
bypass (blocking a production deployment path technically, not just
asking nicely) and has to be paired with leadership that treats a
blocked deadline as an acceptable cost of the gate actually working —
which is an organizational commitment, not an engineering design
choice.

**Red flag:** Proposes only a checklist or a recommended review with no
enforcement mechanism, or doesn't address what happens when the gate
conflicts with a real deadline.

**Follow-up:** "Your approval gate blocks a launch two days before a
committed deadline because a new tool integration hasn't been vetted.
What actually happens next, and who decides?"

**What this proves:** Can design a real, enforceable process rather than
a paper policy, and reasons honestly about the organizational tension
between a security gate and delivery pressure — not just the technical
shape of the gate itself.

---

### 6. (Senior) Coppervale's leadership wants to rely solely on "we only pull models from Hugging Face, a reputable platform" as its supply-chain policy, arguing platform reputation is sufficient. Evaluate this as a sole strategy.

**Strong answer:** Insufficient as a sole strategy, and the gap is
directly evidenced by this chapter's own cited research. JFrog's security
research found roughly 100 malicious models hosted on Hugging Face itself
using a pickle payload to establish a reverse shell — the platform's own
existing scanning (including PickleScan, built with Microsoft) did not
catch all of them, and independent research (Sonatype, and the PickleBall
paper's own findings) shows the scanning approach itself has real,
disclosed bypass vulnerabilities and measured false-negative rates. A
reputable hosting platform is a real, positive signal — it's meaningfully
different from an anonymous, unmoderated file share — but "hosted on a
reputable platform" and "independently verified safe" are not the same
claim, and this chapter's own research shows the gap between them is not
hypothetical. A sound policy uses the platform's own scanning as one
signal among several (Defenses 1-4), not as the entire policy.

**Red flag:** Treats platform reputation as equivalent to independent
verification, or is unaware that the platform's own scanning has
documented gaps.

**Follow-up:** "Given that even the platform's own scanning has known
gaps, what additional, independent check would you add before trusting
a specific model pulled from it?"

**What this proves:** Can evaluate a platform-level control's real,
bounded scope honestly, using this chapter's own cited research rather
than a general instinct that "a well-known platform is probably fine."

---

### 7. (Architect) You're advising a healthcare-adjacent startup (Solstice-shaped) on whether to build formal, SLSA-style signed provenance attestation into its ML pipeline from day one, versus relying on Defenses 1-4 applied informally as needed. What tradeoffs would you name, and how would you decide?

**Strong answer:** A formal, signed-attestation approach (the Atlas-style
framework this chapter cites, built on the same attestation family SLSA
uses for traditional software) provides a categorically stronger
guarantee than informal, ad hoc provenance checks: cryptographically
verifiable, tamper-evident records of exactly how an artifact was built,
from what source, rather than an unverified claim on a model card that
anyone could have written inaccurately or dishonestly. The real tradeoff
to name explicitly: building and operating a formal attestation pipeline
is real, ongoing engineering investment — it requires tooling most teams
don't have installed by default, a process for every internal fine-tuning
run to actually produce a signed attestation (not just document it after
the fact), and a real cost in engineering time that has to be weighed
against a startup's actual risk profile. For a healthcare-adjacent product
specifically, where a Category 1 backdoor could directly affect a
clinical triage decision, the sensitivity of the failure mode argues for
investing early rather than retrofitting after an incident — the same
"first-class design input, not a post-launch patch" reasoning Chapter 7's
own architect-level question established for extraction risk. The
decision should weigh: (1) how directly a Category 1 failure could cause
real harm in this specific product (here, genuinely high — a suppressed
urgency flag is a patient-safety issue, not just a business one), (2) the
team's actual engineering capacity to build and maintain attestation
tooling versus applying Defenses 1-4 informally but consistently, and (3)
whether informal application of Defenses 1-4, actually enforced by
Defense 4's approval gate, already closes enough of the gap that formal
attestation's added guarantee isn't proportionate to its cost yet.

**Red flag:** Recommends formal attestation unconditionally regardless of
risk profile or team capacity, or dismisses it as unnecessary overhead
without weighing the specific harm profile of a healthcare-adjacent
product.

**Follow-up:** "The team can't staff a formal attestation pipeline this
quarter. What's the strongest informal version of Defenses 1-4 you'd
insist on instead, and what residual risk would you document as
accepted?"

**What this proves:** Architect-level judgment — weighs a stronger,
more expensive guarantee against a team's real capacity and a product's
actual harm profile, rather than treating "more formal security tooling"
as an unconditional good.

---

### 8. (Architect) Given that this chapter's research shows both a major public model hub (JFrog's finding) and a widely trusted, legitimate PyPI package (`ultralytics`) have each been real, documented supply-chain compromise vectors, how should this change how your org designs a *new* LLM-powered product's dependency-adoption process from the start, rather than trusting individual sources on a case-by-case basis?

**Strong answer:** The two findings together establish something a
case-by-case trust model can't capture: neither "obscure, unknown source"
nor "well-known, reputable source" is a reliable predictor of safety on
its own, because both failure modes are real and documented against
real, currently-used infrastructure. A from-the-start design should treat
every dependency — whether a base model, an adapter, a library, or a
tool — as requiring the same baseline verification regardless of source
reputation: (1) build the internal vetted-registry and approval gate
(Defense 4) into the org's actual deployment pipeline from day one, not
as a policy document, so no artifact reaches production without clearing
it; (2) default to safe serialization formats (Defense 2) for any new
internal model artifact, and treat any external artifact still using an
unsafe format as requiring sandboxed loading, no exceptions based on
publisher reputation; (3) build dependency scanning and pinning (Defense
3) into CI/CD from the start, with a deliberate, reviewed process for
version bumps rather than auto-updating on a schedule that outruns
review; (4) require provenance verification (Defense 1) — checksums,
signed attestations where available — as a mandatory step regardless of
whether the source is an anonymous hub account or Hugging Face itself.
Crucially, none of this produces a guarantee of zero supply-chain risk —
the honest deliverable is the same one this course has required since
Chapter 5: a documented, stated residual-risk posture, communicated to
the business before launch, naming specifically what's verified, what's
accepted risk, and what would trigger an incident response if a
compromise like the ones this chapter cites happened to your own
dependency instead of someone else's.

**Red flag:** Proposes a policy that still trusts reputable sources by
default without independent verification, or treats supply-chain
defenses as something to add only after a specific incident.

**Follow-up:** "Six months after launch, your provenance-verification
step flags a checksum mismatch on a library your team has used without
incident for years. Walk me through what you'd actually do in the next
24 hours."

**What this proves:** Can synthesize research findings that cut against
the natural instinct to trust reputation, and design a uniform,
from-the-start adoption process rather than a source-by-source judgment
call — genuine architect-level systems thinking about an entire org's
dependency-adoption posture, not just a single artifact's evaluation.

## Strategy Tips

- Keep the "you never trained anything" distinction sharp for Category 1:
  supply-chain risk in inherited weights means none of Chapter 6's
  data-pipeline defenses have anything to attach to, because there was
  no training step of your own.
- Be ready to name which of the three categories (compromised weights,
  vulnerable ML-toolchain dependency, excessive tool trust) a given
  scenario fits, and precisely what's new about Category 3 relative to
  Chapter 2's and Module 4's tool-related coverage (the initial trust
  decision, not the runtime behavior of an already-added tool).
- For every defense, be ready to state its honest limit, not just what
  it catches — especially that safe loading (Defense 2) says nothing
  about a model's own learned behavior, and that a reputable source
  (platform or package) can still be compromised, per this chapter's
  own cited JFrog and ultralytics evidence.
- For senior/architect questions, the interviewer is listening for
  layered, category-aware thinking, an explicit residual-risk posture,
  and — at the architect level — a uniform, from-the-start adoption
  process rather than case-by-case trust based on source reputation
  alone.
