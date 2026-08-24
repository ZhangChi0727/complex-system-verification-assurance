---
title: ARINC 615A Temporary Object Mapping Register
status: working
version: 0.1
baseline: post-v0.2
owner: research
last_updated: 2026-08-25
dependencies:
  - cross_repository_instance_contract.md
  - instance_registry.md
  - ../01_normative_foundation/research_tasks/002_iso_iec_9646_series.md
  - ../02_verification_framework/generic_verification_suite_core.md
---

# ARINC 615A Temporary Object Mapping Register

## Control boundary

This register is a `temporary controlled mapping`, not a stable registry, equivalence claim or Framework Rule. Source baseline for active rows is external commit `0ce96f701159fd4156d5e5e9889360f53977a61b` / `RB-2026-001-v4.2.1`. Rows mentioning Draft PR #9 use head `53a98447bcfa862f082ce443d69115067d3ff2f1` and are marked **UNMERGED EXTERNAL CANDIDATE — NO ACTIVE SEMANTIC AUTHORITY**.

Current statuses are limited to `NOT-DETERMINED`, `CANDIDATE`, `PARTIAL`, `CONFLICT` and `OUT-OF-SCOPE`. No row has passed compatibility review.

## Mapping population

| Framework candidate/role | ARINC object | Source baseline | Relation | Mapping status | Rationale | Open dependency | Migration note | Review status |
|---|---|---|---|---|---|---|---|---|
| Applicability/Profile Declaration | PICS-like declaration | active v4.2.1 | `realizes` | `CANDIDATE` | declares capability/applicability and affects the applicable CRS population; it is not itself Verification Basis | ISO/IEC 9646 Task 002; profile review | retain declaration separately from basis items | pending |
| VerificationBasisElement | applicable CRS item | active v4.2.1 | `instantiates` | `CANDIDATE` | an applicable normative item may act as a typed basis element; population aggregation remains explicit | Task 002 and mapping review | preserve CRS locator and applicability provenance | pending |
| VerificationObligation | current ARINC requirement-obligation aspect | active v4.2.1 | `no-direct-correspondence` | `CONFLICT` | current structure does not expose a controlled object equivalent to the framework candidate | obligation identity/semantics review | do not retrofit a stable ID into the legacy baseline | pending |
| VerificationObligation | PR #9 Verification Objective | PR #9 / v4.3 candidate | `candidate-correspondence` | `NOT-DETERMINED` | candidate may address the missing intermediary but its semantics are unmerged and unreviewed | method merge plus instance migration/compatibility review | UNMERGED EXTERNAL CANDIDATE — NO ACTIVE SEMANTIC AUTHORITY | pending |
| Obligation/Coverage aspect | functional/state/timing and related classifications | active v4.2.1 | `classifies` | `CANDIDATE` | classification may qualify obligation/coverage views without becoming a universal Core level | Task 002 and coverage study | keep T0–T3/Profile taxonomy out of Generic promotion | pending |
| VerificationStrategy | Test-and-Analysis allocation | active v4.2.1 | `realizes` | `PARTIAL` | allocation covers only a bounded strategy decision subset | strategy criteria and rationale review | retain omitted environment/coverage/evidence decisions | pending |
| VerificationCase | VC | active v4.2.1 | `instantiates` | `CANDIDATE` | VC is a candidate case realization; Test Purpose equivalence is deliberately not presumed | Task 002 Test Purpose study | map only after locator-backed source study | pending |
| VerificationProcedure | procedure | active v4.2.1 | `instantiates` | `CANDIDATE` | executable steps may instantiate the procedure role | procedure/configuration review | separate reusable procedure from run configuration | pending |
| Observation | packet trace/timestamp/log | active v4.2.1 | `instantiates` | `CANDIDATE` | captured facts are observations/raw records with provenance | evidence characterization rules | do not auto-promote trace/log to Evidence | pending |
| Result | verdict | active v4.2.1 | `instantiates` | `CANDIDATE` | verdict is an evaluated result, not the rule that produced it | Oracle/result review | preserve rule inputs and result separately | pending |
| Oracle | discrete/robust timing rule | active v4.2.1 | `implements` | `CANDIDATE` | rule/mechanism evaluates observations against expected constraints | ISO-G04 and Task 002 | version the rule and concrete parameters in Binding/Configuration | pending |
| Evidence | characterized execution/analysis record | active v4.2.1 | `candidate-correspondence` | `NOT-DETERMINED` | raw records need identity, provenance, applicability and credibility characterization before Evidence role | Evidence admission/credibility study | manifests remain provenance containers, not automatic Evidence | pending |
| Argument | scoped assurance reasoning | active v4.2.1 | `realizes` | `PARTIAL` | some reasoning may support a scope but full assurance-argument equivalence is not shown | Claim/Argument boundary review | retain explicit inference and limitations | pending |
| Claim | PR #9 CEI claim entry candidate | PR #9 / v4.3 candidate | `indexes`; `candidate-correspondence` | `NOT-DETERMINED` | CEI is reviewer-facing index candidate and does not automatically equal Claim, Argument or Evidence Architecture | instance migration and 15026-informed review | UNMERGED EXTERNAL CANDIDATE — NO ACTIVE SEMANTIC AUTHORITY | pending |
| CompositeGate | RG/G gate package | PR #9 / v4.3 candidate | `specializes` | `NOT-DETERMINED` | gate package may specialize assessment/review/decision/state event, but decomposition and authority are unreviewed | CompositeGate compatibility review | UNMERGED EXTERNAL CANDIDATE — NO ACTIVE SEMANTIC AUTHORITY | pending |
| Configuration | IUT/setup/procedure identity | active v4.2.1 | `specializes` | `CANDIDATE` | instance configuration specializes the candidate configuration role | identity/version contract | separate Binding definitions from run values | pending |
| Anomaly/Change/Impact | Problem Closure plus CR/DD | active v4.2.1 | `candidate-correspondence` | `NOT-DETERMINED` | overlap may exist but lifecycle/state/authority equivalence is unknown | change/closure review | preserve legacy states and map transitions explicitly | pending |
| SufficiencyAssessment | PR #9 OSR/claim-review candidate | PR #9 / v4.3 candidate | `candidate-correspondence` | `NOT-DETERMINED` | review artefact may contribute to sufficiency reasoning but cannot be assumed equivalent | RQ4 semantics and instance review | UNMERGED EXTERNAL CANDIDATE — NO ACTIVE SEMANTIC AUTHORITY | pending |

## Required semantic corrections

1. A PICS-like declaration controls applicability and therefore the applicable CRS/Basis Element population; it is not itself Verification Basis.
2. Test Purpose has no final Generic correspondence before ISO/IEC 9646 Task 002 clause study and independent review. It is not preassigned to VerificationCase.
3. Oracle is the evaluation rule/mechanism; Verdict is a Result.
4. Raw trace, manifest, timestamp or log is first an Observation, Raw Record or Provenance Container. Evidence role requires explicit characterization; PASS does not automatically establish Evidence, Objective Satisfaction or Compliance Claim.
5. PR #9 CEI is a reviewer-facing index candidate and is not automatically Argument, Claim or Evidence Architecture.
6. ARINC T0–T3, A0–A4, R0–R5 and RG/G are instance/Profile taxonomy candidates, not universal Candidate GVS Core levels.
7. Every PR #9-derived row remains **UNMERGED EXTERNAL CANDIDATE — NO ACTIVE SEMANTIC AUTHORITY** until a later reviewed migration and compatibility disposition.

Any future mapping change requires immutable source/target identities, rationale, dependency, migration impact and independent review. No row may move to a reviewed compatibility status inside this PR.
