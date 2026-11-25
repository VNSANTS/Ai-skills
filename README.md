# Ai-skills — biblioteca universal de recursos para agentes de IA

Uma biblioteca organizada de **Skills, ferramentas, agentes, servidores MCP, frameworks, hooks, prompts, SDKs, design, segurança, marketing, finanças e eficiência de tokens**.

Em 25/11/2026, a biblioteca reúne **34 skills próprias** e **147 repositórios com metadados confirmados** em 14 catálogos. Três endereços antigos continuam sem confirmação. O histórico preserva quatro fichas de ferramentas e 42 referências de pedidos anteriores.

> Cada entrada externa descreve origem, atividade e licença informada pelo GitHub. A biblioteca funciona com orçamento adicional de **R$ 0**. As verificações executadas estão no [status técnico](docs/STATUS.md).

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
| Reproduzir os testes do repositório | [Comandos de validação](docs/STATUS.md#reproduzir-os-testes) |
| Rever o legado dos 31 Markdown | [docs/ZIP_REVIEW.md](docs/ZIP_REVIEW.md) |

## Execute uma tarefa de ponta a ponta

Comece pela [task-orchestration](skills/task-orchestration/SKILL.md). Dê a tarefa e diga como reconhecer o resultado. A skill consulta o projeto, esclarece as decisões que faltam, escolhe os recursos disponíveis para cada etapa, executa e confere a entrega. Pode trabalhar sozinha ou chamar as auxiliares [task-clarification](skills/task-clarification/SKILL.md) e [model-agent-routing](skills/model-agent-routing/SKILL.md).

> Use a task-orchestration para transformar os CSVs de inscrições deste projeto em um resumo para a coordenação. Entregue a contagem por oficina, identifique divergências e confira os totais com os arquivos de origem.

Para usá-la num projeto seu, siga o [guia de uso local](install/README.md#usar-as-skills-próprias-em-um-projeto). Para escolher outra especialidade, consulte as [skills por tarefa](skills/README.md).

## Princípios

- **Pesquisar antes de instalar:** inspecionar projeto canônico, licenças completas, arquivos executáveis, hooks, dependências, permissões e privacidade.
- **Eficiência real:** escolher ferramentas apenas quando ajudam; evitar bibliotecas gigantes no contexto de cada tarefa.
- **R$ 0 adicional:** nada de planos, APIs ou hospedagem paga sem nova decisão explícita.
- **Segurança:** manter segredos e fontes privadas fora do GitHub público. Nenhum teste ofensivo sem autorização.
- **Rastreabilidade:** anotar data, estrelas e status; não anunciar testes que não foram realizados.

## Limites transparentes

O catálogo registra identidades e metadados oficiais. Compatibilidade e execução dependem do ambiente em que cada ferramenta for adotada. Veja a [cobertura dos testes das skills próprias](docs/STATUS.md) e os [endereços pendentes](docs/UNRESOLVED.md).

## Repositórios externos e backups

**Referência/catalogação não é backup.** Os projetos externos do INDEX.md, catalog/*.json e tools/* estão documentados, mas seus códigos-fonte NÃO foram clonados para esta biblioteca.

- **ctresb/leis:** [projeto original](https://github.com/ctresb/leis), acervo brasileiro de legislação em Markdown. **Backup independente ainda não realizado.** O submódulo anterior foi removido porque não é uma cópia autônoma.
- Para produzir uma cópia real dos arquivos do projeto, consulte [o procedimento e os limites](docs/EXTERNAL_REPOSITORIES.md) e [o importador PowerShell](scripts/import-repository-snapshot.ps1).

Não confunda um registro de fonte, link ou submódulo com um espelho preservado. Este repositório ainda não substitui backups independentes dos projetos de terceiros.
