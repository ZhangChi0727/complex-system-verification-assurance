---
title: SAE ARP4761A Internal Research Review
status: completed
version: 0.2
baseline: candidate
owner: research
last_updated: 2026-08-16
review_type: internal-research-review
review_target:
  - ../standard_notes/sae_arp4761a.md
  - ../standards_map.md
  - ../normative_gap_matrix.md
---

# SAE ARP4761A Internal Research Review

## 1. Review result

| Area | Result | Review note |
|---|---|---|
| Source/version identity | PASS | SAE ARP4761 Revision A, revised 2023-12, verified from the licensed local source |
| Scope and status boundary | PASS | Recommended-practice and certification-context limits retained; no regulation claim |
| Main-body coverage | PASS | Scope, definitions and Sections 3.1–3.9 covered |
| Focus-appendix coverage | PASS | Appendices A–F, P and Q role/boundary reviewed; Appendix Q remains illustrative and is not reproduced |
| Method-appendix coverage | PASS | Appendices G–O mapped only to method taxonomy, obligations, independence, evidence and model boundaries |
| Safety provenance chain | PASS | Failure Condition → classification → Safety Objective → Safety Requirement → constraints → obligation recorded with typed relations |
| FDAL/IDAL boundary | PASS | Development-assurance constraints retained; not relabeled as Verification Levels/methods/classifications |
| Independence taxonomy | PASS | Functional, item-development, physical and process forms separated; Principle ≠ Requirement |
| Verification/Safety Assessment boundary | PASS | SSA/ASA evidence interaction retained; SSA ≠ Verification Process and ASA ≠ V12 |
| Assumption lifecycle | PASS | capture, propagation, conversion, confirmation, correction and change reassessment represented |
| Evidence/coverage/sufficiency | PASS | multi-source evidence and aviation coverage dimensions recorded without universal metric/percentage claims |
| Change synchronization | PASS | V10 safety reassessment subflow added without changing stable ID |
| Cross-standard consistency | PASS | ARP4754B development assurance and ARP4761A safety assessment responsibilities compared explicitly |
| Required questions | PASS | R4761-Q01–Q15 and final framework questions 1–15 answered |
| Copyright/source-control hygiene | PASS | No licensed PDF, extracted text, screenshots, figures, tables or internal source path added to tracked research artefacts |

**Blocking findings:** 0

**Required changes remaining for this research round:** 0

**Internal review result:** READY FOR EXTERNAL/PR REVIEW

## 2. Locator spot checks

| Conclusion | Primary locator | Check |
|---|---|---|
| Recommended-practice scope and alternative effective processes | Section 1; 1.3 | PASS |
| Core definitions and four independence types | 2.2 | PASS |
| Iterative safety-assessment interactions and completion | 3.1.1 | PASS |
| Safety-analysis method taxonomy | 3.1.2; Section 4 | PASS |
| AFHA/PASA/SFHA/PSSA roles | 3.2–3.5 | PASS |
| SSA/ASA implemented-design assessments | 3.6–3.7 | PASS |
| Analysis depth and FDAL/IDAL purpose | 3.8–3.9 | PASS |
| Assumption lifecycle | A.6; D.4.3.2; E.4 | PASS |
| PSSA Safety Requirement provenance/completion | D.4.3; D.5–D.6 | PASS |
| SSA evidence aggregation/completion | E.3–E.5 | PASS |
| ASA completion/outputs | F.4–F.5 | PASS |
| MBSA technology neutrality, model verification and documentation | N.1; N.3.6; N.5 | PASS |
| FDAL/IDAL assignment, independence and reuse | P.1–P.5 | PASS |
| Appendix Q illustrative status | 1.3; Appendix Q | PASS |

## 3. Boundary assertions

- ARP4761A is not treated as a regulation or complete certification basis.
- Failure Condition Classification does not directly define a verification method or test count.
- Safety Analysis Method and Verification Method remain separate taxonomies.
- FDAL/IDAL are aviation Development Assurance constraints, not generic Verification Levels.
- SSA and ASA aggregate/evaluate evidence; neither replaces ARP4754B Implementation Verification.
- Safety Assessment completion contributes aviation-profile inputs to V12 but does not equal V12.
- Safety-specific objects remain behind an Aviation Profile boundary pending cross-standard review.

## 4. Deliberately deferred questions

- Generic promotion/cardinality/state semantics for `Assumption` and typed independence.
- Formal claim ontology and sufficiency argument structure for safety-objective/requirement satisfaction.
- DO-178C/DO-254 item-objective and independence mapping; DO-297 IMA responsibility/allocation mapping.
- Universal coverage, closure authority, waiver/reopening and model/tool evidence-admissibility rules.

## 5. Recommended next step

Run a Cross-Standard Consistency & Gap Review over ISO/IEC/IEEE 15288:2023, ISO/IEC/IEEE 24748-1:2024, ISO/IEC/IEEE 24748-2:2024, SAE ARP4754B and SAE ARP4761A. Do not start item-level standards automatically.

## 6. External PR review follow-up

The original internal-review result above is preserved as historical research provenance. A subsequent PR #4 external review identified three source-provenance/ontology-strength findings:

- `R-01` — invalid ARP4761A `1.4` locator;
- `R-02` — over-linear Safety Requirement provenance;
- `R-03` — source definition and substantiation criterion mixed for independence.

The branch returned temporarily to `CHANGES REQUIRED` while these targeted corrections were applied. V0–V12 stable IDs, V10 `Change Impact & Re-verification`, the dual process-view architecture, SAF-G01–SAF-G06 and the Generic/Aviation Profile boundary were retained.

## 7. Finding disposition

| Finding | Status | Files changed | Resolution |
|---|---|---|---|
| R-01 | CLOSED | `sae_arp4761a.md`; this review | Replaced nonexistent `1.1–1.4`/`1.4` references with Section 1 and 1.3 locators; repository scan confirms no ARP4761A `1.4` locator remains |
| R-02 | CLOSED | ARP4761A note; gap/map; terminology; DBSE/information model; VSR | Replaced the unique linear chain with typed multi-source origins from Safety Objective or Safety Process constraints, including Independence Principle, controlled assumption and architecture/analysis provenance; obligation formation still requires a Requirement/Constraint relation |
| R-03 | CLOSED | ARP4761A note; terminology | Restored the 2.2 source definitions for all four independence types and separated Appendix P/CMA claim-substantiation criteria and evidence |

**Status after targeted corrections:** READY FOR PR RE-REVIEW
