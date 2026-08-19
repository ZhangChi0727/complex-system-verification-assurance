---
title: ISO/IEC/IEEE 15026-2:2022 Clause Study
status: reviewed
version: 0.2
baseline: post-v0.2-candidate
owner: research
last_updated: 2026-08-19
research_type: clause-level-normative-study
source_role: assurance-case-structure-source
primary_layer_role: generic-methodological-source
source:
  standard: ISO/IEC/IEEE 15026-2:2022
  edition: second
  date: 2022-11
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

## 2. Normative dependencies

Clause 2 对 ISO/IEC/IEEE 15026-1 采用未注明年份的规范性引用；按本标准的 undated-reference rule，现行版 ISO/IEC/IEEE 15026-1:2025 是该引用以及 Clause 3 imported terms 的当前依赖，也是本框架唯一现行采用的 assurance vocabulary and concepts 版本。另一方面，5.3.3 对 `Claim` type 明确引用 ISO/IEC/IEEE 15026-1:2019；该 2019 版还出现在一个关于 uncertainty 的资料性 NOTE 中。这些 dated references 只保存 source-native provenance，不构成当前版本采用或独立研究任务。

仓库已取得 ISO/IEC/IEEE 15026-1:2025 的本地受许可原文但尚未完成条款研究；不要求取得或单独研究 2019 全文。以下事项保持开放：

- 2025 版中 assurance、claim、uncertainty 及仓库实际采用共用概念的条款级定义；
- Clause 2/3 的 current undated-reference dependency mapping；
- 把 2025 Claim 概念连接到 15026-2:2022, 5.3.3 结构前的限定兼容性检查；
- 15026-1:2025 与当前 ISO 15288:2023 assurance terminology 的精确版本映射；
- 由 15026-1:2025 支撑的 claim 属性、限制和不确定性语义。

不开展 2019→2025 全文 delta，也不把 15026-2 的明示 2019 locator 机械改写成 2025 条款号。这不妨碍研究 15026-2 自身明确规定的 record types 和 relations；在 targeted compatibility review 完成前，只能声明框架主动采用 2025 定义，不能声明 15026-2:2022 的 dated Claim type 与 2025 完全等价。

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

The standard permits many artefact kinds and defines `Evidence Item` as a four-field record. It does not define a standalone evidence-admission or characterization workflow. The framework may characterize/admit a Result or Artefact as an Evidence Item only through a **framework-defined relation constrained by 5.3.2** so that artefact identity, applicability scope, uncertainty and assumptions are represented. Argument use is a later, source-native 5.3.5 relation. An independently managed or currently unreferenced Evidence Item may exist; it supports no specific Claim until a leaf Argument references it. `unused/orphan evidence` is therefore a framework review status, not a source-native Evidence Item type or admission gate. Exact workflow states, admission authority and cardinality remain open.

### 3.5 Claim and inference — 5.3.3–5.3.4

15026-2:2022, 5.3.3 source-native provenance: dated reference to ISO/IEC/IEEE 15026-1:2019, 3.1.4. The framework's current vocabulary baseline is ISO/IEC/IEEE 15026-1:2025; equivalence is not presumed pending targeted compatibility review. Examples show claims can include limits on property value, duration or uncertainty. They are informative examples, not a closed claim taxonomy. The dated locator must remain unchanged in provenance records.

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

Only `Claim` itself and the Supported Claim/Argument relations are source-native here; several implementation fields below remain candidates because the current full Claim definition must be established from ISO 15026-1:2025 and checked against the 15026-2 structures actually adopted by the framework.

| Candidate | Support status | Basis / boundary |
|---|---|---|
| statement/assertion | DEPENDENCY OPEN | Current Claim definition to be established from ISO 15026-1:2025 |
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
  ─framework characterization constrained by 5.3.2→ Evidence Item
Evidence Item
  ─direct 5.3.5 reference by→ leaf Argument
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
| Claim | Generic Core | RETAIN WITH DEPENDENCY | Full current definition and targeted compatibility depend on 15026-1:2025 |
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
| RQ-D | A Result/artefact may become an independently managed Evidence Item through a framework-defined characterization/admission relation constrained by the four-field record in 5.3.2. It supports a specific Claim only through a later source-native leaf-Argument reference in 5.3.5. | Two-stage architecture; first relation framework-defined, second relation source-native |

## 7. Dependency and non-claim register

| ID | Status | Boundary |
|---|---|---|
| DEP-15026-01 | SOURCE ACQUIRED; CLAUSE STUDY PENDING | ISO/IEC/IEEE 15026-1:2025 is the sole current vocabulary version and the current dependency for the undated Clause 2 reference and Clause 3 imported terms |
| DEP-15026-01A | DATED-REFERENCE PROVENANCE ONLY; NO STANDALONE STUDY PLANNED | ISO/IEC/IEEE 15026-1:2019, 3.1.4 is the explicit source-native `Claim` locator in 5.3.3; related uncertainty provenance is retained without adopting or independently studying the 2019 edition |
| DEP-15026-01B | TARGETED COMPATIBILITY REVIEW OPEN | Review only the 2025 Claim, assurance, uncertainty and repository-adopted concepts needed to connect the current vocabulary to 15026-2; no full 2019→2025 delta and no equivalence presumption |
| DEP-15026-02 | DEPENDENCY OPEN | ISO/IEC/IEEE 15289:2019 report/record references are not independently studied in this repository |
| NC-15026-01 | PROHIBITED CLAIM | Structural conformance or completeness does not prove claim truth |
| NC-15026-02 | PROHIBITED CLAIM | The standard does not define universal evidence quality or sufficiency thresholds |
| NC-15026-03 | PROHIBITED CLAIM | The standard does not require GSN, SACM, CAE or any concrete notation |
| NC-15026-04 | PROHIBITED CLAIM | The standard does not establish certification acceptance or risk-acceptance authority |
| NC-15026-05 | PROHIBITED CLAIM | A trace link from artefact to claim does not by itself constitute an Argument or valid Inference |
| NC-15026-06 | PROHIBITED CLAIM | Evidence reuse does not imply applicability or credit without assessment |

## 8. Baseline decision

**Decision: CLAUSE STUDY REVIEWED; ISO 15026-1:2025 CURRENT VOCABULARY STUDY / TARGETED COMPATIBILITY OPEN; 2019 DATED-REFERENCE PROVENANCE ONLY.**

Independent review confirms the locally defined record types and relations while preserving the source/framework boundary for evidence characterization. The study promotes Supported Claim, Inference, Context, Undeveloped Argument and Narrative Introduction concepts, and records Evidence Item as artefact/applicability/uncertainty/assumptions. It strengthens but does not close generic sufficiency, authority, executable-schema or claim-vocabulary gaps.
