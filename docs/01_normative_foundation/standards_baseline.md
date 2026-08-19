---
title: Controlled Candidate-Source Baseline
status: reviewed
version: 1.1
baseline: post-v0.2
owner: research
last_updated: 2026-08-19
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

## Controlled candidate-source register

未由官方目录核验的字段写作 `metadata pending`。`Availability` 不含内部 URL；受版权限制全文不提交。

| Canonical ID | Document type | Title | Edition / date | Issuer | Publication status | Supersedes / relation | Availability | Primary layer role | Research trigger | Study status |
|---|---|---|---|---|---|---|---|---|---|---|
| ISO/IEC/IEEE 15288:2023 | International Standard | *System life cycle processes* | Ed. 2 / 2023-05 | ISO/IEC/IEEE | Published | 15288:2015 | Local licensed source; not committed | Generic methodological source | v0.2 foundation | CLAUSE STUDY REVIEWED |
| ISO/IEC/IEEE 24748-1:2024 | International Standard | *Life cycle management — Part 1* | Ed. 2 / 2024-03 | ISO/IEC/IEEE | Published | 24748-1:2018 | Local licensed source; not committed | Generic methodological source | v0.2 foundation | CLAUSE STUDY REVIEWED |
| ISO/IEC/IEEE 24748-2:2024 | International Standard | *Life cycle management — Part 2* | Ed. 2 / 2024-03 | ISO/IEC/IEEE | Published | 24748-2:2018 | Local licensed source; not committed | Generic methodological source | v0.2 foundation | CLAUSE STUDY REVIEWED |
| ISO/IEC/IEEE 15289:2019 | International Standard | *Content of life-cycle information items (documentation)* | Ed. 4 / 2019-07 | ISO/IEC/IEEE | Published; revision under development | 15289:2017 | Source acquired; not committed | Generic methodological source | ISO-G07C / interoperability | SOURCE ACQUIRED; CLAUSE STUDY PENDING |
| ISO/IEC/IEEE 29148:2018 | International Standard | *Life cycle processes — Requirements engineering* | Ed. 2 / 2018-11 | ISO/IEC/IEEE | Published; current-status recheck pending | metadata pending | Local licensed source; not committed | Generic methodological source | Verification Basis / requirement quality | CLAUSE STUDY REVIEWED; 15288:2015→2023 VERSION MAPPING OPEN |
| ISO/IEC/IEEE 15026-1:2025 | International Standard | *Systems and software assurance — Part 1: Vocabulary and concepts* | Ed. 2 / 2025-12 | ISO/IEC/IEEE | Published | Supersedes 15026-1:2019; current target of the 15026-2 Clause 2 undated reference and Clause 3 imported terms | Not acquired | Generic methodological source | assurance vocabulary / delta | METADATA VERIFIED; CLAUSE STUDY PENDING |
| ISO/IEC/IEEE 15026-1:2019 | International Standard | *Systems and software assurance — Part 1: Concepts and vocabulary* | Ed. 1 / 2019-03 | ISO/IEC/IEEE | Withdrawn | Replaced by 15026-1:2025; explicit dated Claim-type dependency in 15026-2:2022, 5.3.3 | Not acquired | Generic methodological source | dependency and 2019→2025 delta | METADATA VERIFIED; CLAUSE STUDY PENDING |
| ISO/IEC/IEEE 15026-2:2022 | International Standard | *Systems and software assurance — Part 2: Assurance case* | Ed. 2 / 2022-11 | ISO/IEC/IEEE | Published | ISO/IEC 15026-2:2011 | Local licensed source; not committed | Generic methodological source | Claim–Argument–Evidence / RQ4 | CLAUSE STUDY REVIEWED; 15026-1:2025 UNDATED-REFERENCE AND 15026-1:2019 DATED CLAIM-TYPE DEPENDENCIES OPEN |
| ISO/IEC/IEEE 15026-3:2023 | International Standard | *Systems and software assurance — Part 3: System integrity levels* | Ed. 3 / 2023-10 | ISO/IEC/IEEE | Published | ISO/IEC 15026-3:2015 | Not acquired | Generic methodological source | assurance-intensity candidate | METADATA VERIFIED; CLAUSE STUDY PENDING |
| ISO/IEC/IEEE 15026-4:2021 | International Standard | *Systems and software assurance — Part 4: Assurance in the life cycle* | Ed. 1 / 2021-05 | ISO/IEC/IEEE | Current published; DIS revision is not a published replacement | ISO/IEC 15026-4:2012 | Not acquired | Generic methodological source | assurance lifecycle | METADATA VERIFIED; CLAUSE STUDY PENDING |
| ISO/IEC/IEEE 29119-1:2022 | International Standard | *Software testing — Part 1: General concepts* | Ed. 2 / 2022-01 | ISO/IEC/IEEE | Published | 29119-1:2013 | Not acquired | Generic methodological source | testing concepts | METADATA VERIFIED; CLAUSE STUDY PENDING |
| ISO/IEC/IEEE 29119-2:2021 | International Standard | *Software testing — Part 2: Test processes* | Ed. 2 / 2021-10 | ISO/IEC/IEEE | Published | 29119-2:2013 | Not acquired | Generic methodological source | software test processes | METADATA VERIFIED; CLAUSE STUDY PENDING |
| ISO/IEC/IEEE 29119-3:2021 | International Standard | *Software testing — Part 3: Test documentation* | Ed. 2 / 2021-10 | ISO/IEC/IEEE | Published | 29119-3:2013 | Not acquired | Generic methodological source | test information items | METADATA VERIFIED; CLAUSE STUDY PENDING |
| ISO/IEC/IEEE 29119-4:2021 | International Standard | *Software testing — Part 4: Test techniques* | Ed. 2 / 2021-10 | ISO/IEC/IEEE | Published | 29119-4:2015 | Not acquired | Generic methodological source | technique taxonomy | METADATA VERIFIED; CLAUSE STUDY PENDING |
| ISO/IEC TR 29119-11:2020 | Technical Report | *Software testing — Part 11: Guidelines on the testing of AI-based systems* | Ed. 1 / 2020-11 | ISO/IEC | Published; review closed | — | Not acquired | Instance-adjacent guidance | LLM-service instance | METADATA VERIFIED; TRIGGER NOT MET |
| ISO/IEC 9646 series / ITU-T X.290 series | Standards / Recommendations | *Conformance testing methodology and framework* | metadata pending by part | ISO/IEC / ITU-T | metadata pending | paired traditions | Not acquired | Generic methodological source | ISO-G04 / conformance instance | PLANNED; METADATA PENDING |
| IEEE 1012-2024 | IEEE Standard | *IEEE Standard for System, Software, and Hardware Verification and Validation* | Approved 2024 / published 2025-08 | IEEE | Active Standard | IEEE 1012-2016 | Not acquired | Generic methodological source | V&V rigor / integrity levels | METADATA VERIFIED; CLAUSE STUDY PENDING |
| ISO/IEC/IEEE 24641:2023 | International Standard | *Methods and tools for model-based systems and software engineering* | Ed. 1 / 2023-05 | ISO/IEC/IEEE | Published | — | Not acquired | Generic methodological source | ISO-G08 / MBSE | METADATA VERIFIED; CLAUSE STUDY PENDING |
| ISO/IEC/IEEE 24748-6:2023 | International Standard | *Life cycle management — Part 6: System and software integration* | Ed. 1 / 2023-07 | ISO/IEC/IEEE | Published | ISO/IEC TS 24748-6:2016 | Not acquired | Generic methodological source | integration information items | METADATA VERIFIED; CLAUSE STUDY PENDING |
| ISO/IEC/IEEE 15939:2017 | International Standard | *Systems and software engineering — Measurement process* | Ed. 1 / 2017-05 | ISO/IEC/IEEE | Published; confirmed 2022 | ISO/IEC 15939:2007 | Not acquired | Generic methodological source | evidence metrics | METADATA VERIFIED; CLAUSE STUDY PENDING |
| ISO/IEC/IEEE 16326:2019 | International Standard | *Life cycle processes — Project management* | Ed. 2 / 2019-12 | ISO/IEC/IEEE | Published; confirmed 2026 | 16326:2009 | Not acquired | Generic methodological source | project information | METADATA VERIFIED; CLAUSE STUDY PENDING |
| ISO/IEC/IEEE 24748-8 | metadata pending | metadata pending | metadata pending | ISO/IEC/IEEE | metadata pending | referenced by 24748-1:2024 | Not acquired | Generic methodological source | review/gate semantics | METADATA PENDING |
| SAE ARP4754B:2023 | Recommended Practice | *Guidelines for Development of Civil Aircraft and Systems* | Rev. B / 2023-12 | SAE | Published | ARP4754A | Local licensed source; not committed | Domain assurance profile | v0.2 profile | CLAUSE STUDY REVIEWED |
| SAE ARP4761A:2023 | Recommended Practice | *Guidelines for Conducting the Safety Assessment Process on Civil Aircraft, Systems, and Equipment* | Rev. A / 2023-12 | SAE | Published | ARP4761 | Local licensed source; not committed | Domain assurance profile | v0.2 profile | CLAUSE STUDY REVIEWED |
| RTCA DO-178C / DO-254 / DO-297 / supplements | Domain standards / supplements | metadata pending by document | metadata pending | RTCA / EUROCAE | metadata pending | metadata pending | Not acquired | Domain assurance profile | UAV/item-level scope | METADATA PENDING; TRIGGER NOT MET |
| ARINC 615A and applicable instance standards | Instance standards | metadata pending by instance | metadata pending | applicable issuers | metadata pending | metadata pending | Not acquired | Instance standard | external instance | INSTANCE-CONTROLLED; METADATA PENDING |
| ETSI TTCN-3 / SysML / SysML v2 / tools | Specifications / technologies | metadata pending by selection | metadata pending | applicable issuers | metadata pending | — | Not acquired | Execution technology | platform ADR | SELECTION NOT STARTED |

候选源登记是 discovery control，不是新颖性或规范支持证据。强创新主张必须等相关检索达到 `SOURCE SEARCH COMPLETE` 并通过 falsification review。
