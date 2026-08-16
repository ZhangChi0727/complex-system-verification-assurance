---
title: Verification Information Model Workspace
status: planned
version: 0.5
baseline: v0.1
owner: research
last_updated: 2026-08-16
dependencies:
  - ../03_dbse_workflow/README.md
---

# Verification Information Model Workspace

Candidate information entities — not yet frozen:

`Requirement`、`Verification Obligation`、`Assurance Objective`、`Verification Strategy`、`Verification Activity`、`Verification Method`、`Verification Technique`、`Verification Case`、`Verification Procedure`、`Verification Environment`、`Configuration`、`Stimulus`、`System State`、`Expected Result`、`Observed Result`、`Acceptance Criterion`、`Oracle`、`Coverage Obligation`、`Coverage Result`、`Verification Data`、`Evidence`、`Evidence Credit`、`Anomaly`、`Change`、`Change Impact / Re-verification Activity`、`Compliance Claim`。

Aviation profile adds candidates `Failure Condition`、`Failure Condition Classification`、`Safety Objective`、`Safety Requirement`（`Requirement` subtype/classification）、`Assurance Constraint`（including traceable FDAL/IDAL assignments）、typed `Independence Principle / Requirement / Claim`、`Safety Analysis Method/Result`、`Safety Assessment`、`Assumption`、`Assumption Obligation` and `Assumption Confirmation`. Generic promotion and cardinalities are not frozen.

Candidate safety derivation/aggregation relations:

```text
Failure Condition → Classification → Safety Objective
{Safety Objective,
 Safety Process Constraint,
 Independence Principle,
 Controlled Assumption,
 Architecture/Analysis Result} → Safety Requirement
Safety Requirement | Assurance Constraint → Verification / Assurance Obligation
Development Verification Evidence + Safety Analysis Evidence
  → SSA/ASA Safety Assessment Evidence
```

`SafetyRequirementOrigin` is a candidate typed provenance relation rather than a mandatory single-valued source. A Failure Condition remains upstream and does not directly generate an obligation; each obligation must be justified through a Requirement or Constraint relation. Independence source definitions, claims and substantiation criteria/evidence are also separate objects or relations.

Current evidence-architecture hypothesis：`Verification Result/Data → may constitute or support Evidence → supports Argument → supports Claim`。这只是 framework research hypothesis；Evidence identity 与 provenance、integrity/control、claim applicability、credibility 和 sufficiency contribution 分开建模，不能用固定条件把 Result 二值转换为 Evidence，也不能归因于 ARP4754B/ARP4761A 的完整原生 ontology。`Development Verification Evidence`、`Safety Analysis Evidence` 与 `Safety Assessment Evidence` 是候选 evidence roles，不是互斥的物理文件类型。

**Future contents:** fields、relationships、ownership、lifecycle states、traceability 和 configuration semantics。

**Status:** Planned；依赖 DBSE activities 稳定。
