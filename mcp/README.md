# Servidores MCP e integrações

Os servidores MCP são **processos com capacidades** (por exemplo ler arquivos, acessar navegador ou APIs), não simples descrições. A pasta `catalog/` inclui servidores populares e a coleção oficial.

**Nenhum MCP é registrado automaticamente.** Antes de configurar, auditar pacote, comandos de inicialização, privilégios, escopos, variáveis de ambiente, acesso à rede, política de dados e custo.

Priorizar ambientes locais/descartáveis, credenciais de escopo mínimo e permissões explícitas. Evitar colocar segredos em JSON versionado. Restringir acesso ao filesystem e bloquear mutações de produção quando não necessárias.

Referências de descoberta: `modelcontextprotocol/servers`, `punkpeye/awesome-mcp-servers`, `oraios/serena`, `ChromeDevTools/chrome-devtools-mcp` e `microsoft/playwright-mcp` (consulte os metadados verificados nos JSON).
