#!/usr/bin/env python3
"""Validate BeforeRun's repository structure without executing fixtures."""

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parent.parent
SKILL = Path("skills/beforerun/SKILL.md")
REFERENCES = (
    "target-resolution.md",
    "remote-repository-review.md",
    "threat-model.md",
    "review-workflow.md",
    "behavior-patterns.md",
    "evidence-and-confidence.md",
    "report-template.md",
)
REQUIRED = (
    "README.md", "INSTALL.md", "LICENSE", "SECURITY.md", "CONTRIBUTING.md",
    "CHANGELOG.md", "AGENTS.md", "docs/PRD.md", "docs/limitations.md",
    "docs/methodology-sources.md", "docs/integrations/claude-code.md",
    "docs/integrations/antigravity.md", "evals/README.md", "evals/cases/cases.md",
    "evals/rubrics/worksheet.md", "scripts/validate_structure.py",
    "tests/structure/test_validate_structure.py", ".github/workflows/validate.yml",
    str(SKILL), *(f"skills/beforerun/references/{name}" for name in REFERENCES),
    *(f"tests/fixtures/BR-{number:02}.fixture.md" for number in range(1, 13)),
)
DISCLAIMER = "BeforeRun reports suspicious behavior and supporting evidence. It does not certify code as safe."
REPORT_HEADINGS = (
    "Summary", "Target and revision", "Review scope and method", "Findings",
    "Relevant behaviors that were not established as malicious",
    "Coverage gaps and unresolved questions", "Recommended next steps", "Disclaimer",
)
LINK = re.compile(r"(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)")
LOCAL_PATH = re.compile(r"(?:/Users/[^/\s`]+|/home/[^/\s`]+|/private/var/|[A-Za-z]:[\\/]Users[\\/][^\\/\s`]+)")


def validate(root: Path) -> list[str]:
    errors = []
    for relative in REQUIRED:
        if not (root / relative).is_file():
            errors.append(f"Missing required file: {relative}")

    skill_path = root / SKILL
    if skill_path.is_file():
        text = skill_path.read_text(encoding="utf-8")
        parts = text.split("---\n", 2)
        if len(parts) != 3 or parts[0] != "":
            errors.append(f"Invalid simple frontmatter: {SKILL}")
        else:
            fields = dict(re.findall(r"^([a-z][a-z-]*):\s*(\S[^\n]*)$", parts[1], re.MULTILINE))
            if fields.get("name") != "beforerun":
                errors.append("Canonical skill name must be beforerun")
            if not fields.get("description"):
                errors.append("Skill description is missing")
        if DISCLAIMER not in text:
            errors.append(f"Missing disclaimer: {SKILL}")

    report_path = root / "skills/beforerun/references/report-template.md"
    if report_path.is_file():
        report = report_path.read_text(encoding="utf-8")
        if DISCLAIMER not in report:
            errors.append("Missing report disclaimer")
        for number, heading in enumerate(REPORT_HEADINGS, 1):
            if f"## {number}. {heading}" not in report.splitlines():
                errors.append(f"Missing report section: {heading}")

    for folder in (root, root / "docs", root / "skills", root / "evals"):
        if not folder.exists():
            continue
        files = folder.glob("*.md") if folder == root else folder.rglob("*.md")
        for file in files:
            text = file.read_text(encoding="utf-8")
            if LOCAL_PATH.search(text):
                errors.append(f"Possible absolute local path: {file.relative_to(root)}")
            for match in LINK.finditer(text):
                target = match.group(1).strip()
                parsed = urlsplit(target)
                if parsed.scheme or parsed.netloc or not parsed.path:
                    continue
                if parsed.path.startswith("/"):
                    errors.append(f"Absolute Markdown link in {file.relative_to(root)}: {target}")
                elif not (file.parent / unquote(parsed.path)).exists():
                    errors.append(f"Broken link in {file.relative_to(root)}: {target}")
    return errors


def main() -> int:
    errors = validate(ROOT)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Structure validation passed (fixtures were not executed; behavior was not evaluated).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
