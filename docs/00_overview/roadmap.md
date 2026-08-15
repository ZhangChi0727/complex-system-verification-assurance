---
title: Research Roadmap
status: baseline
version: 0.1
baseline: v0.1
owner: research
last_updated: 2026-08-15
dependencies:
  - research_scope.md
  - research_questions.md
---

# Research Roadmap

## Phase 0 — Repository & Practice Baseline

建立 Research Baseline v0.1、知识架构、研究边界、工作术语、贡献规则和 future workspace。当前 PR 属于本阶段。

## Phase 1 — Normative Foundation

系统研究 ISO/IEC/IEEE 15288、ISO/IEC/IEEE 24748、INCOSE、NASA Systems Engineering Handbook、SAE ARP4754B、SAE ARP4761A、RTCA DO-178C、DO-254、DO-297 及适用补充标准。仅在合法取得全文和准确定位后形成规范性结论。

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

研究以下 working architecture：

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
V10 Regression
V11 Coverage & Sufficiency Assessment
V12 Verification Closure
```

V0–V12 是 research hypothesis / working architecture，尚未声明已由标准完整验证。

## Phase 4 — Verification Information Architecture

定义 candidate entities、字段、关系、状态、ownership、traceability 和 configuration semantics。

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
