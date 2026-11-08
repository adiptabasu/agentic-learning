# Resume after cloning or pulling a learning repo

Use this when returning to a learning repository in a new chat, on another computer, or after pulling its latest changes. Continuity depends on the agreed learning records being available in this checkout.

## Recover the learning state

If the repo has an agreed learning home or current-goal file, begin with its Learning Brief. Read the linked plan only if the brief leaves the next topic or route unclear. Use the central LEARNING-JOURNAL.md index only to locate the active topic when needed; read that topic's journal and its README only when the next step needs the extra context. Read the question bank only for a quiz or bank update. Do not load unrelated journals or repeat history already summarized in the brief.

Ask the agent:

> Use the teacher skill to resume my learning in this repository. Start with the agreed Learning Brief. Read the linked plan only if the next step is unclear; use the central journal index only if needed to locate my active topic. Read only the active topic journal and its README if needed for context. Summarize my current goal, milestone, relevant evidence, open questions, and next step in a few lines. Ask whether I want to continue before teaching. Do not read unrelated records or repeat details already in the brief.

If shortcuts are unavailable:

> Read skills/teacher/SKILL.md and follow it. Start from [path to my Learning Brief]. Read the plan, central index, active-topic journal, or README only where needed to identify my next step; do not load unrelated topics or repeat the brief.

If the current topic is unclear, clarify it before opening topic journals. Do not paste a whole journal into a prompt if the agent can read the agreed files locally. If it cannot access files, provide only relevant excerpts you are comfortable sharing.

## Confirm or correct the checkpoint

Check that the agent read the latest records, not an old copy. Correct anything that changed:

> The plan is still current, but [change]. Update your understanding and suggest how the next step should change before we continue.

If the home file, index, or a required topic record is missing:

> Tell me which files you could read and what is missing. Do not infer my progress. I can provide the correct records or help set up a continuity index.

## Continue and save the next checkpoint

Once the summary is accurate, say:

> That checkpoint is accurate. I have [time] today. Continue from [next step], using [preferred study style if relevant].

At the end, review a proposed update:

> Prepare a concise update to the agreed current topic journal and central index if cross-topic information changed. For each solved problem, record my proposed approach, guidance I needed, whether I report the solution was accepted, and what I want to derive or revisit independently. Keep my report separate from evidence of understanding. Show me the proposed changes before saving them.

Only include files in Git according to the agreed tracking policy. Keep private notes out of shared history unless you deliberately chose to track them and confirm that choice.

If no saved learning state exists, you can provide what you remember or begin a one-off lesson. Journals are optional; see the [progress journal guide](05-progress-journal.md) to agree on a structure.
