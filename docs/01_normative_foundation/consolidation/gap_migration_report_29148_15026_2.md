---
title: Gap Migration Report — ISO 29148 / ISO 15026-2
status: reviewed
version: 0.1
baseline: post-v0.2-candidate
owner: research
last_updated: 2026-08-19
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
| ISO-G07 Overall information-item architecture | Open | Candidate studies supply requirements and assurance-case slices | SPLIT + PARTIAL RESOLUTION | Parent Open; ISO-G07A Partially Supported; ISO-G07B Open; ISO-G07C source acquired/study pending |
| LC-G04 Instantiation evidence schema | Open | 15026-2 requires structure mapping and fulfilment records, but not lifecycle/process instantiation schema | CLARIFIED | Open |
| SAF-G02 Assumption lifecycle | Open | 29148 requires requirement assumptions documented/validated; 15026-2 places assumptions in Context/Evidence | STRENGTHENED CONCEPTUALLY | Open for ownership/state/confirmation/cardinality |
| SAF-G04 Safety evidence aggregation | Resolved aviation | 15026-2 supplies generic Evidence Item and recursive Supported Claim structure | GENERALIZED INTERFACE | Resolved for conceptual evidence-to-claim structure; aviation content remains profile-specific |

## 3. New gaps

| ID | Topic | Source trigger | Why open | Priority |
|---|---|---|---|---|
| REQ-G01 | Requirement/Set identity and lifecycle schema | 29148, 5.2.4–5.2.8/7/9 supplies reviewed concepts/content but not an executable lifecycle schema | Identity, mandatory attributes, state and cardinality remain open; formation/grouping/splitting and condition/constraint representation are unnumbered subproblems; 29148:2018→15288:2023 mapping is an open dependency | High — information model |
| REQ-G02 | Verification Criterion placement and cardinality | 29148, 6.5.2.2 supports method/criterion relations while retaining the 4.2/6.1 conformance boundary | Criterion-to-action/basis/requirement representation and cardinality remain framework decisions; no 1:1 Requirement-to-Procedure rule | High — information model |
| ASC-G01 | ISO 15026-1 terminology dependency | 15026-2 Clause 2/3 undated reference and 5.3.3 dated 2019 Claim type | Claim/assurance/uncertainty definitions and the 2019→2025 delta cannot be fully frozen | High |
| ASC-G02 | Framework characterization and later Argument use | Framework relation constrained by 15026-2, 5.3.2; source-native 5.3.5 reference | Four-field Evidence Item structure is established, but characterization/admission workflow/state/authority/cardinality and later Claim-specific use remain distinct/open | High — evidence architecture |
| ASC-G03 | Inference validity and argument-quality assessment | 15026-2, 4.1/5.3.4 | Structure identifies inference but supplies no universal validity-evaluation method | High — sufficiency/profile |
| ASC-G04 | Assurance-case report/snapshot/version semantics | 15026-2, 3.1.2/5.3.6 | Need versioning, assembly/index and baseline rules compatible with repository model | Medium |

`REQ-G01` also carries the open 29148:2018→15288:2023 version-mapping dependency. Requirement formation/grouping/splitting and condition/constraint representation are research subproblems under that authoritative gap; they are not separately numbered controlled gaps in this PR. ISO 15289 information-item interoperability is controlled solely by `ISO-G07C`, whose source is acquired and whose clause study remains pending.

## 4. Gap split details

### ISO-G07 replacement

```text
ISO-G07 Overall Verification-Assurance Information-Item Architecture — OPEN
  ├─ ISO-G07A Requirements and Assurance-Case Conceptual Item/View Taxonomy — PARTIALLY SUPPORTED
  │    BRS / StRS / SyRS / SRS
  │    Assurance Case {Main, Evidence, Report}
  │    Supported Claim / Evidence Item / Narrative Introduction
  ├─ ISO-G07B Executable schema, cardinality, state and serialization — OPEN
       ISO 15289 mapping
       identifiers/version/baseline
       fields/cardinalities/state transitions
  │    physical-document vs repository-view realization
  └─ ISO-G07C ISO 15289 interoperability and document/record mapping — OPEN
       source acquired; clause study pending
```

The parent remains open. ISO-G07A is only partially supported and does not authorize implementation-first schema freezing.

## 5. Research-priority effect

The pending clause study of the acquired ISO 15289 source remains the largest information-item dependency. ISO 15026-1 is a parallel high-priority dependency: Clause 2/3 use an undated reference resolved to the current 2025 edition, while 5.3.3 explicitly imports the dated 2019 Claim type. A rational next sequence is:

1. ISO/IEC/IEEE 15289 — information-item taxonomy/interoperability;
2. ISO/IEC/IEEE 15026-1:2019 and 2025 — dated/undated dependencies plus delta;
3. return to ISO-G07B/ASC-G02 schema decisions;
4. only then freeze DBSE cardinalities or automated validation rules.

This sequence does not automatically authorize acquisition or study of additional copyrighted standards.
