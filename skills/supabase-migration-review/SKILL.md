---
name: supabase-migration-review
description: Review and verify Supabase Postgres migrations that change tables, RLS policies, grants, or RPC functions. Use for migration drift, tenant isolation checks, and rollout preparation.
---

# Revisão de migrações Supabase

1. Compare o histórico local e o histórico aplicado no ambiente alvo. Identifique migrações pendentes, mudanças fora do histórico e consumidores que ainda usam o contrato anterior. Preserve migrações aplicadas e corrija por migração incremental.
2. Leia o SQL e monte a matriz de acesso por operação, papel e tenant. Confira grants, RLS, políticas de leitura e escrita e funções RPC. Em funções com privilégios elevados, confira necessidade, escopo, `search_path` e permissões de execução.
3. Valide a partir de um ambiente descartável ou de homologação autorizado. Use dois tenants sintéticos e papéis representativos. Verifique sucesso no tenant próprio, negação de acesso cruzado e ausência de alteração parcial após falhas. Quando a operação for crítica, valide chamadas concorrentes e repetidas.
4. Planeje a ordem de deploy com versões antigas do cliente e dados existentes. Identifique locks, backfills e mudanças irreversíveis. Registre o procedimento aplicável de recuperação e as verificações pós-deploy.
5. Registre migrações e ambiente verificados, evidências e pendências. Aplique em produção somente quando autorizado.

Exemplo: se uma RPC move estoque, confirme que o saldo e o lançamento mudam juntos e que um usuário de outro tenant recebe a negação esperada sem efeitos colaterais.

## Matriz mínima de isolamento

| Perfil | Caso de teste |
|---|---|
| Usuário autorizado do tenant A | Executa leitura e escrita previstas em A |
| Usuário equivalente do tenant B | Tenta a mesma operação com identificador de A e tem acesso negado |
| Usuário do tenant A sem permissão | Tem a operação restrita negada em A |
| Identidade sem sessão | Recebe somente o acesso público explicitamente previsto |

Execute a matriz usando o caminho de autenticação do aplicativo. Use privilégios administrativos para preparar e conferir os dados de teste, mantendo os papéis reais ao executar as operações avaliadas.
