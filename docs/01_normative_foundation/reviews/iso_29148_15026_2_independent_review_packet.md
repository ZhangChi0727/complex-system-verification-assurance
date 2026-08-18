---
title: ISO 29148 / ISO 15026-2 Independent Review Packet
status: ready-for-independent-review
version: 0.1
baseline: post-v0.2-candidate
owner: research
last_updated: 2026-08-18
review_type: independent-normative-research-review
---

# ISO 29148 / ISO 15026-2 Independent Review Packet

## 1. Review objective

复核本轮研究是否准确建立：

1. Requirement / Requirement Set 到 Verification Obligation 的受控接口；
2. Result/Artefact 到 Evidence Item 的 admission boundary；
3. Evidence Item、Argument、Inference、Supported Claim 和 Context 的结构；
4. requirement/verification chain 与 assurance-case chain 的连接；
5. ISO 15289 与 ISO 15026-1 缺失依赖是否被诚实保留。

本次 review 不重新评审五源 consolidation，不评审 executable schema，也不批准 certification use。

## 2. Review set

| Artifact | Purpose |
|---|---|
| `standard_notes/iso_iec_ieee_29148_2018_clause_study.md` | 29148 clause-level findings and conformance boundary |
| `standard_notes/iso_iec_ieee_15026_2_2022_clause_study.md` | 15026-2 assurance-case structure findings |
| `consolidation/clause_evidence_register_29148_15026_2.md` | Clause-level force, applicability, conclusion-right and non-claim ledger |
| `consolidation/requirements_to_assurance_crosswalk.md` | End-to-end typed bridge and five-column mapping |
| `consolidation/object_promotion_disposition_register_29148_15026_2.md` | Promotion decisions and ontology delta |
| `consolidation/gap_migration_report_29148_15026_2.md` | Existing/new gap disposition |
| `consolidation/repository_impact_plan_29148_15026_2.md` | Deferred implementation plan and validation scenarios |
| `consolidation/five_source_consistency_gap_review.md`, §28–§29 | Authoritative provenance-candidate entries and post-v0.2 research annex |

The licensed PDFs are local review inputs and must not be attached to a public PR or committed.

## 2.1 Source inventory

| Source | Verified identity | Role | Repository handling |
|---|---|---|---|
| ISO/IEC/IEEE 29148:2018, second edition, 2018-11 | Title page, metadata, 104-page PDF and clause outline checked | Primary requirements-engineering/information-item source | Licensed local PDF, excluded from Git |
| ISO/IEC/IEEE 15026-2:2022, second edition, 2022-10 | Title page, metadata, 30-page PDF and clause outline checked | Primary assurance-case structure source | Licensed local PDF, excluded from Git |
| ISO/IEC/IEEE 15288:2023 study | Existing reviewed repository baseline | Cross-check for Verification Basis/lifecycle terminology | Repository research note only |
| Five-source consolidation v0.2 candidate | Existing reviewed repository baseline | Ontology and promotion boundary | Repository artifact |
| ISO/IEC/IEEE 15289 | Source not present | Required future information-item interoperability check | `DEPENDENCY OPEN`; no inferred clauses |
| ISO/IEC/IEEE 15026-1:2019 | Normatively cited source not present | Claim/assurance/uncertainty vocabulary | `DEPENDENCY OPEN`; no secondary substitution |

## 3. Source checkpoints

### ISO/IEC/IEEE 29148:2018

| Check | Locator | Expected interpretation |
|---|---|---|
| Conformance modes | 4.2–4.5 | Process and information-item conformance are distinguishable; tailoring must be declared |
| Requirement construct | 5.2.4 | Requirement, condition and constraint roles remain distinct |
| Individual/set quality | 5.2.5–5.2.6 | Two assessment scopes; neither proves implementation compliance |
| Assumptions/attributes | 5.2.7–5.2.8 | Document/validate assumptions; example attributes are not universal mandatory schema |
| Verification interface | 6.5.2.1–6.5.2.3 | Specified requirements/characteristics, method/criteria and traceability connect planning to results |
| Information items | Clause 7; Clauses 8–9 | Clause 7/9 normative content; Clause 8 outline guidance |
| Verification content | 9.5.18; 9.6.19 | Planned approaches/methods included; parallel organization is recommended |
| Annex status | Annex A/C normative; Annex B informative | No annex-strength flattening |

### ISO/IEC/IEEE 15026-2:2022

| Check | Locator | Expected interpretation |
|---|---|---|
| Scope boundary | Introduction; Clause 1 | Structure terminology, not content-quality or notation requirements |
| Normative dependency | Clause 2; 3.1; 5.3.3 | ISO 15026-1 dependency remains open |
| Sufficiency boundary | 4.1 | Readers assess sufficiency; no universal threshold or authority |
| Top-level record | 5.2 | Main, evidence and report fields preserved |
| Evidence semantics | 5.3.2 | Artefact, applicability, uncertainty and assumptions all represented |
| Recursive reasoning | 5.3.4–5.3.5 | Inference and evidence-reference alternatives preserved; Supported Claim distinct from Claim |
| Report semantics | 3.1.2; 5.3.6 | Report/index is not automatically the whole case |

## 4. Required review questions

| ID | Question | Pass criterion |
|---|---|---|
| RV-01 | Are all normative/recommended/informative statements classified at the correct strength? | No `should`/NOTE/example promoted into universal obligation |
| RV-02 | Does Verification Basis remain broader than Requirement-only? | Requirement, Specified Characteristic and Applicable Constraint remain legal typed roles |
| RV-03 | Is Verification Obligation clearly framework-defined? | No attribution to 29148 as a native class; no forced 1:1 cardinality |
| RV-04 | Is Requirement distinct from Claim and Supported Claim? | No identity shortcut; typed relations only |
| RV-05 | Is Result/Artefact distinct from Evidence Item? | Applicability, uncertainty and assumptions are required conceptual qualifiers |
| RV-06 | Is Argument structure reconstructable? | Evidence-reference leaf and inference/premise recursion are distinguishable |
| RV-07 | Are completeness, truth, sufficiency and authority decisions separate? | No structural-completeness shortcut to acceptance |
| RV-08 | Are absent dependencies explicit? | 15289, 15026-1 and 29148→15288 version mapping remain open |
| RV-09 | Does gap migration avoid false closure? | ISO-G07 split and new gaps match actual evidence |
| RV-10 | Does the impact plan stay within research scope? | No large-scale model/schema/template rewrite in this branch |

## 5. Mandatory non-claims

The reviewer should request changes if any artifact implies that:

- 29148 requirement verifiability is equivalent to completed implementation verification;
- every Requirement maps to exactly one Verification Obligation or Claim;
- any verification report automatically qualifies as assurance Evidence;
- an assurance case without undeveloped arguments proves its Claim;
- 15026-2 establishes evidence-quality/sufficiency thresholds or acceptance authority;
- a particular notation such as GSN is mandatory;
- the repository has completed ISO 15289 or ISO 15026-1 research;
- the conceptual object set is already an executable schema.

## 5.1 Highest-risk interpretations

| Risk | Why high-risk | Required reviewer focus |
|---|---|---|
| Verification Obligation is attributed to ISO 29148 | Would erase framework provenance | Confirm every use labels it framework-defined |
| Requirement, satisfaction Claim and closure state collapse into one object | Would mix normative demand, proposition and authority decision | Confirm typed separation across notes/crosswalk/register |
| Any result/report becomes Evidence automatically | Would omit applicability, uncertainty and assumptions | Confirm evidence-admission boundary |
| Evidence index completeness is treated as argument completeness | Evidence field inventory and main-field references are different structures | Confirm orphan/unreferenced evidence is not proof of support |
| Complete argument structure is treated as sufficient/true/accepted | Explicitly excluded by 15026-2 scope/use | Confirm non-claims and V11/V12 separation |
| 15289 mappings are filled from repository assumptions | Source is absent despite task background assumption | Confirm every mapping stays dependency-open |
| 15026-1 vocabulary is reconstructed from examples | Would substitute examples/secondary inference for normative definitions | Confirm Claim remains dependency-constrained |

## 6. Quality-gate record

| Gate | Author self-check | Independent reviewer result | Notes |
|---|---|---|---|
| Source integrity | PASS | PENDING | PDF identity verified; sources excluded from Git |
| Semantic discipline | PASS | PENDING | Modal strength and annex status recorded |
| Cross-standard consistency | PASS | PENDING | Typed bridge; no object identity shortcut |
| Promotion control | PASS | PENDING | All promoted objects carry source/framework boundary |
| Baseline decision | PASS WITH OPEN DEPENDENCIES | PENDING | Conceptual research complete; dependencies visible |

## 7. Proposed review disposition

```text
Normative accuracy:                 PENDING
Modal-strength discipline:         PENDING
29148 process-version provenance:  PENDING
15026-1 dependency handling:       PENDING
15289 dependency handling:         PENDING
Requirement/Claim separation:      PENDING
Result/Evidence separation:        PENDING
Argument recursion:                PENDING
Promotion control:                 PENDING
Copyright/source hygiene:          PENDING

Blocking findings:                 TBD
Required changes:                  TBD
Overall:                           READY FOR INDEPENDENT REVIEW
```

Baseline recommendation: accept the packet as a **post-v0.2 conceptual research delta candidate** only after independent review closes required findings. Do not promote it directly to an executable schema or certification/compliance baseline.
