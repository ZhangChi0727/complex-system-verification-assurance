---
title: SAE ARP4754B Standards Research Note
status: reviewed
version: 0.2
baseline: candidate
owner: research
last_updated: 2026-08-16
source:
  standard: SAE ARP4754B
  revision: B
  date: 2023-12
  source_type: licensed-local-source-not-committed
  source_form: official-publication
---

# SAE ARP4754B Research Note

## 1. 研究边界与来源分类

本笔记研究 SAE ARP4754B *Guidelines for Development of Civil Aircraft and Systems*。原文件仅在本地研究环境使用，不纳入版本库；正文仅保存合法 locator 和自行撰写的总结。

ARP4754B 是 Aerospace Recommended Practice，而不是法规。1.1 明确其内容是推荐实践，不应被理解为 regulatory requirements，并允许在认证中采用经认可的替代方法。某一目标是否用于 compliance substantiation，取决于适用 certification basis、申请人与 Certification Authority 协调结果及接受的 means of compliance。因此本文使用：

- `ARP DEFINITION`、`ARP RECOMMENDATION`；
- `CERTIFICATION-RELATED OBJECTIVE`、`FDAL-DEPENDENT OBJECTIVE`、`APPENDIX OBJECTIVE`；
- `INTERPRETATION`、`FRAMEWORK IMPLICATION`、`AVIATION PROFILE RULE`；
- `GENERIC RESEARCH PROPOSAL`、`OPEN QUESTION`。

安全评估方法、failure analysis、FDAL/IDAL 详细分配、PSSA/SSA 和 CCA 的研究结论留给 ARP4761A；软件、电子硬件和 IMA item-level 结论分别留给 DO-178C、DO-254 和 DO-297。

## 2. 总体结论

1. ARP4754B 为 aircraft/system development assurance 提供航空专用的 objective–applicability–independence–output–control 结构；它不替代 ISO 15288 通用生命周期过程骨架。
2. 其术语边界清楚地区分 requirements validation（正确且完整）和 implementation verification（实现满足已验证要求）。这是航空语境 taxonomy，不覆盖 ISO 的通用定义。
3. Verification planning、method/procedure sufficiency、requirements-oriented coverage、test readiness、unintended behavior、configuration、Verification Data 和 problem disposition 形成一条可审计保证链。
4. Appendix A 使 FDAL 影响目标适用性、过程独立性和输出控制类别；这支持新增 `Assurance Applicability / Rigor` 维度，但不能推导通用独立性等级。
5. 6.3 和 6.4 强化 change impact、re-verification 与 prior-evidence credit。V10 应改名为 **Change Impact & Re-verification**，保留稳定 ID。
6. Certification approval 不是 Evidence。Verification Result 或 Verification Data 可构成或支持 Evidence；其对特定 claim 的 applicability、credibility、control 和 sufficiency 需要分别评价，再进入 compliance substantiation、certification coordination 和 authority decision。

## 3. Scope、定义与标准边界

### 3.1 Scope and development assurance

**ARP RECOMMENDATION — 1; 1.1; 1.2; 1.4**

- 面向 aircraft/system development，考虑 aircraft functions 和 operating environment，并覆盖 safety、certification 和 product assurance 所需的 requirements validation 与 implementation verification。
- Development Assurance 是以计划和系统化活动建立信心的过程：通过与 failure-condition severity 相称的 rigor，降低影响安全的 development error 可能性。
- Revision B 与 ARP4761A 对齐；FDAL/IDAL 细节和 safety-assessment 内容移交 ARP4761A，并澄清 unintended behavior、derived requirements、modification 和 reuse。

**BOUNDARY:** ARP4754B 不详细规定 software、electronic hardware、IMA 或 safety-assessment processes；不得从本轮研究预判这些标准的 item-level objectives。

### 3.2 Selected definitions

| Concept | Research summary | Classification | Locator |
|---|---|---|---|
| Requirement | function specification 中可被 validation、并可作为 implementation verification 基准的可识别元素 | ARP DEFINITION | 2.2 |
| Validation | 判断产品 requirements 是否正确且完整 | ARP DEFINITION | 2.2 |
| Verification | 评价 requirements 的 implementation 是否满足这些 requirements | ARP DEFINITION | 2.2 |
| Development Assurance | 为证明 development errors 已识别并纠正、系统满足适用 safety objectives 而采取的计划且系统化活动 | ARP DEFINITION | 2.2 |
| FDAL | 对 functions 执行 development-assurance tasks 的 rigor，决定适用的 ARP4754B objectives | ARP DEFINITION | 2.2 |
| IDAL | 对 items 执行 development-assurance tasks 的 rigor；连接 DO-178C software level 或 DO-254 design assurance level | ARP DEFINITION | 2.2 |
| Process independence | 通过职责分离，使活动由执行者之外的人客观评价 | ARP RECOMMENDATION | 5.2.3.2.1.4 |
| Certification | 产品符合适用法规的法律认可 | ARP DEFINITION | 2.2 |

**TERMINOLOGY DECISION:** Repository 保留 ISO generic `Verification` / `Validation`；ARP 定义登记为 aviation-profile contextual taxonomy。`Process Assurance independence`、`Verification/Validation objective independence` 与 architecture independence 也必须分别建模。

## 4. Development Assurance Planning

**ARP RECOMMENDATION — Section 3; 3.1; 3.2**

规划定义满足 aircraft/system requirements 并与 certification basis 相称的开发方式，覆盖：

- lifecycle process activities、FDAL/IDAL；
- process interrelationships、sequence、feedback 和 transition criteria；
- development environment、methods、tools 和 standards；
- validation、implementation verification、configuration management 与 process assurance plans；
- roles、supplier relationships、safety-process interactions、certification data 及需保持配置控制的数据。

**ARP RECOMMENDATION — 3.2.2:** transition criteria 是与 development phases/gates 对齐的 checkpoints/reviews，包含 technical/process entrance and exit criteria；open issues 应被跟踪管理。

**FRAMEWORK IMPLICATION:** V0 在 aviation profile 中属于 Development Assurance Planning 的 verification-specific slice。transition criteria 为 V6/V12 提供航空专用 gate semantics，但不等同于框架 gate。

**CERTIFICATION-RELATED OBJECTIVE — 3.3:** certification coordination 应覆盖 certification basis、means of showing compliance、data submission/retention 和持续协调。Authority agreement/approval 是决策关系，不是 evidence object。

## 5. Aircraft–System–Item architecture and information flow

**ARP RECOMMENDATION — Section 4; 4.6; 4.6.1**

开发信息沿 `aircraft functions/requirements → system functions/requirements/architecture → item requirements` 分解和分配，并以 item outputs、integration results、verification data 和 safety information 反向支撑 system/aircraft conclusions。

System-to-item data 至少涉及 allocated requirements、item DAL/failure-condition context、architectural constraints、separation/independence、在 item level 执行的 system verification activities 以及 system 接受这些 evidence 的条件。

**FRAMEWORK IMPLICATION:** `requirement_allocation_level` 与 `verification_execution_level` 必须分开；若 verification 被下放或取得跨层级 credit，应记录 allocation/delegation、acceptance criteria、evidence provenance、verified configuration 和接受方。

## 6. Safety relationship and rigor boundary

**ARP RECOMMENDATION — 5.1; 5.2**

- Safety assessment 与 development assurance 在生命周期中迭代交互；safety requirements、assumptions 和 outputs 进入 requirements、architecture、validation 和 verification。
- Function development phase 的 requirements 需要 correctness/completeness validation；FDAL 决定 Appendix A 中 function-level objectives 的适用性和 rigor。
- Item development phase 的 IDAL 连接软件/硬件标准。ARP4754B 保留一般原则，但详细 assignment/process 在 ARP4761A。
- Process independence 在 DAL 分配之后用于降低 development-error 可能性；不能把 architecture、physical、functional、item-development 与 process independence 混成一个字段。

**AVIATION PROFILE RULE:** Assurance rigor 不是单一 `DAL` 字符串。Appendix A applicability 记录应保留 `source_standard + source_location + objective_reference + FDAL + objective_applicability` provenance，并把 `process_independence_required` 与 `system_control_category` 作为相关但不同的属性。`certification_credit_intent` 是独立的 project/certification-use relation，不由 FDAL 自动推导。详细 FDAL/IDAL assignment 由 ARP4761A Appendix P 的独立研究切片补充，并继续保留跨标准 provenance。

## 7. Requirements capture and validation

### 7.1 Requirements capture

**ARP RECOMMENDATION — 5.3; 5.3.2; 5.3.3**

- requirements 来源包括 functions、architecture/interfaces、safety assessment、operational/environmental constraints、derived requirements 和 assumptions；
- safety requirements 及其来源、assumptions 和验证证据需要保持可追溯；
- derived requirements 要被识别，并向上评价 functional/safety impact。

### 7.2 Validation

**ARP RECOMMENDATION — 5.4; 5.4.7**

Validation 确认 requirements 对 stakeholder/aircraft/system needs 是正确且完整的。正确性检查包括一致、无歧义、可行、带适当 tolerance、可验证、来源和 rationale；完整性可结合 requirement classes、templates/checklists、用户/运营/维护人员、authority 和接口双方参与。

Validation methods 与 implementation verification methods 具有不同目的；计划应说明 methods、roles、independence、criteria、assumptions、tracking 和 data。Validation Matrix 可链接 requirement、source/function、FDAL、method、evidence 和 conclusion；Validation Summary 汇总结果、限制和问题。

**BOUNDARY:** requirements review、analysis、modeling、prototype/simulation 等 validation 手段不自动成为 implementation verification method。

## 8. Implementation Verification

### 8.1 Purpose and planning

**ARP RECOMMENDATION — 5.5; 5.5.4**

目的为证明 aircraft/system implementation 满足已规定且已 validation 的 requirements。计划应记录 roles、所需 independence、受控 configuration、设施/设备、每项 requirement 的 method、DAL context、success criteria、procedure sufficiency、跨层级 credit、活动 sequence、data 和 environment。

### 8.2 Method taxonomy

**ARP RECOMMENDATION — 5.5.5**

| ARP method family | ISO 15288 comparison | Boundary |
|---|---|---|
| Inspection / Review | 对应 ISO Inspection 的一部分 | lifecycle review/gate 不因此成为 verification method |
| Analysis | 与 ISO Analysis 高度相容 | model/analysis 的有效性取决于目的、输入和可信性 |
| Testing or Demonstration | ARP 合并为一组讨论，ISO 列为两个示例 | taxonomy 结构是 contextual，不做强制一一映射 |
| Similarity / Service Experience | ISO 可容纳于 analysis/analogy 语境，但 ARP 明确讨论 credit | 必须评价适用性、差异、服务问题和补充活动 |

**ARP RECOMMENDATION — 5.5.5.2.2:** Coverage Analysis 判断 requirements 在 development 和 verification activities 中被处理的程度，通常依靠 traceability。它是 requirements-oriented coverage，不提供跨领域 coverage taxonomy 或充分性公式。

**ARP RECOMMENDATION — 5.5.5.3:** Testing/Demonstration 使用 requirements 建立客观 pass/fail criteria；test readiness review 评价 procedures 对 system/item requirements 的适用性。测试既检查 intended functions，也应提供信心以发现影响安全的 unintended behavior。测试配置、输入、期望结果、容差、工具/设施、实际结果、差异和 deficiency 应可复核。

**FRAMEWORK IMPLICATION:** ARP4754B Test Readiness Review 是 aviation profile 中面向 testing/demonstration 的特定 readiness review，可作为 framework-defined V6 Verification Readiness composite gate 的候选输入或组成活动（`contributesTo(V6)`）。它不是 V6 本身，V6 的范围还包括其他方法、basis、procedure、environment、configuration、evidence infrastructure、assessment 和 authorization readiness；该条款也不足以证明其他 verification methods 必须具有对应的正式 readiness review。

### 8.3 Verification Data and evidence chain

**CERTIFICATION-RELATED OBJECTIVE — 5.5.6**

Verification Data 用于提供 verification process 已执行的 evidence，并可按与 Certification Authority 的约定用于 compliance substantiation。典型受控输出包括 Verification Plan、Procedures、Results/Matrix、Summary 和 Problem Reports；system data 应汇总嵌入的软件/硬件 verification 状态，但不得替代其适用 item-level standard。

Verification Result 和 Evidence 是不同的 assurance roles / ontology concepts。Result 可以构成或支持 Evidence；其对特定 compliance/assurance claim 的 credibility、applicability 和 substantiation value，取决于 provenance、method/procedure、verified object/configuration/environment、data control 和 claim traceability。Evidence identity、applicability、control 与 sufficiency 是不同的 predicates；ARP4754B 不建立通用的 Result→Evidence 二值转换判据。Appendix A Objective 5.1 直接关联 method/procedure sufficiency 与 Verification Procedures，并按 FDAL 调整适用性和 independence。

## 9. Configuration Management and Process Assurance

### 9.1 Configuration Management

**CERTIFICATION-RELATED OBJECTIVE — 5.6**

用于认证的数据和记录应可检索，来源与生成方法受控到足以重现相同或相似数据。Requirements validation 或 implementation verification 开始时应建立适用 configuration baseline，并保留 baseline 之间的 change history。配置项覆盖 aircraft/system/item、plans、requirements、validation/verification data、工具/设施及其他关键数据。

**FDAL-DEPENDENT OBJECTIVE — 5.6.4; Appendix A:** System Control Category SC1/SC2 按 FDAL 与输出分配不同控制强度。它是 evidence-control rigor，不是证据内容格式。

### 9.2 Process Assurance

**ARP RECOMMENDATION — 5.7:** Process Assurance 确保 plans 被建立和维护、activities/processes 按计划执行，并对 deviations、reviews 和 authority coordination 保留报告。它应与 development process 有一定独立性。

**BOUNDARY:** Process Assurance independence 不等同于 Appendix A 中具体 validation/verification objective 的 process independence，也不建立 generic independent verification rule。

## 10. Modification, re-verification and evidence reuse

**ARP RECOMMENDATION — 6.3:** modification impact analysis 应评价变更对原 development assurance activities 和 safety assessments 的影响，包括 failure-condition information、DAL、assumptions、validation/verification methods/procedures、environment qualification、operations、interfaces、data 和 architecture；再按 new/modified/affected/unmodified 分类选择活动。

**ARP RECOMMENDATION — 6.4:** 若对既有 certification baseline 的活动寻求 credit，新应用和 certification data 应追溯到该 baseline，并证明适用；不足部分需要补充。可结合差异/适用性分析、经验证假设的 reverse engineering 和 service history。

**FRAMEWORK IMPLICATION:** V10 更名为 `Change Impact & Re-verification`。核心关系为：

`change → affected claims/requirements/configurations → prior-evidence validity → selected re-verification → new/supplemented evidence → updated substantiation`

Evidence reuse 是带条件的 credit relation，不是复制旧结果，也不是“曾经认证即可复用”。

## 11. Appendix A objective model

**APPENDIX OBJECTIVE — Appendix A**

Table A1 把 process objective、FDAL applicability/independence、section、output 和 System Control Category 连接起来。每个标记都必须保留其 `source standard × source location × objective × FDAL × Appendix A cell` provenance，不能脱离该上下文作为 generic assurance-level enum。标记语义为：

| Mark | Research interpretation |
|---|---|
| `R*` | 推荐用于 certification，且带 process independence |
| `R` | 推荐用于 certification |
| `A` | 由 certification 协调商定 |
| `N` | certification 不要求 |

Implementation Verification objectives 5.1–5.5 分别覆盖：method/procedure sufficiency、intended/system requirements、safety requirements、substantiation data，以及 deficiencies 对 safety 的影响。Objective 5.1 在 FDAL A 为 `R*`、B/C 为 `R`、D 为 `A`、E 为 `N`，其输出为 Verification Procedures，并按 FDAL 分配 System Control Category。

**AVIATION PROFILE RULE:** objective applicability、independence 和 output control 是彼此相关但不同的属性。`R*` 不能简化成“所有 verification 必须独立”，`N` 只表达对应 Objective × FDAL cell 的 certification applicability classification，也不等于工程上无需验证。

## 12. ISO 15288 ↔ ARP4754B comparison

| Concern | ISO/IEC/IEEE 15288 | SAE ARP4754B | Framework decision |
|---|---|---|---|
| Role | 通用 system lifecycle process standard | civil-aircraft/system recommended practice | generic core + aviation profile |
| Verification | 对 specified requirements/characteristics 取得 objective evidence | implementation 满足 validated requirements | 保留 ISO generic 定义；登记 ARP context |
| Validation | intended use/stakeholder needs 的满足 | requirements correct and complete | 不强制跨标准同义 |
| Methods | Inspection, Analysis, Demonstration, Testing（资料性示例） | Inspection/Review, Analysis, Testing/Demonstration, Similarity/Service Experience | 建立可映射的 contextual taxonomy |
| Independence | Verification 无通用规则；QA independence | objective/FDAL-dependent process independence；另有 Process Assurance independence | 航空 profile 属性，不上升为 universal rule |
| Coverage | traceability；无通用 taxonomy | requirements-oriented coverage analysis | ISO-G02 仅部分、领域性支持 |
| Sufficiency | assurance argument 支持但无公式 | method/procedure sufficiency 为 Objective 5.1 | ISO-G03 得到航空专用部分支持，不关闭 |
| Gate/review | lifecycle guidance 来自 24748 系列 | transition criteria；test-specific Test Readiness Review | 后者可 contribute to V6，不等价于 V6，也不建立其他方法的正式 readiness review 义务 |
| Evidence | objective evidence + assurance case | controlled Verification Data 可用于 substantiation | 增加 applicability/control/credit 关系 |
| Change/reuse | CM 与 re-verification 间接/直接支撑 | 6.3 impact analysis；6.4 certification evidence reuse | 重构 V10，保留通用/航空边界 |

## 13. V0–V12 reassessment

| ID | Revised name / ontology | ARP4754B effect |
|---|---|---|
| V0 | Verification Planning — activity/planning | aviation profile 嵌入 Development Assurance Planning，并连接 certification basis、FDAL、plans 和 transition criteria |
| V1 | Verification Basis Establishment — activity/information baseline | 增加 validated requirements、safety/derived requirements、assumptions、architecture、DAL 和 certification basis |
| V2 | Requirement Verifiability Analysis — activity | ARP validation correctness checks明确包含 requirement 是否可由 5.5 验证；仍与 requirements validation 分开 |
| V3 | Verification Strategy Definition — activity | 增加 objective applicability、independence、cross-level credit、unintended behavior 和 data/control strategy |
| V4 | Verification Case Design — framework activity | 方法/criteria/coverage/conditions 获得支持，Case 对象仍为提案 |
| V5 | Verification Procedure Development — activity/information item | Appendix A Objective 5.1 直接强化 procedure sufficiency 和受控输出 |
| V6 | Verification Readiness — composite gate | transition criteria 和 test-specific aviation Test Readiness Review 可作为候选输入/组成活动；保持 review/assessment/decision/gate 分离，且不建立 `specializationOf(V6)` |
| V7 | Verification Execution — activity | 增加代表性设施、工具/校准、对象/环境版本和 unintended-behavior checks |
| V8 | Result Evaluation — evaluation/decision | 显式 pass/fail、expected/actual discrepancy、deficiency 和 safety impact |
| V9 | Anomaly Resolution — cross-process concern | 连接 Problem Reports、safety effect、mitigation、deferred closure justification 和 re-test |
| V10 | **Change Impact & Re-verification** — cross-process orchestration | 6.3/6.4 直接强化 impact、prior-evidence validity、credit 和补充活动；稳定 ID 不变 |
| V11 | Coverage & Sufficiency Assessment — assurance assessment | requirements coverage 与 Objective 5.1 提供航空专用输入；无通用充分性公式 |
| V12 | Verification Closure — composite gate | Verification Summary、OPR、configuration index、process assurance 与 certification coordination 为输入；authority approval 仍与 evidence 分离 |

## 14. Framework questions FQ-01–FQ-12

| ID | Answer | Classification | Locator |
|---|---|---|---|
| FQ-01 | ARP4754B 是 recommended practice，不是法规；认证适用性取决于 certification basis 和协调。 | ARP RECOMMENDATION / BOUNDARY | 1; 1.1; 3.3 |
| FQ-02 | Development Assurance 以与 failure-condition severity 相称的 rigor 降低 development error，并整合 validation、verification、CM 和 PA。 | ARP DEFINITION / RECOMMENDATION | 1.2; 5.1–5.7 |
| FQ-03 | ARP requirement 必须可 validation，implementation 可对其 verification；Validation=正确完整，Verification=实现满足要求。 | ARP DEFINITION | 2.2 |
| FQ-04 | V0 属于航空 Development Assurance Planning；transition criteria 给 V6/V12 提供 profile semantics。 | FRAMEWORK IMPLICATION | Section 3; 3.2.2 |
| FQ-05 | aircraft→system→item flow 需要记录 allocation、delegation、cross-level verification credit 和 evidence acceptance。 | AVIATION PROFILE RULE | Section 4; 4.6.1 |
| FQ-06 | FDAL 调整 objective applicability/independence/output control；详细 FDAL/IDAL assignment 留给 ARP4761A。 | FDAL-DEPENDENT OBJECTIVE / BOUNDARY | 5.2; Appendix A |
| FQ-07 | Validation methods 与 implementation verification methods 目的不同；不得合并 taxonomy。 | ARP RECOMMENDATION | 5.4; 5.5 |
| FQ-08 | ARP verification methods 可映射 ISO 四类，但多出 explicit similarity/service-experience credit；映射不是同义替换。 | INTERPRETATION | 5.5.5 |
| FQ-09 | Coverage 是 requirements/trace-oriented；Objective 5.1 支持 method/procedure sufficiency。它们只部分支持 ISO-G02/G03。 | APPENDIX OBJECTIVE / GAP | 5.5.5.2.2; Appendix A objective 5.1 |
| FQ-10 | Process independence 是 FDAL/objective-dependent specialization；Process Assurance independence 是另一个 concern。 | AVIATION PROFILE RULE | 5.2.3.2.1.4; 5.7; Appendix A |
| FQ-11 | 6.3/6.4 支持将 V10 改名为 Change Impact & Re-verification，并把 reuse 表达成受条件约束的 credit relation。 | FRAMEWORK IMPLICATION | 6.3; 6.4 |
| FQ-12 | Certification approval 不是 Evidence；ARP4761A、DO-178C、DO-254、DO-297 的专门结论继续 deferred。 | BOUNDARY / OPEN QUESTION | 1; 3.3; 5.5.6 |

## 15. Gap decisions and follow-up

- `ISO-G01`: **Partially Supported — Aviation Profile Only**。新增 objective-dependent independence，不关闭 generic gap。
- `ISO-G02`: **Partially Supported — Requirements Coverage Only**。没有 universal coverage taxonomy。
- `ISO-G03`: **Partially Supported — Aviation Profile Only**。Objective 5.1 支持 method/procedure sufficiency，不定义整体 sufficiency formula。
- `ISO-G05`: **Strengthened / Renamed response**。V10 改为 Change Impact & Re-verification。
- `ISO-G06`: **Partially Supported**。输出、OPR、CM/PA 和 transition criteria 支持 closure inputs；waiver/reopen/authority state model 未定义。
- `ARP-G01`：ARP4761A 已补充 FDAL/IDAL assignment 与 typed independence；record semantics 仍需 item-level standards 复核后冻结。
- 新增 `ARP-G02`：cross-level verification allocation/delegation/credit acceptance 关系需要信息模型。
- 新增 `ARP-G03`：unintended-behavior obligation 的适用边界、coverage 和 evidence sufficiency 尚待后续标准与实证研究。

ARP4761A 研究已完成并记录于 `sae_arp4761a.md`，补充了 failure-condition classification、Safety Requirement provenance、FDAL/IDAL assignment、typed independence、assumptions 与 safety evidence。下一步是跨标准一致性与差距复审；item-level 结论继续留给 DO-178C、DO-254 和 DO-297。
