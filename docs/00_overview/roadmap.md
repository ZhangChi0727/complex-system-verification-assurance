---
title: Research Roadmap
status: baseline
version: 0.6
baseline: v0.1
owner: research
last_updated: 2026-08-18
dependencies:
  - research_scope.md
  - research_questions.md
---

# Research Roadmap

## Phase 0 — Repository & Practice Baseline

建立 Research Baseline v0.1、知识架构、研究边界、工作术语、贡献规则和 future workspace。当前 PR 属于本阶段。

## Phase 1 — Normative Foundation

系统研究 ISO/IEC/IEEE 15288、ISO/IEC/IEEE 24748、INCOSE、NASA Systems Engineering Handbook、SAE ARP4754B、SAE ARP4761A、RTCA DO-178C、DO-254、DO-297、generic conformance-testing methodology 来源（ISO/IEC 9646 / ITU-T X.290 系列、ETSI TTCN-3）及适用补充标准。仅在合法取得全文和准确定位后形成规范性结论。

第一轮五源 consolidation 已完成：ISO 15288、ISO 24748-1/2、ARP4754B 与 ARP4761A 的 source roles、Generic Core/extension points、Civil Aviation Profile 和 inherited gaps 已统一。其后的 ISO/IEC/IEEE 29148:2018 与 ISO/IEC/IEEE 15026-2:2022 研究建立了 Requirement/Basis→Obligation→Result 与 Evidence Item→Supported Claim/Inference 的受控接口。下一轮采用双轨：**ISO/IEC/IEEE 15289 全量条款精读**（ISO-G07B 主线）与 **ISO/IEC 9646 / ITU-T X.290 概念切片 targeted review**（first-instance 前置）并行；ISO/IEC/IEEE 15026-1 是 assurance/claim/uncertainty 的并行术语依赖。ETSI TTCN-3 待平台原型启动前；DO-178C、DO-254、DO-297 维持 deferred。标准纳入与分层管理遵循 `01_normative_foundation/standards_baseline.md` 的 layering policy。

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

入口条件已由五源 conceptual consolidation 满足。29148/15026-2 已解析 conceptual item/view taxonomy 与 assurance-case recursive structure，但 executable schema、cardinality 和 15289 interoperability 仍开放。先研究 ISO 15289，并解决或显式接受 15026-1 dependency；不得从现有 YAML 字段倒推 ontology。

## Phase 5 — Coverage & Evidence Architecture

建立 Requirement Type → Applicable Coverage Obligations，并研究 Claim → Argument → Evidence 的充分性关系。

## Phase 6 — Verification Pattern Library

从跨项目问题、DCAS 实践（knowledge source）和验证实例中抽象 generic patterns，经抽象阶梯（见 research_scope）进入方法论，记录适用边界和 domain instantiation。

## Phase 7 — DCAS Knowledge-Source Re-instantiation

通过 source mapping 把 DCAS 工业实践重新分类为 Generic Methodology、Domain Rule、Concrete Example、Tooling 或 Organizational Practice。DCAS 不承担框架验证实例职能，仅作为 industrial-practice knowledge source 喂给 pattern library 与 aviation profile；验证实例见 `docs/08_validation/`。

## Phase 8 — MBSE Metamodel

在 DBSE workflow 和 information model 足够稳定后研究 SysML、SysML v2、schema、graph representation 与 executable constraints。

## Phase 9 — Automation

研究 traceability checking、coverage checking、impact analysis、model validation 与 document generation。不得在信息模型稳定前固化工具规则。本阶段产出为**非产品化的 Verification Platform 研究原型**——方法论与模型化架构的执行和演示载体，不进行产品化开发。

## Phase 10 — Cross-Domain Validation

以 **ARINC 615A 协议符合性验证**为 first instance，以无人机飞管系统验证与 LLM 服务可靠性与性能验证为后续实例，按实例 × 框架元素锻炼矩阵（`docs/08_validation/`）评价 completeness、traceability、repeatability、scalability、reusability 和 Evidence quality。DCAS 不作为验证实例。

## Phase gates

每阶段进入下一阶段前，应明确：依赖是否满足、哪些对象已 baseline、哪些仍为 working/TBD、开放问题及可审计产物。
