#!/usr/bin/env python3
import argparse, json
from datetime import datetime, timezone
from pathlib import Path

ALLOWED = {"route_id", "platform", "purpose", "references_loaded", "stage_durations_ms", "h1_edit_ratio", "h2_edit_ratio", "audit_counts", "repair_loops", "final_invariant_passed", "output_char_count"}

def main():
    p = argparse.ArgumentParser(); p.add_argument("command", choices=["log", "summary"]); p.add_argument("--store", required=True); p.add_argument("--input")
    a = p.parse_args(); path = Path(a.store)
    if a.command == "log":
        if not a.input: raise SystemExit("--input is required for log")
        raw = json.loads(Path(a.input).read_text(encoding="utf-8")); event = {k: raw[k] for k in ALLOWED if k in raw}; event["recorded_at"] = datetime.now(timezone.utc).isoformat()
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as f: f.write(json.dumps(event, ensure_ascii=False) + "\n")
        print(json.dumps({"logged": True, "fields": sorted(event)}, ensure_ascii=False)); return
    rows = [json.loads(x) for x in path.read_text(encoding="utf-8").splitlines() if x.strip()] if path.exists() else []
    print(json.dumps({"runs": len(rows), "invariant_passes": sum(bool(x.get("final_invariant_passed")) for x in rows), "repair_loops": sum(int(x.get("repair_loops", 0)) for x in rows)}, ensure_ascii=False, indent=2))

if __name__ == "__main__": main()
