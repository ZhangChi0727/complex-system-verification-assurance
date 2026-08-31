from __future__ import annotations

import copy
import importlib.util
import json
import tempfile
import unittest
from unittest import mock
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "repository_integrity", ROOT / "scripts/check_repository_integrity.py"
)
assert SPEC and SPEC.loader
integrity = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(integrity)


class RepositoryGovernanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.status = integrity.load_status()
        cls.readme = integrity.read("README.md")
        cls.registry = integrity.read("docs/08_validation/instance_registry.md")
        cls.contract = integrity.read("docs/08_validation/cross_repository_instance_contract.md")
        cls.validation = integrity.read("docs/08_validation/README.md")

    def test_json_readme_drift_is_rejected(self) -> None:
        changed = copy.deepcopy(self.status)
        changed["development"]["currentStop"]["objective"] += " changed"
        self.assertNotEqual(
            integrity.sync.replace_status_block(self.readme, changed), self.readme
        )

    def test_pull_request_missing_readme_is_rejected(self) -> None:
        required = set(self.status["governance"]["requiredPullRequestFiles"])
        changed = required - {"README.md"}
        self.assertTrue(integrity.pr_required_file_errors(changed, "pull_request", self.status))

    def test_pull_request_missing_project_status_is_rejected(self) -> None:
        required = set(self.status["governance"]["requiredPullRequestFiles"])
        changed = required - {"project-status.json"}
        self.assertTrue(integrity.pr_required_file_errors(changed, "pull_request", self.status))

    def test_push_does_not_require_both_pr_files(self) -> None:
        self.assertEqual(integrity.pr_required_file_errors(set(), "push", self.status), [])

    def test_mutable_branch_cannot_replace_method_identity(self) -> None:
        identity = self.status["identities"]["methodDefinition"]["commit"]
        changed = self.registry.replace(identity, "ma" + "in")
        errors = integrity.final_state_document_errors(
            changed, self.contract, self.validation, self.status
        )
        self.assertTrue(errors)

    def test_method_definition_and_disposition_cannot_be_swapped(self) -> None:
        changed = copy.deepcopy(self.status)
        method = changed["identities"]["methodDefinition"]["commit"]
        disposition = changed["identities"]["methodCompatibilityDisposition"]["commit"]
        changed["identities"]["methodDefinition"]["commit"] = disposition
        changed["identities"]["methodCompatibilityDisposition"]["commit"] = method
        errors = integrity.final_state_document_errors(
            self.registry, self.contract, self.validation, changed
        )
        self.assertTrue(errors)

    def test_assessed_and_acknowledgement_releases_cannot_be_swapped(self) -> None:
        assessed = self.status["crossRepository"]["arinc615a"]["assessedSource"]["releaseTag"]
        acknowledged = self.status["crossRepository"]["arinc615a"]["acknowledgementRelease"]["releaseTag"]
        changed = self.registry.replace(assessed, "__ASSESSED__", 1)
        changed = changed.replace(acknowledged, assessed, 1).replace("__ASSESSED__", acknowledged, 1)
        errors = integrity.final_state_document_errors(
            changed, self.contract, self.validation, self.status
        )
        self.assertTrue(errors)

    def test_incorrect_acknowledgement_tag_object_is_rejected(self) -> None:
        value = self.status["crossRepository"]["arinc615a"]["acknowledgementRelease"]["tagObject"]
        changed = self.registry.replace(value, "0" * 40, 1)
        self.assertTrue(integrity.final_state_document_errors(
            changed, self.contract, self.validation, self.status
        ))

    def test_incorrect_acknowledgement_peeled_target_is_rejected(self) -> None:
        value = self.status["crossRepository"]["arinc615a"]["acknowledgementRelease"]["peeledTarget"]
        changed = self.contract.replace(value, "1" * 40, 1)
        self.assertTrue(integrity.final_state_document_errors(
            self.registry, changed, self.validation, self.status
        ))

    def test_completed_handshake_cannot_report_acknowledgement_pending(self) -> None:
        pending = self.validation + "\nWork order B remains prohibited."
        errors = integrity.final_state_document_errors(
            self.registry, self.contract, pending, self.status
        )
        self.assertTrue(errors)

    def test_fulfilled_temporary_control_is_rejected(self) -> None:
        changed = copy.deepcopy(self.status)
        changed["temporaryControls"] = [{
            "id": "TMP-GATE",
            "status": "ACTIVE",
            "owner": "research",
            "introducedBy": "governance-change",
            "retireWhen": {
                "path": "crossRepository.arinc615a.thirdHandshake",
                "equals": changed["crossRepository"]["arinc615a"]["thirdHandshake"],
            },
        }]
        self.assertTrue(integrity.sync.temporary_control_errors(changed, ROOT))

    def test_lifecycle_literals_in_validator_are_rejected(self) -> None:
        identity = self.status["identities"]["methodDefinition"]["commit"]
        tag = self.status["crossRepository"]["arinc615a"]["acknowledgementRelease"]["releaseTag"]
        pr_text = "PR " + "#99"
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "validator.py"
            path.write_text(f"COMMIT='{identity}'\nTAG='{tag}'\nLABEL='{pr_text}'\n", encoding="utf-8")
            errors = integrity.lifecycle_literal_errors([path], self.status)
        self.assertGreaterEqual(len(errors), 3)

    def test_mutable_branch_identity_forms_are_rejected(self) -> None:
        candidates = (
            "refs/heads/" + "ma" + "in",
            "origin/" + "ma" + "in",
            "METHOD_IDENTITY = " + repr("latest"),
        )
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "validator.py"
            for candidate in candidates:
                with self.subTest(candidate=candidate):
                    path.write_text(candidate + "\n", encoding="utf-8")
                    errors = integrity.lifecycle_literal_errors([path], self.status)
                    self.assertTrue(any("mutable branch" in error for error in errors))

    def test_production_scan_discovers_sync_and_governance_tests(self) -> None:
        discovered = {path.relative_to(ROOT).as_posix() for path in integrity.governance_code_paths()}
        self.assertIn("scripts/check_repository_integrity.py", discovered)
        self.assertIn("scripts/sync_project_overview.py", discovered)
        self.assertIn("tests/test_repository_integrity.py", discovered)

    def _repository_errors_with_sync_suffix(self, suffix: str) -> list[str]:
        sync_path = (ROOT / "scripts/sync_project_overview.py").resolve()
        original = Path.read_text

        def injected(path: Path, *args: object, **kwargs: object) -> str:
            text = original(path, *args, **kwargs)
            return text + suffix if path.resolve() == sync_path else text

        with mock.patch.object(Path, "read_text", new=injected):
            return integrity.repository_errors(self.status)

    def test_repository_errors_rejects_sha_in_sync_production_path(self) -> None:
        identity = self.status["identities"]["methodDefinition"]["commit"]
        errors = self._repository_errors_with_sync_suffix(f"\nEMBEDDED_ID = '{identity}'\n")
        self.assertTrue(any("lifecycle SHA literal" in error for error in errors))

    def test_repository_errors_rejects_mutable_branch_in_sync_production_path(self) -> None:
        assignment = "DEFAULT_" + "BRANCH = " + repr("ma" + "in")
        errors = self._repository_errors_with_sync_suffix(f"\n{assignment}\n")
        self.assertTrue(any("mutable branch" in error for error in errors))

    def test_active_handoff_link_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "HANDOFF").mkdir()
            (root / "active.md").write_text(
                "---\ntitle: X\nstatus: working\nversion: 1\nbaseline: x\nowner: x\nlast_updated: x\ndependencies: []\n---\n[old](HANDOFF/current_progress.md)\n",
                encoding="utf-8",
            )
            self.assertTrue(integrity.handoff_reference_errors(root))


class MappingTests(unittest.TestCase):
    def setUp(self) -> None:
        self.mapping = integrity.read("docs/08_validation/arinc_615a_object_mapping_register.md")

    def test_controlled_population_passes(self) -> None:
        self.assertEqual(integrity.mapping_errors(self.mapping), [])

    def test_duplicate_source_row_is_rejected(self) -> None:
        row = next(line for line in self.mapping.splitlines() if line.startswith("| R01 |"))
        self.assertTrue(integrity.mapping_errors(self.mapping.replace(row, f"{row}\n{row}", 1)))

    def test_duplicate_instance_row_is_rejected(self) -> None:
        row = next(line for line in self.mapping.splitlines() if line.startswith("| A01 |"))
        self.assertTrue(integrity.mapping_errors(self.mapping.replace(row, f"{row}\n{row}", 1)))

    def test_strengthened_relation_is_rejected(self) -> None:
        changed = self.mapping.replace("`candidate-correspondence`", "`instantiates`", 1)
        self.assertTrue(integrity.mapping_errors(changed))

    def test_missing_row_is_rejected(self) -> None:
        changed = "\n".join(line for line in self.mapping.splitlines() if not line.startswith("| A07 |"))
        self.assertTrue(integrity.mapping_errors(changed))


class InventoryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.status = integrity.load_status()
        self.evidence = integrity.read("docs/08_validation/arinc_615a_v43_migration_evidence_return.md")

    def test_controlled_inventory_passes(self) -> None:
        self.assertEqual(integrity.inventory_errors(self.evidence, self.status), [])

    def test_swapped_hashes_are_rejected(self) -> None:
        items = self.status["crossRepository"]["arinc615a"]["sourceInventory"]
        first, second = items[0]["sha256"], items[1]["sha256"]
        changed = self.evidence.replace(first, "__FIRST__", 1)
        changed = changed.replace(second, first, 1).replace("__FIRST__", second, 1)
        self.assertTrue(integrity.inventory_errors(changed, self.status))

    def test_wrong_byte_count_is_rejected(self) -> None:
        item = self.status["crossRepository"]["arinc615a"]["sourceInventory"][0]
        changed = self.evidence.replace(
            f"| `{item['path']}` | {item['bytes']} |",
            f"| `{item['path']}` | {item['bytes'] + 1} |",
            1,
        )
        self.assertTrue(integrity.inventory_errors(changed, self.status))

    def test_mutable_locator_is_rejected(self) -> None:
        arinc = self.status["crossRepository"]["arinc615a"]
        immutable = f"{arinc['repository']}/blob/{arinc['assessedSource']['releaseCommit']}/"
        mutable = "blob/" + "ma" + "in/"
        changed = self.evidence.replace(immutable, f"{arinc['repository']}/{mutable}", 1)
        self.assertTrue(integrity.inventory_errors(changed, self.status))


if __name__ == "__main__":
    unittest.main()
