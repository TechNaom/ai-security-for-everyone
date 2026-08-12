"""
Chapter 8 Project: A Provenance and Integrity Checker

Build a real, self-contained supply-chain defense tool: a checker that
vets a synthetic set of model/dependency artifacts against an expected
manifest (Defense 1, provenance verification), flags any artifact using
an unsafe serialization format (Defense 2, safe loading), and confirms
each artifact's publisher is on a vetted-source list -- producing a real,
structured vetting report, including the honest, directly observable
limit named in the lesson's own defenses: passing every mechanical check
this tool can perform does not prove an artifact's actual learned
behavior is safe.

-----------------------------------------------------------------------
YOUR TASK
-----------------------------------------------------------------------
Fill in the TODOs below:

  PART 1 -- checksum_matches(): confirm an artifact's as-found checksum
            matches the value independently recorded in the manifest at
            approval time.
  PART 2 -- format_is_safe(): confirm an artifact's serialization format
            is on the safe list (not a pickle-based format capable of
            arbitrary code execution on load).
  PART 3 -- publisher_is_vetted(): confirm an artifact's publisher is on
            the organization's vetted-source list.
  PART 4 -- vet_artifact(): combine the three checks above (plus a
            scan-clean flag already provided in the artifact record) into
            one finding list and a BLOCK/APPROVE verdict.

Then run this file:

    python3 starter.py

-----------------------------------------------------------------------
THE SCENARIO: Solstice Diagnostics / TriageAssist (continuing the lesson)
-----------------------------------------------------------------------
TriageAssist is Solstice's symptom-triage assistant (see lesson.html).
This project builds the tool Solstice's security review should have run
BEFORE any of its three under-deadline decisions reached production: a
provenance and integrity checker that vets every model, adapter, and
dependency artifact against a manifest before it's trusted.

-----------------------------------------------------------------------
NO LIVE MODEL DEPENDENCY -- READ THIS BEFORE RUNNING
-----------------------------------------------------------------------
Like Chapters 6 and 7, this chapter is conceptual/architectural by
nature -- provenance verification and integrity checking are
adoption-time, offline practices, not runtime model interactions. Every
function in this file is pure, deterministic Python operating on
fabricated, clearly-labeled synthetic artifact records, with zero
network dependency and zero live-model call anywhere in this file. There
is nothing to gracefully degrade -- this script always runs the same
way, every time, with or without Ollama reachable.

Run it:

    python3 starter.py
"""

# ---------------------------------------------------------------------------
# Serialization formats considered structurally safe (cannot execute code
# on load) versus unsafe (can execute arbitrary code on load, by design).
# ---------------------------------------------------------------------------

SAFE_FORMATS = {"safetensors", "onnx", "json-weights"}
UNSAFE_FORMATS = {"pickle", "pt-pickle", "dill", "joblib-pickle"}


# ---------------------------------------------------------------------------
# PART 1 -- Confirm an artifact's as-found checksum matches the value
# independently recorded in the manifest at approval time. A mismatch
# means the file has changed since it was last vetted -- tampering, or an
# unreviewed silent update, either way a real finding.
# ---------------------------------------------------------------------------


def checksum_matches(artifact, manifest_entry):
    """
    artifact: dict with an "checksum" key (the as-found value).
    manifest_entry: dict with an "expected_checksum" key (the value
        independently recorded when this artifact was last approved).

    Returns True if they match exactly, False otherwise.
    """
    # TODO: return artifact["checksum"] == manifest_entry["expected_checksum"]
    return False


# ---------------------------------------------------------------------------
# PART 2 -- Confirm an artifact's serialization format is on the safe
# list, not a pickle-based (or similar) format capable of arbitrary code
# execution on load.
# ---------------------------------------------------------------------------


def format_is_safe(artifact):
    """
    artifact: dict with a "format" key.

    Returns True if artifact["format"] is in SAFE_FORMATS, False
    otherwise (including formats not in either set -- unrecognized
    formats are treated as NOT safe, the conservative default).
    """
    # TODO: return artifact["format"] in SAFE_FORMATS
    return False


# ---------------------------------------------------------------------------
# PART 3 -- Confirm an artifact's publisher is on the organization's
# vetted-source list.
# ---------------------------------------------------------------------------


def publisher_is_vetted(artifact, vetted_publishers):
    """
    artifact: dict with a "publisher" key.
    vetted_publishers: a set/list of publisher names the organization has
        independently vetted and trusts.

    Returns True if artifact["publisher"] is in vetted_publishers.
    """
    # TODO: return artifact["publisher"] in vetted_publishers
    return False


# ---------------------------------------------------------------------------
# PART 4 -- Combine PART 1-3's checks, plus the artifact's own
# "scan_clean" flag (already provided in each artifact record -- a
# stand-in for a dependency/malware scan result), into one finding list
# and a BLOCK/APPROVE verdict. ANY finding blocks the artifact -- this
# tool is deliberately conservative, matching the lesson's own framing of
# these as a gate, not a suggestion.
# ---------------------------------------------------------------------------


def vet_artifact(artifact, manifest_entry, vetted_publishers):
    """
    Returns a dict:
        {
            "artifact_id": artifact["id"],
            "findings": [...],   # list of finding strings, empty if none
            "verdict": "APPROVE" or "BLOCK",
        }

    Possible finding strings (use exactly these):
        "CHECKSUM_MISMATCH"        -- checksum_matches() is False
        "UNSAFE_SERIALIZATION_FORMAT" -- format_is_safe() is False
        "UNVETTED_PUBLISHER"       -- publisher_is_vetted() is False
        "SCAN_FLAGGED"             -- artifact["scan_clean"] is False

    verdict is "BLOCK" if findings is non-empty, "APPROVE" otherwise.
    """
    # TODO:
    #   findings = []
    #   if not checksum_matches(artifact, manifest_entry):
    #       findings.append("CHECKSUM_MISMATCH")
    #   if not format_is_safe(artifact):
    #       findings.append("UNSAFE_SERIALIZATION_FORMAT")
    #   if not publisher_is_vetted(artifact, vetted_publishers):
    #       findings.append("UNVETTED_PUBLISHER")
    #   if not artifact.get("scan_clean", False):
    #       findings.append("SCAN_FLAGGED")
    #   verdict = "BLOCK" if findings else "APPROVE"
    #   return {"artifact_id": artifact["id"], "findings": findings, "verdict": verdict}
    return {"artifact_id": artifact.get("id", "unknown"), "findings": ["NOT_IMPLEMENTED"], "verdict": "BLOCK"}


# ---------------------------------------------------------------------------
# The synthetic manifest and as-found artifact set: modeled directly on
# Solstice Diagnostics' TriageAssist scenario. All entirely fabricated for
# this exercise. Provided for you -- no TODOs below this line until
# verify_logic() and main().
# ---------------------------------------------------------------------------

VETTED_PUBLISHERS = {"solstice-internal-ml", "cortexlabs-verified", "openmed-foundation"}

MANIFEST = {
    "base_model_v3": {"expected_checksum": "a1b2c3d4e5"},
    "triage_adapter_v1": {"expected_checksum": "f6a7b8c9d0"},
    "embedding_model_v2": {"expected_checksum": "11aa22bb33"},
    "framework_lib_core": {"expected_checksum": "cc44dd55ee"},
    "drug_interaction_client": {"expected_checksum": "ff66gg77hh"},
}


def build_synthetic_artifacts():
    """
    Six fabricated artifacts, one per row, spanning: a fully clean
    artifact; a tampered checksum; an unsafe serialization format; an
    unvetted publisher; a scan-flagged dependency; and one artifact that
    passes every single mechanical check this tool can perform -- the
    honest hard case Step C highlights.
    """
    return [
        {
            "id": "base_model_v3",
            "narrative": "Solstice's own internally-trained base model, fully vetted",
            "checksum": "a1b2c3d4e5",
            "format": "safetensors",
            "publisher": "solstice-internal-ml",
            "scan_clean": True,
        },
        {
            "id": "triage_adapter_v1",
            "narrative": "The community adapter from the lesson's hook -- checksum has drifted from what was recorded at approval time",
            "checksum": "TAMPERED99",
            "format": "safetensors",
            "publisher": "cortexlabs-verified",
            "scan_clean": True,
        },
        {
            "id": "embedding_model_v2",
            "narrative": "An embedding model shipped in a pickle-based format with no safe alternative recorded",
            "checksum": "11aa22bb33",
            "format": "pickle",
            "publisher": "openmed-foundation",
            "scan_clean": True,
        },
        {
            "id": "framework_lib_core",
            "narrative": "A core ML framework library from a publisher never added to the vetted-source list",
            "checksum": "cc44dd55ee",
            "format": "safetensors",
            "publisher": "unlisted-third-party",
            "scan_clean": True,
        },
        {
            "id": "drug_interaction_client",
            "narrative": "The third-party tool client library from the lesson's hook -- a dependency scan flagged a known vulnerability",
            "checksum": "ff66gg77hh",
            "format": "safetensors",
            "publisher": "cortexlabs-verified",
            "scan_clean": False,
        },
        {
            "id": "quiet_backdoor_candidate",
            "narrative": "Passes every mechanical check this tool can perform -- checksum matches, safe format, vetted publisher, clean scan. This tool cannot tell you whether its actual learned weights are safe.",
            "checksum": "PASSES0000",
            "format": "safetensors",
            "publisher": "solstice-internal-ml",
            "scan_clean": True,
        },
    ]


MANIFEST["quiet_backdoor_candidate"] = {"expected_checksum": "PASSES0000"}


# ---------------------------------------------------------------------------
# Pure-logic self-test: verifies PART 1-4's logic against small, synthetic,
# clearly-labeled example cases -- NOT the full artifact set above. Always
# runs, no dependency of any kind.
# ---------------------------------------------------------------------------


def verify_logic():
    passed = 0
    total = 0

    total += 1
    ok = checksum_matches({"checksum": "abc"}, {"expected_checksum": "abc"}) is True
    passed += int(ok)
    print(f"  [{'OK' if ok else 'MISMATCH'}] checksum_matches, exact match: expected True")

    total += 1
    ok = checksum_matches({"checksum": "abc"}, {"expected_checksum": "xyz"}) is False
    passed += int(ok)
    print(f"  [{'OK' if ok else 'MISMATCH'}] checksum_matches, mismatch: expected False")

    total += 1
    ok = format_is_safe({"format": "safetensors"}) is True
    passed += int(ok)
    print(f"  [{'OK' if ok else 'MISMATCH'}] format_is_safe, safetensors: expected True")

    total += 1
    ok = format_is_safe({"format": "pickle"}) is False
    passed += int(ok)
    print(f"  [{'OK' if ok else 'MISMATCH'}] format_is_safe, pickle: expected False")

    total += 1
    ok = format_is_safe({"format": "some-unknown-format"}) is False
    passed += int(ok)
    print(f"  [{'OK' if ok else 'MISMATCH'}] format_is_safe, unrecognized format: expected False (conservative default)")

    total += 1
    ok = publisher_is_vetted({"publisher": "solstice-internal-ml"}, VETTED_PUBLISHERS) is True
    passed += int(ok)
    print(f"  [{'OK' if ok else 'MISMATCH'}] publisher_is_vetted, vetted: expected True")

    total += 1
    ok = publisher_is_vetted({"publisher": "random-anon-account"}, VETTED_PUBLISHERS) is False
    passed += int(ok)
    print(f"  [{'OK' if ok else 'MISMATCH'}] publisher_is_vetted, unvetted: expected False")

    total += 1
    clean = {"id": "x", "checksum": "abc", "format": "safetensors",
              "publisher": "solstice-internal-ml", "scan_clean": True}
    result = vet_artifact(clean, {"expected_checksum": "abc"}, VETTED_PUBLISHERS)
    ok = result["verdict"] == "APPROVE" and result["findings"] == []
    passed += int(ok)
    print(f"  [{'OK' if ok else 'MISMATCH'}] vet_artifact, fully clean: expected APPROVE with no findings, got {result}")

    total += 1
    dirty = {"id": "y", "checksum": "TAMPERED", "format": "pickle",
             "publisher": "random-anon-account", "scan_clean": False}
    result2 = vet_artifact(dirty, {"expected_checksum": "abc"}, VETTED_PUBLISHERS)
    ok = (result2["verdict"] == "BLOCK"
          and set(result2["findings"]) == {"CHECKSUM_MISMATCH", "UNSAFE_SERIALIZATION_FORMAT",
                                            "UNVETTED_PUBLISHER", "SCAN_FLAGGED"})
    passed += int(ok)
    print(f"  [{'OK' if ok else 'MISMATCH'}] vet_artifact, fails every check: expected BLOCK with all 4 findings, got {result2}")

    print(f"  Logic self-test: {passed}/{total} passed")
    return passed == total


# ---------------------------------------------------------------------------
# Main report: vets all six synthetic artifacts and prints a real
# structured report, including the honest gap named in the lesson's own
# defenses, made directly observable here.
# ---------------------------------------------------------------------------


def main():
    print("Chapter 8 Project -- Provenance and Integrity Checker (Solstice Diagnostics / TriageAssist)")
    print("=" * 92)
    print("\nStep A: verify the checker's own logic against small synthetic cases")
    logic_ok = verify_logic()
    if not logic_ok:
        print("\nOne or more checks disagree with the synthetic self-test above -- "
              "fix the logic before trusting the full-artifact-set report below.")

    print("\nStep B: vet all six synthetic artifacts against the manifest")
    artifacts = build_synthetic_artifacts()
    results = []
    for art in artifacts:
        manifest_entry = MANIFEST.get(art["id"], {"expected_checksum": None})
        result = vet_artifact(art, manifest_entry, VETTED_PUBLISHERS)
        result["narrative"] = art["narrative"]
        results.append(result)

    header = f"{'artifact_id':<28}{'verdict':>10}   findings"
    print("  " + header)
    print("  " + "-" * 90)
    for r in results:
        findings_str = ", ".join(r["findings"]) if r["findings"] else "(none)"
        print(f"  {r['artifact_id']:<28}{r['verdict']:>10}   {findings_str}")
        print(f"      {r['narrative']}")

    blocked = sum(1 for r in results if r["verdict"] == "BLOCK")
    approved = sum(1 for r in results if r["verdict"] == "APPROVE")
    print(f"\n  Summary: {approved} approved, {blocked} blocked out of {len(results)} artifacts vetted.")

    print("\nStep C: the honest gap this report cannot close on its own")
    by_id = {r["artifact_id"]: r for r in results}
    quiet = by_id.get("quiet_backdoor_candidate")
    if quiet:
        print(
            f"  quiet_backdoor_candidate: verdict={quiet['verdict']}, findings={quiet['findings'] or '(none)'}\n"
            f"\n  This artifact passes every single mechanical check this tool can perform: "
            f"its checksum matches the manifest, its format is on the safe list, its publisher "
            f"is vetted, and its scan came back clean. An APPROVE verdict here is a real, useful "
            f"gate result -- and it is honestly NOT proof that this artifact's actual learned "
            f"weights are free of a well-disguised backdoor. A checksum only proves the file "
            f"matches what was recorded at approval time; it says nothing about whether what was "
            f"recorded at approval time was itself safe. This tool implements Defenses 1-3 "
            f"exactly as far as they honestly go -- it cannot, and does not claim to, replace "
            f"the judgment, behavior auditing, and organizational process (Chapter 6's Defense 3 "
            f"and this chapter's own Defense 4) that a complete posture still requires."
        )


if __name__ == "__main__":
    main()
