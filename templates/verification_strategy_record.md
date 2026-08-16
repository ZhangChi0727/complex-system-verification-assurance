---
title: Verification Strategy Record Template
status: working
version: 0.7
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

verification_basis_elements: # provisional typed relations, not a frozen VerificationBasisElement schema
  - basis_type: # Requirement | Specified Characteristic | Applicable Constraint
    reference_id:
    source_and_rationale:
verification_obligation_ids: [] # each obligation requires at least one typed, controlled basis relation

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

expected_result_basis: []
oracle: # explicit research proposal; do not treat as a five-source native object
success_criteria: # maps to ISO 15288 terminology

coverage_obligations:
  - id:
    population_and_scope:
    criterion:
    required_evidence:
    uncovered_disposition_rule:
    configuration_context:

assurance_constraints: [] # generic extension point; type/source/applicability/rigor/evidence controls
independence_constraints: # generic extension point; never reduce to independent: true/false
  - id:
    type_and_profile_vocabulary:
    source_and_rationale:
    applicable_activity_object_or_claim:
    required_condition:
    claim_reference:
    substantiation_evidence: []

required_evidence:
  - evidence_role:
    claim_or_argument_context:
    provenance_requirement:
    configuration_and_control:
    applicability_or_credibility_criteria:

sufficiency_assessment_requirement:
  applicable_obligations:
  coverage_inputs:
  evidence_inputs:
  limitations_and_assumptions:
  anomaly_or_deviation_inputs:
  required_conclusion_and_rationale:
  decision_context:

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
  independence_profile_details: [] # functional/item-development/physical/process + principle/requirement/claim; complements generic constraints above
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

assumption_references: [] # generic conceptual references; owner/status/confirmation fields are profile/project-defined, not universally mandatory

open_issues: []
```
