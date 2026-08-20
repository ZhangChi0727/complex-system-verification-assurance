---
title: PR #4 ARP4761A External Review
status: superseded
version: 1.0
baseline: historical-pre-v0.2
owner: research
last_updated: 2026-08-20
document_role: historical-review-record
body_format: preserved-original
dependencies:
  - sae_arp4761a_internal_review.md
  - ../standard_notes/sae_arp4761a.md
review_type: pull-request-review
review_target:
  repository: ZhangChi0727/complex-system-verification-assurance
  pull_request: 4
  title: docs: establish ISO 24748-2 and SAE aviation assurance baseline
review_result: request-changes
required_action: targeted-corrections-before-merge
---

> **Archive control:** This review records the original PR #4 `request-changes` verdict. The findings were subsequently addressed; current source and research status are governed by the reviewed standard note, internal review and post-v0.2 baseline.

# PR #4 ARP4761A External Review

## 1. Review Purpose

本记录用于对 PR #4：

`docs: establish ISO 24748-2 and SAE aviation assurance baseline`

进行外部复审。

本轮重点检查：

- SAE ARP4761A research note；
- ARP4754B ↔ ARP4761A cross-standard relationship；
- standards map；
- normative gap matrix；
- V0–V12 reassessment；
- V10 Safety Reassessment；
- V11 safety coverage / sufficiency；
- V12 safety-completion input；
- FDAL / IDAL；
- typed independence；
- Safety Requirement provenance；
- safety-analysis/evidence ontology；
- internal review provenance。

---

# 2. Overall Review Result

评审结论：

> **REQUEST CHANGES — TARGETED CORRECTIONS ONLY**

不需要：

- 回退 PR；
- 重做 ARP4761A 研究；
- 推翻 dual-process-view architecture；
- 回退 V10 `Change Impact & Re-verification`；
- 改变 V0–V12 stable IDs；
- 取消 SAF-G01–SAF-G06；
- 改变下一步 Cross-Standard Consistency & Gap Review。

当前核心架构方向可以保留。

PR 已正确保持：

```text
Verification Assurance Process View
        ↕
Safety Assessment Process View
```

而不是将：

```text
AFHA → PASA → SFHA → PSSA → SSA → ASA
```

替换成 V0–V12。

同时，PR 正确把 SSA/ASA completion 作为 aviation-specific V12 input，而不是把 SSA/ASA 等同于 V12。PR 描述也明确保留 FDAL/IDAL 为 provenance-bearing Assurance Constraints，而不是 Verification Levels。

本次发现：

| ID   | Finding                                           | Severity                   | Required before merge |
| ---- | ------------------------------------------------- | -------------------------- | --------------------- |
| R-01 | ARP4761A `1.1–1.4` locator 不存在                 | Required                   | Yes                   |
| R-02 | Safety Requirement provenance chain 过于线性      | Major research-model issue | Yes                   |
| R-03 | Independence 定义与 substantiation criterion 混合 | Required precision fix     | Yes                   |

修复后预计可以进入 `APPROVE`。

------

# 3. Accepted Core Conclusions

以下内容经复审可以继续保留。

## 3.1 Recommended Practice / Regulation Boundary

ARP4761A 被正确定位为 SAE Aerospace Recommended Practice，而非 regulation。

原文 Scope 明确说明其提供 civil-aircraft safety-assessment guidelines，并允许其他有效过程。

因此当前：

```text
ARP4761A ≠ regulation
```

边界正确。

------

## 3.2 Dual Process-View Architecture

接受：

```text
Verification Assurance Process View
        ↕ typed interfaces
Safety Assessment Process View
```

ARP4761A 自身明确说明 safety-assessment process 是 aircraft/system development 中多个 integral processes 之一，并与 requirements management、configuration management、process assurance 等开发活动交互。

标准也明确指出这些 safety processes 与 development processes 并行、迭代并存在大量数据交互。

因此 Safety Assessment 不应被吸收到 Generic Verification Process 中。

------

## 3.3 V10 Safety Reassessment

当前 V10 增加 aviation Safety Reassessment subflow 的方向正确。

ARP4761A 明确指出设计或 principal assessment 的变化可能驱动其他 assessment 改变，修改后的设计必须重新评估，并可能产生修改或新增 Safety Requirements。

Appendix P 同样要求在 FHA、architecture、PSSA 或 assumptions 改变时重新考虑 FDAL/IDAL assignment。

因此保留：

```
V10 Change Impact & Re-verification
```

并增加：

```
Safety Reassessment
```

是合理的。

------

## 3.4 V11 Safety Coverage / Sufficiency

当前 gap matrix 对 Coverage 和 Sufficiency 仍保持：

```
Partially Supported
```

而没有直接关闭 Generic gap，这是正确的。

ARP4761A PSSA completion 确实要求综合：

- quantitative analysis；
- FDAL/IDAL；
- independence requirements；
- safety requirements；
- traceability；
- assumptions；

而不是依赖单一指标。

因此：

```text
Safety Sufficiency
≠ probability only
≠ trace count only
```

这一结论可以保留。

------

## 3.5 SSA / ASA as Assurance Aggregation

当前 Research Note 把 SSA 描述成 aviation Safety Assurance Assessment，而不是新的 Verification Method，这个方向正确。

SSA 的确评价 implemented system 是否满足 Safety Objectives 和 Safety Requirements，并使用 development verification 与 safety-analysis outputs。

ASA 则在 aircraft level 汇总 system safety results 并确认 aircraft-level objectives/requirements。

因此：

```text
SSA ≠ Generic Verification Process
ASA ≠ V12
```

均应保留。

------

# 4. Finding R-01 — Invalid ARP4761A Locator `1.1–1.4`

## Problem

当前 `sae_arp4761a.md` 写：

> relationship with ARP4754B, DO-178C, DO-254, DO-297 and regulatory/advisory material is contextual `(1.1–1.4)`。

而 internal review 同样使用：

> ```
> 1.1–1.4
> ```

并将 Appendix Q illustrative status 定位到：

> ```
> 1.4; Appendix Q
> ```

但 ARP4761A 正文只有：

```text
1.1 Purpose
1.2 Intended Users
1.3 How to Use This Document
```

不存在：

```text
1.4
```

目录和正文均确认这一点。

------

## Required Change

全仓库搜索：

```text
ARP4761A
1.4
1.1–1.4
1.1-1.4
```

所有 ARP4761A locator 应改为实际条款。

关于：

> ARP4754B / DO-178C / DO-254 / DO-297 coordination

主 locator 应为：

```text
1.3 How to Use This Document
```

关于：

> Appendix Q / examples are illustrative and not standalone normative additions

也应使用 1.3 中相应正文，而不是虚构 `1.4`。

------

## Files to Check

至少：

```text
docs/01_normative_foundation/standard_notes/sae_arp4761a.md
docs/01_normative_foundation/reviews/sae_arp4761a_internal_review.md
docs/01_normative_foundation/standards_map.md
docs/01_normative_foundation/normative_gap_matrix.md
```

------

## Acceptance Criteria

-  没有 ARP4761A `1.4` locator 残留；
-  `1.1–1.4` 全部更正；
-  Appendix Q illustrative-status locator 使用真实正文；
-  internal locator spot-check 同步修正。

------

# 5. Finding R-02 — Safety Requirement Provenance Chain Is Too Linear

这是本轮最重要的研究模型问题。

## Current Model

当前 Research Note principal conclusion 写成：

```text
Failure Condition
→ classification
→ Safety Objective
→ Safety Requirement
→ Assurance / Independence Constraint
→ Verification Obligation
```

同时 `SAF-G01` 也写成：

```text
FC → classification → objective → requirement → obligation
```

这个链作为主要场景是成立的，但如果将它当成 Safety Requirement 的通用 provenance model，就过于狭窄。

------

## Source Evidence

ARP4761A 对 Safety Requirement 的定义不是仅：

> 为满足 Safety Objective 而产生的 Requirement。

原文定义为：

> Safety Requirement 是为实现 Safety Objective，**或者满足 Safety Process 建立的 constraint** 所必需的 Requirement。

因此至少存在两类 source path：

```text
Safety Objective
      ↓
Safety Requirement
```

以及：

```text
Safety-process Constraint
      ↓
Safety Requirement
```

此外 PASA/PSSA 还会产生：

- independence requirements；
- quantitative requirements；
- architecture requirements；
- monitoring/protection requirements；
- assumptions converted into requirements。

例如 PASA 会产生 independence requirements 和 FDAL-related constraints。

PSSA 则进一步产生 independence、quantitative 等 system safety requirements。

ARP4761A 甚至明确指出 assumptions 可以用于定义 safety requirements，以便使 assumptions 能够被验证。

------

## Risk

如果当前链直接进入 information model：

```text
SafetyRequirement.source = SafetyObjective
```

则会丢失：

- Independence Principle-derived requirements；
- Safety Process Constraint-derived requirements；
- Assumption-derived requirements；
- architecture-analysis-derived requirements。

这会直接削弱 V10 change impact 和 safety provenance tracing。

------

## Required Change

不要删除：

```text
Failure Condition
→ Classification
→ Safety Objective
```

而是把 Safety Requirement provenance 改为多源结构，例如：

```text
Failure Condition
        ↓ classification
Safety Objective
        ──────────────┐
                      ↓
Safety-process Constraint ─→ Safety Requirement
                      ↑
Independence Principle ────┤
                      ↑
Controlled Assumption ─────┘
```

然后：

```text
Safety Requirement
        ↓
Verification / Assurance Obligation
```

更简单地，也可以表述为：

```text
Safety Requirement may be derived from:
- Safety Objective;
- Safety Process Constraint;
- Independence Principle;
- Safety Assumption converted to a controlled requirement;
- applicable architecture/analysis result.
```

------

## Required Files

至少调整：

```text
sae_arp4761a.md
normative_gap_matrix.md   # SAF-G01
information model
standards_map.md
terminology.md
```

如果 VSR 中存在 Safety Requirement source fields，也需要同步。

------

## Recommended SAF-G01 Wording

建议从：

```text
FC → classification → objective → requirement → obligation
```

改成：

```text
Safety-derived obligation provenance:
Failure Condition / Classification
        → Safety Objective
        ┐
Safety-process Constraint
Independence Principle
Controlled Assumption
        ├→ Safety Requirement
        → Verification / Assurance Obligation
```

不要把所有 Safety Requirements 强制放在 Safety Objective 后面。

------

## Acceptance Criteria

-  Safety Requirement definition 包含 objective 和 safety-process constraint 两类 origin；
-  SAF-G01 不再表现成唯一线性 chain；
-  information model 支持多源 provenance；
-  Independence Principle / Assumption-derived requirement 不丢失来源；
-  Verification Obligation 仍必须通过 requirement/constraint relation 形成，不从 Failure Condition 自动生成。

------

# 6. Finding R-03 — Independence Definition and Substantiation Criteria Are Mixed

## Current Wording

Research Note §14 当前写：

```text
Item Development Independence
— sufficient separation/difference of item requirements and development sources
```

这个描述更接近 Appendix P / CMA 中的 **substantiation criterion**，而不是 2.2 的标准定义。

------

## Source Definition

ARP4761A 2.2 定义：

```text
Functional Independence
→ minimizes common development errors by using different functions

Item Development Independence
→ minimizes common development errors by using different item designs
```



而在 Appendix P 的 IDAL assignment 中，分析者才进一步通过：

- requirements；
- development processes；
- common sources of error；

评价不同 item 是否具有充分的 item-development independence。

也就是说必须区分：

```text
Definition
```

和：

```text
Substantiation / analysis criterion
```

------

## Required Change

§14 建议改为：

```text
Item Development Independence
Definition:
A characteristic that minimizes the likelihood of common development errors by using different item designs.

Framework / substantiation interpretation:
Appendix P and CMA assess whether common sources of development error across item requirements/design/development processes are sufficiently mitigated to substantiate the claimed independence.
```

Functional Independence、Physical Independence、Process Independence 也建议采用同一 discipline：

```text
source definition
→ framework interpretation
→ substantiation method/evidence
```

不要把分析方法中的判定条件直接覆盖 2.2 definition。

------

## Acceptance Criteria

-  Item Development Independence source definition 与 2.2 一致；
-  Appendix P substantiation criteria 独立描述；
-  terminology baseline 不使用分析 criterion 替代 definition；
-  typed-independence architecture 保持不变。

------

# 7. Recommended Non-Blocking Checks

## 7.1 Safety Requirement Core Definition

当前 research-note 表格中：

> ```
> Requirement implemented to satisfy one or more Safety Objectives
> ```

建议一并修正。

更准确的 framework paraphrase 应保留：

> requirement necessary to achieve a Safety Objective **or satisfy a constraint established by the Safety Process**。

否则即使 R-02 主链修正，术语表仍会重新引入单一来源。

------

## 7.2 FDAL Table P1 Wording

当前：

```text
Catastrophic → A
Hazardous → B
Major → C
Minor → D
No Safety Effect → E
```

本身有 Appendix P Table P1 直接依据。

但必须继续明确这是：

> **top-level / initial FDAL assignment**

而不是 universal final mapping。

ARP4761A 后续允许根据 Functional Failure Sets、functional independence、architecture 等进行 assignment refinement。

当前研究 note 已基本做到这一点，因此这里只要求 consistency check，不是 blocker。

------

## 7.3 Internal Review Provenance

当前：

```
sae_arp4761a_internal_review.md
```

记录：

```text
Blocking findings: 0
Required changes remaining: 0
READY FOR EXTERNAL/PR REVIEW
```

不要删除或篡改这一历史结果。

修正后建议追加：

```markdown
## External PR Review Follow-up

PR #4 external review identified:

- R-01 invalid §1.4 locator;
- R-02 Safety Requirement provenance over-linearity;
- R-03 independence definition/substantiation separation.

The original internal-review result is preserved as historical research provenance.

Current disposition:
...
```

然后建立 finding disposition table。

------

# 8. Accepted Gap-Matrix Direction

以下状态建议不因本 review 改变：

```text
ISO-G01 Verification independence
→ Partially Supported

ISO-G02 Verification coverage
→ Partially Supported

ISO-G03 Verification sufficiency
→ Partially Supported

ISO-G05 Change impact and re-verification
→ Partially Supported

ISO-G06 Verification closure
→ Partially Supported
```

当前 gap matrix 很好地避免了把航空 profile rules 自动提升为 Generic rules。

新增：

```text
SAF-G01
SAF-G02
SAF-G03
SAF-G04
SAF-G05
SAF-G06
```

也可以保留。

其中只需要重写 SAF-G01 provenance semantics。

------

# 9. Accepted Information-Architecture Direction

建议继续保留候选对象：

```text
FailureCondition
SafetyObjective
SafetyRequirement
Assumption
IndependencePrinciple
AssuranceConstraint
SafetyAnalysis
SafetyAssessment
SafetyEvidence
```

但仍保持：

```text
Candidate / Aviation Profile
```

状态。

尤其：

```text
Assumption
```

现在还不应直接提升到 Generic Core。

当前 internal review 也正确将 generic promotion 推迟到后续 cross-standard review。

------

# 10. No Architecture Rollback Required

以下内容不得因本 review 被回退：

```text
V10 = Change Impact & Re-verification
```

不得恢复为：

```text
V10 = Regression
```

保留：

```text
SSA/ASA → V11/V12 aviation inputs
```

而不是：

```text
SSA = V11
ASA = V12
```

保留：

```text
Safety Analysis Method ≠ Verification Method
```

保留：

```text
MBSA ≠ MBSE
```

保留：

```text
FDAL/IDAL ≠ Verification Level
```

保留：

```text
Safety Assessment Process View ≠ V0–V12
```

------

# 11. Required Finding Disposition

Codex 修正后，在 review record 或 internal-review follow-up 中记录：

| Finding | Status      | Files changed | Resolution |
| ------- | ----------- | ------------- | ---------- |
| R-01    | OPEN/CLOSED |               |            |
| R-02    | OPEN/CLOSED |               |            |
| R-03    | OPEN/CLOSED |               |            |

全部关闭后再请求 PR re-review。

------

# 12. Definition of Done

PR #4 可重新申请 approval 的条件：

-  ARP4761A `1.4` 错误 locator 全部修正；
-  Safety Requirement provenance 改为多源模型；
-  SAF-G01 已同步修正；
-  Safety Requirement terminology 已包含 safety-process constraint 来源；
-  Independence source definition 与 substantiation criterion 已分离；
-  Item Development Independence 不再用 Appendix-P criterion 替代 2.2 definition；
-  FDAL Table P1 仍明确为 initial/top-level assignment；
-  internal review 保留历史 provenance；
-  external PR findings 有 disposition；
-  V0–V12 stable IDs 未变化；
-  V10 rename 未回退；
-  dual process-view architecture 未回退；
-  Generic / Aviation Profile boundary 未被削弱。

------

# 13. Expected Re-review Result

如果上述三项 required findings 正确关闭，我预期：

```text
Normative/source accuracy:
PASS

ARP4761A safety-process interpretation:
PASS

ARP4754B ↔ ARP4761A boundary:
PASS

V0–V12 reassessment:
PASS

Safety-assurance ontology:
PASS WITH CORRECTIONS APPLIED

Gap matrix:
PASS

Research provenance:
PASS

Expected review result:
APPROVE
```

------

# 14. Final Review Position

PR #4 的主要研究成果是成立的。

特别值得保留的是：

```text
Generic Systems Engineering
        +
Civil-Aircraft Development Assurance
        +
Civil-Aircraft Safety Assurance
```

三层结构，以及：

```text
Verification Assurance Process View
        ↕
Safety Assessment Process View
```

双视图架构。

本次 review 发现的问题不是研究路线错误，而是三个 **source-provenance / ontology-strength** 问题：

```text
1. Locator must be exact.
2. Safety Requirement provenance must allow multiple safety-process origins.
3. Standard definitions must not be silently replaced by substantiation criteria.
```

完成这三项修正后，不需要再扩张 PR scope。

下一步仍应保持 PR 中已经提出的：

> **Cross-Standard Consistency & Gap Review across ISO 15288, ISO 24748-1/2, ARP4754B and ARP4761A**

而不是立即进入 DO-178C / DO-254 / DO-297。

```
最重要的是第二项。ARP4761A 的 Safety Requirement 定义明确保留了 **Safety Objective** 和 **safety-process constraint** 两个来源，因此我们不能让未来信息模型退化成单一路径 `FC → Objective → Requirement`。

等 Codex 更新 PR #4 后，你可以直接让我再复审，我会重点检查这三项 finding 是否真正关闭。
```
