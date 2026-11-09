#!/usr/bin/env python3
"""Offline standard-library validator for curated GitHub metadata JSON."""
from __future__ import annotations

from datetime import datetime
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "catalog"
REPO = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
ALLOWED = {"metadata-verified-only", "unverified"}


def main() -> int:
    errors: list[str] = []
    seen: dict[str, str] = {}
    verified = unresolved = 0
    sources = sorted(CATALOG.glob("*.json"))
    if not sources:
        errors.append("No catalog JSON files were found")
    for path in sources:
        try:
            doc = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError) as exc:
            errors.append(f"{path.name}: invalid JSON: {exc}")
            continue
        if not isinstance(doc, dict) or not isinstance(doc.get("items"), list):
            errors.append(f"{path.name}: missing items array")
            continue
        for pos, item in enumerate(doc["items"], 1):
            tag = f"{path.name} item {pos}"
            if not isinstance(item, dict):
                errors.append(f"{tag}: not an object")
                continue
            repo = item.get("repo")
            if not isinstance(repo, str) or not REPO.fullmatch(repo):
                errors.append(f"{tag}: invalid repo identifier")
                continue
            key = repo.casefold()
            if key in seen:
                errors.append(f"{tag}: duplicate {repo}; also in {seen[key]}")
            seen[key] = tag
            status = item.get("status")
            if status not in ALLOWED:
                errors.append(f"{tag}: unsupported status: {status!r}")
                continue
            if item.get("installed") is True:
                errors.append(f"{tag}: catalog cannot assert installation")
            if status == "unverified":
                unresolved += 1
                continue
            verified += 1
            if item.get("url") != f"https://github.com/{repo}":
                errors.append(f"{tag}: canonical GitHub URL mismatch")
            if type(item.get("stars")) is not int or item["stars"] < 0:
                errors.append(f"{tag}: stars must be nonnegative integer")
            if not isinstance(item.get("archived"), bool):
                errors.append(f"{tag}: archived must be boolean")
            if item.get("license") is not None and not isinstance(item["license"], str):
                errors.append(f"{tag}: license must be string or null")
            try:
                datetime.fromisoformat(item["pushed_at"].replace("Z", "+00:00"))
            except (KeyError, AttributeError, ValueError):
                errors.append(f"{tag}: pushed_at invalid ISO timestamp")
    print(f"Catalog: {len(sources)} files, {verified} GitHub metadata verified, {unresolved} unresolved")
    for error in errors:
        print("ERROR:", error, file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
