import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from scripts.validate_catalog import validate_catalog
from scripts.validate_library import parse_page, validate_library


class CatalogTest(unittest.TestCase):
    def setUp(self):
        tmp = TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.directory = Path(tmp.name)
        self.entry = {
            "repo": "Example/Guide", "repository_id": 371, "aliases": ["Old/Guide"],
            "url": "https://github.com/Example/Guide", "category": "Docs", "type": "tool",
            "status": "metadata-verified-only", "installed": False, "stars": 0,
            "license": None, "archived": False, "pushed_at": "2026-11-03T09:00:00Z"
        }

    def check(self, entries, date="2026-11-25"):
        (self.directory / "list.json").write_text(
            json.dumps({"snapshot": date, "items": entries}), encoding="utf-8")
        return validate_catalog(self.directory)[1]

    def test_valid_metadata_and_unverified_name(self):
        unknown = {"repo": "Other/Guide", "status": "unverified", "reason": "HTTP 404",
                   "type": "tool", "category": "Docs"}
        self.assertEqual(self.check([self.entry, unknown]), [])

    def test_malformed_values_return_diagnostics(self):
        for key, value in [("stars", True), ("installed", "false"), ("status", []),
                           ("pushed_at", "2026-11-25"), ("pushed_at", "2026-11-25T10:00:00"),
                           ("category", ""), ("repository_id", False), ("aliases", "Old/Name")]:
            with self.subTest(key=key, value=value):
                self.assertTrue(self.check([{**self.entry, key: value}]))
        self.assertTrue(self.check([self.entry], "2026-02-31"))
        self.assertTrue(self.check([{**self.entry, "status": "unverified", "reason": "  "}]))

    def test_id_alias_and_canonical_name_are_unique(self):
        second = {**self.entry, "repo": "New/Guide", "url": "https://github.com/New/Guide",
                  "aliases": []}
        self.assertTrue(any("duplicate 371" in e for e in self.check([self.entry, second])))
        second.update(repository_id=900, aliases=["example/guide"])
        self.assertTrue(any("duplicate example/guide" in e for e in self.check([self.entry, second])))


class LibraryTest(unittest.TestCase):
    def setUp(self):
        tmp = TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)
        self.skill = self.root / "skills/demo/SKILL.md"
        self.skill.parent.mkdir(parents=True)
        self.source = "---\nname: demo\ndescription: |\n  Review a demo project.\n---\n# Aplicação\n"
        self.skill.write_text(self.source, encoding="utf-8")
        (self.root / "skills/README.md").write_text("[Demo](demo/SKILL.md#aplicação)\n", encoding="utf-8")
        (self.root / "INDEX.md").write_text("# Recursos\n", encoding="utf-8")

    def errors(self):
        return validate_library(self.root)[1]

    def test_valid_standalone_skill_and_unicode_fragment(self):
        self.assertEqual(self.errors(), [])

    def test_yaml_errors_and_missing_body(self):
        for invalid in [self.source.replace("name: demo", "name: Other"),
                        self.source.replace("name: demo", "name: demo\nname: demo"),
                        self.source.replace("Review a demo project.", "a" * 1025),
                        self.source.replace("description: |", "description: ["),
                        self.source.replace("# Aplicação", "")]:
            with self.subTest(sample=invalid[:48]):
                self.skill.write_text(invalid, encoding="utf-8")
                self.assertTrue(any("SKILL.md:" in e for e in self.errors()))

    def test_missing_link_heading_and_unlisted_skill(self):
        (self.root / "skills/README.md").write_text("[Unknown](missing.md)\n", encoding="utf-8")
        self.skill.write_text(self.source + "[Heading](#outro)\n", encoding="utf-8")
        report = "\n".join(self.errors())
        self.assertIn("missing.md", report)
        self.assertIn("#outro", report)
        self.assertIn("missing skills/demo/SKILL.md", report)

    def test_reference_links_and_code_examples(self):
        page = parse_page("# Uso\n# Uso\n[exemplo][r]\n\n[r]: ../guia.md\n\n"
                          + chr(96) * 3 + "\n[x](ignorar.md)\n" + chr(96) * 3)
        self.assertEqual(page.links, ["../guia.md"])
        self.assertEqual(page.anchors, {"uso", "uso-1"})

    def test_imported_snapshots_are_outside_validation(self):
        external = self.root / "repositories/source"
        external.mkdir(parents=True)
        (external / "README.md").write_text("[external](missing.md)", encoding="utf-8")
        self.assertEqual(self.errors(), [])

    def test_dependency_directories_do_not_contribute_pages(self):
        for name in ("node_modules", "venv"):
            directory = self.root / name
            directory.mkdir()
            (directory / "README.md").write_text("[dependency](missing.md)", encoding="utf-8")
        (self.root / "venv/pyvenv.cfg").touch()
        self.assertEqual(self.errors(), [])

    def test_verified_projects_and_catalog_files_are_discoverable(self):
        directory = self.root / "catalog"
        directory.mkdir()
        url = "https://github.com/Example/Guide"
        (directory / "list.json").write_text(json.dumps(
            {"items": [{"status": "metadata-verified-only", "url": url}]}), encoding="utf-8")
        self.assertEqual(len(self.errors()), 2)
        (self.root / "INDEX.md").write_text(f"[Lista](catalog/list.json) [Guia]({url})", encoding="utf-8")
        self.assertEqual(self.errors(), [])
