#!/usr/bin/env python3
"""
Regression Test Runner for Master Copywriting Skill

Runs regression test suites to verify skill integrity and rule consistency.

Usage:
  python scripts/run_regression.py
  python scripts/run_regression.py --suite facts
  python scripts/run_regression.py --suite purposes
  python scripts/run_regression.py --suite platforms
  python scripts/run_regression.py --suite portability
  python scripts/run_regression.py --suite static-contract
  python scripts/run_regression.py --suite behavioral
  python scripts/run_regression.py --all

PATCH 28: Regression tests are split into two layers:
  - Static Contract Tests: file structure, schema, source of truth, forbidden
    conflict phrases, capability naming, stale section links, output metadata leak.
  - Behavioral Regression Tests: require an actual model run. If no model is
    executed, Behavioral Regression must report NOT RUN — never fake a PASS.
"""

import argparse
import json
import os
import re
import sys


PASS_COUNT = 0
FAIL_COUNT = 0
WARN_COUNT = 0
SKIP_COUNT = 0


def passed(name, detail=""):
    global PASS_COUNT
    PASS_COUNT += 1
    msg = f"  ✓ PASS: {name}"
    if detail:
        msg += f" ({detail})"
    print(msg)


def failed(name, detail=""):
    global FAIL_COUNT
    FAIL_COUNT += 1
    msg = f"  ✗ FAIL: {name}"
    if detail:
        msg += f" — {detail}"
    print(msg)


def warned(name, detail=""):
    global WARN_COUNT
    WARN_COUNT += 1
    msg = f"  ⚠ WARN: {name}"
    if detail:
        msg += f" — {detail}"
    print(msg)


def skipped(name, reason=""):
    global SKIP_COUNT
    SKIP_COUNT += 1
    msg = f"  ⊘ SKIP: {name}"
    if reason:
        msg += f" ({reason})"
    print(msg)


def suite_header(title):
    print(f"\n{'='*60}")
    print(f"  SUITE: {title}")
    print(f"{'='*60}")


def iter_markdown_files(skill_root):
    for root, dirs, files in os.walk(skill_root):
        if ".git" in root:
            continue
        for f in files:
            if f.endswith(".md"):
                yield os.path.join(root, f)


def strip_negative_examples(content):
    return re.sub(
        r"##\s*NEGATIVE EXAMPLES.*?(?=\n##\s|\Z)",
        "", content, flags=re.DOTALL | re.IGNORECASE)


def is_canonical_content(rel_path):
    rel = rel_path.replace("\\", "/")
    if rel.startswith(("references/", "adapters/")):
        return True
    if rel == "SKILL.md":
        return True
    return False


def is_capability_scan_target(rel_path):
    rel = rel_path.replace("\\", "/")
    if rel.startswith(("references/", "adapters/", "schemas/", "assets/")):
        return True
    if rel == "SKILL.md":
        return True
    return False


# ============================================================
# Suite: Facts
# ============================================================

def run_facts_suite(skill_root):
    """Fact integrity regression tests."""
    suite_header("Fact Integrity")

    # Test 1: SKILL.md has fact boundary rules
    skill_path = os.path.join(skill_root, "SKILL.md")
    if os.path.isfile(skill_path):
        with open(skill_path, "r", encoding="utf-8") as f:
            content = f.read()

        if "hard gate" in content.lower() or "硬门" in content:
            passed("Hard gate referenced in SKILL.md")
        else:
            failed("No hard gate reference in SKILL.md")

        if "product truth" in content.lower() or "G1" in content or "产品事实" in content:
            passed("Product truth gate (G1) referenced")
        else:
            failed("No product truth gate in SKILL.md")

    # Test 2: Expression authority reference exists
    expr_auth = os.path.join(skill_root, "references", "execution", "expression-authority.md")
    if os.path.isfile(expr_auth):
        with open(expr_auth, "r", encoding="utf-8") as f:
            content = f.read()
        if "fact boundary" in content.lower() or "事实边界" in content:
            passed("Expression authority has fact boundary rules")
        else:
            warned("Expression authority missing fact boundary mention")

        if "IP Fact Firewall" in content or "IP事实防火墙" in content:
            passed("IP Fact Firewall defined")
        else:
            warned("IP Fact Firewall not found in expression-authority.md")
    else:
        failed("expression-authority.md not found")

    # Test 3: Execution reliability has canonical ledger
    exec_rel = os.path.join(skill_root, "references", "execution", "execution-reliability.md")
    if os.path.isfile(exec_rel):
        with open(exec_rel, "r", encoding="utf-8") as f:
            content = f.read()
        if "Canonical Product Ledger" in content or "Product Ledger" in content:
            passed("Canonical Product Ledger defined")
        else:
            warned("Canonical Product Ledger not found in execution-reliability.md")
    else:
        failed("execution-reliability.md not found")

    # Test 4: Numeric consistency gate exists
    if exec_rel and os.path.isfile(exec_rel):
        with open(exec_rel, "r", encoding="utf-8") as f:
            content = f.read()
        if "numeric" in content.lower() or "数字" in content:
            passed("Numeric consistency rules present")
        else:
            warned("Numeric consistency rules not found in execution-reliability.md")

    # Test 5: External claim admission gate exists
    ext_intel = os.path.join(skill_root, "references", "external", "external-intelligence.md")
    if os.path.isfile(ext_intel):
        with open(ext_intel, "r", encoding="utf-8") as f:
            content = f.read()
        if "Claim Admission" in content or "claim admission" in content.lower() or "准入" in content:
            passed("External Claim Admission Gate defined")
        else:
            warned("External Claim Admission Gate not found")

        if "fabricat" in content.lower() or "虚构" in content or "伪造" in content:
            passed("No fabrication rule for external facts")
        else:
            warned("No explicit fabrication prohibition in external-intelligence.md")
    else:
        failed("external-intelligence.md not found")

    # Test 7: Product facts schema exists and is valid
    schema_path = os.path.join(skill_root, "schemas", "product-facts.schema.json")
    if os.path.isfile(schema_path):
        try:
            with open(schema_path, "r", encoding="utf-8") as f:
                schema = json.load(f)
            if "properties" in schema and "key_facts" in schema.get("properties", {}):
                passed("Product facts schema has key_facts field")
            else:
                warned("Product facts schema missing key_facts")
        except json.JSONDecodeError:
            failed("Product facts schema is invalid JSON")
    else:
        failed("product-facts.schema.json not found")


# ============================================================
# Suite: Purposes
# ============================================================

def run_purposes_suite(skill_root):
    """Purpose integrity regression tests."""
    suite_header("Purpose Integrity")

    purpose_file = os.path.join(skill_root, "references", "execution", "purpose-integrity.md")

    if not os.path.isfile(purpose_file):
        failed("purpose-integrity.md not found")
        return

    with open(purpose_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Test 1: Three purposes defined
    purpose_keywords = ["content", "seed", "sell"]
    found = sum(1 for kw in purpose_keywords if kw in content.lower())
    if found >= 3:
        passed("All three purposes (Content/Seed/Sell) defined")
    else:
        failed(f"Only {found}/3 purpose keywords found")

    # Test 2: Purpose Drift Test exists
    if "Drift Test" in content or "漂移" in content or "drift" in content.lower():
        passed("Purpose Drift Test defined")
    else:
        warned("Purpose Drift Test not found")

    # Test 3: Seed is not weakened Sell
    if "weakened" in content.lower() or "弱化" in content or "不是减弱版" in content:
        passed("Seed ≠ weakened Sell rule defined")
    else:
        warned("Seed-not-weakened-Sell rule not explicit")

    # Test 4: Demonstration truth gate
    if "demonstration" in content.lower() or "演示" in content or "展示" in content:
        passed("Demonstration truth rules present")
    else:
        warned("Demonstration truth rules not found")

    # Test 5: First-person claim scanner
    if "first-person" in content.lower() or "first person" in content.lower() or "第一人称" in content:
        passed("First-person claim rules present")
    else:
        warned("First-person claim rules not found")

    # Test 6: SKILL.md references purpose
    skill_path = os.path.join(skill_root, "SKILL.md")
    if os.path.isfile(skill_path):
        with open(skill_path, "r", encoding="utf-8") as f:
            skill_content = f.read()
        if "purpose" in skill_content.lower():
            passed("Purpose referenced in SKILL.md router")
        else:
            warned("Purpose not referenced in SKILL.md")


# ============================================================
# Suite: Platforms
# ============================================================

# PATCH 27: support canonical ID + Chinese names
PLATFORM_ALIASES = [
    ("douyin", "抖音"),
    ("xiaohongshu", "小红书"),
    ("official_account", "公众号"),
    ("channels", "视频号"),
]


def run_platforms_suite(skill_root):
    """Platform core regression tests."""
    suite_header("Platform Core")

    platforms_file = os.path.join(skill_root, "references", "modes", "platforms.md")

    if not os.path.isfile(platforms_file):
        failed("platforms.md not found")
        return

    with open(platforms_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Test 1: All four platforms covered (canonical ID OR Chinese name)
    found_platforms = []
    for cid, cn in PLATFORM_ALIASES:
        if cid in content.lower() or cn in content:
            found_platforms.append(cid)
    if len(found_platforms) >= 4:
        passed("All 4 platforms (Douyin/XHS/OA/Channels) covered")
    else:
        missing = [cid for cid, _ in PLATFORM_ALIASES if cid not in found_platforms]
        failed(f"Only {len(found_platforms)}/4 platforms found; missing {missing}")

    # Test 2: Cross-platform re-conception exists
    cp_file = os.path.join(skill_root, "references", "cross-platform", "cross-platform-reconception.md")
    if os.path.isfile(cp_file):
        with open(cp_file, "r", encoding="utf-8") as f:
            cp_content = f.read()
        if "re-conception" in cp_content.lower() or "再构思" in cp_content or "reconception" in cp_content.lower():
            passed("Cross-Platform Re-conception Protocol defined")
        else:
            warned("Re-conception concept not explicit")

        if "collision" in cp_content.lower() or "冲突" in cp_content or "碰撞" in cp_content:
            passed("Platform collision check defined")
        else:
            warned("Platform collision check not found")
    else:
        failed("cross-platform-reconception.md not found")

    # Test 4: Commercial identity integrity
    if "commercial identity" in content.lower() or "商业身份" in content:
        passed("Commercial identity rules referenced in platforms")
    else:
        if cp_file and os.path.isfile(cp_file):
            with open(cp_file, "r", encoding="utf-8") as f:
                cp_content = f.read()
            if "commercial identity" in cp_content.lower() or "商业身份" in cp_content:
                passed("Commercial identity integrity defined (cross-platform)")
            else:
                warned("Commercial identity integrity not found")

    # Test 5: 24 modes reference
    modes_file = os.path.join(skill_root, "references", "modes", "24-modes.md")
    if os.path.isfile(modes_file):
        with open(modes_file, "r", encoding="utf-8") as f:
            modes_content = f.read()
        if "24" in modes_content:
            passed("24 modes reference found")
        else:
            warned("24 modes number not found")
    else:
        failed("24-modes.md not found")


# ============================================================
# Suite: Portability
# ============================================================

def run_portability_suite(skill_root):
    """Portability regression tests."""
    suite_header("Portability & Packaging")

    # Test 1: All adapters present
    adapters_dir = os.path.join(skill_root, "adapters")
    required_adapters = ["generic", "claude", "openai", "gemini", "copilot", "limited-agent"]
    if os.path.isdir(adapters_dir):
        found = 0
        for adapter in required_adapters:
            path = os.path.join(adapters_dir, f"{adapter}.md")
            if os.path.isfile(path):
                found += 1
        if found == len(required_adapters):
            passed(f"All {len(required_adapters)} adapters present")
        else:
            failed(f"Only {found}/{len(required_adapters)} adapters found")
    else:
        failed("adapters/ directory not found")

    # Test 2: Capability negotiation in SKILL.md
    skill_path = os.path.join(skill_root, "SKILL.md")
    if os.path.isfile(skill_path):
        with open(skill_path, "r", encoding="utf-8") as f:
            content = f.read()
        if "Capability Negotiation" in content or "能力协商" in content:
            passed("Capability Negotiation section present")
        else:
            failed("No Capability Negotiation in SKILL.md")

        # Test 3: Runtime modes defined
        modes = ["FULL", "GROUNDED", "WEB_ONLY", "TEXT_ONLY"]
        found_modes = sum(1 for m in modes if m in content)
        if found_modes == 4:
            passed("All 4 runtime modes (FULL/GROUNDED/WEB_ONLY/TEXT_ONLY) defined")
        else:
            failed(f"Only {found_modes}/4 runtime modes found")

        # Test 4: Abstract capabilities listed
        caps = ["WEB_SEARCH", "FILE_READ", "CODE_EXECUTION", "MCP", "MEMORY", "STRUCTURED_OUTPUT"]
        found_caps = sum(1 for c in caps if c in content)
        if found_caps >= 4:
            passed(f"Abstract capabilities defined ({found_caps}/6+)")
        else:
            failed(f"Only {found_caps} abstract capabilities found")

    # Test 5: Graceful degradation documented
    cap_matrix = os.path.join(skill_root, "assets", "capability-matrix.md")
    if os.path.isfile(cap_matrix):
        with open(cap_matrix, "r", encoding="utf-8") as f:
            content = f.read()
        if "degrad" in content.lower() or "降级" in content:
            passed("Graceful degradation documented")
        else:
            warned("Graceful degradation not explicitly documented")
    else:
        warned("capability-matrix.md not found")

    # Test 6: Tool independence contract
    if skill_path and os.path.isfile(skill_path):
        with open(skill_path, "r", encoding="utf-8") as f:
            content = f.read()
        if "Tool Independence" in content or "independence" in content.lower() or "工具独立" in content:
            passed("Tool Independence Contract referenced")
        else:
            warned("Tool Independence Contract not found in SKILL.md")

    # Test 7: Progressive disclosure
    if skill_path and os.path.isfile(skill_path):
        with open(skill_path, "r", encoding="utf-8") as f:
            content = f.read()
        if "Progressive Disclosure" in content or "渐进式" in content:
            passed("Progressive Disclosure defined")
        else:
            failed("No Progressive Disclosure in SKILL.md")

    # Test 8: SKILL.md is slim
    if skill_path and os.path.isfile(skill_path):
        with open(skill_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        if len(lines) < 500:
            passed(f"SKILL.md is slim ({len(lines)} lines)")
        elif len(lines) < 800:
            warned(f"SKILL.md is {len(lines)} lines (acceptable but could be slimmer)")
        else:
            failed(f"SKILL.md is {len(lines)} lines — too long for slim core")


# ============================================================
# Suite: Quality & Anti-Pattern
# ============================================================

def run_quality_suite(skill_root):
    """Quality assurance regression tests."""
    suite_header("Quality & Anti-Pattern")

    # Test 1: Anti-patternization exists
    ap_file = os.path.join(skill_root, "references", "quality", "anti-patternization.md")
    if os.path.isfile(ap_file):
        with open(ap_file, "r", encoding="utf-8") as f:
            content = f.read()
        if "anti-pattern" in content.lower() or "反模式" in content:
            passed("Anti-Patternization Layer defined")
        else:
            warned("Anti-Patternization concept not explicit")
    else:
        failed("anti-patternization.md not found")

    # Test 2: Natural depth exists
    nd_file = os.path.join(skill_root, "references", "angle", "natural-depth.md")
    if os.path.isfile(nd_file):
        passed("Natural Depth Layer present")
    else:
        failed("natural-depth.md not found")

    # Test 3: Dynamic angle discovery exists
    da_file = os.path.join(skill_root, "references", "angle", "dynamic-angle-discovery.md")
    if os.path.isfile(da_file):
        with open(da_file, "r", encoding="utf-8") as f:
            content = f.read()
        if "angle" in content.lower() or "角度" in content:
            passed("Dynamic Angle Discovery Engine present")
        else:
            warned("Dynamic Angle Discovery content unclear")
    else:
        failed("dynamic-angle-discovery.md not found")

    # Test 4: Final output polish exists
    fo_file = os.path.join(skill_root, "references", "quality", "final-output.md")
    if os.path.isfile(fo_file):
        passed("Final Output polish reference present")
    else:
        warned("final-output.md not found")

    # Test 5: Default length engine exists
    dl_file = os.path.join(skill_root, "references", "quality", "default-length-engine.md")
    if os.path.isfile(dl_file):
        with open(dl_file, "r", encoding="utf-8") as f:
            content = f.read()
        if "word" in content.lower() or "字数" in content or "长度" in content:
            passed("Default Length Engine present")
        else:
            warned("Default Length Engine content unclear")
    else:
        failed("default-length-engine.md not found")

    # Test 6: Internal metadata leak prevention
    skill_path = os.path.join(skill_root, "SKILL.md")
    if skill_path and os.path.isfile(skill_path):
        with open(skill_path, "r", encoding="utf-8") as f:
            content = f.read()
        if "sanitiz" in content.lower() or "metadata" in content.lower():
            passed("Output sanitization / metadata safety referenced")
        else:
            warned("No output sanitization mentioned in SKILL.md")

    # Test 7: Dynamic angle repetition prevention
    if da_file and os.path.isfile(da_file):
        with open(da_file, "r", encoding="utf-8") as f:
            content = f.read()
        if "repetition" in content.lower() or "重复" in content or "diversity" in content.lower() or "多样性" in content:
            passed("Angle repetition prevention defined")
        else:
            warned("Angle repetition prevention not explicit")


# ============================================================
# Suite: Compliance
# ============================================================

def run_compliance_suite(skill_root):
    """Compliance and safety regression tests."""
    suite_header("Compliance & Safety")

    # Test 1: Compliance reference exists
    comp_file = os.path.join(skill_root, "references", "quality", "compliance.md")
    if os.path.isfile(comp_file):
        passed("Compliance reference present")
    else:
        warned("compliance.md not found")

    # Test 2: No health claims rule
    skill_path = os.path.join(skill_root, "SKILL.md")
    if skill_path and os.path.isfile(skill_path):
        with open(skill_path, "r", encoding="utf-8") as f:
            content = f.read()
        if "compliance" in content.lower() or "合规" in content:
            passed("Compliance referenced in SKILL.md")
        else:
            warned("Compliance not referenced in SKILL.md")

    # Test 3: Fake demonstration prohibition
    purpose_file = os.path.join(skill_root, "references", "execution", "purpose-integrity.md")
    if os.path.isfile(purpose_file):
        with open(purpose_file, "r", encoding="utf-8") as f:
            content = f.read()
        if "fake" in content.lower() or "虚假" in content or "伪造" in content:
            passed("Fake demonstration prohibition defined")
        else:
            warned("Fake demonstration prohibition not explicit")

    # Test 4: Competitor fabrication prohibition
    ext_file = os.path.join(skill_root, "references", "external", "external-intelligence.md")
    if os.path.isfile(ext_file):
        with open(ext_file, "r", encoding="utf-8") as f:
            content = f.read()
        if "competitor" in content.lower() or "竞争" in content:
            passed("Competitor claim rules present")
        else:
            warned("Competitor claim rules not found")

    # Test 5: Build secret scanning (verify build script has it)
    build_script = os.path.join(skill_root, "scripts", "build_package.py")
    if os.path.isfile(build_script):
        with open(build_script, "r", encoding="utf-8") as f:
            content = f.read()
        if "secret" in content.lower() and "scan" in content.lower():
            passed("Build script includes secret scanning")
        else:
            warned("Build script missing secret scanning")
    else:
        failed("build_package.py not found")


# ============================================================
# Suite: Static Contract (PATCH 28/29/30/31/32)
# ============================================================

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

METADATA_TERMS = [
    "angle", "角度", "closing family", "收口家族", "cta family",
    "product role", "ip asset", "qa", "score", "评分", "fingerprint",
    "primary proof", "route",
]

FORBIDDEN_CAPABILITY_NAMES = [
    "CODE_EXEC", "WEB-SEARCH", "FILE-READ", "FILE-SEARCH",
    "CODE-EXECUTION", "WEBSEARCH", "FILEREAD", "FILESEARCH",
    "STRUCTURED-OUTPUT",
]

STALE_SECTION_LINK_PATTERNS = [
    r"主SKILL\s*第\s*(2[2-9]|3[0-9])\s*节",
    r"主SKILL\s*第\s*(2[2-9]|3[0-9])\s*部分",
    r"SKILL\s*第\s*(2[2-9]|3[0-9])\s*节",
]


def run_static_contract_suite(skill_root):
    """Static contract tests (PATCH 28)."""
    suite_header("Static Contract Tests")

    # ---- CTA permission conflict (PATCH 29) ----
    cta_path = os.path.join(skill_root, "references", "craft", "cta.md")
    implicit_default = False
    if os.path.isfile(cta_path):
        with open(cta_path, "r", encoding="utf-8") as f:
            cta_content = f.read()
        if "IMPLICIT_ONLY" in cta_content:
            implicit_default = True

    if implicit_default:
        passed("CTA source of truth defines IMPLICIT_ONLY default")
    else:
        failed("CTA source of truth missing IMPLICIT_ONLY default")

    cta_conflicts = []
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
                cta_conflicts.append(f"{rel}: {m.group(0)[:50]}")
    if cta_conflicts:
        failed("CTA permission conflicts found", "; ".join(cta_conflicts[:5]))
    else:
        passed("No CTA permission conflicts")

    # ---- Full-caliber implicit CTA contract (v4.12.0) ----
    if os.path.isfile(cta_path):
        with open(cta_path, "r", encoding="utf-8") as f:
            cta_content = f.read()
        if "全口径默认高级隐式收口" in cta_content or "全口径硬约束" in cta_content:
            passed("CTA source of truth declares full-caliber implicit closing")
        else:
            failed("CTA source of truth missing full-caliber implicit closing contract")
        stale_caliber = [
            "显式动作、隐式续接、无指令缺口均可",
            "显式动作可选",
            "显式咨询可选",
            "引导预约",
            "想不错过本期，下方预约点一下",
        ]
        stale_hits = [p for p in stale_caliber if p in cta_content]
        if stale_hits:
            failed("CTA caliber table still permits explicit actions", "; ".join(stale_hits))
        else:
            passed("CTA caliber table has no explicit-action defaults")
        if "高级隐式收口" in cta_content and "零动作指令" in cta_content:
            passed("CTA source of truth defines advanced implicit closing QC")
        else:
            failed("CTA source of truth missing advanced implicit closing QC")
    examples_path = os.path.join(skill_root, "references", "craft", "examples.md")
    if os.path.isfile(examples_path):
        with open(examples_path, "r", encoding="utf-8") as f:
            examples_content = f.read()
        old_watch_row = "| 看播 | 【价值预告】，想【了解什么】的，进直播间来看"
        old_reserve_row = "| 预约 | 想不错过【内容主题】，下方预约点一下，开播我提醒你"
        if old_watch_row in examples_content:
            failed("examples.md still shows explicit watch-live CTA as positive template")
        else:
            passed("examples.md watch-live CTA is implicit-only")
        if old_reserve_row in examples_content:
            failed("examples.md still shows explicit reservation CTA as positive template")
        else:
            passed("examples.md reservation CTA is implicit-only")
    skill_path = os.path.join(skill_root, "SKILL.md")
    if os.path.isfile(skill_path):
        with open(skill_path, "r", encoding="utf-8") as f:
            skill_content = f.read()
        if "全口径默认高级隐式收口" in skill_content:
            passed("SKILL.md declares full-caliber implicit closing")
        else:
            failed("SKILL.md missing full-caliber implicit closing rule")

    # ---- Metadata leak (PATCH 30) ----
    leak_found = False
    targets = []
    skill_path = os.path.join(skill_root, "SKILL.md")
    if os.path.isfile(skill_path):
        targets.append(("SKILL.md", skill_path))
    refs_dir = os.path.join(skill_root, "references")
    if os.path.isdir(refs_dir):
        for path in iter_markdown_files(refs_dir):
            targets.append((os.path.relpath(path, skill_root).replace("\\", "/"), path))

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
                    failed(f"Metadata leak: {name} requires default output of '{term}'")
                    leak_found = True
    if not leak_found:
        passed("No default output template requires internal metadata")

    # ---- Source separation (PATCH 31) ----
    schemas_dir = os.path.join(skill_root, "schemas")
    if os.path.isdir(schemas_dir):
        pf_path = os.path.join(schemas_dir, "product-facts.schema.json")
        if os.path.isfile(pf_path):
            try:
                with open(pf_path, "r", encoding="utf-8") as f:
                    pf = json.load(f)
                enum = pf["properties"]["key_facts"]["items"]["properties"]["source_type"]["enum"]
                if enum == ["P1_PRODUCT_FACT"]:
                    passed("Product Facts schema only accepts P1_PRODUCT_FACT")
                else:
                    failed("Product Facts schema source_type must be only P1_PRODUCT_FACT", str(enum))
                pf_str = json.dumps(pf)
                if "commercial_relationship" in pf_str or "commercial_identity" in pf_str:
                    failed("Product Facts schema must not contain commercial relationship")
                else:
                    passed("Product Facts schema has no commercial relationship")
            except (KeyError, TypeError, json.JSONDecodeError):
                failed("Product Facts schema source_type enum missing/invalid")
        else:
            failed("product-facts.schema.json not found")

        ri_path = os.path.join(schemas_dir, "route-instance.schema.json")
        if os.path.isfile(ri_path):
            try:
                with open(ri_path, "r", encoding="utf-8") as f:
                    ri = json.load(f)
                props = ri.get("properties", {})
                required_route = ["commercial_relationship", "cta_permission", "closing_strategy", "verification_limits"]
                missing = [f for f in required_route if f not in props]
                if missing:
                    failed("route-instance.schema.json missing route variables", ", ".join(missing))
                else:
                    passed("route-instance.schema.json has full route variables")
                if "hard_gate_exceptions" in props:
                    failed("route-instance.schema.json must not contain hard_gate_exceptions")
            except json.JSONDecodeError:
                failed("route-instance.schema.json invalid JSON")
        else:
            failed("route-instance.schema.json not found")

        for schema_name in ["research-brief.schema.json", "ip-facts.schema.json"]:
            if os.path.isfile(os.path.join(schemas_dir, schema_name)):
                passed(f"{schema_name} present")
            else:
                failed(f"{schema_name} not found")
    else:
        failed("schemas/ directory not found")

    # ---- Capability naming (PATCH 32) ----
    cap_violations = []
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
                        cap_violations.append(f"{rel}: {m.group(0)}")
                else:
                    if re.search(r"\b" + re.escape(name) + r"\b", content, re.IGNORECASE):
                        cap_violations.append(f"{rel}: {name}")
    if cap_violations:
        failed("Capability naming violations", "; ".join(cap_violations[:5]))
    else:
        passed("All capability names canonical (no CODE_EXEC)")

    # ---- Stale section links (PATCH 21) ----
    stale_links = []
    for path in iter_markdown_files(skill_root):
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        rel = os.path.relpath(path, skill_root).replace("\\", "/")
        for pattern in STALE_SECTION_LINK_PATTERNS:
            m = re.search(pattern, content)
            if m:
                stale_links.append(f"{rel}: {m.group(0)}")
    if stale_links:
        failed("Stale SKILL section links found", "; ".join(stale_links[:5]))
    else:
        passed("No stale '主SKILL第N节' links")

    # ---- Product Acquisition contract (PATCH 14/22/03) ----
    ri_path = os.path.join(skill_root, "schemas", "route-instance.schema.json")
    if os.path.isfile(ri_path):
        try:
            with open(ri_path, "r", encoding="utf-8") as f:
                ri = json.load(f)
            props = ri.get("properties", {})
            missing_pa = [f for f in [
                "product_identity_status", "product_fact_sufficiency", "product_retrieval_status"
            ] if f not in props]
            if missing_pa:
                failed("route-instance.schema.json missing product acquisition fields", ", ".join(missing_pa))
            else:
                passed("route-instance.schema.json has product acquisition fields")
            pfs_enum = props.get("product_fact_source", {}).get("enum", [])
            missing_web_src = [s for s in ["official_web", "authorized_official_listing", "mixed_verified"] if s not in pfs_enum]
            if missing_web_src:
                failed("product_fact_source enum missing official web sources", ", ".join(missing_web_src))
            else:
                passed("product_fact_source includes official web sources")
        except json.JSONDecodeError:
            failed("route-instance.schema.json invalid JSON")
    else:
        failed("route-instance.schema.json not found")

    pa_ref = os.path.join(skill_root, "references", "execution", "product-acquisition.md")
    if os.path.isfile(pa_ref):
        passed("references/execution/product-acquisition.md present")
    else:
        failed("references/execution/product-acquisition.md not found")

    skill_path_pa = os.path.join(skill_root, "SKILL.md")
    if os.path.isfile(skill_path_pa):
        with open(skill_path_pa, "r", encoding="utf-8") as f:
            skill_pa = f.read()
        if "Search Before Ask" in skill_pa or "PRE-GATE 0" in skill_pa:
            passed("SKILL.md references Search Before Ask / PRE-GATE 0")
        else:
            failed("SKILL.md missing Search Before Ask / PRE-GATE 0 reference")

    premature_patterns = [
        r"请提供[：:][^。\n]{0,60}(?:成分表|配料表|营养表|规格|价格|售后)",
        r"请(?:上传|提供|发我|发给我)(?:详情页|配料表|产品资料)",
        r"资料不足[，,]?(?:无法完成|请提供|请上传)",
    ]
    negation_words = ["禁止", "不得", "不要", "不", "别", "勿", "except", "forbidden", "prohibit"]

    def is_negated_context(content, match_start):
        start = max(0, match_start - 40)
        context = content[start:match_start]
        return any(w in context for w in negation_words)

    premature_found = []
    for path in iter_markdown_files(skill_root):
        rel = os.path.relpath(path, skill_root).replace("\\", "/")
        if not is_canonical_content(rel):
            continue
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        content = strip_negative_examples(content)
        for pattern in premature_patterns:
            for m in re.finditer(pattern, content, re.IGNORECASE):
                if is_negated_context(content, m.start()):
                    continue
                premature_found.append(f"{rel}: {m.group(0)[:50]}")
    if premature_found:
        failed("Premature Information Request patterns found", "; ".join(premature_found[:5]))
    else:
        passed("No premature information request patterns in canonical content")

    # ---- Claim Authority contract (PATCH v4.7.0) ----
    if os.path.isfile(ri_path):
        try:
            with open(ri_path, "r", encoding="utf-8") as f:
                ri = json.load(f)
            props = ri.get("properties", {})
            missing_ca = [f for f in [
                "product_regulatory_category", "claim_authority_level",
                "claim_strength", "commercial_value_path"
            ] if f not in props]
            if missing_ca:
                failed("route-instance.schema.json missing claim authority fields", ", ".join(missing_ca))
            else:
                passed("route-instance.schema.json has claim authority fields")
            cat_enum = props.get("product_regulatory_category", {}).get("enum", [])
            if len(cat_enum) >= 8:
                passed("product_regulatory_category has 8+ categories")
            else:
                failed("product_regulatory_category enum too small", str(cat_enum))
            lvl_enum = props.get("claim_authority_level", {}).get("enum", [])
            if len(lvl_enum) == 7:
                passed("claim_authority_level has L0-L6 (7 levels)")
            else:
                failed("claim_authority_level enum must be 7 levels (L0-L6)", str(lvl_enum))
        except json.JSONDecodeError:
            failed("route-instance.schema.json invalid JSON (claim authority)")

    ca_ref = os.path.join(skill_root, "references", "execution", "claim-authority.md")
    if os.path.isfile(ca_ref):
        passed("references/execution/claim-authority.md present")
    else:
        failed("references/execution/claim-authority.md not found")

    if os.path.isfile(skill_path_pa):
        with open(skill_path_pa, "r", encoding="utf-8") as f:
            skill_ca = f.read()
        if "Claim Authority" in skill_ca and "Claim Ceiling" in skill_ca:
            passed("SKILL.md references Claim Authority / Claim Ceiling")
        else:
            failed("SKILL.md missing Claim Authority / Claim Ceiling reference")

    word_replacer = [
        r"改善睡眠\s*(?:→|->)\s*夜里更踏实",
        r"提高免疫\s*(?:→|->)\s*身体更有底",
        r"补血\s*(?:→|->)\s*脸色更漂亮",
        r"抗疲劳\s*(?:→|->)\s*下午不垮",
    ]
    replacer_found = []
    replacer_negation = ["禁止", "不得", "不要", "不", "别", "勿", "forbidden", "prohibit", "except"]

    def is_replacer_negated(content, match_start):
        line_start = content.rfind("\n", 0, match_start) + 1
        context = content[line_start:match_start]
        return any(w in context for w in replacer_negation)

    for path in iter_markdown_files(skill_root):
        rel = os.path.relpath(path, skill_root).replace("\\", "/")
        if not is_canonical_content(rel):
            continue
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        content = strip_negative_examples(content)
        for pattern in word_replacer:
            for m in re.finditer(pattern, content, re.IGNORECASE):
                if is_replacer_negated(content, m.start()):
                    continue
                replacer_found.append(f"{rel}: {m.group(0)[:50]}")
    if replacer_found:
        failed("Forbidden-word → safe-substitute mapping found", "; ".join(replacer_found[:5]))
    else:
        passed("No forbidden-word → safe-substitute mapping tables")

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
        passed("Semantic Claim Check declared (user-understood effect)")
    else:
        failed("Semantic Claim Check not declared in canonical content")

    # ---- Pain Translation contract (PATCH v4.8.0) ----
    if os.path.isfile(ri_path):
        try:
            with open(ri_path, "r", encoding="utf-8") as f:
                ri = json.load(f)
            props = ri.get("properties", {})
            missing_pt = [f for f in [
                "implication_level", "pain_distance",
                "pain_translation_path", "benefit_translation_domain"
            ] if f not in props]
            if missing_pt:
                failed("route-instance.schema.json missing pain translation fields", ", ".join(missing_pt))
            else:
                passed("route-instance.schema.json has pain translation fields")
            imp_enum = props.get("implication_level", {}).get("enum", [])
            if len(imp_enum) == 7 and "I5_A_HARD_PROHIBITION" in imp_enum:
                passed("implication_level has I1-I4 + I5-A/B/C (7 levels, v4.11.0)")
            else:
                failed("implication_level enum must be 7 levels (I1-I4, I5-A/B/C)", str(imp_enum))
            dist_enum = props.get("pain_distance", {}).get("enum", [])
            if len(dist_enum) == 3 and "PARTIAL_PAIN" in dist_enum:
                passed("pain_distance has DIRECT_PAIN / PARTIAL_PAIN / CONTEXT_PAIN (v4.11.0)")
            else:
                failed("pain_distance enum must be DIRECT_PAIN / PARTIAL_PAIN / CONTEXT_PAIN", str(dist_enum))
            ci_enum = props.get("commercial_intensity", {}).get("enum", [])
            if ci_enum == ["CONSERVATIVE", "STANDARD", "AGGRESSIVE"]:
                passed("commercial_intensity has CONSERVATIVE / STANDARD / AGGRESSIVE (v4.11.0)")
            else:
                failed("commercial_intensity enum must be CONSERVATIVE / STANDARD / AGGRESSIVE", str(ci_enum))
        except json.JSONDecodeError:
            failed("route-instance.schema.json invalid JSON (pain translation)")

    ibp_ref = os.path.join(skill_root, "references", "execution", "implicit-benefit-pain.md")
    if os.path.isfile(ibp_ref):
        passed("references/execution/implicit-benefit-pain.md present")
    else:
        failed("references/execution/implicit-benefit-pain.md not found")

    if os.path.isfile(skill_path_pa):
        with open(skill_path_pa, "r", encoding="utf-8") as f:
            skill_pt = f.read()
        if "Pain Translation" in skill_pt and "Implication" in skill_pt:
            passed("SKILL.md references Pain Translation / Implication Ladder")
        else:
            failed("SKILL.md missing Pain Translation / Implication Ladder reference")
        if "Semantic Destination Test" in skill_pt:
            passed("SKILL.md references Semantic Destination Test")
        else:
            failed("SKILL.md missing Semantic Destination Test reference")

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
        passed("Semantic Destination Test declared (audit meaning, not vocabulary)")
    else:
        failed("Semantic Destination Test not declared in canonical content")

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
        passed("Intensify real friction / no invented health fear declared")
    else:
        failed("Intensify real friction / no invented health fear not declared in canonical content")

    # ---- Commercial Intensity contract (PATCH v4.11.0) ----
    # I5-A / I5-B / I5-C declared in implicit-benefit-pain.md
    if os.path.isfile(ibp_ref):
        with open(ibp_ref, "r", encoding="utf-8") as f:
            ibp_c = f.read()
        for tag in ["I5-A", "I5-B", "I5-C"]:
            if tag in ibp_c:
                passed(f"implicit-benefit-pain.md declares {tag}")
            else:
                failed(f"implicit-benefit-pain.md missing {tag} declaration")

    # PARTIAL_PAIN declared
    if os.path.isfile(ibp_ref):
        if "PARTIAL_PAIN" in ibp_c:
            passed("implicit-benefit-pain.md declares PARTIAL_PAIN")
        else:
            failed("implicit-benefit-pain.md missing PARTIAL_PAIN")

    # COMMERCIAL_INTENSITY declared in claim-authority.md
    ca_ref = os.path.join(skill_root, "references", "execution", "claim-authority.md")
    if os.path.isfile(ca_ref):
        with open(ca_ref, "r", encoding="utf-8") as f:
            ca_c = f.read()
        if "COMMERCIAL_INTENSITY" in ca_c and "CONSERVATIVE" in ca_c and "AGGRESSIVE" in ca_c:
            passed("claim-authority.md declares COMMERCIAL_INTENSITY (CONSERVATIVE/STANDARD/AGGRESSIVE)")
        else:
            failed("claim-authority.md missing COMMERCIAL_INTENSITY declaration")
    else:
        failed("references/execution/claim-authority.md not found")

    # Edge Expression Policy (GREEN/AMBER/RED) + Category-Differentiated Ceiling
    cef_ref = os.path.join(skill_root, "references", "execution", "commercial-expression-freedom.md")
    if os.path.isfile(cef_ref):
        with open(cef_ref, "r", encoding="utf-8") as f:
            cef_c = f.read()
        if "Edge Expression Policy" in cef_c and "GREEN" in cef_c and "AMBER" in cef_c and "RED" in cef_c:
            passed("commercial-expression-freedom.md declares Edge Expression Policy (GREEN/AMBER/RED)")
        else:
            failed("commercial-expression-freedom.md missing Edge Expression Policy (GREEN/AMBER/RED)")
        if "品类差异化天花板" in cef_c or "Category-Differentiated Ceiling" in cef_c:
            passed("commercial-expression-freedom.md declares Category-Differentiated Ceiling")
        else:
            failed("commercial-expression-freedom.md missing Category-Differentiated Ceiling")
    else:
        failed("references/execution/commercial-expression-freedom.md not found")

    # Category-Differentiated Anxiety Intensity
    aps_ref = os.path.join(skill_root, "references", "execution", "anxiety-pain-scenification.md")
    if os.path.isfile(aps_ref):
        with open(aps_ref, "r", encoding="utf-8") as f:
            aps_c = f.read()
        if "品类差异化焦虑强度" in aps_c or "Category-Differentiated Anxiety Intensity" in aps_c:
            passed("anxiety-pain-scenification.md declares Category-Differentiated Anxiety Intensity")
        else:
            failed("anxiety-pain-scenification.md missing Category-Differentiated Anxiety Intensity")
    else:
        failed("references/execution/anxiety-pain-scenification.md not found")

    # Semantic Back-Translation recoverable (CONVERSION_RECOVERY)
    bt_rec = False
    for path in iter_markdown_files(skill_root):
        rel = os.path.relpath(path, skill_root).replace("\\", "/")
        if not is_canonical_content(rel):
            continue
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        if "CONVERSION_RECOVERY" in content and "Back-Translation" in content:
            bt_rec = True
            break
    if bt_rec:
        passed("Semantic Back-Translation recoverable (CONVERSION_RECOVERY) declared")
    else:
        failed("Semantic Back-Translation recoverable (CONVERSION_RECOVERY) not declared")

    # I5-A hard-bottom phrases stay prohibited in canonical content (negated contexts only)
    i5a_patterns = [
        r"改善疾病", r"预防疾病", r"治疗", r"改善某生理指标", r"改善激素",
        r"补血", r"抗疲劳", r"提高免疫", r"改善睡眠", r"减肥", r"改善月经",
        r"改善某器官功能",
    ]
    negation = ["禁止", "不得", "不要", "不", "别", "勿", "forbidden", "prohibit", "except", "no", "not", "never", "without"]

    def _is_negated(content, start, end):
        back = content[max(0, start - 400):start]
        fwd = content[end:end + 400]
        return any(w in back for w in negation) or any(w in fwd for w in negation)

    i5a_hits = []
    for path in iter_markdown_files(skill_root):
        rel = os.path.relpath(path, skill_root).replace("\\", "/")
        if not is_canonical_content(rel):
            continue
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        content = strip_negative_examples(content)
        for pat in i5a_patterns:
            for m in re.finditer(pat, content, re.IGNORECASE):
                if _is_negated(content, m.start(), m.end()):
                    continue
                i5a_hits.append(f"{rel}: {m.group(0)[:40]}")
    if i5a_hits:
        failed("I5-A hard-bottom phrase outside prohibition context", "; ".join(i5a_hits[:3]))
    else:
        passed("I5-A hard-bottom phrases appear only in prohibition contexts")

    # SKILL.md declares Commercial Intensity (4.32)
    if os.path.isfile(skill_path_pa):
        with open(skill_path_pa, "r", encoding="utf-8") as f:
            skill_ci = f.read()
        if "Commercial Intensity" in skill_ci and "CONSERVATIVE" in skill_ci and "AGGRESSIVE" in skill_ci:
            passed("SKILL.md declares Commercial Intensity (CONSERVATIVE/STANDARD/AGGRESSIVE)")
        else:
            failed("SKILL.md missing Commercial Intensity declaration")

    # ---- Boundary is Internal contract (PATCH v4.11.1) ----
    # 1. commercial-expression-freedom.md declares Boundary is Internal, Not Content
    if os.path.isfile(cef_ref):
        with open(cef_ref, "r", encoding="utf-8") as f:
            cef_c = f.read()
        if "Boundary is Internal, Not Content" in cef_c and "边界是内部审查标准" in cef_c:
            passed("commercial-expression-freedom.md declares Boundary is Internal, Not Content")
        else:
            failed("commercial-expression-freedom.md missing Boundary is Internal, Not Content")
        if "免责声明式表达（禁止）" in cef_c and "说教式表达（禁止）" in cef_c:
            passed("commercial-expression-freedom.md prohibits disclaimer & didactic expressions")
        else:
            failed("commercial-expression-freedom.md missing disclaimer/didactic prohibition")
    else:
        failed("references/execution/commercial-expression-freedom.md not found (Boundary is Internal)")

    # 2. Old 'must expose real boundary in text' requirement removed (only in prohibition context)
    old_boundary_hits = []
    for path in iter_markdown_files(skill_root):
        rel = os.path.relpath(path, skill_root).replace("\\", "/")
        if not is_canonical_content(rel):
            continue
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        for m in re.finditer(r"露出真实边界", content):
            back = content[max(0, m.start() - 30):m.start()]
            if any(w in back for w in ["不再要求", "禁止", "不得", "不要", "不", "别", "勿"]):
                continue
            old_boundary_hits.append(f"{rel}: {m.group(0)}")
    if old_boundary_hits:
        failed("Old 'must expose real boundary in text' requirement still present", "; ".join(old_boundary_hits[:3]))
    else:
        passed("Old 'expose real boundary in text' requirement removed (v4.11.1)")

    # 3. PARTIAL_PAIN boundary is internal (not content)
    if os.path.isfile(ibp_ref):
        with open(ibp_ref, "r", encoding="utf-8") as f:
            ibp_c = f.read()
        if "边界体现在" in ibp_c and "不夸大" in ibp_c and "禁止在文案里主动声明边界/免责" in ibp_c:
            passed("implicit-benefit-pain.md PARTIAL_PAIN boundary = internal non-exaggeration")
        else:
            failed("implicit-benefit-pain.md PARTIAL_PAIN missing internal-boundary rule")
    else:
        failed("references/execution/implicit-benefit-pain.md not found (Boundary is Internal)")

    # 4. Relief Contrast After prohibits disclaimer tone
    if os.path.isfile(aps_ref):
        with open(aps_ref, "r", encoding="utf-8") as f:
            aps_c = f.read()
        if "After 禁止免责语气" in aps_c and "不能抢走购买理由" in aps_c:
            passed("anxiety-pain-scenification.md Relief Contrast After prohibits disclaimer tone")
        else:
            failed("anxiety-pain-scenification.md missing After disclaimer-tone prohibition")
    else:
        failed("references/execution/anxiety-pain-scenification.md not found (Relief Contrast)")

    # 5. SKILL.md declares Boundary is Internal
    if os.path.isfile(skill_path_pa):
        with open(skill_path_pa, "r", encoding="utf-8") as f:
            skill_bi = f.read()
        if "Boundary is Internal" in skill_bi and "抢走购买理由" in skill_bi:
            passed("SKILL.md declares Boundary is Internal, Not Content")
        else:
            failed("SKILL.md missing Boundary is Internal declaration")

    # 6. Disclaimer/didactic phrases appear only in prohibition contexts (never as instructions)
    disclaim_didactic = [
        r"它不负责让你瘦", r"它不负责改善皮肤", r"我不指望它一夜之间改变什么",
        r"按法规，普通食品不能宣传功效", r"别被神药话术骗", r"那些话术听听就好",
        r"焦虑驱动的东西，往往买完就后悔", r"买之前先学会看这一行字",
    ]
    dd_negation = ["禁止", "不得", "不要", "不", "别", "勿", "forbidden", "prohibit", "except", "错误"]
    dd_hits = []
    for path in iter_markdown_files(skill_root):
        rel = os.path.relpath(path, skill_root).replace("\\", "/")
        if not is_canonical_content(rel):
            continue
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        for pat in disclaim_didactic:
            for m in re.finditer(pat, content):
                back = content[max(0, m.start() - 60):m.start()]
                fwd = content[m.end():m.end() + 60]
                if any(w in back for w in dd_negation) or any(w in fwd for w in dd_negation):
                    continue
                dd_hits.append(f"{rel}: {m.group(0)[:40]}")
    if dd_hits:
        failed("Disclaimer/didactic phrase outside prohibition context", "; ".join(dd_hits[:3]))
    else:
        passed("Disclaimer/didactic phrases appear only in prohibition contexts")

    # ---- Multi-row table template contract (PATCH v4.11.2 / v4.11.3) ----
    # 1. final-output.md declares multi-row table template for multi-version copy
    fo_ref = os.path.join(skill_root, "references", "quality", "final-output.md")
    if os.path.isfile(fo_ref):
        with open(fo_ref, "r", encoding="utf-8") as f:
            fo_c = f.read()
        if "多行表格" in fo_c and "版本标题行" in fo_c and "角度行" in fo_c and "完整口播稿行" in fo_c:
            passed("final-output.md declares multi-row table template (v4.11.2)")
        else:
            failed("final-output.md missing multi-row table template declaration")
        if "单表格" in fo_c:
            passed("final-output.md declares single-table option for 1-version copy")
        else:
            failed("final-output.md missing single-table option")
        if "唯一例外" in fo_c and "多版表格模板" in fo_c and "Angle（角度）作为表格行" in fo_c:
            passed("final-output.md declares angle-only output exception (multi-version table)")
        else:
            failed("final-output.md missing angle-only output exception")
        if "收口家族行" not in fo_c and "Closing Family（收口家族）任何场景都不输出" in fo_c:
            passed("final-output.md removes closing-family row from table template (v4.11.3)")
        else:
            failed("final-output.md still exposes closing-family row in table template")
    else:
        failed("references/quality/final-output.md not found (table template)")

    # 2. SKILL.md synchronizes the multi-row table template
    if os.path.isfile(skill_path_pa):
        with open(skill_path_pa, "r", encoding="utf-8") as f:
            skill_tt = f.read()
        if "多行表格" in skill_tt and "版本标题行" in skill_tt and "角度行" in skill_tt and "完整口播稿行" in skill_tt:
            passed("SKILL.md synchronizes multi-row table template (v4.11.2)")
        else:
            failed("SKILL.md missing multi-row table template synchronization")
        if "唯一例外" in skill_tt and "多版表格模板" in skill_tt and "Angle（角度）作为表格行" in skill_tt:
            passed("SKILL.md declares angle-only output exception")
        else:
            failed("SKILL.md missing angle-only output exception")
        if "收口家族行" not in skill_tt and "Closing Family（收口家族）任何场景都不输出" in skill_tt:
            passed("SKILL.md removes closing-family row from table template (v4.11.3)")
        else:
            failed("SKILL.md still exposes closing-family row in table template")

    # 3. Single-version copy keeps internal metadata internal (no table template)
    if os.path.isfile(fo_ref):
        with open(fo_ref, "r", encoding="utf-8") as f:
            fo_c = f.read()
        if "单版轻量输出时角度也保持内部" in fo_c:
            passed("final-output.md keeps single-version lightweight output internal")
        else:
            failed("final-output.md missing single-version internal-metadata rule")



# ============================================================
# Suite: Behavioral (PATCH 28)
# ============================================================

def run_behavioral_suite(skill_root):
    """Behavioral regression tests — require an actual model run."""
    suite_header("Behavioral Regression Tests")

    # Check whether a model runner is configured
    model_available = os.environ.get("MASTER_COPYWRITING_MODEL") or os.environ.get("BEHAVIORAL_MODEL")
    runner_script = os.path.join(skill_root, "scripts", "run_behavioral_regression.py")

    if model_available and os.path.isfile(runner_script):
        # A model runner is configured; delegate to it.
        try:
            import subprocess
            result = subprocess.run(
                [sys.executable, runner_script, "--root", skill_root],
                capture_output=True, text=True, timeout=600,
            )
            print(result.stdout)
            if result.returncode == 0:
                passed("Behavioral regression (model run)")
            else:
                failed("Behavioral regression (model run)", result.stderr[:200])
        except Exception as e:
            failed("Behavioral regression runner failed", str(e)[:200])
    else:
        # No model executed → must report NOT RUN, never fake PASS.
        skipped("Behavioral regression", "NOT RUN — no model executed in this environment")
        print("  ⊘ Behavioral Regression = NOT RUN (PATCH 28/39: never fake PASS without a model run)")


# ============================================================
# Main
# ============================================================

SUITES = {
    "facts": run_facts_suite,
    "purposes": run_purposes_suite,
    "platforms": run_platforms_suite,
    "portability": run_portability_suite,
    "quality": run_quality_suite,
    "compliance": run_compliance_suite,
    "static-contract": run_static_contract_suite,
    "behavioral": run_behavioral_suite,
}


def main():
    parser = argparse.ArgumentParser(description="Run regression tests for Master Copywriting skill")
    parser.add_argument("--suite", type=str, default=None,
                        choices=list(SUITES.keys()) + ["all"],
                        help="Test suite to run")
    parser.add_argument("--all", action="store_true", help="Run all suites")
    parser.add_argument("--root", type=str, default=None, help="Skill root directory")

    args = parser.parse_args()

    if not (args.suite or args.all):
        args.all = True  # Default: run all

    if args.all:
        suites_to_run = list(SUITES.keys())
    else:
        suites_to_run = [args.suite]

    # Determine skill root
    if args.root:
        skill_root = os.path.abspath(args.root)
    else:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        skill_root = os.path.dirname(script_dir)

    print(f"Running regression tests on: {skill_root}")
    print(f"Suites: {', '.join(suites_to_run)}")

    # Run suites
    for suite_name in suites_to_run:
        if suite_name in SUITES:
            SUITES[suite_name](skill_root)

    # Summary
    total = PASS_COUNT + FAIL_COUNT + WARN_COUNT + SKIP_COUNT
    print(f"\n{'='*60}")
    print("REGRESSION TEST SUMMARY")
    print(f"{'='*60}")
    print(f"  Total:  {total}")
    print(f"  Pass:   {PASS_COUNT}")
    print(f"  Fail:   {FAIL_COUNT}")
    print(f"  Warn:   {WARN_COUNT}")
    print(f"  Skip:   {SKIP_COUNT}")

    if FAIL_COUNT > 0:
        print(f"\n✗ FAILED: {FAIL_COUNT} test(s) failed")
        return 1
    elif WARN_COUNT > 0:
        print(f"\n⚠ PASSED with warnings: {WARN_COUNT} warning(s)")
        return 0
    else:
        print(f"\n✓ ALL PASSED")
        return 0


if __name__ == "__main__":
    sys.exit(main())
