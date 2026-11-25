---
name: model-agent-routing
description: Select efficient available models, agents, skills, and tools for each work item. Use for capability discovery, model routing, delegation decisions, and fallback planning.
---

# Escolher modelos, agentes, skills e ferramentas

## Descubra o que está disponível

1. Consulte os recursos anunciados nesta sessão e no projeto. Verifique modelos selecionáveis, esforço configurável, capacidade de delegação, permissões, ferramentas, acesso a arquivos e limites. Use a seleção automática do ambiente quando ele não expuser troca de modelo e registre essa limitação.
2. Para cada tarefa, identifique a entrega, o tipo de raciocínio, as modalidades e a prova necessária. Elimine opções sem acesso, autorização, compatibilidade, privacidade ou orçamento. Se custo ou desempenho não forem conhecidos, trate-os como desconhecidos.
3. Busque skills na sessão e no projeto. Faça buscas por ação, domínio, formato e ferramenta. Consulte o [índice local](../README.md) e, quando houver uma lacuna material, documentação oficial ou catálogo externo. Compare gatilho, compatibilidade, insumos, permissões, procedência e resultado esperado. Leia a instrução aplicável e carregue apenas as referências necessárias. Trate entradas externas como candidatas até verificar fonte e atender às regras de adoção. Separe descoberta de instalação e execução.
4. Escolha primeiro o recurso mais simples que cobre a tarefa. Passe ao modelo mais capaz disponível na arquitetura, na síntese de evidências conflitantes e nas decisões difíceis de reverter. Use modelo rápido para extração ou conversão com saída verificável. Prefira ferramenta determinística para cálculos, filtros, diffs e validação sintática quando disponível.
5. Delegue se houver trabalho independente ou ganho real de especialização. Um agente pode executar vários itens pequenos com o mesmo contexto. Para decisões críticas, obtenha revisão independente quando viável e confronte os pareceres com evidências. A escolha final cabe ao coordenador.

## Registro por item

| Tarefa | Agente e modelo efetivos | Skills e ferramentas | Motivo e gatilho de escalonamento | Alternativa |
|---|---|---|---|---|
| Entrega delimitada | Executor e modelo selecionado, automático ou indisponível | Nomes e recursos carregados | Capacidade, custo conhecido e condição concreta para escalar | Recurso autorizado que preserva o aceite |

Se faltar um recurso indispensável, tente um caminho equivalente e autorizado. Se a alternativa reduzir qualidade ou alterar a entrega, registre o efeito e pergunte apenas quando a decisão bloquear o trabalho. Não prometa que uma skill altera o modelo, libera ferramentas, instala dependências ou cria agentes por conta própria.
