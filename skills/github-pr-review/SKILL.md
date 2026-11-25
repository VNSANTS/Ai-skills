---
name: github-pr-review
description: Review GitHub pull requests and local diffs for regressions, missing verification, and release blockers. Use for PR reviews, pre-merge checks, and CI failure triage.
---

# Revisão de pull requests

1. Identifique a branch base, o SHA do head, o objetivo do PR e as verificações exigidas. Revise o diff da base comum e leia os chamadores e contratos afetados.
2. Priorize bugs introduzidos pelo diff. Verifique comportamento existente, falhas parciais, compatibilidade de dados, permissões e flags. Aponte arquivo e linha, cenário observável, impacto e a menor correção possível.
3. Identifique o evento e a revisão de cada check exigido. Para testes do head, compare o SHA com o head atual. Para testes de integração, confira nos metadados quais commits da base e do PR, ou qual grupo de merge, foram testados e se atendem à regra do repositório. Diferencie falha, execução pendente, check ignorado e ausência de check. Quando possível, execute primeiro os testes do componente alterado e registre comando e resultado.
4. Entregue achados por gravidade e indique riscos restantes. Se nenhum problema foi encontrado, declare o escopo revisado e os checks executados. Altere, aprove ou integre o PR conforme a autorização do usuário.

Exemplo de revisão: um check verde no commit anterior continua sendo evidência daquele commit. Verifique o novo head antes de concluir que a revisão está pronta.

## Triagem de falhas de CI

1. Abra o primeiro passo com erro e associe o log à revisão que o job testou. Compare com resultados recentes da base quando disponíveis.
2. Classifique a causa como regressão, falha da infraestrutura ou evidência insuficiente. Execute uma reprodução focalizada quando possível. Ao repetir um job, registre a tentativa e preserve o resultado anterior.
3. Para cada bloqueio, indique a evidência que permitiria encerrá-lo. Reconfirme o head e, nos checks de integração, a base ou o grupo de merge antes de integrar o PR com autorização.
