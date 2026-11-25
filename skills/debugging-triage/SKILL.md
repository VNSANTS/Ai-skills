---
name: debugging-triage
description: Diagnose application failures, regressions, and flaky tests. Use for logs, broken builds, runtime errors, and behavior that changed across revisions.
---

# Debugging Triage

1. Registre comportamento esperado, observado, revisão e menor cenário que manifesta o problema no aplicativo.
2. Isole a primeira falha causal com evidência do ambiente, histórico e código. Formule hipóteses com verificações que possam refutá-las.
3. Se um teste for intermitente, compare a execução isolada com a execução na suíte. Registre a ordem, a semente quando houver e quantas tentativas falharam. Inverta a ordem para investigar estado compartilhado entre testes.
4. Corrija na origem e repita o cenário que falhava e um controle que passava antes. Registre a evidência que ainda falta se a causa continuar em aberto.
