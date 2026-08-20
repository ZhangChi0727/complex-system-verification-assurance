---
title: Five-Source Historical Consistency and Gap Review Task
status: superseded
version: 1.0
baseline: historical-pre-v0.2
owner: research
last_updated: 2026-08-20
document_role: historical-task-specification
body_format: preserved-original
dependencies:
  - ../README.md
  - ../../consolidation/five_source_consistency_gap_review.md
  - ../../../00_overview/research_baseline_v0.2.md
---

> **Archive control:** This completed consolidation task specification is retained as v0.2 research provenance. Its original body and numbering are preserved and do not reopen the reviewed consolidation result.

# Five-Source Cross-Standard Consistency & Gap Review Task Specification

## 1. Purpose

对当前已经完成研究的五个来源进行第一次系统性 consolidation：

```
ISO/IEC/IEEE 15288:2023
ISO/IEC/IEEE 24748-1:2024
ISO/IEC/IEEE 24748-2:2024
SAE ARP4754B
SAE ARP4761A
```

本任务不新增第六个主要标准。

核心目标不是继续积累标准摘要，而是回答：

> **五个来源共同支持的 Verification Assurance Framework 到底是什么；哪些概念应进入 Generic Core，哪些只能属于 Aviation Profile，哪些仍只是 Research Proposal，哪些问题尚不能由现有五源闭合。**

最终应把当前：

```
five separately researched sources
```

转化为：

```
one coherent normative architecture
+
explicit aviation specialization
+
controlled unresolved gaps
```

------

# 2. Current Source Roles to Validate

本轮首先验证而不是默认接受以下 source-role hypothesis：

```
ISO 15288
→ Generic lifecycle/process + V&V + assurance foundation


ISO 24748-1
→ Lifecycle management / stage / gate / process-view guidance


ISO 24748-2
→ Supporting application guidance for ISO 15288


ARP4754B
→ Civil-aircraft Development Assurance profile


ARP4761A
→ Civil-aircraft Safety Assessment / Safety Assurance profile
```

当前 repository 已基本采用这一结构。24748-2 已被明确分类为 `Reviewed Supporting Source`，且没有改变 V0–V12 ontology。

Codex 必须检查是否存在任何 source-role conflict。

若不存在，应在 consolidation 后正式记录并冻结。

------

# 3. Primary Research Question

本轮的总问题是：

> **一个产品无关的 Verification Assurance Framework，应包含哪些稳定对象、活动、关系和 assurance semantics；民机 Development/Safety Assurance 又通过什么 profile-specific constraints 对它进行特化？**

不要问：

> “哪个标准最权威？”

而要问：

```
Which concept?
At what abstraction level?
Supported by which source?
With what normative/guidance strength?
Generic or domain-specific?
What remains unresolved?
```

------

# 4. Required Main Output

建议新增：

```
docs/01_normative_foundation/
consolidation/
five_source_consistency_gap_review.md
```

这是本轮主要研究产物。

同时根据结果更新：

```
docs/01_normative_foundation/standards_map.md
docs/01_normative_foundation/normative_gap_matrix.md


docs/00_overview/terminology.md
docs/00_overview/research_scope.md
docs/00_overview/roadmap.md


docs/03_dbse_workflow/README.md


docs/04_information_model/...
templates/verification_strategy_record.md
```

只有 consolidation 真正证明有必要时才修改模板/信息模型。

------

# 5. Do Not Re-Summarize Standards

严禁把输出写成：

```
Chapter 1 ISO 15288
Chapter 2 ISO 24748-1
Chapter 3 ISO 24748-2
Chapter 4 ARP4754B
Chapter 5 ARP4761A
```

这些工作已经完成。

应按 **Framework Concern** 组织：

```
Verification
Validation
Assurance
Requirement
Verification Obligation
Strategy
Method
Independence
Coverage
Sufficiency
Evidence
Gate
Change
Safety
...
```

每个 concern 横向比较五源。

------

# 6. Consolidation Classification Model

每个 Framework concept 最终只能进入以下类别之一：

```
GENERIC CORE
GENERIC EXTENSION POINT
AVIATION PROFILE
SUPPORTING GUIDANCE
RESEARCH PROPOSAL
OPEN GAP
CONFLICT / CONTEXTUAL SEMANTIC DIFFERENCE
```

其中：

### GENERIC CORE

已有足够通用来源支持，可以进入产品无关 Framework。

### GENERIC EXTENSION POINT

Generic Framework 确认需要这一维度，但具体 semantics 由 domain profile 决定。

例如 independence 很可能属于此类。

### AVIATION PROFILE

ARP4754B / ARP4761A 专用，不可反向提升成所有复杂系统规则。

例如：

```
FDAL
IDAL
Failure Condition Classification
SSA
ASA
```

### SUPPORTING GUIDANCE

主要解释 Generic Core 的实际应用，但不增加新的 Framework obligation。

24748-2 大量内容预计属于此类。

### RESEARCH PROPOSAL

现有来源支持其研究价值，但没有直接定义它。

例如当前：

```
Oracle
Composite Gate
Verification Obligation
```

可能仍包含此类成分。

### OPEN GAP

五源仍无法回答。

------

# 7. Layer 1 — Terminology Reconciliation

这是 consolidation 第一优先级。

建立：

```
Concept
↓
Source Definitions
↓
Semantic Difference
↓
Generic Definition
↓
Profile Definition
```

至少研究以下概念。

### Verification

ISO 15288：

> 对 specified requirements 获得 objective evidence。

ARP4754B：

> implementation 是否满足 validated requirements。

当前 repository 已正确把 ARP 定义保存为 aviation contextual taxonomy，而没有覆盖 ISO generic definition。

本轮必须决定最终结构应否为：

```
Verification
    Generic Core definition
        ↓ specialization/context
Implementation Verification
    Aviation Profile
```

而不是维护两个互相竞争的 `Verification` 定义。

------

### Validation

必须区分：

```
Generic system/intended-use Validation
Requirement Validation
```

ARP4754B 的：

```
requirements correct + complete
```

不能覆盖 ISO 15288 的 intended-use Validation。

最终需要建立 contextual taxonomy。

------

### Requirement

比较：

```
ISO Requirement
ARP4754B Requirement
Safety Requirement
```

ARP4761A 已经确认 Safety Requirement 可以来自 Safety Objective 或 Safety Process Constraint，而不是单一线性链。

本轮必须决定：

```
SafetyRequirement subtypeOf Requirement ?
```

是否足以成为稳定 ontology decision。

------

# 8. Layer 2 — Process / Activity / View / Gate Ontology

统一以下概念：

```
Process
Activity
Task
Process View
Assessment
Review
Decision
Gate
Stage
Lifecycle Model
Orchestration
```

当前 24748-1 已经明确支持：

```
Stage ≠ Process
Process ≠ Process View
Review ≠ Gate
Criteria satisfaction ≠ authorization decision
```

并将 V0–V12 发展成 mixed-ontology Process View。

本轮要决定：

> 这一 ontology 是否已经足够成熟，可以从 `candidate interpretation` 升级成 Framework baseline。

尤其评价：

```
V6 Verification Readiness
V12 Verification Closure
```

是否继续冻结为：

```
Composite Gate
```

以及 Composite Gate 最小结构是否可定义为：

```
Assessment
+ optional Review
+ Decision
+ State/Baseline Event
```

注意 `Composite Gate` 仍可能是 Framework term，而不是标准原生词。

------

# 9. Layer 3 — Verification Assurance Process View

重新评价完整：

```
V0–V12
```

不要主要问每个 V-ID“哪个标准支持”。

要问：

> **这个 V-element 到底是什么 ontology type？它解决什么 concern？它从哪些 source processes 获得行为？**

建议最终表：

| V-ID | Stable Label | Ontology | Generic Source | Aviation Profile | Remaining Gap |
| ---- | ------------ | -------- | -------------- | ---------------- | ------------- |
|      |              |          |                |                  |               |

重点检查：

```
V0 Planning
V1 Verification Basis
V2 Requirement Verifiability
V3 Strategy
V4 Case Design
V5 Procedure
V6 Readiness
V7 Execution
V8 Evaluation
V9 Anomaly Resolution
V10 Change Impact & Re-verification
V11 Coverage & Sufficiency
V12 Closure
```

当前 repository 已把 V10 正式扩展为 Change Impact & Re-verification，并将 ARP4761A Safety Reassessment 作为 aviation subflow。

本轮应判断哪些 V-element 可以冻结名称与 ontology。

------

# 10. Layer 4 — Verification Obligation

这是 consolidation 中最值得重点研究的核心对象之一。

当前五源已经形成：

```
Requirement
Safety Requirement
Safety Objective
Assurance Constraint
Independence Constraint
FDAL / IDAL
```

但真正驱动执行 Verification 的中间对象仍主要是我们提出的：

```
Verification Obligation
```

本轮必须回答：

### Q

Verification Obligation 是否应该正式进入 Generic Core？

### Q

它与 Requirement 是：

```
1 Requirement → N Obligations
```

还是别的关系？

### Q

Safety Requirement 如何生成或约束 obligation？

### Q

Assurance Constraint 是否改变：

```
whether
how
who
with what rigor
with what evidence
```

而不是 requirement 本身？

建议研究：

```
Requirement / Constraint
        ↓
Verification Obligation
        ↓
Verification Strategy
```

是否能够成为 Framework 主干。

------

# 11. Layer 5 — Assurance Architecture

统一：

```
Assurance
Development Assurance
Safety Assurance / Safety Assessment
Verification Assurance
```

ISO 15288 已提供：

```
Claim
→ Argument
→ Evidence
```

并明确 traceability 不能替代 assurance argument。

ARP4754B 又加入 Development Assurance，ARP4761A 加入 Safety Assessment evidence aggregation。

本轮必须回答：

> `Verification Assurance` 是否已经有足够跨标准基础，可以从 research working term 晋级为正式 Framework top-level concern？

候选结构：

```
Assurance
├─ Verification Assurance
├─ Development Assurance      [Aviation]
└─ Safety Assurance/Assessment [Aviation]
```

或者：

```
Verification Assurance
    is a cross-cutting assurance view
    interacting with
Development Assurance
and
Safety Assessment
```

不要提前决定，必须根据现有 source relationships 推导。

------

# 12. Layer 6 — Generic Core vs Aviation Profile

这是本轮最核心的 consolidation deliverable。

至少建立：

| Concept | Generic Core | Aviation Profile | Decision |
| ------- | ------------ | ---------------- | -------- |
|         |              |                  |          |

预计应检查：

```
Verification Strategy
Verification Method
Success Criteria
Evidence
Traceability
Configuration
Change Impact
Coverage
Sufficiency
Independence
Assurance Constraint
Safety Objective
Safety Requirement
Failure Condition
FDAL
IDAL
SSA
ASA
Safety Analysis Method
Certification Credit
```

例如：

### FDAL / IDAL

当前五源研究已经很明确：

```
FDAL / IDAL
≠ Verification Level
```

属于航空 Development Assurance constraint。

因此预计：

```
Generic Core:
Assurance Constraint / Rigor extension point


Aviation Profile:
FDAL / IDAL
```

这种 pattern 很可能成为 consolidation 的重要设计原则。

------

# 13. Layer 7 — Independence Consolidation

当前已经出现：

```
QA Independence
Process Independence
Functional Independence
Item Development Independence
Physical Independence
```

standards map 已明确指出 Generic independence rule 仍然 open，而航空标准提供 typed support。

本轮需要决定 Generic Framework 应采用：

```
IndependenceConstraint
```

作为 extension point，而不是：

```
independent: true/false
```

并将航空 profile 专门化为：

```
Functional
Item Development
Physical
Process
```

同时明确：

```
independence type
≠ independence claim
≠ independence requirement
≠ substantiation evidence
```

------

# 14. Layer 8 — Coverage Model

五源目前支持：

```
Requirement Coverage
Failure Condition Coverage
Safety Objective Coverage
Safety Requirement Coverage
Assumption Coverage
Independence Requirement Coverage
```

但 standards map 仍正确记录：

> no universal taxonomy / no universal percentage。

本轮必须决定是否建立 Generic abstraction：

```
Coverage Obligation
```

例如：

```
Coverage
=
covered population
+
coverage criterion
+
coverage evidence
+
uncovered disposition
```

而：

```
Requirement Coverage
Safety Coverage
Code Coverage [future]
```

作为 profiles。

这可能比现在简单：

```
coverage_obligations: []
```

更加稳定。

------

# 15. Layer 9 — Sufficiency Model

必须避免将五源中的不同 sufficiency 概念混为一体。

当前：

ISO 15288：

```
assurance reasoning
```

ARP4754B：

```
method/procedure sufficiency
```

ARP4761A：

```
heterogeneous safety assessment completion
```

standards map 已正确标注 generic formula 仍 open。

本轮研究问题：

> 是否可以先冻结一个 Generic `Sufficiency Assessment` interface，而不冻结 sufficiency algorithm？

候选：

```
Sufficiency Assessment
inputs:
  obligations
  coverage
  evidence
  limitations
  assumptions
  anomalies
  assurance constraints


output:
  conclusion
  rationale
  residual gaps
```

这可能成为 V11 的稳定 semantic contract。

------

# 16. Layer 10 — Evidence Architecture

这应是本轮第二个最重要的领域。

当前已经有：

```
Verification Result
Verification Data
Development Verification Evidence
Safety Analysis Evidence
Safety Assessment Evidence
```

ARP4754B 已明确帮助我们修正：

```
Result ≠ Evidence
```

不应理解为二值转换，而是：

```
Result
→ may constitute/support Evidence
```

其 applicability、credibility、control、sufficiency 分开评价。

本轮应正式统一：

```
Observation / Raw Record
Result
Evidence
Claim
Argument
```

并明确关系：

```
Result
  may support
Evidence


Evidence
  supports
Argument


Argument
  supports
Claim
```

再决定：

```
Verification Data
```

是 Evidence subtype、container，还是受控 information-item role。

不要在没有依据时把所有航空 artifact 变成 Generic classes。

------

# 17. Layer 11 — Traceability vs Provenance vs Argument

这是一个可能需要新增的三分法：

```
Traceability
Provenance
Argumentation
```

ISO 15288 直接支持 traceability 和 assurance argument，但航空研究又大量出现：

```
source analysis
baseline
allocation
credit basis
assumption origin
safety-requirement origin
```

这些更接近 provenance。

需要明确：

```
Traceability
→ what is related


Provenance
→ where an object/conclusion came from


Argument
→ why evidence justifies a conclusion
```

这可能对未来 DBSE/MBSE 图模型非常重要。

------

# 18. Layer 12 — Change Impact & Re-verification

整合五源：

```
ISO:
change / CM / re-verification


24748:
iterative re-entry


ARP4754B:
modification impact + prior evidence applicability


ARP4761A:
safety reassessment + assumption / DAL / architecture impact
```

最终评价是否可以冻结：

```
V10 Change Impact & Re-verification
```

为 Generic Core concern。

候选统一链：

```
Change
↓
Impact Scope
↓
Affected Requirements / Claims / Assumptions / Configuration
↓
Prior-Evidence Validity
↓
Affected Assurance Constraints
↓
Selected Re-verification / Re-analysis
↓
Updated Evidence
↓
Reassessment / Closure
```

domain profile 只增加影响维度和选择规则。

------

# 19. Layer 13 — Assumption

ARP4761A 已经使 Assumption 成为一个很有潜力的对象：

```
capture
→ allocate
→ confirm
→ convert to requirement
→ change impact
```

但当前 note 有意推迟是否提升到 Generic Core。

这次 review 必须做决定之一：

```
Promote to Generic Core
Keep as Generic Extension Point
Keep Aviation-only
Defer
```

不能继续无限保持“以后研究”。

判断依据必须来自五源整体，而不只是 ARP4761A。

------

# 20. Layer 14 — Safety / Development / Verification Dual or Multi-View Model

当前已经有：

```
Verification Assurance Process View
        ↕
Safety Assessment Process View
```

必须加入 ARP4754B Development Assurance 后重新考虑：

究竟是：

```
Verification Assurance View
        ↕
Development Assurance View
        ↕
Safety Assessment View
```

还是：

```
Development Assurance
as aviation governance layer


Verification Assurance View
        ↕
Safety Assessment View
```

这一点不能靠图画方便性决定。

要研究：

- Development Assurance 是独立 Process View？
- 还是 ARP4754B 对 aircraft/system development processes 的 assurance profile？
- Verification Assurance 在其中是什么位置？

这是本轮最重要的 architecture question 之一。

------

# 21. Layer 15 — Closure

统一：

```
ISO approval/baseline
24748 gate
ARP4754B development completion / OPR / CM / PA
ARP4761A SSA/ASA completion
```

然后确认：

```
V12 Verification Closure
```

是否仍适合作为 Composite Gate。

重点形成：

```
Closure ≠ all tests passed
Closure ≠ review completed
Closure ≠ certification approval
Closure ≠ SSA/ASA
```

候选 semantic contract：

```
Assessment completed
+
Applicable obligations dispositioned
+
Evidence/coverage/sufficiency accepted
+
Anomalies/deviations dispositioned
+
Configuration identified
+
Required dependent assurance assessments completed
+
Authority decision
```

仍然不要强行规定通用 authority。

------

# 22. Cross-Standard Conflict Register

必须新建专门一节。

不要把所有术语差异都“调和掉”。

至少检查：

```
Verification definition
Validation definition
Verification Method taxonomy
Review
Independence
Requirement
Assurance
Coverage
Completion
Evidence
```

分类：

```
TRUE CONFLICT
CONTEXTUAL DIFFERENCE
DIFFERENT ABSTRACTION LEVEL
DOMAIN SPECIALIZATION
COMPATIBLE
```

例如 ISO vs ARP Validation 大概率属于：

```
CONTEXTUAL / DIFFERENT OBJECT LEVEL
```

而不是标准冲突。

------

# 23. Gap Disposition Review

对现有全部 gap：

```
ISO-G01–G08
LC-G01–G04
ARP-G01–G03
SAF-G01–G06
```

逐条重新评价。

允许：

```
KEEP OPEN
PARTIALLY RESOLVED
RESOLVED FOR AVIATION PROFILE
RESOLVED GENERICALLY
MERGE WITH ANOTHER GAP
SPLIT
RENAME
CLOSE
```

这是本轮最重要的实际产出之一。

不要为了证明五源研究成功而关闭 gap。

------

# 24. Particularly Important Gap Decisions

重点：

### ISO-G01 Independence

预计可能变成：

```
Generic extension point established
Aviation profile partially resolved
Universal rule open
```

### ISO-G02 Coverage

可能需要从一个 gap 拆成：

```
Generic coverage meta-model
Domain coverage taxonomies
```

### ISO-G03 Sufficiency

可能转化为：

```
Generic Sufficiency Assessment contract
Domain decision criteria open
```

### ISO-G05

V10 已成熟，考虑：

```
rename gap from whether Change/Re-verification exists
to selection/impact semantics gap
```

### ISO-G06 Closure

Composite architecture 可能已经较成熟。

剩余 gap 主要可能变成：

```
authority
waiver
deviation
reopening
state machine
```

### ISO-G07 Schema

需要判断：

> 是否现在已经应该正式研究 ISO 15289。

------

# 25. Generic-Core Promotion Decisions

本轮必须有一个专门表：

| Candidate | Current | Decision | Basis |
| --------- | ------- | -------- | ----- |
|           |         |          |       |

至少：

```
Verification Obligation
Composite Gate
Coverage Obligation
Sufficiency Assessment
Assurance Constraint
Independence Constraint
Assumption
Evidence Provenance
Verification Credit
Safety Requirement
```

每一个必须明确：

```
PROMOTE
PROFILE-ONLY
KEEP PROPOSAL
DEFER
```

不要继续全部保持 candidate。

------

# 26. Information Model Consolidation

只有完成上述 concept decisions 后，才修改 information model。

禁止：

> 先看现在有哪些 YAML 字段，再倒推 ontology。

正确顺序：

```
Source semantics
↓
Consolidated concepts
↓
Relations
↓
Information model
↓
Template fields
```

重点检查：

```
Requirement
VerificationObligation
VerificationStrategy
VerificationAction
Procedure
Result
Evidence
Claim
Argument
Configuration
Assumption
AssuranceConstraint
IndependenceConstraint
CoverageObligation
SufficiencyAssessment
Change
Decision
Gate
```

及 Aviation Profile entities。

------

# 27. Five-Source Assurance Causal Chain

本轮应尝试建立第一版完整因果链，例如：

```
Need / Requirement
        ↓
Verification Basis
        ↓
Verification Obligation
        ↓
Assurance Constraints
        ↓
Verification Strategy
        ↓
Action / Procedure
        ↓
Result
        ↓
Evidence
        ↓
Coverage + Sufficiency Assessment
        ↓
Argument / Claim
        ↓
Closure Decision
```

航空安全 profile 再提供：

```
Failure Condition
        ↓
Safety Objective / Constraint
        ↓
Safety Requirement
        ↓
FDAL / IDAL / Independence
        ↓
Verification / Assurance Obligation
```

这两条链应能在信息模型中连接，但不能合并成同一条航空专用流程。

------

# 28. Verification Assurance Framework v0.2 Readiness

本轮最后必须回答：

> **五源研究是否足以将 Framework 从 v0.1 research infrastructure 推进到 v0.2 conceptual baseline？**

建议至少检查：

```
Stable terminology?
Stable V0–V12 ontology?
Stable Generic/Profile boundary?
Stable evidence semantics?
Stable change semantics?
Stable gate semantics?
Known unresolved gaps documented?
Information model sufficiently coherent?
```

可能 verdict：

```
READY FOR v0.2
CONDITIONALLY READY
NOT READY
```

不要为了版本推进强行判断 Ready。

------

# 29. Next-Standard Selection Must Be an Output, Not an Input

本轮结束前不预设：

```
DO-178C
DO-254
DO-297
ISO 15289
ISO 29148
```

谁下一个。

根据 gap 做 priority matrix：

```
Framework Gap Relevance
×
Expected New Information
×
Domain Authority
÷
Research Cost
```

再决定。

例如：

- 如果最大 gap 是 information-item semantics → 15289；
- requirements/verification basis → 29148；
- software verification rigor/coverage → DO-178C；
- hardware → DO-254；
- IMA allocation/integration → DO-297。

------

# 30. Required Final Report Structure

建议：

```
# Five-Source Cross-Standard Consistency & Gap Review


1. Purpose and Source Set
2. Source Roles
3. Consolidation Method
4. Generic Core vs Aviation Profile
5. Terminology Reconciliation
6. Process / View / Gate Ontology
7. V0–V12 Consolidation
8. Verification Obligation
9. Verification Strategy
10. Assurance Architecture
11. Independence
12. Coverage
13. Sufficiency
14. Evidence Architecture
15. Traceability / Provenance / Argument
16. Change Impact & Re-verification
17. Assumptions
18. Closure
19. Development Assurance / Safety Assessment Interfaces
20. Cross-Standard Conflict Register
21. Gap Disposition
22. Generic-Core Promotion Decisions
23. Information-Model Implications
24. Framework v0.2 Readiness
25. Next-Standard Prioritization
26. Open Questions
27. Final Conclusions
```

------

# 31. Definition of Done

本轮只有在以下条件满足后结束：

- 五源 source roles 已统一；
- 不再逐标准组织主要结论；
- Verification / Validation contextual definitions 已协调；
- Generic Core / Aviation Profile 已明确；
- V0–V12 ontology 已重新确认；
- Verification Obligation 是否晋级已明确；
- Independence architecture 已明确；
- Coverage meta-model decision 已完成；
- Sufficiency interface decision 已完成；
- Result / Evidence / Claim / Argument 关系已明确；
- Assumption promotion decision 已完成；
- V10 已 consolidate；
- V12 semantics 已 consolidate；
- 所有现有 gap 已重新 disposition；
- cross-standard conflict register 已完成；
- information model 的修改由 consolidation decisions 驱动；
- v0.2 readiness verdict 已给出；
- 下一项标准依据剩余 gap 选择，而不是按引用链自动选择；
- 不新增任何未经五源支持却写成 normative requirement 的规则。

------

# 32. Core Rule

这轮必须坚持：

> **Consolidation is not standard harmonization by force.**

如果两个来源：

- 处于不同 abstraction level；
- 面向不同 system object；
- 具有不同 domain context；

应保留差异，而不是制造一个“平均定义”。

最终 Framework 应呈现为：

```
Generic Core
        │
        ├── Extension Points
        │
        └── Domain Profiles
                 └── Civil Aviation
                       ├── Development Assurance
                       └── Safety Assurance
```

而不是把 ARP4754B/ARP4761A 的航空规则反向写进所有复杂系统。
