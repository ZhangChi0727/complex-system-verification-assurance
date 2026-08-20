---
title: Normative Research Task Register
status: working
version: 0.6
baseline: post-v0.2
owner: research
last_updated: 2026-08-21
dependencies:
  - ../standards_baseline.md
  - ../normative_gap_matrix.md
  - ../consolidation/architecture_impact_register.md
  - ../../../HANDOFF/next_plan.md
  - historical/README.md
---

# Normative Research Task Register

本目录把 Controlled Candidate-Source Baseline 中尚有研究义务的来源转化为逐项任务说明。任务登记不表示条款研究已经开始，也不提升 `Availability`、`Study status`、gap 状态或 architecture-impact disposition。

## Inclusion boundary

纳入：待条款研究、待 targeted compatibility、待 overlap review 或受控 revision watch 的来源。排除：已经完成且无本轮独立任务的 five-source/29148/15026-2 clause studies、15026-1:2019 dated provenance、`TRIGGER NOT MET`、instance-controlled sources 和尚未完成 ADR selection 的 execution technologies。

ISO/IEC/IEEE 29148:2018 仅保留一个 15288:2015→2023 targeted mapping closure 任务，不重做全文研究。ISO/IEC/IEEE 15026-2:2022 的开放兼容性问题并入 15026-1:2025 任务，不另建重复 clause study。

## Common execution protocol

每项任务都必须：

1. 在任何条款提取前核验 canonical ID、edition/date、页数、语言、完整性与 SHA-256；只记录合法取得状态和受控相对文件名，PDF 不得提交；
2. 区分 normative/informative、`shall`/`should`/`may`、definition、note/example 与 framework interpretation；
3. 使用 `Standard → Interpretation → Framework implication → Research proposal` 四层分离；
4. 对相关 gap 只更新 candidate scope，除非 clause study 已完成独立复核；
5. 在 Architecture Impact Register 中使用 `CONFIRM/EXTEND/MODIFY/SPLIT/MERGE/DEPRECATE/NO-IMPACT/DEFERRED` 受控词汇，并满足本文件下述 locator、兼容性与迁移控制；
6. 保持 V0–V12 为 `OPEN-CANDIDATE`；条款研究和 working information-model exploration 不得冻结 schema、metamodel、state machine 或 automation interface；
7. 形成独立评审包并在通过前停止状态提升。

每条标准证据对创新候选只允许 `SUPPORT`、`QUALIFY`、`FALSIFY` 或 `NO EVIDENCE`。`NO EVIDENCE` 只表示该来源没有回答，不表示研究贡献新颖。标准研究可形成规范缺口、竞争解释和后续检索问题，但不能替代同行评议文献、专利与工业方案的新颖性检索。

来源与评审隐私控制适用于全部任务：不得提交 PDF、截图、OCR dump、提取全文或大段逐字内容；不得记录许可主体、账号、订单、下载时间、水印、内部 URL 或用户绝对路径。评审者使用自己合法取得且版本/指纹匹配的原文核验 locator；review packet 只包含短释义、定位符和结论，不得重构标准正文。CD/DIS/FDIS 仅用于 metadata/revision watch，不能成为 normative basis。

## Two-stage dependency and closure rule

研究依赖采用两阶段闭合，避免前向或循环依赖：

1. 较早任务只产生该来源的 `source-native dependency inventory`、`provisional crosswalk` 和 `downstream closure questions`；这些输出可供后续任务使用，但不能宣称最终跨源等价、ownership 或 architecture disposition；
2. 只有相关来源均完成条款研究和独立评审后，指定的后续 owner 或 architecture synthesis 才能产生 final cross-source disposition。每个 final matrix 只允许一个 owner；较早任务的 Definition of Done 不得依赖尚未完成的后续来源。

Task 005/013 按该规则分层：Task 013 的 24748-3 source-native extraction 可立即开始；12207:2017 语义确认等待受控历史原文；24748-3 current-baseline mapping、promotion 或 architecture disposition 等待 Task 005 独立评审；任何 V0–V12 freeze 仍等待 Task 022 和单独的 architecture-synthesis gate。

Task 001 是当前研究第一停点，但不是全局串行冻结。其评审前，15289 相关状态提升、ISO-G07C closure、信息模型冻结及依赖“已评审 15289 结论”的 final mapping/promotion 保持阻塞；无依赖的 metadata verification、source acquisition、source inventory 和 working/candidate research 可以继续。所有 V0–V12、schema、metamodel、state machine 和 automation interface 始终保持 working/open，直至各自独立门禁满足。

## Research contribution and data contract

当前 `001–021` 均为 `version: 0.4` 的 agent-executable work order；Task 022 是独立的 `cross-standard-synthesis` 工作单。每份任务必须含 `task_type`、`research_questions`、`innovation_candidates`、`contribution_modes`、`source_population`，并在正文中落实 Research contribution contract、Candidate falsification tests、Negative findings and non-answers、Generalization rights、Synthesis handoff dataset。执行者不得只依赖本登记表摘要。

所有 clause-study/mapping note 的可合并最小记录如下；字段为空时写 `none/not determined`，不得删列：

| Field | Required content |
|---|---|
| `source_locator` | clause/table/figure/annex + physical PDF page |
| `source_class` | normative requirement / recommendation / informative / example |
| `proposition` | faithful short paraphrase; no substantial quotation |
| `object_relation` | source-native object and relation |
| `rq_contribution` | RQ identifier and exact sub-question |
| `candidate_test` | candidate ID + SUPPORT/QUALIFY/FALSIFY/NO EVIDENCE + rationale |
| `framework_mapping` | V-ID/gap/concept + relation type; interpretation kept separate |
| `layer` | Generic/Extension/Profile/Practice/No adoption |
| `unsupported_inference` | inference explicitly prohibited by the evidence |
| `version_dependency` | source-native locator, current counterpart and relation |
| `confidence_review` | evidence quality, unresolved item and independent-review disposition |

Task 022 consumes only these reviewed records. Narrative conclusions without the record set cannot close an RQ, candidate test, gap or architecture impact.

Architecture-impact disposition 的受控词汇为 `CONFIRM / EXTEND / MODIFY / SPLIT / MERGE / DEPRECATE / NO-IMPACT / DEFERRED`。`MODIFY`、`SPLIT`、`MERGE`、`DEPRECATE` 必须记录 before/after 语义、compatibility 和 migration；`EXTEND` 必须证明与既有 V-element 的兼容性；`CONFIRM` 与 `NO-IMPACT` 必须给出已评审 locator 和理由；`DEFERRED` 只表示证据、依赖或评审不足，不是架构结论。具体登记与成熟度门禁以 `../consolidation/architecture_impact_register.md` 为准。

一份任务说明与其受控标准原文交给新的 agent 时，agent 仍应先读取说明中列出的 repository dependencies，以获取当前 gap、术语和架构状态；但不得要求未记录的口头上下文才能理解任务。任务说明中的目标文件名是默认交付路径，如仓库结构在执行前已发生受控变化，agent 应记录等价迁移而不是创建重复文件。

统一状态流为：

```text
PLANNED / SOURCE GATE
        ↓
CLAUSE STUDY IN PROGRESS
        ↓
REVIEW PENDING
        ↓
REVIEWED or CORRECTION REQUIRED
```

`SOURCE ACQUIRED`、metadata verification、报告初稿或内部自检都不能单独产生 `REVIEWED` 状态。任务完成必须同时满足该任务自身的 Definition of Done、仓库一致性检查和独立评审 disposition。

## RQ and innovation-candidate coverage

| Task | RQ coverage | Innovation candidates / falsification path |
|---|---|---|
| 001 | RQ1, RQ5, RQ7 | INN-T2/T3/I1; 15289 direct mechanism or schema non-answer |
| 002 | RQ3, RQ5, RQ8 | INN-T2/T3/M4/I2; 9646 conformance chain and Oracle alternative |
| 003 | RQ4, RQ5 | INN-T1/T3; 15026 vocabulary/reasoning/evidence mechanism |
| 004 | RQ2, RQ4, RQ5 | INN-T1/T3/M1; lifecycle assurance/re-assurance alternative |
| 005 | RQ1–RQ5, RQ7 | INN-T1/T2/T3/A1/M1/M2/M4/I2; current software-lifecycle countermechanisms |
| 006 | RQ3, RQ5, RQ7 | INN-T2/M3/M4/I2; current test-model ontology |
| 007 | RQ2, RQ3, RQ5 | INN-A1/M1/M2; process/re-entry/closure alternatives |
| 008 | RQ5, RQ7 | INN-T3/I1; information-item and schema alternative |
| 009 | RQ3, RQ4, RQ6 | INN-M3/M4/A3; techniques, coverage and reusable-pattern counterexamples |
| 010 | RQ2–RQ5, RQ8 | INN-T1/A1/M1/A3; sufficient-evidence and integrity/task mechanism |
| 011 | RQ3, RQ4, RQ5 | INN-T1/A1; level claim/determination/approval mechanism |
| 012 | RQ2, RQ3, RQ5 | INN-A1/M1/M2; planning input versus selection/closure alternative |
| 013 | RQ2, RQ3, RQ5 | INN-A1/M1/I2; application/tailoring alternative |
| 014 | RQ2, RQ3, RQ5, RQ7 | INN-A1/I1; software-planning/process/content alternative |
| 015 | RQ2, RQ3, RQ5 | INN-A1/M1/M3; integration/change/coverage alternative |
| 016 | RQ2, RQ8 | INN-A1/M1/A3; linear-topology counterexamples |
| 017 | metadata only | future INN-A3/M2; no clause/candidate disposition permitted |
| 018 | RQ3, RQ5, RQ7, RQ8 | INN-T3/M5/I1; model/tool admissibility alternatives |
| 019 | RQ3, RQ4, RQ5 | INN-T1/T3/M3; measurement-quality versus sufficiency alternative |
| 020 | RQ2, RQ5, RQ7 | INN-A1/M2; project-control versus closure-machine alternative |
| 021 | RQ1, RQ3, RQ7 | INN-T2/I1; historical/current requirements-chain alternative |
| 022 | RQ1–RQ8 | INN-T1–INN-I2; cross-source conflict/silence ledger plus independent novelty-search questions |

RQ1–RQ8 each have at least two source families and an explicit countermechanism or non-equivalence path. Source count does not establish evidence quality; Task 022 must register any weak, single-family or unresolved coverage as a research gap.

## Progress reporting

Progress denominators are separate and shall never be collapsed: `clause-study` (19 planned source studies), `mapping-closure` (Task 021), `metadata-watch` (Task 017) and `cross-standard-synthesis` (Task 022). A watch cycle is not a completed clause study. If 24748-8 is formally replaced/acquired, create a new numbered clause-study task rather than converting Task 017.

## Ordered task set

| Order | Source/work package | Task document | Local source observation | Start control |
|---|---|---|---|---|
| 01 | ISO/IEC/IEEE 15289:2019 | [Task 01](001_iso_iec_ieee_15289_2019.md) | Verified baseline source file present | Current research stop |
| 02 | ISO/IEC 9646 Parts 1/2/4/5/6/7 | [Task 02](002_iso_iec_9646_series.md) | Complete controlled ISO source population acquired | Part 3/ITU excluded; clause study may start |
| 03 | ISO/IEC/IEEE 15026-1:2025 | [Task 03](003_iso_iec_ieee_15026_1_2025.md) | Verified baseline source file present | After/alongside 15289 as dependency permits |
| 04 | ISO/IEC/IEEE 15026-4:2021 | [Task 04](004_iso_iec_ieee_15026_4_2021.md) | Acquired published source verified | Part 1 vocabulary; provisional downstream dependencies only |
| 05 | ISO/IEC/IEEE 12207:2026 | [Task 05](005_iso_iec_ieee_12207_2026.md) | Acquired: 154 pages; controlled fingerprint | Source-native study may start; historical 2017 map remains blocked |
| 06 | ISO/IEC/IEEE 29119-1:2022 | [Task 06](006_iso_iec_ieee_29119_1_2022.md) | Acquired source file verified | Part 1 concepts first |
| 07 | ISO/IEC/IEEE 29119-2:2021 | [Task 07](007_iso_iec_ieee_29119_2_2021.md) | Acquired source file verified | Part 1 concepts first |
| 08 | ISO/IEC/IEEE 29119-3:2021 | [Task 08](008_iso_iec_ieee_29119_3_2021.md) | Acquired source file verified | Coordinate 15289 and Part 2 |
| 09 | ISO/IEC/IEEE 29119-4:2021 | [Task 09](009_iso_iec_ieee_29119_4_2021.md) | Acquired source file verified | Part 1 concepts first |
| 10 | IEEE 1012-2024 | [Task 10](010_ieee_1012_2024.md) | Acquired source file verified | Coordinate 15026-3 |
| 11 | ISO/IEC/IEEE 15026-3:2023 | [Task 11](011_iso_iec_ieee_15026_3_2023.md) | Acquired source file verified | Coordinate IEEE 1012 |
| 12 | ISO/IEC/IEEE 24748-4:2026 | [Task 12](012_iso_iec_ieee_24748_4_2026.md) | Acquired published source verified | Required before final synthesis; overlap provisional |
| 13 | ISO/IEC/IEEE 24748-3:2020 | [Task 13](013_iso_iec_ieee_24748_3_2020.md) | Acquired published source verified | 12207:2017→2026 compatibility depends on Task 05 |
| 14 | ISO/IEC/IEEE 24748-5:2017 | [Task 14](014_iso_iec_ieee_24748_5_2017.md) | Acquired published source verified | Task 12 context; overlap provisional until Task 20 |
| 15 | ISO/IEC/IEEE 24748-6:2023 | [Task 15](015_iso_iec_ieee_24748_6_2023.md) | Acquired published source verified | 15288 context; 12207 mapping provisional until Task 05 |
| 16 | ISO/IEC/IEEE 24748-10:2026 | [Task 16](016_iso_iec_ieee_24748_10_2026.md) | Acquired published source verified | 15288/24748-1 context; required before freeze gate |
| 17 | ISO/IEC/IEEE 24748-8 | [Task 17](017_iso_iec_ieee_24748_8_revision_watch.md) | No matching PDF in current inventory | Revision watch only |
| 18 | ISO/IEC/IEEE 24641:2023 | [Task 18](018_iso_iec_ieee_24641_2023.md) | Acquired published source verified | 15288 context; software mapping provisional until Task 05 |
| 19 | ISO/IEC/IEEE 15939:2017 | [Task 19](019_iso_iec_ieee_15939_2017.md) | Acquired published source verified | Revision recheck and 15288 mapping required |
| 20 | ISO/IEC/IEEE 16326:2019 | [Task 20](020_iso_iec_ieee_16326_2019.md) | Acquired published source verified | Final planning-overlap closure owner after Tasks 12/14 |
| 21 | ISO/IEC/IEEE 29148:2018 targeted mapping | [Task 21](021_iso_iec_ieee_29148_2018_mapping_closure.md) | Reviewed local source present | Mapping closure only |
| 22 | Cross-standard synthesis and innovation falsification | [Task 22](022_cross_standard_research_synthesis_and_innovation_falsification.md) | Consumes reviewed Task 001–021 datasets | Runs after relevant research packages; does not replace novelty search |

## Historical task archive

Completed or superseded pre-v0.2 task specifications use stable `H###` identifiers, `status: superseded`, `version: 1.0` and `body_format: preserved-original`. They retain research provenance and are not part of the current 001–021 execution queue.

| ID | Historical task | Controlled outcome |
|---|---|---|
| H001 | [ISO/IEC/IEEE 15288:2023 clause research](historical/h001_iso_iec_ieee_15288_2023_clause_research.md) | Reviewed standard note and v0.2 foundation |
| H002 | [ISO/IEC/IEEE 24748-1:2024 clause research](historical/h002_iso_iec_ieee_24748_1_2024_clause_research.md) | Reviewed standard note and lifecycle/process-view basis |
| H003 | [ISO/IEC/IEEE 24748-1:2024 clean-source correction](historical/h003_iso_iec_ieee_24748_1_2024_source_baseline_correction.md) | Clean-source provenance correction completed |
| H004 | [ISO/IEC/IEEE 24748-2:2024 + SAE ARP4754B research round](historical/h004_iso_iec_ieee_24748_2_2024_sae_arp4754b_research_round.md) | Reviewed supporting source and aviation-profile contribution |
| H005 | [Five-source consistency and gap review](historical/h005_five_source_consistency_gap_review.md) | v0.2 historical conceptual checkpoint |
| H006 | [SAE ARP4761A:2023 safety-assurance research](historical/h006_sae_arp4761a_2023_safety_assurance_research.md) | Reviewed aviation safety-assessment profile contribution |

The user-supplied [PR #4 ARP4761A external review](../reviews/pr_4_arp4761a_external_review.md) is classified as a historical review record rather than a task specification.

## Explicitly deferred or excluded

- ISO/IEC TR 29119-11:2020: `TRIGGER NOT MET`;
- RTCA DO-178C / DO-254 / DO-297: `TRIGGER NOT MET` and no current source registration by document;
- ARINC 615A and instance standards: instance-controlled, not generic research tasks;
- ISO/IEC 9646-3 and ITU-T X.29x clause study: excluded from Task 002; Part 3 re-enters only for a TTCN/ATS-serialization or executable-suite ADR, while ITU numbers remain bibliographic relationships without text-equivalence claims;
- ETSI TTCN-3 / SysML / tools: local TTCN-3 source parts are acquired, but ADR/selection is not started and SysML/tool sources are not selected; TTCN-3 must not be conflated with the ISO 9646 conformance-methodology task;
- ISO/IEC/IEEE 15026-1:2019: dated-reference provenance only, no standalone study.
