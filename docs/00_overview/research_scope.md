---
title: Research Scope
status: baseline
version: 0.7
baseline: post-v0.2
owner: research
last_updated: 2026-08-25
dependencies: []
---

# Research Scope

## Research objective

建立标准可追溯、过程可执行、证据可审计、规则可检查、模型可实现、领域可复用的复杂系统 Verification Assurance Framework。

主要工程研究成果定位为 **Candidate Generic Verification Suite Core (Candidate GVS Core)**：把产品无关 Verification Methodology、候选 Model-Based Verification Architecture 及其 evaluation contracts 组织为可版本化、可组合的 Verification Capability Packages。machine-readable/executable platform 是可选表达、演示或评价载体，不是必须的软件产品。

```text
Complete Verification Suite
= Candidate Generic Verification Suite Core
+ Verification Profile
+ Product Binding
+ Project Configuration
```

Capability Package 是 Candidate GVS Core 的模块化交付单元，不是并列第五层，也不必是软件 package。Candidate GVS Core 是主要工程成果的 working research position，不表示 novelty 已建立。

对待现有标准的态度：方法论不得与现有标准相矛盾（"标准说了什么"是构建依据）；对标准未覆盖空白的填补是本研究的创新点（"标准没说什么"是创新空间）。二者均登记于 normative foundation，前者形成约束登记，后者形成 gap / 创新清单。

## In scope

- complex systems verification engineering；
- Verification Assurance 与 requirements-based verification；
- Verification lifecycle、strategy、level、methods 与 techniques；
- Coverage、Verification Sufficiency、Traceability、Evidence 与 Compliance Argument；
- Configuration、Anomaly、Change Impact & Re-verification 与 Verification Closure；
- DBSE workflow 与 information architecture；
- MBSE realization、domain instantiation 与后续 automation。

## Primary industrial context (knowledge source)

主要行业语境是 civil aviation / avionics。**DCAS — Display and Crew Alerting System** 的角色是 **Industrial Practice Knowledge Source**：为 aviation profile 与 Verification Pattern Library 提供工程模式来源；它不是 Normative Verification Standard，也**不作为框架验证实例**。

## Validation instances

框架验证（RQ8）采用多领域实例，覆盖方法论的不同应力面：

- **ARINC 615A 协议符合性验证** — first instance：确定性、规范驱动，检验 Core/Profile/Binding/Configuration 隔离以及 design–execution 下半链；
- **无人机飞管系统验证** — planned：安全驱动 rigor，检验 assurance constraints、typed independence、coverage 与 change impact；
- **LLM 服务可靠性与性能验证** — planned：概率性、弱 oracle，检验 sufficiency、evidence/argument 与 coverage 定义边界。

实例定位与实例 × 框架元素锻炼矩阵见 `docs/08_validation/`。实例相关标准（如符合性测试方法论）按抽象原则进入 generic layer，不作为单一实例的专属资产。

**强契约、弱实现耦合**：本仓库控制 Candidate GVS Core 的通用语义、关系、extension-point contract、版本/兼容规则与评价协议；实例仓库控制 Profile、Binding、Configuration、执行工具、具体 Oracle 和原始证据。versioned object registry 建立前使用受控临时映射；实例 finding 只能经 Framework Change Proposal、跨实例相关性分析、依据与独立评审后影响 canonical definition。完整规则见 [Cross-Repository Instance Contract](../08_validation/cross_repository_instance_contract.md)。

## Out of scope for v0.1

- 建立完整 DCAS 产品规范或复现 proprietary system design；
- 建立完整 DO-178C software assurance 或 DO-254 hardware assurance process；
- 自行定义适航法规或声称框架已获认证机构认可；
- 完成标准条款研究、正式 normative gap analysis 或 framework validation；
- 完成 SysML/MBSE implementation 或开发 automation tools；
- 将 Candidate GVS Core 等同现成软件库，或要求其当前直接可执行；
- 将验证平台产品化；machine-readable/executable realization 仅作为可选表达、演示或评价载体；
- 提交受版权限制的标准全文、内部培训材料或 confidential interfaces。

## Complete-suite ownership boundary

| Layer | Controlled responsibility | Excluded from Candidate GVS Core |
|---|---|---|
| Candidate GVS Core | product-independent semantic contracts and Capability Packages | domain/product/project-specific choices |
| Verification Profile | domain or verification-type specialization | concrete product interface and run configuration |
| Product Binding | product/protocol/tool/Oracle realization mapping | authority to redefine Core semantics |
| Project Configuration | selected versions, setup, parameters and project controls | reusable Generic/Profile definition |

ARINC 615A is the first controlled **legacy-to-framework migration instance**. Its active pre-framework baseline is evaluated rather than retrospectively relabelled; one instance cannot close RQ8 or establish generalization rights.
## Research abstraction boundary

| Layer | Meaning | Example |
|---|---|---|
| Generic Core | 跨产品仍成立的对象、关系和 assurance semantics | Verification Obligation、Strategy、Evidence、Provenance、Composite Gate |
| Generic Extension Point | Framework 确认需要、但 taxonomy/criteria/authority 由 profile 决定的维度 | Assurance/Independence Constraint、Coverage Obligation、Sufficiency Assessment、Assumption |
| Domain Profile | 特定行业规则对 Generic Core/extension points 的受控特化 | Civil Aviation FDAL/IDAL、Safety Requirement、SSA/ASA、typed independence |
| Concrete Project Practice | 特定组织、项目、工具或配置采用的做法 | 项目审批流、具体台架与记录格式 |

任何内容进入通用层前都必须回答：更换领域后该规则是否仍然成立，以及它的 normative basis 或 research rationale 是什么。

行业实践与实例相关标准向通用层的吸收遵循显式**抽象阶梯**：

```text
Domain Profile 实践 / 条款（保留 source provenance）
  → 候选 pattern
  → generic pattern / generic-layer 研究对象（声明抽象依据）
  → 经至少一个非源领域实例检验后进入方法论
```

## v0.2 conceptual-baseline boundary

五源 consolidation 的 verdict 是 `CONDITIONALLY READY FOR v0.2 CONCEPTUAL BASELINE`。v0.2 保存经过评审的概念检查点、稳定 V-ID、Generic/Profile boundary、evidence/change/gate semantics 和受控 open gaps；其历史 tag、来源定位与当时审阅结论保持不变。现行架构成熟度为 `OPEN-CANDIDATE`：V0–V12 的名称与 mixed-ontology 分类是当前工作基线，不关闭后续规范来源对元素语义、边界、拓扑、信息项、角色、权威、迭代/重新进入或门禁组成的受控影响。

本仓库当前明确不声明：

- planned normative-source cohort 已完成研究或综合处置；
- 已通过 architecture freeze 并达到 `CONTROLLED-BASELINE`；
- 已形成认证机构接受准则或 certification readiness；
- executable schema、cardinality、state machine 或自动化规则已经冻结。
