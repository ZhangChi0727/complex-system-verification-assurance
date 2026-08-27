---
title: ARINC 615A Temporary Object Mapping Register
status: working
version: 0.3
baseline: post-v0.2
owner: research
last_updated: 2026-08-26
dependencies:
  - cross_repository_instance_contract.md
  - instance_registry.md
  - arinc_615a_v43_migration_evidence_return.md
  - arinc_615a_third_handshake_compatibility_disposition.md
  - ../01_normative_foundation/research_tasks/002_iso_iec_9646_series.md
  - ../02_verification_framework/generic_verification_suite_core.md
---

# ARINC 615A Temporary Object Mapping Register

## Control boundary

This register is a `temporary controlled mapping`, not a stable registry,
equivalence claim or Framework Rule. The historical legacy source remains
release commit `3299e6dae83424862f75a4c1d09b91b80d9d8b00` / annotated tag
`RB-2026-001-v4.2.1`. The active migration baseline is baseline ID
`RB-2026-001-v4.3`, release commit
`523d42bf03a1135b3d63a00bfb47d3b879d3927e`, and annotated release tag
`v4.3` whose object `28312fd9c5470cb15d76eb3762c99a25ab842cfd`
peels to that commit. Pre-migration control commit
`0ce96f701159fd4156d5e5e9889360f53977a61b` is provenance, not the release
identity. PR #9 reviewed head `5d149d1f8e92bbed438fe8bc78be9e8972fecb7d`
is the second parent of the ordinary merge.

The row-level mapping statuses remain limited to `NOT-DETERMINED`, `CANDIDATE`,
`PARTIAL`, `CONFLICT` and `OUT-OF-SCOPE`. The separate third-handshake review
column records interface coexistence without strengthening a source relation or
mapping status. The proposed overall disposition remains review-pending and does
not activate a reviewed compatibility status before independent approval and
merge.

Relation direction is fixed as:

```text
ARINC object --primary relation--> Framework candidate/role
```

Every row has exactly one primary relation. Secondary resemblance, uncertainty
and supporting semantics stay in rationale, review result and qualification.

## Method-side 18-row reconciliation

The source order, relation and mapping status reproduce instance register
`TMP-MAP-ARINC615A-01` version `0.2-candidate` at the v4.3 release commit.

| Source row | Framework candidate/role | ARINC object | Source provenance | Primary relation | Mapping status | Rationale | Open dependency | Migration note | Third-handshake review | Qualification |
|---|---|---|---|---|---|---|---|---|---|---|
| R01 | Applicability/Profile Declaration | PICS-like declaration | v4.3 release; legacy-origin object | `realizes` | `CANDIDATE` | controls applicability and the applicable CRS population; is not Verification Basis | ISO/IEC 9646 Task 002; Profile review | retain declaration separately from basis items | `QUALIFIED-ALIGNED` | Q-04, Q-07 |
| R02 | VerificationBasisElement | applicable CRS item | v4.3 release; legacy-origin object | `candidate-correspondence` | `CANDIDATE` | may play a typed basis role without asserting a frozen Core class | Task 002 and mapping review | preserve CRS locator and applicability provenance | `QUALIFIED-ALIGNED` | Q-04, Q-07 |
| R03 | VerificationObligation | current ARINC requirement-obligation aspect | v4.3 release; legacy-origin object | `no-direct-correspondence` | `NOT-DETERMINED` | no controlled legacy identity exposes comparable semantics | obligation identity/semantics review | do not retrofit a stable ID into frozen history | `OPEN-NO-EQUIVALENCE` | Q-03, Q-04 |
| R04 | VerificationObligation | PR #9 Verification Objective | v4.3 release | `candidate-correspondence` | `NOT-DETERMINED` | VO may address the intermediary but equivalence remains unreviewed | Task 002 and obligation compatibility research | retain VO as Profile/Binding candidate | `OPEN-CANDIDATE-CORRESPONDENCE` | Q-03, Q-04 |
| R05 | Obligation/Coverage aspect | functional/state/timing and related classifications | v4.3 release; legacy-origin object | `classifies` | `CANDIDATE` | local classifications qualify views without becoming a universal Core level | Task 002 and coverage study | keep taxonomy out of Generic promotion | `QUALIFIED-ALIGNED` | Q-04, Q-07 |
| R06 | VerificationStrategy | Test-and-Analysis allocation | v4.3 release; legacy-origin object | `realizes` | `PARTIAL` | allocation covers a bounded strategy-decision subset | strategy criteria and rationale review | retain omitted environment/coverage/evidence decisions | `PARTIAL-BOUNDARY-RETAINED` | Q-03 |
| R07 | VerificationCase | VC | v4.3 release; legacy-origin object | `instantiates` | `CANDIDATE` | VC is a candidate case realization; Test Purpose equivalence is not presumed | Task 002 Test Purpose study | retain Test Purpose separately | `QUALIFIED-ALIGNED` | Q-04 |
| R08 | VerificationProcedure | procedure | v4.3 release; legacy-origin object | `instantiates` | `CANDIDATE` | executable steps may instantiate the procedure role | procedure/configuration review | separate reusable procedure from run configuration | `ALIGNED-AS-MAPPED` | Q-01 |
| R09 | Observation | packet trace/timestamp/log | v4.3 release; legacy-origin object | `instantiates` | `CANDIDATE` | captured facts are observations/raw records with provenance | evidence characterization rules | do not auto-promote trace/log to Evidence | `ALIGNED-AS-MAPPED` | Q-05 |
| R10 | Result | verdict | v4.3 release; legacy-origin object | `instantiates` | `CANDIDATE` | verdict is an evaluated Result, not Observation or Oracle | Oracle/Result review | preserve Observation, rule and Result separately | `ALIGNED-AS-MAPPED` | Q-05 |
| R11 | Oracle | discrete/robust timing rule | v4.3 release; legacy-origin object | `implements` | `CANDIDATE` | rule evaluates controlled Observations and produces a Result | ISO-G04 and Task 002 | version rule and parameters in Binding/Configuration | `QUALIFIED-ALIGNED` | Q-01, Q-04 |
| R12 | Evidence | characterized execution/analysis record | v4.3 release; legacy-origin object | `candidate-correspondence` | `NOT-DETERMINED` | raw records require identity, provenance, applicability, credibility and admission | Evidence admission/credibility study | manifest remains a provenance container | `OPEN-NO-EQUIVALENCE` | Q-02, Q-03, Q-05 |
| R13 | Argument | scoped assurance reasoning | v4.3 release; legacy-origin object | `realizes` | `PARTIAL` | bounded reasoning may support a scope; full equivalence is not shown | Claim/Argument boundary review | retain explicit inference and limitations | `PARTIAL-BOUNDARY-RETAINED` | Q-03, Q-05 |
| R14 | Claim | PR #9 CEI claim entry candidate | v4.3 release | `indexes` | `NOT-DETERMINED` | CEI navigates to a versioned Claim/Decision and is not Claim, Argument or Evidence Architecture | 15026-informed review | retain navigation-only semantics | `OPEN-INDEX-ONLY` | Q-03, Q-05, Q-07 |
| R15 | CompositeGate | RG/G gate package | v4.3 release | `specializes` | `NOT-DETERMINED` | decomposition and authority correspondence remain unresolved | CompositeGate compatibility review | preserve local gate states | `OPEN-SPECIALIZATION-CANDIDATE` | Q-03, Q-07 |
| R16 | Configuration | IUT/setup/procedure identity | v4.3 release; legacy-origin object | `instantiates` | `CANDIDATE` | legacy identity bundle may instantiate a bounded Configuration role | identity/version contract | keep legacy identity distinct from future Project Configuration | `QUALIFIED-LEGACY-CONFIGURATION` | Q-01, Q-03 |
| R17 | Anomaly/Change/Impact | Problem Closure plus CR/DD | v4.3 release; legacy-origin object | `candidate-correspondence` | `NOT-DETERMINED` | lifecycle/state/authority equivalence remains unknown | change/closure review | preserve legacy states and map transitions explicitly | `OPEN-CANDIDATE-CORRESPONDENCE` | Q-03, Q-05 |
| R18 | SufficiencyAssessment | PR #9 OSR/claim-review candidate | v4.3 release | `candidate-correspondence` | `NOT-DETERMINED` | OSR may contribute inputs but is not assumed equivalent | RQ4 and instance review | retain explicit reasoning/decision chain | `OPEN-CANDIDATE-CORRESPONDENCE` | Q-03, Q-05 |

## Instance-only additional rows

These seven rows remain `INSTANCE-ONLY-ADDITIONAL`. A real Framework role is a
review target only; no Generic correspondence or extension-point definition is
created.

| Local row | Row class | External review target | Local ARINC object | Source provenance | Primary relation | Mapping status | Boundary rationale | Open dependency | Third-handshake review | Qualification |
|---|---|---|---|---|---|---|---|---|---|---|
| A01 | `INSTANCE-ONLY-ADDITIONAL` | VerificationCase | Test Purpose | v4.3 release | `no-direct-correspondence` | `NOT-DETERMINED` | Test Purpose is not preassigned to VerificationCase | ISO/IEC 9646 Task 002 | `PROFILE-LOCAL; NO CASE EQUIVALENCE` | Q-04 |
| A02 | `INSTANCE-ONLY-ADDITIONAL` | Evidence | Execution Evidence Manifest | v4.3 release | `no-direct-correspondence` | `NOT-DETERMINED` | manifest is provenance, not admitted Evidence | Evidence characterization policy | `PROVENANCE CONTAINER; NO EVIDENCE EQUIVALENCE` | Q-02, Q-05 |
| A03 | `INSTANCE-ONLY-ADDITIONAL` | Configuration | Test Conformity Record | v4.3 release | `no-direct-correspondence` | `NOT-DETERMINED` | local control record is not authority conformity or Core Configuration | Configuration review | `PROJECT CONTROL; NO CORE CONFIGURATION EQUIVALENCE` | Q-01, Q-07 |
| A04 | `INSTANCE-ONLY-ADDITIONAL` | Argument | L0–L7 ARINC evidence view | v4.3 release | `no-direct-correspondence` | `NOT-DETERMINED` | composite Profile view spans several roles | Profile architecture review | `PROFILE VIEW; NO SINGLE CORE OBJECT` | Q-07, Q-08 |
| A05 | `INSTANCE-ONLY-ADDITIONAL` | SufficiencyAssessment | A0–A4 ARINC assurance states | v4.3 release | `no-direct-correspondence` | `NOT-DETERMINED` | local assurance taxonomy is not a Generic authority level | Profile/claim review | `PROFILE/PROJECT TAXONOMY; NO GENERIC AUTHORITY LEVEL` | Q-07, Q-08 |
| A06 | `INSTANCE-ONLY-ADDITIONAL` | SufficiencyAssessment | R0–R5 instance research maturity | v4.3 release | `no-direct-correspondence` | `NOT-DETERMINED` | research maturity is orthogonal to assurance/certification | research/claim review | `PROJECT RESEARCH STATE; ORTHOGONAL TO ASSURANCE` | Q-07, Q-08 |
| A07 | `INSTANCE-ONLY-ADDITIONAL` | Configuration | future Project Configuration `TMP-PC-ARINC615A-01` | v4.3 release | `no-direct-correspondence` | `NOT-DETERMINED` | no controlled values exist; no Configuration instance is established | actual controlled values | `PLACEHOLDER ONLY; CONFIGURATION NOT ESTABLISHED` | Q-01, Q-02 |

## Required semantic corrections retained

1. A PICS-like declaration controls applicability and therefore the applicable CRS/Basis Element population; it is not itself Verification Basis.
2. Test Purpose has no final Generic correspondence before ISO/IEC 9646 Task 002 clause study and independent review. It is not preassigned to VerificationCase.
3. Oracle is the evaluation rule/mechanism; Verdict is a Result.
4. Raw trace, manifest, timestamp or log is first an Observation, Raw Record or Provenance Container. Evidence role requires explicit characterization; PASS does not automatically establish Evidence, Objective Satisfaction or Compliance Claim.
5. CEI is a reviewer-facing index and is not automatically Argument, Claim or Evidence Architecture.
6. ARINC T0–T3, L0–L7, A0–A4, R0–R5 and RG/G are instance/Profile taxonomy candidates, not universal Candidate GVS Core levels.
7. PR #9 is merged and tagged as a GVS-bound migration baseline; this changes source authority but does not strengthen any row relation/status or establish empirical evaluation.

Any future mapping change requires immutable source/target identities, rationale,
dependency, migration impact and independent review. The overall third-handshake
candidate cannot convert a row to equivalence or close its research dependency.
