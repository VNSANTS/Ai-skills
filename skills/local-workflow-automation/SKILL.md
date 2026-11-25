---
name: local-workflow-automation
description: Design repeatable local workflows for files, reports, and build tasks. Use to replace recurring manual steps with scripts or task runners.
---

# Local Workflow Automation

1. Capture entradas, saídas, frequência e exceções do fluxo manual. Identifique operações com efeitos externos que exigem autorização.
2. Reutilize comandos existentes e defina execução não interativa, mensagens de erro e como retomar após falha parcial. Proteja contra gravação duplicada.
3. Teste com dados sintéticos, casos vazios e reexecução. Entregue comando, dependências e forma de verificar o resultado.
4. Se a tarefa publicar um diretório, prepare e verifique os arquivos em uma pasta temporária no mesmo volume. Teste uma interrupção antes da publicação e duas execuções para o mesmo destino. Confira se o resultado já existente foi preservado.
