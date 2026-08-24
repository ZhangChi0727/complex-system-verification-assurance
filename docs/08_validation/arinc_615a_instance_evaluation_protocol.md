---
title: ARINC 615A Instance Evaluation Protocol
status: working
version: 0.1
baseline: post-v0.2
owner: research
last_updated: 2026-08-25
dependencies:
  - cross_repository_instance_contract.md
  - instance_registry.md
  - arinc_615a_object_mapping_register.md
  - ../02_verification_framework/generic_verification_suite_core.md
  - ../00_overview/research_questions.md
---

# ARINC 615A Instance Evaluation Protocol

## Purpose and execution boundary

This is the method-repository-owned **working evaluation protocol** for the ARINC 615A legacy instance. A later, separately governed instance change may execute it. This PR does not execute the protocol, approve a migration, establish compatibility or validate the Candidate GVS Core.

The evaluation binds immutable method/instance commits, active baseline, Profile/Binding/Configuration versions, mapping-register version and evidence manifest identity before any conclusion is admitted.

## Mandatory evaluation questions

1. When the product under test changes, which Core artefacts remain unchanged?
2. Which changes belong only to Project Configuration?
3. Which changes belong only to Product Binding?
4. Does an ARINC protocol or Profile revision contaminate Candidate GVS Core semantics?
5. Can generic Oracle responsibility be separated from ARINC-specific evaluation logic?
6. Can one Verification Case/Procedure contract execute through different Bindings, or does it hide product assumptions?
7. Can packet traces, timestamps, logs, results, review records and analysis outputs be accommodated without changing Core semantics?
8. Can impact be localized when Core, Profile, Binding or Configuration changes separately?
9. Does the instance repository reverse-define any Generic object, state or authority?
10. Is the Candidate GVS Core overconstrained, missing an extension point or carrying aviation/protocol assumptions?
11. What Profile/Binding development cost, reuse rate, change isolation and review effort are observed?
12. Is each finding an instance defect, binding defect, profile ambiguity, core insufficiency, core overconstraint, evaluation defect or candidate generalization?

## Evaluation matrix

Each row must produce a finding record even when the disposition is “no issue observed”. Allowed conclusions are bounded observations for this instance, not universal validation.

| Dimension | Research question | Required input | Acceptable evidence | Falsification / failure condition | Allowed conclusion | Prohibited claim | Finding output | Disposition owner |
|---|---|---|---|---|---|---|---|---|
| completeness | Does the four-layer contract represent every required ARINC verification responsibility without forcing instance detail into Core? | frozen Core/Profile/Binding/Configuration inventory and mapping | reconciled object/responsibility coverage with explicit gaps | required responsibility has no layer/extension point or is hidden in implementation | complete/incomplete for this bounded instance scope | framework universally complete | gap/finding with missing role and proposed layer | method architecture review |
| traceability | Can basis/applicability, obligation, case, procedure, observation, result and reviewed evidence be traversed with immutable provenance? | mapping rows, identifiers, manifest | bidirectional trace report with unresolved links | silent link, mutable target or provenance break | traceable/qualified for sampled instance population | universal traceability solved | trace defect or qualification | instance configuration owner plus method reviewer |
| repeatability | Can another controlled run reproduce inputs, rule versions and result production? | Configuration, Binding, tool/rule versions, run record | repeated run package and explained variance | required state/version unavailable or result cannot be reproduced/explained | repeatable/qualified for specified configuration | deterministic proof for all products | repeatability finding | instance execution owner |
| reviewability | Can an independent reviewer reconstruct decisions without hidden chat/tool state? | case/procedure, Oracle, result, evidence characterization, review log | reviewer walkthrough and issue log | conclusion depends on undocumented inference or inaccessible identity | reviewable/qualified in this review | authority acceptance | reviewability finding | independent instance reviewer |
| change-impact localization | Are Core/Profile/Binding/Configuration changes separately identifiable with bounded affected artefacts? | controlled change scenarios and dependency graph | impact reports compared with known seeded changes | unrelated layers change or affected artefacts are missed | localization performance for tested scenarios | complete universal impact algorithm | missed/false impact finding | method and instance change owners |
| reuse/change isolation | What remains reusable across product/configuration changes and at what adaptation cost? | paired product/configuration scenarios, effort log | unchanged/changed artefact counts, rationale and review effort | Core must change for product-only variation or reused artefact hides assumptions | measured reuse and isolation for scenarios | general cross-domain reusability | reuse/overconstraint finding | cross-instance evaluation owner |
| evidence provenance/integrity | Can raw records be distinguished from characterized Evidence and protected through lineage? | traces/logs/manifests/results/reviews and hashes | provenance chain, access boundary and characterization rationale | raw artefact is promoted automatically or lineage/configuration is missing | evidence role admissible/qualified for item | PASS or manifest proves satisfaction/compliance | evidence-admission finding | evidence governance reviewer |
| interface conformance | Does a Binding satisfy semantic inputs/outputs/invariants/failure rules independently of implementation technology? | semantic contract, binding specification and conformance record | contract checklist and negative/failure-path tests | implementation-specific API silently replaces semantic obligation | conforms/qualified/incompatible for reviewed binding | API/schema is the Core definition | binding defect or qualification | compatibility reviewer |
| hidden-assumption detection | Are protocol, aviation, tool or product assumptions present in Core/package contracts? | assumption inventory and cross-layer review | explicit assumptions with owner/status and counterexample scenarios | unowned product/profile assumption appears as Generic invariant | assumption found/not found in reviewed scope | assumption-free framework | core overconstraint/profile ambiguity | method research owner |
| migration effort | What effort and risk are required to move legacy v4.2.1 toward a version-bound contract? | baseline diff, mapping, issue/effort/review logs | hours/changes/findings by layer and rollback plan | migration cannot preserve history or impact is not attributable | bounded migration cost and residual risk | migration proves compatibility or scalability | migration finding | instance migration owner and method governance reviewer |

## Finding record

Each output contains finding ID, classification, immutable instance commit/baseline, Candidate GVS Core definition context, Profile/Binding/Configuration identities, mapping row/version, evidence manifest ID, observed condition, limitation, counterevidence, privacy/copyright boundary, proposed disposition and owner. Findings follow the cross-repository feedback chain and cannot directly modify canonical definitions.

## RQ8 and generalization boundary

ARINC is the first instance and mainly exercises the design–execution lower chain plus layer isolation. It may support, qualify or falsify candidate claims, but cannot alone establish completeness, scalability, reusability, product independence or interface generality. RQ8 remains `Open` until controlled UAV FMS and LLM service evaluations and cross-instance synthesis are independently reviewed.
