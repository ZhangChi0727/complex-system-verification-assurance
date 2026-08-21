---
title: NASA Systems Engineering Handbook (SP-2016-6105 Rev2) Research Note
status: working
version: 0.1
baseline: v0.1
owner: research
last_updated: 2026-08-19
review_state: awaiting internal review
source:
  standard: NASA Systems Engineering Handbook
  document_id: NASA/SP-2016-6105 Rev2
  edition: second (supersedes SP-2007-6105 Rev1)
  date: 2016
  source_type: local-copy-not-committed (U.S. Government work; locator+paraphrase only)
  layer_role: practice-comparison reference（per standards_baseline practice-comparison reference register；非 clause-study 源）
dependencies:
  - ../standards_baseline.md
  - ../standards_map.md
  - ../consolidation/five_source_consistency_gap_review.md
---

# NASA Systems Engineering Handbook (SP-2016-6105 Rev2) Research Note

> 状态说明：本笔记已完成条款级研究，**待内部评审**（评审范围与本笔记结论遵循 CONTRIBUTING 触点清单）；评审通过前不更新 standards_baseline 的 Study status，不进入跨标准映射。

## 1. 研究边界与来源分类

本笔记研究 NASA/SP-2016-6105 Rev2（2016 第二版，297 页），覆盖 §2（基础）、§3（生命周期与 tailoring）、§5.3–5.4（Product Verification/Validation）、§6.1/6.2/6.5–6.7（技术规划、需求管理、配置管理、技术数据管理、技术评估）及附录 C/D/E/I/J。原文为美国政府出版物（public domain），但本笔记仍按仓库纪律采用转述 + 条款定位，不复制大段原文。

**认识论边界（本笔记最重要的前提）**：手册是 **guidance**，其描述的 17 个 common technical processes 的强制性载体是 **NPR 7123.1**（NASA 内部程序性要求），入口/成功判据在 NPR 7123.1 Appendix G，生命周期与 KDP 在 NPR 7120.5。**本仓库未直接研究任何 NPR**——凡手册归于 NPR 的要求，本笔记一律标 `NPR-ATTRIBUTED (second-hand)`，不得当作直接规范依据引用。这使本来源的独特价值定位为：**非航空领域的工程实践对照与证据源**，而非 generic-layer 规范基础；其结论进入 generic 层只能走抽象阶梯（layering policy 规则 3）。

分类标签：`NASA GUIDANCE`（手册正文指导）、`NPR-ATTRIBUTED (second-hand)`（手册转述的 NPR 要求）、`PRACTICE EVIDENCE`（实践证据，用于加固既有跨标准结论）、`INTERPRETATION`、`FRAMEWORK IMPLICATION`、`RESEARCH PROPOSAL`。

## 2. 总体结论

1. **V&V 语义三分格局获得决定性加固**：NASA 的 Validation 明确绑定 ConOps/stakeholder expectations/MOEs（§2.4; §5.4），与 ISO 15288 的 intended-use 语义同侧，而非 ARP4754B 的 requirement-validation 对象层。五源 consolidation 的 Validation 双对象层决策（§5）现在有了**第三个独立来源**。
2. **Verification 完成判据首次获得显式双条件**：§5.3.1.3 给出 "(1) documented objective evidence of compliance with requirements or waiver and (2) closure of all discrepancy and nonconformance reports"——ISO 无命名 closure、ARP4754B 只有输入清单之后，NASA 给出了最接近 V12 完成语义的实践表述（含 waiver 显式进入关闭条件）。
3. **Certification ≠ Evidence 获跨域确认**：§5.3.1.1 框定义 Certification 为 "audit process by which the body of evidence ... is provided to the appropriate certifying authority"——与 ARP4754B 研究的 F-12/M-02 结论同构，且来自非认证监管语境。
4. **TRR 语义与 `contributesTo(V6)` 处置精确吻合**：§5.3.1.2.1 NOTE 将 TRR 定位为 Technical Assessment Process 的活动，早期阶段可非正式、后期正式、一项目多次、entrance/success criteria 可裁剪；且 TRR **不在** lifecycle review 总表（Table 6.7-1）中。这为 PR #6 评审的 M-01 处置提供了第三个来源佐证。
5. **方法 taxonomy 第三样本**：Analysis/Demonstration/Inspection/Test 四法与 ISO informative 示例、ARP4754B 家族可映射；**similarity 位于 Analysis 之内**（含 heritage product 相似性验证），支持 ISO 式归类而弱化 ARP 的独立方法族地位——三源中 2:1 支持 similarity 作为 technique。
6. **信息项 schema 证据丰富（ISO-G07 前置输入）**：Table 5.3-1（procedure/report 内容）、Appendix D RVM、Appendix I V&V Plan outline、Table 3.0-1（产品成熟度矩阵：Preliminary/Baseline/Update/Initial/Final 状态 × review 关联，** = review 必需产品）构成本仓库目前最完整的**公开可得**信息项结构样本。
7. **两个抽象阶梯输入**：payload risk class A–D（NPR 8705.4）驱动 verification formality——与 FDAL 构成两个独立领域的 criticality-scaled rigor 实例，直接支撑 INN-A3 抽象；end-to-end testing（任务线程/场景驱动、外部接口焦点）是五源未有的 named verification 活动模式，为 scenario-based case design 提供实践母体。
8. **回归测试获得显式定义但无选择算法**：§5.4 定义 regression testing 为 "rerunning previously used acceptance tests (primarily used for software)"——ISO-G05 的 open 状态不变，但获得实践语义锚点。

## 3. SE 引擎与过程架构

**NASA GUIDANCE / NPR-ATTRIBUTED — §2.1; Figure 2.1-1**

17 个过程分三组：System Design（4，自顶向下逐层应用）、Product Realization（5：Implementation/Integration/**Verification**/**Validation**/Transition，自底向上逐层应用）、Technical Management（8，crosscutting）。"iterative"（对同一产品集纠正偏差）与 "recursive"（对相邻产品层重复应用）定义转述自 NPR 7123.1。

- **PRACTICE EVIDENCE**：这是继 ISO 15288 5.8、ISO 24748-1 Clause 5/Annex A 之后第三个确认迭代/递归/并发过程应用的来源；且 "Product Realization 逐层向上、System Design 逐层向下" 的双向递归结构为 `requirement_allocation_level ≠ verification_execution_level` 提供了过程学解释。
- Table 2.1-1 给出 17 过程 ↔ AS9100 条款对齐——NASA 过程模型与航空质量体系（AS9100/ARP 语境）的工程互操作性证据，间接触证跨标准调和的可行性。
- **FRAMEWORK IMPLICATION**：V0–V12 过程视图叙事再次获得独立确认；不改变既有 ontology 冻结。

## 4. V&V 语义与跨标准定位

**NASA GUIDANCE — §2.4; §5.3; §5.4**

| 维度 | Verification（§5.3） | Validation（§5.4） |
|---|---|---|
| 核心问题 | "Was the end product realized right?" | "Was the right end product realized?" |
| 参考基准 | approved requirements set（"shall" statements）+ configuration baseline | baselined stakeholder expectations：needs/goals/objectives + **ConOps + MOEs** |
| 方法 | test/analysis/inspection/demonstration（同一四法） | 同一四法 |
| 执行时机 | 可在生命周期不同阶段多次 | **每阶段用 phase products（模型、mock-up）执行，不只在交付时**；逐产品层递归向上 |
| 参与者 | 常由开发方执行，user/customer 参与，QA 关键 | 尽可能由预期 operators/users 执行 |

**跨标准定位（INTERPRETATION）**：

```text
Validation 对象层谱系：
  ISO 15288   → intended use / operational context（系统/产品层）
  NASA        → ConOps / stakeholder expectations / MOEs（系统层 + 阶段产品层）← 与 ISO 同侧
  ARP4754B    → requirements correct & complete（需求文本层）          ← 不同对象层
```

NASA 侧证据使 consolidation §5 的 "DIFFERENT OBJECT LEVEL" 分类从 2 源对峙变为 **2:1**，System/intended-use Validation 作为 generic 语义的置信度提升。另注意 §6.2 出现 "requirements verification and validation" 措辞（指需求质量确认）与 Appendix C "Requirements Validation Checklist"——NASA 在需求层也使用 validation 词汇但**不重定义** Validation 过程本身，与 ARP 的处理不同；登记为 CONTEXTUAL DIFFERENCE，不改变结论。

**BOUNDARY**：V&V 合并执行被允许（"combining tests to perform verification and validation simultaneously"，§5.3）——合并的是**测试事件**，不是语义；与框架"共享信息骨架、分开 claim/reference/actor"的处置一致。

## 5. Product Verification 过程解析

### 5.1 输入（§5.3.1.1）

product to be verified（来自 Implementation/Integration）、**baselined verification plan**（Technical Planning 产出）、**specified requirements baseline（"Acceptance criteria should have been identified for each requirement to be verified"）**、enabling products。侧栏框同时区分 Verification / Qualification / Acceptance / Certification 四概念。

**FRAMEWORK IMPLICATION**：逐需求预置 acceptance criteria 是 V1/V3 的第三源实践证据（ISO 的 success criteria task + ARP 的 per-requirement method 之后）；"verification program performed once regardless of how many flight units（as long as the design doesn't change）" 为 Prior Evidence Applicability 提供设计不变性判据的实践表述。

### 5.2 五活动与流程位置（§5.3.1.2）

prepare → perform → analyze results → report → capture work products。要点：

- **准备就绪语义**：四项 outcome（plan/procedures/baseline on hand；被测件与 enabling products 已并入验证环境；资源到位；**环境 adequacy/completeness/readiness/integration 已评价**）——V6 readiness assessment 的实践判据集；
- **TRR**：见 §2 结论 4；peer reviews 作为补充（正式或非正式）；
- **多层验证与 end-to-end testing**：验证可分布于 component/assembly/subsystem/system 各层；end-to-end testing 按 verification plan 指定的层级（通常 segment/element）聚焦**外部接口**与完整任务线程（operational scenarios），内部接口不属其范围；
- **discrepancy 处置**：观察即停、出 discrepancy report、区分 product nonconformance 与验证执行/程序问题、用 **Decision Analysis Process** 决定计划/环境/程序变更——V9 编排 + 显式决策点的实践样本；
- **结果分析**：数据按 "quality, integrity, correctness, consistency, validity" 分析；结果记入 **requirements compliance / verification matrix**；**waivers 于此识别**；nonconformance 经 MRB/CCB（含风险管理参与）审批；
- **再工程与再验证**：变更产品 → 重新 plan/perform verification。

### 5.3 完成判据（§5.3.1.3）

**PRACTICE EVIDENCE（本笔记最高价值条目）**：双条件 = ①合规的客观证据文件化 **或 waiver**；②全部 discrepancy/nonconformance report 关闭。对应 V12 composite gate 的 assurance-assessment + disposition 输入；waiver 进入完成条件为 ISO-G06 的 waiver 语义提供实践锚点。authority/state model 仍 open（KDP 决策权在 NPR 7120.5，second-hand）。

## 6. 验证方法 taxonomy

**NASA GUIDANCE — §5.3 Methods of Verification 侧栏**

| NASA 方法 | 定义要点 | 与 ISO/ARP 对照 |
|---|---|---|
| Analysis | 数学建模与分析技术；**含 modeling & simulation**；含 **verification by similarity of a heritage product** | similarity 归入 Analysis（与 ISO NOTE 一致，与 ARP4754B 独立方法族不同）→ 2:1 |
| Demonstration | 基本性能确认，**无详细数据采集**（区别于 test 的判据） | 首次给出 test/demonstration 的操作性区分判据 |
| Inspection | 对已实现产品的目视检查；可含 drawings/documents/records 检查 | 对象含文档记录，支持 artefact-level verification |
| Test | 受控条件下逐需求获取详细数据；最资源密集 | "Test as you fly, and fly as you test" 原则 |

**FRAMEWORK IMPLICATION**：Demonstration/Test 的区分判据（数据采集深度）可进入 Verification Method 语义注记；similarity 统计更新为 ISO+NASA 归 technique、ARP 归 method——method taxonomy 保持 contextual mapping，不冻结任一来源枚举（维持 consolidation §20 决定）。

## 7. 信息项 schema 证据（ISO-G07 前置输入）

**NASA GUIDANCE — Table 5.3-1; App D; App E; App I; Table 3.0-1**

- **Verification Procedure 字段**（Table 5.3-1 左列）：被测件标识、目标与判据（含容差的可接受/拒收特征值）、顺序步骤、软件标识、测量设备（range/accuracy/type）与**校准记录规定**、as-run procedure 副本（含 redlines）、测试布局图、危险与安全事项、环境条件及容差、nonconformance 处置指令、设施规范；
- **Verification Report 字段**（右列）：目标达成程度、测试配置与**飞行构型差异**、偏差描述、逐活动/逐程序结果与**数据/工件链接**、分析结果、性能数据表、nonconformance 汇总 + disposition + 纠正措施 + retest 计划、结论建议、**"Authentication of test results and authorization of acceptability"**（结果认证与可接受性授权——Result 与 approval 分离的又一实证）；
- **RVM（App D）**：requirement no. / document / paragraph / shall statement / **verification success criteria** / method / facility / phase / acceptance 标志 / performing organization / **results（objective evidence 文档指针）**；"Only 'shall' requirements should be included"——basis 即 requirement 类型，义务粒度 = shall 语句；
- **V&V Plan outline（App I）**：方法定义（含 qualification/other test 细分）、**certification process** 节、acceptance testing 哲学、test article **pedigree**、逐 end-item × 4 方法的活动矩阵、**PDR 意见并入后 baseline**；
- **产品成熟度矩阵（Table 3.0-1, NPR-ATTRIBUTED）**：SE 产品（含 V&V plans、V&V results）× 阶段/review 的 Preliminary/Baseline/Update/Initial/Final 状态，`**` 标记 review 必需产品——**信息项生命周期状态模型的实践实例**，直接喂 ISO-G07 与 composite gate 入口判据。

**BOUNDARY**：以上均为 guidance 示例，不构成规范 schema；进入框架须经 15289 研究后按 §28 annex schema gate 处理。

## 8. Product Validation 与回归测试（§5.4）

- 验证后逐层向上验证；validation deficiency 三分：执行不良 / verification 短板 / **设计本身错误**（排除前两类后 validation 的真正价值是发现设计变更需求）；
- "Pass Verification but Fail Validation?" 侧栏：预防手段是早期 ConOps 与用户参与——V&V 语义分离的工程论据；
- **Regression testing 显式定义（PRACTICE EVIDENCE）**："a formal process of rerunning previously used acceptance tests (primarily used for software), is one method to ensure a change does not affect function or performance that was previously accepted"——V10 获得非航空语境的回归语义（acceptance-test 重跑基线）；选择算法仍无，ISO-G05 维持 open；
- 生产多台后续交付件用 **acceptance testing** 而非持续 V&V——V&V 与验收的证据适用性边界实践。

## 9. 技术管理过程要点

- **Requirements Management（§6.2）**：traceability/bidirectional traceability 定义（与 ISO 3.52 语义一致）；**V&V results 回映射到 requirements database，"goal of verifying and validating all requirements"**——需求域 coverage 的实践表述（ISO-G02 侧证）；self-derived requirements 处置（trace 至 parent 或确认自衍生，否则视为 gold-plating 消除）——orphan disposition 的实践规则；
- **CM（§6.5）**：四基线绑定 review（functional@SDR、allocated@PDR、product@CDR、as-deployed@ORR）；**waiver/deviation 定义**（waiver = 有意解除某要求符合性的书面协议；deviation 用于 Implementation 前）；CM 原则溯源 SAE/EIA-649B（跨行业标准再引用现象）；FCA/PCA 审计属 configuration verification；
- **Technical Assessment（§6.7 + Table 6.7-1）**：13 类 lifecycle review（MCR/SRR/MDR-SDR/PDR/PRR/SIR/CDR/SAR/ORR/FRR/PLAR/CERR/PFAR），entrance/success criteria 全部指向 NPR 7123.1 App. G 表（second-hand）；PDR 结果含 "verification methods have been described"、CDR 批准 verification plans、SAR/ORR/FRR 消费 V&V 证据——**composite gate 的完整实践标本**：review（评价）→ KDP（决策权在 decision authority，可附 **liens** 限期解除、可重试或终止，§3.0）→ baseline 事件（Table 3.0-1 状态迁移）；
- **Tailoring（§3.11）**：compliance matrix 方法 + 审批要求——LC-G04 instantiation record 的第三实践源。

## 10. V0–V12 reassessment

| V-ID | NASA 实践证据 | 关系强度 |
|---|---|---|
| V0 | Technical Planning/SEMP/V&V Plan；验证途径因素清单（项目类型、A–D class、成本进度、风险、设施、采办策略、heritage） | contributes（实践对照） |
| V1 | specified requirements baseline + 逐需求 acceptance criteria | strengthens |
| V2 | App C verifiability 清单 + **不可验证词表**（flexible/easy/sufficient/safe…） | strengthens（第三源） |
| V3 | 验证方法选择的 risk-informed trade + engineering judgment | strengthens |
| V4 | RVM 逐需求目标/判据；operational scenarios/end-to-end 线程 | contributes（Case 前身实践） |
| V5 | Table 5.3-1 procedure 字段集 | strengthens |
| V6 | 准备就绪四判据 + TRR（Technical Assessment 活动、可裁剪、多次） | **`contributesTo(V6)` 第三源确认** |
| V7 | 执行 + 校准 + 数据采集；end-to-end testing | strengthens |
| V8 | 五性数据分析；pass/fail 声明；authentication/authorization 分离 | strengthens |
| V9 | discrepancy 即停/报告/归因/Decision Analysis/MRB-CCB | strengthens |
| V10 | regression 定义；nonconformance 变更后 re-verification；设计不变性判据 | strengthens（算法仍 open） |
| V11 | RVM 全需求闭合目标；TPM/MOE 监控 | 需求域 coverage 侧证 |
| V12 | 双条件完成判据（含 waiver）；SAR/ORR/FRR + KDP liens | **显著加固**；authority/state 仍 open |

无一改动 V0–V12 冻结本体；全部为实践对照级贡献。

## 11. Gap matrix 影响（不新增行，仅状态证据）

| Gap | 影响 |
|---|---|
| ISO-G01 independence | UNCHANGED——"developer 常执行验证 + QA 参与 + requirements 尽可能独立评价"，无独立性等级；再次确认 typed independence 为 aviation-only |
| ISO-G02 coverage | 侧证增强——RVM + "all requirements" 目标；无 taxonomy/百分比 |
| ISO-G03 sufficiency | UNCHANGED——完成判据 ≠ 充分性推理 |
| ISO-G04 oracle | UNCHANGED——acceptance/success criteria 存在，无独立 Oracle 对象 |
| ISO-G05 regression | CLARIFIED——显式定义（acceptance-test 重跑）；无选择算法 |
| ISO-G06 closure | STRENGTHENED——双条件完成判据 + waiver + KDP liens；authority/state 仍 open |
| ISO-G07 schema | CONTRIBUTES——公开信息项结构样本（15289 前的最大实践输入） |
| ISO-G08 MBSE | CLARIFIED——M&S 属 Analysis；M&S 保真度列为 validation deficiency 成因；"all analysis under configuration control" |
| LC-G01/G02 | STRENGTHENED——KDP(决策)/review(评价)/TRR(活动) 三分实践标本 |

## 12. 抽象阶梯输入（INN 联动）

1. **Payload Class A–D → verification formality**（NPR 8705.4 驱动，§5.3.1.2）：与 FDAL 构成双域实例 → INN-A3 criticality-scaled assurance intensity 的实践证据增强；候选通用依据仍待 ISO 15026-3 / IEEE 1012 研究；
2. **End-to-end testing / operational scenario 线程**：五源无此 named 模式 → scenario-based verification pattern 候选（Phase 6），并与 9646 test purpose 线索潜在汇合；
3. **Test article pedigree**（breadboard/prototype/engineering/qualification/protoflight/flight）：evidence applicability 的配置维度实践枚举 → Prior Evidence Applicability / evidence-identity 语义参考。

## 13. 研究问题答复（NNASA-Q01–Q10）

| ID | 问题 | 答复 | 分类 / 定位 |
|---|---|---|---|
| Q01 | 手册是要求还是指导？ | Guidance；强制性在 NPR 7123.1/7120.5（未直接研究） | §1 边界 |
| Q02 | V&V 语义与 ISO/ARP 关系？ | Validation 与 ISO 同侧（ConOps/stakeholder 层）；Verification 与两者同侧（specified requirements 合规） | §2.4; §5.3–5.4 |
| Q03 | 方法 taxonomy？ | 四法；similarity 属 Analysis；demonstration/test 以数据采集深度区分 | §5.3 侧栏 |
| Q04 | TRR 是 gate 吗？ | 否——Technical Assessment 活动、可裁剪、不在 lifecycle review 表中 | §5.3.1.2.1 NOTE; Table 6.7-1 |
| Q05 | 验证完成判据？ | 双条件：证据或 waiver + 报告全关闭 | §5.3.1.3 |
| Q06 | certification 与 evidence？ | Certification = 向 authority 提交证据体的审计过程，非证据本身 | §5.3.1.1 框 |
| Q07 | 回归如何处理？ | 显式定义（acceptance-test 重跑）；变更后 re-verification；无选择算法 | §5.4; §5.3.1.2.3 |
| Q08 | 独立性？ | 无验证独立性要求；QA 参与；需求评价"尽可能独立" | §5.3.1.2; §6.2 |
| Q09 | 需求可验证性？ | App C 清单 + 不可验证词表 + shall/will/should 纪律 | App C |
| Q10 | 信息项成熟度模型？ | Table 3.0-1 产品状态 × review 矩阵（NPR-ATTRIBUTED） | §3; Table 3.0-1 |

## 14. 开放问题

- NPR 7123.1/7120.5/8705.4 是否值得纳入研究（当前均不在冻结列表，且属 NASA 内部要求，研究价值需按 §25 重评分判断——初步判断：手册层证据已足够，NPR 边际增益低）；
- End-to-end testing 模式与 9646 test purpose 概念切片的汇合点（Phase 6/首轮双轨研究时处理）；
- Table 3.0-1 成熟度状态集（Preliminary/Baseline/Update/Initial/Final）与 15289 信息项状态的形式化对齐。

## 15. Baseline decision（待评审确认）

本来源已随本次 PR 登记于 Controlled Candidate-Source Baseline 的 **practice-comparison reference register**（note status: `NOTE DRAFTED; INTERNAL REVIEW PENDING`）。建议的最终状态为 `Reviewed; practice-comparison reference`：不改变五源冻结结论、不新增 gap 行、不进入 established clause basis 或 Task 022 clause dataset；贡献集中于 V&V 语义三分加固、V12 完成判据实践证据、ISO-G07 公开 schema 样本、TRR/V6 关系第三源确认、两个抽象阶梯输入。该状态晋升须待内部评审通过。
