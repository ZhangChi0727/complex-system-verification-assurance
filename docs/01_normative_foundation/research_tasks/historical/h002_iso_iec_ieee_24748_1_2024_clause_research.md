---
title: ISO/IEC/IEEE 24748-1:2024 Historical Clause Research Task
status: superseded
version: 1.0
baseline: historical-pre-v0.2
owner: research
last_updated: 2026-08-20
document_role: historical-task-specification
body_format: preserved-original
dependencies:
  - ../README.md
  - ../../standard_notes/iso_24748_1.md
  - ../../reviews/iso_24748_1_informal_review.md
---

> **Archive control:** This completed pre-v0.2 task specification is retained as research provenance. Its original body and numbering are preserved; current execution status and future work are governed by the parent task register and controlled source baseline.

# ISO/IEC/IEEE 24748-1:2024 Normative Research Task Specification

## 1. Task Purpose

对 **ISO/IEC/IEEE 24748-1:2024 — Systems and software engineering — Life cycle management — Part 1: Guidelines for life cycle management** 开展结构化研究。

本任务的目标不是再次总结 ISO/IEC/IEEE 15288 的 Verification Process，而是回答：

> **ISO 24748-1 如何指导 15288 生命周期过程在实际项目中的组织、映射、裁剪、阶段化、评审和管理，以及这些指导如何影响本项目的 Verification Activity Architecture / DBSE Workflow。**

ISO 24748-1:2024 的定位是为 systems and software life-cycle management 提供统一、整合的指导，并明确用于辅助 15288 和 12207 中 process content 的应用。

因此，本轮研究的核心关系是：

```text
ISO/IEC/IEEE 15288
    defines WHAT processes exist
               ↓
ISO/IEC/IEEE 24748-1
    guides HOW those processes are
    organized and applied in a life cycle
```

---

# 2. Research Positioning

15288 第一轮研究已经得到：

```text
Verification Process
→ Prepare
→ Perform
→ Manage Results
```

以及：

- Verification Strategy；
- Verification Procedure；
- Results / Evidence；
- Traceability；
- Configuration；
- Assurance Case；
- iterative / recursive / concurrent application。

24748-1 的研究重点因此不是重复这些结论。

本标准主要用于回答：

```text
Process
↓
Life Cycle Model
↓
Stage
↓
Entry / Exit Criteria
↓
Decision Gate
↓
Review
↓
Project Adaptation
↓
Process View
```

以及这些机制怎样把 15288 的抽象 process model 转化为项目可执行 lifecycle architecture。

---

# 3. Source Status

研究源：

```text
ISO/IEC/IEEE 24748-1:2024
Systems and software engineering —
Life cycle management —
Part 1: Guidelines for life cycle management
Second edition
2024-03
```

当前附件是 licensed copy。

注意：

> 当前 PDF 是 Redline 版本，包含新版正文和前版差异标识。

文件自身明确说明只有 current base version 才是正式标准内容，Redline 的差异标识由第三方生成，不能被视为出版社正式解释。

因此研究时：

- 可以使用 Redline 帮助理解变化；
- 不要把颜色/删除线本身当 normative source；
- 最终引用 locator 应针对 2024 base text；
- 不要把“2018→2024 change”写成正式 normative requirement，除非该研究确实需要版本差异分析。

---

# 4. Important Source Classification Rule

与 15288 不同，本标准标题和 Scope 明确定位为：

> **Guidelines for life cycle management**

其作用是提供 guidance，补充 15288/12207 的 process application。

因此 Codex 不得把 24748-1 中的建议性 lifecycle guidance 自动提升为：

```text
ISO 15288 conformance requirement
```

必须严格区分：

```text
15288 normative process requirement
vs
24748-1 life-cycle management guidance
```

研究报告建议使用：

- `GUIDANCE`
- `INFORMATIVE ANNEX`
- `INTERPRETATION`
- `FRAMEWORK IMPLICATION`
- `RESEARCH PROPOSAL`

若某一正文语句使用规范性 modal verb，也仍必须结合本标准本身的 scope 和 context 精确表述。

---

# 5. Required Outputs

至少形成：

```text
docs/01_normative_foundation/
standard_notes/
iso_24748_1.md
```

并更新：

```text
standards_map.md
normative_gap_matrix.md
```

如 ISO 15288 review note 中已有 pending issues 被 24748-1 澄清，应同步记录 resolution，但不要删除旧 research provenance。

---

# 6. Primary Research Questions

本轮必须回答以下问题。

### R24748-Q1

Life Cycle Model 与 15288 Process Model 的关系是什么？

### R24748-Q2

Stage 与 Process 是什么关系？

### R24748-Q3

Entry Criteria / Exit Criteria / Decision Gate 如何定义和使用？

### R24748-Q4

是否支持我们当前 V0–V12 作为一个 **Verification Process View / Activity Architecture**？

### R24748-Q5

Project lifecycle adaptation 应如何记录？

### R24748-Q6

不同 development approaches 是否允许不同 process sequencing？

### R24748-Q7

Technical / management reviews 在 lifecycle 中承担什么角色？

### R24748-Q8

Readiness Review、Closure Gate 等 framework concepts 能获得多强支持？

### R24748-Q9

Problem Reporting 应如何跨生命周期统一管理？

### R24748-Q10

标准是否提供 verification-specific coverage、sufficiency 或 independence 规则？

### R24748-Q11

如何避免把 life-cycle stage 与 verification activity 错误建立一对一关系？

### R24748-Q12

Process View 对我们建立 Verification Assurance Process View 有什么直接启发？

---

# 7. Priority Research Scope

重点研究：

```text
Clause 1      Scope
Clause 3      Selected terminology

Clause 4      Life cycle-related concepts
Clause 5      Life cycle stages

Clause 6      Life cycle model adaptation
Clause 7      Relationship with detailed process standards

Annex A       Process concepts
Annex C       Project concepts
Annex D       Process views
Annex E       Development approaches / build planning
Annex F       Candidate joint stakeholder reviews
Annex G       Problem reporting capability
```

不是每一段都需要同等深度。

研究重点应始终围绕：

> **这部分内容是否影响我们的 Verification Activity Architecture、Gate Model、Review Model、Change/Problem Model 或 DBSE information model？**

---

# 8. Layer A — Life Cycle Model Concepts

研究 Clause 4。

重点提取：

- system life cycle；
- life cycle model；
- stage；
- enabling system；
- system-of-interest；
- process application；
- relationship between SoI and enabling-system lifecycles。

目标不是制作生命周期教科书，而是明确：

```text
Life Cycle Model ≠ Process Model
Stage ≠ Process
```

这是本轮最重要的概念边界之一。

需要形成：

```text
Process Model
  describes engineering/management processes

Life Cycle Model
  organizes project progression over time/context

Stage
  groups lifecycle concerns around defined purpose/outcomes
```

最终必须评价：

> 我们的 V0–V12 属于 process/activity architecture，而不应被直接称为 project lifecycle stages。

---

# 9. Layer B — Stage Architecture

研究 Clause 5。

重点研究：

- Concept；
- Development；
- Production；
- Utilization；
- Support；
- Retirement；

但不要机械复制各 stage 内容。

重点提取：

```text
Stage Purpose
Stage Outcomes
Stage Relationship
Entry Criteria
Exit Criteria
Decision
```

标准明确指出 stages 可以存在并行关系，且每个 stage 需要其自身的 entry 和 exit criteria；这些 criteria 形成 project-control mechanism，而不要求固定 waterfall sequence。

### Framework Question

这对当前：

```text
V6 Verification Readiness
V12 Verification Closure
```

有何影响？

初步假设：

```text
Readiness / Closure
```

可能不应被建成独立“technical processes”，而更适合表达为：

```text
Gate / Decision State
```

由：

- criteria；
- evidence；
- risks；
- open anomalies；
- project-control authority；

共同决定。

Codex 应验证或修正这一假设。

---

# 10. Entry / Exit Criteria Research

必须单独建立一节：

```text
Entry / Exit Criteria and Verification Gates
```

研究：

- entry criteria；
- exit criteria；
- milestones；
- decision gates；
- review points；
- stage overlap。

目标是回答：

> Verification Readiness Review 和 Verification Closure 是否应该属于更通用的 Gate Model？

建议比较：

```text
Entry Criteria
   ≈ readiness conditions?

Exit Criteria
   ≈ closure conditions?

Decision Gate
   ≈ approval/authorization event?
```

但严禁直接写：

```text
ISO 24748-1 defines VRR
```

除非标准明确使用该术语。

更合理的输出是：

> 24748-1 provides lifecycle-management guidance supporting criteria-driven readiness and completion decisions; `VRR` and `Verification Closure Gate` remain framework-defined specializations.

---

# 11. Layer C — Lifecycle Adaptation

Clause 6 是本标准的研究核心之一。

需要逐项研究：

```text
6.2 Adaptation sequence
6.3 Life cycle model adaptation guidance
```

特别关注：

- project environment；
- regulatory constraints；
- standards selection；
- development approach；
- stages/processes；
- process model；
- adaptation rationale；
- documentation。

标准明确要求/建议根据：

- organizational context；
- policies；
- regulatory constraints；
- safety/security/etc.；
- stakeholder input；

来选择并调整 lifecycle application。

这对我们的 Verification Assurance Framework 很重要，因为它意味着：

> Generic Framework 不能假设一个固定 lifecycle implementation。

而应该支持：

```text
Framework
↓
Project / Domain Tailoring
↓
Instantiated Verification Process View
```

---

# 12. Development Approach and Process Sequencing

重点研究：

```text
6.2.5
6.2.6
6.2.7
Annex E
```

标准明确指出 development approach 可以是：

- waterfall；
- evolutionary；
- incremental；
- agile；
- spiral；
- other approaches；

并且 processes / activities 可以：

- sequential；
- repeated；
- combined；
- parallel。

同时再次强调 15288/12207 并不规定 processes 的 sequence，也不规定特定 lifecycle model。

### Required Framework Implication

必须形成明确结论：

> **V0–V12 numerical IDs must not imply a universal temporal sequence.**

建议后续表达为：

```text
Verification Activity Architecture
```

并由 project lifecycle model 决定其：

- invocation；
- repetition；
- concurrence；
- sequencing；
- gate relationship。

---

# 13. Adaptation Decision Record

重点研究 6.2.8。

标准建议记录：

- selected processes；
- activities；
- lifecycle mapping；
- relationships；
- adaptation rationale；

并把这些信息纳入 project planning。

这对 DBSE 非常关键。

需要讨论是否新增 framework object：

```text
Lifecycle / Process Tailoring Record
```

或：

```text
Verification Process Instantiation Record
```

候选字段：

```text
project context
applicable standards
selected processes
selected activities
excluded activities
rationale
risk basis
domain constraints
lifecycle stages
entry criteria
exit criteria
decision gates
verification process view
```

但这些字段只能作为 framework proposal，不能宣称由 24748-1 原样规定。

---

# 14. Gap Analysis as an Engineering Activity

24748-1 直接建议把 organization 当前 practices/processes 与适用标准中的 processes / activities / tasks 进行 mapping，以识别 current vs target state gap。

这与本项目当前：

```text
Normative Source
vs
Current DCAS Practice
vs
Proposed Framework
```

非常一致。

必须记录：

> 我们当前的 normative gap analysis methodology 获得了 24748-1 的明确 guidance support。

但也要区分：

```text
ISO lifecycle adaptation gap analysis
```

与：

```text
our Verification Assurance normative gap matrix
```

后者仍然是研究特化。

---

# 15. Layer D — Process Views

重点研究：

```text
Annex D
```

这是对我们 framework 可能最重要的部分之一。

15288 已经说明 Process View 可以跨多个 lifecycle processes 聚合活动和任务。

24748-1 Annex D 应进一步研究：

- Process View purpose；
- concerns；
- outcomes；
- selected lifecycle activities；
- cross-cutting engineering threads。

必须回答：

> **Verification Assurance 是否适合作为一个 Process View，而不是新造一个 ISO process？**

这是本轮最重要的理论问题之一。

建议研究候选模型：

```text
Verification Assurance Process View

selects/constrains activities from:
├─ Project Planning
├─ Assessment & Control
├─ Decision Management
├─ Risk Management
├─ Configuration Management
├─ Information Management
├─ Measurement
├─ Quality Assurance
├─ Requirements
├─ Integration
├─ Verification
└─ Validation
```

如果 Annex D 支持这种 cross-process view 概念，那么我们后续可以把：

```text
V0–V12
```

重新定位成：

> **Verification Assurance Process View Activities**

而不是声称创造一个新的 lifecycle process。

---

# 16. Layer E — Reviews and Gates

研究 Annex F：

```text
Candidate Joint Stakeholder Reviews
```

注意：

> Annex F 是 informative。

标准明确说其中 reviews 是 candidate set，没有意图要求必须采用，也不排除替代或组合方案。

重点研究：

- plan reviews；
- requirements reviews；
- architecture/design reviews；
- test-related reviews；
- acceptance-related reviews；
- reviews 与 milestone / decision gate 的关系。

目标是回答：

> 我们 future VRR / Closure Review / Evidence Review 应属于哪一类对象？

必须避免：

```text
Review = Verification Method
```

这里的 review 更可能属于：

```text
management / technical decision mechanism
```

而不是 15288 6.4.9 中的 verification method taxonomy。

这是后续 DCAS `Review Case` taxonomy 必须特别注意的地方。

---

# 17. Review vs Verification Method Boundary

必须建立专门对照：

```text
Inspection / peer review
within Verification Method context

vs

Lifecycle / technical / management reviews
within project decision context
```

回答：

> 两种“Review”是不是同一层级？

预计结论大概率为：

> 不是。

必须由 Codex 根据 15288 + 24748-1 给出严谨 explanation。

---

# 18. Layer F — Problem Reporting

研究 Annex G：

```text
Problem Reporting Capability
```

以及 6.3 adaptation 中对 unified problem reporting 的说明。

24748-1 建议跨 lifecycle processes 维持统一 problem reporting capability，并根据 category / priority 等方式分类。

这与我们：

```text
Anomaly
Problem
PR
Change
Regression
Closure
```

信息模型直接相关。

必须研究：

```text
Incident
Problem
Anomaly
Change Request
Corrective Action
```

在 15288 / 24748-1 中是否需要保持区别。

不要默认 DCAS 中的 `PR` 可以直接等价为 ISO 的某一个 object。

---

# 19. Problem Lifecycle Model

建议输出候选关系：

```text
Observation
↓
Incident / Anomaly
↓
Problem Classification
↓
Analysis
↓
Disposition
↓
Corrective Change
↓
Re-verification
↓
Closure
```

然后逐项标记：

```text
source-supported
interpretation
framework extension
```

特别关注 Annex G 的：

- category；
- priority；
- status；
- tracking；
- closure；

如果有明确指导，应提取到 future Anomaly Information Model。

---

# 20. Layer G — Project / Technical Reviews

Annex C / F 以及正文中有关：

- decision points；
- milestone reviews；
- project reviews；
- stakeholder reviews；

需要与 V6/V12 进行映射。

重点回答：

### Q

Verification Readiness 是：

- verification technical activity？
- project-control activity？
- gate？
- review？
- combination？

### Q

Verification Closure 是：

- process outcome？
- approval decision？
- stage exit？
- assurance decision？
- baseline event？

不要强行提前给唯一答案。

应形成：

```text
candidate role model
```

供 ARP4754B 后续进一步约束。

---

# 21. Layer H — Detailed Process Standards

研究 Clause 7。

重点不是列完整 standards bibliography，而是识别：

> 24748-1 自己把哪些专题下沉给哪些 detailed process standards。

特别关注：

- ISO/IEC/IEEE 15289；
- 24748-2；
- 24748-6；
- ISO/IEC/IEEE 29148；
- ISO/IEC/IEEE 15939；
- ISO/IEC/IEEE 16326；
- ISO/IEC/IEEE 24641；
- IEEE 1012；
- technical review standards。

标准 bibliography / detailed-standard relationships 已明确列出多个后续来源，包括 15289、24748-2、24748-6、24641、29148 等。

输出：

```text
Follow-up Standards Register
```

但只记录与 Verification Assurance Framework 直接相关的来源。

---

# 22. Key Question: Should 24748-2 Become Priority?

本轮必须判断：

> **ISO/IEC/IEEE 24748-2:2024 是否应加入 Phase 1 高优先级研究？**

24748-1 自身指出 24748-2 提供 ISO 15288 的 application guidance。

因此需要在最终报告中明确：

```text
24748-2 Priority:
High / Medium / Low

Reason:
...
```

这一判断可能改变我们原来：

```text
24748-1 → ARP4754B
```

的研究顺序。

---

# 23. V0–V12 Mapping Required Update

ISO 15288 第一轮得到：

```text
V0–V12 = iterative / recursive / concurrent activity architecture
```

24748-1 应继续回答：

> 这些 activity 怎样映射到 lifecycle stages 和 project gates？

建议增加以下列：

| V Activity | ISO 15288 basis | 24748-1 lifecycle implication | Entity type |
|---|---|---|---|
| V0 | ... | ... | Activity / Planning |
| V1 | ... | ... | Activity |
| V2 | ... | ... | Activity |
| V3 | ... | ... | Activity |
| V4 | ... | ... | Activity |
| V5 | ... | ... | Activity |
| V6 | ... | ... | Gate/Activity? |
| V7 | ... | ... | Activity |
| V8 | ... | ... | Activity |
| V9 | ... | ... | Cross-process activity |
| V10 | ... | ... | Cross-process orchestration |
| V11 | ... | ... | Assurance assessment |
| V12 | ... | ... | Gate/Decision? |

目的不是强制重构，而是发现：

> 我们当前把不同 ontology type 都叫 V-Activity 是否存在概念错误。

这是本轮非常重要的检查。

---

# 24. Expected Architectural Question

Codex 必须明确评价以下候选架构：

```text
Verification Assurance Process View
│
├─ Activities
│   ├─ Basis Analysis
│   ├─ Strategy
│   ├─ Case/Procedure Design
│   ├─ Execution
│   ├─ Result Evaluation
│   ├─ Anomaly/Re-verification
│   └─ Sufficiency Assessment
│
├─ Gates
│   ├─ Readiness Gate
│   └─ Closure Gate
│
├─ Information Items
│
├─ Decisions
│
└─ Cross-process Dependencies
```

这个模型是否比：

```text
V0 → V1 → ... → V12
```

作为统一“activity chain”更符合 15288 + 24748-1？

不要提前假设答案为 Yes。

---

# 25. Standards Map Update

`standards_map.md` 的 ISO 24748 列需要开始填充。

至少研究：

```text
Verification planning
Requirement validation
Requirement verification
Verification method
Verification independence
Verification environment
Configuration control
Traceability
Anomaly management
Regression
Coverage
Evidence
Verification closure
Safety-derived rigor
Reuse of prior evidence
Tool considerations
```

但预计 24748-1 对其中很多项只是：

```text
Lifecycle Guidance
Indirect
Not Addressed
```

不要为了填满矩阵强行建立 support。

---

# 26. New Framework Concerns to Consider Adding

如果研究证据充分，可以考虑向 standards map 新增：

```text
Lifecycle tailoring
Process adaptation
Entry criteria
Exit criteria
Decision gates
Technical reviews
Problem reporting
Process views
Development approach
Process-stage mapping
```

但只有确实对后续 framework architecture 有价值时才添加。

---

# 27. Normative Gap Matrix Update

重点观察 ISO 15288 gaps 是否被 24748-1 部分缓解：

```text
ISO-G05 Regression
ISO-G06 Verification Closure
ISO-G07 Information-item schema
ISO-G08 MBSE automation/model evidence
```

例如：

### Closure

24748-1 可能提供：

- exit criteria；
- decision gates；
- reviews；

从而加强 V12 的 lifecycle management basis。

但即使如此，也不能自动写：

```text
Gap closed
```

除非确实形成完整 Verification Closure model。

更可能状态是：

```text
Partially Addressed
```

---

# 28. Expected New Gap Candidates

根据当前初步阅读，可能出现：

### LC-G01 — Process-to-stage mapping

Generic lifecycle guidance 存在，但 Verification-specific mapping 仍需 framework 定义。

### LC-G02 — Gate semantics

标准提供 lifecycle decision gates，但 Verification Readiness / Closure 的具体 criteria 仍未定义。

### LC-G03 — Review taxonomy

存在多种 review context，需要区分：

- verification inspection；
- technical review；
- stakeholder management review；
- certification review。

### LC-G04 — Tailoring evidence

需要定义 project tailoring 如何形成受控 Verification Assurance evidence。

这些只作为候选，Codex 必须研究后决定是否真正加入 Gap Matrix。

---

# 29. No Over-claim Rules

禁止：

```text
ISO 24748-1 requires V0–V12.
```

禁止：

```text
ISO 24748-1 requires a Verification Readiness Review.
```

禁止：

```text
ISO 24748-1 defines Verification Closure.
```

禁止：

```text
ISO 24748-1 mandates waterfall stages.
```

禁止：

```text
ISO 24748-1 makes reviews a Verification Method.
```

禁止：

```text
ISO 24748-1 requires all stages to execute sequentially.
```

这些都必须通过 source-supported distinction 避免。

---

# 30. Copyright Rules

与 ISO 15288 相同：

- 不提交 PDF；
- 不提交截图；
- 不长段复制；
- repository 中保留 clause locator；
- 使用 paraphrase；
- 对 Annex 明确标记 informative。

---

# 31. Suggested `iso_24748_1.md` Structure

```text
# ISO/IEC/IEEE 24748-1:2024 Research Notes

1. Metadata
2. Research Scope
3. Relationship to ISO 15288
4. Source / Guidance Classification
5. Life Cycle Concepts
6. Life Cycle Model vs Process Model
7. Stage Architecture
8. Entry / Exit Criteria
9. Decision Gates
10. Lifecycle Adaptation
11. Development Approaches
12. Process Selection and Mapping
13. Adaptation Decision Documentation
14. Process Views
15. Reviews and Review Taxonomy
16. Problem Reporting
17. Relationship to Verification Assurance Framework
18. V0–V12 Reassessment
19. Gate / Activity / Decision Ontology Assessment
20. Standards Map Updates
21. Normative / Guidance Gaps
22. Follow-up Standards
23. Open Questions
24. Final Conclusions
```

---

# 32. Required Final Comparison with ISO 15288

报告结尾必须形成：

| Question | ISO 15288 | ISO 24748-1 | Framework Consequence |
|---|---|---|---|
| What processes exist? | primary source | guidance | use 15288 |
| How are they sequenced? | not fixed | lifecycle-model guidance | project-specific |
| How are stages defined? | limited lifecycle concepts | detailed guidance | distinguish stage/process |
| Entry/exit criteria | supporting context | explicit lifecycle guidance | gate model |
| Decision gates | project-control support | stronger guidance | model separately |
| Process views | introduced | elaborated | candidate VAF architecture |
| Adaptation | conformance/tailoring | detailed guidance | instantiation record |
| Reviews | multiple contexts | candidate review guidance | distinguish method vs gate review |
| Problem reporting | process-specific | unified lifecycle guidance | common anomaly/problem model |

---

# 33. Definition of Done

本轮研究完成必须满足：

1. `iso_24748_1.md` 完成；
2. 已清晰区分 Life Cycle Model / Process Model / Stage；
3. 已研究 entry/exit criteria 与 decision gates；
4. 已研究 adaptation sequence；
5. 已研究 process mapping 与 rationale documentation；
6. 已研究 Process Views；
7. 已研究 Annex F reviews；
8. 已研究 Annex G problem reporting；
9. 已重新评价 V0–V12 ontology；
10. 已明确 V6/V12 是 Activity、Gate、Decision 或组合的候选分类；
11. `standards_map.md` 已更新；
12. `normative_gap_matrix.md` 已更新；
13. 已判断 24748-2 的后续优先级；
14. 没有把 guidance 误写成 15288 conformance requirement；
15. 没有把 lifecycle sequence 误写成 universal V-model waterfall。

---

# 34. Core Research Principle

本轮的核心原则是：

> **ISO 15288 告诉我们需要哪些 lifecycle processes；ISO 24748-1 帮助我们理解如何把这些 processes 放进一个实际可管理的 lifecycle architecture。**

因此，不要让 24748-1 去“证明 Verification Process 内容”。

它真正应该改变的是我们对以下对象的理解：

```text
Activity
Process
Process View
Stage
Gate
Review
Decision
Tailoring
Problem
```

如果研究结果表明我们当前 V0–V12 把这些不同 ontology types 混成了一条 activity list，应允许 framework 被重构。

---

# 35. Expected Research Value

完成本轮后，我们应从当前：

```text
V0 → V1 → ... → V12
```

这种 working representation，进一步发展出更严格的结构，例如：

```text
Verification Assurance Process View
        │
        ├─ Verification Activities
        ├─ Cross-process Activities
        ├─ Decision Gates
        ├─ Reviews
        ├─ Information Items
        ├─ Evidence
        └─ Lifecycle Instantiation Rules
```

是否最终采用这一架构，由研究结果决定。

本轮研究成功的标准不是“24748-1 摘要写得完整”，而是回答：

> **我们的 Verification Assurance Framework 应如何被实例化进不同生命周期模型，同时保持 15288 process semantics、项目可裁剪性、criteria-driven gates 和证据完整性。**
