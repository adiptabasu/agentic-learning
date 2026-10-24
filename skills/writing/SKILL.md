---
name: writing
description: Draft or revise clear, natural-sounding content and accurate Git commit messages without generic AI filler.
---
# Writing

Use this skill when drafting or editing prose, including documentation, learning materials, emails, summaries, and Git commit messages. Match the requested audience, purpose, format, and voice. If a missing detail would materially change the result, ask; otherwise make a reasonable choice and keep moving.

## Make prose clear and natural

- Lead with the point the reader needs. Prefer concrete words, specific details, and active phrasing when they fit.
- Keep the tone appropriate to the audience and context. Preserve the user's voice when editing their draft; do not make every piece sound like the same polished corporate template.
- Use varied, readable sentence lengths and natural transitions. Do not add intentional errors, fake informality, or fabricated personal anecdotes to imitate a human.
- Remove generic openings and conclusions, repetitive summaries, empty intensifiers, inflated claims, canned transitions, and phrases that add no information. Avoid common AI filler such as “delve,” “it's important to note,” “in today's fast-paced world,” and “I hope this helps” unless the context genuinely calls for it.
- Preserve meaning, uncertainty, and factual limits. Do not invent experience, evidence, quotations, citations, results, or promises. Flag gaps instead of filling them with plausible-sounding details.
- Keep necessary nuance. Brevity is useful when it improves clarity, not when it removes information the reader needs.

## Write commit messages

When asked to prepare a commit message, inspect the staged diff, or the intended change if it is not staged, and use the repository's established convention when one is clear. Describe the actual change and its purpose; do not infer intent beyond the evidence.

- Keep the subject specific and concise. A conventional form such as `type(scope): imperative summary` is a useful default only when it fits the repo's style; do not force it.
- Add a body when it explains a meaningful reason, behavior change, or trade-off that the subject cannot convey. Omit boilerplate and restatements of the diff.
- Mention tests or verification only when they were actually run and their results are known. Do not invent issue numbers, breaking changes, or affected behavior.
- If the change has multiple unrelated parts, flag that the scope may deserve separation instead of disguising it with a vague subject.
- Writing or suggesting a message does not authorize staging, committing, or pushing. Follow the repo's Git policy and the learner's action-specific authorization.

## Review before delivery

Check that the draft answers its purpose, sounds suited to its audience, preserves the known facts, and contains no filler or unsupported claims. For edits, retain useful original wording and change only what improves the result. Present a clean version; explain significant editorial choices only when useful or requested.
