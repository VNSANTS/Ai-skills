---
name: secure-tool-adoption
description: Review agent tools, Skills, MCP servers and hooks before adoption. Use for dependency provenance, least-privilege setup, isolated trials, and rollback planning.
---

# Secure tool adoption

For each proposed integration:

1. Pin canonical repository and version; inspect LICENSE, provenance and changelog.
2. Read every executable entry point, install step, hook, SKILL.md and MCP server configuration.
3. Assess permissions, outbound requests, secret handling, telemetry and potential persistence.
4. Confirm target platform and runtime, and whether services require subscriptions or provider keys.
5. Test isolated with synthetic data, record commands and outcomes, estimate rollback.
6. Ask for explicit approval before global installation, credentials, paid services or production changes.
7. Never mark a tool secure or tested based solely on stars or GitHub license metadata.

## Evidência para a decisão

- Para o artefato ou versão escolhida, liste processos iniciados, gatilhos, destinos de rede, dados acessados, arquivos escritos e mecanismo de desativação. Inclua scripts de instalação e dependências que executam código.
- Teste com permissões mínimas num ambiente descartável. Exerça inicialização, operação comum, falha com permissão negada e remoção. Compare arquivos e processos antes e depois.
- Registre versão ou hash, escopo autorizado, comandos executados e pendências. Quando uma dependência muda, refaça as verificações afetadas.

No installations are performed by this Skill itself.
