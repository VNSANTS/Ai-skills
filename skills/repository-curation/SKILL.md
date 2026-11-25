---
name: repository-curation
description: Verify and catalog GitHub repositories for skills, tools, MCP servers, and frameworks. Use for resolving aliases, handling renamed repositories, refreshing metadata, and maintaining catalog JSON.
---

# Repository curation

1. Read INDEX.md and catalog/*.json only as needed; deduplicate canonical repository IDs.
2. Identify project type accurately; inspect official repository metadata and upstream project README.
3. Collect dated star count, last push, license SPDX metadata, URL, description and archive status.
4. Use status `metadata-verified-only` until code/license/scripts/security have been inspected and tests recorded.
5. Do not install or mirror code automatically; keep cost at R$ 0 and respect source licenses.
6. Place data in appropriate catalog JSON, run `python scripts/validate_catalog.py`, update INDEX.md and report unresolved aliases.
7. Prefer fewer well-evidenced projects over hundreds of unconfirmed names. Stars do not equal trust.

## Identidade e evidência

- Compare o nome canônico na API com o nome informado. Ao descobrir um renome, procure entradas com o slug antigo, o slug atual e, quando disponível, o ID estável do repositório. Atualize a entrada existente e preserve o alias no registro de origem quando útil.
- Confira se URL, estrelas e estado de arquivamento vieram da mesma consulta. Registre a data do snapshot e revise os totais antes e depois de executar o validador.
- Use `unverified` quando a identidade continuar ambígua. Registre a evidência que falta para que outra pessoa possa concluir a triagem.

Status: original workflow; no external installation.
