#!/usr/bin/env python3
"""Verify Pilot 02 v0.2 integrity and semantic invariants."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any


LOCK_REL = Path("pilot-02/protocol-lock/v0.2/pilot02_endpoint_lock.json")
MANIFEST_REL = Path("pilot-02/protocol-lock/v0.2/LOCK_MANIFEST.json")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def validate_semantics(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []

    _require(data.get("lock_id") == "pilot02-endpoint-v0.2", "lock_id drift", errors)
    _require(data.get("status") == "FROZEN_FOR_DEV_30", "status drift", errors)

    object_ = data.get("research_object", {})
    _require(
        object_.get("not_primary_alone") == ["RAW_TOKEN_REDUCTION", "DECISION_ACCURACY"],
        "sole-primary exclusions drift",
        errors,
    )

    primary = data.get("study_level_primary", {})
    _require(primary.get("type") == "ORDERED_NONCOMPENSATORY_GATES", "primary type drift", errors)
    gates = primary.get("gates", [])
    _require(len(gates) == 2, "primary gate count drift", errors)
    if len(gates) == 2:
        _require(gates[0].get("id") == "QUALITY_AND_SAFETY_NONINFERIORITY", "gate 1 drift", errors)
        _require(gates[1].get("id") == "RESOURCE_AND_ECONOMIC_BENEFIT", "gate 2 drift", errors)
        _require(gates[0].get("compensation_allowed") is False, "gate 1 became compensatory", errors)
        _require(gates[1].get("compensation_allowed") is False, "gate 2 became compensatory", errors)
    _require(primary.get("positive_result_requires_all_gates") is True, "positive-result gate drift", errors)

    tracks = data.get("tracks", {})
    verifiable = tracks.get("verifiable_output", {})
    bounded = tracks.get("bounded_natural_language", {})
    _require(
        verifiable.get("decision_endpoint_role") == "CO_PRIMARY_WITH_STUDY_LEVEL_JOINT_OUTCOME",
        "verifiable decision endpoint drift",
        errors,
    )
    _require(verifiable.get("oracle_contract_required") is True, "verifiable oracle requirement removed", errors)
    expected_oracle = {
        "FROZEN_REQUIREMENT_MAP",
        "EXECUTABLE_VERIFIER",
        "FROZEN_COMPLETION_OBLIGATIONS",
        "ACCEPTABLE_STOP_INTERVAL",
        "FROZEN_CHECKPOINT_SCHEDULE",
        "ACTION_ORACLE",
        "FAILURE_SEVERITY_MAP",
    }
    _require(set(verifiable.get("oracle_contract", [])) == expected_oracle, "verifiable oracle contract drift", errors)
    _require(verifiable.get("test_pass_alone_is_universal_oracle") is False, "test-pass overclaim introduced", errors)
    _require(
        bounded.get("decision_endpoint_role") == "CONFIRMATORY_SECONDARY_MECHANISM_METRIC",
        "bounded-NL decision endpoint drift",
        errors,
    )
    _require(
        bounded.get("decision_labels_are_independent_ground_truth") is False,
        "bounded-NL labels upgraded to independent ground truth",
        errors,
    )

    _require(
        data.get("primary_action_lane") == ["CONTINUE", "STOP", "ABSTAIN"],
        "primary action lane drift",
        errors,
    )
    _require(
        data.get("separate_action_modules") == ["REGENERATE", "ROUTE", "ESCALATE"],
        "separate action modules drift",
        errors,
    )

    h5 = data.get("h5_incremental_value", {})
    _require(
        h5.get("arms")
        == [
            "A_SIMPLE_HEURISTIC",
            "B_REVAS_WITHOUT_NEOMUNDI",
            "C_REVAS_WITH_NEOMUNDI",
            "D_REVAS_WITH_DIRECT_SUBSTITUTE",
        ],
        "H5 arm structure drift",
        errors,
    )
    _require(
        set(h5.get("incremental_value_requires", []))
        == {
            "IMPROVEMENT_OVER_B_REVAS_WITHOUT_NEOMUNDI",
            "IMPROVEMENT_OVER_D_DIRECT_SUBSTITUTE",
            "ADDED_LATENCY_AND_COST_INCLUDED",
        },
        "H5 adoption rule drift",
        errors,
    )

    freeze = data.get("calibration_and_freeze", {})
    _require(freeze.get("dev_30_role") == "CALIBRATION_ONLY", "DEV-30 role drift", errors)
    _require(freeze.get("dev_30_may_establish_performance") is False, "DEV-30 performance leakage", errors)
    _require(freeze.get("calibration_source") == "DEV_30_ONLY", "calibration source drift", errors)
    _require(freeze.get("locked_corpus_role") == "EVALUATION_ONLY", "locked corpus role drift", errors)
    _require(
        freeze.get("locked_corpus_must_remain_unopened_until_full_freeze") is True,
        "locked corpus opening gate removed",
        errors,
    )
    _require(
        freeze.get("post_open_endpoint_or_threshold_changes_allowed") is False,
        "post-open tuning enabled",
        errors,
    )

    prohibited = set(data.get("prohibited_drift", []))
    expected_prohibited = {
        "RAW_TOKEN_REDUCTION_AS_SOLE_PRIMARY",
        "DECISION_ACCURACY_AS_SOLE_PRIMARY",
        "BOUNDED_NL_LABELS_PRESENTED_AS_UNIVERSAL_GROUND_TRUTH",
        "POSITIVE_RESULT_WHEN_QUALITY_OR_SAFETY_FAILS",
        "POSITIVE_RESULT_WHEN_NET_COST_INCREASES",
        "REASONING_TOKEN_SCALING_USED_AS_VISIBLE_CONTINUATION_ORACLE",
        "ENDPOINT_ONTOLOGY_CHANGE_AFTER_LOCKED_CORPUS_ACCESS",
        "SILENT_IN_PLACE_EDIT_OF_V0_2",
    }
    _require(prohibited == expected_prohibited, "prohibited-drift set changed", errors)

    control = data.get("change_control", {})
    _require(control.get("v0_2_edit_in_place_allowed") is False, "in-place v0.2 edits enabled", errors)
    _require(control.get("silent_change_allowed") is False, "silent change enabled", errors)

    return errors


def validate_manifest(root: Path) -> list[str]:
    errors: list[str] = []
    manifest_path = root / MANIFEST_REL
    if not manifest_path.exists():
        return [f"missing manifest: {MANIFEST_REL}"]
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    for rel, expected in manifest.get("sha256", {}).items():
        path = root / rel
        if not path.exists():
            errors.append(f"missing locked file: {rel}")
            continue
        actual = sha256_file(path)
        if actual != expected:
            errors.append(f"hash mismatch: {rel}: expected {expected}, got {actual}")
    return errors


def repository_root() -> Path:
    return Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=repository_root())
    parser.add_argument("--semantic-only", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    lock_path = root / LOCK_REL
    if not lock_path.exists():
        print(f"FAIL: missing lock: {lock_path}", file=sys.stderr)
        return 1

    data = json.loads(lock_path.read_text(encoding="utf-8"))
    errors = validate_semantics(data)
    if not args.semantic_only:
        errors.extend(validate_manifest(root))

    if errors:
        print("PILOT02_V0_2_LOCK_FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PILOT02_V0_2_LOCK_OK")
    print(f"lock_id={data['lock_id']}")
    print(f"lock_sha256={sha256_file(lock_path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
