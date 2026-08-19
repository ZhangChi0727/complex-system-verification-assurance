---
title: Normative Foundation Workspace
status: working
version: 0.8
baseline: v0.2
owner: research
last_updated: 2026-08-19
dependencies:
  - ../00_overview/research_scope.md
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
- cross-standard consolidation: [Five-Source Cross-Standard Consistency & Gap Review](consolidation/five_source_consistency_gap_review.md) 已完成；source roles、Generic Core/extension points、Civil Aviation Profile、V0–V12 ontology、concept promotion 与全部 inherited gap dispositions 已冻结为 v0.2 conceptual-baseline candidate；
- cross-standard map: ISO lifecycle foundation、24748 supporting guidance、ARP4754B development-assurance profile 与 ARP4761A safety-assessment profile roles reviewed and frozen；
- normative gap matrix: 原 21 个 gap 已逐项 disposition，coverage/sufficiency 分拆为 generic interface 与 open domain-rule successors；
- detailed clause study: [ISO/IEC/IEEE 15288:2023](standard_notes/iso_15288.md) reviewed for the v0.1 research scope；review provenance is recorded in [ISO 15288 informal review](reviews/iso_15288_informal_review.md)。
- lifecycle-management supporting review: [ISO/IEC/IEEE 24748-2:2024](standard_notes/iso_24748_2_targeted_review.md) found a minor framework delta and introduced no new requirements。
- aviation safety-assurance study: [SAE ARP4754B](standard_notes/sae_arp4754b.md) development-assurance slice 与 [SAE ARP4761A](standard_notes/sae_arp4761a.md) safety-assessment slice 已完成；两者通过 Safety Requirement provenance、FDAL/IDAL、typed independence 和 multi-source evidence 连接，但不合并过程本体。
- external informal review: [ISO 24748-2 / SAE ARP4754B review](reviews/ISO-24748-2--SAE-ARP4754B-External-Informal-Review.md) 的 2 项 Major 与 4 项 Minor findings 已关闭；Test Readiness Review/V6、Result/Evidence、Appendix A provenance 和 certification-credit dimensionality 已按较低 ontology strength 修正。
- readiness: `CONDITIONALLY READY FOR v0.2 CONCEPTUAL BASELINE`；不宣称 executable schema、item-level completeness、certification acceptance 或 framework validation；
- next research round: 定位变更触发 §25 gap-priority 重评分；按当前评分预期采用**双轨**——ISO/IEC/IEEE 15288:2023 之后的 **ISO/IEC/IEEE 15289 全量条款精读**（ISO-G07 主线）与 **ISO/IEC 9646 / ITU-T X.290 概念切片 targeted review**（first-instance 前置，候选支撑 ISO-G04 与 Case/Procedure schema）并行；ISO 29148 与 ISO 15026-2 排后批；TTCN-3 待平台原型启动前；DO-178C、DO-254、DO-297 维持 deferred。新来源纳入与跨层结论受 standards_baseline layering policy 约束。
