#!/usr/bin/env python3
"""Validate the catalog's metadata snapshot without network access."""
from __future__ import annotations

from collections import Counter
from datetime import date, datetime
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REPO = re.compile(r"[A-Za-z0-9][A-Za-z0-9-]*/[A-Za-z0-9_.-]+")
VERIFIED = "metadata-verified-only"
UNVERIFIED = "unverified"


def is_slug(value: object) -> bool:
    return (isinstance(value, str) and bool(REPO.fullmatch(value))
            and value.split("/", 1)[1] not in {".", ".."})


def is_date(value: object) -> bool:
    if not isinstance(value, str):
        return False
    try:
        return date.fromisoformat(value).isoformat() == value
    except ValueError:
        return False


def is_timestamp(value: object) -> bool:
    if not isinstance(value, str) or "T" not in value:
        return False
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).utcoffset() is not None
    except ValueError:
        return False


def validate_catalog(directory: Path) -> tuple[Counter, list[str]]:
    errors = []
    counts = Counter()
    names = {}
    identities = {}

    def remember(table, key, label):
        if key in table:
            errors.append(f"{label}: duplicate {key} (also in {table[key]})")
        else:
            table[key] = label

    for path in sorted(directory.glob("*.json")):
        counts["files"] += 1
        try:
            doc = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError) as exc:
            errors.append(f"{path.name}: invalid JSON: {exc}")
            continue
        if not isinstance(doc, dict) or not isinstance(doc.get("items"), list):
            errors.append(f"{path.name}: missing items array")
            continue
        if not is_date(doc.get("snapshot")):
            errors.append(f"{path.name}: snapshot requires YYYY-MM-DD")
        for position, item in enumerate(doc["items"], 1):
            label = f"{path.name} item {position}"
            if not isinstance(item, dict):
                errors.append(f"{label}: expected an object")
                continue
            repo = item.get("repo")
            if not is_slug(repo):
                errors.append(f"{label}: invalid repo identifier")
                continue
            label = f"{label} ({repo})"
            remember(names, repo.casefold(), label)
            aliases = item.get("aliases", [])
            if not isinstance(aliases, list) or not all(is_slug(a) for a in aliases):
                errors.append(f"{label}: aliases must be a list of GitHub identifiers")
            else:
                for alias in aliases:
                    remember(names, alias.casefold(), label)
            for field in ("category", "type"):
                if not isinstance(item.get(field), str) or not item[field].strip():
                    errors.append(f"{label}: missing {field}")
            if "installed" in item and item["installed"] is not False:
                errors.append(f"{label}: installed must be false in this catalog")
            status = item.get("status")
            if status not in (VERIFIED, UNVERIFIED):
                errors.append(f"{label}: unsupported status {status!r}")
                continue
            counts[status] += 1
            if status == UNVERIFIED:
                if not isinstance(item.get("reason"), str) or not item["reason"].strip():
                    errors.append(f"{label}: unresolved identity needs a reason")
                continue
            rid = item.get("repository_id")
            if type(rid) is not int or rid <= 0:
                errors.append(f"{label}: repository_id must be a positive integer")
            else:
                remember(identities, rid, label)
            if item.get("url") != f"https://github.com/{repo}":
                errors.append(f"{label}: canonical GitHub URL mismatch")
            if type(item.get("stars")) is not int or item["stars"] < 0:
                errors.append(f"{label}: stars must be a nonnegative integer")
            if not isinstance(item.get("archived"), bool):
                errors.append(f"{label}: archived must be boolean")
            if "license" not in item or not isinstance(item["license"], (str, type(None))):
                errors.append(f"{label}: license must be a string or null")
            if not is_timestamp(item.get("pushed_at")):
                errors.append(f"{label}: pushed_at requires an ISO timestamp with timezone")
    if not counts["files"]:
        errors.append("No catalog JSON files were found")
    return counts, errors


def main() -> int:
    counts, errors = validate_catalog(ROOT / "catalog")
    print(f"Catalog: {counts['files']} files, {counts[VERIFIED]} GitHub metadata verified, "
          f"{counts[UNVERIFIED]} unresolved")
    for error in errors:
        print("ERROR:", error, file=sys.stderr)
    return int(bool(errors))


if __name__ == "__main__":
    sys.exit(main())
