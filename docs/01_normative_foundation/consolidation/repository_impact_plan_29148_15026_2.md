---
title: Repository Impact Plan — ISO 29148 / ISO 15026-2
status: reviewed
version: 0.1
baseline: post-v0.2-candidate
owner: research
last_updated: 2026-08-19
dependencies:
  - requirements_to_assurance_crosswalk.md
  - object_promotion_disposition_register_29148_15026_2.md
  - gap_migration_report_29148_15026_2.md
---

# Repository Impact Plan — ISO 29148 / ISO 15026-2

## 1. Change-control boundary

本轮只形成规范研究成果、基线索引和影响计划，不对 Phase 3–8 文件实施大规模重写，不冻结 executable schema，不修改模板使其看起来已经满足 ISO 15289/15026-1。

## 2. Planned downstream changes

### 2.1 Minimal changes applied in this research branch

| Target | Applied research-only update |
|---|---|
| `standards_baseline.md` | Verified editions/source roles and open dependencies |
| `standards_map.md` | Added post-v0.2 delta and five-column rows without rewriting the five-source snapshot |
| `normative_gap_matrix.md` | Split ISO-G07 and registered new requirement/assurance gaps |
| five-source consolidation report §28–§29 | Updated the authoritative provenance annex with review candidates and added a post-baseline research annex; prior methodology and frozen decisions remain intact |
| `docs/00_overview/roadmap.md` | Updated research sequence to ISO 15289 plus ISO 15026-1 dependency |

### 2.2 Deferred implementation impacts

| Target | Proposed change | Trigger / dependency | Timing |
|---|---|---|---|
| `docs/00_overview/terminology.md` | Add/refine Requirement Set, Supported Claim, Inference, Context, Evidence Item, Undeveloped Argument and Assurance Case Report; retain source/framework labels | Reviewed packet; 15289/15026-1 dependencies remain | Next controlled baseline PR |
| `docs/00_overview/research_questions.md` | Refine RQ-A–D around basis formation, framework characterization, recursive argument and closure boundary | Independent review accepted conceptual delta | Next controlled baseline PR |
| `docs/03_process_model/` | Add explicit V2 individual-vs-set requirement assessment; refine V8 result-to-evidence admission and V11 argument/sufficiency inputs | Crosswalk accepted | Later model update |
| `docs/04_information_model/README.md` | Replace linear evidence shorthand with recursive Supported Claim/Inference structure; add candidate item/view taxonomy | ISO 15289 + ISO 15026-1 research preferred before schema freeze | Deferred |
| `docs/05_coverage_and_evidence/README.md` | Separate Result/Artefact, framework-defined characterization, source-native Evidence Item/later Argument use, applicability and sufficiency | Crosswalk accepted | Later evidence-architecture update |
| `docs/06_change_and_reverification/` | Extend impact targets to context, assumptions, claims, arguments and evidence | 15026-2 lifecycle maintenance semantics | Later model update |
| `docs/07_closure/` | Use assurance case/report as decision input; preserve independent authority/decision/state | ISO-G06 remains open | Later closure update |
| `docs/08_validation/README.md` | Add tests for structural completeness vs claim truth, evidence applicability and inference reconstruction | Executable conceptual model exists | Deferred |
| `templates/verification_strategy_record.md` | Consider requirement-set, condition/constraint and method/criteria links | ISO 15289 mapping + template review | Deferred |
| Future assurance-case template | Provide main/evidence/report views and structure mapping without mandating a notation | ISO 15026-1 dependency resolved | Deferred |

## 3. Candidate information-model relations

The following relations are approved for conceptual prototyping, not schema freezing:

```text
Requirement ─memberOf→ RequirementSet
Requirement ─qualifiedBy→ Condition
VerificationBasisElement ─givesBasisTo→ VerificationObligation
VerificationObligation ─addressedBy→ VerificationAction
VerificationAction ─produces→ Result
Result/Artefact ─frameworkCharacterizedAs→ EvidenceItem
EvidenceItem ─applicableWithin→ Scope
EvidenceItem ─hasUncertainty→ UncertaintyDescription
EvidenceItem ─reliesOn→ Assumption
SupportedClaim ─hasClaim→ Claim
SupportedClaim ─supportedBy→ Argument
Argument ─uses→ Inference | EvidenceReference | UndevelopedArgument
Inference ─hasPremise→ SupportedClaim
Inference ─derives→ Claim
AssuranceCase ─hasMain→ SupportedClaim
AssuranceCase ─hasEvidenceField→ EvidenceItemSet
AssuranceCase ─hasReport→ NarrativeIntroduction
```

Cardinality, ownership, states, allowed cycles and identity syntax remain open.

## 4. Validation scenarios for later implementation

| Scenario | Expected rule |
|---|---|
| A Requirement is marked verifiable but has no implementation result | Requirement-quality result may pass; implementation verification remains open |
| One test addresses multiple requirements | Allowed if obligation coverage and criteria/result provenance remain reconstructable |
| A test report is linked directly to a top-level claim | Reject as sufficient structure unless a valid leaf argument/inference chain is represented |
| Framework characterization lacks applicability scope, uncertainty or assumptions | Candidate artefact has not yet satisfied the framework-defined interface constrained by the source-native Evidence Item record |
| Assurance case contains an undeveloped argument | Case is structurally incomplete; no automatic assertion that claim is false |
| Assurance case has no undeveloped argument | Structural completeness passes; truth, sufficiency and acceptance remain separate assessments |
| Context changes after a system modification | Trigger impact assessment of claims, arguments, assumptions and evidence applicability |
| A GSN diagram maps unambiguously to the abstract structure | Potentially acceptable; notation is not mandated by the baseline |

## 5. Exit criteria for implementation work

Broad information-model/template changes should wait until:

- independent review remains recorded as complete, with no reopened source/strength finding;
- ISO 15289 mapping is available or the project explicitly accepts the dependency gap;
- ISO 15026-1 terminology is studied or all dependent terms remain visibly provisional;
- field/cardinality choices are identified as framework decisions and tested against at least the scenarios above.
