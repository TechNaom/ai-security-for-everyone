# Chapter 13 / Capstone Rubric — L4 Architecture Challenge

Per `docs/curriculum/CURRICULUM_MAP.md`'s Module 6 entry, this project's
assessment type is **"capstone rubric (architecture challenge, Level
4)"** — the course's final, and only Architect-tier, project. This
rubric grades ADR quality and trade-off reasoning, not just "did you
list all ten OWASP categories." It has **six criteria, one more than
every prior chapter's five-criterion rubric**, reflecting the added
judgment dimensions a Level 4 architecture challenge requires beyond a
find-and-fix lab (Chapters 9, 10, 12) or a single findings report
(Chapter 11). Each criterion is worth up to 4 points (24 points total).

## 1. Threat-model completeness and honesty (0-4)

- **4:** All ten OWASP 2026 categories are present with a real,
  specific rationale tied to a named Aegis Copilot component — and at
  least one category the team cannot confidently rate is flagged
  honestly (not silently rated with false confidence, not silently
  omitted).
- **2:** All ten categories are present, but rationale is generic
  (could apply to any LLM system, not specifically to Aegis Copilot),
  or no category is honestly flagged as low-confidence even though the
  course itself never built dedicated depth on LLM06/LLM07.
- **0:** Categories are missing, or every rationale is a placeholder.

## 2. ADR quality and real trade-off reasoning (0-4)

- **4:** All six required ADRs (per `REQUIRED_ADR_TOPICS`) state a real
  decision, at least one seriously-considered rejected alternative
  (not a straw man), and a real, honestly-priced trade-off — not "we
  did the secure thing, no downsides." Every ADR reads like the
  lesson's own ADR-02 worked example: a decision a future engineer
  could actually understand and not silently violate.
- **2:** ADRs are present for all six topics, but at least half list
  "none" or a trivial trade-off, or an alternative that was never a
  real contender (e.g., "do nothing" as the only alternative
  considered).
- **0:** Fewer than six required ADRs are present, or ADRs are just a
  list of mitigations with no context/alternatives/trade-off structure
  at all.

## 3. Correct application of Chapter 5's three-category defense taxonomy (0-4)

- **4:** Every ADR states which of structural, detection, or
  consequence-bounding its decision belongs to, the tag is factually
  correct for what the decision actually does, and the ADR set uses
  more than one category across the six decisions — not every decision
  labeled "structural" regardless of what it actually does.
- **2:** Categories are stated but at least one is mislabeled (e.g., a
  detection-based scanner tagged "structural"), or the set leans
  entirely on one category with no acknowledgment that other decisions
  need a different one.
- **0:** No defense category stated for any ADR, or categories are
  applied inconsistently with no evident understanding of what each one
  actually means.

## 4. Self-directed red-team pass with real findings (0-4)

- **4:** At least two real, specific findings against the learner's own
  ADR set, spanning more than one severity level, each naming exactly
  which ADR's stated purpose the finding defeats or leaves open — not
  vague ("there might be edge cases") but a real, reasoned gap (like
  this chapter's own ADR-06 email-body example).
- **2:** Findings are present but generic, restate a risk the ADR
  itself already fully addresses (not a real residual gap), or all
  carry the same severity with no differentiation.
- **0:** Zero findings, or findings that don't reference any specific
  ADR at all.

## 5. Honest, prioritized launch recommendation (0-4)

- **4:** The final recommendation explicitly separates at least three
  categories — must-fix before GA, accepted and monitored residual
  risk, and needs-further-review — referencing specific findings and
  threat-model gaps by name, not a single undifferentiated GO/NO-GO
  statement.
- **2:** A recommendation is present but collapses to a single
  launch/no-launch statement, or doesn't reference the actual findings
  and flagged gaps produced earlier in the same submission.
- **0:** No launch recommendation, or one that contradicts the
  submission's own findings (e.g., recommending unconditional GO
  despite an unresolved "blocking" finding).

## 6. Coherence: the whole review reads as one system, not four disconnected artifacts (0-4)

- **4:** The threat model's flagged risks are the ones the ADRs
  address; the red-team findings target the actual ADRs written (not
  generic industry advice); the launch recommendation's priorities
  trace back to the findings' severities. A reader could follow the
  reasoning from "here's the system" to "here's what we decided and
  why" to "here's what we checked" to "here's what we recommend"
  without a gap in the chain.
- **2:** The four pieces are individually reasonable but don't clearly
  connect — an ADR addresses a risk the threat model never flagged, or
  a finding targets an ADR that doesn't exist.
- **0:** The four sections read as unrelated exercises with no evident
  connection to the same system or to each other.

## Passing bar

**19/24 (about 80%)** or higher, with no single criterion scoring 0, is
a passing capstone submission for this chapter's own self-graded check —
the same honest, stated-limit grading discipline this course has used
since Chapter 5, now scaled to a sixth criterion this project's added
judgment dimension requires.

## How this rubric was used to grade `solution.py`

Run `python3 solution.py`. Its self-check assertions directly verify
criteria 1-4 and 6 at full strength: all ten threat-model categories
present with real, component-specific rationale (criterion 1, including
the honest LLM06/LLM07 flag); all six required ADRs valid with real
alternatives and trade-offs (criterion 2); all three defense categories
genuinely used across the six ADRs, correctly tagged (criterion 3);
three real red-team findings spanning all three severities, each naming
a specific ADR (criterion 4); and the whole submission traces
coherently from system description through ADRs through findings
(criterion 6). It scores **only 0/4 on criterion 5** —
`LAUNCH_RECOMMENDATION` is deliberately left as a structural placeholder
naming that a synthesis is needed, not a finished, prioritized
recommendation, matching Chapter 11's own precedent of deliberately
leaving one criterion's actual skill for the learner to practice rather
than copy. A genuinely complete submission (your own written launch
recommendation, synthesizing `solution.py`'s three findings — or your
own — into a real must-fix/accepted/follow-up breakdown) should close
that gap and score in the 22-24/24 range.
