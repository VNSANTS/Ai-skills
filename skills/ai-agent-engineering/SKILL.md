---
name: ai-agent-engineering
description: Use for agent architectures, retrieval systems, memory, tool use and evaluation
---

# AI agents, RAG and tool safety

## When to use
Use for agent architectures, retrieval systems, memory, tool use and evaluation.

## Workflow
- Define measurable objectives, budgets and failure boundaries.
- Separate instructions from retrieved untrusted content.
- Use least-privilege tool access, explicit confirmation for destructive actions, quotas and audit trails.
- Evaluate retrieval precision, groundedness, latency and cost with test cases.
- Treat reasoning-engine descriptions as conceptual patterns, not guarantees of hidden model internals.
- Do not claim persistent memory or autonomy without implemented storage and scheduling.

## Source and status
- Adapted from user-provided original Markdown documents: 01_Project_Instructions.md, 02_Core_System_Part1.md, 02_Core_System_Part2.md, 10_AI_System_Part1.md, 10_AI_System_Part2A.md, 10_AI_System_Part2B.md, 10_AI_System_Part2C.md, 10_AI_System_Part3.md, 10_AI_System_Part4.md.
- This is a **reviewed derivative**, not a verbatim copy of internal/confidential source material.
- **Status:** draft; not functionally tested in Codex/Claude/ChatGPT.
- Verify tools, versions and official docs in the target environment before execution.
- No third-party code or dependency is bundled.
