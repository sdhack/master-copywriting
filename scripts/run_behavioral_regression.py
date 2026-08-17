#!/usr/bin/env python3
"""
Behavioral Regression Runner for Master Copywriting Skill

PATCH 28/38/39: Behavioral regression tests require an ACTUAL model run.
This script does NOT fake a PASS. If no model endpoint is configured, it
reports Behavioral Regression = NOT RUN.

Usage:
  python scripts/run_behavioral_regression.py --root <skill_root>
  python scripts/run_behavioral_regression.py --prompt "写一条抖音卖货，某款乌龙茶" --agent claude-like

Configuration (optional, enables a real run):
  env MASTER_COPYWRITING_MODEL   e.g. "openai:gpt-4o" / "anthropic:claude-sonnet-4" / "gemini:gemini-2.0-flash"
  env BEHAVIORAL_API_KEY         API key for the configured provider
"""

import argparse
import json
import os
import sys


# Fixed prompt set for cross-agent behavioral testing (PATCH 38)
BEHAVIORAL_CASES = [
    {
        "id": "CTA-01",
        "agent": "claude-like",
        "prompt": "写一条抖音卖货口播，某款乌龙茶。",
        "expect": {
            "platform": "douyin",
            "purpose": "sell",
            "cta_permission": "IMPLICIT_ONLY",
        },
        "forbidden": ["小黄车", "链接在下面", "去拍", "下单", "想试的下面就是"],
    },
    {
        "id": "CTA-02",
        "agent": "openai-like",
        "prompt": "写一条小红书卖货笔记，某款乌龙茶。",
        "expect": {
            "platform": "xiaohongshu",
            "purpose": "sell",
            "cta_permission": "IMPLICIT_ONLY",
        },
        "forbidden": ["小黄车", "链接在下面", "去拍", "下单"],
    },
    {
        "id": "CTA-03",
        "agent": "gemini-like",
        "prompt": "写一条视频号 IP 卖货口播，某款乌龙茶。",
        "expect": {
            "platform": "channels",
            "purpose": "sell",
            "ip_mode": "ip",
            "cta_permission": "IMPLICIT_ONLY",
        },
        "forbidden": ["小黄车", "链接在下面", "去拍", "下单"],
    },
    {
        "id": "CTA-04",
        "agent": "copilot-like",
        "prompt": "写一条公众号卖货长文，某款乌龙茶。",
        "expect": {
            "platform": "official_account",
            "purpose": "sell",
            "cta_permission": "IMPLICIT_ONLY",
        },
        "forbidden": ["小黄车", "链接在下面", "去拍", "下单"],
    },
    {
        "id": "CTA-06",
        "agent": "generic",
        "prompt": "直播最后30秒，给我明确成交口令，某款乌龙茶。",
        "expect": {
            "platform": "generic",
            "purpose": "sell",
            "cta_permission": "EXPLICIT_ALLOWED",
        },
        "forbidden": [],
    },
    {
        "id": "ROUTE-01",
        "agent": "limited-agent",
        "prompt": "我是店主，写一条抖音卖货口播，某款乌龙茶。",
        "expect": {
            "commercial_relationship": "shop_owner",
            "cta_permission": "IMPLICIT_ONLY",
        },
        "forbidden": [],
    },
]


def check_model_available():
    return bool(os.environ.get("MASTER_COPYWRITING_MODEL"))


def run_real_behavioral(skill_root):
    """Run behavioral cases against a configured model. Placeholder for a real
    provider call — in this environment no model endpoint is configured."""
    # NOTE: This is the integration point for a real model call.
    # Without MASTER_COPYWRITING_MODEL, we must NOT fabricate results.
    return None


def main():
    parser = argparse.ArgumentParser(description="Behavioral regression runner (PATCH 38)")
    parser.add_argument("--root", type=str, default=None, help="Skill root directory")
    parser.add_argument("--prompt", type=str, default=None, help="Single prompt override")
    parser.add_argument("--agent", type=str, default="generic", help="Agent body label")
    args = parser.parse_args()

    if args.root:
        skill_root = os.path.abspath(args.root)
    else:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        skill_root = os.path.dirname(script_dir)

    print(f"Behavioral Regression on: {skill_root}")

    if not check_model_available():
        print("\n" + "=" * 60)
        print("BEHAVIORAL REGRESSION = NOT RUN")
        print("=" * 60)
        print("No model endpoint configured (env MASTER_COPYWRITING_MODEL missing).")
        print("PATCH 28/39: Behavioral Regression must NOT be reported as PASS")
        print("without an actual model run.")
        print("\nConfigured behavioral cases (would run with a model):")
        for case in BEHAVIORAL_CASES:
            print(f"  - {case['id']} [{case['agent']}]: {case['prompt'][:40]}...")
        return 0

    # Real model run path (requires provider integration)
    results = run_real_behavioral(skill_root)
    if results is None:
        print("\nModel configured but runner integration not implemented.")
        print("BEHAVIORAL REGRESSION = NOT RUN")
        return 0

    failures = [r for r in results if not r["pass"]]
    print(f"\nBehavioral cases: {len(results)} total, {len(failures)} failed")
    for r in results:
        status = "PASS" if r["pass"] else "FAIL"
        print(f"  {status}: {r['id']}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
