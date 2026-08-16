---
title: Working Terminology Baseline
status: baseline
version: 0.7
baseline: v0.1
owner: research
last_updated: 2026-08-16
dependencies:
  - research_scope.md
---

# Working Terminology Baseline

本文件冻结 v0.1 的工作语言，而不是声称已经完成跨标准术语协调。除非另有说明，所有条目的 **Normative status** 均为 `To be verified`。ISO 15288 的支持结论受其 Clause 4 conformance mode 约束；NOTE 与资料性附录只作为 informative guidance。

### Life Cycle Model

**Working definition:** 组织生命周期相关过程和活动的框架，可使用 stages 为决策、沟通和管理提供共同参照。

**Normative status:** Direct term and guidance — ISO/IEC/IEEE 24748-1:2024, 3.25 and 4.3

**Related concepts:** Life Cycle, Stage, Process, Decision Gate

**Notes:** Life Cycle Model ≠ Process Model；模型具有 stages 不表示系统生命周期脱离模型后天然具有固定阶段。

### Stage

**Working definition:** 与系统描述或实现状态有关的一段生命周期期间，可关联重大进展、milestones、entry/exit criteria 和 decisions。

**Normative status:** Direct term and guidance — ISO/IEC/IEEE 24748-1:2024, 3.48, 4.3 and Clause 5

**Related concepts:** Life Cycle Model, Process, Entry Criterion, Exit Criterion

**Notes:** Stage ≠ Process；stages 可重叠、并行、非顺序或重复。V0–V12 不属于 ISO 24748-1 lifecycle stages。

### Decision Gate

**Working definition:** 依据 stage criteria、风险、评审结果和外部事件等输入，由授权角色作出继续、开始、保持、重启或终止等决定的管理节点。

**Normative status:** Guidance-supported working definition — ISO/IEC/IEEE 24748-1:2024, 4.3 and Clause 5

**Related concepts:** Entry Criterion, Exit Criterion, Review, Decision Authority

**Notes:** Criteria satisfaction ≠ Review completion ≠ Gate decision。V6/V12 的完整状态模型仍是 research proposal。

### Process View

**Working definition:** 围绕某项跨生命周期 concern，选择和组织源标准中已有 process activities/tasks 的视图，并声明 stakeholder、purpose、outcomes 与 source references。

**Normative status:** Informative guidance — ISO/IEC/IEEE 24748-1:2024, Annex D

**Related concepts:** Process, Activity, Task, Verification Assurance

**Notes:** Process view 不定义自己的新源标准活动或任务。框架新增 orchestration behavior 必须明确标为 interpretation/proposal。

### Lifecycle / Process Instantiation Record

**Working definition:** 记录项目语境、适用标准、development approach、stages、criteria、gates、过程选择/排除、映射关系和理由的受控信息项。

**Normative status:** Record concept is guidance-supported; schema and name are a research proposal — ISO/IEC/IEEE 24748-1:2024, 6.2.2–6.2.8

**Related concepts:** Tailoring, Life Cycle Model, Process View, Decision Record

**Notes:** 该记录用于审计 project instantiation，不应被描述为 ISO 24748-1 强制模板。

### Verification

**Working definition:** 为判断规定的要求是否得到满足而规划、实施、评价并记录客观活动与结果的工程过程。

**Normative status:** Direct normative support — ISO/IEC/IEEE 15288:2023, 3.55 and 6.4.9

**Related concepts:** Test, Analysis, Inspection, Evidence

**Notes:** Test 只是候选 Verification activity/method 之一，不能代表全部 Verification。

**Aviation profile:** SAE ARP4754B, 2.2 and 5.5 将 Verification 限定为评价 requirements 的 implementation 是否满足已验证 requirements。该定义是 aircraft/system development context，不覆盖 ISO 通用定义。

### Validation

**Working definition:** 评价需求、系统或产品相对于预期用途和运行语境是否适当的过程。

**Normative status:** Direct normative support — ISO/IEC/IEEE 15288:2023, 3.54 and 6.4.11

**Related concepts:** Verification, Intended Use, Operational Context

**Notes:** 与 Verification 的精确边界需要按来源和生命周期层级研究。

**Aviation profile:** SAE ARP4754B, 2.2 and 5.4 将 Validation 定义为判断产品 requirements 是否正确且完整。它是 requirements-validation taxonomy，不与 ISO intended-use/system-validation 定义强制同义。

### Requirement

**Working definition:** 表达或转化某项 need，并包含其相关 constraints 和 conditions 的陈述。

**Normative status:** Direct normative support — ISO/IEC/IEEE 15288:2023, 3.36

**Related concepts:** Stakeholder Need, Verification Basis, Verification Obligation, Traceability

**Notes:** Requirement information model 必须保留相关约束和条件，不能只表达期望行为。Stakeholder requirement validation、system requirement validation、requirement quality/verification 与 system validation 应分别建模。

### Verification Assurance

**Working definition:** 对 Verification 过程、结果及其充分性建立可信性，使相关 claim 能由受控、可追溯和可复核的信息支持。

**Normative status:** Research proposal

**Related concepts:** Assurance Argument, Evidence, Sufficiency

**Notes:** 这是本研究核心概念，尚未声明为任何标准的原生术语。

### Development Assurance

**Working definition:** 在开发生命周期中，通过规划、过程和目标达成降低开发错误风险的保证语境。

**Normative status:** Direct aviation-domain definition — SAE ARP4754B, 1.2 and 2.2

**Related concepts:** Verification Assurance, Independence, Assurance Level

**Notes:** ARP4754B 把 Development Assurance 定位为 planned/systematic、与 safety-derived rigor 相称的过程，用于建立 development errors 已识别和纠正的信心。它是航空 profile 概念，不替代 ISO 通用 Assurance；FDAL/IDAL 详细分配继续由 ARP4761A 研究。

### Assurance Applicability / Rigor

**Working definition:** 在某一 domain profile 中，描述 assurance level 与 objective applicability、活动独立性及输出控制强度之间关系的集合。

**Normative status:** Aviation relationship directly supported; unified entity remains a research proposal — SAE ARP4754B, 5.2, 5.6.4 and Appendix A

**Related concepts:** FDAL, IDAL, Process Independence, System Control Category, Certification Credit Intent

**Notes:** 不能压缩成一个 `DAL` 或 `independent=true`。Appendix A 的 `R* / R / A / N` 只在 `source × objective × FDAL × cell` 上下文中分别表达带独立性的推荐、推荐、认证协商和认证不要求；它们不是 generic assurance-level enum，也不直接决定工程活动是否必要。Certification Credit Intent 是独立的 project/certification-use relation，不由 FDAL 自动推导。

### Verification Basis

**Working definition:** 规定 Verification 适用要求、约束、架构、接口、配置和适用来源的受控集合。

**Normative status:** Research proposal

**Related concepts:** Requirement, Configuration, Normative Source

**Notes:** 候选 DBSE information item。

### Verification Obligation

**Working definition:** 对某项 Requirement 或 Assurance Objective 需要证明什么的明确陈述。

**Normative status:** Research proposal

**Related concepts:** Verification Objective, Verification Strategy

**Notes:** 不等同于 Requirement 本身。

### Verification Objective

**Working definition:** Verification 活动拟达成的目标或判定状态。

**Normative status:** To be verified

**Related concepts:** Verification Obligation, Acceptance Criterion

**Notes:** 后续需区分标准中的 objective 与本框架的工作对象。

### Verification Strategy

**Working definition:** 针对 Verification Obligation 对执行层级、方法、技术、环境、配置、Oracle、Coverage、独立性和 Evidence 的受控选择及理由。

**Normative status:** Direct concept support; field model remains a research proposal — ISO/IEC/IEEE 15288:2023, 6.4.9.3(a)(4)

**Related concepts:** Level, Method, Technique, Oracle, Evidence

**Notes:** 定义 Verification Strategy 的 task 有直接支持；scope、actions、methods、success criteria、enablers、evidence points 和 trade-offs 的详细内容主要来自 NOTE。当前完整 VSR schema 不是标准规定。

### Verification Level

**Working definition:** Requirement 分配或 Verification 执行所在的系统分解/集成层级。

**Normative status:** To be verified

**Related concepts:** Allocation, Integration, Verification Strategy

**Notes:** Requirement allocation level 与 verification execution level 可能不同。ARP4754B, 4.6.1 和 5.5.4 进一步要求 aviation profile 记录跨 aircraft/system/item 层级的 allocation、delegation、evidence acceptance 和 credit basis。

### Verification Method

**Working definition:** 用于获得 Verification 结论的一级实现类别，如 Test、Analysis 或 Inspection 等候选分类。

**Normative status:** Method selection is directly supported; taxonomy examples are informative — ISO/IEC/IEEE 15288:2023, 6.4.9.3(a)(3)

**Related concepts:** Verification Technique, Verification Case

**Notes:** ISO 15288 的 NOTE 示例为 Inspection、Analysis、Demonstration、Testing。ARP4754B, 5.5.5 使用 Inspection/Review、Analysis、Testing or Demonstration、Similarity/Service Experience。两者是可映射的 contextual taxonomies；lifecycle review/gate 不因名称相同而成为 Verification Method。

### Verification Technique

**Working definition:** 在某种 Verification Method 内构造刺激、分析范围或覆盖的具体技术。

**Normative status:** Research proposal

**Related concepts:** Boundary Value, State Transition, Fault Injection

**Notes:** Boundary Value 等不与 Test/Analysis 放在同一抽象层级。

### Verification Case

**Working definition:** 描述需要证明什么、适用条件、刺激、预期响应、判据和 coverage contribution 的逻辑验证单元。

**Normative status:** Research proposal

**Related concepts:** Verification Strategy, Procedure, Acceptance Criterion

**Notes:** Case 表达 intent；Procedure 表达 execution implementation。

### Verification Procedure

**Working definition:** 在指定环境和配置中执行 Verification Case 的可操作步骤与记录要求。

**Normative status:** Procedure concept directly supported; this working definition remains partly proposed — ISO/IEC/IEEE 15288:2023, 6.4.9.3(b)(1)

**Related concepts:** Verification Case, Environment, Execution Record

**Notes:** 不应在 Case 尚未稳定前把工具步骤当作验证目标。

### Verification Environment

**Working definition:** 执行 Verification 所需的设施、设备、软件、模型、接口、人员能力及受控条件。

**Normative status:** Direct concept support — ISO/IEC/IEEE 15288:2023, 6.4.9.3(a)–(b)

**Related concepts:** Configuration, Tool, Procedure

**Notes:** 环境身份和状态是 Evidence 可审计性的候选组成。

### Configuration

**Working definition:** 与 Verification 对象、环境、输入、工具和数据有关的受控版本及组合状态。

**Normative status:** Direct cross-process support — ISO/IEC/IEEE 15288:2023, 3.8, 6.3.5 and 6.4.9.3(c)(5)

**Related concepts:** Baseline, Change, Evidence

**Notes:** Result 与配置不一致时其有效性需要重新评价。

### Stimulus

**Working definition:** 为触发或观察目标行为而施加的输入、事件、状态变化或条件。

**Normative status:** Research proposal

**Related concepts:** Verification Case, System State, Observed Result

**Notes:** 可包含正常、边界、异常或故障条件。

### Expected Result

**Working definition:** 在给定前置条件、配置、状态和刺激下预期观察到的响应。

**Normative status:** Research proposal

**Related concepts:** Oracle, Acceptance Criterion

**Notes:** Expected Result ≠ Oracle；前者是期望，后者是其正确性依据。

### Observed Result

**Working definition:** Verification execution 实际产生并记录的响应或测量结果。

**Normative status:** Research proposal

**Related concepts:** Expected Result, Result Evaluation, Raw Record

**Notes:** Result 与 Evidence 是不同的 assurance roles。Observed Result 可以构成或支持 Evidence；其 provenance、integrity/control、claim applicability、credibility 和对 sufficiency 的贡献应分别评价，不能建模为固定条件触发的 Result→Evidence 二值转换。

### Acceptance Criterion

**Working definition:** 判定 Observed Result 是否满足 Verification Objective 的明确规则、阈值或条件。

**Normative status:** Research proposal

**Related concepts:** Expected Result, Oracle, Pass/Fail

**Notes:** 应可执行或可由审查者一致解释。

### Oracle

**Working definition:** 支撑 Expected Result 和 Acceptance Criterion 正确性的独立或受控依据。

**Normative status:** Research proposal

**Related concepts:** Requirement, Reference Model, Independent Calculation

**Notes:** Oracle 的可信性需要单独评价。

### Coverage

**Working definition:** 对已执行 Verification 相对于明确 coverage obligations 的范围度量或状态描述。

**Normative status:** To be verified

**Related concepts:** Coverage Obligation, Sufficiency, Requirement Type

**Notes:** 不假设所有 coverage dimensions 对所有系统均强制适用。

### Verification Sufficiency

**Working definition:** 对所选策略、活动、coverage、配置、异常处置和 Evidence 是否足以支持目标 claim 的综合评价。

**Normative status:** Research proposal

**Related concepts:** Coverage, Evidence, Assurance Argument

**Notes:** Requirement Coverage = 100% 本身不证明充分。

### Evidence

**Working definition:** 具有可识别来源、适用配置、完整性和可复核性的受控信息，用于支持 claim 或 argument。

**Normative status:** Direct concept support; framework definition is narrower — ISO/IEC/IEEE 15288:2023, 5.10 and 6.4.9

**Related concepts:** Result, Traceability, Compliance Claim

**Notes:** ISO 15288 支持 objective evidence，并在 assurance case 中区分 claim、argument 与 evidence。ARP4754B, 5.5.6 and 5.6 支持 Verification Data 提供 evidence 并在约定语境中用于 compliance substantiation，但不定义 generic Result→Evidence conversion rule。某项 result/data 可构成或支持 Evidence；其对特定 claim 的 applicability、credibility、control 和 sufficiency 是分开的评价。Certification approval 不是 Evidence。

### Verification Data

**Working definition:** 对 Verification 的计划、程序、执行结果、矩阵、汇总和问题记录进行组织并受配置控制的数据集合。

**Normative status:** Direct aviation-domain concept — SAE ARP4754B, 5.5.6 and Appendix A

**Related concepts:** Result, Evidence, Configuration, Compliance Substantiation

**Notes:** Verification Data 可以提供、构成或支持 evidence，但 data/result 与 evidence role 不自动等价。Evidence identity 与其对特定 claim 的 applicability、credibility/control、sufficiency 需要分开；认证用途取决于 certification coordination，而不是 Evidence existence 的定义条件。

### Evidence Credit

**Working definition:** 在新或变更应用中，经 baseline traceability、适用性/差异分析和补充活动证明后，对既有受控 evidence 的有限接受关系。

**Normative status:** Aviation relationship directly supported; unified entity remains a research proposal — SAE ARP4754B, 6.4

**Related concepts:** Evidence Reuse, Modification Impact, Service History, Certification Baseline

**Notes:** `credit` ≠ copy，也不等于既有认证自动延续；应记录 credit objective、basis、differences、limitations、acceptance 和 supplemental evidence。

### Traceability

**Working definition:** 在来源、要求、活动、信息项、结果、Evidence 和 Claim 之间建立可导航关系的能力。

**Normative status:** Direct concept support — ISO/IEC/IEEE 15288:2023, 3.52 and 6.4.9.3(c)(4)

**Related concepts:** Digital Thread, Evidence, Change Impact

**Notes:** ISO 15288 的 NOTE 支持 verified element 与 strategy、architecture、design、requirements、results/evidence、anomalies 和 deviations 的双向关联。Traceability ≠ Assurance Argument；关联存在不自动证明证据充分。

### Compliance Claim

**Working definition:** 关于某项适用要求或 assurance objective 已得到满足的可审查陈述。

**Normative status:** Research proposal

**Related concepts:** Assurance Argument, Evidence

**Notes:** Claim 的适用认证语境必须由后续研究限定。

### Assurance Argument

**Working definition:** 解释一组 Evidence 为什么足以支持某个 claim 的结构化推理。

**Normative status:** Direct concept support — ISO/IEC/IEEE 15288:2023, 5.10

**Related concepts:** Compliance Claim, Evidence, GSN

**Notes:** 不能由 trace links 的数量替代。

### Anomaly

**Working definition:** Verification 过程中发现的预期与观察不一致、过程偏离、数据问题或其他需要处置的异常事项。

**Normative status:** Direct concept support — ISO/IEC/IEEE 15288:2023, 6.4.9.2 and 6.4.9.3(c)

**Related concepts:** Disposition, Change, Regression

**Notes:** 分类、授权和 closure rules 待研究。

### Change Impact & Re-verification

**Working definition:** 因变更、异常处置或既有证据适用性变化，识别受影响的 requirements、claims、配置和 evidence，并选择重新执行或重新评价 Verification 的跨过程活动集合。

**Normative status:** Generic concept support plus direct aviation specialization; named orchestration remains framework-defined — ISO/IEC/IEEE 15288:2023, 6.3.5 and 6.4.9; SAE ARP4754B, 6.3–6.4

**Related concepts:** Change Impact, Evidence Validity, Configuration

**Notes:** V10 保留稳定 ID，并从 `Regression` 改名为 `Change Impact & Re-verification`。ARP4754B 直接支持 modification impact 和 prior-evidence credit 的航空关系，但仍未定义通用选择算法；re-verification 不等同于无差别重复全部测试。

### Verification Closure

**Working definition:** 对目标、coverage、Evidence、配置、异常和限制是否满足关闭条件的正式评价与决策。

**Normative status:** Research proposal

**Related concepts:** Sufficiency, Compliance Claim, Baseline

**Notes:** ISO 24748-1:2024 的 stage exit criteria、decision gates 和 authorization 为组合 closure decision 提供指导性支撑，但不定义名为 Verification Closure 的过程。v0.1 不冻结具体 closure criteria、waiver、reopening 或 authority semantics。

### DBSE

**Working definition:** Document-Based Systems Engineering；以受控信息项、模板、关系和评审状态组织系统工程知识的工作方式。

**Normative status:** Working definition

**Related concepts:** Information Model, MBSE, Configuration Management

**Notes:** DBSE ≠ “用文档代替工程”；它是本研究进入形式化模型前的可审计基线。

### MBSE

**Working definition:** Model-Based Systems Engineering；以机器可解释模型作为重要工程信息载体，支持关联、查询、约束和分析。

**Normative status:** Informative support — ISO/IEC/IEEE 15288:2023, Annex D

**Related concepts:** Metamodel, SysML, Automation

**Notes:** Annex D 支持模型查询、检查、影响分析和模型辅助 V&V，但不强制 MBSE、SysML 或特定工具；替代实物的模型用途依赖模型验证。MBSE ≠ “把已有文档画成 SysML 图”。

### Domain Profile

**Working definition:** 将 Generic Framework 以特定领域架构、接口、约束、patterns、examples 和 tooling 进行实例化的受控集合。

**Normative status:** Research proposal

**Related concepts:** Generic Framework, DCAS, Concrete Project Practice

**Notes:** Domain knowledge 不能反向成为无依据的 generic rule。

### Verification Pattern

**Working definition:** 对重复出现的 Verification 问题、适用条件、构造规则、coverage obligation、Oracle 与 Evidence 的可复用解决结构。

**Normative status:** Research proposal

**Related concepts:** Verification Technique, Case Design, Domain Instance

**Notes:** v0.1 中的 pattern 名称与 taxonomy 均为 working proposal。

### Failure Condition

**Working definition:** 由 failures/errors 造成或促成、并结合飞行阶段、运行/环境事件等语境描述的 aircraft/occupant condition。

**Normative status:** Aviation definition — SAE ARP4761A, 2.2

**Related concepts:** Failure Effect, Failure Mode, Classification, Safety Objective

**Notes:** Failure Mode 是对象失效的具体方式；Failure Effect 是其后果；Failure Condition 是上游 safety object，不是 Verification Case。其 classification 影响分析与保证严谨度，但不直接定义测试数量。

### Safety Objective

**Working definition:** 与 Failure Condition 相关、规定可接受 safety performance 的判据。

**Normative status:** Aviation definition — SAE ARP4761A, 2.2

**Related concepts:** Failure Condition, Classification, Verification Basis, Safety Requirement

**Notes:** 可作为 Verification Basis 输入，但不等同 Verification Objective、Case 或 Procedure。

### Safety Requirement

**Working definition:** 为实现 Safety Objective，或满足 Safety Process 所建立 constraint 而必需的 requirement。

**Normative status:** Aviation definition — SAE ARP4761A, 2.2

**Related concepts:** Requirement, Safety Objective, Verification Obligation

**Notes:** Framework 中作为 `Requirement` subtype/classification，并允许多个 typed origins：Safety Objective、Safety Process Constraint、Independence Principle、转化为受控 requirement 的 Assumption，以及适用的 architecture/analysis result。保留 source analysis、rationale、allocation 与 assumption provenance；不能退化为单一 `SafetyObjective → SafetyRequirement` source 字段。

### Safety Assessment

**Working definition:** 对 Failure Conditions、Safety Objectives/Requirements、architecture、assumptions 和适用 evidence 进行系统评价的航空过程族。

**Normative status:** Aviation concept support — SAE ARP4761A, Section 3 and Appendices A–F

**Related concepts:** AFHA, PASA, SFHA, PSSA, SSA, ASA, Safety Analysis

**Notes:** SSA/ASA 可专门化为 aviation assurance assessments；`SSA ≠ generic Verification Process`，`ASA ≠ V12`。

### Safety Analysis Method

**Working definition:** 用于分析 failure behavior、failure combinations/probabilities、common causes、zones 或 particular risks 的方法类型。

**Normative status:** Aviation taxonomy — SAE ARP4761A, 3.1.2 and Section 4

**Related concepts:** FTA, DD, MA, MBSA, FMEA/FMES, CEA, ZSA, PRA, CMA

**Notes:** 与 Verification Method 分层；受控分析结果可以构成或支持 Safety Analysis Evidence。

### FDAL / IDAL

**Working definition:** 分别调节 function/system development 与 software/electronic-hardware item development assurance tasks 严谨度的航空等级。

**Normative status:** Aviation definition and assignment guidance — SAE ARP4761A, 2.2, 3.9 and Appendix P

**Related concepts:** Failure Condition Classification, Architecture, Functional Failure Set, Assurance Constraint

**Notes:** 不是 Verification Level、method、safety classification 或自动 certification credit；应建模为带 source/assignment provenance 的 Assurance Constraint。

### Independence

**Working definition:** ARP4761A 区分四种航空 independence：Functional Independence 以不同 functions 降低 common development error likelihood；Item Development Independence 以不同 item designs 降低 common development error likelihood；Physical Independence 以 separation/segregation 降低物理失效、损伤或环境效应造成的 common failures；Process Independence 以职责分离实现由活动执行者之外人员进行 objective evaluation。

**Normative status:** Aviation definitions — SAE ARP4761A, 2.2

**Related concepts:** Independence Principle, Independence Requirement, Independence Claim, CMA, ZSA, PRA

**Notes:** Source definition 与 substantiation criterion 分开。Appendix P 在 FDAL/IDAL assignment 语境中通过 requirement sets、item designs、development processes 与 common-error sources 评价 functional/item-development independence claim，并可使用 CMA 或等效技术提供 substantiation；这些判定条件不替代 2.2 definition。

### Independence Principle / Independence Requirement

**Working definition:** Independence Principle 是 intended implementation 中被判定需要 independence 的特征；Independence Requirement 是对该需要的可分配、可确认约束。

**Normative status:** Aviation definition/concept — SAE ARP4761A, 2.2 and Appendix P

**Related concepts:** Functional Independence, Item Development Independence, Physical Independence, Process Independence

**Notes:** Principle ≠ Requirement。四类 independence 需要分别记录 claim、rationale 和 CMA/ZSA/PRA 或 development-process substantiation；不能压缩为一个布尔值。

### Assumption

**Working definition:** 在尚未获得已验证信息时用于分析的 premise，并在生命周期中被拥有、传播、确认或纠正。

**Normative status:** Aviation definition/lifecycle support; generic promotion pending — SAE ARP4761A, 2.2, A.6 and D.4.3.2

**Related concepts:** Assumption Obligation, Assumption Confirmation, Requirement, Change Impact

**Notes:** 组织可控制的 premise 宜转化为 proposed requirement；未确认 assumption 会限制 safety conclusion validity。是否提升为 Generic Framework object 留待跨标准复审。
