# Evidence and confidence

For each meaningful finding provide a finding ID, category, concise title, potential severity, qualitative evidence confidence, evidence origin, file and location, observed behavior, trigger or reachability, established sensitive source and destination, plausible benign explanation, unresolved questions, and recommended next action. Use `not established` where evidence is missing.

Severity describes potential impact, not certainty. Confidence describes the strength of the evidence, not a calibrated probability. Explain both rather than inventing numerical scores.

Label evidence and conclusions by origin:

- `directly_observed`: behavior or text actually present in retrieved content.
- `inferred`: a relationship or consequence reasoned from the observed evidence, including cross-file inference; identify the supporting observations and uncertainties.
- `documentation_claim`: what documentation says, without treating it as proof of implementation.

Separate observed code behavior from inferred relationships, plausible risks, and unknowns. A source-to-sink relationship is confirmed only when reviewed code supports the connection. A source or sink alone does not prove transfer. Documentation alone cannot establish that data stays local or a demo mode avoids sensitive operations. Do not claim intent with certainty.

Copy reported paths, filenames, identifiers, and short excerpts exactly from the inspected evidence; if they cannot be verified, say so instead of reconstructing them. Do not assert that a remote destination is attacker-controlled without supporting evidence; describe that possibility as conditional risk when appropriate.

Treat pseudocode, signatures, and examples as descriptions, not implementations. Do not assert their runtime behavior, side effects, or return values without supporting implementation evidence; state what the text depicts and what remains unknown.

Limit absence claims to the scope actually inventoried or inspected. A reference to a file in a single-file target does not establish whether that file exists elsewhere. Do not make categorical claims that a target has no risk; describe the observed content and the limits of the review instead.

Use exact line numbers only when the tool supplied or verified them. Otherwise cite the path and function or symbol, with a short redacted excerpt when useful. Omit file line and byte totals unless the user explicitly requests them. If requested, report totals only when measured with a trusted tool, specify the method, and otherwise say they are not established; do not estimate them from memory or visual inspection. Never invent files, lines, commits, API calls, dependency results, or test outcomes. If a sensitive value appears, omit it from the report and further tool inputs.

Do not claim that no endpoint, network access, or external service was used merely because no target endpoint was contacted. The host may communicate with a model provider or other services; describe only the specific access observed, and say when broader communication is not established.
