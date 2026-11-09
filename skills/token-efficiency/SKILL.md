---
name: token-efficiency
description: Optimize token and context usage in coding and research agents without sacrificing correctness, safety, or necessary tests. Use for long-running tasks, repository audits, and constrained model budgets.
---

# Token and context efficiency

## Goals
Minimize redundant context, tool calls and output while preserving evidence, task completion and safety. Never optimize token usage at the cost of silently skipping essential verification.

## Workflow
1. **Orient once:** read the latest project checkpoint, AGENTS.md, task-specific documentation and git status. Avoid re-reading whole repositories.
2. **Plan by evidence:** identify what is already verified, what changed since the last run, and the smallest set of files needed.
3. **Search narrowly:** use filename discovery and targeted content searches before opening files. Read only relevant ranges; expand when dependencies require it.
4. **Batch independent operations:** combine searches and tests where the environment supports it, but preserve ordering for dependent or destructive steps.
5. **Load skills on demand:** read only relevant SKILL.md files and supporting references. Do not load the entire library.
6. **Use bounded output:** request concise tool logs, focused diffs, error summaries and targeted test results. Preserve complete logs in files only when necessary and safe.
7. **Validate proportionately:** run changed-component tests first, then broader regression/security tests when risk or release gates require them. Never claim a test passed unless executed.
8. **Checkpoint:** write a short, durable handoff with branch/commit, decisions, verified results, pending tasks, blockers and exact next commands.
9. **Respect cost caps:** select free providers where required, enforce explicit request/token budgets and prevent paid fallbacks. Stop and request authorization before spending money.
10. **Report honestly:** distinguish completed work, inferred findings, skipped checks and blocked steps. Do not invent token savings.

## Compact checkpoint template
```md
# CHECKPOINT
- Goal:
- Branch / commit:
- Completed:
- Tests executed / results:
- Decisions and constraints:
- Remaining / blockers:
- Next actions:
```

## Anti-patterns
- Dumping entire repositories into prompts.
- Repeating completed audits without changed evidence.
- Running all tests for every trivial documentation change.
- Installing dozens of skills into every session.
- Compressing context so aggressively that safety or acceptance criteria disappear.
- Claiming precise token savings without measurement.

## Verification
Track actual input/output tokens and task success when the provider exposes usage. Compare equivalent tasks, not unrelated sessions.

## Status
Original library skill. Documentation created; no runtime benchmark or agent compatibility test has yet been performed.
