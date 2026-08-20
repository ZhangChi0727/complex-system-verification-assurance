---
title: Architecture Impact Register
status: working
version: 0.3
baseline: post-v0.2
owner: research
last_updated: 2026-08-21
dependencies:
  - ../standards_baseline.md
  - ../normative_gap_matrix.md
  - ../../00_overview/roadmap.md
  - ../../03_dbse_workflow/README.md
---

# Architecture Impact Register

本登记表控制后续标准研究对 V0–V12 的确认、扩展、修改、拆分、合并、弃用或无影响处置，并保持稳定 V-ID、历史语义和迁移影响可追溯。它不是 `Established clause basis`，也不能替代条款研究、来源定位或独立复核。

`SOURCE ACQUIRED`、`METADATA VERIFIED`、标准标题或公开摘要均不能产生架构结论。只有完成 clause-level study 并通过 independent review 后，某项 disposition 才能标为 `REVIEWED`。未经研究的来源统一登记为 `DEFERRED — pending clause study`，不得从候选主题推断 `CONFIRM`、`EXTEND` 或其他实质影响。

## Controlled dispositions

The controlled vocabulary is `CONFIRM / EXTEND / MODIFY / SPLIT / MERGE / DEPRECATE / NO-IMPACT / DEFERRED`; no synonymous or implicit disposition may bypass the controls below.

| Disposition | Meaning | Additional control |
|---|---|---|
| `CONFIRM` | Reviewed evidence confirms the current architecture checkpoint. | Record the reviewed clause locator, affected dimensions and confirmation rationale. |
| `EXTEND` | Add an attribute, relation or controlled extension point without replacing existing semantics. | Record compatibility with current V-elements. |
| `MODIFY` | Change an existing element's semantics or boundary. | Before/after semantics, compatibility and migration statement required. |
| `SPLIT` | Split an existing element or responsibility. | Before/after semantics, stable-ID history, compatibility and migration statement required. |
| `MERGE` | Merge duplicated elements or responsibilities. | Before/after semantics, stable-ID history, compatibility and migration statement required. |
| `DEPRECATE` | Retire a candidate element or relation shown to be unsupported, duplicated or incompatible. | Before/after semantics, stable-ID history, replacement/compatibility and migration statement required. |
| `NO-IMPACT` | Reviewed findings do not affect V0–V12. | Record the reviewed clause locator and rationale for no architecture effect. |
| `DEFERRED` | Evidence, dependency or review is insufficient for disposition. | This is not an architecture conclusion; no architecture effect may be inferred. |

## Impact register

| Source | Study status | Affected V-elements/dimensions | Candidate impact | Disposition | Basis locator | Independent review | Migration required | Residual uncertainty |
|---|---|---|---|---|---|---|---|---|
| ISO/IEC/IEEE 15288:2023 | CLAUSE STUDY REVIEWED | V0–V12 process/view basis; Verification process relations | Historical contribution already represented in v0.2 | CONFIRM — historical v0.2 checkpoint | `../standard_notes/iso_15288.md`; `../reviews/iso_15288_informal_review.md`; `../../00_overview/research_baseline_v0.2.md` | REVIEWED | No — preserve historical checkpoint | Later source cohort can still modify orchestration semantics or boundaries |
| ISO/IEC/IEEE 24748-1:2024 | CLAUSE STUDY REVIEWED | Lifecycle/process-view and current composite-gate assumptions | Historical contribution already represented in v0.2 | CONFIRM — historical v0.2 checkpoint | `../standard_notes/iso_24748_1.md`; `five_source_consistency_gap_review.md`; `../../00_overview/research_baseline_v0.2.md` | REVIEWED | No — preserve historical checkpoint | Authority, state, iteration and information-item assignments remain open |
| ISO/IEC/IEEE 24748-2:2024 | CLAUSE STUDY REVIEWED | Strategy integration, process instantiation and current V10/V6/V12 inputs | Historical reviewed supporting refinement | CONFIRM — historical v0.2 checkpoint | `../standard_notes/iso_24748_2_targeted_review.md`; `../reviews/ISO-24748-2--SAE-ARP4754B-External-Informal-Review.md` | REVIEWED | No — preserve historical checkpoint | Later lifecycle/software/agility sources remain unstudied |
| SAE ARP4754B:2023 | CLAUSE STUDY REVIEWED | Civil-aviation governance/profile extensions to V0–V12 | Historical aviation-profile extension already represented in v0.2 | EXTEND — historical aviation-profile checkpoint | `../standard_notes/sae_arp4754b.md`; `five_source_consistency_gap_review.md` | REVIEWED | No — profile boundary retained | Item-level objectives and certification authority remain outside current basis |
| SAE ARP4761A:2023 | CLAUSE STUDY REVIEWED | Safety Assessment Process View and aviation inputs to V10–V12 | Historical aviation-profile extension already represented in v0.2 | EXTEND — historical aviation-profile checkpoint | `../standard_notes/sae_arp4761a.md`; `five_source_consistency_gap_review.md` | REVIEWED | No — profile boundary retained | Generic safety/assurance sufficiency and authority remain open |
| ISO/IEC/IEEE 12207:2026 | SOURCE ACQUIRED; CLAUSE STUDY PENDING; 2017 HISTORICAL DEPENDENCY OPEN | Software-lifecycle foundation; 15026-4 software view; 24748-3 compatibility | Potential software-process/orchestration impact only | DEFERRED — pending clause study | Acquired source fingerprint only; no clause locator | NOT STARTED | Undetermined | 12207:2017→2026 process-location and semantic mapping remains `NOT DETERMINED` without the historical text |
| ISO/IEC/IEEE 24748-3:2020 | SOURCE ACQUIRED; CLAUSE STUDY PENDING; 12207:2017→2026 COMPATIBILITY OPEN | LC-G03/LC-G04; software-lifecycle and ISO-G07 candidate dimensions | Potential software-process application and information-item impact only | DEFERRED — pending clause study | Source fingerprint only; no clause locator | NOT STARTED | Undetermined | Source-native study may proceed; historical mapping remains `NOT DETERMINED` |
| ISO/IEC/IEEE 24748-4:2026 | SOURCE ACQUIRED; CLAUSE STUDY PENDING | V0; planning/governance information items; LC-G04/ISO-G07C | Potential SEMP/planning information-item impact only | DEFERRED — pending clause study | Source fingerprint only; no clause locator | NOT STARTED | Undetermined | Must be studied before final architecture synthesis; overlap with 15289/16326 open |
| ISO/IEC/IEEE 24748-5:2017 | SOURCE ACQUIRED; CLAUSE STUDY PENDING; OVERLAP REVIEW REQUIRED | Software planning information items; LC-G04/ISO-G07C | Potential software-plan and information-item impact only | DEFERRED — pending overlap and clause study | Source fingerprint only; no clause locator | NOT STARTED | Undetermined | 12207/15289/16326 overlap unresolved |
| ISO/IEC/IEEE 24748-6:2023 | SOURCE ACQUIRED; CLAUSE STUDY PENDING | Integration information items; LC-G04/ISO-G07 candidate dimensions | Potential integration-information assignment impact only | DEFERRED — pending clause study | Source fingerprint only; no clause locator | NOT STARTED | Undetermined | Relationship to current V-elements and 15289 taxonomy unstudied |
| ISO/IEC/IEEE 24748-8:2019 | METADATA VERIFIED; FORMAL REVISION WATCH; CLAUSE STUDY DEFERRED | LC-G01/LC-G02; domain review/gate abstraction only | Potential defence-profile review/audit patterns; no direct Generic Core impact | DEFERRED — await published replacement and source decision | Metadata only; FDIS excluded as normative basis | NOT STARTED | Undetermined | Cross-domain abstraction, current-edition acquisition and replacement timing open |
| ISO/IEC/IEEE 24748-10:2026 | SOURCE ACQUIRED; CLAUSE STUDY PENDING; REQUIRED BEFORE ARCHITECTURE FREEZE | LC-G03/ISO-G05; iteration, re-entry, tailoring and dynamic-environment dimensions | Potential iteration/re-entry/tailoring impact only | DEFERRED — pending clause study | Source fingerprint only; no clause locator | NOT STARTED | Undetermined | Must be disposed before architecture freeze; no reduction of evidence or gate obligations permitted |

## Planned-task candidate-impact preregistration

Pre-registration creates a common disposition entry point but no architecture conclusion. Every row remains `DEFERRED`; `Expected evidence` describes the research question, not an anticipated result.

| Task / source | RQ | Innovation candidate | Affected gap / V-ID | Expected evidence | Status | Migration trigger | Reviewer |
|---|---|---|---|---|---|---|---|
| 001 / ISO 15289 | RQ1/RQ5/RQ7 | INN-T2/T3/I1 | ISO-G07/B/C; V0–V12 information I/O | information-item/content/document boundaries and schema non-answers | DEFERRED | reviewed MODIFY/SPLIT/MERGE/DEPRECATE proposal | independent normative + architecture reviewer |
| 002 / ISO 9646 | RQ3/RQ5/RQ8 | INN-T2/T3/M4/I2 | ISO-G04/G07; V2–V8/V11 | capability, test-purpose, ATS/ETS, verdict/report/claim relations | DEFERRED | Oracle or conformance-boundary incompatibility | independent conformance + architecture reviewer |
| 003 / ISO 15026-1 | RQ4/RQ5 | INN-T1/T3 | ISO-G03B/G07A; V11 | assurance/reasoning/evidence vocabulary | DEFERRED | current vocabulary changes assurance/evidence semantics | independent assurance reviewer |
| 004 / ISO 15026-4 | RQ2/RQ4/RQ5 | INN-T1/T3/M1 | ISO-G03B/G05; V9–V12 | lifecycle assurance, change and re-assurance | DEFERRED | reviewed lifecycle/change incompatibility | independent assurance + lifecycle reviewer |
| 005 / ISO 12207 | RQ1–RQ5/RQ7 | INN-T1/T2/T3/A1/M1/M2/M4/I2 | LC-G03/G04; ISO-G03B/G05/G06/G07; V0–V12 | current software lifecycle and Verification process relations | DEFERRED | reviewed process/topology/information incompatibility | independent lifecycle + architecture reviewer |
| 006 / ISO 29119-1 | RQ3/RQ5/RQ7 | INN-T2/M3/M4/I2 | ISO-G02B/G04/G07; V2–V8 | current test-model ontology and term collisions | DEFERRED | current terms conflict with candidate ontology | independent software-testing reviewer |
| 007 / ISO 29119-2 | RQ2/RQ3/RQ5 | INN-A1/M1/M2 | LC-G03; ISO-G05/G06; V0–V12 | process iteration, re-entry and completion boundaries | DEFERRED | reviewed topology/closure incompatibility | independent process + architecture reviewer |
| 008 / ISO 29119-3 | RQ5/RQ7 | INN-T3/I1 | ISO-G07/B/C; V0–V12 information I/O | information-item content and schema limitations | DEFERRED | reviewed information-model incompatibility | independent information-model reviewer |
| 009 / ISO 29119-4 | RQ3/RQ4/RQ6 | INN-M3/M4/A3 | ISO-G02B/G03B/G04; V3–V5/V11 | technique, coverage and pattern eligibility | DEFERRED | reviewed coverage/Oracle/pattern incompatibility | independent testing + patterns reviewer |
| 010 / IEEE 1012 | RQ2–RQ5/RQ8 | INN-T1/A1/M1/A3 | ISO-G01/G03B/G05; ARP-G01; V0–V12 | integrity/task/independence/sufficient-evidence controls | DEFERRED | reviewed rigor/topology incompatibility | independent V&V assurance reviewer |
| 011 / ISO 15026-3 | RQ3/RQ4/RQ5 | INN-T1/A1 | ISO-G03B; ARP-G01; V0/V11 | integrity-level claim/determination/approval | DEFERRED | reviewed level/rigor semantic incompatibility | independent assurance reviewer |
| 012 / ISO 24748-4 | RQ2/RQ3/RQ5 | INN-A1/M1/M2 | LC-G04/ISO-G07C; V0 | SEMP planning and ownership inputs | DEFERRED | reviewed V0/planning ownership change | independent planning + architecture reviewer |
| 013 / ISO 24748-3 | RQ2/RQ3/RQ5 | INN-A1/M1/I2 | LC-G03/G04; software profile | application/tailoring guidance and bounded version map | DEFERRED | reviewed application/process incompatibility | independent lifecycle reviewer |
| 014 / ISO 24748-5 | RQ2/RQ3/RQ5/RQ7 | INN-A1/I1 | LC-G04/ISO-G07C; V0 | software planning/process/content ownership | DEFERRED | reviewed plan/schema ownership change | independent planning reviewer |
| 015 / ISO 24748-6 | RQ2/RQ3/RQ5 | INN-A1/M1/M3 | LC-G04/ISO-G05/G07; V6–V12 | integration interfaces, re-entry and evidence boundaries | DEFERRED | reviewed integration/topology incompatibility | independent integration + architecture reviewer |
| 016 / ISO 24748-10 | RQ2/RQ8 | INN-A1/M1/A3 | LC-G03/ISO-G05; V0–V12 topology | iteration/re-entry counterexamples and evidence continuity | DEFERRED | fixed/linear topology falsified | independent agility + architecture reviewer |
| 017 / ISO 24748-8 watch | none | future INN-A3/M2 | LC-G01/G02 | metadata trigger only; no clause evidence | DEFERRED | none until a new clause-study task exists | repository-governance reviewer |
| 018 / ISO 24641 | RQ3/RQ5/RQ7/RQ8 | INN-T3/M5/I1 | ISO-G08/G07; V4/V7/V8/V11 | model/tool credibility, reproducibility and admissibility | DEFERRED | reviewed model-evidence incompatibility | independent MBSE + assurance reviewer |
| 019 / ISO 15939 | RQ3/RQ4/RQ5 | INN-T1/T3/M3 | ISO-G02B/G03B; V8/V11 | measurement/product-quality versus sufficiency | DEFERRED | reviewed metric/evidence semantic change | independent measurement reviewer |
| 020 / ISO 16326 | RQ2/RQ5/RQ7 | INN-A1/M2 | ISO-G06/G07C/LC-G04; V0/V12 | project controls, authority and final planning ownership | DEFERRED | reviewed authority/closure incompatibility | independent project-governance reviewer |
| 021 / ISO 29148 mapping | RQ1/RQ3/RQ7 | INN-T2/I1 | REQ-G01/G02/ISO-G07C; V1/V2 | old/current locator mapping and framework-chain qualification | DEFERRED | reviewed mapping changes adopted semantics | independent requirements reviewer |
| 022 / cross-standard synthesis | RQ1–RQ8 | INN-T1–INN-I2 | all open gaps; V0–V12 | conflict, silence, RQ and candidate-disposition ledgers | DEFERRED | reviewed cross-standard migration proposal | independent research-design + architecture reviewer |

## Governance rules

- Stable V-identifiers do not make current semantics immutable.
- A source may affect multiple V-elements or dimensions, but every impact must retain source and review provenance.
- `MODIFY`, `SPLIT`, `MERGE` and `DEPRECATE` require before/after semantics, compatibility analysis and a migration note before approval; silent reinterpretation or retirement of a stable V-ID is prohibited.
- `EXTEND` requires an explicit compatibility statement for every affected existing V-element.
- `CONFIRM` and `NO-IMPACT` require a reviewed locator and a disposition rationale; source metadata or silence is insufficient.
- `DEFERRED` records insufficient evidence, dependency or review and is never an architecture conclusion.
- Five-source rows record historical reviewed impact only and do not reopen or rewrite v0.2 conclusions.
- Candidate rows must remain `DEFERRED` until clause study and independent review support another disposition.
- Architecture maturity can move from `OPEN-CANDIDATE` to `REVIEWED-PROVISIONAL` only through the roadmap's architecture-synthesis gate.
