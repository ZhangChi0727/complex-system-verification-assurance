---
title: Candidate Generic Verification Suite Core Working Definition
status: working
version: 0.2
baseline: post-v0.2
owner: research
last_updated: 2026-08-25
dependencies:
  - ../00_overview/research_scope.md
  - ../00_overview/innovation_statement.md
  - ../00_overview/research_questions.md
  - ../00_overview/roadmap.md
  - ../08_validation/cross_repository_instance_contract.md
  - ../08_validation/instance_registry.md
---

# Candidate Generic Verification Suite Core Working Definition

## Research position

The **Candidate Generic Verification Suite Core (Candidate GVS Core)** is the working research position for this repository's principal engineering outcome. It is a product-independent, composable set of semantic contracts and **Verification Capability Packages** intended to support later profile specialization, product binding and project configuration. It is not an existing software library, executable platform, finalized architecture or established novelty claim.

The working composition is:

```text
Complete Verification Suite
= Candidate Generic Verification Suite Core
+ Verification Profile
+ Product Binding
+ Project Configuration
```

This formula is a separation-of-responsibility contract, not a frozen executable schema. A complete suite is obtained only when all four layers are identified and version-bound for an instance.

## Four-layer ownership boundary

| Layer | Candidate responsibility | Authority / owner | Excluded responsibility |
|---|---|---|---|
| Candidate Generic Verification Suite Core | Product-independent object roles, relations, lifecycle/decision contracts, extension-point contracts, provenance and evaluation protocol | This method repository, subject to normative research and independent review | Domain rules, product interfaces, project values and implementation technology |
| Verification Profile | Domain/verification-type specialization, applicable rigor, taxonomy, constraints and admissible extension choices | Controlled profile definition, normally maintained with the relevant domain or instance family | Product-specific protocol/item identity and project configuration |
| Product Binding | Mapping from the profile/core contracts to the product, protocol, interfaces, executable artefacts and concrete Oracle implementations | External instance repository | Redefinition of Candidate GVS Core semantics |
| Project Configuration | Selected versions, IUT/setup/environment, parameters, procedures, tools, approvals and run-specific controls | Concrete project/instance | Generic or profile definition authority |

A Profile, Binding or Configuration is not part of the Candidate GVS Core merely because it is reusable. External instances own their implementation assets and may only propose changes to Core definitions through the controlled feedback contract.

## Verification Capability Packages

A **Verification Capability Package** is a candidate modular, product-independent delivery unit inside the Candidate GVS Core. It is not a fifth architecture layer and not necessarily a software package. A package may combine controlled definitions, relations, invariants, extension points, patterns, templates, evaluation questions and version/migration rules needed to exercise one coherent verification capability.

Candidate package population includes:

1. **Lifecycle/process/decision contracts** — planning, basis establishment, verifiability, strategy, design, procedure, readiness, execution, result evaluation, anomaly/change, coverage/sufficiency and closure responsibilities, while V0–V12 remain `OPEN-CANDIDATE`.
2. **Object-and-relation contracts** — candidate roles for Verification Basis Element, Verification Obligation, Verification Strategy, Verification Case, Verification Procedure, Observation, Result, Evidence Item, Argument and Claim; the source-native/framework-defined distinction remains mandatory.
3. **Extension-point contracts** — Coverage, Sufficiency, Assurance/Independence and Assumption dimensions whose taxonomy, criteria, authority or lifecycle detail may be supplied by a Profile or later reviewed evidence.
4. **Governance contracts** — version identity, provenance, configuration, impact analysis, migration and explicit failure semantics.
5. **Pattern/template/evaluation contracts** — reusable construction and falsification aids with applicability, variation, prohibited generalization and review controls.
6. **Optional realizations** — machine-readable models, SysML/SysML v2 views, schemas, executable adapters or tools used to express, evaluate or demonstrate the contracts after their respective gates.

Package composition does not imply that every package, field or relationship is already supported by a standard. Each element remains classified as source-native, framework-defined candidate, profile specialization, practice or open proposal.

## Meaning of interface stabilization

In this research, an interface is stabilized first at the semantic-contract level. The candidate contract covers:

- object responsibility and non-equivalence boundaries;
- required inputs, outputs and relations;
- invariants, applicability and extension points;
- immutable version identity and canonical locator expectations;
- compatibility and migration rules;
- failure, unresolved and `NOT-DETERMINED` semantics;
- provenance and review authority.

It does **not** currently freeze a programming language, Python class, REST API, file serialization, database schema, metamodel, cardinality, state machine, tool technology or SysML role. A later implementation may be replaced without changing the semantic contract; a semantic change requires controlled review and migration assessment.

## Explicit non-goals

The Candidate GVS Core:

- need not be directly executable at the current maturity;
- is not a product-specific verification tool or commercial platform;
- is not the ARINC 615A Verification Profile, Product Binding or Project Configuration;
- is not an authority-accepted or certification-ready solution;
- does not make raw traces, manifests, PASS results or tool outputs Evidence by default;
- does not freeze language, API, schema, metamodel, SysML/SysML v2 role or implementation architecture;
- does not establish a stable object registry or promote candidate prefixes to stable IDs;
- does not establish novelty merely because it is identified as the principal engineering research outcome.

## Maturity and promotion gate

Current maturity remains `OPEN-CANDIDATE`. Promotion requires, at minimum:

1. **`OPEN-CANDIDATE → REVIEWED-PROVISIONAL`:** completion or reviewed deferral of the planned normative-source cohort; Task 022 legacy/current evidence reconciliation and cross-standard synthesis; reviewed Architecture Impact dispositions; and independent cross-source architecture review.
2. **`REVIEWED-PROVISIONAL → CONTROLLED-BASELINE`:** an explicit architecture freeze, version/migration review, controlled identity and change rules, and disposition of residual conflicts. Normative synthesis alone cannot perform this promotion.
3. **Single-instance exercise:** an immutable method definition, reviewed binding and bounded protocol execution may yield `INSTANCE-EXERCISED` evidence for ARINC. It does not advance the general framework to `VALIDATED-BASELINE` or close RQ8.
4. **`VALIDATED-BASELINE` / RQ8 closure:** controlled ARINC 615A, UAV FMS and LLM service evaluations plus independently reviewed cross-instance synthesis; limitations and counterevidence remain visible.
5. **Separate realization gates:** executable schema, versioned object registry and automation contracts require their own prerequisites and freeze reviews.

The historical `research-baseline/v0.2` checkpoint and current V0–V12 identifiers are preserved. This working position neither changes their semantics nor advances architecture maturity.

## Instance and research interfaces

- Research objectives and abstraction boundaries: [Research Scope](../00_overview/research_scope.md)
- Candidate contribution and falsification controls: [Innovation Statement](../00_overview/innovation_statement.md)
- Open questions, including RQ7/RQ8: [Research Questions](../00_overview/research_questions.md)
- Cross-repository authority and migration rules: [Cross-Repository Instance Contract](../08_validation/cross_repository_instance_contract.md)
- Temporary instance population: [Instance Registry](../08_validation/instance_registry.md)
- Validation workspace and protocols: [Framework Validation Workspace](../08_validation/README.md)

The Candidate GVS Core is therefore a **working research position** and candidate engineering integration target. Standard evidence may support, qualify or falsify its contents; instance evidence may reveal insufficiency, overconstraint or hidden assumptions. Neither pathway may be replaced by advocacy for the current design.
