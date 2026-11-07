# Antigravity integration

**Status:** experimental; documented, not runtime-tested for BeforeRun. Official [Google Antigravity agent skills documentation](https://antigravity.google/docs/skills/) was inspected November 7, 2026. The `antigravity` command was not found on PATH; Antigravity App 2.29.0 was found in the standard macOS Applications directory, but its skill discovery and invocation were not tested. See the [readiness report](../mvp-readiness.md).

## Installation and invocation

The documentation lists `~/.gemini/config/skills/<skill-folder>/` as the global skill location and `<workspace-root>/.agents/skills/<skill-folder>/` as a workspace location. Prefer the global location when reviewing unrelated targets from a fresh trusted session outside the target. Manually copy the whole canonical `skills/beforerun/` folder to `~/.gemini/config/skills/beforerun/`; keep the references and do not overwrite an existing installation without review.

The Antigravity App documentation describes manual `/skill-name` invocation; the CLI also documents slash-command discovery. An intended invocation is `/beforerun https://github.com/owner/repository`, but BeforeRun's invocation and target argument handling have not been runtime-tested. If needed, state the explicit review request and target in the conversation. The CLI documentation suggests `/skills reload` or a new conversation after adding skills while it is running; actual BeforeRun discovery remains unverified.

## Automatic loading and permissions

The documentation also describes autonomous invocation for relevant tasks. BeforeRun's explicit-request rule is an instruction, not a platform-enforced guarantee. No Antigravity-specific automatic-invocation control has been verified here; do not claim one. Review host permissions separately and grant only access needed for the review. Instructions do not replace OS isolation, and a fresh session cannot prove that no untrusted instructions were previously loaded.

## Removal

Remove the installed `beforerun` directory from the chosen skills location. No plugin manifest, hook, or global configuration change is required by these instructions. See [installation](../../INSTALL.md).
