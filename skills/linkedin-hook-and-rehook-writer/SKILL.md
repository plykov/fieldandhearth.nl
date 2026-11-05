---
name: linkedin-hook-and-rehook-writer
description: Writes and fixes the first three lines of a LinkedIn post (the hook and rehook that decide whether anyone taps see more), using patterns from a 2025 analysis of viral LinkedIn posts. Covers the three hook families (curiosity, problem-solution, personal story), rehook moves that keep the click going, the roughly 200-character preview cutoff and why images shorten it, line-break tactics, hook length and clarity rules, and a scoring test for a draft opener, and hook-ingredient layering (number, quote, question, first person). Use whenever the user wants a stronger LinkedIn opener, asks for hook options, says their posts get impressions but few reads, wants to rewrite a weak first line, or is drafting any LinkedIn post and the opening is not yet sharp. For a full post structure use linkedin-post-templates. For timing and metrics use linkedin-posting-strategy-and-metrics.
---

# LinkedIn hook and rehook writer

The feed shows only the opening of a post. If those lines do not earn the "see more" tap, nothing below them is read, liked or answered. Treat lines 1 to 3 as one unit and write them first, last and again.

## Workflow

1. **Get the raw material.** Ask for the post's point (one sentence), the audience, and the proof or story behind it. If the user already has a draft, read it and find the most surprising or emotional moment. That is usually buried and belongs on line 1.
2. **Pick a hook family** from `references/hook-patterns.md` (curiosity, problem-solution, personal story). Match it to the post: a story post wants a story hook, a how-to wants a result-plus-twist hook, an opinion post wants a contrarian line.
3. **Write 5 hook options**, at least one in each family, each under about 15 words and understandable at a glance.
4. **Write the rehook** (lines 2 to 3) for the best two. Use one of the four moves below.
5. **Preview check.** Count the first ~200 characters (fewer if an image is attached). Make sure the cut falls at a suspense point, not mid-boring-sentence.
6. **Score** each opener with the test below and deliver the best one with one alternative and a one-line reason.

## Rehook moves
- **Keep the gap open.** Promise the answer without giving it: "I was shocked when I found out. Here is what happened:"
- **Front-load a result or bold claim.** "Leads rose 50% in a week." Readers stay to learn how.
- **Orient, then withhold.** A one-word hook ("I failed.") followed by just enough context to place the reader, not the outcome.
- **Turn it toward the reader.** After an "I" line, widen it: "Here is what this can teach you about X."
- **Colon cliffhanger.** End the visible part on "Here it is:" or similar so the tap feels like the natural next step.

## Opener score (aim for 4 of 5)
1. Does it create an information gap or emotion in the first line?
2. Is it specific (a number, role, moment) rather than abstract?
3. Is it under ~15 words and clear without context?
4. Does it speak to a defined reader ("you", a role, a situation)?
5. Do lines 2 to 3 raise the stakes instead of repeating line 1?

## Guardrails
- A hook must be honest about what follows. Withholding is fine, a bait-and-switch is not, because readers punish it with silence and the post is judged on what it delivers.
- Do not fabricate a story, number or "almost quit" moment to fit a pattern. Ask for the real one.
- Avoid corporate filler openers ("Excited to announce", "In today's fast-paced world").

The patterns come from one secondary analysis (see `references/evidence-notes.md`): treat them as strong heuristics to test on your own audience, not laws.

Layer tactics: strong hooks usually combine two or three ingredients (a specific number, an open loop, a human or dramatic element). `references/hook-mechanics.md` has the shares from a second analysis of 850 top posts and a 0-3 mechanics score. Target about 130 characters, with 200 as the ceiling. For a deterministic check, `linkedin-ai-post-agent-builder` has a scoring script.

Read `references/hook-patterns.md` for formulas, examples and annotated hook plus rehook pairs.
