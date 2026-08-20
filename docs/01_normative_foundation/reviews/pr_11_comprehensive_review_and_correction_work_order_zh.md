---
title: PR #11 Comprehensive Review and Correction Work Order
status: working
version: 1.1
baseline: post-v0.2
owner: research
last_updated: 2026-08-20
review_target: PR #11 head 078720ecbfd72510e93d3d97d3bc61b6b24c4cdb
review_result: request-changes
dependencies:
  - ../research_tasks/README.md
  - ../standards_baseline.md
---

# PR #11 全面复审与修正工作单

> **Execution note:** 本文件保留外部评审在复审 head 上的原始判断。修正执行以本地实际核验为准：ISO/IEC 9646-7:1995 已在受控本地目录发现并核验，因此 correction 将把 Part 7 记为已取得，剩余 Part 3 / X.292 与 paired-recommendation selection 继续开放；Part 2 的复算 SHA-256 为 64 位 `B16937B8DAAAFB45A9B2DCFBD73F2F00B20B39714B6D8E192AC1C0EFD3DA2333`，评审表原值少一个 `A`，作为原始评审记录不机械改写。上述差异不改变 Task 002 仍为 partial acquisition 的评审结论。

## 1. 文档控制

| 字段 | 内容 |
|---|---|
| 仓库 | `ZhangChi0727/complex-system-verification-assurance` |
| PR | `#11 — docs: add executable normative research task specifications` |
| 复审 head | `078720ecbfd72510e93d3d97d3bc61b6b24c4cdb` |
| 复审日期 | 2026-08-20 |
| PR 状态 | `OPEN / Draft / mergeable`；无 GitHub checks、review 或 review thread |
| 评审结论 | **REQUEST CHANGES** |
| 评审边界 | 研究治理、任务可执行性、来源控制、依赖关系和标准专属研究范围；不执行新的 clause study，不关闭 gap，不冻结 V0–V12 或 schema |

## 2. 总体结论

PR #11 的总体方向正确，21 份现行任务已经形成较一致的来源门禁、完整清单、证据提取、映射、禁止过度主张、独立评审和 Definition of Done 结构。历史任务 `H001–H006` 与现行队列的隔离也基本正确。

当前仍不应转为 Ready 或合并，原因不是任务说明不够详细，而是以下控制问题会使执行者得到相互冲突或无法闭合的指令：

1. 多份已经取得原文的标准仍被登记为 `Not acquired`；
2. Task 001 的全局硬停点与 PR #10 已建立的开放研究治理冲突；
3. 多个早期任务要求完成依赖于后续任务的最终 crosswalk，形成前向或循环依赖；
4. Task 016 使用了错误的硬依赖；
5. 多个标准以旧版 12207/15288 为基础，但任务没有要求保留原始版本依据并映射到当前基线；
6. 29148、15939、15289、15026-4 等来源的正式修订状态没有采用统一控制规则；
7. 若干标准专属附件、过程组或信息项需要在工作单中显式列出，不能只依靠“完整清单”这一通用要求。

## 3. 已核验来源清单

下表页数为本次取得 PDF 的物理页数。PDF 不得提交到 Git；应复制到已被忽略的 `references/PDF/`，采用 canonical filename，并在本地重新计算 SHA-256 后再更新状态。

| Canonical source | 建议本地文件名 | 页数 | SHA-256 | PR 后续状态 |
|---|---:|---:|---|---|
| ISO/IEC/IEEE 15288:2023 | `15288-2023.pdf` | 128 | `917FC68D65C71D16AF10AAF9BD3C2E66B3DAD0AD25052FA7F771C2445C4345E7` | 已评审基础；核对现有受控指纹，不重开研究 |
| ISO/IEC/IEEE 15026-4:2021 | `15026-4-2021.pdf` | 48 | `07B206A483612EC06253BFA315F60A580FA3C07617019F14D462E7EEC3A1AE57` | `SOURCE ACQUIRED; CLAUSE STUDY PENDING` |
| ISO/IEC/IEEE 24748-3:2020 | `24748-3-2020.pdf` | 76 | `55D115E328972FEE0C0D30E98E49773718FC6078337E4F902DFD0263751C6B4F` | `SOURCE ACQUIRED; CLAUSE STUDY PENDING; 12207:2017→2026 COMPATIBILITY OPEN` |
| ISO/IEC/IEEE 24748-4:2026 | `24748-4-2026.pdf` | 64 | `DFF6297870D3D2695C880E64658321A2310E722EB6FB5C4EA453697529CEFBC8` | `SOURCE ACQUIRED; CLAUSE STUDY PENDING` |
| ISO/IEC/IEEE 24748-5:2017 | `24748-5-2017.pdf` | 48 | `4E35BB795B95B6CBE0D118F00E309C82D7D4EE62EBAAA0A6773491A3A8D06DA4` | `SOURCE ACQUIRED; CLAUSE STUDY PENDING; OVERLAP/VERSION REVIEW REQUIRED` |
| ISO/IEC/IEEE 24748-6:2023 | `24748-6-2023.pdf` | 56 | `D809A681300BCC52EB940D91C1FF88DBDEDD8C4736CB0E6AA5DD5FAF959C5B3A` | `SOURCE ACQUIRED; CLAUSE STUDY PENDING; 12207:2017→2026 COMPATIBILITY OPEN` |
| ISO/IEC/IEEE 24748-10:2026 | `24748-10-2026.pdf` | 30 | `065C10C29EFDCD4AB90D19B62F34CA8D205C510B7D91AC2C8FE5AA48826424C0` | `SOURCE ACQUIRED; CLAUSE STUDY PENDING; REQUIRED BEFORE ARCHITECTURE FREEZE` |
| ISO/IEC/IEEE 24641:2023 | `24641-2023.pdf` | 98 | `2AF9ADDB7FE6731DEF01A31A0BBA0B13D81C505F4BDE7AE5FA136258CB180F83` | `SOURCE ACQUIRED; CLAUSE STUDY PENDING` |
| ISO/IEC/IEEE 15939:2017 | `15939-2017.pdf` | 49 | `7DE2D709B59F6314966FD0106DAE937AB70E44681694DD77CB6A18AA7DB18A8C` | `SOURCE ACQUIRED; CLAUSE STUDY PENDING; FORMAL REVISION WATCH` |
| ISO/IEC/IEEE 16326:2019 | `16326-2019.pdf` | 42 | `98823F1F7CAF5E85AC324E8461DEF031CD6751EA260161A55520020D85F5DFB3` | `SOURCE ACQUIRED; CLAUSE STUDY PENDING` |
| ISO/IEC 9646-1:1994 | `9646-1-1994.pdf` | 56 | `A879A40A00F2B4086A3D1D4E68497D0008F24D5D6C43A531B13112CFE5E92F65` | Task 002 partial acquisition |
| ISO/IEC 9646-2:1994 | `9646-2-1994.pdf` | 40 | `B16937B8DAAFB45A9B2DCFBD73F2F00B20B39714B6D8E192AC1C0EFD3DA2333` | Task 002 partial acquisition |
| ISO/IEC 9646-4:1994 | `9646-4-1994.pdf` | 20 | `4177D2EEA43675C0F1AA6ADA450573DCC9B1E484800E3D13402B2240C80CDED7` | Task 002 partial acquisition |
| ISO/IEC 9646-5:1994 | `9646-5-1994.pdf` | 44 | `A09BB65A2AD43C22F9E95D336BEC777D9BBCF7F26D324AA2FA6220755AAD2490` | Task 002 partial acquisition |
| ISO/IEC 9646-6:1994 | `9646-6-1994.pdf` | 24 | `9B14CD1BF9E9FF5872B387FBFBF7E8CDAE7CE60EFFC9192C73157C584800B3ED` | Task 002 partial acquisition |

补充说明：

- ISO/IEC/IEEE 15939 PDF 标题页为 `2017-04`，ISO catalogue publication date 为 `2017-05`。应同时记录“printed edition date”和“catalogue publication date”，不得误判为不同版本。
- ISO/IEC/IEEE 24748-4 PDF 内部页眉出现 `2025/2026`，canonical published identifier 仍为 `ISO/IEC/IEEE 24748-4:2026`，Edition 2 / 2026-02。
- ISO 9646 扫描件的 PDF metadata 较弱，但标题页经可视核验与 Part 1、2、4、5、6 相符。
- 部分 PDF 带机构许可水印。仓库只应记录 `Local licensed source; not committed`、canonical metadata、页数和 SHA-256；不得记录或提交许可主体、账户、下载时间、水印或包含个人/机构信息的绝对路径。

### 3.1 尚未取得但不阻止本 PR 工作单治理修正的来源

- ISO/IEC/IEEE 12207:2026：Task 005 必须继续保持 `SOURCE NOT ACQUIRED`，不得从 24748-3 或目录摘要替代推导条款结论。
- ISO/IEC 9646-3 / ITU-T X.292：用于验证 TTCN 表示法边界；取得前 Task 002 只能完成 part-selection register，不能完成方法论—表示法—执行技术的最终边界。
- ISO/IEC 9646-7 / ITU-T X.296：Implementation Conformance Statements；这是 Task 002 capability declaration、applicability 和 conformance-claim 范围的实质来源，取得前不得完成 Task 002。

24748-8 FDIS、15026-4 DIS、29148 DIS、15939 DIS 和 15289 CD 不需要作为本轮条款依据取得；它们只能用于 metadata/revision watch。

## 4. 必须修正的评审发现

### F-01 — 来源状态与实际原文库存不一致（Blocking）

受影响文件至少包括：

- `docs/01_normative_foundation/research_tasks/README.md`
- `docs/01_normative_foundation/standards_baseline.md`
- Tasks `002`、`004`、`013`–`016`、`018`–`020`
- `HANDOFF/current_progress.md`
- `HANDOFF/next_plan.md`
- `CHANGELOG.md`

按第 3 节更新 canonical filename、页数、SHA-256 和 study status。Task 002 必须写作 `PARTIAL SOURCE ACQUISITION; PART SELECTION/REMAINING ACQUISITION OPEN`，不得因取得五个分册而写成完整 source acquired。

Task 005 保持 `METADATA VERIFIED; SOURCE NOT ACQUIRED; CLAUSE STUDY PENDING`。Task 017 继续保持 revision watch，不因未取得 2019 正式版而改变为普通 clause study。

### F-02 — Task 001 重新引入全局串行冻结（Blocking）

Task 001 当前 Stop conditions 中“the next source may begin only after this task's independent review disposition is recorded”与 PR #10 已建立的治理冲突。

修改为：

- Task 001 未独立评审前，不得提升 15289 相关状态、关闭 ISO-G07C、冻结信息模型，或启动依赖“已评审 15289 结论”的 promotion；
- Task 008、012 等依赖 15289 结论的最终映射/状态提升保持阻塞；
- 无依赖的 metadata verification、source acquisition、source inventory 和 working/candidate research 可以继续；
- 所有 V0–V12、schema、metamodel、state machine 和 automation interface 继续保持 working/open。

同步修改 Task Register 和 `HANDOFF/next_plan.md`，删除“一方面 dependency-driven、另一方面全局单线执行”的双重语义。

### F-03 — 任务间存在前向或循环依赖（Blocking）

建立统一的两阶段规则：

1. 较早任务只产生 `source-native dependency inventory`、`provisional crosswalk` 和 `downstream closure questions`；
2. 只有所有相关来源均完成研究与独立评审后，较后任务或 architecture synthesis 才产生 final cross-source disposition。

建议在 front matter 或 Control record 增加：

```yaml
dependencies:
downstream_closure:
```

必须处理以下关系：

| 当前冲突 | 修正责任 |
|---|---|
| Task 004 要求 Part 3 和 12207 最终 crosswalk，但 Tasks 011/005 尚未完成 | Task 004 只登记 Part 4 source-native dependency；Task 005、011 或综合阶段关闭跨源比较 |
| Task 010 要求 IEEE 1012→15026-3；Task 011 又要求 15026-3→IEEE 1012 | Task 010 完成 IEEE source-native rigor model；Task 011 显式依赖 Task 010 并拥有最终 non-equivalence matrix，或反向选择唯一 owner |
| Task 012 要求 24748-4/24748-5/16326 ownership，但后两者尚未研究 | Task 012 只形成 provisional overlap register；Task 020 依赖 Task 012/014 并关闭 final planning ownership matrix |
| Task 014 同时要求尚未研究的 24748-4/16326 最终结论 | 依赖 Task 012；对 16326 保留 provisional rows，由 Task 020 关闭 |
| Task 020 仅依赖 Task 001，却承担 24748-4/-5 overlap | 增加 Tasks 012、014 及当前 15288/12207 foundation 依赖 |

较早任务的 Definition of Done 不得要求尚未研究来源的 final disposition，否则任务永远无法按自身依赖闭合。

### F-04 — Task 016 使用错误的硬依赖（Blocking）

ISO/IEC/IEEE 24748-10:2026 没有 normative references，其 scope 和 strategic aspects 面向 ISO/IEC/IEEE 15288 的系统工程应用。当前 Task 016 把 Task 005（12207:2026）设为硬依赖，没有充分来源依据。

修改要求：

- 删除 Task 005 作为硬 prerequisite；如保留，只能作为可选 software-context comparison；
- 增加已评审 ISO/IEC/IEEE 15288:2023 note 和 ISO/IEC/IEEE 24748-1:2024 lifecycle/process-view note 为 context dependencies；
- 完整研究 Clause 4 和 Clause 5 的 source-native taxonomy：
  - adaptable modular architecture；
  - iterative and incremental development；
  - attentive situational awareness；
  - attentive decision making；
  - common-mission teaming；
  - shared-knowledge management；
  - continual integration and test；
  - being agile；
- Annex A case story 和 Annex B Industrial DevOps 只能作为 informative evidence，不得产生 mandatory workflow。

### F-05 — 旧版生命周期依据到当前基线的映射缺失（Blocking）

以下标准必须保留 source-native old-edition provenance，并建立 bounded current-baseline mapping；不得机械替换原 locator：

| Task | 源内版本事实 | 必须增加的控制 |
|---|---|---|
| Task 013 / 24748-3:2020 | 全文应用 12207:2017；无 normative references | 现有 2017→2026 protocol 基本正确；增加 Annex A tailoring 全覆盖及 source-acquired 指纹 |
| Task 014 / 24748-5:2017 | Clause 2 规范性引用当时的 `FDIS 12207:2017` | 明确 FDIS→published 12207:2017 身份关系，再做 2017→2026 bounded mapping；研究 Clause 5 conformance 和 Clause 10 SDP content |
| Task 015 / 24748-6:2023 | 规范性引用 12207:2017 和 15288:2023 | 增加 12207:2017→2026 compatibility protocol；增加 reviewed 15288:2023 dependency；显式覆盖 Clause 7 Integration plan 和 informative Annex A coupling matrices |
| Task 018 / 24641:2023 | 使用 15288:2023 和 12207:2017 过程语义 | 增加 reviewed 15288 dependency；软件过程映射依赖 Task 005，未关闭前保持 provisional；建立 Plan/Build/Support/Perform MBSSE 完整 process/task/tool-capability matrix |
| Task 019 / 15939:2017 | 与 15288:2015 对齐 | 增加 15288:2015→2023 targeted mapping；显式区分 normative Clause 6 与 informative Annex A/B/D；不得把 Annex D 示例质量准则变成通用 evidence admissibility rule |
| Task 020 / 16326:2019 | 复现 15288:2015、12207:2017 技术管理过程，并指向 24748-4:2016/24748-5:2017 | 增加双版本映射和 Tasks 005/012/014 依赖；最终 ownership matrix 应区分 quoted process text、16326 guidance 和 PMP normative content |

### F-06 — 24748-4 附件分类必须显式化（Major）

Task 012 当前把 annex 概括为 examples/guidance，不足以防止误分类。必须明确：

- Annex A `Tailoring policies` 是 **normative**；
- Annex B `Expanded process view for systems engineering management planning` 是 **informative**；
- Annex C `Example information item content mapping tables` 是 **informative**。

同时完整覆盖 Clause 4 conformance、Clause 5 concepts、Clause 6 SEMP content。Annex B/C 不得被转换为 mandatory process topology、field/cardinality 或固定文档结构。

### F-07 — 正式修订状态控制不统一（Major）

在 `standards_baseline.md` 和相关任务中增加统一 revision-control fields：

| 来源 | 当前正式依据 | 替代项目状态 | 执行规则 |
|---|---|---|---|
| 15289 | 15289:2019 | Edition 5 CD under development | Task 001 继续研究正式 2019 版；执行/评审时复核状态，不使用 CD 条款 |
| 15026-4 | 15026-4:2021 | Edition 2 DIS under development | Task 004 使用正式 2021 版并持续 watch；DIS 不作 normative basis |
| 29148 | 29148:2018 | Edition 3 DIS under development | Task 021 执行前复核；替代正式版发布时提交 retarget decision，不自动研究 DIS |
| 15939 | 15939:2017 | Edition 2 DIS under development | Task 019 执行前复核；若替代版先发布，停止旧任务并重定向 |
| 24748-8 | 24748-8:2019 | Edition 2 FDIS under development | 维持现有 revision watch；不研究 FDIS |

每项至少记录：current published basis、replacement stage、metadata last verified、official URL、execution-time recheck、retarget condition、draft-use prohibition。

### F-08 — Task 002 来源集合仍不完整（Major）

Task 002 的当前实际状态应为 partial acquisition。已取得 Parts 1、2、4、5、6；仍需：

- Part 3 / X.292：完成 methodology–notation–execution technology 边界；
- Part 7 / X.296：完成 ICS/IXIT、capability/applicability declaration 和 conformance-claim 研究。

Part 1 明确把 certification 排除在 ISO 9646 范围之外；该结论应成为 claim-boundary table 的强制检查项。Part 3 即使最终被分类为 notation/context，也必须有受控 include/context/exclude 决定，不能因为 TTCN-3 属于 execution technology 就静默省略。Part 6 是 protocol-profile specialization，不得直接晋升为 Generic Core。

### F-09 — 来源许可与仓库隐私控制（Major）

在 Task Register 的 Common execution protocol 和所有要求记录 access provenance 的任务中加入：

- 只记录 canonical source、合法取得状态、页数、语言、完整性和 SHA-256；
- 不提交 PDF、提取全文、截图、OCR dump 或大段逐字内容；
- 不记录许可主体、账号、订单、下载时间、水印、内部 URL 或用户绝对路径；
- 独立评审者使用自己合法取得且指纹匹配的原文复核 locator；review packet 只包含短释义、定位符和结论，不应重构标准正文。

## 5. 标准专属任务的最终评审结论

| Task | 结论 | 主要处理 |
|---|---|---|
| 001 — 15289:2019 | 内容范围充分；需修 Stop condition 和 revision recheck | 不应形成全局研究冻结 |
| 002 — 9646/X.290 | 结构合理；来源仅部分齐备 | 加 Parts 3/7 source gate；Part 1 certification exclusion |
| 003 — 15026-1:2025 | 基本通过 | 保留 bounded 2019/2025 compatibility，不做全文 delta；保留 Part 2 dated provenance |
| 004 — 15026-4:2021 | 需修改 | 改为 source acquired；跨 Part 3/12207 只作 provisional dependency |
| 005 — 12207:2026 | 工作单结构可接受，但未作全文核验 | 保持 source not acquired；不得执行 clause study |
| 006–009 — 29119-1/-2/-3/-4 | 通过，依赖结构基本闭合 | 保持 Part 1→Part 2/4、Part 2+15289→Part 3；不把 testing 泛化为全部 Verification |
| 010 — IEEE 1012 | 需修改 crosswalk ownership | 提取 IEEE source-native rigor/independence；最终 15026-3 comparison 由唯一后续 owner 关闭 |
| 011 — 15026-3 | 需增加 Task 010 dependency 或明确 two-stage comparison | 默认 non-equivalence；不得将 level 数字对齐 |
| 012 — 24748-4 | 需修改 annex classification 与 overlap responsibility | Annex A normative；B/C informative；planning ownership 后续关闭 |
| 013 — 24748-3 | 基本充分 | 改 source acquired；显式 Annex A 和 2017→2026 mapping |
| 014 — 24748-5 | 需增加版本映射和 conformance/content packages | FDIS 12207:2017 provenance；Clause 5、10；Annex A–C informative |
| 015 — 24748-6 | 需增加 dated normative dependency mapping | 12207:2017→2026；15288:2023；Clause 7/Annex A |
| 016 — 24748-10 | 需要实质修改 | 删除错误 hard dependency；按 Clause 5 八项 strategic aspects 重写研究包 |
| 017 — 24748-8 watch | 通过 | 继续 metadata-only watch，不使用 FDIS |
| 018 — 24641 | 范围方向正确；需加强完整 process/task matrix | Plan/Build/Support/Perform；12207 mapping provisional；不得推导 tool qualification |
| 019 — 15939 | 范围充分；需版本和 annex 控制 | 15288:2015→2023；Annex D 仅 informative；增加 DIS watch |
| 020 — 16326 | 需实质修改依赖和 ownership | 区分 quoted old-process text、guidance、PMP content；最终关闭 planning overlap |
| 021 — 29148 mapping closure | 工作单结构充分；需 revision watch 和执行优先级复核 | 不重开全文研究；新正式版发布时先作 retarget decision |

## 6. Task 003 的 15026-1:2019 处理原则

不要删除 15026-2:2022 对 `15026-1:2019, 3.1.4` 的 source-native dated locator。正确边界是：

- 当前框架术语完全采用 15026-1:2025；
- 2019 不进入现行 candidate-source register，不建立 standalone study；
- 不做 2019→2025 全文版本差异研究；
- 只对仓库实际沿用的 Claim/assurance/uncertainty 关系作 bounded compatibility decision；
- 描述 15026-2 原始依据时保留 2019 locator，并在旁边标识当前 2025 terminology adoption；
- 不得把“框架选择 2025”写成“15026-2:2022 原文采用 2025”。

这既符合“完全采用 2025、不研究 2019”的架构决定，也避免篡改 Part 2 的来源真实性。

## 7. 逐文件修改范围

### 7.1 必改治理文件

- `docs/01_normative_foundation/research_tasks/README.md`
  - 更新来源观察状态；
  - 增加 partial acquisition、revision control、sanitized provenance；
  - 明确 dependency-driven research 与 promotion/freeze gate 的边界；
  - 增加 provisional crosswalk / downstream closure 规则。
- `docs/01_normative_foundation/standards_baseline.md`
  - 更新第 3 节取得来源的 Availability/Study status；
  - 补 29148、15939 正式修订状态；
  - 15026-4 更新 source acquired；
  - 9646 按 part 建立已取得/未取得/选择状态，不再只写 family-level `Not acquired`。
- `HANDOFF/current_progress.md`
  - 同步 acquired/partial/not-acquired 三类状态；
  - 保持当前 clause research stop 为 15289:2019。
- `HANDOFF/next_plan.md`
  - 采用依赖图而不是隐藏的全局单线；
  - 指出哪些工作可以并行、哪些 promotion 被 Task 001 阻塞；
  - 修复 Task 016、Task 020 等依赖。
- `CHANGELOG.md`
  - 记录“source inventory reconciliation + task dependency correction”；
  - 不写 clause study completed、gap closed 或 architecture promoted。

### 7.2 必改任务文件

- `001`：修全局 stop condition；加入 revision recheck。
- `002`：写入 Parts 1/2/4/5/6 指纹，标记 Parts 3/7 未取得；强化 claim boundary。
- `004`：source acquired；拆分 provisional/final crosswalk。
- `010`、`011`：选择 IEEE 1012↔15026-3 最终比较的唯一 owner。
- `012`：Annex A/B/C 分类；overlap register 仅 provisional。
- `013`：source acquired；Annex A；保留 12207:2017 provenance。
- `014`：source acquired；FDIS 12207:2017→published 2017→2026；Clause 5/10。
- `015`：source acquired；12207:2017→2026；15288:2023；Clause 7/Annex A。
- `016`：source acquired；重写 dependency 和八项 strategic-aspect packages。
- `018`：source acquired；完整 process/task/tool matrix；增加版本依赖。
- `019`：source acquired；15288 version mapping；DIS watch；annex classification。
- `020`：source acquired；增加 005/012/014 依赖；旧版基础映射；final ownership matrix。
- `021`：增加 DIS watch、execution-time retarget 和优先级判断。

其余任务只做横向状态/术语一致性修改，不应借机重写已经合理的研究范围。

## 8. 建议提交结构

不得 amend 或 force-push 现有提交。继续在 PR #11 分支普通提交：

1. `docs: reconcile PR11 controlled source inventory`
   - canonical filenames、页数、SHA-256、availability、revision watch、隐私控制；
2. `docs: repair normative task dependencies and scope controls`
   - F-02 至 F-08 的依赖、范围、附件分类和 Definition of Done 修正。

保持 PR 为 Draft。推送后从远端重新读取 head，再进行 external re-review。

## 9. 验收清单

### 9.1 来源与状态

- [ ] 第 3 节每个 acquired source 的 canonical ID、页数和 SHA-256 在 task/baseline/HANDOFF 中一致。
- [ ] 12207:2026 仍为 source not acquired，未出现条款结论。
- [ ] 9646 Parts 1/2/4/5/6 为 partial acquired，Parts 3/7 明确 open。
- [ ] 没有 PDF、OCR、截图、patch、绝对用户路径、许可主体或水印信息被跟踪。
- [ ] Draft/CD/DIS/FDIS 没有进入 established basis。

### 9.2 依赖与任务可执行性

- [ ] 每个 front-matter dependency 都存在且方向无环。
- [ ] 每个 early task 的 Definition of Done 只依赖其已声明 prerequisites。
- [ ] provisional crosswalk 与 final downstream closure owner 唯一且可追溯。
- [ ] Task 016 不再把 12207:2026 当作无依据的硬 prerequisite。
- [ ] Task 020 拥有 24748-4/-5/16326 final planning overlap closure。
- [ ] IEEE 1012↔15026-3 final non-equivalence matrix 只有一个 owner。

### 9.3 研究治理

- [ ] Task 001 只阻止依赖性 promotion/freeze，不阻止无依赖 working research。
- [ ] V0–V12 仍全部是 `OPEN-CANDIDATE`。
- [ ] 没有 gap 因 source acquisition 或 metadata verification 被关闭。
- [ ] 没有 schema、metamodel、state machine、automation interface 或 certification-readiness 主张。
- [ ] 15026-1:2019 仅保留 source-native dated provenance，没有 standalone study 或 full delta。

### 9.4 仓库机械验证

- [ ] 相对 Markdown links 全部解析。
- [ ] front matter 必填字段和 dependency 路径通过检查。
- [ ] Markdown tables 列数一致。
- [ ] 任务 ID、gap ID、V-ID 无重复或意外改义。
- [ ] `git diff --check` 通过。
- [ ] 冲突标记、凭据模式、citation token、临时制品扫描为零。
- [ ] `git status --short` 干净。
- [ ] 远端 PR head 与本地一致；PR 仍为 Draft、未合并、旧提交历史未改写。

## 10. 合并门禁

只有在 F-01 至 F-09 全部关闭、上述验收完成并经过新的外部内容复审后，PR #11 才可转为 Ready。

当前没有 GitHub checks，因此本地验证记录和外部复审是合并前的必要证据。最终通过后使用普通 merge commit，保留原始任务提交和 correction commits；合并后删除临时 PR 分支。不得在本轮修正中启动 Task 001 条款研究或把任何来源提升为 `CLAUSE STUDY REVIEWED`。

## 10.1 修正执行记录

本节记录对原评审意见的本地处置，不改变第 1 节 `REQUEST CHANGES` 的原始评审结论；所有 finding 均需新的外部复审确认后才能视为 externally closed。

| Finding | Local disposition | External state |
|---|---|---|
| F-01 | Acquired/not-acquired/partial 状态、canonical filenames、页数和 SHA-256 已按实际库存统一；12207 保持未取得；9646 Part 7 经本地核验为已取得，Part 3/paired selection 仍开放 | CORRECTED; REREVIEW PENDING |
| F-02 | Task 001 全局锁改为 15289-dependent promotion/freeze gate；无依赖 working research 可继续 | CORRECTED; REREVIEW PENDING |
| F-03 | 全部任务增加 `downstream_closure`；早期 provisional、后期唯一 final owner 规则已建立 | CORRECTED; REREVIEW PENDING |
| F-04 | Task 016 删除 Task 005 硬依赖，改用 reviewed 15288/24748-1 context，并覆盖八项 Clause 5 strategic aspects | CORRECTED; REREVIEW PENDING |
| F-05 | Tasks 013/014/015/018/019/020 增加 source-native old-edition provenance 与 bounded current-baseline mapping | CORRECTED; REREVIEW PENDING |
| F-06 | Task 012 明确 Annex A normative、Annex B/C informative，并完整覆盖 Clauses 4–6 | CORRECTED; REREVIEW PENDING |
| F-07 | baseline 与 Tasks 001/004/017/019/021 增加统一 formal revision-watch controls | CORRECTED; REREVIEW PENDING |
| F-08 | Task 002 登记 Parts 1/2/4/5/6/7，Part 3/X.292 selection open；加入 certification exclusion 与 Part 6 profile boundary | CORRECTED; REREVIEW PENDING |
| F-09 | baseline/register 增加 sanitized provenance、copyright 与 reviewer-source rules；PDF 保持 ignored/untracked | CORRECTED; REREVIEW PENDING |

第一笔普通 correction commit 为 `9a6cb1e`（source inventory reconciliation）。依赖与范围修正使用第二笔普通 commit；没有 amend、rebase 或 force-push。PR 在外部复审前继续保持 Draft。

## 11. 官方元数据参考

- ISO/IEC/IEEE 12207:2026: https://www.iso.org/standard/90219.html
- ISO/IEC/IEEE 24748-4:2026: https://www.iso.org/standard/87797.html
- ISO/IEC/IEEE 24748-10:2026: https://www.iso.org/standard/90086.html
- ISO/IEC/IEEE 24748-8:2019: https://www.iso.org/standard/75405.html
- ISO/IEC/IEEE FDIS 24748-8: https://www.iso.org/standard/91563.html
- ISO/IEC/IEEE DIS 15026-4: https://www.iso.org/standard/92746.html
- ISO/IEC/IEEE DIS 29148: https://www.iso.org/standard/94091.html
- ISO/IEC/IEEE CD 15289: https://www.iso.org/standard/94699.html
- ISO/IEC/IEEE 15939:2017: https://www.iso.org/standard/71197.html
- ISO/IEC/IEEE DIS 15939: https://www.iso.org/standard/95100.html
- ISO/IEC 9646-1:1994: https://www.iso.org/standard/17473.html
- ITU-T X.290: https://www.itu.int/rec/T-REC-X.290/en
