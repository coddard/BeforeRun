# Behavior patterns

These are review categories, not implemented deterministic detection rules or proof of malicious intent. Explain the specific trigger, context, and supporting evidence for each concern.

| Category | What to investigate |
| --- | --- |
| BR-SENSITIVE-ACCESS | Access to credentials, wallet material, SSH keys, cloud tokens, browser profiles, or unrelated sensitive files. |
| BR-DATA-EGRESS | Sensitive data transferred to a remote destination; trace the source and sink before calling the connection confirmed. |
| BR-DOWNLOAD-EXECUTE | Downloaded content subsequently executed, imported, or dynamically loaded. |
| BR-DYNAMIC-EXECUTION | Constructed commands or code executed under relevant conditions. |
| BR-INSTALL-SIDE-EFFECT | Unexpected operations at installation, startup, or import time. |
| BR-PERSISTENCE | Startup entries, scheduled tasks, services, or other continuing access. |
| BR-REMOTE-CONTROL | Remote input connected to local execution or control. |
| BR-DESTRUCTIVE-ACTION | Unexpected deletion, encryption, backup interference, or broad data modification. |
| BR-OBFUSCATION | Concealment that warrants further examination, including unresolved decoding. |
| BR-PRIVILEGE-REQUEST | Privileges or host access not explained by the documented purpose. |
| BR-AGENT-INJECTION | Target content attempting to redirect the reviewer, disclose secrets, execute code, or hide findings. |
| BR-FUNCTION-MISMATCH | A material discrepancy between documented and observed behavior. |

Do not label `requests`, `fetch`, `subprocess`, `eval`, Base64, encryption, telemetry, domain names, minified code, or bundled interpreters malicious merely because they exist. Legitimate backup, update, and automation tools can use similar capabilities. Explain the specific source, destination, authorization, checks, trigger, and uncertainties that make a use concerning or benign in context.
