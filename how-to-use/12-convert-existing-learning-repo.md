# Convert an existing Git learning repo for easy resumption

Use this when you already have learning material and history in a Git repository, but its structure is inconsistent or does not make it easy for an agent to continue. This workflow keeps the existing repository and its commit history, reorganizes files only after you approve a concrete plan, and prepares a clear checkpoint for future sessions.

## 1. Open the existing repository and request an inventory

Open the old repo in the agent you intend to use. Invoke `workspace-intake`, or say:

> Read `skills/workspace-intake/SKILL.md` and follow it for this existing repository at [path]. I have already been learning [topic or goal] here. First inspect its instructions, file structure, Git branch/status/remotes, and relevant learning materials. Summarize what is present and what it suggests about my progress. Do not modify anything yet.

The agent should treat files and commit history as evidence of work performed, not proof that you understand the material. If your goal has changed, clarify the current goal before connecting old materials to it.

## 2. Decide whether to restructure

The agent should ask whether you want to keep the existing layout or restructure it. Choose explicitly:

> I do want to restructure this repo into an agreed learning format so an agent can resume easily after a clone or pull. Propose the target structure first; do not move or edit files yet.

Ask for a file-by-file map and review the consequences:

> Show the current path and proposed path for every file you want to move, copy, add, keep, or remove. Explain effects on links, imports, build or config files, tests, tools, and Git history. Identify which old material supports my current goal, what is unclear, and what should stay untouched. Do not delete or overwrite anything in the proposal.

If you prefer not to reorganize, say:

> Keep the existing structure. Only propose an agreed learning index and any small additions needed to resume; do not move existing files.

## 3. Agree on the learning records and Git policy

To make future sessions easy to restart, decide where the repo will keep an entry point, active goal, confirmed plan, central journal index, topic journals, and session notes. Ask:

> Propose a repo-local learning home/current-goal file and central LEARNING-JOURNAL.md index. Keep the index small: link to topic-specific journals and include only cross-topic notes. Put detailed reflections and problem history beside each topic's materials in that topic's LEARNING-JOURNAL.md. Tell me exactly which files will be tracked in Git and which will remain private or ignored. Use the existing continuity and journal templates if helpful. Do not create files until I agree to their paths and contents.

When converting an existing monolithic journal, ask for an inventory before moving anything. Count every session entry and problem-history row, map each to a topic destination, and flag ambiguous material for review. Preserve all entries, dates, references, and uncertainty; fix relative links after moves. Compare source and destination counts and review the final link map before retiring the original.

Review the plan for personal details. Choose whether the journal and session notes belong in Git; private records should remain untracked unless you explicitly want to share them. Confirm the intended remote and branch from the repo's actual Git configuration rather than guessing.

## 4. Approve and apply the migration

Once the target paths, contents, and tracking policy are clear, approve the exact plan:

> I approve this migration plan: [identify or quote the final map]. Apply only those changes. Preserve existing content and Git history. Update affected references and configuration, and inspect the final tree and diff. Stop and show me any unexpected conflict or risk before proceeding.

The agent should adapt the existing material rather than claim more progress than the evidence supports. Have it mark uncertain conclusions in the journal as uncertain. Keep original files or copies when the agreed plan requires them; don't reinitialize Git, replace the remote, or rewrite history as part of a structure migration.

Before publishing, inspect the staged diff and confirm the exact files. Example:

> Read `skills/git-updates/SKILL.md`. Review the current branch and remote and show me the exact files and diff proposed for publication. Exclude private or ignored learning records. Do not stage, commit, or push yet.

After reviewing the diff, authorize the actions separately. For example:

> Stage only [approved paths]. Do not commit or push yet.

Then, after reviewing what is staged:

> Commit these staged changes with `[type(scope): specific summary]`. Do not push yet.

Then, if you want to publish:

> Push commit [identifier] from [branch] to [verified remote/branch]. Do not include other commits.

## 5. Resume later from the new clone or pull

After cloning the repo elsewhere or pulling it on another machine, open the repository and say:

> Use the teacher skill to resume my learning. Read the agreed learning home/current-goal file and confirmed plan, then the central LEARNING-JOURNAL.md index. For my active topic, read only its README.md and LEARNING-JOURNAL.md. Summarize my current goal, topic, milestone, relevant evidence, open questions, and next step. Ask me to confirm before teaching.

If that host does not expose the `teacher` shortcut, say:

> Read `skills/teacher/SKILL.md` and follow it. First read `LEARNING.md` and the learning records it links to, then summarize where I left off and ask me to confirm before we continue.

If a linked record is missing or stale, correct it before the lesson. Do not let the agent fill gaps by guessing. For more detail on a resumed session, see [resume after a pull](04-resume-after-pull.md).
