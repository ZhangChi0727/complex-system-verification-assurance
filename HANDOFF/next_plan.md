---
title: Next Plan
status: working
version: 0.1
baseline: v0.1
owner: research
last_updated: 2026-08-19
dependencies:
  - README.md
  - current_progress.md
---

# Next Plan

## Step 0 — v0.2 conceptual baseline 冻结

各受控文件 `baseline` 字段 v0.1→v0.2 晋升 + README/CHANGELOG 声明。**待 owner 确认执行**；冻结后 v0.2 边界声明（不宣称 executable schema / domain criteria / item-level completeness / certification acceptance / framework validation）生效。

## Step 1 — gap-priority 重评分 + 双轨标准研究

1. 按定位变更重跑 five-source consolidation §25 评分矩阵（`Gap relevance × expected new information × domain authority ÷ research cost`），确认双轨顺序并记录评分；
2. **ISO/IEC/IEEE 15289 全量条款精读**：先核对版本，按 ISO 15288 精读模式产出 standard note + 五列映射 + gap 更新；主线目标 ISO-G07（信息项 schema）；
3. **ISO/IEC 9646 / ITU-T X.290 概念切片 targeted review**：聚焦 test purpose / ATS / PICS-PIXIT / verdict 的对象语义，按 24748-2 targeted-review 模式起步；产出对 ISO-G04（Oracle）与 Case/Procedure schema 的通用层依据判定，并直接支撑 first instance。

## 并行线 — ARINC 615A 外部实例仓库

外部仓库基于本仓库方法论/平台框架启动实例化（PICS→Basis、test purpose→Case、verdict→Oracle 的**应用**研究；对象定义一律引用本仓库稳定 ID）；证据按锻炼矩阵维度回流。

## 后批标准（已入列、按序研究）

ISO 29148 → ISO 15026 系列（-2 优先，-1/-3/-4 同批协调）→ IEEE 1012 → 29119 核心部分 → 24641 / 24748-6 / 24748-8 → 15939 / 16326（低优先）。

## 门槛触发（不主动启动）

| 触发条件 | 启动项 |
|---|---|
| 平台原型启动（Phase 9 前） | ETSI TTCN-3 targeted review（execution technology 身份） |
| UAV FMS 实例启动 | DO-178C / DO-254 / DO-297（domain profile）；如需第二安全域：评估 IEC 61508 / ISO 26262 |
| LLM 服务实例启动 | ISO/IEC/IEEE 29119-11 |

## 延迟决策（已记录、勿重复讨论）

- `data/` 结构化迁移：ISO 15289 研究后单独立项；
- Sufficiency scope memo：Phase 5 启动时视需要建立（RQ4 条目内标注已覆盖跟踪需求）；
- 概率 oracle：高风险高回报，LLM 实例成败均报告。

## 冻结规则提醒

实例无关（generic-layer）标准列表已冻结（standards_baseline 0.9）；新增唯一通道 = §25 重评分 + 理由记录。
