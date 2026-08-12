"""
Chapter 10 Exercises: Securing Agentic Systems Against Adversarial Tool Output

Scenario for these exercises (deliberately different from the lesson's
Ferngate Logistics example): Talbridge Health Network, a fictional
regional healthcare provider.

    Talbridge Health Network runs Rounds Assistant, an internal agentic
    tool that helps clinic schedulers manage patient appointments.
    Rounds Assistant has two tools: check_lab_status(patient_id), which
    queries a partner lab-results API and returns a patient's latest lab
    processing status, and reschedule_priority_slot(patient_id, slot_id),
    a side-effecting tool that bumps a patient into a same-day priority
    slot, displacing whichever appointment currently holds it. A security
    review is assessing Rounds Assistant's exposure to adversarial tool
    output using this chapter's three-moment round-trip model, six
    defenses, and cited research.

Fill in every TODO below, then run this file:

    python3 starter.py

to see your score. Compare against solution.py for reference answers.
"""

MOMENTS = {
    "result_arrival": "Result arrival -- what the tool actually returns, before it reaches the model",
    "context_assembly": "Context assembly -- how the result gets formatted into what the model sees next",
    "action_proposal": "Action proposal -- what the model decides to do next, based on that context",
}

DEFENSES = {
    "schema_validation": "Schema and type validation of tool results",
    "content_sanitization": "Content sanitization of tool-result free text",
    "structural_separation": "Structural separation and reinforced framing of tool results",
    "provenance_tagging": "Field-level provenance tagging",
    "permission_scoping": "Permission and capability scoping per tool call",
    "human_in_loop_backstop": "Human-in-the-loop confirmation and a hard least-privilege backstop",
}

RESEARCH_SOURCES = {
    "owasp_llm06": "OWASP Top 10 for LLM Applications 2025 (LLM06:2025, Excessive Agency)",
    "owasp_agentic_top10": "OWASP GenAI Security Project, Top 10 for Agentic Applications (v1.0, December 2025) -- ASI02 Tool Misuse, ASI03 Identity & Privilege Abuse",
    "injecagent_2024": "Zhan, Ding, Xu, Tan, Xu, Kang, and He, 'InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated Large Language Model Agents' (arXiv:2403.02691, ACL 2024 Findings)",
    "agentdojo_2024": "Debenedetti, Zhang, Balunović, Beurer-Kellner, Fischer, and Tramèr, 'AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents' (arXiv:2406.13352)",
}

# ---------------------------------------------------------------------------
# Exercise 1 -- Classify six scenarios into the correct round-trip moment.
# Use the short keys from MOMENTS.
# ---------------------------------------------------------------------------
EXERCISE_1_SCENARIOS = {
    "lab_api_mixed_fields": "The partner lab API's JSON response mixes a structured, lab-system-generated 'result_code' enum with a free-text 'clinician_comment' field populated by whoever last annotated the result, with nothing in the response distinguishing which is which.",
    "tool_role_not_enough": "Rounds Assistant puts check_lab_status's result inside a proper tool-role message in the framework's message list, but the model still treats a persuasive sentence inside clinician_comment as an instruction.",
    "model_proposes_reschedule": "After reading check_lab_status's result, the model proposes calling reschedule_priority_slot for a patient, unprompted, based solely on wording found in clinician_comment.",
    "raw_concatenation_tool_and_system": "Rounds Assistant's prompt-assembly code concatenates the tool result directly after the system prompt with no delimiters and no framing distinguishing tool output from system instructions.",
    "unscoped_credential": "The credential Rounds Assistant's check_lab_status call uses can also write to the scheduling database, even though the tool itself only ever reads lab data.",
    "no_confirmation_before_execute": "reschedule_priority_slot executes immediately once the model decides to call it, with no human confirmation step anywhere in the flow.",
}

exercise_1_answers = {
    "lab_api_mixed_fields": "result_arrival",
    "tool_role_not_enough": "context_assembly",
    "model_proposes_reschedule": "action_proposal",
    "raw_concatenation_tool_and_system": "context_assembly",
    "unscoped_credential": "action_proposal",
    "no_confirmation_before_execute": "action_proposal",
}

# ---------------------------------------------------------------------------
# Exercise 2 (production-gear: compute a real permission-scope risk score)
# -- Talbridge's security team scores each tool call on a composite signal
# combining four independent 0/1 checks:
#
#   credential_matches_tool_scope = False  (the credential can do MORE than the tool exposes)
#   result_can_expand_authority = True     (a tool's result CAN itself grant new authority)
#   side_effecting = True                  (the tool call has a real side effect)
#   human_gate_present = False             (there is NO human confirmation step before execution)
#
#   risk_score = (number of RISKY checks / 4) * 100, rounded to 1 decimal place
#   -- a check counts as "risky" when its value indicates the DANGEROUS
#      condition: credential_matches_tool_scope=False is risky,
#      result_can_expand_authority=True is risky, side_effecting=True is
#      risky, human_gate_present=False is risky.
# ---------------------------------------------------------------------------
CREDENTIAL_MATCHES_TOOL_SCOPE = False
RESULT_CAN_EXPAND_AUTHORITY = True
SIDE_EFFECTING = True
HUMAN_GATE_PRESENT = False


def compute_permission_risk_score():
    risky_checks = [
        CREDENTIAL_MATCHES_TOOL_SCOPE is False,
        RESULT_CAN_EXPAND_AUTHORITY is True,
        SIDE_EFFECTING is True,
        HUMAN_GATE_PRESENT is False,
    ]
    return round((sum(risky_checks) / 4) * 100, 1)


# ---------------------------------------------------------------------------
# Exercise 3 -- For each statement, decide whether it describes a real,
# honest agentic-defense claim (True) or an overclaim (False).
# ---------------------------------------------------------------------------
EXERCISE_3_STATEMENTS = {
    "stmt_a": "\"We put every tool result inside a proper tool-role message, so our message structure itself guarantees the model won't treat its content as an instruction.\"",
    "stmt_b": "\"Tool-role message structure is necessary scaffolding, not a content-level defense on its own -- we reinforce framing inside the message content itself and layer sanitization and permission scoping on top.\"",
    "stmt_c": "\"We schema-validate every tool response, so no malicious content can reach the model through a tool call.\"",
    "stmt_d": "\"Schema validation confirms a free-text field is the right shape; it doesn't confirm the field's content is safe, since the field is supposed to contain arbitrary text.\"",
}

exercise_3_answers = {
    "stmt_a": False,
    "stmt_b": True,
    "stmt_c": False,
    "stmt_d": True,
}

# ---------------------------------------------------------------------------
# Exercise 4 (production-gear: defense matching) -- For each scenario, name
# which single defense from DEFENSES is the BEST fit, using the keys above.
# ---------------------------------------------------------------------------
EXERCISE_4_SCENARIOS = {
    "planted_note_no_directive_phrasing": "A planted instruction in clinician_comment is worded to read exactly like an ordinary clinical annotation, with no explicit 'system:' or directive phrasing a pattern scanner could catch.",
    "no_field_trust_recorded": "Nothing in Rounds Assistant's tool-handling code records that result_code is lab-system-generated while clinician_comment is externally submitted free text.",
    "credential_reaches_further_than_tool": "The credential behind check_lab_status can write to the scheduling database, even though the tool itself only exposes a read-only lab-status lookup.",
    "reschedule_authorized_by_tool_content_alone": "reschedule_priority_slot gets called on the strength of clinician_comment's wording alone, with no independent human check and no hard rule preventing a tool result from authorizing it.",
}

exercise_4_answers = {
    "planted_note_no_directive_phrasing": "content_sanitization",
    "no_field_trust_recorded": "provenance_tagging",
    "credential_reaches_further_than_tool": "permission_scoping",
    "reschedule_authorized_by_tool_content_alone": "human_in_loop_backstop",
}

# ---------------------------------------------------------------------------
# Exercise 5 -- Match each of the two named moments below to the defense
# that operates there most directly (per this chapter's own pairing). Note:
# action-proposal is intentionally excluded here -- Exercise 4 already
# covers Defenses 5 and 6 from a scenario-matching angle.
# ---------------------------------------------------------------------------
exercise_5_answers = {
    "result_arrival": "schema_validation",
    "context_assembly": "structural_separation",
}

# ---------------------------------------------------------------------------
# Exercise 6 (production-gear: critique flawed reports) -- For each report
# excerpt, decide whether it contains a real, flawed reasoning gap (True) or
# is sound (False).
# ---------------------------------------------------------------------------
EXERCISE_6_REPORTS = {
    "report_a": "\"We added a hard dollar cap to reschedule_priority_slot's underlying credit-adjacent logic, so our agentic tool-output exposure is now fully closed.\"",
    "report_b": "\"A dollar cap on one tool's one parameter is a real, useful piece of the human-in-the-loop backstop, but it doesn't address schema validation, sanitization, structural framing, or permission scoping -- we're treating it as one layer, not a complete posture.\"",
    "report_c": "\"Our system prompt tells the model tool results are never instructions, so our pipeline architecturally cannot be manipulated by a planted tool result.\"",
    "report_d": "\"Our system prompt reinforces that tool results are data, not instructions -- a real reliability improvement, but role weighting is trained, not architecturally guaranteed, so we don't treat this as a hard guarantee.\"",
}

exercise_6_answers = {
    "report_a": True,
    "report_b": False,
    "report_c": True,
    "report_d": False,
}

# ---------------------------------------------------------------------------
# Exercise 7 (production-gear: research citation matching) -- Match each
# finding to its real, cited source using RESEARCH_SOURCES keys.
# ---------------------------------------------------------------------------
EXERCISE_7_FINDINGS = {
    "excessive_agency_category": "Names the risk of a system granting a tool more functionality, permission, or autonomy than a task requires, with no human checkpoint at a point one is warranted.",
    "tool_misuse_and_privilege_categories": "A December 2025 taxonomy naming both an agent bending a legitimate tool toward a destructive outcome, and a credential/permission-scoping gap, as current, dedicated categories.",
    "twenty_four_percent_finding": "Measured a strong, widely-deployed model successfully manipulated via tool output roughly a quarter of the time in a base setting, nearly doubling under a reinforced-attacker-instruction variant.",
    "forty_eight_percent_finding": "Measured a targeted attack success rate of roughly 48% against a strong model across 629 realistic security test cases spanning email, e-banking, and travel-booking agent tasks.",
}

exercise_7_answers = {
    "excessive_agency_category": "owasp_llm06",
    "tool_misuse_and_privilege_categories": "owasp_agentic_top10",
    "twenty_four_percent_finding": "injecagent_2024",
    "forty_eight_percent_finding": "agentdojo_2024",
}

# ---------------------------------------------------------------------------
# Exercise 8 (production-gear: written reasoning) -- Write a one-sentence
# justification for why field-level provenance tagging (Defense 4) alone
# doesn't stop anything. Must reference BOTH the idea that it's a
# prerequisite/enabling step AND the idea that later defenses (permission
# scoping, human-in-the-loop) are what actually act on the tagged trust
# tiers, to pass the substance check.
# ---------------------------------------------------------------------------
exercise_8_reasoning = (
    "Field-level provenance tagging is a prerequisite, enabling step that "
    "records which fields are high-trust and which are low-trust; it "
    "doesn't block or filter anything by itself -- it's only useful once "
    "later defenses, like permission scoping and the human-in-the-loop "
    "backstop, actually act on the tags it produces."
)


# ===========================================================================
# Scoring harness -- do not need to edit anything below this line.
# ===========================================================================

def score_exercise_1():
    key = {
        "lab_api_mixed_fields": "result_arrival",
        "tool_role_not_enough": "context_assembly",
        "model_proposes_reschedule": "action_proposal",
        "raw_concatenation_tool_and_system": "context_assembly",
        "unscoped_credential": "action_proposal",
        "no_confirmation_before_execute": "action_proposal",
    }
    correct = sum(1 for k, v in key.items() if exercise_1_answers.get(k) == v)
    return correct, len(key)


def score_exercise_2():
    correct = 0
    if abs(compute_permission_risk_score() - 100.0) < 0.02:
        correct += 1
    return correct, 1


def score_exercise_3():
    key = {"stmt_a": False, "stmt_b": True, "stmt_c": False, "stmt_d": True}
    correct = sum(1 for k, v in key.items() if exercise_3_answers.get(k) is v)
    return correct, len(key)


def score_exercise_4():
    key = {
        "planted_note_no_directive_phrasing": "content_sanitization",
        "no_field_trust_recorded": "provenance_tagging",
        "credential_reaches_further_than_tool": "permission_scoping",
        "reschedule_authorized_by_tool_content_alone": "human_in_loop_backstop",
    }
    correct = sum(1 for k, v in key.items() if exercise_4_answers.get(k) == v)
    return correct, len(key)


def score_exercise_5():
    key = {
        "result_arrival": "schema_validation",
        "context_assembly": "structural_separation",
    }
    correct = sum(1 for k, v in key.items() if exercise_5_answers.get(k) == v)
    return correct, len(key)


def score_exercise_6():
    key = {"report_a": True, "report_b": False, "report_c": True, "report_d": False}
    correct = sum(1 for k, v in key.items() if exercise_6_answers.get(k) is v)
    return correct, len(key)


def score_exercise_7():
    key = {
        "excessive_agency_category": "owasp_llm06",
        "tool_misuse_and_privilege_categories": "owasp_agentic_top10",
        "twenty_four_percent_finding": "injecagent_2024",
        "forty_eight_percent_finding": "agentdojo_2024",
    }
    correct = sum(1 for k, v in key.items() if exercise_7_answers.get(k) == v)
    return correct, len(key)


def score_exercise_8():
    text = exercise_8_reasoning.lower()
    prereq_words = ["prerequisite", "enable", "enabling", "requires", "depends", "own its own", "by itself"]
    action_words = ["permission", "scoping", "human", "confirmation", "act on", "later defense", "backstop"]
    has_prereq = any(w in text for w in prereq_words)
    has_action = any(w in text for w in action_words)
    correct = int(has_prereq) + int(has_action)
    return correct, 2


def main():
    exercises = [
        ("Exercise 1 -- classify scenarios by round-trip moment", score_exercise_1),
        ("Exercise 2 -- compute a real permission-scope risk score", score_exercise_2),
        ("Exercise 3 -- honest claim vs. overclaim", score_exercise_3),
        ("Exercise 4 -- match defense to scenario", score_exercise_4),
        ("Exercise 5 -- match moment to its defense", score_exercise_5),
        ("Exercise 6 -- critique flawed reports", score_exercise_6),
        ("Exercise 7 -- research citation matching", score_exercise_7),
        ("Exercise 8 -- written reasoning", score_exercise_8),
    ]

    total_correct = 0
    total_possible = 0
    print("Chapter 10 Exercises -- Score Report")
    print("=" * 60)
    for label, fn in exercises:
        correct, possible = fn()
        total_correct += correct
        total_possible += possible
        print(f"{label}: {correct}/{possible}")
    print("=" * 60)
    print(f"TOTAL: {total_correct}/{total_possible}")
    if total_possible and total_correct == total_possible:
        print("Perfect score -- every scenario correctly classified and evaluated.")
    else:
        print("Keep going -- fill in the remaining TODOs and re-run this file.")


if __name__ == "__main__":
    main()
