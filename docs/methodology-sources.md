# Methodology and integration sources

BeforeRun's procedure and examples are original. The following are methodological context, not implementation templates. The books' contents or specific chapters were not inspected for this project; they are listed as bibliographic references only, without quotations or chapter claims.

- Michael Sikorski and Andrew Honig, *Practical Malware Analysis*, 2012.
- Joshua Saxe and Hillary Sanders, *Malware Data Science*, 2018.
- [OpenSSF Package Analysis](https://github.com/ossf/package-analysis), repository accessed November 7, 2026. Its project investigates package behavior; BeforeRun does not copy its implementation or perform dynamic execution.
- [Claude Code skills documentation](https://code.claude.com/docs/en/skills), inspected November 7, 2026 for documented skill locations, invocation, arguments, and automatic-invocation controls. See [integration notes](integrations/claude-code.md) for runtime status.
- [Google Antigravity agent skills documentation](https://antigravity.google/docs/skills/), inspected November 7, 2026 for documented skill locations and invocation. See [integration notes](integrations/antigravity.md) for runtime status.
- [Agent Skills specification](https://agentskills.io/specification), [Codex skills](https://developers.openai.com/codex/skills), [VS Code agent skills](https://code.visualstudio.com/docs/copilot/customization/agent-skills), [Cursor skills](https://cursor.com/docs/context/skills), [Gemini CLI skills](https://geminicli.com/docs/cli/skills/), and [OpenCode skills](https://opencode.ai/docs/skills/), inspected November 7, 2026 for the portable format and documented personal locations. Documentation review is not a BeforeRun runtime test.

Documentation may change. Reverify before upgrading a platform's support label or changing installation instructions.
