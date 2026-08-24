---
title: Candidate Contribution Register and Work Boundary
status: working
version: 0.4
baseline: post-v0.2
owner: research
last_updated: 2026-08-25
dependencies:
  - research_scope.md
  - research_questions.md
  - ../01_normative_foundation/normative_gap_matrix.md
  - ../01_normative_foundation/consolidation/five_source_consistency_gap_review.md
  - ../02_verification_framework/generic_verification_suite_core.md
  - ../08_validation/cross_repository_instance_contract.md
---

# Candidate Contribution Register and Work Boundary

本文件控制候选研究贡献，不把 gap 当作 novelty proof。标准没有在已研究切片中给出某对象，仅能触发更广的 source search；只有相关检索达到 `SOURCE SEARCH COMPLETE`、强反例检验未推翻主张且验证完成后，才可形成强原创性表述。

## Candidate-test ownership and novelty boundary

Tasks 001–021 may return only `SUPPORT`、`QUALIFY`、`FALSIFY` or `NO EVIDENCE` for their assigned candidates. Task 022 reconciles those records as `SUPPORTED`、`QUALIFIED`、`FALSIFIED` or `OPEN` and produces follow-on search questions. Neither a source task nor Task 022 may set `novelty established`.

`Standards silence ≠ novelty`：标准未规定某对象或算法只形成 `innovation-space observation`。强新颖性结论必须由单独、可复核的同行评议文献、专利及工业方案检索与 falsification review 支持，并说明检索总体、时间边界、查询式、排除规则、竞争机制和残余不确定性。来源数量不能替代证据质量，跨标准综合也不能替代该检索。

允许值：`claim_type` = thesis / architecture / mechanism / implementation；`novelty_status` = hypothesis / candidate / not established；`validation_status` = conceptual / planned / in progress / supported / falsified。

## Work boundary

| 内容 | 本研究角色 | 非主张边界 |
|---|---|---|
| 通用过程、信息项、assurance 与测试方法标准 | 条款研究、比较、可追溯抽象 | 不把标准原生概念据为原创 |
| 航空保证来源 | profile 研究；经抽象阶梯形成可证伪候选 | 不把航空规则直接泛化 |
| 实例标准与实例数据 | 外部仓库实例化和评价 | 不反向重定义框架对象 |
| 执行技术 | 可替换选型与原型评价 | 不定义 normative semantics |

跨标准调和、Generic/Profile 分层、条款研究和 gap 登记是必要的 related-work 与治理基础，但不是本研究的主要创新主张。

## Candidate GVS Core engineering-outcome position

The [Candidate GVS Core](../02_verification_framework/generic_verification_suite_core.md) is the working principal engineering outcome: composable Verification Capability Packages plus semantic, extension, version, migration and evaluation contracts. This is an integration target for the controlled candidates below, not a new claim that the package set is novel, validated or executable. Standard evidence and instance evidence may only `SUPPORT`、`QUALIFY` or `FALSIFY` relevant candidates under their existing gates.

The cross-repository boundary uses **strong semantic contract / weak implementation coupling**. Canonical Core definitions remain here; external repositories own Profile, Binding, Configuration, implementation and raw evidence. ARINC evidence cannot directly promote an object, close RQ8 or establish Generic rights.
## Controlled candidate contributions

| ID | Candidate contribution | claim_type | novelty_status | validation_status | Falsification condition | Source / gap anchor | Non-claim |
|---|---|---|---|---|---|---|---|
| INN-T1 | Verification Sufficiency 的显式推理接口与残差处理语义 | thesis | candidate | conceptual | 既有通用标准或文献已给出等价、可执行且跨证据类型的完整语义 | RQ4; ISO-G03B; 15026 family / IEEE 1012 candidate search | 不宣称五源未定义 sufficiency 即证明原创 |
| INN-T2 | `typed Verification Basis → Verification Obligation → Strategy` 的框架中间对象链 | thesis | hypothesis | conceptual | 既有 standards/research 已定义等价 obligation 对象、typed basis 与生命周期关系 | §28; ISO-G07; 15289/29148/29119/9646 candidate search | 不声称标准普遍“从 requirement 直接跳到 test”；五源局部观察不是全领域结论 |
| INN-T3 | Evidence identity、provenance、applicability、credibility 与 sufficiency 的分离模型 | thesis | candidate | conceptual | 既有 assurance/evidence metamodel 已提供等价谓词和关系 | consolidation §14/§28; 15026 search | 不把 Evidence 或 Claim–Argument–Evidence 概念本身主张为原创 |
| INN-A1 | V0–V12 mixed-ontology 编排与可分解 Composite Gate | architecture | candidate | conceptual | 既有 lifecycle architecture 已提供等价编排和相同可分解 gate contract | LC-G01/LC-G03; 24748 family | 不主张 gate/review/decision 概念本身原创 |
| INN-A2 | 在保留 dual definitions/taxonomies/profiles 的前提下建立可追溯一致性视图 | architecture | not established | supported | 文献显示该调和产物仅是常规 standards mapping，且无独特机制或评价增量 | five-source consolidation | 跨标准调和本身不是主要方法论创新；仅作为贡献性研究资产评价 |
| INN-A3 | profile pattern 经受控抽象阶梯进入 generic candidate 的机制 | architecture | hypothesis | planned | 已有 profile-extension governance 提供等价 provenance、promotion gate 和跨域验证规则 | research_scope; §28; Phase 6 | 不把 criticality 或 model evidence 概念据为原创 |
| INN-M1 | 风险与影响驱动的 re-verification selection 方法 | mechanism | hypothesis | planned | 更广标准/文献已规定等价 selection 方法，或实例评价不能优于透明基线 | ISO-G05; IEEE 1012 / change-impact literature search | 不声称“标准只要求重验、不定义选择”；这是待检索假设 |
| INN-M2 | waiver/deviation/reopen/authority/scope state 的 Closure 状态模型 | mechanism | hypothesis | planned | 既有 lifecycle/change-control 标准已定义等价模型，或状态模型不能稳定处理实例 | ISO-G06; 24748-8/16326 candidates | 不把审批或基线状态本身主张为原创 |
| INN-M3 | population + criterion + evidence + disposition 的可计算 coverage 模型 | mechanism | hypothesis | conceptual | 既有 coverage metamodel 等价，或跨实例无法保持可比且可扩展 | ISO-G02B; 29119/item-profile candidates | 不主张任何 universal percentage 或 completion rule |
| INN-M4 | 将 expected-result 正确性依据建模为受控 Oracle 候选对象 | mechanism | hypothesis | planned | ISO/IEC 9646、testing literature 或其他来源已有等价对象与控制语义，或实例无独立对象需求 | ISO-G04; ISO/IEC 9646 / 29119 search | 不把 expected result 自动重标为 Oracle |
| INN-M5 | 模型/工具输出承担 Evidence role 的通用可采性条件 | mechanism | hypothesis | planned | MBSE/V&V 文献已有等价通用规则，或跨领域评价失败 | ISO-G08; 24641 / assurance literature | 不声称工具输出天然是 Evidence |
| INN-I1 | Candidate GVS Core 的可选 machine-readable metamodel / executable evaluation realization | implementation | hypothesis | planned | 既有开源/研究平台提供等价模型和评价能力，或原型无法支持审计查询 | Phase 8/9 | 不把工程实现本身自动等同学术创新 |
| INN-I2 | conformance-testing 与 lifecycle-assurance 传统之间的受控映射模型 | implementation | not established | planned | ISO/IEC 9646、29119、15026 或既有研究已经给出等价统一模型 | ISO-G04/G07; source search pending | 新颖性未建立；不预设 PICS/test purpose/verdict 映射为原创 |

## Methodology–instance decoupling contract

1. 本仓库控制 Candidate GVS Core 的通用对象职责、关系、extension-point contract、跨实例评价协议及未来兼容规则；实例仓库控制 Verification Profile、Product Binding、Project Configuration、执行工具、具体 Oracle 实现和原始证据；
2. 强契约首先固定语义、输入/输出、关系、不变量、版本身份、兼容/迁移规则和失败语义，不冻结语言、API、serialization、schema、metamodel 或工具实现；
3. `VOB-`、`VSR-`、`COV-` 等目前只是 candidate prefixes。versioned object registry 建立前使用受控临时映射；稳定引用最低字段保持 `ObjectID`、`ObjectVersion`、`DefinitionVersion`、`IntroducedIn`、`SupersededBy`、`Status`、`CanonicalLocator`、`CompatibilityRule`；
4. 实例 finding 反馈链为 `Instance finding → Framework Change Proposal → cross-instance relevance assessment → normative basis / research rationale → review → architecture/object registration when eligible → framework update → instance migration assessment`；
5. 实例证据只能 `SUPPORT`、`QUALIFY` 或 `FALSIFY` 候选主张。在变更获批前，它不修改 canonical definition；单一 ARINC 实例不能关闭 RQ8；
6. 通用教程权威属于本方法仓库；实例仓库只能维护实例教程或标明非权威的派生视图；
7. 受控契约、[temporary instance registry](../08_validation/instance_registry.md)、[ARINC mapping register](../08_validation/arinc_615a_object_mapping_register.md) 与 [evaluation protocol](../08_validation/arinc_615a_instance_evaluation_protocol.md) 是当前治理入口；
8. 任何 publication 必须引用当时不可变版本，并区分 hypothesis、candidate、validated contribution 与 non-claim。
