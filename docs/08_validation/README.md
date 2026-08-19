---
title: Framework Validation Workspace
status: working
version: 0.2
baseline: v0.2
owner: research
last_updated: 2026-08-19
dependencies:
  - ../00_overview/research_scope.md
  - ../00_overview/research_questions.md
---

# Framework Validation Workspace

本目录管理框架验证实例与验证策略，回答 RQ8：framework 的 completeness、traceability、repeatability、scalability 与 reusability 是否成立。评价维度还包括 Reviewability、Change Impact Detection、Coverage Explicitness、Evidence Quality 与 Automation Potential。

实例只检验框架，不反向污染 generic methodology（见 research_scope 抽象边界与抽象阶梯）。

## Validation instances

| Instance | Verification type | Status | Primary thesis contribution |
|---|---|---|---|
| ARINC 615A 协议符合性验证 | 确定性、规范驱动的 conformance verification | **First instance**（scoping 待启动） | 检验 Basis/Obligation → Case/Procedure → Oracle/verdict → 平台执行链 |
| 无人机飞管系统验证 | 安全驱动 rigor 的系统验证 | Planned | 检验 assurance constraints、typed independence、coverage、change impact |
| LLM 服务可靠性与性能验证 | 概率性、弱 oracle 的服务验证 | Planned | 检验 sufficiency、evidence/argument 与 coverage 定义边界 |

**DCAS 不作为验证实例。** DCAS 定位为 industrial-practice knowledge source：其模式经抽象阶梯（profile 实践 → 候选 pattern → generic pattern → 跨域实例检验）进入方法论，见 `domains/dcas/` 与 Phase 7。

## Instance × framework-element exercise matrix

读法：H = 强锻炼，M = 中等，L = 弱/边界。矩阵用于显式管理每个实例对论文主张的贡献；**单一实例通过不得表述为框架整体成立**。

| Framework element | ARINC 615A | UAV FMS | LLM service |
|---|---|---|---|
| V1 Verification Basis / Obligation | H（协议条款/PICS 类声明 → typed basis） | M | L（basis 需构造） |
| V2 Requirement verifiability | H | M | L |
| V3 Verification Strategy | H | H | M |
| V4 Verification Case Design | H（test purpose 类） | M | M |
| V5 Verification Procedure | H（可执行测试套） | M | M |
| V6 Verification Readiness gate | M | M | L |
| V7/V8 Execution / Result Evaluation | H（verdict 语义） | M | M |
| V9/V10 Anomaly / Change Impact | M | H | M |
| V11 Coverage | M（条款覆盖） | H | L（覆盖定义本身受挑战） |
| V11 Sufficiency（RQ4） | L | H | H |
| Assurance / Independence constraints | L | H | M |
| Evidence / Argument / Claim | M | H | H |
| Oracle（ISO-G04） | H（协议预期行为） | M | L（开放研究问题） |
| MBSE 模型 / 平台执行链 | H | M | M |

总体分工：ARINC 615A 主要锻炼框架的"设计—执行"下半链，UAV FMS 锻炼"assurance—充分性"上半链，LLM 服务冲击 coverage/sufficiency/oracle 的定义边界。三实例合起来覆盖论文主张全集。

## 实例与标准的关系

实例相关标准按抽象原则处理（见 research_scope 抽象阶梯）：符合性测试方法论（ISO/IEC 9646 / ITU-T X.290 系列、ETSI TTCN-3）作为 **generic-layer 方法论来源**研究并向上抽象，不作为 ARINC 615A 专属资产；ARINC 615A 本体保持 Level E 实例标准。详见 `../01_normative_foundation/standards_baseline.md`。

## Status

- working：实例定位与锻炼矩阵（本文件）；
- planned：ARINC 615A 实例 scoping note——研究 PICS/PIXIT → Verification Basis、test purpose → Verification Case、verdict → Oracle/Result 的映射，并检验符合性测试方法论对 ISO-G04/ISO-G07 的支撑；
- 不声称 framework 已通过任何实例验证。
