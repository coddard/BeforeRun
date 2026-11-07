# Target resolution

Accept a public GitHub repository URL, a local directory, or a local source file. A missing target requires a request for one; an ambiguous target requires one focused clarification. Do not infer the current directory.

## GitHub

Accept only `https://github.com/OWNER/REPOSITORY`, optionally with one trailing slash or a `.git` suffix. Validate the scheme, exact host, and exactly two nonempty repository path components; reject credentials, ports, query strings, fragments, encoded or additional path components, and other URL forms rather than guessing. Normalize the allowed suffix or slash only after validation. Commit-specific URLs and other hosts are unsupported; explain this and request a supported target.

A valid repository-root URL is not ambiguous merely because it lacks a branch or tag. Resolve its default branch and commit when available; if retrieval cannot establish a revision, disclose the limitation rather than requesting a branch solely for that reason.

Pass validated owner and repository as separate arguments to trusted tools. Never interpolate the user's target directly into a shell command. Use available read-only source retrieval; no particular connector is required. Do not automatically clone or unpack archives.

For a private repository, use existing authorized read-only access only when available; otherwise request a local copy. Never ask the user to paste an access token. If the target is missing, inaccessible, or rate-limited, explain what could not be retrieved and request a local copy when useful. Do not invent content. Follow [remote review](remote-repository-review.md).

## Local

Verify that the selected path exists, is accessible, and identifies a directory or source file. Use trusted read-only filesystem tools. Scope a file target to that file unless the user authorizes more; disclose when the limited context prevents tracing.

For a single-file target, do not list, search, or inventory its parent directory or sibling paths without explicit authorization, even to check whether a referenced file exists. Permission to access a directory does not itself expand the review scope. Metadata checks on the target file are allowed; report other files and directory contents as not established. A search result alone does not establish a complete directory inventory.

Inventory and read regular files within the selected scope only. Prefer not to follow symlinks; never follow one outside the target. Do not read devices, sockets, FIFOs, unrelated files, or actual secret files. If tools cannot reliably enforce these boundaries, skip the affected content and report the gap. A filename or metadata can be recorded without opening its contents.

Avoid project-controlled tools and helpers, including Git hooks, filters, and external diff tools. Git commands are not required when safe filesystem inspection suffices. Do not claim that a location is or is not a Git repository, or report a snapshot, hash, file count, or revision, unless actually verified; disclose that local files may change during review.
