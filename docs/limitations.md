# Limitations

- Agents can miss, misinterpret, or hallucinate behavior and evidence. Confidence labels are qualitative, not calibrated probabilities.
- Untrusted content can attempt prompt injection. Instructions help define the boundary but do not guarantee that the host follows it. A session started outside the target can still have loaded untrusted instructions.
- Context, time, permissions, rate limits, and incomplete or truncated retrieval can leave important paths unreviewed. Large repositories require prioritization, not implied completeness.
- Language, framework, and tool availability vary. An unfamiliar or unsupported language may only receive partial review; report the actual coverage rather than asserting support.
- Obfuscated, generated, or binary content can conceal behavior. Binary reverse engineering and execution are outside the MVP. Runtime-only behavior cannot be established by static review alone.
- Dependencies, submodules, LFS payloads, and release artifacts may not be examined. Source inspection does not prove that a release binary was built from the inspected source.
- BeforeRun does not enforce a sandbox. Host tool permissions and operating-system isolation are separate controls. Never treat a prompt as equivalent to either.
- The skill has no independent LLM API client, but the host agent may send content to its model provider. Redaction cannot guarantee removal of all secrets; do not intentionally read secret files.
- Claude Code has limited local and user-reported tests with outstanding evidence failures and timeouts, not complete boundary or remote-review verification. User-shared Antigravity BR-12 and BR-07 requests and reports are available; BR-07 has evidence issues, and command dispatch, discovery, effective permissions and log completeness remain unverified. The host may load skills automatically despite the skill's instruction to review only on explicit request; host-specific controls and actual behavior must be checked. See the [readiness report](mvp-readiness.md).

BeforeRun reports suspicious behavior and supporting evidence. It does not certify code as safe.
