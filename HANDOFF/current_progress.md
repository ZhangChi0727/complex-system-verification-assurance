---
title: Current Progress
status: working
version: 0.2
baseline: post-v0.2
owner: research
last_updated: 2026-08-19
dependencies:
  - README.md
  - ../docs/00_overview/research_baseline_v0.2.md
---

# Current Progress

- **Snapshot source:** `research-baseline/v0.2`
- **Integration status:** post-v0.2 governance increment in progress
- 最终 integration commit / main SHA 将在 consolidated PR 的第四个提交与合并完成后登记；本文件不使用中间 SHA 冒充最终快照。

## Established baseline

v0.2 是由 ISO 15288、ISO 24748-1/2、ARP4754B、ARP4761A 形成的 five-source conceptual baseline。它不宣称 executable schema、domain criteria、item-level completeness、certification acceptance 或 framework validation。

## Governance increment in progress

- standards register 已改为 **Controlled Candidate-Source Baseline**：控制来源变更过程，不封闭未来 source universe；
- gap matrix 区分 established clause basis 与 candidate-source search；未研究来源不能关闭 gap；
- candidate contribution register 把 gap、novelty hypothesis 与 validated contribution 分开；
- 外部实例引用目前使用受控临时映射。`VOB-` / `VSR-` / `COV-` 只是 candidate prefixes，stable object registry 尚未建立；
- 受控实例反馈允许进入 Framework Change Proposal 流程，但不得直接重定义框架对象。

## Source state

- `CLAUSE STUDY REVIEWED`：five-source v0.2 sources；
- `SOURCE ACQUIRED; CLAUSE STUDY PENDING`：ISO/IEC/IEEE 15289:2019；
- `SOURCE ACQUIRED; INTEGRATION PENDING`：ISO/IEC/IEEE 29148:2018、ISO/IEC/IEEE 15026-2:2022；
- 后续候选源与官方元数据状态见 `docs/01_normative_foundation/standards_baseline.md`。

## Open work

ISO-G07 information-item schema、ISO-G04 Oracle、ISO-G02B coverage、ISO-G03B sufficiency、ISO-G05 selection、ISO-G06 closure 与 ISO-G08 model evidence 继续保持可见。下一轮顺序见 `next_plan.md`。
