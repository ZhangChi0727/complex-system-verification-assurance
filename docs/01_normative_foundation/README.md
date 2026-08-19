---
title: Normative Foundation Workspace
status: working
version: 0.9
baseline: post-v0.2
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
- requirements-to-assurance research: [ISO/IEC/IEEE 29148:2018](standard_notes/iso_iec_ieee_29148_2018_clause_study.md) 与 [ISO/IEC/IEEE 15026-2:2022](standard_notes/iso_iec_ieee_15026_2_2022_clause_study.md) 条款研究已通过独立评审；[crosswalk](consolidation/requirements_to_assurance_crosswalk.md) 将 Requirement/Basis→Obligation→Result 链与 Evidence Item→Argument→Supported Claim/Inference 链连接，并把 Result/Artefact→Evidence Item 明确为受 5.3.2 约束的 framework-defined characterization。ISO 15289、15026-1:2019/2025 与 29148→15288 版本映射仍开放。
- external informal review: [ISO 24748-2 / SAE ARP4754B review](reviews/ISO-24748-2--SAE-ARP4754B-External-Informal-Review.md) 的 2 项 Major 与 4 项 Minor findings 已关闭；Test Readiness Review/V6、Result/Evidence、Appendix A provenance 和 certification-credit dimensionality 已按较低 ontology strength 修正。
- readiness: `CONDITIONALLY READY FOR v0.2 CONCEPTUAL BASELINE`；不宣称 executable schema、item-level completeness、certification acceptance 或 framework validation；
- next research round: 依次推进 ISO 15289、ISO 9646/X.290、15026-1:2019/2025 delta、29119-2/3/4、IEEE 1012/15026-3；具体依赖和后续 schema/registry/platform 顺序见 `../../HANDOFF/next_plan.md`。
- source governance: `standards_baseline.md` 是 **Controlled Candidate-Source Baseline**，冻结变更流程而非来源全集。新来源关联 open gap、登记 layer/trigger/status 并经评审；未完成 clause study 的候选不得关闭 gap。
