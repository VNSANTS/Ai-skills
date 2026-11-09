---
name: secure-tool-adoption
description: Evaluate proposed agent skills, MCP servers, hooks and tools before installation, with license, security, permission and zero-cost gates.
---

# Secure tool adoption

For each proposed integration:

1. Pin canonical repository and version; inspect LICENSE, provenance and changelog.
2. Read every executable entry point, install step, hook, SKILL.md and MCP server configuration.
3. Assess permissions, outbound requests, secret handling, telemetry and potential persistence.
4. Confirm target platform and runtime, and whether services require subscriptions or provider keys.
5. Test isolated with synthetic data, record commands and outcomes, estimate rollback.
6. Ask for explicit approval before global installation, credentials, paid services or production changes.
7. Never mark a tool secure or tested based solely on stars or GitHub license metadata.

No installations are performed by this Skill itself.
