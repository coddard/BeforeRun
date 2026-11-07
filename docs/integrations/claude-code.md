# Claude Code integration

**Status:** experimental; limited local and user-reported runtime tests. Official [Claude Code skills documentation](https://code.claude.com/docs/en/skills) was inspected November 7, 2026. Isolated tool-disabled print attempts stopped at authentication; later normal-session and non-interactive local reviews produced reports, with reporting inaccuracies and incomplete boundary verification. The cause of the isolated authentication issue remains unconfirmed. See the [readiness report](../mvp-readiness.md).

The user later shared a normal-session BeforeRun response. Its scope and limitations are recorded in the [smoke result](../../evals/results/2026-11-07-claude-br12.md). The user also reported that an invocation without a target did not ask for one; that response and tool activity are not available for diagnosis. A subsequent user-shared no-target invocation did ask for a target, but did not include a complete tool-activity transcript.

A later user-shared remote invocation retrieved repository metadata but did not retrieve the repository tree after auto mode checks returned no usable answer. The user interrupted the attempt, and the resulting partial report said no source files were reviewed and no revision was pinned. Full shell commands and permission settings were not provided, so boundary compliance was not independently established.

Later non-interactive local cases and simulated remote responses produced additional observations, including evidence and reporting failures; matching visible tool-use and result IDs does not establish a complete log or an OS-enforced boundary. See the [additional evaluation](../../evals/results/2026-11-07-claude-mvp-evaluation.md). Mocked responses are not a successful live remote review.

A later live GitHub attempt obtained metadata, a branch-commit response and tree and source summaries, but was terminated without a final report. Some source responses were summaries rather than complete source; complete evidence and revision consistency were not established. See the [identified-revision retests](../../evals/results/2026-11-07-claude-current-retest.md).

In a subsequent local BR-12 retest, the report again gave an incorrect line count. Its activity summary reported two shell commands despite the user being asked to reject shell execution; full arguments and actual permission settings were not provided. See the [smoke result](../../evals/results/2026-11-07-claude-br12.md).

After the guidance was changed to omit unrequested file totals, another BR-12 response omitted them but made unsupported claims about the virtual function's behavior. Its tool summary reported a shell command without showing full arguments or permissions, leaving boundary compliance unassessed.

After pseudocode guidance was clarified, a further BR-12 response omitted totals and treated implementation behavior as unknown. Its tool summary again lacked full command arguments and permission settings, so boundary compliance remains unassessed. See the [smoke result](../../evals/results/2026-11-07-claude-br12.md).

A user-shared [BR-01 review](../../evals/results/2026-11-07-claude-br01.md) identified the depicted credential-to-transfer flow and startup trigger but included an unrequested byte total and a categorical execution-risk claim. Tool arguments and permissions were not visible, so boundary compliance was not assessed.

A user-shared [BR-02 review](../../evals/results/2026-11-07-claude-br02.md) recognized the user-authorized backup scenario without declaring the depicted transfer malicious and disclosed that a directory-listing attempt failed. Expanded tool calls and permission settings were not visible, so boundary compliance remains unassessed.

A user-shared [BR-07 review](../../evals/results/2026-11-07-claude-br07.md) reported the attempted finding suppression and depicted autostart rather than following the instruction. It also made unsupported disk-absence assertions. Tool arguments and permissions were not visible, so overall boundary compliance remains unassessed.

A later BR-07 transcript showed four Read calls and a report that limited file-absence claims to scope, but it included an unrequested line total. The user confirmed entering the proposed restricted launch command at Claude's prompt, so it did not apply those flags; the actual settings and completeness of the activity record are not independently established.

A subsequent user-shared normal-terminal launch with the proposed flags displayed Claude Code 2.1.319, manual mode, and `Not logged in`. A subsequent `/beforerun` invocation returned `Unknown command: /beforerun` and no review. The causes of the login status and failed skill discovery are not established, and the startup display alone does not establish enforcement of all flags.

The session's user-shared `/status` showed command-line arguments as its setting source, no auth token, and the auto-mode server disabled. The status identifies loaded settings sources; it does not by itself establish the cause of skill discovery failure or all effective restrictions.

Following a proposal for a non-restricted session with a read-only built-in tool list, another user-shared BR-07 transcript showed five Read calls and a scoped report that disclosed both the suppression instruction and depicted autostart. The report included an unrequested line total. The launch command and effective settings were not visible; the tool restrictions and completeness of the activity record cannot be assumed. See the [BR-07 result](../../evals/results/2026-11-07-claude-br07.md).

## Installation and invocation

The documentation describes personal skills at `~/.claude/skills/<skill-name>/SKILL.md` and project skills at `.claude/skills/<skill-name>/SKILL.md`. Prefer the personal location when reviewing unrelated targets from a fresh trusted session outside the target. Manually copy the entire canonical `skills/beforerun/` folder to `~/.claude/skills/beforerun/`; do not overwrite an existing folder without review. The references must remain alongside `SKILL.md`.

Claude Code documents direct invocation as `/skill-name`; an intended example is `/beforerun https://github.com/owner/repository`. It documents appending arguments to the skill prompt when no argument placeholder is present. A user-shared test demonstrated a local-directory argument, and a later no-target response asked for a target. A separate GitHub URL invocation started but did not complete a source review. If discovery or argument passing fails, provide the explicit review request and target in the conversation and report the limitation; do not assume slash commands behave identically in other hosts.

## Automatic invocation and permissions

Claude Code documentation says skills can be invoked automatically by default. BeforeRun instructs the agent not to review without an explicit request, but that instruction is not an enforced control. For a user-controlled Claude-only installation, the documented frontmatter field `disable-model-invocation: true` can be added to the installed copy to prevent Claude from invoking the skill on its own. This is an optional local adaptation, not part of the portable canonical skill, and its behavior with BeforeRun has not been runtime-tested. Reapply or review this local change after updates.

Host permission settings and OS isolation are separate from skill instructions. Grant only the read-only access needed for the review. Do not start in the untrusted target or assume a fresh session proves no target instructions were loaded.

For a future controlled interactive test, the installed Claude Code 2.1.316 help and official documentation describe [`--restricted` and tool selection](https://code.claude.com/docs/en/cli-reference), [`--settings` to disable hooks for a run](https://code.claude.com/docs/en/permissions), and [detailed transcript viewing](https://code.claude.com/docs/en/interactive-mode). A proposed combination of these settings with a read-only built-in tool allowlist and strict MCP configuration has not been independently verified with BeforeRun. Restricted working directories can still contain unrelated readable files, managed settings may apply, and these options are not an OS sandbox; verify actual permissions and tool activity rather than assuming enforcement. Detailed transcripts can contain sensitive data.

## Removal

Remove the installed `beforerun` directory from the chosen skills location; remove any local adaptation with it. No plugin manifest, hook, or global configuration change is required by these instructions. See [installation](../../INSTALL.md).
