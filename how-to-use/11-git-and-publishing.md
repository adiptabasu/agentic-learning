# Choose what to track and publish with Git

Use this when you want to save learning-system changes or share a learning repo. Journal and session records may contain private information, so decide what belongs in Git before publishing.

## Agree on what belongs in Git

Before changing or publishing files, decide which records are shared and which stay private. You can ask:

> Help me set a Git policy for this learning repo. Identify likely reusable project files versus personal learning data. Ask me what I want tracked, what should stay private or ignored, and which branch and remote are intended. Do not change Git settings or publish anything.

Do not assume all notes are safe to publish. Review the ignore rules and current tracking status before putting private details into a file; a file already tracked by Git remains tracked even if you later add an ignore rule.

## Review the exact proposed change

Invoke `git-updates`, or say:

> Read `skills/git-updates/SKILL.md` and follow it. Inspect this repo's current branch, remote, status, and diffs. I may want to publish [brief description]. First show me the exact files and content that would be included, identify private or unexpected data, and recommend a commit message. Do not stage, commit, or push yet.

Review the file list and diff. Ask for exclusions or corrections. A good commit message describes the change actually present; it should not claim checks or tests you did not run.

## Authorize each action you want

Once the exact files are agreed, authorize only the next action. For example:

> Stage only [file list] for a commit on [branch]. Do not commit or push yet.

After checking the staged diff:

> Commit the staged [file list] with this message: `[type(scope): specific summary]`. Do not push yet.

Then, if you intend to publish it:

> Push commit [commit identifier or description] from [branch] to [remote/branch]. Do not include other commits or files.

You can ask for review, staging, or a commit without asking for a push. Authorization for one action does not authorize the others. Do not force-push or rewrite history unless you explicitly request that exact operation.

## Check the result

After the action, ask the agent to report the commit identifier, destination, and whether the working tree and branch are synchronized. If the push fails, review the reason and proposed next step before authorizing a retry or a different operation.
