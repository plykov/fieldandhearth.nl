#!/usr/bin/env python3
"""Score which GTM tactics fit a company, using the preconditions and counter-signs on each card.

Give answers as condition keys (see --list-conditions in search_tactics.py):
  --yes demo_obvious_in_seconds,value_in_one_day      conditions that are TRUE for you
  --no  founder_public_voice                           conditions that are FALSE for you
  (anything not mentioned is treated as unknown)
Counter-signs (blockers) are conditions too: put them in --yes if they are true for you,
e.g. --yes needs_technical_person.

Or pass a JSON file: {"yes": [...], "no": [...]}

Output: tactics ranked as GO (all preconditions met, no blockers), CONDITIONAL (some unknown),
NOT YET (a precondition is explicitly missing) or BLOCKED (a counter-sign applies).
"""
import argparse, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data", "tactics.json")

def classify(t, yes, no):
    req, blk = t["requires"], t["blockers"]
    blocked = [b for b in blk if b in yes]
    met = [r for r in req if r in yes]
    missing = [r for r in req if r in no]
    unknown = [r for r in req if r not in yes and r not in no]
    if blocked:
        status = "BLOCKED"
    elif missing:
        status = "NOT YET"
    elif unknown:
        status = "CONDITIONAL"
    else:
        status = "GO"
    score = len(met) / len(req) if req else 0.0
    return dict(status=status, score=round(score, 2), met=met, missing=missing, unknown=unknown, blocked=blocked)

ORDER = {"GO": 0, "CONDITIONAL": 1, "NOT YET": 2, "BLOCKED": 3}

def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--yes", default="")
    p.add_argument("--no", default="")
    p.add_argument("--file")
    p.add_argument("--min-status", choices=list(ORDER), default="BLOCKED", help="hide statuses worse than this")
    p.add_argument("--format", choices=["text", "json"], default="text")
    p.add_argument("--include-narrative", action="store_true", help="also score recognition-only narrative plays (not recommended)")
    a = p.parse_args()
    with open(DATA, encoding="utf-8") as f:
        d = json.load(f)
    yes = {x.strip() for x in a.yes.split(",") if x.strip()}
    no = {x.strip() for x in a.no.split(",") if x.strip()}
    if a.file:
        with open(a.file, encoding="utf-8") as f:
            j = json.load(f)
        yes |= set(j.get("yes", []))
        no |= set(j.get("no", []))
    bad = [k for k in yes | no if k not in d["vocab"]]
    if bad:
        print("Unknown condition keys: " + ", ".join(bad), file=sys.stderr)
        sys.exit(2)
    if yes & no:
        print("Conditions in both yes and no: " + ", ".join(sorted(yes & no)), file=sys.stderr)
        sys.exit(2)
    rows = []
    for t in d["tactics"]:
        if t["engine"] == "narrative" and not a.include_narrative:
            continue
        r = classify(t, yes, no)
        if ORDER[r["status"]] <= ORDER[a.min_status]:
            rows.append((t, r))
    rows.sort(key=lambda x: (ORDER[x[1]["status"]], -x[1]["score"], x[0]["company"]))
    if a.format == "json":
        json.dump([dict(id=t["id"], company=t["company"], tactic=t["tactic"], **r) for t, r in rows], sys.stdout, indent=1)
        print()
        return
    cur = None
    for t, r in rows:
        if r["status"] != cur:
            cur = r["status"]
            print(f"\n== {cur} ==")
        print(f"- {t['company']}: {t['tactic']}  [{t['id']}] fit {int(r['score']*100)}%")
        if r["blocked"]:
            print("    counter-sign applies: " + "; ".join(d["vocab"][b] for b in r["blocked"]))
        if r["missing"]:
            print("    missing: " + "; ".join(d["vocab"][m] for m in r["missing"]))
        if r["unknown"]:
            print("    to confirm: " + "; ".join(d["vocab"][u] for u in r["unknown"]))
    print()
    print("Note: fit is a screening aid built from one article's stated preconditions; verify with your own data.")

if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError:
        sys.exit(0)
