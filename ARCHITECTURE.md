---
title: Repository and Knowledge Architecture
status: baseline
version: 0.5
baseline: post-v0.2
owner: research
last_updated: 2026-08-25
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

- `README.md` / `project-status.json`：唯一当前状态界面与机器可读状态；耐久事实仍由 `docs/`、`models/`、`data/`、`domains/` 及不可变 Git 身份支撑。
- `publications/`：论文和教程的发布视图，不是独立事实源。
- `archive/`：superseded baseline 或 legacy transformation material；不能替代 Git history。

核心定义只在 `docs/`、`models/`、`data/` 和 `domains/` 中维护。`publications/` 只能引用、重组或解释这些资产，避免 configuration drift。

**Definition ownership：** framework-defined 对象的对象级定义、晋级决定与 provenance 以 five-source consolidation report 的 provenance annex（§28）为唯一权威登记；`terminology.md`、`templates/`、`standards_map.md`、`normative_gap_matrix.md` 只引用不重定义。后续迁入 `data/` 结构化形态时该权威随迁。

## Abstraction boundary

```text
Complete Verification Suite
= Candidate Generic Verification Suite Core
+ Verification Profile
+ Product Binding
+ Project Configuration
```

The Candidate GVS Core owns product-independent semantic contracts and Verification Capability Packages. A Verification Profile specializes domain or verification-type policy; a Product Binding maps those contracts to product/protocol/tool assets and concrete Oracle implementations; Project Configuration selects immutable versions, setup and run controls. Capability Packages remain inside the Core and are not a fifth layer or necessarily software.

The method repository controls Candidate GVS Core definitions and the cross-instance evaluation contract. External instance repositories control Profile/Binding/Configuration implementations and raw evidence. They are read-only evidence/finding providers from this repository's perspective and cannot redefine Core semantics without the [cross-repository change path](docs/08_validation/cross_repository_instance_contract.md).

如果把 DCAS 替换成汽车 EPS、无人机或其他复杂系统后某规则仍然成立，它才可能成为 Candidate GVS Core 研究对象；依赖 IDU、IMA/GPM、ARINC 总线、告警抑制、具体产品接口或项目参数的内容进入 Profile、Binding 或 Configuration。该判断仍需 normative/research rationale 与跨实例评价，不能由单一实例直接晋级。

本分层不建立 executable architecture，也不冻结 API、schema、metamodel、serialization、SysML role 或 versioned object registry。

## Architecture maturity and controlled openness

**V0–V12 is a controlled open candidate architecture.** Stable V-identifiers are retained for traceability and impact analysis. The current element names and ontology classifications form a reviewed conceptual checkpoint, while element semantics, boundaries, ordering, entry/exit criteria, information-item assignments, roles, decision authority, iteration/re-entry rules and assurance-gate composition remain subject to controlled revision until the planned normative-source cohort has completed clause-level study, independent review and architecture-impact disposition.

**V0–V12 是受控开放的候选架构。** V 编号为保持可追溯性和影响分析连续性而稳定保留。当前元素名称及本体分类构成经过评审的概念检查点；但元素语义、边界、顺序、进入/退出条件、信息项分配、角色、决策权威、迭代/重新进入规则及保证门禁组成，在计划规范来源完成条款研究、独立复核和架构影响处置前均可通过受控变更修订。

`research-baseline/v0.2` 是真实且不可改写的 historical conceptual checkpoint，不是关闭未来 normative-source impact 的最终架构冻结。当前分层如下：

- **稳定保留：** `V0`–`V12` 标识、历史来源定位、既有评审记录和变更追溯；
- **当前概念检查点：** 元素名称、mixed-ontology 分类、V10/V11 当前契约、V6/V12 composite-gate 假设；
- **保持开放：** 元素语义和边界、执行拓扑与顺序、迭代/回退、entry/exit criteria、信息项、角色和权威、状态机、schema 与门禁充分性规则。

| Architecture maturity | Meaning |
|---|---|
| `OPEN-CANDIDATE` | Planned standards research can still modify architecture semantics, boundaries or topology; current repository state. |
| `REVIEWED-PROVISIONAL` | The planned source cohort is substantially studied and synthesized, while controlled instance feedback remains admissible. |
| `CONTROLLED-BASELINE` | Architecture objects and gates have passed a formal freeze review; later changes require impact analysis and migration. |
| `VALIDATED-BASELINE` | ARINC 615A, UAV FMS and LLM service evaluations plus cross-instance synthesis have been independently reviewed; RQ8 closure is separately justified. |

Promotion on this axis is sequential: normative-source reconciliation and Task 022 can support `OPEN-CANDIDATE → REVIEWED-PROVISIONAL`; a formal architecture freeze, version/migration review and controlled change rules are required for `REVIEWED-PROVISIONAL → CONTROLLED-BASELINE`. Instance execution does not itself promote Architecture maturity. `VALIDATED-BASELINE` and RQ8 closure require all three planned instances and independently reviewed cross-instance synthesis.

### Instance evaluation state

Instance evaluation is a separate, orthogonal state dimension. `INSTANCE-EXERCISED` means only that one immutable method-definition context has undergone a bounded evaluation by one controlled instance and that the resulting findings have been reviewed. It may coexist with `OPEN-CANDIDATE`, `REVIEWED-PROVISIONAL` or `CONTROLLED-BASELINE`; it neither changes Architecture maturity nor establishes cross-domain validation. An instance that has not met those conditions remains `NOT-EXERCISED` for the identified method context.

Every later clause study must record an architecture-impact disposition in `docs/01_normative_foundation/consolidation/architecture_impact_register.md`. Allowed dispositions are `CONFIRM`, `EXTEND`, `MODIFY`, `SPLIT`, `MERGE`, `NO-IMPACT` and `DEFERRED`. A `MODIFY`, `SPLIT` or `MERGE` disposition requires an explicit compatibility/migration note and may not silently rewrite the historical meaning of a stable V-ID.

## Document status taxonomy

- `working`：正在研究，尚未形成受控基线；
- `baseline`：已纳入当前研究基线；
- `planned`：已预留范围，但依赖尚未满足；
- `superseded`：已被新基线替代。

## Candidate object prefixes

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

这些只是 candidate prefixes，不是 stable IDs。versioned object registry 建立前，仓库内外使用受控临时映射。稳定引用至少需要 `ObjectID`、`ObjectVersion`、`DefinitionVersion`、`IntroducedIn`、`SupersededBy`、`Status`、`CanonicalLocator` 与 `CompatibilityRule`。对象分级、来源属性与 schema gate 见 `docs/01_normative_foundation/consolidation/five_source_consistency_gap_review.md` §28 annex。
