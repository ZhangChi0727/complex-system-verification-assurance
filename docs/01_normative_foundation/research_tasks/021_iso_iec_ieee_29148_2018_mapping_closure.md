---
title: ISO/IEC/IEEE 29148:2018 to 15288:2023 Mapping Closure Task
status: planned
version: 0.2
baseline: post-v0.2
owner: research
last_updated: 2026-08-20
dependencies:
  - README.md
  - ../standard_notes/iso_iec_ieee_29148_2018_clause_study.md
  - ../reviews/iso_29148_15026_2_independent_review_packet.md
---

# ISO/IEC/IEEE 29148:2018 to 15288:2023 Mapping Closure Task

## Control record

| Field | Value |
|---|---|
| Order / priority | 21 / targeted residual dependency |
| Baseline status | `CLAUSE STUDY REVIEWED; 15288:2015→2023 VERSION MAPPING OPEN` |
| Source | `references/PDF/29148-2018.pdf`; 104 pages; SHA-256 `E8FB679F758AA078B290FB1849E288996D059968D5911ABD0E96A75C0539E6C8` |
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

## Detailed execution specification

### Execution outcome and strict scope

Produce a complete, independently reviewed mapping for every ISO/IEC/IEEE 15288:2015 dependency actually used by the existing 29148:2018 study. This is a provenance/compatibility closure task, not a second clause study of 29148 and not a full 15288 edition delta.

### Source and baseline gate

Reconfirm the 29148 source path, 104-page extent and SHA-256; confirm the reviewed 29148 study/review packet is unchanged; use the controlled ISO 15288:2023 source/study. Record the starting commit and enumerate every 2015 citation or semantic dependency in the 29148 study, maps, gap matrix, terminology and architecture artifacts.

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

Done requires a reconciled 100% mapping population; exact 2015 and 2023 locators for every determinable row; explicit unresolved rows; all actions applied or justified; synchronized repository statuses; clean link/diff/provenance scans; and independent review approval. The existing 29148 study remains reviewed throughout unless a mapped change explicitly requires a controlled correction.
