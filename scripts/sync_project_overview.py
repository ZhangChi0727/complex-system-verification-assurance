#!/usr/bin/env python3
"""Synchronize the governed README status block from project-status.json."""

from __future__ import annotations

import argparse
import difflib
import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
STATUS_PATH = ROOT / "project-status.json"
README_PATH = ROOT / "README.md"
COMMIT_RE = re.compile(r"^[0-9a-f]{40}$")

# STABLE_INVARIANT: these are schema vocabulary, not mutable project state.
ALLOWED_ARCHITECTURE_MATURITY = {
    "OPEN-CANDIDATE",
    "REVIEWED-PROVISIONAL",
    "CONTROLLED-BASELINE",
    "VALIDATED-BASELINE",
}
ALLOWED_INSTANCE_EVALUATION = {"NOT-EXERCISED", "INSTANCE-EXERCISED"}
ALLOWED_COMPATIBILITY = {
    "NOT-DETERMINED",
    "REVIEWED-COMPATIBLE-WITH-QUALIFICATION",
    "REVIEWED-INCOMPATIBLE",
}


class StatusError(ValueError):
    """Raised when the status document violates its generic schema."""


def load_status(path: Path = STATUS_PATH) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise StatusError(f"cannot load {path}: {exc}") from exc
    errors = status_errors(data, root=path.parent)
    if errors:
        raise StatusError("; ".join(errors))
    return data


def _get(data: dict[str, Any], dotted: str) -> Any:
    value: Any = data
    for key in dotted.split("."):
        if not isinstance(value, dict) or key not in value:
            raise KeyError(dotted)
        value = value[key]
    return value


def status_errors(data: dict[str, Any], root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    required = (
        "schemaVersion",
        "updatedAt",
        "repository.role",
        "repository.displayRole",
        "currentIncrement.title",
        "currentIncrement.summary",
        "development.architectureMaturity",
        "development.currentStop.taskId",
        "development.currentStop.standard",
        "development.currentStop.objective",
        "development.nextSteps",
        "development.nextInstanceStep",
        "development.blockedClaims",
        "development.blockedActions",
        "claimsBoundary",
        "temporaryControls",
        "identities.historicalResearchBaseline.commit",
        "identities.methodDefinition.commit",
        "identities.methodCompatibilityDisposition.commit",
        "crossRepository.arinc615a.thirdHandshake",
        "crossRepository.arinc615a.compatibility.status",
        "crossRepository.arinc615a.projectConfiguration.status",
        "crossRepository.arinc615a.instanceEvaluation",
        "crossRepository.arinc615a.rq8",
        "governance.requiredPullRequestFiles",
        "governance.readmeMarkers.start",
        "governance.readmeMarkers.end",
    )
    for dotted in required:
        try:
            value = _get(data, dotted)
        except KeyError:
            errors.append(f"missing required field: {dotted}")
            continue
        if value in (None, ""):
            errors.append(f"empty required field: {dotted}")

    for dotted in (
        "identities.historicalResearchBaseline.commit",
        "identities.methodDefinition.commit",
        "identities.methodCompatibilityDisposition.commit",
        "crossRepository.arinc615a.assessedSource.releaseCommit",
        "crossRepository.arinc615a.assessedSource.tagObject",
        "crossRepository.arinc615a.acknowledgementRelease.releaseCommit",
        "crossRepository.arinc615a.acknowledgementRelease.tagObject",
        "crossRepository.arinc615a.acknowledgementRelease.peeledTarget",
    ):
        try:
            value = _get(data, dotted)
        except KeyError:
            errors.append(f"missing immutable identity: {dotted}")
        else:
            if not isinstance(value, str) or not COMMIT_RE.fullmatch(value):
                errors.append(f"invalid immutable identity: {dotted}")

    try:
        method_path = root / _get(data, "identities.methodDefinition.path")
        disposition_path = root / _get(
            data, "identities.methodCompatibilityDisposition.path"
        )
        if not method_path.is_file():
            errors.append("method definition path does not exist")
        if not disposition_path.is_file():
            errors.append("method compatibility disposition path does not exist")
    except KeyError as exc:
        errors.append(f"missing path field: {exc.args[0]}")

    try:
        maturity = _get(data, "development.architectureMaturity")
        if maturity not in ALLOWED_ARCHITECTURE_MATURITY:
            errors.append(f"invalid architecture maturity: {maturity}")
        evaluation = _get(data, "crossRepository.arinc615a.instanceEvaluation")
        if evaluation not in ALLOWED_INSTANCE_EVALUATION:
            errors.append(f"invalid instance evaluation: {evaluation}")
        compatibility = _get(data, "crossRepository.arinc615a.compatibility.status")
        if compatibility not in ALLOWED_COMPATIBILITY:
            errors.append(f"invalid compatibility status: {compatibility}")
    except KeyError:
        pass

    errors.extend(temporary_control_errors(data, root=root))
    return errors


def temporary_control_errors(data: dict[str, Any], root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    controls = data.get("temporaryControls", [])
    if not isinstance(controls, list):
        return ["temporaryControls must be a list"]
    for index, control in enumerate(controls):
        label = f"temporaryControls[{index}]"
        if not isinstance(control, dict):
            errors.append(f"{label} must be an object")
            continue
        required = {"id", "status", "owner", "introducedBy", "retireWhen"}
        missing = sorted(required - set(control))
        if missing:
            errors.append(f"{label} missing {', '.join(missing)}")
            continue
        retire = control["retireWhen"]
        if not isinstance(retire, dict) or set(retire) < {"path", "equals"}:
            errors.append(f"{label}.retireWhen needs path and equals")
            continue
        try:
            actual = _get(data, str(retire["path"]))
        except KeyError:
            errors.append(f"{label} has unknown retirement path")
            continue
        if actual == retire["equals"]:
            errors.append(f"{label} retirement condition is fulfilled; remove the control")
    return errors


def _short(commit: str) -> str:
    return commit[:12]


def _commit_link(repository: str, commit: str) -> str:
    return f"[`{_short(commit)}`]({repository}/commit/{commit})"


def _bullets(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)


def render_status_block(data: dict[str, Any]) -> str:
    arinc = data["crossRepository"]["arinc615a"]
    stop = data["development"]["currentStop"]
    method = data["identities"]["methodDefinition"]
    disposition = data["identities"]["methodCompatibilityDisposition"]
    assessed = arinc["assessedSource"]
    acknowledgement = arinc["acknowledgementRelease"]
    qualifications = ", ".join(arinc["compatibility"]["qualificationIds"])
    method_repository = data["repository"]["url"]
    instance_repository = arinc["repository"]
    return f"""## 当前开发图景

| 维度 | 当前受控状态 |
|---|---|
| 仓库角色 | {data['repository']['displayRole']} |
| 研究阶段 | {data['development']['phase']} |
| 架构成熟度 | `{data['development']['architectureMaturity']}` |
| 历史研究基线 | `{data['identities']['historicalResearchBaseline']['id']}` @ {_commit_link(method_repository, data['identities']['historicalResearchBaseline']['commit'])} |
| Candidate GVS Core 方法定义 | `{method['version']}` @ {_commit_link(method_repository, method['commit'])} |
| ARINC 第三次握手 | `{arinc['thirdHandshake']}`；实例确认版本 `{acknowledgement['baselineId']}` / `{acknowledgement['releaseTag']}` |
| 跨仓库兼容性 | `{arinc['compatibility']['status']}`，受 {qualifications} 限定 |
| 实例状态 | Project Configuration `{arinc['projectConfiguration']['status']}`；评价 `{arinc['instanceEvaluation']}`；RQ8 `{arinc['rq8']}` |
| 当前研究停点 | Task {stop['taskId']} — {stop['standard']} |
| 下一实例步骤 | {data['development']['nextInstanceStep']} |

方法仓库拥有 Generic Core、方法边界与治理规则；实例仓库拥有 Profile、Binding、Configuration、执行记录和实例证据。方法定义提交 {_commit_link(method_repository, method['commit'])} 与兼容性处置提交 {_commit_link(method_repository, disposition['commit'])} 是不同的不可变身份，不得互换。

## 本次集成增量

**{data['currentIncrement']['title']}**

{_bullets(data['currentIncrement']['summary'])}

保持不变的边界：

{_bullets(data['currentIncrement']['unchangedBoundaries'])}

跨仓库最终状态：方法仓库评估的来源是 `{assessed['baselineId']}` / `{assessed['releaseTag']}` @ {_commit_link(instance_repository, assessed['releaseCommit'])}；ARINC 仓库以 `{acknowledgement['baselineId']}` / `{acknowledgement['releaseTag']}` @ {_commit_link(instance_repository, acknowledgement['releaseCommit'])} 确认该处置。此次确认不创建方法仓库 baseline 或 tag。

## 当前停点

`Task {stop['taskId']}` — **{stop['standard']}**：{stop['objective']}

当前不得越过的结论边界：

{_bullets(data['development']['blockedClaims'])}

## 下一步开发计划

{_bullets(data['development']['nextSteps'])}
"""


def replace_status_block(readme: str, data: dict[str, Any]) -> str:
    markers = data["governance"]["readmeMarkers"]
    start, end = markers["start"], markers["end"]
    if readme.count(start) != 1 or readme.count(end) != 1:
        raise StatusError("README must contain exactly one governed marker pair")
    before, remainder = readme.split(start, 1)
    _, after = remainder.split(end, 1)
    block = render_status_block(data).rstrip()
    return f"{before}{start}\n{block}\n{end}{after}"


def synchronized_readme(
    data: dict[str, Any], readme_path: Path = README_PATH
) -> tuple[str, str]:
    current = readme_path.read_text(encoding="utf-8")
    return current, replace_status_block(current, data)


def diff_text(current: str, expected: str) -> str:
    return "".join(
        difflib.unified_diff(
            current.splitlines(keepends=True),
            expected.splitlines(keepends=True),
            fromfile="README.md (current)",
            tofile="README.md (generated)",
        )
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true", help="update README in place")
    mode.add_argument("--check", action="store_true", help="fail if README has drifted")
    args = parser.parse_args(argv)

    try:
        data = load_status()
        current, expected = synchronized_readme(data)
    except StatusError as exc:
        print(f"project overview error: {exc}", file=sys.stderr)
        return 1

    if current == expected:
        print("project overview is synchronized")
        return 0
    if args.write:
        README_PATH.write_text(expected, encoding="utf-8", newline="\n")
        print("README governed status block updated")
        return 0
    print(diff_text(current, expected), file=sys.stderr)
    print("run scripts/sync_project_overview.py --write", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
