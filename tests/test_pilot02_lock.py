#!/usr/bin/env python3

from __future__ import annotations

import copy
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LOCK = ROOT / "pilot-02/protocol-lock/v0.2/pilot02_endpoint_lock.json"
VERIFY = ROOT / "tools/verify_pilot02_lock.py"

spec = importlib.util.spec_from_file_location("verify_pilot02_lock", VERIFY)
module = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(module)


class Pilot02EndpointLockTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.base = json.loads(LOCK.read_text(encoding="utf-8"))

    def assert_rejected(self, mutate) -> None:
        candidate = copy.deepcopy(self.base)
        mutate(candidate)
        self.assertTrue(module.validate_semantics(candidate))

    def test_authoritative_lock_passes(self) -> None:
        self.assertEqual(module.validate_semantics(copy.deepcopy(self.base)), [])

    def test_reject_raw_tokens_as_sole_primary(self) -> None:
        self.assert_rejected(lambda d: d["research_object"].update(not_primary_alone=["DECISION_ACCURACY"]))

    def test_reject_decision_accuracy_as_sole_primary(self) -> None:
        self.assert_rejected(lambda d: d["research_object"].update(not_primary_alone=["RAW_TOKEN_REDUCTION"]))

    def test_reject_compensatory_quality_gate(self) -> None:
        self.assert_rejected(lambda d: d["study_level_primary"]["gates"][0].update(compensation_allowed=True))

    def test_reject_missing_resource_gate(self) -> None:
        self.assert_rejected(lambda d: d["study_level_primary"].update(gates=d["study_level_primary"]["gates"][:1]))

    def test_reject_bounded_nl_ground_truth_upgrade(self) -> None:
        self.assert_rejected(lambda d: d["tracks"]["bounded_natural_language"].update(decision_labels_are_independent_ground_truth=True))

    def test_reject_verifiable_oracle_removal(self) -> None:
        self.assert_rejected(lambda d: d["tracks"]["verifiable_output"].update(oracle_contract_required=False))

    def test_reject_test_pass_as_universal_oracle(self) -> None:
        self.assert_rejected(lambda d: d["tracks"]["verifiable_output"].update(test_pass_alone_is_universal_oracle=True))

    def test_reject_action_scope_expansion(self) -> None:
        self.assert_rejected(lambda d: d["primary_action_lane"].append("ROUTE"))

    def test_reject_direct_substitute_removal(self) -> None:
        self.assert_rejected(lambda d: d["h5_incremental_value"].update(arms=d["h5_incremental_value"]["arms"][:3]))

    def test_reject_dev_as_performance_evidence(self) -> None:
        self.assert_rejected(lambda d: d["calibration_and_freeze"].update(dev_30_may_establish_performance=True))

    def test_reject_locked_corpus_tuning(self) -> None:
        self.assert_rejected(lambda d: d["calibration_and_freeze"].update(post_open_endpoint_or_threshold_changes_allowed=True))

    def test_reject_in_place_edit_permission(self) -> None:
        self.assert_rejected(lambda d: d["change_control"].update(v0_2_edit_in_place_allowed=True))

    def test_reject_silent_change_permission(self) -> None:
        self.assert_rejected(lambda d: d["change_control"].update(silent_change_allowed=True))

    def test_manifest_detects_tampered_locked_file(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_root = Path(tmp)
            for rel in [module.LOCK_REL, module.MANIFEST_REL]:
                target = tmp_root / rel
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes((ROOT / rel).read_bytes())
            lock_path = tmp_root / module.LOCK_REL
            lock_path.write_text(lock_path.read_text(encoding="utf-8") + "\n", encoding="utf-8")
            errors = module.validate_manifest(tmp_root)
            self.assertTrue(any("hash mismatch" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
