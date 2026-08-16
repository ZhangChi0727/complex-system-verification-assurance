---
title: Standards Research Target Baseline
status: reviewed
version: 0.7
baseline: v0.1
owner: research
last_updated: 2026-08-16
dependencies:
  - README.md
---

# Standards Research Target Baseline

本文件冻结研究目标、资料可得性与五源 consolidation 后的 source role。`Metadata / secondary-source only` 表示当前不能从仓库记录推出条款级结论；`conceptual baseline` 不表示 source-native schema 或 certification acceptance 已建立。

| Level | Standard ID | Title | Version / Revision | Organization | Research role | Availability | Study status | Notes |
|---|---|---|---|---|---|---|---|---|
| A | ISO/IEC/IEEE 15288 | *Systems and software engineering — System life cycle processes* | Second edition, 2023-05 | ISO/IEC/IEEE | Generic lifecycle/process, V&V and assurance foundation | Local licensed source — not committed | Reviewed; conceptual-baseline source | Source role frozen by five-source consolidation；see `standard_notes/iso_15288.md` |
| A | ISO/IEC/IEEE 24748-1 | *Systems and software engineering — Life cycle management — Part 1: Guidelines for life cycle management* | Second edition, 2024-03 | ISO/IEC/IEEE | Lifecycle management, stage/gate and process-view guidance | Clean official edition; local licensed source — not committed | Reviewed; conceptual-baseline guidance | Source role frozen；informative annex examples are not conformance requirements |
| A | ISO/IEC/IEEE 24748-2 | *Systems and software engineering — Life cycle management — Part 2: Guidelines for the application of ISO/IEC/IEEE 15288 (System life cycle processes)* | Second edition, 2024-03 | ISO/IEC/IEEE | Supporting application guidance for ISO/IEC/IEEE 15288 | Clean official edition; local licensed source — not committed | Reviewed; supporting source | Targeted review found minor framework delta and no new requirements; see `standard_notes/iso_24748_2_targeted_review.md` |
| A | ISO/IEC/IEEE 15289 | Title/edition to be verified before study | TBD | ISO/IEC/IEEE | Content of life-cycle information items; ISO-G07 resolution candidate | Full text not committed | **Next priority; not started** | Selected by five-source gap-priority matrix before item-level standards |
| A | ISO/IEC/IEEE 24748-8 | Title/edition to be verified before study | Referenced by ISO 24748-1:2024 | ISO/IEC/IEEE | Technical reviews and audits supporting decision gates | Full text not committed | Backlog; medium priority | Use to refine review/gate semantics after 24748-2 |
| A | ISO/IEC/IEEE 29148 | Title/metadata to be verified before study | 2018 referenced by ISO 15288:2023 | ISO/IEC/IEEE | Requirements engineering, requirement characteristics, and needs-to-requirements transformation | Cross-reference identified in ISO 15288; full text not committed | Backlog; not started | Study after ISO 24748-1, ARP4754B, and ARP4761A first round; complements ISO 15289 |
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
| E | DO-160; ARINC 429/664/661/653/615A; human factors; cybersecurity | TBD by source | TBD | Applicable organizations | Domain-specific constraints and validation cases | Metadata / secondary-source only | Not started | Add only when research scope requires |

受版权限制的全文不得提交。不可公开资料只记录 `Source available internally — not committed`，且不能包含内部 URL、凭据或 confidential locator。
