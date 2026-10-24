# Make skills available in your agent

Use this when you have cloned Agentic Learning and want its skills available through your AI agent's skill picker or commands. The host application determines discovery; the model name alone does not.

## Start the initializer

If the `initialize` shortcut is available, invoke it. Otherwise say:

> Read `skills/initialize/SKILL.md` and follow it for this repository. I use [agent host or application]. The model is [model name, if relevant]. This is [a fresh learning repo / an existing repo I want to adapt]. Inspect the current layout and check the host's current official skill instructions. Tell me what you recommend before changing files.

Examples of hosts include Codex, Claude Code, and Abacus AI Agent. If you only know that you are using VS Code, identify which agent or extension is running in it. Give the host and the model as separate details.

## Review the setup proposal

The initializer should identify the verified skill path and invocation, current missing or differing copies, and the files it proposes to add or change. It should also explain any compatibility limits. Ask it to confirm current instructions using official host documentation, not assumptions based on another host.

Before it writes anything, review the proposal and approve the exact host folder and changes. For example:

> I approve adding the current canonical skills to [host-specific project folder] in this repo. Preserve canonical files and any differing copies; show conflicts instead of overwriting them. Do not initialize Git, change remotes, commit, or push.

If you want to compare options instead, say:

> Do not write files yet. Compare the supported setup options for [host] and tell me what each would change.

## Check that skills are discoverable

After the approved setup, ask:

> Verify that the host-specific skill copies match the canonical files. Tell me what the agent can verify from the files and what I need to check in the host UI. If the skills do not appear, give me the documented refresh or reload steps for this host.

The presence of files is not proof that a host's UI exposes the commands. Follow any host-specific refresh instructions, then check its skill picker or command menu. If the host does not expose shortcuts, you can still ask the agent to read a canonical file such as `skills/learning-guide/SKILL.md` and follow it.

## Keep canonical skills as the source

Edit canonical skill files in `skills/`. If copies become stale, ask the initializer to compare them and show conflicts. Do not force an overwrite without reviewing differences. Git setup, tracking choices, commits, and pushes are separate decisions; use the Git policy rather than treating initialization as permission to publish.
