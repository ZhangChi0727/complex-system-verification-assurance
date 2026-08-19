---
title: Five-Source Cross-Standard Consistency & Gap Review
status: reviewed
version: 0.3
baseline: v0.2
owner: research
last_updated: 2026-08-19
dependencies:
  - ../standard_notes/iso_15288.md
  - ../standard_notes/iso_24748_1.md
  - ../standard_notes/iso_24748_2_targeted_review.md
  - ../standard_notes/sae_arp4754b.md
  - ../standard_notes/sae_arp4761a.md
  - ../standards_map.md
  - ../normative_gap_matrix.md
---

# Five-Source Cross-Standard Consistency & Gap Review

## 1. Purpose and source set

本报告把五个已经分别研究并完成内部/外部非正式评审的来源整合为一个可审计的 normative architecture：

- ISO/IEC/IEEE 15288:2023；
- ISO/IEC/IEEE 24748-1:2024；
- ISO/IEC/IEEE 24748-2:2024；
- SAE ARP4754B；
- SAE ARP4761A。

本轮不引入第六个主要标准，不把五份标准改写为一个“平均标准”，也不把民机 assurance rules 反向推广为所有复杂系统规则。结论使用以下分类：`GENERIC CORE`、`GENERIC EXTENSION POINT`、`AVIATION PROFILE`、`SUPPORTING GUIDANCE`、`RESEARCH PROPOSAL`、`OPEN GAP`、`CONTEXTUAL SEMANTIC DIFFERENCE`。

## 2. Source roles

| Source | Consolidated role | Strength boundary | Decision |
|---|---|---|---|
| ISO 15288 | Generic lifecycle/process、V&V 与 assurance foundation | Clause 6/Annex A 的 conformance 边界；NOTE/其他资料性内容不升级为 requirement | FROZEN |
| ISO 24748-1 | Lifecycle management、stage/gate、process application 与 process-view guidance | guidance；Annex D/F 等资料性内容不制造新的源标准任务或固定评审 | FROZEN |
| ISO 24748-2 | ISO 15288 application guidance，特别是 strategy integration、repeated application 与 enabling systems | `Reviewed Supporting Source`；不增加 ISO 15288 requirement、不改变 V0–V12 ontology | FROZEN |
| ARP4754B | Civil-aircraft Development Assurance profile | SAE recommended practice；certification applicability/credit 仍需与 authority 协调 | FROZEN |
| ARP4761A | Civil-aircraft Safety Assessment / Safety Assurance profile | SAE recommended practice；Safety Assessment 不替代 generic Verification | FROZEN |

未发现 source-role conflict。五源形成“generic foundation + supporting application guidance + civil-aviation specialization”，而不是一条权威性排序链。

## 3. Consolidation method

本轮按 framework concern 横向比较，而非逐标准复述。每个判断依次记录：

```text
source semantics and locator
  → abstraction/object/context comparison
  → generic/profile/proposal classification
  → relation and information-model consequence
  → residual gap
```

`Direct` 只表示来源直接定义或要求相关对象/活动；`Guidance` 表示 application/lifecycle guidance；`Profile` 表示航空 recommended-practice semantics；`Framework-defined` 表示由多源共同约束但名称或组合结构并非标准原生词。Framework-defined 对象可以进入 conceptual baseline，但必须保留这一 provenance，不能重标为标准要求。

## 4. Generic Core vs Aviation Profile

| Concept | Generic Core / extension point | Civil Aviation profile | Decision |
|---|---|---|---|
| Verification | specified requirement/characteristic 的客观证据与异常处理 | Implementation Verification：implementation 满足 validated requirements | Generic definition + contextual specialization |
| Validation | intended use/application 与 operational context | Requirement Validation：requirements correct and complete | 两种 object level 并存，不互相覆盖 |
| Verification Strategy | obligation、scope、method、criterion、environment、configuration 与 evidence needs 的选择和理由 | FDAL-dependent objectives、independence、cross-level credit、certification context | `GENERIC CORE` + profile constraints |
| Evidence | 受控信息在给定 context 中支持 argument/claim 的角色 | Development Verification、Safety Analysis、Safety Assessment evidence roles | `GENERIC CORE` + profile roles |
| Traceability | 对象间可导航关系 | safety allocation、objective/requirement、baseline/credit links | `GENERIC CORE` |
| Provenance | 对象、结论或 evidence 的来源与推导历史 | safety requirement origin、analysis/assumption/DAL/credit basis | `GENERIC CORE` relation |
| Configuration | object/environment/tool/data 的受控身份和状态 | SC1/SC2、certification baseline、safety model baseline | `GENERIC CORE` + profile rigor |
| Change impact | affected basis/claims/configuration/evidence 与 selected re-verification | modification impact、prior credit、safety reassessment、DAL/assumption impact | `GENERIC CORE` + aviation subflow |
| Coverage | population/criterion/evidence/uncovered disposition interface | requirement、FC、objective、safety requirement、assumption、independence coverage | `GENERIC EXTENSION POINT` |
| Sufficiency | reasoned assessment interface，不规定统一算法 | objective-/DAL-/safety-completion criteria | `GENERIC EXTENSION POINT` |
| Independence | typed constraint/claim/evidence extension point | functional、item-development、physical、process types | `GENERIC EXTENSION POINT` + profile taxonomy |
| Assurance Constraint | 对 obligation 的 applicability、rigor、performer、method/evidence controls 施加约束 | FDAL、IDAL、independence、safety-process constraints | `GENERIC EXTENSION POINT` |
| Safety Objective / Requirement | 不进入产品无关 taxonomy | ARP4761A safety objects；Safety Requirement 是 Requirement subtype | `AVIATION PROFILE` |
| Failure Condition / classification | 无通用强制等价物 | aviation safety-analysis objects | `AVIATION PROFILE` |
| SSA / ASA | 无通用过程同义词 | safety assessments，向 V11/V12 提供输入 | `AVIATION PROFILE` |
| Certification credit/approval | authority/acceptance extension point | certification-use relationship | `AVIATION PROFILE`；approval ≠ Evidence |

稳定分层如下：

```text
Generic Verification Assurance Framework
├─ Generic Core
├─ Generic Extension Points
└─ Domain Profiles
   └─ Civil Aviation
      ├─ Development Assurance profile / governance constraints [ARP4754B]
      └─ Safety Assessment view and assurance constraints [ARP4761A]
```

## 5. Terminology reconciliation

| Concept | Source-level difference | Consolidated definition | Classification |
|---|---|---|---|
| Verification | ISO 15288 面向 system/system element/artefact 与 specified requirements/characteristics；ARP4754B 面向 validated requirements 的 implementation | 以 ISO 定义作为 generic；`Implementation Verification` 是 aviation contextual specialization | DOMAIN SPECIALIZATION |
| Validation | ISO 15288 面向 intended use/application；ARP4754B 面向 requirements correctness/completeness | `System/Intended-use Validation` 与 `Requirement Validation` 是不同被评价对象 | DIFFERENT OBJECT LEVEL |
| Requirement | ISO 表达 need 及相关 constraints/conditions；航空加入 safety-derived 类型 | `Requirement` 为 generic；`Safety Requirement subtypeOf Requirement`，并保留 typed origin | DOMAIN SPECIALIZATION |
| Review | verification method 中的 inspection/review 与 lifecycle joint review/gate review 不同 | 分离 `Verification Review/Inspection`、`Lifecycle Review` 与 `Gate Decision` | CONTEXTUAL DIFFERENCE |
| Assurance | ISO 建立 justified confidence 与 claim–argument–evidence；ARP4754B/4761A 施加航空目标和评估 | generic Assurance 为上位语义；Development Assurance 与 Safety Assessment 为 profile mechanisms | COMPATIBLE |
| Evidence | ISO 强调 objective evidence/assurance case；ARP4754B 使用 Verification Data 支撑 substantiation；ARP4761A 汇聚多类结果 | Evidence 是 contextual role；Result/Data 可构成或支持 Evidence，但不自动等价 | DIFFERENT ABSTRACTION LEVEL |
| Coverage | ISO 不给通用 taxonomy；航空给出若干受评价 population | 采用可扩展 meta-model，不给通用百分比 | COMPATIBLE WITH OPEN TAXONOMY |
| Completion | generic approval/baseline/gate 与航空 SSA/ASA completion 的 scope 不同 | dependent assessment completion 是 closure input，不等同 V12 | DOMAIN SPECIALIZATION |

## 6. Process / activity / view / gate ontology

以下关系进入 conceptual baseline：

```text
Lifecycle Model contains Stage references
Stage invokes/applies Process as needed
Process contains Activity and Task as defined by its source
Process View selects/maps source activities and tasks around a concern
Assessment evaluates criteria and produces a conclusion
Review is an interaction that may inform an assessment or decision
Decision is an authority act based on declared inputs
Gate is a decision point, not a synonym for review or criteria satisfaction
Orchestration coordinates re-entry and cross-process dependencies
```

`Stage ≠ Process`、`Process ≠ Process View`、`Assessment ≠ Review`、`Review ≠ Decision`、`criteria satisfied ≠ authorization` 均冻结。V0–V12 是 mixed-ontology `Verification Assurance Process View`；它选择/映射源过程行为并增加明确标注的 framework orchestration，不是新的 ISO process set。

`Composite Gate` 晋级为 framework-defined generic architecture：

```text
Assessment
+ optional Review
+ Authority Decision
+ State/Baseline Event
```

“optional”表示 review 由适用标准、profile 或项目规则决定；并不允许跳过必要 assessment 或 authority decision。

## 7. V0–V12 consolidation

| V-ID | Stable label | Ontology | Generic source/process behavior | Aviation profile | Remaining gap |
|---|---|---|---|---|---|
| V0 | Verification Planning | Activity / information design | planning、scope、resources、schedule、roles | assurance objectives、FDAL/IDAL、independence、safety programme inputs | record schema |
| V1 | Verification Basis Establishment | Activity / information design | requirements、characteristics、architecture、configuration、source applicability | Safety Objectives/Requirements、assumptions、certification basis | basis completeness rules |
| V2 | Requirement Verifiability Analysis | Activity / evaluation | requirement quality 与 feasible verification actions | requirement-validation rigor、safety-derived constraints | detailed quality taxonomy |
| V3 | Verification Strategy Definition | Activity / information design | method、success criteria、environment、enablers、evidence points 与 trade-offs | FDAL-dependent method/independence/credit constraints | oracle and item rules |
| V4 | Verification Case Design | Activity / information design | framework decomposition from obligation to logical cases | unintended-behavior and safety scenarios where applicable | case/oracle schema |
| V5 | Verification Procedure Development | Activity / information design | executable procedures、conditions、records | representative environment、controlled facilities/tools | item-level procedure criteria |
| V6 | Verification Readiness | Composite gate | readiness assessment + optional review + decision + state/baseline event | test-readiness or safety inputs may contribute | authority/state/waiver semantics |
| V7 | Verification Execution | Activity | execute controlled procedure and capture observations/results | profile controls and independence apply | tool/evidence admissibility |
| V8 | Result Evaluation | Evaluation / decision | compare observed with expected/success criteria；record conclusion/anomaly | profile-specific objective and independence evaluation | decision taxonomy |
| V9 | Anomaly Resolution | Cross-process orchestration | report、classify、analyse、disposition、feed corrective/change processes | safety-impact escalation and OPR coordination | universal severity/closure rules |
| V10 | Change Impact & Re-verification | Cross-process orchestration | impact scope、prior-evidence validity、selected re-verification、updated evidence | modification credit + safety reassessment/DAL/assumption/architecture impact | generic selection algorithm |
| V11 | Coverage & Sufficiency Assessment | Assurance assessment | obligations、coverage、evidence、limitations、anomalies、constraints → reasoned conclusion | FC/objective/requirement/assumption/independence and heterogeneous safety evidence | domain criteria/authority |
| V12 | Verification Closure | Composite gate | V11 + dispositions + configuration + dependent assessments + decision + state/baseline event | development completion and SSA/ASA completion inputs | waiver/reopening/authority state model |

名称和上述 ontology 全部 `FROZEN FOR v0.2 CONCEPTUAL BASELINE`。冻结不表示每个元素的 schema、算法或 authority 已解决。

## 8. Verification Obligation

`Verification Obligation` 晋级为 framework-defined `GENERIC CORE` object。它不是五源任一标准的原生信息项，而是把 requirement/constraint 连接到可规划 verification 的必要中间对象。

```text
Verification Basis Element
  = Requirement
  | Specified Characteristic
  | Applicable Constraint

Verification Basis Element
  ── givesBasisTo ──> Verification Obligation
Verification Obligation
  ── addressedBy ──> Verification Strategy
```

`Verification Basis Element` 在此是 conceptual union/typed relation role，不是已经冻结 field schema 的新 information-item class。它保留 ISO 15288 Verification Process 对 specified requirements **and specified characteristics** 的适用范围，同时允许 profile/project 通过受控 Applicable Constraint 建立 obligation basis。其 schema、subtypes 与 cardinality refinements 留给 ISO 15289/29148。

基线 cardinality：

- 每个 obligation 必须有一个或多个 typed、受控 Verification Basis Elements；不得从 Failure Condition、DAL 或未形成受控 basis relation 的 project custom 直接无中介生成；
- 每个适用且需要验证的 Requirement 或 Specified Characteristic 必须由一个或多个 obligations 覆盖，或具有明确的 non-verification/disposition rationale；
- 一个 basis element 可产生多个 obligations；一个 obligation 也可联合处理多个 basis elements，因此关系为受约束的 many-to-many，而不是固定 `1:N`；
- Assurance Constraint 主要改变 `whether/how/who/rigor/evidence/control`，通常不改写 requirement 的行为语义；若它本身要求证明某项约束，则可成为 obligation basis。

Safety Requirement 以 Requirement subtype 参与同一主干；航空 profile 仍要求 Safety Objective、Independence Principle 或 Assumption 先形成适当的 Requirement/Constraint/Basis relation，不能形成直接 `FC → obligation` shortcut。FDAL/IDAL 本身是 Assurance Constraint 的来源/取值语境，不是无中介 obligation basis。

## 9. Verification Strategy

Verification Strategy 进入 `GENERIC CORE`，但完整字段集合仍由信息模型控制。最小 semantic contract 是：

```text
basis/obligation + scope
+ selected method/technique and rationale
+ success criteria / expected-result basis
+ execution level, environment and configuration
+ required coverage/evidence
+ applicable assurance and independence constraints
+ limitations, assumptions and re-entry conditions
```

FDAL/IDAL、certification credit、航空 objective applicability 与 safety-analysis method 均是 profile inputs，不是 generic strategy 的固定枚举。

## 10. Assurance architecture

`Verification Assurance` 晋级为 framework top-level concern，但仍标为 framework term，而非标准原生术语。其含义是：通过受控 Verification lifecycle、coverage/sufficiency assessment 和 evidence-based argument，对 verification-related claim 建立 justified confidence。

架构决策：

- Verification Assurance 是 cross-cutting process view/assurance view；
- Development Assurance 不是与 V0–V12 并列的通用过程，而是 ARP4754B 对 aircraft/system development processes 的 governance/rigor profile；
- Safety Assessment 是 ARP4761A 定义的航空 process view/assessment family，与 V0–V12 交换 requirements、constraints、assumptions、results/evidence 和 completion status；
- Safety Assurance 可描述该交互产生的 assurance concern，但 SSA/ASA 的原生定位和术语应优先保留；
- ISO 的 Assurance / assurance case 提供上位 claim–argument–evidence 语义，traceability 不能替代 argument。

## 11. Independence

采用 `IndependenceConstraint` 作为 `GENERIC EXTENSION POINT`，禁止使用一个通用 `independent: true/false` 表达完整语义。最小结构包括：

```text
type/profile vocabulary
source and rationale
applicable activity/object/claim
required separation or independence condition
independence claim
substantiation evidence
assessment and decision
```

航空 profile 专门化为 Functional、Item Development、Physical、Process Independence。必须保持：

```text
independence type
≠ independence principle
≠ independence requirement/constraint
≠ independence claim
≠ substantiation method/evidence
```

通用的“何时需要哪种 independence、由谁决定、何种证据足够”仍为 open gap。

## 12. Coverage

`CoverageObligation` 晋级为 `GENERIC EXTENSION POINT`，其 generic meta-model 冻结为：

```text
covered population and scope
+ applicable coverage criterion
+ coverage evidence/result
+ uncovered item disposition
+ configuration/context
```

`Coverage Result` 只报告 obligation 的满足状态或度量，不自动证明 sufficiency。Requirement Coverage、Safety Coverage 以及未来 Code/Structural Coverage 是 profile taxonomies；五源不支持统一 coverage percentage。

## 13. Sufficiency

`SufficiencyAssessment` 晋级为 `GENERIC EXTENSION POINT` interface，但不冻结通用算法：

```text
inputs:
  applicable obligations
  coverage results and uncovered dispositions
  evidence and provenance
  limitations and assumptions
  anomalies/deviations
  assurance/independence constraints
output:
  conclusion
  rationale/argument
  residual gaps and conditions
  assessor/authority and decision context
```

ARP4754B method/procedure concerns与 ARP4761A heterogeneous completion criteria 是航空 profile input，不是 generic formula。该 interface 是 V11 的稳定 semantic contract。

## 14. Evidence architecture

以下关系进入 conceptual baseline：

```text
Observation / Raw Record
  ── evaluatedAs ──> Result
Result or controlled Data
  ── mayConstituteOrSupport ──> Evidence
Evidence
  ── supports ──> Argument
Argument
  ── justifies ──> Claim
```

Evidence identity、provenance、integrity/configuration control、claim applicability、credibility 与 sufficiency contribution 分开评价。`Result ≠ Evidence`，但同一受控 information item 可在特定 context 中承担 Evidence role。

`Verification Data` 决定为 `AVIATION PROFILE information-item/container role`，不是 generic Evidence subtype。`Development Verification Evidence`、`Safety Analysis Evidence` 与 `Safety Assessment Evidence` 是可重叠的 profile roles，不是互斥文件类型。Certification approval 不是 Evidence。

## 15. Traceability / provenance / argument

三分法进入 `GENERIC CORE`：

| Relation | Answers | Does not prove |
|---|---|---|
| Traceability | 哪些对象存在声明关系、如何导航 | 关系为何足够或来源为何可信 |
| Provenance | 对象、结论、配置或 credit 从何处产生、如何转化 | 证据是否足以支持 claim |
| Argumentation | 为什么给定 context 中的 evidence 足以支持 conclusion/claim | 对象版本和来源可省略 |

SafetyRequirementOrigin、assumption origin、allocation、analysis lineage、baseline 与 credit basis 是 provenance 的 profile/application。未来 DBSE/MBSE graph 必须允许三类边分别查询。

## 16. Change Impact & Re-verification

V10 名称和 generic chain 冻结：

```text
Change / anomaly disposition
  → Impact Scope
  → Affected Requirements / Obligations / Claims / Assumptions / Configuration
  → Prior-Evidence Validity
  → Affected Assurance Constraints
  → Selected Re-verification / Re-analysis
  → Updated Results and Evidence
  → Reassessment and Closure/Re-entry Decision
```

domain profile 只增加 impact dimensions、selection rules 与 dependent assessments。ARP4754B 增加 modification/credit，ARP4761A 增加 safety reassessment、assumption、architecture、FDAL/IDAL 与 SSA/ASA synchronization。五源未给通用 regression-selection algorithm。

## 17. Assumptions

决策：`Assumption` 晋级为 `GENERIC EXTENSION POINT`，而非 aviation-only object。理由是 ISO 来源已要求识别分析/规划语境中的 assumptions，ARP4761A 则提供目前最完整的 lifecycle specialization；但通用 ownership、状态机和转 requirement 规则尚不足以冻结为 universal semantics。

Generic conceptual semantics 应能表示 identity、assumption statement、scope/context、affected objects，以及在适用时的 validity/confirmation information；ownership/responsibility 仅在 applicable process、profile 或 project 已定义时表示。这里冻结的是可表达的概念范围，不是 universal mandatory fields。精确 ownership、mandatory fields、validity states、confirmation obligations、cardinalities 与 lifecycle state transitions 均保持 open，等待 ISO 15289 和后续 domain evidence。航空 profile 可增加：capture → allocate/propagate → convert controllable premise to proposed requirement → confirm/correct → reassess impact。

## 18. Closure

V12 继续作为 `Composite Gate`，不等于“全部测试通过”、review completed、certification approval、SSA 或 ASA。generic semantic contract：

```text
applicable assessments completed
+ applicable obligations dispositioned
+ evidence, coverage and sufficiency conclusion available
+ anomalies/deviations/limitations dispositioned or explicitly accepted
+ configuration/baseline identified
+ required dependent assurance assessments completed
+ authority decision recorded
+ resulting state/baseline event recorded
```

具体 authority、waiver/deviation、reopening trigger 和 state machine 保持 open。V12 可在不同 scope/level 多次应用，不是唯一 project end event。

## 19. Development Assurance / Safety Assessment interfaces

采用“governance profile + interacting views”模型：

```text
Civil Aviation Development Assurance profile [ARP4754B]
  constrains planning, objectives, rigor, independence, control and credit
                 │
                 ▼
Verification Assurance Process View [V0–V12]
                 ↕
Safety Assessment Process View [AFHA/PASA/SFHA/PSSA/SSA/ASA]
```

Development Assurance 不另造一套与 V0–V12 竞争的 V-ID。Safety Assessment 也不替换 Verification：它产生/约束 Safety Requirements 和 Assurance Constraints，汇聚 development/safety evidence，并把 completion conclusions 输入 V11/V12。

## 20. Cross-standard conflict register

| Concern | Sources | Classification | Resolution |
|---|---|---|---|
| Verification definition | ISO 15288 vs ARP4754B | DOMAIN SPECIALIZATION | Generic Verification + aviation Implementation Verification |
| Validation definition | ISO 15288 vs ARP4754B | DIFFERENT OBJECT LEVEL / CONTEXTUAL | System/intended-use Validation 与 Requirement Validation 分开 |
| Verification method taxonomy | ISO 15288 vs ARP4754B | COMPATIBLE CONTEXTUAL TAXONOMIES | 不冻结一个来源专属枚举；保留 mapping/provenance |
| Review | ISO 24748-1 vs ISO/ARP verification review | CONTEXTUAL DIFFERENCE | Lifecycle Review、method inspection/review、gate decision 分开 |
| Independence | ISO QA/IV&V guidance vs ARP typed forms | DOMAIN SPECIALIZATION | generic extension point + aviation taxonomy；无 universal rule claim |
| Requirement | ISO generic vs Safety Requirement | DOMAIN SPECIALIZATION | Safety Requirement subtypeOf Requirement + typed provenance |
| Assurance | ISO assurance case vs Development/Safety Assurance | DIFFERENT ABSTRACTION LEVEL | generic justified-confidence semantics + aviation mechanisms |
| Coverage | ISO open taxonomy vs aviation populations | DOMAIN SPECIALIZATION | generic meta-model + profile taxonomies |
| Completion | generic gate/approval vs SSA/ASA completion | DIFFERENT SCOPE | dependent completion as V12 input |
| Evidence | objective evidence vs Verification Data/safety aggregation | DIFFERENT INFORMATION ROLE | Result/Data may support Evidence；profile roles retained |

未识别 `TRUE CONFLICT`。不存在冲突不表示术语可互换；上述 contextual boundaries 是 baseline 的一部分。

## 21. Gap disposition

| Gap | Disposition | Consolidated result | Residual gap / successor |
|---|---|---|---|
| ISO-G01 Independence | PARTIALLY RESOLVED | generic typed extension point + aviation taxonomy established | universal applicability、selection、authority、substantiation rule open |
| ISO-G02 Coverage | SPLIT | generic coverage meta-model resolved | ISO-G02A closed generically；ISO-G02B domain taxonomy/rules open |
| ISO-G03 Sufficiency | SPLIT | generic Sufficiency Assessment interface resolved | ISO-G03A closed generically；ISO-G03B domain criteria/authority open |
| ISO-G04 Oracle | KEEP PROPOSAL | expected-result justification remains useful | validity/configuration and domain support open |
| ISO-G05 Change/re-verification | RENAME + PARTIALLY RESOLVED | V10 existence/chain resolved generically | successor concerns selection/impact semantics |
| ISO-G06 Closure | RENAME + PARTIALLY RESOLVED | Composite Gate architecture resolved | authority、waiver、deviation、reopening、state model open |
| ISO-G07 Information-item schema | KEEP OPEN | relations are clearer, field/cardinality basis incomplete | prioritize ISO 15289 |
| ISO-G08 MBSE/model evidence | KEEP OPEN | ARP4761A supplies aviation MBSA lessons | generic model validity、tool qualification/admissibility open |
| LC-G01 Gate semantics | RESOLVED GENERICALLY | Composite Gate and event separation frozen | residual state/authority tracked by ISO-G06 |
| LC-G02 Review taxonomy | RESOLVED GENERICALLY | method review、lifecycle review、decision separated | profile/project naming remains contextual, not a framework gap |
| LC-G03 Process-view provenance | RESOLVED GENERICALLY | every V-element has ontology/source/profile/gap mapping | future element-level detailed mappings required during DBSE build |
| LC-G04 Instantiation evidence | PARTIALLY RESOLVED | record concept retained | schema/approval/cardinality waits for ISO 15289 and project validation |
| ARP-G01 Applicability/rigor | PARTIALLY RESOLVED FOR AVIATION | Assurance Constraint and separate credit intent established | item objectives wait for DO-178C/DO-254 |
| ARP-G02 Cross-level credit | RESOLVED FOR AVIATION PROFILE | allocation、performance、evidence source、acceptance、credit basis separated | generic reuse vocabulary remains extension point |
| ARP-G03 Unintended behavior | KEEP OPEN | aviation concern retained | item applicability/method diversity/sufficiency waits for item standards |
| SAF-G01 Safety→obligation | RESOLVED FOR AVIATION PROFILE | typed origins converge through Requirement/Constraint | cardinality validation during information-model work |
| SAF-G02 Assumption lifecycle | PARTIALLY RESOLVED | generic extension point + aviation lifecycle established | universal state/ownership rules open |
| SAF-G03 Multi-type independence | RESOLVED FOR AVIATION PROFILE | type/principle/requirement/claim/evidence separated | generic rule remains ISO-G01 |
| SAF-G04 Safety evidence aggregation | RESOLVED FOR AVIATION PROFILE | three evidence roles + provenance/configuration semantics | physical artifact schema remains ISO-G07 |
| SAF-G05 Safety sufficiency | PARTIALLY RESOLVED FOR AVIATION | completion criteria become V11 profile inputs | programme decision thresholds/authority remain contextual |
| SAF-G06 Change synchronization | RESOLVED FOR AVIATION PROFILE | V10 safety subflow frozen | generic selection semantics remain successor ISO-G05 |

## 22. Generic-Core promotion decisions

| Candidate | Previous state | Decision | Baseline classification and basis |
|---|---|---|---|
| Verification Obligation | Research proposal | PROMOTE | framework-defined `GENERIC CORE`; required bridge from basis to strategy |
| Composite Gate | Research proposal | PROMOTE | framework-defined `GENERIC CORE` architecture; assessment/review/decision/event separation |
| Coverage Obligation | Candidate | PROMOTE | `GENERIC EXTENSION POINT`; meta-model stable, taxonomies open |
| Sufficiency Assessment | Candidate | PROMOTE | `GENERIC EXTENSION POINT`; interface stable, algorithm open |
| Assurance Constraint | Aviation candidate | PROMOTE | `GENERIC EXTENSION POINT`; aviation supplies FDAL/IDAL/independence specializations |
| Independence Constraint | Scalar candidate | PROMOTE | `GENERIC EXTENSION POINT`; typed relation, not Boolean |
| Assumption | Aviation candidate | PROMOTE | `GENERIC EXTENSION POINT`; capability-oriented conceptual semantics, no mandatory generic field/state schema |
| Evidence Provenance | Working relation | PROMOTE | `GENERIC CORE` relation distinct from traceability/argument |
| Verification Credit | Aviation candidate | PROFILE-ONLY | explicit certification/verification credit remains aviation; generic prior-evidence applicability retained |
| Safety Requirement | Aviation candidate | PROFILE-ONLY | `Requirement` subtype in civil-aviation safety profile |
| Oracle | Research proposal | KEEP PROPOSAL | no five-source direct object basis |

“PROMOTE”表示进入 Framework conceptual baseline，不表示声称标准原生命名或 universal algorithm 已存在。

## 23. Information-model implications

决策驱动的第一版稳定对象集合：

```text
GENERIC CORE
  Requirement
  VerificationBasisElement role {Requirement, SpecifiedCharacteristic, ApplicableConstraint}
  VerificationObligation
  VerificationStrategy
  VerificationAction / Procedure
  Observation / Result
  Evidence
  Claim / Argument
  Configuration
  Change / ImpactAssessment
  Decision
  CompositeGate

GENERIC EXTENSION POINTS
  AssuranceConstraint
  IndependenceConstraint
  CoverageObligation / CoverageResult
  SufficiencyAssessment
  Assumption
  PriorEvidenceApplicability

AVIATION PROFILE
  FailureCondition / Classification
  SafetyObjective / SafetyRequirement
  FDAL / IDAL assignment
  IndependencePrinciple / Requirement / Claim
  SafetyAnalysisMethod / Result
  PSSA / SSA / ASA assessment roles
  VerificationCredit / CertificationCreditIntent
```

稳定关系：

```text
{Requirement, SpecifiedCharacteristic, ApplicableConstraint}
  ─typed givesBasisTo→ VerificationObligation
VerificationObligation ─addressedBy→ VerificationStrategy
Strategy ─realizedBy→ Action/Procedure
Procedure ─produces→ Observation/Result
Result/Data ─mayConstituteOrSupport→ Evidence
Evidence ─supports→ Argument ─justifies→ Claim
CoverageObligation ─assessedBy→ CoverageResult
SufficiencyAssessment ─considers→ obligations/coverage/evidence/limitations/anomalies/constraints
Change ─affects→ basis/claim/assumption/configuration/evidence
Decision ─authorizes→ GateStateTransition
```

关系仍需保留 source locator、classification、configuration 和 decision provenance。模板只能在这些决策之后更新；不能把 future DO/ISO 15289 fields 预先伪装成已支持字段。

### Five-source assurance causal chain

```text
Need / source concern
  → controlled Verification Basis
       contains typed Basis Elements
       {Requirement | Specified Characteristic | Applicable Constraint}
  → Verification Obligation
  → applicable Assurance / Independence Constraints
  → Verification Strategy
  → Action / Procedure
  → Observation / Result
  → Evidence
  → Coverage + Sufficiency Assessment
  → Argument / Claim
  → Closure Decision
```

航空 safety chain 连接但不替换该链：

```text
Failure Condition
  → Classification
  → Safety Objective / Safety Process Constraint
  → Safety Requirement
  → FDAL / IDAL / Independence Constraints
  → Verification or Assurance Obligation
```

## 24. Framework v0.2 readiness

| Criterion | Result | Basis |
|---|---|---|
| Stable terminology | PASS | Verification/Validation/Requirement/Evidence contextual taxonomy reconciled |
| Stable V0–V12 ontology | PASS | labels and mixed ontology frozen |
| Generic/Profile boundary | PASS | generic、extension、aviation roles explicit |
| Evidence semantics | PASS | Observation/Result/Evidence/Argument/Claim and provenance separated |
| Change semantics | PASS WITH OPEN SELECTION RULES | V10 chain stable；algorithm/profile criteria open |
| Gate semantics | PASS WITH OPEN STATE/AUTHORITY | Composite Gate stable；waiver/reopening open |
| Known gaps controlled | PASS | all 21 inherited gaps dispositioned, including splits/successors |
| Information model coherence | PASS FOR CONCEPTUAL BASELINE | entities/relations coherent；field/cardinality schema not frozen |

**Verdict: CONDITIONALLY READY FOR v0.2 CONCEPTUAL BASELINE.**

条件是：v0.2 只能宣称 conceptual baseline，不宣称 executable schema、item-level assurance coverage、certification acceptance 或 validated framework。ISO-G07、ISO-G02B、ISO-G03B、ISO-G05 successor、ISO-G06 successor 和 ISO-G08 必须保持可见。

## 25. Next-standard prioritization

评分使用 `Gap relevance × expected new information × domain authority ÷ research cost`，每个因子 1–5；数值只用于透明排序，不伪装为精确工程度量。

| Candidate | Relevance | New information | Authority | Cost | Score | Priority rationale |
|---|---:|---:|---:|---:|---:|---|
| ISO/IEC/IEEE 15289 | 5 | 5 | 5 | 3 | 41.7 | 直接处理 ISO-G07、record/content provenance，并支撑 Phase 4 |
| ISO/IEC/IEEE 29148 | 5 | 4 | 5 | 3 | 33.3 | 深化 Requirement/Verification Basis/verifiability 与信息项关系 |
| DO-178C | 4 | 5 | 5 | 5 | 20.0 | 软件 objective、coverage、independence 与 evidence rigor；解决 profile/item gaps |
| DO-254 | 4 | 4 | 5 | 5 | 16.0 | 硬件 item assurance 与 cross-level evidence |
| DO-297 | 3 | 4 | 5 | 4 | 15.0 | IMA allocation/integration/credit，需在 item semantics 后研究更有效 |

下一主要标准选择为 **ISO/IEC/IEEE 15289**。它不表示 item standards 不重要，而是当前最大结构性 gap 已从“有没有 process”转为“信息项内容、关系和 schema provenance”。之后应重新评分，不自动沿引用链推进。

## 26. Open questions

- Coverage profile taxonomies 与 completion rules 如何在跨领域保持可比较？
- Sufficiency decision authority、threshold 和 residual-risk acceptance 如何 profile 化？
- Oracle 是否能在 DO-178C/DO-254 或其他领域获得稳定对象基础？
- Generic assumption 状态、owner、confirmation obligation 与 requirement conversion 的最小规则是什么？
- Composite Gate 的 waiver/deviation/reopening 和 scope-level state machine 如何定义？
- Prior Evidence Applicability 与航空 Verification/Certification Credit 的边界和 cardinality 如何形式化？
- MBSE/model/tool outputs 在什么条件下可承担 Evidence role？
- V0–V12 的 element-level source-task mapping 应以何种 ISO 15289-compatible information item 保存？

## 27. Final conclusions

五源足以形成第一版 coherent normative architecture：ISO 15288 提供 generic lifecycle/V&V/assurance backbone，ISO 24748-1/2 提供 lifecycle/process application guidance，ARP4754B/ARP4761A 提供 civil-aviation Development Assurance 与 Safety Assessment specialization。没有发现 true conflict；主要差异来自 object level、abstraction level 和 domain context。

Framework 的稳定主干是 `Verification Basis Element {Requirement | Specified Characteristic | Applicable Constraint} → Verification Obligation → Strategy → Action/Result → Evidence → Coverage/Sufficiency → Argument/Claim → Closure Decision`。V0–V12 作为 mixed-ontology Verification Assurance Process View 进入 v0.2 conceptual baseline；V6/V12 是 framework-defined Composite Gates，V10 与 V11 的 semantic contracts 已稳定。Independence、Coverage、Sufficiency 与 Assumption 以 generic extension points 进入基线，航空 taxonomy 和 constraints 留在 profile。

本轮没有把 open gaps 隐藏为“已 harmonized”。Framework 可条件性进入 v0.2 conceptual baseline，但 executable information schema、domain criteria、item assurance 和 model-evidence rules 仍需后续标准研究与项目验证。

### Informal review disposition

| Finding | Disposition | Applied correction |
|---|---|---|
| R-01 Verification Obligation basis completeness | CLOSED | Replaced Requirement/Constraint-only basis with typed Requirement / Specified Characteristic / Applicable Constraint basis role；retained prohibition of direct FC/DAL/uncontrolled-project shortcut and deferred schema detail |
| R-02 Assumption conceptual/schema boundary | CLOSED | Replaced mandatory generic minimum fields with capability-oriented conceptual semantics；ownership、states、confirmation obligations、cardinalities and lifecycle transitions remain open |

## 28. Framework-object provenance annex（post-freeze governance）

本 annex 是 §22–§23 晋级决定的对象级 provenance 权威登记，不改变任何已冻结结论。目的：使 `PROMOTE ≠ source-native` 成为可查询事实，防止 framework-defined 对象在后续 Phase 4/5/8 中被误当作标准原生信息项。列含义：**Source-native** = 是否为五源原生术语/对象；**Non-aviation basis** = 是否存在非航空来源依据（generic 侧审计列）；**Schema gate** = 进入 executable schema 前必须满足的条件。

| Object | Classification | Source-native | Non-aviation basis | v0.2 frozen boundary | Open items | Schema gate |
|---|---|---|---|---|---|---|
| Verification Obligation | GENERIC CORE (framework-defined) | No | Indirect（ISO 15288 verification scope/trace tasks） | 对象存在；typed-basis 规则；受约束 many-to-many | field schema；disposition 语义 | ISO 15289 + conformance-testing methodology 研究后 |
| Verification Strategy | GENERIC CORE (source-supported) | Yes（6.4.9.3(a)(4)） | Direct | 概念 + 最小 semantic contract | 完整 VSR schema | ISO-G07 |
| Verification Basis Element role | framework-defined union role | No（构造于 ISO 概念之上） | Direct（3.36；6.4.9.1–.2） | typed union {Requirement \| Specified Characteristic \| Applicable Constraint} | class schema、subtypes、cardinality | ISO 15289 / 29148 |
| Verification Action / Procedure | source-supported | Yes（6.4.9.3(b)(1)） | Direct | 概念 | item-level 判据 | Phase 4 + item standards |
| Observation / Result | framework semantics over source concept | Partial | Direct（6.4.9.3(b)–(c)） | 与 Evidence 的 role 区分 | record schema | Phase 4 |
| Evidence | GENERIC CORE | Yes（5.10；6.4.9） | Direct | role 语义；mayConstituteOrSupport 关系 | physical artifact schema | ISO-G07 |
| Claim / Argument | GENERIC CORE | Conceptual support（5.10） | Direct | 与 Evidence 的关系 | claim ontology | Phase 5 |
| Configuration / Baseline | source-native | Yes（3.8；6.3.5） | Direct | 强制依赖 | — | — |
| Change / ImpactAssessment | framework-defined | No | Indirect（6.3.5 re-verification） | V10 chain | selection algorithm | ISO-G05 successor |
| Decision / Composite Gate | framework-defined | No | Guidance（ISO 24748-1 4.3/Clause 5） | assessment + optional review + authority decision + state/baseline event 分离 | waiver/reopen/authority/state model | ISO-G06 successor |
| Evidence Provenance | GENERIC CORE relation | No | Indirect（5.10） | 与 traceability/argumentation 三分 | schema | Phase 4 |
| Assurance Constraint | GENERIC EXTENSION POINT | No | Framework interface | extension interface | universal levels（不主张） | profile-supplied |
| Independence Constraint | GENERIC EXTENSION POINT | No | Hook only（ISO QA independence） | typed 结构（type/rationale/applicability/claim/substantiation） | applicability/authority/substantiation rules | ISO-G01 |
| Coverage Obligation / Result | GENERIC EXTENSION POINT | No | Framework meta-model | population+criterion+evidence+disposition+context | domain taxonomies/completion rules | ISO-G02B |
| Sufficiency Assessment | GENERIC EXTENSION POINT | No | Indirect（5.10 reasoning context） | I/O interface | reasoning semantics、criteria、authority | ISO-G03B / RQ4 / Phase 5 |
| Assumption | GENERIC EXTENSION POINT | No | Indirect（ISO 规划/分析语境提及 assumptions） | capability-oriented conceptual semantics | states/ownership/cardinality | ISO 15289 |
| Prior Evidence Applicability | GENERIC EXTENSION POINT | No | Framework concept | applicability relation | 与 credit 的边界/cardinality | Phase 4/5 |
| Oracle | RESEARCH PROPOSAL | No | None in five sources | 保持提案 | 对象依据 | conformance-testing methodology 研究（候选） |
| Verification Case / Technique / Stimulus / Expected / Observed / Acceptance Criterion | RESEARCH PROPOSAL layer | No | Informative NOTEs partial | 术语提案 | schemas | Phase 4/5 |
| Aviation Profile objects（Safety Requirement subtype、Failure Condition/Classification、Safety Objective、FDAL/IDAL assignment、Independence Principle/Requirement/Claim、Safety Analysis Method/Result、PSSA/SSA/ASA、Verification/Certification Credit） | PROFILE-ONLY | ARP-native | n/a（profile） | role 级 profile taxonomy | item-level 细化 | DO-178C/DO-254 轮次 |

**Generic-basis 审计结论（§22 复核）：** 无任何 Generic Core / Extension Point 对象仅依赖航空来源——航空专属候选（Safety Requirement、Verification/Certification Credit）均已保持 PROFILE-ONLY。该结论应随每次新增 promotion 重新验证。

**维护规则：**

1. 任何对象进入 Phase 4 executable schema 前，其 annex 行的 Schema gate 必须满足并更新为 `schema-ready`；
2. 新增 promotion 必须先在本 annex 登记（含来源属性与通用侧依据），再进入 terminology / templates / map；
3. 本 annex 是 framework-defined 对象 provenance 的唯一权威；其他文件引用不重定义（见 ARCHITECTURE.md definition-ownership 规则）。
