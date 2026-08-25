#!/usr/bin/env python3
"""Repository-governance integrity checks for controlled research documents.

This checker deliberately does not implement Verification Framework semantics.
It uses only the Python standard library and local Git metadata.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FRONTMATTER = {
    "title", "status", "version", "baseline", "owner", "last_updated", "dependencies"
}
ARINC_BASELINE_RELEASE_COMMIT = "3299e6dae83424862f75a4c1d09b91b80d9d8b00"
ARINC_CONTROL_STATE_COMMIT = "0ce96f701159fd4156d5e5e9889360f53977a61b"
METHOD_AUTHORING_BASE = "196cfc2426a841a4adb9c9159660253896b0257c"
ARINC_ACTIVE_BASELINE = "RB-2026-001-v4.2.1"
ARINC_PR9_HEAD = "53a98447bcfa862f082ce443d69115067d3ff2f1"
V02_TAG_COMMIT = "357ad14ffc4e59abd071cb794912eb949a6ae6cf"

REQUIRED_DOCUMENTS = [
    "docs/02_verification_framework/generic_verification_suite_core.md",
    "docs/08_validation/cross_repository_instance_contract.md",
    "docs/08_validation/instance_registry.md",
    "docs/08_validation/pr_14_external_review_disposition.md",
    "docs/08_validation/arinc_615a_object_mapping_register.md",
    "docs/08_validation/arinc_615a_instance_evaluation_protocol.md",
    "scripts/check_repository_integrity.py",
    ".github/workflows/repository-integrity.yml",
]

CONTROLLED_FILES = [
    ROOT / "README.md",
    ROOT / "ARCHITECTURE.md",
    ROOT / "CONTRIBUTING.md",
    ROOT / "CHANGELOG.md",
    ROOT / "HANDOFF/current_progress.md",
    ROOT / "HANDOFF/next_plan.md",
    ROOT / "tools/README.md",
    ROOT / "docs/01_normative_foundation/consolidation/architecture_impact_register.md",
]
for directory in ("docs/00_overview", "docs/02_verification_framework", "docs/08_validation"):
    CONTROLLED_FILES.extend(sorted((ROOT / directory).glob("*.md")))
CONTROLLED_FILES = sorted(set(CONTROLLED_FILES))

LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
CONFLICT_RE = re.compile(r"^(<<<<<<<|=======|>>>>>>>)", re.MULTILINE)
COMMIT_RE = re.compile(r"^[0-9a-f]{40}$")


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def frontmatter_keys(text: str) -> set[str]:
    if not text.startswith("---\n"):
        return set()
    end = text.find("\n---\n", 4)
    if end < 0:
        return set()
    keys: set[str] = set()
    for line in text[4:end].splitlines():
        match = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):", line)
        if match:
            keys.add(match.group(1))
    return keys


def frontmatter_dependencies(text: str) -> list[str]:
    if not text.startswith("---\n"):
        return []
    end = text.find("\n---\n", 4)
    if end < 0:
        return []
    dependencies: list[str] = []
    collecting = False
    for line in text[4:end].splitlines():
        if line == "dependencies:":
            collecting = True
            continue
        if collecting and line.startswith("  - "):
            dependencies.append(line[4:].strip().strip("\"").strip("'"))
            continue
        if collecting and line and not line.startswith(" "):
            collecting = False
    return dependencies

def table_width(line: str) -> int:
    escaped = False
    count = 0
    for char in line:
        if char == "|" and not escaped:
            count += 1
        if char == "\\" and not escaped:
            escaped = True
        else:
            escaped = False
    return count


def table_cells(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def local_link_target(raw: str) -> str:
    target = raw.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    if " " in target and not target.startswith(("http://", "https://")):
        target = target.split(" ", 1)[0]
    return unquote(target)


def main() -> int:
    errors: list[str] = []
    checked_links = 0
    checked_tables = 0

    for relative in REQUIRED_DOCUMENTS:
        if not (ROOT / relative).is_file():
            errors.append(f"missing required document: {relative}")

    for path in CONTROLLED_FILES:
        if not path.is_file():
            errors.append(f"missing controlled file: {path.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8")
        relative = path.relative_to(ROOT).as_posix()

        missing = REQUIRED_FRONTMATTER - frontmatter_keys(text)
        if missing:
            errors.append(f"{relative}: missing front matter fields {sorted(missing)}")

        for dependency in frontmatter_dependencies(text):
            if not dependency or dependency.startswith(("http://", "https://")):
                continue
            if dependency.startswith("file://") or re.match(r"^[A-Za-z]:[/\\]", dependency):
                errors.append(f"{relative}: prohibited dependency path {dependency}")
                continue
            resolved_dependency = (path.parent / dependency).resolve()
            try:
                resolved_dependency.relative_to(ROOT)
            except ValueError:
                errors.append(f"{relative}: dependency escapes repository {dependency}")
                continue
            if not resolved_dependency.exists():
                errors.append(f"{relative}: missing front matter dependency {dependency}")
        if CONFLICT_RE.search(text):
            errors.append(f"{relative}: conflict marker")

        for match in LINK_RE.finditer(text):
            target = local_link_target(match.group(1))
            if not target or target.startswith("#") or target.startswith(("http://", "https://", "mailto:")):
                continue
            if target.startswith("file://") or re.match(r"^[A-Za-z]:[/\\]", target):
                errors.append(f"{relative}: prohibited local/absolute link {target}")
                continue
            file_part = target.split("#", 1)[0]
            if not file_part:
                continue
            resolved = (path.parent / file_part).resolve()
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                errors.append(f"{relative}: link escapes repository {target}")
                continue
            checked_links += 1
            if not resolved.exists():
                errors.append(f"{relative}: missing local link target {target}")

        expected_width = 0
        in_fence = False
        for number, line in enumerate(text.splitlines(), 1):
            if line.lstrip().startswith("```"):
                in_fence = not in_fence
                expected_width = 0
                continue
            if not in_fence and line.startswith("|") and line.endswith("|"):
                width = table_width(line)
                if expected_width == 0:
                    expected_width = width
                    checked_tables += 1
                elif width != expected_width:
                    errors.append(
                        f"{relative}:{number}: table width {width}, expected {expected_width}"
                    )
            else:
                expected_width = 0

    registry_path = ROOT / "docs/08_validation/instance_registry.md"
    registry = registry_path.read_text(encoding="utf-8")
    registry_rows = {}
    for line in registry.splitlines():
        if line.startswith("|"):
            cells = table_cells(line)
            if len(cells) == 2:
                registry_rows[cells[0]] = cells[1]

    expected_registry = {
        "Temporary mapping key": "`TMP-ARINC615A-01`",
        "External active baseline release commit": f"`{ARINC_BASELINE_RELEASE_COMMIT}`",
        "External active baseline tag/ID": f"`{ARINC_ACTIVE_BASELINE}`",
        "Repository control-state snapshot": f"`{ARINC_CONTROL_STATE_COMMIT}` — post-release recording commit; not the baseline content commit",
        "PR #14 authoring base": f"`{METHOD_AUTHORING_BASE}` — authoring provenance only; predates the Candidate GVS Core contract",
        "Candidate method definition identity": "`NOT YET ESTABLISHED — PENDING PR #14 MERGE`",
        "Origin classification": "`PRE-FRAMEWORK LEGACY INSTANCE BASELINE`",
        "Candidate GVS Core binding status": "`NOT YET ESTABLISHED`",
        "Compatibility status": "`NOT-DETERMINED`",
    }
    for field, expected in expected_registry.items():
        if registry_rows.get(field) != expected:
            errors.append(f"instance registry: {field} must equal {expected}")

    release_commit = registry_rows.get("External active baseline release commit", "").strip("`")
    if not COMMIT_RE.fullmatch(release_commit):
        errors.append("instance registry: baseline release commit is not 40 lowercase hexadecimal")
    for field in ("External active baseline release commit", "External active baseline tag/ID"):
        value = registry_rows.get(field, "").lower()
        if any(token in value for token in ("main", "latest", "file://", "c:/", "e:/", "c:\\", "e:\\")):
            errors.append(f"instance registry: mutable/local token in {field}")
    migration = registry_rows.get("Migration candidate", "")
    if ARINC_PR9_HEAD not in migration or "UNMERGED MIGRATION CANDIDATE" not in migration:
        errors.append("instance registry: PR #9 is not a controlled unmerged migration candidate")
    if registry.count("| Temporary mapping key | `TMP-ARINC615A-01` |") != 1:
        errors.append("instance registry: temporary key definition is missing or duplicated")

    mapping_path = ROOT / "docs/08_validation/arinc_615a_object_mapping_register.md"
    mapping = mapping_path.read_text(encoding="utf-8")
    required_pairs = {
        ("Applicability/Profile Declaration", "PICS-like declaration"),
        ("VerificationBasisElement", "applicable CRS item"),
        ("VerificationObligation", "current ARINC requirement-obligation aspect"),
        ("VerificationObligation", "PR #9 Verification Objective"),
        ("Obligation/Coverage aspect", "functional/state/timing and related classifications"),
        ("VerificationStrategy", "Test-and-Analysis allocation"),
        ("VerificationCase", "VC"),
        ("VerificationProcedure", "procedure"),
        ("Observation", "packet trace/timestamp/log"),
        ("Result", "verdict"),
        ("Oracle", "discrete/robust timing rule"),
        ("Evidence", "characterized execution/analysis record"),
        ("Argument", "scoped assurance reasoning"),
        ("Claim", "PR #9 CEI claim entry candidate"),
        ("CompositeGate", "RG/G gate package"),
        ("Configuration", "IUT/setup/procedure identity"),
        ("Anomaly/Change/Impact", "Problem Closure plus CR/DD"),
        ("SufficiencyAssessment", "PR #9 OSR/claim-review candidate"),
    }
    seen_pairs: set[tuple[str, str]] = set()
    allowed_relations = {
        "instantiates", "specializes", "realizes", "implements", "supports",
        "indexes", "classifies", "candidate-correspondence", "no-direct-correspondence"
    }
    allowed_statuses = {"NOT-DETERMINED", "CANDIDATE", "PARTIAL", "CONFLICT", "OUT-OF-SCOPE"}
    for line in mapping.splitlines():
        if not line.startswith("|"):
            continue
        cells = table_cells(line)
        if len(cells) != 9 or cells[0] in {"Framework candidate/role", "---"}:
            continue
        seen_pairs.add((cells[0], cells[1]))
        relation = cells[3].strip().strip("`")
        if ";" in cells[3] or relation not in allowed_relations:
            errors.append(f"mapping row {cells[0]}/{cells[1]}: relation must be one allowed primary value")
        status = cells[4].strip("`")
        if status not in allowed_statuses:
            errors.append(f"mapping row {cells[0]}/{cells[1]}: invalid current status {status}")
        for index, field_name in ((6, "dependency"), (7, "migration note"), (8, "review status")):
            if not cells[index] or cells[index].lower() in {"none", "n/a"}:
                errors.append(f"mapping row {cells[0]}/{cells[1]}: missing {field_name}")
    for pair in sorted(required_pairs - seen_pairs):
        errors.append(f"mapping register: missing required row {pair}")

    expected_row_semantics = {
        ("VerificationBasisElement", "applicable CRS item"): ("candidate-correspondence", "CANDIDATE"),
        ("VerificationObligation", "current ARINC requirement-obligation aspect"): ("no-direct-correspondence", "NOT-DETERMINED"),
        ("Claim", "PR #9 CEI claim entry candidate"): ("indexes", "NOT-DETERMINED"),
        ("Configuration", "IUT/setup/procedure identity"): ("instantiates", "CANDIDATE"),
    }
    for line in mapping.splitlines():
        if not line.startswith("|"):
            continue
        cells = table_cells(line)
        if len(cells) != 9:
            continue
        key = (cells[0], cells[1])
        if key in expected_row_semantics:
            expected_relation, expected_status = expected_row_semantics[key]
            if cells[3].strip("`") != expected_relation or cells[4].strip("`") != expected_status:
                errors.append(f"mapping row {key}: required relation/status semantics changed")
    if ARINC_BASELINE_RELEASE_COMMIT not in mapping or ARINC_CONTROL_STATE_COMMIT not in mapping:
        errors.append("mapping register: release/control-state identities are not separated")
    if "ARINC object --primary relation--> Framework candidate/role" not in mapping:
        errors.append("mapping register: directional relation contract is missing")


    combined = "\n".join(path.read_text(encoding="utf-8") for path in CONTROLLED_FILES if path.exists())
    forbidden = {
        "PICS direct equivalence": ["pics→verification basis", "pics -> verification basis", "pics = verification basis"],
        "Verdict direct equivalence": ["verdict→oracle", "verdict -> oracle", "verdict = oracle"],
        "PASS auto-promotion": ["pass → objective satisfied", "pass→objective satisfied", "pass → compliance", "pass→compliance"],
    }
    lower = combined.lower()
    for label, phrases in forbidden.items():
        if any(phrase in lower for phrase in phrases):
            errors.append(f"prohibited semantic shortcut: {label}")

    for line in combined.splitlines():
        if ARINC_PR9_HEAD in line and "UNMERGED" not in line.upper():
            errors.append("PR #9 head appears outside an unmerged-candidate context")
        hashes = re.findall(r"[0-9a-f]{40}", line)
        if "baseline release commit" in line.lower() and hashes and ARINC_BASELINE_RELEASE_COMMIT not in hashes:
            errors.append("non-controlled ARINC baseline release commit found")
        if "control-state commit `" in line.lower() and hashes and ARINC_CONTROL_STATE_COMMIT not in hashes:
            errors.append("non-controlled ARINC repository control-state commit found")
    protocol = (ROOT / "docs/08_validation/arinc_615a_instance_evaluation_protocol.md").read_text(encoding="utf-8")
    if "| scalability |" not in protocol or "tested ranges only" not in protocol:
        errors.append("evaluation protocol: bounded scalability dimension is missing")
    if "specified-binding contract checks satisfied/qualified/not satisfied" not in protocol:
        errors.append("evaluation protocol: interface conclusion exceeds contract-check scope")


    tracked = git("ls-files").splitlines()
    prohibited_suffixes = {".pdf", ".patch", ".tmp", ".bak", ".orig", ".swp"}
    credential_names = {".env", "credentials.json", "secrets.json", "id_rsa", "id_ed25519"}
    for name in tracked:
        path = Path(name)
        lower_name = name.lower()
        if path.suffix.lower() in prohibited_suffixes:
            errors.append(f"tracked prohibited artefact: {name}")
        if path.name.lower() in credential_names or lower_name.endswith(("~", ".backup")):
            errors.append(f"tracked temporary/credential artefact: {name}")
        if "extract" in path.name.lower() and path.suffix.lower() in {".txt", ".md"}:
            errors.append(f"tracked extraction artefact: {name}")

    secret_patterns = {
        "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
        "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
        "GitHub token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b"),
    }
    for name in tracked:
        path = ROOT / name
        if not path.is_file() or path.stat().st_size > 1_000_000:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for label, pattern in secret_patterns.items():
            if pattern.search(text):
                errors.append(f"tracked content resembles {label}: {name}")

    impact = (ROOT / "docs/01_normative_foundation/consolidation/architecture_impact_register.md").read_text(encoding="utf-8")
    if impact.count("| `GOV-INSIGHT-GVS-INSTANCE-SEPARATION` |") != 1:
        errors.append("GOV-INSIGHT-GVS-INSTANCE-SEPARATION definition is missing or duplicated")
    rq = (ROOT / "docs/00_overview/research_questions.md").read_text(encoding="utf-8")
    if len(re.findall(r"\*\*Status:\*\* Open", rq)) != 8:
        errors.append("RQ1–RQ8 are not all Open")
    progress = (ROOT / "HANDOFF/current_progress.md").read_text(encoding="utf-8")
    next_plan = (ROOT / "HANDOFF/next_plan.md").read_text(encoding="utf-8")
    architecture = (ROOT / "ARCHITECTURE.md").read_text(encoding="utf-8")
    if "ISO/IEC/IEEE 15289:2019" not in next_plan or "Current research stop" not in next_plan:
        errors.append("Task 001 / ISO 15289 current research stop is missing")
    if "OPEN-CANDIDATE" not in architecture or "OPEN-CANDIDATE" not in progress:
        errors.append("V0–V12 OPEN-CANDIDATE maturity boundary is missing")
    if "research-baseline/v0.2" not in combined:
        errors.append("historical research-baseline/v0.2 reference is missing")
    try:
        if git("rev-parse", "research-baseline/v0.2^{}") != V02_TAG_COMMIT:
            errors.append("research-baseline/v0.2 tag target changed")
    except subprocess.CalledProcessError:
        errors.append("research-baseline/v0.2 tag unavailable; checkout must include tags")

    if "| `INSTANCE-EXERCISED` |" in architecture:
        errors.append("INSTANCE-EXERCISED must not be an Architecture maturity table row")
    if "### Instance evaluation state" not in architecture or "orthogonal state dimension" not in architecture:
        errors.append("orthogonal instance-evaluation state contract is missing")

    if errors:
        print("Repository integrity check: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Repository integrity check: PASS")
    print(f"- controlled Markdown files: {len(CONTROLLED_FILES)}")
    print(f"- resolved local links: {checked_links}")
    print(f"- Markdown tables checked: {checked_tables}")
    print(f"- ARINC baseline release commit: {ARINC_BASELINE_RELEASE_COMMIT}")
    print(f"- ARINC compatibility: NOT-DETERMINED")
    print("- required mapping rows: 18")
    print("- framework semantic automation: not performed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
