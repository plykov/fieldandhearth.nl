---
name: agent-ready-product-distribution
description: Makes a product discoverable and selectable by other software and AI agents, using the Supabase teardown from Origin Notes. Covers the API or embedded default layer so partners can create accounts with nobody clicking, treating the AI agent as a user (command line, MCP server, published agent skills, public docs and troubleshooting guides), choosing an open standard, open-source substrate with a clearly easier hosted version, launch weeks, free tiers funded until growth, usage-signal sales that looks like support, and the agent-selection test of whether software can find, set up and get value from your product without a person. Also covers dependence on a few choosers and independent evidence about how agents pick tools. Use whenever a founder asks how to get AI coding agents or app builders to pick their product, plans an API for platforms, writes agent-facing docs or MCP servers, designs a free tier for AI-created usage, or asks how Supabase grew.
---

# Agent-Ready Product Distribution (Supabase pattern)

Based on the Origin Notes Supabase teardown (2026), paraphrased. Company-reported: 13M+ registered developers (Oct 2026), 70% of new databases created by agents or AI tools, 250K+ paying customers (June 2026), $650M raised in 2026; revenue undisclosed (outside estimate ~$170M ARR). An independent test found a coding agent picked plain Postgres 58% of the time and Supabase 24%, mostly as an all-in-one bundle. Illustrative only.

Companions: `gtm-tactic-library`, `bottom-up-to-enterprise-gtm`, `open-platform-network-effect-gtm`, `ai-startup-gtm-tactics`, `mcp-builder`.

## Workflow
1. **Run the agent-selection test**: can another piece of software find your product, set it up and get value with no person involved? List every human step (sales call, manual config, approval, CAPTCHA).
2. **Automate setup via API**: programmatic account/project creation, billing hooks, org management; package as a platform offering for partners.
3. **Make the agent a first-class user** (`references/agent-first-checklist.md`): CLI, MCP server, open agent skills/instructions, public docs and troubleshooting where models can read them, deterministic errors.
4. **Standardise**: build on an open standard that models already know; avoid proprietary lock-in as the headline.
5. **Open the substrate** when your hosted version is clearly easier than self-hosting; hire and fund the maintainers of what you depend on.
6. **Price for AI-created usage**: generous free tier, cost controls and abuse detection (a partner creating many databases can look like an attack), conversion triggered by growth.
7. **Package launches**: recurring launch weeks from real shipped work.
8. **Sales as support**: usage-signal triggers (storage or compute limits) send automated help; compensate on lift versus a control group; decline contracts that require custom features.
9. **Measure and de-risk**: agent-originated share, success rate of agent tasks, share of volume from top choosers; plan for a chooser changing defaults.

## Output template
Agent-selection audit | API/platform plan | agent-first checklist status | standards and openness position | pricing and abuse controls | launch and sales-signal design | dependence risks and mitigations | metrics.

## Guardrails
- Don't manipulate agents or models (hidden prompt injections, deceptive docs); be accurate so agents finish tasks safely.
- Give agents least-privilege access and clear confirmation boundaries; incidents involving agents deleting data are a real risk.
- Self-reported developer counts are registered accounts, not active users; state that when reporting.
