---
title: Research Roadmap
status: baseline
version: 0.9
baseline: v0.2
owner: research
last_updated: 2026-08-20
dependencies:
  - research_scope.md
  - research_questions.md
---

# Research Roadmap

## Phase 0 — Repository & Practice Baseline

建立 Research Baseline v0.1、知识架构、研究边界、工作术语、贡献规则和 future workspace。当前 PR 属于本阶段。

## Phase 1 — Normative Foundation

系统研究 ISO/IEC/IEEE 15288、ISO/IEC/IEEE 24748、INCOSE、NASA Systems Engineering Handbook、SAE ARP4754B、SAE ARP4761A、RTCA DO-178C、DO-254、DO-297、generic conformance-testing methodology 来源（ISO/IEC 9646 / ITU-T X.290 系列、ETSI TTCN-3）及适用补充标准。planned normative-source cohort 还包括 ISO/IEC/IEEE 15289:2019、15026-1:2025、15026-4:2021、12207:2026、29119-1/-2/-3/-4、IEEE 1012:2024、15026-3:2023 与 24748-3/-4/-5/-6/-10。仅在合法取得全文和准确定位后形成规范性结论；24748-8 保持 defence-domain profile/revision-watch 边界。

第一轮 five-source consolidation 已由 `research-baseline/v0.2` 保存为 historical conceptual checkpoint。post-v0.2 来源采用 Controlled Candidate-Source Baseline：候选登记、资料取得、条款研究和评审是不同状态，未研究来源不能关闭 gap。ISO/IEC/IEEE 29148:2018 与 15026-2:2022 的 clause studies 已通过独立评审，建立 Requirement/Basis→Obligation→Result 与 Evidence Item→Argument→Supported Claim/Inference 的受控接口；其中 evidence characterization 是受 15026-2, 5.3.2 约束的 framework-defined relation。后续按依赖驱动队列推进，并为每个来源登记 architecture-impact disposition；不开展 15026-1:2019 独立研究或 2019→2025 全文 delta。详细优先级见 `HANDOFF/next_plan.md`。

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

五源 consolidation 形成了 V0–V12 的 reviewed conceptual checkpoint：V-ID 稳定用于追踪和影响分析；V0–V5/V7 的 activity/information design、V8 的 evaluation/decision、V9–V10 的 cross-process orchestration、V11 的 assurance assessment 及 V6/V12 的 framework-defined Composite Gate 是当前 mixed-ontology 工作基线。架构成熟度为 `OPEN-CANDIDATE`；元素语义、边界、拓扑、iteration/re-entry、信息项、角色、权威和 gate composition 可由后续规范研究通过受控 impact disposition 修订。

## Architecture synthesis and controlled-freeze gate

Phase 3 之后、进入 architecture freeze 前必须满足：

- planned normative-source cohort 已完成 clause-level study，或具有明确且经评审的 `DEFERRED` disposition；
- 每项来源已在 Architecture Impact Register 中完成 `CONFIRM`、`EXTEND`、`MODIFY`、`SPLIT`、`MERGE`、`NO-IMPACT` 或 `DEFERRED` 处置；
- 架构冲突、兼容/迁移影响和 residual gaps 已登记；
- 独立 cross-source architecture synthesis review 已完成；
- ISO/IEC/IEEE 24748-10:2026 已研究并处置其 iteration、re-entry、tailoring 与 dynamic-environment 候选影响。

满足该 gate 后只能把成熟度推进到 `REVIEWED-PROVISIONAL`；不得从 `OPEN-CANDIDATE` 直接跳到 `CONTROLLED-BASELINE`。

This gate does not block Phase 4–7 working research; it controls promotion to `REVIEWED-PROVISIONAL` and any architecture, schema, metamodel or automation freeze.

## Phase 4 — Verification Information Architecture

定义 candidate entities、字段、关系、状态、ownership、traceability 和 configuration semantics。

五源 conceptual consolidation 已满足 working-level conceptual information-architecture exploration 的入口，但未满足 architecture/schema freeze。ISO 15289、15026、29119、12207、24748 及其他相关来源的条款研究和 impact disposition 仍需形成该 freeze gate 的输入；在 gate 通过前，entities、fields、relations、states 和 cardinalities 只能保持 candidate/working 状态，executable schema 不得冻结。29148/15026-2 已解析 conceptual item/view taxonomy 与 assurance-case recursive structure，但 executable schema、cardinality 和 15289 interoperability 仍开放。先研究 ISO 15289，再以 15026-1:2025 精化当前 assurance vocabulary，并在连接 2025 Claim 与 15026-2:2022, 5.3.3 前完成限定兼容性检查；不得从现有 YAML 字段倒推 ontology。

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
