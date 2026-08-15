---
title: ISO/IEC/IEEE 15288:2023 Informal Research Review
status: closed
version: 0.2
baseline: v0.1
owner: research
last_updated: 2026-08-15
review_type: informal
review_result: changes-requested-minor-to-moderate
corrections_applied: true
review_scope:
  - ../standard_notes/iso_15288.md
  - ../standards_map.md
  - ../normative_gap_matrix.md
source:
  standard: ISO/IEC/IEEE 15288:2023
  source_type: licensed-local-source-not-committed
---

# ISO/IEC/IEEE 15288:2023 Informal Research Review

## Review purpose

本记录保存 ISO/IEC/IEEE 15288:2023 首轮研究的非正式评审 provenance。评审对象包括 clause-level research note、cross-standard map 和 normative gap matrix。该评审不代表最终 normative baseline；其作用是记录发现、修正决定以及修正后的 baseline-candidate 状态。

原始评审形成于 ISO 24748-1 研究之前。为避免研究计划随来源数量变化而漂移，本归档使用 `initial cross-standard consistency review` 表示后续一致性复核阶段，不保留固定标准数量作为 baseline 条件。

## Review result

```text
Review result: CHANGES REQUESTED — Minor-to-Moderate
Corrections applied: Yes
Research status after correction: Reviewed
Baseline readiness: Candidate
```

研究方法和主要分类纪律可接受，但首个 normative baseline candidate 需要提高 clause-level accuracy、normative/informative 分类精度、direct/indirect support 边界，以及 framework abstraction 与标准原生概念的区分。

## Confirmed strengths

### Source and conformance discipline

研究明确区分 `NORMATIVE`、`INFORMATIVE`、`INTERPRETATION`、`FRAMEWORK IMPLICATION` 和 `RESEARCH PROPOSAL`，并保留 Clause 4 的 outcome-based、task-based 和 tailored conformance 边界。该纪律应继续用于后续标准研究。

### Verification Strategy

ISO 15288 6.4.9 直接支持定义 Verification Strategy，但不规定 repository 的完整 VSR schema。`oracle`、`coverage_obligations` 等字段继续保持 research proposal 或待跨标准验证状态。

### Method and technique taxonomy

Inspection、Analysis、Demonstration 和 Testing 是 Verification Method 的 informative examples；peer review 是 Inspection 示例，modelling/simulation/analogy 是 Analysis 示例。Boundary Value、State Transition、Fault Injection 等 technique 不应被误标为 ISO 定义的一级 Method。

### Traceability and assurance

Clause 5.10 支持 Claim–Argument–Evidence 结构，因此 `Traceability ≠ Assurance Argument`。Evidence Architecture 不应退化为 requirement-to-test trace matrix，coverage 和 sufficiency 也不能由 trace completeness 自动推出。

### Gaps retained

Verification independence、coverage、sufficiency、Oracle、Regression、Verification Closure、information-item schema 和 MBSE/model evidence 均是有效研究空间。Re-verification 有标准支持，但通用 Regression process/selection algorithm 不是 ISO 15288 原生概念。

## Blocking finding and applied correction

### Requirement definition — Clause 3.36

**Finding:** 初始研究误用了另一种常见 requirement 定义，没有反映 ISO/IEC/IEEE 15288:2023 Clause 3.36。

**Required correction:** Requirement 应解释为表达或转化某项 need，并包含 associated constraints and conditions 的 statement。Requirement information model 必须保留这些约束和条件，不能只表示期望行为。

**Resolution:** 已修正 `iso_15288.md`、working terminology 和相关 framework implication。该问题不再阻塞 baseline-candidate 状态。

## Required classification refinements and resolutions

### Requirement validation

**Finding:** 不能把 Requirement Validation 简单等同于 6.4.11 Validation Process。

**Resolution:** 映射已区分：

- stakeholder requirements 的直接 task-level support：6.4.2.3(e)(3)；
- system requirements review 及其 validation relationship：6.4.3.3(c)(3) 与相关 informative note；
- general artefact relationship：6.4.11 的 informative note；
- stakeholder/system requirement validation 与 complete system/product validation 分别建模。

### V2 Requirement Verifiability Analysis

**Finding:** requirement quality/verifiability analysis 的功能支持程度被低估。

**Resolution:** V2 改为 `Directly Supported in function; framework-defined in activity boundary/name`。6.4.2.3(e) 与 6.4.3.3(c) 直接支持 requirement-set analysis，但 V2 名称、独立边界和 orchestration 仍是 framework abstraction。

### V0 Verification Planning

**Finding:** 6.3.1 Project Planning 是 supporting process，不是独立 Verification Planning 的直接定义。

**Resolution:** 映射已拆分为：

- direct preparation support：6.4.9.3(a)；
- indirect/supporting project-planning support：6.3.1；
- V0 名称和边界继续保持 framework-defined。

### V9 Anomaly Resolution

**Finding:** Verification Process 直接支持 results/anomalies/problems 的记录和跟踪，但 root-cause analysis、corrective action 和 technical change 跨越多个 supporting/technical processes。

**Resolution:** V9 改为直接支持的 anomaly-management concern 加 cross-process framework orchestration，不再描述为单一 ISO-native Verification activity。

## Gap-matrix review

以下 gap 经评审后保留：

| ID | Topic | Review conclusion |
|---|---|---|
| ISO-G01 | Verification independence | QA independence 不能重标为 Verification independence；等待航空标准 |
| ISO-G02 | Verification coverage | traceability 不提供通用 coverage taxonomy |
| ISO-G03 | Verification sufficiency | Claim–Argument–Evidence 不提供统一 sufficiency formula |
| ISO-G04 | Oracle | success criteria/expected results 不建立独立 Oracle entity |
| ISO-G05 | Regression | re-verification 有支持；通用 Regression process/selection rules 仍缺失 |
| ISO-G06 | Verification closure | approval、traceability、assessment 和 baseline support 不构成完整 Closure process |
| ISO-G07 | Information-item schema | 需要 ISO/IEC/IEEE 15289 等来源补充 field-level basis |
| ISO-G08 | MBSE automation/model evidence | Annex D 为 informative，不规定 MBSE、工具或 evidence-admissibility regime |

## Follow-up implications

- ISO/IEC/IEEE 29148 保持 requirements-engineering backlog，用于 requirement characteristics、needs-to-requirements transformation 和 requirements information items；
- ISO/IEC/IEEE 15289 保持 information-item schema 的重要后续来源；
- independence、coverage 和 rigor 等结论等待 ARP4754B、ARP4761A、DO-178C、DO-254 等来源约束；
- 最终 classification 等待 initial cross-standard consistency review，而不是由固定来源数量决定。

## Final review position

所有 blocking 和 classification findings 已在当前研究资产中得到处理。ISO/IEC/IEEE 15288:2023 研究可以保持：

```text
Research status: reviewed
Baseline readiness: candidate
Final normative baseline: not yet established
```

核心研究原则保持不变：标准用于约束和修正 Framework，而不是用于证明预设 Framework 必然正确。
