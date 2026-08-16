---
title: ISO 24748-2 and SAE ARP4754B Internal Research Review
status: completed
version: 0.2
baseline: candidate
owner: research
last_updated: 2026-08-16
review_type: internal-research-review
review_target:
  - ../standard_notes/iso_24748_2_targeted_review.md
  - ../standard_notes/sae_arp4754b.md
---

# ISO 24748-2 and SAE ARP4754B Internal Research Review

## 1. Review result

| Area | Result | Review note |
|---|---|---|
| Source/version identity | PASS | ISO clean second edition (2024-03) and SAE ARP4754B (2023-12) verified from local licensed sources |
| ISO 24748-2 targeted scope | PASS | Required clauses and six research questions covered; no unnecessary full-note duplication |
| ARP4754B required clause coverage | PASS | Scope/definitions, Sections 3–6.4 and Appendix A covered |
| Recommended-practice/regulation boundary | PASS | No ARP recommendation restated as law; certification applicability remains contextual |
| Validation/Verification terminology | PASS | ARP contextual taxonomy retained without overwriting ISO generic terminology |
| FDAL/IDAL and ARP4761A boundary | PASS | ARP4754B interface recorded; detailed safety assessment and assignment conclusions deferred |
| Appendix A semantics | PASS | R*/R/A/N, objective applicability, independence, outputs and System Control Category kept separate |
| Gate/review/decision separation | PASS | Transition criteria and test readiness review recorded as aviation-profile inputs while retaining review/assessment/decision/gate separation |
| Coverage/sufficiency claims | PASS | Requirements coverage and Objective 5.1 recorded as domain-specific partial support; generic gaps not closed |
| Evidence/certification separation | PASS | Result, Verification Data, evidence, substantiation, coordination and authority decision kept distinct |
| Modification/reuse semantics | PASS | V10 renamed; prior evidence modeled as conditional credit, not automatic reuse |
| Copyright/source-control hygiene | PASS | No standard PDF, screenshot, extracted text, internal path or extended quotation added to tracked research assets |

**Blocking findings:** 0

**Required changes remaining for this research round:** 0

**Internal review result:** READY FOR EXTERNAL/PR REVIEW

## 2. Locator spot checks

| Research conclusion | Primary locator | Check |
|---|---|---|
| 24748-2 introduces no new requirements | ISO 24748-2, 6.1 | PASS |
| Verification can be applied multiple times by strategy/context | ISO 24748-2, 6.7.5.4.4 | PASS |
| ARP is recommended practice, not regulation | ARP4754B, 1.1 | PASS |
| Development Assurance purpose | ARP4754B, 1.2 | PASS |
| Transition criteria/gate checkpoints | ARP4754B, 3.2.2 | PASS |
| Aircraft/system/item information flow | ARP4754B, 4.6.1 | PASS |
| Requirements validation correctness/completeness | ARP4754B, 5.4 | PASS |
| Implementation Verification and planning | ARP4754B, 5.5; 5.5.4 | PASS |
| Requirements coverage | ARP4754B, 5.5.5.2.2 | PASS |
| Test readiness and unintended behavior | ARP4754B, 5.5.5.3 | PASS |
| Verification Data | ARP4754B, 5.5.6 | PASS |
| Configuration and Process Assurance independence | ARP4754B, 5.6; 5.7 | PASS |
| Modification impact/evidence reuse | ARP4754B, 6.3; 6.4 | PASS |
| Objective 5.1 and R*/R/A/N semantics | ARP4754B, Appendix A | PASS |

## 3. Deliberately deferred questions

- ARP4761A: failure-analysis methods, PSSA/SSA/CCA, detailed FDAL/IDAL assignment and safety evidence relations.
- DO-178C / DO-254: item-level objectives, independence details, coverage taxonomies and tool qualification.
- DO-297: IMA roles, responsibility allocation and integration assurance.
- ISO/IEC/IEEE 15289: cross-standard information-item content and field-level schema provenance.
- Framework: universal sufficiency aggregation, closure authority/state model, evidence-credit cardinality and unintended-behavior coverage.

These are research backlog items, not defects in the present notes.

## 4. External informal review follow-up

The original internal-review result above is retained as research provenance. A subsequent [external informal review](ISO-24748-2--SAE-ARP4754B-External-Informal-Review.md) identified additional research-strength and ontology findings before PR creation:

- `M-01` — V6 / Test Readiness Review ontology relation;
- `M-02` — Result / Evidence ontology strength;
- `m-01` — ARP research-note title ambiguity;
- `m-02` — Appendix A applicability provenance;
- `m-03` — certification-credit-intent dimensionality;
- `m-04` — review provenance and disposition recording.

The branch temporarily returned to `CHANGES REQUIRED BEFORE PR` while these findings were addressed.

## 5. Finding disposition

| Finding | Disposition | Evidence |
|---|---|---|
| M-01 | CLOSED | ARP note and DBSE workflow now model the test-specific review as `contributesTo(V6)`, not equivalence or specialization; review/assessment/decision/gate remain separate |
| M-02 | CLOSED | ARP note, terminology, standards map and information-model workspace separate Evidence identity from applicability, credibility/control and sufficiency |
| m-01 | CLOSED | ARP frontmatter title changed to `Standards Research Note`; recommended-practice boundary retained |
| m-02 | CLOSED | ARP note and VSR preserve source, Appendix A location, objective and FDAL provenance for R*/R/A/N |
| m-03 | CLOSED | VSR places `certification_credit_intent` outside `assurance_applicability` and states that FDAL does not imply it |
| m-04 | CLOSED | This follow-up preserves the original internal result and records the subsequent external-review disposition |

**Final status after targeted corrections:** READY FOR PR REVIEW
