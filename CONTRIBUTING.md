# Contributing to Agentic Learning

Thanks for helping improve Agentic Learning. Keep contributions focused on the reusable learning system; never include private learner journals or personal study data.

## Propose a change

For a new skill, persona, or substantial behavior change, first compare the proposal with the lists in `README.md` and the relevant files under `skills/` and `personas/`. Explain the gap and why an existing workflow should not be extended instead. Raise a focused issue or discussion before investing in a large change.

Read `AGENTS.md` and, for canonical skill changes, `skills/AGENTS.md`. Keep portable skill sources under `skills/` and persona guidance under `personas/`. Use concise, matching Agent Skills frontmatter; keep the smallest coherent workflow change and avoid host-specific behavior in canonical instructions.

## Prepare a change

- Preserve the project principles: clarify goals rather than assuming them, distinguish activity from demonstrated understanding, and do not promise exam, career, or hiring outcomes.
- Update relevant manual cases under `evals/cases/` when changing a covered skill. For new or high-impact behavior, add positive and negative routing examples and a behavioral scenario where useful.
- Run checks relevant to the change. At minimum, inspect the complete diff and run `git diff --check`; report the commands actually run and their results. Evaluation cases are manual prompts; there is no automated runner or CI enforcement.
- Do not include secrets, private learner records, private repository contents, or unrelated formatting changes. Redact personal details in examples.

## Open an issue or pull request

Describe the learner need, affected persona or skill, intended behavior, and why existing workflows do not already cover it. For skill changes, include relevant evaluation prompts and observed results. State what was checked, what could not be checked, and any known limitations. For behavior reports, include a sanitized prompt, expected and actual behavior, and the host/runtime when relevant.

Do not post private learner data or exploitable security details in a public issue. Contact the repository maintainer privately for sensitive reports until a dedicated reporting process is published.

## License for contributions

By submitting a contribution for inclusion in this repository, you agree that the contribution is provided under the repository's [MIT License](LICENSE). Submit only material you authored or are authorized to contribute.
