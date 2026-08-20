---
title: Normative Foundation Workspace
status: working
version: 0.14
baseline: post-v0.2
owner: research
last_updated: 2026-08-20
dependencies:
  - ../00_overview/research_scope.md
  - consolidation/architecture_impact_register.md
  - research_tasks/README.md
---

# Normative Foundation Workspace

本目录是 Phase 1 的首要研究空间，目标是区分 proposed Verification Assurance Framework 中哪些内容由标准直接支持、哪些属于工程解释、哪些是 industrial practice、哪些是 research proposal。

```text
Normative Source
      ↓
Extracted Objective / Requirement
      ↓
Interpretation
      ↓
Framework Implication
      ↓
Framework Rule
```

每个研究条目必须区分：`NORMATIVE`、`INFORMATIVE`、`INTERPRETATION`、`FRAMEWORK IMPLICATION` 或 `RESEARCH PROPOSAL`，并在映射层说明 direct、indirect 或 partial support。没有合法原文和准确定位时只记录 metadata、study queue 与 `TBD`，不得把 secondary-source summary 当作直接规范要求。

## Current state

- standards target baseline: ISO/IEC/IEEE 15288:2023 与 ISO/IEC/IEEE 24748-1:2024 reviewed baseline candidates；ISO/IEC/IEEE 24748-2:2024 reviewed supporting source；SAE ARP4754B 与 ARP4761A reviewed aviation-profile baseline candidates；
- cross-standard consolidation: [Five-Source Cross-Standard Consistency & Gap Review](consolidation/five_source_consistency_gap_review.md) 已完成并保留为 v0.2 historical conceptual checkpoint；稳定 V-ID 和既有评审 provenance 保持不变，现行 V0–V12 架构成熟度为 `OPEN-CANDIDATE`；
- cross-standard map: ISO lifecycle foundation、24748 supporting guidance、ARP4754B development-assurance profile 与 ARP4761A safety-assessment profile roles reviewed and frozen；
- normative gap matrix: 原 21 个 gap 已逐项 disposition，coverage/sufficiency 分拆为 generic interface 与 open domain-rule successors；
- detailed clause study: [ISO/IEC/IEEE 15288:2023](standard_notes/iso_15288.md) reviewed for the v0.1 research scope；review provenance is recorded in [ISO 15288 informal review](reviews/iso_15288_informal_review.md)。
- lifecycle-management supporting review: [ISO/IEC/IEEE 24748-2:2024](standard_notes/iso_24748_2_targeted_review.md) found a minor framework delta and introduced no new requirements。
- aviation safety-assurance study: [SAE ARP4754B](standard_notes/sae_arp4754b.md) development-assurance slice 与 [SAE ARP4761A](standard_notes/sae_arp4761a.md) safety-assessment slice 已完成；两者通过 Safety Requirement provenance、FDAL/IDAL、typed independence 和 multi-source evidence 连接，但不合并过程本体。
- requirements-to-assurance research: [ISO/IEC/IEEE 29148:2018](standard_notes/iso_iec_ieee_29148_2018_clause_study.md) 与 [ISO/IEC/IEEE 15026-2:2022](standard_notes/iso_iec_ieee_15026_2_2022_clause_study.md) 条款研究已通过独立评审；[crosswalk](consolidation/requirements_to_assurance_crosswalk.md) 将 Requirement/Basis→Obligation→Result 链与 Evidence Item→Argument→Supported Claim/Inference 链连接，并把 Result/Artefact→Evidence Item 明确为受 5.3.2 约束的 framework-defined characterization。ISO 15289、15026-1:2025 targeted compatibility 与 29148→15288 版本映射仍开放；15026-1:2019 仅保留为 15026-2 明示 dated-reference provenance。
- architecture governance: [Architecture Impact Register](consolidation/architecture_impact_register.md) 控制后续来源对 V0–V12 的 `CONFIRM/EXTEND/MODIFY/SPLIT/MERGE/NO-IMPACT/DEFERRED` 处置；metadata 或 source acquisition 不构成架构结论；
- research task control: [Normative Research Task Register](research_tasks/README.md) 为每个仍有研究义务的标准或受控 work package 建立 agent-executable `version: 0.3` 任务说明，逐项控制来源、完整条款清单、证据提取、标准专属研究包、provisional/final closure ownership、映射、仓库更新、评审包和完成条件；任务登记不表示 clause study 已开始；
- software-lifecycle candidate foundation: ISO/IEC/IEEE 12207:2026 以 `METADATA VERIFIED; SOURCE NOT ACQUIRED; CLAUSE STUDY PENDING` 登记，用于 15026-4 software view 与 24748-3 compatibility 的后续研究；尚未形成条款结论或 established basis；
- planned 24748 candidates: Parts 3、4、5、6、10 仅作为 generic methodological candidate sources 登记；Part 8:2019 仅作为 defence-domain profile candidate 并保持 formal-revision watch。它们未进入 established clause basis，未改变任何 gap 持续状态；
- external informal review: [ISO 24748-2 / SAE ARP4754B review](reviews/ISO-24748-2--SAE-ARP4754B-External-Informal-Review.md) 的 2 项 Major 与 4 项 Minor findings 已关闭；Test Readiness Review/V6、Result/Evidence、Appendix A provenance 和 certification-credit dimensionality 已按较低 ontology strength 修正。
- readiness: `CONDITIONALLY READY FOR v0.2 CONCEPTUAL BASELINE`；不宣称 executable schema、item-level completeness、certification acceptance 或 framework validation；
- next research round: 当前停点保持 ISO 15289；其余来源按依赖驱动队列推进，并在 architecture synthesis/freeze 前完成规定的 impact dispositions。具体依赖和后续 schema/registry/platform 顺序见 `../../HANDOFF/next_plan.md`。
- source governance: `standards_baseline.md` 是 **Controlled Candidate-Source Baseline**，冻结变更流程而非来源全集。新来源关联 open gap、登记 layer/trigger/status 并经评审；未完成 clause study 的候选不得关闭 gap。
