---
title: ISO/IEC/IEEE 24748-1:2024 Historical Source-Baseline Correction Task
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

> **Archive control:** This completed clean-source correction task is retained as research provenance. Its original body and numbering are preserved; the controlled baseline records the current source status.

# ISO/IEC/IEEE 24748-1:2024 Source Baseline Replacement — Correction Task

## 1. Task Purpose

当前 `ISO/IEC/IEEE 24748-1:2024` 研究最初基于一个 **Redline 版本 PDF** 展开。

现已将研究源文件替换为正式 clean edition：

```text
ISO/IEC/IEEE 24748-1:2024
Systems and software engineering —
Life cycle management —
Part 1: Guidelines for life cycle management
Second edition
2024-03
```

正式版首页已确认版本信息。

本任务的目标是：

> **将所有 ISO 24748-1 研究资产的 source provenance、locator、措辞和 review conclusion 统一迁移到正式 clean edition，并移除所有仅因 Redline 文本混排而产生的解释性说明。**

本任务不是重新研究 ISO 24748-1，也不是推翻当前研究结论。

当前核心研究结论原则上保留。

---

# 2. Source of Truth

从本任务开始，以下正式 clean edition 是唯一 normative research source：

```text
ISO/IEC/IEEE 24748-1:2024(en)
Second edition
2024-03
```

之前的 Redline 版本：

```text
status: historical research aid only
```

不得再作为：

- authoritative locator source；
- final clause-title source；
- normative wording source；
- PR review source；
- standards-map evidence source。

如果仓库中存在 Redline source metadata、说明或 citation，应清理或降级为 historical note。

---

# 3. Key Principle

本次变更遵循：

```text
Research conclusion
      ≠
Source provenance
```

即：

- 如果正式版支持现有结论，则保留结论；
- 只修正 source、locator、title、classification 和说明；
- 只有正式版与现有结论真正冲突时，才修改研究结论。

当前已检查的核心结论没有发现需要推翻的情况。

---

# 4. Required Files to Review

至少检查并修正：

```text
docs/01_normative_foundation/standard_notes/iso_24748_1.md
docs/01_normative_foundation/standards_map.md
docs/01_normative_foundation/normative_gap_matrix.md
docs/01_normative_foundation/reviews/iso_24748_1_informal_review.md
docs/03_dbse_workflow/README.md
templates/lifecycle_process_instantiation_record.md
docs/00_overview/terminology.md
docs/00_overview/roadmap.md
docs/01_normative_foundation/standards_baseline.md
references/*
CHANGELOG.md
```

不要求机械修改所有文件。

只修改：

> source replacement 实际影响的内容。

---

# 5. Remove Redline-Specific Source Description

`iso_24748_1.md` 中如存在以下类型内容：

```text
Current PDF is a Redline edition.
```

```text
red text / deleted text was used to interpret the current wording.
```

```text
the parser mixes old and new wording.
```

应删除。

正式研究笔记应改为：

```text
Source class:
licensed-local-source-not-committed

Source edition:
ISO/IEC/IEEE 24748-1:2024
Second edition
2024-03
Clean official edition
```

不要在最终研究笔记中保留 Redline 解析问题作为当前 source limitation。

---

# 6. Correct Annex F.3.6 Treatment

这是 source replacement 中最重要的一项。

正式版 Annex F.3.6 明确标题为：

```text
F.3.6 Verification reviews
```



因此，所有以下旧表述必须删除：

```text
Verification Test readiness reviews
```

```text
Redline parser shows Verification Test readiness reviews
```

```text
current text inferred from deleted/added Redline content
```

---

## 6.1 Required Final Interpretation

正式研究结论应写成：

> ISO/IEC/IEEE 24748-1:2024 Annex F.3.6 defines candidate `Verification reviews`. These reviews consider verification status, including the test environment, test cases and procedures, and the status of the system or element being tested. The clause does not define a mandatory `Verification Readiness Review (VRR)`.

正式文本明确列出：

- test environment；
- test cases；
- test procedures；
- system / element status；

并说明 verification 可使用 testing、analysis、demonstration 和 inspection。

---

## 6.2 Framework Consequence

保留当前结论：

```text
V6 Verification Readiness
≠ ISO-mandated VRR
```

V6 仍应定位为：

```text
framework-defined composite gate
```

由：

```text
readiness assessment
+ optional review
+ authorization decision
```

组成。

---

# 7. Update Informal Review Note

当前：

```text
docs/01_normative_foundation/reviews/
iso_24748_1_informal_review.md
```

中如果存在：

> “由于 Redline 解析混合了 Verification / Test readiness，因此通过图像检查确认……”

这部分应删除。

建议替换成：

```markdown
## ISO 24748-1 does not mandate a fixed VRR

The clean ISO/IEC/IEEE 24748-1:2024 edition explicitly titles Annex F.3.6 as `Verification reviews`.

The review addresses open issues associated with verification status, including the test environment, test cases and procedures, and the system or element being tested.

Because Annex F is informative and provides candidate joint stakeholder reviews, this does not establish a mandatory `Verification Readiness Review (VRR)`.

Therefore, V6 remains a framework-defined composite gate rather than an ISO-defined review process.
```

---

# 8. Confirm Annex F Status

正式目录明确：

```text
Annex F (informative)
Candidate joint stakeholder reviews
```



因此所有 Annex F 映射必须继续标：

```text
INFORMATIVE ANNEX
```

不能因 clean edition 更换而升级成：

```text
Direct normative requirement
```

---

# 9. Confirm Annex D Status

正式目录同样明确：

```text
Annex D (informative)
Process views
```



因此以下结论保持不变：

```text
Verification Assurance Process View
= framework architecture supported by informative ISO guidance
```

而不是：

```text
ISO-mandated process
```

---

# 10. Reconfirm Process View Wording

对 Annex D 的所有 locator 做一次 clean-edition consistency check。

保留核心边界：

```text
Process View
has:
- name
- purpose
- outcomes
- source process/activity/task references

Process View
does not create new source-standard activities/tasks
```

如果任何现有文档是从 Redline 文本中引用条款标题或编号，改为 clean edition locator。

不需要重新解释 framework architecture。

---

# 11. Correct Source Metadata

在 `iso_24748_1.md` front matter 或 metadata 中，明确：

```yaml
source:
  standard: ISO/IEC/IEEE 24748-1:2024
  edition: second
  date: 2024-03
  source_type: licensed-local-source-not-committed
  source_form: clean-official-edition
```

不要提交 PDF。

不要记录本地绝对路径：

```text
E:\...
```

到 public repository。

---

# 12. Clause 1 and Introduction Should Carry the Guidance-Role Argument

当前研究中关于：

> ISO 24748-1 是 lifecycle-management guidance，而不是替代 ISO 15288 process conformance baseline

的判断应继续保留。

但其依据应明确来自：

- document title；
- Introduction；
- Clause 1 Scope。

Introduction 明确说明本文件用于促进 ISO 15288/12207 process content 的使用，并提供统一 lifecycle-management guidance。

Clause 1 则明确说明：

> 本文件提供 systems/software life-cycle management guidance，并补充 ISO 15288/12207 processes。

---

# 13. Clause 2 Interpretation Correction

正式版 Clause 2 明确：

```text
There are no normative references in this document.
```



这句话可以保留。

但不要再写成：

```text
Because Clause 2 has no normative references,
the document is not a conformance framework.
```

这种因果推理过强。

正确处理：

```markdown
Clause 2 contains no normative references.

The document's guidance role and its relationship to ISO/IEC/IEEE 15288 are established primarily by its title, Introduction and Scope.
```

---

# 14. Reconfirm Clause 6.4 Evaluation Taxonomy

正式 clean edition Clause 6.4 直接可读，确认 lifecycle evaluation 分为多个类别，其中包括：

- process-internal evaluations；
- verification and validation；
- joint reviews and audits；
- quality assurance；
- process improvement。



因此以下结论保留：

```text
Verification / Validation
≠ Joint Review / Audit
```

以及：

```text
Lifecycle review
≠ Verification Method inspection
```

这进一步支持：

```text
LC-G02 Review taxonomy
```

不需要修改该 gap 的核心结论。

---

# 15. Standards Map Correction

检查：

```text
docs/01_normative_foundation/standards_map.md
```

ISO 24748 列中所有 locator 是否来自 clean edition。

特别检查：

```text
Annex F.3.6
```

应统一为：

```text
Verification reviews
```

禁止出现：

```text
Test readiness review
```

或者：

```text
Verification Test readiness review
```

---

# 16. Normative Gap Matrix Correction

当前以下 gap 可保留：

```text
LC-G01 Gate semantics
LC-G02 Review taxonomy
LC-G03 Process-view provenance
LC-G04 Lifecycle/process instantiation evidence
```

不需要因 source replacement 删除。

但是检查 `LC-G02` 的文字。

建议最终写：

> ISO/IEC/IEEE 24748-1:2024 Annex F provides candidate joint stakeholder reviews. F.3.6 defines `Verification reviews`, not a mandatory `Verification Readiness Review`.

---

# 17. DBSE Workflow Check

检查：

```text
docs/03_dbse_workflow/README.md
```

保留：

```text
V0–V12
= Verification Assurance Process View /
cross-process orchestration architecture
```

并保留：

```text
V6 / V12 = Composite gate
```

确认没有引用 Redline-specific interpretation。

推荐最终 V6 表述：

```text
V6 Verification Readiness:
framework-defined composite gate supported by
criteria-driven lifecycle evaluation,
optional verification/lifecycle review,
and authorization decision.
```

推荐 V12：

```text
V12 Verification Closure:
framework-defined composite gate integrating
assurance assessment,
approval decision,
traceability/baseline completion,
and applicable lifecycle gate semantics.
```

---

# 18. Lifecycle / Process Instantiation Record Check

当前模板：

```text
lifecycle_process_instantiation_record.md
```

可保留。

正式版仍支持：

- lifecycle model；
- stages；
- entry/exit criteria；
- process selection；
- mappings；
- rationale；
- decision gates。

因此无需删除该模板。

只需确认其 normative-basis 描述继续是：

```text
ISO/IEC/IEEE 24748-1:2024 guidance;
schema is a research proposal
```

不要因 clean edition 替换将 template 升级成：

```text
ISO-required information item
```

---

# 19. Source Provenance Cleanup

仓库中如存在类似：

```text
source: redline
```

```text
source_type: redline-edition
```

```text
verified using redline page
```

全部改为：

```text
source_form: clean-official-edition
```

Redline 版本如需要保留历史记录，只允许出现在：

```text
archive/
```

或 review provenance 说明中，并标：

```text
historical research aid
not authoritative
```

但不建议 public repository 存储受版权保护 PDF 本身。

---

# 20. Locator Consistency Pass

对整个 ISO 24748-1 slice 做一次 locator-only review。

重点检查：

```text
Clause 1
Clause 2
3.24 / 3.25 / 3.48
4.3
Clause 5
6.2.2–6.2.8
6.3
6.4
Clause 7
Annex A
Annex C
Annex D
Annex E
Annex F
Annex G
```

目的：

> 确保 locator 全部基于 clean 2024 edition，而不是旧版或 Redline merge-text。

不要借机重新写整份研究报告。

---

# 21. Version-Difference Commentary

除非研究主题本身需要比较：

```text
2018 vs 2024
```

否则删除所有：

```text
old text
new text
deleted wording
added wording
```

这类内容。

当前研究任务是：

```text
ISO/IEC/IEEE 24748-1:2024
```

不是 version-delta analysis。

---

# 22. Preserve Existing Core Conclusions

Source replacement 后，以下结论原则上继续保留：

```text
Stage ≠ Process
Process ≠ Process View
V-ID ≠ execution sequence
Review ≠ Gate
Criteria satisfaction ≠ authorization decision
Lifecycle review ≠ Verification Method
```

以及：

```text
V0–V12
→ Verification Assurance Process View

V6 / V12
→ framework-defined composite gates
```

当前正式版没有证据要求推翻这些结论。

---

# 23. Preserve 24748-2 Priority

正式版 Introduction 明确说明：

```text
ISO/IEC/IEEE 24748-2
```

用于支持 ISO 15288 的单独应用。

因此：

```text
ISO/IEC/IEEE 24748-2:2024
Priority: High / Next
```

继续保留。

---

# 24. Update Review Status

完成本任务后，建议：

```text
ISO/IEC/IEEE 24748-1:2024
Research status: reviewed
Baseline readiness: candidate
Source baseline: clean official edition
```

不需要因为 source replacement 将其重新降为：

```text
Unreviewed
```

前提是完成 locator consistency pass。

---

# 25. Required Changelog Entry

建议在 Changelog 增加类似：

```markdown
### Changed

- Replaced ISO/IEC/IEEE 24748-1:2024 research source baseline from a Redline edition to the official clean 2024 edition.
- Revalidated Annex F.3.6 as `Verification reviews`.
- Removed Redline-specific interpretation and updated source provenance and locators.
- No core Verification Assurance architecture conclusions were changed.
```

不要写：

```text
updated the standard version
```

因为标准版本没有变，仍然是：

```text
ISO/IEC/IEEE 24748-1:2024
```

变化的是：

```text
source representation / source baseline
```

而不是 standard revision。

---

# 26. Required Acceptance Checks

修正完成后检查：

### AC-01

没有 active research document 再把 Redline 版作为 authoritative source。

### AC-02

F.3.6 全部统一为：

```text
Verification reviews
```

### AC-03

没有 `Test readiness reviews` 残留作为 2024 正式标题。

### AC-04

没有通过 Clause 2 无 normative references 单独推导整体 guidance status。

### AC-05

所有 guidance-role 论证以 Title / Introduction / Scope 为主要依据。

### AC-06

Annex D / F / G 均继续标记 informative。

### AC-07

standards_map locators 已与 clean edition 对齐。

### AC-08

normative_gap_matrix 核心 gap 仍有 source support。

### AC-09

V0–V12 ontology 没有因 source replacement 无理由回退。

### AC-10

24748-2 仍保持 `High / Next`。

---

# 27. Final Expected State

完成后：

```text
ISO/IEC/IEEE 24748-1:2024
│
├─ Authoritative research source:
│    clean official 2024 edition
│
├─ Research note:
│    reviewed
│
├─ Standards map:
│    clean-edition locators
│
├─ Gap matrix:
│    retained and source-corrected
│
├─ DBSE architecture:
│    unchanged in principle
│
└─ Redline:
     historical aid only
```

---

# 28. Core Correction Principle

本次任务的核心不是：

> “重新做 ISO 24748-1 研究。”

而是：

> **把已经形成的研究成果从一个可能产生新旧正文混排歧义的 Redline source，迁移到正式 clean edition，并确保所有 provenance、locator 和 normative wording 都与新的 authoritative source 一致。**

如果 clean edition 与现有结论一致：

```text
preserve conclusion
```

如果 locator 不一致：

```text
correct locator
```

如果旧结论只来自 Redline 差异推断：

```text
revalidate against clean text
```

如果 clean text 不支持：

```text
revise or remove conclusion
```

不得为了维持旧结论而继续引用 Redline。
