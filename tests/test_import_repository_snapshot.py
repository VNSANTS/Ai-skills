"""Exercise the shipped importer with disposable local Git repositories, offline."""
import os
from pathlib import Path
import subprocess
import tempfile
import unittest


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
if os.name == "nt":
    ENTRY = ["powershell.exe", "-NoProfile", "-NonInteractive", "-ExecutionPolicy", "Bypass",
             "-File", str(SCRIPTS / "import-repository-snapshot.ps1")]
else:
    ENTRY = ["bash", str(SCRIPTS / "import-repository-snapshot.sh")]

MANIFEST = "NEXUS_BACKUP_MANIFEST.md"


class SnapshotTests(unittest.TestCase):
    def setUp(self):
        scratch = tempfile.TemporaryDirectory(prefix="snapshot tests ")
        self.addCleanup(scratch.cleanup)
        self.root = Path(scratch.name)
        self.source = self.root / "source with spaces"
        self.receiver = self.root / "receiving repo"
        self.target = self.receiver / "repositories" / "demo"
        self.env = {
            **os.environ, "GIT_CONFIG_NOSYSTEM": "1",
            "GIT_CONFIG_GLOBAL": str(self.root / "gitconfig"),
            "GIT_ALLOW_PROTOCOL": "file", "GIT_TERMINAL_PROMPT": "0",
            "GIT_AUTHOR_NAME": "Fixture", "GIT_AUTHOR_EMAIL": "fixture@example.invalid",
            "GIT_COMMITTER_NAME": "Fixture", "GIT_COMMITTER_EMAIL": "fixture@example.invalid",
            "GIT_AUTHOR_DATE": "2000-01-01T00:00:00Z", "GIT_COMMITTER_DATE": "2000-01-01T00:00:00Z",
        }
        for name in ("GIT_DIR", "GIT_COMMON_DIR", "GIT_INDEX_FILE", "GIT_WORK_TREE", "BASH_ENV"):
            self.env.pop(name, None)
        for repo in (self.source, self.receiver):
            repo.mkdir()
            self.git("init", "-q", "-b", "main", cwd=repo)
            self.git("config", "core.autocrlf", "false", cwd=repo)
        self.git("commit", "--allow-empty", "-qm", "initial")

    def git(self, *args, cwd=None, data=None):
        return subprocess.run(["git", *args], cwd=cwd or self.source, env=self.env, input=data,
                              capture_output=True, check=True, timeout=60).stdout

    def commit(self, files):
        for relative, content in files.items():
            path = self.source / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(content)
        self.git("add", "-f", "--", ".")
        self.git("commit", "-qm", "fixture")

    def start(self, destination="repositories/demo", *, source=None, branch="main", cwd=None, env=None):
        source = str(self.source) if source is None else source
        args = (["-Source", source, "-Branch", branch, "-Destination", destination]
                if os.name == "nt" else [source, branch, destination])
        return subprocess.Popen([*ENTRY, *args], cwd=cwd or self.receiver, env=env or self.env,
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    def result(self, process):
        try:
            output = process.communicate(timeout=60)[0].decode("utf-8", errors="replace")
        except subprocess.TimeoutExpired:
            process.kill()
            process.communicate()
            raise
        return process.returncode, output

    def run_import(self, **kwargs):
        return self.result(self.start(**kwargs))

    def assert_rejected(self, expected, **kwargs):
        code, output = self.run_import(**kwargs)
        self.assertNotEqual(code, 0, output)
        self.assertIn(expected, output)
        self.assertFalse(self.target.exists())
        self.assertEqual(list(self.receiver.rglob(".nexus-snapshot.*")), [])

    def test_selected_branch_has_exact_tracked_bytes_and_provenance(self):
        self.git("switch", "-qc", "selected")
        files = {
            ".gitattributes": (b"keep export-ignore\nformat export-subst\nident ident\n"
                               b"eol text eol=crlf\n"),
            ".gitignore": b"ignored\n",
            "keep": b"retained",
            "format": b"$Format:%H$",
            "ident": b"$Id$\n",
            "eol": b"one\ntwo\n",
            "nested/caf\u00e9 [1].bin": bytes(range(256)),
            "empty": b"",
        }
        self.commit(files)
        self.git("update-index", "--chmod=+x", "--", "keep")
        self.git("commit", "-qm", "executable mode")
        selected = self.git("rev-parse", "HEAD").decode().strip()
        (self.source / "ignored").write_bytes(b"untracked")
        (self.source / "untracked").write_bytes(b"also absent")
        self.git("config", "--global", "core.autocrlf", "true")
        nested = self.receiver / "subdir"
        nested.mkdir()
        source_argument = os.path.relpath(self.source, nested)
        code, output = self.run_import(branch="selected", source=source_argument, cwd=nested)
        self.assertEqual(code, 0, output)
        self.assertEqual({p.relative_to(self.target).as_posix() for p in self.target.rglob("*")
                          if p.is_file()}, set(files) | {MANIFEST})
        self.assertFalse((self.target / ".git").exists())
        for name in files:
            self.assertEqual((self.target / name).read_bytes(), self.git("show", f"{selected}:{name}"))
        if os.name != "nt":
            self.assertTrue(os.access(self.target / "keep", os.X_OK))
        record = (self.target / MANIFEST).read_text(encoding="utf-8-sig").splitlines()
        for line in (f"Source: {source_argument}", "Branch: selected", f"Source commit: {selected}",
                     f"Tracked files copied: {len(files)}"):
            self.assertIn(line, record)

    def test_empty_commit_and_repeat_preserve_existing_destination(self):
        code, output = self.run_import()
        self.assertEqual(code, 0, output)
        self.assertEqual([p.name for p in self.target.iterdir()], [MANIFEST])
        record = (self.target / MANIFEST).read_bytes()
        self.assertIn(b"Tracked files copied: 0", record)
        (self.target / "sentinel").write_bytes(b"keep me")
        self.commit({"new-file": b"new upstream state"})
        code, output = self.run_import()
        self.assertNotEqual(code, 0, output)
        self.assertEqual((self.target / MANIFEST).read_bytes(), record)
        self.assertEqual((self.target / "sentinel").read_bytes(), b"keep me")
        self.assertFalse((self.target / "new-file").exists())

    def test_failed_clone_cleans_new_parents_and_can_be_retried(self):
        destination = "repositories/group/demo"
        self.assert_rejected("Clone failed", destination=destination, branch="missing")
        self.assertFalse((self.receiver / "repositories").exists())
        code, output = self.run_import(destination=destination + "/")
        self.assertEqual(code, 0, output)
        self.assertTrue((self.receiver / destination / MANIFEST).is_file())

    def test_reserved_source_manifest_file_and_directory(self):
        collision = MANIFEST.lower()
        self.commit({collision: b"original upstream file"})
        self.assert_rejected("reserved manifest")
        (self.source / collision).unlink()
        self.commit({collision + "/nested.txt": b"also reserved"})
        self.assert_rejected("reserved manifest")

    def test_gitlinks_and_symbolic_links_fail_before_publication(self):
        commit = self.git("rev-parse", "HEAD").decode().strip()
        self.git("update-index", "--add", "--cacheinfo", f"160000,{commit},module")
        self.git("commit", "-qm", "gitlink")
        self.assert_rejected("submodule")
        self.git("update-index", "--force-remove", "module")
        link_blob = self.git("hash-object", "-w", "--stdin", data=b"relative.txt").decode().strip()
        self.git("update-index", "--add", "--cacheinfo", f"120000,{link_blob},link")
        self.git("commit", "-qm", "symbolic link")
        self.assert_rejected("symbolic link")

    def test_lfs_pointer_is_rejected_even_without_attributes(self):
        pointer = b"version https://git-lfs.github.com/spec/v1\noid sha256:" + b"0" * 64 + b"\nsize 25\n"
        self.commit({"nested/data.bin": pointer})
        self.assert_rejected("Git LFS pointer")
        self.assertFalse((self.receiver / "repositories").exists())
        self.commit({"nested/data.bin": b"documentation\n" + pointer})
        code, output = self.run_import()
        self.assertEqual(code, 0, output)

    def test_invalid_destinations_and_working_directory(self):
        for destination in ("other/demo", "repositories/../outside", "repositories/.git/hidden",
                            "repositories/.", "repositories/a//b", "repositories/item.",
                            "repositories/con.txt", "repositories/"):
            with self.subTest(destination=destination):
                self.assert_rejected("destination", destination=destination)
        self.assert_rejected("receiving Git clone", cwd=self.root)
        self.assertFalse((self.receiver / "repositories").exists())

    def test_linked_destination_cannot_leave_receiver(self):
        outside = self.root / "outside"
        outside.mkdir()
        link = self.receiver / "repositories"
        if os.name == "nt":
            subprocess.run(["cmd.exe", "/d", "/c", "mklink", "/J", str(link), str(outside)],
                           capture_output=True, check=True, timeout=30)
        else:
            link.symlink_to(outside, target_is_directory=True)
        self.assert_rejected("filesystem link")
        self.assertEqual(list(outside.iterdir()), [])

    def test_verifier_rejects_changed_checkout_bytes(self):
        self.commit({"payload.bin": b"original"})
        # Change a staged file after Git's checkout and before verification, without editing the importer.
        startup = self.root / "simulate-io-failure.bash"
        startup.write_text(
            'git() {\n'
            '    local arg previous="" tree="" checkout=no\n'
            '    for arg; do\n'
            '        if [[ $previous == -C ]]; then tree=$arg; fi\n'
            '        if [[ $arg == read-tree ]]; then checkout=yes; fi\n'
            '        previous=$arg\n'
            '    done\n'
            '    command git "$@" || return $?\n'
            '    if [[ $checkout == yes ]]; then printf changed > "$tree/payload.bin"; fi\n'
            '}\n', encoding="ascii",
        )
        self.assert_rejected("differs from the source tree",
                             env={**self.env, "BASH_ENV": startup.as_posix()})
        self.assertFalse((self.receiver / "repositories").exists())

    def test_concurrent_import_publishes_once(self):
        self.commit({"payload": b"identical"})
        processes = [self.start() for _ in range(2)]
        results = [self.result(process) for process in processes]
        self.assertEqual(sorted(code == 0 for code, _ in results), [False, True], results)
        self.assertEqual({path.name for path in self.target.iterdir()}, {"payload", MANIFEST})
        self.assertEqual((self.target / "payload").read_bytes(), b"identical")
        self.assertEqual(list(self.receiver.rglob(".nexus-snapshot.*")), [])


if __name__ == "__main__":
    unittest.main()
