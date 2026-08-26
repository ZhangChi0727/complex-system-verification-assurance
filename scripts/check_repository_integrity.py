#!/usr/bin/env python3
"""Repository-governance integrity checks for controlled research documents.

The checker validates recorded identities, document structure and governance
invariants. It deliberately does not automate Framework semantic judgment or
access mutable state in another repository at runtime.
"""

from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FRONTMATTER = {
    "title", "status", "version", "baseline", "owner", "last_updated", "dependencies"
}

METHOD_DEFINITION_COMMIT = "48dd8232b7efe6b0dba3fcb75dfc154d034d2b0b"
METHOD_AUTHORING_BASE = "196cfc2426a841a4adb9c9159660253896b0257c"
ARINC_LEGACY_RELEASE_COMMIT = "3299e6dae83424862f75a4c1d09b91b80d9d8b00"
ARINC_LEGACY_TAG = "RB-2026-001-v4.2.1"
ARINC_CONTROL_STATE_COMMIT = "0ce96f701159fd4156d5e5e9889360f53977a61b"
ARINC_REVIEWED_HEAD = "5d149d1f8e92bbed438fe8bc78be9e8972fecb7d"
ARINC_V43_MERGE_COMMIT = "523d42bf03a1135b3d63a00bfb47d3b879d3927e"
ARINC_V43_BASELINE_ID = "RB-2026-001-v4.3"
ARINC_V43_RELEASE_TAG = "v4.3"
ARINC_V43_TAG_OBJECT = "28312fd9c5470cb15d76eb3762c99a25ab842cfd"
ARINC_HUMAN_REVIEW_ID = "5029797924"
V02_TAG_COMMIT = "357ad14ffc4e59abd071cb794912eb949a6ae6cf"

SOURCE_SHA256 = {
    "docs/control/contracts/EXTERNAL_GVS_BINDING.md": "97e76ec345d58f4c89d35f1118663335744adecdd6eba9551035e5e90675bd4d",
    "docs/control/contracts/ARINC615A_PROFILE_BINDING_CONFIGURATION.md": "0f9a864feb17e7e8735a00e3109c42da9995ebdb13d66d1309cee4769fd35af8",
    "docs/control/contracts/GVS_INSTANCE_MAPPING.md": "f5a4a30ec598b0624b910bd6fbb2895db94f150eb96f20ca800b33114166f43a",
    "docs/control/baselines/RB-2026-001-v4.3.md": "de0483c6590293e748abe2e964e42b267fcb4518e75c4b1ac06f7a9c2bf6456e",
    "docs/control/changes/CR-2026-004.md": "339a68b2f270f5fdecf5e37be8d05350568fdc1128d8fcb9a088eba2e8bc5ff9",
    "docs/control/reviews/PR9_GVS_MIGRATION_REVIEW_HANDOFF.md": "30c084d803a5b9296e02867a8ed49584a091895b507edbe5fb5c2ed02362e418",
    "docs/control/risks/RISK_REGISTER.md": "ec7064c8da3c16fc7e9a5a64d6323f93fd2d1b0e7598206f94f1fcb99842e2c5",
    "scripts/check_repo_baseline.py": "f2f241928717434ecbd44e81a15c6f523d2149a05d0f2b8ca6e1320b627b843f",
}

REQUIRED_DOCUMENTS = [
    "docs/02_verification_framework/generic_verification_suite_core.md",
    "docs/08_validation/cross_repository_instance_contract.md",
    "docs/08_validation/instance_registry.md",
    "docs/08_validation/pr_14_external_review_disposition.md",
    "docs/08_validation/arinc_615a_object_mapping_register.md",
    "docs/08_validation/arinc_615a_instance_evaluation_protocol.md",
    "docs/08_validation/arinc_615a_v43_migration_evidence_return.md",
    "docs/08_validation/arinc_615a_third_handshake_compatibility_disposition.md",
    "scripts/check_repository_integrity.py",
    "tests/test_repository_integrity.py",
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
SOURCE_ROW_RE = re.compile(r"^R\d{2}$")
ADDITIONAL_ROW_RE = re.compile(r"^A\d{2}$")

ALLOWED_RELATIONS = {
    "instantiates", "specializes", "realizes", "implements", "supports",
    "indexes", "classifies", "candidate-correspondence", "no-direct-correspondence",
}
ALLOWED_MAPPING_STATUSES = {
    "NOT-DETERMINED", "CANDIDATE", "PARTIAL", "CONFLICT", "OUT-OF-SCOPE",
}
ALLOWED_CANDIDATE_DISPOSITIONS = {
    "REVIEWED-COMPATIBLE-WITH-QUALIFICATION", "REVIEWED-INCOMPATIBLE",
}

EXPECTED_SOURCE_ROWS = {
    "R01": ("Applicability/Profile Declaration", "PICS-like declaration", "realizes", "CANDIDATE"),
    "R02": ("VerificationBasisElement", "applicable CRS item", "candidate-correspondence", "CANDIDATE"),
    "R03": ("VerificationObligation", "current ARINC requirement-obligation aspect", "no-direct-correspondence", "NOT-DETERMINED"),
    "R04": ("VerificationObligation", "PR #9 Verification Objective", "candidate-correspondence", "NOT-DETERMINED"),
    "R05": ("Obligation/Coverage aspect", "functional/state/timing and related classifications", "classifies", "CANDIDATE"),
    "R06": ("VerificationStrategy", "Test-and-Analysis allocation", "realizes", "PARTIAL"),
    "R07": ("VerificationCase", "VC", "instantiates", "CANDIDATE"),
    "R08": ("VerificationProcedure", "procedure", "instantiates", "CANDIDATE"),
    "R09": ("Observation", "packet trace/timestamp/log", "instantiates", "CANDIDATE"),
    "R10": ("Result", "verdict", "instantiates", "CANDIDATE"),
    "R11": ("Oracle", "discrete/robust timing rule", "implements", "CANDIDATE"),
    "R12": ("Evidence", "characterized execution/analysis record", "candidate-correspondence", "NOT-DETERMINED"),
    "R13": ("Argument", "scoped assurance reasoning", "realizes", "PARTIAL"),
    "R14": ("Claim", "PR #9 CEI claim entry candidate", "indexes", "NOT-DETERMINED"),
    "R15": ("CompositeGate", "RG/G gate package", "specializes", "NOT-DETERMINED"),
    "R16": ("Configuration", "IUT/setup/procedure identity", "instantiates", "CANDIDATE"),
    "R17": ("Anomaly/Change/Impact", "Problem Closure plus CR/DD", "candidate-correspondence", "NOT-DETERMINED"),
    "R18": ("SufficiencyAssessment", "PR #9 OSR/claim-review candidate", "candidate-correspondence", "NOT-DETERMINED"),
}

EXPECTED_ADDITIONAL_ROWS = {
    "A01": ("VerificationCase", "Test Purpose"),
    "A02": ("Evidence", "Execution Evidence Manifest"),
    "A03": ("Configuration", "Test Conformity Record"),
    "A04": ("Argument", "L0–L7 ARINC evidence view"),
    "A05": ("SufficiencyAssessment", "A0–A4 ARINC assurance states"),
    "A06": ("SufficiencyAssessment", "R0–R5 instance research maturity"),
    "A07": ("Configuration", "future Project Configuration `TMP-PC-ARINC615A-01`"),
}

PROTECTED_PREFIXES = (
    "docs/01_normative_foundation/standards_baseline.md",
    "docs/01_normative_foundation/normative_gap_matrix.md",
    "docs/01_normative_foundation/research_tasks/",
    "docs/01_normative_foundation/standard_notes/",
    "docs/01_normative_foundation/reviews/",
    "docs/02_verification_framework/generic_verification_suite_core.md",
    "docs/00_overview/research_questions.md",
    "docs/00_overview/innovation_statement.md",
)


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def frontmatter_keys(text: str) -> set[str]:
    if not text.startswith("---\n"):
        return set()
    end = text.find("\n---\n", 4)
    if end < 0:
        return set()
    return {
        match.group(1)
        for line in text[4:end].splitlines()
        if (match := re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):", line))
    }


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
        elif collecting and line.startswith("  - "):
            dependencies.append(line[4:].strip().strip("\"").strip("'"))
        elif collecting and line and not line.startswith(" "):
            collecting = False
    return dependencies


def table_width(line: str) -> int:
    escaped = False
    count = 0
    for char in line:
        if char == "|" and not escaped:
            count += 1
        escaped = char == "\\" and not escaped
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


def parse_mapping_tables(text: str) -> tuple[dict[str, tuple[str, ...]], dict[str, tuple[str, ...]]]:
    source: dict[str, tuple[str, ...]] = {}
    additional: dict[str, tuple[str, ...]] = {}
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        cells = table_cells(line)
        if len(cells) != 11:
            continue
        if SOURCE_ROW_RE.fullmatch(cells[0]):
            source[cells[0]] = tuple(cells)
        elif ADDITIONAL_ROW_RE.fullmatch(cells[0]):
            additional[cells[0]] = tuple(cells)
    return source, additional


def mapping_errors(text: str) -> list[str]:
    errors: list[str] = []
    source, additional = parse_mapping_tables(text)
    expected_source_order = list(EXPECTED_SOURCE_ROWS)
    expected_additional_order = list(EXPECTED_ADDITIONAL_ROWS)
    if list(source) != expected_source_order:
        errors.append(f"source mapping rows/order differ: {list(source)}")
    if list(additional) != expected_additional_order:
        errors.append(f"instance-only rows/order differ: {list(additional)}")
    review_results: set[str] = set()
    for row_id, expected in EXPECTED_SOURCE_ROWS.items():
        cells = source.get(row_id)
        if cells is None:
            continue
        actual = (cells[1], cells[2], cells[4].strip("`"), cells[5].strip("`"))
        if actual != expected:
            errors.append(f"{row_id} missing or strengthened: expected {expected}, found {actual}")
        if actual[2] not in ALLOWED_RELATIONS or ";" in cells[4]:
            errors.append(f"{row_id} does not have one allowed primary relation")
        if actual[3] not in ALLOWED_MAPPING_STATUSES:
            errors.append(f"{row_id} has invalid mapping status {actual[3]}")
        if not cells[7] or not cells[8] or not cells[9] or not cells[10]:
            errors.append(f"{row_id} lacks dependency, migration, review or qualification")
        review_results.add(cells[9].strip("`"))
    if len(review_results) < 5:
        errors.append("18-row third-handshake review was mechanically homogenized")
    for row_id, expected in EXPECTED_ADDITIONAL_ROWS.items():
        cells = additional.get(row_id)
        if cells is None:
            continue
        actual = (cells[2], cells[3])
        if actual != expected:
            errors.append(f"{row_id} locator/object differs: expected {expected}, found {actual}")
        if cells[1].strip("`") != "INSTANCE-ONLY-ADDITIONAL":
            errors.append(f"{row_id} is not marked INSTANCE-ONLY-ADDITIONAL")
        if (cells[5].strip("`"), cells[6].strip("`")) != (
            "no-direct-correspondence", "NOT-DETERMINED"
        ):
            errors.append(f"{row_id} was strengthened into a Generic correspondence")
    return errors


def third_handshake_document_errors(
    evidence: str, disposition: str, registry: str, contract: str
) -> list[str]:
    errors: list[str] = []
    combined = "\n".join((evidence, disposition, registry, contract))
    required = (
        METHOD_DEFINITION_COMMIT, METHOD_AUTHORING_BASE, ARINC_LEGACY_RELEASE_COMMIT,
        ARINC_LEGACY_TAG, ARINC_CONTROL_STATE_COMMIT, ARINC_REVIEWED_HEAD,
        ARINC_V43_MERGE_COMMIT, ARINC_V43_BASELINE_ID, ARINC_V43_RELEASE_TAG,
        ARINC_V43_TAG_OBJECT, ARINC_HUMAN_REVIEW_ID,
    )
    for identity in required:
        if identity not in combined:
            errors.append(f"third-handshake identity missing: {identity}")
    if f"Candidate method definition identity | `{METHOD_DEFINITION_COMMIT}`" not in registry:
        errors.append("registry MethodDefinitionCommit differs from the controlled method definition")
    if "platform state `COMMENTED`; body outcome `APPROVE`" not in evidence:
        errors.append("human review platform/body outcomes are not separately truthful")
    if "Post-merge control state | `NONE`" not in evidence:
        errors.append("post-merge control state is missing or substituted")
    if "annotated release tag | `v4.3`" not in registry:
        errors.append("registry does not identify v4.3 as the actual annotated release tag")
    if "Candidate overall disposition | `REVIEWED-COMPATIBLE-WITH-QUALIFICATION`" not in disposition:
        errors.append("candidate overall disposition is absent or not qualified")
    candidate_match = re.search(r"Candidate overall disposition \| `([^`]+)`", disposition)
    if not candidate_match or candidate_match.group(1) not in ALLOWED_CANDIDATE_DISPOSITIONS:
        errors.append("candidate overall disposition is outside the allowed vocabulary")
    if "Candidate overall disposition | `REVIEWED-COMPATIBLE`" in disposition:
        errors.append("unqualified REVIEWED-COMPATIBLE is prohibited for this handshake")
    if "Active formal compatibility before approval/merge | `NOT-DETERMINED`" not in disposition:
        errors.append("Draft compatibility was promoted before independent review/merge")
    qualification_ids = set(re.findall(r"(?m)^\| (Q-\d{2}) \|", disposition))
    if qualification_ids != {f"Q-{number:02d}" for number in range(1, 10)}:
        errors.append(f"qualification population differs: {sorted(qualification_ids)}")
    if "Project Configuration | `TMP-PC-ARINC615A-01`; `NOT YET ESTABLISHED`" not in registry:
        errors.append("Project Configuration was established without controlled values")
    if "Evaluation protocol |" not in registry or "`NOT-EXERCISED`" not in registry:
        errors.append("instance evaluation state is missing or promoted")
    if "`NOT AVAILABLE — MIGRATION-ONLY REVIEW`" not in evidence:
        errors.append("missing execution manifest was not explicitly recorded")
    if "v4.3` is the only release tag" not in contract:
        errors.append("baseline ID and actual v4.3 release tag are not separated")
    for path, digest in SOURCE_SHA256.items():
        if path not in evidence or digest not in evidence:
            errors.append(f"source inventory/hash missing: {path}")
    return errors


def protected_delta_errors() -> list[str]:
    errors: list[str] = []
    base_ref = os.environ.get("GITHUB_BASE_REF")
    candidates = [f"origin/{base_ref}" if base_ref else "origin/main", METHOD_DEFINITION_COMMIT]
    base = next((candidate for candidate in candidates if _rev_exists(candidate)), None)
    if base is None:
        return ["cannot resolve a base for protected-diff validation"]
    changed = git("diff", "--name-only", f"{base}...HEAD").splitlines()
    for name in changed:
        if any(name == prefix or name.startswith(prefix) for prefix in PROTECTED_PREFIXES):
            errors.append(f"protected file changed in third-handshake delta: {name}")
    return errors


def _rev_exists(revision: str) -> bool:
    return subprocess.run(
        ["git", "rev-parse", "--verify", revision], cwd=ROOT,
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False,
    ).returncode == 0


def document_structure_errors() -> tuple[list[str], int, int]:
    errors: list[str] = []
    checked_links = 0
    checked_tables = 0
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
            resolved = (path.parent / dependency).resolve()
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                errors.append(f"{relative}: dependency escapes repository {dependency}")
                continue
            if not resolved.exists():
                errors.append(f"{relative}: missing dependency {dependency}")
        if CONFLICT_RE.search(text):
            errors.append(f"{relative}: conflict marker")
        for match in LINK_RE.finditer(text):
            target = local_link_target(match.group(1))
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
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
            elif not in_fence and line.startswith("|") and line.endswith("|"):
                width = table_width(line)
                if expected_width == 0:
                    expected_width = width
                    checked_tables += 1
                elif width != expected_width:
                    errors.append(f"{relative}:{number}: table width {width}, expected {expected_width}")
            else:
                expected_width = 0
    return errors, checked_links, checked_tables


def hygiene_errors() -> list[str]:
    errors: list[str] = []
    tracked = git("ls-files").splitlines()
    prohibited_suffixes = {".pdf", ".patch", ".tmp", ".bak", ".orig", ".swp"}
    credential_names = {".env", "credentials.json", "secrets.json", "id_rsa", "id_ed25519"}
    secret_patterns = {
        "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
        "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
        "GitHub token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b"),
    }
    for name in tracked:
        path = Path(name)
        lower_name = name.lower()
        if path.suffix.lower() in prohibited_suffixes:
            errors.append(f"tracked prohibited artefact: {name}")
        if path.name.lower() in credential_names or lower_name.endswith(("~", ".backup")):
            errors.append(f"tracked temporary/credential artefact: {name}")
        if "extract" in path.name.lower() and path.suffix.lower() in {".txt", ".md"}:
            errors.append(f"tracked extraction artefact: {name}")
        full = ROOT / name
        if not full.is_file() or full.stat().st_size > 1_000_000:
            continue
        try:
            text = full.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if name != "scripts/check_repository_integrity.py" and re.search(
            r"(?:C:\\Users\\|[A-Za-z]:\\Project\\|file://|/home/[^/]+/)", text
        ):
            errors.append(f"tracked text exposes a machine/private path: {name}")
        for label, pattern in secret_patterns.items():
            if pattern.search(text):
                errors.append(f"tracked content resembles {label}: {name}")
    return errors


def main() -> int:
    errors: list[str] = []
    for relative in REQUIRED_DOCUMENTS:
        if not (ROOT / relative).is_file():
            errors.append(f"missing required document: {relative}")

    structure, checked_links, checked_tables = document_structure_errors()
    errors.extend(structure)

    mapping = read("docs/08_validation/arinc_615a_object_mapping_register.md")
    evidence = read("docs/08_validation/arinc_615a_v43_migration_evidence_return.md")
    disposition = read("docs/08_validation/arinc_615a_third_handshake_compatibility_disposition.md")
    registry = read("docs/08_validation/instance_registry.md")
    contract = read("docs/08_validation/cross_repository_instance_contract.md")
    errors.extend(mapping_errors(mapping))
    errors.extend(third_handshake_document_errors(evidence, disposition, registry, contract))

    combined = "\n".join(
        path.read_text(encoding="utf-8") for path in CONTROLLED_FILES if path.exists()
    )
    forbidden = {
        "PICS direct equivalence": ("pics→verification basis", "pics -> verification basis", "pics = verification basis"),
        "Verdict direct equivalence": ("verdict→oracle", "verdict -> oracle", "verdict = oracle"),
        "PASS auto-promotion": ("pass → objective satisfied", "pass→objective satisfied", "pass → compliance", "pass→compliance"),
    }
    lower = combined.lower()
    for label, phrases in forbidden.items():
        if any(phrase in lower for phrase in phrases):
            errors.append(f"prohibited semantic shortcut: {label}")

    protocol = read("docs/08_validation/arinc_615a_instance_evaluation_protocol.md")
    if "| scalability |" not in protocol or "tested ranges only" not in protocol:
        errors.append("evaluation protocol lacks bounded scalability")
    if "specified-binding contract checks satisfied/qualified/not satisfied" not in protocol:
        errors.append("interface conclusion exceeds contract-check scope")

    rq = read("docs/00_overview/research_questions.md")
    if len(re.findall(r"\*\*Status:\*\* Open", rq)) != 8:
        errors.append("RQ1–RQ8 are not all Open")
    architecture = read("ARCHITECTURE.md")
    progress = read("HANDOFF/current_progress.md")
    next_plan = read("HANDOFF/next_plan.md")
    if "OPEN-CANDIDATE" not in architecture or "OPEN-CANDIDATE" not in progress:
        errors.append("OPEN-CANDIDATE maturity boundary is missing")
    if "| `INSTANCE-EXERCISED` |" in architecture:
        errors.append("INSTANCE-EXERCISED must not be an Architecture maturity row")
    if "### Instance evaluation state" not in architecture or "orthogonal state dimension" not in architecture:
        errors.append("orthogonal instance-evaluation contract is missing")
    if "ISO/IEC/IEEE 15289:2019" not in next_plan or "Current research stop" not in next_plan:
        errors.append("Task 001 / ISO 15289 current research stop is missing")

    impact = read("docs/01_normative_foundation/consolidation/architecture_impact_register.md")
    if impact.count("| `GOV-INSIGHT-GVS-INSTANCE-SEPARATION` |") != 1:
        errors.append("GOV-INSIGHT-GVS-INSTANCE-SEPARATION is missing or duplicated")

    errors.extend(hygiene_errors())
    errors.extend(protected_delta_errors())
    try:
        if git("rev-parse", "research-baseline/v0.2^{}") != V02_TAG_COMMIT:
            errors.append("research-baseline/v0.2 tag target changed")
    except subprocess.CalledProcessError:
        errors.append("research-baseline/v0.2 tag unavailable")

    if errors:
        print("Repository integrity check: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Repository integrity check: PASS")
    print(f"- controlled Markdown files: {len(CONTROLLED_FILES)}")
    print(f"- resolved local links: {checked_links}")
    print(f"- Markdown tables checked: {checked_tables}")
    print(f"- MethodDefinitionCommit: {METHOD_DEFINITION_COMMIT}")
    print(f"- ARINC v4.3 release commit/tag: {ARINC_V43_MERGE_COMMIT} / {ARINC_V43_RELEASE_TAG}")
    print("- mapping populations: 18 source + 7 instance-only")
    print("- formal compatibility: NOT-DETERMINED; candidate disposition review pending")
    print("- Project Configuration / instance evaluation: NOT YET ESTABLISHED / NOT-EXERCISED")
    print("- framework semantic automation: not performed")
    return 0


if __name__ == "__main__":
    sys.exit(main())

