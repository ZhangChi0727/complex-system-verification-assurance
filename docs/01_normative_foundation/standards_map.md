---
title: Cross-Standard Research Map
status: working
version: 0.6
baseline: v0.1
owner: research
last_updated: 2026-08-15
dependencies:
  - standards_baseline.md
---

# Cross-Standard Research Map

本矩阵按标准精读进度更新。`Direct` 表示规范正文直接支持，`Informative` 表示 NOTE 或资料性附录支持，`Indirect` 表示由相关生命周期过程提供支撑，`Gap` 表示在已研究范围内未建立该框架概念。所有结论必须保留条款定位和 conformance 边界。

| Framework Concern | ISO 15288 | ISO 24748-1 | ARP4754B | ARP4761A | DO-178C | DO-254 | DO-297 | Status |
|---|---|---|---|---|---|---|---|---|
| Verification planning | Direct preparation: 6.4.9.3(a); indirect/supporting planning: 6.3.1 | Guidance on lifecycle/process instantiation and project planning: 6.2.2–6.2.8 | TBD | TBD | TBD | TBD | TBD | ISO/24748-1 reviewed |
| Requirement validation | Stakeholder requirements direct: 6.4.2.3(e)(3); system requirements review direct with informative validation relationship: 6.4.3.3(c)(3), NOTE 18; general artefact relationship informative: 6.4.11 NOTE 2 | No verification-specific elaboration; candidate requirements reviews informative: Annex F | TBD | TBD | TBD | TBD | TBD | 15288 direct / 24748-1 contextual |
| Requirement verification | Requirement-set analysis direct: 6.4.2.3(e)(1), 6.4.3.3(c)(1); relationship to good-requirement quality informative: 6.4.3.3(b) NOTE 14 | No verification-specific elaboration; candidate requirements reviews informative: Annex F | TBD | TBD | TBD | TBD | TBD | 15288 direct / 24748-1 contextual |
| Verification method | Direct selection task; examples informative: 6.4.9.3(a)(3) | F.3.6 `Verification reviews` refers to testing, analysis, demonstration and inspection in an informative candidate-review context; it does not define a new method taxonomy | TBD | TBD | TBD | TBD | TBD | 15288 direct / 24748-1 informative |
| Verification independence | Gap for Verification; QA independence only: 6.3.8 | Context may consider IV&V policy; no universal rule: 6.2.2; 6.4 | TBD | TBD | TBD | TBD | TBD | Generic gap |
| Verification environment | Direct through constraints, enablers and procedure conditions: 6.4.9.3(a)–(b) | Enabling-system lifecycle alignment guidance: 4.3.3; Annex A | TBD | TBD | TBD | TBD | TBD | ISO/24748-1 reviewed |
| Configuration control | Indirect/direct cross-process support: 6.3.5; 6.4.9.3(c)(5) | Information updates and enabling-system/tool lifecycle context; no verification-specific control rule: Clause 5; Annex A | TBD | TBD | TBD | TBD | TBD | 15288 direct / 24748-1 contextual |
| Traceability | Direct task; detailed links informative: 3.52; 6.4.9.2(g), .3(c)(4) | Process-view and lifecycle/process mapping provenance guidance: 6.2.8; Annex D | TBD | TBD | TBD | TBD | TBD | ISO/24748-1 reviewed |
| Anomaly management | Direct recording/tracking; resolution via supporting processes: 6.4.9.2, .3(c) | Unified problem reporting guidance; category/priority examples informative: 6.3.1; Annex G | TBD | TBD | TBD | TBD | TBD | ISO/24748-1 partial |
| Regression | Indirect re-verification support; no named process: 6.3.5; 6.4.9.3(b)–(c) | Interoperability-specific regression-testing guidance only: 6.3.4.3.6 | TBD | TBD | TBD | TBD | TBD | Generic gap |
| Coverage | Limited: assurance case may reveal requirements-coverage gaps; no taxonomy: 5.10 | Not addressed as a verification taxonomy | TBD | TBD | TBD | TBD | TBD | Generic gap |
| Evidence | Direct objective-evidence concept; assurance relationship: 3.54–3.55; 5.10; 6.4.9 | V&V results/evidence can support assurance and lifecycle decisions: Clause 5 | TBD | TBD | TBD | TBD | TBD | ISO/24748-1 reviewed |
| Verification closure | Indirect approval/assessment/baseline support; no named closure process: 6.3.2; 6.4.9.3(c) | Stage criteria, decision gates and authorization guidance; no named closure: 4.3; Clause 5; 6.2.6 | TBD | TBD | TBD | TBD | TBD | Generic partial |
| Safety-derived rigor | Gap in studied clauses | Specialty critical characteristics may add stage-exit criteria; no verification rigor allocation scheme: 6.3.4 | TBD | TBD | TBD | TBD | TBD | Generic gap |
| Reuse of prior evidence | Informative model/reuse discussion only: Annex D | Build/reuse planning guidance; no verification-evidence credit rules: Annex E | TBD | TBD | TBD | TBD | TBD | Generic gap |
| Tool considerations | Enablers direct; model/tool guidance informative; no qualification rule: 6.4.9.3; Annex D | Tools have lifecycles and should align with system-of-interest; no qualification rule: Annex A | TBD | TBD | TBD | TBD | TBD | Generic partial |
| Lifecycle tailoring | Tailored conformance framework: Clause 4 | Context, standards, approach, stages and mapping guidance: 6.2.2–6.2.8 | TBD | TBD | TBD | TBD | TBD | ISO/24748-1 reviewed |
| Process-to-stage mapping | No prescribed lifecycle model or sequence: 5.7–5.8 | Direct guidance to map processes/activities to lifecycle model and stage outcomes: 6.2.6–6.2.8 | TBD | TBD | TBD | TBD | TBD | 24748-1 reviewed |
| Entry/exit criteria | Indirect planning/decision support | Direct lifecycle-management guidance: 4.3; Clause 5; 6.2.6 | TBD | TBD | TBD | TBD | TBD | 24748-1 reviewed |
| Decision gates | Decision Management support: 6.3.3 | Direct lifecycle-management guidance and candidate decisions: 4.3; Clause 5 | TBD | TBD | TBD | TBD | TBD | 24748-1 reviewed |
| Technical/management reviews | Verification inspection/peer-review examples are method-level informative guidance | Candidate lifecycle reviews are informative and not mandated: Annex C; Annex F | TBD | TBD | TBD | TBD | TBD | 24748-1 reviewed |
| Process views | Cross-process application possible | Explicit informative construction guidance; no new source tasks: Annex D | TBD | TBD | TBD | TBD | TBD | 24748-1 reviewed |
| Development approach | Processes may be iterative, recursive and concurrent: 5.7–5.8 | Once-through/incremental/evolutionary examples and build guidance: 6.2.5; Annex E | TBD | TBD | TBD | TBD | TBD | 24748-1 reviewed |

## 标准—验证目标—活动—信息项—证据映射

本表采用统一的“标准—验证目标—活动—信息项—证据”五列视图，对已研究标准逐步追加跨标准切片。各行的规范强度必须结合对应标准的 source class、正文/NOTE/Annex 属性及 conformance context 解释。ISO/IEC/IEEE 15288:2023 Clause 6 的 task 是否构成 conformance requirement，取决于其 Clause 4 所声明的 task-based、outcome-based 或 tailored conformance；ISO/IEC/IEEE 24748-1:2024 的行保持 lifecycle-management guidance 定位。

| 标准 | 验证目标 | 活动 | 信息项 | 证据 |
|---|---|---|---|---|
| ISO/IEC/IEEE 15288:2023, 6.4.9 | 为系统、系统元素或 artefact 满足规定要求与特性取得客观证据，并识别异常 | 准备：范围/actions、约束、方法与 success criteria、Verification Strategy、反馈、enablers | Strategy 及其受控关联；具体文档名不由本标准强制 | 方法/判据/约束和 evidence points 的受控定义；详细内容主要来自 NOTE |
| ISO/IEC/IEEE 15288:2023, 6.4.9 | 同上 | 执行：定义并实施 Verification Procedures | Procedure、execution records | 观察/测量、与预期结果和 success criteria 的比较、判定记录 |
| ISO/IEC/IEEE 15288:2023, 6.4.9 | 同上 | 管理：记录结果/异常、跟踪问题、取得批准、维护追溯、提交基线 artefacts | Results、anomalies/problems、approval、trace links、baseline candidates | objective evidence、结果/偏差、异常处置状态、批准记录和受控配置 |
| ISO/IEC/IEEE 15288:2023, 5.10 | 为 assurance claim 建立 justified confidence | 组织 claim、subclaims、argument、evidence 和 context | Assurance case（可审计 artefact） | pass/fail、measurement、qualitative evaluation 等；证据须由结构化推理连接到 claim |
| ISO/IEC/IEEE 15288:2023, 6.3.1–6.3.8 | 支撑 verification outcomes 的规划、控制、决策、风险、配置、信息、测量和质量目标 | supporting project processes | plans、decision/risk/configuration/information/measurement/QA records | 受控基线、变更影响、测量结果、QA evaluation 等间接证据 |
| ISO/IEC/IEEE 24748-1:2024, 4.3; Clause 5 | 使生命周期阶段转换和继续授权具有明确管理依据 | 定义/评价 stage entry and exit criteria，实施 milestone/review，作出 gate decision | lifecycle model、stage criteria、decision record、updated information items | 条件达成状态、评审结果、风险/外部事件输入、授权或保持/终止决定 |
| ISO/IEC/IEEE 24748-1:2024, 6.2.2–6.2.8 | 使所选过程与项目语境、development approach、阶段 outcome 相匹配 | 识别语境与适用标准，选择阶段/过程，映射过程—阶段关系并记录理由 | lifecycle/process instantiation mapping、project plans；具体 schema 为框架提案 | 适用性判断、映射完整性、选择/排除理由及实现 stage outcome 的能力评价 |
| ISO/IEC/IEEE 24748-1:2024, Annex D（资料性） | 围绕跨过程 concern 形成一致的 lifecycle view | 从源标准选择并组织已有 process activities/tasks | process view：stakeholder、concern、purpose、outcomes、source references | view element 到源 activity/task 的可审计映射；不得产生伪 ISO task |
| ISO/IEC/IEEE 24748-1:2024, Annex F（资料性）, F.3.6 | 为 lifecycle milestone 或 gate 提供技术/管理评价输入 | 候选 joint stakeholder reviews；F.3.6 `Verification reviews` 评价 verification status 和相关 open issues | review criteria、review record、issues/actions | test environment、test cases/procedures、system/element status 等评价输入；附录不强制 VRR 或固定 review 清单 |
| ISO/IEC/IEEE 24748-1:2024, 6.3.1; Annex G（资料性） | 统一跨生命周期 problem reporting | 记录、分类并按影响确定 priority | problem report；状态机和字段 schema 未规定 | category、priority 与影响理由；不等于完整 anomaly closure evidence |
