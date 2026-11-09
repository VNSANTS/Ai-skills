# Hooks de agentes — política de segurança

Hooks executam ações em momentos do ciclo do agente e podem interceptar comandos, outputs e arquivos. Portanto **não habilitar hooks globalmente por padrão**.

Exemplos úteis a investigar: compressão de saída do RTK, instrumentação de tokens, bloqueio de comandos destrutivos e revisão de segredos. Antes de ativar: ler o código, verificar edições, usar `--dry-run` quando existir, testar em projeto temporário e preservar desinstalação/rollback.

Não copiar configurações diretamente da internet sem confirmar versões e escopos. Nenhum hook externo foi instalado por este catálogo.
