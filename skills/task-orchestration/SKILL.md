---
name: task-orchestration
description: Turn a user task into a verified result by clarifying scope, inspecting the project, planning dependencies, routing work to agents, and integrating deliverables. Use when asked to execute a multi-step project end to end.
---

# Orquestrar da tarefa à entrega

Execute o trabalho até a entrega verificada. Encerre no plano quando o usuário pedir apenas planejamento. Para uma tarefa simples, faça a leitura necessária, execute e confira diretamente.

## 1. Feche o escopo

Leia o pedido, as regras aplicáveis, os arquivos de entrada e o trabalho em curso. Defina destinatário, entregas, destinos, critérios de aceite e limites de autorização. Se uma ambiguidade material persistir, mostre as consequências, pergunte pela decisão que falta e avance no que independe dela. Incorpore correções sem repetir etapas ainda válidas.

Procure pelo nome as skills auxiliares no catálogo do ambiente ou no projeto indicado e abra a correspondência disponível. `task-clarification` devolve o brief a este fluxo. `model-agent-routing` apoia a escolha de recursos e `deliverable-review` apoia a conferência final. Se apenas esta pasta estiver instalada, siga os passos desta página com os recursos existentes. A execução pode prosseguir sem um índice, pastas irmãs ou instalações adicionais.

## 2. Distribua o trabalho

Organize as etapas pelo resultado e pelas dependências. Para cada etapa relevante, identifique entrada, responsável, recurso realmente disponível, entrega, critério de aceite e alternativa se ela falhar. Se houver uma skill de domínio pertinente, localize-a pelo nome ou pela tarefa e leia suas instruções antes de aplicá-la.

Confira capacidades, modelo selecionável, permissões, custo e acesso às entradas. Use cálculos ou testes determinísticos para resultados reproduzíveis. Para arquitetura, planejamento complexo e decisões de alto impacto, prefira o modelo mais capaz que atenda às restrições. Se um modelo for obrigatório e o ambiente não confirmar sua seleção, consulte o usuário antes de substituí-lo. Sob orçamento fechado, siga por um recurso com custo adicional conhecido e autorizado.

## 3. Execute e recupere

Delegue etapas independentes quando houver benefício, permissão e vaga. Forneça objetivo, versão das entradas, limites de escrita, recursos escolhidos, formato de retorno e critério de aceite. Separe áreas de escrita ou atribua uma revisão somente leitura. Compartilhe somente o contexto necessário. Peça a evidência, o resultado e eventuais bloqueios.

Se não houver agente disponível, execute as etapas em sequência. Se um agente falhar ou entregar parcialmente, examine o que foi gravado e o que já passou na verificação. Reatribua a parte faltante ou assuma-a localmente, dentro da autorização existente. Confira o estado de qualquer ação com efeito externo antes de repeti-la. Registre a causa da mudança e o executor efetivo.

## 4. Integre e entregue

Compare as saídas entre si e com as entradas. Em resultados de alto impacto, peça a um revisor uma conferência independente nas fontes. Sem revisor, use outro método de cálculo ou teste e identifique quem o executou. Resolva divergências antes de incorporar resultados. Reabra a versão final no formato pedido, confira cada requisito, corrija falhas e repita os testes afetados. Entregue os arquivos solicitados e indique decisões assumidas e pendências materiais.

[Exemplo de roteiro, delegação e recuperação](references/example.md)
