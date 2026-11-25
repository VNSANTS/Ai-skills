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
- Exercite duas requisições fora de ordem e saída da tela durante uma operação. Descarte respostas obsoletas, mantenha a inscrição no ciclo de vida correto e preserve rascunhos quando o fluxo exigir.
- Se houver sincronização offline, teste gravação local, fila, reconexão, reenvio e conflito. Confirme os estados com teste de widget ou integração e registre o dispositivo quando verificar desempenho real.

## Source and status
- Adapted from user-provided original Markdown documents: 01_FLUTTER_CORE.md, 02_FLUTTER_DATA.md, 03_FLUTTER_QUALITY.md.
- This is a **reviewed derivative**, not a verbatim copy of internal/confidential source material.
- **Status:** draft; not functionally tested in Codex/Claude/ChatGPT.
- Verify tools, versions and official docs in the target environment before execution.
- No third-party code or dependency is bundled.
