#!/usr/bin/env python3
"""Data-driven repository-governance integrity checks.

Mutable lifecycle identity and current project state live in project-status.json.
This checker contains only stable schema and semantic invariants; it does not
query another repository or automate substantive framework judgment.
"""

from __future__ import annotations

import importlib.util
import json
import os
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path
from typing import Any
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
STATUS_PATH = ROOT / "project-status.json"

SYNC_SPEC = importlib.util.spec_from_file_location(
    "sync_project_overview", ROOT / "scripts/sync_project_overview.py"
)
assert SYNC_SPEC and SYNC_SPEC.loader
sync = importlib.util.module_from_spec(SYNC_SPEC)
SYNC_SPEC.loader.exec_module(sync)

# STABLE_INVARIANT: document/control schema vocabulary, not lifecycle state.
REQUIRED_FRONTMATTER = {
    "title", "status", "version", "baseline", "owner", "last_updated", "dependencies"
}
ALLOWED_RELATIONS = {
    "instantiates", "specializes", "realizes", "implements", "supports",
    "indexes", "classifies", "candidate-correspondence", "no-direct-correspondence",
}
ALLOWED_MAPPING_STATUSES = {
    "NOT-DETERMINED", "CANDIDATE", "PARTIAL", "CONFLICT", "OUT-OF-SCOPE",
}
SOURCE_ROW_RE = re.compile(r"^R\d{2}$")
ADDITIONAL_ROW_RE = re.compile(r"^A\d{2}$")
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
CONFLICT_RE = re.compile(r"^(<<<<<<<|=======|>>>>>>>)", re.MULTILINE)
FULL_SHA_RE = re.compile(r"(?<![0-9a-f])[0-9a-f]{40}(?![0-9a-f])")
PR_LITERAL_RE = re.compile(r"\bPR\s*#\d+\b", re.IGNORECASE)
# STABLE_INVARIANT: mutable Git refs are navigation state, never immutable identities.
MUTABLE_BRANCH_IDENTITY_RE = re.compile(
    r"(?:refs/heads/|origin/|blob/)(?:main|master|latest)(?![\w.-])"
    r"|(?:BRANCH|REF|IDENTITY|COMMIT|TAG|BASELINE)[A-Z0-9_]*\s*=\s*[\"'](?:main|master|latest)[\"']",
    re.IGNORECASE,
)

# STABLE_INVARIANT: controlled 18+7 mapping shape and relation/status semantics.
EXPECTED_SOURCE_SHAPE = {
    "R01": ("realizes", "CANDIDATE"),
    "R02": ("candidate-correspondence", "CANDIDATE"),
    "R03": ("no-direct-correspondence", "NOT-DETERMINED"),
    "R04": ("candidate-correspondence", "NOT-DETERMINED"),
    "R05": ("classifies", "CANDIDATE"),
    "R06": ("realizes", "PARTIAL"),
    "R07": ("instantiates", "CANDIDATE"),
    "R08": ("instantiates", "CANDIDATE"),
    "R09": ("instantiates", "CANDIDATE"),
    "R10": ("instantiates", "CANDIDATE"),
    "R11": ("implements", "CANDIDATE"),
    "R12": ("candidate-correspondence", "NOT-DETERMINED"),
    "R13": ("realizes", "PARTIAL"),
    "R14": ("indexes", "NOT-DETERMINED"),
    "R15": ("specializes", "NOT-DETERMINED"),
    "R16": ("instantiates", "CANDIDATE"),
    "R17": ("candidate-correspondence", "NOT-DETERMINED"),
    "R18": ("candidate-correspondence", "NOT-DETERMINED"),
}
EXPECTED_ADDITIONAL_SHAPE = {
    row_id: ("no-direct-correspondence", "NOT-DETERMINED")
    for row_id in ("A01", "A02", "A03", "A04", "A05", "A06", "A07")
}

REQUIRED_DOCUMENTS = (
    "README.md",
    "project-status.json",
    "docs/02_verification_framework/generic_verification_suite_core.md",
    "docs/08_validation/README.md",
    "docs/08_validation/cross_repository_instance_contract.md",
    "docs/08_validation/instance_registry.md",
    "docs/08_validation/arinc_615a_object_mapping_register.md",
    "docs/08_validation/arinc_615a_instance_evaluation_protocol.md",
    "docs/08_validation/arinc_615a_v43_migration_evidence_return.md",
    "docs/08_validation/arinc_615a_third_handshake_compatibility_disposition.md",
    "scripts/sync_project_overview.py",
    "scripts/check_repository_integrity.py",
    "tests/test_repository_integrity.py",
    ".github/workflows/repository-integrity.yml",
)

PROTECTED_PREFIXES = (
    "docs/01_normative_foundation/normative_gap_matrix.md",
    "docs/01_normative_foundation/standards_baseline.md",
    "docs/01_normative_foundation/consolidation/architecture_impact_register.md",
    "docs/02_verification_framework/generic_verification_suite_core.md",
)
TASK_PREFIX = "docs/01_normative_foundation/research_tasks/"


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def git(*args: str) -> str:
    result = subprocess.run(
        ["git", *args], cwd=ROOT, text=True, encoding="utf-8",
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False,
    )
    return result.stdout.strip() if result.returncode == 0 else ""


def load_status(path: Path = STATUS_PATH) -> dict[str, Any]:
    return sync.load_status(path)


def parse_table_rows(text: str, pattern: re.Pattern[str]) -> list[list[str]]:
    rows: list[list[str]] = []
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        cells = [cell.strip().strip("`") for cell in line.strip().strip("|").split("|")]
        if cells and pattern.fullmatch(cells[0]):
            rows.append(cells)
    return rows


def mapping_errors(text: str) -> list[str]:
    errors: list[str] = []
    source_rows = parse_table_rows(text, SOURCE_ROW_RE)
    additional_rows = parse_table_rows(text, ADDITIONAL_ROW_RE)
    for name, rows, expected in (
        ("source", source_rows, EXPECTED_SOURCE_SHAPE),
        ("instance-only", additional_rows, EXPECTED_ADDITIONAL_SHAPE),
    ):
        ids = [row[0] for row in rows]
        duplicates = sorted(key for key, count in Counter(ids).items() if count > 1)
        if duplicates:
            errors.append(f"duplicate {name} row IDs: {', '.join(duplicates)}")
        if ids != list(expected):
            errors.append(f"{name} row population/order differs from controlled shape")
        for row in rows:
            if len(row) < 7:
                errors.append(f"{row[0]} has insufficient columns")
                continue
            relation_index, status_index = (4, 5) if name == "source" else (5, 6)
            relation, status = row[relation_index], row[status_index]
            if relation not in ALLOWED_RELATIONS:
                errors.append(f"{row[0]} has invalid or multi-valued relation")
            if status not in ALLOWED_MAPPING_STATUSES:
                errors.append(f"{row[0]} has invalid mapping status")
            if row[0] in expected and (relation, status) != expected[row[0]]:
                errors.append(f"{row[0]} relation/status differs from controlled semantics")
    return errors


def inventory_errors(evidence: str, status: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    arinc = status["crossRepository"]["arinc615a"]
    commit = arinc["assessedSource"]["releaseCommit"]
    repository = arinc["repository"]
    for item in arinc["sourceInventory"]:
        row = f"| `{item['path']}` | {item['bytes']} | `{item['sha256']}` |"
        if evidence.count(row) != 1:
            errors.append(f"source inventory row missing/changed: {item['path']}")
        locator = f"{repository}/blob/{commit}/{item['path']}"
        if locator not in evidence:
            errors.append(f"immutable source locator missing: {item['path']}")
    return errors


def final_state_document_errors(
    registry: str, contract: str, validation_readme: str, status: dict[str, Any]
) -> list[str]:
    errors: list[str] = []
    arinc = status["crossRepository"]["arinc615a"]
    method = status["identities"]["methodDefinition"]["commit"]
    disposition = status["identities"]["methodCompatibilityDisposition"]["commit"]
    required = {
        "method definition": method,
        "method compatibility disposition": disposition,
        "assessed baseline": arinc["assessedSource"]["baselineId"],
        "assessed tag": arinc["assessedSource"]["releaseTag"],
        "assessed release": arinc["assessedSource"]["releaseCommit"],
        "assessed tag object": arinc["assessedSource"]["tagObject"],
        "acknowledgement baseline": arinc["acknowledgementRelease"]["baselineId"],
        "acknowledgement tag": arinc["acknowledgementRelease"]["releaseTag"],
        "acknowledgement release": arinc["acknowledgementRelease"]["releaseCommit"],
        "acknowledgement tag object": arinc["acknowledgementRelease"]["tagObject"],
        "acknowledgement peeled target": arinc["acknowledgementRelease"]["peeledTarget"],
        "compatibility": arinc["compatibility"]["status"],
        "configuration": arinc["projectConfiguration"]["status"],
        "evaluation": arinc["instanceEvaluation"],
        "RQ8": arinc["rq8"],
    }
    for name, value in required.items():
        for label, text in (("registry", registry), ("contract", contract)):
            if value not in text:
                errors.append(f"{label} missing {name}")
    assessed_row = (
        f"| Assessed migration baseline | baseline ID `{arinc['assessedSource']['baselineId']}`; "
        f"release tag `{arinc['assessedSource']['releaseTag']}`;"
    )
    acknowledgement_row = (
        f"| Instance acknowledgement release | baseline ID "
        f"`{arinc['acknowledgementRelease']['baselineId']}`; release tag "
        f"`{arinc['acknowledgementRelease']['releaseTag']}`;"
    )
    for label, text in (("registry", registry), ("contract", contract)):
        if assessed_row not in text:
            errors.append(f"{label} has incorrect assessed-release role binding")
        if acknowledgement_row not in text:
            errors.append(f"{label} has incorrect acknowledgement-release role binding")
    if f"| Method definition identity | `{method}`" not in registry:
        errors.append("registry has incorrect method-definition role binding")
    if f"| Method compatibility disposition identity | `{disposition}`" not in registry:
        errors.append("registry has incorrect method-disposition role binding")
    if f"| Method definition | Candidate GVS Core at `{method}`" not in contract:
        errors.append("contract has incorrect method-definition role binding")
    if f"| Method compatibility disposition | `{disposition}`" not in contract:
        errors.append("contract has incorrect method-disposition role binding")
    for value in (arinc["thirdHandshake"], arinc["acknowledgementRelease"]["releaseTag"]):
        if value not in validation_readme:
            errors.append(f"validation README missing final state value: {value}")
    if method == disposition:
        errors.append("method definition and compatibility disposition identities are swapped/collapsed")
    if arinc["acknowledgementRelease"]["releaseCommit"] != arinc["acknowledgementRelease"]["peeledTarget"]:
        errors.append("acknowledgement tag does not peel to its release commit")
    joined = "\n".join((registry, contract, validation_readme))
    if re.search(r"work order\s+\w+\s+remains prohibited", joined, re.IGNORECASE) or re.search(
        r"工作单\s*\w+.*禁止启动", joined
    ):
        errors.append("completed handshake still reports the acknowledgement work as pending")
    return errors


def frontmatter_errors(path: Path, text: str) -> list[str]:
    if not text.startswith("---\n"):
        return [f"{path}: missing front matter"]
    parts = text.split("---", 2)
    if len(parts) < 3:
        return [f"{path}: malformed front matter"]
    keys = {
        line.split(":", 1)[0].strip()
        for line in parts[1].splitlines()
        if ":" in line and not line.startswith((" ", "\t"))
    }
    missing = REQUIRED_FRONTMATTER - keys
    return [f"{path}: missing front-matter field {key}" for key in sorted(missing)]


def markdown_link_errors(path: Path, text: str) -> list[str]:
    errors: list[str] = []
    for raw in LINK_RE.findall(text):
        target = unquote(raw.split("#", 1)[0].strip().strip("<>"))
        if not target or target.startswith(("http://", "https://", "mailto:")):
            continue
        if not (path.parent / target).resolve().exists():
            errors.append(f"{path}: broken link {raw}")
    return errors


def active_markdown_files(root: Path = ROOT) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*.md"):
        rel = path.relative_to(root).as_posix()
        if rel.startswith(".git/") or "/reviews/" in f"/{rel}":
            continue
        if "review" in path.stem.lower() or "disposition" in path.stem.lower():
            continue
        files.append(path)
    return files


def controlled_markdown_files(root: Path = ROOT) -> list[Path]:
    files = [
        root / "README.md",
        root / "ARCHITECTURE.md",
        root / "CONTRIBUTING.md",
        root / "CHANGELOG.md",
        root / "tools/README.md",
    ]
    for directory in (
        "docs/00_overview",
        "docs/02_verification_framework",
        "docs/08_validation",
    ):
        files.extend(sorted((root / directory).glob("*.md")))
    return [path for path in files if path.is_file()]


def handoff_reference_errors(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    if (root / "HANDOFF").exists():
        errors.append("retired HANDOFF directory still exists")
    for path in active_markdown_files(root):
        text = path.read_text(encoding="utf-8")
        if re.search(r"(?:\.\./)*HANDOFF/", text, re.IGNORECASE):
            errors.append(f"active HANDOFF reference remains: {path.relative_to(root)}")
    return errors


def lifecycle_literal_errors(paths: list[Path], status: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    current_tags = {
        status["crossRepository"]["arinc615a"]["assessedSource"]["releaseTag"],
        status["crossRepository"]["arinc615a"]["acknowledgementRelease"]["releaseTag"],
    }
    for path in paths:
        text = path.read_text(encoding="utf-8")
        if FULL_SHA_RE.search(text):
            errors.append(f"lifecycle SHA literal in executable governance code: {path.name}")
        if PR_LITERAL_RE.search(text):
            errors.append(f"PR-number literal in executable governance code: {path.name}")
        if MUTABLE_BRANCH_IDENTITY_RE.search(text):
            errors.append(f"mutable branch used as lifecycle identity: {path.name}")
        for tag in current_tags:
            if re.search(rf"(?<![\w.-]){re.escape(tag)}(?![\w.-])", text):
                errors.append(f"current release-tag literal in executable governance code: {path.name}")
    return errors


def governance_code_paths(root: Path = ROOT) -> list[Path]:
    """Discover production governance Python and its regression tests."""
    paths = list((root / "scripts").rglob("*.py"))
    paths.extend((root / "tests").rglob("test_*.py"))
    return sorted(
        path for path in paths
        if "__pycache__" not in path.parts and path.is_file()
    )


def pr_required_file_errors(changed: set[str], event_name: str, status: dict[str, Any]) -> list[str]:
    if event_name != "pull_request":
        return []
    required = set(status["governance"]["requiredPullRequestFiles"])
    missing = sorted(required - changed)
    return [f"pull request must update {path}" for path in missing]


def changed_files_for_event() -> set[str]:
    if os.getenv("GITHUB_EVENT_NAME") != "pull_request":
        return set()
    base = os.getenv("GITHUB_BASE_REF")
    if not base:
        return set()
    ref = f"origin/{base}"
    output = git("diff", "--name-only", f"{ref}...HEAD")
    return {line for line in output.splitlines() if line}


def protected_delta_errors() -> list[str]:
    base = os.getenv("GITHUB_BASE_REF")
    if not base:
        return []
    changed = changed_files_for_event()
    errors = [
        f"protected semantic file changed: {path}"
        for path in sorted(changed)
        if path.startswith(PROTECTED_PREFIXES)
    ]
    ref = f"origin/{base}"
    for path in sorted(changed):
        if not path.startswith(TASK_PREFIX):
            continue
        diff = git("diff", "--unified=0", ref, "--", path)
        content_lines = [
            line for line in diff.splitlines()
            if (line.startswith("+") and not line.startswith("+++"))
            or (line.startswith("-") and not line.startswith("---"))
        ]
        removed_ok = all("HANDOFF" in line for line in content_lines if line.startswith("-"))
        added_ok = all(
            "project-status.json" in line or "README.md" in line
            for line in content_lines if line.startswith("+")
        )
        if not content_lines or not removed_ok or not added_ok:
            errors.append(f"research-task change is not administrative HANDOFF retirement: {path}")
    return errors


def tag_errors(status: dict[str, Any]) -> list[str]:
    baseline = status["identities"]["historicalResearchBaseline"]
    actual = git("rev-list", "-n", "1", baseline["tag"])
    if actual and actual != baseline["commit"]:
        return ["historical research baseline tag target changed"]
    return []


def repository_errors(status: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for relative in REQUIRED_DOCUMENTS:
        if not (ROOT / relative).is_file():
            errors.append(f"missing required document: {relative}")
    errors.extend(sync.status_errors(status, ROOT))
    current, expected = sync.synchronized_readme(status)
    if current != expected:
        errors.append("README governed block differs from project-status.json")
    errors.extend(handoff_reference_errors())
    errors.extend(
        lifecycle_literal_errors(
            governance_code_paths(),
            status,
        )
    )
    changed = changed_files_for_event()
    errors.extend(pr_required_file_errors(changed, os.getenv("GITHUB_EVENT_NAME", ""), status))
    errors.extend(protected_delta_errors())
    errors.extend(tag_errors(status))
    mapping = read("docs/08_validation/arinc_615a_object_mapping_register.md")
    errors.extend(mapping_errors(mapping))
    evidence = read("docs/08_validation/arinc_615a_v43_migration_evidence_return.md")
    errors.extend(inventory_errors(evidence, status))
    errors.extend(
        final_state_document_errors(
            read("docs/08_validation/instance_registry.md"),
            read("docs/08_validation/cross_repository_instance_contract.md"),
            read("docs/08_validation/README.md"),
            status,
        )
    )
    for path in controlled_markdown_files():
        text = path.read_text(encoding="utf-8")
        if CONFLICT_RE.search(text):
            errors.append(f"{path}: merge conflict marker")
        errors.extend(frontmatter_errors(path, text))
        errors.extend(markdown_link_errors(path, text))
    return errors


def main() -> int:
    try:
        status = load_status()
    except sync.StatusError as exc:
        print(f"ERROR: {exc}")
        return 1
    errors = repository_errors(status)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    arinc = status["crossRepository"]["arinc615a"]
    print("repository integrity checks passed")
    print(f"third handshake: {arinc['thirdHandshake']}")
    print(f"compatibility: {arinc['compatibility']['status']}")
    print("external remote approval and tag existence are release-gate checks, not local runtime checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
