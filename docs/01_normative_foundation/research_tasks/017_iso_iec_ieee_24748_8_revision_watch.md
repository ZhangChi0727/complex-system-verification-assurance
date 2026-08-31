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
contribution_modes: [metadata-only]
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

执行本任务前必须先读取本节与 frontmatter dependencies，并把工作边界固定为 `metadata-watch`。本任务不进入标准正文、不形成 clause finding，也不处置 RQ、innovation candidate 或 Architecture Impact。

### Task purpose and research attitude

仅监视正式出版状态、replacement relation、source-acquisition decision 与 retarget trigger。官方 catalogue metadata 可以控制研究入口，但不能替代条款证据。当前框架假设不得改变 catalogue 事实；未取得正文不构成内容沉默或 novelty evidence。

### Source-specific metadata entry

当前 PDF inventory 中没有 ISO/IEC/IEEE 24748-8 的受控正式原文。受控 population 由当前已发布 2019 版与 Edition 2 FDIS 的官方 catalogue records、每次 access date、publication/development state 以及仓库 source-gate 状态构成。FDIS 只用于 publication-state watch，禁止下载、引用或解释其条款。

### Research questions and future candidates

- 本任务不回答任何 RQ；任何 RQ contribution 等待正式 replacement、批准取得的原文、单独编号的 clause-study task 与 independent review。
- `INN-A3` 与 `INN-M2` 只是未来任务的 search targets。本 watch 不返回 `SUPPORT / QUALIFY / FALSIFY / NO EVIDENCE`，因为 metadata 不是内容证据。

### Metadata evidence hierarchy

1. official ISO/IEC/IEEE catalogue record for the published edition;
2. official development-stage/replacement catalogue record;
3. repository standards baseline and prior watch record;
4. framework research trigger and acquisition proposal.

每个事实必须带 catalogue locator、access date 和 publication state。第三、四层只能解释仓库动作，不能覆盖官方 metadata。不得要求 PDF page、clause locator、normative force 或 source modality。

### Durable watch interface

每次 watch cycle 生成一条自包含 `metadata-watch` record，使后续 agent 能判定“是否正式发布、是否已取得、是否应新建 clause-study task”，而不依赖聊天历史。记录不得伪装成 common clause-evidence，也不得产生 content conclusion。

### Core watch principles

1. `Catalogue fact -> repository gate implication -> acquisition/retarget proposal` 三层分离；
2. FDIS/CD/DIS status 不等于 published normative basis；
3. metadata absence 不等于标准内容沉默；
4. 只对实际 publication-state change 更新仓库；
5. V0–V12、gap 与 Architecture Impact 保持不变，直至未来 clause study 通过独立评审。

## Objective

Maintain an accurate publication/replacement watch and define the gate for a future defence-domain review/audit abstraction study.

## Preliminary mapping hypotheses

以下是 watch assumptions，不是条款假设。每个 watch cycle 先冻结 official catalogue population，再逐行给出 `CONFIRMED / QUALIFIED / CORRECTED / NOT ADDRESSED`、catalogue locator、access date、理由和 repository-gate effect；不得使用 `FALSIFIED` 表示 innovation disposition。

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

Emit only the `metadata-watch` record subtype defined below. It is excluded from the common clause/mapping evidence population and from Task 022 content synthesis.

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

Update the standards baseline watch date/status, add a concise CHANGELOG entry only for a material publication-state change, update project-status.json and README if the queue changes, and create an Architecture Impact entry only after clause study—not from metadata. Retain evidence of the catalogue check as paraphrased metadata/link, not copyrighted draft content.

### No-overclaim rules

Do not state that an FDIS is the published normative basis, that defence gates are generic assurance gates, or that publication metadata supports clause conclusions. Do not use the watch event to close LC-G01/LC-G02 or change V0–V12.

### Metadata-watch record and durable-handoff controls

Each watch event emits exactly one record using this dedicated subtype; do not populate the README clause/mapping schema with artificial `none` values:

| Field | Required content |
|---|---|
| `record_type` | fixed value `metadata-watch` |
| `catalogue_locator` | stable official catalogue URL or identifier |
| `access_date` | ISO date of the metadata check |
| `published_identifier` | current formally published identifier/edition/date |
| `publication_state` | `CURRENT` / `REPLACED` / `WITHDRAWN` / `AMBIGUOUS` |
| `development_record` | edition/stage and official locator for any replacement project |
| `replacement_relation` | relation between current publication and development item |
| `source_availability` | `NOT ACQUIRED` / `ACQUISITION PROPOSED` / `ACQUIRED` |
| `trigger_disposition` | `NO CHANGE` / `PUBLISHED REPLACEMENT AVAILABLE` / `STATUS AMBIGUOUS` / `WATCH CLOSED` |
| `repository_action` | exact baseline/project-status.json/README/task action or no-change rationale |
| `confidence_review` | metadata ambiguity and reviewer disposition |

No PDF page, clause locator, source class, modality, RQ contribution or candidate disposition is permitted in this subtype.

### Hypothesis reconciliation and self-contained report rule

After freezing the official catalogue population, reconcile every watch assumption against the dated metadata snapshot. The record must be self-contained enough for a later agent to reproduce the gate decision from the official catalogue locators and access date; it must not claim to reproduce or interpret source content.

### Repository consistency checks

Before review handoff: run `git diff --check`; validate relative links/frontmatter/tables; reconcile source/study/review status; search stale `SOURCE ACQUIRED`, `IN PROGRESS`, `REVIEW PENDING`, `REVIEWED` and architecture-freeze wording; verify controlled Architecture Impact vocabulary; verify all hypotheses and promoted conclusions have dispositions/locators; verify no PDF, screenshot, OCR dump, full extraction, substantial quotation, licence identity, account, order, download timestamp, watermark or absolute user path is staged; verify provisional downstream rows retain their closure owner.

### Definition of done for a watch cycle

A cycle is complete when official metadata, access date and disposition are recorded consistently, no draft-derived claim was introduced, links/status terms pass checks, and any published-replacement event has a separate acquisition/task decision. The overall watch remains `planned` until formally closed or replaced.
