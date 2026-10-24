# Resume after cloning or pulling a learning repo

Use this when you return to a learning repository in a new chat, on another computer, or after pulling its latest changes. Continuity works only if the agreed learning records were saved where this checkout can access them.

## Ask the agent to recover the learning state

If the repo has an agreed `LEARNING.md` or other index, start with:

> Use the `teacher` skill to resume my learning in this repository. First read [path to the agreed learning index, such as `LEARNING.md`] and the active goal, plan, journal, and latest session note it links to. Summarize the goal, current milestone, last evidence of what I understand, open questions, and next step. Ask me to confirm that I want to continue this goal before teaching.

If shortcuts are not available, say:

> Read `skills/teacher/SKILL.md` and follow it. For continuity, read [path to the agreed learning index] and the linked learning records before teaching.

Do not paste your whole journal into a prompt if the agent can read the agreed files locally. If it cannot access the repo files, provide only the relevant excerpts you are comfortable sharing.

## Confirm or correct the checkpoint

Check that the agent read the latest records, not an old copy. If something changed since the last session, correct it:

> The plan is still current, but [change in schedule / goal / background]. Please update your understanding and suggest how the next step should change before we continue.

If the expected learning index or records are missing, do not let the agent invent progress. Say:

> I don't see the learning checkpoint. Tell me which files you could read and what is missing. I can provide the correct records or help set up a continuity index.

## Continue and save the next checkpoint

Once you confirm the summary, tell the Teacher how much time you have and what you want from the session:

> That checkpoint is accurate. I have [time] today. Continue from [next step], using [preferred study style if relevant].

At the end, review the proposed progress update:

> Prepare a concise update to the agreed journal and learning index. Record what we covered, evidence I demonstrated, what remains uncertain, and the next step. Show me the proposed changes before saving them.

Only include files in Git according to the repo's agreed tracking policy. Keep private notes out of shared history unless you deliberately chose to track them and confirm that choice.

## If there is no saved learning state

You can still continue by telling the agent what you remember, or begin a fresh session with the [one-session lesson guide](03-one-off-learning-session.md). If you want durable continuity, ask `workspace-intake` to agree on an index path, linked records, and a privacy/Git policy; the reusable starting point is [the learning-home template](../templates/learning-home-template.md).
