# Agent-first checklist and tactics (paraphrased)

## Why Lovable chose the product (six reasons, from the customer's own list)
Open source (no lock-in); built on a standard database; works with major sign-in providers; generous free tier; more than a database (live updates, storage, background tasks); friendly interface for non-technical users. Early developers gave similar reasons in 2020.

## Tactics, numbers and don't-copy-if
- **API / embedded default layer** (API shipped Aug 2022; platform offering 2025): an API handled ~90% of one partner's interactions; platform customers +370% in six months. Needs a complete product and automated setup. Don't copy if a person must configure each customer.
- **Build for AI agents**: CLI and MCP server as first-class; open Agent Skills; public docs on GitHub. Agent skills raised one coding agent's success from 46% to 71% (author: early, small sample). Don't copy if a person must buy or set up.
- **Open-source substrate**: everything open except platform and billing code; 100K+ GitHub stars; fund maintainers. Don't copy if hosted is not clearly easier.
- **Freemium + usage-based**: ~2% paying of registered accounts (author's arithmetic). Needs usage that grows with success and funding for free users.
- **Launch as a campaign**: one launch a day for a week every few months since 2021; each feature post written by the engineer who built it; ~20% bumps. Don't copy if you must pad the week.
- **Bottom-up to enterprise as support**: usage thresholds trigger offers of help; team paid on lift vs control; customers who talked to success grew usage 125% a quarter vs 25% without.

## Agent-readiness checklist
Programmatic signup and project creation | stable, documented API with idempotent calls | CLI and MCP server | agent skill files and examples | docs and error messages readable by models, kept public | sensible defaults (an agent can choose them safely) | sandbox/test vs production separation | usage quotas, abuse detection | pricing that works when no human watches the meter | telemetry to see which agents/tools create accounts.

## Risks (author)
How many AI-created free databases ever pay; dependence on a few choosers (app builders, coding agents); the chooser building its own backend or changing defaults; luck (the platform's core database standard rose in popularity). Question to keep asking: would an agent pick us over plain defaults, and why?
