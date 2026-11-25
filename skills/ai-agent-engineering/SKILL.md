---
name: ai-agent-engineering
description: Design and evaluate AI agents with retrieval, memory and tool access. Use for RAG pipelines, tool contracts, agent budgets, and grounding evaluations.
---

# AI agents, RAG and tool safety

## Workflow
- Define measurable objectives, budgets and failure boundaries.
- Separate instructions from retrieved untrusted content.
- Use least-privilege tool access, explicit confirmation for destructive actions, quotas and audit trails.
- Evaluate retrieval precision, groundedness, latency and cost with test cases.
- Treat reasoning-engine descriptions as conceptual patterns, not guarantees of hidden model internals.
- Do not claim persistent memory or autonomy without implemented storage and scheduling.

## Verificação de comportamento

- Defina para cada ferramenta o esquema de entrada, a autoridade para executar, o efeito observável e a política de timeout. Antes de repetir uma operação que escreve, consulte seu estado ou use uma chave de idempotência.
- Monte casos com evidência suficiente, evidência ausente, fontes conflitantes e instruções maliciosas dentro de documentos. Registre a fonte esperada, a ação permitida e o resultado observado.
- Teste recuperação e geração separadamente. Se a fonte existe mas ficou fora do contexto, investigue a busca. Se entrou no contexto e a resposta a contradiz, investigue a geração.
- Para cada pergunta com evidência conhecida, meça a fração das fontes esperadas que aparece nos primeiros k resultados (recall@k). Quando as fontes divergem, considere a autoridade e a vigência na data a que a pergunta se refere. Se a divergência persistir, cite as fontes e indique o que ficou em aberto.

## Source and status
- Adapted from user-provided original Markdown documents: 01_Project_Instructions.md, 02_Core_System_Part1.md, 02_Core_System_Part2.md, 10_AI_System_Part1.md, 10_AI_System_Part2A.md, 10_AI_System_Part2B.md, 10_AI_System_Part2C.md, 10_AI_System_Part3.md, 10_AI_System_Part4.md.
- This is a **reviewed derivative**, not a verbatim copy of internal/confidential source material.
- Rascunho aplicado explicitamente no Codex com corpus sintético e regras determinísticas de resposta. A avaliação com um modelo e um provedor reais continua pendente.
- Verify tools, versions and official docs in the target environment before execution.
- No third-party code or dependency is bundled.
