#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
master-copywriting 技能更新器
从 GitHub 拉取最新版，覆盖安装到本地技能目录。

用法:
  python update_skill.py            # 检查并更新（有新版才更新）
  python update_skill.py --check    # 仅检查版本，不更新
  python update_skill.py --force    # 强制覆盖安装（版本相同也更新）
  python update_skill.py --dry-run  # 试运行：走完整流程但不实际覆盖

说明:
  - 版本来源: GitHub 仓库 sdhack/master-copywriting 的 main 分支
  - 覆盖前自动备份当前版本到 _backup/ 目录
  - 覆盖后自动运行 validate_skill.py 校验，失败则回滚备份
"""

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.request
from datetime import datetime
from pathlib import Path

REPO_URL = "https://github.com/sdhack/master-copywriting.git"
RAW_URL = "https://raw.githubusercontent.com/sdhack/master-copywriting/main/SKILL.md"
DEFAULT_BRANCH = "main"

# 本地技能安装目录（本脚本所在技能的上级目录）
LOCAL_DIR = Path(__file__).resolve().parent.parent
BACKUP_ROOT = LOCAL_DIR.parent / "_skill-backups"
BACKUP_DIR = BACKUP_ROOT / f"master-copywriting-{datetime.now():%Y%m%d-%H%M%S}"

VERSION_RE = re.compile(r"^\s*version:\s*([\w.]+)", re.MULTILINE)


def get_local_version() -> str:
    skill_md = LOCAL_DIR / "SKILL.md"
    if not skill_md.exists():
        return "0.0.0"
    m = VERSION_RE.search(skill_md.read_text(encoding="utf-8"))
    return m.group(1) if m else "0.0.0"


def get_remote_version() -> str:
    """通过 raw.githubusercontent.com 读取远程 SKILL.md 的版本号（轻量检查）。"""
    try:
        with urllib.request.urlopen(RAW_URL, timeout=30) as resp:
            text = resp.read().decode("utf-8")
        m = VERSION_RE.search(text)
        return m.group(1) if m else "unknown"
    except Exception as e:
        print(f"[错误] 无法获取远程版本: {e}")
        return "unknown"


def parse_version(v: str):
    nums = re.findall(r"\d+", v)
    return tuple(int(n) for n in nums) if nums else (0,)


def clone_to_temp() -> Path:
    """浅克隆远程仓库到临时目录，返回临时目录路径。"""
    tmp = Path(tempfile.mkdtemp(prefix="mcw-update-"))
    try:
        subprocess.run(
            ["git", "clone", "--depth", "1", "--branch", DEFAULT_BRANCH, REPO_URL, str(tmp / "repo")],
            check=True,
            capture_output=True,
            text=True,
        )
    except subprocess.CalledProcessError as e:
        print(f"[错误] git clone 失败: {e.stderr.strip()}")
        shutil.rmtree(tmp, ignore_errors=True)
        sys.exit(1)
    return tmp / "repo"


def backup_local() -> None:
    BACKUP_ROOT.mkdir(parents=True, exist_ok=True)
    shutil.copytree(LOCAL_DIR, BACKUP_DIR, ignore=shutil.ignore_patterns("__pycache__", ".git"))
    print(f"[备份] 当前版本已备份到 {BACKUP_DIR}")


def install_from(repo: Path) -> None:
    """用仓库内容覆盖本地技能目录（保留 .git 与 __pycache__ 不覆盖）。"""
    for item in repo.iterdir():
        if item.name in (".git", "__pycache__"):
            continue
        target = LOCAL_DIR / item.name
        if target.exists():
            if target.is_dir():
                shutil.rmtree(target)
            else:
                target.unlink()
        shutil.copytree(item, target) if item.is_dir() else shutil.copy2(item, target)
    print("[安装] 已用最新版覆盖本地技能目录")


def run_validation() -> bool:
    validator = LOCAL_DIR / "scripts" / "validate_skill.py"
    if not validator.exists():
        print("[提示] 未找到 validate_skill.py，跳过校验")
        return True
    try:
        result = subprocess.run(
            [sys.executable, str(validator)], capture_output=True, text=True, timeout=300
        )
        print(result.stdout[-2000:] if result.stdout else "")
        if result.returncode != 0:
            print(result.stderr[-2000:] if result.stderr else "")
        return result.returncode == 0
    except Exception as e:
        print(f"[提示] 校验执行异常，跳过: {e}")
        return True


def rollback() -> None:
    if not BACKUP_DIR.exists():
        return
    for item in LOCAL_DIR.iterdir():
        if item.name in (".git", "__pycache__"):
            continue
        if item.is_dir():
            shutil.rmtree(item)
        else:
            item.unlink()
    for item in BACKUP_DIR.iterdir():
        shutil.copytree(item, LOCAL_DIR / item.name) if item.is_dir() else shutil.copy2(
            item, LOCAL_DIR / item.name
        )
    print("[回滚] 校验失败，已恢复备份版本")


def main() -> None:
    parser = argparse.ArgumentParser(description="master-copywriting 技能更新器")
    parser.add_argument("--check", action="store_true", help="仅检查版本，不更新")
    parser.add_argument("--force", action="store_true", help="强制覆盖安装")
    parser.add_argument("--dry-run", action="store_true", help="试运行，不实际覆盖")
    args = parser.parse_args()

    local_ver = get_local_version()
    remote_ver = get_remote_version()
    print(f"本地版本: {local_ver}")
    print(f"远程版本: {remote_ver}")

    if remote_ver == "unknown":
        sys.exit(1)

    has_new = parse_version(remote_ver) > parse_version(local_ver)
    if args.check:
        if has_new:
            print(f"[检查] 发现新版本 {remote_ver}（本地 {local_ver}），可执行更新")
        else:
            print("[检查] 本地已是最新版本")
        return

    if not has_new and not args.force:
        print("[跳过] 本地已是最新版本（如需强制覆盖请加 --force）")
        return

    if args.dry_run:
        print("[试运行] 将执行: 备份当前版本 → 从 GitHub 覆盖安装 → 运行 validate_skill.py 校验")
        return

    print("[更新] 开始更新...")
    backup_local()
    repo = clone_to_temp()
    try:
        install_from(repo)
    finally:
        shutil.rmtree(repo.parent, ignore_errors=True)

    if run_validation():
        print(f"[完成] 已更新到 {remote_ver}（原 {local_ver}）")
    else:
        rollback()
        print("[完成] 校验未通过，已回滚到原版本")


if __name__ == "__main__":
    main()
