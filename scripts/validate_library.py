#!/usr/bin/env python3
"""Check local Markdown links, Agent Skills frontmatter and both discovery indexes."""
from __future__ import annotations

from dataclasses import dataclass, field
import json
import os
from pathlib import Path
import re
import sys
import unicodedata
from urllib.parse import unquote, urlsplit

from markdown_it import MarkdownIt
import yaml

ROOT = Path(__file__).resolve().parents[1]
MARKDOWN = MarkdownIt("commonmark").enable("table")
SKILL_NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")


@dataclass
class Page:
    links: list[str] = field(default_factory=list)
    anchors: set[str] = field(default_factory=set)


def parse_page(body: str) -> Page:
    page = Page()
    heading = False
    for token in MARKDOWN.parse(body):
        if token.type == "heading_open":
            heading = True
        elif token.type == "heading_close":
            heading = False
        if token.type != "inline":
            continue
        children = token.children or []
        if heading:
            title = "".join(c.content for c in children if c.type in ("text", "code_inline"))
            slug = "".join(ch for ch in title.strip().lower()
                           if ch in "-_ " or unicodedata.category(ch)[0] in "LNM").replace(" ", "-")
            anchor = slug
            suffix = 0
            while anchor in page.anchors:
                suffix += 1
                anchor = f"{slug}-{suffix}"
            page.anchors.add(anchor)
        for child in children:
            if child.type in ("link_open", "image"):
                page.links.append(child.attrs["href" if child.type == "link_open" else "src"])
    return page


def skill_body(path: Path, text: str, errors: list[str]) -> str:
    lines = text.splitlines()
    if not lines or lines[0] != "---" or "---" not in lines[1:]:
        errors.append(f"{path}: missing YAML frontmatter delimiters")
        return ""
    end = lines.index("---", 1)
    front = "\n".join(lines[1:end])
    body = "\n".join(lines[end + 1:])
    try:
        meta = yaml.safe_load(front)
        if not isinstance(meta, dict):
            raise ValueError("expected a YAML mapping")
        node = yaml.compose(front, Loader=yaml.SafeLoader)
        keys = [key.value for key, _ in node.value]
        if len(keys) != len(set(keys)):
            raise ValueError("duplicate YAML keys")
    except (yaml.YAMLError, ValueError, TypeError) as exc:
        errors.append(f"{path}: invalid YAML: {exc}")
        return body
    name = meta.get("name")
    if (not isinstance(name, str) or not SKILL_NAME.fullmatch(name)
            or len(name) > 64 or name != path.parent.name):
        errors.append(f"{path}: invalid skill name or folder mismatch")
    description = meta.get("description")
    if not isinstance(description, str) or not description.strip() or len(description) > 1024:
        errors.append(f"{path}: description requires 1–1024 characters")
    if not body.strip():
        errors.append(f"{path}: missing instructions")
    return body


def first_party_pages(root: Path):
    for directory, dirs, files in os.walk(root):
        here = Path(directory)
        # Imported source trees have their own conventions. The local repositories/README.md is ours.
        if here == root / "repositories":
            dirs.clear()
        else:
            dirs[:] = sorted(d for d in dirs if not d.startswith(".") or d == ".github")
        for name in sorted(files):
            if name.endswith(".md"):
                yield here / name


def validate_library(root: Path) -> tuple[dict, list[str]]:
    root = root.resolve()
    errors = []
    pages = {}
    skills = set()
    for directory in sorted((root / "skills").glob("*/")):
        if directory.is_dir() and not directory.name.startswith("."):
            skill = directory / "SKILL.md"
            if not skill.is_file():
                errors.append(f"{skill.relative_to(root)}: missing SKILL.md")
            else:
                skills.add(skill)
    if not skills:
        errors.append("No first-party skills found")

    for path in first_party_pages(root):
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"{path.relative_to(root)}: {exc}")
            continue
        if path in skills:
            text = skill_body(path.relative_to(root), text, errors)
        pages[path] = parse_page(text)

    skill_index = root / "skills/README.md"
    catalog_index = root / "INDEX.md"
    for index in (skill_index, catalog_index):
        if index not in pages:
            errors.append(f"{index.relative_to(root)}: missing index")

    indexed_skills = set()
    indexed_catalogs = set()
    indexed_urls = set()
    local_links = 0
    for path, page in pages.items():
        label = path.relative_to(root)
        for link in page.links:
            try:
                url = urlsplit(link)
            except ValueError:
                errors.append(f"{label}: invalid link {link}")
                continue
            if url.scheme or url.netloc:
                if path == catalog_index:
                    indexed_urls.add(link.rstrip("/").casefold())
                continue
            local_links += 1
            target = (path.parent / unquote(url.path)).resolve() if url.path else path
            if not target.is_relative_to(root) or not target.exists():
                errors.append(f"{label}: missing or out-of-tree target {link}")
                continue
            if path == skill_index:
                indexed_skills.add(target)
            if path == catalog_index:
                indexed_catalogs.add(target)
            if url.fragment:
                linked_page = target / "README.md" if target.is_dir() else target
                if linked_page in pages and unquote(url.fragment) not in pages[linked_page].anchors:
                    errors.append(f"{label}: unknown heading in {link}")
    for skill in sorted(skills - indexed_skills):
        errors.append(f"skills/README.md: missing {skill.relative_to(root)}")
    for file in sorted((root / "catalog").glob("*.json")):
        if file not in indexed_catalogs:
            errors.append(f"INDEX.md: missing {file.relative_to(root)}")
        try:
            catalog = json.loads(file.read_text(encoding="utf-8"))
        except (ValueError, OSError) as exc:
            errors.append(f"{file.relative_to(root)}: {exc}")
            continue
        if not isinstance(catalog, dict) or not isinstance(catalog.get("items"), list):
            errors.append(f"{file.relative_to(root)}: missing items array")
            continue
        for item in catalog["items"]:
            if isinstance(item, dict) and item.get("status") == "metadata-verified-only":
                url = item.get("url")
                if not isinstance(url, str) or url.casefold() not in indexed_urls:
                    errors.append(f"INDEX.md: missing catalog URL {url}")
    return {"skills": len(skills), "pages": len(pages), "links": local_links}, errors


def main() -> int:
    counts, errors = validate_library(ROOT)
    print("Library: {skills} skills, {pages} Markdown files, {links} local links".format(**counts))
    for error in errors:
        print("ERROR:", error, file=sys.stderr)
    return int(bool(errors))


if __name__ == "__main__":
    sys.exit(main())
