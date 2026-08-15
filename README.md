# Complex System Verification Assurance Framework

面向复杂工程系统的验证保证研究仓库。项目以国际系统工程与民机开发保证规范为依据，先建立可审计的 DBSE 研究基线，再逐步形成 MBSE 元模型、规则检查与领域实例。

## 研究定位

本仓库的单一事实源覆盖：规范基线、验证目标、DBSE 活动、信息项、证据、覆盖充分性、领域实例与后续机器可读模型。通用方法论与 DCAS 实例严格分层，论文和工程教程仅作为不同发布视图。

## Repository Baseline V0.1

- 研究大纲：[`docs/00_overview/research_outline.md`](docs/00_overview/research_outline.md)
- 知识架构：[`ARCHITECTURE.md`](ARCHITECTURE.md)
- 规范基线：[`docs/01_normative_foundation/standards_baseline.md`](docs/01_normative_foundation/standards_baseline.md)
- 五列映射：[`docs/01_normative_foundation/standards_map.md`](docs/01_normative_foundation/standards_map.md)
- 机器可读映射：[`data/standards/standard_verification_mapping.csv`](data/standards/standard_verification_mapping.csv)
- DBSE 生命周期：[`docs/03_dbse_workflow/lifecycle_overview.md`](docs/03_dbse_workflow/lifecycle_overview.md)
- 信息项基线：[`docs/04_information_model/information_items.md`](docs/04_information_model/information_items.md)
- DCAS 实践分类：[`domains/dcas/source_mapping/dcas_industrial_practice_map.md`](domains/dcas/source_mapping/dcas_industrial_practice_map.md)

## 当前研究顺序

1. ISO/IEC/IEEE 15288:2023 与 SAE ARP4754B 条款级精读和五列映射；
2. 加入 ARP4761A，建立安全目标与验证严谨度关系；
3. 加入 DO-178C、DO-254、DO-297，保持系统层与 item 层语境隔离；
4. 将候选规则与 DCAS 现有实践做来源分类和 gap analysis；
5. 稳定 DBSE 信息模型后再进入 MBSE 与自动化。

## 内容与版权

仓库不保存 SAE、RTCA、ISO 等受版权保护标准的全文。仅保存合法取得材料的引用元数据、条款索引、研究笔记、派生映射和本地材料定位说明。

## License

本仓库原创内容采用 [MIT License](LICENSE) 发布。引用的第三方标准、名称与材料仍受各自权利人的版权和许可条件约束。

## 状态约定

- `working`：正在讨论或尚未完成来源核验；
- `baseline`：已评审并形成研究共识；
- `superseded`：已被后续基线替代。
