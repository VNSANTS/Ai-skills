# Instalação de Skills e ferramentas de agentes

**Catalogar não instala.** Esta pasta documenta como instalar, testar, desativar e remover ferramentas em ambientes próprios (Termux, Linux, Windows, Codex CLI, Claude Code etc.). Instalação no terminal não significa instalação permanente dentro do ChatGPT.

## Método observado: npx

No Termux foi observado o comando:

```sh
npx rea-agents setup
```

A captura de tela mostrou que o npm pediu confirmação para obter `rea-agents@6.8.0`. **Isso não comprova que o pacote foi instalado, que o setup terminou ou que é seguro.** A identidade do mantenedor, o código, a licença, os scripts de instalação e os efeitos de `setup` ainda precisam ser verificados. **Não execute novamente apenas por estar neste catálogo.**

### Antes de executar um setup

```sh
node --version
npm --version
npm view rea-agents@6.8.0 name version repository homepage license dist.integrity scripts --json
```

Verifique também o código-fonte do pacote, os scripts npm, o comportamento do instalador e quais arquivos globais/locais ele modifica. `npm view` consulta metadados; não é auditoria de segurança. Evite `sudo`, acesso root, chaves reais ou executar comandos remotos sem inspeção.

## Outras formas de instalar (dependem do projeto)

| Método | Exemplo ilustrativo | Atenção |
|---|---|---|
| npm/npx | `npx <pacote> --help` | Pode baixar e executar código; não é somente leitura |
| pip/uv | `uv tool install <pacote>` | Fixar versão e conferir scripts e dependências |
| Git clone | `git clone <url>` | Clonar não habilita Skills automaticamente |
| Skills locais | Copiar uma pasta com `SKILL.md` para o diretório reconhecido pelo agente | Local varia por agente/versão |
| MCP | Registrar servidor no arquivo de configuração do agente | Pode executar processos e receber dados/chaves |
| Hooks | Habilitar após revisão do script e escopo | Pode executar automaticamente em cada tarefa |

**Não usar `curl ... | sh` sem auditoria.** Consulte a documentação oficial de cada agente para os diretórios e comandos corretos, pois mudam com versões.

## Verificação e rollback

1. Registrar versão, origem, hash e arquivos alterados antes do setup.
2. Testar com projeto descartável, sem credenciais e sem permissões de root.
3. Confirmar qual agente detecta a Skill ou ferramenta, executando um caso de teste reproduzível.
4. Conferir consumo de tokens e chamadas externas, quando possível.
5. Documentar como desabilitar/remover o pacote, os hooks, os arquivos de configuração e o cache sem afetar outros projetos.
6. Não declarar "instalado" apenas porque o npm exibiu uma confirmação de download.

## Integração com esta biblioteca

As Skills autorais ficam em `skills/<nome>/SKILL.md`. Elas podem ser copiadas **depois de inspecionadas** para o local aceito pelo agente de destino. O catálogo de ferramentas externas está em `INDEX.md`; seus links não são instaladores.

**Política:** custo adicional R$ 0; nenhuma API paga, fallback pago, root ou alteração global automática. Leia [política de adoção](../docs/ADOPTION_POLICY.md).
