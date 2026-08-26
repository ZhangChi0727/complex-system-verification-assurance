---
title: Temporary Controlled Instance Register
status: working
version: 0.3
baseline: post-v0.2
owner: research
last_updated: 2026-08-26
dependencies:
  - cross_repository_instance_contract.md
  - arinc_615a_object_mapping_register.md
  - arinc_615a_instance_evaluation_protocol.md
  - arinc_615a_v43_migration_evidence_return.md
  - arinc_615a_third_handshake_compatibility_disposition.md
---

# Temporary Controlled Instance Register

This is a **temporary controlled instance register** used before a versioned
object registry exists. Temporary keys are navigation/mapping identities only;
they are not stable object IDs, executable schema keys or compatibility
approvals.

## Registered instance

| Field | Controlled value |
|---|---|
| Temporary mapping key | `TMP-ARINC615A-01` |
| Instance name/type | ARINC 615A protocol conformance verification / deterministic protocol-conformance instance |
| Canonical repository URL | <https://github.com/ZhangChi0727/arinc-615a-conformance> |
| Historical legacy baseline release commit | `3299e6dae83424862f75a4c1d09b91b80d9d8b00` |
| Historical legacy annotated tag | `RB-2026-001-v4.2.1` |
| Historical origin classification | `PRE-FRAMEWORK LEGACY INSTANCE BASELINE` |
| Pre-migration control-state commit | `0ce96f701159fd4156d5e5e9889360f53977a61b` — control provenance; not release content |
| Active migration baseline ID | `RB-2026-001-v4.3` |
| Active migration release commit | `523d42bf03a1135b3d63a00bfb47d3b879d3927e` |
| Active migration annotated release tag | `v4.3` |
| Active migration tag object / peeled target | `28312fd9c5470cb15d76eb3762c99a25ab842cfd` / `523d42bf03a1135b3d63a00bfb47d3b879d3927e` |
| Post-merge control-state commit | `NONE` |
| Active migration classification | `GVS-BOUND LEGACY MIGRATION BASELINE`; legacy historical origin preserved |
| PR #9 reviewed head | `5d149d1f8e92bbed438fe8bc78be9e8972fecb7d` |
| PR #9 human review | Review ID `5029797924`; platform `COMMENTED`; body outcome `APPROVE`; exact reviewed head above |
| PR #14 authoring base | `196cfc2426a841a4adb9c9159660253896b0257c` — authoring provenance only |
| Candidate method definition identity | `48dd8232b7efe6b0dba3fcb75dfc154d034d2b0b` — Candidate GVS Core 0.3 |
| Conformance-Testing Profile | `TMP-CTP-ARINC615A-01`, version `0.1-candidate` |
| Product Binding | `TMP-PB-ARINC615A-01`, version `0.1-candidate` |
| Project Configuration | `TMP-PC-ARINC615A-01`; `NOT YET ESTABLISHED` |
| Candidate GVS Core binding status | `ESTABLISHED FOR MIGRATION` at the method definition commit; temporary contract |
| Compatibility status | `NOT-DETERMINED`; candidate `REVIEWED-COMPATIBLE-WITH-QUALIFICATION` is pending independent method-side review |
| Mapping register | [ARINC 615A Object Mapping Register](arinc_615a_object_mapping_register.md), version 0.3; 18 + 7 rows |
| Migration evidence return | [ARINC v4.3 Migration Evidence Return](arinc_615a_v43_migration_evidence_return.md), version 0.1; `REVIEW PENDING` |
| Compatibility disposition | [Third-Handshake Compatibility Disposition](arinc_615a_third_handshake_compatibility_disposition.md), version 0.1; candidate only |
| Evaluation protocol | [ARINC 615A Instance Evaluation Protocol](arinc_615a_instance_evaluation_protocol.md), version 0.2; `NOT-EXERCISED` |
| Execution evidence manifest | `NOT AVAILABLE — MIGRATION-ONLY REVIEW` |
| Open blockers | method-side third-handshake independent review/merge; later ARINC acknowledgement; controlled Project Configuration; separate protocol execution |
| Non-claims | no protocol conformance, empirical instance evaluation, framework validation, stable registry, certification readiness or Generic promotion |

## Historical and active-migration boundary

The legacy v4.2.1 release predates the Candidate GVS Core and remains frozen.
The v4.3 release is a GVS-bound migration baseline, not a retrospective rewrite
of that origin. Baseline ID `RB-2026-001-v4.3` and release tag `v4.3` are separate
controlled fields. The pre-migration control-state commit and PR reviewed head
are provenance; neither substitutes for the tagged release commit.

PR #9 merge and release establish the versioned method binding and migration
contract. They do not establish compatibility or empirical evaluation. The
method-side third handshake proposes a qualified compatibility disposition, but
formal compatibility stays `NOT-DETERMINED` until independent approval and
merge. The future ARINC acknowledgement is a separate baseline change.

## Configuration and evaluation boundary

`TMP-PC-ARINC615A-01` remains a temporary placeholder. No controlled IUT,
setup, procedure, tool, clock/error-budget, environment, evidence-destination
or reviewer values are registered. Consequently, no execution manifest exists,
the evaluation protocol has not run, `INSTANCE-EXERCISED` is not obtained and
RQ8 remains `Open`.

The temporary key must never be called stable. Future replacement by a
versioned registry requires an explicit migration record preserving all
historical and active-migration identities above.
