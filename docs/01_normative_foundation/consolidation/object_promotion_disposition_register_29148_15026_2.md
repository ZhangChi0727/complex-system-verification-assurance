---
title: Object Promotion and Disposition Register — ISO 29148 / ISO 15026-2
status: reviewed
version: 0.2
baseline: post-v0.2-candidate
owner: research
last_updated: 2026-08-19
dependencies:
  - requirements_to_assurance_crosswalk.md
---

# Object Promotion and Disposition Register

## 1. Decision rules

Promotion requires a stable semantic identity, an explicit source locator, compatibility with the five-source ontology, and a clear generic/profile boundary. Promotion here is conceptual only; it does not freeze database fields, cardinalities, state machines or tooling. Authoritative dispositions use: `source-native adopted`, `framework-defined, source-supported`, `candidate extension point`, `partially supported`, `dependency open`, or `rejected/deferred`.

Section 2 records the evidence summary. Section 3 records this research round's independently reviewed dispositions and uses only the task-controlled vocabulary: `KEEP AS GENERIC CORE`, `PROMOTE TO GENERIC CORE`, `KEEP AS EXTENSION POINT`, `DEMOTE TO PROFILE/PROJECT`, `SPLIT`, `MERGE`, `RENAME`, `REFERENCE ONLY`, `KEEP OPEN`, `REMOVE`. The authoritative cross-round provenance register remains §28 of `five_source_consistency_gap_review.md`; review accepts these as a post-v0.2 conceptual research delta, not an executable schema or v0.2 tag change. In the final column, the former independent-review gate is now satisfied; schema and dependency gates remain open exactly as stated.

## 2. Register

| ID | Candidate | Layer | Disposition | Basis | Required boundary |
|---|---|---|---|---|---|
| OP-01 | Requirement | Generic Core | RETAIN + STRENGTHEN | 29148, 5.2.4–5.2.7 | Verifiable is not verified |
| OP-02 | Requirement Set | Generic Core aggregate/view | PROMOTE | 29148, 5.2.6 | Set-quality assessment differs from implementation coverage |
| OP-03 | Requirement Condition | Generic typed qualifier | PROMOTE AS ROLE | 29148, 5.2.4 | Not always a standalone basis object |
| OP-04 | Applicable Constraint | Generic Core basis role | RETAIN + REFINE | 29148, 5.2.4/5.2.8 | Can be global, linked or standalone; representation remains contextual |
| OP-05 | Specified Characteristic | Generic Core basis role | RETAIN | 29148, 6.5.2.1 + ISO 15288 baseline | Universal schema remains open |
| OP-06 | Verification Basis Element | Framework abstraction | RETAIN | Cross-source consistency | Typed union/role, not source-native class |
| OP-07 | Verification Obligation | Framework-defined Generic Core | RETAIN + STRENGTHEN | 29148, 6.5.2.2 and existing baseline | Formation/grouping/cardinality remain project/model concerns |
| OP-08 | Requirement quality assessment | Generic activity/result role | PROMOTE | 29148, 5.2.5–5.2.6 | Separate individual vs set evaluation |
| OP-09 | BRS/StRS/SyRS/SRS | Generic information-item/view types | PROMOTE CONCEPTUALLY | 29148, Clauses 7–9 | Not necessarily physical documents; 15289 alignment open |
| OP-10 | Requirement attribute universal field set | Executable schema | REJECT AS UNIVERSAL | 29148, 5.2.8 uses recommendations/examples | Profile/project selection required |
| OP-11 | RTM/VCRM | Representation option | RETAIN AS EXAMPLE | 29148, 6.5.2 | No mandatory spreadsheet/matrix ontology |
| OP-12 | Assurance Case | Generic Core aggregate | REFINE | 15026-2, 3.1.1/5.2 | Structure does not prove content quality |
| OP-13 | Supported Claim | Generic Core recursive node | PROMOTE | 15026-2, 5.3.5 | Distinct from bare Claim |
| OP-14 | Claim | Generic Core | RETAIN WITH DEPENDENCY | 15026-2, 5.3.3 structure/provenance; current vocabulary dependency is 15026-1:2025 | Full definition and targeted compatibility not frozen |
| OP-15 | Argument | Generic Core | REFINE | 15026-2, 5.3.5 | Preserve undeveloped vs inference/evidence-reference alternatives |
| OP-16 | Inference | Generic Core | PROMOTE | 15026-2, 3.1.4/5.3.4–5.3.5 | Explicit premises, conclusion and context |
| OP-17 | Context | Generic Core relation/value role | PROMOTE | 15026-2, 5.3.1 | Scoped definition/basic assumption/document reference |
| OP-18 | Evidence Item | Generic Core | REFINE | 15026-2, 5.3.2 | Artefact + applicability + uncertainty + assumptions |
| OP-19 | Basic Assumption | Assurance-case context subtype | PROMOTE AS SUBTYPE/ROLE | 15026-2, 3.1.3/5.3.1 | Does not replace generic Assumption extension point |
| OP-20 | Undeveloped Argument | Generic structural type/state | PROMOTE | 15026-2, 3.1.7/5.3.5 | Signals incomplete structure, not false claim |
| OP-21 | Narrative Introduction | Generic information-item/view | PROMOTE | 15026-2, 5.3.6 | Not identical to whole Assurance Case |
| OP-22 | Assurance Case Report | Generic report/index view | PROMOTE CONCEPTUALLY | 15026-2, 3.1.2/5.2(c) | Separate publication may be unnecessary; report field semantics remain |
| OP-23 | Framework characterization / later Argument use | Framework assessment plus source-native later relation | partially supported | Framework relation constrained by 15026-2, 5.3.2; direct usage structure in 5.3.5 | Four-field record constrains characterization; the standard does not define an admission workflow; later reference establishes Claim-specific use; neither implies sufficiency |
| OP-24 | Universal sufficiency threshold | Generic rule | REJECT AS UNIVERSAL | 15026-2, 4.1 | Reader/profile/project decision |
| OP-25 | Assurance acceptance authority | Generic authority | KEEP OPEN | Not supplied by either source | Composite Gate authority remains contextual |
| OP-26 | 15289-compatible executable schema | Information architecture | dependency open | 15289 source acquired; clause study pending | Do not infer from current Markdown/YAML |

## 3. Review-candidate disposition of the mandatory object set

| Object | Current role | New finding | Final disposition | Source-native / basis | Abstraction rationale and prohibited interpretation | Impact / schema gate / review |
|---|---|---|---|---|---|---|
| Verification Basis | Generic aggregate/role | 29148 strengthens controlled requirement information and specified-characteristic verification purpose | KEEP AS GENERIC CORE | Framework-defined; 29148, 5.2.4/6.5.2.1 plus ISO 15288 baseline | Basis may compose typed elements; not Requirement-only | Info model; schema OPEN; independent review required |
| Verification Basis Element | Typed basis role | Conditions/constraints need representation care | KEEP AS GENERIC CORE | Framework-defined; 29148, 5.2.4/6.5.2.1 | Requirement/SpecifiedCharacteristic/ApplicableConstraint; do not add Need/Assumption automatically | Info model; schema OPEN; review required |
| Verification Obligation | Generic Core | Method/action/criteria relation strengthened; cardinality absent | KEEP AS GENERIC CORE | Framework-defined; 29148, 6.5.2.2 | Do not attribute class to ISO or force Requirement 1:1 | V1/V3/V4; schema OPEN; review required |
| Requirement | Generic Core basis object | Normative construct/quality and information content clarified | KEEP AS GENERIC CORE | Source-native; 29148, 5.2.4–5.2.7 | Verifiable ≠ verified; Requirement ≠ Claim | Terminology/info model; schema OPEN; review required |
| Specified Characteristic | Generic Core basis role | 29148 repeats verification purpose but gives no universal schema | KEEP AS GENERIC CORE | Source-native phrase/Framework role; 29148, 6.5.2.1 | Do not force characteristic into Requirement merely for tooling | Info model; schema OPEN; review required |
| Applicable Constraint | Generic Core basis role | Constraint can be qualifier, relation, global restriction or standalone requirement | SPLIT | Source-native concept + framework role; 29148, 5.2.4 | Separate constraint content/relationship from independently controlled basis use | Terminology/info model; schema OPEN; review required |
| Assumption | Generic Extension Point | Requirement assumptions documented/validated; context/evidence assumptions explicit | KEEP AS EXTENSION POINT | Source-native across 29148, 5.2.7/9.5.19 and 15026-2, 5.3.1–5.3.2 | No universal owner/status/state/cardinality; not a direct obligation shortcut | Terminology/change/evidence; schema OPEN; review required |
| Verification Criterion | Candidate generic relation/object | Explicitly associated with verification actions | PROMOTE TO GENERIC CORE | Source-native concept; 29148, 6.5.2.2 | Success criterion is not an independent Oracle unless later justified | V3/V5/V8; conceptual only; review required |
| Verification Method | Generic Core strategy element | Requirement-method association strengthened | KEEP AS GENERIC CORE | Source-native; 29148, 6.5.2.2 | Method taxonomy examples are not universally exhaustive | V3; schema OPEN; review required |
| Verification Result | Generic Core | Result/objective information remains upstream of framework-defined Evidence Item characterization | KEEP AS GENERIC CORE | Cross-source; 29148, 6.5.2.2–6.5.2.3 | Result ≠ Evidence Item ≠ Claim | V7/V8/evidence; schema OPEN; normative review complete |
| Evidence | Generic Core role | 15026-2 provides precise `Evidence Item`; generic evidence wording remains broader | SPLIT | Cross-source concept | Separate candidate artefact/result, Evidence Item and evidence role; do not equate inventory with support | Evidence workspace; schema OPEN; review required |
| Evidence Artefact | Generic Core artefact role | 15026-2 artefact is one Evidence Item field | RENAME | Framework-defined → `Candidate Evidence Artefact` where not yet admitted; 15026-2, 5.3.2(a) | Artefact existence ≠ Evidence Item | Evidence workspace; schema OPEN; review required |
| Evidence Item | Not fully distinguished | Four-part source-native record found; independent management allowed | source-native adopted | Source-native record; 15026-2, 5.3.2 | Framework characterization constrained by the record may establish an Evidence Item; existence/reference are separate and existence ≠ claim support | Info/evidence model; workflow/schema BLOCKED by 15289/15026-1:2025; reviewed with dependencies open |
| Provenance | Generic Core relation | Complements but is not a substitute for 15026-2 applicability/uncertainty | KEEP AS GENERIC CORE | Framework abstraction with five-source support | Provenance ≠ Context ≠ Argument | Info/evidence; schema OPEN; review required |
| Traceability | Generic Core relation | 29148 strengthens bidirectional lifecycle trace; 15026-2 requires reasoning structure beyond trace | KEEP AS GENERIC CORE | Source-native relation; 29148, 6.5.2.3 | Trace link ≠ Inference/Argument | Info model; schema OPEN; review required |
| Claim | Generic Core | 15026-2 structure uses a dated locator; current vocabulary depends on 15026-1:2025 | KEEP OPEN | Source-native 15026-2, 5.3.3 provenance + framework adoption of current 2025 vocabulary; targeted compatibility open | Do not freeze full semantics from examples, mechanically replace the dated locator, or presume equivalence | Terminology; schema BLOCKED; review required |
| Compliance Claim | Generic Core candidate | No direct equivalence to 15026-2 Claim or authority acceptance | KEEP AS EXTENSION POINT | Framework/domain term; 15026-2 gives generic claim structure only | Do not imply regulatory acceptance | Closure/profile; schema OPEN; review required |
| Assurance Claim | Generic Core candidate | Generic Claim in assurance-case context; current vocabulary dependency remains | KEEP OPEN | Candidate specialization/typing of `Claim`; decision blocked by 15026-1:2025 study and targeted compatibility review | Do not merge or duplicate classes before the normative vocabulary dependency is resolved | Terminology; schema BLOCKED; review required |
| Supported Claim | Previously implicit | Recursive Claim+Argument+Contexts structure is direct | PROMOTE TO GENERIC CORE | Source-native; 15026-2, 5.3.5 | Supported Claim ≠ bare Claim or status field | Info/evidence model; schema OPEN; review required |
| Inference | Previously implicit/research proposal | Explicit reasoning step with premises/conclusion | PROMOTE TO GENERIC CORE | Source-native; 15026-2, 3.1.4/5.3.4–5.3.5 | Inference ≠ trace, approval or automated result | Argument model; schema OPEN; review required |
| Argument | Generic Core | Recursive alternatives now precise | KEEP AS GENERIC CORE | Source-native; 15026-2, 5.3.5 | Preserve undeveloped/inference/evidence-reference alternatives | Argument model; schema OPEN; review required |
| Context | Previously distributed | Explicit scoped list role | PROMOTE TO GENERIC CORE | Source-native; 15026-2, 5.3.1 | Context ≠ Provenance/Evidence/full Assumption record | Info/argument model; schema OPEN; review required |
| Sufficiency Assessment | Generic Extension Point | 15026-2 clarifies uncertainty/relevance inputs and leaves sufficiency to readers | KEEP AS EXTENSION POINT | Framework-defined; 15026-2, 4.1 | No universal threshold, algorithm or authority | V11; schema/rules OPEN; review required |
| Objective Satisfaction | Candidate conclusion/state | Can be represented as a Claim plus separate assessment/decision state | SPLIT | Framework-defined; constrained by 15026-2, 5.3.5 | Claim of satisfaction ≠ decision that closure is authorized | V8/V11/V12; schema OPEN; review required |
| Composite Gate | Framework-defined Generic Core | Assurance case/report can inform it; authority remains outside argument | KEEP AS GENERIC CORE | Framework-defined; five-source basis + 15026-2, 4.1 | Gate ≠ Argument/Supported Claim; structure ≠ acceptance | Closure; schema OPEN; review required |
| Verification Closure | Framework Composite Gate/state concern | Top-level supported claim is input, not closure itself | KEEP AS EXTENSION POINT | Framework-defined; no direct source-native closure process | Do not infer closure from complete case or passed claim structure | V12; authority/state OPEN; review required |

`Verification Criterion` promotion is conceptual: it is a stable relation-bearing concept needed between obligation/action/result. Whether it is an entity, value object or controlled relation remains part of ISO-G07B/REQ-G02 and cannot be fixed by this decision.

### 3.1 Authoritative allowed-state dispositions

This table is the controlling disposition for the mandatory set; earlier `KEEP/PROMOTE/REFINE` wording records integration actions only.

| Object | Disposition | Boundary |
|---|---|---|
| Requirement | source-native adopted | Generic basis role; full schema/cardinality open |
| Requirement Set | source-native adopted | Conceptual aggregate/view; lifecycle identity open |
| Verification Criterion | source-native adopted | Relation-bearing concept; entity/value/relation decision open |
| Evidence Item | source-native adopted | Four-field record is source-native; characterization/admission relation is framework-defined; later Argument use separate |
| Supported Claim | source-native adopted | Recursive assurance-case node; clause study reviewed |
| Inference | source-native adopted | Validity/quality assessment remains open |
| Context | source-native adopted | Scoped role; not Provenance/Evidence |
| Undeveloped Argument | source-native adopted | Structural incompleteness only |
| Narrative Introduction | source-native adopted | Report/index view; physical realization open |
| Assurance Case aggregate | source-native adopted | Structure source-supported; quality/sufficiency/acceptance not implied |
| Verification Obligation | framework-defined, source-supported | Not a 29148 native class; formation/cardinality open |
| Evidence characterization workflow | framework-defined, partially supported | 15026-2 supplies four-field record constraints, not the workflow; operational states, admission authority, responsibility and cardinality open |
| 15289-compatible executable schema | dependency open | Source acquired; clause study pending |

## 4. Baseline delta

The v0.2 conceptual chain changes from the shorthand:

```text
Evidence → Argument → Claim
```

to the more precise recursive structure:

```text
EvidenceItem ─referencedBy→ leaf Argument ─supports→ Claim
SupportedClaim := Claim + Argument + Context
Inference(premise SupportedClaims) ─derives→ conclusion Claim
```

This is a semantic refinement, not a reversal of the five-source consolidation. Verification Obligation, Composite Gate, Coverage/Sufficiency split, aviation profile boundaries and the V0–V12 ontology remain intact.
