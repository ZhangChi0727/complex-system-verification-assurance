---
title: Next Plan
status: working
version: 0.3
baseline: post-v0.2
owner: research
last_updated: 2026-08-19
dependencies:
  - README.md
  - current_progress.md
  - ../docs/01_normative_foundation/standards_baseline.md
---

# Next Plan

`research-baseline/v0.2` 已完成，不再重复执行冻结动作。后续研究按 open gap、candidate-source 状态和 source availability 排序：

1. **ISO/IEC/IEEE 15289:2019**：信息项内容研究，推进 ISO-G07；
2. **ISO/IEC 9646 / ITU-T X.290**：conformance-testing targeted study，检验 ISO-G04 与 Case/Procedure 候选；
3. **ISO/IEC/IEEE 15026-1:2025**：以正式发布的 2025 版作为当前 assurance vocabulary and concepts 基础，研究 15026-2 Clause 2/3 的不注日期依赖，并对框架实际采用的 Claim、assurance、uncertainty 等概念进行限定兼容性检查；不开展 2019→2025 全文版本差异研究。15026-2:2022 中的明示 2019 引用仅作为原始来源追溯保留；
4. **ISO/IEC/IEEE 29119-2/3/4**：测试过程、文档与技术；
5. **IEEE 1012-2024 / ISO/IEC/IEEE 15026-3:2023**：V&V rigor 与 assurance-intensity；
6. **Executable information schema**：仅在相关 schema gates 满足后启动；
7. **Versioned object registry**：建立稳定引用所需版本、定位和兼容规则；
8. **Platform reference architecture**：在信息模型稳定后进行可替换技术选型；
9. **External-instance integration**：通过临时映射迁移到稳定 registry，并使用 Framework Change Proposal 接收反馈。

ISO 29148:2018 与 ISO 15026-2:2022 的现有研究已在本 consolidated integration 中完成独立评审修正；它们不会因评审完成而关闭 15289、15026-1:2025 targeted compatibility、executable schema、sufficiency/authority 或 stable-registry 依赖，也不改写上述下一轮顺序。ISO/IEC/IEEE 15026-1:2019 不再是独立 clause-study 对象或待研究标准。

## Triggered work

| Trigger | Work |
|---|---|
| platform prototype ADR | TTCN-3 / modelling technology selection |
| UAV item-level scope | DO-178C / DO-254 / DO-297 and applicable supplements |
| LLM-service instance | AI testing guidance current-source assessment |

任何新增候选源都必须按 Controlled Candidate-Source Baseline 登记；候选登记不构成 normative support 或 novelty proof。
