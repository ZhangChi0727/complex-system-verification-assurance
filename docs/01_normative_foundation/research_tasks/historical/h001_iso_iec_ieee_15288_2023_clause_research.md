---
title: ISO/IEC/IEEE 15288:2023 Historical Clause Research Task
status: superseded
version: 1.0
baseline: historical-pre-v0.2
owner: research
last_updated: 2026-08-20
document_role: historical-task-specification
body_format: preserved-original
dependencies:
  - ../README.md
  - ../../standard_notes/iso_15288.md
  - ../../reviews/iso_15288_informal_review.md
---

> **Archive control:** This completed pre-v0.2 task specification is retained as research provenance. Its original body and numbering are preserved; current execution status and future work are governed by the parent task register and controlled source baseline.

# ISO/IEC/IEEE 15288:2023 Normative Research Task Specification

## 1. Task Purpose

对 **ISO/IEC/IEEE 15288:2023 — Systems and software engineering — System life cycle processes** 开展条款级研究，提取其中与本项目 **Complex System Verification Assurance Framework** 相关的规范性概念、过程、活动、信息关系和保证逻辑，并将其转化为可用于后续 DBSE / MBSE 研究的结构化知识。

本任务不是“总结 ISO 15288”，也不是“把标准内容抄进仓库”。

本任务的核心目标是回答：

> **ISO 15288 为我们的 Verification Assurance Framework 提供了哪些直接依据、哪些间接依据、哪些边界条件，以及哪些研究概念仍然属于我们自己的扩展。**

ISO 15288:2023 本身建立的是一个通用系统生命周期 process framework，适用于 system、system element 以及 system of systems；它明确不规定具体 lifecycle model、development methodology、modelling approach 或 verification technique。

因此，研究必须始终保持：

```
Standard
↓
Interpretation
↓
Framework Implication
↓
Research Proposal
```

四层分离。

------

# 2. Source Status

研究源：

```
ISO/IEC/IEEE 15288:2023
Systems and software engineering —
System life cycle processes
Second edition
2023-05
```

当前 PDF 为合法机构访问版本。

**严禁：**

- 将原 PDF 提交到公开 GitHub；
- 大段复制标准原文；
- 将标准中的 NOTE 当作强制 requirement；
- 将我们的 interpretation 写成“ISO 要求”；
- 将 `should`、`may` 与 `shall` 混为一谈。

ISO 15288 明确指出，标准中的强制性要求使用 `shall`，推荐使用 `should`，许可使用 `may`；同时 conformance 还取决于采用的是 outcome-based、task-based 还是 tailored conformance。

------

# 3. Primary Research Question

研究 ISO 15288 时，不要问：

> “它有没有我们的 V0、V1、V2……？”

而应该问：

> **ISO 15288 自己如何定义 system verification、validation、process application、evidence、traceability、configuration、information、assurance 和 MBSE？**

然后再比较：

> **这些内容如何支持、修改或否定我们当前 working framework？**

------

# 4. Required Research Outputs

本任务至少应形成以下三个主要产物。

## 4.1 Standard Study Note

创建或更新：

```
docs/01_normative_foundation/
standard_notes/
iso_15288.md
```

这是 ISO 15288 的主要条款研究记录。

------

## 4.2 Cross-Standard Matrix Update

更新：

```
docs/01_normative_foundation/
standards_map.md
```

把当前部分 `TBD` 替换为有依据的 ISO 15288 研究结论。

------

## 4.3 Normative Gap Candidates

更新：

```
docs/01_normative_foundation/
normative_gap_matrix.md
```

但只添加真正有意义的 gap，例如：

```
Framework concept:
Verification Strategy


ISO 15288:
Directly supported


Framework extension:
Oracle field not explicitly defined by ISO 15288
```

不要为了填表而制造 gap。

------

# 5. Extraction Model

每个重要条款都按以下模板研究。

```
## Clause X.X.X — Title


### Source Classification
- Normative / Informative
- shall / should / may / note


### Standard Intent
用自己的话说明该条款解决什么问题。


### Normative Objects
- process
- activity
- task
- artefact
- information item
- role
- result
- evidence
- traceability
...


### Inputs / Preconditions
标准明确或合理可识别的输入。


### Required / Recommended Activities
严格区分 shall / should / note。


### Outputs / Outcomes


### Relationships
与其他 process / artefact / requirement / baseline 的关系。


### Verification-Framework Implication
该条款对我们的 framework 有什么意义。


### Classification
- Direct normative support
- Indirect normative support
- Guidance
- Interpretation
- Research extension


### Open Questions
```

------

# 6. Priority Clause Set

不要逐页平均用力。

ISO 15288 中与本研究最相关的内容分成六个研究层级。

------

# 7. Layer A — Definitions and Conformance

首先研究：

```
Clause 3
Clause 4
```

重点术语：

- requirement
- system
- system element
- artefact
- information item
- traceability
- validation
- verification
- baseline
- process
- activity
- task

ISO 15288 对 verification 的定义是：通过 objective evidence 确认 specified requirements 得到满足；并说明 Verification 是把 system 或 system element 与 required characteristics 进行比较的一组活动。

Validation 则强调 specific intended use / application，以及系统是否能够在类似 operational environment 中完成 intended use、goals 和 objectives。

这里必须输出一个：

```
Verification vs Validation boundary
```

并明确：

```
Verification → specified requirements / characteristics
Validation   → intended use / stakeholder context
```

但不要简化成只有一句：

```
built right vs right system
```

因为后续 process clauses 比这更丰富。

------

# 8. Layer B — Process Architecture

重点研究：

```
5.6
5.7
5.8
```

尤其是：

```
5.8 Process application
5.8.2 iteration, recursion, concurrency
5.8.3 process views
```

这是研究 V0–V12 是否应该被理解为“顺序 workflow”的关键。

ISO 15288 明确指出：

- process 可以 iterative；
- recursive；
- concurrent；
- 图中的箭头不代表固定 temporal sequence。

并且 Verification 与 Integration 可以通过迭代逐渐增加对系统 conformance 的信心。

因此必须形成一项明确的 framework implication：

> **V0–V12 不应被描述为严格线性 lifecycle。**

后续更合理的表达应研究为：

```
Verification Activity Architecture
```

或：

```
Verification Process View
```

------

# 9. Layer C — Verification Core Process

这是本任务的核心。

完整研究：

```
6.4.9 Verification process
```

必须逐项提取：

```
Purpose
Outcomes
Prepare for verification
Perform verification
Manage results of verification
```

## 9.1 Verification Purpose

ISO 15288 明确将目的定义为：

- system；
- system element；
- artefact；

满足 specified requirements / characteristics 的 objective evidence。

特别注意：

> Verification object 不只是最终产品。

还包括：

- requirements；
- architecture description；
- design description；
- implemented system elements；
- life cycle processes。

因此我们的 Verification Object Model 后续必须覆盖这些类型。

------

# 10. Verification Preparation Extraction

重点研究 6.4.9.3(a)。

至少提取以下概念：

```
Verification Scope
Verification Action
Verification Constraint
Verification Method
Success Criteria
Verification Strategy
Verification Enabling System
Verification Environment
```

ISO 15288 明确要求识别 verification scope 和 actions，并指出 strategy 应描述：

- what will be verified；
- verification method；
- expected result；
- success criteria。

因此：

```
Verification Strategy
```

应从当前的：

```
Research proposal
```

调整为：

```
Normatively supported concept
```

但是我们的 VSR 中：

```
oracle
coverage obligation
independence
required evidence
```

等字段不能自动宣称全部来自 ISO 15288。

必须逐字段分类。

------

# 11. Verification Methods Taxonomy

ISO 15288 的 Verification Method taxonomy 必须单独记录。

标准列出：

```
Inspection
Analysis
Demonstration
Testing
```

其中 Analysis 包括：

```
modelling
simulation
analogy / similarity
```

Inspection 包括 peer review。

需要形成：

```
ISO15288 Verification Method Taxonomy
```

并明确：

```
Verification Method ≠ Verification Technique
```

例如：

```
Test
```

是 Method；

```
Boundary Value Analysis
State Transition Testing
Fault Injection
```

属于我们后续研究的 Technique / Pattern 层。

不要把这些概念混排。

------

# 12. Verification Strategy Extraction

完整研究：

```
6.4.9.3(a)(4)
```

重点总结 Verification Strategy 包含什么。

ISO 15288 的相关 NOTE 表明 strategy 涉及：

- verification scope；
- constraints；
- verification actions；
- method；
- enabling systems；
- lifecycle evidence points；
- risk/cost/schedule trade-off。

需要输出一个对照表：

| Proposed VSR Field  | ISO 15288 support               | Status             |
| ------------------- | ------------------------------- | ------------------ |
| scope               | direct                          | supported          |
| method              | direct                          | supported          |
| expected result     | direct                          | supported          |
| success criteria    | direct                          | supported          |
| enabling system     | direct                          | supported          |
| environment         | direct/related                  | supported          |
| configuration       | indirect                        | needs CM linkage   |
| oracle              | not explicit                    | research extension |
| coverage obligation | not explicit as current concept | research extension |
| independence        | not established here            | further study      |
| required evidence   | partial                         | interpretation     |

------

# 13. Verification Procedure and Execution

研究：

```
6.4.9.3(b)
```

提取：

- procedure；
- purpose；
- success criteria；
- expected result；
- method；
- enabling system；
- environment；
- resource；
- qualified personnel。

标准要求 procedure 包含这些内容。

执行逻辑应抽象为：

```
Perform Procedure
↓
Capture Result
↓
Compare Result with Expected Result
↓
Apply Success Criteria
↓
Determine Correctness
↓
Determine Confidence
```

ISO 15288 明确描述了这一执行逻辑。

这部分应与我们现有：

```
Observed Result
Expected Result
Acceptance Criterion
Oracle
```

进行映射。

------

# 14. Anomaly and Re-verification

研究：

```
6.4.9.3(c)
```

重点提取：

- verification result；
- anomaly；
- root cause；
- corrective action；
- problem resolution；
- re-verification；
- approval；
- traceability；
- baseline。

标准要求记录 verification results 和 anomalies，并说明失败后的问题处理可能要求 re-verification。

因此可以支持：

```
Anomaly
↓
Resolution
↓
Change
↓
Re-verification
```

但不要直接将：

```
Regression
```

等价为 ISO 原生术语。

当前应分类为：

```
Regression concept:
indirectly supported by change + re-verification logic
```

------

# 15. Approval and Closure

重点研究：

```
6.4.9.3(c)(3)-(5)
```

标准明确要求：

- approval authority agreement；
- maintain traceability；
- provide key artefacts for baselines。

因此：

```
Verification Closure
```

作为我们研究对象有明确依据。

但 ISO 并没有在这里直接定义一个叫：

```
Verification Closure Process
```

的 process。

所以必须标记：

```
Verification Closure
= framework abstraction based on ISO result management,
approval, traceability, and baseline handoff.
```

------

# 16. Layer D — Validation Process

完整研究：

```
6.4.11 Validation process
```

不是为了扩张研究范围，而是为了防止 Verification/Validation 混淆。

ISO 15288 对 Validation 的 purpose 是：

> system 在使用中满足 business/mission objectives、stakeholder needs and requirements，并在 intended operational environment 中实现 intended use。

Validation 也有：

```
scope
actions
methods
strategy
enabling systems
procedures
results
anomalies
traceability
baseline
```

等结构。

研究结果至少应形成：

```
Verification / Validation structural comparison
```

例如：

| Dimension   | Verification                     | Validation                               |
| ----------- | -------------------------------- | ---------------------------------------- |
| reference   | specified requirements           | intended use / stakeholder needs         |
| environment | defined verification environment | operational / representative environment |
| approval    | approval authority               | stakeholder confirmation                 |
| outcome     | requirements satisfied           | intended use satisfied                   |

------

# 17. Layer E — Supporting Technical Management Processes

Verification 不能孤立研究。

至少研究以下 process 与 Verification 的关系：

```
6.3.1 Project Planning
6.3.2 Project Assessment and Control
6.3.3 Decision Management
6.3.4 Risk Management
6.3.5 Configuration Management
6.3.6 Information Management
6.3.7 Measurement
6.3.8 Quality Assurance
```

重点不是完整总结这些 process，而是回答：

> **它们如何为 Verification 提供输入、约束、管理或 Evidence 控制？**

------

# 18. Configuration Management Extraction

重点研究：

```
6.3.5
```

特别提取：

- configuration item；
- unique identifier；
- baseline；
- change request；
- impact assessment；
- status accounting；
- configuration audit；
- verification of changes。

标准指出 requirements、models、system elements、services、baselines 等通常属于 configuration-managed items，并要求使用唯一标识。

标准还明确将 approved change 与 verification / validation 联系起来。

需要形成：

```
Configuration → Change → Impact → Verification → Baseline
```

关系模型。

------

# 19. Information Management Extraction

重点研究：

```
6.3.6
```

记录标准对于受控 engineering information 的要求。

Information Management 明确关注：

```
unambiguous
complete
verifiable
consistent
modifiable
traceable
presentable
```

并要求定义 information item 的：

- representation；
- responsibility；
- content；
- format；
- structure。

这部分是 DBSE Information Architecture 的核心依据。

同时必须记录：

> ISO 15288 不规定 information item 的具体 name / format / explicit content / medium；ISO/IEC/IEEE 15289 专门处理 life-cycle documentation。

因此输出一个：

```
Follow-up standard:
ISO/IEC/IEEE 15289
Priority: High
Reason: DBSE information-item definition
```

------

# 20. Layer F — Assurance Architecture

重点研究：

```
5.10 Assurance and quality characteristics
```

这是整个研究非常关键的部分。

ISO 15288 将 Assurance 与：

```
claim
confidence
evidence
argument
assurance case
```

联系起来。

标准指出 assurance case 是一个 auditable artefact，用 evidence 和 structured argument 支撑 claim，并强调 evidence 与 claim 之间通常不是直接关系。

因此我们的：

```
Claim
↓
Argument
↓
Evidence
```

模型具有明确标准支持。

必须记录：

```
Traceability ≠ Assurance Argument
```

因为 traceability 表示关联；

argument 表示为什么 evidence 足够支持 claim。

------

# 21. Evidence Extraction

从 5.10 和 6.4.9 中总结：

ISO 15288 对 evidence 的理解至少包括：

- test pass/fail results；
- quantitative measurements；
- qualitative evaluations；
- verification results；
- anomaly/deviation records；
- requirement satisfaction information。

但不要因此自行创建“ISO Evidence Taxonomy”。

应分类为：

```
Evidence examples provided by ISO 15288
```

不是：

```
complete normative evidence taxonomy
```

------

# 22. Annex B — Information Items

研究：

```
Annex B
```

注意：

> Annex B 是 informative，不是 normative。

重点提取 Verification 相关 example artefacts / information items。

标准列出：

```
Verified system
Verification records and reports
```

其中 records/reports 可包含：

- approach；
- criteria；
- results；
- discrepancies。

这可以用于验证我们 DBSE artifact list 是否合理。

但不能写成：

> “ISO 强制要求文件必须叫 Verification Report。”

------

# 23. Annex D — MBSE

重点研究：

```
Annex D
```

注意：

> Annex D 是 informative。

ISO 15288 将 MBSE 描述为 formalized application of modelling across the life cycle，并强调 model 可以成为关于 SoI 和 lifecycle processes 的主要知识源。

重点提取 MBSE 能支持：

- verification；
- validation；
- measurement；
- impact analysis；
- completeness；
- consistency；
- interface analysis；
- traceability；
- reuse。

尤其记录：

```
model query → impact analysis
model relations → completeness/consistency checking
validated models → surrogate V&V in some contexts
```

相关依据见 Annex D。

这与本项目：

```
DBSE
↓
Information Model
↓
MBSE
↓
Automated Query / Check / Impact Analysis
```

高度一致。

但必须标记：

```
Annex D = informative support
```

------

# 24. Verification Framework Mapping

完成条款研究后，必须对当前 working framework 做第一轮映射。

至少评价：

```
V0 Verification Planning
V1 Verification Basis Establishment
V2 Requirement Verifiability Analysis
V3 Verification Strategy Definition
V4 Verification Case Design
V5 Verification Procedure Development
V6 Verification Readiness
V7 Verification Execution
V8 Result Evaluation
V9 Anomaly Resolution
V10 Regression
V11 Coverage & Sufficiency
V12 Verification Closure
```

分类只能使用：

```
Directly Supported
Partially Supported
Indirectly Supported
Not Identified
Research Extension
Potential Conflict
```

不要使用简单：

```
Yes / No
```

------

# 25. Known Preliminary Mapping to Validate

当前可以作为研究假设，但必须由 Codex 自己对照条款确认：

| Framework Activity         | Preliminary status                         |
| -------------------------- | ------------------------------------------ |
| V0 Planning                | indirect / supporting process              |
| V1 Basis                   | framework abstraction                      |
| V2 Verifiability           | partial                                    |
| V3 Strategy                | direct                                     |
| V4 Case Design             | partial via verification actions           |
| V5 Procedure               | direct                                     |
| V6 Readiness               | partial via enablers/environment           |
| V7 Execution               | direct                                     |
| V8 Evaluation              | direct                                     |
| V9 Anomaly                 | direct + cross-process                     |
| V10 Regression             | indirect via change/re-verification        |
| V11 Coverage & Sufficiency | research gap                               |
| V12 Closure                | partial via approval/traceability/baseline |

Codex 的工作是验证或修正这张表，而不是照抄。

------

# 26. Concepts That Must Be Specifically Checked

必须逐一回答以下问题。

### Q1

ISO 15288 是否直接使用 `Verification Strategy`？

### Q2

Strategy 包含哪些明确字段？

### Q3

ISO 15288 的 Verification Methods 是什么？

### Q4

Review 是一级 Method，还是 Inspection 的一种形式？

### Q5

Verification Procedure 最低应包含什么？

### Q6

Expected Result 与 Success Criteria 如何关系？

### Q7

是否出现类似 Oracle 的概念？

### Q8

是否存在显式 Verification Coverage 概念？

### Q9

是否定义 Verification Sufficiency？

### Q10

是否要求双向 traceability？

### Q11

Evidence 被如何使用？

### Q12

Assurance Case 在 Verification 中是什么角色？

### Q13

如何处理 anomaly、change 和 re-verification？

### Q14

Configuration baseline 如何与 Verification 交互？

### Q15

MBSE 对 Verification 提供什么支持？

------

# 27. Required Evidence Classification

每个研究结论必须标记来源类型：

```
NORMATIVE
INFORMATIVE
INTERPRETATION
FRAMEWORK IMPLICATION
RESEARCH PROPOSAL
```

例如：

```
Claim:
Verification methods include inspection, analysis, demonstration and testing.


Classification:
NORMATIVE / clause task + NOTE clarification


Framework implication:
Generic Verification Method taxonomy can initially use these four categories.


Research extension:
Boundary Value Analysis remains a Verification Technique, not an ISO method.
```

------

# 28. No Over-claim Rule

以下写法禁止：

```
ISO 15288 requires V0–V12.
ISO 15288 requires Oracle.
ISO 15288 requires Requirement Coverage = 100%.
ISO 15288 defines Regression Testing.
ISO 15288 mandates MBSE.
```

除非找到明确条文。

正确表达例如：

```
ISO 15288 directly requires defining a verification strategy.
Our V3 activity is therefore directly supported in concept,
although its detailed information model is a research extension.
```

------

# 29. Copyright Rule

仓库中：

- 不复制长段标准原文；
- 优先使用 paraphrase；
- 保留 clause number；
- 必要时只保留极短术语或 phrase；
- 不提交 PDF；
- 不提交截图。

格式建议：

```
Source:
ISO/IEC/IEEE 15288:2023, 6.4.9.3(a)(4)


Interpretation:
The verification strategy integrates scope, constraints,
verification actions, methods, enablers, and lifecycle evidence needs.
```

------

# 30. Suggested `iso_15288.md` Structure

```
# ISO/IEC/IEEE 15288:2023 Research Notes


1. Metadata
2. Scope and Applicability
3. Conformance Model
4. Core Terminology
5. Process Architecture
6. Verification Process
   6.1 Purpose
   6.2 Outcomes
   6.3 Preparation
   6.4 Methods
   6.5 Strategy
   6.6 Procedure
   6.7 Execution
   6.8 Result Evaluation
   6.9 Anomaly Management
   6.10 Approval
   6.11 Traceability
   6.12 Baseline Interaction
7. Validation Process
8. Configuration Management Relationship
9. Information Management Relationship
10. Planning / Risk / Measurement / QA Relationships
11. Assurance and Assurance Cases
12. Artefacts and Information Items
13. MBSE Implications
14. Mapping to Current Verification Framework
15. Normative Gaps
16. Research Extensions
17. Follow-up Standards
18. Open Questions
```

------

# 31. Required Final Summary

Codex 完成 ISO 15288 研究后必须给出一个最终结论表：

| Concept                | ISO 15288 status                      | Framework consequence              |
| ---------------------- | ------------------------------------- | ---------------------------------- |
| Verification           | Direct                                | baseline terminology               |
| Validation             | Direct                                | maintain separation                |
| Verification Strategy  | Direct                                | promote from proposal              |
| Verification Method    | Direct                                | adopt initial taxonomy             |
| Verification Technique | Not explicit as our taxonomy          | retain research layer              |
| Procedure              | Direct                                | DBSE support                       |
| Expected Result        | Direct                                | information-model support          |
| Success Criteria       | Direct                                | study against Acceptance Criterion |
| Oracle                 | Not identified                        | research extension                 |
| Traceability           | Direct                                | core relationship                  |
| Evidence               | Direct                                | core information object            |
| Assurance Case         | Informative/direct conceptual support | evidence architecture support      |
| Configuration          | Direct cross-process support          | mandatory framework dependency     |
| Anomaly                | Direct                                | workflow support                   |
| Re-verification        | Direct                                | basis for regression research      |
| Coverage               | TBD                                   | major research topic               |
| Sufficiency            | TBD                                   | major research topic               |
| Closure                | Partial                               | framework abstraction              |
| MBSE                   | Informative                           | supports model-based realization   |

------

# 32. Definition of Done

本任务只有在以下条件满足后才算完成：

1. `iso_15288.md` 已完成；
2. Verification Process 6.4.9 已逐任务分析；
3. Validation Process 6.4.11 已完成对照；
4. Configuration / Information / Assurance / MBSE 关系已研究；
5. 所有结论区分 normative / informative / interpretation；
6. `standards_map.md` 中 ISO 15288 列已有真实研究结果；
7. `normative_gap_matrix.md` 中只加入经过论证的 gap；
8. 已形成 V0–V12 第一轮映射；
9. 已识别哪些 framework concepts 应升级、保留或修改；
10. 没有把标准原文或受版权保护材料提交到仓库；
11. 没有将 NOTE、interpretation 或 research proposal 写成强制标准要求；
12. 已明确下一步需要由 ISO/IEC/IEEE 24748-1 和 15289 补充研究的问题。

------

# 33. Core Research Principle

整个任务必须遵守：

> **不要证明我们的框架是对的，而要允许 ISO 15288 改变我们的框架。**

如果标准与当前假设冲突：

```
Standard
wins over
current framework hypothesis
```

如果标准没有回答：

```
mark as gap / research space
```

不要自行补齐。

------

# 34. Expected Research Value

完成本任务后，我们应该第一次能够把仓库中的概念分成：

```
ISO 15288 directly supported
↓
ISO 15288 indirectly supported
↓
ISO 15288 informative guidance
↓
Our interpretation
↓
Our research extension
```

这将成为后续：

```
ISO 24748-1
↓
ARP4754B
↓
ARP4761A
↓
DO-178C / DO-254 / DO-297
```

继续叠加规范证据的基础。

最终目标不是建立一个“ISO 15288 流程复刻”，而是回答：

> **一个产品无关、可用于复杂系统 Verification Assurance 的框架，哪些部分已经被国际系统工程标准明确支持，哪些部分还需要航空开发保证标准补充，哪些部分则构成本研究真正需要提出和论证的方法学扩展。**

------
