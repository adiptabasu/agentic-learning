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

1. **Discuss the goal.** Use the Learning Guide workflow to clarify what you want to learn or change, why it matters, what you know already, your constraints, and what success looks like. If you are unsure of the goal, explore it without forcing a decision.
2. **Confirm understanding.** The guide summarizes the goal and starting point so you can correct them. It distinguishes known facts, estimates, assumptions, and unknowns.
3. **Agree on a plan.** Build an ordered route with topics, prerequisites, milestones, practice, evidence of progress, and review points. Estimates are labeled and provided only when justified.
4. **Study with the Teacher.** Discuss how you prefer to study, then work through the agreed route with explanations, examples, and practice.
5. **Check progress.** Use assessments for covered topics or goal-specific preparation such as qualification tests and mock interviews. Results are evidence about specific material, not a guarantee of mastery, passing, or hiring.
6. **Keep history if wanted.** A journal is optional. Choose a private workspace and agree on its location before creating one. Blank formats are in templates/.
7. **Adapt the route.** Revisit older material and adjust the plan when goals, constraints, or evidence change.

The Learning Guide should be candid and respectful. It should not promise success. If a target seems infeasible, it should explain why, identify evidence and uncertainties, and explore alternatives. Slow progress is a prompt to investigate prerequisites, workload, practice, and teaching fit, not a judgment of ability.

## Repository structure

- AGENTS.md — shared project guidance for agents that read this convention.
- personas/ — portable Learning Guide and Teacher behavior definitions.
- skills/ — canonical, tool-independent skill sources.
- templates/ — blank formats for an optional private journal, session notes, and a repo-local learning continuity index.
- evals/learning-workflows.md — example situations and observable behaviors for manually reviewing workflow quality.
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

- **Learning Guide:** Understands goals and context, asks instead of assuming, assesses feasibility honestly, and collaborates on a route.
- **Teacher:** Follows an agreed plan, adapts to study preferences, checks understanding, and adjusts instruction based on evidence.

## Canonical skills

- **initialize:** Clarifies the agent host and model separately, inspects the repository, verifies current discovery instructions, and proposes a native layout and Git policy.
- **learning-guide:** Entry workflow for clarifying a learning goal and preparing an agreed handoff to planning.
- **teacher:** Entry workflow for starting or resuming instruction from an agreed plan.
- **learning-plan:** Produces an ordered, adjustable path after the goal is understood.
- **progress-journal:** Records cross-session progress using evidence and learner-reviewed updates.
- **assessment:** Provides topic checks and goal-related practice tests or interviews.
- **visual-notes:** Produces visual summaries suited to the material.
- **writing:** Drafts or edits natural, audience-appropriate content and specific, accurate commit messages without generic AI filler.
- **workspace-intake:** Creates an agreed workspace or inspects an existing learning repository.
- **git-updates:** Applies the learner's Git policy and respects authorization before commits and pushes.

These canonical skill files are not automatically host shortcuts until a native folder has been set up or the host is explicitly told to read the skill file.

## Optional learner workspaces and journals

Personal learning data is not created automatically. Before creating a journal or topic workspace, agree on its name, exact location, contents, and whether it belongs in Git. Keep private notes and personal progress out of this shared learning system by default.

The journal template tracks goals, starting evidence, session history, uncertainty, difficult areas, review needs, and sources. A completed course file or Git commit alone does not demonstrate mastery. Record evidence such as explaining a concept, solving a new problem, applying it in a project, or an assessment result.

## Existing learning repositories

Use workspace-intake to inspect a repo where learning is already underway. Inventory its materials, relate them to the agreed goal, and propose journal updates with references to evidence. Distinguish what the materials show was completed from what they establish the learner understands. It asks whether you want a restructure or prefer to keep the current layout. If you opt in, it can propose a better structure with a current-to-proposed path map and effects on references, imports, configuration, tests, and host discovery; it applies only the specific reorganization you approve.

If you want to resume learning after cloning or pulling the repo, ask it to set up an agreed learning entry point from [the continuity index template](templates/learning-home-template.md). The index links to the active goal, plan, journal, and latest session notes, and records the current milestone, demonstrated evidence, open questions, and next step. Future agents should read it before resuming; if the host does not discover it automatically, direct the agent to the file. You choose which records are tracked in Git; private details stay out unless you explicitly choose to include them. During a later session, use the Teacher skill to resume from the saved state.

## Git policy

Discuss what should be tracked, what should remain private or untracked, how journal changes are handled, commit style, branch, and remote before connecting or reshaping a workspace. Keep changes focused: make the smallest coherent change and preserve unrelated work. Before each Git action, show the exact files and destination. Authorization to stage, commit, and push is separate; a request authorizes only the action and scope it explicitly covers. Do not initialize Git or publish changes without authorization.

## Quality checks

The manual scenarios in evals/learning-workflows.md cover goal discovery, constraints, lessons without journals, importing an existing repo, mock interviews, and Git publication. They are evaluation prompts and criteria, not proof that a model has passed them.

## License

This project is released under the MIT License. See [LICENSE](LICENSE) for details.

## Official host references

- Abacus AI Agent skills: https://abacus.ai/help/abacusai-desktop/agents-and-skills
- Codex skills: https://learn.chatgpt.com/docs/build-skills
- Claude Code skills: https://code.claude.com/docs/en/skills
