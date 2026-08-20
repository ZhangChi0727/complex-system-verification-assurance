---
title: ISO/IEC/IEEE 24748-2:2024 and SAE ARP4754B Historical Research Round
status: superseded
version: 1.0
baseline: historical-pre-v0.2
owner: research
last_updated: 2026-08-20
document_role: historical-task-specification
body_format: preserved-original
dependencies:
  - ../README.md
  - ../../standard_notes/iso_24748_2_targeted_review.md
  - ../../standard_notes/sae_arp4754b.md
  - ../../reviews/ISO-24748-2--SAE-ARP4754B-External-Informal-Review.md
---

> **Archive control:** This completed pre-v0.2 research-round specification is retained as provenance. Its original combined-task body and numbering are preserved; it is not part of the current ordered queue.

# Normative Foundation Next Research Round

## ISO/IEC/IEEE 24748-2:2024 Targeted Review + SAE ARP4754B Full Research Task Specification

### Document Status

```
title: Normative Foundation Next Research Round
status: working
version: 0.1
baseline_dependency: repository baseline after PR #3
research_scope:
  - ISO/IEC/IEEE 24748-2:2024 targeted applicability review
  - SAE ARP4754B full clause-level research
next_expected_source:
  - SAE ARP4761A
```

------

# 1. Purpose of This Research Round

本轮研究包含两个性质不同的任务。

```
Task A
ISO/IEC/IEEE 24748-2:2024
Targeted Applicability & Delta Review
             ↓
Freeze / correct Generic SE interpretation


Task B
SAE ARP4754B
Full Clause-Level Research
             ↓
Introduce Civil Aircraft Development Assurance layer
```

本轮不得重新推翻已经完成并评审的：

```
ISO/IEC/IEEE 15288:2023
ISO/IEC/IEEE 24748-1:2024
```

除非新的 source evidence 明确说明当前 interpretation 有误。

本轮的核心研究问题是：

> **Generic systems-engineering verification semantics 在进入 civil-aircraft development assurance 后，会增加哪些 assurance obligations、rigor、independence、coverage、evidence 和 certification-related constraints？**

------

# PART I — ISO/IEC/IEEE 24748-2:2024 TARGETED REVIEW

# 2. Source Positioning

研究源：

```
ISO/IEC/IEEE 24748-2:2024
Systems and software engineering —
Life cycle management —
Part 2:
Guidelines for the application of
ISO/IEC/IEEE 15288
Second edition
2024-03
```

其正式标题直接表明这是 15288 的 application guidance。

Clause 1 说明该标准指导：

- system concepts；
- life-cycle concepts；
- organizational concepts；
- project concepts；
- process concepts；
- conformance/adaptation；

并从 strategy、planning、organization 和 project application 等角度解释 ISO 15288 的应用。

更加关键的是 6.1 明确：

> 该标准用于帮助理解 ISO 15288 provisions 如何应用，guidance text 不引入新的 requirements。

因此本标准在当前 repository 中的角色应定义为：

```
Source Role:
Supporting Application Guidance


Not:
Independent Verification Assurance Requirement Source
```

------

# 3. Why This Is a Targeted Review Rather Than a Full Research Slice

已经完成的 ISO 15288 + ISO 24748-1 研究基本解决：

```
Verification semantics
Process / Activity / Task
Iteration / recursion / concurrency
Life Cycle Model
Stage
Process View
Entry / Exit Criteria
Decision Gate
Lifecycle tailoring / instantiation
```

24748-2 大量内容是在逐个解释如何实际应用 15288 的 processes，其目录也直接按 agreement、organizational、technical-management 和 technical processes 展开。

因此本轮不得开展：

> “重新把整份 24748-2 从头到尾做一遍 standards summary。”

而只检查：

> **24748-2 是否产生足以改变当前 Verification Assurance Framework 的 delta。**

------

# 4. Required Output

创建：

```
docs/01_normative_foundation/
standard_notes/
iso_24748_2_targeted_review.md
```

不要将其命名为完整：

```
iso_24748_2.md
```

除非研究过程中发现它确实产生大量独立 framework implications，需要升级研究级别。

文档状态建议：

```
research_type: targeted-applicability-review
source_role: supporting-guidance
baseline_status: supporting-source
```

------

# 5. Six Mandatory Research Questions

24748-2 本轮只需要系统回答以下六个问题。

## Q24748-2-01

是否改变我们对 ISO 15288 Verification Process 的解释？

## Q24748-2-02

是否改变：

```
Verification Assurance Process View
```

以及当前 V0–V12 mixed ontology？

## Q24748-2-03

是否改变：

```
V6 Verification Readiness
V12 Verification Closure
```

作为 Composite Gate 的定位？

## Q24748-2-04

是否要求调整：

```
Lifecycle / Process Tailoring and Instantiation Record
```

的 candidate information fields？

## Q24748-2-05

是否为以下对象提供新的、有价值的 application semantics？

```
Verification Strategy
Verification Planning
Enabling Systems
Configuration
Information
Integration
Evidence
Decision Gates
```

## Q24748-2-06

是否能够：

```
close
partially address
clarify
or leave unchanged
```

当前任何 `ISO-Gxx / LC-Gxx` gap？

------

# 6. Mandatory Clauses to Review

不需要逐章平均研究。

优先分析：

```
1       Scope
5       Application concepts
6.1     Overview
6.2     Application strategy
6.4     Application of life-cycle concepts
6.4.2   Decision gates
6.6     Application of project concepts
6.7.4   Technical management processes
6.7.5   Technical processes
6.7.5.4 System realization
6.7.5.4.3 Integration
6.7.5.4.4 Verification
6.7.5.4.6 Validation, if relevant
6.8     Conformance and adaptation
Annex C MBSSE, only if it changes current MBSE interpretation
```

其他内容只有在与六个 research questions 直接相关时才提取。

------

# 7. Verification Process Application Review

重点研究：

```
6.7.5.4.4
Application of verification process
```

24748-2 明确重申 Verification：

- 可在生命周期中多次实施；
- 应按照 verification strategy 开展；
- 会受到 system type、life-cycle stage 和 entry/exit decision 的影响。

并重新列举 Inspection、Analysis、Demonstration 等 verification methods。

Codex 应回答：

> 这些内容是否只是对 ISO 15288 既有 semantics 的 operational clarification？

如果是，则标：

```
DELTA:
Clarification only
Framework change: No
```

不要复制成一套新的 Method taxonomy。

------

# 8. Planning Integration Review

24748-2 对 Project Planning 给出了一个非常值得吸收的 application interpretation：

plans 应考虑 implementation、integration、verification、transition、validation 的：

- scope；
- tasks；
- methods；
- tools；
- measures；
- risks；
- resources；

并将其他 process strategies 作为 Project Planning 输入。

应评估这是否意味着：

```
V0 Verification Planning
```

需要更加明确地建模成：

```
Verification-specific strategy/planning
       ↓
integrated into
Project / Development Planning
```

而不是孤立的 plan。

如果当前 DBSE workflow 已经表达此语义，则只增强 source mapping。

------

# 9. Decision Gate Review

24748-2 明确说明：

- life-cycle stage 不决定 process 的固定执行顺序；
- stage manager 根据 stage purpose/outcomes 与 entry/exit criteria 选择合适 processes；
- milestones 和 decision gates 用于管理 decisions；
- artefacts 为 gate 提供 decision-making information。

Clause 6.4.2 进一步把 decision gate 与 management control 联系起来，并明确不同 lifecycle approaches 可以采用不同 review/gate cadence。

必须检查：

```
V6 / V12 Composite Gate
```

是否需要改变。

预期分类：

```
Current architecture:
Supported / strengthened


Not:
Replaced by ISO-defined Verification Gate
```

禁止写：

```
ISO 24748-2 defines V6.
ISO 24748-2 defines Verification Closure.
```

------

# 10. Enabling-System Implication

24748-2 对 enabling systems 提供了比 15288 更工程化的说明：

- enabling systems 可能支持任何 lifecycle process；
- 可能在或不在 project boundary 内；
- 但始终属于 project span of interest；
- enabling-system 与 SoI schedules 应协调；
- enabling-system requirements 需要被识别并满足。

检查是否应该强化当前：

```
Verification Environment
Verification Enabling System
```

之间的区分。

潜在 Framework implication：

```
Verification Environment
may rely on
one or more Verification Enabling Systems


Enabling System
has its own:
requirements
configuration
availability
life-cycle dependencies
```

但只有确实影响 information model 时才修改。

------

# 11. Configuration / Evidence Relationship

24748-2 对 configuration audit 的解释值得记录。

其 functional audit 可检查：

- verification results 是否与 specification 一致；
- planned verification procedures 是否执行；
- verification results 是否与 authorized configuration documentation 一致。

因此检查当前 Evidence Architecture 是否需要增加关系：

```
Verification Evidence
        ↕
Verified Configuration
        ↕
Configuration Baseline
```

如果已有类似关系，则标记为 additional supporting guidance。

不要创建：

```
ISO-required Evidence Architecture
```

------

# 12. Targeted Gap Review

至少重新检查：

```
ISO-G01 Verification independence
ISO-G02 Coverage
ISO-G03 Sufficiency
ISO-G04 Oracle
ISO-G05 Regression
ISO-G06 Closure
ISO-G07 Information-item schema
ISO-G08 Model evidence


LC-G01 Gate semantics
LC-G02 Review taxonomy
LC-G03 Process-view provenance
LC-G04 Lifecycle/process instantiation
```

允许状态：

```
UNCHANGED
CLARIFIED
PARTIALLY ADDRESSED
CLOSED
```

`CLOSED` 必须非常谨慎。

------

# 13. 24748-2 Exit Criterion

Targeted Review 完成后必须给一个明确 verdict：

```
Framework Delta:
None / Minor / Significant


Need full ISO 24748-2 research:
Yes / No


Recommended role:
Supporting source / Core source
```

若结论是：

```
Framework Delta: Minor
Need full research: No
```

则立即结束 24748-2 研究，不继续扩张 scope。

预计其 repository 定位为：

```
Supporting Application Guidance
Reviewed
No standalone normative framework layer
```

------

# PART II — SAE ARP4754B FULL RESEARCH

# 14. Research Purpose

在完成 24748-2 targeted review 后，立即进入：

```
SAE ARP4754B
Guidelines for Development of Civil Aircraft and Systems
Revision B
2023-12
```

该文件为 SAE Aerospace Recommended Practice，Revision B 于 2023-12 发布并 supersede ARP4754A。

ARP4754B 是本项目第一次正式从：

```
Generic Systems Engineering
```

进入：

```
Civil Aircraft Development Assurance
```

的核心规范来源。

------

# 15. Critical Source Classification

必须从一开始保持一个重要边界：

ARP4754B **不是法规本身**。

标准自己明确：

> 内容属于 recommended practices，不应被解释为 regulatory requirements，并承认认证申请人可以采用其他可接受方法。

因此研究分类不能简单沿用 ISO 的：

```
NORMATIVE SHALL
```

而建议新增 source strength：

```
ARP RECOMMENDATION
CERTIFICATION-RELATED RECOMMENDATION
DEFINITION
OBJECTIVE
PROCESS GUIDANCE
APPENDIX OBJECTIVE / DAL-DEPENDENT APPLICABILITY
INTERPRETATION
FRAMEWORK IMPLICATION
RESEARCH PROPOSAL
```

尤其不能写：

> “ARP4754B legally requires X.”

正确表达应是：

> “ARP4754B recommends X for civil-aircraft/system development assurance; certification applicability depends on the certification basis and accepted means of compliance.”

------

# 16. Primary Research Goal

ARP4754B 研究必须回答：

> **Civil-aircraft development assurance 给 Generic Verification Framework 增加了什么？**

而不是写一份通用“ARP4754B 摘要”。

特别关注：

```
Development Assurance
FDAL / IDAL
Process Independence
Requirements Validation
Implementation Verification
Verification Coverage
Verification Sufficiency
Safety Requirements
Derived Requirements
Unintended Behavior
Configuration Control
Process Assurance
Certification Evidence
Modification Impact
Reuse of Evidence
Aircraft/System/Item hierarchy
```

------

# 17. Required Outputs

创建：

```
docs/01_normative_foundation/
standard_notes/
sae_arp4754b.md
```

更新：

```
docs/01_normative_foundation/standards_map.md
docs/01_normative_foundation/normative_gap_matrix.md
docs/00_overview/terminology.md
docs/03_dbse_workflow/README.md
templates/verification_strategy_record.md
```

如确实有依据，可新增：

```
templates/development_assurance_record.md
```

或新的 candidate information item。

但：

> **不要为了体现研究量而随意新增 schema。**

先提取，再决定。

------

# 18. ARP4754B Research Layers

建议按八个研究层进行。

```
A. Scope & Development Assurance
B. Development Assurance Planning
C. Aircraft/System Development Architecture
D. Safety / DAL Interface
E. Requirements Capture & Validation
F. Implementation Verification
G. CM / Process Assurance / Evidence
H. Modification / Reuse / Change Impact
```

------

# 19. Layer A — Scope and Development Assurance

重点研究：

```
1
1.1
1.2
1.4
2.2
```

ARP4754B Scope 明确包含：

- requirements validation；
- verification of design implementation；
- safety；
- certification；
- product assurance。

而 1.2 进一步定义 Development Assurance 是一种 process-based approach，用于建立足够 confidence，使可能影响航空器安全的 development errors 被限制。

必须形成一张：

```
ISO Assurance
vs
ARP4754B Development Assurance
```

对照。

至少比较：

```
purpose
claim/confidence
development error
safety relationship
rigor
process assurance
verification
validation
certification role
```

------

# 20. Terminology Delta

特别提取：

- Assurance
- Development Assurance
- Development Error
- Requirement
- Validation
- Verification
- Traceability
- Independence
- Process Independence
- FDAL
- IDAL
- Safety Requirement
- Derived Requirement
- Unintended Behavior

ARP4754B 对 Requirement 的定义特别值得注意：

> Requirement 是 function specification 中可被 validation、且 implementation 可针对其进行 verification 的可识别元素。

ARP4754B 又明确：

```
Validation
= determination that requirements are correct and complete


Verification
= evaluation of implementation of requirements
  to determine they have been met
```



必须和 ISO 15288 terminology 做差异分析，不要简单覆盖 ISO 定义。

------

# 21. Verification Object Boundary

这是重点研究问题。

ISO 15288 的 Verification object 可以包括：

```
system
system element
artefact
requirements
architecture/design artefacts
```

而 ARP4754B 的术语明确强调：

```
Validation
→ requirements


Verification
→ implementation of requirements
```

必须研究：

> 这是否意味着 aviation specialization 中应把 `Requirements Verification` 与 `Implementation Verification` 更严格地区分？

不要提前认定冲突。

可能结果是：

```
Generic ISO layer:
Verification may apply to artefacts.


ARP4754B specialization:
requirements correctness/completeness is handled
primarily under Requirements Validation,
while Implementation Verification demonstrates
the implementation satisfies validated requirements.
```

这很可能直接影响 Framework ontology。

------

# 22. Layer B — Development Assurance Planning

完整研究：

```
Section 3
```

ARP4754B planning 不只是 project planning。

它要求考虑：

- requirements；
- FDAL / IDAL；
- development life-cycle relationships；
- sequencing；
- feedback mechanisms；
- transition criteria；
- development environment；
- methods/tools；
- development standards；
- integral process plans。

Table 1 更明确把：

- Requirements Capture；
- Requirements Validation；
- Implementation Verification；
- Configuration Management；
- Process Assurance；

作为 Development Assurance Planning elements。

因此必须研究：

> Generic V0 Verification Planning 是否应该在 aviation profile 中作为 Development Assurance Plan 的一个组成部分，而不是独立顶层 plan？

------

# 23. Transition Criteria / Gate Relationship

Section 3.2.2 很重要。

ARP4754B 明确把：

- lifecycle checkpoints；
- reviews；
- program phases；
- gates；
- maturity expectations；
- technical/process entrance criteria；
- exit criteria；
- open issues；

联系起来。

这将第一次给：

```
V6
V12
```

提供 aviation-specific gate semantics。

需要比较：

```
ISO 24748-1/2 generic gate
vs
ARP4754B development-assurance transition criteria
```

注意仍不要自动创造：

```
mandatory VRR
```

除非 Section 5.5 明确支持特定 review。

------

# 24. Layer C — Aircraft/System/Item Development Architecture

研究：

```
Section 4
4.1
4.2–4.6
```

尤其关注：

```
Aircraft
→ System
→ Item
```

信息和 verification obligation 如何向下分配、向上返回。

ARP4754B 明确说明 generic development process 是一个方便讨论的 framework，并不意味着唯一 preferred method；实际 development 可以 iterative/concurrent，同时结合 top-down 和 bottom-up。

这与当前 non-linear Process View 架构兼容。

------

# 25. System ↔ Item Information Flow

完整研究：

```
4.6.1
```

尤其关注：

```
System process → Item process
Item process → System process
```

ARP4754B 明确要求/建议在 system/item 之间传递：

- allocated requirements；
- DAL；
- independence constraints；
- system verification activities to be performed at item level；
- derived requirements；
- item-level verification evidence；
- problem/change data；
- limitations/configuration constraints；
- proposed item verification activities to be done at system level。

这是当前 Framework 中非常重要的新对象。

必须研究是否需要：

```
Verification Credit
Verification Delegation
Verification Allocation
```

作为独立关系。

------

# 26. Layer D — Development Assurance Level / Safety Interface

研究：

```
5.1
5.2
```

但注意：

Revision B 已把 FDAL/IDAL assignment 的详细 activities 转移给 ARP4761A，ARP4754B 主要保留 general principles。

因此当前只研究：

> DAL 如何改变 Verification/Validation assurance rigor。

不要尝试完整重建 FDAL/IDAL assignment algorithm。

------

# 27. Process Independence

这是当前 `ISO-G01` 的高优先级研究对象。

ARP4754B 对 Process Independence 给出明确定义：

> 通过 separation of responsibilities，由 activity performer 之外的人完成 objective evaluation，从而降低 development error likelihood。

同时明确指出：

- validation process independence；
- verification process independence；

可以由 FDAL 决定。

Requirements Validation：

- FDAL A/B 推荐 process independence。

Implementation Verification：

- Level A requirements 推荐 independence；
- Level B safety requirements 推荐 independence。

因此：

```
ISO-G01 Verification independence
```

很可能第一次从：

```
Open
```

进入：

```
Domain-specific / Assurance-level-dependent support
```

但注意：

> 不要把 ARP4754B independence 直接提升为所有复杂系统的 Generic rule。

更合理：

```
Generic Framework:
Independence Requirement = optional strategy dimension


Aviation Profile:
Applicability derived from FDAL / objective
```

------

# 28. Appendix A Must Be Treated as a Core Research Source

Appendix A 是本轮极其重要的研究材料。

它提供：

```
Process Objective
FDAL Applicability
Independence
Output
System Control Category
```

的矩阵。

例如 Implementation Verification Objective 5.1 明确涉及：

> verification methods/procedures sufficiency

并提供：

> evidence of verification procedure sufficiency。

Appendix A 还使用：

```
R*
R
A
N
```

表示：

- recommended with process independence；
- recommended；
- as negotiated；
- not required for certification。

这对我们的“assurance obligation”模型非常重要。

------

# 29. New Candidate Object — Assurance Applicability

必须研究是否需要把 Verification Strategy 从：

```
requirement
→ method
→ environment
→ criteria
```

扩展成：

```
Verification Obligation
       ↓
Assurance Applicability
       ↓
FDAL / safety relevance
       ↓
Independence
       ↓
Method / Procedure
       ↓
Evidence Control
```

候选字段：

```
assurance_level:
objective_applicability:
process_independence_required:
system_control_category:
certification_credit_intent:
```

但这些字段只能在研究后决定。

------

# 30. Layer E — Requirements Capture

研究：

```
5.3
```

重点：

- requirement classes；
- safety requirements；
- derived requirements；
- maintenance requirements；
- modeling requirements。

尤其研究：

```
Derived Requirement
```

如何反馈到 higher level，以及其 functional/safety impact 如何被评估。

这是未来：

```
Requirement Provenance
Verification Obligation
Change Impact
```

的重要输入。

------

# 31. Requirements Validation

完整研究：

```
5.4
```

ARP4754B 将 Requirements Validation 定义成：

> 确保 specified requirements 足够 correct 和 complete，以满足 customers/users/suppliers/maintainers/Certification Authorities 等 stakeholder needs。

研究必须拆开：

```
Correctness
Completeness
Validation Approach
Validation Method
Validation Data
Independence
```

这很可能直接提升我们：

```
V1 Verification Basis
V2 Requirement Verifiability Analysis
```

的本体设计。

------

# 32. Validation Methods

ARP4754B 给出的 Validation Methods 包括：

- traceability；
- analysis；
- modeling；
- test；
- similarity；
- engineering review；

同时要求考虑：

- intended functions；
- unintended behaviors。

必须注意：

> **Validation Method taxonomy ≠ Verification Method taxonomy。**

不要再使用一个通用 `method` enum 同时覆盖二者而不加 context。

------

# 33. Validation Data

研究：

```
5.4.7
```

尤其提取：

```
Validation Plan
Validation Matrix
Validation Summary
Supporting Data
Assumptions
```

Validation Plan 需要定义如何证明 requirements correct/complete 以及如何管理 assumptions。

这可能形成：

```
Requirement Validation Evidence
```

作为独立 evidence class。

------

# 34. Layer F — Implementation Verification

这是 ARP4754B 本轮最重要的 section。

完整研究：

```
5.5
```

ARP4754B 明确：

> Implementation Verification 的目的，是确认每一级 implementation 满足 specified requirements。

5.5.1 又明确 Verification：

- confirms intended functions correctly implemented；
- confirms requirements satisfied；
- ensures safety-analysis conclusions remain correct for implemented system。

必须与 ISO 15288 的 Verification purpose 做 cross-standard comparison。

------

# 35. Verification Planning

完整提取：

```
5.5.4
```

ARP4754B 明确要求 planning 涵盖：

- roles/responsibilities；
- design/verification independence；
- configuration；
- special test equipment/facilities；
- method per requirement；
- DAL consideration；
- success criteria；
- procedure sufficiency；
- credit from other levels；
- dependent activity sequence；
- verification data；
- verification environment。

这对当前 `Verification Strategy Record` 是第一次非常强的 domain-level field validation。

必须逐字段做：

```
Current VSR Field
↓
ARP4754B Equivalent
↓
Direct / Partial / No support
↓
Aviation Profile requirement?
```

------

# 36. Verification Methods Taxonomy

ARP4754B 5.5.5 使用：

```
Inspection / Review
Analysis
Testing or Demonstration
Similarity / Service Experience
```



这与 ISO 15288：

```
Inspection
Analysis
Demonstration
Testing
```

并不完全相同。

必须建立：

## Cross-Standard Method Taxonomy Comparison

而不是选择其中一个覆盖另一个。

特别研究：

```
Similarity / Service Experience
```

到底属于：

- Method；
- Analysis subtype；
- Evidence reuse strategy；

还是 aviation-specific method family。

------

# 37. Coverage — Major Research Breakthrough Candidate

当前 `ISO-G02 Verification coverage` 一直处于 open。

ARP4754B 5.5.5.2.2 直接出现：

```
Coverage Analysis
```

并说明它用于判断 requirements 在 development 和 verification activities 中被 address 的程度，通常通过 traceability 实现。

必须非常谨慎地分析：

> 这是否只是 Requirement Coverage？

还是：

> 能否支持更一般的 Verification Coverage concept？

不要因为出现 `Coverage Analysis` 就宣布：

```
ISO-G02 CLOSED
```

更可能是：

```
ARP-specific support for requirements-oriented coverage
```

------

# 38. Sufficiency — Another Major Candidate

Appendix A Objective 5.1 明确写：

> Verification methods and procedures are sufficient

并要求：

> Evidence of verification procedure sufficiency。

这是我们 V11 `Coverage & Sufficiency Assessment` 第一次获得非常直接的航空 assurance 支持。

必须深入回答：

```
What does ARP mean by sufficient?
How is sufficiency demonstrated?
Is traceability enough?
What evidence demonstrates sufficiency?
How does FDAL affect sufficiency?
```

这可能改变：

```
ISO-G03
```

状态。

但不要在没有完整分析 5.5 + Appendix A 前关闭 gap。

------

# 39. Test Readiness Review

ARP4754B 5.5.5.3 明确说：

> test readiness reviews establish the applicability of test procedures to system/item requirements。

这一点非常重要，因为它和 ISO 24748-1 的：

```
Verification reviews
```

不同。

因此必须明确：

```
ISO 24748-1:
does not mandate generic VRR


ARP4754B:
explicitly recognizes test readiness reviews
within testing/demonstration guidance
```

这很可能要求进一步分层：

```
Generic V6 Verification Readiness Gate
         ↓ specialization
Aviation Test Readiness Review
```

但不能直接写：

```
V6 = Test Readiness Review
```

因为 V6 的 scope 大于单一 test readiness。

------

# 40. Unintended Behavior

ARP4754B Revision B 特别强化了 unintended behavior。Revision B overview 也说明这一概念被进一步澄清。

Development Assurance Plan 本身要求定义识别和处理 unintended behaviors 的方法。

必须研究：

> Generic Framework 是否需要独立：

```
Unintended Behavior Exploration Obligation
```

或作为：

```
Robustness / negative / exploratory verification
```

的一部分。

不要提前决定。

------

# 41. Verification Data / Evidence Architecture

完整研究：

```
5.5.6
```

ARP4754B 明确说 Verification Data 的目的就是：

> 提供 verification process 已执行的 evidence，并且这些 evidence 可能用于 compliance substantiation。

同时推荐：

```
Verification Matrix
Verification Summary Report
```

因此必须建立：

```
Verification Activity
↓
Verification Result
↓
Verification Data
↓
Compliance Substantiation
```

与当前：

```
Evidence
↓
Argument
↓
Claim
```

架构的映射。

这可能成为 Evidence Architecture 的关键 aviation specialization。

------

# 42. Evidence Is Not Just Result

必须检查 ARP4754B 是否支持我们此前的：

```
Result ≠ Evidence
```

预计答案是 Yes。

因为 Appendix A 已经明确分别出现：

- procedures；
- results；
- verification matrix；
- verification summary；
- evidence of procedure sufficiency；
- problem reports。

因此 aviation evidence model 很可能至少需要：

```
Plan
Procedure
Result
Sufficiency Evidence
Matrix
Summary
Problem Record
Configuration Evidence
```

------

# 43. Layer G — Configuration Management

研究：

```
5.6
```

重点关注：

```
System Control Categories
```

Appendix A 把 objective outputs 与 System Control Category 按 FDAL 对应。

必须判断：

> evidence rigor 是否不仅取决于“有没有 evidence”，还取决于 evidence/configuration control rigor？

这可能对当前 Evidence Architecture 产生重要影响。

------

# 44. Process Assurance

完整研究：

```
5.7
```

ARP4754B 明确说 Process Assurance 用于确保 development assurance activities 被维持和遵守，同时 Process Assurance 应与 development process 保持一定独立性。

必须区分：

```
Verification Independence
Process Assurance Independence
```

不能把二者混为同一个 independence mechanism。

------

# 45. Layer H — Modification and Regression

完整研究：

```
Section 6
```

尤其：

```
6.3 Modification Impact Analysis
6.4 Reuse of Evidence
```

Modification Impact Analysis 明确要求评价修改对：

- original development assurance activities；
- safety assessments；
- architectural assumptions；
- DAL allocations；
- installation；

等的影响。

这与当前：

```
V10 Regression
```

高度相关。

------

# 46. Reframe V10

必须研究是否应将：

```
V10 Regression
```

进一步重命名/扩展成：

```
Change Impact & Re-verification
```

或保留 V10 稳定 ID、改变 label。

候选逻辑：

```
Change
↓
Impact Analysis
↓
Affected Assurance Objectives
↓
Affected Requirements / Architecture / Safety Assumptions
↓
Reusable Evidence
↓
Additional Verification
↓
Updated Evidence Baseline
```

这比单纯的：

```
rerun old tests
```

更符合 ARP4754B。

------

# 47. Reuse of Evidence

ARP4754B 6.4 明确允许对此前 certification evidence 寻求 credit，但要求：

- trace to previous baseline；
- confirm applicability；
- identify objectives already satisfied；
- supplement insufficient evidence；
- assess service history / similarity。

因此需要研究一个新的 candidate concern：

```
Evidence Reuse / Credit
```

这可能直接进入 Generic Framework，而 aviation rules 则成为 specialization。

------

# 48. ARP4754B Gap Analysis Targets

研究结束后必须重新评价：

```
ISO-G01 Independence
ISO-G02 Coverage
ISO-G03 Sufficiency
ISO-G04 Oracle
ISO-G05 Regression
ISO-G06 Closure
ISO-G07 Information-item schema
ISO-G08 Model evidence


LC-G01 Gate semantics
LC-G02 Review taxonomy
LC-G03 Process-view provenance
LC-G04 Lifecycle/process instantiation
```

并允许新增：

```
ARP-Gxx
```

候选可能包括：

```
Assurance-level applicability
Verification credit across levels
Derived-requirement handling
Unintended-behavior assurance
Certification evidence admissibility
System-control rigor
Safety/verification evidence integration
```

只有真正不能由已有 Framework 表达的才新增。

------

# 49. Standards Map Expansion

`standards_map.md` 应新增 ARP4754B slice。

至少研究：

```
Development assurance
Verification planning
Requirement validation
Requirement verification / implementation verification
Verification method
Verification independence
Verification environment
Configuration control
Traceability
Anomaly / OPR management
Modification impact
Re-verification
Coverage
Sufficiency
Evidence
Closure
Safety-derived rigor
Evidence reuse
Certification coordination
Tool/model considerations
```

------

# 50. V0–V12 Reassessment

ARP4754B 研究后必须再次评价：

```
V0–V12
```

但不要因为航空标准出现新 terminology 就改稳定 ID。

建议表：

| V-ID | Current ontology | ARP4754B support | Aviation specialization | Change needed? |
| ---- | ---------------- | ---------------- | ----------------------- | -------------- |
|      |                  |                  |                         |                |

尤其重点：

```
V0 Planning
V1 Verification Basis
V2 Requirement Analysis
V3 Strategy
V6 Readiness
V9 Anomaly
V10 Change / Re-verification
V11 Coverage & Sufficiency
V12 Closure
```

------

# 51. Certification Is Not the Same as Assurance

必须建立明确边界：

```
Verification Evidence
≠ Certification Approval
```

ARP4754B Scope 和 planning sections 把 development assurance outputs 与 certification coordination 联系起来，但 certification 本身仍是 Certification Authority 的 legal recognition。ARP4754B 自己定义 certification 为 applicable regulations compliance 的 legal recognition。

因此：

```
Evidence
→ compliance substantiation
→ certification coordination
→ authority decision
```

而不是：

```
test pass
→ certified
```

------

# 52. ARP4754B ↔ ARP4761A Boundary

研究必须明确记录：

> ARP4754B Revision B 已将大量 FDAL/IDAL detailed assignment 和 safety-assessment details 移到 ARP4761A。

因此以下问题不得在 ARP4754B research 中强行闭合：

```
Failure-condition analysis detail
FDAL assignment algorithm
IDAL allocation detail
PSSA/SSA method detail
Common-cause analysis methods
```

应标：

```
Follow-up source:
SAE ARP4761A
Priority: Next
```

------

# 53. Required Cross-Standard Comparison

ARP4754B 最终研究报告必须包含：

## ISO 15288 vs ARP4754B

至少比较：

| Concern              | ISO 15288                          | ARP4754B                                        | Framework consequence     |
| -------------------- | ---------------------------------- | ----------------------------------------------- | ------------------------- |
| Verification purpose | generic objective evidence         | implementation satisfies validated requirements | specialization            |
| Validation           | intended use / stakeholder context | requirement correctness/completeness            | terminology profile       |
| Strategy             | explicit                           | planning/approach                               | harmonize                 |
| Method               | generic method family              | aviation-specific method family                 | contextual taxonomy       |
| Independence         | limited                            | FDAL-dependent                                  | aviation specialization   |
| Coverage             | limited                            | explicit coverage analysis                      | expand                    |
| Sufficiency          | assurance concept                  | verification method/procedure sufficiency       | expand V11                |
| Evidence             | generic                            | certification-oriented verification data        | aviation evidence profile |
| Change               | re-verification                    | formal modification impact/reuse                | strengthen V10            |
| Configuration        | generic CM                         | SC-controlled outputs                           | rigor profile             |

------

# 54. Required Research Report Structure

Create:

```
# SAE ARP4754B Research Notes


1. Metadata and Source Classification
2. Scope and Certification Context
3. Development Assurance Concept
4. Core Terminology
5. Relationship to ISO 15288
6. Development Assurance Planning
7. Aircraft/System/Item Development Architecture
8. Safety-Assessment Interface
9. FDAL / IDAL and Assurance Rigor
10. Process Independence
11. Requirements Capture
12. Requirements Validation
    12.1 Correctness
    12.2 Completeness
    12.3 Methods
    12.4 Independence
    12.5 Validation Data
13. Implementation Verification
    13.1 Objectives
    13.2 Approach
    13.3 Planning
    13.4 Methods
    13.5 Coverage
    13.6 Test Readiness
    13.7 Unintended Behavior
    13.8 Verification Data
14. Configuration Management
15. Process Assurance
16. Modification Impact Analysis
17. Evidence Reuse / Certification Credit
18. Appendix A Objective / FDAL Mapping
19. Mapping to Verification Assurance Framework
20. V0–V12 Reassessment
21. Standards Map Changes
22. Gap Matrix Changes
23. New Research Proposals
24. ARP4761A Follow-up Questions
25. Final Conclusions
```

------

# 55. Required Classification Discipline

每项结论至少使用一种：

```
ARP DEFINITION
ARP RECOMMENDATION
CERTIFICATION-RELATED OBJECTIVE
FDAL-DEPENDENT OBJECTIVE
APPENDIX OBJECTIVE
INTERPRETATION
FRAMEWORK IMPLICATION
AVIATION PROFILE RULE
GENERIC RESEARCH PROPOSAL
OPEN QUESTION
```

不要简单复制 ISO 的：

```
NORMATIVE
```

因为 ARP4754B 自己明确强调其 recommended-practice 属性。

------

# 56. Critical No-Overclaim Rules

禁止：

```
ARP4754B is a regulation.
```

禁止：

```
Every complex system requires FDAL.
```

禁止：

```
All verification requires independence.
```

禁止：

```
Requirement coverage proves verification sufficiency.
```

禁止：

```
Test readiness review is equivalent to V6.
```

禁止：

```
ARP4754B defines our V0–V12.
```

禁止：

```
All verification methods must be test.
```

禁止：

```
All evidence from previous certification is reusable.
```

------

# 57. Expected Major Framework Questions

研究结束必须明确回答：

### FQ-01

是否应保留 `Verification Obligation` 作为 Generic concept？

### FQ-02

是否增加：

```
Assurance Applicability / Rigor
```

dimension？

### FQ-03

Independence 应作为 Verification Strategy 的一部分，还是独立 Assurance Constraint？

### FQ-04

Validation 和 Verification 是否需要 context-dependent taxonomy？

### FQ-05

Coverage 应如何从“Requirement Coverage”发展成 Framework Coverage Model？

### FQ-06

Sufficiency 是否应作为独立 assessment object？

### FQ-07

Verification Data 与 Evidence 是什么关系？

### FQ-08

是否需要显式：

```
Verification Credit
Evidence Reuse
```

relations？

### FQ-09

V10 是否应该从 `Regression` 扩展为 `Change Impact & Re-verification`？

### FQ-10

V6 Generic Composite Gate 与 aviation Test Readiness Review 如何 specialization？

### FQ-11

V12 是否可从 development completion / certification substantiation 获得更强 aviation-specific closure semantics？

### FQ-12

Safety Assessment 如何成为 Verification Obligation / Rigor 的 source？

最后一个问题只能部分回答，完整答案留给 ARP4761A。

------

# 58. Repository Change Discipline

本轮允许：

```
new standard note
matrix updates
gap updates
terminology refinements
V0–V12 semantic refinements
template refinements
new candidate information item
roadmap update
```

但禁止：

```
large-scale repository restructuring
premature MBSE implementation
tool development
DCAS-specific case migration
ARP4761A conclusions
DO-178C/DO-254 conclusions
```

------

# 59. Research Sequence

Codex 应按以下顺序执行：

```
Step 1
24748-2 targeted applicability review


Step 2
Record delta/no-delta against current Generic Framework


Step 3
Mark 24748-2 as supporting source unless evidence requires otherwise


Step 4
Full ARP4754B clause-level research


Step 5
Cross-map ARP4754B against ISO 15288 / 24748-1 / 24748-2


Step 6
Update Standards Map


Step 7
Update Gap Matrix


Step 8
Reassess V0–V12 and information models


Step 9
Create an internal research review package


Step 10
Stop before ARP4761A conclusions
```

------

# 60. Expected Status After This Round

理想结果：

```
ISO/IEC/IEEE 15288:2023
→ Reviewed Baseline Candidate


ISO/IEC/IEEE 24748-1:2024
→ Reviewed Baseline Candidate


ISO/IEC/IEEE 24748-2:2024
→ Reviewed Supporting Source


SAE ARP4754B
→ Research Complete / Baseline Candidate


SAE ARP4761A
→ Next Major Research Source
```

------

# 61. Definition of Done

本轮只有在以下条件全部满足时完成：

-  24748-2 targeted review 已回答六个 mandatory questions；
-  已明确 24748-2 是否产生 Framework delta；
-  没有将 24748-2 guidance 误写为新增 15288 requirement；
-  ARP4754B research note 已完成；
-  Development Assurance 概念已与 ISO Assurance 对照；
-  Requirements Validation 已完整分析；
-  Implementation Verification 5.5 已完整分析；
-  Verification Planning 字段已映射到现有 VSR；
-  Verification Methods 已做 cross-standard taxonomy comparison；
-  Process Independence 已映射到 assurance level；
-  Coverage Analysis 已研究；
-  Verification Sufficiency 已研究；
-  Verification Data / Evidence Architecture 已研究；
-  Test Readiness Review 与 V6 已明确区分；
-  Modification Impact / Evidence Reuse 已研究；
-  Appendix A FDAL-dependent objectives 已纳入研究；
-  Standards Map 已更新；
-  Gap Matrix 已更新；
-  V0–V12 已重新评价但未无理由改 stable IDs；
-  没有将 ARP 推荐实践写成法规；
-  没有提前研究 ARP4761A conclusions；
-  最终明确下一项研究为 ARP4761A。

------

# 62. Final Research Principle

这一轮必须坚持两个不同原则。

对于 **ISO 24748-2**：

> **寻找 delta，而不是寻找更多可以摘录的内容。**

如果它只是解释已经建立的 Generic Framework：

```
record support
do not expand scope
move on
```

对于 **ARP4754B**：

> **允许航空 Development Assurance 真正改变 Generic Verification Framework，但必须区分 Generic Methodology 与 Aviation Profile。**

最终目标不是把 Repository 变成：

```
ISO + SAE standards summary collection
```

而是逐步形成：

```
Generic Verification Assurance Framework
                │
                ├── supported by ISO systems-engineering standards
                │
                └── specialized by Civil Aviation Development Assurance
                             │
                             ├── ARP4754B
                             └── ARP4761A
```

本轮最值得关注的潜在突破是：

```
Verification
        ↓
Verification Obligation
        ↓
Assurance Applicability / FDAL
        ↓
Independence
        ↓
Verification Strategy
        ↓
Coverage
        ↓
Sufficiency
        ↓
Controlled Evidence
        ↓
Compliance Substantiation
```

如果 ARP4754B 的完整研究支持这条链，它将成为当前 Verification Assurance Framework 从“通用系统工程验证模型”进入“开发保证模型”的第一次实质性跃迁。
