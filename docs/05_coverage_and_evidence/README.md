---
title: Coverage and Evidence Workspace
status: conceptual-baseline
version: 0.2
baseline: v0.1
owner: research
last_updated: 2026-08-16
dependencies:
  - ../01_normative_foundation/README.md
  - ../04_information_model/README.md
---

# Coverage and Evidence Workspace

## Coverage research track

候选维度包括 Requirement、Function、Interface、State、Transition、Boundary、Input Domain、Scenario、Failure-Mode、Configuration、Source、Timing、Safety Objective 与 Structural Coverage。维度清单尚未冻结为 universal taxonomy。

这些维度不是所有系统都必须全部采用的统一强制集合。研究目标是建立：

```text
Coverage Obligation
= population/scope
+ criterion
+ evidence/result
+ uncovered disposition
+ configuration/context
```

Requirement Coverage、aviation Safety Coverage 以及未来 Code/Structural Coverage 是 profiles。Coverage Result 不自动证明 Sufficiency。

## Evidence research track

Working architecture：

```text
Observation / Raw Record
  → Result
  → may constitute or support Evidence
  → supports Argument
  → justifies Claim
```

Evidence identity、provenance、integrity/configuration、claim applicability、credibility 与 sufficiency contribution 分开评价。`Traceability ≠ Provenance ≠ Argumentation`：存在 trace link 不自动证明 evidence 足以支持 claim。

`SufficiencyAssessment` interface 已冻结为 generic extension point：它接收 obligations、coverage、evidence、limitations、assumptions、anomalies 与 assurance constraints，输出 conclusion、rationale、residual gaps 和 decision context；算法、threshold 和 authority 仍由 profile/项目决定。

**Status:** Conceptual baseline；等待 ISO 15289 information-item research 和后续 domain/item standards 完善 schema 与 criteria。
