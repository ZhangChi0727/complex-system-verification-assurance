---
title: Repository and Knowledge Architecture
status: baseline
version: 0.2
baseline: v0.1
owner: research
last_updated: 2026-08-17
dependencies: []
---

# Repository and Knowledge Architecture

本仓库按研究资产与知识层级组织，而不是按论文 chapter 组织。论文目录会随叙事调整，规范来源、框架对象、领域实例和模型数据则需要稳定归属与可追溯关系。

## Knowledge chain

```text
Normative Source
      ↓
Framework Rule
      ↓
Verification Activity
      ↓
Information Item
      ↓
Verification Strategy
      ↓
Verification Pattern
      ↓
Domain Profile
      ↓
Concrete Case
      ↓
Evidence
      ↓
Compliance Claim
      ↓
Model Element
      ↓
Automation Rule
```

链条表示研究对象间的目标关系，不表示 v0.1 已经证明所有关系成立。任何 Framework Rule 都必须标明 direct normative requirement、guidance、interpretation、industrial practice 或 research proposal。

## Repository layers

- `docs/`：产品无关的方法论。标准研究先于框架规则，DBSE workflow 先于 MBSE realization。
- `domains/`：领域 profile 与 industrial-practice knowledge source（如 DCAS）。Domain Profile 不能反向污染 generic framework；框架验证实例统一由 `docs/08_validation/` 管理，不在此层实例化。
- `models/`：从稳定的 DBSE 信息模型迁移到 metamodel、schema、SysML/SysML v2 或图表示。
- `data/`：standards matrix、traceability、coverage 和其他机器可读数据。
- `references/`：合法 bibliographic metadata、检索策略、阅读记录和不可公开资料的定位说明。
- `tools/`：未来的一致性、覆盖、影响分析、模型校验和文档生成工具。
- `examples/`：脱敏、最小可复现和端到端研究实例。
- `publications/`：论文和教程的发布视图，不是独立事实源。
- `archive/`：superseded baseline 或 legacy transformation material；不能替代 Git history。

核心定义只在 `docs/`、`models/`、`data/` 和 `domains/` 中维护。`publications/` 只能引用、重组或解释这些资产，避免 configuration drift。

**Definition ownership：** framework-defined 对象的对象级定义、晋级决定与 provenance 以 five-source consolidation report 的 provenance annex（§28）为唯一权威登记；`terminology.md`、`templates/`、`standards_map.md`、`normative_gap_matrix.md` 只引用不重定义。后续迁入 `data/` 结构化形态时该权威随迁。

## Abstraction boundary

```text
Generic Framework
      ↓ instantiates
Domain Profile
      ↓ specializes
Concrete Project Practice
```

如果把 DCAS 替换成汽车 EPS、无人机或其他复杂系统后某规则仍然成立，它原则上属于 Generic Framework；依赖 IDU、IMA/GPM、ARINC 总线、告警抑制或具体组织流程的内容进入 Domain Profile 或 Concrete Project Practice。

## Document status taxonomy

- `working`：正在研究，尚未形成受控基线；
- `baseline`：已纳入当前研究基线；
- `planned`：已预留范围，但依赖尚未满足；
- `superseded`：已被新基线替代。

## Candidate stable IDs

| Prefix | Object | Example |
|---|---|---|
| `STD-` | Standard / normative source | `STD-ARP4754B` |
| `ACT-` | Verification activity | `ACT-V03-001` |
| `VOB-` | Verification obligation | `VOB-0001` |
| `VSR-` | Verification strategy record | `VSR-0001` |
| `PAT-` | Verification pattern | `PAT-BVA-01` |
| `COV-` | Coverage object | `COV-REQ-01` |
| `EVD-` | Evidence | `EVD-0001` |
| `CLM-` | Compliance claim | `CLM-0001` |
| `ANM-` | Anomaly | `ANM-0001` |

这些前缀是 v0.1 候选约定，不在本基线实现自动编号工具。对象的分级、来源属性（source-native / framework-defined）与 schema gate 登记见 `docs/01_normative_foundation/consolidation/five_source_consistency_gap_review.md` §28 annex。
