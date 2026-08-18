---
title: ISO/IEC/IEEE 29148:2018 Clause Study
status: research-complete
version: 0.1
baseline: post-v0.2-candidate
owner: research
last_updated: 2026-08-18
research_type: clause-level-normative-study
source_role: requirements-engineering-and-information-item-source
primary_layer_role: generic-methodological-source
source:
  standard: ISO/IEC/IEEE 29148:2018
  edition: second
  date: 2018-11
  source_type: licensed-local-source-not-committed
dependencies:
  - ../consolidation/five_source_consistency_gap_review.md
  - ../normative_gap_matrix.md
  - ../consolidation/clause_evidence_register_29148_15026_2.md
---

# ISO/IEC/IEEE 29148:2018 Clause Study

## 1. 研究目的与边界

本笔记研究 ISO/IEC/IEEE 29148:2018 如何约束需求构造、需求集合、需求属性、需求信息项以及需求与 verification 的连接。原 PDF 只用于本地研究，不纳入版本库；本文只保存条款定位、规范强度和自行撰写的摘要。

逐条款的完整 `Source / Clause / force / object / relation / applicability / conformance / classification / conclusion / non-claim / dependency / disposition` 记录见 [Clause Evidence Register](../consolidation/clause_evidence_register_29148_15026_2.md)。

本标准对本框架有三种不同强度的贡献：

- `NORMATIVE`：Clause 4 的 conformance 规则，5.2.4–5.2.7 的需求构造与质量要求，Clause 7、Clause 9 和 Annex A 的信息项/内容要求；
- `RECOMMENDED / GUIDANCE`：以 `should` 表述的需求属性、方法记录、规格结构与实践建议；
- `FRAMEWORK INTERPRETATION`：把需求及其条件、约束、验证方法和追踪关系映射为 Verification Basis、Obligation 和后续 evidence architecture。该映射不是标准原生 metamodel。

本标准引用 ISO/IEC/IEEE 15288:2015 与 ISO/IEC/IEEE 12207:2017 的过程条款。仓库当前 generic lifecycle baseline 是 ISO/IEC/IEEE 15288:2023。因此，本文接受 29148 自身的需求工程与信息项要求，但把所有跨版本 process-clause 等价关系标为 `VERSION-MAPPING OPEN`，不直接声称 2015 与 2023 条款逐字或逐任务等价。

## 2. Source integrity 与 conformance

| Item | Finding |
|---|---|
| Source identity | PDF title/metadata and title page identify ISO/IEC/IEEE 29148:2018, second edition, 2018-11 |
| Source handling | Licensed local source; not committed; no internal locator retained in repository |
| Full conformance | Clause 4.2 combines selected requirement-fundamental provisions, cited lifecycle processes, Clause 7 information items, and Clause 9/Annex A content |
| Process conformance | Clause 4.3 points to 6.1 and the referenced lifecycle-process provisions |
| Information-item conformance | Clause 4.4 requires the stated items and demonstration that their content requirements are met |
| Tailored conformance | Clause 4.5.2 requires declared tailoring under normative Annex C when full information-item conformance is not claimed |
| Repository implication | The framework may reuse concepts without claiming full or tailored conformance; any future conformance claim needs an explicit scope and evidence record |

Clause 4.4 also makes clear that a conforming information item need not be a standalone published document: repository content, split volumes, or combined information can conform if the required content remains available. This supports model/repository representation, but does not supply an executable schema.

## 3. Clause-level findings

### 3.1 Requirements fundamentals — 5.2.2–5.2.8

| Locator | Strength | Research finding | Framework consequence |
|---|---|---|---|
| 5.2.2 | Descriptive | Stakeholders include users/acquirers and can include developers, operators and regulatory authorities | Preserve stakeholder/source provenance; authority concern does not automatically create acceptance authority in the framework |
| 5.2.3 | Descriptive | Needs/goals/objectives are transformed into stakeholder requirements and recursively into lower-level requirements | `Need/Goal/Objective → Requirement` is a controlled transformation, not an identity relation |
| 5.2.4 | Normative + guidance | A well-formed requirement expresses a needed capability/property/constraint under conditions and must be verifiable; conditions and constraints are distinguished from the requirement statement | Requirement is a valid typed Verification Basis element; condition and constraint must retain their role and scope |
| 5.2.5 | Normative | Each requirement must be necessary, appropriate, unambiguous, complete, singular, feasible, verifiable, correct and conforming | V2 Requirement Verifiability Analysis gains a source-backed quality checklist; passing it does not prove implementation compliance |
| 5.2.6 | Normative | A requirements set must be complete, consistent, feasible, comprehensible and able to be validated | Individual-item and set-level assessments are distinct; set completeness is not verification coverage of an implementation |
| 5.2.7 | Mixed | Vague/non-verifiable language is prohibited; assumptions about a requirement must be documented and validated | Assumption has a requirements-context role; exact universal state/owner schema remains open |
| 5.2.8 | Recommended examples | Identification, version, owner, priority, risk, rationale, difficulty and type are candidate attributes | These are source-backed examples, not a mandatory universal field set; future schema must preserve modal strength |

Two semantic separations are mandatory for the framework:

1. `need/concern` is not yet a well-formed requirement;
2. `verifiable requirement` means its realization can be demonstrated, not that it has already been verified.

The standard describes conditions as measurable qualifiers and constraints as restrictions that may apply globally, to a requirement/set, or as standalone requirements. The v0.2 typed basis role remains valid, but should not flatten all conditions into independent `ApplicableConstraint` objects. A project must record whether a condition is part of a requirement, an attribute, or a separately controlled basis element.

### 3.1.1 Source-native ontology and attribute candidate register

“Object/attribute/relation” below describes the source's usage, not a frozen implementation shape. `Basis eligibility` indicates whether the concept can legitimately participate in controlled verification-basis formation; it does not mean an obligation is generated automatically.

| Concept | Source-native role and strength | Locator | Basis eligibility / disposition |
|---|---|---|---|
| Need / Stakeholder Need | Upstream concern/input transformed into requirements; descriptive | 5.2.3 | Not a direct basis by default; transform into a controlled Requirement or justify a project extension |
| Stakeholder Requirement | Requirement subtype/set at stakeholder perspective; normative quality rules apply | 5.2.3–5.2.6 | Eligible Requirement basis after applicability analysis |
| System Requirement | Requirement subtype/set for system/system element; normative quality rules apply | 5.2.3–5.2.6 | Eligible Requirement basis |
| Software Requirement | Requirement subtype/content represented in SRS; normative Clause 9 content | 5.4; 7; 9.6 | Eligible Requirement basis; software assurance rigor not defined here |
| Requirement | Statement translating a need with associated constraints/conditions; normative construct | 5.2.4 | Direct Generic Core basis candidate |
| Requirement Set | Collection evaluated by distinct normative characteristics | 5.2.6 | Aggregate/view; gives coverage context, not necessarily a single obligation |
| Constraint | Restriction; can apply across requirements, relate to one/set, or appear as standalone requirement | 5.2.4 | Eligible as `ApplicableConstraint` only when controlled and applicable |
| Condition | Measurable qualitative/quantitative qualifier | 5.2.4 | Normally qualifies a Requirement/criteria; standalone basis treatment is project/model decision |
| Assumption | Requirement-associated information that must be documented and validated; also SyRS/SRS content | 5.2.7; 9.5.19; 9.6.8 | Not a direct obligation shortcut; affects applicability/change and may drive a Requirement |
| Rationale | Recommended example attribute pointing to supporting analysis/evidence | 5.2.8.2 | Provenance/context, not Verification Basis by itself |
| Source/origin | Trace relation to motivating requirement/stakeholder/study; guidance | 6.4.3 ending; 6.5.2.3 | Provenance/traceability relation, not independent basis by itself |
| Identifier | Recommended requirement attribute; normative identifiers also appear in CM tasks | 5.2.8.2; 6.6.2.2 | Identity support; exact syntax not specified |
| Version/change information | Recommended version attribute plus configuration/change controls | 5.2.8.2; 6.6.2 | Basis configuration/provenance support |
| Owner | Recommended example attribute | 5.2.8.2 | Project schema candidate, not universal mandatory field |
| Priority | Recommended example attribute | 5.2.8.2 | Planning input; does not negate necessity |
| Criticality | Guidance concept for more rigorous analysis, not listed as universal attribute | 5.3.2 | Profile/project attribute or assurance constraint input |
| Risk | Recommended example attribute | 5.2.8.2 | Rigor/management input; not direct proof or obligation shortcut |
| Status | Not established as a universal requirement attribute in 5.2.8 | — | Framework/project candidate; `KEEP OPEN` |
| Verification Method | Method/technique associated with requirements/actions; guidance around referenced task | 6.5.2.2 | Strategy/action relation, not a Requirement attribute by default |
| Verification Criterion / success criterion | Associated with every verification action in referenced task; closure/success semantics described | 6.5.2.2 | Required conceptual relation to action/obligation; exact object/schema open |
| Verification Measure | Requirement measures and collected data are discussed; no single source-native `VerificationMeasure` class | 6.6.3 | Framework/project candidate; distinguish engineering measure from success criterion |
| Traceability Relation | Requirement-to-source and forward life-cycle relation; task/guidance | 6.5.2.3 and preceding requirements process text | Generic relation; not an Argument or Evidence |

Attribute strength classes:

| Class | Candidates |
|---|---|
| Source-required | Well-formed requirement content/quality; controlled configuration; Clause 9 required information content; method/criteria selection through cited verification task |
| Source-recommended | Identifier, version, owner, priority, risk, rationale, difficulty, type; method-definition detail; traceability practices |
| Source-example | Specific attribute value schemes, method documentation forms, RTM/VCRM representation and named measures |
| Framework-required candidate | Basis identity/scope/configuration, obligation relation, criteria and result provenance—requires later schema decision |
| Profile-specific | Criticality/rigor taxonomy, authority, independence and certification-oriented fields |
| Project-defined | Status vocabulary, ownership workflow, local priorities, tool identifiers and physical layout |

### 3.2 Iteration, recursion and information-item scope — 5.3–5.4

| Locator | Strength | Research finding | Framework consequence |
|---|---|---|---|
| 5.3.1 | Guidance | Requirements work is iterative at one system level and recursive across system levels | Trace links require level/scope; iteration and decomposition must not be inferred from identifier hierarchy alone |
| 5.3.2 | Guidance | Architecture/design can generate derived requirements; critical requirements deserve more rigorous analysis | `derivedFrom` must retain source decision/study/rationale; criticality can constrain rigor but does not itself prove sufficiency |
| 5.4 | Descriptive | BRS, StRS, SyRS and SRS represent different requirement sets and can have multiple recursive/iterative instances | Information-item type and requirement type are separate dimensions; a Requirement may be stored in a repository view rather than one file |

### 3.3 Requirements activities in verification — 6.5.2

| Locator | Strength/source | Research finding | Framework consequence |
|---|---|---|---|
| 6.5.2.1 | Purpose carried from referenced lifecycle standards | Verification obtains objective evidence that specified requirements and characteristics are fulfilled | Confirms that generic Verification Basis is broader than requirements alone; `SpecifiedCharacteristic` remains a legal basis role |
| 6.5.2.2 | Referenced task + 29148 guidance | An appropriate method/technique and criteria are selected for each verification action; method definition can address how, responsibility, event timing and venue/environment | Each obligation needs an addressed-by strategy/action relation and success criteria; example responsibility fields are not automatically universal mandatory fields |
| 6.5.2.2 | Guidance | Inspection, analysis/simulation, demonstration and test are the four described methods; similarity is discussed within analysis | Method taxonomy is useful guidance, not proof that these are the only methods in every profile |
| 6.5.2.2 | Guidance | A method links a requirement to activities that yield objective information and includes a closure approach | Supports `Requirement → Verification Obligation → Method/Action → Result`; it does not define the framework's Closure Decision ontology |
| 6.5.2.3 | Referenced task + guidance | Maintain traceability of verified elements; associate methods and information with requirements and extend links through life-cycle work products | Strengthens requirement-to-method/result traceability and unique identity; evidence provenance remains distinct from traceability |

The phrase “for every verification action” does not mean every Requirement must always map one-to-one to one Procedure. One requirement can require multiple actions; one action can address multiple compatible obligations. Cardinalities remain an information-model decision to validate later.

### 3.3.1 V2–V10 process-interface consequence

```text
V2  assess statement + individual quality + set quality
V3  select method/technique, criteria, responsibility/context as applicable
V4  group/decompose basis into framework-defined Verification Obligations/Cases
V5  elaborate procedure and enabling environment (partly ISO 15288 baseline; 29148 gives method detail)
V7  execute and produce objective information/results
V8  compare/evaluate result against criteria; keep requirement identity separate from result/status
V9  record anomaly/problem; route requirement change through controlled management
V10 assess change impact, maintain version/traceability, and select re-verification contextually
```

29148 does not define V4 `Verification Case`, a universal anomaly state machine, or a V10 selection algorithm. A verification outcome should update a relationship/status record about satisfaction under a configuration; it should not rewrite the Requirement's normative content except through the controlled change process.

### 3.4 Requirements management — 6.6

| Locator | Strength | Research finding | Framework consequence |
|---|---|---|---|
| 6.6.1 | Descriptive | Requirements and their context/history evolve; baselines and controlled change span the life cycle | Basis identity/version and change-impact provenance are required concepts |
| 6.6.2.1 | Guidance | Proposed changes pass impact assessment, review and approval with trace/version control | Supports V10 orchestration; does not prescribe universal change authority |
| 6.6.2.2 | Mixed | Requirements are configuration managed; functional, allocated, developmental and product baselines are described | Verification results must identify applicable basis/configuration; named baseline use remains project-contextual |
| 6.6.2.3 | Normative + guidance | Requirement information is managed through the organization’s information-management process | Repository representation remains legitimate; retention/access rules require project implementation |
| 6.6.3 | Mixed | Quality, quantity, volatility, traceability, verification and validation measures can support management | Measures are indicators, not universal coverage or sufficiency thresholds |

### 3.5 Information items — Clauses 7–9

| Locator | Strength | Research finding | Framework consequence |
|---|---|---|---|
| Clause 7 | Normative | Produce BRS, StRS, SyRS and, for 12207 use, SRS; content follows Clause 9 | These are controlled information-item types, not necessarily four physical documents |
| Clause 8 | Guidance | Provides example outlines and audience/purpose guidance | Outline placement should not be treated as normative field cardinality |
| 9.2 | Normative content | Identification, revision, front matter, definitions, references and abbreviations form general document content | Useful for rendered specifications; not all fields belong on every atomic model object |
| 9.5 | Normative content | SyRS covers system purpose/scope/context, requirements by concern, verification approaches, assumptions/dependencies | Supports a coherent System Requirements Specification view and basis-to-verification planning interface |
| 9.5.18 | Normative content statement | Provide planned verification approaches and methods, recommended in parallel with requirement sections | Verification planning is a first-class view of SyRS content; parallel presentation is recommended, not a required physical layout |
| 9.5.19 | Normative content statement | List assumptions/dependencies applicable to system requirements and relevant to lower-level allocation/derivation | Assumptions affect requirement provenance and change impact; state machine/cardinality remain open |
| 9.6.19 | Normative content statement | Provide planned software qualification approaches/methods in parallel with specified requirement content | Same interface applies to SRS; item-level software assurance rigor is not supplied by 29148 |

Annex A is normative and defines System Operational Concept content. Annex B is informative Concept of Operations guidance. Annex C is normative for tailored conformance. These annex classifications must be retained whenever their content is cited.

## 4. Verification Basis 与 Verification Obligation

### 4.1 Accepted source-backed chain

```text
Need / Goal / Objective / Concern
  ─controlled transformation→ Requirement

Requirement
  + measurable conditions
  + applicable constraints
  + source/rationale/level/configuration
  ─givesBasisTo→ Verification Obligation
  ─addressedBy→ Verification Method / Action
  ─produces→ Objective Information / Result
```

ISO 29148 strongly supports Requirement as a Verification Basis element and makes verification approach part of SyRS/SRS content. It also repeats the ISO lifecycle purpose covering specified characteristics. Therefore the v0.2 union remains:

```text
VerificationBasisElement :=
  Requirement | SpecifiedCharacteristic | ApplicableConstraint
```

This is a framework-defined conceptual role, not an ISO 29148 class. `SpecifiedCharacteristic` is retained primarily from ISO 15288/29148 verification-purpose wording; 29148 does not provide its universal object schema.

### 4.2 Obligation formation rule

A candidate Verification Obligation is legitimate only when it records:

- the controlled basis element and its applicable version/scope;
- the aspect to be demonstrated and applicable conditions;
- success/acceptance criteria or a controlled pointer to them;
- the planned method/action relationship;
- applicable context such as system level, configuration and environment.

This list is a **conceptual interface**, not a frozen mandatory database schema. Requirements, constraints and characteristics do not automatically become separate obligations merely by existing; the project strategy determines obligation grouping and decomposition while preserving coverage and traceability.

## 5. Requirements information-item disposition

| Source object/content | Proposed repository role | Disposition | Rationale |
|---|---|---|---|
| Requirement | Generic Core basis object | RETAIN / STRENGTHEN | Normative construct and quality characteristics |
| Requirement set | Generic Core aggregate/view | PROMOTE CONCEPTUALLY | Set-level quality differs from item quality; schema/cardinality open |
| Condition | Typed qualifier or basis relation | RETAIN AS ROLE | May qualify a Requirement; not always a standalone constraint |
| Constraint | Requirement content or typed basis element | RETAIN | Standard permits multiple representations/scopes |
| Requirement attribute | Profile/project schema candidate | DO NOT FREEZE | 5.2.8 provides recommended examples, not universal mandatory fields |
| BRS / StRS / SyRS / SRS | Information-item/view types | PROMOTE CONCEPTUALLY | Clause 7/9 normative content; physical-document assumption prohibited |
| Verification approach/method content | Requirement-specification view | PROMOTE INTERFACE | Normative content in 9.5.18/9.6.19; exact schema open |
| RTM / VCRM | Optional representation | RETAIN AS EXAMPLE | Mentioned as documentation practice, not sole valid implementation |
| Requirement Verification Status | Derived/reporting view | RESEARCH PROPOSAL | Standard supports tracing/results, but no universal state machine |

## 6. Research questions

| ID | Answer | Confidence / boundary |
|---|---|---|
| RQ-A | A controlled Requirement is a direct Verification Basis element. Conditions and constraints qualify or restrict it and may be separately controlled; specified characteristics remain valid through the verification-purpose wording. | High for Requirement; medium for independent characteristic schema |
| RQ-B | A well-formed, verifiable Requirement is connected to selected verification actions through method/technique and criteria; the framework represents this as one or more Verification Obligations. | High for relation; cardinality and obligation schema are framework-defined/open |
| RQ-C | 29148 gets as far as objective information/results and traceability. It does not define the Claim–Argument–Evidence structure needed to justify assurance claims. | High; bridge requires 15026-2 |
| RQ-D | The interface is `Requirement/basis → method/action/result`; results become assurance evidence only after evidence applicability/uncertainty/assumptions are recorded and an argument supports a claim. | Cross-standard interpretation, not a single-standard rule |

## 7. Dependency and non-claim register

| ID | Status | Boundary |
|---|---|---|
| DEP-29148-01 | VERSION-MAPPING OPEN | 29148 cites ISO 15288:2015; exact mapping to repository ISO 15288:2023 has not been independently verified clause-by-clause |
| DEP-29148-02 | DEPENDENCY OPEN | ISO/IEC/IEEE 15289 is referenced for information-item planning, but no local source/study exists |
| NC-29148-01 | PROHIBITED CLAIM | Requirement verifiability does not mean implementation verification has passed |
| NC-29148-02 | PROHIBITED CLAIM | Clause 9 content does not establish an executable repository schema or universal cardinalities |
| NC-29148-03 | PROHIBITED CLAIM | RTM/VCRM is not the only conforming representation of traceability or verification planning |
| NC-29148-04 | PROHIBITED CLAIM | Requirement measures do not establish universal evidence sufficiency thresholds |
| NC-29148-05 | PROHIBITED CLAIM | Regulatory stakeholder participation does not establish framework acceptance authority |
| NC-29148-06 | PROHIBITED CLAIM | Conformance to ISO 29148 does not establish aircraft/product airworthiness compliance or authority acceptance of a verification claim |

## 8. Baseline decision

**Decision: ACCEPT AS REVIEWED NORMATIVE SOURCE FOR REQUIREMENTS ENGINEERING AND INFORMATION-ITEM CONTENT.**

The study strengthens Requirement as a Generic Core Verification Basis element, adds a conceptual Requirement Set assessment role, and supports BRS/StRS/SyRS/SRS plus planned-verification views. It does not freeze an executable information model, close ISO-G07 in full, or replace ISO 15288:2023 as the lifecycle-process baseline.
