---
title: ISO/IEC 9646 Series Clause Research Task
status: planned
version: 0.4
baseline: post-v0.2
owner: research
last_updated: 2026-08-21
task_type: clause-study
research_questions: [RQ3, RQ5, RQ8]
innovation_candidates: [INN-T2, INN-T3, INN-M4, INN-I2]
contribution_modes: [support, qualify, falsify, no-evidence]
source_population: complete-clauses
dependencies:
  - README.md
  - ../standards_baseline.md
  - ../normative_gap_matrix.md
downstream_closure:
  - "Task 002: final ISO/IEC 9646 source-native disposition after independent review"
  - "Architecture synthesis: ISO-G04 promotion decision after independent review"
---

# ISO/IEC 9646 Series Clause Research Task

## Control record

| Field | Value |
|---|---|
| Order / priority | 02 / targeted conformance-methodology study |
| Baseline status | `SOURCE POPULATION ACQUIRED; CLAUSE STUDY PENDING` |
| Source | ISO/IEC 9646 Parts 1/2/4/5/6/7 acquired and fingerprinted; complete controlled population for this methodology study |
| Layer / trigger | Generic methodological source / ISO-G04 and conformance instance |
| Initial impact | `DEFERRED — clause study and independent review pending` |

### Controlled local source inventory

| Part | Canonical local file | Physical pages | SHA-256 | Control status |
|---|---|---:|---|---|
| ISO/IEC 9646-1:1994 | `references/PDF/9646-1-1994.pdf` | 56 | `A879A40A00F2B4086A3D1D4E68497D0008F24D5D6C43A531B13112CFE5E92F65` | Included |
| ISO/IEC 9646-2:1994 | `references/PDF/9646-2-1994.pdf` | 40 | `B16937B8DAAAFB45A9B2DCFBD73F2F00B20B39714B6D8E192AC1C0EFD3DA2333` | Included |
| ISO/IEC 9646-3 | — | — | — | `OUT OF SCOPE — TEST NOTATION / EXECUTION TECHNOLOGY`; not a blocker |
| ISO/IEC 9646-4:1994 | `references/PDF/9646-4-1994.pdf` | 20 | `4177D2EEA43675C0F1AA6ADA450573DCC9B1E484800E3D13402B2240C80CDED7` | Included |
| ISO/IEC 9646-5:1994 | `references/PDF/9646-5-1994.pdf` | 44 | `A09BB65A2AD43C22F9E95D336BEC777D9BBCF7F26D324AA2FA6220755AAD2490` | Included |
| ISO/IEC 9646-6:1994 | `references/PDF/9646-6-1994.pdf` | 24 | `9B14CD1BF9E9FF5872B387FBFBF7E8CDAE7CE60EFFC9192C73157C584800B3ED` | Acquired; protocol-profile specialization |
| ISO/IEC 9646-7:1995 | `references/PDF/9646-7-1995.pdf` | 68 | `AC28B93C3670C9EC6932785E8F73457645F652DC27D92C46DA7D49320D9CCB35` | Included |

ITU-T X.29x numbers are bibliographic relationships only. No ITU acquisition or paired locator is required, and textual identity must not be claimed. Part 3 is excluded because TTCN representation is outside this task; a future ATS serialization, TTCN or executable-suite ADR must open a separate task.

## Objective

Extract the selected ISO/IEC 9646 methodology family and determine how capability/applicability, test-purpose, abstract/executable-test, result, verdict, report and conformance-claim semantics constrain VAF.

## Required questions

- How do the selected ISO/IEC 9646 parts divide general concepts, ATS specification, test realization, laboratory/client responsibility, protocol-profile testing and implementation conformance statements?
- How are implementation under test, abstract test suite, test purpose, test case, procedure, verdict and conformance claim distinguished?
- Does any selected clause support the VAF Oracle proposal, or only expected-result/verdict structures?
- Which concepts are methodology and which belong to execution technology such as TTCN-3?

## Required work and outputs

1. Reconfirm the six included ISO sources and the controlled Part 3/ITU exclusion decision.
2. Produce `../standard_notes/iso_iec_9646_series_clause_study.md` and an ISO-G04 crosswalk; do not use TTCN-3 files as substitutes.
3. Cover PICS/ICS, PIXIT/IXIT, test purpose, ATS/ETS, means of testing, laboratory/client, verdict/report/claim and Part 7 SCS/ICS/profile-RL support/status/predicate semantics.
4. Record `NO-IMPACT`, another reviewed disposition, or keep `DEFERRED`; do not promote Oracle from title-level evidence.

## Stop conditions

No conformance or certification claim may be inferred from a test verdict alone. Part 3/ITU acquisition is not a stop condition; any notation/tool interpretation must stop and open a separate task.

## Research contribution contract

This task answers RQ3/RQ5/RQ8 for conformance testing by studying Parts 1, 2, 4, 5, 6 and 7 as the complete controlled population. It shall connect capability/applicability declarations, test purposes, abstract/executable means, expected/observed outcomes, verdicts, reports and claims while preserving the boundary between protocol conformance testing and lifecycle assurance.

## Candidate falsification tests

- `INN-T2/INN-I2`: test whether the family already supplies an equivalent controlled chain from basis and applicability through obligation/test purpose to evidence-backed claim.
- `INN-T3`: test whether result, report, verdict and conformance claim already carry equivalent provenance/credibility separation.
- `INN-M4`: test whether expected-result or means-of-testing controls provide an equivalent governed Oracle object; do not rename them by assumption.

## Negative findings and non-answers

Record Part 3 as `OUT OF SCOPE — TEST NOTATION / EXECUTION TECHNOLOGY`. ITU-T X.29x identifiers are bibliographic relations only: no dual locator, acquisition gate or text-equivalence claim is allowed. Part 6 findings are profile-limited; Part 7 profile RL/SCS/ICS/PICS semantics cannot be generalized without evidence.

## Generalization rights

Conformance-method concepts may enter `Extension`; protocol/profile declarations remain `Profile`; laboratory/client procedures remain `Practice`; only cross-domain independently reviewed abstractions may be proposed for `Generic`.

## Synthesis handoff dataset

Emit the common record plus `part`, `PICS_ICS_PIXIT_IXIT_role`, `test_purpose`, `ATS_ETS_relation`, `expected_observed_verdict_claim`, `profile_predicate` and `lifecycle_assurance_limit`.

## Detailed execution specification

### Execution outcome and boundary

This is a clause study of the closed ISO/IEC 9646 population comprising Parts 1, 2, 4, 5, 6 and 7. Only those acquired and fingerprinted ISO texts may support conclusions. ITU-T identifiers may be recorded as bibliographic relationships but are not evidence locators.

### Phase A — canonical series register

Reconfirm a part-level register with canonical identifier, title, edition/date, status, relevance and decision. Record Parts 1/2/4/5/6/7 as `include`, Part 3 as `exclude — notation/execution technology`, and the related ITU number only as a bibliographic relation.

Do not treat ETSI TTCN-3, a vendor tutorial, a catalogue abstract or a later tool language as the normative methodology source. If any included ISO text fails identity/completeness control, update the blocker and stop before clause conclusions.

Part 3 is explicitly excluded as test notation/execution technology. Part 7 is mandatory and shall cover Implementation Conformance Statements, PICS proforma, profile Requirements Lists, support/status/predicate semantics, capability/applicability declarations and conformance-claim scope.

### Phase B — source control

For each included source record local path, canonical title, edition/date, page count, SHA-256, completeness, language and official status. Inspect normative references and annex status. Licensed texts remain outside Git. Do not infer ISO/ITU textual equivalence; the ISO set is the sole clause basis.

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

The Part 1 scope statement excluding certification from ISO/IEC 9646 shall be a mandatory row in the claim-boundary table. Part 6 is a protocol-profile specialization and shall not be promoted directly into Generic Core; any abstraction must pass the profile-to-generic ladder and independent review.

### Evidence extraction template

Each used proposition shall record exact part and clause/table/annex locator, PDF page, source class/modality, faithful paraphrase, native objects/relations, applicability conditions, framework implication, ISO-G04 relevance and confidence. Follow `source → interpretation → VAF implication → proposal`; expected outcome or verdict language must not silently become an `Oracle` entity.

### Required mappings and tests

Produce:

- a series/part relationship register;
- `Basis → applicability/capability declaration (PICS/ICS, PIXIT/IXIT) → Test Purpose/Verification Obligation candidate → ATS/ETS → Expected/Observed outcome → Verdict → Report/Conformance Claim`, with each arrow classified as source-direct, interpreted or framework-defined;
- `native concept → VAF Case/Procedure/Expected Result/Observed Result/Verdict/Oracle candidate` crosswalk;
- `methodology → notation → executable test system` boundary matrix;
- an Oracle hypothesis test addressing correctness, configuration, provenance, authority and failure modes;
- a claim-boundary table distinguishing test verdict, implementation conformance statement, conformance claim, certification and authority decision.

For each Oracle attribute proposed by VAF, mark `direct support`, `indirect support`, `contradicted`, `absent` or `not applicable`, with locators and limitations.

### Repository deliverables

Create `../standard_notes/iso_iec_9646_series_clause_study.md`; update ISO-G04 and only genuinely affected gaps; update `../standards_map.md` and `../consolidation/architecture_impact_register.md`; update HANDOFF and CHANGELOG states; create an independent-review packet listing population reconciliation, Part 3/ITU exclusions, changed files and Oracle disposition.

### Required disposition

The final report must choose and justify one of: `Oracle unsupported`, `Oracle partially supported as a framework abstraction`, `Oracle requires modification/split`, or `DEFERRED`. It must also identify whether conformance-testing concepts are generic methodological candidates or a protocol-testing profile. The claim-boundary conclusion shall state explicitly that ISO/IEC 9646 excludes certification from scope. Any `EXTEND/MODIFY/SPLIT/MERGE` disposition requires migration notes.

### No-overclaim rules

Do not state that a passed test proves total product conformance, certification or assurance sufficiency. Do not equate expected result, verdict mechanism and oracle validity. Do not generalize a protocol test architecture to every verification context. Do not claim current equivalence between historical ISO parts and ITU Recommendations without controlled evidence.

### Mandatory execution sequence and report structure

Execute in this order: snapshot state; reconfirm the controlled register/exclusions and source fingerprints; inventory all included clauses; extract terminology and test architecture; build capability/test-purpose/verdict/oracle/claim mappings; apply bounded repository changes; run consistency checks; create review packet; stop at review.

The study note shall contain: control record; controlled population/exclusion register; fingerprint table; clause inventories by part; PICS/ICS and PIXIT/IXIT; Part 7 SCS/ICS/profile-RL semantics; terminology; test architecture; test specification/realization chain; outcome/verdict model; Oracle hypothesis test; conformance-claim boundary; methodology/notation/technology boundary; gap and architecture dispositions; limitations; repository delta; conclusions and review handoff.

The review packet shall reconcile every selected/excluded part, every primary clause and each Oracle attribute; list changed files and statuses; and include copyright, link and overclaim checks. Metadata-only blocked work must use the same packet to show that no clause conclusion was introduced.

### Definition of done

Done requires the controlled Parts 1/2/4/5/6/7 register; the recorded Part 3/ITU exclusion decision; complete Part 7 capability/claim/profile coverage; clause inventories with exclusions; the Part 1 certification-exclusion check; a profile-limited Part 6 disposition; all mappings/tests above; locator-backed conclusions; synchronized repository statuses; successful Markdown/link/diff checks; and independent review. Part 3 or ITU acquisition is not part of DoD.
