from __future__ import annotations

import importlib.util
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


class ThirdHandshakeMappingTests(unittest.TestCase):
    def setUp(self) -> None:
        self.mapping = integrity.read(
            "docs/08_validation/arinc_615a_object_mapping_register.md"
        )

    def test_controlled_18_plus_7_population_passes(self) -> None:
        self.assertEqual(integrity.mapping_errors(self.mapping), [])

    def test_duplicate_source_row_is_rejected(self) -> None:
        row = next(line for line in self.mapping.splitlines() if line.startswith("| R01 |"))
        changed = self.mapping.replace(row, f"{row}\n{row}", 1)
        self.assertTrue(integrity.mapping_errors(changed))

    def test_duplicate_instance_only_row_is_rejected(self) -> None:
        row = next(line for line in self.mapping.splitlines() if line.startswith("| A01 |"))
        changed = self.mapping.replace(row, f"{row}\n{row}", 1)
        self.assertTrue(integrity.mapping_errors(changed))

    def test_source_relation_strengthening_is_rejected(self) -> None:
        changed = self.mapping.replace(
            "| R02 | VerificationBasisElement | applicable CRS item | v4.3 release; legacy-origin object | `candidate-correspondence` |",
            "| R02 | VerificationBasisElement | applicable CRS item | v4.3 release; legacy-origin object | `instantiates` |",
            1,
        )
        self.assertTrue(integrity.mapping_errors(changed))

    def test_missing_instance_only_row_is_rejected(self) -> None:
        changed = "\n".join(
            line for line in self.mapping.splitlines() if not line.startswith("| A07 |")
        )
        self.assertTrue(integrity.mapping_errors(changed))

    def test_instance_only_generic_promotion_is_rejected(self) -> None:
        changed = self.mapping.replace(
            "| A01 | `INSTANCE-ONLY-ADDITIONAL` | VerificationCase | Test Purpose | v4.3 release | `no-direct-correspondence` | `NOT-DETERMINED` |",
            "| A01 | `INSTANCE-ONLY-ADDITIONAL` | VerificationCase | Test Purpose | v4.3 release | `instantiates` | `CANDIDATE` |",
            1,
        )
        self.assertTrue(integrity.mapping_errors(changed))


class ThirdHandshakeIdentityTests(unittest.TestCase):
    def setUp(self) -> None:
        self.evidence = integrity.read(
            "docs/08_validation/arinc_615a_v43_migration_evidence_return.md"
        )
        self.disposition = integrity.read(
            "docs/08_validation/arinc_615a_third_handshake_compatibility_disposition.md"
        )
        self.registry = integrity.read("docs/08_validation/instance_registry.md")
        self.contract = integrity.read(
            "docs/08_validation/cross_repository_instance_contract.md"
        )

    def errors(
        self,
        *,
        evidence: str | None = None,
        disposition: str | None = None,
        registry: str | None = None,
        contract: str | None = None,
    ) -> list[str]:
        return integrity.third_handshake_document_errors(
            evidence or self.evidence,
            disposition or self.disposition,
            registry or self.registry,
            contract or self.contract,
        )

    def test_controlled_documents_pass(self) -> None:
        self.assertEqual(self.errors(), [])

    def test_swapped_source_hashes_are_rejected(self) -> None:
        first = integrity.SOURCE_INVENTORY[
            "docs/control/contracts/EXTERNAL_GVS_BINDING.md"
        ][1]
        second = integrity.SOURCE_INVENTORY[
            "docs/control/contracts/ARINC615A_PROFILE_BINDING_CONFIGURATION.md"
        ][1]
        changed = self.evidence.replace(first, "__FIRST_HASH__", 1)
        changed = changed.replace(second, first, 1).replace("__FIRST_HASH__", second, 1)
        self.assertTrue(self.errors(evidence=changed))

    def test_incorrect_source_byte_count_is_rejected(self) -> None:
        changed = self.evidence.replace(
            "| `docs/control/contracts/EXTERNAL_GVS_BINDING.md` | 9949 |",
            "| `docs/control/contracts/EXTERNAL_GVS_BINDING.md` | 9950 |",
            1,
        )
        self.assertTrue(self.errors(evidence=changed))

    def test_incorrect_tag_object_is_rejected(self) -> None:
        changed = self.evidence.replace(
            f"| v4.3 tag object | `{integrity.ARINC_V43_TAG_OBJECT}` |",
            f"| v4.3 tag object | `{'0' * 40}` |",
            1,
        )
        self.assertTrue(self.errors(evidence=changed))

    def test_incorrect_peeled_target_is_rejected(self) -> None:
        changed = self.evidence.replace(
            f"| v4.3 peeled target | `{integrity.ARINC_V43_MERGE_COMMIT}` |",
            f"| v4.3 peeled target | `{'1' * 40}` |",
            1,
        )
        self.assertTrue(self.errors(evidence=changed))

    def test_mutable_source_locator_is_rejected(self) -> None:
        immutable = (
            f"{integrity.ARINC_REPOSITORY}/blob/"
            f"{integrity.ARINC_V43_MERGE_COMMIT}/"
        )
        changed = self.evidence.replace(
            immutable, f"{integrity.ARINC_REPOSITORY}/blob/main/", 1
        )
        self.assertTrue(self.errors(evidence=changed))

    def test_wrong_review_id_is_rejected(self) -> None:
        changed = self.evidence.replace(
            f"Review ID {integrity.ARINC_HUMAN_REVIEW_ID}",
            "Review ID 0000000000",
            1,
        )
        self.assertTrue(self.errors(evidence=changed))

    def test_weakened_activation_event_is_rejected(self) -> None:
        changed = self.disposition.replace(
            "independent approval of unchanged PR #15 head plus ordinary two-parent merge commit",
            "merge PR #15",
            1,
        )
        self.assertTrue(self.errors(disposition=changed))

    def test_wrong_method_definition_is_rejected(self) -> None:
        changed = self.registry.replace(
            integrity.METHOD_DEFINITION_COMMIT, "0" * 40
        )
        self.assertTrue(self.errors(registry=changed))

    def test_mutable_release_tag_is_rejected(self) -> None:
        changed = self.registry.replace(
            "Active migration annotated release tag | `v4.3`",
            "Active migration annotated release tag | `main`",
        )
        self.assertTrue(self.errors(registry=changed))

    def test_unqualified_compatibility_is_rejected(self) -> None:
        changed = self.disposition.replace(
            "Candidate overall disposition | `REVIEWED-COMPATIBLE-WITH-QUALIFICATION`",
            "Candidate overall disposition | `REVIEWED-COMPATIBLE`",
            1,
        )
        self.assertTrue(self.errors(disposition=changed))

    def test_project_configuration_promotion_is_rejected(self) -> None:
        changed = self.registry.replace(
            "Project Configuration | `TMP-PC-ARINC615A-01`; `NOT YET ESTABLISHED`",
            "Project Configuration | `TMP-PC-ARINC615A-01`; `ESTABLISHED`",
        )
        self.assertTrue(self.errors(registry=changed))

    def test_instance_evaluation_promotion_is_rejected(self) -> None:
        changed = self.registry.replace("`NOT-EXERCISED`", "`INSTANCE-EXERCISED`", 1)
        self.assertTrue(self.errors(registry=changed))


class ThirdHandshakeActivationTests(unittest.TestCase):
    def test_pull_request_event_cannot_self_activate(self) -> None:
        with mock.patch.dict(integrity.os.environ, {"GITHUB_EVENT_NAME": "pull_request"}):
            self.assertFalse(integrity.third_handshake_activated())

    def test_ordinary_two_parent_merge_activates_on_main_history(self) -> None:
        merge = "a" * 40
        with (
            mock.patch.dict(integrity.os.environ, {}, clear=True),
            mock.patch.object(
                integrity,
                "git",
                side_effect=[merge, f"{merge} {'b' * 40} {'c' * 40}"],
            ),
            mock.patch.object(
                integrity.subprocess,
                "run",
                return_value=mock.Mock(returncode=0),
            ),
        ):
            self.assertTrue(integrity.third_handshake_activated())

    def test_pre_activation_state_is_not_determined(self) -> None:
        self.assertEqual(
            integrity.compatibility_for_activation(False),
            "NOT-DETERMINED",
        )

    def test_post_activation_state_is_qualified_compatible(self) -> None:
        self.assertEqual(
            integrity.compatibility_for_activation(True),
            "REVIEWED-COMPATIBLE-WITH-QUALIFICATION",
        )


if __name__ == "__main__":
    unittest.main()
