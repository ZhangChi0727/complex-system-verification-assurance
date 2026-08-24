---
title: Cross-Repository Instance Contract
status: working
version: 0.1
baseline: post-v0.2
owner: research
last_updated: 2026-08-25
dependencies:
  - ../02_verification_framework/generic_verification_suite_core.md
  - instance_registry.md
  - arinc_615a_object_mapping_register.md
  - arinc_615a_instance_evaluation_protocol.md
  - ../00_overview/innovation_statement.md
---

# Cross-Repository Instance Contract

## Purpose and scope

This document is the working research-position contract between the method repository and independently governed instance repositories. It defines authority, immutable version binding, temporary mappings, compatibility review and finding feedback for the **Candidate Generic Verification Suite Core (Candidate GVS Core)**. It does not create a stable object registry, executable schema, implementation dependency or compatibility approval.

Current controlled external snapshot:

- method repository base: `196cfc2426a841a4adb9c9159660253896b0257c`;
- ARINC repository: <https://github.com/ZhangChi0727/arinc-615a-conformance>;
- active external commit: `0ce96f701159fd4156d5e5e9889360f53977a61b`;
- active external baseline: `RB-2026-001-v4.2.1`;
- origin: `PRE-FRAMEWORK LEGACY INSTANCE BASELINE`;
- compatibility: `NOT-DETERMINED`;
- Draft PR #9 at `53a98447bcfa862f082ce443d69115067d3ff2f1`: `UNMERGED MIGRATION CANDIDATE`, no active semantic authority.

## Authority and ownership matrix

| Controlled concern | Method repository | Instance repository | Prohibited shortcut |
|---|---|---|---|
| Candidate GVS Core semantic contracts | canonical working authority, subject to normative research/review | consume through versioned mapping; may submit findings | copy or silently redefine canonical definitions |
| Verification Profile | defines extension contract and generalization gate | owns instance/profile specialization and rationale | promote profile taxonomy to Generic by use alone |
| Product Binding | defines binding obligations and compatibility questions | owns product/protocol/tool mapping and concrete Oracle realization | bind to mutable branch or internal implementation API |
| Project Configuration | defines separation and provenance expectations | owns selected versions, IUT/setup, parameters and run controls | encode project values as Core defaults |
| Execution tools and raw evidence | no ownership of instance implementation | owns tools, manifests, raw records and access controls | treat tool output as Evidence without characterization |
| Cross-instance evaluation | owns protocol and synthesis gate | executes protocol and returns controlled findings | single-instance generalization |
| Generic tutorial | canonical authority | may host instance tutorial or identified non-authoritative derived view | duplicate an unversioned canonical tutorial |

## Two meanings of upstream

1. **Instance-baseline upstream** is the commit/tag/baseline inside an instance repository from which an instance candidate evolves. It controls the instance's own Git and evidence lineage.
2. **External Generic Framework upstream** is an immutable method-repository commit or tagged definition context used by a Profile/Binding mapping. It controls semantic compatibility, not the instance's internal Git ancestry.

Neither meaning authorizes dependence on mutable `main`, `latest`, local paths or an ordinary hyperlink as identity.

## Immutable binding and stable-reference minimum

Every binding shall identify immutable method and instance commits/tags/baselines plus a mapping version. A future stable reference requires at least:

| Field | Required meaning |
|---|---|
| `ObjectID` | controlled object identifier |
| `ObjectVersion` | version of the object instance/definition |
| `DefinitionVersion` | version of the defining semantic contract |
| `IntroducedIn` | immutable introduction commit/tag/baseline |
| `SupersededBy` | immutable successor or explicit none |
| `Status` | controlled lifecycle/review state |
| `CanonicalLocator` | repository-relative or immutable remote locator |
| `CompatibilityRule` | version-transition and consumer obligation |

These are minimum future fields only. This PR does not establish a versioned object registry and does not make candidate prefixes stable.

## Temporary mapping vocabulary

Exactly one mapping status is used per disposition:

- `NOT-DETERMINED`
- `CANDIDATE`
- `PARTIAL`
- `CONFLICT`
- `OUT-OF-SCOPE`
- `REVIEWED-COMPATIBLE`
- `REVIEWED-COMPATIBLE-WITH-QUALIFICATION`
- `REVIEWED-INCOMPATIBLE`

The final three statuses require an independent compatibility review. Current ARINC mappings may use only the first five.

Allowed candidate relations are:

- `instantiates`
- `specializes`
- `realizes`
- `implements`
- `supports`
- `indexes`
- `classifies`
- `candidate-correspondence`
- `no-direct-correspondence`

A relation never implies equivalence unless a later reviewed contract explicitly says so.

## Binding record and failure semantics

A temporary binding record shall include method commit/definition context, instance active commit/baseline, Profile version, Binding version, Configuration identity, mapping-register version, evaluation-protocol version, review status and migration impact. Missing identity or unavailable evidence yields `NOT-DETERMINED`; semantic mismatch yields `CONFLICT`; partial scope yields `PARTIAL`. No consumer may convert these states into compatibility by default.

## Finding classification

Every returned finding uses one class:

- `instance-specific defect`;
- `binding defect`;
- `profile-contract ambiguity`;
- `core insufficiency`;
- `core overconstraint`;
- `evaluation-protocol defect`;
- `candidate generalization`.

`candidate generalization` is a question for cross-instance assessment, never automatic Generic promotion.

## Bidirectional feedback chain

```text
Instance finding
  → Framework Change Proposal
  → cross-instance relevance assessment
  → normative basis / research rationale
  → review
  → architecture/object registration when eligible
  → framework update
  → instance migration assessment
```

The minimum evidence-return record contains:

- immutable instance commit and baseline;
- Candidate GVS Core definition context;
- mapping-register version and affected row/object;
- finding ID and classification;
- evidence manifest ID, not copied protected evidence;
- limitation, applicability and counterevidence;
- privacy/copyright/access boundary;
- proposed disposition and owner.

A finding cannot change a canonical definition until the Framework Change Proposal and independent review have passed.

## Historical baseline and migration rule

Historical method and instance baselines remain truthful. A pre-framework instance is not retrospectively relabelled as framework-based. Migration creates a new candidate binding that identifies both old and target contexts, maps changed semantics, records compatibility risk and retains a rollback/qualification path. Merging an instance migration PR does not by itself produce a compatibility verdict.

## Coupling prohibitions

The repositories shall not establish semantic authority through:

- Git submodules or mutable imports;
- copying canonical definitions into the instance repository;
- shared internal code or implementation-specific APIs;
- unversioned `main`, `latest`, local filesystem paths or ordinary hyperlinks;
- importing raw evidence into the method repository;
- treating an implementation class, serialization or SysML view as the semantic contract.

Strong semantic contract and weak implementation coupling allow implementations to vary while keeping mapping and migration auditable.

## Paired Draft PR and three-way handshake

1. **Method-contract handshake:** a method-repository Draft PR defines/reviews the Candidate GVS Core context, temporary mapping rules and evaluation protocol, then merges to an immutable method commit.
2. **Instance-migration handshake:** a separate instance-repository Draft PR binds to that immutable method commit, declares Profile/Binding/Configuration versions, applies migration mappings and reports protocol findings. It does not modify the method repository.
3. **Compatibility-disposition handshake:** a later method-repository review verifies both immutable heads, mapping completeness and evidence-return records, then records `REVIEWED-COMPATIBLE`, `REVIEWED-COMPATIBLE-WITH-QUALIFICATION` or `REVIEWED-INCOMPATIBLE`. Instance migration is assessed again against that disposition.

Each handshake requires a distinct reviewable commit/PR context. Links aid navigation but do not replace immutable identities.

## Review and generalization gates

Compatibility dispositions and Framework Change Proposals require independent review. Certification relevance remains candidate until applicable clause-level research and review exist. ARINC supplies first-instance evidence only; it cannot prove cross-domain completeness, scalability, reusability or generalization, and cannot close RQ8 without UAV FMS, LLM service and cross-instance synthesis.
