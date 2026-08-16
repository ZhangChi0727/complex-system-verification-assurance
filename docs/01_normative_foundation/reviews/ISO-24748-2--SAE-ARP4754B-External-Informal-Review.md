---
title: ISO 24748-2 / SAE ARP4754B External Informal Review
status: completed
version: 0.2
last_updated: 2026-08-16
review_type: external-informal-review
review_scope:
  - ISO/IEC/IEEE 24748-2:2024 targeted applicability review
  - SAE ARP4754B full clause-level research
  - cross-standard standards map
  - normative gap matrix
  - Verification Assurance Process View
  - Verification Strategy Record
review_target_branch: agent/iso24748-2-arp4754b-research
review_result: ready-for-pr-review
required_action: completed
blocking_findings_remaining: 0
---

# ISO 24748-2 / SAE ARP4754B Research — External Informal Review

## 1. Review Purpose

本记录用于对本地研究分支：

`agent/iso24748-2-arp4754b-research`

进行提交 PR 前的外部非正式评审。

本轮研究主要包括：

- ISO/IEC/IEEE 24748-2:2024 targeted applicability & delta review；
- SAE ARP4754B full clause-level research；
- standards map 更新；
- normative gap matrix 更新；
- V0–V12 reassessment；
- V10 `Regression` → `Change Impact & Re-verification`；
- Verification Strategy Record aviation-profile candidate fields；
- internal research review。

本评审不是要求重新执行 ISO 24748-2 或 ARP4754B 全量研究。

目标是：

> 检查研究结论的 normative strength、ontology strength、Generic/Aviation boundary、evidence semantics 和 provenance discipline 是否足够严谨，以决定当前分支是否适合进入 PR review。

---

# 2. Overall Review Result

评审结论：

> **CONDITIONALLY READY — TARGETED CORRECTIONS REQUIRED BEFORE PR**

没有发现需要：

- 回退当前分支；
- 推翻 ISO 24748-2 targeted-review strategy；
- 重做 ARP4754B 全条款研究；
- 回退 V0–V12 mixed ontology；
- 回退 V10 rename；
- 改变下一项研究为 ARP4761A；

的架构性问题。

本轮发现：

| ID   | Finding                                                      | Severity | Required before PR |
| ---- | ------------------------------------------------------------ | -------: | -----------------: |
| M-01 | Test Readiness Review 与 V6 的 ontology relation 过强        |    Major |                Yes |
| M-02 | Result → Evidence 被表达为过强的必要条件转换规则             |    Major |                Yes |
| m-01 | `Normative Research Note` 标题存在 source-strength 歧义      |    Minor |        Recommended |
| m-02 | Appendix A `R*/R/A/N` 需要保持 Objective × FDAL provenance   |    Minor |        Recommended |
| m-03 | `certification_credit_intent` 与 Assurance Applicability 混合 |    Minor |        Recommended |
| m-04 | Internal Review 应记录本轮 external findings disposition     |    Minor |                Yes |

这里的 `Major` 表示：

> **PR 前必须处理的 research-strength / ontology issue**

而不是：

> framework architecture fundamentally incorrect。

预计所有 finding 都可通过局部修改关闭，无需大规模重构。

---

# 3. Accepted Research Conclusions

以下研究结论经本轮评审可以保留。

## 3.1 ISO 24748-2 定位

接受：

`Framework Delta: Minor`

接受：

`Reviewed Supporting Source`

接受：

> ISO 24748-2 是 ISO 15288 application guidance，而不是独立 Verification Assurance requirement layer。

接受：

> ISO 24748-2 不改变当前 ISO 15288 baseline interpretation。

接受：

> ISO 24748-2 不改变 V0–V12 mixed ontology。

接受：

> ISO 24748-2 不定义 V6 或 V12。

因此不需要把 targeted review 升级成完整 standalone standards research slice。

---

## 3.2 Generic / Aviation Profile Separation

当前研究已经开始明确区分：

`Generic Verification Assurance Framework`

与：

`Civil Aviation Development Assurance Profile`

这一方向正确。

特别保留：

- FDAL 不属于所有复杂系统的 Generic rule；
- ARP4754B Process Independence 不应提升成 universal verification independence；
- certification-oriented evidence control 不等于所有领域必须采用同等 assurance rigor；
- ARP4754B recommended practices 不应表述为法规；
- certification approval 不等于 verification evidence。

---

## 3.3 Coverage / Sufficiency Gap Disposition

接受当前谨慎分类：

`ISO-G02 Verification Coverage`
→ `Partially Supported — Requirements Coverage Only`

而不是：

`Closed`

接受：

`ISO-G03 Verification Sufficiency`
→ `Partially Supported`

ARP4754B 对 verification methods/procedures sufficiency 提供重要 aviation-domain support，但不足以建立 Generic total verification sufficiency theory。

---

## 3.4 Verification Independence

接受：

`ISO-G01 Verification Independence`
→ `Partially Supported`

并保持：

`Generic Framework`
→ independence is an assurance/strategy dimension

`Aviation Profile`
→ applicability can depend on FDAL / objective

不要将 ARP4754B 的 independence recommendations 提升为 universal Generic requirement。

---

## 3.5 V10 Rename

明确接受：

`V10 Regression`

重命名为：

`V10 Change Impact & Re-verification`

Stable ID 保持不变。

这一修改比原有 `Regression` 更准确地表达：

```text
change
→ impact analysis
→ affected assurance obligations
→ previous evidence applicability
→ selected re-verification
→ evidence supplementation
→ updated substantiation
```

不得在本轮 finding correction 中回退该修改。

---

# 4. Finding M-01 — V6 / Test Readiness Review Ontology Relation Is Too Strong

## 4.1 Current Problem

当前 SAE ARP4754B research note / DBSE interpretation 中存在类似：

> `Test readiness review is an aviation specialization of V6`

的表达。

该表述的 ontology strength 过高。

ARP4754B 的 Test Readiness Review 是针对 testing/demonstration context 的特定 readiness review。

而 Generic：

`V6 Verification Readiness`

作为 framework-defined composite gate，范围明显更广。

V6 可能需要考虑：

- verification basis readiness；
- method/procedure readiness；
- test readiness；
- analysis readiness；
- inspection/review readiness；
- verification environment readiness；
- enabling-system readiness；
- verified configuration readiness；
- evidence infrastructure readiness；
- unresolved anomaly status；
- readiness assessment；
- review input；
- authorization decision。

因此不能由一个 test-specific review 直接推出：

`Test Readiness Review specializationOf V6`

---

## 4.2 Ontology Risk

如果保留当前表达，未来 MBSE metamodel 很可能错误建立：

`TestReadinessReview --specializationOf--> V6`

这会混淆：

- activity；
- review；
- assessment；
- gate；
- decision；

并削弱此前 ISO 24748-1 研究已经建立的：

`Review ≠ Gate`

`Assessment ≠ Authorization Decision`

边界。

---

## 4.3 Required Change

全仓库搜索：

- `aviation specialization`
- `specialization of V6`
- `Test Readiness Review`
- `test readiness review`

检查所有 V6 relation。

建议统一改成：

> **ARP4754B Test Readiness Review is an aviation-profile, test-specific readiness review that can contribute to the framework-defined V6 Verification Readiness composite gate. It is neither equivalent to V6 nor evidence that all verification methods require an analogous formal readiness review.**

建议中文解释：

> ARP4754B Test Readiness Review 是航空 profile 中面向 testing/demonstration 的特定 readiness review，可作为 V6 Verification Readiness composite gate 的候选输入或组成活动；它不是 V6 本身，也不足以证明其他 verification methods 必须具有对应的正式 readiness review。

---

## 4.4 Preferred Relation

优先使用：

`contributesTo(V6)`

或：

`candidateComponentOf(V6)`

不要使用：

`equivalentTo(V6)`

也暂不使用：

`specializationOf(V6)`

除非后续 ontology research 提供更严格依据。

---

## 4.5 Acceptance Criteria

M-01 只有在以下条件满足后关闭：

- [ ] 不再将 Test Readiness Review 直接描述为 V6 specialization；
- [ ] 明确其 test-specific scope；
- [ ] 明确它可以 contribute to V6；
- [ ] 明确 V6 scope 大于 Test Readiness Review；
- [ ] 保留 Review / Assessment / Decision / Gate distinction；
- [ ] 不推导其他 verification methods 必须存在对应 formal readiness review。

---

# 5. Finding M-02 — Result → Evidence Conversion Rule Is Overstated

## 5.1 Current Problem

当前研究中存在类似表述：

> `result ≠ evidence`：结果在来源、方法、对象/环境配置、完整性、控制和适用 claim 都可审查后，才可作为 evidence 使用。

以及类似：

> Verification Data 只有在 provenance、configuration、control 和 applicable claim 可复核时才能用于 compliance substantiation。

研究方向正确，但逻辑强度过高。

---

## 5.2 Ontology Problem

当前措辞隐含：

`Verification Result`

经过一组条件后：

`becomes Evidence`

即：

```text
Result
+ provenance
+ method
+ configuration
+ completeness
+ claim applicability
→ Evidence
```

但这混合了至少五个不同概念：

1. Evidence identity；
2. Evidence provenance；
3. Evidence integrity/control；
4. Evidence applicability；
5. Evidence sufficiency。

一个 Verification Result 可以：

- 构成 evidence；
- 支持某个 claim；
- 对 Claim A applicable；
- 对 Claim B irrelevant；
- provenance 不完整；
- configuration control 不充分；
- assurance credibility 不足；
- 或不足以独立 substantiate claim。

这些状态不能简单压缩成：

`not evidence` → `evidence`

二值转换。

---

## 5.3 Preferred Evidence Model

建议采用：

```text
Verification Result
→ may constitute/support
→ Evidence
```

Evidence 再具有：

- provenance；
- source activity；
- method/procedure；
- verified object；
- verified configuration；
- environment；
- integrity/control；
- traceability；
- claim applicability；
- assurance credibility；
- contribution to sufficiency。

因此：

`Evidence`

与：

`Evidence acceptable/sufficient for Claim X`

不是同一个 predicate。

---

## 5.4 Required Change

修改 SAE ARP4754B research note、standards map、terminology 或其他受影响文件中类似的必要条件式表达。

建议替换为：

> **Verification Result can constitute or support Evidence. Its credibility, applicability and substantiation value for a particular compliance or assurance claim depend on factors such as provenance, verification method/procedure, verified configuration and environment, data control, and traceability to the claim. ARP4754B does not establish a generic Result-to-Evidence conversion rule.**

中文：

> Verification Result 可以构成或支持 Evidence。其对特定 compliance/assurance claim 的可信性、适用性和 substantiation value 取决于 provenance、verification method/procedure、verified configuration/environment、data control 以及与该 claim 的 traceability。ARP4754B 本身不建立通用的 Result→Evidence 转换判据。

---

## 5.5 Preserve Existing Research Direction

不要因此删除：

`Result ≠ Evidence`

这一研究区分。

更准确的表达应是：

> **Result 和 Evidence 是不同的 assurance roles / ontology concepts；某个 Result 可以被用作或支持 Evidence，但不能仅凭“产生了结果”推出该结果足以支持目标 Claim。**

未来可以进一步研究：

```text
Result
→ Evidence
→ Argument
→ Claim
```

但本轮不要提前建立完整 assurance-case metamodel。

---

## 5.6 Acceptance Criteria

M-02 关闭条件：

- [ ] 删除 Result 必须满足固定条件后“才成为 Evidence”的二值转换表达；
- [ ] 保留 Result 与 Evidence 的 ontology distinction；
- [ ] 明确 Result may constitute/support Evidence；
- [ ] Evidence applicability 与 Evidence identity 分离；
- [ ] Evidence sufficiency 与 Evidence identity 分离；
- [ ] Claim applicability 被建模为 relation/property，而不是 Evidence existence condition；
- [ ] 不声称 ARP4754B 定义了 Generic Result→Evidence conversion rule。

---

# 6. Finding m-01 — `Normative Research Note` Title Ambiguity

## Problem

SAE ARP4754B note 当前使用类似：

`SAE ARP4754B Normative Research Note`

的标题。

Repository 中的 `normative foundation` 可以合理指：

> standards / authoritative-source foundation

但 ARP4754B 本身属于 Recommended Practice。

因此 `Normative Research Note` 容易被误读为：

> ARP4754B itself has regulatory/normative force equivalent to regulation.

---

## Recommended Change

建议改为：

`SAE ARP4754B Research Note`

或：

`SAE ARP4754B Standards Research Note`

目录仍可保持：

`01_normative_foundation`

无需重命名 repository architecture。

---

## Acceptance Criterion

- [ ] 文档标题不造成 ARP4754B regulatory status 歧义；
- [ ] 正文继续明确 Recommended Practice / certification-context boundary。

---

# 7. Finding m-02 — Preserve Appendix A Objective × FDAL Provenance

## Problem

当前对：

`R* / R / A / N`

的解释基本正确。

但未来 schema 化时存在把这些值 flatten 成通用：

`objective_applicability`

enum 的风险。

这些 marking 的语义依赖：

`Objective × FDAL × Appendix A cell`

上下文。

因此：

`R*`

不能脱离 objective 和 FDAL 独立解释为一种通用 assurance level。

---

## Required/Recommended Treatment

如果 VSR 保留：

```yaml
objective_reference:
objective_applicability:
process_independence_required:
```

则同时确保能够保存：

```
source_standard:
source_location:
objective_reference:
fdal:
objective_applicability:
```

不要把：

```
R* / R / A / N
```

建模成脱离 source/objective/FDAL 的 Generic assurance-level enum。

------

## Important Boundary

继续保持：

```
N
```

不等于：

```
engineering verification unnecessary
```

而只表示 Appendix A 对相应 certification objective / FDAL cell 的 applicability classification。

------

# 8. Finding m-03 — `certification_credit_intent` Should Not Be Implied by Assurance Applicability

## Current Candidate Schema

当前 VSR 中类似：

```
assurance_applicability:
  assurance_level:
  objective_reference:
  objective_applicability:
  process_independence_required:
  system_control_category:
  certification_credit_intent:
```

------

## Problem

前几项主要回答：

> 某 assurance objective 在某 assurance level 下如何适用？

而：

```
certification_credit_intent
```

回答的是：

> 项目准备如何使用某项 activity/evidence/objective satisfaction 获得 certification credit？

这是 project/certification-use relation，不完全属于 objective applicability。

------

## Recommended Change

最低限度：

```
certification_credit_intent: # candidate project/certification-use relation; not implied by FDAL
```

更理想的未来模型：

```
Assurance Applicability
        ≠
Certification Credit Intent
```

本轮不强制进行 schema restructuring。

只需避免形成：

```
FDAL → certification credit intent
```

的隐含因果关系。

------

# 9. Finding m-04 — Internal Review Provenance Must Be Preserved and Updated

## Current Situation

当前：

```
iso_24748_2_arp4754b_internal_review.md
```

给出：

```
READY FOR EXTERNAL/PR REVIEW
```

以及：

```
Blocking findings: 0
Required changes remaining: 0
```

这可以作为当时 internal review 的历史结论保留。

不要删除或重写成“internal review 当时发现了本轮 external findings”。

------

## Required Change

建议在 internal review 后追加：

```
## External Informal Review Follow-up


A subsequent external informal review identified additional
research-strength and ontology findings before PR creation.


Findings:


- M-01 — V6 / Test Readiness Review ontology relation
- M-02 — Result / Evidence ontology strength
- m-01 — ARP research-note title ambiguity
- m-02 — Appendix A applicability provenance
- m-03 — certification-credit-intent dimensionality


The original internal-review result is retained as research provenance.


Current branch status:


CHANGES REQUIRED BEFORE PR
```

修复后再追加：

```
## Finding Disposition


| Finding | Disposition | Evidence |
|---|---|---|
| M-01 | CLOSED | ... |
| M-02 | CLOSED | ... |
| m-01 | CLOSED / ACCEPTED | ... |
| m-02 | CLOSED / ACCEPTED | ... |
| m-03 | CLOSED / ACCEPTED | ... |


Final status:


READY FOR PR REVIEW
```

------

# 10. 24748-2 Targeted Review — No Rework Required

除非 Codex 在处理上述 findings 时发现新的 source conflict，否则：

```
iso_24748_2_targeted_review.md
```

不需要重新研究。

保持：

```
Framework Delta:
Minor


Full standalone research:
No


Source Role:
Reviewed Supporting Application Guidance


V0–V12 ontology change:
No
```

24748-2 对：

- planning integration；
- lifecycle/process application；
- decision gates；
- enabling systems；
- configuration/evidence relationships；

提供 supporting semantics。

但不要把这些 guidance 解释成新的 ISO 15288 requirements。

------

# 11. SAE ARP4754B — No Full Rework Required

不要求重新执行 full clause-level research。

当前研究已经合理覆盖：

- Development Assurance；
- Requirement terminology；
- Requirements Validation；
- Implementation Verification；
- Process Independence；
- Verification Planning；
- Verification Methods；
- Coverage Analysis；
- Sufficiency；
- Test Readiness Review；
- Unintended Behavior；
- Verification Data；
- Configuration Management；
- Process Assurance；
- Modification Impact；
- Evidence Reuse；
- Appendix A；
- V0–V12 reassessment。

本轮只要求修正：

> ontology strength / source-strength / relation semantics。

------

# 12. Gap Matrix Disposition

除非 source evidence 明确要求改变，否则保持：

```
ISO-G01 Verification Independence
→ PARTIALLY SUPPORTED


ISO-G02 Verification Coverage
→ PARTIALLY SUPPORTED
   requirements-oriented coverage


ISO-G03 Verification Sufficiency
→ PARTIALLY SUPPORTED
   method/procedure sufficiency support
```

不要升级成：

```
CLOSED
```

同时保留新增 ARP gaps，例如：

- Assurance applicability / rigor；
- Cross-level verification credit；
- Unintended-behavior assurance；

前提是当前 gap definition 没有把 aviation-specific concern 错误提升成 universal Generic requirement。

------

# 13. V10 Disposition

保持：

```
V10 Change Impact & Re-verification
```

不要恢复：

```
V10 Regression
```

继续保持 stable ID。

建议全仓库检查旧 label：

- `V10 Regression`
- `Regression`
- `regression stage`

区分：

1. historical description；
2. generic regression concept；
3. obsolete V10 label。

只替换第三类。

------

# 14. Verification Strategy Record Disposition

当前新增 aviation-profile candidate fields 可以保留，包括：

- assurance applicability；
- cross-level verification credit；
- unintended behavior；
- historical evidence / certification credit。

但必须继续标记为：

```
candidate
```

或：

```
aviation-profile candidate
```

不得因为 ARP4754B 研究而提升成 Generic mandatory schema。

特别检查：

```
process_independence_required
```

应具有 aviation applicability context。

```
certification_credit_intent
```

不得被解释为 FDAL 自动推导结果。

```
historical evidence credit
```

必须保留 applicability / baseline / configuration / previous evidence assessment 条件。

------

# 15. Cross-Level Verification Credit

本轮研究识别出的：

```
ARP-G02 Cross-level verification credit
```

建议保留。

未来 information model 很可能需要区分：

```
Requirement allocated to
        ≠
Verification activity performed at
        ≠
Evidence generated by
        ≠
Evidence accepted by
        ≠
Verification credit claimed by
```

本轮不要急于建立最终 relation schema。

只需保持 gap 和 research question。

------

# 16. Evidence Architecture Boundary

本轮修正后建议暂时保持以下 architecture hypothesis：

```
Verification Activity
        ↓
Verification Result
        ↓
may constitute/support
        ↓
Evidence
        ↓
supports
        ↓
Argument
        ↓
Claim
```

同时 Evidence 具有或关联：

```
provenance
verified object
verified configuration
environment
method/procedure
control/integrity
traceability
claim applicability
```

但：

> 此模型目前仍属于 Framework research hypothesis。

不要声称 ARP4754B 直接定义了完整 Claim–Argument–Evidence architecture。

------

# 17. Required Repository Consistency Pass

修正后执行一次全仓库 consistency search。

至少检查：

```
Test Readiness Review
specialization
specialization of V6
result ≠ evidence
becomes evidence
only ... evidence
Normative Research Note
R*
objective_applicability
certification_credit_intent
V10 Regression
Change Impact & Re-verification
Blocking findings
Required changes remaining
```

目的不是机械替换，而是检查 semantic consistency。

------

# 18. Changelog / Roadmap

如当前 Changelog 已记录本轮研究成果，可以保留。

完成 external informal review corrections 后，应补充：

```
- Applied external informal review corrections to the
  ISO 24748-2 / ARP4754B research slice.
- Refined the relationship between ARP4754B Test Readiness Review
  and framework-defined V6 Verification Readiness.
- Refined Verification Result / Evidence semantics to separate
  evidence identity, applicability, control and sufficiency.
```

不要写：

```
fixed incorrect ARP4754B research
```

因为本轮问题主要是 interpretation strength refinement，不是标准条款研究整体错误。

------

# 19. Required Finding Disposition Table

Codex 修改完成后，应在本 review record 中填写：

| Finding | Status               | Files changed | Resolution |
| ------- | -------------------- | ------------- | ---------- |
| M-01    | OPEN/CLOSED          |               |            |
| M-02    | OPEN/CLOSED          |               |            |
| m-01    | OPEN/CLOSED/ACCEPTED |               |            |
| m-02    | OPEN/CLOSED/ACCEPTED |               |            |
| m-03    | OPEN/CLOSED/ACCEPTED |               |            |
| m-04    | OPEN/CLOSED          |               |            |

对于不采纳的 Minor finding，必须记录：

```
ACCEPTED — no change
```

并给出 rationale。

Major findings M-01 / M-02 不允许无理由 `ACCEPTED`。

------

# 20. Definition of Done

本轮 correction 完成条件：

-  M-01 已关闭；
-  M-02 已关闭；
-  Test Readiness Review 不再被直接等同/强关系建模为 V6 specialization；
-  Test Readiness Review 被明确为 test-specific aviation-profile review；
-  V6 仍保持 framework-defined composite gate；
-  Result / Evidence ontology 已降低到 source-supported strength；
-  Evidence identity、applicability、control、sufficiency 不再混为单一 predicate；
-  ARP research note 标题不存在明显 regulatory/normative ambiguity；
-  R*/R/A/N 保留 Objective × FDAL provenance；
-  `certification_credit_intent` 不被表示为 FDAL 自动推导属性；
-  internal review 保留原始 provenance；
-  external findings disposition 已记录；
-  ISO 24748-2 仍为 `Reviewed Supporting Source`；
-  ARP4754B 不被描述为 regulation；
-  Coverage/Sufficiency gaps 未被无依据关闭；
-  V10 仍为 `Change Impact & Re-verification`；
-  V10 stable ID 未变化；
-  Generic / Aviation Profile distinction 保持；
-  ARP4761A conclusions 未提前引入。

------

# 21. Expected Status After Correction

若所有 required findings 关闭，则：

```
ISO 24748-2 targeted review:
PASS


SAE ARP4754B clause-level research:
PASS WITH CORRECTIONS APPLIED


Standards map:
PASS


Normative gap matrix:
PASS


V0–V12 reassessment:
PASS


V10 rename:
PASS


Verification Strategy Record:
PASS / candidate fields retained


Research provenance:
PASS


Branch status:
READY FOR PR REVIEW
```

------

# 22. Research Baseline Consequence

本轮修正不应改变总体研究路线。

完成并通过 PR review 后，预期状态：

```
ISO/IEC/IEEE 15288:2023
→ Reviewed Baseline Candidate


ISO/IEC/IEEE 24748-1:2024
→ Reviewed Baseline Candidate


ISO/IEC/IEEE 24748-2:2024
→ Reviewed Supporting Source


SAE ARP4754B
→ Reviewed Aviation Baseline Candidate
```

下一项 major normative research source：

```
SAE ARP4761A
```

ARP4761A 应继续回答当前 ARP4754B 有意留下的 safety-assurance questions，包括：

- failure-condition classification；
- safety assessment process；
- FDAL / IDAL derivation and allocation；
- safety-derived requirements；
- architectural mitigation；
- common-cause concerns；
- safety evidence；
- safety → development assurance → verification rigor relationship。

不要在本轮 correction 中提前关闭这些问题。

------

# 23. Final Review Position

本轮研究总体是成功的。

需要修正的核心不是：

> 标准研究方向错误。

而是：

> **少数 Framework interpretation 已经比 source evidence 向前走了一步，需要降低 ontology / normative strength。**

尤其需要坚持：

```
Source says X
        ↓
Interpret X
        ↓
Framework implication
        ↓
Research proposal
```

不能变成：

```
Source mentions X
        ↓
Framework ontology immediately treats X as mandatory relation
```

当前最重要的两个修正正是这一原则的体现：

```
Test Readiness Review
≠ V6 itself
≠ necessarily specializationOf(V6)


Verification Result
≠ automatically sufficient Evidence for a Claim
```

更准确的关系是：

```
Test Readiness Review
→ may contribute to V6


Verification Result
→ may constitute/support Evidence
→ whose applicability, credibility and sufficiency
   are separately assessed
```

完成上述 targeted corrections 后，本分支可以进入正式 PR review，无需重新执行 ISO 24748-2 或 SAE ARP4754B 全量研究。

---

# 24. Finding Disposition — 2026-08-16

本节记录对上述外部非正式评审的复审和修改结果。原始 finding、条件性评审结论及论证正文均保留为 research provenance；frontmatter 已更新为最终处置状态。

| Finding | Status | Files changed | Resolution |
|---|---|---|---|
| M-01 | CLOSED | `standard_notes/sae_arp4754b.md`; `docs/03_dbse_workflow/README.md` | Test Readiness Review 明确为 testing/demonstration-specific aviation review，只能作为 V6 的候选输入/组成活动（`contributesTo(V6)`）；不等价于 V6，不使用 `specializationOf(V6)`，也不推出其他方法的正式 review 义务 |
| M-02 | CLOSED | `standard_notes/sae_arp4754b.md`; `standards_map.md`; `terminology.md`; `docs/03_dbse_workflow/README.md`; `docs/04_information_model/README.md` | Result/Data 可构成或支持 Evidence；Evidence identity、provenance、applicability、credibility/control 和 sufficiency 分开，且不归因于 ARP4754B 的 generic conversion rule |
| m-01 | CLOSED | `standard_notes/sae_arp4754b.md` | 标题改为 `SAE ARP4754B Standards Research Note`；正文继续声明 recommended-practice / certification-context boundary |
| m-02 | CLOSED | `standard_notes/sae_arp4754b.md`; `templates/verification_strategy_record.md`; `normative_gap_matrix.md`; `terminology.md` | R*/R/A/N 记录必须包含 source standard、Appendix A location、objective reference 和 FDAL；不作为 generic enum |
| m-03 | CLOSED | `templates/verification_strategy_record.md`; `standard_notes/sae_arp4754b.md`; `normative_gap_matrix.md`; `terminology.md` | `certification_credit_intent` 已移出 `assurance_applicability`，并明确为不由 FDAL 自动推导的 project/certification-use relation |
| m-04 | CLOSED | `reviews/iso_24748_2_arp4754b_internal_review.md`; 本记录 | 保留原始 internal-review result，并追加 external follow-up 与完整 disposition |

## 24.1 Final status

| Review target | Final result |
|---|---|
| ISO 24748-2 targeted review | PASS — Reviewed Supporting Source unchanged |
| SAE ARP4754B clause-level research | PASS WITH TARGETED CORRECTIONS APPLIED |
| Standards map / gap matrix | PASS |
| V0–V12 reassessment | PASS; mixed ontology and composite-gate boundaries retained |
| V10 rename | PASS; `Change Impact & Re-verification`, stable ID retained |
| Verification Strategy Record | PASS as research-draft / aviation-profile candidate schema |
| Research provenance | PASS |
| Branch status | **READY FOR PR REVIEW** |

**Blocking findings remaining:** 0

**Required changes remaining:** 0
