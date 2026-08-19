---
title: Normative Gap Matrix
status: reviewed
version: 1.2
baseline: post-v0.2
owner: research
last_updated: 2026-08-19
dependencies:
  - standards_baseline.md
  - standards_map.md
  - consolidation/five_source_consistency_gap_review.md
---

# Normative Gap Matrix

本矩阵把**已经研究并评审的条款依据**与**尚待研究的候选来源**分开。Gap 是研究问题和候选贡献的输入，不是创新证明。未研究候选源不得进入 `Established clause basis`、不得关闭 gap，也不得支撑强 novelty claim。

受控检索状态只有：`SEARCH NOT STARTED`、`PARTIAL SOURCE COVERAGE`、`PLANNED SOURCES IDENTIFIED`、`SOURCE ACQUISITION OPEN`、`CLAUSE STUDY IN PROGRESS`、`SOURCE SEARCH COMPLETE`、`NO ADEQUATE SOURCE FOUND`。`SOURCE SEARCH COMPLETE` 只表示为当前明示范围完成了充分检索，不等于“证明原创”。

| ID | Framework topic | Established clause basis | Candidate source scope | Source-search status | Current interpretation / response | Disposition | Status |
|---|---|---|---|---|---|---|---|
| ISO-G01 | Independence applicability and substantiation | ISO 15288, 6.3.8/6.4.9; ISO 24748-1, 6.2.2/6.4; ARP4754B, 5.2/5.7/App. A; ARP4761A, 2.2/Apps. E,J–M,P | IEEE 1012; item profiles | PLANNED SOURCES IDENTIFIED | Generic extension point and aviation taxonomy established; universal applicability, authority and substantiation remain open. | PARTIALLY RESOLVED | Open |
| ISO-G02 | Verification coverage (parent) | ISO 15288, 5.10/6.4.9; ARP4754B, 5.5.5.2.2; ARP4761A, D.5/E.4/F.4 | 29119 family; item profiles | PARTIAL SOURCE COVERAGE | Split interface from domain taxonomy; no universal percentage. | SPLIT → ISO-G02A/B | Closed as parent |
| ISO-G02A | Coverage meta-model | Same established basis as ISO-G02 | 29119-2/3 for refinement | PARTIAL SOURCE COVERAGE | Generic `population + criterion + evidence/result + disposition + context` interface retained. | RESOLVED GENERICALLY | Resolved |
| ISO-G02B | Domain coverage taxonomy and completion rules | ARP4754B, 5.5.5.2.2; ARP4761A, D.5/E.4/F.4 | 29119-2/4; DO-178C/DO-254 | PLANNED SOURCES IDENTIFIED | Aviation dimensions are profile inputs; cross-domain rules remain open. | KEEP OPEN | Open |
| ISO-G03 | Verification sufficiency (parent) | ISO 15288, 5.10; ARP4754B, 5.5.4–5.5.5/App. A; ARP4761A, D.5/E.4/F.4 | 15026 family; IEEE 1012 | PARTIAL SOURCE COVERAGE | Split stable interface from contextual decision criteria. | SPLIT → ISO-G03A/B | Closed as parent |
| ISO-G03A | Sufficiency Assessment interface | Same established basis as ISO-G03 | 15026-2/4 | CLAUSE STUDY IN PROGRESS | Inputs, reasoned conclusion, rationale and residual gaps retained; no universal algorithm. | RESOLVED GENERICALLY | Resolved |
| ISO-G03B | Sufficiency criteria and authority | Same established basis as ISO-G03 | 15026-2/4; IEEE 1012; domain profiles | PLANNED SOURCES IDENTIFIED | Thresholds, aggregation rules and authority remain contextual. | KEEP OPEN | Open |
| ISO-G04 | Oracle validity/configuration | ISO 15288, 6.4.9.3(a)–(b), expected results/success criteria only | ISO/IEC 9646; ITU-T X.290; 29119; testing literature | PLANNED SOURCES IDENTIFIED | Oracle remains an explicit proposal; expected result does not imply an Oracle entity. | KEEP PROPOSAL | Research Proposal |
| ISO-G05 | Re-verification selection and impact semantics | ISO 15288, 6.3.5/6.4.9; 24748-2, 6.7.5.4.4; ARP4754B, 6.3–6.4; ARP4761A, 3.1.1/A.6/E.4/P.1 | IEEE 1012; change-impact literature | PLANNED SOURCES IDENTIFIED | V10 chain retained; universal trigger/selection method remains a hypothesis. | RENAME + PARTIALLY RESOLVED | Open |
| ISO-G06 | Closure authority and state semantics | ISO 15288, 6.3.2/6.4.9; 24748-1, 4.3/Cl.5; ARP4754B, 3.2.2/4.7/5.5–5.7 | 24748-8; 16326; governance literature | SOURCE ACQUISITION OPEN | Composite Gate resolved conceptually; authority, waiver, reopening and state model remain open. | RENAME + PARTIALLY RESOLVED | Open |
| ISO-G07 | Information-item schema | ISO 15288, 5.6/6.3.6/6.4.9/Annex B; 24748-1, 6.2.8; 24748-2, 6.7.4/6.8; ARP4754B, 5.4.7/5.5.6 | 15289; 29148; 15026-2; 29119-3 | CLAUSE STUDY IN PROGRESS | Relations are supported; unified class/field/cardinality schema remains open. | KEEP OPEN | Open |
| ISO-G08 | MBSE automation/model evidence | ISO 15288, Annex D; 24748-1, Annex A.10; ARP4761A, Appendix N | 24641; IEEE 1012; model-evidence literature | PLANNED SOURCES IDENTIFIED | No generic language, qualification or admissibility regime established. | KEEP OPEN | Open |
| LC-G01 | Gate ontology | ISO 24748-1, 4.3/Cl.5/6.2.6 | 24748-8 for refinement | PARTIAL SOURCE COVERAGE | Assessment, optional review, authority decision and event remain separate. | RESOLVED GENERICALLY | Resolved |
| LC-G02 | Review taxonomy | ISO 24748-1, 6.4/Annexes C,F | 24748-8 | SOURCE ACQUISITION OPEN | Method review, lifecycle review and gate decision remain distinct. | RESOLVED GENERICALLY | Resolved |
| LC-G03 | Process-view provenance | ISO 15288, 5.8; 24748-1, Annex D | 15289 / registry design | PARTIAL SOURCE COVERAGE | Framework-added orchestration remains labelled and traceable. | RESOLVED GENERICALLY | Resolved |
| LC-G04 | Lifecycle/process instantiation evidence schema | 24748-1, 6.2.2–6.2.8; 24748-2, 6.4/6.7.4.1/6.8 | 15289; 16326 | CLAUSE STUDY IN PROGRESS | Record concept retained; schema/approval/cardinality remain open. | PARTIALLY RESOLVED | Open |
| ARP-G01 | Assurance applicability and rigor | ARP4754B, 5.2/5.6.4/App. A; ARP4761A, 3.9/App. P | IEEE 1012; 15026-3; item profiles | PLANNED SOURCES IDENTIFIED | Generic constraint hook plus aviation rigor retained; universal scale not claimed. | PARTIALLY RESOLVED FOR AVIATION | Open |
| ARP-G02 | Cross-level verification credit | ARP4754B, 4.6.1/5.5.4/5.5.6 | DO-178C/DO-254/DO-297 | PLANNED SOURCES IDENTIFIED | Aviation credit relations separate from generic prior-evidence applicability. | RESOLVED FOR AVIATION PROFILE | Resolved |
| ARP-G03 | Unintended-behavior assurance | ARP4754B, 4.6.4/5.5.5.3/App. A; ARP4761A, Cl.4 | DO-178C/DO-254 | PLANNED SOURCES IDENTIFIED | Optional aviation obligation retained; item criteria open. | KEEP OPEN | Open |
| SAF-G01 | Safety-to-obligation derivation | ARP4761A, 2.2/3.2–3.5/D.4.3 | 29148 for generic basis refinement | CLAUSE STUDY IN PROGRESS | Typed origins must reach a controlled basis; direct Failure Condition→obligation shortcut prohibited. | RESOLVED FOR AVIATION PROFILE | Resolved |
| SAF-G02 | Assumption lifecycle | 24748-2, 6.7.5.3.5; ARP4761A, 2.2/A.6/D.4.3.2/E.4 | 15289; 29148; assurance literature | CLAUSE STUDY IN PROGRESS | Capability-oriented semantics retained; mandatory fields/state machine remain open. | PARTIALLY RESOLVED | Open |
| SAF-G03 | Multi-type independence | ARP4761A, 2.2/Apps. E,J–M,P | IEEE 1012; item profiles | PLANNED SOURCES IDENTIFIED | Type, principle, requirement, claim and evidence remain separate. | RESOLVED FOR AVIATION PROFILE | Resolved |
| SAF-G04 | Safety evidence aggregation | ARP4761A, E.3–E.5/F.3–F.5 | 15026-2; item profiles | CLAUSE STUDY IN PROGRESS | Development Verification, Safety Analysis and Assessment are evidence roles, not mutually exclusive files. | RESOLVED FOR AVIATION PROFILE | Resolved |
| SAF-G05 | Safety sufficiency reasoning | ARP4761A, D.5/E.4/F.4 | 15026 family; item profiles | PLANNED SOURCES IDENTIFIED | Aviation criteria feed V11; programme thresholds and authority remain open. | PARTIALLY RESOLVED FOR AVIATION | Open |
| SAF-G06 | Safety/change synchronization | ARP4761A, 3.1.1/A.6/E.4/P.1 | IEEE 1012; item profiles | PLANNED SOURCES IDENTIFIED | Aviation V10 subflow retained; generic selection remains ISO-G05. | RESOLVED FOR AVIATION PROFILE | Resolved |

允许持续状态：`Open`、`Research Proposal`、`Partially Supported`、`Resolved`、`Closed as parent`。Disposition 词汇遵循 consolidation report；每一行必须保留 source statement 与 framework interpretation 的边界，且不得保存受版权限制的原文。
