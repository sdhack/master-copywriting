#!/usr/bin/env python3
import argparse, json, re
from pathlib import Path

def tokens(obj):
    text = " ".join(str(obj.get(k, "")) for k in ("core_proposition", "angle_type", "creative_driver", "hook_type", "tone"))
    text += " " + " ".join(obj.get("tags", []))
    return set(re.findall(r"[\w\u4e00-\u9fff]+", text.lower()))

def similarity(a, b):
    x, y = tokens(a), tokens(b)
    return len(x & y) / len(x | y) if x or y else 0.0

def load_store(path):
    if not path.exists(): return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]

def main():
    p = argparse.ArgumentParser(); sub = p.add_subparsers(dest="cmd", required=True)
    for name in ("add", "check"):
        q = sub.add_parser(name); q.add_argument("--store", required=True); q.add_argument("--input", required=True); q.add_argument("--threshold", type=float, default=.72)
    q = sub.add_parser("list"); q.add_argument("--store", required=True)
    a = p.parse_args(); store = Path(a.store); rows = load_store(store)
    if a.cmd == "list": print(json.dumps(rows, ensure_ascii=False, indent=2)); return
    item = json.loads(Path(a.input).read_text(encoding="utf-8"))
    matches = sorted(({"content_id": r.get("content_id"), "similarity": round(similarity(item, r), 4)} for r in rows), key=lambda x: x["similarity"], reverse=True)
    if a.cmd == "check": print(json.dumps({"duplicate": bool(matches and matches[0]["similarity"] >= a.threshold), "matches": matches[:5]}, ensure_ascii=False, indent=2)); return
    if matches and matches[0]["similarity"] >= a.threshold: raise SystemExit(f"similarity threshold exceeded: {matches[0]}")
    store.parent.mkdir(parents=True, exist_ok=True)
    with store.open("a", encoding="utf-8") as f: f.write(json.dumps(item, ensure_ascii=False) + "\n")
    print(json.dumps({"added": item.get("content_id"), "nearest": matches[:1]}, ensure_ascii=False))

if __name__ == "__main__": main()
