---
title: Temporary Controlled Instance Register
status: working
version: 0.4
baseline: post-v0.2
owner: research
last_updated: 2026-08-30
dependencies:
  - ../../project-status.json
  - cross_repository_instance_contract.md
  - arinc_615a_object_mapping_register.md
  - arinc_615a_instance_evaluation_protocol.md
  - arinc_615a_v43_migration_evidence_return.md
  - arinc_615a_third_handshake_compatibility_disposition.md
---

# Temporary Controlled Instance Register

This temporary register is used before a versioned object registry exists. Its keys support navigation and mapping only; they are not stable object IDs, executable schema keys or compatibility approvals. Current machine-readable values are canonical in [`project-status.json`](../../project-status.json).

## Registered ARINC 615A instance

| Field | Controlled value |
|---|---|
| Temporary mapping key | `TMP-ARINC615A-01` |
| Instance name/type | ARINC 615A protocol conformance verification / deterministic protocol-conformance instance |
| Canonical repository URL | <https://github.com/ZhangChi0727/arinc-615a-conformance> |
| Method definition identity | `48dd8232b7efe6b0dba3fcb75dfc154d034d2b0b` — Candidate GVS Core method context |
| Method compatibility disposition identity | `c02330d21fe2d3e89e7e2d6352872d52461a6dda` — distinct from method definition |
| Assessed migration baseline | baseline ID `RB-2026-001-v4.3`; release tag `v4.3`; release commit `523d42bf03a1135b3d63a00bfb47d3b879d3927e`; tag object `28312fd9c5470cb15d76eb3762c99a25ab842cfd` |
| Instance acknowledgement release | baseline ID `RB-2026-001-v4.3.1`; release tag `v4.3.1`; release commit `72ca6df88cb8def5221a8fa54e69551f9e7041db` |
| Acknowledgement tag object / peeled target | `55005cc57e26dd56ea1f0fec3ffdbbf1e67d1beb` / `72ca6df88cb8def5221a8fa54e69551f9e7041db` |
| Third-handshake state | `COMPLETE` |
| Compatibility | `REVIEWED-COMPATIBLE-WITH-QUALIFICATION`; subject to Q-01–Q-09 |
| Conformance-Testing Profile | `TMP-CTP-ARINC615A-01`, version `0.1-candidate` |
| Product Binding | `TMP-PB-ARINC615A-01`, version `0.1-candidate` |
| Project Configuration | `TMP-PC-ARINC615A-01`; `NOT YET ESTABLISHED` |
| Mapping register | [ARINC 615A Object Mapping Register](arinc_615a_object_mapping_register.md), 18 source rows + 7 instance-only rows |
| Evaluation protocol | [ARINC 615A Instance Evaluation Protocol](arinc_615a_instance_evaluation_protocol.md); `NOT-EXERCISED` |
| RQ8 | `OPEN` |
| Execution evidence manifest | `NOT AVAILABLE — MIGRATION-ONLY REVIEW` |
| Open work | establish a controlled Project Configuration and execute a separate bounded evaluation; later add UAV and LLM evidence before cross-instance synthesis |
| Non-claims | no protocol conformance, empirical instance evaluation, framework validation, stable registry, certification readiness or Generic promotion |

## Historical provenance retained

| Role | Immutable provenance |
|---|---|
| Pre-framework legacy release | `3299e6dae83424862f75a4c1d09b91b80d9d8b00`; baseline/tag `RB-2026-001-v4.2.1` |
| Pre-migration control-state snapshot | `0ce96f701159fd4156d5e5e9889360f53977a61b`; governance provenance, not release content |
| Reviewed migration head | `5d149d1f8e92bbed438fe8bc78be9e8972fecb7d`; natural-person Review `5029797924`, platform `COMMENTED`, body outcome `APPROVE` |
| Method-contract authoring base | `196cfc2426a841a4adb9c9159660253896b0257c`; authoring provenance only |

The v4.2.1 origin is never relabelled as framework-based. The v4.3 release is the assessed GVS-bound migration baseline; v4.3.1 is the later instance acknowledgement of the method-side disposition. These roles are not interchangeable.

## Configuration and evaluation boundary

`TMP-PC-ARINC615A-01` is still a placeholder. No controlled IUT, setup, procedure, tool, clock/error budget, environment, evidence destination or reviewer population is registered. Therefore no execution manifest exists, `INSTANCE-EXERCISED` is not obtained and RQ8 remains `OPEN`.

Future replacement by a versioned registry requires an explicit migration record preserving all historical, assessed and acknowledgement identities above.
