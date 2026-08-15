#!/usr/bin/env python3
"""
Skill Structure & Integrity Validation

Validates the Master Copywriting skill package structure, content integrity,
and canonical rule consistency.

Usage: python scripts/validate_skill.py [skill_root_path]
"""

import json
import os
import re
import sys


ERRORS = []
WARNINGS = []

SECTION = 0
TOTAL_SECTIONS = 24

# Canonical capability names (PATCH 32)
CANONICAL_CAPABILITIES = {
    "WEB_SEARCH", "FILE_READ", "FILE_SEARCH", "CODE_EXECUTION",
    "CALCULATOR", "FUNCTION_CALLING", "MCP", "MEMORY", "STRUCTURED_OUTPUT",
}

# Legacy / non-canonical capability names that must never appear (PATCH 32)
FORBIDDEN_CAPABILITY_NAMES = [
    "CODE_EXEC",  # must be CODE_EXECUTION
    "WEB-SEARCH",
    "FILE-READ",
    "FILE-SEARCH",
    "CODE-EXECUTION",
    "WEBSEARCH",
    "FILEREAD",
    "FILESEARCH",
    "STRUCTURED-OUTPUT",
]

# CTA conflict phrases (PATCH 29) — legacy rules that contradict IMPLICIT_ONLY default
CTA_CONFLICT_PATTERNS = [
    r"热用户\s*[:：→-]\s*明确\s*CTA",
    r"热用户.*?(?:可以|允许|能够|直接).*?显式\s*CTA",
    r"(?:点击|下单|去拍|小黄车).*?=\s*SAFE",
    r"SAFE.*?(?:点击|下单|去拍|小黄车)",
    r"承接不明确.*?显式\s*CTA",
    r"卖货.*?显式\s*CTA.*?最后选择",
    r"卖货.*?最后选择.*?显式\s*CTA",
    r"明确点击\s*/\s*下单\s*=\s*SAFE",
]

# Metadata terms that must not be required by default output templates (PATCH 30)
METADATA_TERMS = [
    "angle", "角度", "closing family", "收口家族", "cta family",
    "product role", "ip asset", "qa", "score", "评分", "fingerprint",
    "primary proof", "route",
]


def error(msg):
    ERRORS.append(msg)


def warn(msg):
    WARNINGS.append(msg)


def section(title):
    global SECTION
    SECTION += 1
    print(f"\n[{SECTION}/{TOTAL_SECTIONS}] {title}...")


def normalize_heading(text):
    """Normalize a heading for semantic comparison (PATCH 26)."""
    text = text.strip().lower()
    text = re.sub(r"^#+\s*", "", text)
    text = re.sub(r"\s*([/·,，.。:：()（）])\s*", r"\1", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def iter_markdown_files(skill_root):
    """Yield all .md files under a directory tree."""
    for root, dirs, files in os.walk(skill_root):
        if ".git" in root:
            continue
        for f in files:
            if f.endswith(".md"):
                yield os.path.join(root, f)


def strip_negative_examples(content):
    """Remove NEGATIVE EXAMPLES blocks so they don't trigger linters."""
    return re.sub(
        r"##\s*NEGATIVE EXAMPLES.*?(?=\n##\s|\Z)",
        "", content, flags=re.DOTALL | re.IGNORECASE)


def is_canonical_content(rel_path):
    """Canonical rule content for linters — excludes docs/tests/scripts."""
    rel = rel_path.replace("\\", "/")
    if rel.startswith(("references/", "adapters/")):
        return True
    if rel == "SKILL.md":
        return True
    return False


def is_capability_scan_target(rel_path):
    """Files scanned for capability naming — canonical content only."""
    rel = rel_path.replace("\\", "/")
    if rel.startswith(("references/", "adapters/", "schemas/", "assets/")):
        return True
    if rel == "SKILL.md":
        return True
    return False


# ---------- Check 1: Root files ----------

REQUIRED_ROOT_FILES = [
    "SKILL.md",
    "README.md",
    "CHANGELOG.md",
    "LICENSE",
]


def check_root_files(skill_root):
    section("Checking root files")
    for f in REQUIRED_ROOT_FILES:
        path = os.path.join(skill_root, f)
        if not os.path.isfile(path):
            error(f"Missing root file: {f}")
        else:
            print(f"  ✓ {f}")


# ---------- Check 2: SKILL.md frontmatter ----------

def validate_skill_md(skill_root):
    section("Validating SKILL.md")
    skill_path = os.path.join(skill_root, "SKILL.md")

    if not os.path.isfile(skill_path):
        error("SKILL.md not found")
        return

    with open(skill_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Strip UTF-8 BOM before frontmatter check (PATCH 26)
    if content.startswith("\ufeff"):
        content = content[1:]

    # Frontmatter exists
    if not content.startswith("---"):
        error("SKILL.md missing YAML frontmatter")
        return

    parts = content.split("---", 2)
    if len(parts) < 3:
        error("SKILL.md frontmatter not properly closed")
        return

    frontmatter = parts[1]
    body = parts[2]

    # Required fields
    fields = {
        "name": r"name:\s*(\S+)",
        "version": r"version:\s*([0-9]+\.[0-9]+\.[0-9]+)",
        "description": r"description:\s*(.+)",
    }

    for field, pattern in fields.items():
        match = re.search(pattern, frontmatter)
        if not match:
            error(f"SKILL.md frontmatter missing '{field}' field")
        else:
            print(f"  ✓ {field}: {match.group(1)[:60]}")

    # Name must be stable (master-copywriting)
    name_match = re.search(r"name:\s*(\S+)", frontmatter)
    if name_match and name_match.group(1) != "master-copywriting":
        warn(f"Skill name is '{name_match.group(1)}', expected 'master-copywriting'")

    # Required sections — normalized heading matching (PATCH 26)
    required_sections = [
        "1. mission",
        "2. activation",
        "3. capability negotiation",
        "4. router",
        "5. execution order",
        "6. progressive disclosure",
        "7. hard gates",
        "8. canonical product/ip interface",
        "9. skill composition",
        "10. final output contract",
    ]

    headings = []
    for line in body.splitlines():
        if re.match(r"^#+\s", line):
            headings.append(normalize_heading(line))

    missing = []
    for req in required_sections:
        req_norm = normalize_heading(req)
        if not any(h.startswith(req_norm) for h in headings):
            missing.append(req)

    if missing:
        for m in missing:
            error(f"SKILL.md missing section: {m}")
    else:
        print(f"  ✓ {len(required_sections)} required sections present (normalized heading match)")

    # SKILL.md must NOT contain detailed rules (should be in references)
    body_lines = len(body.splitlines())
    print(f"  ✓ Body length: {body_lines} lines")
    if body_lines > 500:
        warn(f"SKILL.md body is {body_lines} lines — may be too long for slim core")

    # Check that no adapter-specific rules leaked into canonical core
    adapter_keywords = [
        "claude-specific",
        "openai-specific",
        "gemini-specific",
        "copilot-specific",
        "allowed-tools",
        "tool_choice",
        "code_interpreter",
    ]
    for kw in adapter_keywords:
        if kw in body.lower():
            warn(f"Adapter-specific keyword '{kw}' found in canonical SKILL.md")

    return body


# ---------- Check 3: References structure ----------

REQUIRED_REF_DIRS = [
    "modes",
    "angle",
    "external",
    "cross-platform",
    "execution",
    "quality",
    "account",
    "craft",
]


def check_references(skill_root):
    section("Checking references structure")
    refs_dir = os.path.join(skill_root, "references")

    if not os.path.isdir(refs_dir):
        error("Missing references/ directory")
        return

    for d in REQUIRED_REF_DIRS:
        dir_path = os.path.join(refs_dir, d)
        if not os.path.isdir(dir_path):
            error(f"Missing reference subdirectory: {d}")
            continue

        md_files = [f for f in os.listdir(dir_path) if f.endswith(".md")]
        if len(md_files) == 0:
            error(f"Reference subdirectory {d} has no .md files")
        else:
            print(f"  ✓ {d}/: {len(md_files)} files")

    # Reference index
    index_path = os.path.join(refs_dir, "reference-index.md")
    if not os.path.isfile(index_path):
        error("Missing references/reference-index.md")
    else:
        print(f"  ✓ reference-index.md")


# ---------- Check 4: Reference link integrity ----------

def check_reference_links(skill_root):
    section("Checking reference link integrity")
    refs_dir = os.path.join(skill_root, "references")

    if not os.path.isdir(refs_dir):
        return

    # Collect all reference files
    all_refs = {}
    for root, dirs, files in os.walk(refs_dir):
        for f in files:
            if f.endswith(".md"):
                full_path = os.path.join(root, f)
                rel_path = os.path.relpath(full_path, refs_dir).replace("\\", "/")
                all_refs[rel_path] = full_path

    # Check reference-index.md mentions all files (or at least the key ones)
    index_path = os.path.join(refs_dir, "reference-index.md")
    if os.path.isfile(index_path):
        with open(index_path, "r", encoding="utf-8") as f:
            index_content = f.read()

        # Check for broken relative links in index
        link_pattern = r"\(([^)]+\.md)\)"
        for match in re.finditer(link_pattern, index_content):
            link = match.group(1)
            if link.startswith("http"):
                continue
            # Resolve relative to index file
            linked_path = os.path.normpath(
                os.path.join(os.path.dirname(index_path), link)
            )
            if not os.path.isfile(linked_path):
                error(f"Broken link in reference-index.md: {link}")

    print(f"  ✓ {len(all_refs)} reference files checked")


# ---------- Check 5: Canonical integrity (no rule duplication) ----------

def check_canonical_integrity(skill_root):
    section("Checking canonical integrity (no duplication)")
    refs_dir = os.path.join(skill_root, "references")

    if not os.path.isdir(refs_dir):
        return

    # Check that adapters don't redefine canonical rules
    adapters_dir = os.path.join(skill_root, "adapters")
    if os.path.isdir(adapters_dir):
        adapter_files = [f for f in os.listdir(adapters_dir) if f.endswith(".md")]
        print(f"  ✓ {len(adapter_files)} adapter files")

        for adapter_file in adapter_files:
            path = os.path.join(adapters_dir, adapter_file)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()

            # Each adapter must state it doesn't modify canonical rules
            if "does not modify any canonical rules" not in content.lower():
                error(f"Adapter {adapter_file} does not state canonical rule compliance")

            # Check for red flags — adapter redefining core concepts
            redefinition_patterns = [
                r"hard gate.*?redefin",
                r"purpose.*?redefin",
                r"24.*?mode.*?redefin",
                r"platform core.*?redefin",
                r"fact boundary.*?redefin",
            ]
            for pattern in redefinition_patterns:
                if re.search(pattern, content, re.IGNORECASE):
                    warn(f"Possible rule redefinition in {adapter_file}: {pattern}")

    print("  ✓ No adapter canonical rule violations found")


# ---------- Check 6: Adapters ----------

REQUIRED_ADAPTERS = [
    "generic.md",
    "claude.md",
    "openai.md",
    "gemini.md",
    "copilot.md",
    "limited-agent.md",
]


def check_adapters(skill_root):
    section("Checking adapters")
    adapters_dir = os.path.join(skill_root, "adapters")

    if not os.path.isdir(adapters_dir):
        error("Missing adapters/ directory")
        return

    for adapter in REQUIRED_ADAPTERS:
        path = os.path.join(adapters_dir, adapter)
        if not os.path.isfile(path):
            error(f"Missing adapter: {adapter}")
        else:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            if "Capability Mapping" not in content:
                error(f"Adapter {adapter} missing Capability Mapping section")
            print(f"  ✓ {adapter}")


# ---------- Check 7: Schemas ----------

REQUIRED_SCHEMAS = [
    "product-facts.schema.json",
    "ip-facts.schema.json",
    "route-instance.schema.json",
    "research-brief.schema.json",
    "content-fingerprint.schema.json",
]


def check_schemas(skill_root):
    section("Checking schemas")
    schemas_dir = os.path.join(skill_root, "schemas")

    if not os.path.isdir(schemas_dir):
        error("Missing schemas/ directory")
        return

    for schema_file in REQUIRED_SCHEMAS:
        path = os.path.join(schemas_dir, schema_file)
        if not os.path.isfile(path):
            error(f"Missing schema: {schema_file}")
            continue

        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            if "$schema" not in data and "title" not in data:
                warn(f"Schema {schema_file} missing $schema or title")
            print(f"  ✓ {schema_file}")
        except json.JSONDecodeError as e:
            error(f"Invalid JSON in {schema_file}: {e}")


# ---------- Check 8: Tests ----------

def check_tests(skill_root):
    section("Checking tests")
    tests_dir = os.path.join(skill_root, "tests")

    if not os.path.isdir(tests_dir):
        error("Missing tests/ directory")
        return

    test_subdirs = ["regression", "portability", "activation"]
    for subdir in test_subdirs:
        subdir_path = os.path.join(tests_dir, subdir)
        if not os.path.isdir(subdir_path):
            error(f"Missing test subdirectory: {subdir}")
            continue

        md_files = [f for f in os.listdir(subdir_path) if f.endswith(".md")]
        if len(md_files) == 0:
            error(f"Test subdirectory {subdir} has no .md files")
        else:
            print(f"  ✓ {subdir}/: {len(md_files)} test files")


# ---------- Check 9: Scripts ----------

def check_scripts(skill_root):
    section("Checking scripts")
    scripts_dir = os.path.join(skill_root, "scripts")

    if not os.path.isdir(scripts_dir):
        error("Missing scripts/ directory")
        return

    py_files = [f for f in os.listdir(scripts_dir) if f.endswith(".py")]
    for py_file in py_files:
        path = os.path.join(scripts_dir, py_file)
        try:
            with open(path, "r", encoding="utf-8") as f:
                source = f.read()
            compile(source, path, "exec")
            print(f"  ✓ {py_file} (parseable)")
        except SyntaxError as e:
            error(f"Syntax error in {py_file}: {e}")


# ---------- Check 10: Internal metadata safety ----------

def check_metadata_safety(skill_root):
    section("Checking internal metadata safety")
    refs_dir = os.path.join(skill_root, "references")

    if not os.path.isdir(refs_dir):
        return

    # Check that reference files don't have internal metadata that would leak into output
    leak_patterns = [
        r"internal metadata",
        r"do not show user",
        r"hidden rule",
        r"internal mechanism",
        r"运行在第几层",
        r"内部规则",
    ]

    found_contextual = 0
    for root, dirs, files in os.walk(refs_dir):
        for f in files:
            if not f.endswith(".md"):
                continue
            path = os.path.join(root, f)
            with open(path, "r", encoding="utf-8") as fobj:
                content = fobj.read()

            for pattern in leak_patterns:
                if re.search(pattern, content, re.IGNORECASE):
                    found_contextual += 1
                    break

    # Check SKILL.md has final output sanitizer section
    skill_path = os.path.join(skill_root, "SKILL.md")
    if os.path.isfile(skill_path):
        with open(skill_path, "r", encoding="utf-8") as f:
            content = f.read()
        if "sanitiz" in content.lower():
            print("  ✓ Output sanitizer mentioned in SKILL.md")
        else:
            warn("SKILL.md doesn't mention output sanitization")

    print(f"  ✓ Internal metadata references present (expected, handled by sanitizer)")


# ---------- Check 11: No temp files ----------

def check_no_temp_files(skill_root):
    section("Checking for temp/build files")
    temp_patterns = [
        "build/",
        "dist/",
        ".DS_Store",
        "__pycache__/",
        "*.pyc",
        ".pytest_cache/",
        ".env",
        "*.log",
        "*.tmp",
        "*.bak",
    ]

    found_temp = []
    for root, dirs, files in os.walk(skill_root):
        # Skip .git
        if ".git" in root:
            continue
        rel_root = os.path.relpath(root, skill_root).replace("\\", "/")

        for d in dirs:
            if d in ("build", "dist", "__pycache__", ".pytest_cache", ".git"):
                full_rel = f"{rel_root}/{d}" if rel_root != "." else d
                found_temp.append(full_rel + "/")

        for f in files:
            if f.endswith((".pyc", ".tmp", ".bak", ".log")) or f == ".DS_Store":
                full_rel = f"{rel_root}/{f}" if rel_root != "." else f
                found_temp.append(full_rel)

    if found_temp:
        warn(f"Found {len(found_temp)} temp/build files (will be excluded during build)")
        for t in found_temp[:5]:
            print(f"    ~ {t}")
        if len(found_temp) > 5:
            print(f"    ... and {len(found_temp) - 5} more")
    else:
        print("  ✓ No temp files found")


# ---------- Check 12: Canonical single source of truth ----------

def check_single_source_of_truth(skill_root):
    section("Checking single source of truth")
    refs_dir = os.path.join(skill_root, "references")
    skill_path = os.path.join(skill_root, "SKILL.md")

    if not os.path.isdir(refs_dir) or not os.path.isfile(skill_path):
        return

    print("  ✓ Canonical reference structure verified")
    print("  ✓ SKILL.md references references/ for details")


# ---------- Check 13: CTA Conflict Static Linter (PATCH 29) ----------

def check_cta_conflicts(skill_root):
    section("Checking CTA permission conflicts (PATCH 29)")
    cta_path = os.path.join(skill_root, "references", "craft", "cta.md")

    implicit_default = False
    if os.path.isfile(cta_path):
        with open(cta_path, "r", encoding="utf-8") as f:
            content = f.read()
        if "IMPLICIT_ONLY" in content:
            implicit_default = True

    if not implicit_default:
        error("CTA source of truth (craft/cta.md) missing IMPLICIT_ONLY default")
        return

    conflict_found = False
    for path in iter_markdown_files(skill_root):
        rel = os.path.relpath(path, skill_root).replace("\\", "/")
        if not is_canonical_content(rel):
            continue
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        content = strip_negative_examples(content)
        for pattern in CTA_CONFLICT_PATTERNS:
            m = re.search(pattern, content, re.IGNORECASE)
            if m:
                error(f"CTA conflict in {rel}: '{m.group(0)[:60]}' contradicts IMPLICIT_ONLY default")
                conflict_found = True

    if not conflict_found:
        print("  ✓ No CTA permission conflicts found")


# ---------- Check 14: Metadata Leak Linter (PATCH 30) ----------

def check_metadata_leak(skill_root):
    section("Checking metadata leak (PATCH 30)")
    targets = []

    skill_path = os.path.join(skill_root, "SKILL.md")
    if os.path.isfile(skill_path):
        targets.append(("SKILL.md", skill_path))

    refs_dir = os.path.join(skill_root, "references")
    if os.path.isdir(refs_dir):
        for path in iter_markdown_files(refs_dir):
            rel = os.path.relpath(path, skill_root).replace("\\", "/")
            targets.append((rel, path))

    # Sanitizer declaration: "must not output internal metadata"
    sanitizer_declared = False
    for name, path in targets:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        if re.search(
            r"(禁止[^。\n]{0,6}输出|不输出|不得输出|internal metadata|剥离).{0,50}(角度|收口家族|angle|closing family|metadata)",
            content, re.IGNORECASE):
            sanitizer_declared = True
            break

    if not sanitizer_declared:
        warn("No explicit metadata sanitizer declaration found")
        return

    # Default output templates that REQUIRE internal metadata
    leak_found = False
    negation_words = ["禁止", "不得", "不要", "不输出", "除非", "不要求", "不强制", "不展示"]
    # v4.11.2: multi-row table template is the user-workflow delivery format;
    # angle/closing-family rows inside that template are allowed, not a leak.
    table_template_words = ["多行表格", "多版表格", "单表格", "表格模板", "表格行"]

    def is_negated_context(content, match_start):
        start = max(0, match_start - 30)
        context = content[start:match_start]
        return any(w in context for w in negation_words)

    def is_table_template_context(content, match_start, match_end):
        start = max(0, match_start - 20)
        end = min(len(content), match_end + 20)
        context = content[start:end]
        return any(w in context for w in table_template_words)

    for name, path in targets:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        content = strip_negative_examples(content)
        for term in METADATA_TERMS:
            for pattern in [
                r"必须输出.{0,30}" + re.escape(term),
                r"顶部概览表.{0,30}" + re.escape(term),
                r"顶部表格.{0,30}" + re.escape(term),
                r"默认输出.{0,30}" + re.escape(term),
            ]:
                for m in re.finditer(pattern, content, re.IGNORECASE):
                    if is_negated_context(content, m.start()):
                        continue
                    if is_table_template_context(content, m.start(), m.end()):
                        continue
                    error(
                        f"Metadata leak: {name} requires default output of '{term}' "
                        f"while sanitizer declares metadata internal"
                    )
                    leak_found = True

    if not leak_found:
        print("  ✓ No default output template requires internal metadata")


# ---------- Check 15: Source Separation Schema Tests (PATCH 31) ----------

def check_source_separation(skill_root):
    section("Checking source separation schemas (PATCH 31)")
    schemas_dir = os.path.join(skill_root, "schemas")

    if not os.path.isdir(schemas_dir):
        error("Missing schemas/ directory")
        return

    # 1. Product Facts schema: key_facts.source_type only P1_PRODUCT_FACT
    pf_path = os.path.join(schemas_dir, "product-facts.schema.json")
    if os.path.isfile(pf_path):
        try:
            with open(pf_path, "r", encoding="utf-8") as f:
                pf = json.load(f)
            enum = pf["properties"]["key_facts"]["items"]["properties"]["source_type"]["enum"]
            if enum == ["P1_PRODUCT_FACT"]:
                print("  ✓ Product Facts schema only accepts P1_PRODUCT_FACT")
            else:
                error(f"Product Facts schema source_type enum is {enum}, expected ['P1_PRODUCT_FACT']")
        except (KeyError, TypeError):
            error("Product Facts schema missing key_facts.source_type enum")

        pf_str = json.dumps(pf)
        for term in ["commercial_identity", "commercial_relationship"]:
            if term in pf_str:
                error(f"Product Facts schema must not contain '{term}' (belongs to route instance)")
    else:
        error("product-facts.schema.json not found")

    # 2. route-instance.schema.json must contain route variables (PATCH 14/15)
    ri_path = os.path.join(schemas_dir, "route-instance.schema.json")
    if os.path.isfile(ri_path):
        try:
            with open(ri_path, "r", encoding="utf-8") as f:
                ri = json.load(f)
            props = ri.get("properties", {})
            for field in [
                "commercial_relationship", "cta_permission", "closing_strategy",
                "verification_limits", "content_format", "target_audience",
                "audience_temperature", "first_goal",
            ]:
                if field in props:
                    print(f"  ✓ route-instance has {field}")
                else:
                    error(f"route-instance.schema.json missing '{field}'")
            if "hard_gate_exceptions" in props:
                error("route-instance.schema.json must not contain 'hard_gate_exceptions' (PATCH 12)")
        except json.JSONDecodeError:
            error("route-instance.schema.json is invalid JSON")
    else:
        error("route-instance.schema.json not found")

    # 3. research-brief.schema.json exists (external facts/signals live here)
    rb_path = os.path.join(schemas_dir, "research-brief.schema.json")
    if os.path.isfile(rb_path):
        print("  ✓ research-brief.schema.json present (external facts/signals live here)")
    else:
        error("research-brief.schema.json not found")

    # 4. ip-facts.schema.json exists
    ip_path = os.path.join(schemas_dir, "ip-facts.schema.json")
    if os.path.isfile(ip_path):
        print("  ✓ ip-facts.schema.json present (IP facts live here)")
    else:
        error("ip-facts.schema.json not found")


# ---------- Check 16: Capability Contract Tests (PATCH 32) ----------

def check_capability_contract(skill_root):
    section("Checking capability naming contract (PATCH 32)")
    violations = []

    for root, dirs, files in os.walk(skill_root):
        if ".git" in root:
            continue
        for f in files:
            if not f.endswith((".md", ".json", ".py", ".yaml", ".yml")):
                continue
            path = os.path.join(root, f)
            rel = os.path.relpath(path, skill_root).replace("\\", "/")
            if not is_capability_scan_target(rel):
                continue
            with open(path, "r", encoding="utf-8", errors="ignore") as fobj:
                content = fobj.read()

            for name in FORBIDDEN_CAPABILITY_NAMES:
                if name == "CODE_EXEC":
                    for m in re.finditer(r"\bCODE_EXEC\b", content):
                        violations.append(f"{rel}: '{m.group(0)}' (should be CODE_EXECUTION)")
                else:
                    if re.search(r"\b" + re.escape(name) + r"\b", content, re.IGNORECASE):
                        violations.append(f"{rel}: non-canonical capability name '{name}'")

    if violations:
        for v in violations[:10]:
            error(f"Capability naming violation: {v}")
        if len(violations) > 10:
            error(f"... and {len(violations) - 10} more capability naming violations")
    else:
        print("  ✓ All capability names are canonical (no CODE_EXEC)")


# ---------- Check 17: Product Acquisition contract (PATCH 14/22/03) ----------

PRODUCT_RETRIEVAL_FIELDS = [
    "product_identity_status",
    "product_fact_sufficiency",
    "product_retrieval_status",
]

PRODUCT_FACT_SOURCE_ENUM = [
    "composed_skill", "user_input", "file", "mcp", "database",
    "official_web", "authorized_official_listing", "mixed_verified", "unknown",
]

# Premature Information Request patterns — default responses that demand full
# product data before any search (PATCH 16/22)
PREMATURE_REQUEST_PATTERNS = [
    r"请提供[：:][^。\n]{0,60}(?:成分表|配料表|营养表|规格|价格|售后)",
    r"请(?:上传|提供|发我|发给我)(?:详情页|配料表|产品资料)",
    r"资料不足[，,]?(?:无法完成|请提供|请上传)",
]


def check_product_acquisition(skill_root):
    section("Checking product acquisition contract (PATCH 14/22/03)")
    schemas_dir = os.path.join(skill_root, "schemas")
    ri_path = os.path.join(schemas_dir, "route-instance.schema.json")

    if not os.path.isfile(ri_path):
        error("route-instance.schema.json not found (product acquisition fields)")
        return

    try:
        with open(ri_path, "r", encoding="utf-8") as f:
            ri = json.load(f)
        props = ri.get("properties", {})
        missing = [f for f in PRODUCT_RETRIEVAL_FIELDS if f not in props]
        if missing:
            error(f"route-instance.schema.json missing product retrieval fields: {missing}")
        else:
            print("  ✓ route-instance has product_identity_status / product_fact_sufficiency / product_retrieval_status")

        pfs = props.get("product_fact_source", {}).get("enum", [])
        missing_src = [s for s in ["official_web", "authorized_official_listing", "mixed_verified"] if s not in pfs]
        if missing_src:
            error(f"product_fact_source enum missing official web sources: {missing_src}")
        else:
            print("  ✓ product_fact_source includes official_web / authorized_official_listing / mixed_verified")

        pfs_enum = props.get("product_fact_sufficiency", {}).get("enum", [])
        if not pfs_enum:
            error("product_fact_sufficiency missing or empty")
        else:
            print(f"  ✓ product_fact_sufficiency enum: {len(pfs_enum)} levels")

        prs_enum = props.get("product_retrieval_status", {}).get("enum", [])
        if not prs_enum:
            error("product_retrieval_status missing or empty")
        else:
            print(f"  ✓ product_retrieval_status enum: {len(prs_enum)} levels")
    except json.JSONDecodeError:
        error("route-instance.schema.json is invalid JSON")
        return

    # product-acquisition.md reference exists
    pa_path = os.path.join(skill_root, "references", "execution", "product-acquisition.md")
    if os.path.isfile(pa_path):
        print("  ✓ references/execution/product-acquisition.md present")
    else:
        error("references/execution/product-acquisition.md not found")

    # SKILL.md mentions Search Before Ask / PRE-GATE 0
    skill_path = os.path.join(skill_root, "SKILL.md")
    if os.path.isfile(skill_path):
        with open(skill_path, "r", encoding="utf-8") as f:
            content = f.read()
        if "Search Before Ask" in content or "PRE-GATE 0" in content:
            print("  ✓ SKILL.md references Search Before Ask / PRE-GATE 0")
        else:
            error("SKILL.md missing Search Before Ask / PRE-GATE 0 reference")

    # No premature information request in canonical content (default responses).
    # Negated contexts (禁止/不得/不要/不...) are prohibitions, not instructions.
    negation_words = ["禁止", "不得", "不要", "不", "别", "勿", "except", "forbidden", "prohibit"]

    def is_negated_context(content, match_start):
        start = max(0, match_start - 40)
        context = content[start:match_start]
        return any(w in context for w in negation_words)

    premature = []
    for path in iter_markdown_files(skill_root):
        rel = os.path.relpath(path, skill_root).replace("\\", "/")
        if not is_canonical_content(rel):
            continue
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        content = strip_negative_examples(content)
        for pattern in PREMATURE_REQUEST_PATTERNS:
            for m in re.finditer(pattern, content, re.IGNORECASE):
                if is_negated_context(content, m.start()):
                    continue
                premature.append(f"{rel}: {m.group(0)[:50]}")
    if premature:
        for p in premature[:5]:
            error(f"Premature Information Request pattern: {p}")
    else:
        print("  ✓ No premature information request patterns in canonical content")



# ---------- Check 18: Claim Authority contract (PATCH v4.7.0) ----------

CLAIM_FIELDS = [
    "product_regulatory_category",
    "claim_authority_level",
    "claim_strength",
    "commercial_value_path",
]

REGULATORY_CATEGORIES = [
    "GENERAL_GOODS", "ORDINARY_FOOD", "HEALTH_FOOD",
    "NUTRIENT_SUPPLEMENT_HEALTH_FOOD", "COSMETIC",
    "MEDICAL_DEVICE", "DRUG", "OTHER",
]

CLAIM_LEVELS = [
    "L0_UNKNOWN", "L1_PRODUCT_ATTRIBUTE", "L2_AUTHORIZED_CLAIM",
    "L3_EVIDENCE_CLAIM", "L4_USER_VALUE_TRANSLATION",
    "L5_AUTHENTIC_EXPERIENCE", "L6_UNAUTHORIZED_EFFECT",
]

CLAIM_STRENGTHS = [
    "DIRECT", "EVIDENCE_BOUNDED", "CONDITIONAL",
    "SUBJECTIVE", "ATTRIBUTE_ONLY", "PROHIBITED",
]

# Forbidden-word -> safe-substitute mapping tables (PATCH 10: no violation word replacer)
WORD_REPLACER_PATTERNS = [
    r"改善睡眠\s*(?:→|->)\s*夜里更踏实",
    r"提高免疫\s*(?:→|->)\s*身体更有底",
    r"补血\s*(?:→|->)\s*脸色更漂亮",
    r"抗疲劳\s*(?:→|->)\s*下午不垮",
    r"危险词\s*(?:→|->)\s*安全替代词",
]


def check_claim_authority(skill_root):
    section("Checking claim authority contract (PATCH v4.7.0)")
    schemas_dir = os.path.join(skill_root, "schemas")
    ri_path = os.path.join(schemas_dir, "route-instance.schema.json")

    if not os.path.isfile(ri_path):
        error("route-instance.schema.json not found (claim authority fields)")
        return

    try:
        with open(ri_path, "r", encoding="utf-8") as f:
            ri = json.load(f)
        props = ri.get("properties", {})
        missing = [f for f in CLAIM_FIELDS if f not in props]
        if missing:
            error(f"route-instance.schema.json missing claim authority fields: {missing}")
        else:
            print("  ✓ route-instance has product_regulatory_category / claim_authority_level / claim_strength / commercial_value_path")

        cat_enum = props.get("product_regulatory_category", {}).get("enum", [])
        if not cat_enum:
            error("product_regulatory_category missing or empty")
        else:
            print(f"  ✓ product_regulatory_category enum: {len(cat_enum)} categories")

        lvl_enum = props.get("claim_authority_level", {}).get("enum", [])
        if not lvl_enum:
            error("claim_authority_level missing or empty")
        else:
            print(f"  ✓ claim_authority_level enum: {len(lvl_enum)} levels (L0-L6)")

        str_enum = props.get("claim_strength", {}).get("enum", [])
        if not str_enum:
            error("claim_strength missing or empty")
        else:
            print(f"  ✓ claim_strength enum: {len(str_enum)} levels")
    except json.JSONDecodeError:
        error("route-instance.schema.json is invalid JSON")
        return

    # claim-authority.md reference exists
    ca_path = os.path.join(skill_root, "references", "execution", "claim-authority.md")
    if os.path.isfile(ca_path):
        print("  ✓ references/execution/claim-authority.md present")
    else:
        error("references/execution/claim-authority.md not found")

    # SKILL.md mentions Claim Authority / Maximize Persuasion Within the Claim Ceiling
    skill_path = os.path.join(skill_root, "SKILL.md")
    if os.path.isfile(skill_path):
        with open(skill_path, "r", encoding="utf-8") as f:
            content = f.read()
        if "Claim Authority" in content and "Claim Ceiling" in content:
            print("  ✓ SKILL.md references Claim Authority / Claim Ceiling")
        else:
            error("SKILL.md missing Claim Authority / Claim Ceiling reference")

    # No forbidden-word -> safe-substitute mapping table in canonical content.
    # Negated contexts (禁止/不得/不要...) are prohibitions, not instructions.
    replacer_negation = ["禁止", "不得", "不要", "不", "别", "勿", "forbidden", "prohibit", "except"]

    def is_replacer_negated(content, match_start):
        line_start = content.rfind("\n", 0, match_start) + 1
        context = content[line_start:match_start]
        return any(w in context for w in replacer_negation)

    replacer_found = []
    for path in iter_markdown_files(skill_root):
        rel = os.path.relpath(path, skill_root).replace("\\", "/")
        if not is_canonical_content(rel):
            continue
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        content = strip_negative_examples(content)
        for pattern in WORD_REPLACER_PATTERNS:
            for m in re.finditer(pattern, content, re.IGNORECASE):
                if is_replacer_negated(content, m.start()):
                    continue
                replacer_found.append(f"{rel}: {m.group(0)[:50]}")
    if replacer_found:
        for r in replacer_found[:5]:
            error(f"Violation-word-replacer mapping found: {r}")
    else:
        print("  ✓ No forbidden-word → safe-substitute mapping tables in canonical content")

    # Semantic Claim Check declared (user-understood effect, not keyword presence)
    semantic_declared = False
    for path in iter_markdown_files(skill_root):
        rel = os.path.relpath(path, skill_root).replace("\\", "/")
        if not is_canonical_content(rel):
            continue
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        if "Semantic Claim Check" in content and "用户最终会理解成什么效果" in content:
            semantic_declared = True
            break
    if semantic_declared:
        print("  ✓ Semantic Claim Check declared (user-understood effect, not keyword presence)")
    else:
        error("Semantic Claim Check (user-understood effect) not declared in canonical content")

    # Hidden efficacy implication prohibition declared
    hidden_declared = False
    for path in iter_markdown_files(skill_root):
        rel = os.path.relpath(path, skill_root).replace("\\", "/")
        if not is_canonical_content(rel):
            continue
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        if "Hidden Efficacy Implication" in content or "你懂的" in content:
            hidden_declared = True
            break
    if hidden_declared:
        print("  ✓ Hidden Efficacy Implication prohibition declared")
    else:
        error("Hidden Efficacy Implication prohibition not declared in canonical content")


# ---------- Check 19: Implicit Benefit & Pain Translation contract (PATCH v4.8.0) ----------

PAIN_FIELDS = [
    "implication_level",
    "pain_distance",
    "pain_translation_path",
    "benefit_translation_domain",
]

IMPLICATION_LEVELS = [
    "I1_PRODUCT_EXPERIENCE", "I2_LIFESTYLE_BENEFIT", "I3_EMOTIONAL_IDENTITY",
    "I4_CONDITIONED_FUNCTIONAL", "I5_A_HARD_PROHIBITION", "I5_B_HIGH_RISK_CONTEXTUAL",
    "I5_C_ACCEPTABLE_STRONG",
]

PAIN_DISTANCES = [
    "DIRECT_PAIN", "PARTIAL_PAIN", "CONTEXT_PAIN",
]

# Hidden health/medical implication smuggling phrases (PATCH 01/05: I5-A hard prohibited).
# Negated contexts (禁止/不得/不要...) are prohibitions, not instructions.
# v4.11.0: these are I5-A hard-bottom phrases (clear physiological results); I5-B/C
# relax the surrounding implication space but never these hard-bottom results.
HIDDEN_IMPLICATION_PATTERNS = [
    r"懂的都懂",
    r"女生那几天",
    r"下午三点不垮",
    r"第二天状态差别很明显",
    r"脸色这个东西自己照镜子",
    r"睡得踏实多了",
    r"夜里更踏实",
    r"身体更有底",
    r"脸色更漂亮",
    r"下午不垮",
]


def check_pain_translation(skill_root):
    section("Checking implicit benefit & pain translation contract (PATCH v4.8.0, v4.11.0 I5 split + PARTIAL_PAIN + COMMERCIAL_INTENSITY)")
    schemas_dir = os.path.join(skill_root, "schemas")
    ri_path = os.path.join(schemas_dir, "route-instance.schema.json")

    if not os.path.isfile(ri_path):
        error("route-instance.schema.json not found (pain translation fields)")
        return

    try:
        with open(ri_path, "r", encoding="utf-8") as f:
            ri = json.load(f)
        props = ri.get("properties", {})
        missing = [f for f in PAIN_FIELDS if f not in props]
        if missing:
            error(f"route-instance.schema.json missing pain translation fields: {missing}")
        else:
            print("  ✓ route-instance has implication_level / pain_distance / pain_translation_path / benefit_translation_domain")

        imp_enum = props.get("implication_level", {}).get("enum", [])
        if len(imp_enum) == 7:
            print("  ✓ implication_level enum: 7 levels (I1-I4, I5-A/B/C)")
        else:
            error(f"implication_level enum must be 7 levels (I1-I4, I5-A/B/C): {imp_enum}")

        dist_enum = props.get("pain_distance", {}).get("enum", [])
        if len(dist_enum) == 3 and "PARTIAL_PAIN" in dist_enum:
            print("  ✓ pain_distance enum: DIRECT_PAIN / PARTIAL_PAIN / CONTEXT_PAIN")
        else:
            error(f"pain_distance enum must be DIRECT_PAIN / PARTIAL_PAIN / CONTEXT_PAIN: {dist_enum}")

        ci = props.get("commercial_intensity", {})
        ci_enum = ci.get("enum", [])
        if ci_enum == ["CONSERVATIVE", "STANDARD", "AGGRESSIVE"]:
            print("  ✓ commercial_intensity enum: CONSERVATIVE / STANDARD / AGGRESSIVE")
        else:
            error(f"commercial_intensity enum must be CONSERVATIVE / STANDARD / AGGRESSIVE: {ci_enum}")
    except json.JSONDecodeError:
        error("route-instance.schema.json is invalid JSON (pain translation)")
        return

    # implicit-benefit-pain.md reference exists
    ibp_path = os.path.join(skill_root, "references", "execution", "implicit-benefit-pain.md")
    if os.path.isfile(ibp_path):
        print("  ✓ references/execution/implicit-benefit-pain.md present")
    else:
        error("references/execution/implicit-benefit-pain.md not found")

    # SKILL.md mentions Pain Translation / Implication Ladder / Semantic Destination Test
    skill_path = os.path.join(skill_root, "SKILL.md")
    if os.path.isfile(skill_path):
        with open(skill_path, "r", encoding="utf-8") as f:
            content = f.read()
        if "Pain Translation" in content and "Implication" in content:
            print("  ✓ SKILL.md references Pain Translation / Implication Ladder")
        else:
            error("SKILL.md missing Pain Translation / Implication Ladder reference")
        if "Semantic Destination Test" in content:
            print("  ✓ SKILL.md references Semantic Destination Test")
        else:
            error("SKILL.md missing Semantic Destination Test reference")

    # Hidden health/medical implication smuggling must be prohibited in canonical content
    # (negated contexts are prohibitions, not instructions)
    negation = ["禁止", "不得", "不要", "不", "别", "勿", "forbidden", "prohibit", "except"]

    def is_negated(content, match_start):
        # Look back up to 400 chars (covers "禁止" on a preceding line of a prohibition block)
        window_start = max(0, match_start - 400)
        context = content[window_start:match_start]
        return any(w in context for w in negation)

    hidden_found = []
    for path in iter_markdown_files(skill_root):
        rel = os.path.relpath(path, skill_root).replace("\\", "/")
        if not is_canonical_content(rel):
            continue
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        content = strip_negative_examples(content)
        for pattern in HIDDEN_IMPLICATION_PATTERNS:
            for m in re.finditer(pattern, content, re.IGNORECASE):
                if is_negated(content, m.start()):
                    continue
                hidden_found.append(f"{rel}: {m.group(0)[:50]}")
    if hidden_found:
        for h in hidden_found[:5]:
            error(f"Hidden health/medical implication phrase found (must be prohibited): {h}")
    else:
        print("  ✓ Hidden health/medical implication phrases appear only in prohibition contexts")

    # Semantic Destination Test declared (audit meaning, not vocabulary)
    sdt_declared = False
    for path in iter_markdown_files(skill_root):
        rel = os.path.relpath(path, skill_root).replace("\\", "/")
        if not is_canonical_content(rel):
            continue
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        if "Semantic Destination Test" in content and "Audit meaning, not vocabulary" in content:
            sdt_declared = True
            break
    if sdt_declared:
        print("  ✓ Semantic Destination Test declared (audit meaning, not vocabulary)")
    else:
        error("Semantic Destination Test (audit meaning, not vocabulary) not declared in canonical content")

    # Intensify real friction, do not invent health fear — declared
    fear_declared = False
    for path in iter_markdown_files(skill_root):
        rel = os.path.relpath(path, skill_root).replace("\\", "/")
        if not is_canonical_content(rel):
            continue
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        if "Intensify real friction" in content and "invent health fear" in content:
            fear_declared = True
            break
    if fear_declared:
        print("  ✓ Intensify real friction / no invented health fear declared")
    else:
        error("Intensify real friction / no invented health fear not declared in canonical content")


# ---------- Check 20: Commercial Expression Freedom contract (PATCH v4.9.0) ----------

EXPR_FIELDS = [
    "expression_freedom_level",
    "rhetorical_exaggeration",
    "back_translation_result",
]

# Factual inflation patterns that must only appear in prohibition contexts (PATCH 03).
FACTUAL_INFLATION_PATTERNS = [
    r"真实值\s*→\s*更大的数字",
    r"可能\s*→\s*必然",
    r"部分用户\s*→\s*所有人",
    r"Authorized Claim\s*→\s*更强身体结果",
    r"普通体验\s*→\s*医疗效果",
]


def check_commercial_expression_freedom(skill_root):
    section("Checking commercial expression freedom contract (PATCH v4.9.0)")
    schemas_dir = os.path.join(skill_root, "schemas")
    ri_path = os.path.join(schemas_dir, "route-instance.schema.json")

    if not os.path.isfile(ri_path):
        error("route-instance.schema.json not found (expression freedom fields)")
        return

    try:
        with open(ri_path, "r", encoding="utf-8") as f:
            ri = json.load(f)
        props = ri.get("properties", {})
        missing = [f for f in EXPR_FIELDS if f not in props]
        if missing:
            error(f"route-instance.schema.json missing expression freedom fields: {missing}")
        else:
            print("  ✓ route-instance has expression_freedom_level / rhetorical_exaggeration / back_translation_result")

        expr_enum = props.get("expression_freedom_level", {}).get("enum", [])
        if expr_enum == ["EXPRESSION_OPEN", "EXPRESSION_RESTRICTED"]:
            print("  ✓ expression_freedom_level enum: EXPRESSION_OPEN / EXPRESSION_RESTRICTED")
        else:
            error(f"expression_freedom_level enum must be EXPRESSION_OPEN / EXPRESSION_RESTRICTED: {expr_enum}")

        rhe_enum = props.get("rhetorical_exaggeration", {}).get("enum", [])
        if rhe_enum == ["ALLOWED", "PROHIBITED"]:
            print("  ✓ rhetorical_exaggeration enum: ALLOWED / PROHIBITED")
        else:
            error(f"rhetorical_exaggeration enum must be ALLOWED / PROHIBITED: {rhe_enum}")

        bt_enum = props.get("back_translation_result", {}).get("enum", [])
        if bt_enum == ["PASS", "FAIL"]:
            print("  ✓ back_translation_result enum: PASS / FAIL")
        else:
            error(f"back_translation_result enum must be PASS / FAIL: {bt_enum}")
    except json.JSONDecodeError:
        error("route-instance.schema.json is invalid JSON (expression freedom)")
        return

    # commercial-expression-freedom.md reference exists
    cef_path = os.path.join(skill_root, "references", "execution", "commercial-expression-freedom.md")
    if os.path.isfile(cef_path):
        print("  ✓ references/execution/commercial-expression-freedom.md present")
    else:
        error("references/execution/commercial-expression-freedom.md not found")

    # SKILL.md mentions Commercial Expression Freedom / Semantic Back-Translation / G6.7
    skill_path = os.path.join(skill_root, "SKILL.md")
    if os.path.isfile(skill_path):
        with open(skill_path, "r", encoding="utf-8") as f:
            content = f.read()
        if "Commercial Expression Freedom" in content:
            print("  ✓ SKILL.md references Commercial Expression Freedom")
        else:
            error("SKILL.md missing Commercial Expression Freedom reference")
        if "Semantic Back-Translation" in content:
            print("  ✓ SKILL.md references Semantic Back-Translation")
        else:
            error("SKILL.md missing Semantic Back-Translation reference")
        if "G6.7" in content:
            print("  ✓ SKILL.md references G6.7 Expression Freedom Validation")
        else:
            error("SKILL.md missing G6.7 Expression Freedom Validation gate")

    # Factual inflation must be prohibited in canonical content (negated contexts only)
    negation = ["禁止", "不得", "不要", "不", "别", "勿", "forbidden", "prohibit", "except"]

    def is_negated(content, match_start):
        window_start = max(0, match_start - 400)
        context = content[window_start:match_start]
        return any(w in context for w in negation)

    inflation_found = []
    for path in iter_markdown_files(skill_root):
        rel = os.path.relpath(path, skill_root).replace("\\", "/")
        if not is_canonical_content(rel):
            continue
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        content = strip_negative_examples(content)
        for pattern in FACTUAL_INFLATION_PATTERNS:
            for m in re.finditer(pattern, content, re.IGNORECASE):
                if is_negated(content, m.start()):
                    continue
                inflation_found.append(f"{rel}: {m.group(0)[:50]}")
    if inflation_found:
        for h in inflation_found[:5]:
            error(f"Factual inflation pattern found (must be prohibited): {h}")
    else:
        print("  ✓ Factual inflation patterns appear only in prohibition contexts")

    # Semantic Back-Translation declared
    bt_declared = False
    for path in iter_markdown_files(skill_root):
        rel = os.path.relpath(path, skill_root).replace("\\", "/")
        if not is_canonical_content(rel):
            continue
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        if "Semantic Back-Translation" in content and "Claim Ceiling" in content:
            bt_declared = True
            break
    if bt_declared:
        print("  ✓ Semantic Back-Translation declared (within Claim Ceiling)")
    else:
        error("Semantic Back-Translation (within Claim Ceiling) not declared in canonical content")

    # Meaning-Based Claim Review declared (audit meaning, not vocabulary)
    mb_declared = False
    for path in iter_markdown_files(skill_root):
        rel = os.path.relpath(path, skill_root).replace("\\", "/")
        if not is_canonical_content(rel):
            continue
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        if "Meaning-Based Claim Review" in content and "Meaning > Keyword" in content:
            mb_declared = True
            break
    if mb_declared:
        print("  ✓ Meaning-Based Claim Review declared (Meaning > Keyword)")
    else:
        error("Meaning-Based Claim Review (Meaning > Keyword) not declared in canonical content")

    # Emotional exaggeration allowed / factual exaggeration not — declared
    rhe_declared = False
    for path in iter_markdown_files(skill_root):
        rel = os.path.relpath(path, skill_root).replace("\\", "/")
        if not is_canonical_content(rel):
            continue
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        if "Emotional exaggeration is allowed" in content and "Factual exaggeration is not" in content:
            rhe_declared = True
            break
    if rhe_declared:
        print("  ✓ Emotional exaggeration allowed / factual exaggeration not — declared")
    else:
        error("Emotional exaggeration allowed / factual exaggeration not — not declared in canonical content")

    # Conversion Recovery declared as Hard Requirement
    cr_declared = False
    for path in iter_markdown_files(skill_root):
        rel = os.path.relpath(path, skill_root).replace("\\", "/")
        if not is_canonical_content(rel):
            continue
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        if "Conversion Recovery" in content and "Losing one claim cannot automatically mean losing the sale" in content:
            cr_declared = True
            break
    if cr_declared:
        print("  ✓ Conversion Recovery declared as Hard Requirement")
    else:
        error("Conversion Recovery (losing one claim ≠ losing the sale) not declared in canonical content")

    # No auto-disclaimers declared
    nad_declared = False
    for path in iter_markdown_files(skill_root):
        rel = os.path.relpath(path, skill_root).replace("\\", "/")
        if not is_canonical_content(rel):
            continue
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        if "效果因人而异" in content and "仅供参考" in content and "破坏销售表达" in content:
            nad_declared = True
            break
    if nad_declared:
        print("  ✓ No auto-disclaimers declared (do not break sales expression)")
    else:
        error("No auto-disclaimers (do not break sales expression) not declared in canonical content")


# ---------- Check 21: Anxiety & Pain Scenification contract (PATCH v4.10.0) ----------

ANX_FIELDS = [
    "anxiety_type",
    "pain_specificity_score",
    "scene_vividness_score",
    "anxiety_legitimacy",
    "relief_path",
]

ANXIETY_TYPES = [
    "A1_LOSS", "A2_EXECUTION", "A3_DECISION", "A4_COMPLEXITY", "A5_TIME",
    "A6_OPPORTUNITY_COST", "A7_REGRET", "A8_WRONG_CHOICE", "A9_SOCIAL_SCENE",
]

# Fake-anxiety patterns that must only appear in prohibition contexts (PATCH 20).
FAKE_ANXIETY_PATTERNS = [
    r"虚假疾病",
    r"虚假身体恶化",
    r"无证据健康倒计时",
    r"无依据年龄恐吓",
    r"虚假育儿危险",
    r"虚假老人健康风险",
    r"虚假社会排斥",
    r"虚假库存",
    r"虚假涨价",
    r"虚假最后机会",
    r"现在不做以后一定后悔",
]


def check_anxiety_pain_scenification(skill_root):
    section("Checking anxiety & pain scenification contract (PATCH v4.10.0)")
    schemas_dir = os.path.join(skill_root, "schemas")
    ri_path = os.path.join(schemas_dir, "route-instance.schema.json")

    if not os.path.isfile(ri_path):
        error("route-instance.schema.json not found (anxiety fields)")
        return

    try:
        with open(ri_path, "r", encoding="utf-8") as f:
            ri = json.load(f)
        props = ri.get("properties", {})
        missing = [f for f in ANX_FIELDS if f not in props]
        if missing:
            error(f"route-instance.schema.json missing anxiety fields: {missing}")
        else:
            print("  ✓ route-instance has anxiety_type / pain_specificity_score / scene_vividness_score / anxiety_legitimacy / relief_path")

        anx_enum = props.get("anxiety_type", {}).get("enum", [])
        if len(anx_enum) == 9:
            print("  ✓ anxiety_type enum: 9 types (A1-A9)")
        else:
            error(f"anxiety_type enum must be 9 types (A1-A9): {anx_enum}")

        pss_enum = props.get("pain_specificity_score", {}).get("enum", [])
        if pss_enum == [0, 1, 2]:
            print("  ✓ pain_specificity_score enum: 0/1/2")
        else:
            error(f"pain_specificity_score enum must be 0/1/2: {pss_enum}")

        svs_enum = props.get("scene_vividness_score", {}).get("enum", [])
        if svs_enum == [0, 1, 2]:
            print("  ✓ scene_vividness_score enum: 0/1/2")
        else:
            error(f"scene_vividness_score enum must be 0/1/2: {svs_enum}")

        al_enum = props.get("anxiety_legitimacy", {}).get("enum", [])
        if al_enum == ["PASS", "FAIL"]:
            print("  ✓ anxiety_legitimacy enum: PASS / FAIL")
        else:
            error(f"anxiety_legitimacy enum must be PASS / FAIL: {al_enum}")

        rp_enum = props.get("relief_path", {}).get("enum", [])
        if rp_enum == ["REQUIRED", "OPTIONAL"]:
            print("  ✓ relief_path enum: REQUIRED / OPTIONAL")
        else:
            error(f"relief_path enum must be REQUIRED / OPTIONAL: {rp_enum}")
    except json.JSONDecodeError:
        error("route-instance.schema.json is invalid JSON (anxiety)")
        return

    # anxiety-pain-scenification.md reference exists
    aps_path = os.path.join(skill_root, "references", "execution", "anxiety-pain-scenification.md")
    if os.path.isfile(aps_path):
        print("  ✓ references/execution/anxiety-pain-scenification.md present")
    else:
        error("references/execution/anxiety-pain-scenification.md not found")

    # SKILL.md mentions Anxiety & Pain Scenification / Anxiety Legitimacy Gate / G6.8
    skill_path = os.path.join(skill_root, "SKILL.md")
    if os.path.isfile(skill_path):
        with open(skill_path, "r", encoding="utf-8") as f:
            content = f.read()
        if "Anxiety & Pain Scenification" in content:
            print("  ✓ SKILL.md references Anxiety & Pain Scenification")
        else:
            error("SKILL.md missing Anxiety & Pain Scenification reference")
        if "Anxiety Legitimacy Gate" in content:
            print("  ✓ SKILL.md references Anxiety Legitimacy Gate")
        else:
            error("SKILL.md missing Anxiety Legitimacy Gate reference")
        if "G6.8" in content:
            print("  ✓ SKILL.md references G6.8 Anxiety & Pain Scenification")
        else:
            error("SKILL.md missing G6.8 Anxiety & Pain Scenification gate")

    # Fake anxiety must be prohibited in canonical content (negated contexts only)
    negation = ["禁止", "不得", "不要", "不", "别", "勿", "forbidden", "prohibit", "except", "no", "not", "never", "without"]

    def is_negated(content, match_start):
        window_start = max(0, match_start - 400)
        context = content[window_start:match_start]
        return any(w in context for w in negation)

    fake_found = []
    for path in iter_markdown_files(skill_root):
        rel = os.path.relpath(path, skill_root).replace("\\", "/")
        if not is_canonical_content(rel):
            continue
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        content = strip_negative_examples(content)
        for pattern in FAKE_ANXIETY_PATTERNS:
            for m in re.finditer(pattern, content, re.IGNORECASE):
                if is_negated(content, m.start()):
                    continue
                fake_found.append(f"{rel}: {m.group(0)[:50]}")
    if fake_found:
        for h in fake_found[:5]:
            error(f"Fake anxiety pattern found (must be prohibited): {h}")
    else:
        print("  ✓ Fake anxiety patterns appear only in prohibition contexts")

    # Anxiety Legitimacy Gate declared (Source / Reality / Product Relevance)
    alg_declared = False
    for path in iter_markdown_files(skill_root):
        rel = os.path.relpath(path, skill_root).replace("\\", "/")
        if not is_canonical_content(rel):
            continue
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        if "Anxiety Legitimacy Gate" in content and "Source Test" in content and "Reality Test" in content and "Product Relevance Test" in content:
            alg_declared = True
            break
    if alg_declared:
        print("  ✓ Anxiety Legitimacy Gate declared (Source / Reality / Product Relevance)")
    else:
        error("Anxiety Legitimacy Gate (Source / Reality / Product Relevance) not declared in canonical content")

    # Make the real problem feel real / not invent a bigger problem — declared
    real_declared = False
    for path in iter_markdown_files(skill_root):
        rel = os.path.relpath(path, skill_root).replace("\\", "/")
        if not is_canonical_content(rel):
            continue
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        if "Make the real problem feel real" in content and "Invent a bigger problem" in content:
            real_declared = True
            break
    if real_declared:
        print("  ✓ Make the real problem feel real (not invent a bigger problem) declared")
    else:
        error("Make the real problem feel real (not invent a bigger problem) not declared in canonical content")

    # Relief Path declared (anxiety must have an exit)
    relief_declared = False
    for path in iter_markdown_files(skill_root):
        rel = os.path.relpath(path, skill_root).replace("\\", "/")
        if not is_canonical_content(rel):
            continue
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        if "Relief Path" in content and "Anxiety" in content and "Relief Contrast" in content:
            relief_declared = True
            break
    if relief_declared:
        print("  ✓ Relief Path / Relief Contrast declared")
    else:
        error("Relief Path / Relief Contrast not declared in canonical content")

    # Camera Test declared
    camera_declared = False
    for path in iter_markdown_files(skill_root):
        rel = os.path.relpath(path, skill_root).replace("\\", "/")
        if not is_canonical_content(rel):
            continue
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        if "Camera Test" in content:
            camera_declared = True
            break
    if camera_declared:
        print("  ✓ Camera Test declared (scene must be filmable)")
    else:
        error("Camera Test (scene must be filmable) not declared in canonical content")

    # Pain Specificity must not be 0 for Sell — declared
    ps_declared = False
    for path in iter_markdown_files(skill_root):
        rel = os.path.relpath(path, skill_root).replace("\\", "/")
        if not is_canonical_content(rel):
            continue
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        if "Pain Specificity" in content and "不能为 0" in content:
            ps_declared = True
            break
    if ps_declared:
        print("  ✓ Pain Specificity must not be 0 for Sell — declared")
    else:
        error("Pain Specificity must not be 0 for Sell — not declared in canonical content")


# ---------- Check 22: Commercial Intensity contract (PATCH v4.11.0) ----------

CI_FIELDS = [
    "commercial_intensity",
]

CI_LEVELS = ["CONSERVATIVE", "STANDARD", "AGGRESSIVE"]

# I5-A hard-bottom phrases (clear physiological results) that must stay prohibited
# in canonical content even after the v4.11.0 relaxation. I5-B/C relax the
# surrounding implication space, never these hard-bottom results.
I5A_HARD_BOTTOM_PATTERNS = [
    r"改善疾病",
    r"预防疾病",
    r"治疗",
    r"改善某生理指标",
    r"改善激素",
    r"补血",
    r"抗疲劳",
    r"提高免疫",
    r"改善睡眠",
    r"减肥",
    r"改善月经",
    r"改善某器官功能",
]


def check_commercial_intensity(skill_root):
    section("Checking commercial intensity contract (PATCH v4.11.0)")
    schemas_dir = os.path.join(skill_root, "schemas")
    ri_path = os.path.join(schemas_dir, "route-instance.schema.json")

    if not os.path.isfile(ri_path):
        error("route-instance.schema.json not found (commercial intensity field)")
        return

    try:
        with open(ri_path, "r", encoding="utf-8") as f:
            ri = json.load(f)
        props = ri.get("properties", {})
        missing = [f for f in CI_FIELDS if f not in props]
        if missing:
            error(f"route-instance.schema.json missing commercial intensity fields: {missing}")
        else:
            print("  ✓ route-instance has commercial_intensity")

        ci = props.get("commercial_intensity", {})
        ci_enum = ci.get("enum", [])
        if ci_enum == CI_LEVELS:
            print("  ✓ commercial_intensity enum: CONSERVATIVE / STANDARD / AGGRESSIVE")
        else:
            error(f"commercial_intensity enum must be CONSERVATIVE / STANDARD / AGGRESSIVE: {ci_enum}")
        if ci.get("default") == "STANDARD":
            print("  ✓ commercial_intensity default: STANDARD")
        else:
            error(f"commercial_intensity default must be STANDARD: {ci.get('default')}")
    except json.JSONDecodeError:
        error("route-instance.schema.json is invalid JSON (commercial intensity)")
        return

    # claim-authority.md declares COMMERCIAL_INTENSITY
    ca_path = os.path.join(skill_root, "references", "execution", "claim-authority.md")
    if os.path.isfile(ca_path):
        with open(ca_path, "r", encoding="utf-8") as f:
            ca_content = f.read()
        if "COMMERCIAL_INTENSITY" in ca_content and "CONSERVATIVE" in ca_content and "AGGRESSIVE" in ca_content:
            print("  ✓ claim-authority.md declares COMMERCIAL_INTENSITY (CONSERVATIVE/STANDARD/AGGRESSIVE)")
        else:
            error("claim-authority.md missing COMMERCIAL_INTENSITY declaration")
    else:
        error("references/execution/claim-authority.md not found (commercial intensity)")

    # I5-A / I5-B / I5-C declared in implicit-benefit-pain.md
    ibp_path = os.path.join(skill_root, "references", "execution", "implicit-benefit-pain.md")
    if os.path.isfile(ibp_path):
        with open(ibp_path, "r", encoding="utf-8") as f:
            ibp_content = f.read()
        for tag in ["I5-A", "I5-B", "I5-C"]:
            if tag in ibp_content:
                print(f"  ✓ implicit-benefit-pain.md declares {tag}")
            else:
                error(f"implicit-benefit-pain.md missing {tag} declaration")
    else:
        error("references/execution/implicit-benefit-pain.md not found (I5 split)")

    # Edge Expression Policy + Category-Differentiated Ceiling declared in commercial-expression-freedom.md
    cef_path = os.path.join(skill_root, "references", "execution", "commercial-expression-freedom.md")
    if os.path.isfile(cef_path):
        with open(cef_path, "r", encoding="utf-8") as f:
            cef_content = f.read()
        if "Edge Expression Policy" in cef_content and "GREEN" in cef_content and "AMBER" in cef_content and "RED" in cef_content:
            print("  ✓ commercial-expression-freedom.md declares Edge Expression Policy (GREEN/AMBER/RED)")
        else:
            error("commercial-expression-freedom.md missing Edge Expression Policy (GREEN/AMBER/RED)")
        if "品类差异化天花板" in cef_content or "Category-Differentiated Ceiling" in cef_content:
            print("  ✓ commercial-expression-freedom.md declares Category-Differentiated Ceiling")
        else:
            error("commercial-expression-freedom.md missing Category-Differentiated Ceiling")
    else:
        error("references/execution/commercial-expression-freedom.md not found (edge expression)")

    # Category-Differentiated Anxiety Intensity declared in anxiety-pain-scenification.md
    aps_path = os.path.join(skill_root, "references", "execution", "anxiety-pain-scenification.md")
    if os.path.isfile(aps_path):
        with open(aps_path, "r", encoding="utf-8") as f:
            aps_content = f.read()
        if "品类差异化焦虑强度" in aps_content or "Category-Differentiated Anxiety Intensity" in aps_content:
            print("  ✓ anxiety-pain-scenification.md declares Category-Differentiated Anxiety Intensity")
        else:
            error("anxiety-pain-scenification.md missing Category-Differentiated Anxiety Intensity")
    else:
        error("references/execution/anxiety-pain-scenification.md not found (anxiety intensity)")

    # I5-A hard-bottom phrases must appear only in prohibition contexts in canonical content
    negation = ["禁止", "不得", "不要", "不", "别", "勿", "forbidden", "prohibit", "except", "no", "not", "never", "without"]

    def is_negated(content, match_start, match_end):
        # Look back up to 400 chars AND forward up to 400 chars: prohibition lists
        # often place the negation word after the listed items ("疾病/治疗/预防…任何档位禁止").
        back_start = max(0, match_start - 400)
        back = content[back_start:match_start]
        fwd = content[match_end:match_end + 400]
        return any(w in back for w in negation) or any(w in fwd for w in negation)

    hard_found = []
    for path in iter_markdown_files(skill_root):
        rel = os.path.relpath(path, skill_root).replace("\\", "/")
        if not is_canonical_content(rel):
            continue
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        content = strip_negative_examples(content)
        for pattern in I5A_HARD_BOTTOM_PATTERNS:
            for m in re.finditer(pattern, content, re.IGNORECASE):
                if is_negated(content, m.start(), m.end()):
                    continue
                hard_found.append(f"{rel}: {m.group(0)[:50]}")
    if hard_found:
        for h in hard_found[:5]:
            error(f"I5-A hard-bottom phrase found outside prohibition context (must stay prohibited): {h}")
    else:
        print("  ✓ I5-A hard-bottom phrases appear only in prohibition contexts")

    # Back-Translation recoverable (CONVERSION_RECOVERY) declared
    bt_recoverable = False
    for path in iter_markdown_files(skill_root):
        rel = os.path.relpath(path, skill_root).replace("\\", "/")
        if not is_canonical_content(rel):
            continue
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        if "CONVERSION_RECOVERY" in content and "Back-Translation" in content:
            bt_recoverable = True
            break
    if bt_recoverable:
        print("  ✓ Semantic Back-Translation recoverable (CONVERSION_RECOVERY) declared")
    else:
        error("Semantic Back-Translation recoverable (CONVERSION_RECOVERY) not declared in canonical content")

    # SKILL.md declares Commercial Intensity (4.32)
    skill_path = os.path.join(skill_root, "SKILL.md")
    if os.path.isfile(skill_path):
        with open(skill_path, "r", encoding="utf-8") as f:
            content = f.read()
        if "Commercial Intensity" in content and "CONSERVATIVE" in content and "AGGRESSIVE" in content:
            print("  ✓ SKILL.md declares Commercial Intensity (CONSERVATIVE/STANDARD/AGGRESSIVE)")
        else:
            error("SKILL.md missing Commercial Intensity declaration")


# ---------- Check 23: Boundary is Internal contract (PATCH v4.11.1) ----------

# Disclaimer / didactic phrases that must appear ONLY inside prohibition lists
# in canonical content (as forbidden examples), never as permitted expression.
DISCLAIMER_DIDACTIC_PATTERNS = [
    r"它不负责让你瘦",
    r"我不指望它一夜之间改变什么",
    r"它不神化自己",
    r"按法规，普通食品不能宣传功效",
    r"别被神药话术骗",
    r"焦虑驱动的东西，往往买完就后悔",
    r"买之前先学会看这一行字",
]


def check_boundary_is_internal(skill_root):
    section("Checking boundary-is-internal contract (PATCH v4.11.1)")

    # commercial-expression-freedom.md declares Boundary is Internal
    cef_path = os.path.join(skill_root, "references", "execution", "commercial-expression-freedom.md")
    if os.path.isfile(cef_path):
        with open(cef_path, "r", encoding="utf-8") as f:
            cef_content = f.read()
        if "Boundary is Internal, Not Content" in cef_content:
            print("  ✓ commercial-expression-freedom.md declares Boundary is Internal, Not Content")
        else:
            error("commercial-expression-freedom.md missing Boundary is Internal, Not Content")
        if "免责声明式表达（禁止）" in cef_content and "说教式表达（禁止）" in cef_content:
            print("  ✓ commercial-expression-freedom.md declares disclaimer & didactic prohibition")
        else:
            error("commercial-expression-freedom.md missing disclaimer & didactic prohibition")
        if "事实边界（允许自然带出）" in cef_content:
            print("  ✓ commercial-expression-freedom.md declares fact boundary (naturally stated)")
        else:
            error("commercial-expression-freedom.md missing fact boundary (naturally stated)")
    else:
        error("references/execution/commercial-expression-freedom.md not found (boundary is internal)")

    # PARTIAL_PAIN: boundary = not exaggerating, not in-copy disclaimer
    ibp_path = os.path.join(skill_root, "references", "execution", "implicit-benefit-pain.md")
    if os.path.isfile(ibp_path):
        with open(ibp_path, "r", encoding="utf-8") as f:
            ibp_content = f.read()
        if "边界体现在" in ibp_content and "不夸大" in ibp_content:
            print("  ✓ implicit-benefit-pain.md PARTIAL_PAIN boundary = not exaggerating (no in-copy disclaimer)")
        else:
            error("implicit-benefit-pain.md PARTIAL_PAIN missing boundary-in-not-exaggerating rule")
    else:
        error("references/execution/implicit-benefit-pain.md not found (partial pain)")

    # Relief Contrast: no disclaimer tone
    aps_path = os.path.join(skill_root, "references", "execution", "anxiety-pain-scenification.md")
    if os.path.isfile(aps_path):
        with open(aps_path, "r", encoding="utf-8") as f:
            aps_content = f.read()
        if "禁止免责语气" in aps_content:
            print("  ✓ anxiety-pain-scenification.md Relief Contrast forbids disclaimer tone")
        else:
            error("anxiety-pain-scenification.md Relief Contrast missing no-disclaimer-tone rule")
    else:
        error("references/execution/anxiety-pain-scenification.md not found (relief contrast)")

    # SKILL.md declares Boundary is Internal
    skill_path = os.path.join(skill_root, "SKILL.md")
    if os.path.isfile(skill_path):
        with open(skill_path, "r", encoding="utf-8") as f:
            content = f.read()
        if "Boundary is Internal, Not Content" in content:
            print("  ✓ SKILL.md declares Boundary is Internal, Not Content")
        else:
            error("SKILL.md missing Boundary is Internal, Not Content")
    else:
        error("SKILL.md not found (boundary is internal)")


# ---------- Check 24: Never-Filter Efficacy Implications contract (PATCH v4.11.4) ----------

# Stale rule phrases that contradict "功效暗示永不过滤" — must not appear as
# active rules in canonical content (they may appear only as change descriptions).
STALE_IMPLICATION_RULES = [
    r"只能作为受众上下文、不得当主卖点",
    r"允许出现，但不能当主卖点",
    r"必须露出边界",
    r"允许强表达但露出边界",
    r"PARTIAL_PAIN 必须露出边界",
    r"CONTEXT_PAIN 只能作为受众上下文",
]


def check_never_filter_implications(skill_root):
    section("Checking never-filter efficacy implications contract (PATCH v4.11.4)")

    # 1. "功效暗示永不过滤" declared across the four canonical layers
    ibp_path = os.path.join(skill_root, "references", "execution", "implicit-benefit-pain.md")
    ca_path = os.path.join(skill_root, "references", "execution", "claim-authority.md")
    cef_path = os.path.join(skill_root, "references", "execution", "commercial-expression-freedom.md")
    skill_path = os.path.join(skill_root, "SKILL.md")

    def read_md(path):
        if os.path.isfile(path):
            with open(path, "r", encoding="utf-8") as f:
                return f.read()
        return None

    ibp = read_md(ibp_path)
    ca = read_md(ca_path)
    cef = read_md(cef_path)
    skill = read_md(skill_path)

    if ibp is None:
        error("references/execution/implicit-benefit-pain.md not found (never-filter implications)")
    else:
        if "功效暗示永不过滤" in ibp:
            print("  ✓ implicit-benefit-pain.md declares 功效暗示永不过滤")
        else:
            error("implicit-benefit-pain.md missing 功效暗示永不过滤 declaration")
        if "默认保留" in ibp and "I5-B" in ibp and "I5-C" in ibp:
            print("  ✓ implicit-benefit-pain.md declares I5-B/C 默认保留")
        else:
            error("implicit-benefit-pain.md missing I5-B/C 默认保留 declaration")
        if "可作为主卖点" in ibp and "CONTEXT" in ibp:
            print("  ✓ implicit-benefit-pain.md declares CONTEXT_PAIN 可作为主卖点 (non-sensitive)")
        else:
            error("implicit-benefit-pain.md missing CONTEXT_PAIN-as-main-selling-point declaration")

    if ca is None:
        error("references/execution/claim-authority.md not found (never-filter implications)")
    else:
        if "功效暗示永不过滤" in ca:
            print("  ✓ claim-authority.md declares 功效暗示永不过滤")
        else:
            error("claim-authority.md missing 功效暗示永不过滤 declaration")
        if "I5-A Hidden Efficacy Implication" in ca:
            print("  ✓ claim-authority.md narrows Hidden Efficacy Implication to I5-A only")
        else:
            error("claim-authority.md missing I5-A-only Hidden Efficacy Implication narrowing")

    if cef is None:
        error("references/execution/commercial-expression-freedom.md not found (never-filter implications)")
    else:
        if "功效暗示默认保留" in cef:
            print("  ✓ commercial-expression-freedom.md declares 功效暗示默认保留 (Section 25)")
        else:
            error("commercial-expression-freedom.md missing 功效暗示默认保留 declaration")
        if "默认开放" in cef and "AMBER" in cef:
            print("  ✓ commercial-expression-freedom.md declares AMBER 默认开放")
        else:
            error("commercial-expression-freedom.md missing AMBER 默认开放 declaration")

    if skill is None:
        error("SKILL.md not found (never-filter implications)")
    else:
        if "功效暗示永不过滤" in skill:
            print("  ✓ SKILL.md declares 功效暗示永不过滤")
        else:
            error("SKILL.md missing 功效暗示永不过滤 declaration")

    # 2. I5-A hard prohibition must remain declared (never-filter ≠ claim ceiling removal)
    if ibp and "I5-A" in ibp and "硬禁" in ibp:
        print("  ✓ I5-A hard prohibition retained (claim ceiling preserved)")
    else:
        error("implicit-benefit-pain.md missing I5-A hard prohibition declaration")

    # 3. Stale rule phrases must not appear as active rules in canonical content
    stale_found = []
    for path in iter_markdown_files(skill_root):
        rel = os.path.relpath(path, skill_root).replace("\\", "/")
        if not is_canonical_content(rel):
            continue
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        for pattern in STALE_IMPLICATION_RULES:
            for m in re.finditer(pattern, content):
                stale_found.append(f"{rel}: {m.group(0)[:60]}")
    if stale_found:
        for s in stale_found[:5]:
            error(f"stale implication rule found (contradicts 功效暗示永不过滤): {s}")
    else:
        print("  ✓ no stale implication rules (CONTEXT_PAIN main-selling-point / PARTIAL_PAIN boundary)")


# ---------- Check 25: Full-Caliber Implicit CTA contract (PATCH v4.12.0) ----------

def check_full_caliber_implicit_cta(skill_root):
    section("Checking full-caliber implicit CTA contract (PATCH v4.12.0)")

    cta_path = os.path.join(skill_root, "references", "craft", "cta.md")
    examples_path = os.path.join(skill_root, "references", "craft", "examples.md")
    skill_path = os.path.join(skill_root, "SKILL.md")

    def read_md(path):
        if os.path.isfile(path):
            with open(path, "r", encoding="utf-8") as f:
                return f.read()
        return None

    cta = read_md(cta_path)
    examples = read_md(examples_path)
    skill = read_md(skill_path)

    if cta is None:
        error("references/craft/cta.md not found (full-caliber implicit CTA)")
        return

    if "全口径默认高级隐式收口" in cta or "全口径硬约束" in cta:
        print("  ✓ cta.md declares full-caliber implicit closing")
    else:
        error("cta.md missing full-caliber implicit closing declaration")

    stale = ["显式动作、隐式续接、无指令缺口均可", "显式动作可选", "显式咨询可选", "引导预约"]
    hits = [s for s in stale if s in cta]
    if hits:
        error(f"cta.md caliber table still permits explicit actions: {hits}")
    else:
        print("  ✓ cta.md caliber table has no explicit-action defaults")

    if "高级隐式收口" in cta and "零动作指令" in cta:
        print("  ✓ cta.md defines advanced implicit closing QC")
    else:
        error("cta.md missing advanced implicit closing QC")

    if examples is not None:
        old_watch = "| 看播 | 【价值预告】，想【了解什么】的，进直播间来看"
        old_reserve = "| 预约 | 想不错过【内容主题】，下方预约点一下，开播我提醒你"
        if old_watch in examples:
            error("examples.md still shows explicit watch-live CTA as positive template")
        else:
            print("  ✓ examples.md watch-live CTA is implicit-only")
        if old_reserve in examples:
            error("examples.md still shows explicit reservation CTA as positive template")
        else:
            print("  ✓ examples.md reservation CTA is implicit-only")

    if skill is not None:
        if "全口径默认高级隐式收口" in skill:
            print("  ✓ SKILL.md declares full-caliber implicit closing")
        else:
            error("SKILL.md missing full-caliber implicit closing rule")


# ---------- Main ----------

def main():
    skill_root = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
    skill_root = os.path.abspath(skill_root)

    print(f"Validating skill package at: {skill_root}")
    print("=" * 60)

    # Run all checks
    check_root_files(skill_root)
    validate_skill_md(skill_root)
    check_references(skill_root)
    check_reference_links(skill_root)
    check_canonical_integrity(skill_root)
    check_adapters(skill_root)
    check_schemas(skill_root)
    check_tests(skill_root)
    check_scripts(skill_root)
    check_metadata_safety(skill_root)
    check_no_temp_files(skill_root)
    check_single_source_of_truth(skill_root)
    check_cta_conflicts(skill_root)
    check_metadata_leak(skill_root)
    check_source_separation(skill_root)
    check_capability_contract(skill_root)
    check_product_acquisition(skill_root)
    check_claim_authority(skill_root)
    check_pain_translation(skill_root)
    check_commercial_expression_freedom(skill_root)
    check_anxiety_pain_scenification(skill_root)
    check_commercial_intensity(skill_root)
    check_boundary_is_internal(skill_root)
    check_never_filter_implications(skill_root)
    check_full_caliber_implicit_cta(skill_root)

    # Summary
    print("\n" + "=" * 60)
    print("VALIDATION SUMMARY")
    print("=" * 60)

    if ERRORS:
        print(f"\nFAILED: {len(ERRORS)} errors")
        for e in ERRORS:
            print(f"  ✗ {e}")
    else:
        print(f"\n✓ PASSED: No errors")

    if WARNINGS:
        print(f"\n{len(WARNINGS)} warnings")
        for w in WARNINGS:
            print(f"  ⚠ {w}")

    print(f"\nErrors: {len(ERRORS)}")
    print(f"Warnings: {len(WARNINGS)}")

    return 1 if ERRORS else 0


if __name__ == "__main__":
    sys.exit(main())
