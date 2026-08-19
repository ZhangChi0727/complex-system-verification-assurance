---
title: Standards Research Target Baseline
status: reviewed
version: 0.8
baseline: v0.2
owner: research
last_updated: 2026-08-19
dependencies:
  - README.md
---

# Standards Research Target Baseline

本文件冻结研究目标、资料可得性与五源 consolidation 后的 source role。`Metadata / secondary-source only` 表示当前不能从仓库记录推出条款级结论；`conceptual baseline` 不表示 source-native schema 或 certification acceptance 已建立。

## Standards layering policy

每个来源登记**恰好一个 primary layer role**，该角色决定其研究结论允许影响的框架层：

| Layer role | 允许影响 | 禁止 | 现有成员 |
|---|---|---|---|
| Generic methodological source | Generic Core / extension points（经五级分类与条款定位纪律） | — | ISO 15288、24748-1/2、15289、29148、15026-2、ISO/IEC 9646 / ITU-T X.290、24748-8 |
| Domain assurance profile | Domain Profile；其概念进入 generic 只能走抽象阶梯 | 直接写入 generic 规则 | ARP4754B、ARP4761A、DO-178C/254/297、DO-331/332/333、INCOSE/NASA handbook（实践对照） |
| Instance standard | 实例 Verification Basis 与验证依据（`docs/08_validation/`） | 进入 generic 层或充当方法论来源 | ARINC 615A、DO-160、ARINC 429/664/661/653 |
| Execution technology | 平台研究原型的实现选型 | 定义框架语义或信息模型 | ETSI TTCN-3、SysML/SysML v2、具体工具 |

规则：

1. 下方 Level 列与 layer role 的对应：A≈generic/execution（按各行 Notes 区分），B/C/D=domain profile，E=instance；
2. 双重角色必须拆分登记——例如 TTCN-3 的测试记法概念若要进方法论，须另以 9646/X.290 类 generic source 为依据，不得以执行技术身份直接进入；
3. 跨层流动只走抽象阶梯（见 `../00_overview/research_scope.md`），概念晋级登记于 five-source consolidation §28 annex；
4. 每份研究笔记必须声明来源的 layer role，结论不得越层主张；评审按 CONTRIBUTING 触点清单核查。

| Level | Standard ID | Title | Version / Revision | Organization | Research role | Availability | Study status | Notes |
|---|---|---|---|---|---|---|---|---|
| A | ISO/IEC/IEEE 15288 | *Systems and software engineering — System life cycle processes* | Second edition, 2023-05 | ISO/IEC/IEEE | Generic lifecycle/process, V&V and assurance foundation | Local licensed source — not committed | Reviewed; conceptual-baseline source | Source role frozen by five-source consolidation；see `standard_notes/iso_15288.md` |
| A | ISO/IEC/IEEE 24748-1 | *Systems and software engineering — Life cycle management — Part 1: Guidelines for life cycle management* | Second edition, 2024-03 | ISO/IEC/IEEE | Lifecycle management, stage/gate and process-view guidance | Clean official edition; local licensed source — not committed | Reviewed; conceptual-baseline guidance | Source role frozen；informative annex examples are not conformance requirements |
| A | ISO/IEC/IEEE 24748-2 | *Systems and software engineering — Life cycle management — Part 2: Guidelines for the application of ISO/IEC/IEEE 15288 (System life cycle processes)* | Second edition, 2024-03 | ISO/IEC/IEEE | Supporting application guidance for ISO/IEC/IEEE 15288 | Clean official edition; local licensed source — not committed | Reviewed; supporting source | Targeted review found minor framework delta and no new requirements; see `standard_notes/iso_24748_2_targeted_review.md` |
| A | ISO/IEC/IEEE 15289 | Title/edition to be verified before study | TBD | ISO/IEC/IEEE | Content of life-cycle information items; ISO-G07 resolution candidate | Full text not committed | **Next priority; not started** | Selected by five-source gap-priority matrix before item-level standards |
| A | ISO/IEC/IEEE 24748-8 | Title/edition to be verified before study | Referenced by ISO 24748-1:2024 | ISO/IEC/IEEE | Technical reviews and audits supporting decision gates | Full text not committed | Backlog; medium priority | Use to refine review/gate semantics after 24748-2 |
| A | ISO/IEC/IEEE 29148 | Title/metadata to be verified before study | 2018 referenced by ISO 15288:2023 | ISO/IEC/IEEE | Requirements engineering, requirement characteristics, and needs-to-requirements transformation | Cross-reference identified in ISO 15288; full text not committed | Backlog; not started | Study after ISO 24748-1, ARP4754B, and ARP4761A first round; complements ISO 15289 |
| A | ISO/IEC/IEEE 15026-2 | *Systems and software engineering — Systems and software assurance — Part 2: Assurance case*（title/edition to be verified before study） | Edition 待核对 | ISO/IEC/IEEE | Assurance case 内容与结构规范；Claim/Argument/Evidence 的对象级依据候选 | Full text not committed | Backlog; medium-high | Phase 5 / RQ4 直接输入；与 ISO 15289 之后的批次协调；layer role: generic methodological source |
| A | ISO/IEC/IEEE 29119-11 | *Software and systems engineering — Software testing — Part 11: Testing of AI-based systems*（Technical Report；title/edition to be verified） | TR，edition 待核对 | ISO/IEC/IEEE | AI 系统测试方法参考；第三实例（LLM 服务）的未来依据 | Availability to be verified | Backlog; not started | 实例启动前再研究，现阶段仅登记；layer role: instance-adjacent guidance，进入 generic 须经抽象阶梯 |
| A | ISO/IEC 9646 series / ITU-T X.290 series | *Conformance testing methodology and framework*（title/part list to be verified before study；X.290–X.296 对应系列） | 9646-1:1994 起，edition 待核对 | ISO/IEC / ITU-T | Generic conformance-testing methodology：test purpose、abstract test suite、PICS/PIXIT、verdict semantics；按抽象原则进入 generic layer，不作为单一实例专属来源 | Full text not committed | **High priority; not started** | First instance（ARINC 615A 协议符合性验证）前置依赖；与 ISO 15289 一并纳入下一轮 gap 评分；候选支撑 Oracle（ISO-G04）与 Case/Procedure schema（ISO-G07）的通用层对象依据；layer role: generic methodological source |
| A | ETSI ES 201 873 series (TTCN-3) | *Methods for Testing and Specification (MTS) — The Testing and Test Control Notation version 3*（title/edition to be verified before study） | TBD | ETSI | 测试规范与执行技术；平台研究原型的候选执行技术 | Open availability to be verified | Backlog; medium-high priority | layer role: **execution technology**——不定义框架语义/信息模型；方法论概念进入 generic 须经 9646/X.290 类 generic source，见 layering policy 规则 2 |
| A | INCOSE Systems Engineering Handbook | TBD | TBD | INCOSE | Systems engineering practice context | Metadata / secondary-source only | Not started | Edition and access TBD |
| A | NASA Systems Engineering Handbook | TBD | TBD | NASA | Public engineering guidance and comparison source | Public availability to be verified | Not started | Exact edition TBD |
| B | SAE ARP4754B / EUROCAE ED-79B | *Guidelines for Development of Civil Aircraft and Systems* / paired EUROCAE document | ARP4754B, 2023-12; ED-79B details not independently studied | SAE / EUROCAE | Civil-aircraft Development Assurance profile/governance | Official SAE source available internally — not committed | Reviewed; aviation conceptual-baseline source | Recommended practice, not regulation；source role frozen；see `standard_notes/sae_arp4754b.md` |
| B | SAE ARP4754A / EUROCAE ED-79A | TBD | Historical revision | SAE / EUROCAE | Historical/project baseline comparison | Metadata / secondary-source only | Not started | Include only when needed |
| C | SAE ARP4761A / EUROCAE ED-135 | *Guidelines for Conducting the Safety Assessment Process on Civil Aircraft, Systems, and Equipment* / paired EUROCAE document | ARP4761A, revised 2023-12; ED-135 not independently studied | SAE / EUROCAE | Civil-aircraft Safety Assessment/Safety Assurance profile | Official SAE source available internally — not committed | Reviewed; aviation conceptual-baseline source | Recommended practice, not regulation；source role frozen；Appendix Q is illustrative |
| D | RTCA DO-178C / EUROCAE ED-12C | TBD | TBD | RTCA / EUROCAE | Software item-level assurance context | Metadata / secondary-source only | Not started | Preserve item-level applicability |
| D | RTCA DO-254 / EUROCAE ED-80 | TBD | TBD | RTCA / EUROCAE | Electronic hardware item-level assurance context | Metadata / secondary-source only | Not started | Preserve item-level applicability |
| D | RTCA DO-297 / EUROCAE ED-124 | TBD | TBD | RTCA / EUROCAE | IMA roles and integration assurance context | Metadata / secondary-source only | Not started | Exact scope TBD |
| D | RTCA DO-331 | TBD | TBD | RTCA | Candidate model-based supplement research | Metadata / secondary-source only | Not started | Do not equate with system MBSE |
| D | RTCA DO-332 | TBD | TBD | RTCA | Candidate supplement research | Metadata / secondary-source only | Not started | Applicability TBD |
| D | RTCA DO-333 | TBD | TBD | RTCA | Candidate supplement research | Metadata / secondary-source only | Not started | Applicability TBD |
| E | ARINC 615A | Title/edition to be verified before study | TBD | AEEC | 首个框架验证实例的协议对象与验证依据（见 `docs/08_validation/`） | Metadata / secondary-source only | Not started; instance scoping pending | 实例标准；协议本体不进入 generic layer |
| E | DO-160; ARINC 429/664/661/653; human factors; cybersecurity | TBD by source | TBD | Applicable organizations | Domain-specific constraints and validation cases | Metadata / secondary-source only | Not started | Add only when research scope requires |

受版权限制的全文不得提交。不可公开资料只记录 `Source available internally — not committed`，且不能包含内部 URL、凭据或 confidential locator。
