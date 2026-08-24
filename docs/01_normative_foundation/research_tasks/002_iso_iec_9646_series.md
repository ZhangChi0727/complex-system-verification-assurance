---
title: ISO/IEC 9646 Series Normative Research Task Specification
status: planned
version: 0.6
baseline: post-v0.2
owner: research
last_updated: 2026-08-24
task_type: clause-study
research_questions: [RQ3, RQ5, RQ8]
innovation_candidates: [INN-T2, INN-T3, INN-M4, INN-I2]
contribution_modes: [support, qualify, falsify, no-evidence]
source_population: complete-clauses
dependencies:
  - README.md
  - ../standards_baseline.md
  - ../normative_gap_matrix.md
  - ../../00_overview/research_questions.md
  - ../../00_overview/innovation_statement.md
  - ../../00_overview/research_scope.md
downstream_closure:
  - "Task 002: final ISO/IEC 9646 source-native disposition after independent review"
  - "Architecture synthesis: ISO-G04 promotion decision after independent review"
---

# ISO/IEC 9646 Series Normative Research Task Specification

## Control record

| Field | Value |
|---|---|
| Order / priority | 02 / targeted conformance-methodology study |
| Baseline status | `SOURCE POPULATION ACQUIRED; CLAUSE STUDY PENDING` |
| Source | ISO/IEC 9646 Parts 1/2/4/5/6/7 acquired and fingerprinted; complete controlled population for this methodology study |
| Layer / trigger | Generic methodological source / ISO-G04 and conformance instance |
| Initial impact | `DEFERRED — clause study and independent review pending` |

### Controlled local source inventory

| Part | Canonical local file | Physical pages | SHA-256 | Control status |
|---|---|---:|---|---|
| ISO/IEC 9646-1:1994 | `references/PDF/9646-1-1994.pdf` | 56 | `A879A40A00F2B4086A3D1D4E68497D0008F24D5D6C43A531B13112CFE5E92F65` | Included |
| ISO/IEC 9646-2:1994 | `references/PDF/9646-2-1994.pdf` | 40 | `B16937B8DAAAFB45A9B2DCFBD73F2F00B20B39714B6D8E192AC1C0EFD3DA2333` | Included |
| ISO/IEC 9646-3 | — | — | — | `OUT OF SCOPE — TEST NOTATION / EXECUTION TECHNOLOGY`; not a blocker |
| ISO/IEC 9646-4:1994 | `references/PDF/9646-4-1994.pdf` | 20 | `4177D2EEA43675C0F1AA6ADA450573DCC9B1E484800E3D13402B2240C80CDED7` | Included |
| ISO/IEC 9646-5:1994 | `references/PDF/9646-5-1994.pdf` | 44 | `A09BB65A2AD43C22F9E95D336BEC777D9BBCF7F26D324AA2FA6220755AAD2490` | Included |
| ISO/IEC 9646-6:1994 | `references/PDF/9646-6-1994.pdf` | 24 | `9B14CD1BF9E9FF5872B387FBFBF7E8CDAE7CE60EFFC9192C73157C584800B3ED` | Acquired; protocol-profile specialization |
| ISO/IEC 9646-7:1995 | `references/PDF/9646-7-1995.pdf` | 68 | `AC28B93C3670C9EC6932785E8F73457645F652DC27D92C46DA7D49320D9CCB35` | Included |

ITU-T X.29x numbers are bibliographic relationships only. No ITU acquisition or paired locator is required, and textual identity must not be claimed. Part 3 is excluded because TTCN representation is outside this task; a future ATS serialization, TTCN or executable-suite ADR must open a separate task.

## Research orientation

执行本任务前必须先读取本节与 frontmatter dependencies，并带着明确的研究问题、候选反证路径和来源边界进入原文。任务不是一般性总结，也不是为当前框架寻找支持。

### Task purpose and research attitude

研究 Parts 1/2/4/5/6/7 的 conformance-testing methodology，建立 capability/applicability、test purpose、ATS/ETS、outcome、verdict、report 与 claim 的受控链，并严格隔离 notation/execution technology。

本任务服务于 `research_scope.md` 的三层目标：产品无关 Verification Methodology -> Model-Based Verification Architecture -> 非产品化 Verification Platform 研究原型。标准明确规定的内容形成构建约束；标准没有回答的内容形成 gap 或 innovation-space observation。`Standard wins over current framework hypothesis`；标准沉默不得由 agent 补齐，也不得作为 novelty proof。

### Source-specific research entry

原文总体覆盖 Part 1 conformance/testing concepts、Part 2 abstract test suite specification、Part 4 test realization、Part 5 laboratory/client requirements、Part 6 protocol-profile test specification 与 Part 7 implementation conformance statements/profile requirements lists。Part 3 保持受控排除。

该结构说明研究入口，不构成条款结论。Agent 必须在 source gate 后建立完整 inventory，并允许实际条款内容修正本说明中的初始假设。

### Research questions carried by this task

- **RQ3**: 如何系统确定 Level + Method + Technique + Environment + Oracle + Coverage + Evidence？ 本任务只回答与本来源及其受控 scope 直接相关的子问题；完整答案由 Task 022 综合。
- **RQ5**: Verification Evidence 如何通过可审查的 Assurance Argument 支持 Compliance Claim？ 本任务只回答与本来源及其受控 scope 直接相关的子问题；完整答案由 Task 022 综合。
- **RQ8**: 如何通过多领域实例验证 framework 的 completeness、traceability、repeatability、scalability 与 reusability？ 本任务只回答与本来源及其受控 scope 直接相关的子问题；完整答案由 Task 022 综合。

### Innovation candidates under test

- **INN-T2** — typed Verification Basis -> Verification Obligation -> Strategy 的框架中间对象链。Falsification condition: 既有 standards/research 已定义等价 obligation 对象、typed basis 与生命周期关系。Non-claim: 不声称标准普遍从 requirement 直接跳到 test。执行时必须比较 purpose、objects、relations、lifecycle、authority 和 applicability，而不是只比较标签。
- **INN-T3** — Evidence identity、provenance、applicability、credibility 与 sufficiency 的分离模型。Falsification condition: 既有 assurance/evidence metamodel 已提供等价谓词和关系。Non-claim: 不把 Evidence 或 Claim-Argument-Evidence 概念本身主张为原创。执行时必须比较 purpose、objects、relations、lifecycle、authority 和 applicability，而不是只比较标签。
- **INN-M4** — 将 expected-result 正确性依据建模为受控 Oracle 候选对象。Falsification condition: ISO/IEC 9646、testing literature 或其他来源已有等价对象与控制语义，或实例不需要独立对象。Non-claim: 不把 expected result 自动重标为 Oracle。执行时必须比较 purpose、objects、relations、lifecycle、authority 和 applicability，而不是只比较标签。
- **INN-I2** — conformance-testing 与 lifecycle-assurance 传统之间的受控映射模型。Falsification condition: ISO/IEC 9646、29119、15026 或既有研究已经给出等价统一模型。Non-claim: 不预设 PICS、test purpose 或 verdict 映射为原创。执行时必须比较 purpose、objects、relations、lifecycle、authority 和 applicability，而不是只比较标签。

Tasks 001-021 只能返回 `SUPPORT / QUALIFY / FALSIFY / NO EVIDENCE`；Task 022 只能综合为 `SUPPORTED / QUALIFIED / FALSIFIED / OPEN`。任何任务都不能设置 `novelty established`。

### Evidence hierarchy

1. target-source normative provisions;
2. target-source informative material;
3. independently reviewed repository research on other normative sources;
4. directly checked practice-comparison sources;
5. framework hypotheses and research proposals.

低层级证据可以提出问题、比较维度或反例，但不得覆盖或替代高层级证据。Informative material 不得转成 requirement；reviewed note 不替代本任务原文研究；practice source 不生成 target-source clause record；framework hypothesis 不决定标准应当说什么。来源数量不能替代证据质量，禁止来源投票。

### Durable research interface

本任务产生的 reviewed note 是下游研究的耐久接口。执行者必须研究完整受控原文，独立评审者必须使用自己合法取得且指纹匹配的原文核验关键 locator；评审通过后，下游任务应只消费 note 中的 locator + faithful paraphrase + source class + object/relation + limitation + review disposition，而不重新进行同一标准的全文研究。研究笔记不得以“见原文”代替命题，也不取代正式标准。

### Core research principles

1. `Standard evidence -> interpretation -> framework implication -> proposal` 四层分离；
2. 先记录 source-native objects/relations/conditions，再映射 VAF；
3. 冲突、反例、ambiguity 和 `NO EVIDENCE IN THE REVIEWED SOURCE POPULATION` 必须可见；
4. standard silence 不证明 novelty，也不授权任意设计；
5. 只进行 locator-backed 的最小仓库变更；
6. V0-V12 保持 `OPEN-CANDIDATE`，不得在 source task 中冻结 schema、metamodel、state machine 或 automation interface。


## Objective

Extract the selected ISO/IEC 9646 methodology family and determine how capability/applicability, test-purpose, abstract/executable-test, result, verdict, report and conformance-claim semantics constrain VAF.

## Required questions

- How do the selected ISO/IEC 9646 parts divide general concepts, ATS specification, test realization, laboratory/client responsibility, protocol-profile testing and implementation conformance statements?
- How are implementation under test, abstract test suite, test purpose, test case, procedure, verdict and conformance claim distinguished?
- Does any selected clause support the VAF Oracle proposal, or only expected-result/verdict structures?
- Which concepts are methodology and which belong to execution technology such as TTCN-3?

## Preliminary mapping hypotheses

以下是进入原文前的可证伪假设，不是预期答案。Stage 1 完成完整 clause/annex inventory 后、实质提取前，agent 必须补充 `agent-derived from inventory` 行。最终报告不得删除任何假设；每行必须给出 `CONFIRMED / QUALIFIED / CORRECTED / FALSIFIED / NOT ADDRESSED`、locator、理由和影响。

| ID | Preliminary hypothesis | Basis type | Required test | Prohibited inference |
|---|---|---|---|---|
| H1 | PICS/ICS 与 PIXIT/IXIT 分别控制 capability/applicability 和测试附加信息 | Parts 1/7 source structure | 比较 identity、scope、selection 与 claim role | 不得泛化为所有领域的 verification basis |
| H2 | test purpose -> abstract test case/suite -> executable means -> outcome/verdict 可能构成 obligation/case/result 候选链 | Parts 1/2/4 structure | 逐箭头分类 direct/interpreted/framework-defined | 不得仅凭相似词 falsify INN-T2 |
| H3 | expected outcome 与 verdict mechanism 可能只部分对应 Oracle | INN-M4 hypothesis | 核验 correctness basis、configuration、authority 和 failure modes | 不得把 expected result 自动重命名为 Oracle |
| H4 | test verdict、conformance statement、conformance claim 与 certification 具有不同边界 | Part 1 scope and reporting structure | 建立 claim-boundary matrix | passed verdict 不证明 total conformance/certification/sufficiency |
| H5 | Part 6/7 的 profile predicates 和 status semantics 是 profile-limited | Parts 6/7 source role | 通过 abstraction ladder 检查可推广元素 | 不得直接进入 Generic |
| H6 | Part 3 notation 与 TTCN execution technology 不属于本方法论研究总体 | controlled population decision | 记录排除及未来 ADR trigger | 不得用 ETSI TTCN-3 代替 ISO 9646 方法论证据 |

## Required work and outputs

1. Reconfirm the six included ISO sources and the controlled Part 3/ITU exclusion decision.
2. Produce `../standard_notes/iso_iec_9646_series_clause_study.md` and an ISO-G04 crosswalk; do not use TTCN-3 files as substitutes.
3. Cover PICS/ICS, PIXIT/IXIT, test purpose, ATS/ETS, means of testing, laboratory/client, verdict/report/claim and Part 7 SCS/ICS/profile-RL support/status/predicate semantics.
4. Record `NO-IMPACT`, another reviewed disposition, or keep `DEFERRED`; do not promote Oracle from title-level evidence.

## Stop conditions

No conformance or certification claim may be inferred from a test verdict alone. Part 3/ITU acquisition is not a stop condition; any notation/tool interpretation must stop and open a separate task.

## Research contribution contract

This task answers RQ3/RQ5/RQ8 for conformance testing by studying Parts 1, 2, 4, 5, 6 and 7 as the complete controlled population. It shall connect capability/applicability declarations, test purposes, abstract/executable means, expected/observed outcomes, verdicts, reports and claims while preserving the boundary between protocol conformance testing and lifecycle assurance.

## Candidate falsification tests

- `INN-T2/INN-I2`: test whether the family already supplies an equivalent controlled chain from basis and applicability through obligation/test purpose to evidence-backed claim.
- `INN-T3`: test whether result, report, verdict and conformance claim already carry equivalent provenance/credibility separation.
- `INN-M4`: test whether expected-result or means-of-testing controls provide an equivalent governed Oracle object; do not rename them by assumption.

## Negative findings and non-answers

Record Part 3 as `OUT OF SCOPE — TEST NOTATION / EXECUTION TECHNOLOGY`. ITU-T X.29x identifiers are bibliographic relations only: no dual locator, acquisition gate or text-equivalence claim is allowed. Part 6 findings are profile-limited; Part 7 profile RL/SCS/ICS/PICS semantics cannot be generalized without evidence.

## Generalization rights

Conformance-method concepts may enter `Extension`; protocol/profile declarations remain `Profile`; laboratory/client procedures remain `Practice`; only cross-domain independently reviewed abstractions may be proposed for `Generic`.

## Synthesis handoff dataset

Emit the common record plus `part`, `PICS_ICS_PIXIT_IXIT_role`, `test_purpose`, `ATS_ETS_relation`, `expected_observed_verdict_claim`, `profile_predicate` and `lifecycle_assurance_limit`.

## Detailed execution specification

### Execution outcome and boundary

This is a clause study of the closed ISO/IEC 9646 population comprising Parts 1, 2, 4, 5, 6 and 7. Only those acquired and fingerprinted ISO texts may support conclusions. ITU-T identifiers may be recorded as bibliographic relationships but are not evidence locators.

### Phase A — canonical series register

Reconfirm a part-level register with canonical identifier, title, edition/date, status, relevance and decision. Record Parts 1/2/4/5/6/7 as `include`, Part 3 as `exclude — notation/execution technology`, and the related ITU number only as a bibliographic relation.

Do not treat ETSI TTCN-3, a vendor tutorial, a catalogue abstract or a later tool language as the normative methodology source. If any included ISO text fails identity/completeness control, update the blocker and stop before clause conclusions.

Part 3 is explicitly excluded as test notation/execution technology. Part 7 is mandatory and shall cover Implementation Conformance Statements, PICS proforma, profile Requirements Lists, support/status/predicate semantics, capability/applicability declarations and conformance-claim scope.

### Phase B — source control

For each included source record local path, canonical title, edition/date, page count, SHA-256, completeness, language and official status. Inspect normative references and annex status. Licensed texts remain outside Git. Do not infer ISO/ITU textual equivalence; the ISO set is the sole clause basis.

### Phase C — mandatory research packages

Analyse the selected clauses for:

1. implementation under test/system under test and implementation conformance statement boundaries;
2. conformance requirement, test purpose, abstract test case, executable/means-of-testing concepts and test suite structure;
3. preamble, test body, postamble, coordination procedure and test event relationships where present;
4. observed outcome, expected outcome, verdict, inconclusive result, error and test-system validity;
5. controllability, observability, test architecture, upper/lower tester and points of control/observation;
6. parameterization, selection, applicability and capability declarations;
7. test campaign/reporting, traceability and conformance claim limits;
8. separation between methodology, notation and execution technology.

The Part 1 scope statement excluding certification from ISO/IEC 9646 shall be a mandatory row in the claim-boundary table. Part 6 is a protocol-profile specialization and shall not be promoted directly into Generic Core; any abstraction must pass the profile-to-generic ladder and independent review.

### Evidence extraction template

Each used proposition shall record exact part and clause/table/annex locator, PDF page, source class/modality, faithful paraphrase, native objects/relations, applicability conditions, framework implication, ISO-G04 relevance and confidence. Follow `source → interpretation → VAF implication → proposal`; expected outcome or verdict language must not silently become an `Oracle` entity.

### Required mappings and tests

Produce:

- a series/part relationship register;
- `Basis → applicability/capability declaration (PICS/ICS, PIXIT/IXIT) → Test Purpose/Verification Obligation candidate → ATS/ETS → Expected/Observed outcome → Verdict → Report/Conformance Claim`, with each arrow classified as source-direct, interpreted or framework-defined;
- `native concept → VAF Case/Procedure/Expected Result/Observed Result/Verdict/Oracle candidate` crosswalk;
- `methodology → notation → executable test system` boundary matrix;
- an Oracle hypothesis test addressing correctness, configuration, provenance, authority and failure modes;
- a claim-boundary table distinguishing test verdict, implementation conformance statement, conformance claim, certification and authority decision.

For each Oracle attribute proposed by VAF, mark `direct support`, `indirect support`, `contradicted`, `absent` or `not applicable`, with locators and limitations.

### Repository deliverables

Create `../standard_notes/iso_iec_9646_series_clause_study.md`; update ISO-G04 and only genuinely affected gaps; update `../standards_map.md` and `../consolidation/architecture_impact_register.md`; update HANDOFF and CHANGELOG states; create an independent-review packet listing population reconciliation, Part 3/ITU exclusions, changed files and Oracle disposition.

### Required disposition

The final report must choose and justify one of: `Oracle unsupported`, `Oracle partially supported as a framework abstraction`, `Oracle requires modification/split`, or `DEFERRED`. It must also identify whether conformance-testing concepts are generic methodological candidates or a protocol-testing profile. The claim-boundary conclusion shall state explicitly that ISO/IEC 9646 excludes certification from scope. Any `EXTEND/MODIFY/SPLIT/MERGE` disposition requires migration notes.

### No-overclaim rules

Do not state that a passed test proves total product conformance, certification or assurance sufficiency. Do not equate expected result, verdict mechanism and oracle validity. Do not generalize a protocol test architecture to every verification context. Do not claim current equivalence between historical ISO parts and ITU Recommendations without controlled evidence.

### Mandatory execution sequence and report structure

Execute in this order: snapshot state; reconfirm the controlled register/exclusions and source fingerprints; inventory all included clauses; extract terminology and test architecture; build capability/test-purpose/verdict/oracle/claim mappings; apply bounded repository changes; run consistency checks; create review packet; stop at review.

The study note shall contain: control record; controlled population/exclusion register; fingerprint table; clause inventories by part; PICS/ICS and PIXIT/IXIT; Part 7 SCS/ICS/profile-RL semantics; terminology; test architecture; test specification/realization chain; outcome/verdict model; Oracle hypothesis test; conformance-claim boundary; methodology/notation/technology boundary; gap and architecture dispositions; limitations; repository delta; conclusions and review handoff.

The review packet shall reconcile every selected/excluded part, every primary clause and each Oracle attribute; list changed files and statuses; and include copyright, link and overclaim checks. Metadata-only blocked work must use the same packet to show that no clause conclusion was introduced.

### Common evidence record and durable-handoff controls

Every clause-study or mapping proposition used in a repository conclusion shall use the authoritative README common schema. No field may be removed; use `not-applicable` or `not-determined` where appropriate:

| Field | Required content |
|---|---|
| `record_type` | `clause-evidence` / `mapping-evidence` |
| `source_locator` | exact clause/table/figure/annex identifier plus physical PDF page; mapping records may carry a controlled locator pair |
| `source_class` | `normative` / `informative` |
| `source_kind` | `requirement` / `recommendation` / `permission` / `definition` / `descriptive` / `note` / `example` / `annex-guidance` |
| `modality` | `shall` / `should` / `may` / `descriptive` / `not-applicable` |
| `proposition` | faithful short paraphrase; no substantial quotation |
| `object_relation` | source-native object and relation |
| `conditions_applicability` | applicability, tailoring, lifecycle, conformance and stated conditions |
| `rq_contribution` | RQ ID and exact task sub-question |
| `candidate_test` | candidate ID + `SUPPORT` / `QUALIFY` / `FALSIFY` / `NO EVIDENCE` + rationale |
| `framework_mapping` | V-ID/gap/concept + typed relation; interpretation separate |
| `layer` | `Generic` / `Extension` / `Profile` / `Practice` / `No adoption` |
| `unsupported_inference` | inference explicitly prohibited by the evidence |
| `version_dependency` | source-native locator, current counterpart and relation |
| `hypothesis_disposition` | hypothesis ID + `CONFIRMED` / `QUALIFIED` / `CORRECTED` / `FALSIFIED` / `NOT ADDRESSED` + rationale |
| `destination` | note/table/gap/register location receiving the conclusion |
| `downstream_closure_owner` | task/gate owning any provisional or unresolved cross-source closure |
| `confidence_review` | evidence quality, ambiguity and independent-review disposition |

Practice-comparison prompts never enter the normative clause dataset.

### Hypothesis reconciliation and self-contained report rule

After the inventory, extend and freeze the working hypothesis ledger. After extraction and required mappings, dispose every preliminary and inventory-derived row. The note must define key terminology and carry enough locator-backed paraphrase and classification that a downstream task can consume reviewed conclusions without reopening the source. Independent source review still requires a legally obtained, fingerprint-matching original.

### Repository consistency checks

Before review handoff: run `git diff --check`; validate relative links/frontmatter/tables; reconcile source/study/review status; search stale `SOURCE ACQUIRED`, `IN PROGRESS`, `REVIEW PENDING`, `REVIEWED` and architecture-freeze wording; verify controlled Architecture Impact vocabulary; verify all hypotheses and promoted conclusions have dispositions/locators; verify no PDF, screenshot, OCR dump, full extraction, substantial quotation, licence identity, account, order, download timestamp, watermark or absolute user path is staged; verify provisional downstream rows retain their closure owner.

### Definition of done

Done requires the controlled Parts 1/2/4/5/6/7 register; the recorded Part 3/ITU exclusion decision; complete Part 7 capability/claim/profile coverage; clause inventories with exclusions; the Part 1 certification-exclusion check; a profile-limited Part 6 disposition; all mappings/tests above; locator-backed conclusions; synchronized repository statuses; successful Markdown/link/diff checks; and independent review. Part 3 or ITU acquisition is not part of DoD.
