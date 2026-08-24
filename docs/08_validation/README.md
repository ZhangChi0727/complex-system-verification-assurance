---
title: Framework Validation Workspace
status: working
version: 0.4
baseline: post-v0.2
owner: research
last_updated: 2026-08-24
dependencies:
  - ../00_overview/research_scope.md
  - ../00_overview/research_questions.md
  - ../02_verification_framework/generic_verification_suite_core.md
  - cross_repository_instance_contract.md
  - instance_registry.md
  - arinc_615a_object_mapping_register.md
  - arinc_615a_instance_evaluation_protocol.md
---

# Framework Validation Workspace

本目录管理 Candidate GVS Core 的跨仓库实例治理与 RQ8 验证准备：completeness、traceability、repeatability、scalability、reusability，以及 Reviewability、Change Impact Detection、Coverage Explicitness、Evidence Quality、interface isolation 和 hidden-assumption detection。

实例只能 `SUPPORT`、`QUALIFY` 或 `FALSIFY` 候选主张，不得直接重定义 Generic semantic contract。实例 finding 必须经 [cross-repository contract](cross_repository_instance_contract.md) 的 Framework Change Proposal、跨实例相关性、依据和独立评审链。

## Controlled governance entry points

- [Candidate GVS Core working definition](../02_verification_framework/generic_verification_suite_core.md)
- [Cross-Repository Instance Contract](cross_repository_instance_contract.md)
- [Temporary Controlled Instance Register](instance_registry.md)
- [ARINC 615A Temporary Object Mapping Register](arinc_615a_object_mapping_register.md)
- [ARINC 615A Instance Evaluation Protocol](arinc_615a_instance_evaluation_protocol.md)

## Validation instances

| Instance | Verification type | Status | Primary thesis contribution |
|---|---|---|---|
| ARINC 615A protocol conformance verification | deterministic, specification-driven conformance verification | **First controlled legacy-to-framework instance**; compatibility scoping | exercises Core/Profile/Binding/Configuration isolation and the design–execution lower chain |
| UAV flight-management system verification | safety-driven system verification | Planned | assurance constraints, typed independence, coverage and change impact |
| LLM service reliability/performance verification | probabilistic, weak-Oracle service verification | Planned | sufficiency, evidence/argument and coverage boundaries |

ARINC active external identity is repository <https://github.com/ZhangChi0727/arinc-615a-conformance>, commit `0ce96f701159fd4156d5e5e9889360f53977a61b`, baseline `RB-2026-001-v4.2.1`. It is a `PRE-FRAMEWORK LEGACY INSTANCE BASELINE`; Candidate GVS Core binding is `NOT YET ESTABLISHED` and compatibility is `NOT-DETERMINED`.

[Draft PR #9](https://github.com/ZhangChi0727/arinc-615a-conformance/pull/9), head `53a98447bcfa862f082ce443d69115067d3ff2f1`, candidate baseline `RB-2026-001-v4.3`, is an `UNMERGED MIGRATION CANDIDATE`. It is not the active baseline and has no active semantic authority. This repository does not modify or approve that PR.

**DCAS is not a validation instance.** It remains an industrial-practice knowledge source whose patterns pass through the controlled abstraction ladder.

## Instance × framework-element exercise matrix

H = strong exercise, M = medium, L = weak/boundary. These H/M/L judgments are unchanged by the present governance increment. A single passing instance cannot establish the whole framework.

| Framework element | ARINC 615A | UAV FMS | LLM service |
|---|---|---|---|
| V1 Verification Basis / Obligation | H（PICS-like declaration controls applicability; applicable CRS items are candidate typed basis; obligation mapping remains open） | M | L（basis must be constructed） |
| V2 Requirement verifiability | H | M | L |
| V3 Verification Strategy | H | H | M |
| V4 Verification Case Design | H（Test Purpose correspondence remains open pending ISO/IEC 9646 Task 002） | M | M |
| V5 Verification Procedure | H（executable test-suite procedures） | M | M |
| V6 Verification Readiness gate | M | M | L |
| V7/V8 Execution / Result Evaluation | H（Oracle applies evaluation rules; Verdict is Result） | M | M |
| V9/V10 Anomaly / Change Impact | M | H | M |
| V11 Coverage | M（clause/obligation coverage candidate） | H | L（coverage definition challenged） |
| V11 Sufficiency（RQ4） | L | H | H |
| Assurance / Independence constraints | L | H | M |
| Evidence / Argument / Claim | M | H | H |
| Oracle（ISO-G04） | H（generic rule responsibility separated from ARINC-specific logic） | M | L（open research question） |
| MBSE model / optional executable realization | H | M | M |

ARINC mainly exercises the design–execution lower chain and the four-layer ownership boundary; it cannot validate the Candidate GVS Core's complete assurance/sufficiency scope. UAV FMS and LLM service remain required, and RQ8 remains `Open`.

## Instance and standard boundary

Generic conformance-testing methodology research population remains ISO/IEC 9646 Parts 1/2/4/5/6/7; ITU-T X.29x is bibliographic context and TTCN-3 is execution technology. No clause conclusion is added here. In particular:

- PICS-like declaration controls applicability and the applicable basis population; PICS is not itself Verification Basis;
- Test Purpose correspondence remains `NOT-DETERMINED` until Task 002 clause study and independent review; it is not preassigned to VerificationCase;
- Oracle is an evaluation rule/mechanism; Verdict is Result;
- raw trace, timestamp, log or manifest begins as Observation/Raw Record/Provenance Container and is not automatically Evidence;
- PASS does not automatically establish Objective Satisfaction or Compliance Claim.

The authoritative temporary row-level dispositions are in the [mapping register](arinc_615a_object_mapping_register.md), not in this overview.

## Strong contract / weak implementation coupling

```text
Complete Verification Suite
= Candidate Generic Verification Suite Core
+ Verification Profile
+ Product Binding
+ Project Configuration
```

The method repository owns Candidate GVS Core semantics and evaluation contracts. The external instance repository owns its Profile, Binding, Configuration, tools, concrete Oracle implementation and original evidence. Coupling uses immutable version identities and reviewed mappings, not copied definitions, mutable branches, submodules, shared internal code or implementation APIs.

Current work is compatibility scoping only. No compatibility verdict, stable registry, schema freeze, certification acceptance or instance validation is claimed.
