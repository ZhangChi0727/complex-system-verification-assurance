---
title: ISO 29148 / ISO 15026-2 Independent Review Packet
status: reviewed
version: 0.1
baseline: post-v0.2-candidate
owner: research
last_updated: 2026-08-19
review_type: independent-normative-research-review
---

# ISO 29148 / ISO 15026-2 Independent Review Packet

## 1. Review objective and disposition

复核本轮研究是否准确建立：

1. Requirement / Requirement Set 到 Verification Obligation 的受控接口；
2. Result/Artefact 到 Evidence Item 的 framework-defined characterization boundary，以及后续 source-native Argument-use boundary；
3. Evidence Item、Argument、Inference、Supported Claim 和 Context 的结构；
4. requirement/verification chain 与 assurance-case chain 的连接；
5. ISO 15289 与 ISO 15026-1 缺失依赖是否被诚实保留。

本次 independent review 已完成。它不重新评审五源 consolidation，不评审 executable schema，也不批准 certification use。结论只接受为 `post-v0.2-candidate` conceptual research delta；不会改变 `research-baseline/v0.2` 标签。

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
| ISO/IEC/IEEE 29148:2018, second edition, 2018-11 | Complete 104-page licensed local PDF; title page, metadata, contents, Clauses 4, 5.2, 5.3, 5.4, 6.1, 6.5.2, 6.6, 7, 8, 9.5.18, 9.5.19, 9.6.19, and Annexes A-C independently checked | Primary requirements-engineering/information-item source | Licensed local PDF, excluded from Git; no local path or watermark recorded |
| ISO/IEC/IEEE 15026-2:2022, second edition, 2022-11 | Title page, metadata, 30-page PDF and clause outline checked | Primary assurance-case structure source | Licensed local PDF, excluded from Git |
| ISO/IEC/IEEE 15288:2023 study | Existing reviewed repository baseline | Cross-check for Verification Basis/lifecycle terminology | Repository research note only |
| Five-source consolidation v0.2 candidate | Existing reviewed repository baseline | Ontology and promotion boundary | Repository artifact |
| ISO/IEC/IEEE 15289:2019 | Source acquired; clause study pending | Required future information-item interoperability check | `DEPENDENCY OPEN`; no inferred clauses |
| ISO/IEC/IEEE 15026-1:2025 | Current edition; source not acquired | Current dependency for the undated Clause 2 reference and Clause 3 imported terms | `DEPENDENCY OPEN`; clause study and compatibility assessment not performed |
| ISO/IEC/IEEE 15026-1:2019 | Source not acquired | Explicit dated Claim-type dependency in 15026-2, 5.3.3; also cited by an informative uncertainty note | `DEPENDENCY OPEN`; exact Claim definition not reconstructed |
| ISO/IEC/IEEE 15026-1:2019→2025 | Neither edition studied | Delta needed before freezing a current complete assurance vocabulary baseline | `VERSION-MAPPING OPEN`; does not block locally defined 15026-2 record/relation review |

## 3. Source checkpoints

### ISO/IEC/IEEE 29148:2018

| Check | Locator | Expected interpretation |
|---|---|---|
| Conformance modes | 4.2–4.5; 6.1 | Full conformance combines 5.2.4–5.2.7, the applicable three requirements-engineering processes, Clause 7 and required Clause 9/Annex A content; process/item conformance remain distinguishable |
| Requirement construct | 5.2.4 | Requirement, condition and constraint roles remain distinct |
| Individual/set quality | 5.2.5–5.2.6 | Two assessment scopes; neither proves implementation compliance |
| Assumptions/attributes | 5.2.7–5.2.8 | Document/validate assumptions; example attributes are not universal mandatory schema |
| Verification interface | 6.5.2.1–6.5.2.3 | Specified requirements/characteristics, method/criteria and traceability connect planning to results; lifecycle-task text, ISO guidance and direct `shall` statements retain separate provenance/modal force |
| Requirements management | 6.6 | Lifecycle-task material, ISO guidance/examples and direct `shall` statements remain distinguishable; 4.2/6.1 control conformance scope |
| Information items | Clause 7; Clauses 8–9 | Clause 7/9 normative content; Clause 8 outline guidance |
| Verification content | 9.5.18; 9.6.19 | Planned approaches/methods included; parallel organization is recommended |
| Annex status | Annex A/C normative; Annex B informative | No annex-strength flattening |

### ISO/IEC/IEEE 15026-2:2022

| Check | Locator | Expected interpretation |
|---|---|---|
| Scope boundary | Introduction; Clause 1 | Structure terminology, not content-quality or notation requirements |
| Normative dependency | Clause 2; 3.1; 5.3.3 | Current 2025 undated-reference dependency and dated 2019 Claim-type dependency are separately recorded; both studies and delta remain open |
| Sufficiency boundary | 4.1 | Readers assess sufficiency; no universal threshold or authority |
| Top-level record | 5.2 | Main, evidence and report fields preserved |
| Evidence semantics | 5.3.2 | Source-native Evidence Item is a four-field record; characterization/admission is a framework relation constrained by those fields, not a source-native workflow |
| Recursive reasoning | 5.3.4–5.3.5 | Inference and evidence-reference alternatives preserved; Supported Claim distinct from Claim |
| Report semantics | 3.1.2; 5.3.6 | Report/index is not automatically the whole case |

## 4. Required review questions

| ID | Question | Pass criterion |
|---|---|---|
| RV-01 | Are all normative/recommended/informative statements classified at the correct strength? | No `should`/NOTE/example promoted into universal obligation; 29148 6.5/6.6 source categories remain distinct |
| RV-02 | Does Verification Basis remain broader than Requirement-only? | Requirement, Specified Characteristic and Applicable Constraint remain legal typed roles |
| RV-03 | Is Verification Obligation clearly framework-defined? | No attribution to 29148 as a native class; no forced 1:1 cardinality |
| RV-04 | Is Requirement distinct from Claim and Supported Claim? | No identity shortcut; typed relations only |
| RV-05 | Are characterization and Argument use separate? | Framework characterization constrained by 5.3.2 is separate from source-native 5.3.5 Argument reference; only the latter supports a specific Claim |
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
| Any result/report becomes Evidence automatically | Would omit applicability, uncertainty and assumptions and misattribute an admission workflow to the source | Confirm source-native record/framework characterization boundary |
| Evidence index completeness is treated as argument completeness | Evidence field inventory and main-field references are different structures | Confirm orphan/unreferenced evidence is not proof of support |
| Complete argument structure is treated as sufficient/true/accepted | Explicitly excluded by 15026-2 scope/use | Confirm non-claims and V11/V12 separation |
| 15289 mappings are filled from repository assumptions | Source is acquired but unstudied | Confirm every mapping stays dependency-open |
| 15026-1 vocabulary is reconstructed from examples | Would substitute examples/secondary inference for normative definitions | Confirm Claim remains dependency-constrained |

## 6. Independent-review quality-gate record

| Gate | Author self-check | Independent reviewer result | Notes |
|---|---|---|---|
| Source integrity | PASS | PASS | 29148 complete 104-page source independently checked; both licensed sources excluded from Git |
| Semantic discipline | PASS | PASS | Modal strength, annex status and 6.5/6.6 provenance boundaries recorded |
| Cross-standard consistency | PASS | PASS | Typed bridge; no object identity shortcut; two-stage evidence provenance corrected |
| Promotion control | PASS | PASS | All promoted objects carry source/framework boundary; gap updates are selective |
| Baseline decision | PASS WITH OPEN DEPENDENCIES | PASS WITH OPEN DEPENDENCIES | Accept only as post-v0.2 conceptual research delta |

## 7. Final review disposition

```text
Normative accuracy:                 PASS WITH OPEN DEPENDENCIES
Modal-strength discipline:         PASS
29148 process-version provenance:  PASS; 15288:2015 -> 2023 mapping OPEN
15026-1 dependency handling:       PASS; 2019 and 2025 sources/study OPEN
15289 dependency handling:         PASS; clause study OPEN
Requirement/Claim separation:      PASS
Result/Evidence separation:        PASS
Argument recursion:                PASS
Promotion control:                 PASS
Copyright/source hygiene:          PASS

Blocking findings:                 0
Required changes:                  CLOSED — IR-29148-01, IR-29148-02,
                                   IR-29148-03, IR-15026-01,
                                   IR-15026-02, IR-PR9-01,
                                   IR-PR9-02, IR-PR9-03, IR-PR9-04
Overall:                           INDEPENDENT REVIEW COMPLETE;
                                   ACCEPT AS POST-v0.2 CONCEPTUAL RESEARCH DELTA
```

Baseline disposition: accept the packet as a **post-v0.2 conceptual research delta candidate**. Do not promote it directly to an executable schema, certification/compliance baseline, stable registry or authority/sufficiency rule.

## 8. Closed findings

| Finding | Closing disposition | Status |
|---|---|---|
| IR-29148-01 Source integrity | Complete 104-page edition and independently checked clause set recorded without local path/watermark | CLOSED |
| IR-29148-02 Full-conformance scope versus guidance | 4.2/6.1 boundary and 6.5/6.6 lifecycle-task/guidance/direct-`shall` provenance separated across note/register/crosswalk | CLOSED |
| IR-29148-03 Direct concept versus normative transformation | 5.2.3 classified `DIRECT-DESCRIPTIVE`, not a universal conformance requirement | CLOSED |
| IR-15026-01 15026-1 dependency split | Current 2025 undated dependency, dated 2019 Claim-type dependency and 2019→2025 delta separately open | CLOSED |
| IR-15026-02 Evidence-characterization provenance | Evidence Item four-field record is source-native; characterization/admission is framework-defined; 5.3.5 Argument reference is source-native | CLOSED |
| IR-PR9-01 Commit-message consistency | Commit 3/4 are rebuilt; stable SHAs are recorded in the final PR-level review snapshot | CLOSED |
| IR-PR9-02 HANDOFF state | Applied in the final repository-state commit; no self-referential post-merge commit planned | CLOSED |
| IR-PR9-03 Review packets/statuses | Notes and shared artifacts set to `reviewed`; explicit dependencies and non-claims retained | CLOSED |
| IR-PR9-04 Selective gap promotion | Only reviewed clause slices enter established basis; ISO-G07/G07B/G07C and all required successor gaps remain open as specified | CLOSED |

Rewritten Commit 3 is recorded by SHA in the final PR-level integration review. Commit 4 is described as the commit containing that final snapshot and is resolved externally by the PR head SHA, avoiding a circular self-reference.
