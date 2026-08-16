---
title: DBSE Verification Workflow Workspace
status: working
version: 0.6
baseline: v0.1
owner: research
last_updated: 2026-08-16
dependencies:
  - ../01_normative_foundation/README.md
  - ../02_verification_framework/README.md
---

# DBSE Verification Workflow Workspace

候选架构包含 `V0` 至 `V12`，详见 [research roadmap](../00_overview/roadmap.md)。ISO/IEC/IEEE 15288:2023 的 5.7–5.8 支持迭代、递归和并发应用过程；ISO/IEC/IEEE 24748-1:2024 Clause 5、Annex A、D 和 E 进一步说明 stage ≠ process、过程可跨阶段调用，以及 process view 不定义新的源标准任务。

因此 V0–V12 定位为 **Verification Assurance Process View / cross-process orchestration architecture**：编号仅用于稳定标识和覆盖分析，不表示 lifecycle stage、强制时间顺序或瀑布模型。每个 V-element 必须声明自身本体和源任务映射：

- `Activity / information design`：V0–V5、V7；
- `Evaluation / decision`：V8；
- `Cross-process concern or orchestration`：V9–V10，其中 V10 现命名为 `Change Impact & Re-verification`；
- `Assurance assessment`：V11；
- `Composite gate`：V6 与 V12。

V6 `Verification Readiness` 是 framework-defined composite gate，由 criteria-driven lifecycle evaluation、可选 verification/lifecycle review 和 authorization decision 组成。V12 `Verification Closure` 同样是 framework-defined composite gate，整合 assurance assessment、approval decision、traceability/baseline completion 及适用的 lifecycle-gate semantics。ISO 24748-1 Annex F 只给出候选 `Verification reviews`，不要求名为 `Verification Readiness Review` 的固定 gate，也不定义名为 `Verification Closure` 的过程。

ISO/IEC/IEEE 24748-2:2024 不改变上述本体；它进一步说明 process strategy 应整合进 project planning、Verification 可按 system type/stage/entry-exit decision 多次应用、enabling systems 有自己的 requirements/configuration/availability/lifecycle dependencies。它不引入新的 ISO requirements，也不把 V6/V12 定义成 ISO gate。

SAE ARP4754B 为 aviation profile 增加以下关系，但不反向成为 generic rules：

- `FDAL/objective → applicability + process independence + output System Control Category`；
- `aircraft/system verification activity → item-level allocation/delegation → evidence acceptance/credit`；
- `transition criteria → readiness/closure assessment inputs`；ARP4754B Test Readiness Review 是 testing/demonstration-specific aviation review，可 `contributesTo(V6)`，但不等同于 V6、不建立 `specializationOf(V6)`，也不推出其他 verification methods 必须具有正式 readiness review；
- `change → impact → prior-evidence validity → selected re-verification → supplemented substantiation`，因此 V10 从 `Regression` 改名而不改 ID；
- `Verification Result/Data → may constitute or support Evidence → may support substantiation`；Evidence identity、applicability、credibility/control 和 sufficiency 分别评价，之后才涉及 certification coordination 与 authority decision；Certification approval 不是 Evidence。

SAE ARP4761A 增加一个相互连接但不替代 V0–V12 的 **Safety Assessment Process View**：

```text
AFHA/SFHA → Failure Conditions + classifications + Safety Objectives
PASA/PSSA → architecture assessment + Safety Requirements + FDAL/IDAL/independence
SSA       → implemented-system safety assurance assessment
ASA       → aircraft-level safety assurance aggregation
```

双视图通过 Safety Objective/Requirement、Verification Obligation、Assurance Constraint、Assumption 和 Evidence 关联。`Safety Analysis Method` 与 `Verification Method` 分层；SSA 不是 generic Verification Process，ASA 不是 V12。

ARP4761A 对稳定 V-ID 的影响限定为 profile extension：V0–V3 接收 safety basis/constraints；V10 增加 `safety impact → assumption/FDAL/IDAL reassessment → prior-evidence validity → selected re-analysis/re-verification`；V11 评价 Failure Condition、objective、requirement、assumption、independence coverage 及 heterogeneous evidence sufficiency；V12 接收 SSA/ASA completion 作为 aviation-specific input，但仍保留 assessment、review、decision 与 baseline event 的分离。

每个 view element 未来统一描述：Element ID、Ontology、Purpose、Normative Basis、Source Process/Activity/Task Mapping、Inputs、Entry Criteria、Roles/Decision Authority、Process/Assessment、Decision Rules、Outputs、Required Records、Traceability、Independence、Configuration Control、Exit Criteria、Iteration/Re-entry Rules。

项目实例应使用 [Lifecycle / Process Tailoring and Instantiation Record](../../templates/lifecycle_process_instantiation_record.md) 记录适用标准、development approach、阶段/条件/gates、过程选择及理由。模板是 research draft，不是 ISO 24748-1 规定的信息项 schema。

**Status:** ISO 15288、ISO 24748-1、ISO 24748-2 supporting guidance、ARP4754B development assurance 与 ARP4761A safety assurance 已 mapped；generic gate state model、完整 coverage/sufficiency、closure authority 和 item-level objectives 仍不冻结。下一步是 Cross-Standard Consistency & Gap Review，而非自动进入 item-level 标准。
