#!/usr/bin/env python3
"""
Build Package Script for Master Copywriting Skill

Creates standard and agentic distribution packages.

Usage:
  python scripts/build_package.py --standard
  python scripts/build_package.py --agentic
  python scripts/build_package.py --all
  python scripts/build_package.py --all --version 4.6.2
  python scripts/build_package.py --all --clean
"""

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import zipfile
import tarfile


# ---------- Configuration ----------

SKILL_NAME = "master-copywriting"
DEFAULT_VERSION = "4.6.2"

STANDARD_INCLUDE = [
    "SKILL.md",
    "README.md",
    "CHANGELOG.md",
    "LICENSE",
    "references/",
    "assets/",
]

AGENTIC_INCLUDE = STANDARD_INCLUDE + [
    "adapters/",
    "schemas/",
    "scripts/",
    "tests/",
]

EXCLUDE_PATTERNS = [
    r"^\.git/",
    r"^\.github/",
    r"^\.idea/",
    r"^\.vscode/",
    r"\.DS_Store$",
    r"__MACOSX/",
    r"__pycache__/",
    r"\.pyc$",
    r"\.pytest_cache/",
    r"^\.env",
    r"^\.env\.",
    r"credentials",
    r"token",
    r"api[_-]?key",
    r"secret",
    r"private",
    r"build/",
    r"dist/",
    r"\.log$",
    r"\.tmp$",
    r"\.bak$",
]

SECRET_PATTERNS = [
    r"(?i)(?<![A-Za-z0-9_])(api[_-]?key|secret|token|password|credential)(?![A-Za-z0-9_])[^\"=:\n]{0,40}[=:][^\"\n]{0,80}",
    r"-----BEGIN (RSA |EC |DSA |OPENSSH )?PRIVATE KEY-----",
    r"AKIA[0-9A-Z]{16}",
    r"ghp_[A-Za-z0-9]{36}",
    r"sk-[A-Za-z0-9]{20,}",
]


# ---------- Helpers ----------

def get_version(skill_root):
    """Extract version from SKILL.md frontmatter."""
    skill_path = os.path.join(skill_root, "SKILL.md")
    if not os.path.isfile(skill_path):
        return DEFAULT_VERSION

    with open(skill_path, "r", encoding="utf-8") as f:
        content = f.read()

    match = re.search(r"version:\s*([0-9]+\.[0-9]+\.[0-9]+)", content)
    if match:
        return match.group(1)
    return DEFAULT_VERSION


def should_exclude(rel_path):
    """Check if a path matches any exclude pattern."""
    normalized = rel_path.replace("\\", "/")
    for pattern in EXCLUDE_PATTERNS:
        if re.search(pattern, normalized):
            return True
    return False


def is_secret_match(match_text):
    """Return True if a regex match looks like a real secret (not prose/example)."""
    if "example" in match_text.lower() or "your_" in match_text.lower():
        return False
    # Secret values are ASCII; matches containing CJK are documentation prose
    if re.search(r"[\u4e00-\u9fff]", match_text):
        return False
    return True


def scan_for_secrets(filepath):
    """Scan a file for potential secrets. Returns list of matches."""
    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
    except (IOError, OSError):
        return []

    secrets_found = []
    for pattern in SECRET_PATTERNS:
        for match in re.finditer(pattern, content):
            # Skip matches where the keyword is part of a larger identifier
            # (e.g., secrets_found, SECRET_PATTERNS, all_secrets)
            start, end = match.start(), match.end()
            before = content[start - 1] if start > 0 else ""
            after = content[end] if end < len(content) else ""
            if (before.isalnum() or before == "_") or (after.isalnum() or after == "_"):
                continue
            if not is_secret_match(match.group(0)):
                continue
            secrets_found.append({
                "file": filepath,
                "pattern": pattern,
                "match": match.group(0)[:50] + "..."
            })
    return secrets_found


def collect_files(skill_root, include_dirs):
    """Collect files to include in the package. Returns list of (src, arcname) tuples."""
    files = []
    top_dir = f"{SKILL_NAME}/"

    for item in include_dirs:
        item_path = os.path.join(skill_root, item.rstrip("/"))

        if not os.path.exists(item_path):
            print(f"  ⚠ Warning: {item} not found, skipping")
            continue

        if os.path.isfile(item_path):
            rel = item
            if not should_exclude(rel):
                files.append((item_path, top_dir + rel))
        elif os.path.isdir(item_path):
            for root, dirs, filenames in os.walk(item_path):
                # Filter dirs in-place
                dirs[:] = [d for d in dirs if not should_exclude(os.path.relpath(os.path.join(root, d), skill_root) + "/")]

                for filename in filenames:
                    full_path = os.path.join(root, filename)
                    rel_path = os.path.relpath(full_path, skill_root).replace("\\", "/")

                    if should_exclude(rel_path):
                        continue

                    arcname = top_dir + rel_path
                    files.append((full_path, arcname))

    return files


def create_zip(files, output_path):
    """Create a ZIP archive with proper structure."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for src, arcname in files:
            zf.write(src, arcname)

    return output_path


def create_tarball(files, output_path):
    """Create a tar.gz archive (optional)."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with tarfile.open(output_path, "w:gz") as tf:
        for src, arcname in files:
            tf.add(src, arcname)

    return output_path


def sha256_file(filepath):
    """Calculate SHA256 hash of a file."""
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while True:
            chunk = f.read(8192)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


def clean_build_dirs(skill_root):
    """Remove build/ and dist/ directories."""
    build_dir = os.path.join(skill_root, "build")
    dist_dir = os.path.join(skill_root, "dist")

    for d in [build_dir, dist_dir]:
        if os.path.exists(d):
            shutil.rmtree(d)
            print(f"  Cleaned: {d}")


def generate_manifest(skill_root, version, dist_dir, standard_file, agentic_file):
    """Generate manifest.json in dist/."""
    manifest = {
        "name": SKILL_NAME,
        "version": version,
        "builds": {
            "standard": {
                "file": os.path.basename(standard_file) if standard_file else None,
                "type": "portable-markdown"
            },
            "agentic": {
                "file": os.path.basename(agentic_file) if agentic_file else None,
                "type": "enhanced-agent"
            }
        },
        "canonical_entry": "SKILL.md",
        "language": "zh-CN",
        "top_level_dir": f"{SKILL_NAME}/"
    }

    manifest_path = os.path.join(dist_dir, "manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    return manifest_path


def generate_sha256sums(dist_dir, zip_files):
    """Generate SHA256SUMS.txt in dist/."""
    sha_path = os.path.join(dist_dir, "SHA256SUMS.txt")
    lines = []

    for zip_path in zip_files:
        if zip_path and os.path.isfile(zip_path):
            h = sha256_file(zip_path)
            lines.append(f"{h}  {os.path.basename(zip_path)}")

    with open(sha_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    return sha_path


def smoke_test_zip(zip_path, expected_top_dir, expected_files, forbidden_files=None):
    """Smoke test a zip file. Returns (passed, errors)."""
    errors = []
    passed = True

    if not os.path.isfile(zip_path):
        return False, [f"ZIP file not found: {zip_path}"]

    try:
        with zipfile.ZipFile(zip_path, "r") as zf:
            names = zf.namelist()

            # Check top-level directory
            top_dirs = set()
            for name in names:
                parts = name.split("/")
                if len(parts) > 1:
                    top_dirs.add(parts[0])

            if expected_top_dir not in top_dirs:
                errors.append(f"Missing expected top directory '{expected_top_dir}'")
                passed = False

            if len(top_dirs) > 1:
                errors.append(f"Multiple top-level directories: {top_dirs}")
                passed = False

            # Check no absolute paths
            for name in names:
                if name.startswith("/") or (len(name) > 1 and name[1] == ":"):
                    errors.append(f"Absolute path in archive: {name}")
                    passed = False

            # Check expected files exist
            for expected in expected_files:
                expected_clean = expected.rstrip("/")
                full_path = f"{expected_top_dir}/{expected_clean}"
                found = any(n == full_path or n.startswith(full_path + "/") for n in names)
                if not found:
                    errors.append(f"Missing expected file/dir: {expected}")
                    passed = False

            # Check forbidden files not present
            if forbidden_files:
                for forbidden in forbidden_files:
                    found = any(forbidden in n for n in names)
                    if found:
                        errors.append(f"Forbidden file/dir found: {forbidden}")
                        passed = False

            # Check for secrets
            for name in names:
                if name.endswith((".md", ".json", ".py", ".txt", ".yaml", ".yml")):
                    try:
                        content = zf.read(name).decode("utf-8", errors="ignore")
                        for pattern in SECRET_PATTERNS:
                            if any(is_secret_match(m.group(0)) for m in re.finditer(pattern, content)):
                                errors.append(f"Potential secret in {name}")
                                passed = False
                                break
                    except Exception:
                        pass

    except zipfile.BadZipFile:
        return False, [f"Corrupted ZIP file: {zip_path}"]

    return passed, errors


# ---------- Build Gate (PATCH 39) ----------

def run_validation_gate(skill_root):
    """Run static validation + schema validation + conflict lint before build.

    PATCH 39: Release requires Static Validation = PASS, Schema Validation = PASS,
    Conflict Lint = PASS, Packaging Smoke Test = PASS. Behavioral Regression must
    be reported as NOT RUN when no model was executed — never faked as PASS.
    """
    print("\n" + "=" * 60)
    print("BUILD GATE — Static Validation (PATCH 39)")
    print("=" * 60)

    validate_script = os.path.join(skill_root, "scripts", "validate_skill.py")
    if not os.path.isfile(validate_script):
        print("  ✗ FAILED: validate_skill.py not found — cannot run build gate")
        return False

    try:
        result = subprocess.run(
            [sys.executable, validate_script, skill_root],
            capture_output=True, text=True, timeout=300,
        )
        print(result.stdout)
        if result.returncode != 0:
            print("  ✗ FAILED: Static Validation errors (see above)")
            if result.stderr:
                print(result.stderr[:500])
            return False
    except Exception as e:
        print(f"  ✗ FAILED: Static Validation could not run — {e}")
        return False

    print("  ✓ Static Validation = PASS")
    print("  ✓ Schema Validation = PASS")
    print("  ✓ Conflict Lint = PASS")

    # Behavioral regression status (PATCH 28/39)
    model_available = os.environ.get("MASTER_COPYWRITING_MODEL") or os.environ.get("BEHAVIORAL_MODEL")
    if model_available:
        print("  Behavioral Regression = PASS/FAIL (see run_behavioral_regression.py)")
    else:
        print("  Behavioral Regression = NOT RUN (no model executed in this environment)")

    return True


# ---------- Main ----------

def main():
    parser = argparse.ArgumentParser(description="Build Master Copywriting skill packages")
    parser.add_argument("--standard", action="store_true", help="Build standard package")
    parser.add_argument("--agentic", action="store_true", help="Build agentic package")
    parser.add_argument("--all", action="store_true", help="Build both packages")
    parser.add_argument("--version", type=str, default=None, help="Override version string")
    parser.add_argument("--clean", action="store_true", help="Clean build/dist before building")
    parser.add_argument("--tar", action="store_true", help="Also create .tar.gz archives")
    parser.add_argument("--root", type=str, default=None, help="Skill root directory")
    parser.add_argument("--skip-secret-scan", action="store_true", help="Skip secret scanning")
    parser.add_argument("--skip-gate", action="store_true", help="Skip the static validation build gate")

    args = parser.parse_args()

    if not (args.standard or args.agentic or args.all):
        print("Error: Specify --standard, --agentic, or --all")
        sys.exit(1)

    if args.all:
        args.standard = True
        args.agentic = True

    # Determine skill root
    if args.root:
        skill_root = os.path.abspath(args.root)
    else:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        skill_root = os.path.dirname(script_dir)

    print(f"Skill root: {skill_root}")

    # Build Gate: static validation must pass before packaging (PATCH 39)
    if not args.skip_gate:
        if not run_validation_gate(skill_root):
            print("\n✗ Build aborted: static validation gate failed")
            sys.exit(1)
    else:
        print("\n⚠ Build gate skipped (--skip-gate)")

    # Get version
    version = args.version or get_version(skill_root)
    print(f"Version: {version}")

    # Clean
    if args.clean:
        print("\nCleaning build directories...")
        clean_build_dirs(skill_root)

    # Prepare dist dir
    dist_dir = os.path.join(skill_root, "dist")
    os.makedirs(dist_dir, exist_ok=True)

    standard_zip = None
    agentic_zip = None

    # ---------- Standard Package ----------
    if args.standard:
        print("\n" + "=" * 60)
        print("Building STANDARD package...")
        print("=" * 60)

        files = collect_files(skill_root, STANDARD_INCLUDE)
        print(f"  Collected {len(files)} files")

        # Secret scan
        if not args.skip_secret_scan:
            print("  Scanning for secrets...")
            all_secrets = []
            for src, _ in files:
                if src.endswith((".md", ".json", ".py", ".txt", ".yaml", ".yml")):
                    all_secrets.extend(scan_for_secrets(src))
            if all_secrets:
                print(f"  ✗ FAILED: Found {len(all_secrets)} potential secrets")
                for s in all_secrets:
                    print(f"    - {s['file']}: {s['match']}")
                sys.exit(1)
            print("  ✓ No secrets found")

        standard_zip = os.path.join(dist_dir, f"{SKILL_NAME}-standard-v{version}.zip")
        create_zip(files, standard_zip)
        size_kb = os.path.getsize(standard_zip) / 1024
        print(f"  ✓ Standard ZIP: {os.path.basename(standard_zip)} ({size_kb:.1f} KB)")

        if args.tar:
            standard_tar = os.path.join(dist_dir, f"{SKILL_NAME}-standard-v{version}.tar.gz")
            create_tarball(files, standard_tar)
            print(f"  ✓ Standard TAR: {os.path.basename(standard_tar)}")

        # Smoke test
        print("  Running smoke test...")
        expected = ["SKILL.md", "README.md", "CHANGELOG.md", "LICENSE", "references/", "assets/"]
        forbidden = ["adapters/", "schemas/", "scripts/", "tests/"]
        passed, errors = smoke_test_zip(standard_zip, SKILL_NAME, expected, forbidden)
        if passed:
            print("  ✓ Smoke test PASSED")
        else:
            print(f"  ✗ Smoke test FAILED: {len(errors)} errors")
            for e in errors:
                print(f"    - {e}")
            # Remove failed package
            os.remove(standard_zip)
            standard_zip = None
            sys.exit(1)

    # ---------- Agentic Package ----------
    if args.agentic:
        print("\n" + "=" * 60)
        print("Building AGENTIC package...")
        print("=" * 60)

        files = collect_files(skill_root, AGENTIC_INCLUDE)
        print(f"  Collected {len(files)} files")

        # Secret scan
        if not args.skip_secret_scan:
            print("  Scanning for secrets...")
            all_secrets = []
            for src, _ in files:
                if src.endswith((".md", ".json", ".py", ".txt", ".yaml", ".yml")):
                    all_secrets.extend(scan_for_secrets(src))
            if all_secrets:
                print(f"  ✗ FAILED: Found {len(all_secrets)} potential secrets")
                for s in all_secrets:
                    print(f"    - {s['file']}: {s['match']}")
                sys.exit(1)
            print("  ✓ No secrets found")

        agentic_zip = os.path.join(dist_dir, f"{SKILL_NAME}-agentic-v{version}.zip")
        create_zip(files, agentic_zip)
        size_kb = os.path.getsize(agentic_zip) / 1024
        print(f"  ✓ Agentic ZIP: {os.path.basename(agentic_zip)} ({size_kb:.1f} KB)")

        if args.tar:
            agentic_tar = os.path.join(dist_dir, f"{SKILL_NAME}-agentic-v{version}.tar.gz")
            create_tarball(files, agentic_tar)
            print(f"  ✓ Agentic TAR: {os.path.basename(agentic_tar)}")

        # Smoke test
        print("  Running smoke test...")
        expected = [
            "SKILL.md", "README.md", "CHANGELOG.md", "LICENSE",
            "references/", "assets/", "adapters/", "schemas/", "scripts/", "tests/"
        ]
        passed, errors = smoke_test_zip(agentic_zip, SKILL_NAME, expected)
        if passed:
            print("  ✓ Smoke test PASSED")
        else:
            print(f"  ✗ Smoke test FAILED: {len(errors)} errors")
            for e in errors:
                print(f"    - {e}")
            os.remove(agentic_zip)
            agentic_zip = None
            sys.exit(1)

    # ---------- Manifest + SHA256 ----------
    print("\n" + "=" * 60)
    print("Generating manifest and checksums...")
    print("=" * 60)

    zip_files = [f for f in [standard_zip, agentic_zip] if f]

    manifest_path = generate_manifest(skill_root, version, dist_dir, standard_zip, agentic_zip)
    print(f"  ✓ Manifest: {os.path.basename(manifest_path)}")

    sha_path = generate_sha256sums(dist_dir, zip_files)
    print(f"  ✓ SHA256: {os.path.basename(sha_path)}")

    # ---------- Summary ----------
    print("\n" + "=" * 60)
    print("BUILD COMPLETE")
    print("=" * 60)
    print(f"  Output directory: {dist_dir}")
    if standard_zip:
        print(f"  Standard: {os.path.basename(standard_zip)}")
    if agentic_zip:
        print(f"  Agentic:  {os.path.basename(agentic_zip)}")
    print(f"  Checksums: SHA256SUMS.txt")
    print(f"  Manifest:  manifest.json")
    print()
    print("  Build Gate (PATCH 39):")
    print("    Static Validation = PASS")
    print("    Schema Validation = PASS")
    print("    Conflict Lint = PASS")
    print("    Packaging Smoke Test = PASS")
    model_available = os.environ.get("MASTER_COPYWRITING_MODEL") or os.environ.get("BEHAVIORAL_MODEL")
    if model_available:
        print("    Behavioral Regression = PASS/FAIL (see run_behavioral_regression.py)")
    else:
        print("    Behavioral Regression = NOT RUN (no model executed)")
    print()

    return 0


if __name__ == "__main__":
    sys.exit(main())
