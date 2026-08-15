---
status: baseline
version: 0.1
baseline_date: 2026-08-15
owner: research
---

# Repository Knowledge Architecture

```text
Normative Source
      ↓
Verification Objective
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
Model Element / Automation Rule
      ↓
Controlled Evidence → Compliance Claim
```

## 分层边界

- `docs/`：产品无关的方法论与受控研究基线。
- `domains/`：DCAS、ARINC 615A 等领域 profile 与实例。
- `data/`：可被脚本、表格或模型消费的机器可读研究数据。
- `templates/`：DBSE 活动和信息项模板。
- `models/`：后续 MBSE 元模型、视图与交换表示。
- `tools/`：一致性、覆盖、影响分析与报告生成工具。
- `references/`：引用元数据、结构决策、阅读索引与不公开材料定位说明；不存标准全文。
- `publications/`：论文和教程发布视图，不复制权威定义。
- `archive/`：被替代但仍需保留的研究资产。

## 单一事实源

规范结论以 `docs/01_normative_foundation/` 为权威入口，结构化行以 `data/standards/standard_verification_mapping.csv` 为权威数据源。论文、教程、模型与报告必须引用这些对象，不维护平行定义。

## 分类判据

若某规则在替换为非航空复杂系统后仍成立，则归入通用框架；依赖航空适航、IMA、总线、显示或组织惯例的内容分别归入航空保证层、领域 profile 或项目惯例层。
