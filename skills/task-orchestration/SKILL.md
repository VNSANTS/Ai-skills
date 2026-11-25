---
name: task-orchestration
description: Turn a user task into a verified result by clarifying scope, inspecting the project, planning dependencies, routing work to agents, and integrating deliverables. Use when asked to execute a multi-step project end to end.
---

# Orquestrar da tarefa à entrega

## 1. Entenda a tarefa e o projeto

Use [task-clarification](../task-clarification/SKILL.md) para extrair o brief. Identifique regras do projeto, arquivos e ambiente relevantes, trabalho em curso, comandos de verificação e limites de autorização. Inspecione primeiro o que pode alterar escopo, dependências ou risco. Para tarefas diretas, execute e valide sem criar um time.

## 2. Crie o roteiro executável

Use o modelo mais capaz disponível para decisões de arquitetura ou com alto custo de erro. Separe etapas por resultado, não por ferramenta. Para cada etapa, registre responsável, insumos, dependências, entrega, critério de aceite e ação se falhar. Defina a ordem crítica, os pontos de integração e o que pode correr ao mesmo tempo.

Use [model-agent-routing](../model-agent-routing/SKILL.md) para selecionar recursos por etapa e revise a alocação quando aparecer um bloqueio ou evidência nova. Cada tarefa paralela deve ter fronteira de escrita clara ou ser somente leitura. Use cópias de trabalho isoladas quando as alterações independentes ainda precisarem tocar o mesmo código. Integre alterações em sequência.

## 3. Delegue e acompanhe

- Envie a cada agente o objetivo, entradas e revisão, escopo de escrita, skills e ferramentas selecionadas, limites de autorização, formato de saída, verificação esperada e condição para parar. Compartilhe somente o contexto necessário. Mantenha credenciais no ambiente autorizado.
- Registre atribuição planejada e executor real. Peça o resultado, evidência, arquivos alterados e bloqueios. Se houver dependência incompleta, execute etapas independentes e preserve os resultados válidos. Se uma verificação falhar, investigue a causa e tente uma recuperação compatível com o escopo.
- Ao falhar uma ação externa ou mutação, consulte o estado antes de repetir. Se não houver agentes, execute localmente em sequência, mantendo os mesmos critérios e sem representar etapas próprias como delegadas.
- Aplique correções do usuário ao brief e invalide verificações e atribuições atingidas por elas. Peça aprovação quando exigida para publicar, gastar ou produzir um efeito externo.

## 4. Integre e entregue

Compare interfaces, arquivos e pressupostos entre as saídas. Execute verificações da versão integrada e aplique [deliverable-review](../deliverable-review/SKILL.md) antes da entrega. O coordenador confirma cada critério de aceite e relata resultados, pendências, decisões assumidas e bloqueios. Conclua com o resultado solicitado sempre que houver trabalho autorizado que possa ser realizado.

[Leia o exemplo de roteiro, delegação e recuperação](references/example.md) se precisar de um modelo de execução.
