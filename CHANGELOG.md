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

### Research

- Added a controlled candidate-contribution register with claim type, novelty/validation status, falsification condition, source/gap anchor and non-claim; gaps and five-source absences are explicitly not novelty proof.
- Added a HANDOFF workspace (current progress snapshot + next plan) maintained per merged PR; not a source of truth.
- Established a Controlled Candidate-Source Baseline: the source-change process is controlled without claiming a closed source universe; official metadata, availability, layer role, trigger and study state are separated.
- Updated the validation workspace with the methodology–instance decoupling boundary (mapping methodology is generic research; instance artifacts live in external repos).
- Recorded the controlled next sequence: ISO 15289 → ISO 9646/X.290 → 15026-1:2019/2025 delta → 29119-2/3/4 → IEEE 1012/15026-3 → executable schema → versioned registry → platform architecture → external integration.
- Added a standards layering policy to the target baseline: one primary layer role per source (generic methodological / domain assurance profile / instance standard / execution technology), layer-bounded conclusion rights, dual-role splitting and abstraction-ladder-only cross-layer flow.
- Added ISO/IEC/IEEE 15026-2 (assurance case content, Phase 5/RQ4 input) and ISO/IEC/IEEE 29119-11 (AI-based system testing, third-instance reference) to the standards backlog; marked TTCN-3 as execution technology under the layering policy.
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
