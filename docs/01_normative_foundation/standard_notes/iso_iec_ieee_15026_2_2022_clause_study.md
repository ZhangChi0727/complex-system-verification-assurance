---
title: ISO/IEC/IEEE 15026-2:2022 Clause Study
status: research-complete-with-open-dependency
version: 0.1
baseline: post-v0.2-candidate
owner: research
last_updated: 2026-08-18
research_type: clause-level-normative-study
source_role: assurance-case-structure-source
primary_layer_role: generic-methodological-source
source:
  standard: ISO/IEC/IEEE 15026-2:2022
  edition: second
  date: 2022-10
  source_type: licensed-local-source-not-committed
dependencies:
  - ../consolidation/five_source_consistency_gap_review.md
  - ../normative_gap_matrix.md
  - ../consolidation/clause_evidence_register_29148_15026_2.md
---

# ISO/IEC/IEEE 15026-2:2022 Clause Study

## 1. 研究目的与边界

本笔记研究 assurance case 的规范结构，以及 Evidence、Claim、Argument、Inference、Context、Assumption 与 Report 的关系。原 PDF 只用于本地研究，不纳入版本库；本文保存条款定位和自行撰写的结构性结论。

逐条款的完整审计字段记录见 [Clause Evidence Register](../consolidation/clause_evidence_register_29148_15026_2.md)。

ISO/IEC/IEEE 15026-2:2022 规定 assurance case 的**结构术语及其含义**。Introduction 明确排除对内容质量的要求；4.1 把证据充分性判断留给 assurance-case 读者。因此：

- 结构符合本标准，不等于 claim 为真；
- assurance case 完整，不等于 evidence 充分、可信或被权威接受；
- 本标准不规定 concrete notation、图形表示或物理数据实现；
- 本标准不产生 certification authority、acceptance threshold 或风险接受规则。

## 2. Normative dependency

Clause 2 唯一规范性引用是 ISO/IEC/IEEE 15026-1。Clause 3 又直接采用其中的术语定义，尤其是 `claim`，4.1 也依赖其 assurance/uncertainty 基础概念。

仓库没有 ISO/IEC/IEEE 15026-1:2019 原文或研究笔记。因此以下事项登记为 `DEPENDENCY OPEN`：

- assurance、claim 和 uncertainty 的完整 source-native 定义；
- 15026-1 与当前 ISO 15288:2023 assurance terminology 的精确版本映射；
- 由 15026-1 支撑的 claim 属性、限制和不确定性语义。

这不妨碍研究 15026-2 自身明确规定的 record types 和 relations，但本轮不能宣称完整的 15026 系列术语基线。

## 3. Clause-level findings

### 3.1 Purpose and use — Introduction, Clauses 1 and 4

| Locator | Strength | Research finding | Framework consequence |
|---|---|---|---|
| Introduction | Scope boundary | Defines consistent/comparable assurance-case structure; excludes requirements on content quality and concrete representation | Treat as conceptual metamodel source, not a sufficiency or notation standard |
| Clause 1 | Normative scope | Applies to developing and maintaining assurance cases | Assurance case lifecycle/change concerns are in scope |
| 4.1 | Explanatory semantics | Claims concern selected system properties and arguments support their truth under context and uncertainty | Claim must identify property/scope/context; structural support is not automatic truth |
| 4.1 | Explanatory semantics | Uncertainty can concern inference validity, context relevance, and evidence relevance/trustworthiness | Uncertainty is multi-location and cannot be reduced to one numeric confidence field |
| 4.1 | Boundary | Readers assess sufficiency; demanded validity/confidence should be proportionate to risk reduction | No universal threshold or automatic closure inference |
| 4.1 | Lifecycle guidance | Assurance cases should begin early and be maintained as system, use and environment change | Connect change impact to claims, context, assumptions, evidence and argument |
| 4.2 | Application requirement | Provide a Clause-5-shaped assurance case, a logical mapping to that structure, and fulfilment records | Conformance evidence and structure mapping are part of the case |

4.1 notes that top-level claims can originate in stakeholder requirements, be established by an approval authority, or be selected internally. This is an informative source of possible origins, not a rule that every Requirement becomes a Claim or that every Claim requires an authority origin.

### 3.2 Top-level structure — 5.1–5.2

An assurance case has three fields:

| Field | Required type | Interpretation |
|---|---|---|
| Main | Supported Claim | Argument structure rooted at a top-level claim |
| Evidence | Set of Evidence Items | Evidence inventory available to referenced leaf support |
| Report | Narrative Introduction | System/environment/lifecycle/change/goal and structure-mapping context |

5.1 additionally requires an identifier mechanism that unambiguously resolves values/types, declared parameters or generally accepted terms. This directly supports identity/referential integrity, but does not prescribe UUIDs, graph databases or a particular serialization.

The assurance case is incomplete if its main field contains an undeveloped argument. “Incomplete” is a structural status; it must not be converted into a negative truth judgment about the claim, just as structural completeness must not be converted into acceptance.

### 3.3 Context — 5.3.1

Context is a list whose elements can be a definition, a basic assumption, or a reference to a system-of-interest document. Context can define scoped identifiers for evidence, case elements, the system and environment.

Framework disposition:

- Context is a Generic Core relation/value role attached to Supported Claim or Argument;
- Basic Assumption is one allowed context element, not the only form of assumption in the entire framework;
- scoping must be explicit when identifiers have local meanings;
- project requirements/specifications can be referenced as context without thereby becoming evidence.

### 3.4 Evidence — 5.3.2

The Evidence Item record contains four semantic fields:

| Field | Meaning | Framework mapping |
|---|---|---|
| Artefact | Tangible data/information, including lifecycle items, reports, records or authoritative documents | `EvidenceArtifact` / referenced controlled artefact |
| Scope of applicability | Where the item can legitimately support a claim | `applicabilityScope` and link to system/configuration/context |
| Uncertainty | Includes source credibility and measurement accuracy | `EvidenceUncertainty` / credibility and measurement-quality assessment |
| Assumptions | Conditions relied upon by the evidence | typed `reliesOn Assumption` relation |

An item may pre-exist the case or be created/collected for it; evidence may be managed independently of arguments. These statements support evidence reuse and independent configuration management, but do not grant credit automatically. `PriorEvidenceApplicability` remains a separate assessment.

The standard permits many artefact kinds. Being an artefact is insufficient: it becomes an Evidence Item only with its applicability, uncertainty and assumptions represented and when referenced by an argument that supports a claim.

### 3.5 Claim and inference — 5.3.3–5.3.4

Claim type is normatively inherited from ISO/IEC/IEEE 15026-1:2019 and therefore remains dependency-constrained in this repository. Examples show claims can include limits on property value, duration or uncertainty. They are informative examples, not a closed claim taxonomy.

Inference is the reasoning step that derives a conclusion claim from premise claims under a specified context. Justification can be given in context. Even an “obvious” inference remains explicit so assumptions are visible. Framework consequences:

- `Inference` is not interchangeable with `Argument`;
- premise and conclusion relations must be explicit and ordered/scoped sufficiently to reconstruct reasoning;
- no inference may be fabricated merely because evidence and a claim share a trace link.

### 3.6 Supported Claim and Argument — 5.3.5

The standard mutually and recursively defines Supported Claim and Argument:

```text
SupportedClaim = Claim + supporting Argument + applicable Contexts

Argument =
  UndevelopedArgument
  OR
  Contexts + (
    Inference from a list of SupportedClaims
    OR reference to an EvidenceItem
  )
```

This structure establishes two different support cases:

1. an inference decomposes a conclusion into recursively supported premise claims;
2. a leaf argument refers to an evidence item supporting the truth of its claim.

Accordingly, the v0.2 shorthand `Evidence → Argument → Claim` is directionally correct but incomplete. The information model must preserve Supported Claim recursion and distinguish inference-mediated support from evidence-reference leaf support.

Cardinality conclusions must remain conservative. The record definition gives each `SupportedClaim` one claim field and one argument field, while an inference can use a list of supported claims and an assurance case has a set of evidence items. It does not settle whether a project may maintain multiple alternative Supported Claim structures around the same semantic Claim, nor does it prohibit one Evidence Item from being referenced by multiple leaf Arguments. Those reuse/identity cardinalities are framework schema questions.

### 3.6.1 Claim and related-object candidate structure

Only `Claim` itself and the Supported Claim/Argument relations are source-native here; several implementation fields below remain candidates because the full Claim definition comes from ISO 15026-1.

| Candidate | Support status | Basis / boundary |
|---|---|---|
| statement/assertion | DEPENDENCY OPEN | Claim definition imported from ISO 15026-1 |
| property under assurance | Direct explanatory support | 4.1; claims concern selected system properties |
| subject/system scope | Indirect/candidate | System of interest is described in narrative/context; exact Claim field not defined in 15026-2 |
| limitation / applicable condition | Example-supported candidate | 5.3.3 examples; do not promote example shape into mandatory field |
| validity duration | Example-supported candidate | 5.3.3 example only |
| uncertainty | Direct conceptual support | 4.1 and 5.3.5 Note; location/representation can be Context |
| configuration identity | Cross-standard framework candidate | Needed for controlled applicability; not a direct 15026-2 Claim field |
| Supported Claim contexts | Direct structure | 5.3.5(c) |
| Argument contexts | Direct structure | 5.3.5(e)(1) |
| inference rule/rationale | Direct inference + contextual justification | 5.3.4; exact schema open |

`Verification Result` is normally a Result/artefact that may be admitted as an Evidence Item; it is not itself a Claim. `Objective Satisfaction` should be separated into a Claim about satisfaction and an assessment/decision state. `Compliance Claim` may specialize or type a Claim in a profile but cannot be equated with authority acceptance.

### 3.7 Narrative introduction — 5.3.6

The report/narrative introduction records:

- system and service;
- operational environment;
- system lifecycle;
- top-level claim and its uncertainty;
- relevant changes from/to adjacent system versions;
- unambiguous mapping to the standard structure, including justified omissions;
- records demonstrating fulfilment of this standard.

This supports a snapshot/report view and change provenance. The assurance case report is not the whole assurance case: it introduces the case and supplies a complete index from which the relevant argument/evidence can be assembled. For simple cases it can be superfluous as described in the definition note; a future schema must preserve the distinction between the `report field` required by 5.2 and whether a separate published report document is useful.

## 4. Requirements-to-assurance bridge

15026-2 does not define requirements engineering, and 29148 does not define assurance-case argument structure. The defensible interface is therefore typed rather than an object identity:

```text
Requirement / Specified Characteristic / Applicable Constraint
  ─givesBasisTo→ Verification Obligation
  ─addressedBy→ Verification Action
  ─produces→ Result / controlled artefact

Result / artefact
  ─evaluatedFor applicability, uncertainty, assumptions→ Evidence Item
  ─referencedBy→ leaf Argument
  ─supportsTruthOf→ Claim

Claim
  ─can be premise in→ Inference
  ─supports recursively→ higher-level Claim
```

No direct universal equivalence is established between `Requirement` and `Claim`:

- a requirement can be referenced in Context;
- a claim can assert that a requirement or property is satisfied;
- a top-level claim may originate from a stakeholder requirement, authority or internal assurance goal;
- one requirement can contribute to multiple claims, and one claim can rely on many requirements/results/evidence items.

## 5. Object disposition

| Source concept | Framework role | Disposition | Boundary |
|---|---|---|---|
| Assurance Case | Generic Core aggregate | PROMOTE / REFINE | Structure source-backed; content quality not guaranteed |
| Supported Claim | Generic Core recursive node | PROMOTE | Distinct from bare Claim |
| Claim | Generic Core | RETAIN WITH DEPENDENCY | Full definition depends on 15026-1 |
| Argument | Generic Core | REFINE | Either undeveloped or context plus inference/evidence reference |
| Inference | Generic Core | PROMOTE | Distinct reasoning step with premises and conclusion |
| Evidence Item | Generic Core | REFINE | Artefact + applicability + uncertainty + assumptions |
| Context | Generic Core role | PROMOTE | Definitions/basic assumptions/document references; scope matters |
| Basic Assumption | Assurance-case context subtype | RETAIN | Does not replace broader framework Assumption extension point |
| Undeveloped Argument | Structural state/type | PROMOTE | Makes incomplete reasoning explicit; not a claim-false state |
| Narrative Introduction / Assurance Case Report | Information-item/view | PROMOTE CONCEPTUALLY | Report/index differs from full case |
| Validity/confidence threshold | Profile/project rule | KEEP OPEN | No universal criterion supplied |
| Acceptance decision/authority | Gate/profile concern | KEEP OPEN | Standard supports use in decisions but does not confer authority |

## 6. Research questions

| ID | Answer | Confidence / boundary |
|---|---|---|
| RQ-A | 15026-2 does not define Verification Basis. Requirements/specifications can be Context; lifecycle outputs/results can become Evidence Items only with the required evidence semantics. | High |
| RQ-B | 15026-2 does not form Verification Obligations from Requirements. That bridge comes from 29148/15288 plus a framework-defined obligation abstraction. | High |
| RQ-C | Evidence supports a leaf Claim through an Argument reference; Inference recursively connects supported premise Claims to a conclusion Claim, all under applicable Context. | High for 15026-2 structure; Claim definition dependency remains open |
| RQ-D | Verification results/artefacts cross into assurance only after evidence applicability, uncertainty and assumptions are represented and the Evidence Item is used in the supported-claim structure. | Cross-standard interpretation, strongly constrained by 5.3.2/5.3.5 |

## 7. Dependency and non-claim register

| ID | Status | Boundary |
|---|---|---|
| DEP-15026-01 | DEPENDENCY OPEN | ISO/IEC/IEEE 15026-1:2019 is normative and absent; full assurance/claim/uncertainty terminology cannot be frozen |
| DEP-15026-02 | DEPENDENCY OPEN | ISO/IEC/IEEE 15289:2019 report/record references are not independently studied in this repository |
| NC-15026-01 | PROHIBITED CLAIM | Structural conformance or completeness does not prove claim truth |
| NC-15026-02 | PROHIBITED CLAIM | The standard does not define universal evidence quality or sufficiency thresholds |
| NC-15026-03 | PROHIBITED CLAIM | The standard does not require GSN, SACM, CAE or any concrete notation |
| NC-15026-04 | PROHIBITED CLAIM | The standard does not establish certification acceptance or risk-acceptance authority |
| NC-15026-05 | PROHIBITED CLAIM | A trace link from artefact to claim does not by itself constitute an Argument or valid Inference |
| NC-15026-06 | PROHIBITED CLAIM | Evidence reuse does not imply applicability or credit without assessment |

## 8. Baseline decision

**Decision: ACCEPT AS REVIEWED NORMATIVE SOURCE FOR ASSURANCE-CASE STRUCTURE, WITH ISO 15026-1 DEPENDENCY OPEN.**

The study promotes Supported Claim, Inference, Context, Undeveloped Argument and Narrative Introduction concepts, and refines Evidence Item into artefact/applicability/uncertainty/assumptions. It strengthens but does not close generic sufficiency, authority, executable-schema or claim-vocabulary gaps.
