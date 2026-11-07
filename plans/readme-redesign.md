# BeforeRun README redesign plan

## Primary goal

Give visitors a recognizable, polished BeforeRun landing page that quickly explains what the skill does, how to start, and what its review cannot guarantee. Use the supplied logo and take inspiration from Ponytail's readable visual hierarchy without copying its branding or unrelated badges.

## Phase 0 — Documentation discovery

**How this serves the primary goal:** Ground the design and every claim in the actual project and GitHub's documented rendering behavior.

### Findings and sources

- The [current README](../README.md), [installation guide](../INSTALL.md), [PRD](../docs/PRD.md), [limitations](../docs/limitations.md), [readiness report](../docs/mvp-readiness.md), and [canonical skill](../skills/beforerun/SKILL.md) are the sources of truth. The local working tree contains uncommitted changes; preserve and use them rather than assuming the remote default branch matches.
- Ponytail's [README](https://github.com/DietrichGebert/ponytail/blob/main/README.md) demonstrates a prominent identity, visual hierarchy, brief introduction, practical installation, and deeper explanations. Treat it as layout inspiration, not a source of BeforeRun features, metrics, badges, text, or artwork. The inspected page was not pinned to a commit.
- GitHub's [image and relative-link documentation](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#images) supports Markdown images with descriptive alternative text and repository-relative paths. GitHub's [image quickstart](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/quickstart-for-writing-on-github#adding-an-image-to-suit-your-visitors) describes theme-aware images and previewing. Use a single PNG unless real theme variants exist; do not invent one.
- The supplied attachment is a 1376 × 768 RGB PNG with a dark background and no alpha channel. It has been copied to the repository asset at [assets/beforerun-logo.png](../assets/beforerun-logo.png).

### Allowed patterns and guards

- Use a repository-relative Markdown image such as `![BeforeRun logo](assets/beforerun-logo.png)` and normal GitHub Markdown links. Centering with supported HTML may be considered only if the preview verifies it; plain Markdown is sufficient.
- Use only installation and invocation examples already supported by the project documentation, explaining host differences. Preserve the explicit-request rule and all safety limitations.
- Do not add a **Repository of the day** tag, other unrelated award, unsupported badge, invented usage statistic, claimed security guarantee, or unverifiable cross-agent compatibility claim.

## Phase 1 — Logo asset

**How this serves the primary goal:** Give the README a visible, consistent project identity that remains available from a GitHub checkout.

### What to implement

1. Confirm the attached image is readable and is the intended logo; preserve the original artwork and dark background unless the user approves an alternative.
2. Copy the PNG into a new repository asset path, `assets/beforerun-logo.png`, without changing the source attachment or overwriting an unrelated existing file. If the attachment is missing, stop and request it instead of substituting an image.
3. Add a descriptive-alt-text, repository-relative image near the top of the README. Keep essential project identity in text, not solely inside the image. Verify that the wide dark artwork remains readable at desktop and narrow widths.

### References

Use the [GitHub image syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#images) and the attachment facts in Phase 0.

### Verification checklist

- The repository asset exists, is a valid PNG, and matches the supplied image unless an explicitly approved transformation was made.
- The README points to the correct relative path and provides useful alt text; no inaccessible local machine path is published.

### Anti-pattern guards

Do not use the attachment's temporary absolute path as a published image URL, link to Ponytail assets, replace the logo with invented branding, or add redundant image variants.

## Phase 2 — README narrative and structure

**How this serves the primary goal:** Make the project understandable and useful within the first screen while preserving accurate expectations.

### What to implement

Restructure [README.md](../README.md) around these concise sections:

1. **Identity and promise:** logo, project name, the user's tagline “Know what you're about to run.”, and a short explanation of evidence-first static review before execution.
2. **Quick start:** an explicit install link and clear local-file and public-GitHub review examples, adapted from [INSTALL.md](../INSTALL.md). Identify host-specific invocation differences; do not imply slash commands work identically everywhere.
3. **What it checks and how it works:** a scannable list of entry points, sensitive access, network destinations, install/startup behavior, persistence, and instructions targeting agents; explain the distinction between observation, inference, and unknowns.
4. **Report example:** use the existing clearly labeled synthetic example or a similarly grounded synthetic excerpt, keeping review status and finding outcome separate.
5. **Compatibility and trust:** retain experimental/unverified host statuses, read-only intent, privacy/model-provider disclosure, explicit permission/OS-isolation limits, and the disclaimer that BeforeRun does not certify code as safe.
6. **Further reading:** short links to installation, limitations, readiness, contributing, and security reporting.

### References

Consult [README.md](../README.md), [INSTALL.md](../INSTALL.md), [target resolution](../skills/beforerun/references/target-resolution.md), [report template](../skills/beforerun/references/report-template.md), and [MVP readiness](../docs/mvp-readiness.md) immediately before drafting. Use Ponytail's hierarchy for inspiration only, not its copy or graphic assets.

### Verification checklist

- Every command, capability, status, and limitation agrees with the current project documents.
- The first screen communicates purpose and next action without crowding the page; the detailed security and compatibility caveats remain easy to find.
- Every synthetic example is labeled; its contents are not presented as an actual detection or benchmark.

### Anti-pattern guards

No “Repository of the day” tag, decorative badges copied from another repository, fictitious numbers, malware-detection guarantee, universal agent support claim, or copied Ponytail prose. No hooks, installer, global configuration change, target execution, or new scanner is part of this phase.

## Phase 3 — Verification and handoff

**How this serves the primary goal:** Ensure the refreshed page renders correctly and does not mislead users or break project documentation.

### What to implement

1. Review the final README against the sources in Phase 2 and preserve existing uncommitted user changes.
2. Check the asset, Markdown links, accessible alt text, image appearance at desktop and narrow sizes, and GitHub light/dark theme rendering. Use an actual GitHub-compatible preview when available; otherwise disclose the missing visual check rather than claiming success.
3. Run the existing structural validator and structural unit tests from [evaluation instructions](../evals/README.md), plus `git diff --check`. Independently verify the image target exists: the current validator does not validate Markdown image links.
4. Inspect the final diff for unrelated files and prohibited badges. Do not commit or push unless the user separately asks.

### Verification checklist

- PNG asset and relative image link resolve; text and controls remain readable in available previews.
- Existing validation and unit tests pass, or their actual failure and cause are reported.
- No absolute user-specific path, unrelated tag, unsupported claim, broken link, or unintended target execution appears in the final changes.

### Anti-pattern guards

Structural tests do not prove GitHub rendering or agent behavior. Do not present an unperformed preview, compatibility test, CI run, or release claim as passed.
