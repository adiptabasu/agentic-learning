# Learning workflow evaluation scenarios

Use these as manual end-to-end behavior checks when revising the Learning Counselor, Teacher, journal, assessment, or question-bank workflows. Skill-specific routing and behavior cases are indexed in the [evaluation case catalog](README.md). These scenarios are not claims that an AI passed an evaluation. Assess observable behavior against the criteria below.

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

## Scenario 10: Topic question bank across lessons

Prompt: “Add two reusable questions from today's arrays lesson to my agreed topic bank, then quiz me on one. Do not record my attempts.”

Look for:
- Uses the agreed central index and active topic bank only; does not read other topic banks by default.
- Grounds each question and answer key or rubric in covered material, with source references and uncertainty marked.
- Keeps prompts, keys, explanations, and sources in the bank; does not save the learner's attempt without permission.
- Uses the Question Bank skill to ask one question and withholds its answer until the learner responds.
- Gives evidence-based feedback without treating one answer as proof of mastery.

## Scenario 11: Close Counselor mode with a Teacher handoff

Prompt: “I have explained my goal, current experience, constraints, and success criteria. I do not want a detailed route yet. I am done for now; prepare a Learning Brief for the Teacher and close Counselor mode.”

Look for:
- Creates a brief from confirmed conversation details and leaves missing values explicitly unknown.
- Marks the plan as not requested instead of inventing a route.
- Shows the brief for correction/confirmation before calling it a settled handoff.
- Offers to save only at an agreed path and Git policy; still provides the reviewed brief in the conversation.
- States that Counselor mode is closed only after consolidating the brief.

## Scenario 12: Teacher recommends, but does not impose, an assessment

Prompt: “I keep mixing up the prerequisite ideas while studying this unit. Should I take a test now?”

Look for:
- Connects a recommendation to the observed confusion and explains what a short diagnostic would clarify.
- Lets the learner choose before starting the assessment.
- Uses a low-stakes check limited to relevant prerequisites or covered material.
- Reports specific evidence and limits; does not infer broad mastery or save results without opt-in.

## Scenario 13: Separate Markdown study notes, handwritten PNG, and interviews

Prompts: “Create detailed notes for my Git repo.” Then: “Make a colorful page I can copy by hand.” Then: “Run a mock interview and save useful questions in my agreed bank.”

Look for:
- Routes detailed, source-grounded repository notes to `study-notes` as Markdown.
- Routes the copy-by-hand request to `handwritten-visual-notes` as a colorful PNG and does not save it to Git unless separately requested.
- Routes the role simulation to `interview`, keeps subject quizzes in `assessment`, and uses `question-bank` for reusable questions/rubrics only after the bank path and policy are agreed.
- Keeps interview answers, scores, and other learner attempt history separate from reusable questions and opt-in.
