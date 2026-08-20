---
title: SAE ARP4761A:2023 Historical Safety-Assurance Research Task
status: superseded
version: 1.0
baseline: historical-pre-v0.2
owner: research
last_updated: 2026-08-20
document_role: historical-task-specification
body_format: preserved-original
dependencies:
  - ../README.md
  - ../../standard_notes/sae_arp4761a.md
  - ../../reviews/sae_arp4761a_internal_review.md
  - ../../reviews/pr_4_arp4761a_external_review.md
---

> **Archive control:** This completed ARP4761A safety-assurance work order is retained as pre-v0.2 research provenance. Its original body and numbering are preserved; current aviation-profile status is governed by the reviewed note and review records.

# SAE ARP4761A Safety Assurance Research Task Specification

## 1. Task Purpose

对：

**SAE ARP4761A — Guidelines for Conducting the Safety Assessment Process on Civil Aircraft, Systems, and Equipment**

开展条款级研究，并将其与当前已经建立的：

- ISO/IEC/IEEE 15288:2023；
- ISO/IEC/IEEE 24748-1:2024；
- ISO/IEC/IEEE 24748-2:2024；
- SAE ARP4754B；

研究结果进行交叉映射。

本轮研究核心不是建立一份 Safety Engineering 教程，也不是穷尽 FTA/FMEA/CMA 等方法细节，而是回答：

> **Safety Assessment 如何产生和约束 Verification Assurance Obligations，以及安全严重度、架构、独立性和 Development Assurance Level 如何影响验证 rigor、coverage、evidence 和 closure。**

------

# 2. Source Positioning

研究源：

```
SAE ARP4761A
Guidelines for Conducting the Safety Assessment Process
on Civil Aircraft, Systems, and Equipment


Revision A
Revised: 2023-12
Supersedes: ARP4761
```

该文档是 SAE Aerospace Recommended Practice，不是法规。首页明确其使用是 voluntary，并由使用者自行判断 suitability。

Scope 进一步说明：

- 它提供 civil-aircraft/system/equipment safety-assessment guidelines；
- 可用于支持 certification compliance；
- 也可用于企业内部安全标准；
- 文中过程不是唯一可接受过程；
- 其他等效过程也可能有效。

因此严禁：

```
ARP4761A legally requires X.
```

优先采用：

```
ARP4761A recommends...
ARP4761A provides guidance for...
ARP4761A safety-assessment practice establishes...
```

并继续区分：

```
ARP RECOMMENDATION
SAFETY-ASSESSMENT GUIDANCE
CERTIFICATION-RELATED GUIDANCE
DEFINITION
INTERPRETATION
FRAMEWORK IMPLICATION
AVIATION PROFILE RULE
RESEARCH PROPOSAL
```

------

# 3. Relationship to ARP4754B

这是本轮最重要的 source boundary。

ARP4761A 明确说明其 terminology 与 ARP4754B/ED-79B 对齐，并建议与 ARP4754B、DO-178C、DO-254、DO-297 及适用法规/咨询材料一起使用。

应将二者理解为：

```
ARP4754B
Development Assurance / Development Process
        ↕
ARP4761A
Safety Assessment Process
```

而不是：

```
ARP4761A replaces ARP4754B.
```

Safety Assessment 和 Development Process 是并行且不断交换信息的两个体系。标准 Figure 2 直接显示 AFHA/PASA/SFHA/PSSA/SSA/ASA 与 requirements、architecture、implementation、system integration & verification 和 aircraft integration & verification 之间的双向接口。

------

# 4. Required Outputs

创建：

```
docs/01_normative_foundation/
standard_notes/
sae_arp4761a.md
```

并更新：

```
docs/01_normative_foundation/standards_map.md
docs/01_normative_foundation/normative_gap_matrix.md
docs/00_overview/terminology.md
docs/03_dbse_workflow/README.md
templates/verification_strategy_record.md
```

如果证据充分，可提出新的 candidate information objects，例如：

```
Safety Objective Record
Safety Requirement Provenance
Safety Assurance Constraint
Independence Principle
Failure Condition
Safety Assessment Obligation
Assumption / Assumption Confirmation
```

但不要为了“覆盖标准”而无必要新增 schema。

------

# 5. Primary Research Questions

必须系统回答以下问题。

### R4761-Q01

Failure Condition 如何产生 Safety Objective？

### R4761-Q02

Safety Objective 如何进一步产生 Safety Requirement？

### R4761-Q03

Failure Condition Classification 如何影响 analysis depth？

### R4761-Q04

FDAL / IDAL 与 failure condition、architecture、independence 之间是什么关系？

### R4761-Q05

Safety Assessment 如何影响 Verification Strategy / Verification Rigor？

### R4761-Q06

Safety Requirement 与普通 Requirement 在 Framework 中应是什么关系？

### R4761-Q07

Independence Principle 与 Process Independence 有什么不同？

### R4761-Q08

PSSA 如何产生 independence / quantitative / architectural safety requirements？

### R4761-Q09

SSA / ASA 中的“verify”与 ARP4754B Implementation Verification 是什么关系？

### R4761-Q10

Safety-analysis methods 的结果是什么类型的 Evidence？

### R4761-Q11

Safety assumptions 应如何进入 verification obligation / evidence architecture？

### R4761-Q12

Safety Assessment completion 是否为 V12 提供新的 aviation-specific closure semantics？

### R4761-Q13

设计变更如何触发 safety reassessment，并如何与 V10 `Change Impact & Re-verification` 联动？

### R4761-Q14

FDAL / IDAL 应作为 Verification Strategy 字段，还是独立的 Assurance Constraint？

### R4761-Q15

Safety-derived rigor 是否属于 Generic Framework，还是 Aviation Profile？

------

# 6. Research Scope

完整研究正文：

```
1       Scope
2.2     Definitions
3       Safety Assessment Process
3.1     Overview and interactions
3.2     AFHA
3.3     PASA
3.4     SFHA
3.5     PSSA
3.6     SSA
3.7     ASA
3.8     Depth of Analysis
3.9     FDAL / IDAL Assignment
```

重点研究 Appendices：

```
A   AFHA
B   PASA
C   SFHA
D   PSSA
E   SSA
F   ASA
P   FDAL / IDAL Assignment
Q   Contiguous Example
```

方法类 Appendices：

```
G FTA
H DD
I MA
J FMEA/FMES
K ZSA
L PRA
M CMA
N MBSA
O CEA
```

**不要求等深度研究。**

只提取：

> 它们怎样形成 Safety Evidence、支持 Requirement/Objective verification、验证 Independence、决定 Analysis Depth 或影响 Framework taxonomy。

不要把本轮变成 Safety Analysis Method Handbook。

------

# 7. Layer A — Safety Assurance Concepts

首先提取：

- Failure；
- Failure Mode；
- Failure Effect；
- Failure Condition；
- Failure Condition Classification；
- Hazard；
- Risk；
- Safety；
- Safety Objective；
- Safety Requirement；
- Independence；
- Independence Principle；
- FDAL；
- IDAL；
- Assumption；
- Assurance；
- Development Assurance。

ARP4761A 明确把 Safety Objective 定义为：

> 为达到某 failure condition 所要求安全水平而需要的定性和/或定量属性。

Safety Requirement 则是：

> 为实现 Safety Objective 或满足 safety process 建立的 constraint 所必需的 requirement。

必须建立：

```
Failure Condition
        ↓ classification
Safety Objective
        ↓
Safety Requirement
```

这一基本关系。

------

# 8. Safety Requirement Provenance

这是本轮对 Framework 可能最重要的新内容之一。

ARP4761A 明确说明 PASA/PSSA 会产生 Safety Requirements，包括：

- quantitative probability requirements；
- independence requirements；
- architecture requirements；
- FDAL/IDAL-related constraints；
- monitoring/redundancy/protection requirements；
- assumptions converted to requirements。

标准甚至建议每个 Safety Requirement 保存 rationale，并具体追溯到：

- architecture；
- Independence Principle；
- fault tree；
- safety analysis source；

以支持未来 change impact 和 requirement validation。

因此必须研究：

```
Requirement
      ↑
Safety Requirement
```

是否应该是 subtype / classification。

并考虑：

```
Safety Requirement Provenance
```

至少包含：

```
source_failure_condition:
source_safety_objective:
source_assessment:
source_analysis:
source_assumption:
rationale:
allocated_level:
```

但这只是 candidate model。

------

# 9. AFHA / SFHA — Hazard Identification Layer

研究：

```
3.2 AFHA
3.4 SFHA
Appendix A
Appendix C
```

AFHA/SFHA 的核心作用是：

```
Function
↓
Failure Condition
↓
Severity Classification
↓
Safety Objective
```

AFHA 负责 aircraft level；SFHA 负责 system level。

必须研究：

> `Failure Condition` 是否应成为 Verification Obligation 的上游 source object。

例如：

```
FC-001 Catastrophic
      ↓
Safety Objective
      ↓
Safety Requirement
      ↓
Verification Obligation
```

但不能直接把：

```
Failure Condition = Verification Case
```

二者完全不同。

------

# 10. PASA / PSSA — Safety Requirement Generation Layer

PASA/PSSA 是本轮最重要的 architecture-driving processes。

PASA：

- 评价 proposed aircraft architecture；
- 根据 safety objectives 建立 aircraft safety requirements；
- 分析 common causes；
- 产生 independence requirements；
- 参与 FDAL assignment。

PSSA：

- 评价 proposed system architecture；
- 从 SFHA failure conditions 和 PASA allocations 出发；
- 建立 system/subsystem/item safety requirements；
- 建立 independence requirements；
- 分解 quantitative requirements；
- 分配 FDAL/IDAL；
- 管理 assumptions。

因此候选链：

```
FHA
↓
Safety Objective
↓
PASA/PSSA
↓
Safety Constraint / Requirement
↓
Development Process
↓
Implementation
↓
SSA/ASA
```

必须被映射进 Framework。

------

# 11. PSSA Completion Criteria

Appendix D 很有价值，因为它提供了一个领域性的 completeness/sufficiency assessment。

PSSA completion 不是只看 probability。

它综合检查：

- quantitative analyses；
- FDAL/IDAL assignment；
- independence requirements；
- safety requirements；
- development acceptance；
- newly introduced failure conditions；
- traceability from safety requirement to source assessment；
- lower-level assumptions confirmation。

这一结构对 V11 很重要。

必须研究：

> 这是否是 **domain-specific Safety Sufficiency Assessment**，而不是 Generic Verification Sufficiency 的完整定义。

预期结论：

```
supports V11 aviation specialization
≠ closes Generic sufficiency gap
```

------

# 12. SSA — Safety Verification Layer

完整研究：

```
3.6
Appendix E
```

SSA 是最直接与 Verification Assurance Framework 对接的部分。

标准明确：

> SSA examines the implemented system and verifies that safety requirements and safety objectives are met.

SSA 依赖 development process 验证：

- FDAL / IDAL accomplished；
- monitors；
- redundancies；
- protections；
- self-test；
- other safety requirements。

同时 SSA 自身使用：

- CMA；
- ZSA；
- PRA；
- FTA；
- other qualitative/quantitative analyses；

确认 independence、quantitative objectives 等。

必须避免把 SSA 简化为：

```
another Verification Method
```

更合理是：

> **SSA 是一个 domain-specific Safety Assurance Assessment，它聚合 development verification evidence 和 safety-analysis evidence，形成 system safety substantiation。**

------

# 13. ASA — Aircraft-Level Safety Claim

ASA 研究同样重要。

标准明确区分：

```
PASA
→ proposed architecture
→ requirements generation


ASA
→ implemented aircraft
→ confirmation of qualitative/quantitative safety objectives and requirements
```



因此可以探索：

```
SSA
→ System Safety Claim


ASA
→ Aircraft Safety Claim
```

但 Claim terminology 与 ISO assurance-case architecture 的映射应标记为：

```
FRAMEWORK INTERPRETATION
```

而不是 ARP 原生 `Claim` object。

------

# 14. Safety Assessment Completion / Closure

ARP4761A 提供了很有价值的 closure semantics：

> Safety Assessment Process complete when applicable SSA(s) and ASA results show applicable system-level and aircraft-level safety objectives are satisfied and safety requirements are met.

这可能加强：

```
V12 Verification Closure
```

但不要直接得出：

```
V12 = SSA/ASA completion
```

正确研究问题是：

> Safety closure 是否应作为 Aviation Profile 中 V12 composite gate 的一个 mandatory assurance input？

候选：

```
V12
├─ Verification completion
├─ Evidence completeness
├─ open/deferred anomaly disposition
├─ Safety Assessment completion
├─ applicable SSA/ASA acceptance
└─ baseline/approval decision
```

这将是重要 framework implication。

------

# 15. Change / Reassessment — V10

ARP4761A 对 V10 有非常强的支持。

标准明确：

- change to design or principal assessment can trigger changes elsewhere；
- modified design must be reassessed；
- safety requirements may change；
- new safety requirements may emerge。

Appendix P 同样要求：

- FHA revision；
- architecture modification；
- changed assumptions；

触发 FDAL/IDAL reconsideration。

因此：

```
V10 Change Impact & Re-verification
```

应进一步增加：

```
Safety Impact Analysis
Safety Reassessment
FDAL/IDAL Reassessment
Assumption Revalidation
```

但仍不要改 stable ID。

------

# 16. Depth of Analysis

研究：

```
3.8
```

标准明确：

> analysis depth 通常由 Failure Condition Classification 驱动，同时还可能依赖其他 system/aircraft characteristics；可能采用 design/installation appraisal、verification analysis、qualitative/quantitative assessment。

这很重要，因为它提供：

```
Safety Severity
        ↓
Analysis Depth
```

这一 rigor chain。

但注意：

> ARP4761A 自己把完整 depth-of-analysis 选择进一步指向适用 advisory material。

因此不要声称：

```
ARP4761A alone fully defines all safety verification rigor.
```

可能的新 Framework relation：

```
Failure Condition Classification
→ Safety Analysis Depth Constraint
```

------

# 17. FDAL / IDAL

完整研究：

```
3.9
Appendix P
```

这是本轮最重要的章节之一。

必须明确：

```
FDAL
= rigor of Development Assurance tasks applied to functions


IDAL
= rigor applied to items
```

定义依据见标准术语。

Appendix P 进一步说明：

```
Failure Condition
+ Function
+ Architecture
+ Functional Independence
        ↓
FDAL


FDAL
+ Item allocation
+ Item Development Independence
        ↓
IDAL
```



因此当前 ARP4754B 中：

```
assurance_level
```

字段应重新审查。

很可能需要从一个模糊字段拆成：

```
fdal:
idal:
applicable_assurance_context:
```

但仅当信息模型确实需要。

------

# 18. FDAL / IDAL Are Not Verification Levels

必须建立严格边界：

```
FDAL ≠ Verification Level
IDAL ≠ Verification Method
FDAL ≠ Requirement Criticality
IDAL ≠ System Safety Classification
```

它们是：

> Development Assurance rigor levels。

其意义是影响：

- applicable objectives；
- independence；
- development assurance rigor；
- software/hardware assurance levels。

不能把 FDAL/IDAL 简化成：

```
more severe → more tests
```

------

# 19. Development Error vs Random Failure

这是 Framework 很重要的一层。

ARP4761A Safety Assessment 同时关注：

```
Failures
```

以及：

```
Development Errors
```

FDAL/IDAL 主要用于控制：

> development error contribution to failure conditions。

而 FTA/FMEA 等很多方法主要分析：

> random/functional failure mechanisms。

因此必须建立：

```
Random Failure Assurance
vs
Development Error Assurance
```

的区别。

这是后续 Coverage 模型可能必须引入的一个维度。

------

# 20. Independence Taxonomy

ARP4761A 定义四类 independence：

- Functional Independence；
- Item Development Independence；
- Physical Independence；
- Process Independence。

这对当前 terminology 是一次重要修正。

必须避免只用：

```
independence_required: true/false
```

因为“独立性”不是一个单一 boolean concept。

候选模型：

```
independence_constraint:
  type:
    - functional
    - item_development
    - physical
    - process
  source:
  rationale:
  verification_method:
  evidence:
```

------

# 21. Independence Principle

特别研究：

```
Independence Principle
```

它并不等同于：

```
Independence Requirement
```

标准定义为：

> intended implementation 中被判定为必须保持 independence 的设计 feature。

PASA/PSSA 中 Independence Principles 可进一步转化成 requirements，并需要 CMA/ZSA/PRA 等方法确认。

因此可能的 chain：

```
Safety Analysis
↓
Independence Principle
↓
Safety Requirement
↓
Architecture / Implementation
↓
CMA / ZSA / PRA
↓
Independence Evidence
```

------

# 22. Safety Analysis Method Taxonomy

ARP4761A 列出：

- FTA；
- DD；
- MA；
- MBSA；
- FMEA/FMES；
- CEA；
- ZSA；
- PRA；
- CMA。

不要把这些直接并入 Generic：

```
Verification Method
```

它们属于：

```
Safety Analysis Method
```

可能支持：

- hazard identification；
- architecture assessment；
- independence verification；
- probability calculation；
- safety requirement derivation；
- safety evidence generation。

应建立：

```
Verification Method Taxonomy
≠
Safety Analysis Method Taxonomy
```

但允许某些 Safety Analysis Method 产生 verification evidence。

------

# 23. FTA / DD / MA / MBSA

不做算法教材。

仅研究：

```
Input
Purpose
Output
Applicable Safety Assessment Stage
Evidence Contribution
Framework Relation
```

特别关注：

> FTA / DD / MA / MBSA 在同一 safety objective verification context 中可能互为 alternative methods。

ARP4761A 明确说这些方法可以根据所需数据和 system context 选用。

------

# 24. FMEA / FMES

研究其角色：

```
Failure Mode
↓
Local / higher-level effect
↓
support higher-level safety analysis
```

但不要把：

```
FMEA = Verification Technique
```

它更像 bottom-up safety analysis method。

同时记录：

> FMEA/FMES 输出可能作为 SSA/FTA evidence input。

------

# 25. CMA / ZSA / PRA

这是 Independence 验证的关键。

ARP4761A 明确：

- CMA 是 SSA 中验证 independence requirements 的主要方法；
- ZSA/PRA 可以补充验证 physical/installation independence。

因此：

```
Independence Requirement
      ↓
CMA / ZSA / PRA
      ↓
Safety Evidence
```

应成为 Aviation Profile mapping。

------

# 26. MBSA

研究 Appendix N，但必须保持一个关键边界：

ARP4761A 明确：

> MBSA 不依赖 MBSE development process；它可以用于传统文本开发，也可以用于 MBSE。

因此禁止：

```
MBSA = MBSE Safety View
```

或：

```
MBSA requires MBSE.
```

但 MBSA 对我们的 model-based Verification Assurance 很有参考价值，因为它显式建立：

```
Failure Condition Observer
Failure Propagation Model
System States
Architecture
Safety Requirements
Analysis Results
```

这可能成为未来 safety metamodel 的候选实例。

------

# 27. Assumptions

这是本轮必须重点研究的新对象。

Safety Assessment 大量依赖：

```
Assumptions
```

而这些 assumptions 必须：

- 被记录；
- 向 higher/lower levels 传递；
- 必要时转换成 requirements；
- 被确认/验证；
- 在设计变化后重新评估。

PSSA 输出甚至明确包含使 PSSA 有效所需 assumptions。

因此建议考虑新的 Generic candidate concept：

```
Assumption
Assumption Obligation
Assumption Confirmation
```

这可能不仅限于 Aviation Profile，具有通用价值。

但是否提升到 Generic Core，应在 cross-standard review 后决定。

------

# 28. Assumption → Requirement Transformation

尤其关注：

```
Assumption
↓
Safety Requirement
```

ARP4761A 明确指出 assumption 可以用于定义 safety requirement，以便验证 assumption。

这可能是我们 Framework 中非常有价值的 pattern：

```
Unverified Assumption
        ↓
Convert to Constraint / Requirement
        ↓
Verification Obligation
        ↓
Evidence
```

需要作为候选 research pattern 记录。

------

# 29. Verification Obligation Generation

本轮结束时必须尝试建立：

```
Safety Assessment Finding
        ↓
Safety Objective
        ↓
Safety Requirement
        ↓
Assurance / Independence Constraint
        ↓
Verification Obligation
```

例如：

```
Catastrophic FC
↓
Quantitative Safety Objective
↓
Independence Principle
↓
Physical Independence Requirement
↓
CMA / PRA / ZSA Verification
↓
Evidence
```

这可能第一次真正给 `Verification Obligation` 一个 upstream causal model。

------

# 30. Safety Evidence

研究必须区分：

```
Development Verification Evidence
Safety Analysis Evidence
Safety Assessment Evidence
```

它们可能互相引用，但不完全相同。

例如 SSA：

- 使用 development verification results；
- 使用 CMA/FTA/FMEA 等 safety-analysis results；
- 形成 system safety substantiation。

因此建议：

```
Evidence
├─ Development Verification Evidence
├─ Safety Analysis Evidence
└─ Safety Assessment Evidence
```

仅作为 candidate taxonomy。

------

# 31. SSA Evidence Aggregation

SSA 明确依赖：

- lower-level assessment results；
- development verification；
- safety requirement verification；
- independence verification；
- quantitative analysis；
- assumptions confirmation。

这说明 SSA 是一个非常典型的：

```
Evidence Aggregation / Assurance Assessment
```

过程。

这可能直接支持 V11 的概念深化：

```
V11 Coverage & Sufficiency Assessment
```

在 Aviation Safety Profile 下：

```
Safety Evidence Sufficiency
```

需要综合多类 evidence。

------

# 32. Safety Coverage

不要轻率创造：

```
Safety Coverage = X%
```

但必须研究：

> 什么叫“所有 applicable failure conditions、safety objectives、safety requirements 都被覆盖”？

例如 SSA main body 明确要 cover PSSA 中识别的所有 specific safety requirements。

Appendix Q 的 completion example 还要求所有 safety requirements 在 Verification Matrix 中有 trace 并确认 satisfied。

因此可能形成：

```
Safety Objective Coverage
Safety Requirement Coverage
Failure Condition Coverage
Assumption Coverage
Independence Requirement Coverage
```

但均应先标：

```
Aviation-profile candidate coverage dimensions
```

------

# 33. Safety Sufficiency

ARP4761A 对 Safety Sufficiency 的价值可能大于 ARP4754B。

PSSA completion 强调：

> 不能只看 quantitative probability 或 FDAL/IDAL，而要看 collective results。

这是重要概念：

```
Sufficiency
≠ one metric
≠ requirement trace count
≠ probability only
```

更可能是：

```
structured assessment of heterogeneous evidence
```

这个结论值得明确记录。

------

# 34. Change Impact / Safety Reassessment

强化 V10：

```
Change
↓
Affected Design
Affected Failure Conditions
Affected Safety Objectives
Affected Safety Requirements
Affected Assumptions
Affected Independence
Affected FDAL / IDAL
↓
Safety Reassessment
↓
Re-verification
```

这比 ARP4754B 单独提供的 Modification Impact Analysis 更完整。

------

# 35. Legacy / Reuse

Appendix P 对 legacy FDAL/IDAL reuse 给出很多条件。

必须注意：

> legacy assurance levels 不能直接沿用。

需要重新检查：

- new AFHA/SFHA；
- changed failure conditions；
- changed architecture；
- independence；
- new operating environment；
- assumptions。

这应该进一步强化：

```
Evidence / Assurance Reuse
requires applicability assessment
```

但不要重新引入之前被纠正的：

```
Result becomes Evidence only if...
```

这两者是不同概念。

------

# 36. Open / Deferred Problems

Appendix Q 的例子值得用于 V12/closure interpretation。

示例 completion 会检查：

- verification activities complete；
- all safety requirements traced；
- open/deferred PRs reviewed；
- deferred issues do not present unacceptable aircraft-level risk。

但 Appendix Q 是 example。

不得写成：

> ARP4761A universally mandates this exact PR closure process.

正确分类：

```
illustrative support for aviation closure semantics
```

------

# 37. V0–V12 Reassessment

必须重新评价，但保持 stable IDs。

重点：

| V-ID | ARP4761A question                                            |
| ---- | ------------------------------------------------------------ |
| V0   | Safety Program Plan 与 Verification Planning 如何交互？      |
| V1   | Safety objectives/requirements 是否进入 Verification Basis？ |
| V2   | Safety Requirement validation / assumption validation 如何映射？ |
| V3   | Failure severity / FDAL / independence 如何约束 Strategy？   |
| V4   | Safety-analysis-derived obligations 如何形成 cases？         |
| V5   | Safety-analysis/verification procedures 如何关联？           |
| V6   | Safety readiness 是否需要独立 gate input？                   |
| V7   | development verification 与 safety analyses 如何并行执行？   |
| V8   | safety objective satisfaction 如何评估？                     |
| V9   | safety findings/anomalies 如何进入 problem resolution？      |
| V10  | safety reassessment / DAL reassessment 如何纳入 change impact？ |
| V11  | safety evidence sufficiency 如何评估？                       |
| V12  | SSA/ASA completion 如何作为 closure input？                  |

不要因为 ARP4761A 出现新 processes，就把：

```
AFHA → PASA → SFHA → PSSA → SSA → ASA
```

直接替换 V0–V12。

这是另一个 Process View。

------

# 38. Candidate Dual-View Architecture

本轮应评估：

```
Verification Assurance Process View
        ↕


Safety Assessment Process View
```

它们共享：

- Requirements；
- Architecture；
- Assumptions；
- Verification Obligations；
- Evidence；
- Configuration；
- Change；
- Assurance Level；
- Claims。

而不是将 Safety Assessment process 吞并到 Verification workflow。

这是本轮非常关键的 architecture question。

------

# 39. Standards Map Update

新增 ARP4761A slice。

至少覆盖：

```
Safety assessment
Failure-condition analysis
Safety objectives
Safety requirements
Requirement provenance
Independence
Verification rigor
FDAL / IDAL
Verification planning input
Verification strategy input
Coverage
Sufficiency
Evidence
Change impact
Re-verification
Assumption management
Closure
Evidence reuse
MBSE / MBSA
```

不要为了填满矩阵而强行映射。

------

# 40. Gap Matrix Update

重新评价现有：

```
ISO-G01 Independence
ISO-G02 Coverage
ISO-G03 Sufficiency
ISO-G04 Oracle
ISO-G05 Change/Re-verification
ISO-G06 Closure
ISO-G07 Information schema
ISO-G08 Model evidence


LC-Gxx
ARP-Gxx
```

预期可能：

### ISO-G01

进一步从 Process Independence 扩展成：

```
multi-type independence model
```

但 Generic gap 未必关闭。

### ISO-G02

获得 Safety Requirement / Failure Condition / Safety Objective coverage 支持。

### ISO-G03

获得 collective safety-assessment sufficiency 支持。

### ISO-G05

进一步加强 safety reassessment。

### ISO-G06

获得 SSA/ASA completion 的 aviation closure semantics。

### ARP-G01

Assurance applicability / rigor 可能得到更完整解释。

### ARP-G02

Cross-level credit 进一步与 FDAL/IDAL/independence 联系。

------

# 41. Candidate New ARP4761A Gaps

只有必要时新增。

候选：

```
SAF-G01 Safety-to-verification obligation derivation
SAF-G02 Assumption lifecycle and confirmation
SAF-G03 Multi-type independence representation
SAF-G04 Safety evidence aggregation
SAF-G05 Safety sufficiency reasoning
SAF-G06 Safety-assessment/change synchronization
```

Codex 应自行判断是否确实构成 Framework gap。

------

# 42. Terminology Update

可能新增或精化：

```
Failure Condition
Failure Condition Classification
Failure Mode
Failure Effect
Safety Objective
Safety Requirement
Safety Assessment
Safety Analysis
Assumption
Independence Principle
Functional Independence
Item Development Independence
Physical Independence
FDAL
IDAL
SSA
ASA
PSSA
PASA
```

保持：

```
Safety Analysis ≠ Verification
Safety Assessment ≠ Verification Process
FDAL ≠ Verification Level
Safety Requirement ⊂ Requirement candidate classification
```

------

# 43. Verification Strategy Record Reassessment

检查当前 candidate fields 是否需要增加：

```
safety_context:
  failure_condition_ids:
  safety_objective_ids:
  safety_requirement_ids:
  fdal:
  idal:
  independence_constraints:
  safety_analysis_dependencies:
  assumption_ids:
  safety_assessment_reference:
```

但不要直接全部加入正式模板。

先建立：

```
candidate aviation safety profile extension
```

或在 research note 中记录 proposed fields。

------

# 44. Potential New Information Model

本轮可提出候选：

```
FailureCondition
SafetyObjective
SafetyRequirement
SafetyConstraint
Assumption
IndependencePrinciple
AssuranceLevelAssignment
SafetyAnalysis
SafetyAssessment
SafetyEvidence
```

关系候选：

```
Function
→ hasFailureCondition


FailureCondition
→ classifiedAs


Classification
→ drives SafetyObjective


SafetyObjective
→ derives SafetyRequirement


SafetyRequirement
→ allocatedTo RequirementOwner


SafetyRequirement
→ creates VerificationObligation


Assumption
→ supports SafetyAssessment


Assumption
→ mayBeConvertedTo SafetyRequirement


IndependencePrinciple
→ derives IndependenceRequirement


SafetyEvidence
→ supports SafetyAssessment
```

全部标：

`Candidate Information Model`.

------

# 45. ARP4754B Cross-Standard Consistency Review

必须专门形成：

## ARP4754B ↔ ARP4761A

至少比较：

| Concern               | ARP4754B                       | ARP4761A                                  | Framework consequence  |
| --------------------- | ------------------------------ | ----------------------------------------- | ---------------------- |
| Development Assurance | Defines development framework  | Safety-driven rigor source                | connect                |
| FDAL                  | principles                     | assignment process                        | split responsibility   |
| IDAL                  | principles/interface           | assignment process                        | split responsibility   |
| Safety Requirements   | development capture/validation | derived by safety process                 | provenance             |
| Independence          | process independence           | functional/item/physical/process          | expand taxonomy        |
| Verification          | implementation verification    | safety objective/requirement confirmation | evidence interaction   |
| Change                | modification impact            | safety reassessment                       | unify V10              |
| Closure               | development evidence           | SSA/ASA completion                        | composite V12          |
| Evidence              | verification data              | safety-analysis/assessment evidence       | multi-source assurance |

------

# 46. MBSA / MBSE Boundary

明确：

```
MBSA ≠ MBSE
```

同时研究：

> MBSA 是否可以作为未来 Model-Based Safety Assurance profile 的一个实例。

ARP4761A Appendix N 明确保持技术中立，并允许传统文本开发或 MBSE 开发。

因此不要把 MBSA 强行绑定 SysML。

------

# 47. Copyright Rule

ARP4761A PDF 不得提交公开仓库。版权页明确禁止未经许可复制和传播。

Repository 中只保留：

- metadata；
- clause locator；
- paraphrase；
- small necessary terminology fragments；
- framework interpretation。

尤其 Appendix Q 有大量完整示例，不要复制其 tables / figures。

------

# 48. Required Research Note Structure

创建：

```
# SAE ARP4761A Research Note

23. Legacy / Reuse
24. Safety Assessment Completion
25. Relationship to Verification Assurance Framework
26. V0–V12 Reassessment
27. ARP4754B Cross-Standard Comparison
28. Standards Map Update
29. Gap Matrix Update
30. Candidate Information Model
31. Research Proposals
32. Open Questions
33. Final Conclusions
```

------

# 49. Required Final Framework Questions

研究完成后必须明确回答：

1. Safety Requirement 是否应作为 Requirement subtype？
2. Safety Objective 是否属于 Verification Basis？
3. Failure Condition 是否产生 Verification Obligation？
4. FDAL/IDAL 是 Strategy 属性还是 Assurance Constraint？
5. Independence 是否必须建模为多类型对象？
6. Safety Analysis Method 与 Verification Method 如何分层？
7. SSA 是否属于 V11 的 aviation specialization？
8. ASA 是否应被建模为 aircraft-level assurance aggregation？
9. Safety Assessment completion 如何影响 V12？
10. Assumption 是否应提升为 Generic Framework object？
11. V10 是否需要显式 Safety Reassessment subflow？
12. Safety Coverage 是否应作为 Coverage Model 新维度？
13. Safety Evidence 与 Development Verification Evidence 是什么关系？
14. Safety Objective / Requirement satisfaction 是否构成独立 Claim type？
15. Generic Framework 如何避免被航空 Safety Process 反向污染？

------

# 50. No-Overclaim Rules

禁止：

```
ARP4761A is regulation.
```

禁止：

```
All complex systems require FDAL/IDAL.
```

禁止：

```
All Catastrophic functions require the same verification method.
```

禁止：

```
Safety Analysis Method = Verification Method.
```

禁止：

```
SSA = Verification Process.
```

禁止：

```
ASA = V12.
```

禁止：

```
CMA is always mandatory for every system.
```

禁止：

```
Failure Condition Classification directly defines test count.
```

禁止：

```
ARP4761A alone fully defines certification compliance.
```

------

# 51. Expected Framework Impact

本轮最可能产生的真正 Framework delta 应集中在：

```
1. Safety Requirement provenance
2. Safety-derived Verification Obligation
3. Multi-type Independence
4. FDAL / IDAL Assurance Constraints
5. Assumption lifecycle
6. Safety Evidence
7. Safety Coverage / Sufficiency
8. Safety Reassessment in V10
9. Safety Closure inputs to V12
10. Verification Assurance ↔ Safety Assessment dual-view architecture
```

而不是：

> 重写 V0–V12。

------

# 52. Definition of Done

完成条件：

-  ARP4761A full research note 已完成；
-  6 个 principal safety processes 已研究；
-  Appendix P FDAL/IDAL 已完整研究；
-  Safety Requirement provenance 已提取；
-  Failure Condition → Objective → Requirement 链已建立；
-  Assumption lifecycle 已研究；
-  Independence taxonomy 已研究；
-  Safety-analysis method taxonomy 与 Verification Method 分开；
-  SSA/ASA 与 Verification Assurance 的关系已分析；
-  Safety Coverage / Sufficiency 已分析；
-  V10 safety reassessment 已分析；
-  V12 safety closure input 已分析；
-  Standards Map 已更新；
-  Gap Matrix 已更新；
-  ARP4754B cross-standard comparison 已完成；
-  V0–V12 reassessment 已完成但 stable IDs 未无理由修改；
-  没有把 Recommended Practice 写成法规；
-  没有将 Safety Process 强行并入 Generic Verification Process；
-  没有提交 ARP4761A PDF；
-  内部 review package 已生成。

------

# 53. Expected Status After This Round

理想状态：

```
ISO/IEC/IEEE 15288
→ Generic SE baseline candidate


ISO/IEC/IEEE 24748-1
→ Lifecycle baseline candidate


ISO/IEC/IEEE 24748-2
→ Supporting application guidance


SAE ARP4754B
→ Civil-aircraft development-assurance baseline candidate


SAE ARP4761A
→ Civil-aircraft safety-assurance baseline candidate
```

这时我们第一次具备：

```
Generic Systems Engineering
        +
Development Assurance
        +
Safety Assurance
```

三层完整的第一轮 normative foundation。

------

# 54. Recommended Stop Point After ARP4761A

本轮完成后，**不要自动继续 DO-178C / DO-254**。

先进行一次完整：

```
Cross-Standard Consistency & Gap Review
```

覆盖：

```
15288
24748-1
24748-2
ARP4754B
ARP4761A
```

重点判断：

```
哪些 Generic Framework concepts 已得到充分支持？
哪些只是 Aviation Profile？
哪些 Gap 仍需要 item-level standards？
哪些地方需要 15289 / 29148？
是否已经可以正式冻结 DBSE Verification Assurance Framework v0.2？
```

只有完成这次 review 后，再决定：

- DO-178C；
- DO-254；
- DO-297；
- ISO 15289；
- ISO 29148；

谁应该成为下一项研究源。

------

这轮 ARP4761A 很可能是当前 Phase 1 的一个分水岭：前面我们一直在研究“**Verification 怎么做**”，而这份标准开始真正回答“**为什么某些 Verification 必须比另一些更严格，以及这种 rigor 从哪里来**”。Failure-condition classification 会影响 analysis depth，PASA/PSSA 会生成 safety requirements 和 independence constraints，而 FDAL/IDAL 会进一步控制 development-assurance rigor。
