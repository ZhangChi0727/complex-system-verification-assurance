---
title: Cross-Repository Instance Contract
status: working
version: 0.3
baseline: post-v0.2
owner: research
last_updated: 2026-08-26
dependencies:
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

This document is the working research-position contract between the method
repository and independently governed instance repositories. It defines
authority, immutable version binding, temporary mappings, compatibility review
and finding feedback for the **Candidate Generic Verification Suite Core
(Candidate GVS Core)**. It does not create a stable object registry, executable
schema, implementation dependency or empirical validation result.

## Current controlled ARINC snapshot

| Concern | Controlled identity / state |
|---|---|
| PR #14 authoring provenance | `196cfc2426a841a4adb9c9159660253896b0257c`; predates the contract and is not the method definition |
| Candidate method definition | Candidate GVS Core 0.3 / merge commit `48dd8232b7efe6b0dba3fcb75dfc154d034d2b0b` |
| ARINC repository | <https://github.com/ZhangChi0727/arinc-615a-conformance> |
| Historical legacy release | commit `3299e6dae83424862f75a4c1d09b91b80d9d8b00`; annotated tag `RB-2026-001-v4.2.1`; `PRE-FRAMEWORK LEGACY INSTANCE BASELINE` |
| Pre-migration control state | `0ce96f701159fd4156d5e5e9889360f53977a61b`; not a release-content identity |
| PR #9 reviewed head | `5d149d1f8e92bbed438fe8bc78be9e8972fecb7d` |
| Active migration baseline | baseline ID `RB-2026-001-v4.3`; release commit `523d42bf03a1135b3d63a00bfb47d3b879d3927e`; annotated tag `v4.3` |
| Tag object / peeled target | `28312fd9c5470cb15d76eb3762c99a25ab842cfd` / `523d42bf03a1135b3d63a00bfb47d3b879d3927e` |
| Post-merge control state | `NONE`; ARINC `main` equals the tagged release commit |
| Migration classification | `GVS-BOUND LEGACY MIGRATION BASELINE`; historical origin remains pre-framework |
| Project Configuration / evaluation | `NOT YET ESTABLISHED` / `NOT-EXERCISED` |
| Compatibility pre-activation | `NOT-DETERMINED` |
| Compatibility activation | independent approval of the unchanged PR #15 head plus an ordinary two-parent merge commit |
| Compatibility post-activation | `REVIEWED-COMPATIBLE-WITH-QUALIFICATION`; subject to Q-01–Q-09; merge SHA is the method-disposition identity |

`RB-2026-001-v4.3` is the baseline ID and `v4.3` is the only release tag.
They are different identity fields. Mutable `main`, `latest`, local paths and
ordinary hyperlinks are never binding identities.

## Authority and ownership matrix

| Controlled concern | Method repository | Instance repository | Prohibited shortcut |
|---|---|---|---|
| Candidate GVS Core semantic contracts | canonical working authority, subject to normative research/review | consume through versioned mapping; may submit findings | copy or silently redefine canonical definitions |
| Verification Profile | defines extension contract and generalization gate | owns instance/Profile specialization and rationale | promote Profile taxonomy to Generic by use alone |
| Product Binding | defines binding obligations and compatibility questions | owns product/protocol/tool mapping and concrete Oracle realization | bind to mutable branch or internal implementation API |
| Project Configuration | defines separation and provenance expectations | owns selected versions, IUT/setup, parameters and run controls | encode project values as Core defaults |
| Execution tools and raw evidence | no ownership of instance implementation | owns tools, manifests, raw records and access controls | treat tool output as Evidence without characterization |
| Cross-instance evaluation | owns protocol and synthesis gate | executes protocol and returns controlled findings | single-instance generalization |
| Generic tutorial | canonical authority | may host an identified non-authoritative derived view | duplicate an unversioned canonical tutorial |

The dependency direction is `Core → Profile → Binding → Configuration`. A lower
layer may select or realize an upstream extension point but may not silently
redefine it.

## Two meanings of upstream

1. **Instance-baseline upstream** is the commit/tag/baseline inside an instance
   repository from which an instance candidate evolves. It controls instance Git
   and evidence lineage.
2. **External Generic Framework upstream** is the immutable method-repository
   definition context used by a Profile/Binding. It controls semantic
   compatibility, not instance Git ancestry.

## Immutable binding and stable-reference minimum

Every binding identifies immutable method and instance commits/tags/baselines
plus a mapping version. A future stable reference requires at least:

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

These remain minimum future fields only. Temporary prefixes are not stable keys.

## Temporary mapping vocabulary

Exactly one source mapping status is used per row:

- `NOT-DETERMINED`
- `CANDIDATE`
- `PARTIAL`
- `CONFLICT`
- `OUT-OF-SCOPE`
- `REVIEWED-COMPATIBLE`
- `REVIEWED-COMPATIBLE-WITH-QUALIFICATION`
- `REVIEWED-INCOMPATIBLE`

The final three require independent compatibility review. A candidate overall
disposition does not replace row status or imply equivalence.

Allowed primary relations are `instantiates`, `specializes`, `realizes`,
`implements`, `supports`, `indexes`, `classifies`, `candidate-correspondence`
and `no-direct-correspondence`. Every mapping is directional:

```text
ARINC object --primary relation--> Framework candidate/role
```

Each row contains exactly one primary relation. `instantiates` requires a
sufficiently established candidate class/role; a conceptual union or typed role
such as `VerificationBasisElement` is not presumed to be an instantiated class.

## Binding record and failure semantics

A temporary binding record includes method definition commit, instance release
commit and baseline/tag identities, repository control-state snapshot where
relevant, Profile/Binding/Configuration identities, mapping/protocol versions,
review status and migration impact. MethodDefinitionCommit is
`48dd8232b7efe6b0dba3fcb75dfc154d034d2b0b`; neither the PR #14 authoring base
nor a mutable PR head may substitute for it.

Missing identity or unavailable evidence yields `NOT-DETERMINED`; `CONFLICT` is
reserved for a demonstrated semantic mismatch between identified objects;
partial scope yields `PARTIAL`. No consumer may convert these states into
compatibility by default.

## Compatibility-disposition rule

The subject is the structural, ownership, mapping and semantic-interface
compatibility of the `RB-2026-001-v4.3` GVS-bound legacy migration contract
against Candidate GVS Core 0.3 at `48dd823…`. It excludes protocol conformance,
execution, sufficiency, certification, authority acceptance and generality.

`REVIEWED-COMPATIBLE` is prohibited because Project Configuration and
execution evidence are absent, mappings remain open, research dependencies
remain, and IDs/mappings are temporary. The controlled conditional transition
is:

1. pre-activation: formal compatibility is `NOT-DETERMINED`;
2. activation event: an independent review approves the unchanged PR #15 head,
   followed by an ordinary two-parent merge containing that head;
3. post-activation: formal compatibility is
   `REVIEWED-COMPATIBLE-WITH-QUALIFICATION` subject to Q-01–Q-09, and the merge
   SHA is the immutable method-disposition identity.

The event is self-executing in repository history. It does not require a
post-merge status commit, does not promote any row-level mapping and does not
start empirical evaluation.

## Finding classification and return

Every returned finding uses one class:

- `instance-specific defect`;
- `binding defect`;
- `profile-contract ambiguity`;
- `core insufficiency`;
- `core overconstraint`;
- `evaluation-protocol defect`;
- `candidate generalization`.

The minimum evidence-return record contains immutable instance and method
identities, affected mapping row/version, finding/classification, evidence
manifest identity or explicit absence, limitation/counterevidence,
privacy/copyright boundary, proposed disposition and owner. A finding cannot
change the Core until a Framework Change Proposal and independent review pass.

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

## Historical baseline and migration rule

Historical baselines remain truthful. v4.2.1 is not retrospectively relabelled
as framework-based. v4.3 creates a GVS-bound migration baseline while preserving
the legacy origin, changed semantics, compatibility risk and rollback/
qualification route. A migration merge/tag is necessary but not sufficient for
a compatibility disposition or empirical evaluation.

## Coupling prohibitions

The repositories shall not establish semantic authority through Git submodules,
mutable imports, copied canonical definitions, shared internal code/APIs,
unversioned branch/local paths, imported raw evidence, or treating a
serialization, implementation class or SysML view as the semantic contract.

## Three-way handshake state

1. **Method-contract handshake:** PR #14 merged at
   `48dd8232b7efe6b0dba3fcb75dfc154d034d2b0b`; method definition established.
2. **Instance-migration handshake:** ARINC PR #9 merged at
   `523d42bf03a1135b3d63a00bfb47d3b879d3927e`, released as baseline ID
   `RB-2026-001-v4.3` with annotated tag `v4.3`; migration established without
   compatibility/evaluation promotion.
3. **Compatibility-disposition handshake:** this method-repository PR
   verifies both immutable heads, 18/18 + 7 rows and the evidence return. Its
   formal state follows the pre/activation/post rule above. Only the ordinary
   merge of an independently approved unchanged head activates the qualified
   disposition. The later ARINC acknowledgement is a separate work order and
   repository PR bound to that method-disposition merge SHA.

## Review and generalization gates

Compatibility dispositions and Framework Change Proposals require independent
review. Approval must attach to the final unchanged PR head; a later status
commit invalidates that approval. ARINC supplies first-instance migration
evidence only. It cannot prove completeness, scalability, reusability or
generality, cannot produce `INSTANCE-EXERCISED`, and cannot close RQ8 without
controlled UAV FMS, LLM service and cross-instance synthesis.
