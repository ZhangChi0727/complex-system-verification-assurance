---
title: Working Terminology Baseline
status: baseline
version: 0.1
baseline: v0.1
owner: research
last_updated: 2026-08-15
dependencies:
  - research_scope.md
---

# Working Terminology Baseline

本文件冻结 v0.1 的工作语言，而不是声称已经完成跨标准术语协调。除非另有说明，所有条目的 **Normative status** 均为 `To be verified`。

### Verification

**Working definition:** 为判断规定的要求是否得到满足而规划、实施、评价并记录客观活动与结果的工程过程。

**Normative status:** To be verified

**Related concepts:** Test, Analysis, Inspection, Evidence

**Notes:** Test 只是候选 Verification activity/method 之一，不能代表全部 Verification。

### Validation

**Working definition:** 评价需求、系统或产品相对于预期用途和运行语境是否适当的过程。

**Normative status:** To be verified

**Related concepts:** Verification, Intended Use, Operational Context

**Notes:** 与 Verification 的精确边界需要按来源和生命周期层级研究。

### Verification Assurance

**Working definition:** 对 Verification 过程、结果及其充分性建立可信性，使相关 claim 能由受控、可追溯和可复核的信息支持。

**Normative status:** Research proposal

**Related concepts:** Assurance Argument, Evidence, Sufficiency

**Notes:** 这是本研究核心概念，尚未声明为任何标准的原生术语。

### Development Assurance

**Working definition:** 在开发生命周期中，通过规划、过程和目标达成降低开发错误风险的保证语境。

**Normative status:** To be verified

**Related concepts:** Verification Assurance, Independence, Assurance Level

**Notes:** 其航空语境和分配机制需在 ARP4754B 等来源中研究。

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

**Normative status:** Research proposal

**Related concepts:** Level, Method, Technique, Oracle, Evidence

**Notes:** 不是正式 industry standard；v0.1 只建立研究草案。

### Verification Level

**Working definition:** Requirement 分配或 Verification 执行所在的系统分解/集成层级。

**Normative status:** To be verified

**Related concepts:** Allocation, Integration, Verification Strategy

**Notes:** Requirement allocation level 与 verification execution level 可能不同。

### Verification Method

**Working definition:** 用于获得 Verification 结论的一级实现类别，如 Test、Analysis 或 Inspection 等候选分类。

**Normative status:** To be verified

**Related concepts:** Verification Technique, Verification Case

**Notes:** Verification Method ≠ Verification Technique；最终 taxonomy 待标准研究。

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

**Normative status:** Research proposal

**Related concepts:** Verification Case, Environment, Execution Record

**Notes:** 不应在 Case 尚未稳定前把工具步骤当作验证目标。

### Verification Environment

**Working definition:** 执行 Verification 所需的设施、设备、软件、模型、接口、人员能力及受控条件。

**Normative status:** To be verified

**Related concepts:** Configuration, Tool, Procedure

**Notes:** 环境身份和状态是 Evidence 可审计性的候选组成。

### Configuration

**Working definition:** 与 Verification 对象、环境、输入、工具和数据有关的受控版本及组合状态。

**Normative status:** To be verified

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

**Notes:** Result ≠ Evidence；只有满足来源、配置和控制条件的信息才能成为适用 Evidence。

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

**Normative status:** To be verified

**Related concepts:** Result, Traceability, Compliance Claim

**Notes:** 原始记录、评价结果与 Evidence 的关系待信息模型研究。

### Traceability

**Working definition:** 在来源、要求、活动、信息项、结果、Evidence 和 Claim 之间建立可导航关系的能力。

**Normative status:** To be verified

**Related concepts:** Digital Thread, Evidence, Change Impact

**Notes:** Traceability ≠ Assurance Argument；关联存在不自动证明证据充分。

### Compliance Claim

**Working definition:** 关于某项适用要求或 assurance objective 已得到满足的可审查陈述。

**Normative status:** Research proposal

**Related concepts:** Assurance Argument, Evidence

**Notes:** Claim 的适用认证语境必须由后续研究限定。

### Assurance Argument

**Working definition:** 解释一组 Evidence 为什么足以支持某个 claim 的结构化推理。

**Normative status:** To be verified

**Related concepts:** Compliance Claim, Evidence, GSN

**Notes:** 不能由 trace links 的数量替代。

### Anomaly

**Working definition:** Verification 过程中发现的预期与观察不一致、过程偏离、数据问题或其他需要处置的异常事项。

**Normative status:** To be verified

**Related concepts:** Disposition, Change, Regression

**Notes:** 分类、授权和 closure rules 待研究。

### Regression

**Working definition:** 因变更、异常处置或影响分析而重新执行或重新评价 Verification 的活动集合。

**Normative status:** To be verified

**Related concepts:** Change Impact, Evidence Validity, Configuration

**Notes:** Regression 不等同于无差别重复全部测试。

### Verification Closure

**Working definition:** 对目标、coverage、Evidence、配置、异常和限制是否满足关闭条件的正式评价与决策。

**Normative status:** Research proposal

**Related concepts:** Sufficiency, Compliance Claim, Baseline

**Notes:** v0.1 不冻结具体 closure criteria。

### DBSE

**Working definition:** Document-Based Systems Engineering；以受控信息项、模板、关系和评审状态组织系统工程知识的工作方式。

**Normative status:** Working definition

**Related concepts:** Information Model, MBSE, Configuration Management

**Notes:** DBSE ≠ “用文档代替工程”；它是本研究进入形式化模型前的可审计基线。

### MBSE

**Working definition:** Model-Based Systems Engineering；以机器可解释模型作为重要工程信息载体，支持关联、查询、约束和分析。

**Normative status:** To be verified

**Related concepts:** Metamodel, SysML, Automation

**Notes:** MBSE ≠ “把已有文档画成 SysML 图”。

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
