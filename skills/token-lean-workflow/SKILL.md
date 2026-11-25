---
name: token-lean-workflow
description: Resume long or interrupted coding tasks from a checkpoint with bounded retrieval and verification. Use after handoffs, interrupted builds, or context limits.
---

# Token-lean workflow

1. Read latest checkpoint, AGENTS.md and git status first. Preserve verified work.
2. Locate relevant paths with filenames and narrow searches. Never dump an entire repo by default.
3. Group independent calls and keep outputs bounded; retain full logs privately when necessary.
4. Load only applicable Skills and references.
5. Run targeted tests first and broaden based on risk; do not skip required release/security gates.
6. Record branch, commit, decisions, completed work, tests and exact next actions.
7. Enforce zero additional spend, provider quotas and no paid fallback.
8. Report measured token use only when instrumentation exists.

## Retomada de tarefa interrompida

1. Registre o resultado esperado e o bloqueio mais recente. Compare a revisão atual, o diff local e a revisão do checkpoint para detectar trabalho posterior ou alterações do usuário.
2. Para build, PR ou deploy interrompido, consulte primeiro o estado e a revisão da execução existente. Retome a etapa pendente e reaproveite os resultados que ainda correspondem à revisão e ao ambiente.
3. Se o próximo comando falhar, registre a mensagem relevante, o que já foi descartado e a evidência que falta. Deixe um checkpoint pequeno o suficiente para orientar a próxima sessão em uma única leitura.

Use [token-efficiency](../token-efficiency/SKILL.md) para medir consumo ou otimizar o contexto de um fluxo estável.

**Provenance:** reconstructed from the user's earlier Nexus Finance workflow request. This is not asserted to be a byte-identical copy of the original project Skill. **Status:** untested in this repository.
