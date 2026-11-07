# BeforeRun MVP

**Status:** MVP implementation and evaluation in progress. This document states requirements; the [readiness report](mvp-readiness.md) records actual evidence and outstanding release work.

## Purpose

BeforeRun is a portable skill for evidence-first static review of untrusted repositories and source files before execution. Its focus is potentially intentional harmful behavior, not general code quality or comprehensive vulnerability scanning. Observations, inferences, plausible risks, and unknowns must remain distinct.

## Users and use cases

- A developer wants to examine a source file, local project, or public GitHub repository before deciding what to do with it.
- A reviewer needs a reproducible explanation of concerning and ordinary behaviors, the evidence supporting each, and what was not examined.
- A contributor needs inert scenarios and an explicit rubric to evaluate whether an agent follows the methodology without executing a target.

## User workflow

1. Install the entire skill folder, including its references, in a trusted host location; consult the host-specific installation and permission guidance.
2. Explicitly request a review with a target. If none or an ambiguous target is supplied, the agent asks rather than guessing.
3. Use trusted read-only tools to establish scope, review relevant evidence, trace relationships where possible, and stop when access or safe tooling is insufficient.
4. Receive a report with separate completion status and finding outcome, evidence and uncertainties, coverage gaps, next steps, and the disclaimer. No review result is approval to execute the target.

## Scope

The MVP consists of one canonical skill and references, local and GitHub review guidance, report and evidence conventions, documentation, harmless behavioral evaluation fixtures, lightweight structural validation, and repository CI. Platform support must be backed by official documentation and reported with its actual runtime-test status.

The MVP excludes an analysis engine, standalone scanner, hosted service, MCP server, GitHub App, dynamic target execution, target dependency installation, automated clone or archive extraction, automatic remediation, and global agent configuration changes. A deterministic engine is a possible future extension, not an MVP deliverable.

## Functional requirements

| ID | Requirement | Evidence or acceptance check |
| --- | --- | --- |
| FR-01 | Maintain one portable, manually installable canonical skill and its relative references. | Structural validation and a host-specific installation or copied-folder check; report actual host-test limitations. |
| FR-02 | Review only on explicit request; accept a local file, local directory, or supported GitHub repository root. Ask when target is missing or ambiguous. | Missing-target and explicit-target observations; do not infer a target from the working directory. |
| FR-03 | Restrict inspection to the authorized scope. Treat target content and tool descriptions as evidence, not instructions. | Manual scope and injection cases; flag unauthorized exploration and do not claim host-enforced isolation from a prompt alone. |
| FR-04 | Use trusted read-only retrieval; never require running, installing, importing, building, or modifying the target. Do not intentionally open actual secret files or probe target services. | Review method and observed tool calls; report when logs, permissions, or isolation cannot be verified. |
| FR-05 | Examine entry points, sensitive access, network and execution flows, persistence, agent-directed instructions, and other relevant categories. | Findings trace source, destination, trigger, and conditions where evidence supports them; ordinary capabilities are not automatically malicious. |
| FR-06 | Separate observations, inferences, documentation claims, plausible benign explanations, and unknowns; do not infer behavior from pseudocode alone. | Per-case evidence and context rubric, including benign counterexamples. |
| FR-07 | Report independent review status and finding outcome, examined and omitted scope, revision limitations, evidence, and recommended next steps. | Report template and coverage rubric; include the disclaimer and never assert a safety verdict. |
| FR-08 | Handle inaccessible, partial, or changing remote content without inventing files, commits, or results. | Mocked access-failure and truncation cases; a mock is not proof of live GitHub support. |
| FR-09 | Supply at least 12 inert synthetic cases, manual rubric, structural validation, and minimal CI. | Files exist, local validator and unit tests pass; disclose whether behavioral cases and hosted CI actually ran. |
| FR-10 | Document installation, host-specific status, privacy, security reporting, limitations, and removal. | Official platform documentation is checked for platform claims; runtime status is supported by recorded evidence. |

## Nonfunctional requirements

- **Safety and privacy:** Do not execute fixtures or target content. Avoid opening real secrets; redact incidental secrets and disclose that the host may transmit reviewed content to its model provider.
- **Portability:** Keep host-specific behavior outside the canonical methodology. Do not assume every agent discovers skills, interprets arguments, or enforces permissions identically.
- **Transparency:** Clearly identify partial reviews, untested paths, synthetic evidence, and inconsistent or unavailable logs. Confidence is qualitative, not a calibrated probability.
- **Maintainability:** Keep documentation and implementation aligned; run the repository's existing structural validator and tests without adding target execution or unnecessary services.

## Acceptance and release gates

The skill can be installed as a folder, requests an explicit target, handles access limitations honestly, and does not require target execution. Its report distinguishes findings from completion status and discloses evidence origins, unknowns, and omitted content without a safety verdict. At least 12 inert behavioral cases, structural validation, and minimal CI are required before MVP readiness; documentation alone does not demonstrate behavioral compliance. See [limitations](limitations.md).

Before a release-readiness claim, record actual case outcomes against the [rubric](../evals/rubrics/worksheet.md), platform and model versions, relevant access boundaries, and unresolved failures; run and inspect the hosted workflow once hosting is available. If a host, permission boundary, or integration cannot be tested, retain its experimental status rather than treating it as passed. Structural tests and prompt instructions do not establish behavioral safety.

## Dependencies and unresolved decisions

- Agent-host authentication, permission controls, model behavior, and read-only source retrieval are supplied by the host, not by BeforeRun.
- Antigravity runtime verification, a hosted GitHub Actions run, and consistently passing behavioral results on an identified revision remain outstanding and must be recorded rather than assumed. Observations across earlier revisions are listed in the readiness report.
- Detection metrics, guaranteed malware detection, universal host compatibility, and a safety certification are not MVP promises.
