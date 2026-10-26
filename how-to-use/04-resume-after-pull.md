# Resume after cloning or pulling a learning repo

Use this when returning to a learning repository in a new chat, on another computer, or after pulling its latest changes. Continuity depends on the agreed learning records being available in this checkout.

## Recover the learning state

If the repo has an agreed learning home or current-goal file, begin there. If it links to a central LEARNING-JOURNAL.md, read that index, then only the active topic's README.md and LEARNING-JOURNAL.md. Do not load every topic journal by default. Read the linked confirmed plan and latest session note when needed to understand the next step.

Ask the agent:

> Use the teacher skill to resume my learning in this repository. Read the agreed learning home/current-goal file and confirmed plan, then the central LEARNING-JOURNAL.md index. For my current topic, read only its README.md and LEARNING-JOURNAL.md. Summarize my goal, current topic and milestone, relevant evidence, open questions, and next step. Ask whether I want to continue before teaching. Do not read other topic journals unless you explain why they are needed.

If shortcuts are unavailable:

> Read skills/teacher/SKILL.md and follow it. For continuity, read [path to my learning home/current-goal file], the linked confirmed plan, the central LEARNING-JOURNAL.md index, and only [current topic path]/README.md and [current topic path]/LEARNING-JOURNAL.md.

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
