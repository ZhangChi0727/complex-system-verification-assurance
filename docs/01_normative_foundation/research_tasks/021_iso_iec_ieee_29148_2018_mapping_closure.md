---
title: ISO/IEC/IEEE 29148:2018 Normative Research Task Specification
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

# ISO/IEC/IEEE 29148:2018 Normative Research Task Specification

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

执行本任务前必须先读取本节与 frontmatter dependencies，并带着明确的研究问题、候选反证路径和来源边界进入原文。任务不是一般性总结，也不是为当前框架寻找支持。

### Task purpose and research attitude

只关闭 reviewed 29148:2018 研究实际使用的 15288:2015 -> 2023 provenance/compatibility mapping，不重做 29148 全文研究或完整版本 delta。

本任务服务于 `research_scope.md` 的三层目标：产品无关 Verification Methodology -> Model-Based Verification Architecture -> 非产品化 Verification Platform 研究原型。标准明确规定的内容形成构建约束；标准没有回答的内容形成 gap 或 innovation-space observation。`Standard wins over current framework hypothesis`；标准沉默不得由 agent 补齐，也不得作为 novelty proof。

### Source-specific research entry

29148:2018 原文目录显示 requirements concepts、requirements construct/attributes、iteration/recursion、processes、verification/validation activities、management、information items/outlines/content；本任务只消费既有 reviewed study 中实际依赖这些内容的受控 population。

该结构说明研究入口，不构成条款结论。Agent 必须在 source gate 后建立完整 inventory，并允许实际条款内容修正本说明中的初始假设。

### Research questions carried by this task

- **RQ1**: 复杂系统 Verification 的规范性基础是什么？ 本任务只回答与本来源及其受控 scope 直接相关的子问题；完整答案由 Task 022 综合。
- **RQ3**: 如何系统确定 Level + Method + Technique + Environment + Oracle + Coverage + Evidence？ 本任务只回答与本来源及其受控 scope 直接相关的子问题；完整答案由 Task 022 综合。
- **RQ7**: DBSE Verification Workflow 如何形成机器可解释、可查询和可检查的 MBSE information model？ 本任务只回答与本来源及其受控 scope 直接相关的子问题；完整答案由 Task 022 综合。

### Innovation candidates under test

- **INN-T2** — typed Verification Basis -> Verification Obligation -> Strategy 的框架中间对象链。Falsification condition: 既有 standards/research 已定义等价 obligation 对象、typed basis 与生命周期关系。Non-claim: 不声称标准普遍从 requirement 直接跳到 test。执行时必须比较 purpose、objects、relations、lifecycle、authority 和 applicability，而不是只比较标签。
- **INN-I1** — 机器可读 verification metamodel 与非产品化研究原型。Falsification condition: 既有开源或研究平台提供等价模型和评价能力，或原型无法支持审计查询。Non-claim: 不把工程实现本身自动等同学术创新。执行时必须比较 purpose、objects、relations、lifecycle、authority 和 applicability，而不是只比较标签。

Tasks 001-021 只能返回 `SUPPORT / QUALIFY / FALSIFY / NO EVIDENCE`；Task 022 只能综合为 `SUPPORTED / QUALIFIED / FALSIFIED / OPEN`。任何任务都不能设置 `novelty established`。

### Evidence hierarchy

1. target-source normative provisions;
2. target-source informative material;
3. independently reviewed repository research on other normative sources;
4. directly checked practice-comparison sources;
5. framework hypotheses and research proposals.

低层级证据可以提出问题、比较维度或反例，但不得覆盖或替代高层级证据。Informative material 不得转成 requirement；reviewed note 不替代本任务原文研究；practice source 不生成 target-source clause record；framework hypothesis 不决定标准应当说什么。来源数量不能替代证据质量，禁止来源投票。

### Durable research interface

本任务产生的 reviewed note 是下游研究的耐久接口。执行者必须研究完整受控原文，独立评审者必须使用自己合法取得且指纹匹配的原文核验关键 locator；评审通过后，下游任务应只消费 note 中的 locator + faithful paraphrase + source class + object/relation + limitation + review disposition，而不重新进行同一标准的全文研究。研究笔记不得以“见原文”代替命题，也不取代正式标准。

### Core research principles

1. `Standard evidence -> interpretation -> framework implication -> proposal` 四层分离；
2. 先记录 source-native objects/relations/conditions，再映射 VAF；
3. 冲突、反例、ambiguity 和 `NO EVIDENCE IN THE REVIEWED SOURCE POPULATION` 必须可见；
4. standard silence 不证明 novelty，也不授权任意设计；
5. 只进行 locator-backed 的最小仓库变更；
6. V0-V12 保持 `OPEN-CANDIDATE`，不得在 source task 中冻结 schema、metamodel、state machine 或 automation interface。


## Objective

Close only the controlled 15288:2015→2023 dependency mapping used by the reviewed 29148 study, without reopening or repeating the full requirements-engineering clause study.

## Required questions

- Which cited 15288:2015 process/term locators have direct, moved, changed or absent counterparts in 15288:2023?
- Do any changes affect Requirement/Set, Verification Basis, Verification Criterion or obligation relations already adopted?
- Which mappings require errata, qualification or residual open status?

## Preliminary mapping hypotheses

以下是进入原文前的可证伪假设，不是预期答案。Stage 1 完成完整 clause/annex inventory 后、实质提取前，agent 必须补充 `agent-derived from inventory` 行。最终报告不得删除任何假设；每行必须给出 `CONFIRMED / QUALIFIED / CORRECTED / FALSIFIED / NOT ADDRESSED`、locator、理由和影响。

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

### Mapping record

| Field | Required content |
|---|---|
| Row ID | stable mapping identifier |
| Repository location | file/section or line anchor |
| 29148 locator | clause/page using or citing 15288:2015 |
| 2015 dependency | exact cited locator/concept as source-native provenance |
| 2023 counterpart | exact locator/concept or `none/not determined` |
| Relation | direct, moved/renamed, semantically changed, removed, split/merged, unclear |
| Effect | no impact, wording qualification, mapping correction, architecture impact |
| Action | exact file change or explicit no-change rationale |
| Confidence/review | evidence quality and reviewer disposition |

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

Every proposition used in a repository conclusion shall use the README common data contract. No column may be removed; use `none/not determined` where needed:

| Field | Required content |
|---|---|
| `source_locator` | exact clause/table/figure/annex plus physical PDF page |
| `source_class` | normative requirement / recommendation / permission / definition / informative / note / example / annex guidance |
| `proposition` | faithful short paraphrase; no substantial quotation |
| `object_relation` | source-native object and relation |
| `rq_contribution` | RQ ID and exact task sub-question |
| `candidate_test` | candidate ID + controlled disposition + rationale |
| `framework_mapping` | V-ID/gap/concept + typed relation; interpretation separate |
| `layer` | Generic / Extension / Profile / Practice / No adoption |
| `unsupported_inference` | inference explicitly prohibited by the evidence |
| `version_dependency` | source-native locator, current counterpart and relation |
| `confidence_review` | evidence quality, ambiguity and independent-review disposition |

Each source task shall additionally retain modality, conditions/applicability, hypothesis ID/disposition, destination and downstream closure owner where relevant. Practice-comparison prompts never enter the normative clause dataset.

### Hypothesis reconciliation and self-contained report rule

After the inventory, extend and freeze the working hypothesis ledger. After extraction and required mappings, dispose every preliminary and inventory-derived row. The note must define key terminology and carry enough locator-backed paraphrase and classification that a downstream task can consume reviewed conclusions without reopening the source. Independent source review still requires a legally obtained, fingerprint-matching original.

### Repository consistency checks

Before review handoff: run `git diff --check`; validate relative links/frontmatter/tables; reconcile source/study/review status; search stale `SOURCE ACQUIRED`, `IN PROGRESS`, `REVIEW PENDING`, `REVIEWED` and architecture-freeze wording; verify controlled Architecture Impact vocabulary; verify all hypotheses and promoted conclusions have dispositions/locators; verify no PDF, screenshot, OCR dump, full extraction, substantial quotation, licence identity, account, order, download timestamp, watermark or absolute user path is staged; verify provisional downstream rows retain their closure owner.

### Definition of done

Done requires an execution-time revision/priority decision; a reconciled 100% mapping population; exact 2015 and 2023 locators for every determinable row; explicit unresolved rows; all actions applied or justified; synchronized repository statuses; clean link/diff/provenance scans; and independent review approval. The existing 29148 study remains reviewed throughout unless a mapped change explicitly requires a controlled correction.
