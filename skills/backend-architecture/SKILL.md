---
name: backend-architecture
description: Design or review backend architecture, API contracts, request authorization, persistence, and operational behavior. Use for new endpoints, contract changes, multi-tenant APIs, and reliability reviews.
---

# Backend architecture and API engineering

## Workflow

1. Inspect existing routes, callers, storage constraints, and deployment requirements. Map the request path from identity and tenant selection to the database and external services.
2. Specify inputs, outputs, error responses, and compatibility with existing clients. Validate input at the boundary, use parameterized queries, and derive resource authorization from trusted identity and ownership. Check access wherever a resource is read or changed.
3. Trace failures and retries for writes. Enforce invariants with constraints or transactions, and define idempotency where clients or queues may retry. Identify which side effects need reconciliation after a partial failure.
4. Choose the smallest change that fits existing conventions. For data changes, plan migration order and recovery. Record the signals that let operators detect broken invariants without logging secrets.
5. Verify a successful request, invalid input, unauthorized access, and a failure mid-operation. For tenant-scoped writes, verify isolation and unchanged state after rejection. Report executed checks and remaining gaps.

Example: for `POST /orders`, verify that a repeated request does not duplicate an order, a caller cannot claim another tenant's identifier, and a failed stock update cannot leave an order partially recorded.

## Source and status
- Adapted from user-provided original Markdown documents: 01_BACKEND_CORE.md, 02_BACKEND_SECURITY.md, 03_BACKEND_OPS.md.
- This is a **reviewed derivative**, not a verbatim copy of internal/confidential source material.
- **Status:** draft; not functionally tested in Codex/Claude/ChatGPT.
- Verify tools, versions and official docs in the target environment before execution.
- No third-party code or dependency is bundled.
