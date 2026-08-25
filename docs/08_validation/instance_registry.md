---
title: Temporary Controlled Instance Register
status: working
version: 0.2
baseline: post-v0.2
owner: research
last_updated: 2026-08-25
dependencies:
  - cross_repository_instance_contract.md
  - arinc_615a_object_mapping_register.md
  - arinc_615a_instance_evaluation_protocol.md
---

# Temporary Controlled Instance Register

This is a **temporary controlled instance register** used before a versioned object registry exists. Temporary keys are navigation/mapping identities only; they are not stable object IDs, executable schema keys or compatibility approvals.

## Registered instance

| Field | Controlled value |
|---|---|
| Temporary mapping key | `TMP-ARINC615A-01` |
| Instance name/type | ARINC 615A protocol conformance verification / deterministic protocol-conformance instance |
| Canonical repository URL | <https://github.com/ZhangChi0727/arinc-615a-conformance> |
| External active baseline release commit | `3299e6dae83424862f75a4c1d09b91b80d9d8b00` |
| External active baseline tag/ID | `RB-2026-001-v4.2.1` |
| Repository control-state snapshot | `0ce96f701159fd4156d5e5e9889360f53977a61b` — post-release recording commit; not the baseline content commit |
| PR #14 authoring base | `196cfc2426a841a4adb9c9159660253896b0257c` — authoring provenance only; predates the Candidate GVS Core contract |
| Candidate method definition identity | `NOT YET ESTABLISHED — PENDING PR #14 MERGE` |
| Origin classification | `PRE-FRAMEWORK LEGACY INSTANCE BASELINE` |
| Candidate GVS Core binding status | `NOT YET ESTABLISHED` |
| Compatibility status | `NOT-DETERMINED` |
| Mapping register | [ARINC 615A Object Mapping Register](arinc_615a_object_mapping_register.md), version 0.2 |
| Evaluation protocol | [ARINC 615A Instance Evaluation Protocol](arinc_615a_instance_evaluation_protocol.md), version 0.2; not executed |
| Latest independent review | none; external review pending |
| Open blockers | method PR approval/merge; versioned binding; mapping review; instance migration; compatibility review |
| Migration candidate | [Draft PR #9](https://github.com/ZhangChi0727/arinc-615a-conformance/pull/9), head `53a98447bcfa862f082ce443d69115067d3ff2f1`, candidate baseline `RB-2026-001-v4.3`, `UNMERGED MIGRATION CANDIDATE` |
| Non-claims | not fully framework-based; not compatible; not validated; not certification-ready; not Generic evidence by default |

## Legacy and migration boundary

The active baseline release commit/tag predates the Candidate GVS Core contract. The later repository control-state snapshot records release governance but does not replace the tagged content identity. Neither shall be described as “fully based on” this method repository, and historical labels shall not be rewritten. Draft PR #9 is not part of the active baseline and provides no active semantic authority. Its eventual migration must bind the final PR #14 merge SHA; no binding may use `196cfc…` or a mutable PR head as the Candidate method definition.

This method-repository PR does not approve or promote PR #9 concepts including `Verification Objective`, OSR, CEI, A0–A4, R0–R5 or its seven-layer evidence model. Even if PR #9 later merges, compatibility remains `NOT-DETERMINED` until the contract's third handshake and independent compatibility review complete.

The temporary key must never be called stable. Future replacement by a versioned registry requires an explicit migration record preserving this provenance.
