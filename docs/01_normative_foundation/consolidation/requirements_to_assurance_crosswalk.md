---
title: Requirements-to-Assurance Crosswalk — ISO 29148 and ISO 15026-2
status: research-complete
version: 0.1
baseline: post-v0.2-candidate
owner: research
last_updated: 2026-08-18
dependencies:
  - ../standard_notes/iso_iec_ieee_29148_2018_clause_study.md
  - ../standard_notes/iso_iec_ieee_15026_2_2022_clause_study.md
  - five_source_consistency_gap_review.md
---

# Requirements-to-Assurance Crosswalk

## 1. Purpose

本 crosswalk 回答需求工程链与 assurance-case 链如何连接。它不把两个标准合并为一个虚构过程，也不把框架关系反向归因给任一标准。

Classification：

- `DIRECT`：标准正文直接定义或要求；
- `GUIDANCE`：标准以 recommended/descriptive 形式提供；
- `CROSS-STANDARD INTERPRETATION`：由两个来源共同约束的框架桥接；
- `DEPENDENCY OPEN`：缺少被引用标准原文，不能完成条款级确认；
- `FRAMEWORK PROPOSAL`：为 DBSE 可操作性提出、尚未规范冻结。

## 2. End-to-end semantic chain

```text
Need / Goal / Objective / Concern
  ─29148 transformation→ Requirement
  ─with→ Condition / Constraint / Rationale / Source

Verification Basis Element
  {Requirement | Specified Characteristic | Applicable Constraint}
  ─framework givesBasisTo→ Verification Obligation
  ─29148/15288 constrained addressedBy→ Method / Action + Criteria
  ─produces→ Observation / Result / Artefact

Candidate artefact
  ─15026-2 evidence characterization→ Evidence Item
    {artefact, applicability scope, uncertainty, assumptions}
  ─referenced by leaf Argument→ Supported Claim
  ─through Inference recursion→ higher-level Supported Claim
  ─assembled with Evidence set + Narrative Introduction→ Assurance Case

Assurance Case / Sufficiency Assessment
  ─input to, not replacement for→ Authority Decision / Composite Gate
```

## 3. Five-column normative mapping

| 标准 | 验证/保证目标 | 活动 | 信息项 | 证据 |
|---|---|---|---|---|
| ISO/IEC/IEEE 29148:2018, 5.2.3–5.2.7 | 把需要转化为正确、完整、可行且可验证的需求/需求集 | 需求形成、分析、质量检查、验证/确认需求语句与集合 | Requirement、Requirement Set、source/rationale/condition/constraint | 需求质量评估记录；不是实现符合性证据 |
| ISO/IEC/IEEE 29148:2018, 6.5.2.1–6.5.2.3 | 为系统/元素满足规定要求与特性取得客观证据 | 为 verification action 选择方法和 criteria；执行后维护需求—方法—工作产品追踪 | Verification approach/method、criteria、RTM/VCRM 或等效 repository view | objective information、结果与贯穿生命周期的 trace links |
| ISO/IEC/IEEE 29148:2018, 9.5.18/9.6.19 | 在 SyRS/SRS 中规划如何 qualification | 与 requirement content 平行组织 planned approaches/methods | SyRS/SRS verification content/view | 尚属计划信息；执行结果另行产生 |
| ISO/IEC/IEEE 15026-2:2022, 4.1/5.2 | 对选定系统属性提出 claim，并以 argument/evidence 支持 | 构造并维护 assurance case；呈现 uncertainty/context | Main、Evidence、Report fields | Evidence Item set；结构完整不等于充分或真实 |
| ISO/IEC/IEEE 15026-2:2022, 5.3.2 | 使候选 artefact 在明确适用域和不确定性下支持 assertion | 记录 applicability、uncertainty/credibility/accuracy 和 assumptions | Evidence Item | tangible data/information plus the three semantic qualifiers |
| ISO/IEC/IEEE 15026-2:2022, 5.3.4–5.3.5 | 通过可审计推理支持 claim | 以 evidence reference 支持 leaf claim；以 inference 从 supported premises 导出结论 | Supported Claim、Argument、Inference、Context | referenced Evidence Item at leaf support |
| ISO/IEC/IEEE 15026-2:2022, 5.3.6 | 使 case 可定位、可组装并与系统/环境/版本变化关联 | 记录系统、环境、生命周期、goal/uncertainty、changes、mapping 和 conformance records | Narrative Introduction / Assurance Case Report | 结构 mapping 与 fulfilment records；不是 claim acceptance record |

## 4. Object-to-object crosswalk

| Upstream object | Relation | Downstream object | Classification | Locator / rationale |
|---|---|---|---|---|
| Need/Goal/Objective | transformedInto | Requirement | DIRECT concept | 29148, 5.2.3 |
| Requirement | qualifiedBy | Condition | DIRECT concept | 29148, 5.2.4 |
| Requirement/Set | boundedBy or includes | Constraint | DIRECT concept with representation choices | 29148, 5.2.4–5.2.6 |
| Requirement | assessedFor | Individual quality characteristics | DIRECT requirement | 29148, 5.2.5 |
| Requirement Set | assessedFor | Set quality characteristics | DIRECT requirement | 29148, 5.2.6 |
| Requirement/Basis | givesBasisTo | Verification Obligation | CROSS-STANDARD INTERPRETATION | Framework abstraction constrained by 29148, 6.5.2 and existing ISO 15288 baseline |
| Verification Obligation | addressedBy | Method/Action + Criteria | DIRECT relation semantics / framework object | 29148, 6.5.2.2 |
| Action | produces | Result/Artefact | CROSS-STANDARD INTERPRETATION | 29148 objective-information chain plus lifecycle baseline |
| Result/Artefact | characterizedAs | Evidence Item | CROSS-STANDARD INTERPRETATION | Must satisfy 15026-2, 5.3.2 evidence semantics |
| Requirement specification | referencedIn | Context | DIRECT allowed context form | 15026-2, 5.3.1 Example; example is informative, context type is normative |
| Evidence Item | supports via reference | Leaf Supported Claim | DIRECT structure | 15026-2, 5.3.5(e)(2)(ii) |
| Supported Claims | usedAsPremisesBy | Inference | DIRECT structure | 15026-2, 5.3.4–5.3.5 |
| Inference | derives | Conclusion Claim | DIRECT structure | 15026-2, 3.1.4/5.3.5 |
| Claim/Argument | scopedBy | Context | DIRECT structure | 15026-2, 5.3.1/5.3.5 |
| Evidence Item | reliesOn | Assumption | DIRECT structure | 15026-2, 5.3.2(d) |
| Assurance Case | informs | Sufficiency/Authority Decision | GUIDANCE + FRAMEWORK INTERPRETATION | 15026-2, 4.1; authority and threshold not specified |

## 5. Requirement, Obligation and Claim are not synonyms

| Concept | Primary question | Source basis | Non-equivalence rule |
|---|---|---|---|
| Requirement | What capability/property/constraint must the subject satisfy? | 29148, 5.2.4 | A requirement is not a claim that implementation already satisfies it |
| Verification Obligation | What controlled demonstration must address a basis element under criteria/context? | Framework-defined using 29148/15288 relations | Not source-native; not automatically one-to-one with Requirement |
| Claim | What proposition about a property is asserted for assurance reasoning? | 15026-2 using 15026-1 definition | Full source definition remains dependency-open; a claim may concern more than one requirement |
| Supported Claim | How is a Claim linked to an Argument and Context? | 15026-2, 5.3.5 | It is a recursive assurance-case node, not a requirement status field |

## 6. Evidence admission interface

A verification Result or artefact is only a **candidate** assurance evidence source. Before it assumes the Evidence Item role, the model must be capable of representing:

1. the tangible artefact/data identity and controlled version;
2. its applicability scope, including relevant system/configuration/environment;
3. uncertainty, including source credibility and measurement accuracy where relevant;
4. assumptions relied upon;
5. the leaf Argument reference showing which Claim it supports;
6. provenance to the producing action/result.

Items 1 and 6 combine existing framework provenance/configuration rules with 15026-2 structure. Exact fields/cardinalities remain open. Traceability alone is not evidence admission, and evidence admission alone is not a sufficiency decision.

## 7. ISO 15289 interface placeholder

The task called for relationships to ISO/IEC/IEEE 15289 information items. No 15289 source or prior clause study exists in the repository. Consequently:

| Proposed interface | Current status | Required future check |
|---|---|---|
| 29148 BRS/StRS/SyRS/SRS ↔ 15289 information-item taxonomy | DEPENDENCY OPEN | Verify edition, clauses, overlap and conformance interaction |
| 15026-2 Evidence artefact report/record ↔ 15289 report/record types | DEPENDENCY OPEN | Study the 15289 edition cited by 15026-2 and reconcile with repository target |
| Assurance Case Report ↔ generic report information item | DEPENDENCY OPEN | Determine whether mapping is type inheritance, view, composition or reference |
| Verification result/record ↔ evidence artefact | DEPENDENCY OPEN at schema level | Preserve conceptual role now; defer fields/cardinality |

No placeholder above is treated as a verified mapping.

## 8. V0–V12 mapping

`15289` cells are deliberately `DEPENDENCY OPEN`; they are research targets, not completed mappings.

| Framework element | ISO 29148 basis | ISO 15289 interface | ISO 15026-2 basis | Ontology / boundary |
|---|---|---|---|---|
| V0 Verification Planning | Method definition can address how/who/when/where: 6.5.2.2 | Plan mapping DEPENDENCY OPEN | Assurance case should start early and be maintained: 4.1 | Mixed planning concern; no single-source process |
| V1 Basis/Obligation | Need→Requirement and requirement constructs: 5.2.3–5.2.4 | Requirement information organization DEPENDENCY OPEN | Requirement/specification reference can be Context: 5.3.1 | Basis source-supported; Obligation framework-defined |
| V2 Verifiability | Direct individual/set/language quality rules: 5.2.4–5.2.7 | Information quality mapping DEPENDENCY OPEN | No direct requirement-quality process | Source-supported activity with separate scopes |
| V3 Strategy | Method/criteria association: 6.5.2.2 | Plan mapping DEPENDENCY OPEN | Context and early lifecycle integration: 4.1/5.3.1 | Framework orchestration |
| V4 Verification Case Design | Partial method/criteria and specification content: 6.5.2.2; 9.5.18/9.6.19 | Specification/procedure mapping DEPENDENCY OPEN | No verification-case object | Framework-defined information design |
| V5 Procedure Development | Method detail and objective-information intent: 6.5.2.2 | Procedure mapping DEPENDENCY OPEN | Preparation/collection description can itself be Evidence: 5.3.2 Note | Mixed; exact procedure schema open |
| V6 Verification Readiness | No named gate; method/venue/resources are readiness inputs | Review/report mapping DEPENDENCY OPEN | No named gate | Framework Composite Gate |
| V7 Execution | Activity yields objective information: 6.5.2.2 | Record mapping DEPENDENCY OPEN | Result/record can be candidate artefact: 5.3.2 | Source-supported execution + evidence-source role |
| V8 Result Evaluation | Criteria and result traceability: 6.5.2.2–6.5.2.3 | Evaluation report mapping DEPENDENCY OPEN | Evidence applicability/uncertainty/assumptions and Claim support: 5.3.2/5.3.5 | Mixed evaluation/admission/decision |
| V9 Anomaly Resolution | Anomalies may trigger requirement change; controlled change: 6.5.2.3/6.6.2 | Problem record/report mapping DEPENDENCY OPEN | Anomaly artefact may be Evidence or Context only through typed use | Cross-process orchestration |
| V10 Change Impact & Re-verification | Impact/review/approval/version/trace control: 6.6 | Change request/status mapping DEPENDENCY OPEN | Case maintenance and relevant-version changes: 4.1/5.3.6 | Mixed orchestration; selection rule open |
| V11 Coverage & Sufficiency | Requirement/trace measures only partial: 6.6.3 | Report/record mapping DEPENDENCY OPEN | Argument structure and uncertainty inputs; no sufficiency algorithm: 4.1/5.3.5 | Generic Extension Point |
| V12 Verification Closure | No universal state machine/authority | Review/report/record mapping DEPENDENCY OPEN | Top-level Supported Claim and report can inform decision; no authority rule | Framework Composite Gate |

## 9. Relation-support register

| Arrow | Support classification | Boundary |
|---|---|---|
| Need → Requirement | DIRECT — 29148 | Controlled transformation, not identity |
| Requirement → Verification Criterion/Method | DIRECT/INDIRECT — 29148 task plus guidance | Criteria attaches to verification action; exact data model open |
| Basis Element → Verification Obligation | FRAMEWORK-DEFINED | Source-constrained abstraction; no direct need/FC/DAL shortcut |
| Obligation → Action/Procedure | FRAMEWORK-DEFINED with DIRECT relation semantics | 29148 supports action/method/criteria, not Obligation class |
| Action → Result/Artefact | INDIRECT cross-lifecycle support | Maintain execution/configuration provenance |
| Result/Artefact → Evidence Item | CROSS-STANDARD FRAMEWORK RELATION | Requires 15026-2 applicability/uncertainty/assumptions; not automatic |
| Evidence Item → leaf Supported Claim | DIRECT — 15026-2 | Via Argument evidence reference, not a bare trace link |
| premise Supported Claims → top-level Claim | DIRECT — 15026-2 | Via explicit Inference and Context |
| Supported Claim/Assurance Case → Closure Decision | FRAMEWORK-DEFINED / PROFILE-SPECIFIC | Standard provides decision input, not authority or acceptance rule |

## 10. Crosswalk verdict

The two standards establish a defensible interface but not a single normative end-to-end process. ISO 29148 controls the demand side—requirements, quality, verification method/criteria and specification content. ISO 15026-2 controls the assurance reasoning side—evidence semantics, context, recursive supported claims, inference and report/index structure. `Verification Obligation` and the admission of Results into Evidence are framework bridge abstractions with explicit provenance.
