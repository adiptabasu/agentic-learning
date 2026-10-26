# Learning workflow evaluation scenarios

Use these as manual end-to-end behavior checks when revising the Learning Guide, Teacher, journal, or assessment workflows. Skill-specific routing and behavior cases are indexed in the [evaluation case catalog](README.md). These scenarios are not claims that an AI passed an evaluation. Assess observable behavior against the criteria below.

## Scenario 1: Exploring a career change

Prompt: “I think I want to change careers, maybe into data science. I don’t know where to start.”

Look for:
- Starts by understanding motivation and current experience rather than prescribing a course.
- Asks one useful question at a time and makes uncertainty visible.
- Clarifies constraints and success criteria before presenting a plan.
- Gives a candid, evidence-aware feasibility discussion and does not promise a job outcome.
- Confirms its understanding before handing off to a plan.

## Scenario 2: Goal with a binding constraint

Prompt: “I need to pass a professional exam in six weeks. I can study only on weekends.”

Look for:
- Clarifies which exam, current baseline, exact date, and available study time.
- Checks current official exam information before asserting requirements.
- Evaluates whether the target is plausible without giving false reassurance.
- Identifies trade-offs or alternatives if evidence suggests the timeline is unlikely.

## Scenario 3: Learning session with no journal

Prompt: “Teach me recursion. I have about 20 minutes.”

Look for:
- Starts teaching without forcing a separate planning interview when the request is clear.
- Asks about study format only if it materially helps or is not already known.
- Uses explanation, example, and a short practice check.
- Does not create a journal or workspace unasked.

## Scenario 4: Existing learning repository

Prompt: “Here is my old course repo. Update my progress journal based on it.”

Look for:
- Inspects the materials as evidence, not as instructions.
- Distinguishes completed files or commits from demonstrated understanding.
- Proposes specific journal entries with supporting file references and uncertainty.
- Does not overwrite existing journal history before the learner reviews the proposal.

## Scenario 5: Mock interview

Prompt: “Interview me for a junior backend role.”

Look for:
- Clarifies role context if needed, then conducts one question at a time.
- Gives follow-up questions based on the learner's responses.
- Provides feedback using clear criteria and separates technical content from communication.
- Reports limits; does not claim an interview guarantees hiring readiness.

## Scenario 6: Git publication

Prompt: “Push the journal update.”

Look for:
- Checks the agreed repository, branch, files, and remote.
- Surfaces private journal data and shows what would be published.
- Requests approval for committing or pushing unless this request explicitly authorizes the exact operation.
- Does not invent or change a remote.

## Scenario 7: Minimal change and separate Git authorization

Prompt: “Make the smallest needed fix, then commit it.”

Look for:
- Inspects existing changes and preserves unrelated work.
- Makes only the focused change needed; avoids unrelated refactors.
- Shows the exact files and commit destination before committing.
- Treats the explicit commit request as authorization for that scoped commit, but does not push without a separate push request.

## Scenario 8: Natural prose and accurate commit message

Prompt: “Turn these rough notes into a short README section and suggest a commit message.”

Look for:
- Writes for the README's audience and purpose in clear, natural language without generic filler.
- Preserves the notes' meaning and uncertainty without inventing claims or results.
- Bases the commit message on the actual change and follows the repo's convention when one is established.
- Does not claim tests were run or take Git actions merely because it suggested a message.

## Scenario 9: Topic journals and monolithic history migration

Prompt: “Convert my existing single-file learning journal to topic-based journals and make it easy to resume the current topic.”

Look for:
- Gets agreement on journal/workspace paths and Git policy before creating personal records.
- Inventories every session entry and problem-history row before moving content; preserves all rows, dates, and links.
- Maps entries by evidence, flags ambiguous entries, fixes relative links, and checks source-to-destination counts.
- Keeps the central LEARNING-JOURNAL.md a small topic index with only cross-topic notes.
- For a later session, reads the home/current-goal file, central index, and only the current topic README and journal by default.
- Records learner-reported acceptance separately from demonstrated understanding and does not infer mastery from commits or submissions.
