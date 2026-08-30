---
title: Cross-Repository Instance Contract
status: working
version: 0.5
baseline: post-v0.2
owner: research
last_updated: 2026-08-31
dependencies:
  - ../../project-status.json
  - ../02_verification_framework/generic_verification_suite_core.md
  - instance_registry.md
  - arinc_615a_object_mapping_register.md
  - arinc_615a_instance_evaluation_protocol.md
  - arinc_615a_v43_migration_evidence_return.md
  - arinc_615a_third_handshake_compatibility_disposition.md
  - ../00_overview/innovation_statement.md
---

# Cross-Repository Instance Contract

## Purpose and scope

This is the working contract between the method repository and independently governed instance repositories. It controls authority, immutable version binding, temporary mappings, compatibility review and finding feedback for the Candidate GVS Core. It does not create a stable registry, executable schema, implementation dependency or empirical validation result.

## Current controlled ARINC snapshot

| Concern | Controlled identity / state |
|---|---|
| Method definition | Candidate GVS Core at `48dd8232b7efe6b0dba3fcb75dfc154d034d2b0b` |
| Method compatibility disposition | `c02330d21fe2d3e89e7e2d6352872d52461a6dda`; separate immutable identity |
| ARINC repository | <https://github.com/ZhangChi0727/arinc-615a-conformance> |
| Historical legacy release | `3299e6dae83424862f75a4c1d09b91b80d9d8b00`; `RB-2026-001-v4.2.1`; pre-framework provenance |
| Assessed migration baseline | baseline ID `RB-2026-001-v4.3`; release tag `v4.3`; release commit `523d42bf03a1135b3d63a00bfb47d3b879d3927e`; tag object `28312fd9c5470cb15d76eb3762c99a25ab842cfd` |
| Instance acknowledgement release | baseline ID `RB-2026-001-v4.3.1`; release tag `v4.3.1`; release commit / peeled target `72ca6df88cb8def5221a8fa54e69551f9e7041db`; tag object `55005cc57e26dd56ea1f0fec3ffdbbf1e67d1beb` |
| Three-way handshake | `COMPLETE` |
| Compatibility | `REVIEWED-COMPATIBLE-WITH-QUALIFICATION`; Q-01–Q-09 |
| Project Configuration / evaluation / RQ8 | `NOT YET ESTABLISHED` / `NOT-EXERCISED` / `OPEN` |

Mutable branches, `latest`, local paths and ordinary hyperlinks are never binding identities. The method definition and method compatibility disposition commits have different roles and may not substitute for one another. The v4.3 source and v4.3.1 acknowledgement are also distinct lifecycle roles.

## Authority and ownership

| Controlled concern | Method repository | Instance repository | Prohibited shortcut |
|---|---|---|---|
| Candidate GVS Core | canonical working authority, subject to research/review | consumes through immutable mapping; may return findings | copy or silently redefine definitions |
| Verification Profile | defines extension and generalization gates | owns domain specialization and rationale | promote domain taxonomy by usage alone |
| Product Binding | defines binding obligations and compatibility questions | owns product/protocol/tool mapping and Oracle realization | bind to mutable branch or internal API |
| Project Configuration | defines separation and provenance expectations | owns selected versions, IUT/setup, parameters and run controls | encode project values as Core defaults |
| Execution and raw evidence | owns evaluation contract, not instance implementation | owns tools, manifests, raw records and access control | treat tool output as Evidence without characterization |
| Cross-instance synthesis | owns synthesis and promotion gate | supplies controlled instance results | generalize from one instance |

Dependency direction is `Core → Profile → Binding → Configuration`. A lower layer may select or realize an extension point but may not redefine it.

## Two meanings of upstream

- Instance-baseline upstream controls Git and evidence lineage inside an instance repository.
- External method upstream is the immutable method-definition context used for semantic compatibility; it does not control instance Git ancestry.

## Immutable binding and temporary mapping

A binding records immutable method-definition, method-disposition, instance release and mapping identities. Future stable references require controlled identity, object and definition versions, introduction/supersession, status, canonical locator and compatibility rule. Temporary prefixes remain navigation keys only.

Each mapping is directional and has one primary relation:

```text
Instance object --primary relation--> Framework candidate/role
```

Allowed relations are defined by the mapping register and repository checker. Missing identity or evidence yields `NOT-DETERMINED`; `CONFLICT` is reserved for demonstrated semantic mismatch; partial scope yields `PARTIAL`. No consumer may convert these states into compatibility by default.

## Three-way handshake and compatibility

1. The method-contract handshake established the immutable Candidate GVS Core definition.
2. The instance-migration handshake released the assessed ARINC v4.3 migration baseline without compatibility/evaluation promotion.
3. The method-side independently reviewed disposition was ordinarily merged, and ARINC v4.3.1 subsequently acknowledged that exact disposition. The third handshake is therefore `COMPLETE`.

The resulting compatibility is `REVIEWED-COMPATIBLE-WITH-QUALIFICATION` under Q-01–Q-09. This is a structural, ownership, mapping and semantic-interface conclusion. It excludes protocol conformance, execution, sufficiency, certification, authority acceptance, generic scalability and generality. No method-repository baseline or tag was created for this handshake.

## Finding return and promotion

Every returned finding is classified as instance-specific defect, binding defect, profile-contract ambiguity, core insufficiency, core overconstraint, evaluation-protocol defect or candidate generalization. The minimum return includes immutable instance/method identities, affected mapping, evidence identity or explicit absence, limitations, privacy/copyright boundary, proposed disposition and owner.

```text
Instance finding
  → Framework Change Proposal
  → cross-instance relevance assessment
  → normative basis / research rationale
  → independent review
  → eligible architecture registration and framework update
  → instance migration assessment
```

An instance finding cannot directly change the Core. Atomic baselines, change requests, reviews and historical evidence remain immutable.

## Coupling and generalization prohibitions

Semantic authority shall not be established through submodules, mutable imports, copied canonical definitions, shared internal code/APIs, unversioned branches/local paths or imported raw evidence. ARINC supplies bounded first-instance migration evidence only. It cannot prove completeness, scalability, reusability or generality, produce `INSTANCE-EXERCISED`, advance architecture maturity, or close RQ8 without controlled ARINC execution, UAV FMS and LLM evaluations, and cross-instance synthesis.
