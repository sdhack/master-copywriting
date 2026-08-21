#!/usr/bin/env python3
import argparse, json
from pathlib import Path

PLATFORMS = {"douyin", "xiaohongshu", "official_account", "channels", "generic"}
PURPOSES = {"content", "seed", "sell"}

def compile_bundle(route):
    platform = route.get("platform", "generic")
    purpose = route.get("purpose", "content")
    if platform not in PLATFORMS or purpose not in PURPOSES:
        raise ValueError("unsupported platform or purpose")
    refs = [
        "references/execution/execution-reliability.md",
        "references/execution/audit-severity.md",
        "references/quality/humanization-engine.md",
        "references/quality/final-output.md",
        "references/craft/cta.md",
        "references/modes/platforms.md",
    ]
    if purpose in {"seed", "sell"}: refs += ["references/execution/purpose-integrity.md", "references/execution/claim-authority.md"]
    if route.get("task_type") == "cross_platform": refs.append("references/cross-platform/cross-platform-reconception.md")
    if route.get("ip_mode") == "ip": refs.append("references/quality/voice-profile.md")
    if route.get("product_fact_sufficiency") == "insufficient": refs.append("references/execution/product-acquisition.md")
    refs = list(dict.fromkeys(refs))
    pipeline = route.get("humanization_pipeline") or ("DOUBLE_AUDIT" if route.get("paid_commercial") else "CHINESE_NATIVE")
    return {"route": route, "references": refs, "gates": [f"G{i}" for i in range(1, 13)], "humanization": ["Draft", "H1", "G1-G12 repair", "H2", "read-only invariant check"], "pipeline": pipeline, "output": "user-facing copy only", "exclusions": ["internal route", "scores", "audit trace", "unsupported facts"]}

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--route", required=True)
    p.add_argument("--format", choices=["json", "markdown"], default="json")
    a = p.parse_args()
    route = json.loads(Path(a.route).read_text(encoding="utf-8"))
    bundle = compile_bundle(route)
    if a.format == "json": print(json.dumps(bundle, ensure_ascii=False, indent=2))
    else:
        print("# Route Bundle\n")
        print("## References")
        for ref in bundle["references"]: print(f"- `{ref}`")
        print("\n## Pipeline\n" + " -> ".join(bundle["humanization"]))

if __name__ == "__main__": main()
