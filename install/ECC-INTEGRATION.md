# ECC (Everything Claude Code): integração e instalação

Fonte: https://github.com/affaan-m/ECC

Status: **já referenciado no catálogo Ai-skills; guia de instalação adicionado; não instalado automaticamente em dispositivos ou no ChatGPT**.

## Objetivo

Usar os agentes, skills e comandos do ECC como biblioteca opcional, sem importar centenas de instruções para o contexto de uma vez, nem executar hooks de terceiros sem auditoria.

## Instalação local (procedimento conservador)

1. Abra o repositório oficial e confira README, LICENSE, CHANGELOG e instruções atuais.
2. Em um diretório de teste sem segredos, clone: `git clone https://github.com/affaan-m/ECC.git`.
3. Inspecione scripts de instalação, hooks, MCPs e comandos antes de habilitá-los. **Clonar não significa instalar no Claude Code/Codex.**
4. Escolha apenas as skills pertinentes e siga o mecanismo de instalação suportado pela versão atual do agente; teste primeiro em ambiente descartável.
5. Confirme que o agente reconhece os recursos com um teste simples e registre versão/commit e rollback.

## Compatibilidade e custos

- Claude Code: projeto de origem; conferir instruções e versão.
- Codex CLI e Gemini CLI: compatibilidade não presumida; adaptar somente recursos portáveis após revisão.
- ChatGPT: este repositório não instala skills diretamente na sessão ou no serviço.
- Orçamento adicional: R$ 0. Não configurar provedores pagos nem fallback pago.

## Checklist de segurança

- [ ] Fixar commit e conferir licença dos componentes reutilizados
- [ ] Auditar hooks, scripts, permissões e chamadas externas
- [ ] Verificar duplicações com as skills existentes
- [ ] Instalar somente componentes selecionados em ambiente isolado
- [ ] Executar smoke test e documentar remoção

**Observação:** quantidades de agentes/skills/comandos variam conforme a versão; não tratar números divulgados em redes sociais como inventário verificado.
