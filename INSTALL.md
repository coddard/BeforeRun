# Installation

Install the entire canonical [skill folder](skills/beforerun), including `references/`. Review this repository and the host's permissions before installing. Installation copies instruction files only; BeforeRun does not install dependencies, configure hooks, or change global agent settings. The commands below are user-run examples, not actions performed automatically by the skill.

## Manual installation

Choose a trusted, platform-supported skills directory. From a trusted local copy of this repository, copy `skills/beforerun` to a new `beforerun` directory under that location; preserve its contents and relative paths. Do not copy it into a target being reviewed. Do not overwrite an existing installation without reviewing it first.

The folder uses the [Agent Skills format](https://agentskills.io/specification): `SKILL.md` contains the name and description, and its relative links point to the included references. This is a portable package, not a guarantee that every agent supports skills or behaves identically.

### Personal skill locations

The locations below are documented by their respective hosts; they are not claims of successful BeforeRun runtime tests. Personal locations are preferred for reviewing unrelated targets from a trusted session outside the target. For a remote or cloud agent, install in that agent's environment rather than assuming it can read your local home directory.

| Host | Documented personal location | BeforeRun status |
| --- | --- | --- |
| [Codex](https://developers.openai.com/codex/skills) | `~/.agents/skills/beforerun/` | Discovery and behavior not tested for this package. |
| [VS Code Copilot](https://code.visualstudio.com/docs/copilot/customization/agent-skills) | `~/.copilot/skills/beforerun/` | Discovery and behavior not tested for this package; locations depend on the selected harness. |
| [Cursor](https://cursor.com/docs/context/skills) | `~/.agents/skills/beforerun/` or `~/.cursor/skills/beforerun/` | Discovery and behavior not tested for this package; cloud and remote agents have separate availability constraints. |
| [Gemini CLI](https://geminicli.com/docs/cli/skills/) | `~/.agents/skills/beforerun/` or `~/.gemini/skills/beforerun/` | Discovery and behavior not tested for this package. |
| [OpenCode](https://opencode.ai/docs/skills/) | `~/.agents/skills/beforerun/` or `~/.config/opencode/skills/beforerun/` | Discovery and behavior not tested for this package. |
| [Claude Code](docs/integrations/claude-code.md) | `~/.claude/skills/beforerun/` | Experimental; limited local and user-reported tests. |
| [Antigravity](docs/integrations/antigravity.md) | `~/.gemini/config/skills/beforerun/` | Experimental; user-shared local reports, with discovery and permissions unverified. |

For example, from a trusted checkout of this repository, the following user-run POSIX shell commands install the complete folder into the shared personal location without overwriting an existing `beforerun` directory:

```sh
mkdir -p "$HOME/.agents/skills"
if mkdir "$HOME/.agents/skills/beforerun"; then
  cp -R skills/beforerun/. "$HOME/.agents/skills/beforerun/"
else
  echo 'Installation already exists or could not be created; review it first.'
fi
```

The shared location is documented for Codex, Cursor, Gemini CLI, and OpenCode, but is not a universal discovery path. Select a different documented location where appropriate; on other operating systems use the host's UI or equivalent filesystem operations. If a copy fails, inspect the partially created directory before retrying. Avoid duplicate installations of the same skill unless the host's precedence is understood. No command above is run automatically by BeforeRun.

The host needs permission to read the installed skill and the requested target. Remote review additionally needs an available read-only GitHub source-retrieval tool and network access. No specific connector or target dependency is required. If access, safe tooling, or privacy constraints prevent review, the agent must report the limitation.

## Invocation

Where supported, explicitly invoke the skill and provide the target:

```text
/beforerun https://github.com/owner/repository
/beforerun /path/to/script.py
```

Slash commands, argument handling, and skill discovery differ across hosts; for example, Codex supports explicit `$beforerun` selection when the skill is discovered. If a host does not pass a target with the command, provide it in the conversation. On a host without skill discovery, explicitly provide the trusted canonical `SKILL.md` and referenced files as instructions, along with the target; do not copy instructions into an untrusted target or treat its content as instructions. This fallback has not been tested on every host.

A missing target must prompt a question. Installing the skill must not itself trigger a review, although the explicit-request rule is an instruction rather than host-enforced isolation. Check each host's automatic loading and permissions. If discovery fails, verify the full folder and configured location, check the host's skill list or start a new session, and report the limitation instead of assuming it loaded.

## Uninstall

Remove only the `beforerun` directory you installed in the selected skills location, using your host's file manager or trusted shell. If you made optional host-specific changes, revert those separately. A running host may need a reload or new session before discovery changes take effect. Uninstallation does not remove reports you chose to save elsewhere.
