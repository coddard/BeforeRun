import importlib.util
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[2] / "scripts/validate_structure.py"
SPEC = importlib.util.spec_from_file_location("validate_structure", SCRIPT)
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)


class StructureTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        for relative in validator.REQUIRED:
            file = self.root / relative
            file.parent.mkdir(parents=True, exist_ok=True)
            file.write_text("", encoding="utf-8")
        self.skill = self.root / validator.SKILL
        self.skill.write_text(
            f"---\nname: beforerun\ndescription: Review a target.\n---\n{validator.DISCLAIMER}\n",
            encoding="utf-8",
        )
        self.report = self.root / "skills/beforerun/references/report-template.md"
        headings = "\n".join(f"## {number}. {heading}" for number, heading in enumerate(validator.REPORT_HEADINGS, 1))
        self.report.write_text(f"{headings}\n{validator.DISCLAIMER}\n", encoding="utf-8")

    def test_valid_tree_and_inert_fixtures(self):
        fixture = self.root / "tests/fixtures/BR-01.fixture.md"
        fixture.write_text("raise AssertionError('must never run')\n", encoding="utf-8")
        self.assertEqual(validator.validate(self.root), [])

    def test_missing_file(self):
        (self.root / "LICENSE").unlink()
        self.assertIn("Missing required file: LICENSE", validator.validate(self.root))

    def test_skill_frontmatter_and_disclaimer(self):
        self.skill.write_text("---\nname: wrong\n---\n", encoding="utf-8")
        errors = validator.validate(self.root)
        self.assertIn("Canonical skill name must be beforerun", errors)
        self.assertIn("Skill description is missing", errors)
        self.assertTrue(any("Missing disclaimer" in error for error in errors))

    def test_link_and_absolute_local_path(self):
        (self.root / "README.md").write_text("[missing](missing.md)\n/Users/example/project\n", encoding="utf-8")
        errors = validator.validate(self.root)
        self.assertTrue(any("Broken link" in error for error in errors))
        self.assertTrue(any("Possible absolute local path" in error for error in errors))

    def test_missing_report_section(self):
        self.report.write_text(validator.DISCLAIMER, encoding="utf-8")
        self.assertTrue(any("Missing report section: Summary" in error for error in validator.validate(self.root)))


if __name__ == "__main__":
    unittest.main()
