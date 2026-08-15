---
status: working
version: 0.1
baseline_date: 2026-08-15
owner: research
depends_on:
  - STD-ISO15288-2023
  - STD-ARP4754B
---

# Standard → Verification Objective → Activity → Information Item → Evidence

本映射用于把标准要求转化为 DBSE 可执行对象。权威结构化数据位于 [`../../data/standards/standard_verification_mapping.csv`](../../data/standards/standard_verification_mapping.csv)。

## 五列定义

| Column | Question | Completion criterion |
|---|---|---|
| Standard | 规则来自哪个标准、版本和条款？ | 标准 ID、版本、条款定位完整 |
| Verification Objective | 为什么要做、需要证明什么？ | 保留原标准语境，避免把活动误作目标 |
| Activity | 谁在何时执行什么？ | 可映射到 V0–V12 或记录 gap |
| Information Item | 活动读取、更新或产生什么受控信息？ | 对象、关键字段、状态和关系明确 |
| Evidence | 什么记录足以支持目标已达成？ | 来源、配置、审批、追溯和充分性可审计 |

## 当前候选映射

> `[候选]` 表示仅由研究大纲和官方公开范围建立，尚不能作为规范性结论。完成标准原文精读后，替换为带条款定位的正式行。

| Standard | Verification Objective | Activity | Information Item | Evidence |
|---|---|---|---|---|
| STD-ISO15288-2023（条款待确认） | [候选] 确认规定的系统或系统元素要求得到满足 | [候选] 规划验证、准备条件、实施验证、分析结果、管理异常与关闭 | Verification Plan；Verification Strategy；Verification Procedure；Result；Anomaly；Trace Record | 受控结果、分析记录、覆盖状态、异常处置与配置记录 |
| STD-ISO15288-2023（条款待确认） | [候选] 保持验证信息在生命周期内可识别、受控和可用 | [候选] 配置管理、信息管理、变更影响分析 | Baseline；Configuration Record；Change Record；Information Item Index | 基线批准记录、版本/配置标识、变更与影响记录 |
| STD-ARP4754B（条款待确认） | [候选] 验证 aircraft/system design implementation 满足其 requirements | [候选] 规划开发保证、需求/设计验证、集成验证、结果评审 | Development/Verification Plan；Requirement；Design Data；Verification Case/Procedure/Result | 经批准的验证数据、追溯记录、集成结果与符合性支持记录 |
| STD-ARP4754B（条款待确认） | [候选] 验证活动的严谨度与分配的 development assurance 相称 | [候选] 分配保证属性、确定独立性与验证策略、评审完成状态 | FDAL/IDAL attributes；Independence Record；Verification Strategy | 独立性记录、目标完成矩阵、评审与批准记录 |

## 条款精读工作流

1. 在 `standard_notes/` 记录版本、术语、条款索引和必要的短摘录/释义；
2. 每条要求先判断是通用规则、航空特有保证要求，还是项目惯例；
3. 将目标与活动分开，再识别 activity 的输入/输出信息项；
4. 判断哪些信息能构成证据，以及配置、独立性、覆盖和批准约束；
5. 双人复核或记录 reviewer 后，将 `[候选]` 提升为 baseline；
6. 由 CSV 生成矩阵、gap analysis 和后续模型输入，避免平行维护。
