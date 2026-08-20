---
title: ISO/IEC/IEEE 24748-8 Revision-Watch Task
status: planned
version: 0.2
baseline: post-v0.2
owner: research
last_updated: 2026-08-20
dependencies:
  - README.md
  - ../standards_baseline.md
---

# ISO/IEC/IEEE 24748-8 Revision-Watch Task

## Control record

| Field | Value |
|---|---|
| Order / priority | 17 / revision watch, not current clause study |
| Baseline status | `METADATA VERIFIED; FORMAL REVISION WATCH; CLAUSE STUDY DEFERRED` |
| Source | No matching PDF in current inventory; 2019 remains the published edition, while the replacement FDIS is not a normative basis |
| Layer / trigger | Domain assurance/application profile / defence review and audit abstraction |
| Initial impact | `DEFERRED — await published replacement and source decision` |

## Objective

Maintain an accurate publication/replacement watch and define the gate for a future defence-domain review/audit abstraction study.

## Required actions

1. Periodically verify the official publication state without studying the FDIS text.
2. When a replacement is formally published, update metadata and decide whether to acquire it.
3. If acquired and triggered, create a new clause-study task focused on LC-G01/LC-G02 and cross-domain abstraction.
4. Preserve `Domain assurance/application profile`; no direct Generic Core promotion is allowed.

## Stop conditions

Do not acquire or analyze the FDIS for normative conclusions, generalize defence authority/gate rules, or start clause extraction under this watch task.

## Detailed execution specification

### Nature of this task

This document is a publication-control runbook, not a clause-research authorization. Its purpose is to prevent a draft replacement or a defence-domain profile from silently becoming a Generic Core basis.

### Authoritative watch procedure

At each scheduled or research-triggered check:

1. consult official ISO/IEC/IEEE catalogue records and record access date and stable URL/reference;
2. capture published identifier, title, edition/date, lifecycle status and any replacement/withdrawal relation;
3. distinguish FDIS approval/publication workflow from an actually published standard;
4. compare official metadata with `../standards_baseline.md` and this control record;
5. record `NO CHANGE`, `PUBLISHED REPLACEMENT AVAILABLE`, `STATUS AMBIGUOUS` or `WATCH CLOSED`;
6. do not download, quote or interpret draft text as normative evidence.

### Trigger to create a clause-study task

A new task may be created only when the replacement is formally published, canonical metadata is stable, the source-acquisition decision is approved and the research trigger remains relevant. The new task must receive a new current-sequence identifier/version; this watch document is not converted in place into a clause study.

### Scope of the future research brief

The future task shall focus on review/audit terminology, purpose and participants; lifecycle/project decision points; entry/exit and evidence inputs; authority and independence; findings/actions/waivers/reopening; information items and records; tailoring; and defence-specific context. It must compare those concepts with LC-G01/LC-G02, Composite Gate and generic assessment/review/decision/event separation.

### Required repository updates per watch event

Update the standards baseline watch date/status, add a concise CHANGELOG entry only for a material publication-state change, update HANDOFF if the queue changes, and create an Architecture Impact entry only after clause study—not from metadata. Retain evidence of the catalogue check as paraphrased metadata/link, not copyrighted draft content.

### No-overclaim rules

Do not state that an FDIS is the published normative basis, that defence gates are generic assurance gates, or that publication metadata supports clause conclusions. Do not use the watch event to close LC-G01/LC-G02 or change V0–V12.

### Definition of done for a watch cycle

A cycle is complete when official metadata, access date and disposition are recorded consistently, no draft-derived claim was introduced, links/status terms pass checks, and any published-replacement event has a separate acquisition/task decision. The overall watch remains `planned` until formally closed or replaced.
