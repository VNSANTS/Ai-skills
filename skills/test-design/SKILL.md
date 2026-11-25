---
name: test-design
description: Design focused software verification for new features, fixes, integration boundaries, and regressions.
---

# Test Design

1. Mapeie cada requisito a um resultado observável. Escolha o nível mais simples que cubra o risco e preserve testes existentes relevantes.
2. Inclua caminho normal, entradas no limite e falha recuperável. Use dados determinísticos e confira efeitos persistidos além da resposta.
3. Execute a menor suíte informativa primeiro e registre os casos, comandos, ambiente e resultados.
4. Em testes de cópia, compare os bytes com uma origem conhecida e inclua um arquivo vazio e um binário. Altere um arquivo temporário antes da verificação para confirmar que o controle detecta a diferença e que a falha preserva o destino.
