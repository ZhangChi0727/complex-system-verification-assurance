---
title: Complex System Verification Assurance Framework
status: baseline
version: 0.3
baseline: post-v0.2
owner: research
last_updated: 2026-08-19
dependencies: []
---

# Complex System Verification Assurance Framework

**面向复杂系统的验证保证框架研究——基于国际系统工程与民机开发保证规范的 DBSE/MBSE 方法**

English working title: *A Verification Assurance Framework for Complex Systems: From Document-Based to Model-Based Verification Engineering*

## Why this research exists

复杂系统已经积累大量 Verification 工程实践，但 standard requirements、organizational procedures、testing techniques、domain-specific knowledge、evidence management 与 tooling 往往混杂。本项目将这些内容按可追溯的研究层级重新组织：

```text
Normative Requirements
        ↓
Verification Assurance Framework
        ↓
DBSE Workflow
        ↓
Information / Coverage / Evidence Architecture
        ↓
MBSE → Automation → Domain Applications
```

目标是建立一套标准可追溯、过程可执行、证据可审计、规则可检查、模型可实现、领域可复用的复杂系统 Verification Assurance Framework。

## Research objectives

1. 建立 normative foundation；
2. 形成 product-independent verification methodology；
3. 定义 DBSE Verification Workflow；
4. 建立 Verification Strategy 决策方法；
5. 研究 Coverage 与 Verification Sufficiency；
6. 建立 Evidence Architecture 与 Compliance Argument；
7. 建立 Verification Pattern Library；
8. 形成 MBSE verification metamodel；
9. 支持一致性、覆盖与影响分析自动化；
10. 通过多领域实例（ARINC 615A 协议符合性验证、无人机飞管系统验证、LLM 服务可靠性验证）验证框架。

## Current baseline

```text
Current Research Baseline: v0.2
Status: Conceptual Normative-Foundation Baseline
Repository maturity: Normative-foundation research late stage / conceptual architecture early stage
```

[`research-baseline/v0.2`](docs/00_overview/research_baseline_v0.2.md) 冻结五源 normative foundation、V0–V12 conceptual ontology、generic/profile 边界及 PR #6 的实例定位和 meta-risk governance。它不是完整方法论产品基线，不代表 executable architecture、certification acceptance 或 framework validation 已建立。后续标准研究和治理变更均作为 post-v0.2 增量管理。

## Repository map

| Path | Purpose | Current status |
|---|---|---|
| `docs/00_overview/` | 研究范围、问题、术语、路线与创新主张/边界 | baseline |
| `docs/01_normative_foundation/` | 标准研究目标、矩阵与 gap workspace | working |
| `docs/02_verification_framework/` | 产品无关 Verification Assurance Framework | planned |
| `docs/03_dbse_workflow/` | DBSE working lifecycle | planned |
| `docs/04_information_model/` | Verification information entities and relations | planned |
| `docs/05_coverage_and_evidence/` | Coverage、Sufficiency、Evidence 与 Argument | planned |
| `docs/06_pattern_library/` | 通用 Verification Patterns | planned |
| `docs/07_mbse/` | 机器可读模型与 MBSE realization | planned |
| `docs/08_validation/` | 验证实例定位与实例 × 框架元素锻炼矩阵 | working |
| `domains/` | 领域 profile 与知识源（DCAS）；与 generic methodology 隔离 | working |
| `models/`, `data/`, `tools/` | 后续模型、结构化数据与自动化 | planned |
| `references/` | 检索策略、书目和阅读记录 | working |
| `templates/` | DBSE research draft templates | working |
| `HANDOFF/` | 仓库当前进度与下一步计划（交接快照，非事实源） | working |
| `publications/` | 论文与教程发布视图 | planned |

## Research principles

- Standards before framework rules.
- DBSE before MBSE.
- Generic methodology is separated from domain examples.
- Traceability is not equivalent to an Assurance Argument.
- Test is not equivalent to Verification.
- Requirement Coverage alone does not prove Verification Sufficiency.
- Automation follows stable information models.
- No normative claim without an identifiable basis.

## Expected outputs

1. Research Repository；
2. 产品无关的 Verification Methodology；
3. Model-Based Verification Architecture（machine-readable metamodel）；
4. 非产品化的 Verification Platform 研究原型；
5. Academic Paper / Thesis 与 Engineering Handbook / Tutorial。

## Copyright and license

不要提交 SAE、RTCA、EUROCAE 等受版权限制的标准全文，或 proprietary DCAS/项目资料。仓库原创内容采用 [MIT License](LICENSE)；第三方材料仍受各自权利人的许可约束。
