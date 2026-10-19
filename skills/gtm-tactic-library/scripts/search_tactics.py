#!/usr/bin/env python3
"""Search the GTM tactic library.

Examples:
  python3 scripts/search_tactics.py --text pricing
  python3 scripts/search_tactics.py --engine bottom_up --company Replit
  python3 scripts/search_tactics.py --list-engines
  python3 scripts/search_tactics.py --text "waitlist" --format json
"""
import argparse, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data", "tactics.json")

def load():
    with open(DATA, encoding="utf-8") as f:
        return json.load(f)

def matches(t, a):
    if a.company and a.company.lower() not in t["company"].lower():
        return False
    if a.engine and a.engine.lower() != t["engine"].lower():
        return False
    if a.condition and a.condition not in t["requires"] + t["blockers"]:
        return False
    if a.text:
        blob = " ".join(str(v) for v in t.values()).lower()
        if not all(w in blob for w in a.text.lower().split()):
            return False
    return True

def show(t):
    print(f"[{t['id']}] {t['company']}: {t['tactic']}  (engine: {t['engine']}; evidence: {t['evidence']})")
    print(f"  number:       {t['number']}")
    print(f"  precondition: {t['precondition']}")
    print(f"  don't copy if:{' ' + t['dont_copy_if']}")
    print(f"  who else:     {t['who_else']}")
    if t.get("note"):
        print(f"  note:         {t['note']}")
    print(f"  source:       {t['source_article']}")
    print()

def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--text", help="words that must all appear anywhere in the card")
    p.add_argument("--company")
    p.add_argument("--engine")
    p.add_argument("--condition", help="condition key used in requires or blockers")
    p.add_argument("--format", choices=["text", "json"], default="text")
    p.add_argument("--list-engines", action="store_true")
    p.add_argument("--list-conditions", action="store_true")
    a = p.parse_args()
    d = load()
    if a.list_engines:
        engines = {}
        for t in d["tactics"]:
            engines.setdefault(t["engine"], []).append(t["company"])
        for e, cs in sorted(engines.items()):
            print(f"{e}: {len(cs)} cards ({', '.join(sorted(set(cs)))})")
        return
    if a.list_conditions:
        for k, v in d["vocab"].items():
            print(f"{k}: {v}")
        return
    hits = [t for t in d["tactics"] if matches(t, a)]
    if a.format == "json":
        json.dump(hits, sys.stdout, indent=1)
        print()
    else:
        for t in hits:
            show(t)
        print(f"{len(hits)} card(s)")

if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError:
        sys.exit(0)
