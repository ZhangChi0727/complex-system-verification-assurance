---
title: Research Questions
status: baseline
version: 0.5
baseline: v0.2
owner: research
last_updated: 2026-08-25
dependencies:
  - research_scope.md
  - ../01_normative_foundation/research_tasks/README.md
---

# Research Questions

以下问题在 v0.1 全部保持 `Open`，本基线不提前给出答案。

当前 standards-research task ownership、typed source-role coverage、开放缺口和反证路径见 [Normative Research Task Register](../01_normative_foundation/research_tasks/README.md#rq-and-innovation-candidate-coverage)。该链接只分配研究责任，不构成 RQ 答案或关闭证据；Task 022 可把独立评审后的记录综合为 RQ1–RQ7 standards-evidence answer drafts，但对 RQ8 只形成 `OPEN` validation-readiness handoff，最终回答依赖三个实例的受控评价结果。

## RQ1 — Normative foundation

复杂系统 Verification 的规范性基础是什么？

**Status:** Open
## RQ2 — Lifecycle

复杂系统 Verification 的完整生命周期是什么？

**Status:** Open

## RQ3 — Verification Strategy

如何系统确定 `Level + Method + Technique + Environment + Oracle + Coverage + Evidence`？

**Status:** Open

## RQ4 — Verification Sufficiency

如何定义 Verification Sufficiency，且为什么 Requirement Coverage 本身不足以证明充分性？

**Status:** Open

**v0.2 partial progress:** `SufficiencyAssessment` 的 generic I/O interface 已冻结（inputs / conclusion / rationale / residual gaps / decision context，见 consolidation §13 与 ISO-G03A）；**推理语义——为何 coverage 不足以证明充分、异构证据如何聚合为 reasoned conclusion、阈值与 decision authority——保持 open**（ISO-G03B），由 Phase 5 构建并经 UAV FMS 与 LLM 服务实例检验。接口冻结不得被解读为 RQ4 已闭合；充分性语义是框架核心论题（见 research_scope"标准没说什么"创新登记）。

## RQ5 — Evidence and claim

Verification Evidence 如何通过可审查的 Assurance Argument 支持 Compliance Claim？

**Status:** Open

## RQ6 — Reusable patterns

哪些 Verification Techniques 可以抽象为产品无关的 Verification Patterns？

**Status:** Open

## RQ7 — DBSE to MBSE

DBSE Verification Workflow 如何形成机器可解释、可查询和可检查的 MBSE information model？

Machine-readable/executable realization 是 Candidate GVS Core 的候选表达和评价载体；本研究问题不把 Candidate GVS Core 等同于软件产品。

**Status:** Open

## RQ8 — Framework validation

如何通过多领域实例（ARINC 615A 协议符合性验证为 first instance，无人机飞管系统验证与 LLM 服务可靠性与性能验证为后续实例）验证 framework 的 completeness、traceability、repeatability、scalability 与 reusability？

ARINC first-instance evaluation 由 [ARINC 615A Instance Evaluation Protocol](../08_validation/arinc_615a_instance_evaluation_protocol.md) 控制，只形成部分实例证据；它不能单独关闭 RQ8。

**Status:** Open
