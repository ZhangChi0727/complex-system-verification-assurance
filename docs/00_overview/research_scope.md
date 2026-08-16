---
title: Research Scope
status: baseline
version: 0.3
baseline: v0.1
owner: research
last_updated: 2026-08-16
dependencies: []
---

# Research Scope

## Research objective

建立标准可追溯、过程可执行、证据可审计、规则可检查、模型可实现、领域可复用的复杂系统 Verification Assurance Framework。

## In scope

- complex systems verification engineering；
- Verification Assurance 与 requirements-based verification；
- Verification lifecycle、strategy、level、methods 与 techniques；
- Coverage、Verification Sufficiency、Traceability、Evidence 与 Compliance Argument；
- Configuration、Anomaly、Change Impact & Re-verification 与 Verification Closure；
- DBSE workflow 与 information architecture；
- MBSE realization、domain instantiation 与后续 automation。

## Primary domain context

主要行业语境是 civil aviation / avionics，主要工业案例是 **DCAS — Display and Crew Alerting System**。DCAS 作为 Industrial Practice Source 和 Domain Profile，不作为通用 Verification 标准。

## Secondary validation domain

预留 **ARINC 615A** 作为 cross-domain validation candidate，用于检验框架的可复用性，而不是扩展 DCAS 教程。

## Out of scope for v0.1

- 建立完整 DCAS 产品规范或复现 proprietary system design；
- 建立完整 DO-178C software assurance 或 DO-254 hardware assurance process；
- 自行定义适航法规或声称框架已获认证机构认可；
- 完成标准条款研究、正式 normative gap analysis 或 framework validation；
- 完成 SysML/MBSE implementation 或开发 automation tools；
- 提交受版权限制的标准全文、内部培训材料或 confidential interfaces。

## Research abstraction boundary

| Layer | Meaning | Example |
|---|---|---|
| Generic Core | 跨产品仍成立的对象、关系和 assurance semantics | Verification Obligation、Strategy、Evidence、Provenance、Composite Gate |
| Generic Extension Point | Framework 确认需要、但 taxonomy/criteria/authority 由 profile 决定的维度 | Assurance/Independence Constraint、Coverage Obligation、Sufficiency Assessment、Assumption |
| Domain Profile | 特定行业规则对 Generic Core/extension points 的受控特化 | Civil Aviation FDAL/IDAL、Safety Requirement、SSA/ASA、typed independence |
| Concrete Project Practice | 特定组织、项目、工具或配置采用的做法 | 项目审批流、具体台架与记录格式 |

任何内容进入通用层前都必须回答：更换领域后该规则是否仍然成立，以及它的 normative basis 或 research rationale 是什么。

## v0.2 conceptual-baseline boundary

五源 consolidation 的 verdict 是 `CONDITIONALLY READY FOR v0.2 CONCEPTUAL BASELINE`。这允许冻结稳定 terminology、V0–V12 ontology、Generic/Profile boundary、evidence/change/gate semantics 与受控 open gaps；不允许宣称 executable schema、统一 coverage/sufficiency algorithm、item-level assurance completeness、certification acceptance 或 framework validation 已完成。
