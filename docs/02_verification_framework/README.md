---
title: Verification Framework Workspace
status: working
version: 0.2
baseline: post-v0.2
owner: research
last_updated: 2026-08-24
dependencies:
  - ../00_overview/research_scope.md
  - ../01_normative_foundation/README.md
  - ../08_validation/README.md
---

# Verification Framework Workspace

本目录是产品无关 Verification Assurance Framework 的 working workspace。当前入口是 [Candidate Generic Verification Suite Core Working Definition](generic_verification_suite_core.md)，它把主要工程研究成果定位为由可组合 Verification Capability Packages 构成的 Candidate GVS Core，并保持 Core / Profile / Binding / Configuration 分离。

后续内容包括 candidate framework concepts、relations、decision/lifecycle contracts、extension points、applicability boundaries、normative traceability 和独立评审后的 migration proposals。所有内容必须保留 source-native、framework-defined、profile 与 practice 分类。

当前边界：

- V0–V12 成熟度仍为 `OPEN-CANDIDATE`；
- 本目录没有已验证或已冻结的 Framework Rules；
- 没有 executable schema、cardinality、state machine、metamodel、API 或 automation contract；
- Verification Capability Package 是 Core 内部的模块化、产品无关交付单元，不是第五层或现成软件包；
- machine-readable/executable realization 只是可选表达或评价载体；
- 外部实例通过 [validation workspace](../08_validation/README.md) 的受控契约提供 evidence/finding，不得直接重定义通用对象。

依赖仍是 normative foundation 的来源研究、Task 022 综合、Architecture Impact review 和多实例评价。本工作区状态为 `working`，不表示 architecture freeze、novelty established 或 framework validated。
