# Bring in an existing learning repository

Use this when you already have notes, course work, exercises, projects, or another learning repo and want to connect that work to a learning goal. The agent should inspect and report first. Giving it a repo does not automatically authorize restructuring or edits.

## Ask for an inventory

Open the existing repository in your agent and invoke `workspace-intake`, or say:

> Read `skills/workspace-intake/SKILL.md` and follow it for this repository at [path]. My learning goal is [goal, if known]. First inspect the project instructions, tree, Git status, and learning materials. Summarize what is here and how it might relate to my goal. Do not edit or move files yet.

If you do not yet have a learning goal, say so and first use the [goal exploration guide](01-explore-a-learning-goal.md).

## Decide whether to restructure

The agent should ask whether you want to keep the current structure or consider a redesign. Choose explicitly:

> Keep the existing structure. Please only give me the inventory and suggest any targeted learning records that would help.

Or:

> I want to consider restructuring. First explain what problem the current layout causes and propose a target structure. Show a current-to-proposed path map, which files would move, stay, be added, or be removed, and the impact on links, imports, configuration, tests, tooling, and agent discovery. Do not make changes until I approve the exact plan.

Review the proposal. Ask questions about any uncertain file purpose or risk. If you decide to proceed, approve only the version you agree with:

> I approve this structure plan: [briefly identify it or quote the final plan]. Apply only those changes. Preserve file contents, update affected references, and show me the resulting tree and diff. Stop if you encounter an unplanned conflict or risk.

If you do not approve, nothing should be moved or deleted. You can ask for a smaller change or keep the repo as it is.

## Connect the materials to your goal

Ask the agent to separate observed facts from conclusions:

> Based on the files you inspected, list completed activities separately from evidence that I understand the material. Cite the relevant file paths and flag uncertain inferences. Suggest any gaps or next learning steps, but do not update my journal yet.

A completed assignment or commit is not, by itself, proof of mastery. If you want journal updates, use the [progress journal guide](05-progress-journal.md) and review each proposed change.

## Add continuity only if you want it

If you want a future agent to resume after a clone or pull, say:

> I want this repo to preserve my learning state across sessions. Propose an easy-to-find learning index and paths for my active goal, confirmed plan, journal, and latest session note. Tell me exactly which files would be tracked in Git and which would remain private or ignored. Do not create them until I agree to the paths and tracking policy.

After agreement, the agent can adapt [the learning-home template](../templates/learning-home-template.md). For a future session, follow the [resume after pull guide](04-resume-after-pull.md).

## Git boundaries

Review the current branch, remote, staged changes, and private data before publishing. This guide does not authorize Git initialization, remote changes, commits, or pushes. Use the separate Git workflow and explicitly authorize each action you want.
