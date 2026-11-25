---
name: github-pr-review
description: Review GitHub pull requests and local diffs for regressions, missing verification, and release blockers. Use for PR reviews, pre-merge checks, and CI failure triage.
---

# Revisão de pull requests

1. Identifique a branch base, o SHA do head, o objetivo do PR e as verificações exigidas. Revise o diff da base comum e leia os chamadores e contratos afetados.
2. Priorize bugs introduzidos pelo diff. Verifique comportamento existente, falhas parciais, compatibilidade de dados, permissões e flags. Aponte arquivo e linha, cenário observável, impacto e a menor correção possível.
3. Compare o SHA dos checks com o head atual. Diferencie falha, execução pendente, check ignorado e ausência de check. Quando possível, execute primeiro os testes do componente alterado e registre comando e resultado.
4. Entregue achados por gravidade e indique riscos restantes. Se nenhum problema foi encontrado, declare o escopo revisado e os checks executados. Altere, aprove ou integre o PR conforme a autorização do usuário.

Exemplo de revisão: um check verde no commit anterior continua sendo evidência daquele commit. Verifique o novo head antes de concluir que a revisão está pronta.
