#!/usr/bin/env python3
"""Real-model behavioral regression. Never converts an unavailable run to PASS."""
import argparse, json, os, sys, urllib.request, urllib.error
from pathlib import Path

def post(url, key, payload):
    req = urllib.request.Request(url, data=json.dumps(payload).encode(), headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as response: return json.loads(response.read().decode())

def call_model(model_spec, key, messages, base_url):
    provider, sep, model = model_spec.partition(":")
    if provider != "openai" or not sep or not model: raise ValueError("supported model format: openai:<model>")
    data = post(base_url.rstrip("/") + "/chat/completions", key, {"model": model, "messages": messages, "temperature": 0})
    return data["choices"][0]["message"]["content"]

def parse_json(text):
    text = text.strip()
    if text.startswith("```"): text = text.split("\n", 1)[1].rsplit("```", 1)[0]
    return json.loads(text)

def main():
    p = argparse.ArgumentParser(); p.add_argument("--root"); p.add_argument("--cases"); p.add_argument("--limit", type=int)
    a = p.parse_args(); root = Path(a.root).resolve() if a.root else Path(__file__).resolve().parent.parent
    cases_path = Path(a.cases) if a.cases else root / "tests" / "behavioral" / "cases.json"
    model, key = os.getenv("MASTER_COPYWRITING_MODEL"), os.getenv("BEHAVIORAL_API_KEY")
    print(f"Behavioral Regression on: {root}")
    if not model or not key:
        print("BEHAVIORAL REGRESSION = NOT RUN")
        print("Set MASTER_COPYWRITING_MODEL=openai:<model> and BEHAVIORAL_API_KEY.")
        return 0
    cases = json.loads(cases_path.read_text(encoding="utf-8")); cases = cases[:a.limit] if a.limit else cases
    skill = (root / "SKILL.md").read_text(encoding="utf-8")
    base = os.getenv("BEHAVIORAL_BASE_URL", "https://api.openai.com/v1")
    results = []
    for case in cases:
        try:
            output = call_model(model, key, [{"role":"system","content":skill},{"role":"user","content":case["prompt"]}], base)
            judge_prompt = {"case": case, "candidate": output, "rubric": {"dimensions":["fact_integrity","purpose_completion","platform_fit","naturalness","commercial_usefulness"],"score":"0/1/2 each","hard_override":"unsupported fact, fake experience, identity fabrication, or unauthorized CTA means pass=false"}}
            judged = parse_json(call_model(model, key, [{"role":"system","content":"Judge strictly. Return JSON only: {pass:boolean,scores:object,hard_failures:array,reasons:array}."},{"role":"user","content":json.dumps(judge_prompt,ensure_ascii=False)}], base))
            results.append({"id":case["id"], **judged})
        except Exception as exc: results.append({"id":case["id"],"pass":False,"error":str(exc)})
    failed = [x for x in results if not x.get("pass")]
    print(json.dumps(results, ensure_ascii=False, indent=2))
    print(f"BEHAVIORAL REGRESSION = {'PASS' if not failed else 'FAIL'} ({len(results)-len(failed)}/{len(results)})")
    return 1 if failed else 0

if __name__ == "__main__": sys.exit(main())
