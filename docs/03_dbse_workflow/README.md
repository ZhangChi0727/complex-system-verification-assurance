---
title: DBSE Verification Workflow Workspace
status: working
version: 0.3
baseline: v0.1
owner: research
last_updated: 2026-08-15
dependencies:
  - ../01_normative_foundation/README.md
  - ../02_verification_framework/README.md
---

# DBSE Verification Workflow Workspace

候选架构包含 `V0` 至 `V12`，详见 [research roadmap](../00_overview/roadmap.md)。ISO/IEC/IEEE 15288:2023 的 5.7–5.8 支持迭代、递归和并发应用过程；ISO/IEC/IEEE 24748-1:2024 Clause 5、Annex A、D 和 E 进一步说明 stage ≠ process、过程可跨阶段调用，以及 process view 不定义新的源标准任务。

因此 V0–V12 定位为 **Verification Assurance Process View / cross-process orchestration architecture**：编号仅用于稳定标识和覆盖分析，不表示 lifecycle stage、强制时间顺序或瀑布模型。每个 V-element 必须声明自身本体和源任务映射：

- `Activity / information design`：V0–V5、V7；
- `Evaluation / decision`：V8；
- `Cross-process concern or orchestration`：V9–V10；
- `Assurance assessment`：V11；
- `Composite gate`：V6 与 V12。

V6 `Verification Readiness` 是 framework-defined composite gate，由 criteria-driven lifecycle evaluation、可选 verification/lifecycle review 和 authorization decision 组成。V12 `Verification Closure` 同样是 framework-defined composite gate，整合 assurance assessment、approval decision、traceability/baseline completion 及适用的 lifecycle-gate semantics。ISO 24748-1 Annex F 只给出候选 `Verification reviews`，不要求名为 `Verification Readiness Review` 的固定 gate，也不定义名为 `Verification Closure` 的过程。

每个 view element 未来统一描述：Element ID、Ontology、Purpose、Normative Basis、Source Process/Activity/Task Mapping、Inputs、Entry Criteria、Roles/Decision Authority、Process/Assessment、Decision Rules、Outputs、Required Records、Traceability、Independence、Configuration Control、Exit Criteria、Iteration/Re-entry Rules。

项目实例应使用 [Lifecycle / Process Tailoring and Instantiation Record](../../templates/lifecycle_process_instantiation_record.md) 记录适用标准、development approach、阶段/条件/gates、过程选择及理由。模板是 research draft，不是 ISO 24748-1 规定的信息项 schema。

**Status:** ISO 15288 与 ISO 24748-1 mapped；source-task provenance、domain rules、gate state model、coverage/sufficiency 和 closure authority 仍不冻结。
