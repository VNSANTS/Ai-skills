---
name: backend-architecture
description: Use for designing or reviewing backend architecture, API contracts, authentication, authorization, persistence, performance and operations
---

# Backend architecture and API engineering

## When to use
Use for designing or reviewing backend architecture, API contracts, authentication, authorization, persistence, performance and operations.

## Workflow
- Inspect existing code and constraints first.
- Map domain boundaries and data flows.
- Apply least privilege, input validation, parameterized SQL, secure secret storage and authorization at each resource boundary.
- Propose minimal changes with migrations and rollback.
- Add focused tests for authorization, tenant isolation, failure modes and observability.
- Never assume JWT validation or CORS alone enforces access control.
- Prefer established project conventions over new frameworks.

## Source and status
- Adapted from user-provided original Markdown documents: 01_BACKEND_CORE.md, 02_BACKEND_SECURITY.md, 03_BACKEND_OPS.md.
- This is a **reviewed derivative**, not a verbatim copy of internal/confidential source material.
- **Status:** draft; not functionally tested in Codex/Claude/ChatGPT.
- Verify tools, versions and official docs in the target environment before execution.
- No third-party code or dependency is bundled.
