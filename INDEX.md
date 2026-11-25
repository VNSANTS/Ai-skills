# Índice de recursos para agentes de IA

> **Metadados do GitHub em 25 de novembro de 2026.** O retrato registra estrelas, licença SPDX, último push e estado de arquivamento informados pela API do GitHub. A verificação cobre apenas metadados.

**147 repositórios com metadados confirmados**, 3 caminhos antigos pendentes e **14 catálogos JSON**. Os quatro caminhos históricos confirmados permanecem como aliases dos repositórios atuais. Veja também [42 referências antigas](docs/HISTORICAL_RESOURCES.md), [pendências](docs/UNRESOLVED.md) e [política de adoção](docs/ADOPTION_POLICY.md).

## Produtividade de desenvolvimento

Seleção de 25/11/2026 para diminuir o trabalho repetitivo na busca, revisão, validação e preparação de contexto. Critérios: utilidade frequente, sobreposição com ferramentas já catalogadas, manutenção visível e possibilidade de uso sem contratar um plano adicional. [Metadados JSON](catalog/developer-productivity.json).

| Uso | Projeto | Aplicação prática |
|---|---|---|
| Busca | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep) | Buscar texto e arquivos no código respeitando regras de exclusão do Git. |
| Busca | [ast-grep/ast-grep](https://github.com/ast-grep/ast-grep) | Encontrar padrões pela estrutura sintática, como chamadas a uma função em TypeScript. |
| Revisão | [Wilfred/difftastic](https://github.com/Wilfred/difftastic) | Comparar código pela sintaxe e facilitar revisão de arquivos reformatados. |
| Revisão | [cli/cli](https://github.com/cli/cli) | Consultar PRs, checks e execuções do GitHub Actions pelo terminal. |
| Revisão | [reviewdog/reviewdog](https://github.com/reviewdog/reviewdog) | Levar diagnósticos dos linters ao diff do PR. Conferir permissões antes de publicar comentários. |
| CI | [rhysd/actionlint](https://github.com/rhysd/actionlint) | Detectar erros em workflows do GitHub Actions antes do push. |
| CI | [zizmorcore/zizmor](https://github.com/zizmorcore/zizmor) | Revisar defensivamente permissões e práticas de segurança em workflows do GitHub Actions. |
| CI | [astral-sh/ruff](https://github.com/astral-sh/ruff) | Rodar lint e formatar Python com uma ferramenta, inclusive no CI. |
| Automação | [casey/just](https://github.com/casey/just) | Registrar comandos recorrentes de build, lint e testes em um justfile. |
| Automação | [go-task/task](https://github.com/go-task/task) | Definir tarefas e dependências em um Taskfile YAML multiplataforma. |
| Automação | [jqlang/jq](https://github.com/jqlang/jq) | Extrair campos de respostas JSON para reduzir a leitura de logs e saídas de API. |
| Contexto | [yamadashy/repomix](https://github.com/yamadashy/repomix) | Empacotar arquivos selecionados em um artefato de contexto. Revisar o conteúdo antes de compartilhar. |
| Contexto | [mksglu/context-mode](https://github.com/mksglu/context-mode) | Indexar saídas extensas e recuperar trechos sob demanda. Conferir retenção e acesso antes de habilitar. |

### Combinações por tarefa

- **Nexus Finance e ERP:** use ripgrep para localizar rotas e símbolos, ast-grep quando precisar procurar uma estrutura TypeScript, e GitHub CLI para consultar os checks do PR. Use actionlint quando o diff mexer em workflows.
- **JARVIS:** use Ruff para diagnosticar problemas de Python e escolha Just ou Task se o projeto precisar padronizar comandos. Preserve os comandos de teste já definidos e confira o shell usado no Windows.
- **Sessões longas com IA:** comece por filtros de arquivos e campos. Use Repomix quando precisar montar um pacote de arquivos selecionados e Context Mode quando o problema for saída longa do terminal ou das ferramentas. Compare com [RTK](https://github.com/rtk-ai/rtk) para compactação da saída de comandos e use a [skill de eficiência](skills/token-efficiency/SKILL.md) para medir o efeito com a mesma tarefa.

O catálogo registra a licença detectada pelo GitHub. `NOASSERTION` indica que a API não determinou um identificador SPDX. A avaliação foi documental, sem benchmark de desempenho ou instalação.

## Skills descobertas no Instagram

Achados no perfil [Coral Tech](https://www.instagram.com/coraltechh/), com identidade e metadados conferidos na API do GitHub em 25/11/2026. [Metadados JSON](catalog/instagram-skills.json).

| Projeto | Uso | Reel |
|---|---|---|
| [founder-skill](https://github.com/Jakeschincariol/founder-skill) | Organiza hipóteses de negócio, preço e ponto de equilíbrio. Valide as hipóteses com clientes reais. | [Demonstração](https://www.instagram.com/coraltechh/reel/Df7AqGruas0/) |
| [teardown](https://github.com/elvarofficial/teardown) | Cria visualizações interativas de mecanismos em 3D e permite gerar vídeos explicativos. | [Demonstração](https://www.instagram.com/coraltechh/reel/DfzysLjqk5G/) |
| [claude-animation-skills](https://github.com/artemnovitckii/claude-animation-skills) | Coleção para criar animações e explicações visuais curtas com renderização local. Confira a licença integral e os requisitos do ambiente. | [Demonstração](https://www.instagram.com/coraltechh/reel/DgKTuYKyuQt/) |

Dois destaques dos Reels já estavam no catálogo: [Superpowers](https://github.com/obra/superpowers) para planejamento e testes de código e [Unslop](https://github.com/heydamir/unslop) para revisão visual de interfaces. A licença `NOASSERTION` é o valor retornado pela API. As demos são referências de descoberta e a execução segue sem teste neste catálogo.

## Skills e ferramentas descobertas no YouTube

Seleção a partir de demonstrações de [Matt Wolfe](https://www.youtube.com/watch?v=STH929HARLo) e [Y Combinator](https://www.youtube.com/watch?v=wkv2ifxPpF8), com metadados conferidos na API do GitHub em 25/11/2026. [Metadados JSON](catalog/youtube-skills.json).

| Projeto | Uso | Demonstração |
|---|---|---|
| [gstack](https://github.com/garrytan/gstack) | Organiza planejamento, revisão e QA em fluxos reutilizáveis. Para o Nexus, comece avaliando a revisão e o QA sem habilitar publicação automática. | [YouTube](https://www.youtube.com/watch?v=wkv2ifxPpF8) |
| [Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | Cria um mapa navegável do código para entender rotas, dependências e módulos antes de refatorar. | [YouTube](https://www.youtube.com/watch?v=STH929HARLo&t=854s) |
| [last30days-skill](https://github.com/mvanhorn/last30days-skill) | Resume discussões recentes de várias fontes. Confira cobertura, credenciais e custo de cada integração. | [YouTube](https://www.youtube.com/watch?v=STH929HARLo&t=1119s) |
| [stop-slop](https://github.com/hardikpandya/stop-slop) | Revisa prosa para remover construções repetitivas e clichês. Confira o resultado no idioma da publicação. | [YouTube](https://www.youtube.com/watch?v=STH929HARLo&t=494s) |
| [hyperframes](https://github.com/heygen-com/hyperframes) | Renderiza composições HTML em MP4, como demos de produto com capturas do app. | [YouTube](https://www.youtube.com/watch?v=STH929HARLo&t=1486s) |

Prioridade para desenvolvimento: GStack para estruturar revisão e QA, e Understand Anything para navegar no código. Compatibilidade, permissões e impacto na produtividade ainda precisam de teste no ambiente escolhido.

## ★ 25 repositórios com mais estrelas

| Projeto | Estrelas | Licença detectada | Categoria |
|---|---:|---|---|
| [morluto/rea](https://github.com/morluto/rea) | 478.062 | MIT | Engenharia reversa |
| [mattpocock/skills](https://github.com/mattpocock/skills) | 332.681 | MIT | Engenharia |
| [obra/superpowers](https://github.com/obra/superpowers) | 326.366 | MIT | Engenharia |
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | 310.545 | MIT | Eficiência |
| [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | 266.039 | MIT | Autonomia controlada |
| [anomalyco/opencode](https://github.com/anomalyco/opencode) | 229.119 | MIT | CLI e edição |
| [n8n-io/n8n](https://github.com/n8n-io/n8n) | 212.100 | NOASSERTION | Automação |
| [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | 209.687 | AGPL-3.0 | Coleta web |
| [anthropics/skills](https://github.com/anthropics/skills) | 200.335 | a verificar | Oficiais |
| [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | 198.542 | MIT | Eficiência |
| [microsoft/markitdown](https://github.com/microsoft/markitdown) | 198.411 | MIT | Documentos |
| [twbs/bootstrap](https://github.com/twbs/bootstrap) | 175.133 | MIT | CSS |
| [langgenius/dify](https://github.com/langgenius/dify) | 161.889 | NOASSERTION | Plataforma |
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | 157.031 | a verificar | Programação |
| [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | 154.062 | MIT | Design |
| [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | 153.233 | Apache-2.0 | Análise de código |
| [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | 149.979 | MIT | Framework |
| [garrytan/gstack](https://github.com/garrytan/gstack) | 142.628 | MIT | Engenharia |
| [stablyai/orca](https://github.com/stablyai/orca) | 137.536 | MIT | Orquestração |
| [openai/codex](https://github.com/openai/codex) | 136.426 | Apache-2.0 | Programação |
| [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw) | 136.290 | MIT | Diagramas |
| [shadcn-ui/ui](https://github.com/shadcn-ui/ui) | 129.066 | MIT | Componentes UI |
| [earendil-works/pi](https://github.com/earendil-works/pi) | 123.848 | MIT | Agente leve |
| [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | 123.751 | Apache-2.0 | Pesquisa financeira |
| [browser-use/browser-use](https://github.com/browser-use/browser-use) | 122.031 | MIT | Automação web |

## Lista completa por área

Cada JSON registra o caminho canônico em `repo`, a categoria em `category` e o tipo em `type`. As fichas confirmadas guardam o ID estável do GitHub em `repository_id`, além de URL, estrelas, licença, último push, estado de arquivamento e descrição. O campo `aliases` registra caminhos antigos quando a API os associa ao mesmo ID. Os três catálogos temáticos no início deste índice também fazem parte da lista completa.

### Skills essenciais

[Metadados JSON](catalog/skills-core.json)

| Projeto | ★ | Tipo | Situação |
|---|---:|---|---|
| [morluto/rea](https://github.com/morluto/rea) | 478.062 | skill-tool | Metadados OK |
| [mattpocock/skills](https://github.com/mattpocock/skills) | 332.681 | skill-collection | Metadados OK |
| [obra/superpowers](https://github.com/obra/superpowers) | 326.366 | skill-framework | Metadados OK |
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | 310.545 | agent-toolkit | Metadados OK |
| [anthropics/skills](https://github.com/anthropics/skills) | 200.335 | skill-collection | Metadados OK |
| [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | 153.233 | skill-tool | Metadados OK |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 120.368 | skill-collection | Metadados OK |
| [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | 116.686 | skill-tool | Metadados OK |
| [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | 78.231 | skill | Metadados OK |
| [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | 34.906 | skill-collection | Metadados OK |
| [openai/skills](https://github.com/openai/skills) | 29.132 | skill-collection | Metadados OK |
| [jakubkrehel/skills](https://github.com/jakubkrehel/skills) | 12.703 | skill-collection | Metadados OK |

### Ecossistema de Skills

[Metadados JSON](catalog/skills-ecosystem.json)

| Projeto | ★ | Tipo | Situação |
|---|---:|---|---|
| [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | 80.281 | awesome-list | Metadados OK |
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | 58.780 | awesome-list | Metadados OK |
| [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | 50.310 | awesome-list | Metadados OK |
| [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | 48.178 | plugin-collection | Metadados OK |
| [github/awesome-copilot](https://github.com/github/awesome-copilot) | 41.554 | skill-collection | Metadados OK |
| [anthropics/financial-services](https://github.com/anthropics/financial-services) | 41.511 | skill-collection | Metadados OK |
| [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | 37.540 | awesome-list | Metadados OK |
| [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | 36.888 | plugin-collection | Metadados OK |
| [huggingface/skills](https://github.com/huggingface/skills) | 11.398 | skill-collection | Metadados OK |
| [anthropics/claude-for-legal](https://github.com/anthropics/claude-for-legal) | 10.090 | skill-collection | Metadados OK |
| [trailofbits/skills](https://github.com/trailofbits/skills) | 8.424 | skill-collection | Metadados OK |
| [remotion-dev/skills](https://github.com/remotion-dev/skills) | 7.995 | skill-collection | Metadados OK |

### Outras coleções e agentes oficiais

[Metadados JSON](catalog/skills-extra.json)

| Projeto | ★ | Tipo | Situação |
|---|---:|---|---|
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | 157.031 | agent | Metadados OK |
| [openai/codex](https://github.com/openai/codex) | 136.426 | agent | Metadados OK |
| [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | 121.420 | skill | Metadados OK |
| [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | 109.102 | agent | Metadados OK |
| [tt-a1i/archify](https://github.com/tt-a1i/archify) | 99.823 | skill-tool | Metadados OK |
| [openai/openai-cookbook](https://github.com/openai/openai-cookbook) | 77.488 | examples | Metadados OK |
| [google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model) | 22.946 | agent-toolkit | Metadados OK |
| [heydamir/unslop](https://github.com/heydamir/unslop) | 21.581 | skill | Metadados OK |
| [GoogleCloudPlatform/agent-starter-pack](https://github.com/GoogleCloudPlatform/agent-starter-pack) | 6.572 | agent-toolkit | Metadados OK · arquivado |
| [anthropics/commerce-agents](https://github.com/anthropics/commerce-agents) | 3.530 | skill-collection | Metadados OK |
| [Sandy4321/awesome-agent-skills-july2026](https://github.com/Sandy4321/awesome-agent-skills-july2026) | 0 | awesome-list | Metadados OK |

### Agentes e frameworks

[Metadados JSON](catalog/agents-frameworks.json)

| Projeto | ★ | Tipo | Situação |
|---|---:|---|---|
| [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | 266.039 | agent | Metadados OK |
| [anomalyco/opencode](https://github.com/anomalyco/opencode) | 229.119 | agent | Metadados OK |
| [langgenius/dify](https://github.com/langgenius/dify) | 161.889 | platform | Metadados OK |
| [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | 149.979 | framework | Metadados OK |
| [earendil-works/pi](https://github.com/earendil-works/pi) | 123.848 | agent | Metadados OK |
| [cline/cline](https://github.com/cline/cline) | 71.890 | agent | Metadados OK |
| [microsoft/autogen](https://github.com/microsoft/autogen) | 61.968 | framework | Metadados OK · arquivado |
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | 61.254 | framework | Metadados OK |
| [FlowiseAI/Flowise](https://github.com/FlowiseAI/Flowise) | 55.595 | platform | Metadados OK · arquivado |
| [Aider-AI/aider](https://github.com/Aider-AI/aider) | 50.255 | agent | Metadados OK |
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | 45.410 | framework | Metadados OK |
| [microsoft/semantic-kernel](https://github.com/microsoft/semantic-kernel) | 28.807 | framework | Metadados OK |

### MCP, memória e automação

[Metadados JSON](catalog/mcp-memory.json)

| Projeto | ★ | Tipo | Situação |
|---|---:|---|---|
| [n8n-io/n8n](https://github.com/n8n-io/n8n) | 212.100 | platform | Metadados OK |
| [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | 209.687 | tool | Metadados OK |
| [browser-use/browser-use](https://github.com/browser-use/browser-use) | 122.031 | agent-tool | Metadados OK |
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | 119.699 | tool | Metadados OK |
| [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | 98.495 | awesome-list | Metadados OK |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | 92.241 | mcp-collection | Metadados OK |
| [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | 80.841 | context-tool | Metadados OK |
| [mem0ai/mem0](https://github.com/mem0ai/mem0) | 69.462 | framework | Metadados OK |
| [upstash/context7](https://github.com/upstash/context7) | 65.444 | mcp-server | Metadados OK |
| [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | 59.321 | mcp-server | Metadados OK |
| [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) | 40.131 | mcp-server | Metadados OK |
| [ComposioHQ/composio](https://github.com/ComposioHQ/composio) | 31.290 | agent-tool | Metadados OK |

### Eficiência, roteamento e ferramentas

[Metadados JSON](catalog/optimization-tools.json)

| Projeto | ★ | Tipo | Situação |
|---|---:|---|---|
| [microsoft/markitdown](https://github.com/microsoft/markitdown) | 198.411 | tool | Metadados OK |
| [stablyai/orca](https://github.com/stablyai/orca) | 137.536 | agent-framework | Metadados OK |
| [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | 87.799 | cli-tool | Metadados OK |
| [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | 82.405 | agent-framework | Metadados OK |
| [usestrix/strix](https://github.com/usestrix/strix) | 77.538 | security-tool | Metadados OK |
| [BerriAI/litellm](https://github.com/BerriAI/litellm) | 63.897 | gateway | Metadados OK |
| [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | 58.191 | gateway | Metadados OK |
| [run-llama/llama_index](https://github.com/run-llama/llama_index) | 53.001 | framework | Metadados OK |
| [qdrant/qdrant](https://github.com/qdrant/qdrant) | 35.705 | database | Metadados OK |
| [chroma-core/chroma](https://github.com/chroma-core/chroma) | 29.763 | database | Metadados OK |
| [vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop) | 26.612 | agent-tool | Metadados OK |

### Design, motion e gráficos

[Metadados JSON](catalog/design-motion.json)

| Projeto | ★ | Tipo | Situação |
|---|---:|---|---|
| [twbs/bootstrap](https://github.com/twbs/bootstrap) | 175.133 | design-library | Metadados OK |
| [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw) | 136.290 | design-tool | Metadados OK |
| [shadcn-ui/ui](https://github.com/shadcn-ui/ui) | 129.066 | design-library | Metadados OK |
| [d3/d3](https://github.com/d3/d3) | 114.015 | data-visualization | Metadados OK |
| [mui/material-ui](https://github.com/mui/material-ui) | 99.394 | design-library | Metadados OK |
| [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss) | 98.825 | design-library | Metadados OK |
| [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | 75.663 | video-framework | Metadados OK |
| [chartjs/Chart.js](https://github.com/chartjs/Chart.js) | 67.823 | data-visualization | Metadados OK |
| [penpot/penpot](https://github.com/penpot/penpot) | 62.734 | design-tool | Metadados OK |
| [chakra-ui/chakra-ui](https://github.com/chakra-ui/chakra-ui) | 40.750 | design-library | Metadados OK |
| [fabricjs/fabric.js](https://github.com/fabricjs/fabric.js) | 31.566 | graphics-library | Metadados OK |
| [processing/p5.js](https://github.com/processing/p5.js) | 24.431 | graphics-library | Metadados OK |

### Segurança e testes

[Metadados JSON](catalog/security-testing.json)

| Projeto | ★ | Tipo | Situação |
|---|---:|---|---|
| [microsoft/playwright](https://github.com/microsoft/playwright) | 101.048 | testing-tool | Metadados OK |
| [aquasecurity/trivy](https://github.com/aquasecurity/trivy) | 39.730 | security-tool | Metadados OK |
| [gitleaks/gitleaks](https://github.com/gitleaks/gitleaks) | 31.335 | security-tool | Metadados OK |
| [renovatebot/renovate](https://github.com/renovatebot/renovate) | 23.266 | maintenance-tool | Metadados OK |
| [semgrep/semgrep](https://github.com/semgrep/semgrep) | 17.940 | security-tool | Metadados OK |
| [vitest-dev/vitest](https://github.com/vitest-dev/vitest) | 17.453 | testing-tool | Metadados OK |
| [zaproxy/zaproxy](https://github.com/zaproxy/zaproxy) | 16.274 | security-tool | Metadados OK |
| [pytest-dev/pytest](https://github.com/pytest-dev/pytest) | 14.760 | testing-tool | Metadados OK |
| [anchore/grype](https://github.com/anchore/grype) | 13.345 | security-tool | Metadados OK |
| [dependency-check/DependencyCheck](https://github.com/dependency-check/DependencyCheck) | 7.790 | security-tool | Metadados OK |
| [ossf/scorecard](https://github.com/ossf/scorecard) | 5.868 | security-tool | Metadados OK |
| `trufflesuite/trufflehog` | — | security-tool | Não confirmado (HTTP 404) |

### Finanças, SDKs e avaliação

[Metadados JSON](catalog/finance-sdk-evals.json)

| Projeto | ★ | Tipo | Situação |
|---|---:|---|---|
| [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | 123.751 | finance-agent | Metadados OK |
| [microsoft/qlib](https://github.com/microsoft/qlib) | 50.572 | finance-framework | Metadados OK |
| [QuantConnect/Lean](https://github.com/QuantConnect/Lean) | 22.707 | finance-framework | Metadados OK |
| [google/adk-python](https://github.com/google/adk-python) | 22.351 | agent-sdk | Metadados OK |
| [AI4Finance-Foundation/FinGPT](https://github.com/AI4Finance-Foundation/FinGPT) | 21.713 | finance-framework | Metadados OK |
| [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) | 21.382 | agent-framework | Metadados OK |
| [openai/evals](https://github.com/openai/evals) | 19.803 | evals-framework | Metadados OK |
| [AI4Finance-Foundation/FinRL](https://github.com/AI4Finance-Foundation/FinRL) | 17.181 | finance-framework | Metadados OK |
| [AI4Finance-Foundation/FinRobot](https://github.com/AI4Finance-Foundation/FinRobot) | 8.478 | finance-agent | Metadados OK |
| [openai/openai-agents-js](https://github.com/openai/openai-agents-js) | 4.030 | agent-sdk | Metadados OK |
| `openai/agents-python` | — | agent-sdk | Não confirmado (HTTP 404) |

### Marketing e conhecimento

[Metadados JSON](catalog/marketing-knowledge.json)

| Projeto | ★ | Tipo | Situação |
|---|---:|---|---|
| [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | 154.062 | skill-collection | Metadados OK |
| [infiniflow/ragflow](https://github.com/infiniflow/ragflow) | 94.696 | platform | Metadados OK |
| [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | 62.581 | skill-collection | Metadados OK |
| [microsoft/graphrag](https://github.com/microsoft/graphrag) | 36.751 | framework | Metadados OK |
| [getzep/graphiti](https://github.com/getzep/graphiti) | 33.085 | knowledge-tool | Metadados OK |
| [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | 32.336 | skill-collection | Metadados OK |
| [vercel/ai](https://github.com/vercel/ai) | 28.197 | sdk | Metadados OK |
| [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | 11.857 | skill-collection | Metadados OK |
| [TheCraigHewitt/seomachine](https://github.com/TheCraigHewitt/seomachine) | 7.639 | skill-tool | Metadados OK |
| [aaron-he-zhu/aaron-marketing-skills](https://github.com/aaron-he-zhu/aaron-marketing-skills) | 3.197 | skill-collection | Metadados OK |
| [RankSpotAI/awesome-seo-agent-skills](https://github.com/RankSpotAI/awesome-seo-agent-skills) | 29 | awesome-list | Metadados OK |
| `postiz-app/postiz` | — | automation-platform | Não confirmado (HTTP 404) |

### Descobertas e repositórios corrigidos

[Metadados JSON](catalog/corrected-discoveries.json)

| Projeto | ★ | Tipo | Situação |
|---|---:|---|---|
| [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | 198.542 | skill | Metadados OK |
| [supabase/supabase](https://github.com/supabase/supabase) | 115.468 | platform | Metadados OK |
| [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) | 94.318 | agent-platform | Metadados OK |
| [astral-sh/uv](https://github.com/astral-sh/uv) | 92.642 | dev-tool | Metadados OK |
| [openbq-org/OpenBB](https://github.com/openbq-org/OpenBB) | 75.726 | finance-platform | Metadados OK |
| [gitroomhq/postiz-app](https://github.com/gitroomhq/postiz-app) | 42.397 | automation-platform | Metadados OK |
| [oraios/serena](https://github.com/oraios/serena) | 31.696 | mcp-server | Metadados OK |
| [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | 30.870 | agent-sdk | Metadados OK |
| [trufflesecurity/trufflehog](https://github.com/trufflesecurity/trufflehog) | 29.652 | security-tool | Metadados OK |
| [github/docs](https://github.com/github/docs) | 21.563 | documentation | Metadados OK |
| [cloudflare/workers-sdk](https://github.com/cloudflare/workers-sdk) | 4.749 | sdk | Metadados OK |
| [badlogic/pi-skills](https://github.com/badlogic/pi-skills) | 2.673 | skill-collection | Metadados OK |

## Como usar sem desperdiçar tokens ou comprometer segurança

1. Busque a categoria relevante e leia somente as instruções necessárias.
2. Antes de integrar um projeto, confira fonte canônica, licença integral, scripts, permissões, dados enviados e custo.
3. Mantenha **R$0 em custos adicionais**; serviços premium, infraestrutura e APIs externas exigem aprovação própria.
4. Não instale hooks, MCPs, Skills nem ferramentas diretamente do catálogo. Use testes isolados e versões fixadas após inspeção.
5. Meça economia de tokens com cenários equivalentes; números de READMEs não são garantias.
6. Para novas inclusões, siga [repository-curation](skills/repository-curation/SKILL.md), execute `python scripts/validate_catalog.py` e atualize este índice.

O catálogo também reúne a [ficha da galeria Prompt Motion](tools/prompt-motion/README.md) e o [índice das 34 Skills autorais ou reconstruídas](skills/README.md).
