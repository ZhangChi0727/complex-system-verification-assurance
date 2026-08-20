---
title: Controlled Candidate-Source Baseline
status: reviewed
version: 1.6
baseline: post-v0.2
owner: research
last_updated: 2026-08-20
dependencies:
  - README.md
  - normative_gap_matrix.md
---

# Controlled Candidate-Source Baseline

本文件控制研究候选源、资料可得性、来源角色与研究状态。它冻结的是**变更流程**，不是标准全集：候选登记不表示条款已经研究，不得用未研究或未评审来源关闭 gap，也不表示 executable schema、certification acceptance 或跨领域适用性已经建立。

## Layering and change-control policy

| Primary layer role | 允许影响 | 禁止 |
|---|---|---|
| Generic methodological source | Generic Core / extension point 候选，经条款研究和五级分类后纳入 | 用未研究元数据形成规范性结论 |
| Domain assurance profile | Domain Profile；经抽象阶梯形成 generic 候选 | 直接写成 universal rule |
| Instance standard | 实例 Verification Basis 与评价依据 | 充当 generic 方法论来源 |
| Execution technology | 原型实现与可替换技术选择 | 定义框架语义或信息模型 |

1. Generic source 的增删替换必须关联 open gap，记录预期信息、权威性、成本、overlap 与 source-search 状态，并经 PR 评审；
2. Domain profile、instance standard、execution technology 分别由领域适用性、实例范围与平台 ADR 触发；
3. 跨层晋级只走 `../00_overview/research_scope.md` 的抽象阶梯与 consolidation §28 登记；
4. 只有 `CLAUSE STUDY REVIEWED` 的来源可进入 gap matrix 的 `Established clause basis`。`SOURCE ACQUIRED`、未完成独立评审的 clause study 或 metadata verification 均不足以关闭 gap；
5. 来源版本/状态变化时同步本表、gap matrix、standards map、roadmap 与 CHANGELOG。

## Licensed-source privacy and revision control

本仓库只登记 canonical identifier/title/edition、合法取得状态、受控相对文件名、物理页数、语言、完整性与 SHA-256。不得提交 PDF、截图、OCR dump、提取全文或可重构标准正文的大段逐字内容；不得记录许可主体、账号、订单、下载时间、水印、内部 URL 或用户绝对路径。独立评审者必须使用自己合法取得且版本/指纹匹配的原文复核 locator，review packet 只保留短释义、定位符和研究结论。

Draft、CD、DIS、FDIS 只用于 publication/revision metadata watch，不构成 clause basis。每个受监控任务在执行开始和独立评审开始时复核官方状态；若替代版已经正式发布，必须先作 retarget decision，不能静默继续旧版研究，也不能把 draft 条款混入现行正式版结论。

## Controlled candidate-source register

未由官方目录核验的字段写作 `metadata pending`。`Availability` 不含内部 URL；受版权限制全文不提交。

| Canonical ID | Document type | Title | Edition / date | Issuer | Publication status | Supersedes / relation | Availability | Primary layer role | Research trigger | Study status |
|---|---|---|---|---|---|---|---|---|---|---|
| ISO/IEC/IEEE 15288:2023 | International Standard | *System life cycle processes* | Ed. 2 / 2023-05 | ISO/IEC/IEEE | Published | 15288:2015 | Local licensed source; not committed | Generic methodological source | v0.2 foundation | CLAUSE STUDY REVIEWED |
| ISO/IEC/IEEE 24748-1:2024 | International Standard | *Life cycle management — Part 1* | Ed. 2 / 2024-03 | ISO/IEC/IEEE | Published | 24748-1:2018 | Local licensed source; not committed | Generic methodological source | v0.2 foundation | CLAUSE STUDY REVIEWED |
| ISO/IEC/IEEE 24748-2:2024 | International Standard | *Life cycle management — Part 2* | Ed. 2 / 2024-03 | ISO/IEC/IEEE | Published | 24748-2:2018 | Local licensed source; not committed | Generic methodological source | v0.2 foundation | CLAUSE STUDY REVIEWED |
| ISO/IEC/IEEE 12207:2026 | International Standard | *Software life cycle processes* | Ed. 2 / 2026-04 | ISO/IEC/IEEE | Published | ISO/IEC/IEEE 12207:2017 | Not acquired | Generic methodological source | software-lifecycle foundation / 15026-4 software view / 24748-3 compatibility | METADATA VERIFIED; SOURCE NOT ACQUIRED; CLAUSE STUDY PENDING |
| ISO/IEC/IEEE 24748-3:2020 | International Standard | *Life cycle management — Part 3: Guidelines for the application of ISO/IEC/IEEE 12207 (software life cycle processes)* | Ed. 1 / 2020-10 | ISO/IEC/IEEE | Published | Replaces ISO/IEC TR 24748-3:2011; applies ISO/IEC/IEEE 12207:2017 | Local licensed source; not committed | Generic methodological source | 12207 software-lifecycle application / 15026-4 software view | SOURCE ACQUIRED; CLAUSE STUDY PENDING; 12207:2017→2026 COMPATIBILITY OPEN |
| ISO/IEC/IEEE 24748-4:2026 | International Standard | *Life cycle management — Part 4: Systems engineering management planning* | Ed. 2 / 2026-02 | ISO/IEC/IEEE | Published | ISO/IEC/IEEE 24748-4:2016 | Local licensed source; not committed | Generic methodological source | systems engineering planning / SEMP / V0 and governance information items | SOURCE ACQUIRED; CLAUSE STUDY PENDING |
| ISO/IEC/IEEE 24748-5:2017 | International Standard | *Life cycle management — Part 5: Software development planning* | Ed. 1 / 2017-06 | ISO/IEC/IEEE | Published; confirmed 2022 | Normatively cites the then-FDIS text of ISO/IEC/IEEE 12207:2017 | Local licensed source; not committed | Generic methodological source | software development planning and planning information items / 12207-15289-16326 overlap | SOURCE ACQUIRED; CLAUSE STUDY PENDING; OVERLAP/VERSION REVIEW REQUIRED |
| ISO/IEC/IEEE 24748-6:2023 | International Standard | *Life cycle management — Part 6: System and software integration* | Ed. 1 / 2023-07 | ISO/IEC/IEEE | Published | ISO/IEC TS 24748-6:2016; normatively references 12207:2017 and 15288:2023 | Local licensed source; not committed | Generic methodological source | system/software integration and integration information items | SOURCE ACQUIRED; CLAUSE STUDY PENDING; 12207:2017→2026 COMPATIBILITY OPEN |
| ISO/IEC/IEEE 24748-8:2019 | International Standard | *Life cycle management — Part 8: Technical reviews and audits on defense programs* | Ed. 1 / 2019-02 | ISO/IEC/IEEE | Published; confirmed 2024; FDIS replacement under development | Current published edition; ISO/IEC/IEEE FDIS 24748-8 is not yet published | Not acquired | Domain assurance/application profile | defence technical reviews/gates / cross-domain abstraction candidate | METADATA VERIFIED; FORMAL REVISION WATCH; CLAUSE STUDY DEFERRED |
| ISO/IEC/IEEE 24748-10:2026 | International Standard | *Life cycle management — Part 10: Guidelines for systems engineering agility* | Ed. 1 / 2026-02 | ISO/IEC/IEEE | Published | Applies ISO/IEC/IEEE 15288 systems-engineering context; no normative references | Local licensed source; not committed | Generic methodological source | systems engineering agility / dynamic environments / iteration and re-entry | SOURCE ACQUIRED; CLAUSE STUDY PENDING; REQUIRED BEFORE ARCHITECTURE FREEZE |
| ISO/IEC/IEEE 15289:2019 | International Standard | *Content of life-cycle information items (documentation)* | Ed. 4 / 2019-07 | ISO/IEC/IEEE | Current published basis; Edition 5 CD under development | 15289:2017 | Source acquired; not committed | Generic methodological source | ISO-G07C / interoperability | SOURCE ACQUIRED; CLAUSE STUDY PENDING; FORMAL REVISION WATCH |
| ISO/IEC/IEEE 29148:2018 | International Standard | *Life cycle processes — Requirements engineering* | Ed. 2 / 2018-11 | ISO/IEC/IEEE | Current published basis; Edition 3 DIS under development | metadata pending | Local licensed source; not committed | Generic methodological source | Verification Basis / requirement quality | CLAUSE STUDY REVIEWED; 15288:2015→2023 VERSION MAPPING OPEN; FORMAL REVISION WATCH |
| ISO/IEC/IEEE 15026-1:2025 | International Standard | *Systems and software assurance — Part 1: Vocabulary and concepts* | Ed. 2 / 2025-12 | ISO/IEC/IEEE | Published | Supersedes 15026-1:2019; current target of the 15026-2 Clause 2 undated reference and Clause 3 imported terms | Local licensed source; not committed | Generic methodological source | current assurance vocabulary and Part 2/3/4 shared concepts / 15026-2 Clause 2/3 dependency | SOURCE ACQUIRED; CLAUSE STUDY PENDING |
| ISO/IEC/IEEE 15026-2:2022 | International Standard | *Systems and software assurance — Part 2: Assurance case* | Ed. 2 / 2022-11 | ISO/IEC/IEEE | Published | ISO/IEC 15026-2:2011 | Local licensed source; not committed | Generic methodological source | Claim–Argument–Evidence / RQ4 | CLAUSE STUDY REVIEWED; 15026-1:2025 TARGETED COMPATIBILITY REVIEW OPEN; 2019 DATED-REFERENCE PROVENANCE RETAINED |
| ISO/IEC/IEEE 15026-3:2023 | International Standard | *Systems and software assurance — Part 3: System integrity levels* | Ed. 3 / 2023-10 | ISO/IEC/IEEE | Published | ISO/IEC 15026-3:2015 | Local licensed source; not committed | Generic methodological source | assurance-intensity candidate | SOURCE ACQUIRED; CLAUSE STUDY PENDING |
| ISO/IEC/IEEE 15026-4:2021 | International Standard | *Systems and software assurance — Part 4: Assurance in the life cycle* | Ed. 1 / 2021-05 | ISO/IEC/IEEE | Current published; Edition 2 DIS under development | ISO/IEC 15026-4:2012 | Local licensed source; not committed | Generic methodological source | assurance lifecycle | SOURCE ACQUIRED; CLAUSE STUDY PENDING; FORMAL REVISION WATCH |
| ISO/IEC/IEEE 29119-1:2022 | International Standard | *Software testing — Part 1: General concepts* | Ed. 2 / 2022-01 | ISO/IEC/IEEE | Published | 29119-1:2013 | Local licensed source; not committed | Generic methodological source | testing concepts | SOURCE ACQUIRED; CLAUSE STUDY PENDING |
| ISO/IEC/IEEE 29119-2:2021 | International Standard | *Software testing — Part 2: Test processes* | Ed. 2 / 2021-10 | ISO/IEC/IEEE | Published | 29119-2:2013 | Local licensed source; not committed | Generic methodological source | software test processes | SOURCE ACQUIRED; CLAUSE STUDY PENDING |
| ISO/IEC/IEEE 29119-3:2021 | International Standard | *Software testing — Part 3: Test documentation* | Ed. 2 / 2021-10 | ISO/IEC/IEEE | Published | 29119-3:2013 | Local licensed source; not committed | Generic methodological source | test information items | SOURCE ACQUIRED; CLAUSE STUDY PENDING |
| ISO/IEC/IEEE 29119-4:2021 | International Standard | *Software testing — Part 4: Test techniques* | Ed. 2 / 2021-10 | ISO/IEC/IEEE | Published | 29119-4:2015 | Local licensed source; not committed | Generic methodological source | technique taxonomy | SOURCE ACQUIRED; CLAUSE STUDY PENDING |
| ISO/IEC TR 29119-11:2020 | Technical Report | *Software testing — Part 11: Guidelines on the testing of AI-based systems* | Ed. 1 / 2020-11 | ISO/IEC | Published; review closed | — | Not acquired | Instance-adjacent guidance | LLM-service instance | METADATA VERIFIED; TRIGGER NOT MET |
| ISO/IEC 9646-1:1994 | International Standard | *Conformance testing methodology and framework — Part 1: General concepts* | Ed. 2 / 1994 | ISO/IEC | Published historical basis | Paired with ITU-T X.290 family; exact equivalence/selection to be controlled | Local licensed source; not committed | Generic methodological source | ISO-G04 / conformance boundary | SOURCE ACQUIRED; PART SELECTION OPEN |
| ISO/IEC 9646-2:1994 | International Standard | *Conformance testing methodology and framework — Part 2: Abstract test suite specification* | Ed. 2 / 1994 | ISO/IEC | Published historical basis | Paired X.291-series relation to be controlled | Local licensed source; not committed | Generic methodological source | test-suite specification | SOURCE ACQUIRED; PART SELECTION OPEN |
| ISO/IEC 9646-3 / ITU-T X.292 | Standard / Recommendation | *Tree and Tabular Combined Notation / paired methodology source* | exact edition selection pending | ISO/IEC / ITU-T | Selection pending | Methodology–notation boundary source | Not acquired | Generic methodology / notation context candidate | methodology–notation–execution boundary | SOURCE NOT ACQUIRED; SELECTION OPEN |
| ISO/IEC 9646-4:1994 | International Standard | *Conformance testing methodology and framework — Part 4: Test realization* | Ed. 2 / 1994 | ISO/IEC | Published historical basis | Paired X.293-series relation to be controlled | Local licensed source; not committed | Generic methodological source | test realization | SOURCE ACQUIRED; PART SELECTION OPEN |
| ISO/IEC 9646-5:1994 | International Standard | *Conformance testing methodology and framework — Part 5: Requirements on test laboratories and clients* | Ed. 2 / 1994 | ISO/IEC | Published historical basis | Paired X.294-series relation to be controlled | Local licensed source; not committed | Generic methodological source | roles/responsibilities | SOURCE ACQUIRED; PART SELECTION OPEN |
| ISO/IEC 9646-6:1994 | International Standard | *Conformance testing methodology and framework — Part 6: Protocol profile test specification* | Ed. 2 / 1994 | ISO/IEC | Published historical basis | Protocol-profile specialization | Local licensed source; not committed | Generic methodological source with profile-limited conclusions | protocol-profile test specification | SOURCE ACQUIRED; PART SELECTION OPEN |
| ISO/IEC 9646-7:1995 | International Standard | *Conformance testing methodology and framework — Part 7: Implementation Conformance Statements* | Ed. 1 / 1995 | ISO/IEC | Published historical basis | Paired ITU-T X.296 relation to be controlled | Local licensed source; not committed | Generic methodological source | capability/applicability/conformance claims | SOURCE ACQUIRED; PART SELECTION OPEN |
| ITU-T X.290-series paired Recommendations | Recommendations | *OSI conformance testing methodology and framework* | selection pending by Recommendation | ITU-T | Metadata/selection pending | Paired with ISO/IEC 9646 parts | Not acquired as a controlled set | Generic methodological source | equivalence and locator control | PARTIAL SOURCE ACQUISITION; PART SELECTION/REMAINING ACQUISITION OPEN |
| IEEE 1012-2024 | IEEE Standard | *IEEE Standard for System, Software, and Hardware Verification and Validation* | Approved 2024 / published 2025-08 | IEEE | Active Standard | IEEE 1012-2016 | Local licensed source; not committed | Generic methodological source | V&V rigor / integrity levels | SOURCE ACQUIRED; CLAUSE STUDY PENDING |
| ISO/IEC/IEEE 24641:2023 | International Standard | *Methods and tools for model-based systems and software engineering* | Ed. 1 / 2023-05 | ISO/IEC/IEEE | Published | Uses 15288:2023 and 12207:2017 process semantics | Local licensed source; not committed | Generic methodological source | ISO-G08 / MBSE | SOURCE ACQUIRED; CLAUSE STUDY PENDING; 12207 MAPPING PROVISIONAL |
| ISO/IEC/IEEE 15939:2017 | International Standard | *Systems and software engineering — Measurement process* | Printed edition 2017-04; catalogue publication 2017-05 | ISO/IEC/IEEE | Current published basis; Edition 2 DIS under development | ISO/IEC 15939:2007; aligned with 15288:2015 | Local licensed source; not committed | Generic methodological source | evidence metrics | SOURCE ACQUIRED; CLAUSE STUDY PENDING; FORMAL REVISION WATCH; 15288:2015→2023 MAPPING OPEN |
| ISO/IEC/IEEE 16326:2019 | International Standard | *Life cycle processes — Project management* | Ed. 2 / 2019-12 | ISO/IEC/IEEE | Published; confirmed 2026 | 16326:2009; reproduces 15288:2015/12207:2017 technical-management context | Local licensed source; not committed | Generic methodological source | project information | SOURCE ACQUIRED; CLAUSE STUDY PENDING; DUAL VERSION MAPPING OPEN |
| SAE ARP4754B:2023 | Recommended Practice | *Guidelines for Development of Civil Aircraft and Systems* | Rev. B / 2023-12 | SAE | Published | ARP4754A | Local licensed source; not committed | Domain assurance profile | v0.2 profile | CLAUSE STUDY REVIEWED |
| SAE ARP4761A:2023 | Recommended Practice | *Guidelines for Conducting the Safety Assessment Process on Civil Aircraft, Systems, and Equipment* | Rev. A / 2023-12 | SAE | Published | ARP4761 | Local licensed source; not committed | Domain assurance profile | v0.2 profile | CLAUSE STUDY REVIEWED |
| RTCA DO-178C / DO-254 / DO-297 / supplements | Domain standards / supplements | metadata pending by document | metadata pending | RTCA / EUROCAE | metadata pending | metadata pending | Not acquired | Domain assurance profile | UAV/item-level scope | METADATA PENDING; TRIGGER NOT MET |
| ARINC 615A and applicable instance standards | Instance standards | metadata pending by instance | metadata pending | applicable issuers | metadata pending | metadata pending | Not acquired | Instance standard | external instance | INSTANCE-CONTROLLED; METADATA PENDING |
| ETSI TTCN-3 / SysML / SysML v2 / tools | Specifications / technologies | metadata pending by selection | metadata pending | applicable issuers | metadata pending | — | Partial local licensed sources; ETSI TTCN-3 parts present and not committed; SysML/tool sources not selected | Execution technology | platform ADR | PARTIAL SOURCE ACQUISITION; SELECTION NOT STARTED |

## Formal revision-watch register

Metadata was last verified on `2026-08-20`. Official pages control publication state; draft text is prohibited as clause evidence.

| Current published basis | Replacement stage | Official metadata | Execution-time recheck | Retarget condition | Draft-use rule |
|---|---|---|---|---|---|
| ISO/IEC/IEEE 15289:2019 | Edition 5 CD under development | https://www.iso.org/standard/94699.html | Recheck before Task 001 starts and before its independent review | If a replacement is published before extraction starts, stop and issue a retarget decision; if publication occurs during work, preserve 2019 provenance and assess migration explicitly | CD clauses shall not be extracted, cited or used as normative basis |
| ISO/IEC/IEEE 15026-4:2021 | Edition 2 DIS under development | https://www.iso.org/standard/92746.html | Recheck before Task 004 starts and before review | A published replacement requires explicit retarget/current-work disposition | DIS clauses shall not be used as normative basis |
| ISO/IEC/IEEE 29148:2018 | Edition 3 DIS under development | https://www.iso.org/standard/94091.html | Recheck before Task 021 starts | If replacement is published first, decide whether the targeted mapping closes against the reviewed 2018 study or is superseded by a separate new-edition task | DIS shall not reopen or replace the reviewed 2018 clause study |
| ISO/IEC/IEEE 15939:2017 | Edition 2 DIS under development | https://www.iso.org/standard/95100.html | Recheck before Task 019 starts and before review | If replacement is published before extraction, stop the old-edition task and issue a retarget decision | DIS clauses shall not be used as normative basis |
| ISO/IEC/IEEE 24748-8:2019 | Edition 2 FDIS under development | https://www.iso.org/standard/75405.html and https://www.iso.org/standard/91563.html | Continue Task 017 metadata-only checks | Create a new clause-study task only after formal publication, acquisition decision and trigger confirmation | FDIS shall not be acquired or analysed for normative conclusions |

## Historical / dated-reference provenance

本节保存来源真实性，不构成 candidate-source register、当前 Generic Core 规范基础或待执行研究计划。不得把 dated locator 机械替换为现行版条款号。

| Source identifier | Provenance role | Framework adoption | Controlled status |
|---|---|---|---|
| ISO/IEC/IEEE 15026-1:2019 | ISO/IEC/IEEE 15026-2:2022, 5.3.3 explicitly cites the 2019 `Claim` type; an informative uncertainty note also carries a dated 2019 reference | Not adopted as the current vocabulary version; retained only to preserve source-native provenance | DATED-REFERENCE PROVENANCE ONLY; NO STANDALONE STUDY PLANNED |

候选源登记是 discovery control，不是新颖性或规范支持证据。强创新主张必须等相关检索达到 `SOURCE SEARCH COMPLETE` 并通过 falsification review。
