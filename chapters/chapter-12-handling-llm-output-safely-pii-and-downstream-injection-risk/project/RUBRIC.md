# Chapter 12 Find-and-Fix Rubric

This chapter's project is a find-and-fix defense lab (see `README.md`
for why, versus Chapter 11's rubric-graded findings-report shape). Grade
your own completed `starter.py` against the five criteria below, each
worth up to 4 points (20 points total).

## 1. Vulnerability reproduction understood (0-4)

- **4:** Can explain, for each of the three naive functions
  (`generate_ticket_summary`, `render_suggested_reply`,
  `get_related_case_link`), exactly why it's vulnerable and which of
  this chapter's failure shapes it demonstrates (PII reproduction,
  rendered-output injection, downstream-API injection).
- **2:** Can identify that the naive functions are vulnerable but not
  explain the specific mechanism or map it to the correct failure shape.
- **0:** Cannot explain why the naive target is vulnerable at all.

## 2. PII redaction defense (0-4)

- **4:** `redact_pii()` correctly redacts every email and phone-number
  pattern in `secure_generate_ticket_summary()`'s output for all three
  tickets, and you can state its honest limit (doesn't catch free-text
  sensitive detail like Priya's "my ex-husband" mention).
- **2:** `redact_pii()` works on some but not all patterns, or works
  correctly but with no stated understanding of its limits.
- **0:** `redact_pii()` is unimplemented or doesn't redact structured
  PII at all.

## 3. Rendered-output injection defense (0-4)

- **4:** `html_escape_output()` correctly escapes all five special
  characters, applied before interpolation in
  `secure_render_suggested_reply()`, closing T-1002's payload while
  T-1003's legitimate reply text is unchanged in meaning.
- **2:** Escaping is implemented but incomplete (e.g., missing quote
  escaping) or applied in the wrong order (escaping `&` after the
  entities it should protect, causing double-escaping).
- **0:** `html_escape_output()` is unimplemented or the naive unescaped
  payload still reaches the rendered output.

## 4. Downstream-API injection defense (0-4)

- **4:** `is_allowed_case_link()` correctly accepts only exact
  allow-listed hosts over `https://`, rejects `http://`, and rejects
  look-alike subdomains (`cases.fenwick-cx.example.evil.com`,
  `evil.cases.fenwick-cx.example`) — verified by re-running
  `starter.py` and confirming T-1002's link is blocked (`None`) while
  T-1001/T-1003's legitimate links pass through.
- **2:** The check works for the obvious malicious case but is fooled by
  a look-alike-subdomain trick, or blocks legitimate links too.
- **0:** `is_allowed_case_link()` is unimplemented or always returns the
  same value regardless of input.

## 5. No regression on legitimate behavior, and structural (not instructional) framing (0-4)

- **4:** T-1003's summary, reply, and link all pass through the secure
  pipeline unchanged in meaning (no over-aggressive redaction or
  escaping breaking legitimate content), and you can explain — in your
  own words, referencing this chapter's own "structure beats a request
  for good behavior" principle — why these three fixes are structural
  controls rather than a system-prompt instruction, and why that
  distinction matters.
- **2:** No regression on legitimate behavior, but no clear articulation
  of the structural-versus-instructional distinction.
- **0:** Legitimate behavior is broken (e.g., T-1003's clean summary is
  mangled), or the explanation proposes a prompt-level instruction as
  sufficient on its own.

## Passing bar

**16/20 (80%)** or higher, with no single criterion scoring 0, is a
passing implementation for this chapter's own self-graded check. This
mirrors the honest, stated-limit grading discipline this course has used
since Chapter 5 — closing three defenses well but breaking legitimate
behavior on criterion 5, or closing them without understanding *why*
they work structurally, is not a passing implementation.

## How this rubric was used to grade `solution.py`

Run `python3 solution.py`. It scores 4/4 on all five criteria: the
self-check assertion block at the bottom of the file directly verifies
all three naive vulnerabilities reproduce, all three secure defenses
close them, look-alike-subdomain resistance holds, and T-1003's
legitimate behavior is unchanged (`"shipped on time" in
secure_generate_ticket_summary("T-1003")` and the equivalent reply
check both pass). The redaction docstring states its honest limit
explicitly (doesn't catch Priya's free-text detail), matching criterion
2's 4-point bar. Your own implementation, written independently rather
than copied from `solution.py`, should aim for the same 20/20 —
unlike Chapter 11's project, this rubric doesn't leave a criterion
deliberately incomplete in the reference solution, since a find-and-fix
lab's skill (implementing working defenses) is fully demonstrable in one
reference pass.
