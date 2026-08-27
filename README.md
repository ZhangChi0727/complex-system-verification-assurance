---
title: Complex System Verification Assurance Framework
status: baseline
version: 0.6
baseline: post-v0.2
owner: research
last_updated: 2026-08-26
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

本研究的主要工程成果定位为 [Candidate Generic Verification Suite Core (Candidate GVS Core)](docs/02_verification_framework/generic_verification_suite_core.md)：由可组合的 Verification Capability Packages 交付产品无关语义契约，并通过 Verification Profile、Product Binding 与 Project Configuration 形成完整验证套件。machine-readable/executable platform 仅是可选表达、演示或评价载体，不是必须的软件产品。

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
Repository maturity: Normative-foundation research late stage / architecture OPEN-CANDIDATE
```

[`research-baseline/v0.2`](docs/00_overview/research_baseline_v0.2.md) 保存五源 normative foundation、V0–V12 reviewed conceptual checkpoint、generic/profile 边界及 PR #6 实例定位和 meta-risk governance 的历史状态；稳定 V-ID 用于持续追踪。现行 V0–V12 语义、边界和拓扑仍由 `OPEN-CANDIDATE` 治理，不代表 executable architecture、certification acceptance 或 framework validation 已建立。后续标准研究和治理变更均作为 post-v0.2 增量管理。

当前跨仓库治理增量以 Candidate GVS Core 0.3 / 方法定义提交
`48dd8232b7efe6b0dba3fcb75dfc154d034d2b0b` 为不可变方法上下文。ARINC
615A v4.3 已作为 baseline ID `RB-2026-001-v4.3`、普通 merge commit
`523d42bf03a1135b3d63a00bfb47d3b879d3927e` 和 annotated release tag
`v4.3` 发布。方法侧第三次握手提出
`REVIEWED-COMPATIBLE-WITH-QUALIFICATION` 条件处置：PR #15 未激活时正式
compatibility 为 `NOT-DETERMINED`；独立批准未变更 head 并以普通 merge commit
合并后自动转为受 Q-01–Q-09 限定的该处置。Project Configuration 仍未建立，实例
评价仍为 `NOT-EXERCISED`。该治理工作不改变 ISO 15289 Task 001 的当前研究停点。

## Repository map

| Path | Purpose | Current status |
|---|---|---|
| `docs/00_overview/` | 研究范围、问题、术语、路线与创新主张/边界 | baseline |
| `docs/01_normative_foundation/` | 标准研究目标、矩阵与 gap workspace | working |
| `docs/02_verification_framework/` | Candidate GVS Core、Capability Packages 与产品无关语义契约 | working |
| `docs/03_dbse_workflow/` | DBSE working lifecycle | planned |
| `docs/04_information_model/` | Verification information entities and relations | planned |
| `docs/05_coverage_and_evidence/` | Coverage、Sufficiency、Evidence 与 Argument | planned |
| `docs/06_pattern_library/` | 通用 Verification Patterns | planned |
| `docs/07_mbse/` | 机器可读模型与 MBSE realization | planned |
| `docs/08_validation/` | 跨仓库实例契约、临时登记、映射、评价协议与 RQ8 实例治理 | working |
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
2. 由 Verification Capability Packages 构成的 Candidate GVS Core（主要工程研究成果）；
3. Candidate Model-Based Verification Architecture 与可选 machine-readable representation；
4. 可选的非产品化 executable/demonstration realization 与评价载体；
5. Verification Profiles、Product Bindings、Project Configurations 的受控实例化契约；
6. Academic Paper / Thesis 与 Engineering Handbook / Tutorial。

## Copyright and license

不要提交 SAE、RTCA、EUROCAE 等受版权限制的标准全文，或 proprietary DCAS/项目资料。仓库原创内容采用 [MIT License](LICENSE)；第三方材料仍受各自权利人的许可约束。
