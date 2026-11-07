# BeforeRun

**Inspect before you execute.** BeforeRun is a portable agent skill for evidence-first static review of untrusted repositories and scripts before installation or execution. It looks for potentially harmful behavior, distinguishes observed code from inference, and reports what could not be reviewed. A suspicious capability alone does not establish malicious intent.

BeforeRun reports suspicious behavior and supporting evidence. It does not certify code as safe.

## Use

Request a review explicitly. The following are target examples, not a promise of identical slash-command behavior across platforms:

```text
/beforerun https://github.com/owner/repository
/beforerun /path/to/local/repository
/beforerun /path/to/script.py
```

With no target, the skill instructs the agent to ask for one rather than reviewing the current directory. The remote URL form supports a GitHub repository root, optionally with a trailing slash or `.git`; other URL forms are unsupported. See [installation](INSTALL.md) and [target resolution](skills/beforerun/references/target-resolution.md).

## What it reviews

The review prioritizes entry points, installation and startup behavior, sensitive file access, data destinations, command and dynamic execution, persistence, remote control, destructive operations, agent-directed instructions, and discrepancies with documented purpose. It traces relationships when evidence permits and includes benign explanations and coverage gaps. Categories are review prompts, not implemented detection rules.

BeforeRun is not a scanner, sandbox, comprehensive vulnerability assessment, or malware classifier. Its instructions prohibit executing target code, installing dependencies, automatically cloning or unpacking targets, contacting target application endpoints, or automatically remediating findings; enforcement depends on the host. It does not establish intent with certainty. Source review does not prove a release binary corresponds to the source.

## Support

| Integration | Status | Evidence and limits |
| --- | --- | --- |
| Claude Code | Experimental; limited local and user-reported runtime tests | Local reviews and a missing-target response were observed; complete boundary enforcement and remote review remain unverified. See [Claude Code](docs/integrations/claude-code.md). |
| Antigravity | Documented, not runtime-tested; experimental | Official skill locations and invocation are documented; this skill's integration has not been smoke-tested. See [Antigravity](docs/integrations/antigravity.md). |
| Other hosts | Unsupported | Manual installation may be possible, but compatibility is unverified. |

## Illustrative report

This example is synthetic; it is not an evaluation result.

> **Review status:** partial. **Finding outcome:** review_required.
>
> **BR-FUNCTION-MISMATCH:** Documentation claims local-only processing, while reviewed source constructs a request containing a credential-like value. Whether the request is reachable and where it is sent remain unresolved. Review the caller and destination; unexamined dependencies limit the conclusion.

## Privacy and boundaries

The target is untrusted evidence, including its instructions. BeforeRun does not intentionally open actual secrets; incidental values must be redacted. The skill has no independent LLM API client, but the host agent may send reviewed content to its model provider, and masking is not guaranteed. Agent instructions are not an enforced sandbox; host permissions and operating-system isolation are separate controls. Prefer a fresh trusted session outside the target, without assuming that this eliminates previously loaded instructions.

See [limitations](docs/limitations.md), [MVP readiness](docs/mvp-readiness.md), [contributing](CONTRIBUTING.md), and [security reporting](SECURITY.md).
