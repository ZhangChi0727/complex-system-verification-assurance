---
title: Next Plan
status: working
version: 0.4
baseline: post-v0.2
owner: research
last_updated: 2026-08-20
dependencies:
  - README.md
  - current_progress.md
  - ../docs/01_normative_foundation/standards_baseline.md
---

# Next Plan

`research-baseline/v0.2` 已完成并保留为 historical conceptual checkpoint，不再重复执行冻结动作。当前 V0–V12 架构成熟度是 `OPEN-CANDIDATE`；后续研究按 open gap、dependency、candidate-source 状态和 source availability 调度，不采用不可调整的单线序列。

## Current research stop

**ISO/IEC/IEEE 15289:2019** 仍是当前第一停点：开展 information-item clause study，推进 ISO-G07/ISO-G07C。候选源扩充不表示 24748 新分册研究已经开始。

## Dependency-driven research queue

| Work package | Dependency / ordering control | Required output |
|---|---|---|
| ISO/IEC/IEEE 15289:2019 | Current stop; source acquired | Clause study, interoperability mapping and architecture-impact disposition |
| ISO/IEC 9646 / ITU-T X.290 | Prioritize against ISO-G04 and first-instance needs | Targeted conformance-testing study and impact disposition |
| ISO/IEC/IEEE 15026-1:2025 | Current source acquired; retain 2019 only as dated provenance | Clause study plus targeted Claim/assurance/uncertainty compatibility review; no full-edition delta |
| ISO/IEC/IEEE 15026-4:2021 | Coordinate with the 15026-1:2025 vocabulary baseline | Assurance-lifecycle findings and software-view dependency map |
| ISO/IEC/IEEE 12207:2026 | Foundation before 24748-3; coordinate with 15026-4 software view | Software-lifecycle clause study and 2017→2026 dependency context |
| ISO/IEC/IEEE 29119-1/-2/-3/-4 | Part 1 concepts inform Parts 2/3/4 process, documentation and technique studies | Testing/conformance/coverage impacts and dispositions |
| IEEE 1012:2024 + ISO/IEC/IEEE 15026-3:2023 | Coordinate V&V rigor and assurance-intensity questions | Rigor/intensity findings and impact dispositions |
| ISO/IEC/IEEE 24748-4:2026 | Must precede final architecture synthesis | SEMP/V0/planning information-item study and overlap disposition |
| ISO/IEC/IEEE 24748-3:2020 | Start after the 12207:2026 foundation; retain 12207:2017→2026 compatibility as explicit work | Software-lifecycle application impact disposition |
| ISO/IEC/IEEE 24748-5:2017 | Perform 12207/15289/16326 overlap review before promotion decisions | Software-planning information-item impact disposition |
| ISO/IEC/IEEE 24748-6:2023 | Coordinate with 15289 and integration information-item scope | Integration impact disposition |
| ISO/IEC/IEEE 24748-10:2026 | Required before architecture freeze | Iteration/re-entry/tailoring/dynamic-environment impact disposition; no reduction of evidence or gate obligations |
| ISO/IEC/IEEE 24748-8 | Wait for the formally published replacement; retain defence-domain profile boundary | Revision-watch decision, then optional cross-domain abstraction study; do not study the FDIS |
| Architecture synthesis / controlled-freeze gate | Planned cohort studied or explicitly deferred; all impacts disposed; conflicts/migrations/gaps reviewed independently | At most `REVIEWED-PROVISIONAL`; no direct jump to `CONTROLLED-BASELINE` |
| Executable information schema | Architecture synthesis gate and relevant schema dependencies satisfied | Executable schema candidate |
| Versioned object registry | Stable identity/version/compatibility rules available | Controlled registry and migration rules |
| Platform reference architecture | Information model sufficiently stable | Replaceable technology decisions |
| External-instance integration | Registry mappings and framework-change governance available | Controlled instance feedback and cross-instance validation |

ISO 29148:2018 与 ISO 15026-2:2022 的现有研究已完成独立评审修正；它们不会因评审完成而关闭上述依赖。ISO/IEC/IEEE 15026-1:2019 不再是独立 clause-study 对象或待研究标准。

## Triggered work

| Trigger | Work |
|---|---|
| platform prototype ADR | TTCN-3 / modelling technology selection |
| UAV item-level scope | DO-178C / DO-254 / DO-297 and applicable supplements |
| LLM-service instance | AI testing guidance current-source assessment |

任何新增候选源都必须按 Controlled Candidate-Source Baseline 登记；候选登记不构成 normative support 或 novelty proof。
