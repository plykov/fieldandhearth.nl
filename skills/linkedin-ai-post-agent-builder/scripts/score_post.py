#!/usr/bin/env python3
"""Lint a LinkedIn draft: hook mechanics, preview length, readability, links, CTA.

Usage: score_post.py draft.txt [--format text|json]
A heuristic aid, not a quality judge.
"""
import argparse, json, re, sys

JARGON = ["synergy", "leverage", "utilize", "paradigm", "circle back", "best-in-class",
          "game-changer", "thought leader", "move the needle", "low-hanging fruit",
          "in today's fast-paced", "excited to announce", "delighted to share"]
CTA_PATTERNS = [r"\bcomment\b", r"\bdm me\b", r"\bwhat('s| is| are) your\b", r"\bdo you\b",
                r"\bhave you\b", r"\blet me know\b", r"\bfollow\b", r"\bshare your\b", r"\?\s*$"]


def analyze(text):
    lines = [l.rstrip() for l in text.strip().splitlines()]
    nonempty = [l for l in lines if l.strip()]
    hook_lines = nonempty[:3]
    hook = "\n".join(hook_lines)
    preview = hook[:300]
    words = re.findall(r"\b[\w'’-]+\b", text)
    paras = [p for p in re.split(r"\n\s*\n", text.strip()) if p.strip()]
    sent_counts = [len(re.findall(r"[.!?]+(?:\s|$)", p)) or 1 for p in paras]
    first = re.findall(r"[A-Za-z']+", nonempty[0])[:1] if nonempty else []
    first_word = first[0].lower() if first else ""
    has_number = bool(re.search(r"\d", hook))
    has_quote = bool(re.search(r"[\"“”‘’']", hook)) and bool(re.search(r"[\"“”]", hook))
    has_question = "?" in hook or bool(re.search(r"\bhow to\b", hook, re.I))
    layers = {
        "specific_number": has_number,
        "open_loop": has_question or hook.rstrip().endswith(":") or bool(re.search(r"\b(why|secret|mistake|truth|here's|here is)\b", hook, re.I)),
        "human_or_dramatic": first_word in ("i", "my", "we") or has_quote,
    }
    jargon = [j for j in JARGON if j in text.lower()]
    tail = " ".join(nonempty[-3:])
    cta = any(re.search(p, tail, re.I) for p in CTA_PATTERNS)
    findings = []
    plen = len(hook.replace("\n", " "))
    if plen > 200:
        findings.append(f"First three lines run {plen} characters; the feed cuts near 200. Tighten toward ~130.")
    if sum(layers.values()) < 2:
        findings.append("Hook uses fewer than two ingredients (number, open loop, human element).")
    if re.search(r"https?://", text):
        findings.append("External link in the body; consider moving it to the first comment.")
    if sent_counts and max(sent_counts) > 3:
        findings.append("A paragraph has more than three sentences; split it.")
    if jargon:
        findings.append("Jargon or stock phrases: " + ", ".join(jargon))
    if not cta:
        findings.append("No clear closing question or call to action.")
    if len(text) < 600:
        findings.append("Under ~600 characters; fine for a punchy insight, thin for a how-to or story.")
    if len(text) > 3000:
        findings.append("Over the 3,000-character post limit.")
    return {
        "characters": len(text), "words": len(words), "paragraphs": len(paras),
        "avg_sentences_per_paragraph": round(sum(sent_counts) / max(len(sent_counts), 1), 1),
        "hook_preview_chars": plen, "first_word": first_word,
        "hook_layers": layers, "mechanics_score": sum(layers.values()),
        "has_link": bool(re.search(r"https?://", text)), "has_cta": cta,
        "hashtags": len(re.findall(r"#\w+", text)), "jargon": jargon,
        "findings": findings,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--format", choices=["text", "json"], default="text")
    a = ap.parse_args()
    text = open(a.file, encoding="utf-8").read() if a.file != "-" else sys.stdin.read()
    r = analyze(text)
    if a.format == "json":
        print(json.dumps(r, indent=2))
        return
    print(f"Mechanics score: {r['mechanics_score']}/3  layers: " + ", ".join(k for k, v in r['hook_layers'].items() if v))
    print(f"Hook preview: {r['hook_preview_chars']} chars | post: {r['characters']} chars, {r['paragraphs']} paragraphs "
          f"(avg {r['avg_sentences_per_paragraph']} sentences) | link: {r['has_link']} | CTA: {r['has_cta']} | hashtags: {r['hashtags']}")
    print("Findings:" if r["findings"] else "No findings.")
    for f in r["findings"]:
        print(" -", f)


if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError:
        pass
