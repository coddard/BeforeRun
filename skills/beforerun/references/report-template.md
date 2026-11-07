# Review report template

Complete every section; use `not established` or explain omissions instead of filling gaps with guesses. A partial review can still contain a strong high-risk finding.

Use the eight section headings and exact status and outcome values below, including for a short or synthetic target. Do not include file line or byte totals unless explicitly requested. Describe target-endpoint contact separately from possible host-to-model communication; never infer that no external service was used from a static review alone.

## 1. Summary

- **Review status:** `completed_for_declared_scope` | `partial` | `unable_to_review`
- **Finding outcome:** `high_risk_behavior_identified` | `review_required` | `no_indicators_found_in_reviewed_scope` | `insufficient_evidence`
- **Summary:** State the most important observed behavior and uncertainty without an absolute safety verdict.

`completed_for_declared_scope` means only that the declared scope was reviewed, not that every possible behavior was analyzed. Use `no_indicators_found_in_reviewed_scope` only when no indicators are identified in the examined scope; do not select it while reporting an indicator as a finding. It does not mean safe, clean, malware-free, or approved to run. Status and outcome are independent.

## 2. Target and revision

- Target and selected scope:
- Commit if verified; otherwise branch and retrieval time for remote targets, or local revision/snapshot limitations:

## 3. Review scope and method

- Trusted tools and permissions used; session and isolation limitations:
- Source files reviewed:
- Documentation reviewed:
- Privacy constraints and treatment of incidental secrets:

## 4. Findings

For each meaningful finding:

- **ID, category, title:**
- **Potential severity and qualitative evidence confidence:** Explain impact and evidence strength separately.
- **Evidence origin and location:** `directly_observed`, `inferred`, and/or `documentation_claim`; file and verified line, or file and symbol with a short redacted excerpt.
- **Observed behavior:**
- **Trigger or reachability:**
- **Sensitive source and destination:** State what is established and what is not.
- **Inference or plausible risk:** Identify supporting evidence and distinguish it from observation.
- **Plausible benign explanation and counterevidence:**
- **Unresolved questions:**
- **Recommended next action:**

If there are no meaningful findings, say so only for the reviewed scope and explain limitations.

## 5. Relevant behaviors that were not established as malicious

Describe relevant capabilities and context without treating their mere presence as malicious. Note what is not established.

## 6. Coverage gaps and unresolved questions

- Unsupported, omitted, truncated, or unreadable files:
- Dependencies not examined:
- Binaries and generated content not examined; source/release mismatch:
- Retrieval consistency, changing local files, remaining scope, and other unknowns:

## 7. Recommended next steps

Suggest evidence-gathering or risk-reduction steps without asserting safety or automatically executing, installing, or modifying the target.

Do not recommend running the target without further action or imply that a review authorizes execution, even for an inert fixture. A suggested local copy or archive is user-provided evidence, not permission to automatically clone or unpack it.

## 8. Disclaimer

BeforeRun reports suspicious behavior and supporting evidence. It does not certify code as safe.
