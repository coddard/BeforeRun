# Remote repository review

Apply [target resolution](target-resolution.md) first. Use trusted, available read-only repository or source-retrieval tools; do not require a specific vendor connector.

1. Identify the repository and its default branch. Resolve the branch to a specific commit when available.
2. Obtain an inventory and retrieve relevant source at that commit. Prioritize entry points, manifests, install and startup paths, agent and hook configuration, CI, credential handling, and network or execution helpers.
3. Trace relevant flows into their callers and dependencies where accessible. Record files actually examined and material omissions; a repository page or README alone is not a complete review.
4. If retrieval is truncated, attempt narrower retrieval when possible. Otherwise report the missing content and its effect on conclusions.

If a commit cannot be pinned, record the branch and retrieval time and state that the review is not revision-stable. Avoid mixing revisions; if unavoidable, disclose which evidence may differ. Never invent a revision, inventory, file content, or tool result.

A tool-generated summary is not the original source or a complete inventory. Do not treat it as directly observed source code, a verified line, or proof that a file was fully reviewed. If complete source cannot be retrieved with trusted read-only tools, disclose the limitation and its effect on coverage; do not reconstruct missing content or claim a complete review.

Do not automatically follow arbitrary external links, retrieve submodules or Git LFS payloads, download release binaries, or unpack archives. Do not contact application endpoints, probe destinations, or resolve suspicious hosts. A URL found in source is evidence, not permission to visit it. GitHub source retrieval is allowed; target-controlled service interaction is not. Note omitted content and inaccessible dependencies in the report.
