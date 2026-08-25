---
title: Changelog
status: working
version: 0.1
baseline: post-v0.2
owner: research
last_updated: 2026-08-25
dependencies:
  - README.md
  - HANDOFF/current_progress.md
---

# Changelog

## v0.1 — Research Foundation Baseline

### Added

- Repository knowledge architecture
- Research scope
- Research questions
- Working terminology baseline
- Research roadmap
- Normative research workspace
- DBSE/MBSE future architecture
- DCAS domain workspace
- Initial DBSE templates
- Publication views

### Licensing

- Repository original content is released under the MIT License by explicit project decision.

v0.1 establishes research infrastructure and does not claim completion or normative validation of the proposed Verification Assurance Framework.

## v0.2 — Five-Source Conceptual Normative-Foundation Baseline

### Frozen

- Five-source research set: ISO/IEC/IEEE 15288:2023, ISO/IEC/IEEE 24748-1:2024, ISO/IEC/IEEE 24748-2:2024, SAE ARP4754B and SAE ARP4761A.
- V0–V12 conceptual process-view ontology and Generic Core / Extension Point / Civil Aviation Profile boundary.
- Verification Basis, framework-defined Verification Obligation, Result/Evidence/Argument/Claim separation, change-impact and Composite Gate conceptual semantics.
- PR #6 instance repositioning and meta-risk governance: DCAS as knowledge source and ARINC 615A/UAV/LLM scenarios as planned validation instances.

### Boundary

- The authoritative record is `docs/00_overview/research_baseline_v0.2.md` and annotated tag `research-baseline/v0.2`.
- v0.2 is a conceptual normative-foundation baseline, not a complete methodology product, executable architecture, certification-ready package or validated framework.
- ISO 29148/15026-2 research, innovation/HANDOFF governance and later source-control changes are post-v0.2 increments.

## Unreleased

- Recorded PR #14 external `REQUEST CHANGES` at reviewed head `78fe9f222d40758266275547d95e86ed866813b6` and corrected F-01–F-06: separated ARINC release/content and post-release control-state commits; reserved the final method merge SHA as the future definition identity; made mappings directional with one primary relation; aligned missing-identity failure semantics; split architecture promotion/freeze/instance-validation gates; and added bounded scalability plus interface-contract conclusion controls. Lightweight correction-diff rereview remains pending and the PR remains Draft.

### Candidate GVS Core and cross-repository governance

- Positioned the Candidate Generic Verification Suite Core as the principal engineering research outcome, delivered through composable Verification Capability Packages; a complete suite additionally requires Verification Profile, Product Binding and Project Configuration.
- Made machine-readable/executable realization optional and retained SysML/API/schema/metamodel roles as open, gated choices.
- Added the cross-repository instance contract, temporary instance register, ARINC mapping register and ARINC evaluation protocol; recorded active `RB-2026-001-v4.2.1` as a pre-framework legacy baseline with `NOT-DETERMINED` compatibility and PR #9 only as an unmerged migration candidate.
- Corrected PICS/applicability/basis, Test Purpose, Oracle/Verdict and raw-record/Evidence boundaries without starting ISO/IEC 9646 research.
- Added a standard-library repository-governance integrity checker and CI workflow; it performs no Framework semantic automation.
- Non-claims: no new clause study, established-basis or gap change, object promotion, V0–V12 maturity change, schema/API/metamodel freeze, stable registry, instance validation, compatibility approval, certification acceptance or novelty conclusion.

### Practice-comparison reference governance

- Registered NASA/SP-2016-6105 Rev2 and INCOSE-TP-2003-002-04 (SEH 4e) in a new practice-comparison reference register within the Controlled Candidate-Source Baseline: bounded practice-evidence role with local fingerprints, no clause-study candidacy, no gap-closure/established-basis/architecture-impact rights and no Task 022 clause-dataset contribution; second-hand boundaries recorded for INCOSE's 15288:2015 verbatim content and NASA's NPR-attributed statements.
- Added the two drafted practice-comparison research notes (internal review pending): NASA SEH covering V&V object-level reconciliation support, verification completion dual criteria, RVM/V&V-plan information-item samples, TRR/V6 third-source confirmation and abstraction-ladder inputs; INCOSE SEH covering the verification-action five-tuple, V&V action duality with Correctness/Acceptable predicates, similarity credit criteria, decision-gate semantics, the Appendix E information-item dictionary and model VV&A reinforcement.

### Architecture governance

- Clarified V0–V12 as a controlled open candidate architecture while retaining stable V-identifiers and v0.2 historical provenance.
- Added architecture-impact disposition governance and the Architecture Impact Register; metadata/source availability cannot create architecture conclusions.
- Registered ISO/IEC/IEEE 12207:2026 as a not-acquired software-lifecycle candidate foundation for later 15026-4/24748-3 research, without creating clause-level or established-basis claims.
- Expanded planned ISO/IEC/IEEE 24748 coverage with Parts 3, 4, 5 and 10 while retaining Parts 1, 2 and 6.
- Reclassified ISO/IEC/IEEE 24748-8:2019 as a defence-domain profile candidate under formal-revision watch; its FDIS is not a published normative basis.
- Made no clause-level, established-basis, gap-closure, schema, state-machine or certification-readiness claim.

### Research task planning

- Redesigned Tasks 001-022 as `version: 0.6` research-task specifications: unified standard-number titles; expanded RQ/innovation statements instead of ID-only references; added the three overview anchors, target-source-specific research entry, falsifiable preliminary hypotheses, evidence hierarchy, durable downstream-note contract and repository consistency gates. Each source task was checked against its controlled local PDF structure; Task 017 remains metadata-only and Task 022 remains synthesis-only.
- Added a direct practice-source boundary for Task 001 based on the INCOSE and NASA handbook originals: handbook structures may seed self-contained hypotheses but do not depend on the pending-review handbook notes, create target-standard clause records, close gaps, determine Architecture Impact or count as votes.
- Closed the correction-diff review of PR #13 F-01–F-04 and the field-propagation portion of F-05. Subsequent content review corrected F-06–F-09: Task 022 now has a provenance-only adapter and independent-review gate for all seven legacy reviewed sources; RQ6 distinguishes Task 009 direct technique evidence from Task 018 supporting pattern governance and keeps a second direct source open; RQ8 standards work is limited to empirical-validation readiness and remains owned by the three instances; and Task 009 represents technique as a derivation relation. Task 001 now states Annexes A/B are informative, and Task 021 is explicitly a targeted mapping-closure task. PR #13 final rereview passed and it merged by ordinary merge commit `196cfc2426a841a4adb9c9159660253896b0257c`.

- Redesigned PR #11 tasks 001–021 as `version: 0.4` research contracts with explicit RQ ownership, innovation-candidate falsification, negative findings, generalization rights and a mergeable evidence-record schema; added Task 022 for cross-standard synthesis without treating standards silence as novelty.
- Corrected the ISO 29119 second-edition object chain to `test basis → test model → test coverage item → test case → test procedure`; test design technique is recorded as a derivation method/relation, while `test condition` remains edition-transition/collision metadata rather than a fixed current layer.
- Selected ISO/IEC 9646 Parts 1/2/4/5/6/7 as the complete Task 002 population, excluded Part 3 and ITU-T text from the present clause study, and removed paired-equivalence/acquisition gates without claiming textual identity.
- Registered the acquired 154-page ISO/IEC/IEEE 12207:2026 source and the unavailable 12207:2017, 15288:2015 and 24748-4:2016 historical dependency sources; affected semantic mapping rows remain `NOT DETERMINED` and no current established basis was changed.
- Pre-registered DEFERRED Architecture Impact entries for Tasks 001–022 and added candidate task/RQ ownership links to the gap matrix without changing protected established basis, disposition or gap status.
- Added one controlled task specification per actionable standard/work package in the candidate-source baseline, preserving dependency order and independent-review gates.
- Upgraded all 21 current task specifications to agent-executable `version: 0.2` work orders with source gates, complete-inventory rules, standard-specific research packages, extraction records, required mappings, repository deliverables, report structures, independent-review packets, no-overclaim controls and auditable definitions of done.
- Reconciled the earlier PR #11 controlled local source inventory at its reviewed head; the subsequent content-review correction above supersedes its former 12207-not-acquired and 9646-partial status statements. No clause study, gap closure or architecture promotion resulted from acquisition.
- Repaired PR #11 task dependency and scope controls: replaced the Task 001 global lock with dependency-scoped promotion gates, introduced provisional/downstream closure ownership, assigned the IEEE 1012↔15026-3 final matrix to Task 011 and planning-ownership closure to Task 020, corrected Task 016 to the 15288/24748-1 context, and added required old-edition, annex and standard-specific coverage controls. No research conclusion or architecture freeze was performed.
- Addressed PR #11 final re-review precision findings by classifying ISO/IEC/IEEE 24748-3:2020 Annex A as informative, requiring a complete informative-force audit, separating source-native extraction from historical-semantic and current-baseline promotion gates, and aligning the full architecture-impact disposition vocabulary including `DEPRECATE`. Protected gap and preregistered architecture outcomes remain unchanged; final independent re-review passed at head `0f36b39f2ed00ab863c2fef3c9ce56cc28149d3b`.
- Recorded locally verified source files for ISO/IEC/IEEE 15026-3:2023, the ISO/IEC/IEEE 29119-1/-2/-3/-4 set and IEEE 1012-2024 as acquired licensed sources without starting clause study; recorded acquired TTCN-3 parts separately from the still-unselected SysML/tool aggregate.
- Normalized six user-supplied pre-v0.2 work orders into a versioned historical-task archive and restored the PR #4 ARP4761A external review to the reviews workspace without changing its original verdict.

### Consolidated integration

- Closed and externally confirmed re-review findings F-01/F-02 by aligning all current gap references to the authoritative matrix (`REQ-G01` identity/lifecycle schema, `REQ-G02` criterion placement/cardinality, `ISO-G07C` 15289 interoperability) and normalizing the acquired-source/pending-study status.
- Froze `research-baseline/v0.2` before post-v0.2 increments.
- Integrated PR #8 governance through a Controlled Candidate-Source Baseline, controlled candidate-contribution register, temporary cross-repository mappings and governed instance feedback.
- Integrated PR #7 ISO 29148/15026-2 clause studies after independent normative review, with an open ISO-G07 A/B/C split, a current 15026-1:2025 vocabulary dependency, dated-2019 source provenance and explicit source/framework evidence provenance.
- Added a consolidated integration review packet and repository-wide consistency validation. PR #9 was approved and merged by ordinary merge commit `658e3cfcee1d66147c6cbf2d048fc1d46a846f14`; PR #7/#8 were closed as superseded without direct merge, the temporary remote branches were deleted, and `main` is the only remote branch. The controlled research stop now advances to the ISO/IEC/IEEE 15289:2019 clause-level study.

### Research

- Completed independent review of the ISO/IEC/IEEE 29148:2018 and ISO/IEC/IEEE 15026-2:2022 clause studies; retained the post-v0.2 conceptual-candidate boundary and all schema, sufficiency, authority and certification non-claims.
- Clarified ISO 29148 full-conformance scope under 4.2/6.1, classified 5.2.3 as `DIRECT-DESCRIPTIVE`, and separated reproduced lifecycle-task modal force, ISO guidance and direct `shall` statements in 6.5/6.6.
- Adopted ISO 15026-1:2025 as the sole current assurance-vocabulary version; retained the explicit 2019 Claim-type/uncertainty references in 15026-2 only as dated source provenance, cancelled standalone 2019 study and full-edition delta, and kept a targeted Claim/assurance/uncertainty compatibility review open.
- Corrected evidence provenance: ISO 15026-2 defines the four-field Evidence Item record and later leaf-Argument reference, while Result/Artefact characterization/admission remains a framework-defined relation constrained by 5.3.2.
- Selectively promoted reviewed clause support into the gap matrix without closing ISO-G07, ISO-G07B/C, REQ-G01/G02 or ASC-G01–G04.
- Added a controlled candidate-contribution register with claim type, novelty/validation status, falsification condition, source/gap anchor and non-claim; gaps and five-source absences are explicitly not novelty proof.
- Added a HANDOFF workspace (current progress snapshot + next plan) maintained per merged PR; not a source of truth.
- Established a Controlled Candidate-Source Baseline: the source-change process is controlled without claiming a closed source universe; official metadata, availability, layer role, trigger and study state are separated.
- Updated the validation workspace with the methodology–instance decoupling boundary (mapping methodology is generic research; instance artifacts live in external repos).
- Recorded the controlled next sequence: ISO 15289 → ISO 9646/X.290 → 15026-1:2025 clause study and targeted compatibility review → 29119-2/3/4 → IEEE 1012/15026-3 → executable schema → versioned registry → platform architecture → external integration.
- Added a standards layering policy to the target baseline: one primary layer role per source (generic methodological / domain assurance profile / instance standard / execution technology), layer-bounded conclusion rights, dual-role splitting and abstraction-ladder-only cross-layer flow.
- Added ISO/IEC/IEEE 15026-2 (assurance case content, Phase 5/RQ4 input) and ISO/IEC TR 29119-11:2020 (AI-based system testing, third-instance reference) to the candidate-source backlog; marked TTCN-3 as execution technology.
- Added a framework-object provenance annex (§28) to the five-source consolidation report: per-object source-native/framework-defined attribution, non-aviation generic-basis audit, frozen boundaries, open items and schema gates; zero new files, definition-ownership rule recorded in ARCHITECTURE.md.
- Recorded RQ4 partial-progress boundary (assessment interface frozen; reasoning semantics, criteria and authority open for Phase 5).
- Added a coverage note to the cross-standard map so unstudied TBD columns cannot be misread as conclusions; map rows double as the methodology constraint register.
- Refactored the gap matrix to separate established clause basis, candidate-source scope and controlled source-search status; unstudied sources cannot close gaps or establish novelty.
- Added a standards-research touch-point checklist to CONTRIBUTING.md.
- Repositioned DCAS from primary validation case to industrial-practice knowledge source; ARINC 615A protocol conformance verification becomes the first validation instance, with UAV flight-management and LLM service reliability/performance verification as planned instances.
- Recorded the three-tier research output chain: product-independent Verification Methodology → Model-Based Verification Architecture → non-productized Verification Platform research prototype.
- Recorded the two-sided standards-research goal (what standards say = construction basis; what they omit = innovation space) and the explicit abstraction ladder for promoting domain practices and instance-related standards into the generic methodology.
- Added the instance × framework-element exercise matrix and validation-instance set to the validation workspace so each instance's thesis contribution is explicit.
- Added generic conformance-testing methodology sources (ISO/IEC 9646 / ITU-T X.290 series; ETSI ES 201 873 TTCN-3) to the standards target baseline as generic-layer research targets scored alongside ISO 15289; registered ARINC 615A as the first-instance protocol standard (Level E).
- Updated RQ8 and publication candidate views to match the new instance strategy.
- Addressed PR #4 external review findings: corrected ARP4761A Section 1 locators, replaced the linear Safety Requirement chain with typed multi-source provenance, and separated independence definitions from Appendix P/CMA substantiation criteria.
- Preserved the original ARP4761A internal-review result as historical provenance and recorded R-01–R-03 dispositions for re-review.

- Added a clause- and appendix-level SAE ARP4761A research note covering AFHA/PASA/SFHA/PSSA/SSA/ASA, FDAL/IDAL, typed independence, assumptions, safety-analysis methods, evidence and completion boundaries.
- Added the ARP4761A five-column mapping and six safety-specific gap candidates (`SAF-G01`–`SAF-G06`).
- Established a dual Verification Assurance / Safety Assessment process-view architecture without replacing V0–V12.
- Extended V10 with an aviation Safety Reassessment subflow and V11/V12 with safety coverage, sufficiency and completion inputs.
- Added candidate aviation safety-context fields and information-model entities while retaining generic/profile separation and `MBSA ≠ MBSE`.
- Set the next stop point to a Cross-Standard Consistency & Gap Review before any DO-178C, DO-254 or DO-297 study.

- Added a targeted applicability review of ISO/IEC/IEEE 24748-2:2024 and classified it as reviewed supporting guidance with a minor framework delta.
- Added a full SAE ARP4754B clause-level research note, Appendix A objective mapping, ISO comparison, and aviation-profile boundary decisions.
- Extended the five-column map and gap matrix for development assurance, requirements validation, implementation verification, FDAL-dependent independence/control, coverage, sufficiency, change impact, evidence reuse, and certification coordination.
- Renamed V10 from `Regression` to `Change Impact & Re-verification` while preserving its stable identifier.
- Extended the Verification Strategy Record with optional aviation-profile applicability, cross-level credit, unintended-behavior, configuration, and prior-evidence-credit fields.
- Applied the external informal review corrections to the ISO 24748-2 / ARP4754B research slice.
- Refined ARP4754B Test Readiness Review as a test-specific aviation-profile review that may contribute to V6, without equating it to the framework composite gate.
- Refined Verification Result / Evidence semantics to separate evidence identity, provenance, applicability, control/credibility, and sufficiency.
- Preserved Appendix A Objective × FDAL provenance and separated certification-credit intent from assurance applicability in the candidate VSR schema.

- Added clause-level ISO/IEC/IEEE 15288:2023 research note and evidence-backed cross-standard mapping.
- Added meaningful gaps for independence, coverage, sufficiency, Oracle, regression, closure, information schemas, and MBSE evidence.
- Reframed V0–V12 as an iterative, recursive, concurrent Verification Activity Architecture / process view.
- Added and applied the informal ISO 15288 review provenance: corrected the Clause 3.36 requirement definition and refined requirement validation, V0/V2/V9 support boundaries and baseline-candidate status.
- Added the ISO/IEC/IEEE 24748-1:2024 clause/annex research note from the official clean publication and expanded the five-column standards mapping.
- Reclassified V0–V12 as mixed-ontology elements in a Verification Assurance Process View; separated lifecycle reviews, readiness assessments and gate decisions.
- Added lifecycle/process instantiation, gate semantics, review taxonomy and process-view provenance gaps plus a research-draft tailoring record.
- Prioritized ISO/IEC/IEEE 24748-2:2024 for the next research round; the targeted review is now completed above.
- Applied the informal ISO 24748-1 review: generalized the gap-matrix scope, updated the multi-standard five-column mapping description, and tightened the Clause 2 conformance inference.

### Changed

- Replaced the ISO/IEC/IEEE 24748-1:2024 research source baseline from a Redline representation to the official clean 2024 edition.
- Revalidated Annex F.3.6 as `Verification reviews` and retained Annex D, F and G as informative guidance.
- Removed Redline-specific interpretation from active research assets and aligned source provenance and locators with the clean edition.
- Preserved the existing Verification Assurance Process View and composite-gate architecture conclusions.
