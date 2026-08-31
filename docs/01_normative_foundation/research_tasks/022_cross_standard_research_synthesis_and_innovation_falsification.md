---
title: Cross-Standard Research Synthesis and Innovation Falsification Task Specification
status: planned
version: 0.6
baseline: post-v0.2
owner: research
last_updated: 2026-08-24
task_type: cross-standard-synthesis
research_questions: [RQ1, RQ2, RQ3, RQ4, RQ5, RQ6, RQ7, RQ8]
innovation_candidates: [INN-T1, INN-T2, INN-T3, INN-A1, INN-A2, INN-A3, INN-M1, INN-M2, INN-M3, INN-M4, INN-M5, INN-I1, INN-I2]
contribution_modes: [supported, qualified, falsified, open]
source_population: reviewed-current-and-legacy-records
dependencies:
  - README.md
  - ../standards_baseline.md
  - ../normative_gap_matrix.md
  - ../consolidation/architecture_impact_register.md
  - ../../00_overview/research_baseline_v0.2.md
  - ../consolidation/five_source_consistency_gap_review.md
  - ../reviews/consolidated_v02_pr7_pr8_integration_review.md
  - ../reviews/iso_29148_15026_2_independent_review_packet.md
  - ../../00_overview/research_questions.md
  - ../../00_overview/innovation_statement.md
  - ../../00_overview/research_scope.md
downstream_closure:
  - "Architecture synthesis: reviewed V0–V12 impact dispositions and migration proposals"
  - "Literature/patent/practice search: independently execute novelty questions produced here"
  - "Information architecture: schema/metamodel/automation work only after the synthesis gate"
  - "RQ8 empirical closure: docs/08_validation and the ARINC 615A, UAV FMS and LLM service instance projects"
---

# Cross-Standard Research Synthesis and Innovation Falsification Task Specification

## Control record

| Field | Value |
|---|---|
| Order / priority | 22 / synthesis after independently reviewed source packages |
| Baseline status | `PLANNED; INPUT DATASETS PENDING; ARCHITECTURE FREEZE PROHIBITED` |
| Source | Reviewed handoff datasets from Tasks 001–021 and existing reviewed v0.2/29148/15026-2 sources; no new standard text is interpreted here |
| Layer / trigger | Cross-standard synthesis / RQ answer and innovation-candidate falsification gate |
| Initial impact | `DEFERRED — source studies, synthesis and independent review pending` |

## Research orientation

执行本任务前必须读取本节与 frontmatter dependencies，并把工作边界固定为 `cross-standard-synthesis`。本任务不进入任何 target source、不创建新 clause interpretation，也不把未评审 note 或 metadata-watch record 当作内容证据。

### Task purpose and research attitude

把 independently reviewed clause/mapping records 综合为 RQ1–RQ7 的受边界答案、RQ8 validation-readiness handoff、candidate falsification ledger、conflict/silence register 与 Architecture Impact proposals。综合必须允许 reviewed counterevidence 改变框架；source silence、unavailable population 或 schema failure 保持 `OPEN`，不得被填补或转化为 novelty claim。

### Reviewed-input population entry

输入 population 包含两类：一是 Tasks 001–016、018–021 未来生成并通过独立评审的 README common records；二是本任务 Stage 0 将七项既有 reviewed sources 从 legacy artifacts 无损迁移得到、并再次独立复核的 normalized records。Task 017 `metadata-watch` records 只控制 availability/edition boundary，不进入内容综合。执行前冻结 task/artifact version、commit、review disposition，验证 schema、枚举、locator、RQ/candidate coverage 与 downstream closure owner；不合格、provisional 或缺失记录进入 quarantine/open register。

### Research questions and innovation candidates

本任务可形成 RQ1–RQ7 的 standards-evidence draft answers，但对 RQ8 只能形成 validation readiness and empirical handoff，状态固定为 `OPEN`。RQ8 的最终回答与关闭只能来自 ARINC 615A、无人机飞管系统和 LLM 服务三个实例的受控评价结果。每个 RQ1–RQ7 answer 必须显示 support、conflict/counterexample、silence、population limitation 与 residual gap；每个 INN-T1–INN-I2 只允许综合为 `SUPPORTED / QUALIFIED / FALSIFIED / OPEN`，这些不是 novelty verdict。

### Synthesis evidence hierarchy

1. independently reviewed current-task common records and independently re-reviewed normalized legacy records with valid provenance;
2. reviewed cross-source mapping records and controlled conflict/non-equivalence findings;
3. reviewed practice-comparison records kept outside the normative population;
4. framework interpretation, candidate claim and architecture proposal.

不得回到 PDF 修补缺失字段；不合格输入退回其 source-task owner。来源数量不能投票，低层级 synthesis 不能覆盖 source-native force。

### Durable synthesis interface

输出是自包含的 `synthesis-disposition` dataset，保存输入 record IDs/population、强反机制、disposition、claim delta、residual gap、layer right 与 review status。后续 architecture gate 只消费该 dataset 和 locator-backed reviewed inputs，不依赖聊天历史，也不把 synthesis record 冒充 clause evidence。

### Core synthesis principles

1. `Reviewed evidence -> cross-source interpretation -> bounded answer/disposition -> architecture proposal` 四层分离；
2. 先验证 input population/schema，再综合；
3. 冲突、反例、ambiguity 与 silence 不得平均掉；
4. standards silence 不证明 novelty；
5. Task 022 只提出 Architecture Impact，不冻结 V0–V12、schema、metamodel、state machine 或 automation interface；
6. 任何不完整 population 都必须带明确 `OPEN` 与 closure owner。

## Objective

Normalize all legacy reviewed evidence into the common schema, then convert the reconciled reviewed population into auditable draft answers for RQ1–RQ7, an `OPEN` RQ8 validation-readiness handoff, a falsification ledger for every controlled innovation candidate, and bounded Architecture Impact proposals. This task does not prove novelty, replace independent literature/patent/practice search or silently turn framework synthesis into a standard-native rule.

## Preliminary mapping hypotheses

以下是 synthesis hypotheses，不是标准条款假设。Stage 1 先冻结 independently reviewed input population 并通过 README schema validation；在综合前补充 `agent-derived from reviewed population` 行。最终报告不得删除任何假设，并逐行给出 `CONFIRMED / QUALIFIED / CORRECTED / FALSIFIED / NOT ADDRESSED`、input record IDs、理由与 synthesis effect。

| ID | Preliminary hypothesis | Basis type | Required test | Prohibited inference |
|---|---|---|---|---|
| H1 | 同名对象跨标准可能 equivalent/broader/narrower/overlapping/conflicting/not determined | cross-standard ontology discipline | 逐对象比较 purpose/relations/lifecycle/authority | 不得按名称或来源票数等价 |
| H2 | RQ1–RQ7 draft answers 必须同时保留 support、conflict、silence 和 residual gap；RQ8 只形成 readiness handoff | RQ synthesis/empirical boundary | 对 RQ1–RQ7 建立完整 population record，对 RQ8 建立 instance-claim-metric matrix | 不得平均掉反例和沉默，也不得以标准证据替代实例结果 |
| H3 | 每个 INN candidate 都可能被更早标准机制 falsify 或 qualify | innovation register | 执行 strongest-countermechanism test | 不得把 standards silence 当 novelty |
| H4 | Generic promotion 需要 source authority、cross-domain counterexample 和 abstraction rights | research_scope ladder | 记录 layer decision 和 prohibited generalization | profile similarity 不足以进入 Generic |
| H5 | reviewed practice-comparison records 可提供 context/counterexample，但不进入 normative clause dataset | practice-source boundary | 单列 practice comparison population | 不得关闭 normative gap |
| H6 | synthesis 只能提出 Architecture Impact，不能自动 freeze V0-V12/schema/metamodel | architecture gate | 输出 migration-ready proposals 并停在 review | 完成 Task 022 不等于 controlled baseline |
| H7 | legacy reviewed notes 可以通过 provenance/schema migration 接入 common records，但缺失字段必须保持 `not-determined` | F-06 migration gate | 枚举七项 established sources、逐命题映射并独立复核 | 不得重读 PDF、猜测字段或静默排除 established basis |
| H8 | RQ6 目前只有 Task 009 是直接 Verification Technique source；Task 018 仅支持 pattern engineering/reuse governance | RQ6 source-role audit | 分开统计 direct-technique 与 supporting-pattern sources | 不得用 pattern 术语关闭第二直接来源缺口 |

## Entry gate

1. freeze the complete seven-source legacy reviewed-evidence inventory below and the complete set of independently reviewed Task 001–021 common records available at execution time;
2. complete the legacy normalization package and obtain its independent review before any legacy row enters synthesis;
3. identify every established-basis occurrence in the v0.2 baseline, standards map, terminology, gap matrix, five-source consolidation and 29148/15026-2 registers; map it to a normalized record or an explicit justified quarantine row;
4. identify missing, provisional or `not-determined` fields/populations before synthesis and assign a downstream closure owner;
5. record exact source/task/artifact versions, commit locators and review dispositions;
6. do not treat Task 017 metadata as clause evidence;
7. do not resolve historical-version rows that lack controlled old-edition text;
8. permit partial synthesis only when every conclusion states its incomplete population and cannot be mistaken for final closure; RQ8 always remains `OPEN` until empirical closure.

## Legacy reviewed-evidence normalization package

This Stage 0 package is a provenance/schema migration, not a new clause study. It shall enumerate and normalize every material proposition from all sources already marked `CLAUSE STUDY REVIEWED` in `standards_baseline.md` before the v0.6 common schema existed.

### Controlled legacy source inventory

| Reviewed source | Authoritative legacy artifacts | Artifact version | Controlled commit/review point |
|---|---|---|---|
| ISO/IEC/IEEE 15288:2023 | `../standard_notes/iso_15288.md`; `../reviews/iso_15288_informal_review.md`; `../consolidation/five_source_consistency_gap_review.md` | note v0.3; five-source consolidation v0.3 at frozen tag / current reviewed v0.4 | `research-baseline/v0.2` at `357ad14ffc4e59abd071cb794912eb949a6ae6cf` |
| ISO/IEC/IEEE 24748-1:2024 | `../standard_notes/iso_24748_1.md`; `../reviews/iso_24748_1_informal_review.md`; five-source consolidation | note v0.4; five-source consolidation v0.3 at frozen tag / current reviewed v0.4 | `research-baseline/v0.2` at `357ad14ffc4e59abd071cb794912eb949a6ae6cf` |
| ISO/IEC/IEEE 24748-2:2024 | `../standard_notes/iso_24748_2_targeted_review.md`; `../reviews/iso_24748_2_arp4754b_internal_review.md`; `../reviews/ISO-24748-2--SAE-ARP4754B-External-Informal-Review.md`; `../consolidation/five_source_consistency_gap_review.md` | note v0.1; five-source consolidation v0.3 at frozen tag / current reviewed v0.4 | `research-baseline/v0.2` at `357ad14ffc4e59abd071cb794912eb949a6ae6cf` |
| SAE ARP4754B:2023 | `../standard_notes/sae_arp4754b.md`; `../reviews/iso_24748_2_arp4754b_internal_review.md`; `../reviews/ISO-24748-2--SAE-ARP4754B-External-Informal-Review.md`; `../consolidation/five_source_consistency_gap_review.md` | note v0.2; five-source consolidation v0.3 at frozen tag / current reviewed v0.4 | `research-baseline/v0.2` at `357ad14ffc4e59abd071cb794912eb949a6ae6cf` |
| SAE ARP4761A:2023 | `../standard_notes/sae_arp4761a.md`; `../reviews/sae_arp4761a_internal_review.md`; `../reviews/pr_4_arp4761a_external_review.md`; `../consolidation/five_source_consistency_gap_review.md` | note v0.2; five-source consolidation v0.3 at frozen tag / current reviewed v0.4 | `research-baseline/v0.2` at `357ad14ffc4e59abd071cb794912eb949a6ae6cf` |
| ISO/IEC/IEEE 29148:2018 | `../standard_notes/iso_iec_ieee_29148_2018_clause_study.md`; `../consolidation/clause_evidence_register_29148_15026_2.md`; `../consolidation/object_promotion_disposition_register_29148_15026_2.md`; `../consolidation/requirements_to_assurance_crosswalk.md`; `../reviews/iso_29148_15026_2_independent_review_packet.md`; `../reviews/consolidated_v02_pr7_pr8_integration_review.md` | note v0.1 / post-v0.2 reviewed delta | reviewed lineage `40018f996c746034092a7add81d1ba5f2d21349c` → `1028e35dcfdf9e5381674fc5dd491460c0ac5fd1` → `3359927286a39411ccb0e5f6dd34883702eb3ece`; merged at `658e3cfcee1d66147c6cbf2d048fc1d46a846f14` |
| ISO/IEC/IEEE 15026-2:2022 | `../standard_notes/iso_iec_ieee_15026_2_2022_clause_study.md`; `../consolidation/clause_evidence_register_29148_15026_2.md`; `../consolidation/object_promotion_disposition_register_29148_15026_2.md`; `../consolidation/requirements_to_assurance_crosswalk.md`; `../reviews/iso_29148_15026_2_independent_review_packet.md`; `../reviews/consolidated_v02_pr7_pr8_integration_review.md` | note v0.2 / post-v0.2 reviewed delta | reviewed lineage `40018f996c746034092a7add81d1ba5f2d21349c` → `1028e35dcfdf9e5381674fc5dd491460c0ac5fd1` → `3359927286a39411ccb0e5f6dd34883702eb3ece`; merged at `658e3cfcee1d66147c6cbf2d048fc1d46a846f14` |

At execution time, reconcile this table against `standards_baseline.md`. A newly reviewed source must be added; a listed source may not be removed merely because its legacy format is inconvenient.

### Normalization mapping and loss control

For each material legacy proposition create one adapter row that preserves:

| Field | Required content |
|---|---|
| `legacy_record_id` | stable ID scoped to source/artifact |
| `legacy_source` | canonical standard and edition |
| `legacy_artifact` | exact repository path, artifact version and controlled commit |
| `legacy_locator` | locator exactly as reviewed; never silently modernized |
| `original_reviewed_proposition` | faithful proposition already present in the reviewed artifact; no new interpretation |
| `normalized_record_id` | linked 18-field README record ID |
| `normalization_status` | `ADAPTED` / `ADAPTED WITH NOT-DETERMINED` / `QUARANTINED` |
| `missing_fields` | every field not recoverable from the legacy artifact |
| `closure_owner` | source-specific future review or mapping task for each unresolved field |
| `normalization_review` | independent reviewer, reviewed population/commit and disposition |

Populate the 18-field record only from the legacy artifact and its recorded review provenance. Preserve `legacy locator → original reviewed proposition → normalized record` traceability. If `source_class`, `source_kind`, `modality`, physical page, conditions, candidate test or another field cannot be determined without returning to the PDF or making a new interpretation, write `not-determined`, set `normalization_status=ADAPTED WITH NOT-DETERMINED` or `QUARANTINED`, and name a closure owner. Do not infer missing values from surrounding prose.

### Completeness and review gate

Build a population ledger across every proposition used by `research_baseline_v0.2.md`, `standards_map.md`, `terminology.md`, the gap matrix's established clause basis, `five_source_consistency_gap_review.md`, and the 29148/15026-2 consolidation registers. Every occurrence shall point to a normalized record or a justified quarantine row. The adapter output is written to `../consolidation/legacy_reviewed_evidence_normalization_register.md` and receives a separate independent-review packet. Until that review passes, normalized rows are ineligible for Task 022 synthesis. No synthesis may claim `population reconciled` while any established-basis source or occurrence is absent, silently dropped, or quarantined without an explicit reason and closure owner.
## Research contribution contract

For RQ1–RQ7, the task shall combine supporting, conflicting and silent sources; identify the strongest competing explanation; distinguish source-native requirements from interpretation and framework synthesis; and state what evidence would change the answer. For RQ8 it shall not draft a substantive answer: it only prepares the controlled empirical handoff described below and retains `OPEN`. For each candidate it shall decide only `SUPPORTED`, `QUALIFIED`, `FALSIFIED` or `OPEN`, with direct links to the underlying `SUPPORT/QUALIFY/FALSIFY/NO EVIDENCE` records.

## Mandatory synthesis packages

0. **Legacy reviewed-evidence normalization:** execute the seven-source adapter, loss/quarantine ledger, completeness reconciliation and independent-review gate before synthesis.
1. **RQ1 normative foundation:** source/layer/authority matrix; direct normative basis versus guidance, profile, framework synthesis and project practice.
2. **RQ2 lifecycle:** process relation/topology matrix including iteration, concurrency, recursion, re-entry, change and closure; linear interpretations receive explicit counterexample tests.
3. **RQ3 strategy:** Level/Method/Technique/Environment/Oracle/Coverage/Evidence input, constraint, choice and rationale matrix; separate available taxonomy from a selection algorithm.
4. **RQ4 sufficiency:** separate coverage, result quality, evidence credibility, argument adequacy, residual uncertainty and authority decision; source volume cannot close sufficiency.
5. **RQ5 evidence/claim:** typed `Result → Evidence Item → Argument → Claim` alignment, provenance and non-equivalence matrix.
6. **RQ6 patterns:** keep Task 009 as the direct Verification Technique taxonomy; use Task 018 only for supporting pattern expression, variation, repository, reuse and promotion control; register the missing second independent direct Verification Technique source as a residual gap.
7. **RQ7 DBSE/MBSE:** identity, relation, state, provenance, configuration and constraint requirements plus a negative register of schema semantics not supplied by standards.
8. **RQ8 validation readiness and empirical handoff:** output only pending claims, an instance–claim–metric matrix, required data, observable measures, success/failure criteria and closure owners in `docs/08_validation` plus the ARINC 615A/UAV FMS/LLM service instance projects. Every row remains `OPEN`; standards source-family coverage is not empirical validation coverage.

## Candidate falsification tests

For each `INN-T1` through `INN-I2`:

1. state the candidate at its controlled version and weakest defensible scope;
2. identify standard mechanisms that could be equivalent, broader, narrower or conflicting;
3. compare purpose, objects, relations, lifecycle, decision authority, input/output and applicability—not labels alone;
4. record the strongest counterexample and whether it falsifies, qualifies or leaves the candidate open;
5. distinguish `standard gap`, `other standard already provides`, `framework synthesis`, `implementation choice` and `novelty question`;
6. generate literature, patent and industrial-practice search questions for every surviving strong claim.

No candidate becomes `novelty established` in this task. `SUPPORTED` means only that the controlled standards evidence supports the problem/need or framework relation.

## Negative findings and non-answers

The synthesis must retain silence and incompatibility rather than averaging them away. `NO EVIDENCE` cannot become support, a missing schema cannot prove a metamodel contribution, and profile-specific obligations cannot become Generic merely because several profile sources use similar words. Unavailable historical sources, unreviewed notes, unreviewed legacy-normalization rows and metadata-only watch results remain explicit gaps. Pattern-governance evidence cannot fill a missing direct technique-source population, and standards evidence cannot answer RQ8 without instance results.

## Generalization rights

Every proposed adoption receives exactly one layer: `Generic`, `Extension`, `Profile`, `Practice` or `No adoption`. Promotion to Generic requires at least two independent source families or one direct generic source plus a reviewed cross-domain counterexample test. Domain/profile material requires the abstraction ladder and cannot bypass independent review.

## Synthesis handoff dataset

### RQ answer record

| Field | Required content |
|---|---|
| RQ / sub-question | exact controlled question |
| Source population | included/excluded/provisional tasks and versions |
| Supporting evidence | reviewed record IDs and locators |
| Conflict/counterexample | strongest competing mechanism or domain exception |
| Silence | relevant `NO EVIDENCE` records |
| Draft answer | bounded proposition and confidence |
| Residual gap | evidence needed to change/close the answer |
| Adoption right | allowed layer or no adoption |

### RQ8 validation-readiness record

Task 022 shall not use the generic RQ answer record to imply an RQ8 answer. Emit one row per empirical claim:

| Field | Required content |
|---|---|
| `validation_claim` | exact framework claim still requiring empirical evaluation |
| `instance_owner` | ARINC 615A / UAV FMS / LLM service and controlled project/repository owner |
| `metric_or_observation` | completeness, traceability, repeatability, scalability or reusability measure |
| `required_data` | inputs, traces, evidence and configuration needed |
| `success_criterion` | preregistered evidence that would support the claim |
| `failure_criterion` | observation that would falsify or materially qualify the claim |
| `status` | fixed `OPEN` until controlled instance results are reviewed |
| `closure_owner` | `docs/08_validation` plus the named instance evaluation |

RQ8 can be answered or closed only after all three instance evaluations produce controlled, independently reviewed results. A standards-only synthesis can at most declare validation readiness.
### Innovation falsification ledger

| Field | Required content |
|---|---|
| Candidate/version | controlled INN ID and statement |
| Standard evidence | support/qualification/falsification record IDs |
| Equivalent mechanism test | purpose/object/relation/lifecycle/authority comparison |
| Disposition | SUPPORTED / QUALIFIED / FALSIFIED / OPEN |
| Claim delta | exact narrowing, split or retirement proposal |
| Novelty search question | literature/patent/practice query and population boundary |
| Review status | independent reviewer disposition |

### Cross-standard matrices

Produce a terminology alignment matrix, normative-force/layer matrix, conflict matrix, information-item ownership matrix, process/topology matrix and incompatible-items register. Similar names never establish equivalence; every aligned row needs a typed relation such as `equivalent`, `broader`, `narrower`, `overlapping`, `conflicting` or `not determined`.

## Architecture Impact gate

The controlled vocabulary is `CONFIRM / EXTEND / MODIFY / SPLIT / MERGE / DEPRECATE / NO-IMPACT / DEFERRED`. After synthesis, propose a substantive disposition for each affected V-ID/gap only where reviewed evidence supports it; otherwise retain `DEFERRED`, which is not an architecture conclusion. `MODIFY/SPLIT/MERGE/DEPRECATE` requires before/after semantics, affected artifacts, compatibility rule, migration steps and rollback/review conditions; `EXTEND` requires compatibility with existing V-elements; `CONFIRM/NO-IMPACT` requires a reviewed locator and rationale.

Task 022 may submit proposals but may not directly freeze V0–V12, executable schema, metamodel, state machine or automation contract. Architecture maturity can advance only through the separately reviewed roadmap gate.

## Repository deliverables

- create and independently review `../consolidation/legacy_reviewed_evidence_normalization_register.md` before legacy evidence enters synthesis;
- create `../consolidation/cross_standard_research_synthesis_and_innovation_falsification.md`;
- create or embed the RQ answer records, innovation ledger and required matrices;
- update `../consolidation/architecture_impact_register.md` only with reviewed or explicitly `DEFERRED` proposals;
- update `../normative_gap_matrix.md` candidate study/owner/RQ links without altering protected established basis/disposition/status absent reviewed clause evidence;
- update `../../00_overview/innovation_statement.md` only through controlled claim deltas, never novelty establishment;
- update roadmap, project-status.json, README and CHANGELOG with actual—not anticipated—state;
- create an independent-review packet covering population completeness, conflict handling, candidate dispositions, migrations and non-claims.

## No-overclaim rules

Do not count sources as votes, convert silence into novelty, infer universal semantics from a profile, close RQ4 from coverage alone, treat Task 018 as a second direct RQ6 technique source, answer RQ8 from standards evidence, merge Result/Evidence/Argument/Claim, or label framework synthesis as standard-native. Do not promote a candidate because its terminology is absent from the sources. Do not replace independent novelty search or multi-domain validation.

## Mandatory execution sequence

Freeze legacy/current input versions; enumerate and normalize every legacy reviewed proposition; independently review the adapter; validate all dataset schemas; reconcile source/RQ/candidate populations; build terminology and conflict matrices; draft each RQ answer with counterexamples; execute every candidate falsification test; classify layer rights; produce architecture proposals/migrations; run protected-field and provenance checks; prepare independent review; stop before architecture freeze or novelty claims.

### Reviewed-input validator and synthesis record controls

Task 022 shall validate every consumed current-task or independently re-reviewed normalized-legacy clause/mapping record against the authoritative README common schema below. Field names and enums are exact; a missing field, invalid enum or absent independent-review disposition quarantines the record rather than authorizing a source reread:

| Field | Required content |
|---|---|
| `record_type` | `clause-evidence` / `mapping-evidence` |
| `source_locator` | exact clause/table/figure/annex identifier plus physical PDF page; mapping records may carry a controlled locator pair |
| `source_class` | `normative` / `informative` |
| `source_kind` | `requirement` / `recommendation` / `permission` / `definition` / `descriptive` / `note` / `example` / `annex-guidance` |
| `modality` | `shall` / `should` / `may` / `descriptive` / `not-applicable` |
| `proposition` | faithful short paraphrase; no substantial quotation |
| `object_relation` | source-native object and relation |
| `conditions_applicability` | applicability, tailoring, lifecycle, conformance and stated conditions |
| `rq_contribution` | RQ ID and exact task sub-question |
| `candidate_test` | candidate ID + `SUPPORT` / `QUALIFY` / `FALSIFY` / `NO EVIDENCE` + rationale |
| `framework_mapping` | V-ID/gap/concept + typed relation; interpretation separate |
| `layer` | `Generic` / `Extension` / `Profile` / `Practice` / `No adoption` |
| `unsupported_inference` | inference explicitly prohibited by the evidence |
| `version_dependency` | source-native locator, current counterpart and relation |
| `hypothesis_disposition` | hypothesis ID + `CONFIRMED` / `QUALIFIED` / `CORRECTED` / `FALSIFIED` / `NOT ADDRESSED` + rationale |
| `destination` | note/table/gap/register location receiving the conclusion |
| `downstream_closure_owner` | task/gate owning any provisional or unresolved cross-source closure |
| `confidence_review` | evidence quality, ambiguity and independent-review disposition |

Task 017 `metadata-watch` records and unreviewed/provisional records are excluded from the normative synthesis population and listed in the population-control register. Legacy records are eligible only after the adapter completeness review; `not-determined` fields and justified quarantine remain visible with closure owners.

Each synthesis output uses this dedicated subtype instead of manufacturing a clause record:

| Field | Required content |
|---|---|
| `record_type` | fixed value `synthesis-disposition` |
| `synthesis_subject` | RQ/sub-question, innovation candidate, V-ID, gap or terminology relation |
| `input_record_ids` | complete reviewed input set used for the disposition |
| `input_population` | included/excluded/quarantined tasks, versions and commit locators |
| `support_conflict_silence` | strongest support, countermechanism/conflict and relevant silence |
| `disposition` | `SUPPORTED` / `QUALIFIED` / `FALSIFIED` / `OPEN` |
| `bounded_answer_or_claim_delta` | exact answer or candidate narrowing/split/retirement |
| `residual_gap` | missing evidence and condition that could change the disposition |
| `layer` | `Generic` / `Extension` / `Profile` / `Practice` / `No adoption` |
| `architecture_proposal` | controlled Architecture Impact proposal or `DEFERRED` |
| `downstream_closure_owner` | later literature/patent/instance/architecture gate owner |
| `confidence_review` | synthesis confidence and independent-review disposition |

### Hypothesis reconciliation and self-contained report rule

After the reviewed-input population freeze and schema validation, extend the synthesis hypothesis ledger. Dispose every row after cross-source analysis using input record IDs and explicit population limits. The report must be self-contained for the later architecture gate; it may link to reviewed source records but may not reopen or silently reconstruct their source studies.

### Repository consistency checks

Before review handoff: run `git diff --check`; validate relative links/frontmatter/tables; reconcile source/study/review status; search stale `SOURCE ACQUIRED`, `IN PROGRESS`, `REVIEW PENDING`, `REVIEWED` and architecture-freeze wording; verify controlled Architecture Impact vocabulary; verify all hypotheses and promoted conclusions have dispositions/locators; verify no PDF, screenshot, OCR dump, full extraction, substantial quotation, licence identity, account, order, download timestamp, watermark or absolute user path is staged; verify provisional downstream rows retain their closure owner.

## Definition of done

Done requires a reconciled reviewed-input population in which all seven legacy reviewed sources and every established-basis occurrence are normalized or justifiably quarantined with closure owner, and the adapter has independent-review approval; RQ1–RQ7 answer records with support/conflict/silence/residual gaps; an RQ8 instance–claim–metric/data/success/failure handoff fixed at `OPEN`; all controlled candidates disposed as SUPPORTED/QUALIFIED/FALSIFIED/OPEN; all required cross-standard matrices; explicit layer rights; Architecture Impact proposals still DEFERRED until review; novelty-search questions for surviving claims; protected gap/V-ID fields unchanged unless separately authorized by reviewed evidence; clean link/front-matter/table/dependency/diff/privacy checks; and independent-review approval. Completion authorizes the next decision gate, not automatic architecture freeze or novelty establishment.
