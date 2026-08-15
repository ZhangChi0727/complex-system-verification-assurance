---
title: Initial Research Outline
status: superseded
version: 0.0
baseline: pre-v0.1
owner: research
last_updated: 2026-08-15
dependencies: []
---

> Historical design input retained for provenance. This document is not a normative baseline; its standard-related statements and proposed framework elements remain unverified unless promoted into the controlled v0.1 workspaces with identifiable sources.

# 复杂系统验证保证框架研究大纲
## ——基于 DBSE/MBSE 的 Verification Assurance Framework 及 DCAS 领域实例化

### 1. 研究定位

#### 1.1 建议标题

**中文主标题：**

**面向复杂系统的验证保证框架研究——基于国际系统工程与民机开发保证规范的 DBSE/MBSE 方法**

**英文建议：**

**A Verification Assurance Framework for Complex Systems: From Document-Based to Model-Based Verification Engineering**

若后期论文特别强调民机适航，可改为：

**面向民用航空复杂系统的模型化验证保证方法研究——以 DCAS 为应用案例**

但研究过程中建议始终保持“**通用方法论为主体，DCAS 为实例**”，避免最终成果退化为一份 DCAS 测试手册。

---

# 2. 研究背景与问题定义

现有 DCAS《显示系统集成验证》资料已经形成较丰富的工程知识，包括：

- Verification Method 的选择；
- TC/AC/IC/RC 与 TP/AP/IP/RP 文档体系；
- Requirement—Case—Procedure 的追溯；
- 边界值、迟滞、分辨率、源选择等用例设计；
- 告警、有效性、CRC、EDE、重构保持等专项验证；
- 实验环境及自动化工具；
- CP—RDIU—IMA—IDU 数据链排故；
- PR 管理、回归与结果记录。

现有流程也已经规定受控测试文件、受控构型和受控产品作为验证输入，并产生测试日志、PR、ITM/VTM 以及集成/验证报告。

同时，现有资料已经形成较明确的 Verification Case 数据结构，包括 Requirement ID、Verification Method、Detail Steps、Expected Result、Verification Procedure、Verification Site、Coverage Analysis 等字段。

因此，当前问题并不是“没有验证实践”，而是：

> **已有大量局部验证经验，但缺少一个能够解释这些活动为何存在、如何组织、何时充分以及如何形成符合性证据的统一 Verification Assurance Framework。**

本研究拟解决的核心矛盾是：

**工程经验丰富，但方法论层、证据论证层和模型化层不足。**

---

# 3. 总体研究目标

本研究的最终目标是建立一套：

> **标准可追溯、过程可执行、证据可审计、规则可检查、模型可实现、领域可复用的复杂系统 Verification Assurance Framework。**

具体目标包括：

1. 从国际通用系统工程规范和民机开发保证规范中提取 Verification 的规范性要求；
2. 建立产品无关的复杂系统 Verification Lifecycle；
3. 定义 Verification Activity、Information Item、Role、Gate、Traceability 和 Evidence 的标准化 DBSE 工作流；
4. 建立 Verification Strategy 和 Verification Sufficiency 的系统决策机制；
5. 建立多维 Verification Coverage Model；
6. 建立 Requirements—Activities—Evidence—Claims 的证据架构；
7. 建立可复用的 Verification Pattern Library；
8. 将 DBSE 信息模型逐步映射为 MBSE Verification Metamodel；
9. 建立自动一致性检查、覆盖检查和影响分析能力；
10. 以 DCAS 为主要 domain profile，验证该框架的工程适用性；
11. 进一步通过 ARINC 615A 等不同类型系统验证其跨产品复用能力。

---

# 4. 核心研究问题

建议将研究问题正式定义为以下八项。

### RQ1：Verification 的规范性基础是什么？

不同国际标准对于 Verification、Validation、Development Assurance、Safety Assurance、Compliance Evidence 的定义和要求之间是什么关系？

### RQ2：复杂系统 Verification 的完整生命周期是什么？

一项 Requirement 从进入 Verification Process 开始，到最终形成可关闭证据，经历哪些 Activity、Decision Gate 和 Information Item？

### RQ3：如何选择 Verification Strategy？

针对不同 Requirement 类型、安全等级、验证层级和系统架构，如何系统确定：

**Level + Method + Technique + Environment + Coverage + Evidence？**

### RQ4：什么叫“验证充分”？

Requirement Coverage = 100% 是否足够？

如何建立多维 Coverage / Sufficiency Model？

### RQ5：Verification Evidence 如何形成符合性论证？

如何由：

**Requirement → Verification Result**

提升为：

**Compliance Claim → Argument → Evidence？**

### RQ6：哪些测试设计技术具有产品无关性？

边界值、状态迁移、组合逻辑、故障注入、源选择、鲁棒性等是否可以抽象为 reusable verification patterns？

### RQ7：DBSE Verification Workflow 如何模型化？

哪些对象、属性和关系需要成为 MBSE 元素，哪些信息继续作为外部文档存在？

### RQ8：该框架如何证明具有工程有效性？

通过 DCAS、ARINC 615A 或其他系统实例，验证方法论是否具有：

**Completeness、Traceability、Repeatability、Scalability 和 Reusability。**

---

# 5. 规范与标准基础

标准应按层级组织，而不能简单罗列。

## 5.1 第一层：通用系统生命周期规范

### ISO/IEC/IEEE 15288:2023
**Systems and software engineering — System life cycle processes**

作为整个研究的最高层生命周期过程框架。

该标准覆盖系统从 conception、development 到 production、utilization、support 和 retirement 的完整生命周期，并建立统一的 system life-cycle process framework。

重点检索：

- Verification Process
- Validation Process
- Technical Processes
- Configuration Management
- Information Management
- Decision Management
- Risk Management

### ISO/IEC/IEEE 24748 系列

尤其：

**ISO/IEC/IEEE 24748-1:2024**

用于解释系统和软件生命周期管理以及 15288 的工程化应用。

---

# 5.2 第二层：通用系统工程方法

### INCOSE Systems Engineering Handbook

重点关注：

- Verification
- Validation
- V-model
- Requirements traceability
- Technical reviews
- Systems integration
- MBSE

INCOSE 已存在利用 SysML/MBSE 建立 Verification & Validation test framework，并关联 test plans、procedures 等外部验证文档的研究实例，这将是后续 MBSE 架构的重要参考。

### NASA Systems Engineering Handbook

作为公开且高度工程化的参考体系。

NASA 明确区分：

**Product Verification：证明实现产品符合设计需求；**

**Product Validation：确认验证后的产品在预期环境下满足 intended use。**

NASA 还提供专门的 V&V Plan Outline，可用于反向分析一个成熟 Verification Plan 应包含哪些信息项。

---

# 5.3 第三层：民机 Aircraft/System Development Assurance

### SAE ARP4754B / EUROCAE ED-79B

这是 DCAS 应用场景最重要的系统开发保证基础之一。

ARP4754B 于 2023 年发布，针对实现 aircraft/system functions 的 aircraft and system development lifecycle，同时明确将软件、电子硬件和 IMA 的详细开发分别交给 DO-178C、DO-254 和 DO-297。

研究重点：

- Aircraft/System Requirements
- Requirements Validation
- Design Implementation Verification
- Development Assurance
- Integration
- Unintended Behavior
- FDAL / IDAL
- Independence
- Development Assurance Planning
- Verification Data

**重要原则：**

本研究应优先研究 **ARP4754B**；现有项目若实际基于 ARP4754A，则将 A 版作为项目适用基线和历史对照。

---

# 5.4 第四层：System Safety

### SAE ARP4761A / EUROCAE ED-135

ARP4761A 同样于 2023 年发布，用于 civil aircraft、systems 和 equipment 的 safety assessment。

重点研究：

- FHA
- PSSA
- SSA
- Safety Requirement
- Failure Condition
- Safety Objective
- DAL allocation
- Safety evidence

主要作用不是直接告诉我们“测试用例怎么设计”，而是回答：

> **Verification rigor 为什么需要不同？Safety Requirement 从哪里来？Verification 是否形成足够 safety evidence？**

---

# 5.5 第五层：Item-Level Assurance

### RTCA DO-178C / EUROCAE ED-12C

软件保证参考。

DO-178C 目前仍是 airborne software 的核心软件设计保证和产品保证文件，并具有 DO-331、DO-332、DO-333 等模型化、面向对象和形式化方法补充文件。

研究重点包括：

- Requirements-based verification
- Verification independence
- Structural coverage
- MC/DC
- Derived requirements
- Tool qualification
- Life-cycle data

其价值之一是帮助我们**正确区分系统级验证与软件结构覆盖概念**。

### RTCA DO-254 / EUROCAE ED-80

复杂电子硬件保证参考。

其 Verification 内容包括 requirement、simulation 和 hardware test 等活动。

### RTCA DO-297 / EUROCAE ED-124

对于 DCAS 中 IMA/GPM 等架构尤其重要。

DO-297 面向 IMA platform、hosted application、integrator 等角色以及其集成和认证关系。

### DO-331

对于后续 Verification Model / executable model 特别值得研究。

但必须明确：

> DO-331 是 DO-178C/DO-278A 的 Model-Based Development and Verification Supplement，不应被直接等价为系统 MBSE 标准。

---

# 5.6 第六层：特定领域补充标准

根据研究需要逐步加入：

- DO-160：设备环境鉴定；
- ARINC 429 / 664 / 825：接口；
- ARINC 661：座舱显示系统接口；
- ARINC 653：分区执行环境；
- ARINC 615A：数据加载；
- 人因与告警相关 FAA/EASA/RTCA 文件；
- 网络安全 DO-326A / ED-202A 等。

这些不构成通用 Verification Framework 的骨架，而是 **Domain-Specific Constraint Sources**。

---

# 6. 文献检索关键词体系

建议不要只搜索 “system verification”，而是形成关键词矩阵。

## 6.1 Verification 基础理论

- Systems Verification
- System Validation
- Verification and Validation
- V&V Methodology
- Requirements-Based Verification
- Complex System Verification
- Verification Engineering
- Verification Process
- Verification Planning
- Verification Strategy
- Verification Management

## 6.2 Verification Assurance

- Verification Assurance
- Development Assurance
- Assurance Framework
- Assurance Process
- Assurance Case
- Safety Assurance
- Certification Evidence
- Compliance Evidence
- Compliance Demonstration
- Objective Evidence

## 6.3 Evidence 与论证

- Evidence Architecture
- Evidence Management
- Verification Evidence
- Certification Evidence
- Compliance Argument
- Assurance Case
- Safety Case
- Goal Structuring Notation
- GSN
- Claims Arguments Evidence
- Structured Assurance Case

## 6.4 Coverage 与充分性

- Verification Coverage
- Verification Completeness
- Verification Sufficiency
- Requirements Coverage
- Functional Coverage
- Interface Coverage
- Scenario Coverage
- State Coverage
- Transition Coverage
- Failure Mode Coverage
- Configuration Coverage
- Test Adequacy Criteria

## 6.5 Verification Technique

- Boundary Value Analysis
- Equivalence Partitioning
- Decision Table Testing
- State Transition Testing
- Combinatorial Testing
- Pairwise Testing
- MC/DC
- Fault Injection
- Robustness Testing
- Negative Testing
- Model Checking
- Formal Verification
- Worst-Case Analysis
- Timing Verification

## 6.6 DBSE / MBSE

- Document-Based Systems Engineering
- DBSE
- Model-Based Systems Engineering
- MBSE Verification
- Model-Based Verification
- Verification Metamodel
- SysML Verification
- SysML Test Case
- Model-Based V&V
- Digital Engineering
- Digital Thread
- Semantic Traceability
- Verification Knowledge Graph

## 6.7 航空

- ARP4754B Verification
- Development Assurance Verification
- Aircraft System Verification
- Avionics System Verification
- Certification Verification
- DAL Verification
- FDAL Verification
- Integrated Modular Avionics Verification
- DO-297 Integration
- DO-178C Verification
- DO-254 Verification

---

# 7. 总体层次架构

建议最终形成六层体系。

```text
L0  Normative Foundation
        ↓
L1  Verification Assurance Framework
        ↓
L2  Verification Lifecycle / DBSE Workflow
        ↓
L3  Verification Information & Evidence Model
        ↓
L4  MBSE Verification Model
        ↓
L5  Domain Profiles
        ├── DCAS
        ├── ARINC 615A
        └── Future Domains
```

---

# 8. L0——规范基础层

目的：

> 建立每项方法论规则的 normative rationale。

这一层不定义 DCAS 测试方法，只回答：

- Verification 是什么；
- Validation 是什么；
- 为什么需要独立性；
- 为什么需要配置管理；
- 为什么需要 traceability；
- 为什么需要 safety-derived rigor；
- Verification record 为什么需要保存；
- 什么可以作为 evidence；
- 哪些属于系统层，哪些属于 Item 层。

主要成果：

### Standard Requirement Matrix

例如：

| Framework Rule | ISO 15288 | ARP4754B | ARP4761A | DO-178C | DO-254 |
|---|---|---|---|---|---|
| Verification planning | ✓ | ✓ | 关联 | ✓ | ✓ |
| Requirement traceability | ✓ | ✓ | ✓ | ✓ | ✓ |
| Independence | 原则 | DAL相关 | 安全相关 | 明确目标 | 明确目标 |
| Configuration control | ✓ | ✓ | ✓ | ✓ | ✓ |
| Structural coverage | — | — | — | ✓ | 特定方法 |

这个矩阵的意义是防止我们再次出现：

> “某工业实践究竟是适航要求、行业通用原则，还是企业内部约定？”

---

# 9. L1——Verification Assurance Framework

这是整个研究的核心理论层。

建议定义：

## Verification Assurance =

**对 Verification Process、Verification Evidence 及其充分性进行系统性保证，使得相关 compliance claim 可以由客观、受控、可追溯和可复核的 evidence 支持。**

其核心结构：

```text
Requirement
      ↓
Verification Obligation
      ↓
Verification Strategy
      ↓
Verification Activity
      ↓
Verification Evidence
      ↓
Coverage / Sufficiency Evaluation
      ↓
Compliance Claim
```

这里应首次正式引入三个当前工业文档中不够明确的对象：

### Verification Obligation

“该 Requirement 需要证明什么？”

### Verification Strategy

“准备在哪里、用什么方法、以什么充分性证明？”

### Compliance Claim

“最终准备声明什么已经得到证明？”

---

# 10. L2——DBSE Verification Lifecycle

建议 Level-1 流程定义为：

```text
V0 Verification Planning
        ↓
V1 Verification Basis Establishment
        ↓
V2 Requirement Verifiability Analysis
        ↓
V3 Verification Strategy Definition
        ↓
V4 Verification Case Design
        ↓
V5 Verification Procedure Development
        ↓
V6 Verification Readiness
        ↓
V7 Verification Execution
        ↓
V8 Result Evaluation
        ↓
V9 Anomaly Resolution
        ↓
V10 Regression
        ↓
V11 Coverage & Sufficiency Assessment
        ↓
V12 Verification Closure
```

每一项 Activity 均采用统一 DBSE 模板。

### Activity Template

**Activity ID**

**Purpose**

**Normative Basis**

**Inputs**

**Entry Criteria**

**Responsible Role**

**Supporting Roles**

**Process**

**Decision Rules**

**Outputs**

**Records**

**Traceability**

**Independence Requirements**

**Configuration Requirements**

**Exit Criteria**

---

# 11. DBSE 各阶段详细内容

## V0 Verification Planning

定义：

- Scope
- Organization
- Responsibility
- Verification levels
- Environment
- Methods
- Toolchain
- Configuration policy
- Independence
- Anomaly management
- Evidence management
- Reporting
- Schedule

输出：

**Verification Plan**

---

## V1 Verification Basis Establishment

识别：

- Regulations
- Certification basis
- Stakeholder requirements
- Aircraft requirements
- System requirements
- Safety requirements
- ICD
- Architecture
- Configuration constraints

输出：

**Verification Basis Baseline**

---

## V2 Requirement Verifiability Analysis

对每条 Requirement 分析：

- necessity；
- correctness；
- unambiguity；
- consistency；
- feasibility；
- verifiability；
- measurable acceptance criteria；
- allocation；
- derived requirements；
- safety attributes。

输出：

**Validated / Verification-Ready Requirement**

这里应严格区分：

**Requirement Validation**

和

**Design Verification**。

---

## V3 Verification Strategy Definition

这是整个框架最关键的新增环节。

针对一个 Verification Obligation，定义：

**Verification Level**

**Verification Method**

**Verification Technique**

**Verification Environment**

**Verification Configuration**

**Acceptance Oracle**

**Coverage Obligation**

**Independence**

**Required Evidence**

形成：

### Verification Strategy Record — VSR

VSR 应成为 Case 设计的直接输入。

---

# 12. Verification Level Model

不使用简单的：

**System Test / Equipment Test**

二分法。

建议定义：

```text
Aircraft
↓
System
↓
Subsystem / Function
↓
Equipment / LRU
↓
Hosted Application
↓
Software / Hardware Item
```

每条 Requirement 显式关联：

**Requirement Allocation Level**

和：

**Verification Execution Level**

然后研究二者关系。

核心原则：

> Verification 应在能够产生充分且可信证据的适当集成层级实施，而不是机械地“越高层越好”或“越底层越好”。

---

# 13. Verification Method Model

一级 Method 建议采用：

- Test
- Analysis
- Inspection
- Demonstration
- Review（是否独立保留需进一步结合标准 taxonomy 决定）
- Service / Prior Evidence Reuse（作为 evidence source 单独研究）

研究重点不是名称，而是：

> 什么类型 Requirement 允许什么 Method，什么情况下 Method Combination 才充分？

例如：

**Worst-case timing**

可能采用：

**Analysis + Test**

而不是简单二选一。

---

# 14. Verification Technique Model

Method 与 Technique 分离。

例如：

### Test Techniques

- Boundary Value
- Equivalence Partition
- State Transition
- Decision Table
- Combinatorial
- Fault Injection
- Robustness
- Stress
- Scenario-Based
- Timing Measurement

### Analysis Techniques

- Worst-Case Analysis
- Safety Analysis
- Reliability Analysis
- Numerical Analysis
- Simulation
- Model Checking
- Formal Proof

这能够解决当前指南中：

**Test / MC/DC / Boundary Value / Source Selection**

处于不同抽象层级却混在一起的问题。

---

# 15. V4——Verification Case Design

建立统一 Case 结构：

```text
Verification Case
│
├─ Verification Objective
├─ Requirement
├─ Verification Strategy
├─ Preconditions
├─ Configuration
├─ Stimulus
├─ State
├─ Expected Response
├─ Acceptance Criterion
├─ Oracle
├─ Coverage Contribution
└─ Evidence Requirement
```

特别加入当前资料不够显式的：

### Oracle

回答：

> Expected Result 的正确性依据是什么？

可能来源：

- requirement；
- reference model；
- ICD；
- independent calculation；
- architectural model；
- safety analysis；
- certified reference；
- calibrated measurement。

---

# 16. V5——Verification Procedure Development

Case 说明：

> **证明什么。**

Procedure 说明：

> **具体怎么做。**

需要严格分开：

Verification Intent

与：

Execution Implementation。

这与现有 TC→TP 思路一致，但需要将依赖、配置、工具版本和测量精度进一步正式化。

---

# 17. V6——Verification Readiness

增加正式：

### Verification Readiness Review — VRR

检查：

- requirement baseline；
- case approved；
- procedure approved；
- environment qualified/accepted；
- product configuration frozen；
- tool version controlled；
- instrumentation calibrated；
- known anomalies；
- personnel authorization；
- evidence storage ready。

这是把当前“测试前确认事项”提升成正式 Gate。

---

# 18. V7——Execution

必须产生原始证据：

- log；
- measurement；
- screenshot；
- packet capture；
- tool output；
- execution metadata；
- operator；
- timestamp；
- environment configuration；
- product configuration。

原则：

> **Result 不是 Evidence 的全部，Result 是对 Evidence 的判断。**

---

# 19. V8——Result Evaluation

形成：

**Observed Result**

与：

**Expected Result**

比较。

输出状态至少：

- Pass
- Fail
- Blocked
- Invalid
- Not Run

不建议简单使用 Pass / Fail 二元模型。

---

# 20. V9——Anomaly Management

建立：

```text
Anomaly
↓
Classification
↓
Reproduction
↓
Localization
↓
Root Cause
↓
Disposition
↓
Change
↓
Impact Analysis
↓
Regression
↓
Closure
```

当前 DCAS 材料已有很好的工程基础，例如要求 PR 不仅记录问题现象，还记录环境对比、抓包情况和排故过程。

这部分应从经验规则抽象为通用 **Anomaly Evidence Workflow**。

---

# 21. V10——Regression

不能仅规定：

> “修改后重新测试”。

需要研究：

### Regression Scope Determination

依据：

- changed requirement；
- changed architecture；
- changed software/hardware；
- changed ICD；
- impacted interfaces；
- dependency graph；
- previous anomaly；
- safety impact。

MBSE 阶段可以进一步实现自动 Impact Analysis。

---

# 22. V11——Coverage & Sufficiency

这是研究重点之一。

建立多维 Coverage Model：

```text
Requirement Coverage
Function Coverage
Interface Coverage
State Coverage
Transition Coverage
Boundary Coverage
Input Domain Coverage
Scenario Coverage
Failure-Mode Coverage
Configuration Coverage
Source Coverage
Timing Coverage
Safety Objective Coverage
Structural Coverage
```

核心研究问题：

> 不同 Requirement Type 对应哪些 Coverage Obligation？

例如：

**Range Requirement**

→ Boundary + Equivalence Coverage

**State Requirement**

→ State + Transition Coverage

**Fault-Tolerance Requirement**

→ Failure Mode + Reconfiguration Coverage

**Boolean Logic**

→ Decision/Condition Coverage

这样才能真正定义“Complete”。

---

# 23. V12——Verification Closure

建立正式 Closure Gate。

关闭条件至少包含：

- requirements verification complete；
- required coverage satisfied；
- open anomalies disposition acceptable；
- regression complete；
- configuration baseline established；
- traceability complete；
- evidence approved；
- outstanding limitations documented。

输出：

### Verification Accomplishment / Closure Report

这比单纯生成“Verification Report”更具有方法论意义。

---

# 24. L3——Verification Information Model

这一层是 DBSE → MBSE 的桥梁。

定义核心信息对象：

```text
Requirement
Verification Obligation
Assurance Objective
Verification Strategy
Verification Activity
Verification Method
Verification Technique
Verification Case
Verification Procedure
Verification Environment
Configuration
Stimulus
System State
Expected Result
Observed Result
Oracle
Coverage Obligation
Coverage Result
Evidence
Anomaly
Change
Regression Activity
Compliance Claim
```

核心关系：

```text
Requirement
   └─ creates → Verification Obligation

Verification Obligation
   └─ satisfiedBy → Verification Strategy

Verification Strategy
   ├─ selects → Method
   ├─ selects → Technique
   ├─ selects → Level
   └─ defines → Coverage Obligation

Verification Case
   └─ realizes → Verification Strategy

Procedure
   └─ implements → Verification Case

Execution
   └─ produces → Evidence

Evidence
   └─ supports → Compliance Claim
```

---

# 25. Evidence Architecture

建立：

```text
                 Compliance Claim
                        │
                     Argument
                        │
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
 Requirement        Verification     Coverage
   Evidence           Evidence       Evidence
        │               │               │
        └───────────────┼───────────────┘
                        ▼
                Configuration Evidence
```

研究重点：

### Traceability ≠ Argumentation

Traceability 回答：

> 证据在哪里？

Argumentation 回答：

> 为什么这些证据足够？

最终可研究与：

- Assurance Case
- Safety Case
- Claims–Arguments–Evidence
- GSN

的结合。

---

# 26. Verification Pattern Library

建议将通用设计经验形成 Pattern。

统一模板：

**Pattern ID**

**Name**

**Intent**

**Applicable Requirement Type**

**Preconditions**

**Input Domain**

**Construction Rule**

**Coverage Obligation**

**Oracle**

**Expected Evidence**

**Known Failure Modes**

**Applicability Limits**

初始 Pattern 可包括：

### BVA-01
Boundary Value Verification

### EQP-01
Equivalence Partition Verification

### LOG-01
Boolean Logic Verification

### STM-01
State Transition Verification

### SRC-01
Priority / Source Selection Verification

### TIM-01
Timing Constraint Verification

### ROB-01
Invalid / Abnormal Input Verification

### FIT-01
Fault Injection Verification

### RED-01
Redundancy / Reconfiguration Verification

### INT-01
Integrity Mechanism Verification

### IFV-01
Interface Verification

### CFG-01
Configuration-Dependent Verification

---

# 27. L4——MBSE Verification Framework

MBSE 阶段不是把 Excel 画成 SysML 图。

目标是：

> **把 Verification 中需要计算、追溯、约束和自动检查的知识转变成机器可理解的模型。**

主要模型包括：

### Requirement Model

### Architecture Model

### Verification Model

### Safety Model

### Configuration Model

### Evidence Model

### Coverage Model

### Anomaly / Change Model

---

# 28. MBSE 自动检查能力

未来模型至少应支持：

### Rule 1

Requirement 没有 Verification Strategy → ERROR

### Rule 2

Verification Case 没有 Requirement → ERROR

### Rule 3

Test 方法没有 Environment → ERROR

### Rule 4

Case 没有 Oracle → WARNING/ERROR

### Rule 5

Requirement 发生变更 → 所有相关 Evidence 转为 Suspect

### Rule 6

Anomaly 未关闭 → Verification Closure 受阻

### Rule 7

Coverage Obligation 未满足 → Requirement 不允许 Closed

### Rule 8

Configuration 与 Execution Evidence 不一致 → Result Invalid

这些规则才是 MBSE 带来的真正工程价值。

---

# 29. L5——DCAS Domain Profile

DCAS 不再承担方法论定义功能。

它只包含：

### DCAS Architecture

- IDU
- IMA/GPM
- HF/HA
- CP
- RDIU
- OMS
- 429
- 664
- 825

### DCAS Verification Patterns

- Numeric display；
- display resolution；
- LSB；
- hysteresis；
- validity；
- source selection；
- CAS alert；
- alert inhibition；
- reconfiguration；
- data retention；
- CRC；
- EDE；
- BIT；
- IMA hosted function；
- GUI/display；
- bus integration。

现有 PPT 的大量内容均迁移到这里。

例如飞行阶段抑制已经包含“先出现告警后进入抑制阶段”和“先进入抑制阶段后触发告警”两种事件顺序，实际上是非常好的 **State/Transition Verification** 实例。

EDE 中的 MIH、STS、Request Number、ES Index、T1/T2 和 CRC 则可以成为 **Integrity Verification Pattern** 的 DCAS 实例。

---

# 30. 产品无关层与 DCAS 层的隔离原则

以后任何内容都必须先问：

> 换成汽车 EPS 后，这一规则还成立吗？

如果成立：

→ **Generic Verification Framework**

如果不成立：

→ **DCAS Domain Profile**

例如：

| 内容 | 归属 |
|---|---|
| Boundary Value Analysis | Generic |
| State Transition | Generic |
| Fault Injection | Generic |
| Verification Traceability | Generic |
| ARINC 429 SSM | DCAS |
| A664 FSB | DCAS |
| IDU Reconfiguration | DCAS |
| Flight Phase Inhibit | DCAS Case |
| CRC Integrity Verification | Generic Pattern |
| 某 SYN CRC polynomial | DCAS Instance |

这是整个研究必须坚持的原则。

---

# 31. 研究方法

建议采用五种研究方法结合。

### 1. Standards Analysis

提取国际标准中的：

- Process；
- Objective；
- Activity；
- Information Item；
- Assurance Requirement。

### 2. Industrial Practice Reverse Engineering

以当前 DCAS 材料为对象，提取实际：

- Workflow；
- Artifact；
- Rule；
- Pattern；
- Tool；
- Evidence。

### 3. Gap Analysis

比较：

```text
Normative Requirement
        vs
Current Industrial Practice
        vs
Proposed Framework
```

### 4. Metamodel Engineering

建立 Verification Information Metamodel。

### 5. Case Study Validation

采用：

- DCAS；
- ARINC 615A；
- 可选第三领域

验证框架复用性。

---

# 32. 实施阶段

## Phase 0——Baseline

整理当前 DCAS 工业实践。

成果：

**DCAS Verification Practice Baseline**

---

## Phase 1——Literature & Standards Review

系统研究：

- ISO 15288；
- ISO 24748；
- INCOSE；
- NASA；
- ARP4754B；
- ARP4761A；
- DO-178C；
- DO-254；
- DO-297；
- MBSE Verification 论文。

成果：

**Normative Foundation Report**

---

## Phase 2——Normative Gap Analysis

建立：

**Standard → Objective → Existing Practice → Gap → Proposed Rule**

成果：

**Verification Normative Gap Matrix**

---

## Phase 3——DBSE Process Architecture

正式定义：

V0–V12。

成果：

**Verification Process Handbook V1.0**

---

## Phase 4——Information Architecture

定义：

- artifact；
- fields；
- relationships；
- ownership；
- state transitions；
- traceability。

成果：

**Verification Information Model**

---

## Phase 5——Coverage & Evidence Architecture

重点建立：

**Coverage Model**

和：

**Compliance Evidence Model**

成果：

**Verification Sufficiency & Evidence Framework**

---

## Phase 6——Pattern Library

从 DCAS 中抽象出 generic verification patterns。

成果：

**Verification Pattern Catalogue**

---

## Phase 7——DCAS Re-instantiation

把原始 167 页培训材料重新分类。

目标不是简单改写，而是：

```text
Generic Methodology
        ↓
DCAS Rule
        ↓
DCAS Pattern
        ↓
Concrete Example
        ↓
Tool Execution Guide
```

成果：

**DCAS Verification Domain Guide**

---

## Phase 8——MBSE Metamodel

将 DBSE 信息模型映射到：

- SysML；
- SysML v2；
- 或其他适合的 metamodel。

成果：

**Model-Based Verification Metamodel**

---

## Phase 9——Automation

开发：

- traceability checking；
- coverage checking；
- completeness checking；
- impact analysis；
- case generation assistance；
- evidence generation；
- report generation。

成果：

**Verification Automation Prototype**

---

## Phase 10——Validation

选取典型 DCAS Requirement Sets：

- 数值显示；
- 告警；
- 重构；
- EDE；
- 性能/时序。

并选取一个非 DCAS 案例，如 ARINC 615A。

比较：

- 原流程；
- DBSE Framework；
- MBSE Framework。

评价：

- Completeness；
- Reviewability；
- Traceability；
- Change impact detection；
- Reuse；
- Automation；
- Evidence quality。

---

# 33. 预期研究成果体系

最终建议形成以下成果树：

```text
Complex System Verification Assurance Framework
│
├─ 1. Normative Foundation
│
├─ 2. Verification Process Model
│
├─ 3. Verification Information Model
│
├─ 4. Verification Strategy Method
│
├─ 5. Coverage & Sufficiency Model
│
├─ 6. Evidence / Compliance Argument Model
│
├─ 7. Verification Pattern Library
│
├─ 8. DBSE Handbook
│
├─ 9. MBSE Metamodel
│
├─ 10. Automated Verification Rules
│
└─ Domain Profiles
     ├─ DCAS
     └─ ARINC 615A
```

---

# 34. 建议重点形成的核心文档

研究过程中不应一开始追求“一本大指南”，而应首先形成几个相对独立的受控基线：

### D1
**Standards & Literature Baseline**

### D2
**Verification Terminology & Ontology**

### D3
**Verification Lifecycle Process Specification**

### D4
**Verification Information Item Specification**

### D5
**Verification Strategy & Method Selection Guide**

### D6
**Verification Coverage Model**

### D7
**Verification Evidence Architecture**

### D8
**Verification Pattern Catalogue**

### D9
**MBSE Verification Metamodel**

### D10
**DCAS Verification Domain Profile**

最终再将这些整合成：

### D11
**Complex System Verification Assurance Handbook**

---

# 35. 研究中特别需要避免的几个陷阱

### 陷阱一：把测试等于 Verification

Verification 包含但不限于 Test。

### 陷阱二：把 Requirement Coverage = 100% 等于充分

必须研究 Coverage Obligation。

### 陷阱三：直接从当前 PPT 进入 SysML

会得到“模型化的旧流程”，而不是正确的 MBSE Verification Framework。

### 陷阱四：把 DO-178C 概念直接上移到系统层

例如 MC/DC、structural coverage 等必须保留其适用层级和规范语境。

### 陷阱五：将 DCAS 工程知识写入通用规则

必须严格维护 Generic / Domain separation。

### 陷阱六：只建立 Traceability，不建立 Evidence Argument

“需求有 Case”并不能自动推出“需求已被充分证明”。

### 陷阱七：过早开发自动化工具

Automation 必须建立在稳定的信息模型和规则模型之后。

---

# 36. 对研究成功的判据

这个项目是否成功，不应以“写了多少页指南”衡量。

至少应满足以下判据：

**Normative Traceability**

每项核心 Framework Rule 均能够说明来源或工程 rationale。

**Process Completeness**

Verification 从 Planning 到 Closure 全生命周期闭合。

**Information Completeness**

每个 Activity 的输入、输出和状态均被定义。

**Evidence Completeness**

每项 compliance claim 可以追溯至受控证据。

**Coverage Explicitness**

“充分”可以用规则说明，而非仅凭专家主观判断。

**Modelability**

核心信息和关系能够进入 MBSE metamodel。

**Automation Capability**

模型能够支持一致性、覆盖和影响分析。

**Domain Independence**

核心 Framework 中不依赖 DCAS 特定术语。

**Domain Applicability**

DCAS 实践能够自然实例化到 Framework 中。

**Cross-Domain Reuse**

至少一个非 DCAS 案例能够复用主体框架。

---

# 37. 第一阶段的近期工作建议

当前最优先的工作不应是继续编写 DCAS 教程，也不应开始 SysML 建模。

建议依次完成：

1. **建立 Standards Baseline；**
2. **建立 Verification Terminology Baseline；**
3. **完成现有 DCAS 167 页材料的知识分类；**
4. **建立 Normative Gap Matrix；**
5. **定义 V0–V12 DBSE Level-1 Workflow；**
6. **定义每个 Activity 的统一信息模板；**
7. **建立 Verification Strategy Record；**
8. **建立 Verification Information Metamodel V0.1；**
9. **建立 Coverage Taxonomy V0.1；**
10. **选取 5～10 条典型 DCAS Requirements 作为第一轮 validation cases。**

只有完成上述工作后，才建议进入正式 MBSE 架构设计。

---

# 38. 核心研究逻辑

整个项目可以最终浓缩成一条主线：

**Standards**

↓

**Verification Obligations**

↓

**DBSE Process**

↓

**Verification Strategy**

↓

**Cases / Procedures / Analysis / Inspection**

↓

**Controlled Execution**

↓

**Evidence**

↓

**Coverage & Sufficiency**

↓

**Compliance Argument**

↓

**Verification Closure**

↓

**Information Model**

↓

**MBSE Implementation**

↓

**Automation**

↓

**DCAS / Other Domain Instantiation**

这条链条应当成为后续所有研究工作的主干。

---

## 39. 一句话研究定位

> **本研究不是研究“DCAS 测试用例怎么写”，而是研究复杂工程系统如何依据规范，把需求系统地转化为充分、受控、可追溯、可审计的验证证据，并进一步通过 MBSE 将这一过程形式化、关联化和自动化；DCAS 是用于验证这一方法论的主要工业案例。**

补充内容：按照我们现在这套结构，**论文和教程应该被视为同一研究工程的两个不同“发布视图”**，而不是两套分别维护的内容。这样反而是这个仓库结构最重要的收益之一。

论文回答的是：

> **我们提出了什么新问题、构建了什么方法、相比既有方法改进在哪里、如何验证其有效性。**

教程回答的是：

> **一个工程师具体应该如何按这套方法开展复杂系统验证工作。**

它们共享同一套底层研究资产：标准基线、术语体系、DBSE 工作流、Verification Information Model、Coverage Model、Evidence Architecture、Pattern Library、DCAS 案例和验证结果；只是组织方式和叙事目的不同。

论文最终可以形成大致这样的逻辑：

**Introduction → Related Work / Standards → Problem & Gap → Proposed Verification Assurance Framework → DBSE Workflow → Information / Evidence / Coverage Model → MBSE Realization → DCAS Case Study → Cross-domain Validation → Discussion → Conclusion**

也就是说，论文的核心贡献应该集中在几件事：首先把分散在系统工程、开发保证和测试工程中的验证要求整合成统一 Verification Assurance Framework；其次提出从 Verification Obligation 到 Strategy、Activity、Evidence、Coverage、Compliance Claim 的完整信息链；然后证明 DBSE 工作流能够被进一步模型化；最后用 DCAS 和其他案例验证框架的完整性、可复用性和工程价值。

而教程的结构会更接近：

**为什么要验证 → 验证依据是什么 → 如何规划 → 如何分析需求 → 如何制定策略 → 如何设计 Case → 如何编写 Procedure → 如何准备环境 → 如何执行 → 如何处理异常 → 如何回归 → 如何评价覆盖 → 如何关闭验证 → 常见 Verification Patterns → DCAS 专项实例 → 工具与模型化实践。**

这里就可以大量保留你现在 DCAS 材料中的优秀工程内容，比如源选择、迟滞、告警抑制、EDE、CRC、重构、排故等，只是它们不再承担“定义通用方法论”的任务，而是作为 Pattern 的教学案例。

更进一步，我建议我们把最终成果看成 **四级产品**：

1. **Research Repository**：真正的单一事实源，保存标准映射、模型、数据、案例、脚本和研究历史。
2. **Academic Paper / Thesis**：提炼研究问题、创新点、方法、实验和结论。
3. **Engineering Handbook / Tutorial**：把方法转化为可执行的工程流程和案例教学。
4. **Machine-readable Framework**：后期形成 metamodel、schema、规则检查器以及 MBSE/自动化工具。

第四项其实很重要。否则最终仍然只是“论文 + 一本 PDF”，没有真正实现我们所说的 DBSE→MBSE。

论文与教程也不应该是一一对应的章节关系。例如论文可能只有一章介绍 Verification Pattern Library，但教程可能要用几十页分别讲 Boundary、State Transition、Fault Injection、Timing 等；反过来，论文会详细讨论 research gap、validity threats 和 cross-domain evaluation，而教程基本不需要展开这些学术内容。

我还建议仓库未来增加两个很薄的发布目录：

```
publications/
├─ paper/
│  ├─ outline.md
│  ├─ manuscript/
│  ├─ figures/
│  └─ tables/
│
└─ handbook/
   ├─ outline.md
   ├─ chapters/
   ├─ figures/
   └─ examples/
```

但**不要在里面直接复制核心内容长期维护**。例如 Coverage Taxonomy 的权威版本仍然只存在于：

```
docs/05_coverage_and_evidence/
```

论文和教程只是引用、改写和重组它。否则几年后非常容易出现“论文版定义 A，教程版定义 B，模型里又是定义 C”的 configuration drift。

从研究成果的价值来看，我甚至认为可以期望形成不止一篇论文。比较自然的拆分可能是：

- 第一篇：**Complex System Verification Assurance Framework / DBSE Workflow**
- 第二篇：**Verification Information & Evidence Model / MBSE Metamodel**
- 第三篇：**Verification Coverage and Sufficiency Model**
- 应用型文章：**DCAS Case Study**

当然这取决于研究深度和实际成果，目前不需要人为拆论文。

所以最终可以把我们的目标概括成一句话：

> **仓库是“知识与模型本体”，论文是对其学术贡献的证明，教程是对其工程使用方法的解释，MBSE/工具则是对其可执行性的实现。**

如果这个架构始终保持住，那么你现在投入在 DCAS 工程经验整理上的工作不会因为以后转向论文而浪费；反过来，论文阶段做的标准分析和方法论研究，也会直接提升教程的严谨性。
