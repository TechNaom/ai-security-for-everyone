"""
Chapter 10 Practice Bank: Securing Agentic Systems Against Adversarial Tool Output

Eight short, independent scenarios, each with its own fictional system --
none of them Ferngate Logistics (the lesson) or Talbridge Health Network
(the exercises). See practice/README.md for full scenario text. Fill in
every TODO below, then run:

    python3 starter.py

to see your score. Compare against solution.py for reference answers.
"""

MOMENTS = {
    "result_arrival": "Result-arrival risk",
    "context_assembly": "Context-assembly risk",
    "action_proposal": "Action-proposal risk",
}

DEFENSES = {
    "schema_validation": "Schema and type validation of tool results",
    "content_sanitization": "Content sanitization of tool-result free text",
    "structural_separation": "Structural separation and reinforced framing of tool results",
    "provenance_tagging": "Field-level provenance tagging",
    "permission_scoping": "Permission and capability scoping per tool call",
    "human_in_loop_backstop": "Human-in-the-loop confirmation and a hard least-privilege backstop",
}

# Scenario 1 -- Pemberton Insurance Group: a claims-triage agent's
# claims-lookup tool returns a JSON response mixing a structured, system-
# set "claim_status" enum with a free-text "adjuster_note" field an
# external contracted adjuster submitted, containing a planted
# instruction, with nothing distinguishing the two fields by the time the
# response reaches the model. TODO: which moment?
scenario_1_moment = ""  # TODO -- use a MOMENTS key

# Scenario 2 -- Kestrel Robotics: a fleet-dispatch agent's tool-call
# result is correctly placed inside a proper tool-role message, but
# nothing in the message content itself reinforces that the field is
# data, not an instruction, and a persuasive sentence inside it still
# reads to the model like a directive. TODO: which moment?
scenario_2_moment = ""  # TODO -- use a MOMENTS key

# Scenario 3 -- Fairhaven School District: after reading a tool result
# from an attendance-tracking API, an agent proposes waiving a required
# parent-notification step for an unexcused absence, unprompted, based
# solely on wording found in that tool's returned free-text field.
# TODO: which moment?
scenario_3_moment = ""  # TODO -- use a MOMENTS key

# Scenario 4 -- Journeywell Travel: the credential behind a booking
# agent's read-only cancel_status_lookup tool can also authorize a card
# charge, even though the tool itself only ever exposes a status check.
# TODO: which single defense would have stopped this specific failure
# most directly?
scenario_4_defense = ""  # TODO -- use a DEFENSES key

# Scenario 5 -- Brightloom Retail: every field in a retail-support agent's
# tool responses is tagged at result-arrival time with whether it's
# system-generated or vendor-submitted, queryable by every later stage of
# the round trip. TODO: which single defense is this?
scenario_5_defense = ""  # TODO -- use a DEFENSES key

# Scenario 6 (judgment) -- Oakstead Manufacturing's engineering team says:
# "We schema-validate every tool response, so no malicious content can
# ever reach our model through a tool call." Is this conclusion sound?
scenario_6_claim_sound = None  # TODO -- True or False

# Scenario 7 (judgment) -- Silverline Broadcasting scoped every tool
# call's credentials to the narrowest permission the tool needs, and
# concludes: "Since credentials are properly scoped, a manipulated tool
# result can never cause real harm." Is this conclusion sound?
scenario_7_claim_sound = None  # TODO -- True or False

# Scenario 8 (judgment, production-gear) -- Cascade Ridge Outfitters is
# three weeks from launching a new support agent with two tool calls.
# Right now: (a) there is zero content sanitization on tool-result free
# text, AND (b) tool results are concatenated into the prompt with no
# structural framing at all. The team has also decided not to build
# field-level provenance tagging before launch, documenting that gap as
# accepted residual risk to revisit post-launch. Given limited time
# before launch, which single fix -- sanitizing tool-result free text and
# adding structural framing (use "sanitization_and_framing"), or building
# field-level provenance tagging (use "provenance_tagging") -- has the
# higher expected impact? And separately, which defense category is the
# one being explicitly accepted as residual risk for now (use a DEFENSES
# key)?
scenario_8_priority = ""  # TODO
scenario_8_gap_named = ""  # TODO -- use a DEFENSES key


# ===========================================================================
# Scoring harness -- do not need to edit anything below this line.
# ===========================================================================

def score_scenario_1():
    return (1 if scenario_1_moment == "result_arrival" else 0), 1


def score_scenario_2():
    return (1 if scenario_2_moment == "context_assembly" else 0), 1


def score_scenario_3():
    return (1 if scenario_3_moment == "action_proposal" else 0), 1


def score_scenario_4():
    return (1 if scenario_4_defense == "permission_scoping" else 0), 1


def score_scenario_5():
    return (1 if scenario_5_defense == "provenance_tagging" else 0), 1


def score_scenario_6():
    return (1 if scenario_6_claim_sound is False else 0), 1


def score_scenario_7():
    return (1 if scenario_7_claim_sound is False else 0), 1


def score_scenario_8():
    correct = 0
    if scenario_8_priority.strip().lower() == "sanitization_and_framing":
        correct += 1
    if scenario_8_gap_named == "provenance_tagging":
        correct += 1
    return correct, 2


def main():
    scenarios = [
        ("Scenario 1 -- Pemberton Insurance Group", score_scenario_1),
        ("Scenario 2 -- Kestrel Robotics", score_scenario_2),
        ("Scenario 3 -- Fairhaven School District", score_scenario_3),
        ("Scenario 4 -- Journeywell Travel", score_scenario_4),
        ("Scenario 5 -- Brightloom Retail", score_scenario_5),
        ("Scenario 6 -- Oakstead Manufacturing (judgment)", score_scenario_6),
        ("Scenario 7 -- Silverline Broadcasting (judgment)", score_scenario_7),
        ("Scenario 8 -- Cascade Ridge Outfitters (prioritization)", score_scenario_8),
    ]

    total_correct = 0
    total_possible = 0
    print("Chapter 10 Practice Bank -- Score Report")
    print("=" * 60)
    for label, fn in scenarios:
        correct, possible = fn()
        total_correct += correct
        total_possible += possible
        print(f"{label}: {correct}/{possible}")
    print("=" * 60)
    print(f"TOTAL: {total_correct}/{total_possible}")
    if total_possible and total_correct == total_possible:
        print("Perfect score -- fast, accurate judgment across all eight scenarios.")
    else:
        print("Keep going -- fill in the remaining TODOs and re-run this file.")


if __name__ == "__main__":
    main()
