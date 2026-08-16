---
title: ISO/IEC/IEEE 24748-2:2024 Targeted Applicability Review
status: reviewed
version: 0.1
baseline: supporting-source
owner: research
last_updated: 2026-08-16
research_type: targeted-applicability-review
source_role: supporting-guidance
baseline_status: supporting-source
source:
  standard: ISO/IEC/IEEE 24748-2:2024
  edition: second
  date: 2024-03
  source_type: licensed-local-source-not-committed
  source_form: clean-official-edition
---

# ISO/IEC/IEEE 24748-2:2024 Targeted Applicability Review

## 1. 评审目的与边界

本评审只判断 *Guidelines for the application of ISO/IEC/IEEE 15288 (System life cycle processes)* 是否改变现有 Verification Assurance Framework 基线。原文件仅用于本地研究，不纳入版本库；本文仅保存条款定位和自行撰写的总结。

Clause 6.1 明确说明本文件帮助理解和应用 ISO/IEC/IEEE 15288 的规定，不引入新的要求。因此，本评审把正文内容分类为 `APPLICATION GUIDANCE`，把 Annex C 分类为 `INFORMATIVE GUIDANCE`；框架中的记录、gate 和本体仍分别标为 `FRAMEWORK IMPLICATION` 或 `RESEARCH PROPOSAL`。

## 2. 结论

| Decision | Result | Basis |
|---|---|---|
| Framework delta | **Minor** | 细化应用语境、计划、enabling systems、配置审计、重复调用和 gate cadence；不改变 ISO 15288 的 Verification purpose/tasks |
| Full standalone research note required | **No** | 未发现足以建立第二套 normative process baseline 的差异 |
| Source role | **Reviewed supporting application guidance** | Clause 6.1；全篇 application guidance 定位 |
| V0–V12 ontology changed | **No** | 继续采用 mixed-ontology Verification Assurance Process View |
| V6/V12 become ISO-defined gates | **No** | guidance 支持 criteria、review、decision 和 artefact 关系，不定义这两个框架 gate |

## 3. 定向条款审阅

| Locator | Application guidance summary | Framework consequence |
|---|---|---|
| Clause 1 | 指导 ISO 15288 的系统工程应用，面向 system-of-interest 及其生命周期 | 不替代 ISO 15288 conformance baseline |
| 5 | 系统工程过程按项目和生命周期语境应用，强调跨层级、迭代和相互作用 | 保持 V-ID 为稳定标识，不解释为顺序 |
| 6.1 | 不引入新的要求 | 所有新增字段和 gate 语义仍须标为框架提案 |
| 6.2 | 过程应用需要结合系统、项目、组织及 agreement context | V0 应记录适用语境、边界、假设和接口 |
| 6.4; 6.4.2 | stages 不规定固定先后；entry/exit decisions、milestones、gates 和迭代 cadence 用于治理 | 进一步支持把 assessment、review、decision 和 baseline event 分开建模 |
| 6.6 | enabling systems 可在项目边界内外，但属于项目 span of interest；有自己的要求、配置、可用性、进度和生命周期依赖 | Verification Environment 应链接可识别的 enabling-system configuration 与 readiness evidence |
| 6.7.4.1 | Project Planning 整合各过程策略，并覆盖实施、集成、verification、transition、validation 的范围、任务、方法、工具、度量、风险和资源 | V0 是 Development/Project Planning 中的 verification-specific planning concern，不是独立 lifecycle stage |
| 6.7.5.4.3 | Integration 与接口、组合状态及后续 verification 相连 | 保留 integration state → verification configuration 的显式关系 |
| 6.7.5.4.4 | Verification 可按策略在生命周期多次应用；取决于系统类型、阶段和 entry/exit decisions；方法示例仍为 inspection、analysis、demonstration、test | 澄清而不扩张 ISO 15288 方法 taxonomy；支持 re-entry/re-verification |
| 6.7.5.4.6 | Validation 继续保持 intended-use/stakeholder context，与 verification 不合并 | 不采用 ARP4754B 的语境定义覆盖 ISO 通用定义 |
| 6.7.5.4.7 | Transition 与目标环境/运行能力准备有关 | 可作为 lifecycle gate 输入，不等于 Verification Closure |
| 6.8 | conformance/adaptation 允许基于语境选择、替代和裁剪过程，并记录理由；其他标准及 enabling-system 可用性可成为裁剪输入 | 强化 lifecycle/process instantiation record 的 rationale，但不规定通用字段 schema |
| Annex C | 模型应围绕 intended use/questions 选择、互联并保持一致 | 只对模型可信性和信息一致性提供资料性支持；不建立 MBSE evidence admissibility rule |

## 4. 六项研究问题

| ID | Answer | Classification | Locator |
|---|---|---|---|
| Q24748-2-01 | 不改变 ISO 15288 Verification 的目的、输入/输出或 task；它解释了多次应用、语境和方法选择。 | APPLICATION GUIDANCE | 6.1; 6.7.5.4.4 |
| Q24748-2-02 | 不改变 Verification Assurance Process View 或 V0–V12 mixed ontology；反而强化过程可迭代、按 gate cadence 调用。 | FRAMEWORK IMPLICATION | 5; 6.4 |
| Q24748-2-03 | 不把 V6/V12 定义为 ISO gate；只增强 criteria、artefact、review、decision 和治理 cadence 的关系。 | APPLICATION GUIDANCE / BOUNDARY | 6.4; 6.4.2 |
| Q24748-2-04 | 强化对 process selection、tailoring rationale、stage/process relationship 和 project-plan integration 的记录需要，但不规定本仓库字段。 | APPLICATION GUIDANCE / RESEARCH PROPOSAL | 6.4; 6.7.4.1; 6.8 |
| Q24748-2-05 | 新增的是 application semantics：策略整合、enabling-system 生命周期、配置审计、集成状态和重复 verification；未新增通用 evidence 或 sufficiency ontology。 | APPLICATION GUIDANCE | 6.6; 6.7.4; 6.7.5 |
| Q24748-2-06 | 对 gate、迭代、enabler、configuration 和 tailoring 缺口作出澄清；未关闭 independence、coverage、sufficiency、oracle、closure authority 或 schema 缺口。 | GAP ASSESSMENT | 6.1–6.8; Annex C |

## 5. 既有缺口影响

| Gap | Effect | Reason |
|---|---|---|
| ISO-G01 independence | UNCHANGED | 无通用 Verification independence rule |
| ISO-G02 coverage | UNCHANGED | 无通用 coverage taxonomy/metric |
| ISO-G03 sufficiency | UNCHANGED | 无 sufficiency decision model |
| ISO-G04 oracle | UNCHANGED | 无独立 Oracle entity |
| ISO-G05 regression | CLARIFIED | 明确 verification 可按阶段、决定和策略多次调用，但无通用选择算法 |
| ISO-G06 closure | CLARIFIED | gates 和 artefacts 支持组合 closure，但无 V12 或 waiver/reopen 规则 |
| ISO-G07 schema | CLARIFIED | 支持记录和规划，不规定仓库 schema |
| ISO-G08 MBSE evidence | CLARIFIED | Annex C 提供模型使用指导，不规定证据可接受性 |
| LC-G01 gate semantics | CLARIFIED | 治理 cadence 和 artefact/decision 关系更清楚 |
| LC-G02 review taxonomy | UNCHANGED | 未建立强制 Verification Readiness Review |
| LC-G03 process-view provenance | UNCHANGED | 不改变现有 provenance rule |
| LC-G04 instantiation evidence | CLARIFIED | application/tailoring rationale 更明确，字段仍为提案 |

## 6. Baseline decision

ISO/IEC/IEEE 24748-2:2024 被纳入 **Reviewed Supporting Source**。现有 ISO 15288 + ISO 24748-1 通用 lifecycle/process 骨架保持不变；本轮只把 strategy integration、enabling-system configuration、iteration/re-entry 和 gate cadence 加入后续信息模型约束。
