# Pendências e identidades não confirmadas

**Não transformar nomes semelhantes em instalações.** O catálogo guarda referências históricas mas algumas não têm repositório originário validado.

| Nome citado | Estado | Encaminhamento seguro |
|---|---|---|
| BibleMate | Origem não confirmada | Localizar repositório e licença antes de importar |
| OpenLumin | Origem não confirmada | Localizar repositório e licença antes de importar |
| Skill-Theo | Origem não confirmada | Localizar repositório e licença antes de importar |
| Free AI Token | Nome genérico, sem identidade verificável | Exigir projeto canônico |
| Orca (pedido antigo) | Ambíguo | [stablyai/orca](https://github.com/stablyai/orca) é uma referência verificada, **não** confirmação de que era o pedido original |
| Pi monorepo | Antigo `badlogic/pi-mono` não confirmado | [badlogic/pi-skills](https://github.com/badlogic/pi-skills) verificado; confirmar runtime Pi separadamente |
| Antigravity Awesome Skills | Nome anterior não confirmado na API | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) verificado; não assumir equivalência |
| FreeLLMAPI | Identificado | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi): revisar limites/termos |
| UI UX Pro Max | Identificado | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) |
| Graphify | Identificado | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) |
| OpenHands / OpenBB / TruffleHog / Postiz / OpenAI Agents Python | Identificados em novos caminhos | Veja `catalog/corrected-discoveries.json` |

## Recursos fora do GitHub ou com acesso condicionado
- [Prompt Motion](https://prompt-motion.com) é uma galeria; sua ficha está em `tools/prompt-motion/`. Não houve cópia de vídeos/prompts de terceiros.
- Skills oferecidas dentro de conectores ChatGPT (Google, Supabase, Cloudflare, Vercel etc.) podem não ser exportáveis. Disponibilidade aqui não equivale a código redistribuível.
- Referências de teologia e marketing devem ser avaliadas caso a caso, sem inferir validação acadêmica ou eficácia por estrelas.

## Originais e limites de auditoria
- Os **31 Markdown de origem** citados em `docs/ZIP_REVIEW.md` não tiveram auditoria linha a linha comprovada nesta biblioteca. Os originais não foram publicados no repositório público.
- A Skill `token-lean-workflow` foi reconstruída a partir dos requisitos do Nexus Finance; não é garantido que seja o mesmo arquivo da PR anterior.
- Metadados de estrelas e licenças são um retrato em 09/11/2026, não atualização automática nem auditoria integral.
