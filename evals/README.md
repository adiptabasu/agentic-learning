# Manual skill evaluations

These cases help reviewers check skill routing and important learning behaviors. They are manual evaluation prompts, not automated tests; no runner or CI enforcement is currently provided. See also [learning workflow scenarios](learning-workflows.md), which exercise end-to-end situations across multiple skills.

## Running a case

1. Use an isolated repository copy and an agent host where the relevant skill is available.
2. Run a positive trigger and confirm the intended skill is selected or followed. Run a negative trigger and confirm it is not inappropriately selected; an appropriate alternative may be suggested.
3. Run the behavioral scenario and compare the response and any proposed artifacts with every pass criterion in the case.
4. Record the skill revision, host/runtime, prompt, observed outcome, and limitations in the change review. Do not report a case as passed unless it was actually run and reviewed.

Use fictional or redacted learner details. Behavioral cases should not create or publish personal journals or learning workspaces unless the scenario explicitly authorizes it in an isolated copy.

Update relevant cases when covered behavior changes. Add cases for other skills when their risk or expected behavior makes manual evaluation useful. Passing these cases does not prove suitability for every learner, subject, or host.

## Current coverage

- [Assessment](cases/assessment.json)
- [Git Updates](cases/git-updates.json)
- [Initialize](cases/initialize.json)
- [Learning Guide](cases/learning-guide.json)
- [Learning Plan](cases/learning-plan.json)
- [Progress Journal](cases/progress-journal.json)
- [Teacher](cases/teacher.json)
- [Visual Notes](cases/visual-notes.json)
- [Workspace Intake](cases/workspace-intake.json)
- [Writing](cases/writing.json)
