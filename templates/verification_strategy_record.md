---
title: Verification Strategy Record Template
status: working
version: 0.6
baseline: v0.1
owner: research
last_updated: 2026-08-16
dependencies:
  - ../docs/00_overview/terminology.md
---

# Verification Strategy Record

> Research Draft — not an industry standard. ISO/IEC/IEEE 15288:2023, 6.4.9.3(a)(4) supports defining a Verification Strategy, but does not mandate this record name or schema. ISO/IEC/IEEE 24748-2:2024 clarifies integration with project planning. SAE ARP4754B and ARP4761A support the aviation-profile concerns below as recommended practices; neither mandates this unified schema.

```yaml
id:
status:
version:

requirement_id:
verification_obligation_id:

requirement_allocation_level:
verification_execution_level:

verification_allocation_or_delegation: [] # candidate cross-level relations
evidence_acceptance_authority:
cross_level_credit_basis:

verification_method:
verification_technique:

verification_environment:
verification_configuration:
verified_item_or_system_version:
environment_and_tool_versions: []

oracle: # research proposal; expected-result justification source
success_criteria: # maps to ISO 15288 terminology

coverage_obligations: []

independence_requirement: # generic extension point; typed aviation details belong below

required_evidence: []

assurance_applicability: # optional aviation profile; not a generic ISO rule
  source_standard:
  source_location: # e.g., Appendix A table/cell locator
  objective_reference:
  fdal:
  idal:
  objective_applicability: # R*/R/A/N only for the identified ARP4754B Objective x FDAL cell; not a generic enum
  process_independence_required:
  system_control_category:

certification_credit_intent: # candidate project/certification-use relation; separate from applicability and not implied by FDAL

unintended_behavior_obligations: [] # aviation-profile candidate; applicability requires rationale

safety_context: # optional aviation-profile candidate; not a generic requirement
  failure_condition_ids: []
  failure_condition_classifications: []
  safety_objective_ids: []
  safety_requirement_ids: []
  safety_requirement_provenance: [] # typed origins; objective, safety-process constraint, independence principle, controlled assumption, or architecture/analysis result
  assurance_constraint_ids: [] # e.g., traceable FDAL/IDAL assignments
  independence_constraints: [] # type + principle/requirement/claim + substantiation references
  assumption_ids: []
  assumption_confirmation_obligations: []
  safety_analysis_method_ids: [] # distinct from verification_method
  safety_assessment_references: [] # e.g., applicable PSSA/SSA/ASA records

prior_evidence_credit: # optional change/reuse relationship
  source_baseline:
  credit_objectives: []
  applicability_and_differences:
  limitations: []
  supplemental_verification: []
  acceptance_authority:

rationale:

normative_basis: []

assumptions: []

open_issues: []
```
