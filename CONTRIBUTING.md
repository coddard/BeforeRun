# Contributing

BeforeRun is a skill-first, static-review project. Keep the canonical methodology in [the skill](skills/beforerun/SKILL.md) and its references; avoid adding an analysis engine, target execution, or platform-specific assumptions to the portable workflow.

- Support findings with traceable file locations and observed behavior; distinguish inference, documentation claims, and uncertainty. Include plausible benign explanations and counterevidence.
- Add benign counterexamples alongside suspicious patterns so ordinary uses of network, subprocess, encryption, or similar capabilities are not treated as inherently malicious.
- Use only synthetic, inert fixtures with reserved example destinations. Never include real credentials, active malware, executable target fixtures, or calls to real network services. Do not place fixture instructions in automatically discovered agent, hook, or workflow configuration.
- Make platform support claims only with cited official documentation, a verification date, and an honest runtime-test status. Record unavailable tools and failed tests rather than inventing results.
- Contribute original material or material you have the right to redistribute. Do not copy copyrighted books, malware samples, proprietary rules, or large sections of another project's skill.
- Do not run reviewed target code or change its files. Review [security reporting](SECURITY.md) before sharing sensitive material.

See [evaluation guidance](evals/README.md) for the manual cases and repository validation commands. A structural check alone cannot establish that an agent follows the review boundaries.
