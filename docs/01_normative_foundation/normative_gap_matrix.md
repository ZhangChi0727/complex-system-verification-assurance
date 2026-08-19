---
title: Normative Gap Matrix
status: reviewed
version: 1.4
baseline: post-v0.2
owner: research
last_updated: 2026-08-19
dependencies:
  - standards_baseline.md
  - standards_map.md
  - consolidation/five_source_consistency_gap_review.md
---

# Normative Gap Matrix

本矩阵把**已经研究并评审的条款依据**与**尚待研究/评审的候选来源**分开。Gap 是研究问题和候选贡献的输入，不是创新证明。未评审来源不得进入 `Established clause basis`、关闭 gap 或支撑强 novelty claim。

受控检索状态：`SEARCH NOT STARTED`、`PARTIAL SOURCE COVERAGE`、`PLANNED SOURCES IDENTIFIED`、`SOURCE ACQUISITION OPEN`、`SOURCE ACQUIRED; CLAUSE STUDY PENDING`、`CLAUSE STUDY IN PROGRESS`、`SOURCE SEARCH COMPLETE`、`NO ADEQUATE SOURCE FOUND`。`SOURCE SEARCH COMPLETE` 也不等于原创性证明。

| ID | Framework topic | Established clause basis | Candidate source scope | Source-search status | Current interpretation / response | Disposition | Status |
|---|---|---|---|---|---|---|---|
| ISO-G01 | Independence applicability and substantiation | ISO 15288, 6.3.8/6.4.9; 24748-1, 6.2.2/6.4; ARP4754B, 5.2/5.7/App. A; ARP4761A, 2.2/Apps. E,J–M,P | IEEE 1012; item profiles | PLANNED SOURCES IDENTIFIED | Generic hook and aviation taxonomy established; universal applicability/authority/substantiation open. | PARTIALLY RESOLVED | Open |
| ISO-G02 | Verification coverage (parent) | ISO 15288, 5.10/6.4.9; ARP4754B, 5.5.5.2.2; ARP4761A, D.5/E.4/F.4 | 29119; item profiles | PARTIAL SOURCE COVERAGE | Interface separated from domain taxonomy; no universal percentage. | SPLIT → ISO-G02A/B | Closed as parent |
| ISO-G02A | Coverage meta-model | Same as ISO-G02 | 29119-2/3 | PARTIAL SOURCE COVERAGE | `population + criterion + evidence/result + disposition + context` retained. | RESOLVED GENERICALLY | Resolved |
| ISO-G02B | Domain coverage taxonomy/rules | ARP4754B, 5.5.5.2.2; ARP4761A, D.5/E.4/F.4 | 29119-2/4; DO-178C/DO-254 | PLANNED SOURCES IDENTIFIED | Aviation dimensions are profile inputs; cross-domain rules open. | KEEP OPEN | Open |
| ISO-G03 | Verification sufficiency (parent) | ISO 15288, 5.10; ARP4754B, 5.5.4–5.5.5/App. A; ARP4761A, D.5/E.4/F.4 | 15026 family; IEEE 1012 | PARTIAL SOURCE COVERAGE | Stable interface separated from contextual criteria. | SPLIT → ISO-G03A/B | Closed as parent |
| ISO-G03A | Sufficiency Assessment interface | ISO 15288, 5.10; ARP4754B, 5.5.4–5.5.5/App. A; ARP4761A, D.5/E.4/F.4; ISO 15026-2, 4.1/5.3.2/5.3.4–5.3.5 | 15026-4 | PARTIAL SOURCE COVERAGE | Interface retained; reviewed 15026-2 adds context, uncertainty, Evidence Item and recursive Argument structure without a sufficiency algorithm. | RESOLVED GENERICALLY | Resolved |
| ISO-G03B | Sufficiency criteria and authority | Five-source basis as ISO-G03; ISO 15026-2, 4.1 confirms reader judgment and no content-quality threshold | 15026-4; IEEE 1012; profiles | PARTIAL SOURCE COVERAGE | Thresholds, argument quality, residual risk and authority remain open. | KEEP OPEN | Open |
| ISO-G04 | Oracle validity/configuration | ISO 15288, 6.4.9.3(a)–(b), expected results only | ISO/IEC 9646; ITU-T X.290; 29119; literature | PLANNED SOURCES IDENTIFIED | Oracle remains proposal; expected result does not imply Oracle entity. | KEEP PROPOSAL | Research Proposal |
| ISO-G05 | Re-verification selection/impact | ISO 15288, 6.3.5/6.4.9; 24748-2, 6.7.5.4.4; ARP4754B, 6.3–6.4; ARP4761A, 3.1.1/A.6/E.4/P.1 | IEEE 1012; literature | PLANNED SOURCES IDENTIFIED | V10 chain stable; universal selection method open. | PARTIALLY RESOLVED | Open |
| ISO-G06 | Closure authority/state | ISO 15288, 6.3.2/6.4.9; 24748-1, 4.3/Cl.5; ARP4754B, 3.2.2/4.7/5.5–5.7 | 24748-8; 16326; literature | SOURCE ACQUISITION OPEN | Composite Gate stable; waiver/reopen/authority/state open. | PARTIALLY RESOLVED | Open |
| ISO-G07 | Overall Verification-Assurance Information-Item Architecture | Five-source record/relation basis: ISO 15288, 5.6/6.3.6/6.4.9; 24748-1, 6.2.8; 24748-2, 6.7.4/6.8; ARP4754B, 5.4.7/5.5.6 | Reviewed refinements: 29148/15026-2; remaining: 15289/29119-3 | PARTIAL SOURCE COVERAGE | Reviewed requirements/assurance slices refine successors but do not complete the parent taxonomy. | SPLIT → ISO-G07A/B/C | Open |
| ISO-G07A | Requirements and Assurance-Case Conceptual Item/View Taxonomy | Five-source conceptual relations; ISO 29148, 4.4/7/9.5/9.6; ISO 15026-2, 5.2/5.3.1–5.3.6 | ISO 15289 interoperability and remaining VAF views | PARTIAL SOURCE COVERAGE | Requirement/Set, BRS/StRS/SyRS/SRS and assurance-case structure are reviewed slices; whole-VAF completeness not claimed. | PARTIALLY RESOLVED | Partially Supported |
| ISO-G07B | Executable schema, cardinality, state and serialization | Five sources do not establish executable schema | 15289; 29119-3; schema literature | PLANNED SOURCES IDENTIFIED | Fields, identities, cardinalities, lifecycle states and serialization remain open. | KEEP OPEN | Open |
| ISO-G07C | ISO 15289 interoperability and document/record mapping | — | ISO/IEC/IEEE 15289:2019 (source acquired) | SOURCE ACQUIRED; CLAUSE STUDY PENDING | Source acquired; clause-level mapping not started. | NEW — KEEP OPEN | Open |
| ISO-G08 | MBSE/model evidence | ISO 15288, Annex D; 24748-1, Annex A.10; ARP4761A, Appendix N | 24641; IEEE 1012; literature | PLANNED SOURCES IDENTIFIED | No generic tool qualification/admissibility regime. | KEEP OPEN | Open |
| LC-G01 | Gate ontology | ISO 24748-1, 4.3/Cl.5/6.2.6 | 24748-8 | PARTIAL SOURCE COVERAGE | Assessment, optional review, authority decision and event remain separate. | RESOLVED GENERICALLY | Resolved |
| LC-G02 | Review taxonomy | ISO 24748-1, 6.4/Annexes C,F | 24748-8 | SOURCE ACQUISITION OPEN | Method/lifecycle review and decision distinct. | RESOLVED GENERICALLY | Resolved |
| LC-G03 | Process-view provenance | ISO 15288, 5.8; 24748-1, Annex D | 15289; registry design | PARTIAL SOURCE COVERAGE | Framework orchestration remains labelled. | RESOLVED GENERICALLY | Resolved |
| LC-G04 | Process-instantiation evidence schema | 24748-1, 6.2.2–6.2.8; 24748-2, 6.4/6.7.4.1/6.8 | 15289; 16326 | SOURCE ACQUISITION OPEN | Record concept retained; schema/approval/cardinality open. | PARTIALLY RESOLVED | Open |
| ARP-G01 | Assurance applicability/rigor | ARP4754B, 5.2/5.6.4/App. A; ARP4761A, 3.9/App. P | IEEE 1012; 15026-3; item profiles | PLANNED SOURCES IDENTIFIED | Generic hook plus aviation rigor; no universal scale. | PARTIALLY RESOLVED FOR AVIATION | Open |
| ARP-G02 | Cross-level verification credit | ARP4754B, 4.6.1/5.5.4/5.5.6 | DO-178C/DO-254/DO-297 | PLANNED SOURCES IDENTIFIED | Aviation credit separate from prior-evidence applicability. | RESOLVED FOR AVIATION PROFILE | Resolved |
| ARP-G03 | Unintended-behavior assurance | ARP4754B, 4.6.4/5.5.5.3/App. A; ARP4761A, Cl.4 | DO-178C/DO-254 | PLANNED SOURCES IDENTIFIED | Item criteria open. | KEEP OPEN | Open |
| SAF-G01 | Safety-to-obligation derivation | ARP4761A, 2.2/3.2–3.5/D.4.3; ISO 29148, 5.2.4/6.5.2 | ISO 15289 schema implications | PARTIAL SOURCE COVERAGE | Controlled typed basis required; direct Failure Condition→obligation prohibited; Verification Obligation remains framework-defined. | RESOLVED FOR AVIATION PROFILE | Resolved |
| SAF-G02 | Assumption lifecycle | 24748-2, 6.7.5.3.5; ARP4761A, 2.2/A.6/D.4.3.2/E.4; ISO 29148, 5.2.7/9.5.19 | ISO 15289; literature | PARTIAL SOURCE COVERAGE | Documentation/validation capability semantics strengthened; mandatory ownership, fields, states and cardinalities remain open. | PARTIALLY RESOLVED | Open |
| SAF-G03 | Multi-type independence | ARP4761A, 2.2/Apps. E,J–M,P | IEEE 1012; item profiles | PLANNED SOURCES IDENTIFIED | Types/claims/evidence separated. | RESOLVED FOR AVIATION PROFILE | Resolved |
| SAF-G04 | Safety evidence aggregation | ARP4761A, E.3–E.5/F.3–F.5; ISO 15026-2, 5.3.2/5.3.5 | ISO 15026-1:2025; item profiles | PARTIAL SOURCE COVERAGE | Evidence Item record, framework characterization and source-native Argument use remain distinct; aviation content stays profile-specific. | RESOLVED FOR AVIATION PROFILE | Resolved |
| SAF-G05 | Safety sufficiency | ARP4761A, D.5/E.4/F.4 | 15026 family; item profiles | PLANNED SOURCES IDENTIFIED | Profile inputs exist; authority/threshold open. | PARTIALLY RESOLVED FOR AVIATION | Open |
| SAF-G06 | Safety/change synchronization | ARP4761A, 3.1.1/A.6/E.4/P.1 | IEEE 1012; profiles | PLANNED SOURCES IDENTIFIED | Aviation V10 stable; generic selection open. | RESOLVED FOR AVIATION PROFILE | Resolved |
| REQ-G01 | Requirement/Set identity and lifecycle schema | ISO 29148, 5.2.4–5.2.8/7/9 (concepts/content; 5.2.8 attributes are recommendations/examples) | ISO 15289; 29148→15288 version mapping | PARTIAL SOURCE COVERAGE | Reviewed Requirement/Set concepts exist; identity, mandatory attributes, state and cardinality remain unresolved. | NEW — KEEP OPEN | Open |
| REQ-G02 | Verification Criterion placement and cardinality | ISO 29148, 6.5.2.2 (reproduced lifecycle task, ISO guidance and direct `shall` kept distinct; conformance follows 4.2/6.1) | ISO 15289 | PARTIAL SOURCE COVERAGE | Criterion-to-action/basis representation remains a schema decision; no one-Requirement-to-one-Procedure rule. | NEW — KEEP OPEN | Open |
| ASC-G01 | Claim vocabulary/dependency | ISO 15026-2, 5.3.3 identifies a dated 15026-1:2019 Claim-type locator retained as source provenance; it does not supply the full vocabulary | ISO 15026-1:2025 current vocabulary clauses + targeted Claim/assurance/uncertainty compatibility review | SOURCE ACQUIRED; CLAUSE STUDY PENDING | The framework adopts 2025 as its current vocabulary version. Equivalence with the dated 5.3.3 Claim source is not presumed; no standalone 2019 study or full-edition delta is planned. | NEW — KEEP OPEN | Open |
| ASC-G02 | Artefact→Evidence Item characterization and later argument use | ISO 15026-2, 5.3.2 four-field Evidence Item record and 5.3.5 source-native leaf-Argument reference | ISO 15026-1:2025 dependency; workflow/schema decisions | PARTIAL SOURCE COVERAGE | Characterization/admission is framework-defined and constrained by 5.3.2; later Argument reference is source-native. Workflow/state/authority/cardinality remain open. | NEW — PARTIALLY RESOLVED | Open |
| ASC-G03 | Inference validity/argument quality | ISO 15026-2, 4.1/5.3.4–5.3.5 recursive Inference/Supported Claim structure | ISO 15026-1:2025; assurance literature | PARTIAL SOURCE COVERAGE | Structure is reviewed; no universal validity or sufficiency method. | NEW — KEEP OPEN | Open |
| ASC-G04 | Assurance-case report/snapshot/version | ISO 15026-2, 3.1.2/5.2/5.3.6 report and narrative structure | ISO 15289; registry design | PARTIAL SOURCE COVERAGE | Conceptual report/index structure is reviewed; assembly, baseline, version and interoperability rules remain open. | NEW — KEEP OPEN | Open |

持续状态允许 `Open`、`Research Proposal`、`Partially Supported`、`Resolved`、`Closed as parent`。每行必须保持 established basis、candidate scope 与 framework interpretation 的边界。
