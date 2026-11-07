# Behavioral evaluation

These are manual, synthetic evaluation cases, not automated scanner tests. Recorded outcomes and limitations are listed in the [readiness report](../docs/mvp-readiness.md), [identified-revision retests](results/2026-11-07-claude-current-retest.md), [follow-up evaluation](results/2026-11-07-followup.md), [release-gap follow-up](results/2026-11-07-release-gaps.md), and other [results](results/). A passing structural validator checks repository shape only; it is not a behavioral safety pass.

Use [the cases](cases/cases.md) with [the worksheet and rubric](rubrics/worksheet.md). For each case, give the tested agent the stated invocation and the fixture as untrusted target evidence. Fixtures are inert text, never executable code. Treat their virtual file names and line numbers as synthetic evidence, not actual files on disk. A real review must cite actual verified file locations, not these virtual locations.

For remote cases, provide the recorded fictional tool responses through a controlled mock or explicitly tell the evaluator that only those responses are available. Do not contact live repositories or example destinations. Restrict tools so they cannot execute or modify the target, read secret files, or contact target services. These restrictions are independent of skill instructions.

The cases test plausible findings, benign counterexamples, prompt-injection boundaries, access failure, truncated remote retrieval, and limited-scope conclusions. Adapt the invocation to the platform only when necessary and record what was actually supplied. Never claim a score without actual recorded results.

## Structural validation

From the project root, run:

```sh
python3 scripts/validate_structure.py
python3 -m unittest discover -s tests/structure -p 'test_*.py'
```

Python 3.14 was available locally during implementation. The validator uses only the standard library, reads documentation and checks file existence, and never imports or executes fixtures. Its frontmatter check supports only simple single-line `name` and `description` fields; its Markdown link and local-path checks are deliberately limited, not general parsers. CI runs these same checks and does not run fixtures.
