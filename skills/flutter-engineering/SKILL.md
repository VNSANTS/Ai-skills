---
name: flutter-engineering
description: Implement and review Flutter changes involving widgets, state, navigation, offline sync, accessibility, and performance. Use for lifecycle bugs, responsive screens, and stable mobile flows.
---

# Flutter engineering and quality

## Workflow
- Identify actual Flutter/Dart versions and packages before recommending APIs.
- Select state management and persistence based on current project constraints, not a universal default.
- Handle lifecycle, cancellation, retries, error states and secure local storage.
- Validate responsive layout, screen reader semantics and performance on target hardware.
- Run analyzer and focused widget/integration tests when available.
- Never claim compatibility or benchmark results without execution.

## Mudanças de estado e validação

- Localize o responsável pelo estado da tela e pelo dado persistido. Trate transições de carregamento, conteúdo, vazio e erro, incluindo refresh com conteúdo prévio.
- Exercite duas requisições fora de ordem e a saída da tela durante uma operação. Só a requisição vigente, com a tela ativa, pode exibir o resultado, mostrar um erro ou encerrar o indicador de carregamento. Inclua uma falha antiga que chega depois do sucesso mais recente.
- Mantenha a inscrição no ciclo de vida correto e preserve rascunhos quando o fluxo exigir.
- Se houver sincronização offline, teste gravação local, fila, reconexão, reenvio e conflito. Confirme os estados com teste de widget ou integração e registre o dispositivo quando verificar desempenho real.

## Source and status
- Adapted from user-provided original Markdown documents: 01_FLUTTER_CORE.md, 02_FLUTTER_DATA.md, 03_FLUTTER_QUALITY.md.
- This is a **reviewed derivative**, not a verbatim copy of internal/confidential source material.
- Rascunho aplicado explicitamente no Codex a um modelo de ciclo de vida em Python. Análise Dart, testes de widget e desempenho em aparelho continuam pendentes.
- Verify tools, versions and official docs in the target environment before execution.
- No third-party code or dependency is bundled.
