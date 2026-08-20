---
title: ISO/IEC 9646 and ITU-T X.290 Series Scoping Research Task
status: planned
version: 0.2
baseline: post-v0.2
owner: research
last_updated: 2026-08-20
dependencies:
  - README.md
  - ../standards_baseline.md
  - ../normative_gap_matrix.md
---

# ISO/IEC 9646 and ITU-T X.290 Series Scoping Research Task

## Control record

| Field | Value |
|---|---|
| Order / priority | 02 / targeted conformance-methodology study |
| Baseline status | `PARTIAL SOURCE ACQUISITION; PART SELECTION/REMAINING ACQUISITION OPEN` |
| Source | Parts 1/2/4/5/6/7 acquired and fingerprinted; Part 3 / X.292 and the controlled paired-Recommendation set remain open |
| Layer / trigger | Generic methodological source / ISO-G04 and conformance instance |
| Initial impact | `DEFERRED — part selection and remaining acquisition pending` |

### Controlled local source inventory

| Part | Canonical local file | Physical pages | SHA-256 | Control status |
|---|---|---:|---|---|
| ISO/IEC 9646-1:1994 | `references/PDF/9646-1-1994.pdf` | 56 | `A879A40A00F2B4086A3D1D4E68497D0008F24D5D6C43A531B13112CFE5E92F65` | Acquired; selection open |
| ISO/IEC 9646-2:1994 | `references/PDF/9646-2-1994.pdf` | 40 | `B16937B8DAAFB45A9B2DCFBD73F2F00B20B39714B6D8E192AC1C0EFD3DA2333` | Acquired; selection open |
| ISO/IEC 9646-3 / ITU-T X.292 | — | — | — | Not acquired; include/context/exclude decision required |
| ISO/IEC 9646-4:1994 | `references/PDF/9646-4-1994.pdf` | 20 | `4177D2EEA43675C0F1AA6ADA450573DCC9B1E484800E3D13402B2240C80CDED7` | Acquired; selection open |
| ISO/IEC 9646-5:1994 | `references/PDF/9646-5-1994.pdf` | 44 | `A09BB65A2AD43C22F9E95D336BEC777D9BBCF7F26D324AA2FA6220755AAD2490` | Acquired; selection open |
| ISO/IEC 9646-6:1994 | `references/PDF/9646-6-1994.pdf` | 24 | `9B14CD1BF9E9FF5872B387FBFBF7E8CDAE7CE60EFFC9192C73157C584800B3ED` | Acquired; protocol-profile specialization |
| ISO/IEC 9646-7:1995 | `references/PDF/9646-7-1995.pdf` | 68 | `AC28B93C3670C9EC6932785E8F73457645F652DC27D92C46DA7D49320D9CCB35` | Acquired; selection open |

The work package remains partial until Part 3/X.292 and paired-Recommendation selection are controlled; acquisition of six ISO parts does not authorize a completed study.

## Objective

Select the authoritative parts needed to define generic conformance-testing concepts and determine whether they support Case, Procedure, expected result, verdict and oracle-validity concerns.

## Required questions

- Which ISO 9646 and paired X.290 parts are current, historical or superseded, and which are actually relevant?
- How are implementation under test, abstract test suite, test purpose, test case, procedure, verdict and conformance claim distinguished?
- Does any selected clause support the VAF Oracle proposal, or only expected-result/verdict structures?
- Which concepts are methodology and which belong to execution technology such as TTCN-3?

## Required work and outputs

1. Produce a canonical part/version/relationship register before acquiring text.
2. Acquire and fingerprint only the selected authoritative sources; do not use TTCN-3 files as substitutes.
3. Produce `../standard_notes/iso_iec_9646_itu_t_x290_targeted_study.md` and an ISO-G04 crosswalk.
4. Record `NO-IMPACT`, another reviewed disposition, or keep `DEFERRED`; do not promote Oracle from title-level evidence.

## Stop conditions

No clause study begins until the exact parts and sources are controlled. No conformance or certification claim may be inferred from a test verdict alone.

## Detailed execution specification

### Execution outcome and boundary

This is a selection-and-targeted-study work package, not permission to research an unspecified family. The agent must first establish which ISO/IEC 9646 parts and equivalent ITU-T X.290-series Recommendations provide the conformance-testing methodology needed by ISO-G04. Only the selected, acquired and fingerprinted texts may support conclusions.

### Phase A — canonical series register

Using official catalogues, build a part-level register with canonical identifier, title, edition/date, status, replacement/supersession, ISO↔ITU equivalence, relevance and acquisition decision. At minimum investigate the parts governing general concepts, abstract test suite specification, test realization, laboratory/client responsibilities, protocol implementation extra information, conformance claims and test management. Record why each part is `include`, `context`, `exclude` or `unavailable`.

Do not treat ETSI TTCN-3, a vendor tutorial, a catalogue abstract or a later tool language as the normative methodology source. If the authoritative selected texts cannot be acquired, finish the register, update the blocker and stop before clause conclusions.

### Phase B — source control

For each included source record local path, canonical title, edition/date, page count, SHA-256, completeness, language and official status. Inspect normative references and annex status. Licensed texts remain outside Git. Conflicting ISO and ITU editions must be treated as separate sources unless formal equivalence is established.

### Phase C — mandatory research packages

Analyse the selected clauses for:

1. implementation under test/system under test and implementation conformance statement boundaries;
2. conformance requirement, test purpose, abstract test case, executable/means-of-testing concepts and test suite structure;
3. preamble, test body, postamble, coordination procedure and test event relationships where present;
4. observed outcome, expected outcome, verdict, inconclusive result, error and test-system validity;
5. controllability, observability, test architecture, upper/lower tester and points of control/observation;
6. parameterization, selection, applicability and capability declarations;
7. test campaign/reporting, traceability and conformance claim limits;
8. separation between methodology, notation and execution technology.

### Evidence extraction template

Each used proposition shall record exact part and clause/table/annex locator, PDF page, source class/modality, faithful paraphrase, native objects/relations, applicability conditions, framework implication, ISO-G04 relevance and confidence. Follow `source → interpretation → VAF implication → proposal`; expected outcome or verdict language must not silently become an `Oracle` entity.

### Required mappings and tests

Produce:

- a series/part relationship register;
- `native concept → VAF Case/Procedure/Expected Result/Observed Result/Verdict/Oracle candidate` crosswalk;
- `methodology → notation → executable test system` boundary matrix;
- an Oracle hypothesis test addressing correctness, configuration, provenance, authority and failure modes;
- a claim-boundary table distinguishing test verdict, implementation conformance statement, conformance claim, certification and authority decision.

For each Oracle attribute proposed by VAF, mark `direct support`, `indirect support`, `contradicted`, `absent` or `not applicable`, with locators and limitations.

### Repository deliverables

Create `../standard_notes/iso_iec_9646_itu_t_x290_targeted_study.md`; update the source baseline with all selected parts and fingerprints; update ISO-G04 and only genuinely affected gaps; update `../standards_map.md` and `../consolidation/architecture_impact_register.md`; update HANDOFF and CHANGELOG states; create an independent-review packet listing source selection, exclusions, changed files, Oracle disposition and unresolved acquisition issues.

### Required disposition

The final report must choose and justify one of: `Oracle unsupported`, `Oracle partially supported as a framework abstraction`, `Oracle requires modification/split`, or `DEFERRED`. It must also identify whether conformance-testing concepts are generic methodological candidates or a protocol-testing profile. Any `EXTEND/MODIFY/SPLIT/MERGE` disposition requires migration notes.

### No-overclaim rules

Do not state that a passed test proves total product conformance, certification or assurance sufficiency. Do not equate expected result, verdict mechanism and oracle validity. Do not generalize a protocol test architecture to every verification context. Do not claim current equivalence between historical ISO parts and ITU Recommendations without controlled evidence.

### Mandatory execution sequence and report structure

Execute in this order: snapshot state; build the official series register; approve included/excluded parts; acquire/fingerprint selected sources; inventory clauses; extract terminology and test architecture; build verdict/oracle/claim mappings; apply bounded repository changes; run consistency checks; create review packet; stop at review.

The study note shall contain: control record; selection method; official part/equivalence register; acquisition/fingerprint table; clause inventories by part; terminology; test architecture; test specification/realization chain; outcome/verdict model; Oracle hypothesis test; conformance-claim boundary; methodology/notation/technology boundary; gap and architecture dispositions; limitations; repository delta; conclusions and review handoff.

The review packet shall reconcile every selected/excluded part, every primary clause and each Oracle attribute; list changed files and statuses; and include copyright, link and overclaim checks. Metadata-only blocked work must use the same packet to show that no clause conclusion was introduced.

### Definition of done

Done requires an authoritative part register, controlled sources for every studied part, clause inventories with exclusion rationales, all five mappings/tests above, locator-backed conclusions, synchronized repository statuses, successful Markdown/link/diff checks and an independent review disposition. A metadata-only outcome is valid only if clearly recorded as blocked and contains no clause-derived claim.
