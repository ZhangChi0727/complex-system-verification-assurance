---
title: Current Progress
status: working
version: 0.8
baseline: post-v0.2
owner: research
last_updated: 2026-08-20
dependencies:
  - README.md
  - ../docs/00_overview/research_baseline_v0.2.md
---

# Current Progress

- **Snapshot source:** `research-baseline/v0.2`
- **Integration status:** PR #9 is merged; external re-review findings F-01/F-02 are externally confirmed and closed
- **Integrated research head before this final review commit:** `40018f996c746034092a7add81d1ba5f2d21349c`
- **PR #9 reviewed head:** `3359927286a39411ccb0e5f6dd34883702eb3ece`
- **PR #9 merge commit / synchronized main:** `658e3cfcee1d66147c6cbf2d048fc1d46a846f14`
- **Superseded PRs:** PR #7 and PR #8 are closed as superseded; neither was merged directly
- **Repository topology:** `main` is the sole persistent remote branch; review branches are temporary governance artifacts and are deleted after merge
- **Repository maturity:** `Normative-foundation research late stage / architecture OPEN-CANDIDATE`

## Established baseline

v0.2 是由 ISO 15288、ISO 24748-1/2、ARP4754B、ARP4761A 形成的 five-source conceptual baseline。它不宣称 executable schema、domain criteria、item-level completeness、certification acceptance 或 framework validation。

## Established post-v0.2 governance increment

- standards register 已改为 **Controlled Candidate-Source Baseline**：控制来源变更过程，不封闭未来 source universe；
- gap matrix 区分 established clause basis 与 candidate-source search；未研究来源不能关闭 gap；
- candidate contribution register 把 gap、novelty hypothesis 与 validated contribution 分开；
- 外部实例引用目前使用受控临时映射。`VOB-` / `VSR-` / `COV-` 只是 candidate prefixes，stable object registry 尚未建立；
- 受控实例反馈允许进入 Framework Change Proposal 流程，但不得直接重定义框架对象。
- 本轮只调整 V0–V12 开放治理、architecture-impact disposition 和 24748 candidate-source planning；没有形成新增条款结论、established basis、gap closure、schema 或 certification-readiness claim。

## Source state

- `CLAUSE STUDY REVIEWED`：five-source v0.2 sources；
- `SOURCE ACQUIRED; CLAUSE STUDY PENDING`：ISO/IEC/IEEE 15289:2019、ISO/IEC/IEEE 15026-1:2025；
- `CLAUSE STUDY REVIEWED; OPEN DEPENDENCIES`：ISO/IEC/IEEE 29148:2018（15288:2015→2023 mapping open）、ISO/IEC/IEEE 15026-2:2022（15026-1:2025 Clause 2/3 dependency 与 Claim/assurance/uncertainty targeted compatibility review open）；
- `DATED-REFERENCE PROVENANCE ONLY; NO STANDALONE STUDY PLANNED`：ISO/IEC/IEEE 15026-1:2019，仅忠实记录 15026-2:2022, 5.3.3 的 Claim type 及相关 uncertainty 说明来源；
- `PLANNED; NOT STARTED`：ISO/IEC 9646 / ITU-T X.290 targeted study；
- `METADATA VERIFIED; SOURCE NOT ACQUIRED; CLAUSE STUDY PENDING`：ISO/IEC/IEEE 12207:2026；
- `METADATA VERIFIED; CLAUSE STUDY PENDING`：ISO/IEC/IEEE 24748-4:2026、24748-6:2023；
- `METADATA VERIFIED; CLAUSE STUDY PENDING; 12207:2017→2026 COMPATIBILITY OPEN`：ISO/IEC/IEEE 24748-3:2020；
- `METADATA VERIFIED; CLAUSE STUDY PENDING; OVERLAP REVIEW REQUIRED`：ISO/IEC/IEEE 24748-5:2017；
- `METADATA VERIFIED; CLAUSE STUDY PENDING; REQUIRED BEFORE ARCHITECTURE FREEZE`：ISO/IEC/IEEE 24748-10:2026；
- `METADATA VERIFIED; FORMAL REVISION WATCH; CLAUSE STUDY DEFERRED`：ISO/IEC/IEEE 24748-8:2019（defence-domain profile candidate；FDIS 不作为规范依据）；
- 后续候选源与官方元数据状态见 `docs/01_normative_foundation/standards_baseline.md`。

## Open work

ISO-G07 information-item schema、ISO-G04 Oracle、ISO-G02B coverage、ISO-G03B sufficiency、ISO-G05 selection、ISO-G06 closure 与 ISO-G08 model evidence 继续保持可见。F-01 已按权威矩阵统一为 `REQ-G01` Requirement/Set identity and lifecycle schema、`REQ-G02` Verification Criterion placement/cardinality、`ISO-G07C` ISO 15289 interoperability；F-02 已把 ISO-G07C 状态统一为 `SOURCE ACQUIRED; CLAUSE STUDY PENDING`。两项 finding 均已通过外部复审并关闭。当前研究停点转入 **ISO/IEC/IEEE 15289:2019 条款级研究**，用于精化 information-item interoperability 与 document/record mapping；尚未开始的条款结论不得提前写入 established clause basis。

Executable metamodel/schema、versioned object registry、platform implementation 和 ARINC 615A/UAV/LLM instance results 均未建立。仓库不声称 certification-ready、evidence sufficiency solved 或 framework validated。
