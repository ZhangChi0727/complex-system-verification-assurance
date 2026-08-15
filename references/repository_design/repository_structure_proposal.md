我建议这个仓库不要按“论文目录”来组织，而按**研究工程 + 规范基线 + 方法论模型 + 领域实例 + 工具实现**来组织。因为你后续不仅要写文档，还要做 DBSE→MBSE、标准映射、证据架构、规则检查和案例验证；如果一开始按 `chapter1/chapter2` 组织，后面会很快失控。

一个比较稳妥的结构如下：

```
complex-system-verification-assurance/
│
├─ README.md
├─ LICENSE
├─ CONTRIBUTING.md
├─ CHANGELOG.md
│
├─ docs/
│  ├─ 00_overview/
│  │  ├─ research_scope.md
│  │  ├─ research_questions.md
│  │  ├─ terminology.md
│  │  └─ roadmap.md
│  │
│  ├─ 01_normative_foundation/
│  │  ├─ standards_baseline.md
│  │  ├─ standards_map.md
│  │  ├─ normative_gap_matrix.md
│  │  └─ standard_notes/
│  │     ├─ iso_15288.md
│  │     ├─ iso_24748.md
│  │     ├─ arp4754b.md
│  │     ├─ arp4761a.md
│  │     ├─ do_178c.md
│  │     ├─ do_254.md
│  │     └─ do_297.md
│  │
│  ├─ 02_verification_framework/
│  │  ├─ framework_overview.md
│  │  ├─ verification_assurance_concept.md
│  │  ├─ verification_levels.md
│  │  ├─ verification_methods.md
│  │  ├─ verification_techniques.md
│  │  └─ verification_closure.md
│  │
│  ├─ 03_dbse_workflow/
│  │  ├─ lifecycle_overview.md
│  │  ├─ V0_planning.md
│  │  ├─ V1_basis_establishment.md
│  │  ├─ V2_verifiability_analysis.md
│  │  ├─ V3_strategy_definition.md
│  │  ├─ V4_case_design.md
│  │  ├─ V5_procedure_development.md
│  │  ├─ V6_readiness_review.md
│  │  ├─ V7_execution.md
│  │  ├─ V8_result_evaluation.md
│  │  ├─ V9_anomaly_management.md
│  │  ├─ V10_regression.md
│  │  ├─ V11_coverage_sufficiency.md
│  │  └─ V12_closure.md
│  │
│  ├─ 04_information_model/
│  │  ├─ ontology.md
│  │  ├─ information_items.md
│  │  ├─ relationships.md
│  │  ├─ lifecycle_states.md
│  │  └─ traceability_model.md
│  │
│  ├─ 05_coverage_and_evidence/
│  │  ├─ coverage_taxonomy.md
│  │  ├─ sufficiency_model.md
│  │  ├─ evidence_architecture.md
│  │  ├─ compliance_argument.md
│  │  └─ assurance_case_mapping.md
│  │
│  ├─ 06_pattern_library/
│  │  ├─ pattern_template.md
│  │  ├─ BVA_01_boundary_value.md
│  │  ├─ EQP_01_equivalence_partition.md
│  │  ├─ LOG_01_boolean_logic.md
│  │  ├─ STM_01_state_transition.md
│  │  ├─ SRC_01_source_selection.md
│  │  ├─ TIM_01_timing.md
│  │  ├─ ROB_01_robustness.md
│  │  ├─ FIT_01_fault_injection.md
│  │  ├─ RED_01_reconfiguration.md
│  │  ├─ INT_01_integrity.md
│  │  └─ IFV_01_interface_verification.md
│  │
│  ├─ 07_mbse/
│  │  ├─ mbse_strategy.md
│  │  ├─ metamodel.md
│  │  ├─ sysml_mapping.md
│  │  ├─ constraint_rules.md
│  │  └─ automation_rules.md
│  │
│  └─ 08_validation/
│     ├─ validation_strategy.md
│     ├─ evaluation_metrics.md
│     └─ cross_domain_comparison.md
│
├─ domains/
```

这个结构里，我认为有几个原则非常重要。

第一，`docs/` 和 `domains/` 必须严格分开。`docs/` 是**产品无关的方法论**，`domains/dcas/` 才放 IDU、FDAS、429、664、EDE、重构保持之类内容。判断标准仍然是：**如果换成 EPS，这条规则是否仍成立？** 如果成立，就不能放在 DCAS 目录里。

第二，`references/` 不建议直接保存受版权保护的 SAE/RTCA 标准全文。更适合保存 `standards_baseline.md`、阅读笔记、条款索引、引用信息和本地不可公开材料的定位说明。仓库如果未来公开，这一点尤其重要。

第三，`templates/` 很关键。你现在做的是 DBSE，所以最先应该固化的不是 SysML，而是信息项模板。例如 `verification_strategy_record.md` 可以先定义：

```
id:
requirement:
verification_obligation:
verification_level:
verification_method:
verification_technique:
environment:
configuration:
oracle:
coverage_obligation:
independence:
required_evidence:
rationale:
normative_basis:
status:
```

后面 MBSE 化，本质上就是把这些字段和关系逐渐迁移到 metamodel，而不是重新发明一套对象。

第四，`models/` 和 `tools/` 要从一开始就保留，但初期可以几乎为空。这样仓库结构已经为第二阶段预留位置，同时不会逼着当前研究过早进入 SysML 或代码开发。

第五，我建议给所有正式研究对象建立**稳定 ID**，不要只靠文件名。例如：

```
STD-ARP4754B-001
ACT-V03-001
VOB-0001
VSR-0001
PAT-BVA-01
COV-REQ-01
CLAIM-0001
EVD-0001
```

这样未来 DBSE 文档、CSV、SysML 模型、Python 工具和生成报告之间可以共用同一套标识体系，这会直接决定你的 digital thread 能否成立。

版本管理上也建议从一开始区分三类状态：

```
working     尚在讨论
baseline    已达成研究共识
superseded  已被新基线替代
```

所以例如：

```
docs/03_dbse_workflow/lifecycle_overview.md
```

文件头可以固定写：

```
status: baseline
version: 0.1
baseline_date: 2026-08-15
owner: research
depends_on:
  - STD-ISO15288
  - STD-ARP4754B
```

这样比单纯依赖 Git commit history 更适合做系统工程研究。

对于 DCAS 当前 167 页 PPT，我不建议直接拆成 167 个 markdown 塞进仓库。更合理的是先在：

```
domains/dcas/source_mapping/
```

建立一份类似：

```
dcas_industrial_practice_map.md
```

把现有内容映射为：

```
原材料内容
→ Generic / Domain / Tool / Organization Practice
→ 对应 Framework Activity
→ 对应 Pattern
→ 是否有 normative basis
→ Gap
→ 后续处理
```

例如：

```
飞行阶段告警抑制
→ Domain Example
→ V4 Case Design
→ PAT-STM-01
→ normative basis: 待确认
→ 保留为 DCAS state-transition case
```

而：

```
TC必须关联Requirement ID
→ Generic Framework Rule
→ Traceability Model
→ normative basis: ISO 15288 / ARP4754B 待条款化
→ 提升到通用层
```

这样我们是在**重构知识**，而不是单纯搬运 PPT。

我还建议仓库根目录增加一个非常重要的 `ARCHITECTURE.md`，专门说明仓库本身的知识架构：

```
Normative Source
      ↓
Framework Rule
      ↓
DBSE Activity / Information Item
      ↓
Verification Pattern
      ↓
Domain Profile
      ↓
Concrete Case
      ↓
Model Element
      ↓
Automation Rule
```

这张关系图以后应该成为仓库的“地图”。

如果按实施优先级，**第一版仓库实际上不用创建所有文件**。我会先建立最小骨架：

```
README.md
ARCHITECTURE.md


docs/
├─ 00_overview/
├─ 01_normative_foundation/
├─ 03_dbse_workflow/
├─ 04_information_model/
└─ 05_coverage_and_evidence/


domains/
└─ dcas/


templates/


references/


archive/
```

然后第一批只写 8 个文件：

```
README.md
ARCHITECTURE.md
docs/00_overview/research_scope.md
docs/00_overview/terminology.md
docs/01_normative_foundation/standards_baseline.md
docs/03_dbse_workflow/lifecycle_overview.md
docs/04_information_model/information_items.md
domains/dcas/source_mapping/dcas_industrial_practice_map.md
```

这会是一个非常干净的 **Repository Baseline V0.1**。之后每增加一个研究成果，都能明确知道应该进入哪一层，而不会再次出现“标准、方法、测试技巧、DCAS经验、工具说明全部混在同一本指南里”的问题。