---
title: SAE ARP4761A Standards Research Note
status: reviewed
version: 0.2
baseline: v0.2
owner: research
last_updated: 2026-08-19
source:
  standard: SAE ARP4761A
  revision: A
  issued: 1996-12
  revised: 2023-12
  access: local licensed source; not committed
---

# SAE ARP4761A Research Note

## 1. Source, scope and classification

SAE ARP4761A, *Guidelines for Conducting the Safety Assessment Process on Civil Aircraft, Systems, and Equipment*, is an SAE Aerospace Recommended Practice revised in December 2023. This study uses the licensed local publication only; the PDF, extracted text, screenshots, figures and Appendix Q examples are not repository artefacts.

ARP4761A supplies civil-aircraft safety-assessment guidance that can support certification programmes and organizational practices. It is not itself a regulation, does not define the whole certification basis, and allows other effective processes (Section 1). Its intended relationship with ARP4754B, DO-178C, DO-254, DO-297 and applicable regulatory/advisory material is contextual (1.3).

Classification labels used below are `SAFETY-ASSESSMENT GUIDANCE`, `DEFINITION`, `INTERPRETATION`, `FRAMEWORK IMPLICATION`, `AVIATION PROFILE RULE` and `RESEARCH PROPOSAL`. A recommendation is not silently promoted to a universal requirement.

## 2. Principal conclusion

The principal Failure Condition path and the additional Safety Process origins are:

```text
Failure Condition
  → classification
  → Safety Objective
                    ┐
Safety-process Constraint
Independence Principle
Controlled Assumption
Applicable architecture / analysis result
                    ├→ Safety Requirement
                    └→ Assurance / Independence Constraint
                              ↓
                 Verification / Assurance Obligation
  → Development Verification Evidence + Safety Analysis Evidence
  → SSA / ASA Safety Assessment Evidence
```

The diagram is a multi-source provenance model, not an assertion that every Safety Requirement passes through one linear chain. A classification informs objectives and analysis/development-assurance rigor, but does not directly prescribe a test count or one verification method. Within this aviation profile, a Verification/Assurance Obligation still requires a traceable Requirement、Constraint or other explicitly controlled typed Basis relation；it is not generated automatically from a Failure Condition. Safety-assessment results interact with development verification; they do not replace it.

## 3. Core concepts and definitions

| Concept | ARP4761A position | Framework interpretation | Locator |
|---|---|---|---|
| Failure Condition | Aircraft/occupant condition caused or contributed to by failures or errors in context | Upstream safety-analysis object; not a Verification Case | 2.2 |
| Failure Mode / Failure Effect | A specific way an object can fail / the consequence of that mode | Inputs and causal/effect relations, not synonyms for Failure Condition | 2.2 |
| Failure Condition Classification | Severity classification is selected using applicable regulatory/advisory criteria | Safety-criticality input; not a Verification Level | 2.2; 3.8 |
| Safety / Risk | Safety is freedom from unacceptable risk; risk combines predicted frequency and severity | Context for acceptability; no single framework metric follows | 2.2 |
| Safety Objective | Criterion associated with a Failure Condition that defines acceptable safety performance | Candidate Verification Basis input | 2.2; 3.2; Appendix A |
| Safety Requirement | Requirement necessary to achieve a Safety Objective or satisfy a constraint established by the Safety Process | `Requirement` subtype/classification with one or more typed safety-provenance relations | 2.2; 3.3; 3.5; D.4.3 |
| Assurance | Planned/systematic actions that provide confidence/evidence | Broader assurance relation; do not collapse into testing | 2.2 |
| FDAL / IDAL | Rigor applied respectively to function and item development-assurance tasks | Aviation `Assurance Constraint`, not Verification Level | 2.2; 3.9; Appendix P |
| Independence | Functional, item-development, physical and process forms | Typed constraint/object with claim and substantiation | 2.2 |
| Assumption | Premise offered without proof and managed until confirmed/corrected | Candidate lifecycle object and possible obligation source | 2.2; A.6; D.4.3.2 |

## 4. Safety-assessment process and dual view

Section 3 describes AFHA, PASA, SFHA, PSSA, SSA and ASA as principal, interacting processes. They are generally initiated in that order, but are iterative and may overlap; a change to design or one assessment can require reassessment elsewhere (3.1.1). Safety-analysis methods support these assessments and can feed higher-level assessments (3.1.2; Section 4).

The framework therefore keeps two related process views:

```text
Verification Assurance Process View (V0–V12)
                    ↕ typed inputs, obligations and evidence
Safety Assessment Process View (AFHA–PASA–SFHA–PSSA–SSA–ASA)
```

The safety view does not replace or renumber V0–V12.

## 5. AFHA

AFHA identifies and classifies aircraft-level Failure Conditions for aircraft functions. The classification establishes the basis for aircraft Safety Objectives. It records classification rationale and assumptions concerning aircraft/crew mitigations and passes Failure Conditions, classifications and assumptions to PASA (3.2; Appendix A). Assumptions are captured and later confirmed or corrected; an incorrect assumption can cause design or AFHA revision (A.6).

## 6. PASA

PASA evaluates a proposed aircraft architecture against AFHA Failure Conditions and Safety Objectives. It develops aircraft-level safety requirements, considers common causes and independence, assigns FDAL, and allocates relevant information to system-level PSSAs (3.3; Appendix B). It is an architecture-sensitive derivation/evaluation process, not implementation verification.

## 7. SFHA

SFHA identifies and classifies system-function Failure Conditions, establishes system Safety Objectives, and exchanges new cross-level Failure Conditions with AFHA and other systems. It records assumptions and supplies the starting safety information for PSSA (3.4; Appendix C).

## 8. PSSA

PSSA evaluates a proposed system architecture against PASA allocations and SFHA Safety Objectives. It derives and allocates proposed Safety Requirements from applicable Safety Objectives and Safety Process constraints, including independence principles, quantitative and architecture-analysis results, monitoring/detection, protection, redundancy/reconfiguration and required-test concerns, and establishes FDAL/IDAL information (2.2; 3.5; D.4.3; Appendix P).

Each proposed Safety Requirement should retain rationale, source analysis and allocation. External or uncontrolled premises remain assumptions; matters under organizational control should normally be converted to proposed requirements (D.4.3.1–D.4.3.2). This provenance is the bridge from safety analysis to development and verification obligations.

## 9. PSSA completion

PSSA completion is a structured evaluation of heterogeneous outputs: qualitative/quantitative results, DAL rationale, independence and safety requirements, traceability to source assessments, lower-level assumptions, and safety-impact-derived requirements (D.5). No single probability, DAL, trace count or universal percentage is sufficient. Completion supplies a proposed safety baseline and inputs to SSA; it is domain-specific support for V11 rather than generic sufficiency closure.

## 10. SSA

SSA evaluates the implemented system and confirms Safety Objectives and Safety Requirements. It draws on ARP4754B development verification to show requirements and required FDAL/IDAL development objectives were satisfied, and on safety methods such as FTA, CMA, ZSA and PRA for quantitative, independence and installation concerns (3.6; E.3–E.5).

SSA is neither a Verification Method nor the generic Verification Process. It is an aviation Safety Assurance Assessment that aggregates development verification evidence and safety-analysis evidence. Unsatisfied requirements, invalid assumptions and safety-impacting problem reports feed back to development and PSSA; changes may repeat the PSSA/SSA cycle (E.4).

## 11. ASA

ASA evaluates the certification-baseline aircraft implementation and integrates applicable SSAs and aircraft-level safety analyses (3.7; Appendix F). It checks that AFHA/PASA-derived requirements, qualitative/quantitative objectives, architecture, dependencies, FDAL/IDAL application, independence, assumptions and open/deferred problems are acceptably addressed (F.4).

ASA is an aircraft-level assurance aggregation. Mapping its conclusion to a framework `Claim` is an interpretation, not an ARP4761A-native claim ontology. Its outputs include referenced development/safety evidence, status of verification activities and problem reports, and aircraft-level analysis results (F.5).

## 12. Depth of analysis

The depth of safety analysis is generally driven by Failure Condition Classification and also by system/design characteristics, available information, organizational practice and applicable advisory material (3.8). ARP4761A distinguishes appraisal, verification analysis and qualitative/quantitative evaluation, but does not define a universal formula from classification to method, case count or test count.

## 13. FDAL and IDAL

FDAL modulates system/function development-assurance rigor under ARP4754B; IDAL modulates software/electronic-hardware item development rigor under DO-178C/DO-254 (P.1). The assignment uses FHA Failure Conditions/classifications, function descriptions, proposed architecture and PASA/PSSA safety data (P.2).

Initial top-level FDAL mapping is A/B/C/D/E for Catastrophic/Hazardous/Major/Minor/No Safety Effect respectively, with the highest applicable assignment retained for a function. Architectural alternatives may use Functional Failure Sets and substantiated independence. IDAL follows FDAL and item allocation; item-development and functional independence claims are evaluated, with feedback/rework where independence cannot be substantiated (P.3–P.4). The assignment is reconsidered after FHA revision, architecture change, PSSA reassessment or changed assumptions (P.1).

FDAL/IDAL are not safety classifications, verification levels, methods, criticality labels or automatic certification credit.

## 14. Independence

ARP4761A distinguishes four source-defined types (2.2):

- `Functional Independence` — a characteristic that reduces the likelihood of common development errors by using different functions;
- `Item Development Independence` — a characteristic that reduces the likelihood of common development errors by using different item designs;
- `Physical Independence` — a characteristic that reduces common failures caused by physical failure, damage or environmental effects through separation or segregation;
- `Process Independence` — a practice using separation of responsibilities so someone other than the activity performer provides objective evaluation.

These definitions are distinct from substantiation criteria. Appendix P evaluates claimed functional/item-development independence in the FDAL/IDAL assignment context by examining common sources of error across requirement sets, designs and development processes; CMA or equivalent techniques may substantiate those claims (P.3.2.2; P.3.2.4; P.4). Physical independence and particular-risk concerns use the applicable ZSA/PRA/CMA evidence. The analysis criterion must not silently replace the 2.2 definition.

An `Independence Principle` is an intended implementation feature whose independence is judged necessary. It is not the same as a verified Independence Requirement. The principle is refined into requirements/constraints and must be substantiated through relevant development and analyses; CMA, ZSA and PRA address different common-cause/physical aspects (2.2; 3.1.2; Appendices J–M, P).

## 15. Assumption lifecycle

The aviation-profile lifecycle is:

```text
capture → identify owner/source → propagate/allocate
→ convert controllable premise to Requirement where appropriate
→ define confirmation obligation → confirm or correct
→ assess impact → revise design/assessment/evidence after change
```

Assumptions may affect Failure Condition effects/classification, architecture, independence, exposure times, crew actions, interfaces and DAL assignments (A.6; D.4.3.2). Unconfirmed assumptions limit the validity of safety conclusions. Five-source consolidation promotes `Assumption` to a Generic Extension Point whose conceptual semantics can represent statement/context/affected objects and applicable validity、confirmation、ownership information；it does not freeze mandatory fields or states. `Assumption Obligation` and `Assumption Confirmation` remain aviation lifecycle specializations rather than universal states.

## 16. Safety-analysis method taxonomy

ARP4761A includes FTA, DD, MA, MBSA, FMEA/FMES, CEA, ZSA, PRA and CMA (3.1.2; Section 4; Appendices G–O). These are `Safety Analysis Method` instances, not aliases of the framework `Verification Method` taxonomy. Their controlled results can constitute or support Safety Analysis Evidence and may be evaluated alongside Development Verification Evidence.

## 17. FTA, DD, MA and MBSA

FTA, DD and MA are top-down analysis techniques; MBSA represents architecture, function and dysfunctional behavior in a Failure Propagation Model and generates safety-focused outputs such as failure sequences, cut sets and probabilities (4.1–4.1.1; Appendices G–I, N). Selection depends on purpose, data and system context. Their outputs are compared with objectives/requirements within the wider safety assessment.

The study also preserves the development-error/random-failure boundary. Development errors are systematic assurance concerns primarily controlled by Development Assurance rigor and independent activities; random failures are commonly evaluated through qualitative/quantitative safety analyses using failure modes, rates, exposure and combinations. A probabilistic result cannot substitute for Development Assurance, and a DAL cannot substitute for random-failure analysis (4.1.1.1; Appendix P).

## 18. FMEA and FMES

FMEA/FMES provide bottom-up failure-mode/effect information and can supply events/rates or summaries to higher-level safety analyses (4.2; Appendix J). They support evidence about failure behavior; they do not by themselves establish overall Safety Objective satisfaction.

## 19. CMA, ZSA and PRA

CMA examines common-mode/common-source concerns and can substantiate functional/item-development independence; ZSA addresses zonal installation interactions; PRA addresses defined external/particular risks (3.1.2; F.3.9; Appendices K–M). Applicability is contextual—CMA is not asserted as mandatory for every system.

## 20. MBSA / MBSE boundary

`MBSA ≠ MBSE`. Appendix N is technology-neutral, supports text-based or model-based development, and does not require SysML or an MBSE process (N.1). The Failure Propagation Model and failure-condition logic require verification against the real architecture/behavior and non-regression after modification (N.3.6). Model/tool baselines, reproducibility information, failure modes, results, validation evidence and limitations are expected documentation (N.5).

MBSA can be studied later as one instance of a Model-Based Safety Assurance profile, but not as the definition of MBSE.

## 21. Safety evidence, coverage and sufficiency

Candidate evidence taxonomy:

- `Development Verification Evidence` — requirement/implementation and applicable development-assurance results;
- `Safety Analysis Evidence` — controlled outputs of applicable analysis methods;
- `Safety Assessment Evidence` — the traceable aggregation and evaluation produced by PSSA/SSA/ASA.

These categories can overlap in provenance but are not interchangeable. Evidence must retain configuration, applicability, assumptions, method/model validity, problem status and trace links.

Candidate aviation coverage dimensions are Failure Condition, Safety Objective, Safety Requirement, Assumption and Independence Requirement coverage. ARP4761A supports checking these populations but does not prescribe one universal coverage percentage. Safety sufficiency is the reasoned assessment of heterogeneous evidence against applicable objectives/requirements and limitations, not a single metric.

## 22. Change and safety reassessment

Design, architecture, FHA, safety requirement, independence, problem-report or assumption changes can invalidate prior safety results and trigger reassessment (3.1.1; A.6; D.5–D.6; E.4; P.1). Aviation V10 therefore adds:

```text
change/signal
→ safety impact analysis
→ affected FC/objective/requirement/assumption/independence identification
→ FDAL/IDAL reassessment where applicable
→ prior safety-evidence validity assessment
→ selected development re-verification + safety re-analysis/reassessment
→ updated evidence and closure inputs
```

This specializes V10 without changing its ID or defining a universal selection algorithm.

## 23. Legacy / reuse

Prior analysis or DAL assignments are reusable only after applicability assessment. Appendix P.5 requires attention to function/Failure Condition/classification similarity, architecture, independence, operating context, assumptions and modification impact; prior FDAL/IDAL values are starting information rather than automatic credit. Reuse preserves the existing `Result/Data → may constitute or support Evidence` model and does not introduce binary conversion.

## 24. Safety Assessment completion

Section 3.1.1 states the Safety Assessment Process is complete when applicable SSA/ASA results show Safety Objectives are satisfied and Safety Requirements are met, while permitting other effective means. Appendix F adds aircraft-level checks across assumptions, open/deferred problems, architecture, DAL application and independence.

This is an `AVIATION PROFILE RULE` and an input to V12. It is not equivalent to V12, which remains a framework composite of assurance assessment, optional review, authority decision, baseline/configuration event and re-entry semantics.

Open or deferred problem reports remain explicit completion inputs: their safety consequences and acceptability must be evaluated, rather than treating an open status as either automatic failure or automatic acceptance (E.4; F.4–F.5).

## 25. Relationship to the Verification Assurance Framework

- Safety Objective may contribute to `Verification Basis`, but is not a procedure or case.
- Failure Condition is an upstream source object; classification establishes the basis for Safety Objectives, while Safety Requirements can also originate from Safety Process constraints, Independence Principles, controlled assumptions and applicable architecture/analysis results.
- Safety Requirement should be represented as a `Requirement` subtype/classification with one or more explicit, typed provenance relations.
- Safety analysis can lead to a `Verification Obligation` only after the relevant objective/analysis result is formalized through a traceable Requirement、Constraint or other explicitly controlled typed Basis relation；a Failure Condition is never a direct shortcut.
- FDAL/IDAL and independence are aviation Assurance Constraints referenced by strategy, not flattened strategy scalars.
- SSA/ASA aggregate multiple evidence sources and contribute to V11/V12 decisions without replacing generic verification.

## 26. V0–V12 reassessment

| Element | ARP4761A aviation-profile effect |
|---|---|
| V0–V3 | Add applicable Safety Objectives/Requirements, assumptions, DAL and independence constraints to planning/basis/strategy |
| V4–V5 | Derive cases/procedures only from explicit obligations; safety methods remain a separate taxonomy |
| V6 | Safety-analysis/model/configuration readiness can be an input; no new universal gate |
| V7–V9 | Execute/evaluate applicable development verification and safety analyses; manage safety-impacting problems |
| V10 | Add explicit Safety Reassessment and assumption/FDAL/IDAL/evidence-validity subflow |
| V11 | Add aviation safety coverage and heterogeneous safety-evidence sufficiency assessment |
| V12 | Accept SSA/ASA completion status as aviation closure input; retain composite decision semantics |

## 27. ARP4754B cross-standard comparison

| Concern | ARP4754B | ARP4761A | Framework consequence |
|---|---|---|---|
| Development Assurance | Defines aircraft/system development framework | Supplies safety-driven rigor source/context | Connect, do not merge processes |
| FDAL / IDAL | Principles, objectives and interfaces | Assignment/reassessment process | Split responsibility with provenance |
| Safety Requirements | Captures, validates and implements in development | Derives from safety assessments | Preserve origin/allocation/validation links |
| Independence | Objective/process independence and PA independence | Functional, item-development, physical, process | Typed taxonomy; do not conflate |
| Verification | Implementation meets validated requirements | Confirms safety objectives/requirements through development and safety evidence | Evidence interaction, not synonymy |
| Change | Modification impact and prior-evidence credit | Safety reassessment and assumption/DAL revalidation | Unified V10 orchestration |
| Closure | Development verification data/summaries and problem status | SSA/ASA completion assessment | Composite V12 inputs |
| Evidence | Verification Data may support substantiation | Safety-analysis and assessment evidence | Multi-source assurance architecture |

## 28. Standards map update

ARP4761A directly strengthens the aviation-profile map for safety-derived rigor, typed independence, safety-analysis outputs, assumption management, change reassessment, safety coverage/sufficiency and SSA/ASA completion. It does not close generic rules for verification independence, coverage percentages, sufficiency formulas, universal gates or certification authority.

## 29. Gap matrix update

The study supports six distinct aviation-profile gaps: safety-to-verification obligation derivation (`SAF-G01`), assumption lifecycle (`SAF-G02`), multi-type independence (`SAF-G03`), multi-source safety evidence aggregation (`SAF-G04`), safety sufficiency reasoning (`SAF-G05`) and synchronization of change/reassessment (`SAF-G06`). Existing ISO/ARP gaps remain generic or partially supported rather than being falsely closed.

## 30. Candidate information model

Candidate aviation entities/relations:

```text
FailureCondition -classifiedAs→ FailureConditionClassification
FailureCondition -establishesBasisFor→ SafetyObjective
SafetyRequirementOrigin {
  SafetyObjective,
  SafetyProcessConstraint,
  IndependencePrinciple,
  ControlledAssumption,
  ArchitectureOrAnalysisResult
} -derives→ SafetyRequirement
SafetyRequirement -subtypeOf→ Requirement
SafetyRequirement | AssuranceConstraint -derives→ VerificationOrAssuranceObligation
AssuranceConstraint {FDAL, IDAL, IndependenceRequirement, SafetyProcessConstraint}
Assumption -creates→ AssumptionObligation -closedBy→ AssumptionConfirmation
SafetyAnalysisResult -maySupport→ SafetyAnalysisEvidence
SSA/ASA -aggregates→ {DevelopmentVerificationEvidence, SafetyAnalysisEvidence}
```

Five-source consolidation resolves generic promotion/classification but not complete cardinalities or lifecycle states. Stable generic/profile relations are maintained in `docs/04_information_model/README.md`.

## 31. Primary research questions R4761-Q01–Q15

| ID | Answer |
|---|---|
| R4761-Q01 | AFHA/SFHA identify a Failure Condition, assess effects and select a classification; the classification establishes the basis for the corresponding Safety Objective. |
| R4761-Q02 | PASA/PSSA evaluate proposed architecture and derive allocated Safety Requirements from applicable Safety Objectives or other Safety Process constraints, including independence, quantitative, architecture and assumption-derived sources. |
| R4761-Q03 | Classification is a principal depth/rigor driver, but design characteristics, information and advisory material also matter; it does not prescribe test count. |
| R4761-Q04 | FC/classification drives initial rigor; architecture and substantiated independence can alter permitted allocations; PSSA assigns/reassesses FDAL/IDAL across functions/items. |
| R4761-Q05 | It adds safety-derived objectives, requirements, assumptions, DAL/independence constraints and analysis evidence to the aviation Verification Strategy/rigor context. |
| R4761-Q06 | Model Safety Requirement as a Requirement subtype/classification with typed, potentially multi-source derivation and allocation provenance. |
| R4761-Q07 | Independence Principle is an intended architecture feature; Process Independence is one independence type concerning development activities/roles. |
| R4761-Q08 | PSSA traces AFHA/PASA/SFHA inputs through architecture analyses to proposed allocated requirements with rationale and source-analysis links. |
| R4761-Q09 | ARP4754B verifies implementation against validated requirements; SSA/ASA evaluate safety satisfaction using those results plus safety-analysis evidence. |
| R4761-Q10 | Controlled results can constitute/support Safety Analysis Evidence; their role depends on configuration, model/method validity, assumptions and claim applicability. |
| R4761-Q11 | Capture, own, propagate, convert when controllable, create confirmation obligations, record confirmations and reassess conclusions after correction/change. |
| R4761-Q12 | Yes, as aviation-specific closure input; no, it is not V12 itself. |
| R4761-Q13 | V10 adds safety-impact scoping, FC/objective/requirement/assumption/DAL impact, prior-evidence validity, selected re-analysis/re-verification and updated assessment. |
| R4761-Q14 | Treat FDAL/IDAL as Assurance Constraints referenced by strategy, with source/assignment provenance—not as a generic scalar Verification Level. |
| R4761-Q15 | Safety-derived rigor belongs to the Aviation Profile; the generic core only supplies extension points and traceable constraint semantics. |

## 32. Final framework questions and open questions

| # | Decision / current answer |
|---|---|
| 1 | Yes: Safety Requirement is a `Requirement` subtype/classification. |
| 2 | Yes: Safety Objective may be a Verification Basis input. |
| 3 | Indirectly: a Failure Condition participates in a traceable derivation; it is not itself the obligation. |
| 4 | FDAL/IDAL are aviation Assurance Constraints referenced by strategy. |
| 5 | Yes: independence needs typed objects/relations and substantiation state. |
| 6 | Keep `Safety Analysis Method` distinct from `Verification Method`; relate their outputs at evidence/assessment level. |
| 7 | SSA can be modeled as an aviation specialization/profile of V11-style assurance assessment, not as V11 identity. |
| 8 | Yes: ASA is aircraft-level safety assurance aggregation; `Claim` is a framework interpretation. |
| 9 | Completion supplies aviation-specific V12 criteria/evidence inputs, not the V12 decision itself. |
| 10 | Candidate only; promote `Assumption` to generic core after cross-standard consistency review. |
| 11 | Yes: add an explicit aviation Safety Reassessment subflow to V10. |
| 12 | Yes as an Aviation Profile coverage extension; generic taxonomy remains open. |
| 13 | They are distinct, composable evidence classes; SSA/ASA evaluate both. |
| 14 | Candidate `Safety Satisfaction Claim` types are useful, but ARP4761A does not prescribe the framework claim ontology. |
| 15 | Place all safety-specific objects/rules behind typed Aviation Profile extensions with source provenance; do not back-propagate them into generic conformance. |

Open questions for the cross-standard review are: generic assumption semantics; evidence-category overlap/cardinality; independence constraint states; V11/V12 decision authority; and compatibility with DO-178C/DO-254 objectives.

## 33. Final conclusions

ARP4761A closes the first safety-assurance research slice and connects ARP4754B development assurance to safety-derived rigor and multi-source evidence. The five-source Cross-Standard Consistency & Gap Review subsequently froze this source as the civil-aviation Safety Assessment/Safety Assurance profile, while retaining generic/profile boundaries and open schema/criteria gaps. The next normative priority is ISO/IEC/IEEE 15289；item-level standards are not started automatically.
