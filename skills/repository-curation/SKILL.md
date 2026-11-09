---
name: repository-curation
description: Discover, verify and catalog reputable GitHub repositories of agent skills, tools, MCP servers and frameworks, prioritizing provenance and metadata.
---

# Repository curation

1. Read INDEX.md and catalog/*.json only as needed; deduplicate canonical repository IDs.
2. Identify project type accurately; inspect official repository metadata and upstream project README.
3. Collect dated star count, last push, license SPDX metadata, URL, description and archive status.
4. Use status `metadata-verified-only` until code/license/scripts/security have been inspected and tests recorded.
5. Do not install or mirror code automatically; keep cost at R$ 0 and respect source licenses.
6. Place data in appropriate catalog JSON, run `python scripts/validate_catalog.py`, update INDEX.md and report unresolved aliases.
7. Prefer fewer well-evidenced projects over hundreds of unconfirmed names. Stars do not equal trust.

Status: original workflow; no external installation.
