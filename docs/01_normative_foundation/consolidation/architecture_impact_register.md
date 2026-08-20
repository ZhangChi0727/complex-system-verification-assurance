---
title: Architecture Impact Register
status: working
version: 0.1
baseline: post-v0.2
owner: research
last_updated: 2026-08-20
dependencies:
  - ../standards_baseline.md
  - ../normative_gap_matrix.md
  - ../../00_overview/roadmap.md
  - ../../03_dbse_workflow/README.md
---

# Architecture Impact Register

本登记表控制后续标准研究对 V0–V12 的确认、扩展、修改、拆分、合并或无影响处置，并保持稳定 V-ID、历史语义和迁移影响可追溯。它不是 `Established clause basis`，也不能替代条款研究、来源定位或独立复核。

`SOURCE ACQUIRED`、`METADATA VERIFIED`、标准标题或公开摘要均不能产生架构结论。只有完成 clause-level study 并通过 independent review 后，某项 disposition 才能标为 `REVIEWED`。未经研究的来源统一登记为 `DEFERRED — pending clause study`，不得从候选主题推断 `CONFIRM`、`EXTEND` 或其他实质影响。

## Controlled dispositions

| Disposition | Meaning | Additional control |
|---|---|---|
| `CONFIRM` | Reviewed evidence confirms the current architecture checkpoint. | Record the reviewed clause locator and affected dimensions. |
| `EXTEND` | Add an attribute, relation or controlled extension point without replacing existing semantics. | Record compatibility with current V-elements. |
| `MODIFY` | Change an existing element's semantics or boundary. | Compatibility and migration statement required. |
| `SPLIT` | Split an existing element or responsibility. | Stable-ID history and migration statement required. |
| `MERGE` | Merge duplicated elements or responsibilities. | Stable-ID history and migration statement required. |
| `NO-IMPACT` | Reviewed findings do not affect V0–V12. | Record why the source remains relevant. |
| `DEFERRED` | Evidence, dependency or review is insufficient for disposition. | No architecture conclusion is permitted. |

## Impact register

| Source | Study status | Affected V-elements/dimensions | Candidate impact | Disposition | Basis locator | Independent review | Migration required | Residual uncertainty |
|---|---|---|---|---|---|---|---|---|
| ISO/IEC/IEEE 15288:2023 | CLAUSE STUDY REVIEWED | V0–V12 process/view basis; Verification process relations | Historical contribution already represented in v0.2 | CONFIRM — historical v0.2 checkpoint | `../standard_notes/iso_15288.md`; `../reviews/iso_15288_informal_review.md`; `../../00_overview/research_baseline_v0.2.md` | REVIEWED | No — preserve historical checkpoint | Later source cohort can still modify orchestration semantics or boundaries |
| ISO/IEC/IEEE 24748-1:2024 | CLAUSE STUDY REVIEWED | Lifecycle/process-view and current composite-gate assumptions | Historical contribution already represented in v0.2 | CONFIRM — historical v0.2 checkpoint | `../standard_notes/iso_24748_1.md`; `five_source_consistency_gap_review.md`; `../../00_overview/research_baseline_v0.2.md` | REVIEWED | No — preserve historical checkpoint | Authority, state, iteration and information-item assignments remain open |
| ISO/IEC/IEEE 24748-2:2024 | CLAUSE STUDY REVIEWED | Strategy integration, process instantiation and current V10/V6/V12 inputs | Historical reviewed supporting refinement | CONFIRM — historical v0.2 checkpoint | `../standard_notes/iso_24748_2_targeted_review.md`; `../reviews/ISO-24748-2--SAE-ARP4754B-External-Informal-Review.md` | REVIEWED | No — preserve historical checkpoint | Later lifecycle/software/agility sources remain unstudied |
| SAE ARP4754B:2023 | CLAUSE STUDY REVIEWED | Civil-aviation governance/profile extensions to V0–V12 | Historical aviation-profile extension already represented in v0.2 | EXTEND — historical aviation-profile checkpoint | `../standard_notes/sae_arp4754b.md`; `five_source_consistency_gap_review.md` | REVIEWED | No — profile boundary retained | Item-level objectives and certification authority remain outside current basis |
| SAE ARP4761A:2023 | CLAUSE STUDY REVIEWED | Safety Assessment Process View and aviation inputs to V10–V12 | Historical aviation-profile extension already represented in v0.2 | EXTEND — historical aviation-profile checkpoint | `../standard_notes/sae_arp4761a.md`; `five_source_consistency_gap_review.md` | REVIEWED | No — profile boundary retained | Generic safety/assurance sufficiency and authority remain open |
| ISO/IEC/IEEE 24748-3:2020 | METADATA VERIFIED; CLAUSE STUDY PENDING; 12207:2017→2026 COMPATIBILITY OPEN | LC-G03/LC-G04; software-lifecycle and ISO-G07 candidate dimensions | Potential software-process application and information-item impact only | DEFERRED — pending clause study | Metadata only; no clause locator | NOT STARTED | Undetermined | Requires 12207:2026 foundation and targeted compatibility review |
| ISO/IEC/IEEE 24748-4:2026 | METADATA VERIFIED; CLAUSE STUDY PENDING | V0; planning/governance information items; LC-G04/ISO-G07C | Potential SEMP/planning information-item impact only | DEFERRED — pending clause study | Metadata only; no clause locator | NOT STARTED | Undetermined | Must be studied before final architecture synthesis; overlap with 15289/16326 open |
| ISO/IEC/IEEE 24748-5:2017 | METADATA VERIFIED; CLAUSE STUDY PENDING; OVERLAP REVIEW REQUIRED | Software planning information items; LC-G04/ISO-G07C | Potential software-plan and information-item impact only | DEFERRED — pending overlap and clause study | Metadata only; no clause locator | NOT STARTED | Undetermined | 12207/15289/16326 overlap unresolved |
| ISO/IEC/IEEE 24748-6:2023 | METADATA VERIFIED; CLAUSE STUDY PENDING | Integration information items; LC-G04/ISO-G07 candidate dimensions | Potential integration-information assignment impact only | DEFERRED — pending clause study | Metadata only; no clause locator | NOT STARTED | Undetermined | Relationship to current V-elements and 15289 taxonomy unstudied |
| ISO/IEC/IEEE 24748-8:2019 | METADATA VERIFIED; FORMAL REVISION WATCH; CLAUSE STUDY DEFERRED | LC-G01/LC-G02; domain review/gate abstraction only | Potential defence-profile review/audit patterns; no direct Generic Core impact | DEFERRED — await published replacement and source decision | Metadata only; FDIS excluded as normative basis | NOT STARTED | Undetermined | Cross-domain abstraction, current-edition acquisition and replacement timing open |
| ISO/IEC/IEEE 24748-10:2026 | METADATA VERIFIED; CLAUSE STUDY PENDING; REQUIRED BEFORE ARCHITECTURE FREEZE | LC-G03/ISO-G05; iteration, re-entry, tailoring and dynamic-environment dimensions | Potential iteration/re-entry/tailoring impact only | DEFERRED — pending clause study | Metadata only; no clause locator | NOT STARTED | Undetermined | Must be disposed before architecture freeze; no reduction of evidence or gate obligations permitted |

## Governance rules

- Stable V-identifiers do not make current semantics immutable.
- A source may affect multiple V-elements or dimensions, but every impact must retain source and review provenance.
- `MODIFY`, `SPLIT` and `MERGE` require a migration note before approval; silent reinterpretation of a stable V-ID is prohibited.
- Five-source rows record historical reviewed impact only and do not reopen or rewrite v0.2 conclusions.
- Candidate rows must remain `DEFERRED` until clause study and independent review support another disposition.
- Architecture maturity can move from `OPEN-CANDIDATE` to `REVIEWED-PROVISIONAL` only through the roadmap's architecture-synthesis gate.
