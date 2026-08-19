---
title: Research Baseline v0.2 Record
status: frozen
version: 0.2
baseline: v0.2
owner: research
last_updated: 2026-08-19
dependencies:
  - research_scope.md
  - ../01_normative_foundation/consolidation/five_source_consistency_gap_review.md
---

# Research Baseline v0.2 Record

## Baseline identity

| Field | Value |
|---|---|
| Baseline ID | `research-baseline/v0.2` |
| Baseline class | conceptual normative-foundation baseline |
| Frozen commit | the unique commit referenced by annotated tag `research-baseline/v0.2` (the commit carrying this record) |
| Resolution command | `git rev-list -n 1 research-baseline/v0.2` |
| Predecessor | Research Foundation Baseline v0.1 |
| Change authority | repository review and ordinary merge workflow |

The annotated tag is the authoritative machine-resolvable frozen-commit reference. A later report may repeat the resolved SHA for convenience, but cannot redefine the target.

## Frozen source set

- ISO/IEC/IEEE 15288:2023;
- ISO/IEC/IEEE 24748-1:2024;
- ISO/IEC/IEEE 24748-2:2024 as supporting application guidance;
- SAE ARP4754B;
- SAE ARP4761A.

## Included decisions

- V0–V12 mixed-ontology Verification Assurance Process View;
- Generic Core / Generic Extension Point / Civil Aviation Profile boundary;
- typed Verification Basis role over Requirement, Specified Characteristic and Applicable Constraint;
- framework-defined Verification Obligation with explicit provenance;
- Result/Evidence/Argument/Claim separation at the five-source conceptual level;
- change-impact, re-verification and Composite Gate conceptual semantics;
- coverage and sufficiency interface/domain-rule split;
- DCAS as an industrial-practice knowledge source rather than a validation instance;
- ARINC 615A, UAV flight-management and LLM service scenarios as planned validation instances;
- framework-object provenance and standards-layering governance established before this freeze.

## Exclusions and non-claims

This baseline does not include:

- ISO/IEC/IEEE 29148:2018 or ISO/IEC/IEEE 15026-2:2022 research;
- later innovation-register, HANDOFF or candidate-source-control increments;
- an executable schema, cardinality model or machine-readable metamodel;
- universal evidence sufficiency, closure-authority or re-verification-selection rules;
- certification acceptance, airworthiness compliance or framework validation;
- a platform implementation or completed validation-instance result.

## Supersession and change control

v0.2 supersedes v0.1 for the frozen conceptual normative-foundation decisions listed above. It does not retroactively alter historical review records or promote planned workspaces. Changes to frozen decisions require a traceable post-v0.2 proposal, source or research rationale, impact analysis, review, provenance-register update and an explicit later baseline decision.

## Post-v0.2 entry point

All research after this commit is a post-v0.2 increment until a later baseline is explicitly approved. The immediate controlled entry points are standards-source governance, ISO 29148/15026-2 requirements-to-assurance research, ISO 15289 information-item research and targeted generic conformance-testing methodology research.
