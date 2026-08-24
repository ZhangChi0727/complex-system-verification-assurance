---
title: ISO/IEC/IEEE 24748-8 Revision Watch Task Specification
status: planned
version: 0.6
baseline: post-v0.2
owner: research
last_updated: 2026-08-24
task_type: metadata-watch
research_questions: []
innovation_candidates: [INN-A3, INN-M2]
contribution_modes: [no-evidence]
source_population: metadata-only
dependencies:
  - README.md
  - ../standards_baseline.md
  - ../../00_overview/research_questions.md
  - ../../00_overview/innovation_statement.md
  - ../../00_overview/research_scope.md
downstream_closure:
  - "A new separately numbered clause-study task after formal replacement publication and acquisition decision"
---

# ISO/IEC/IEEE 24748-8 Revision Watch Task Specification

## Control record

| Field | Value |
|---|---|
| Order / priority | 17 / revision watch, not current clause study |
| Baseline status | `METADATA VERIFIED; FORMAL REVISION WATCH; CLAUSE STUDY DEFERRED` |
| Source | No matching PDF in current inventory; 2019 remains the published edition, while the replacement FDIS is not a normative basis |
| Revision control | Current published basis: 2019; Edition 2 FDIS under development; metadata last verified `2026-08-20` at https://www.iso.org/standard/75405.html and https://www.iso.org/standard/91563.html; FDIS text prohibited as normative evidence |
| Layer / trigger | Domain assurance/application profile / defence review and audit abstraction |
| Initial impact | `DEFERRED — await published replacement and source decision` |

## Research orientation

执行本任务前必须先读取本节与 frontmatter dependencies，并带着明确的研究问题、候选反证路径和来源边界进入原文。任务不是一般性总结，也不是为当前框架寻找支持。

### Task purpose and research attitude

仅执行正式出版状态、source acquisition 和 retarget trigger 的受控监视；在合法取得正式原文前不进行 clause study、candidate disposition 或 Architecture Impact。

本任务服务于 `research_scope.md` 的三层目标：产品无关 Verification Methodology -> Model-Based Verification Architecture -> 非产品化 Verification Platform 研究原型。标准明确规定的内容形成构建约束；标准没有回答的内容形成 gap 或 innovation-space observation。`Standard wins over current framework hypothesis`；标准沉默不得由 agent 补齐，也不得作为 novelty proof。

### Source-specific research entry

当前 PDF inventory 中没有 ISO/IEC/IEEE 24748-8 正式原文。本任务的 source population 是官方 metadata 与仓库状态，不是标准条款。

该结构说明研究入口，不构成条款结论。Agent 必须在 source gate 后建立完整 inventory，并允许实际条款内容修正本说明中的初始假设。

### Research questions carried by this task

- 本任务不处置 RQ；它只维护 metadata/source gate。任何 RQ 贡献等待正式原文、独立 clause-study task 和 review。

### Innovation candidates under test

- **INN-A3** — profile pattern 经受控抽象阶梯进入 generic candidate 的机制。Falsification condition: 已有 profile-extension governance 提供等价 provenance、promotion gate 和跨域验证规则。Non-claim: 不把 criticality 或 model evidence 概念据为原创。本 revision-watch task 不得给出 candidate disposition。
- **INN-M2** — waiver、deviation、reopen、authority 与 scope state 的 Closure 状态模型。Falsification condition: 既有 lifecycle/change-control 标准已定义等价模型，或该模型不能稳定处理实例。Non-claim: 不把审批或基线状态本身主张为原创。本 revision-watch task 不得给出 candidate disposition。

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

Maintain an accurate publication/replacement watch and define the gate for a future defence-domain review/audit abstraction study.

## Preliminary mapping hypotheses

以下是进入原文前的可证伪假设，不是预期答案。Stage 1 完成完整 clause/annex inventory 后、实质提取前，agent 必须补充 `agent-derived from inventory` 行。最终报告不得删除任何假设；每行必须给出 `CONFIRMED / QUALIFIED / CORRECTED / FALSIFIED / NOT ADDRESSED`、locator、理由和影响。

| ID | Preliminary hypothesis | Basis type | Required test | Prohibited inference |
|---|---|---|---|---|
| H1 | 正式发布和受控原文取得是 clause study 的硬门禁 | revision-watch governance | 每个 watch cycle 核验 publication status、edition、identifier 和 acquisition | metadata 不得成为 clause evidence |
| H2 | 24748-8 可能与 technical review/audit、closure 或 lifecycle management gaps 相关 | research trigger hypothesis | 只登记潜在影响和 future questions | 不得给 INN-A3/M2 SUPPORT/QUALIFY/FALSIFY |
| H3 | draft/CD/DIS/FDIS 只能用于 revision metadata | source-control policy | 记录 stage/date/official locator | 不得解释 draft clauses |
| H4 | source acquisition 后应新建/retarget clause-study specification 并独立评审 | two-stage gate | 定义触发后的 required transition | 不得在 watch task 中静默开始研究 |

## Required actions

1. Periodically verify the official publication state without studying the FDIS text.
2. When a replacement is formally published, update metadata and decide whether to acquire it.
3. If acquired and triggered, create a new clause-study task focused on LC-G01/LC-G02 and cross-domain abstraction.
4. Preserve `Domain assurance/application profile`; no direct Generic Core promotion is allowed.

## Stop conditions

Do not acquire or analyze the FDIS for normative conclusions, generalize defence authority/gate rules, or start clause extraction under this watch task.

## Research contribution contract

This metadata-watch task does not answer an RQ and contributes no clause evidence. It only maintains publication state and the trigger for a future separately numbered defence-profile clause study.

## Candidate falsification tests

No innovation candidate may receive `SUPPORT`, `QUALIFY` or `FALSIFY` from this task. `INN-A3/M2` are future search targets only; every watch-cycle outcome is `NO EVIDENCE` for content claims.

## Negative findings and non-answers

Metadata, FDIS existence and publication timing say nothing about review/audit semantics, authority, closure or novelty. Do not inspect draft clauses.

## Generalization rights

All outputs are governance `No adoption`. A future published-source task must independently establish `Profile` findings before any abstraction.

## Synthesis handoff dataset

Emit only `catalogue_locator`, `access_date`, `publication_state`, `replacement_relation`, `source_acquisition_decision`, `trigger_disposition` and `content_evidence=none`.

## Detailed execution specification

### Nature of this task

This document is a publication-control runbook, not a clause-research authorization. Its purpose is to prevent a draft replacement or a defence-domain profile from silently becoming a Generic Core basis.

### Authoritative watch procedure

At each scheduled or research-triggered check:

1. consult official ISO/IEC/IEEE catalogue records and record access date and stable URL/reference;
2. capture published identifier, title, edition/date, lifecycle status and any replacement/withdrawal relation;
3. distinguish FDIS approval/publication workflow from an actually published standard;
4. compare official metadata with `../standards_baseline.md` and this control record;
5. record `NO CHANGE`, `PUBLISHED REPLACEMENT AVAILABLE`, `STATUS AMBIGUOUS` or `WATCH CLOSED`;
6. do not download, quote or interpret draft text as normative evidence.

### Trigger to create a clause-study task

A new task may be created only when the replacement is formally published, canonical metadata is stable, the source-acquisition decision is approved and the research trigger remains relevant. The new task must receive a new current-sequence identifier/version; this watch document is not converted in place into a clause study.

### Scope of the future research brief

The future task shall focus on review/audit terminology, purpose and participants; lifecycle/project decision points; entry/exit and evidence inputs; authority and independence; findings/actions/waivers/reopening; information items and records; tailoring; and defence-specific context. It must compare those concepts with LC-G01/LC-G02, Composite Gate and generic assessment/review/decision/event separation.

### Required repository updates per watch event

Update the standards baseline watch date/status, add a concise CHANGELOG entry only for a material publication-state change, update HANDOFF if the queue changes, and create an Architecture Impact entry only after clause study—not from metadata. Retain evidence of the catalogue check as paraphrased metadata/link, not copyrighted draft content.

### No-overclaim rules

Do not state that an FDIS is the published normative basis, that defence gates are generic assurance gates, or that publication metadata supports clause conclusions. Do not use the watch event to close LC-G01/LC-G02 or change V0–V12.

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

### Definition of done for a watch cycle

A cycle is complete when official metadata, access date and disposition are recorded consistently, no draft-derived claim was introduced, links/status terms pass checks, and any published-replacement event has a separate acquisition/task decision. The overall watch remains `planned` until formally closed or replaced.
