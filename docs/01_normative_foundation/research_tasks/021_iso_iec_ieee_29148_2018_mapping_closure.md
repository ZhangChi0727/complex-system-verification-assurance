---
title: ISO/IEC/IEEE 29148:2018 to 15288:2023 Mapping Closure Task
status: planned
version: 0.4
baseline: post-v0.2
owner: research
last_updated: 2026-08-21
task_type: mapping-closure
research_questions: [RQ1, RQ3, RQ7]
innovation_candidates: [INN-T2, INN-I1]
contribution_modes: [support, qualify, falsify, no-evidence]
source_population: bounded-dependencies
dependencies:
  - README.md
  - ../standard_notes/iso_iec_ieee_29148_2018_clause_study.md
  - ../reviews/iso_29148_15026_2_independent_review_packet.md
  - ../standard_notes/iso_15288.md
downstream_closure:
  - "Task 021: targeted mapping closure after execution-time revision/priority recheck"
  - "Architecture synthesis: requirements-engineering dependency disposition"
---

# ISO/IEC/IEEE 29148:2018 to 15288:2023 Mapping Closure Task

## Control record

| Field | Value |
|---|---|
| Order / priority | 21 / targeted residual dependency |
| Baseline status | `CLAUSE STUDY REVIEWED; 15288:2015→2023 VERSION MAPPING OPEN; FORMAL REVISION WATCH` |
| Source | `references/PDF/29148-2018.pdf`; 104 pages; SHA-256 `E8FB679F758AA078B290FB1849E288996D059968D5911ABD0E96A75C0539E6C8` |
| Revision control | Current published basis: 2018; Edition 3 DIS under development; official metadata last verified `2026-08-20` at https://www.iso.org/standard/94091.html; recheck before execution; DIS text prohibited; a published replacement requires an explicit retarget/priority decision |
| Layer / trigger | Generic methodological source / requirement-process dependency closure |
| Initial impact | `DEFERRED — targeted mapping review pending`; existing clause study remains reviewed |

## Objective

Close only the controlled 15288:2015→2023 dependency mapping used by the reviewed 29148 study, without reopening or repeating the full requirements-engineering clause study.

## Required questions

- Which cited 15288:2015 process/term locators have direct, moved, changed or absent counterparts in 15288:2023?
- Do any changes affect Requirement/Set, Verification Basis, Verification Criterion or obligation relations already adopted?
- Which mappings require errata, qualification or residual open status?

## Required work and outputs

Create `../consolidation/iso_29148_2018_to_iso_15288_2023_targeted_mapping.md`; update only affected provenance statements; record `CONFIRM/MODIFY/NO-IMPACT/DEFERRED` with migration notes where needed; obtain independent review of the targeted mapping.

## Stop conditions

Do not rewrite source-native 2015 citations, redo the full 29148 study, close unrelated REQ/ISO gaps or silently change established semantics.

## Research contribution contract

This bounded mapping task answers RQ1/RQ3/RQ7 only for the reviewed 29148 study's actual 15288:2015 dependencies. It shall test the framework chain `Requirement/Set → Verification Basis → Specified Characteristic/Constraint → Verification Criterion → Verification Obligation` while separating standard-direct relations from framework synthesis.

## Candidate falsification tests

Test `INN-T2/I1` against every controlled historical/current locator pair. An equivalent chain or machine-readable model must be source-supported; same headings and inferred counterparts are not equivalence evidence.

## Negative findings and non-answers

Without the 15288:2015 source, every semantic mapping row remains `NOT DETERMINED` and the task cannot reach final DoD. Do not reopen the reviewed 29148 clause study or replace old locators.

## Generalization rights

Only reviewed mapping corrections may affect `Generic`; edition-specific provenance remains `Extension`; unresolved rows are `No adoption`.

## Synthesis handoff dataset

Emit the common record plus `repository_occurrence`, `2015_locator`, `2023_counterpart`, `relation`, `effect`, `framework_chain_role`, `direct_or_synthesized` and `review_disposition`.

## Detailed execution specification

### Execution outcome and strict scope

Produce a complete, independently reviewed mapping for every ISO/IEC/IEEE 15288:2015 dependency actually used by the existing 29148:2018 study. This is a provenance/compatibility closure task, not a second clause study of 29148 and not a full 15288 edition delta.

### Source and baseline gate

Reconfirm the 29148 source path, 104-page extent and SHA-256; confirm the reviewed 29148 study/review packet is unchanged; use the controlled ISO 15288:2023 source/study. Record the starting commit and enumerate every 2015 citation or semantic dependency in the 29148 study, maps, gap matrix, terminology and architecture artifacts.

Before execution, recheck the Edition 3 revision status and the queue priority. The controlled ISO/IEC/IEEE 15288:2015 text is a hard source gate: without it, enumerate the population but mark semantic mappings `NOT DETERMINED` and do not claim mapping completion. If a replacement has been formally published, stop and issue a retarget decision that determines whether this task still closes provenance for the reviewed 2018 study or whether a separate new-edition task takes precedence. Never use DIS text or silently transform this task into a new full clause study.

### Mapping population

The mapping population includes explicit clause/table/definition citations, inherited process names, paraphrased 2015 outcomes/tasks, terminology relations and any repository conclusion whose validity depends on 2015 semantics. Each occurrence receives a stable row identifier; no dependency may be silently excluded.

### Mapping record

| Field | Required content |
|---|---|
| Row ID | stable mapping identifier |
| Repository location | file/section or line anchor |
| 29148 locator | clause/page using or citing 15288:2015 |
| 2015 dependency | exact cited locator/concept as source-native provenance |
| 2023 counterpart | exact locator/concept or `none/not determined` |
| Relation | direct, moved/renamed, semantically changed, removed, split/merged, unclear |
| Effect | no impact, wording qualification, mapping correction, architecture impact |
| Action | exact file change or explicit no-change rationale |
| Confidence/review | evidence quality and reviewer disposition |

### Required analysis packages

Separately check terminology/definitions; requirements engineering processes/outcomes/tasks; stakeholder/system/software requirement information relations; traceability and verification/validation criteria; Requirement and Requirement Set identity/lifecycle conclusions; Verification Basis/Specified Characteristic/Constraint relations; Verification Criterion placement/cardinality; and all cross-standard/gap/architecture conclusions inherited from the reviewed 29148 work.

### Change discipline

Preserve every source-native 2015 locator where describing what 29148:2018 cites. Add a 2023 current-baseline mapping beside it. If semantics changed, update only the affected framework interpretation and provide a before/after/migration note. Unrelated improvements are out of scope and must be separately proposed.

### Repository deliverables

Create `../consolidation/iso_29148_2018_to_iso_15288_2023_targeted_mapping.md`; update affected provenance statements in the 29148 note, standards map, gap matrix and Architecture Impact Register; update baseline/HANDOFF/CHANGELOG; create an independent-review packet containing full population reconciliation and exact changed-file list.

### Required final answers

State whether each established Requirement/Set, Verification Basis and Verification Criterion conclusion is confirmed, qualified or modified; list unresolved mappings; state whether REQ-G01, REQ-G02 or ISO-G07C status changes; and confirm that no unrelated clause study was reopened.

### No-overclaim rules

Do not replace a historical citation with a 2023 locator, infer equivalence from identical headings, omit removed/split concepts, or claim the complete editions are equivalent. Do not change stable semantics without an Architecture Impact disposition and migration note.

### Mandatory execution sequence and report structure

Execute in this order: freeze the reviewed starting baseline; enumerate all 2015 dependencies; reconcile the population; map each row to 2023; classify effects; apply only row-authorized changes; run provenance/terminology sweeps; prepare independent review; stop without reopening unrelated research.

The mapping report shall contain: control record/source fingerprints; scope/exclusions; population-construction method; full dependency inventory; terminology mappings; process/outcome/task mappings; Requirement/Set findings; Verification Basis/Characteristic/Constraint findings; Verification Criterion findings; affected repository statements; gap/architecture dispositions and migrations; unresolved rows; exact delta; conclusions and handoff.

The review packet shall prove population completeness, sample every relation class, list all source-native citations protected, all modified semantics/files/statuses and all unresolved rows. Approval applies only to this targeted closure.

### Definition of done

Done requires an execution-time revision/priority decision; a reconciled 100% mapping population; exact 2015 and 2023 locators for every determinable row; explicit unresolved rows; all actions applied or justified; synchronized repository statuses; clean link/diff/provenance scans; and independent review approval. The existing 29148 study remains reviewed throughout unless a mapped change explicitly requires a controlled correction.
