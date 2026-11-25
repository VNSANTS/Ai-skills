---
name: repository-curation
description: Verify and catalog GitHub repositories for skills, tools, MCP servers, and frameworks. Use for resolving aliases, handling renamed repositories, refreshing metadata, and maintaining catalog JSON.
---

# Repository curation

1. Read INDEX.md and catalog/*.json only as needed; deduplicate canonical repository IDs.
2. Identify project type accurately; inspect official repository metadata and upstream project README.
3. Collect dated star count, last push, license SPDX metadata, URL, description and archive status.
4. Use `metadata-verified-only` para metadados oficiais confirmados. Sustente afirmações sobre código, scripts, licença, segurança ou execução com evidências da respectiva revisão ou teste.
5. Do not install or mirror code automatically; keep cost at R$ 0 and respect source licenses.
6. Place data in appropriate catalog JSON, run `python scripts/validate_catalog.py`, update INDEX.md and report unresolved aliases.
7. Prefer fewer well-evidenced projects over hundreds of unconfirmed names. Stars do not equal trust.

## Identidade e evidência

- Compare o nome canônico na API com o nome informado. Quando a API fornecer o ID numérico do repositório, registre-o em `repository_id`. Em renomes, procure o ID e os slugs antigo e atual, atualize a ficha existente e preserve o alias na origem. Mantenha fichas separadas quando os IDs divergirem, mesmo com nomes iguais.
- Confira se URL, estrelas e estado de arquivamento vieram da mesma consulta. Registre a data do snapshot e revise os totais antes e depois de executar o validador.
- Use `unverified` quando a identidade continuar ambígua. Registre a evidência que falta para que outra pessoa possa concluir a triagem.

Status: original workflow; no external installation.
