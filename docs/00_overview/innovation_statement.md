---
title: Research Innovation Statement and Work Boundary
status: working
version: 0.1
baseline: v0.1
owner: research
last_updated: 2026-08-19
dependencies:
  - research_scope.md
  - research_questions.md
  - ../01_normative_foundation/normative_gap_matrix.md
  - ../01_normative_foundation/consolidation/five_source_consistency_gap_review.md
---

# Research Innovation Statement and Work Boundary

本文件声明本研究的创新性主张与工作边界：哪些内容由标准/规范给出、本研究只承担研究、抽象与总结；哪些内容是本研究原创。它同时是论文 contributions 的主张登记，与 gap matrix（"标准没说什么"的创新侧登记）和 §28 provenance annex 联动。

**维护规则：** 创新主张与 gap 状态联动——当后续标准研究为某主张提供对象依据时（如 9646/X.290 之于 Oracle），主张性质从"对象创造"迁移为"对象应用/扩展"，迁移记录于 gap matrix；主张对象进入 executable schema 前必须满足 §28 annex 的 schema gate。publications 只引用本文件，不重定义。

## 1. Work boundary：标准给出 vs 本研究创建

| 内容类别 | 来源 | 本研究的角色 | 输出形式 |
|---|---|---|---|
| 通用过程/信息项/测试方法论标准（ISO 15288、24748 系列、15289、29148、15026 系列、29119 核心部分、9646/X.290、IEEE 1012 等） | generic lifecycle / V&V / 信息项 / 测试方法论 | **研究**：条款精读、五级分类、条款定位、跨标准调和（对齐差异而不抹平差异） | standard notes、standards map（约束登记）、terminology |
| 领域保证标准（ARP4754B/4761A、DO 系列） | domain profile 规则 | **研究 + 抽象**：条款精读；经抽象阶梯提取可泛化 pattern（保留 source provenance） | profile 研究、pattern library 候选、§28 annex 登记 |
| 实例标准（ARINC 615A 等） | 实例验证依据 | **不在本仓库研究其本体**；实例执行在外部仓库 | `docs/08_validation/` 只维护实例策略、锻炼矩阵与评价判据 |
| 测试执行技术（TTCN-3、SysML 等） | 平台实现选型 | **选型评估**，不定义框架语义/信息模型 | 平台参考架构（可替换项） |

**不得声称为己有：** 所有 source-native 概念的引用必须保留条款定位（CONTRIBUTING 规则）。本研究对标准内容的系统性加工（调和、登记、抽象）作为 related-work 级贡献呈现，不作为方法论创新主张的主体。

## 2. Innovation claims（四层主张）

### 2.1 Layer 1 — 论题级（论文存在的理由）

| ID | 主张 | 锚点 | 状态 | 验证载体 |
|---|---|---|---|---|
| INN-T1 | **Verification Sufficiency 推理语义**：异构证据（test/analysis/inspection/model output）聚合为 justified conclusion 的推理结构、残差风险显式接受、argument patterns | RQ4、ISO-G03B、SufficiencyAssessment annex 行 | 概念接口已冻结；推理语义为 Phase 5 开放工作 | UAV FMS、LLM 服务 |
| INN-T2 | **Verification Obligation 中间对象链**：`typed Basis {Requirement \| Specified Characteristic \| Applicable Constraint} → Obligation → Strategy`，填补标准从 requirement 直接跳到测试活动的中间空白 | §22 PROMOTE、annex；standard 无此原生对象 | conceptual baseline；schema gate 未过 | 全部实例（ARINC 615A 最先） |
| INN-T3 | **Evidence 角色分离模型**：identity / provenance / applicability / credibility / sufficiency 五谓词分离，`mayConstituteOrSupport` 而非二值转换 | consolidation §14、Evidence annex 行 | conceptual baseline | 全部实例 |

### 2.2 Layer 2 — 架构级

| ID | 主张 | 锚点 | 状态 | 验证载体 |
|---|---|---|---|---|
| INN-A1 | **V0–V12 mixed-ontology 过程视图 + Composite Gate**：assessment ≠ review ≠ decision ≠ state event 的组合门语义；验证专属跨过程编排 | LC-G01/G03、consolidation §7 | ontology 已冻结；state model 开放 | 平台原型 + 全实例 |
| INN-A2 | **跨标准验证本体调和**：dual V&V 定义、dual method taxonomy、typed independence 的不抹平统一 | consolidation §5/§20 | 已完成首轮（五源） | 论文本体章；全实例术语一致性 |
| INN-A3 | **抽象阶梯机制与首批抽象产物**：机制本身 + criticality-scaled assurance intensity（源自 FDAL，候选通用依据 ISO 15026-3/IEEE 1012 待研究）、model-evidence admissibility（源自 ARP4761A App. N）、DCAS 工程模式（source selection/hysteresis/CRC 等） | research_scope 抽象阶梯、Phase 6 | 机制已立；产物为 Phase 6 工作 | 非源领域实例复用检验 |

### 2.3 Layer 3 — 机制级（gap matrix 中最硬的空白）

| ID | 主张 | 锚点 | 状态 | 验证载体 |
|---|---|---|---|---|
| INN-M1 | **变更影响选择算法**：风险驱动的 re-verification selection（标准只要求"重验"，不定义"选哪些"） | ISO-G05 继承者 | open | UAV FMS（变更场景） |
| INN-M2 | **Closure 状态机**：waiver / deviation / reopen / authority / scope-level state 的形式化模型 | ISO-G06 继承者 | open | 平台原型 + 实例 closure 记录 |
| INN-M3 | **Coverage 计算模型**：population + criterion + evidence + disposition 的可计算对象，domain taxonomy 可插拔 | ISO-G02A/B | meta-model 已冻结；taxonomy 开放 | ARINC 615A（条款覆盖）、UAV（需求/安全覆盖） |
| INN-M4 | **Oracle 对象化**：expected-result 正确性依据作为受控对象；确定性 oracle（9646 候选依据，研究中）+ 概率 oracle（完全开放） | ISO-G04 | research proposal | ARINC 615A + LLM 服务 |
| INN-M5 | **模型证据可采性规则**：模型/工具输出何时可承担 Evidence role 的通用条件 | ISO-G08 | open | 平台原型（模型检查输出）、MBSA 抽象 |

### 2.4 Layer 4 — 实现级

| ID | 主张 | 锚点 | 状态 | 验证载体 |
|---|---|---|---|---|
| INN-I1 | **机器可读验证 metamodel + 非产品化平台原型**：obligation→evidence 全链可查询、可检查、可执行 | Phase 8/9、consolidation §23 | planned | 三实例 + 自动化原型 |
| INN-I2 | **符合性测试传统与生命周期保证传统的统一信息模型**：test purpose/PICS 类声明 ↔ Obligation/Basis、verdict ↔ Result/Evidence、ATS/ETS ↔ Case/Procedure 的焊接（主张的原创性需文献轨核实） | 9646/X.290 研究线、first instance | 研究中（9646 概念切片） | ARINC 615A 实例 |

## 3. Non-claims（明确不主张为创新）

1. 标准条款研究、gap 登记、术语调和——系统性 related work 基础，不是方法论创新主体；
2. Generic/Profile 分层原则——社区已有共识；本研究增量是**条款级执行与机制化**（layering policy、抽象阶梯、provenance annex）；
3. 单一实例跑通 ≠ 框架验证——全称主张须按实例 × 框架元素锻炼矩阵由多实例分担；
4. 不主张任何适航/certification 符合性——平台与框架只产生可审计证据，符合性声明主体永远是组织；
5. 概率 oracle（LLM 实例）为高风险主张：允许以"框架边界暴露"的负结果形式报告。

## 4. Methodology–instance decoupling contract

1. 本仓库的通用验证方法论细化至 **implementation framework** 层级：稳定信息模型、metamodel、平台参考架构（技术选型为可替换项）、extension points、验收判据与评价协议；
2. `docs/` 通用层禁止出现任何特定实例内容（协议名、系统名、实例数据）；实例策略性信息只存在于 `docs/08_validation/`；
3. **实例执行在独立外部仓库进行**：首个实例为 ARINC 615A 协议符合性验证，其仓库全面基于本仓库提出的方法论与平台框架开展实例研究；
4. 外部实例仓库必须**引用本仓库稳定对象 ID**（VOB-/VSR-/COV- 等，见 ARCHITECTURE 候选 ID）而不是重定义框架对象；
5. 实例证据只以评价数据形式按锻炼矩阵维度回流本仓库（RQ8），不得反向定义框架对象；
6. 本仓库方法论若出现实例耦合内容，视为违反本契约的缺陷（评审按 CONTRIBUTING 触点清单核查）。
