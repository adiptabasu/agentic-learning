# Set up or update a progress journal

A journal is optional. Use this guide when you want a durable record of your goals, learning sessions, demonstrated understanding, difficult areas, and next steps.

## If you do not have a journal yet

Do not ask the agent to “make a journal” without deciding where it belongs. First agree on its location, contents, and whether it can be tracked in Git. Then say:

> Use `skills/progress-journal/SKILL.md` to help me set up a progress journal at [exact path]. Include [goal, plan, sessions, evidence, review queue, or other agreed items]. This journal will be [tracked in Git / kept private and ignored]. Show me the proposed file before saving it. Do not create other workspace files.

If you want a starting structure, ask it to use `templates/learner-journal-template.md` and fill in only information you have provided.

## After a learning session

Point to the agreed journal and ask for a reviewable update:

> Read [journal path] and propose an update based on today's session. Record the date and time zone, topic, what I completed, evidence I demonstrated, open questions or difficult areas, review needs, and next step. Separate my demonstrated understanding from activities completed. Show me the exact changes before saving.

Example: “I solved two recursion exercises with hints” is an activity; the explanation or solution is evidence. Do not record mastery just because a topic was covered.

Review the proposal. Correct or remove anything that is inaccurate, too personal, or more certain than the evidence supports. Then say:

> Apply the reviewed changes to [journal path] only.

If you want another agent to resume after a clone or pull, also update the agreed learning index with the active goal, current milestone, last evidence, open questions, and next step.

## Keep private information private

Before tracking or sharing journal files, check the repository's agreed Git policy. Do not add sensitive personal details, credentials, or private reflections by default. If the record should remain local, agree on an ignored path and verify that it is not already tracked before writing private information there. A journal update does not itself authorize staging, committing, or pushing.
