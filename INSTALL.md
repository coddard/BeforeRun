# Installation

Install the entire canonical [skill folder](skills/beforerun), including `references/`. Review this repository and the host's permissions before installing. Installation copies instruction files only; BeforeRun does not install dependencies, configure hooks, or change global agent settings. The commands below are user-run examples, not actions performed automatically by the skill.

## Manual installation

Choose a trusted, platform-supported skills directory. From a trusted local copy of this repository, copy `skills/beforerun` to a new `beforerun` directory under that location; preserve its contents and relative paths. Do not copy it into a target being reviewed. Do not overwrite an existing installation without reviewing it first.

For documented platform locations and invocation details, see [Claude Code](docs/integrations/claude-code.md) or [Antigravity](docs/integrations/antigravity.md). Claude Code has limited local and user-reported runtime tests; Antigravity has not been runtime-tested for BeforeRun. Other hosts are unsupported until verified.

The host needs permission to read the installed skill and the requested target. Remote review additionally needs an available read-only GitHub source-retrieval tool and network access. No specific connector or target dependency is required. If access, safe tooling, or privacy constraints prevent review, the agent must report the limitation.

## Invocation

Where supported, explicitly invoke the skill and provide the target:

```text
/beforerun https://github.com/owner/repository
/beforerun /path/to/script.py
```

Slash commands, argument handling, and skill discovery differ across hosts; see the integration notes. If a host does not pass a target with the command, provide it in the conversation. A missing target must prompt a question. Installing the skill must not itself trigger a review; see each integration's notes on automatic skill loading and its limitations.

## Uninstall

Remove only the `beforerun` directory you installed in the selected skills location, using your host's file manager or trusted shell. If you made optional host-specific changes, revert those separately. A running host may need a reload or new session before discovery changes take effect. Uninstallation does not remove reports you chose to save elsewhere.
