---
title: Gap Migration Report — ISO 29148 / ISO 15026-2
status: research-complete
version: 0.1
baseline: post-v0.2-candidate
owner: research
last_updated: 2026-08-18
dependencies:
  - ../normative_gap_matrix.md
  - object_promotion_disposition_register_29148_15026_2.md
---

# Gap Migration Report — ISO 29148 / ISO 15026-2

## 1. Purpose

本报告只迁移被本轮两源研究实际影响的 gap。`Resolved` 仅表示概念/接口层面有足够支撑；不会被解释为 executable schema、universal criterion 或 authority rule 已完成。

## 2. Existing-gap migration

| Gap | Previous state | New evidence | Disposition | New state / successor |
|---|---|---|---|---|
| ISO-G02A Coverage meta-model | Resolved | 29148 distinguishes requirement-item/set quality and requirement-to-method traceability | CLARIFIED | Resolved; do not confuse requirement-set completeness with implementation coverage |
| ISO-G03A Sufficiency interface | Resolved | 15026-2 identifies inference/context/evidence relevance and uncertainty, while readers assess sufficiency | STRENGTHENED | Resolved interface; conclusion/rationale/uncertainty inputs more explicit |
| ISO-G03B Domain criteria/authority | Open | 15026-2 explicitly avoids content-quality thresholds and leaves sufficiency judgment to readers | CONFIRMED OPEN | Open; no universal threshold/authority |
| ISO-G05 Re-verification selection | Open | 15026-2 requires case maintenance under system/environment/use change; narrative includes adjacent-version changes | CLARIFIED | Open; expand impact targets to claim/context/assumption/evidence/argument |
| ISO-G06 Closure authority/state | Open | Assurance cases can inform decisions but 15026-2 confers no acceptance authority | CONFIRMED OPEN | Open |
| ISO-G07 Information-item schema | Open | 29148 supplies normative BRS/StRS/SyRS/SRS content; 15026-2 supplies assurance-case record types | SPLIT + PARTIAL RESOLUTION | ISO-G07A conceptual item/view taxonomy Resolved; ISO-G07B executable schema/cardinality remains Open; 15289 dependency remains |
| LC-G04 Instantiation evidence schema | Open | 15026-2 requires structure mapping and fulfilment records, but not lifecycle/process instantiation schema | CLARIFIED | Open |
| SAF-G02 Assumption lifecycle | Open | 29148 requires requirement assumptions documented/validated; 15026-2 places assumptions in Context/Evidence | STRENGTHENED CONCEPTUALLY | Open for ownership/state/confirmation/cardinality |
| SAF-G04 Safety evidence aggregation | Resolved aviation | 15026-2 supplies generic Evidence Item and recursive Supported Claim structure | GENERALIZED INTERFACE | Resolved for conceptual evidence-to-claim structure; aviation content remains profile-specific |

## 3. New gaps

| ID | Topic | Source trigger | Why open | Priority |
|---|---|---|---|---|
| REQ-G01 | Requirement-to-Obligation formation/cardinality | 29148, 6.5.2.2 supports per-action method/criteria but no obligation object | Need rules for grouping/splitting and criteria ownership without forcing 1:1 mapping | High — information model |
| REQ-G02 | Requirement condition/constraint representation | 29148, 5.2.4 permits qualifiers, linked constraints and standalone requirements | Need typed representation that preserves semantics across projects | Medium |
| REQ-G03 | 29148:2018 to ISO 15288:2023 process mapping | 29148 cites 15288:2015 | Exact task/version deltas not studied | Medium |
| ASC-G01 | ISO 15026-1 terminology dependency | 15026-2 Clause 2/3/5.3.3 | Claim/assurance/uncertainty definitions cannot be fully frozen | High |
| ASC-G02 | Evidence admission assessment | 15026-2, 5.3.2 and 5.3.5 | Need operational rules for converting Results/artefacts into evidence roles while preserving uncertainty/applicability | High — evidence architecture |
| ASC-G03 | Inference validity and argument-quality assessment | 15026-2, 4.1/5.3.4 | Structure identifies inference but supplies no universal validity-evaluation method | High — sufficiency/profile |
| ASC-G04 | Assurance-case report/snapshot/version semantics | 15026-2, 3.1.2/5.3.6 | Need versioning, assembly/index and baseline rules compatible with repository model | Medium |
| INF-G01 | 15289 interoperability | Both sources refer to 15289; source absent | Cannot verify information-item type/content mappings or schema provenance | Highest dependency |

## 4. Gap split details

### ISO-G07 replacement

```text
ISO-G07 Information-item schema (parent)
  ├─ ISO-G07A Conceptual information-item/view taxonomy — RESOLVED
  │    BRS / StRS / SyRS / SRS
  │    Assurance Case {Main, Evidence, Report}
  │    Supported Claim / Evidence Item / Narrative Introduction
  └─ ISO-G07B Executable schema, cardinality and interoperability — OPEN
       ISO 15289 mapping
       identifiers/version/baseline
       fields/cardinalities/state transitions
       physical-document vs repository-view realization
```

The parent should be closed only after the matrix is updated to show both successors. ISO-G07A does not authorize implementation-first schema freezing.

## 5. Research-priority effect

The absence of ISO 15289 remains the largest information-item dependency. ISO 15026-1 becomes a parallel high-priority dependency because 15026-2 normatively imports its core vocabulary. A rational next sequence is:

1. ISO/IEC/IEEE 15289 — information-item taxonomy/interoperability;
2. ISO/IEC/IEEE 15026-1 — assurance/claim/uncertainty vocabulary;
3. return to ISO-G07B/ASC-G02 schema decisions;
4. only then freeze DBSE cardinalities or automated validation rules.

This sequence does not automatically authorize acquisition or study of additional copyrighted standards.
