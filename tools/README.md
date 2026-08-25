---
title: Tools Workspace
status: planned
version: 0.2
baseline: post-v0.2
owner: research
last_updated: 2026-08-25
dependencies:
  - ../docs/00_overview/roadmap.md
  - ../docs/02_verification_framework/generic_verification_suite_core.md
  - ../docs/08_validation/cross_repository_instance_contract.md
---

# Tools

**Purpose:** future traceability, coverage, impact-analysis, model-validation and document-generation research tools.

**Dependency:** stable information models and independently reviewed Framework Rules.

**Status:** Planned. Framework semantic automation remains prohibited before the relevant information-model, schema and architecture gates.

The repository-governance checker at `scripts/check_repository_integrity.py` is a bounded exception: it validates repository-local links, front matter, Markdown tables, temporary mapping metadata, immutable reference formats and prohibited repository artefacts. It does **not** implement or evaluate Framework Rules, traceability semantics, coverage, Oracle correctness, evidence sufficiency, certification acceptance or instance compatibility.
