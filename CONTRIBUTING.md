# Contributing

本仓库即使处于个人研究阶段，也按可审计研究资产管理变更。

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

## Change quality

- 使用稳定 ID 和统一 YAML metadata；
- 保持链接可解析，Markdown 无明显格式错误；
- 不提交 credentials、内部网址、proprietary interfaces、screenshots 或原始内部培训材料；
- 自动化必须等待信息模型稳定。
