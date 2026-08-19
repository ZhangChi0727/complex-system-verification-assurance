---
title: Research Scope
status: baseline
version: 0.5
baseline: v0.1
owner: research
last_updated: 2026-08-19
dependencies: []
---

# Research Scope

## Research objective

建立标准可追溯、过程可执行、证据可审计、规则可检查、模型可实现、领域可复用的复杂系统 Verification Assurance Framework。

最终产出为三层递进：**产品无关的 Verification Methodology → 该方法论的 Model-Based Verification Architecture → 非产品化的 Verification Platform 研究原型**。

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

- **ARINC 615A 协议符合性验证** — first instance：确定性、规范驱动，检验 Verification Basis/Obligation → Case/Procedure → Oracle/verdict → 平台执行链；
- **无人机飞管系统验证** — planned：安全驱动 rigor，检验 assurance constraints、typed independence、coverage 与 change impact；
- **LLM 服务可靠性与性能验证** — planned：概率性、弱 oracle，检验 sufficiency、evidence/argument 与 coverage 定义边界。

实例定位与实例 × 框架元素锻炼矩阵见 `docs/08_validation/`。实例相关标准（如符合性测试方法论）按抽象原则进入 generic layer，不作为单一实例的专属资产。

**方法论与实例彻底解耦**：本仓库的通用验证方法论细化至 implementation framework 层级（信息模型、metamodel、平台参考架构、评价判据）；实例执行在独立外部仓库进行（首个：ARINC 615A 符合性验证实例仓库），必须引用本仓库稳定对象 ID 而非重定义。解耦契约与创新主张/工作边界见 `innovation_statement.md`。

## Out of scope for v0.1

- 建立完整 DCAS 产品规范或复现 proprietary system design；
- 建立完整 DO-178C software assurance 或 DO-254 hardware assurance process；
- 自行定义适航法规或声称框架已获认证机构认可；
- 完成标准条款研究、正式 normative gap analysis 或 framework validation；
- 完成 SysML/MBSE implementation 或开发 automation tools；
- 将验证平台产品化；平台仅作为方法论与模型化架构的研究原型和执行载体；
- 提交受版权限制的标准全文、内部培训材料或 confidential interfaces。

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

五源 consolidation 的 verdict 是 `CONDITIONALLY READY FOR v0.2 CONCEPTUAL BASELINE`。这允许冻结稳定 terminology、V0–V12 ontology、Generic/Profile boundary、evidence/change/gate semantics 与受控 open gaps；不允许宣称 executable schema、统一 coverage/sufficiency algorithm、item-level assurance completeness、certification acceptance 或 framework validation 已完成。
