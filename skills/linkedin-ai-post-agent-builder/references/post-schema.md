# Post analysis schema

Use one row per post. Fields marked (auto) can be computed with `scripts/score_post.py`; the rest are tagged by a person or model.

## Identity
post_id, creator, url, date, niche, creator_archetype (educator, contrarian, mentor, thought leader)

## Hook (first three lines)
- hook_text
- hook_type: curiosity gap, contrarian, story-open, data-driven, question or how-to, bold claim, quote or dialogue
- hook_has_number (auto), hook_has_quote (auto), hook_has_question (auto)
- hook_first_word: I, my, you, other (auto)
- hook_mechanics_score 0-3 (auto)
- preview_chars (auto)
- rehook_move: keep the gap, front-load result, orient then withhold, turn to reader, colon cliffhanger, none

## Body
- format: listicle, how-to, personal story or case study, contrarian opinion, mindset insight, lead magnet offer, other
- story_framework: AIDA, PAS, BAB, hero journey, teardown, challenge-results, none
- structure_labels: whether sections are labelled (BACKGROUND, RESULTS)
- paragraph_avg_sentences (auto), whitespace_density (auto: blank lines per 100 words)
- has_list (auto), emoji_count (auto), hashtag_count (auto), has_link (auto), media: none, image, carousel, video
- proof_type: result with number, client story, credential, mistake and lesson, none
- payoff_matches_hook: yes/no (human check)

## Narrative and tone
- pov: first person, second person, third person
- tone words (2 or 3), emotion: inspiration, frustration, curiosity, empathy, pride
- jargon_flag (auto)

## CTA
- cta_type: discussion prompt, comment-to-get, direct link, DM invite, soft follow, soft sell, none
- cta_position: early, middle, final
- cta_keyword (for comment-to-get)

## Performance
impressions, reactions, comments, reposts, engagement_rate, comment_ratio, leads_started, calls_booked

## Tagging rules
Tag what is on the page, not what you guess the author intended. Keep categories fixed so counts are comparable. Record uncertainty in a notes column. Do not store full text of other creators' posts beyond what you need for analysis; store the URL and your tags.
