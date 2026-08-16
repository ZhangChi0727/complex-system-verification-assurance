---
title: Research Roadmap
status: baseline
version: 0.5
baseline: v0.1
owner: research
last_updated: 2026-08-16
dependencies:
  - research_scope.md
  - research_questions.md
---

# Research Roadmap

## Phase 0 — Repository & Practice Baseline

建立 Research Baseline v0.1、知识架构、研究边界、工作术语、贡献规则和 future workspace。当前 PR 属于本阶段。

## Phase 1 — Normative Foundation

系统研究 ISO/IEC/IEEE 15288、ISO/IEC/IEEE 24748、INCOSE、NASA Systems Engineering Handbook、SAE ARP4754B、SAE ARP4761A、RTCA DO-178C、DO-254、DO-297 及适用补充标准。仅在合法取得全文和准确定位后形成规范性结论。

第一轮五源 consolidation 已完成：ISO 15288、ISO 24748-1/2、ARP4754B 与 ARP4761A 的 source roles、Generic Core/extension points、Civil Aviation Profile 和 inherited gaps 已统一。下一主要标准由 gap-priority matrix 选择为 **ISO/IEC/IEEE 15289**；ISO 29148 次之。DO-178C、DO-254、DO-297 不再按引用链自动启动。

## Phase 2 — Normative Gap Analysis

比较：

```text
Normative Requirement
vs.
Industrial Practice
vs.
Proposed Framework
```

## Phase 3 — DBSE Process Architecture

研究以下 working Verification Assurance Process View / cross-process orchestration architecture：

```text
V0  Verification Planning
V1  Verification Basis Establishment
V2  Requirement Verifiability Analysis
V3  Verification Strategy Definition
V4  Verification Case Design
V5  Verification Procedure Development
V6  Verification Readiness
V7  Verification Execution
V8  Result Evaluation
V9  Anomaly Resolution
V10 Change Impact & Re-verification
V11 Coverage & Sufficiency Assessment
V12 Verification Closure
```

ISO/IEC/IEEE 15288:2023 的 5.7–5.8 与 ISO/IEC/IEEE 24748-1:2024 Clause 5、Annex A/D/E 支持迭代、递归、并发和跨过程 view；ISO/IEC/IEEE 24748-2:2024 进一步澄清策略整合、多次调用和 gate cadence；SAE ARP4754B, 6.3–6.4 支持 V10 的 aviation modification/credit specialization，ARP4761A, 3.1、Appendices D–F/P 支持 Safety Reassessment、safety-evidence aggregation 和 completion inputs。

五源 consolidation 已冻结 V0–V12 名称和 ontology：V0–V5/V7 是 activity/information design，V8 是 evaluation/decision，V9–V10 是 cross-process orchestration，V11 是 assurance assessment，V6/V12 是 framework-defined Composite Gates。Coverage/Sufficiency 的 generic interfaces 已稳定，但 domain taxonomies/criteria、closure authority/state 与 V10 selection rules仍 open。

## Phase 4 — Verification Information Architecture

定义 candidate entities、字段、关系、状态、ownership、traceability 和 configuration semantics。

入口条件已由五源 conceptual consolidation 满足。先以稳定 entity/relation set 为基础研究 ISO 15289；不得从现有 YAML 字段倒推 ontology，也不得在 source basis 到位前冻结 cardinality/schema。

## Phase 5 — Coverage & Evidence Architecture

建立 Requirement Type → Applicable Coverage Obligations，并研究 Claim → Argument → Evidence 的充分性关系。

## Phase 6 — Verification Pattern Library

从跨项目问题和 DCAS 实践中抽象 generic patterns，记录适用边界和 domain instantiation。

## Phase 7 — DCAS Re-instantiation

通过 source mapping 把工业实践重新分类为 Generic Methodology、Domain Rule、Concrete Example、Tooling 或 Organizational Practice。

## Phase 8 — MBSE Metamodel

在 DBSE workflow 和 information model 足够稳定后研究 SysML、SysML v2、schema、graph representation 与 executable constraints。

## Phase 9 — Automation

研究 traceability checking、coverage checking、impact analysis、model validation 与 document generation。不得在信息模型稳定前固化工具规则。

## Phase 10 — Cross-Domain Validation

以 DCAS 为 primary case，以 ARINC 615A 为 cross-domain candidate，评价 completeness、traceability、repeatability、scalability、reusability 和 Evidence quality。

## Phase gates

每阶段进入下一阶段前，应明确：依赖是否满足、哪些对象已 baseline、哪些仍为 working/TBD、开放问题及可审计产物。
