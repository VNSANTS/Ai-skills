# Ai-skills — biblioteca universal de recursos para agentes de IA

Uma biblioteca organizada de **Skills, ferramentas, agentes, servidores MCP, frameworks, hooks, prompts, SDKs, design, segurança, marketing, finanças e eficiência de tokens**.

**Catálogo atualizado em 25/11/2026:** **145 repositórios com metadados confirmados na API do GitHub**, **8 candidatos ainda não confirmados**, **14 arquivos JSON catalogados**, **28 Skills autorais/reconstruídas**, quatro fichas de ferramentas e 42 referências recuperadas de pedidos antigos.

> **Catalogado ≠ instalado ≠ auditado.** Popularidade e campo de licença do GitHub não garantem segurança. Não foi copiado ou executado código de terceiros nem foram configurados hooks, MCPs ou modelos pagos. O orçamento adicional permitido é **R$ 0**.

## Comece por aqui

| Quero… | Onde encontrar |
|---|---|
| Descobrir projetos por estrelas e categoria | [INDEX.md](INDEX.md) |
| Acelerar busca, revisão, CI e uso de contexto | [Produtividade de desenvolvimento](INDEX.md#produtividade-de-desenvolvimento) |
| Ver skills encontradas em Reels | [Skills descobertas no Instagram](INDEX.md#skills-descobertas-no-instagram) |
| Ver skills encontradas no YouTube | [Demonstrações no YouTube](INDEX.md#skills-e-ferramentas-descobertas-no-youtube) |
| Acessar dados estruturados para IA/scripts | [catalog/](catalog/) — JSONs por área |
| Escolher uma skill própria para qualquer projeto | [Skills por tarefa](skills/README.md) |
| Ver ferramentas pedidas (ECC, Strix, Agent Desktop, Prompt Motion) | [tools/](tools/) |
| Encontrar pedidos antigos | [CATALOG.md](CATALOG.md), [docs/HISTORICAL_RESOURCES.md](docs/HISTORICAL_RESOURCES.md) |
| Conferir nomes não identificados | [docs/UNRESOLVED.md](docs/UNRESOLVED.md) |
| Aprender a instalar Skills, MCPs e ferramentas | [install/README.md](install/README.md) |
| Avaliar segurança, licença e custo | [docs/ADOPTION_POLICY.md](docs/ADOPTION_POLICY.md) |
| Pesquisar novas ferramentas com IA | [prompts/curate-and-verify.md](prompts/curate-and-verify.md) |
| Entender integrações MCP e hooks | [mcp/](mcp/), [hooks/](hooks/) |
| Adotar regras em projeto próprio | [examples/AGENTS.project.md](examples/AGENTS.project.md) |
| Validar dados localmente | `python scripts/validate_catalog.py` |
| Rever o legado dos 31 Markdown | [docs/ZIP_REVIEW.md](docs/ZIP_REVIEW.md) |

## Coleções de Skills autorais

Encontre fluxos reutilizáveis de planejamento, pesquisa, dados, documentação, apresentações, qualidade, acessibilidade, automação, operações e conteúdo no [índice de skills](skills/README.md).

Arquitetura de backend; Flutter; UX/UI; engenharia de agentes; educação financeira; design de aprendizagem; gamificação ética; estratégia de produto; eficiência de tokens; fluxo econômico de tarefas; banners panorâmicos para datashow; curadoria de repositórios; adoção segura de ferramentas.

A coleção também inclui [revisão de PRs no GitHub](skills/github-pr-review/SKILL.md), [release Android e PWA](skills/android-pwa-release/SKILL.md) e [revisão de migrações Supabase](skills/supabase-migration-review/SKILL.md).

Todas ficam em `skills/<nome>/SKILL.md`. Não há garantia de que um agente as carregará automaticamente: é necessário apontar o agente para esse repositório ou copiar a Skill após avaliação.

## Princípios

- **Pesquisar antes de instalar:** inspecionar projeto canônico, licenças completas, arquivos executáveis, hooks, dependências, permissões e privacidade.
- **Eficiência real:** escolher ferramentas apenas quando ajudam; evitar bibliotecas gigantes no contexto de cada tarefa.
- **R$ 0 adicional:** nada de planos, APIs ou hospedagem paga sem nova decisão explícita.
- **Segurança:** manter segredos e fontes privadas fora do GitHub público. Nenhum teste ofensivo sem autorização.
- **Rastreabilidade:** anotar data, estrelas e status; não anunciar testes que não foram realizados.

## Limites transparentes

As 145 entradas têm **metadados oficiais do GitHub conferidos**, não 145 auditorias de software. As 8 referências não confirmadas permanecem registradas para triagem. Este projeto não gerencia configurações privadas do ChatGPT, instalação no Codex ou deploys de terceiros. Consulte o [status técnico](docs/STATUS.md).

## Repositórios externos e backups

**Referência/catalogação não é backup.** Os projetos externos do INDEX.md, catalog/*.json e tools/* estão documentados, mas seus códigos-fonte NÃO foram clonados para esta biblioteca.

- **ctresb/leis:** [projeto original](https://github.com/ctresb/leis), acervo brasileiro de legislação em Markdown. **Backup independente ainda não realizado.** O submódulo anterior foi removido porque não é uma cópia autônoma.
- Para produzir uma cópia real dos arquivos do projeto, consulte [o procedimento e os limites](docs/EXTERNAL_REPOSITORIES.md) e [o importador PowerShell](scripts/import-repository-snapshot.ps1).

Não confunda um registro de fonte, link ou submódulo com um espelho preservado. Este repositório ainda não substitui backups independentes dos projetos de terceiros.
