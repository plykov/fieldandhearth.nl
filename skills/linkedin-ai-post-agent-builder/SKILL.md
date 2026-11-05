---
name: linkedin-ai-post-agent-builder
description: Builds a personal AI assistant for writing LinkedIn posts that attract clients, following the method of a 2025 project that trained an agent on 850 top-decile posts. Covers a 40-variable post-analysis schema (hook type, story framework, CTA type and position, style markers, performance signals), assembling a swipe dataset, enriching it, deriving a brief that fuses the user's voice, positioning and offer, a generate-critique-revise loop, and a scoring script that checks a draft for hook mechanics, preview length, links, readability and CTA. Includes guardrails against copying creators and fabricating proof. Use whenever the user wants a system prompt, custom GPT, Claude project or workflow that drafts LinkedIn posts in their voice, wants to analyze posts they admire, or wants to automatically score drafts. For hand-writing a single post use linkedin-post-templates.
---

# LinkedIn AI post agent builder

An agent is only as good as the brief and the examples behind it. This skill produces three things: a post-analysis schema and swipe file, an agent brief (system prompt) tuned to the user's voice and offer, and a draft scorer.

## Workflow

1. **Define the job.** One sentence: "Draft [n] posts a week that attract [buyer] to [offer], in [name]'s voice." Get the offer, buyer, pillars (see `linkedin-client-attraction-content-system`), tone words, banned phrases, and what the user will never claim.
2. **Collect the swipe file.** Ask for 30 to 100 posts the user admires from creators who serve a similar buyer, plus 10 to 30 of the user's own best posts. Keep source URL and creator for attribution. Use public posts the user can legitimately access; do not scrape against platform terms.
3. **Tag each post** with the schema in `references/post-schema.md`. Do it by hand for a small set or with a model, then spot-check 10%. The schema covers hook type and ingredients, story framework, CTA type and position, style markers and performance signals.
4. **Find patterns.** Tabulate which hook types, frameworks and CTAs show up in the best performers of the user's own niche. Where the user's data is thin, use the findings from `linkedin-hook-and-rehook-writer` and `linkedin-post-templates` as priors, and mark them as priors.
5. **Write the agent brief** from `references/agent-brief-template.md`: role, voice rules, pillars, post-type menu, hook rules, CTA ladder, proof inventory, hard limits.
6. **Run the loop** for every post: draft three hooks, pick one, write the body, critique against the checklist, score with `scripts/score_post.py`, revise, then hand to the human.
7. **Review by a human before publishing.** The agent drafts, the person approves, and any figure, client, quote or claim must be confirmed.
8. **Close the learning loop.** Log each published post's results in the same schema and refresh the patterns monthly.

## Scoring a draft
```
python3 scripts/score_post.py draft.txt
python3 scripts/score_post.py draft.txt --format json
```
It reports preview length (first three non-empty lines), hook ingredients (number, quote, question, first-person or second-person start), a 0-3 mechanics score, paragraph length, link in the body, CTA presence, a jargon flag and a plain-language summary. It is a lint, not a judge: a good post can score low and a hollow one can score high. Use it to catch fixable issues, then apply judgment.

## Guardrails
- Never copy another creator's text. Use their structure, never their sentences or stories. Swipe files are for pattern analysis.
- The agent may not invent results, clients, quotes, anecdotes or credentials. Missing proof is a question for the user, not a gap for the model to fill.
- Mimicking a voice means the user's voice. Do not imitate a named creator to pass as them.
- Keep a human in the loop. Posts that read as generic machine output erode the trust this channel depends on; ask the user for a real detail before drafting.
- Follow platform rules on automation: draft with the agent, post as yourself, avoid automated mass commenting or fake engagement.
- Source limits: the 850-post cohort is curated and lacks ordinary-post baselines; see `references/evidence-notes.md`.

Read `references/post-schema.md` for the schema and tagging rules, `references/agent-brief-template.md` for the system prompt, and `assets/post-log-template.csv` for the log header.
