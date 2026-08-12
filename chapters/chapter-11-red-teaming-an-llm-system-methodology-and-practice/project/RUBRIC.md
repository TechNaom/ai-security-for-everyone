# Chapter 11 / Module 5 Findings-Report Rubric

Module 5's own assessment type, per `docs/curriculum/CURRICULUM_MAP.md`,
is "a red-team report graded against a rubric" — a genuinely different
shape from every prior module's project or written exam. This is that
rubric. Grade your own completed `starter.py` output (or a hand-written
Markdown report built from it) against the five criteria below, each
worth up to 4 points (20 points total).

## 1. Scope and methodology (0-4)

- **4:** States exactly what was and wasn't tested (matching
  `ENGAGEMENT_SCOPE`), names the methodology used (the five-phase
  process from `lesson.html`), and a reader unfamiliar with the
  engagement can tell precisely what claims the report does and doesn't
  make.
- **2:** States scope but not methodology, or vice versa.
- **0:** No stated scope — a reader could reasonably (and wrongly)
  assume the whole system was tested.

## 2. Reproducibility (0-4)

- **4:** Every finding includes exact reproduction steps (the specific
  function call, question, wiki_query, and account_id) precise enough
  for a second person to independently re-run and confirm.
- **2:** Reproduction steps are present but vague (e.g., "ask about
  refunds" instead of the exact question string used).
- **0:** No reproduction steps, or steps that don't match what
  `run_test_case` actually executed.

## 3. Severity classification (0-4)

- **4:** Every confirmed finding has an explicit likelihood and impact
  score (1-4 each), a combined score, and a rating derived from the
  stated formula — consistently applied across all findings, with a
  one-sentence justification for each axis's score.
- **2:** Ratings present but inconsistent (e.g., different formulas
  used per finding, or no justification for the scores chosen).
- **0:** No severity rating, or a rating with no visible basis.

## 4. Recommended fix, real and specific (0-4)

- **4:** Every finding's recommended fix names a real, specific,
  already-taught defense from the correct source chapter (Chapter 3, 9,
  or 10, per `RECOMMENDED_FIXES`) — not a vague "add more security"
  statement, and not an invented defense this course never taught.
- **2:** A fix is present but generic, or points to the wrong chapter's
  defense set for that finding's mechanism.
- **0:** No recommended fix, or a fix that would itself function as
  guidance for a real exploit rather than a real mitigation.

## 5. Executive summary and prioritization (0-4)

- **4:** The report opens with a short summary a non-technical
  stakeholder can act on (what was tested, what was found, overall risk
  level), and closes with a prioritized remediation order matching the
  computed severity ratings, highest first.
- **2:** One of the two (summary or prioritized order) is present, not
  both.
- **0:** Neither present — a reader has to read every finding in full to
  understand overall risk or what to fix first.

## Passing bar

**16/20 (80%)** or higher, with no single criterion scoring 0, is a
passing findings report for this chapter's own self-graded check. This
mirrors the honest, stated-limit grading discipline this course has used
since Chapter 5 — a report that scores well on four criteria but
completely misses one (e.g., real severity scores but zero
reproducibility) is not a passing report, the same way a defense that
stops one attack vector but ignores another isn't "mostly secure."

## How this rubric was used to grade `solution.py`'s own output

Run `python3 solution.py` and grade its printed report against the five
criteria above. It scores 4/4 on criteria 1-4: stated scope and
methodology, exact reproduction steps per finding via
`simulate_assembled_prompt(...)` calls with real arguments, a real
likelihood/impact score and justification comment per finding
(`FINDING_SEVERITY_INPUTS`), and a real named defense per finding
pointing back to the correct chapter (`RECOMMENDED_FIXES`). It scores
only 2/4 on criterion 5 (executive summary and prioritization) --
`solution.py`'s auto-generated report includes a confirmed-findings
count but deliberately does not include a short, non-technical
executive summary or a severity-ordered remediation list. That gap is
intentional: writing those two pieces from the confirmed findings and
their computed severities is the concrete Phase 5 skill this project
leaves for you to practice, not something to copy from a reference
file. A genuinely complete report (your own edited version, or a
hand-written Markdown file built from `solution.py`'s findings) should
close that gap and score 18-20/20.
