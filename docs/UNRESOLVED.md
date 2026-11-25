# Pendências e identidades não confirmadas

O catálogo preserva referências históricas. Confirme a identidade canônica antes de adotar um recurso.

## Caminhos antigos pendentes

Em 25/11/2026, três caminhos antigos do catálogo retornaram HTTP 404 na API do GitHub. Os projetos sugeridos já têm metadados confirmados em suas próprias fichas. A relação com os caminhos antigos segue sem confirmação.

| Caminho antigo | Resultado | Projeto sugerido |
|---|---|---|
| `openai/agents-python` | HTTP 404 | [openai/openai-agents-python](https://github.com/openai/openai-agents-python), publicado na [documentação do OpenAI Agents SDK](https://openai.github.io/openai-agents-python/) |
| `postiz-app/postiz` | HTTP 404 | [gitroomhq/postiz-app](https://github.com/gitroomhq/postiz-app), indicado no [site do Postiz](https://postiz.com/) |
| `trufflesuite/trufflehog` | HTTP 404 | [trufflesecurity/trufflehog](https://github.com/trufflesecurity/trufflehog), indicado no [site da Truffle Security](https://trufflesecurity.com/trufflehog) |

## Mudanças de endereço confirmadas

Cada caminho antigo redirecionou para o ID do repositório canônico na API do GitHub. Os JSONs registram cada repositório uma vez e guardam o caminho antigo em `aliases`.

| Caminho antigo | Repositório atual | ID do GitHub |
|---|---|---:|
| `badlogic/pi-mono` | [earendil-works/pi](https://github.com/earendil-works/pi) | 1035029907 |
| `openbb-finance/OpenBB` | [openbq-org/OpenBB](https://github.com/openbq-org/OpenBB) | 323048702 |
| `All-Hands-AI/OpenHands` | [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) | 771302083 |
| `Sickn33/antigravity-awesome-skills` | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | 1134426800 |

A coleção [badlogic/pi-skills](https://github.com/badlogic/pi-skills) tem uma ficha própria. A API também confirmou [github/docs](https://github.com/github/docs), que estava pendente após uma falha de consulta.

## Outras referências históricas

| Nome citado | Estado | Encaminhamento seguro |
|---|---|---|
| BibleMate | Origem não confirmada | Localizar repositório e licença antes de importar |
| OpenLumin | Origem não confirmada | Localizar repositório e licença antes de importar |
| Skill-Theo | Origem não confirmada | Localizar repositório e licença antes de importar |
| Free AI Token | Nome genérico, sem identidade verificável | Exigir projeto canônico |
| Orca (pedido antigo) | Ambíguo | [stablyai/orca](https://github.com/stablyai/orca) é uma referência verificada, **não** confirmação de que era o pedido original |
| FreeLLMAPI | Identificado | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi): revisar limites/termos |
| UI UX Pro Max | Identificado | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) |
| Graphify | Identificado | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) |

## Recursos fora do GitHub ou com acesso condicionado
- [Prompt Motion](https://prompt-motion.com) é uma galeria; sua ficha está em `tools/prompt-motion/`. Não houve cópia de vídeos/prompts de terceiros.
- Skills oferecidas dentro de conectores ChatGPT (Google, Supabase, Cloudflare, Vercel etc.) podem não ser exportáveis. Disponibilidade aqui não equivale a código redistribuível.
- Referências de teologia e marketing devem ser avaliadas caso a caso, sem inferir validação acadêmica ou eficácia por estrelas.

## Originais e limites de auditoria
- Os **31 Markdown de origem** citados em `docs/ZIP_REVIEW.md` não tiveram auditoria linha a linha comprovada nesta biblioteca. Os originais não foram publicados no repositório público.
- A Skill `token-lean-workflow` foi reconstruída a partir dos requisitos do Nexus Finance; não é garantido que seja o mesmo arquivo da PR anterior.
- O retrato de 25/11/2026 registra estrelas, licença SPDX e atividade informadas pela API do GitHub. A data da consulta consta nos arquivos JSON do catálogo.
