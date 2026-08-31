---
title: Framework Validation Workspace
status: working
version: 0.7
baseline: post-v0.2
owner: research
last_updated: 2026-08-30
dependencies:
  - ../../project-status.json
  - ../00_overview/research_scope.md
  - ../00_overview/research_questions.md
  - ../02_verification_framework/generic_verification_suite_core.md
  - cross_repository_instance_contract.md
  - instance_registry.md
---

# Framework Validation Workspace

本目录保存 Candidate GVS Core 的跨仓库契约、实例登记、映射、评价协议和受控评审证据。当前项目状态只在根 [`README.md`](../../README.md) 展示，机器身份和值只在 [`project-status.json`](../../project-status.json) 维护；本页提供耐久导航和语义边界，不复制完整生命周期台账。

## Controlled governance entry points

- [Candidate GVS Core working definition](../02_verification_framework/generic_verification_suite_core.md)
- [Cross-Repository Instance Contract](cross_repository_instance_contract.md)
- [Temporary Controlled Instance Register](instance_registry.md)
- [ARINC 615A Temporary Object Mapping Register](arinc_615a_object_mapping_register.md)
- [ARINC 615A Instance Evaluation Protocol](arinc_615a_instance_evaluation_protocol.md)
- [ARINC v4.3 Migration Evidence Return](arinc_615a_v43_migration_evidence_return.md)
- [ARINC v4.3 Third-Handshake Compatibility Disposition](arinc_615a_third_handshake_compatibility_disposition.md)
- [ARINC v4.3 Third-Handshake Independent-Review Handoff](arinc_615a_third_handshake_review_handoff.md)
- [PR #14 external review disposition](pr_14_external_review_disposition.md)

## Current durable instance state

ARINC 615A 第三次握手为 `COMPLETE`。方法仓库处置已由实例仓库的 `v4.3.1` 发布确认；兼容性仍为 `REVIEWED-COMPATIBLE-WITH-QUALIFICATION`，并受 Q-01–Q-09 限定。该确认没有创建方法仓库 baseline/tag，也没有建立 Project Configuration、执行评价或关闭 RQ8。精确提交、tag object、peeled target 和 baseline ID 由 `project-status.json` 记录，实例登记册说明各身份的角色。

## Validation instances

| Instance | Verification type | Current role |
|---|---|---|
| ARINC 615A protocol conformance verification | deterministic, specification-driven conformance verification | first GVS-bound legacy migration and bounded compatibility source; evaluation not exercised |
| UAV flight-management system verification | safety-driven system verification | planned second-domain evaluation |
| LLM service reliability/performance verification | probabilistic, weak-Oracle service verification | planned third-domain evaluation |

**DCAS is not a validation instance.** It remains an industrial-practice source whose reusable content must pass the controlled abstraction ladder.

## Ownership and claim boundary

```text
Complete Verification Suite
= Candidate Generic Verification Suite Core
+ Verification Profile
+ Product Binding
+ Project Configuration
```

The method repository owns Candidate GVS Core semantics, promotion governance and the cross-instance evaluation contract. Instance repositories own Profile, Binding, Configuration, tools, concrete Oracle realization, execution and original evidence. Immutable identities and reviewed mappings connect the repositories; copied definitions, mutable branches and shared internal APIs do not.

An instance may `SUPPORT`, `QUALIFY` or `FALSIFY` a candidate claim. A single instance cannot prove generic completeness, scalability, reusability or generality, cannot produce `VALIDATED-BASELINE`, and cannot close RQ8. Project Configuration remains `NOT YET ESTABLISHED` and instance evaluation remains `NOT-EXERCISED` until a separately controlled execution package exists.

## Evaluation dimensions

The maintained protocol covers completeness, traceability, repeatability, scalability, reusability, reviewability, change-impact detection, coverage explicitness, evidence quality, interface isolation and hidden-assumption detection. Compatibility of a migration contract is not execution of that protocol, protocol conformance, evidence sufficiency, certification acceptance or empirical framework validation.
