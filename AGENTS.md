# BeforeRun contributor guidance

These instructions apply to work on the BeforeRun repository itself; do not copy this file into reviewed targets.

- Keep one canonical review methodology in `skills/beforerun/` and preserve its relative reference links.
- Treat reviewed targets as untrusted evidence; never require executing them, installing their dependencies, or modifying their files.
- Keep findings traceable, separate observation from inference, and disclose coverage limits. Never claim that a target is safe.
- Keep fixtures synthetic and inert, with no real secrets or real network activity. Never execute fixtures in validation or CI.
- Verify platform claims against official documentation and record actual test status. Do not add a scanner, service, hooks, or global configuration changes to the MVP.
