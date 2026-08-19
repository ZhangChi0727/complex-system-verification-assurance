---
title: Current Progress
status: working
version: 0.1
baseline: v0.1
owner: research
last_updated: 2026-08-19
dependencies:
  - README.md
---

# Current Progress（截至 2026-08-19，main @ 986cc54）

## 研究基线状态

- **v0.1 已冻结**：研究范围、问题、术语、路线、仓库知识架构；
- **v0.2 conceptual baseline：CONDITIONALLY READY，冻结动作待执行**——五源 consolidation 已完成（source roles、V0–V12 ontology、Generic/Profile 边界、evidence/change/gate semantics、21 项 gap 全部 disposition）；待做的只是各文件 `baseline` 字段 v0.1→v0.2 晋升（owner 确认后执行）。

## 研究定位（已于 PR #6 确立）

- 三层产出链：产品无关 Verification Methodology → Model-Based Verification Architecture → 非产品化 Verification Platform 研究原型（不产品化）；
- DCAS = Industrial Practice Knowledge Source（非验证实例）；验证实例 = **ARINC 615A 协议符合性验证（first，外部仓库执行）**、无人机飞管系统验证、LLM 服务可靠性与性能验证（planned）；
- 方法论与实例彻底解耦（解耦契约见 `docs/00_overview/innovation_statement.md` §4）：本仓库细化到 implementation framework 层，实例执行在外部仓库；
- 标准研究双面性：标准"说了什么"= 构建依据（约束登记）；"没说什么"= 创新空间（创新登记）。

## 标准研究状态

- **已 reviewed + consolidated（五源）**：ISO 15288:2023、ISO 24748-1/2:2024、SAE ARP4754B、SAE ARP4761A；各源 clause-level note + 内部/外部评审 provenance 齐备；
- **下一轮（双轨，重评分后启动）**：ISO/IEC/IEEE 15289 全量条款精读（ISO-G07 主线）+ ISO/IEC 9646 / ITU-T X.290 概念切片 targeted review（first-instance 前置，候选支撑 ISO-G04 Oracle 与 Case/Procedure schema）；
- **实例无关（generic-layer）标准列表已冻结**（standards_baseline 0.9）：IEEE 1012、24641、24748-6、15939、16326 已从 24748-1 note follow-up register 同步入列；15026 系列其余部分与 29119 核心部分补齐；新增只走 §25 gap-priority 重评分；
- 领域/实例层来源按需求门槛触发（TTCN-3 待平台启动；DO 系列待 UAV 实例；29119-11 待 LLM 实例），不违反冻结。

## 治理机制（已落地）

| 机制 | 位置 |
|---|---|
| 对象 provenance 登记（PROMOTE ≠ source-native） | five-source consolidation §28 annex |
| Definition ownership（annex 唯一权威） | ARCHITECTURE.md |
| 标准分层管理（四种 layer role + 越层规则） | standards_baseline.md layering policy |
| 标准研究触点清单（9 步） | CONTRIBUTING.md |
| 抽象阶梯（profile→generic 唯一通道） | research_scope.md |
| 创新主张登记 + 工作边界 + 解耦契约 | innovation_statement.md |
| 实例 × 框架元素锻炼矩阵 | docs/08_validation/README.md |

## 主要开放项

- RQ4 充分性推理语义（Phase 5，UAV/LLM 实例主锻炼面）；
- Oracle 对象依据（9646 概念切片研究中）；
- 信息项 schema（ISO 15289 研究后，ISO-G07）；
- V10 选择算法、V12 closure 状态机（ISO-G05/G06 继承者）；
- 平台原型（Phase 8/9，信息模型稳定后）。

## 实例进展

- ARINC 615A：外部实例仓库（`ZhangChi0727/arinc-615a-conformance`）计划全面基于本仓库方法论与平台框架开展实例研究；本仓库侧待办 = 9646 概念切片研究为其提供 generic 依据；
- UAV FMS / LLM 服务：仅登记于实例策略，未启动。
