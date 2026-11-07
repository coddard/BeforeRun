# Antigravity integration

**Status:** experimental; user-shared local BR-12 and BR-07 slash-form requests and reports are available. Actual skill discovery and command dispatch, effective permissions, and model and app versions for those runs remain unverified. The BR-07 report disclosed the injection and depicted autostart but contained unsupported categorical claims and reported a directory-listing command without visible arguments. Official [Google Antigravity agent skills documentation](https://antigravity.google/docs/skills/) was inspected November 7, 2026. The `antigravity` command was not found on PATH; Antigravity App 2.29.0 was found in the standard macOS Applications directory, but is not confirmed as the version used for either report. See the [readiness report](../mvp-readiness.md).

## Installation and invocation

The documentation lists `~/.gemini/config/skills/<skill-folder>/` as the global skill location and `<workspace-root>/.agents/skills/<skill-folder>/` as a workspace location. Prefer the global location when reviewing unrelated targets from a fresh trusted session outside the target. Manually copy the whole canonical `skills/beforerun/` folder to `~/.gemini/config/skills/beforerun/`; keep the references and do not overwrite an existing installation without review.

The Antigravity App documentation describes manual `/skill-name` invocation; the CLI also documents slash-command discovery. An intended invocation is `/beforerun https://github.com/owner/repository`. The user shared a local `/beforerun` request and a report naming the intended fixture, but actual command dispatch and argument handling were not independently verified. If needed, state the explicit review request and target in the conversation. The CLI documentation suggests `/skills reload` or a new conversation after adding skills while it is running; actual BeforeRun discovery remains unverified.

## Manual smoke test

1. In a separate temporary workspace, copy the canonical skill into `.agents/skills/beforerun/` and copy an inert fixture there. Do not copy the skill into an untrusted target.
2. Open that workspace in Antigravity and start a new conversation. Explicitly invoke `/beforerun` with the fixture's absolute path. If discovery fails, record the error rather than assuming the skill loaded.
3. Permit only the reads needed for the skill and fixture; reject target execution, edits, secret access, and requests to fixture endpoints. Model-provider communication is separate from target-endpoint access.
4. Record the app version, visible invocation, available permission settings, tool activity and report. Check the report against the [evaluation rubric](../../evals/rubrics/worksheet.md); an incomplete transcript cannot independently prove enforcement or completeness. Do not publish raw logs without reviewing them for sensitive information.

## Automatic loading and permissions

The documentation also describes autonomous invocation for relevant tasks. BeforeRun's explicit-request rule is an instruction, not a platform-enforced guarantee. No Antigravity-specific automatic-invocation control has been verified here; do not claim one. Review host permissions separately and grant only access needed for the review. Instructions do not replace OS isolation, and a fresh session cannot prove that no untrusted instructions were previously loaded.

## Removal

Remove the installed `beforerun` directory from the chosen skills location. No plugin manifest, hook, or global configuration change is required by these instructions. See [installation](../../INSTALL.md).
