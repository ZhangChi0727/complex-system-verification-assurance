---
title: PR #13 Research Task Specification v0.6 Review Handoff
status: correction-rereview
version: 0.2
baseline: post-v0.2
owner: research
last_updated: 2026-08-24
review_type: pull-request-review
review_target: Tasks 001-022 research-task specification redesign
dependencies:
  - ../research_tasks/README.md
  - ../../00_overview/research_questions.md
  - ../../00_overview/innovation_statement.md
  - ../../00_overview/research_scope.md
---

# PR #13 Research Task Specification v0.6 Review Handoff

## Review objective

Verify that Tasks 001-022 are sufficiently self-contained and source-specific to guide a new agent from a controlled standard source to a detailed, reviewable research record and bounded repository update.

This review concerns research-task design. It does not review or promote any new standard conclusion.

## External review correction at `e090f3045edabdc816ef7ae230c5a1f2704f2fd7`

The first complete external review returned `REQUEST CHANGES` with five blocking precision findings. This correction keeps PR #13 Draft and changes no standard-study result, gap disposition, standards baseline or Architecture Impact entry.

| Finding | Corrected scope | Disposition |
|---|---|---|
| F-01 | Task 006 current 29119-1:2022 chain and Tasks 006–009 collision sweep | `CORRECTED; LIGHTWEIGHT REREVIEW PENDING` — current chain is `test basis → test model → test coverage items → test cases → test procedures`; `test condition` is edition-transition/collision metadata only, including the bounded 3.111 Note 3 observation |
| F-02 | Tasks 017/021/022 task-type semantics | `CORRECTED; LIGHTWEIGHT REREVIEW PENDING` — dedicated metadata-watch, mapping-closure and reviewed-input synthesis orientation, population gate, hypothesis reconciliation and record subtype |
| F-03 | Task 004 15026-4:2021 population | `CORRECTED; LIGHTWEIGHT REREVIEW PENDING` — controlled source has Clauses 1–7, Bibliography and IEEE notices; `No annex population in the controlled 2021 source` |
| F-04 | README, Tasks 001–021 and Task 022 validator | `CORRECTED; LIGHTWEIGHT REREVIEW PENDING` — one authoritative common schema separates `source_class`, `source_kind` and `modality`, retains applicability/hypothesis/destination/closure fields, and excludes specialized metadata/synthesis records |
| F-05 | Task 018 and README RQ coverage | `CORRECTED; LIGHTWEIGHT REREVIEW PENDING` — RQ6 now has the independent ISO/IEC/IEEE 24641:2023 Clause 6.5 knowledge-reuse/pattern family alongside Task 009 |

The requested next action is a correction-diff-only rereview. The PR must remain Draft until that disposition is recorded.

## Change population

- Tasks 001-016 and 018-020: complete clause-study specifications;
- Task 002: controlled multi-part ISO/IEC 9646 population;
- Task 017: metadata/revision-watch specification only;
- Task 021: bounded mapping-closure specification;
- Task 022: reviewed-dataset synthesis and innovation-falsification specification;
- research-task register, HANDOFF state and CHANGELOG.

No task filename was changed. Frontmatter and H1 titles now follow the standard identifier plus `Normative Research Task Specification`, except the controlled Task 017 and Task 022 special forms.

## Source-reference method

Each source task was checked against the corresponding local controlled PDF before its source-specific research entry and preliminary hypotheses were written. The check covered source presence, page count, SHA-256, title/edition context, table of contents, scope/conformance structure, terms, main clause families and annex force where applicable.

The source PDFs remain local and are not part of the PR. Task control records remain the authoritative source-fingerprint register.

Task 017 has no matching published source PDF and therefore remains metadata-only. Task 022 interprets no new standard text.

## Common v0.6 contract

Every task now includes:

1. the three overview research anchors;
2. expanded RQ responsibility rather than ID-only references;
3. expanded innovation-candidate statement, falsification condition and non-claim;
4. target-source-specific research entry;
5. controlled evidence hierarchy;
6. `Standard wins over current framework hypothesis`;
7. falsifiable preliminary mapping hypotheses;
8. post-inventory hypothesis extension and reconciliation;
9. the README authoritative clause/mapping evidence-record schema or the task-type-specific metadata/synthesis subtype;
10. a durable downstream-note interface;
11. source-review and independent-review separation;
12. copyright/privacy and whole-repository consistency gates.

## Practice-comparison boundary

Task 001 uses direct, bounded hypothesis prompts from the INCOSE Systems Engineering Handbook 4e and NASA/SP-2016-6105 Rev2 originals. It does not depend on the pending-review handbook notes.

These prompts:

- do not create ISO/IEC/IEEE 15289 clause records;
- do not close gaps;
- do not determine Architecture Impact;
- do not enter the Task 022 normative clause dataset;
- do not count as source votes;
- are self-contained, so the Task 001 executing agent does not require the handbooks.

## Protected invariants

The PR shall not:

- start or complete a clause study;
- modify established normative basis or protected gap dispositions;
- promote any Architecture Impact result;
- freeze V0-V12, schema, metamodel, state machine or automation interface;
- establish novelty;
- commit licensed PDFs, screenshots, OCR or substantial source text;
- convert Task 017 metadata into clause evidence;
- allow Task 022 to interpret new standards.

## Validation performed

- 22/22 task files use `version: 0.6`;
- 22/22 contain one Research orientation;
- 22/22 contain one Preliminary mapping hypotheses section;
- 19 clause-study tasks use the authoritative common clause/mapping schema; Task 021 uses the same fields/enums as `mapping-evidence`; Tasks 017/022 use explicit `metadata-watch` and `synthesis-disposition` subtypes;
- README, 19 clause-study tasks, Task 021 and Task 022 validator agree on all 18 common field names/enums;
- Tasks 017/021/022 clause-template leakage scans passed;
- Tasks 006–009 current-chain/collision scan passed; Task 004 no-annex audit and Task 018 Clause 6.5/RQ6 propagation passed;
- title/frontmatter/H1 agreement passed;
- three-anchor dependency checks passed;
- minimum hypothesis-population checks passed;
- relative-link checks passed;
- `git diff --check` passed;
- copyright/privacy/stale-title/status scans passed;
- no PDF or temporary extraction artifact is included.

## Reviewer checklist

### Structure and executability

- [ ] A new agent can understand each task without unrecorded chat context.
- [ ] Each source task clearly identifies its controlled source population and exclusions.
- [ ] Research packages are specific to the target source rather than copied mechanically.
- [ ] Task 017 and Task 022 preserve their special non-clause-study boundaries.

### Research orientation

- [ ] RQ statements match the controlled research questions.
- [ ] Innovation statements, falsification conditions and non-claims match the controlled candidate register.
- [ ] Standard evidence, interpretation, framework implication and proposal remain separate.
- [ ] Standards silence cannot be read as novelty evidence.

### Hypotheses and evidence

- [ ] Preliminary hypotheses are falsifiable and do not predetermine results.
- [ ] Every hypothesis has an explicit prohibited inference.
- [ ] The post-inventory extension/reconciliation rule is executable.
- [ ] The common record supports Task 022 without requiring narrative reconstruction.

### Governance and copyright

- [ ] Practice-comparison material remains non-normative.
- [ ] Historical and current version dependencies are preserved.
- [ ] Architecture Impact and downstream closure ownership remain gated.
- [ ] No protected standard text or licence-specific identity is present.

## Requested disposition

Use one of:

- `APPROVED FOR MERGE`;
- `APPROVED WITH NON-BLOCKING FOLLOW-UP`;
- `REQUEST CHANGES`.

If requesting changes, identify the task ID, exact section, finding class and acceptance criterion. Content review should focus on whether the task can reliably drive future source research, not on performing the future source study inside PR #13.
