---
title: Normative Gap Matrix
status: reviewed
version: 1.0
baseline: v0.1
owner: research
last_updated: 2026-08-16
dependencies:
  - standards_baseline.md
  - standards_map.md
  - consolidation/five_source_consistency_gap_review.md
---

# Normative Gap Matrix

本矩阵记录会影响 Framework 架构或后续研究顺序的实质缺口。缺口表示截至五源 consolidation，某项 concern 尚未得到充分定义、支持或约束；不表示相关标准本身不完整。`Disposition` 是本次交叉评审对原 gap 的处理，`Status` 是处理后的持续状态。

| ID | Framework topic | Five-source basis | Consolidated interpretation / framework response | Disposition | Status |
|---|---|---|---|---|---|
| ISO-G01 | Independence applicability and substantiation | ISO 15288, 6.3.8/6.4.9；ISO 24748-1, 6.2.2/6.4；ARP4754B, 5.2/5.7/App. A；ARP4761A, 2.2/Apps. E, J–M, P | Generic `IndependenceConstraint` extension point and aviation typed taxonomy are established. Universal rules for when, who, authority and sufficient substantiation remain open. | PARTIALLY RESOLVED | Open |
| ISO-G02 | Verification coverage (parent) | ISO 15288, 5.10/6.4.9；ARP4754B, 5.5.5.2.2；ARP4761A, D.5/E.4/F.4 | Split generic meta-model from domain taxonomy/rules; no universal percentage or sufficiency inference. | SPLIT → ISO-G02A/B | Closed as parent |
| ISO-G02A | Coverage meta-model | Same as ISO-G02 | Freeze `population + criterion + evidence/result + uncovered disposition + configuration/context` as generic extension interface. | RESOLVED GENERICALLY | Resolved |
| ISO-G02B | Domain coverage taxonomy and completion rules | ARP4754B, 5.5.5.2.2；ARP4761A, D.5/E.4/F.4 | Aviation requirement/safety populations are profile dimensions; cross-domain taxonomies and completion rules require later sources. | KEEP OPEN | Open |
| ISO-G03 | Verification sufficiency (parent) | ISO 15288, 5.10；ARP4754B, 5.5.4–5.5.5/App. A Obj. 5.1；ARP4761A, D.5/E.4/F.4 | Split stable assessment interface from domain decision criteria/authority. | SPLIT → ISO-G03A/B | Closed as parent |
| ISO-G03A | Sufficiency Assessment interface | Same as ISO-G03 | Freeze inputs, reasoned conclusion, rationale and residual-gaps output; no universal algorithm. | RESOLVED GENERICALLY | Resolved |
| ISO-G03B | Domain sufficiency criteria and decision authority | ARP4754B, 5.5.4–5.5.5；ARP4761A, D.5/E.4/F.4 | Aviation completion criteria are profile inputs; thresholds, aggregation rules and acceptance authority remain contextual. | KEEP OPEN | Open |
| ISO-G04 | Oracle validity/configuration | ISO 15288, 6.4.9.3(a)–(b) supports expected results/success criteria but no Oracle object | Retain Oracle as explicit research proposal; do not infer an independent entity from success criteria. | KEEP PROPOSAL | Research Proposal |
| ISO-G05 | Re-verification selection and impact semantics | ISO 15288, 6.3.5/6.4.9；ISO 24748-2, 6.7.5.4.4；ARP4754B, 6.3–6.4；ARP4761A, 3.1.1/A.6/E.4/P.1 | V10 and the impact→prior-evidence validity→selected activity→updated evidence chain are resolved; universal trigger/selection rules are not. | RENAME + PARTIALLY RESOLVED | Open |
| ISO-G06 | Closure authority and state semantics | ISO 15288, 6.3.2/6.4.9；ISO 24748-1, 4.3/Clause 5；ISO 24748-2, 6.4；ARP4754B, 3.2.2/4.7/5.5–5.7；ARP4761A, 3.1.1/E.4/F.4 | Composite Gate architecture is resolved. Authority, waiver/deviation, reopening and scope-level state machine remain open. | RENAME + PARTIALLY RESOLVED | Open |
| ISO-G07 | Information-item schema | ISO 15288, 5.6/6.3.6/6.4.9/Annex B；ISO 24748-1, 6.2.8；ISO 24748-2, 6.7.4/6.8；ARP4754B, 5.4.7/5.5.6/App. A | Five sources support records and typed basis relations, including Requirement/Specified Characteristic/Applicable Constraint→Obligation, but not a unified class/field/cardinality schema. ISO 15289 is the next priority. | KEEP OPEN | Open |
| ISO-G08 | MBSE automation/model evidence | ISO 15288, Annex D；ISO 24748-1, Annex A.10；ARP4761A, Appendix N | Aviation MBSA controls do not establish a generic language, tool qualification or evidence-admissibility regime. | KEEP OPEN | Open |
| LC-G01 | Gate ontology | ISO 24748-1, 4.3/Clause 5/6.2.6 | Freeze assessment + optional review + authority decision + state/baseline event; criteria/review/decision remain separate. | RESOLVED GENERICALLY | Resolved |
| LC-G02 | Review taxonomy | ISO 24748-1, 6.4/Annexes C and F | Verification method review/inspection, lifecycle review and gate decision are different ontologies; no mandatory universal VRR. | RESOLVED GENERICALLY | Resolved |
| LC-G03 | Process-view provenance | ISO 15288, 5.8；ISO 24748-1, Annex D | V0–V12 table freezes each element's ontology, generic behavior, aviation profile and gap; framework-added orchestration remains labelled. | RESOLVED GENERICALLY | Resolved |
| LC-G04 | Lifecycle/process instantiation evidence schema | ISO 24748-1, 6.2.2–6.2.8；ISO 24748-2, 6.4/6.7.4.1/6.8 | Record concept retained; schema, approval and cardinality await ISO 15289 and project validation. | PARTIALLY RESOLVED | Open |
| ARP-G01 | Assurance applicability and rigor | ARP4754B, 5.2/5.6.4/App. A；ARP4761A, 3.9/App. P | Generic Assurance Constraint extension plus aviation FDAL/IDAL/objective/control semantics established; certification credit remains separate. | PARTIALLY RESOLVED FOR AVIATION | Open |
| ARP-G02 | Cross-level verification credit | ARP4754B, 4.6.1/5.5.4/5.5.6 | Separate `allocated_to`, `performed_at`, `evidence_from`, `accepted_by`, and `credit_basis`; generic prior-evidence applicability remains an extension point. | RESOLVED FOR AVIATION PROFILE | Resolved |
| ARP-G03 | Unintended-behavior assurance | ARP4754B, 4.6.4/5.5.5.3/App. A Obj. 5.2；ARP4761A, Section 4 | Retain optional aviation obligation; item applicability, method diversity and sufficiency require DO-178C/DO-254. | KEEP OPEN | Open |
| SAF-G01 | Safety-to-obligation derivation | ARP4761A, 2.2/3.2–3.5/D.4.3 | Typed origins converge through Requirement or Constraint before forming an obligation; prohibit direct Failure Condition→obligation shortcut. | RESOLVED FOR AVIATION PROFILE | Resolved |
| SAF-G02 | Assumption lifecycle | ISO 24748-2, 6.7.5.3.5；ARP4761A, 2.2/A.6/D.4.3.2/E.4 | Promote capability-oriented generic conceptual semantics and retain aviation capture/propagation/conversion/confirmation/reassessment specialization；no universal mandatory owner/status/link fields or state machine. | PARTIALLY RESOLVED | Open |
| SAF-G03 | Multi-type independence | ARP4761A, 2.2/Apps. E, J–M, P | Separate type, principle, requirement, claim and substantiation evidence. Universal applicability remains ISO-G01. | RESOLVED FOR AVIATION PROFILE | Resolved |
| SAF-G04 | Safety evidence aggregation | ARP4761A, E.3–E.5/F.3–F.5 | Development Verification, Safety Analysis and Safety Assessment are evidence roles with provenance/configuration, not mutually exclusive files. | RESOLVED FOR AVIATION PROFILE | Resolved |
| SAF-G05 | Safety sufficiency reasoning | ARP4761A, D.5/E.4/F.4 | Use heterogeneous completion criteria as aviation V11 inputs; programme thresholds/authority remain ISO-G03B. | PARTIALLY RESOLVED FOR AVIATION | Open |
| SAF-G06 | Safety-assessment/change synchronization | ARP4761A, 3.1.1/A.6/E.4/P.1 | Freeze V10 safety-impact→assumption/DAL/architecture/evidence reassessment subflow; generic selection remains ISO-G05. | RESOLVED FOR AVIATION PROFILE | Resolved |

允许持续状态：`Open`、`Research Proposal`、`Partially Supported`、`Resolved`、`Closed as parent`。Disposition 词汇遵循 consolidation report；每一行必须保留 source statement 与 framework interpretation 的边界，且不得保存受版权限制的原文。
