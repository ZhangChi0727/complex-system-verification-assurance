---
title: Normative Gap Matrix
status: reviewed
version: 1.6
baseline: post-v0.2
owner: research
last_updated: 2026-08-20
dependencies:
  - standards_baseline.md
  - standards_map.md
  - consolidation/five_source_consistency_gap_review.md
  - consolidation/architecture_impact_register.md
---

# Normative Gap Matrix

本矩阵把**已经研究并评审的条款依据**与**尚待研究/评审的候选来源**分开。Gap 是研究问题和候选贡献的输入，不是创新证明。未评审来源不得进入 `Established clause basis`、关闭 gap 或支撑强 novelty claim。

本矩阵不证明 V0–V12 已完成架构收敛。候选来源对稳定 V-ID、现行语义、边界或拓扑的影响由 `consolidation/architecture_impact_register.md` 控制；metadata verification 或 source acquisition 均不能产生 architecture disposition。

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
| ISO-G05 | Re-verification selection/impact | ISO 15288, 6.3.5/6.4.9; 24748-2, 6.7.5.4.4; ARP4754B, 6.3–6.4; ARP4761A, 3.1.1/A.6/E.4/P.1 | IEEE 1012; ISO/IEC/IEEE 24748-10:2026; literature | PLANNED SOURCES IDENTIFIED | V10 chain is the current checkpoint; universal selection plus iteration/re-entry/change-response semantics remain open. | PARTIALLY RESOLVED | Open |
| ISO-G06 | Closure authority/state | ISO 15288, 6.3.2/6.4.9; 24748-1, 4.3/Cl.5; ARP4754B, 3.2.2/4.7/5.5–5.7 | 16326; literature | SOURCE ACQUISITION OPEN | Composite Gate is the current checkpoint; waiver/reopen/authority/state remain open. Defence-profile 24748-8 cannot directly support generic closure. | PARTIALLY RESOLVED | Open |
| ISO-G07 | Overall Verification-Assurance Information-Item Architecture | Five-source record/relation basis: ISO 15288, 5.6/6.3.6/6.4.9; 24748-1, 6.2.8; 24748-2, 6.7.4/6.8; ARP4754B, 5.4.7/5.5.6 | Reviewed refinements: 29148/15026-2; remaining: 15289/29119-3; planned candidates: 24748-3/-4/-5/-6 | PARTIAL SOURCE COVERAGE | Reviewed requirements/assurance slices refine successors but do not complete the parent taxonomy; planned 24748 parts provide no established basis before study. | SPLIT → ISO-G07A/B/C | Open |
| ISO-G07A | Requirements and Assurance-Case Conceptual Item/View Taxonomy | Five-source conceptual relations; ISO 29148, 4.4/7/9.5/9.6; ISO 15026-2, 5.2/5.3.1–5.3.6 | ISO 15289 interoperability and remaining VAF views | PARTIAL SOURCE COVERAGE | Requirement/Set, BRS/StRS/SyRS/SRS and assurance-case structure are reviewed slices; whole-VAF completeness not claimed. | PARTIALLY RESOLVED | Partially Supported |
| ISO-G07B | Executable schema, cardinality, state and serialization | Five sources do not establish executable schema | 15289; 29119-3; schema literature | PLANNED SOURCES IDENTIFIED | Fields, identities, cardinalities, lifecycle states and serialization remain open. | KEEP OPEN | Open |
| ISO-G07C | ISO 15289 interoperability and document/record mapping | — | ISO/IEC/IEEE 15289:2019 (source acquired); 24748-4/-5 planning and 24748-6 integration information-item overlap candidates | SOURCE ACQUIRED; CLAUSE STUDY PENDING | 15289 source acquired; clause-level mapping not started. Planned 24748 sources cannot establish schema support before study. | NEW — KEEP OPEN | Open |
| ISO-G08 | MBSE/model evidence | ISO 15288, Annex D; 24748-1, Annex A.10; ARP4761A, Appendix N | 24641; IEEE 1012; literature | PLANNED SOURCES IDENTIFIED | No generic tool qualification/admissibility regime. | KEEP OPEN | Open |
| LC-G01 | Gate ontology | ISO 24748-1, 4.3/Cl.5/6.2.6 | 24748-8:2019 defence-domain profile candidate; formal revision watch | PARTIAL SOURCE COVERAGE | Assessment, optional review, authority decision and event remain separate; defence review/audit rules require cross-domain abstraction and cannot be generalized directly. | RESOLVED GENERICALLY | Resolved |
| LC-G02 | Review taxonomy | ISO 24748-1, 6.4/Annexes C,F | 24748-8:2019 defence-domain profile candidate; formal revision watch | SOURCE ACQUISITION OPEN | Method/lifecycle review and decision remain distinct; the FDIS is not a published basis and will not be studied. | RESOLVED GENERICALLY | Resolved |
| LC-G03 | Process-view provenance | ISO 15288, 5.8; 24748-1, Annex D | 15289; ISO/IEC/IEEE 12207:2026 software-lifecycle process/view foundation; 24748-3 software-lifecycle application; 24748-10 iteration/re-entry; registry design | PARTIAL SOURCE COVERAGE | Framework orchestration remains labelled; 12207:2017→2026 mapping and all candidate impacts are deferred pending clause study. | RESOLVED GENERICALLY | Resolved |
| LC-G04 | Process-instantiation evidence schema | 24748-1, 6.2.2–6.2.8; 24748-2, 6.4/6.7.4.1/6.8 | 15289; 16326; ISO/IEC/IEEE 12207:2026 software-process instantiation candidate; 24748-3/-4/-5/-6 lifecycle/planning/integration information-item candidates | SOURCE ACQUISITION OPEN | Record concept retained; schema/approval/cardinality and source overlap remain open. 12207 is not treated as a complete information-item content definition; that interface remains dependent on 15289. | PARTIALLY RESOLVED | Open |
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

## Planned research-task coverage overlay

This overlay adds task ownership and RQ links only. It does not modify the established basis, source-search status, disposition or status in the controlled matrix above. Task 022 reconciles reviewed outputs and cannot close a gap solely from standard silence.

| Gap family | Candidate tasks | RQ / synthesis owner |
|---|---|---|
| ISO-G01 / ARP-G01 / SAF-G03 | 010, 011 | RQ2/RQ3/RQ4/RQ5/RQ8; Task 022 |
| ISO-G02A/B | 006, 007, 009, 019 | RQ3/RQ4/RQ6/RQ7; Task 022 |
| ISO-G03A/B / SAF-G05 | 003, 004, 005, 009, 010, 011, 019 | RQ4/RQ5; Task 022 |
| ISO-G04 | 002, 005, 006, 009 | RQ3/RQ5/RQ8; Task 022 |
| ISO-G05 / SAF-G06 | 004, 005, 007, 010, 013, 015, 016 | RQ2/RQ3/RQ5/RQ8; Task 022 |
| ISO-G06 | 005, 007, 012, 020 | RQ2/RQ5/RQ7; Task 022 |
| ISO-G07/A/B/C / ASC-G02/G04 | 001, 002, 003, 005, 006, 008, 012–015, 018, 020, 021 | RQ1/RQ3/RQ5/RQ7/RQ8; Task 022 |
| ISO-G08 | 005, 010, 018 | RQ3/RQ5/RQ7/RQ8; Task 022 |
| LC-G01/G02 | 017 metadata watch only; future clause-study task required | no current RQ evidence; Task 022 retains open/deferred boundary |
| LC-G03/G04 | 001, 004, 005, 007, 012–016, 020 | RQ1/RQ2/RQ3/RQ5/RQ7/RQ8; Task 022 |
| SAF-G01/G02/G04 | 001, 003, 004, 005, 008, 018 | RQ1/RQ4/RQ5/RQ7/RQ8; Task 022 |
| REQ-G01/G02 | 001, 005, 006, 008, 021 | RQ1/RQ3/RQ7; Task 022 |
| ASC-G01/G03 | 003, 004, 011 | RQ4/RQ5; Task 022 |
