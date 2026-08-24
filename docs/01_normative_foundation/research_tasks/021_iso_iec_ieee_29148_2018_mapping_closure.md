---
title: ISO/IEC/IEEE 29148:2018 Targeted Mapping Closure Task Specification
status: planned
version: 0.6
baseline: post-v0.2
owner: research
last_updated: 2026-08-24
task_type: mapping-closure
research_questions: [RQ1, RQ3, RQ7]
innovation_candidates: [INN-T2, INN-I1]
contribution_modes: [support, qualify, falsify, no-evidence]
source_population: bounded-dependencies
dependencies:
  - README.md
  - ../standard_notes/iso_iec_ieee_29148_2018_clause_study.md
  - ../reviews/iso_29148_15026_2_independent_review_packet.md
  - ../standard_notes/iso_15288.md
  - ../../00_overview/research_questions.md
  - ../../00_overview/innovation_statement.md
  - ../../00_overview/research_scope.md
downstream_closure:
  - "Task 021: targeted mapping closure after execution-time revision/priority recheck"
  - "Architecture synthesis: requirements-engineering dependency disposition"
---

# ISO/IEC/IEEE 29148:2018 Targeted Mapping Closure Task Specification

## Control record

| Field | Value |
|---|---|
| Order / priority | 21 / targeted residual dependency |
| Baseline status | `CLAUSE STUDY REVIEWED; 15288:2015→2023 VERSION MAPPING OPEN; FORMAL REVISION WATCH` |
| Source | `references/PDF/29148-2018.pdf`; 104 pages; SHA-256 `E8FB679F758AA078B290FB1849E288996D059968D5911ABD0E96A75C0539E6C8` |
| Revision control | Current published basis: 2018; Edition 3 DIS under development; official metadata last verified `2026-08-20` at https://www.iso.org/standard/94091.html; recheck before execution; DIS text prohibited; a published replacement requires an explicit retarget/priority decision |
| Layer / trigger | Generic methodological source / requirement-process dependency closure |
| Initial impact | `DEFERRED — targeted mapping review pending`; existing clause study remains reviewed |

## Research orientation

执行本任务前必须读取本节与 frontmatter dependencies，并把工作边界固定为 `mapping-closure`。本任务不重新进入 29148 全文研究；它只消费已独立评审的 29148 note/review packet、仓库中实际使用的 15288:2015 dependency occurrences，以及受控 15288:2015/2023 locator pair population。

### Task purpose and research attitude

只关闭 reviewed 29148:2018 研究实际使用的 15288:2015 -> 2023 provenance/compatibility mapping，不重做 29148 clause inventory，也不进行 15288 两版全文 delta。`Standard wins over current framework hypothesis` 仍适用：若受控 locator pair 显示语义变化，必须修正依赖结论；无法确定的行保持 `NOT DETERMINED`。

### Source-specific mapping entry

29148:2018 的 source-native findings 已由既有 reviewed note 固定。本任务的 analysis population 是仓库内每个 15288:2015 明示 locator、术语、paraphrased outcome/task 或隐含语义依赖；每个 occurrence 与受控 15288:2015/2023 counterpart 建立一条 mapping row。不得扩大为未被既有研究使用的完整 29148 或完整 15288 edition population。

### Research questions carried by this mapping

- **RQ1**：只检查既有 requirements-engineering normative basis 是否因 dependency version mapping 而被确认、限定或修正。
- **RQ3**：只检查 Requirement/Set、Verification Basis/Characteristic/Constraint/Criterion 链中受版本依赖影响的选择输入关系。
- **RQ7**：只检查受控映射是否改变机器可解释关系的 provenance 或 compatibility；不据此设计 schema。

### Innovation candidates under mapping test

- **INN-T2**：只针对 mapping population 中实际出现的 typed basis/criterion/obligation relations 检查等价、变化或不可判定；相同标题不构成等价。
- **INN-I1**：只记录版本映射对现有机器可读关系假设的影响；本任务不寻找新的 executable metamodel。

### Mapping evidence hierarchy

1. controlled ISO/IEC/IEEE 15288:2015 source locator and faithful source-native proposition;
2. reviewed ISO/IEC/IEEE 15288:2023 clause record and controlled source locator;
3. independently reviewed 29148:2018 note/review packet and its exact repository occurrence;
4. current framework interpretation and migration proposal.

缺少第 1 层时可以冻结 occurrence population，但 semantic relation 必须为 `not-determined`。既有 reviewed 29148 note 是 population source，不是重新研究 29148 的授权。

### Durable mapping interface

输出是自包含的 mapping report：每行保存 repository occurrence、历史 locator、当前 counterpart、typed relation、effect、action 与 review disposition。后续任务消费该报告，不重新研究 29148 全文；独立评审只核验受控 mapping population 与 locator pairs。

### Core mapping principles

1. `Historical provenance -> current counterpart -> compatibility effect -> repository action` 四层分离；
2. 保留 source-native 2015 locator，不机械替换为 2023；
3. 标题相同不证明语义等价；
4. population 外内容不得借本任务进入架构；
5. unresolved rows 保持显式 closure owner。

## Objective

Close only the controlled 15288:2015→2023 dependency mapping used by the reviewed 29148 study, without reopening or repeating the full requirements-engineering clause study.

## Required questions

- Which cited 15288:2015 process/term locators have direct, moved, changed or absent counterparts in 15288:2023?
- Do any changes affect Requirement/Set, Verification Basis, Verification Criterion or obligation relations already adopted?
- Which mappings require errata, qualification or residual open status?

## Preliminary mapping hypotheses

以下是 mapping hypotheses，不是条款研究答案。先冻结 reviewed 29148 artifacts 中 15288:2015 dependency occurrences 的完整 population，再于 semantic mapping 前补充 `agent-derived from population` 行；最终报告逐行给出 `CONFIRMED / QUALIFIED / CORRECTED / FALSIFIED / NOT ADDRESSED`、locator pair、理由与 effect。

| ID | Preliminary hypothesis | Basis type | Required test | Prohibited inference |
|---|---|---|---|---|
| H1 | 相同过程或术语标题不证明 15288:2015/2023 语义等价 | version-mapping discipline | 逐 occurrence 建立 old locator/current counterpart/relation | 不得机械替换 locator |
| H2 | Requirement/Set、Specified Characteristic/Constraint、Verification Criterion 关系可能受版本变化影响 | reviewed 29148 framework chain | 逐关系检查 direct/moved/changed/split/absent | 不得保护现有框架结论免于修正 |
| H3 | source-native 2015 citation 必须保留，同时增加 current 2023 mapping | provenance rule | 记录双 locator 和 effect | 不得删除历史来源真实性 |
| H4 | 没有受控 15288:2015 原文时语义 mapping 只能 NOT DETERMINED | hard source gate | 允许 population inventory，不允许 semantic closure | 不得用 INCOSE reproduced content 重建 normative baseline |
| H5 | 本任务的 DoD 不包括重新研究 29148 clauses | bounded-dependency scope | 只修改 row-authorized provenance statements | 不得借 mapping task扩大架构重写 |

## Required work and outputs

Create `../consolidation/iso_29148_2018_to_iso_15288_2023_targeted_mapping.md`; update only affected provenance statements; record `CONFIRM/MODIFY/NO-IMPACT/DEFERRED` with migration notes where needed; obtain independent review of the targeted mapping.

## Stop conditions

Do not rewrite source-native 2015 citations, redo the full 29148 study, close unrelated REQ/ISO gaps or silently change established semantics.

## Research contribution contract

This bounded mapping task answers RQ1/RQ3/RQ7 only for the reviewed 29148 study's actual 15288:2015 dependencies. It shall test the framework chain `Requirement/Set → Verification Basis → Specified Characteristic/Constraint → Verification Criterion → Verification Obligation` while separating standard-direct relations from framework synthesis.

## Candidate falsification tests

Test `INN-T2/I1` against every controlled historical/current locator pair. An equivalent chain or machine-readable model must be source-supported; same headings and inferred counterparts are not equivalence evidence.

## Negative findings and non-answers

Without the 15288:2015 source, every semantic mapping row remains `NOT DETERMINED` and the task cannot reach final DoD. Do not reopen the reviewed 29148 clause study or replace old locators.

## Generalization rights

Only reviewed mapping corrections may affect `Generic`; edition-specific provenance remains `Extension`; unresolved rows are `No adoption`.

## Synthesis handoff dataset

Emit the common record plus `repository_occurrence`, `2015_locator`, `2023_counterpart`, `relation`, `effect`, `framework_chain_role`, `direct_or_synthesized` and `review_disposition`.

## Detailed execution specification

### Execution outcome and strict scope

Produce a complete, independently reviewed mapping for every ISO/IEC/IEEE 15288:2015 dependency actually used by the existing 29148:2018 study. This is a provenance/compatibility closure task, not a second clause study of 29148 and not a full 15288 edition delta.

### Source and baseline gate

Reconfirm the 29148 source path, 104-page extent and SHA-256; confirm the reviewed 29148 study/review packet is unchanged; use the controlled ISO 15288:2023 source/study. Record the starting commit and enumerate every 2015 citation or semantic dependency in the 29148 study, maps, gap matrix, terminology and architecture artifacts.

Before execution, recheck the Edition 3 revision status and the queue priority. The controlled ISO/IEC/IEEE 15288:2015 text is a hard source gate: without it, enumerate the population but mark semantic mappings `NOT DETERMINED` and do not claim mapping completion. If a replacement has been formally published, stop and issue a retarget decision that determines whether this task still closes provenance for the reviewed 2018 study or whether a separate new-edition task takes precedence. Never use DIS text or silently transform this task into a new full clause study.

### Mapping population

The mapping population includes explicit clause/table/definition citations, inherited process names, paraphrased 2015 outcomes/tasks, terminology relations and any repository conclusion whose validity depends on 2015 semantics. Each occurrence receives a stable row identifier; no dependency may be silently excluded.

### Mapping record extension

Every row first implements the README common schema with `record_type: mapping-evidence`. Use `source_locator` for the controlled historical/current locator pair and `version_dependency` for its typed relation. Add only these mapping-specific fields:

| Field | Required content |
|---|---|
| `mapping_row_id` | stable mapping identifier |
| `repository_occurrence` | file/section or stable anchor using the 2015 dependency |
| `historical_locator` | exact 2015 locator/concept retained as source-native provenance |
| `current_locator` | exact 2023 counterpart or `not-determined` |
| `mapping_relation` | `direct` / `moved-renamed` / `semantically-changed` / `removed` / `split-merged` / `unclear` |
| `effect` | `no-impact` / `wording-qualification` / `mapping-correction` / `architecture-impact` |
| `action` | exact file change or explicit no-change rationale |

### Required analysis packages

Separately check terminology/definitions; requirements engineering processes/outcomes/tasks; stakeholder/system/software requirement information relations; traceability and verification/validation criteria; Requirement and Requirement Set identity/lifecycle conclusions; Verification Basis/Specified Characteristic/Constraint relations; Verification Criterion placement/cardinality; and all cross-standard/gap/architecture conclusions inherited from the reviewed 29148 work.

### Change discipline

Preserve every source-native 2015 locator where describing what 29148:2018 cites. Add a 2023 current-baseline mapping beside it. If semantics changed, update only the affected framework interpretation and provide a before/after/migration note. Unrelated improvements are out of scope and must be separately proposed.

### Repository deliverables

Create `../consolidation/iso_29148_2018_to_iso_15288_2023_targeted_mapping.md`; update affected provenance statements in the 29148 note, standards map, gap matrix and Architecture Impact Register; update baseline/HANDOFF/CHANGELOG; create an independent-review packet containing full population reconciliation and exact changed-file list.

### Required final answers

State whether each established Requirement/Set, Verification Basis and Verification Criterion conclusion is confirmed, qualified or modified; list unresolved mappings; state whether REQ-G01, REQ-G02 or ISO-G07C status changes; and confirm that no unrelated clause study was reopened.

### No-overclaim rules

Do not replace a historical citation with a 2023 locator, infer equivalence from identical headings, omit removed/split concepts, or claim the complete editions are equivalent. Do not change stable semantics without an Architecture Impact disposition and migration note.

### Mandatory execution sequence and report structure

Execute in this order: freeze the reviewed starting baseline; enumerate all 2015 dependencies; reconcile the population; map each row to 2023; classify effects; apply only row-authorized changes; run provenance/terminology sweeps; prepare independent review; stop without reopening unrelated research.

The mapping report shall contain: control record/source fingerprints; scope/exclusions; population-construction method; full dependency inventory; terminology mappings; process/outcome/task mappings; Requirement/Set findings; Verification Basis/Characteristic/Constraint findings; Verification Criterion findings; affected repository statements; gap/architecture dispositions and migrations; unresolved rows; exact delta; conclusions and handoff.

The review packet shall prove population completeness, sample every relation class, list all source-native citations protected, all modified semantics/files/statuses and all unresolved rows. Approval applies only to this targeted closure.

### Common evidence record and durable-handoff controls

Every mapping proposition used in a repository conclusion shall use the authoritative README common schema. No field may be removed; use `not-applicable` or `not-determined` where appropriate:

| Field | Required content |
|---|---|
| `record_type` | `clause-evidence` / `mapping-evidence`; this task emits `mapping-evidence` |
| `source_locator` | controlled historical/current clause/table/definition locator pair plus physical PDF pages |
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

### Hypothesis reconciliation and self-contained report rule

After freezing and reconciling the controlled dependency-occurrence population, extend the mapping hypothesis ledger and dispose every row after mapping. The report must preserve both locators, source-native provenance, typed relation, effect and review status so downstream work can consume it without reopening the 29148 clause study.

### Repository consistency checks

Before review handoff: run `git diff --check`; validate relative links/frontmatter/tables; reconcile source/study/review status; search stale `SOURCE ACQUIRED`, `IN PROGRESS`, `REVIEW PENDING`, `REVIEWED` and architecture-freeze wording; verify controlled Architecture Impact vocabulary; verify all hypotheses and promoted conclusions have dispositions/locators; verify no PDF, screenshot, OCR dump, full extraction, substantial quotation, licence identity, account, order, download timestamp, watermark or absolute user path is staged; verify provisional downstream rows retain their closure owner.

### Definition of done

Done requires an execution-time revision/priority decision; a reconciled 100% mapping population; exact 2015 and 2023 locators for every determinable row; explicit unresolved rows; all actions applied or justified; synchronized repository statuses; clean link/diff/provenance scans; and independent review approval. The existing 29148 study remains reviewed throughout unless a mapped change explicitly requires a controlled correction.
