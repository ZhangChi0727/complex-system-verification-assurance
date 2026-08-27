---
title: Framework Validation Workspace
status: working
version: 0.6
baseline: post-v0.2
owner: research
last_updated: 2026-08-26
dependencies:
  - ../00_overview/research_scope.md
  - ../00_overview/research_questions.md
  - ../02_verification_framework/generic_verification_suite_core.md
  - cross_repository_instance_contract.md
  - instance_registry.md
  - arinc_615a_object_mapping_register.md
  - arinc_615a_instance_evaluation_protocol.md
  - arinc_615a_v43_migration_evidence_return.md
  - arinc_615a_third_handshake_compatibility_disposition.md
  - arinc_615a_third_handshake_review_handoff.md
---

# Framework Validation Workspace

本目录管理 Candidate GVS Core 的跨仓库实例治理与 RQ8 验证准备：
completeness、traceability、repeatability、scalability、reusability，以及
Reviewability、Change Impact Detection、Coverage Explicitness、Evidence
Quality、interface isolation 和 hidden-assumption detection。

实例只能 `SUPPORT`、`QUALIFY` 或 `FALSIFY` 候选主张，不得直接重定义
Generic semantic contract。实例 finding 必须经跨仓库契约的 Framework
Change Proposal、跨实例相关性、依据和独立评审链。

## Controlled governance entry points

- [Candidate GVS Core working definition](../02_verification_framework/generic_verification_suite_core.md)
- [Cross-Repository Instance Contract](cross_repository_instance_contract.md)
- [Temporary Controlled Instance Register](instance_registry.md)
- [ARINC 615A Temporary Object Mapping Register](arinc_615a_object_mapping_register.md)
- [ARINC 615A Instance Evaluation Protocol](arinc_615a_instance_evaluation_protocol.md)
- [ARINC v4.3 Migration Evidence Return](arinc_615a_v43_migration_evidence_return.md)
- [ARINC v4.3 Third-Handshake Compatibility Disposition](arinc_615a_third_handshake_compatibility_disposition.md)
- [ARINC v4.3 Third-Handshake Independent-Review Handoff](arinc_615a_third_handshake_review_handoff.md)
- [PR #14 external review disposition](pr_14_external_review_disposition.md)

## ARINC immutable identity ledger

| Role | Controlled identity | Meaning |
|---|---|---|
| Historical legacy baseline | release `3299e6dae83424862f75a4c1d09b91b80d9d8b00`; annotated tag `RB-2026-001-v4.2.1` | frozen pre-framework origin |
| Pre-migration control state | `0ce96f701159fd4156d5e5e9889360f53977a61b` | governance provenance, not release content |
| Method definition | Candidate GVS Core 0.3 / `48dd8232b7efe6b0dba3fcb75dfc154d034d2b0b` | immutable method semantic context |
| PR #9 reviewed head | `5d149d1f8e92bbed438fe8bc78be9e8972fecb7d` | natural-person Review 5029797924 attaches here |
| Active migration baseline | baseline ID `RB-2026-001-v4.3`; release `523d42bf03a1135b3d63a00bfb47d3b879d3927e`; annotated tag `v4.3` | GVS-bound legacy migration baseline |
| Tag object / target | `28312fd9c5470cb15d76eb3762c99a25ab842cfd` / `523d42bf03a1135b3d63a00bfb47d3b879d3927e` | annotated tag peels to the ordinary merge |
| Post-merge control state | `NONE` | ARINC `main` equals the release commit |

`RB-2026-001-v4.3` is a baseline ID; `v4.3` is the actual release tag. The
historical v4.2.1 origin is not retroactively described as framework-based.

## Third-handshake state

Method-contract handshake and instance-migration handshake are complete. The
method-side compatibility-disposition handshake follows a conditional
activation rule:

- pre-activation formal compatibility: `NOT-DETERMINED`;
- activation event: independent approval of the unchanged PR #15 head plus an
  ordinary two-parent merge commit;
- post-activation formal compatibility:
  `REVIEWED-COMPATIBLE-WITH-QUALIFICATION` under Q-01–Q-09, with the merge SHA
  as the immutable method-disposition identity;
- required qualifications: Q-01–Q-09;
- source mapping: 18/18 retained without strengthening;
- instance-only population: 7/7 retained as non-Generic;
- Project Configuration: `NOT YET ESTABLISHED`;
- instance evaluation: `NOT-EXERCISED`;
- execution evidence manifest: `NOT AVAILABLE — MIGRATION-ONLY REVIEW`.

Compatibility review concerns migration-contract structure, ownership, mapping
and semantic interfaces. It is not execution of the instance evaluation
protocol. The repository checker reports only whether repository-side PR #15
ordinary-merge evidence is present. It does not access or validate the external
GitHub independent-approval record and therefore never declares formal
compatibility from Git history alone. The final release gate and work order B
must jointly confirm the named natural-person approval, its exact reviewed head,
the ordinary merge and equality between that head and the merge's second parent.

Work order B remains prohibited before that joint confirmation. After the
controlled activation event, ARINC acknowledgement is a separate work order and
baseline change bound to the method-disposition merge SHA; no post-merge method
status commit is needed.

## Validation instances

| Instance | Verification type | Status | Primary thesis contribution |
|---|---|---|---|
| ARINC 615A protocol conformance verification | deterministic, specification-driven conformance verification | first GVS-bound legacy migration baseline; compatibility follows the PR #15 activation rule; evaluation not exercised | Core/Profile/Binding/Configuration isolation and design–execution lower chain |
| UAV flight-management system verification | safety-driven system verification | Planned | assurance constraints, typed independence, coverage and change impact |
| LLM service reliability/performance verification | probabilistic, weak-Oracle service verification | Planned | sufficiency, evidence/argument and coverage boundaries |

**DCAS is not a validation instance.** It remains an industrial-practice
knowledge source whose patterns pass through the controlled abstraction ladder.

## Instance × framework-element exercise matrix

H = strong prospective exercise, M = medium and L = weak/boundary. These are
planning judgments, not executed results. A migration or compatibility review
does not change them into empirical findings.

| Framework element | ARINC 615A | UAV FMS | LLM service |
|---|---|---|---|
| V1 Verification Basis / Obligation | H; applicability/basis and obligation correspondence remain qualified/open | M | L |
| V2 Requirement verifiability | H | M | L |
| V3 Verification Strategy | H | H | M |
| V4 Verification Case Design | H; Test Purpose correspondence remains open | M | M |
| V5 Verification Procedure | H | M | M |
| V6 Verification Readiness gate | M | M | L |
| V7/V8 Execution / Result Evaluation | H; prospective only | M | M |
| V9/V10 Anomaly / Change Impact | M | H | M |
| V11 Coverage | M | H | L |
| V11 Sufficiency（RQ4） | L | H | H |
| Assurance / Independence constraints | L | H | M |
| Evidence / Argument / Claim | M; open dependencies | H | H |
| Oracle（ISO-G04） | H; responsibility separated from ARINC realization | M | L |
| MBSE model / optional executable realization | H | M | M |

ARINC mainly exercises the lower design–execution chain and four-layer ownership
boundary. It cannot validate the complete assurance/sufficiency scope. UAV FMS
and LLM service remain required, and RQ8 remains `Open`.

## Instance and standard boundary

Generic conformance-testing methodology research remains ISO/IEC 9646 Parts
1/2/4/5/6/7. No clause conclusion is added here:

- a PICS-like declaration controls applicability and the basis population; it is not itself Verification Basis;
- Test Purpose correspondence remains `NOT-DETERMINED` until Task 002 study/review;
- Oracle is the rule/mechanism and Verdict is a Result;
- raw trace/log/manifest starts as Observation/Raw Record/Provenance Container;
- PASS does not establish Objective Satisfaction, Evidence sufficiency or Compliance Claim.

The mapping register owns row-level dispositions. ISO/IEC/IEEE 15289:2019 Task
001 remains the first research stop; this parallel governance work does not
start or complete a clause study.

## Strong contract / weak implementation coupling

```text
Complete Verification Suite
= Candidate Generic Verification Suite Core
+ Verification Profile
+ Product Binding
+ Project Configuration
```

The method repository owns Candidate GVS Core semantics and evaluation
contracts. The instance repository owns Profile, Binding, Configuration, tools,
concrete Oracle implementation and original evidence. Coupling uses immutable
identities and reviewed mappings, not copied definitions, mutable branches,
submodules, shared internal code or implementation APIs.

Current work is migration-contract compatibility disposition only. No stable
registry, schema freeze, certification acceptance, instance validation,
`INSTANCE-EXERCISED`, `VALIDATED-BASELINE` or RQ8 closure is claimed.
