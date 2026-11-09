# Agentic Learning

A reusable AI-assisted learning system designed around one learner's needs while remaining adaptable to other people, subjects, study goals, career changes, and job changes.

## Generic starting point

This repository keeps its canonical personas, skills, and templates in host-independent folders. It does not include an agent-specific skills folder by default.

To try a fresh-repository setup:

1. Clone or open this repository in your chosen agent.
2. Ask the agent to read and follow skills/initialize/SKILL.md.
3. Tell it which agent host or application you are using. Give the model name separately only if relevant.
4. Review its findings and agree on any host-specific folder structure before it writes files.
5. Once initialized, use that host's skill picker or command syntax.

For a Codex cold-start trial, paste this into a new Codex chat opened at the repository root:

    Read skills/initialize/SKILL.md and follow it for this repository. I use Codex. Check the current skill layout and tell me what changes would make the canonical skills available in Codex. Do not make changes until you show me the proposed files and I agree. Do not initialize Git, commit, or push.

Because this repository starts without .agents/skills/, initialize is not initially available as a Codex shortcut. The explicit prompt above asks Codex to load the canonical skill file directly. After you approve Codex setup, the initializer can create the native .agents/skills/ copies.

## Learning flow

1. **Clarify the goal.** The Learning Counselor asks focused questions about what you want to learn and why, your current knowledge, constraints, and what success means. It does not assume missing details or force a goal when you are still exploring.
2. **Confirm the handoff.** When Counselor mode ends, it consolidates a Learning Brief with your confirmed goal, baseline, constraints, open questions, and proposed first step. A confirmed route can be included if you chose to plan. The Teacher uses this brief rather than relying on hidden chat history.
3. **Agree on a route.** The learning-plan workflow turns a clarified goal into an ordered route with prerequisites, milestones, practice, evidence of progress, and review points. Estimates are labeled and provided only when justified.
4. **Study with the Teacher.** The Teacher reviews your brief, checks your current knowledge and relevant prerequisites, fills gaps, and teaches with explanations, examples, and practice. It may recommend an assessment at a useful point and asks before starting one.
5. **Check progress or practice interviews.** Assessment checks subject knowledge and goal-related readiness. Interview runs a separate mock interview. A learner-configured topic question bank preserves substantive questions, answer keys, or rubrics from either workflow. Results are evidence about specific material, not a guarantee of mastery, passing, or hiring.
6. **Make notes and keep continuity if wanted.** Study Notes creates detailed Markdown. Handwritten Visual Notes creates a colorful PNG to view and copy into a notebook. A journal is optional. Agree on any save location and Git policy before creating learner records. Blank formats are in templates/.
7. **Close and resume.** Each mode is an explicit workflow in the current conversation: saying “turn on” starts it, and “turn off” closes it after consolidating its current brief, plan, lesson summary, assessment or interview feedback, notes, and any authorized question-bank updates. This is not a persistent application setting. A future chat resumes from saved records only when you have chosen their location and tracking policy.
8. **Adapt the route.** Revisit older material and adjust the plan when goals, constraints, or evidence change.

For copy-ready prompts and complete walkthroughs, start with the [How to use guides](how-to-use/README.md).

The Learning Counselor should be candid and respectful. It should not promise success. If a target seems infeasible, it should explain why, identify evidence and uncertainties, and explore alternatives. The Teacher treats slow progress as a prompt to investigate prerequisites, workload, practice, teaching fit, and outside constraints, not as a judgment of ability.

## Repository structure

- AGENTS.md — shared project guidance for agents that read this convention.
- HANDWRITTEN-VISUAL-NOTES-PALETTE.md — optional reusable color preferences for handwritten visual sheets.
- personas/ — portable Learning Counselor and Teacher behavior definitions.
- skills/ — canonical, tool-independent skill sources.
- templates/ — blank formats for the Counselor-to-Teacher Learning Brief, detailed Markdown notes, optional topic question banks, journal indexes, topic journals, session notes, and a repo-local learning continuity index.
- evals/ — manual workflow scenarios and skill-specific evaluation cases.
- scripts/sync_skills.py — copies canonical skill files into a selected host's native skill folder.
- No host-specific skills folder is included until a learner selects and initializes a host.

Personas describe the ongoing teaching and guidance approach. Skills define invocable workflows. Persona files are portable references; each host may use a different format or may not expose personas as commands.

## Canonical skills and host discovery

Keep one canonical copy of each skill under skills/<name>/SKILL.md. Agent hosts scan different project folders, so the initialize workflow checks current official guidance and prepares the selected host layout only after the learner agrees.

| Agent host | Project skill folder | Invocation after setup |
| --- | --- | --- |
| Abacus AI Agent | .abacusai/skills/ | /skill-name in VS Code |
| OpenAI Codex | .agents/skills/ | Codex skill picker or $skill-name |
| Claude Code | .claude/skills/ | /skill-name |

The host application determines discovery; the underlying model alone does not. This starter list covers these three hosts, not every AI product. Check official documentation before adding another host or claiming compatibility.

The sync script never deletes files. Without --write, it reports missing and differing copies. With --write, it adds missing skill files. If a file differs, it reports a conflict and leaves it untouched. Review conflicts before using --force to update:

    python3 scripts/sync_skills.py --host codex --write
    python3 scripts/sync_skills.py --host all --write

The host choices are abacus, codex, claude, or all. The script is an optional way to populate native folders after the host has been selected and the change is agreed. It does not initialize Git.

## Personas

- **Learning Counselor:** Understands goals and context, asks instead of assuming, assesses feasibility honestly, and prepares a confirmed Learning Brief and route for the Teacher.
- **Teacher:** Uses the confirmed brief, checks baseline knowledge and prerequisites, teaches in depth as useful, recommends assessments when evidence supports them, and adjusts instruction based on evidence.

## Canonical skills

- **initialize:** Clarifies the agent host and model separately, inspects the repository, verifies current discovery instructions, and proposes a native layout and Git policy.
- **learning-guide:** Learning Counselor entry and closeout workflow for clarifying a goal and preparing a confirmed Learning Brief.
- **teacher:** Entry, teaching, assessment-recommendation, and closeout workflow based on the Learning Brief.
- **learning-plan:** Produces an ordered, adjustable path after the goal is understood.
- **progress-journal:** Maintains a small central index and topic-specific records with learner-reviewed, evidence-aware updates.
- **assessment:** Checks baseline, covered topics, milestones, or goal-related exam readiness; Teacher recommendations are optional and learner-led.
- **interview:** Runs realistic mock interviews with follow-ups and rubric-based feedback.
- **question-bank:** Maintains a learner-approved shared topic bank for assessment and interview questions, answer keys, and rubrics; once configured, it saves substantive questions from those sessions under the agreed policy.
- **study-notes:** Produces detailed, source-grounded Markdown study notes for an agreed learning workspace.
- **handwritten-visual-notes:** Produces colorful handwritten-style PNG sheets, reusing palette preferences saved in the project for viewing and copying by hand.
- **visual-notes:** Produces general visual summaries such as concept maps, diagrams, and timelines.
- **writing:** Drafts natural, audience-appropriate content and commit messages with specific subjects and detailed, accurate bodies under this repo's policy.
- **workspace-intake:** Creates an agreed workspace or inspects an existing learning repository.
- **git-updates:** Applies the learner's Git policy and respects authorization before commits and pushes.

These canonical skill files are not automatically host shortcuts until a native folder has been set up or the host is explicitly told to read the skill file.

## Optional topic question banks

A question bank is created only after agreeing on paths, contents, and Git policy. Once configured, the bank saves substantive assessment and interview questions from sessions under that policy. Use a small central `QUESTION-BANK.md` index with links to topic-specific `<topic>/QUESTION-BANK.md` files beside the relevant materials. The index stays small; question prompts, answer keys or rubrics, explanations, and sources live with each topic. Use `templates/question-bank-index-template.md` and `templates/topic-question-bank-template.md` as blank starting points.

Question banks preserve assessment and interview practice across lessons. Assessment and Interview workflows use `question-bank` to save substantive questions, follow-ups, answer keys or rubrics, and sources in the agreed active-topic bank. During practice, the key or rubric stays hidden until the learner tries. Keep learner attempts separate from reusable questions; save attempts or scores only if the learner opts in, in the agreed journal or attempt log. Questions must be grounded in material covered, assigned, or relevant to an agreed interview goal, and uncertain or time-sensitive answers must be marked for review.

## Optional learner workspaces and journals

Personal learning data is not created automatically. Before creating a journal or topic workspace, agree on its name, exact location, contents, and whether it belongs in Git. Keep private notes and personal progress out of this shared learning system by default.

Use templates/learning-brief-template.md for the counselor-to-Teacher handoff, templates/learner-journal-template.md for the central index, and templates/topic-journal-template.md for topic records. The central LEARNING-JOURNAL.md is a small index to topic journals and holds only genuinely cross-topic notes. Keep detailed reflections and problem history beside the relevant topic materials. At session start, begin with the agreed learning home and Learning Brief; read the journal index and active topic README or journal only when needed for the next step. Record the learner’s proposed approach, guidance needed, learner-reported acceptance, and what they want to derive or revisit; distinguish reports from demonstrated evidence. A completed file, commit, or accepted submission alone does not demonstrate mastery.

## Keep session context small

During normal learning, load the active skill and only the records needed for the next step. Start from the Learning Brief; follow its plan link only when route details are missing. Read the active topic journal, README, and question bank only when they add relevant context. Keep briefs near 200 words, omit empty fields, and link to detailed plans instead of repeating them. Do not load the full README, evaluation cases, templates, all skills, or unrelated topic records into an ordinary lesson.

## Existing learning repositories

Use workspace-intake to inspect a repo where learning is already underway. Inventory its materials, relate them to the agreed goal, and propose journal updates with references to evidence. Distinguish what the materials show was completed from what they establish the learner understands. It asks whether you want a restructure or prefer to keep the current layout. If you opt in, it can propose a better structure with a current-to-proposed path map and effects on references, imports, configuration, tests, and host discovery; it applies only the specific reorganization you approve.

If you want to resume learning after cloning or pulling the repo, ask it to set up an agreed learning entry point from [the continuity index template](templates/learning-home-template.md). The index links to the active goal, confirmed Learning Brief and plan, central journal index, current topic materials, and latest session notes, and records the current milestone, demonstrated evidence, open questions, and next step. Future agents should read it before resuming; if the host does not discover it automatically, direct the agent to the file. You choose which records are tracked in Git; private details stay out unless you explicitly choose to include them. During a later session, use the Teacher skill to resume from the saved state.

## Git policy

Discuss what should be tracked, what should remain private or untracked, how journal changes are handled, commit style, branch, and remote before connecting or reshaping a workspace. Keep changes focused: make the smallest coherent change and preserve unrelated work. Before each Git action, show the exact files and destination. Authorization to stage, commit, and push is separate; a request authorizes only the action and scope it explicitly covers. Every commit needs a specific subject and a detailed body explaining why and what changed and which checks were actually run. Do not initialize Git or publish changes without authorization.

## Quality checks

The manual cases in [evals/](evals/README.md) and [evals/learning-workflows.md](evals/learning-workflows.md) cover skill routing and core learning workflows. They are prompts and criteria, not proof that a model has passed them; the repository has no automated runner or CI enforcement.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to propose and review changes.

## License

This project is released under the MIT License. See [LICENSE](LICENSE) for details.

## Official host references

- Abacus AI Agent skills: https://abacus.ai/help/abacusai-desktop/agents-and-skills
- Codex skills: https://learn.chatgpt.com/docs/build-skills
- Claude Code skills: https://code.claude.com/docs/en/skills
