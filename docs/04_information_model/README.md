---
title: Verification Information Model Workspace
status: conceptual-baseline
version: 0.6
baseline: v0.1
owner: research
last_updated: 2026-08-16
dependencies:
  - ../01_normative_foundation/consolidation/five_source_consistency_gap_review.md
  - ../03_dbse_workflow/README.md
---

# Verification Information Model Workspace

五源 consolidation 已稳定第一版 objects/relations，但未冻结 field-level schema、cardinality、state machine 或 serialization。后续必须按 `source semantics → consolidated concepts → relations → information model → template fields` 推进。

## Generic Core

- `Requirement`；
- conceptual `VerificationBasisElement` role over `Requirement`、`SpecifiedCharacteristic` and `ApplicableConstraint`；
- `VerificationObligation`；
- `VerificationStrategy`；
- `VerificationAction`、`VerificationProcedure`；
- `Observation`、`Result`；
- `Evidence`、`Argument`、`Claim`；
- `Configuration`；
- `Change`、`ImpactAssessment`；
- `Decision`、`CompositeGate`。

`Verification Method`、`Verification Technique`、`Verification Case`、`Verification Environment`、`Stimulus`、`System State`、`Expected Result`、`Acceptance Criterion`、`Anomaly` 等继续作为 supporting candidate entities；其精确 field/cardinality 仍需后续来源。

## Generic Extension Points

- `AssuranceConstraint`；
- `IndependenceConstraint`；
- `CoverageObligation`、`CoverageResult`；
- `SufficiencyAssessment`；
- `Assumption`；
- `PriorEvidenceApplicability`。

这些对象进入 conceptual baseline，但 taxonomy、decision criteria、authority 和完整 lifecycle semantics 由 domain profile 或后续研究提供。`Oracle` 继续是显式 `RESEARCH PROPOSAL`。

## Civil Aviation Profile

- `FailureCondition`、`FailureConditionClassification`；
- `SafetyObjective`、`SafetyRequirement`（`Requirement` subtype/classification）；
- traceable `FDALAssignment`、`IDALAssignment`；
- `IndependencePrinciple`、`IndependenceRequirement`、`IndependenceClaim`；
- `SafetyAnalysisMethod`、`SafetyAnalysisResult`；
- `SafetyAssessment` and PSSA/SSA/ASA roles；
- `VerificationCredit`、`CertificationCreditIntent`。

## Stable relations

```text
VerificationBasisElement
  = Requirement | SpecifiedCharacteristic | ApplicableConstraint
VerificationBasisElement
  ─typed givesBasisTo→ VerificationObligation

VerificationObligation
  ─addressedBy→ VerificationStrategy
  ─coveredBy→ one or more VerificationAction/Case dispositions

VerificationStrategy ─realizedBy→ Action / Procedure
Procedure ─produces→ Observation / Result
Result or controlled Data ─mayConstituteOrSupport→ Evidence
Evidence ─supports→ Argument ─justifies→ Claim

CoverageObligation ─assessedBy→ CoverageResult
SufficiencyAssessment
  ─considers→ obligations/coverage/evidence/limitations/assumptions/anomalies/constraints

Change
  ─affects→ requirement/obligation/claim/assumption/configuration/evidence
ImpactAssessment ─selects→ re-verification/re-analysis
Decision ─authorizes→ CompositeGate state/baseline event
```

Verification Obligation basis is constrained many-to-many: every obligation has at least one typed、受控 basis element；每个适用且需要验证的 Requirement 或 Specified Characteristic 至少由一个 obligation 覆盖，或有明确 non-verification/disposition rationale。`VerificationBasisElement` 是 conceptual union/typed relation role，不在 v0.2 冻结为独立 class、field schema 或完整 cardinality model。

## Evidence and relation semantics

```text
Observation / Raw Record → evaluatedAs Result
Result/Data → may constitute or support Evidence
Evidence → supports Argument → justifies Claim
```

Evidence identity、provenance、integrity/configuration、claim applicability、credibility 与 sufficiency contribution 分开建模。`Verification Data` 是 aviation information-item/container role，不是 generic Evidence subtype。`Development Verification Evidence`、`Safety Analysis Evidence` 与 `Safety Assessment Evidence` 是可重叠的 profile roles。

三类 graph relation 必须可分别查询：

- Traceability：什么与什么相关；
- Provenance：对象/结论从何处产生并如何转化；
- Argumentation：为什么 evidence 足以支持 conclusion/claim。

## Aviation derivation and aggregation

```text
Failure Condition → Classification → Safety Objective

{Safety Objective,
 Safety Process Constraint,
 Independence Principle,
 Controlled Assumption,
 Architecture/Analysis Result}
  ─typed SafetyRequirementOrigin→ Safety Requirement

Safety Requirement | Assurance/Independence Constraint
  ─givesBasisTo→ Verification / Assurance Obligation

Development Verification Evidence + Safety Analysis Evidence
  ─aggregated/evaluatedBy→ SSA/ASA Safety Assessment Evidence
```

A Failure Condition is upstream and never directly generates an obligation. Independence type、principle、requirement、claim 与 substantiation evidence 必须分离；不能使用一个 Boolean 表达。

Safety Objective、Independence Principle、Assumption、FDAL/IDAL 或未受控 project custom 不能无中介生成 obligation；必须先形成适当的 Requirement、Applicable Constraint 或其他明确受控的 typed basis relation。航空 profile 继续使用 Safety Requirement 与 Assurance/Independence Constraint 作为直接 basis。

## Assumption conceptual boundary

Generic `Assumption` extension semantics should be capable of representing identity、statement、scope/context、affected objects、applicable validity/confirmation information，以及 applicable process/profile/project 已定义的 ownership/responsibility。该能力清单不是 mandatory information-item schema。Exact ownership、required fields、validity states、confirmation obligations、cardinalities and lifecycle transitions remain open pending ISO 15289 and later domain evidence.

## Coverage, sufficiency and gate interfaces

`CoverageObligation` minimum：population/scope、criterion、evidence/result、uncovered disposition、configuration/context。`SufficiencyAssessment` inputs：obligations、coverage、evidence、limitations、assumptions、anomalies、constraints；outputs：conclusion、rationale、residual gaps、assessor/decision context。

`CompositeGate` minimum：Assessment、optional Review、Authority Decision、State/Baseline Event，并分别保留 identity/provenance。V6/V12 的 authority、waiver、reopening 和 state machine 仍 open。

**Next action:** 研究 ISO/IEC/IEEE 15289 以补充 information-item content/provenance，再决定 field/cardinality 与模板重构；不得把本页概念清单直接当作 executable schema。
