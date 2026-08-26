---
title: Next Plan
status: working
version: 1.1
baseline: post-v0.2
owner: research
last_updated: 2026-08-26
dependencies:
  - README.md
  - current_progress.md
  - ../docs/01_normative_foundation/standards_baseline.md
  - ../docs/01_normative_foundation/research_tasks/README.md
---

# Next Plan

`research-baseline/v0.2` 已完成并保留为 historical conceptual checkpoint，不再重复执行冻结动作。当前 V0–V12 架构成熟度是 `OPEN-CANDIDATE`；后续研究按 open gap、dependency、candidate-source 状态和 source availability 调度，不采用不可调整的单线序列。

## Current research stop

**ISO/IEC/IEEE 15289:2019** 仍是当前第一停点：开展 information-item clause study，推进 ISO-G07/ISO-G07C。候选源扩充不表示 24748 新分册研究已经开始。

每个 work package 的完整 agent-executable 工作单见 `docs/01_normative_foundation/research_tasks/`。Task 001 是第一优先研究停点，但不是全局串行锁：未依赖其 reviewed conclusions 的 metadata verification、source acquisition、inventory 与 working/candidate research 可以并行；依赖 15289 的 final mapping/promotion、ISO-G07C closure 和信息模型冻结必须等待 Task 001 独立评审。所有 V0–V12、schema、metamodel、state machine 和 automation interface 在各自门禁前保持 working/open。

Task 001-022 已由 PR #13 合并为 `version: 0.6` work-order baseline：每项 source task 依据对应标准原文的目录和研究边界配置 Research orientation、完整 inventory 后的 hypothesis reconciliation、标准专用 research packages、公共 evidence contract、自包含 note 与 independent-review gate。该 work-order baseline 不表示任何 clause study 已开始。

## Parallel ARINC governance state

Candidate GVS Core 0.3 is defined at method merge `48dd8232b7efe6b0dba3fcb75dfc154d034d2b0b`. ARINC PR #9 is merged and released as baseline ID `RB-2026-001-v4.3` / annotated tag `v4.3` at `523d42bf03a1135b3d63a00bfb47d3b879d3927e`, while v4.2.1 remains frozen pre-framework history.

Current work order A is the method-side third-handshake Draft: independent review must verify the immutable heads, eight source hashes, 18/18 + 7 mapping, Q-01–Q-09 and the candidate `REVIEWED-COMPATIBLE-WITH-QUALIFICATION`. Work order B must not begin until A is approved and merged by ordinary merge commit. B will then acknowledge that exact method-disposition merge in a separate ARINC baseline change (`RB-2026-001-v4.3.1` baseline ID / future `v4.3.1` release tag). After both handshakes, the next separate instance step is to establish real Project Configuration values and execute the evaluation protocol; it does not close RQ8.

ISO/IEC/IEEE 15289:2019 remains the first research stop regardless of this parallel governance work.

## Dependency-driven research queue

| Work package | Dependency / ordering control | Required output |
|---|---|---|
| ISO/IEC/IEEE 15289:2019 | Current stop; source acquired | Clause study, interoperability mapping and architecture-impact disposition |
| ISO/IEC 9646 | Parts 1/2/4/5/6/7 are the complete controlled population; Part 3/ITU excluded by scope decision | Clause study of capability/applicability→test purpose→ATS/ETS→result/verdict/report/claim |
| ISO/IEC/IEEE 15026-1:2025 | Current source acquired; retain 2019 only as dated provenance | Clause study plus targeted Claim/assurance/uncertainty compatibility review; no full-edition delta |
| ISO/IEC/IEEE 15026-4:2021 | Source acquired; coordinate with Part 1:2025; downstream Part 3/12207 rows provisional | Assurance-lifecycle source-native findings and downstream closure questions |
| ISO/IEC/IEEE 12207:2026 | 154-page source acquired; source-native study may begin; 2017 historical source absent | Current software-lifecycle clause study; historical mapping rows remain `NOT DETERMINED` |
| ISO/IEC/IEEE 29119-1/-2/-3/-4 | Part 1 concepts inform Parts 2/3/4 process, documentation and technique studies | Testing/conformance/coverage impacts and dispositions |
| IEEE 1012:2024 + ISO/IEC/IEEE 15026-3:2023 | Task 010 produces IEEE source-native rigor; Task 011 depends on it and solely owns final non-equivalence matrix | Reviewed rigor/intensity findings and unique final comparison |
| ISO/IEC/IEEE 24748-4:2026 | Source acquired; reviewed 15289 required only for final information mapping; must precede synthesis | SEMP/V0 study plus provisional overlap register |
| ISO/IEC/IEEE 24748-3:2020 | Source-native extraction may start; 2017 semantic confirmation waits for the controlled historical source; current-baseline mapping/promotion waits for Task 05 independent review | Source-native guidance, informative Annex A force audit and bounded version map; architecture freeze remains with Task 022 plus the separate synthesis gate |
| ISO/IEC/IEEE 24748-5:2017 | Source acquired; Task 12 context; 16326 rows provisional | Software-planning findings; final ownership closes in Task 20 |
| ISO/IEC/IEEE 24748-6:2023 | Source acquired; reviewed 15288 context; 12207 mapping remains provisional until Task 05 | Integration findings and bounded dependency inventory |
| ISO/IEC/IEEE 24748-10:2026 | Source acquired; reviewed 15288/24748-1 context; no Task 05 hard dependency; required before freeze | Systems-engineering agility taxonomy and topology stress test |
| ISO/IEC/IEEE 24748-8 | Wait for the formally published replacement; retain defence-domain profile boundary | Revision-watch decision, then optional cross-domain abstraction study; do not study the FDIS |
| ISO/IEC/IEEE 24641:2023 | Source acquired; reviewed 15288 context; 12207 software rows provisional until Task 05 | Plan/Build/Support/Perform matrix and ISO-G08 disposition |
| ISO/IEC/IEEE 15939:2017 | Source acquired; revision recheck and bounded 15288:2015→2023 mapping | Measurement/evidence-metric disposition without universal thresholds |
| ISO/IEC/IEEE 16326:2019 | Source acquired; after Tasks 001/005/012/014; sole final planning-ownership owner | Final 24748-4/24748-5/16326 ownership and project-information disposition |
| Task 022 cross-standard synthesis | First normalize and independently review all seven legacy reviewed sources, then consume reviewed Task 001–021 datasets; retain missing/provisional/quarantined populations | RQ1–RQ7 answer drafts, RQ8 `OPEN` validation-readiness/instance handoff, innovation falsification ledger, conflict/term/ownership matrices and architecture proposals |
| Architecture synthesis / controlled-freeze gate | Planned cohort studied or explicitly deferred; all impacts disposed; conflicts/migrations/gaps reviewed independently | First reach at most `REVIEWED-PROVISIONAL`; a separate formal freeze/version/migration review is required for `CONTROLLED-BASELINE`; orthogonal instance state `INSTANCE-EXERCISED` does not promote Architecture maturity; `VALIDATED-BASELINE`/RQ8 closure require all three instances and cross-instance synthesis |
| Executable information schema | Architecture synthesis gate and relevant schema dependencies satisfied | Executable schema candidate |
| Versioned object registry | Stable identity/version/compatibility rules available | Controlled registry and migration rules |
| Platform reference architecture | Information model sufficiently stable | Replaceable technology decisions |
| External-instance integration | Work order A independent review/merge, then separate ARINC work order B acknowledgement; stable registry remains gated | Qualified compatibility disposition only; then establish Project Configuration and execute the evaluation protocol in another PR |

ISO 29148:2018 与 ISO 15026-2:2022 的现有研究已完成独立评审修正；它们不会因评审完成而关闭上述依赖。ISO/IEC/IEEE 15026-1:2019 不再是独立 clause-study 对象或待研究标准。

所有 cross-source 工作遵守两阶段规则：较早任务交付 source-native inventory、provisional crosswalk 和 downstream closure questions；缺少 12207:2017、15288:2015 或 24748-4:2016 时不得从现行版倒推，受影响行写 `NOT DETERMINED`。只有相关来源均完成独立评审后，由唯一指定的 later owner 或 Task 022/architecture synthesis 形成 final disposition。Task 022 不能替代 literature/patent/practice novelty search。

## Triggered work

| Trigger | Work |
|---|---|
| optional realization ADR | TTCN-3 / modelling technology selection after information-model gates |
| UAV item-level scope | DO-178C / DO-254 / DO-297 and applicable supplements |
| LLM-service instance | AI testing guidance current-source assessment |

任何新增候选源都必须按 Controlled Candidate-Source Baseline 登记；候选登记不构成 normative support 或 novelty proof。
