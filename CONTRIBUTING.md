---
title: Contributing and Change Governance
status: working
version: 0.3
baseline: post-v0.2
owner: research
last_updated: 2026-08-30
dependencies:
  - project-status.json
  - docs/00_overview/research_scope.md
  - docs/00_overview/innovation_statement.md
  - docs/08_validation/cross_repository_instance_contract.md
---

# Contributing

本仓库即使处于个人研究阶段，也按可审计研究资产管理变更。

## Project-status discipline

Every pull request must update both `README.md` and `project-status.json`, even
when the status delta is explicitly “no change.” The README must state the
current increment, current stop and next step; `project-status.json` owns the
machine-readable identities and state. Run:

```powershell
python scripts/sync_project_overview.py --write
python scripts/sync_project_overview.py --check
```

Lifecycle SHA, PR number, release tag, branch and current status values belong
in project data, not validator constants. Validators may hard-code only stable
schema/semantic invariants and must mark them `STABLE_INVARIANT`. Pull-request
CI derives its base from the event; push CI checks consistency without imposing
a synthetic PR diff. Dedicated HANDOFF files and status-only follow-up PRs are
retired: the substantive PR must leave README and project status truthful.

## Normative claims

修改规范性主张时必须说明：

- source 与准确 version/revision；
- legally available 的精确定位信息；
- 原文直接要求、guidance、interpretation、industrial practice 或 research proposal 的分类；
- 适用层级、语境与任何 tailoring 条件。

不得使用无法追溯的“标准规定……”表达，也不得提交受版权限制的标准全文。

## Framework rules

新增或修改 Framework Rule 必须给出 normative basis，或明确标记 research rationale。未经标准研究支持的内容使用 `working`、`candidate`、`TBD` 或 `research proposal`。

## Domain knowledge

DCAS-specific 内容不能直接进入 generic `docs/`。先判断其属于 Generic Method、Generic Process、Domain Rule、Domain Pattern、Concrete Example、Tooling 或 Organizational Practice。

## Terminology changes

术语变更需要同步检查 framework、information model、pattern library、templates 与 domain profiles，尤其保持以下边界：

- Verification Method ≠ Verification Technique；
- Traceability ≠ Assurance Argument；
- Expected Result ≠ Oracle；
- Result ≠ Evidence；
- Test 不等同于全部 Verification。

## Standards-research touch points

新增或修订一份标准研究切片时，按序检查以下触点（漏检即一致性缺陷）：

1. `standards_baseline.md`——来源行、研究角色与优先级；
2. `standard_notes/` 研究笔记——条款定位与五级分类；
3. `standards_map.md`——concern 行、五列切片与 coverage note；
4. `normative_gap_matrix.md`——gap 新增/disposition/状态迁移（含“创新输入”性质迁移）；
5. consolidation report §28 annex——若产生新 promotion，先登记后扩散；
6. `terminology.md`——引用 annex 行，不重定义；
7. `templates/`——candidate 字段标注，不升级为 generic schema；
8. `reviews/`——internal/external 评审 provenance 与 disposition；
9. `CHANGELOG.md`——研究记录。

候选来源必须与 established clause basis 分栏管理。只有完成条款研究和评审的来源可进入 established basis；未研究来源只能使用受控 source-search 状态，不得关闭 gap 或证明 novelty。新增来源须更新 Controlled Candidate-Source Baseline 的版本、状态、availability、layer role 与 trigger。

## Cross-repository change rules

- 外部实例在 versioned object registry 建立前只能使用 [temporary controlled mappings](docs/08_validation/instance_registry.md)；candidate prefixes 不是稳定 ID。
- 每次映射变更必须记录不可变 instance baseline/commit、Candidate GVS Core definition context、mapping status、review status 和 migration impact。PR/Issue 超链接只用于导航，不能替代受控身份。
- 实例仓库不得复制、静默重定义或通过实现 API 反向控制 Candidate GVS Core；Profile、Binding、Configuration、工具和原始证据仍归实例仓库。
- external finding 只有形成 Framework Change Proposal，并完成 cross-instance relevance、normative basis/research rationale、独立评审及 eligible registration 后，才能影响 canonical definition。
- compatibility 与 Framework Change Proposal 必须独立评审；单一实例不能建立 Generic generalization rights 或关闭 RQ8。
- 跨仓库变更遵守 [three-way handshake](docs/08_validation/cross_repository_instance_contract.md#three-way-handshake-and-compatibility)，不得在一个 PR 中同时改写方法与实例仓库历史。

## Change quality

- 使用受控 ID 和统一 YAML metadata；candidate/temporary identity 不得称为 stable；
- 保持链接可解析，Markdown 无明显格式错误；
- 不提交 credentials、内部网址、proprietary interfaces、screenshots 或原始内部培训材料；
- Framework semantic automation 必须等待信息模型稳定；repository-governance integrity checking 可独立运行，但不得实现 Framework Rules。
