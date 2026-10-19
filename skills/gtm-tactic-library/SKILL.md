---
name: gtm-tactic-library
description: A searchable knowledge base and two scripts for go-to-market tactics extracted from nine Origin Notes teardowns (Replit, Supabase, SaaStr, Gamma, Instinct, Lenny Rachitsky, Rogo, Hugging Face, and the fear narrative analysis). Holds 45 tactic cards in the tactic, number, precondition, don't-copy-if, who-else format with evidence labels, a 59-condition vocabulary, a search script (filter by company, engine, condition or text) and a fit script that ranks tactics as GO, CONDITIONAL, NOT YET or BLOCKED from yes and no answers about your company. Use whenever the user asks which GTM tactic fits their startup, wants examples of how companies grew, needs to screen tactics against preconditions, wants to compare engines such as bottom-up, product loop, trust, content, agent distribution or open platform, or asks to look up or add tactic cards. Cards are paraphrased from public articles and mostly company-reported, so treat numbers as dated illustrations.
---

# GTM Tactic Library (knowledge base and tools)

Personal, paraphrased library built from public Origin Notes teardowns (2026). The articles' own paid Tactic Library is a separate product and is not reproduced here; these cards come only from the nine free posts read in this session. Numbers are mostly company-reported or outside estimates and dated; use them for calibration, never as promises.

Files: `data/tactics.json` (cards plus condition vocabulary), `references/tactic-cards.md` (readable view), `references/engines.md` (engine families and how to choose), `scripts/search_tactics.py`, `scripts/tactic_fit.py` (Python 3, standard library only).

Related skills: `gtm-teardown-method` (how to add new cards), `ai-startup-gtm-tactics`, `bottom-up-to-enterprise-gtm`, `trust-led-regulated-market-gtm`, `product-output-viral-loop-gtm`, `agent-ready-product-distribution`, `content-engine-audience-business`, `ai-agent-sales-team-playbook`, `invite-only-launch-and-seeding`, `open-platform-network-effect-gtm`.

## Workflow
1. **Collect facts about the user's company**: product, buyer, price, how people first get value, founder willingness, archive/audience, security posture, cash runway, unit economics.
2. **Translate into conditions** using `python3 scripts/search_tactics.py --list-conditions`. Mark each TRUE (yes), FALSE (no) or leave unknown. Counter-signs (blockers) go in yes when they are true (for example needs_technical_person).
3. **Run the fit script**, from the skill folder:
   `python3 scripts/tactic_fit.py --yes demo_obvious_in_seconds,value_in_one_day --no security_credible`
   Add `--format json` for machine output, `--min-status "NOT YET"` to hide blocked, or `--file answers.json` with {"yes":[],"no":[]}.
4. **Read the top cards** with `python3 scripts/search_tactics.py --text "<keyword>"` or `--engine <name>`; open the matching skill for the playbook.
5. **Resolve unknowns**: each CONDITIONAL card lists what to confirm; collect evidence before committing.
6. **Pick one engine and two supporting tactics**; list what you will not do and why.
7. **Extend the library**: when new teardowns are analysed, add a card to `data/tactics.json` (same fields), regenerate the readable view, and keep the evidence label honest.

## Output template
Company facts and conditions (yes/no/unknown) | ranked tactics with status and reasons | chosen engine and supports | evidence to collect for unknowns | risks and "not now" list | sources (card ids).

## Guardrails
- Screening, not prediction: the preconditions come from one article per company; survivorship bias is likely (Gamma's author warns failed startups may have followed the same playbook).
- Do not recommend the fear/narrative card as a tactic; it is included for recognition and critical reading, and the script skips it unless --include-narrative is passed.
- Respect disclosure and consumer law in endorsement, seeding and testimonial tactics.
