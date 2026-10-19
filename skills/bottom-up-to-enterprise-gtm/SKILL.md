---
name: bottom-up-to-enterprise-gtm
description: Plans and stress-tests a bottom-up (product-led) route into enterprise sales, using the Replit go-to-market teardown from Origin Notes (2026). Covers the engine where one non-technical employee builds a tool, the team adopts it, someone asks for an enterprise plan, and IT and security sign; preconditions (a product one person can buy and get value from in a day, an enterprise layer worth paying for, answers for security teams, guardrails for users who cannot read code); the stages after the first wave (inbound outruns four reps, land in one team and expand, product advocates for every customer, small account books, self-serve contracts up to a ceiling with sales above it); and the signals for when to hire sales. Use whenever a founder or revenue leader asks how to turn individual users into enterprise contracts, when to add sales to a PLG product, how to price and package an enterprise tier, how to handle security reviews for AI products, or whether to copy Replit.
---

# Bottom-Up to Enterprise (the Replit pattern)

Based on the Origin Notes teardown "Replit GTM playbook" (2026). All figures in the article come from Replit, its executives or outside estimates and are dated; treat them as illustrations, not benchmarks. This skill paraphrases a public article for planning use.

Companion skills: `ai-startup-gtm-tactics` (the other four tactics), `gtm-teardown-method` (how to analyse any company the same way), `transactional-sales-call-process` and `meddicc-deal-qualification` (when sales gets involved), `position-b2b-tech`.

## The engine in four steps
1. One person builds a tool their team needs without waiting for engineering (here: a product manager, marketer or analyst, not a developer).
2. The team uses it and colleagues build their own.
3. Someone at the company raises a hand and asks for an enterprise plan.
4. IT and security review and the company signs; the buying power sits with the people who already depend on it.
Why it scales: every company has far more non-developers than developers, so the pool of individual adopters is larger than in classic developer-led PLG.

## Workflow
1. **Describe the user and the first value moment**: who, what they build or achieve in the first day, price they can expense without approval.
2. **Run the preconditions check** in `references/preconditions-and-risks.md` (single-user value in a day; enterprise layer; security answers; guardrails; a technical person not required).
3. **Map the path from individual to contract**: signals that a team has adopted (seat spread, shared assets, domain clustering), who raises the hand, who reviews, what blocks (security, procurement).
4. **Design the enterprise layer**: controls IT needs (SSO, permissions, audit, data handling, environment separation), pricing model, packaging, self-serve ceiling.
5. **Decide the sales motion** with `references/after-the-first-wave.md`: when to add reps, advocates, field engineers, account book sizes, and which deals stay self-serve.
6. **Name the risks**: platform dependence, margin per usage, churn not yet proven, competitors that are your suppliers.

## When bottom-up is the wrong engine
If buyers are conservative, error-intolerant and organised as a prestige hierarchy, use the trust engine (`trust-led-regulated-market-gtm`). If the product can be chosen by software, see `agent-ready-product-distribution`. Support-style expansion tactics from other teardowns are in `references/signals-as-support.md`.

## Output template
User and first-day value | preconditions pass/fail with evidence | bottom-up path and signals | enterprise tier design | sales motion and hiring triggers | metrics to track (activation, team spread, inbound enterprise requests, net retention, gross margin, time to security approval) | risks and mitigations | "don't copy if" verdict.

## Guardrails
- Do not present Replit's numbers as targets or promise similar growth; disclosed figures are partial and some are company claims or estimates.
- Take security seriously for users who cannot inspect what the product does; the article's cautionary example is an agent deleting a production database, after which automatic test/live separation was introduced. Recommend guardrails and honest incident handling.
- Do not recommend circumventing a customer's IT or procurement policies; shadow adoption works only if you then meet security and compliance expectations.
