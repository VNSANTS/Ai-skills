---
name: ux-ui-design
description: Design or review user interfaces, accessible flows, design systems, and responsive states. Use for screen redesigns, usability audits, and interaction specifications.
---

# UX/UI design systems and patterns

## Workflow
- Start with user goals, constraints and current screens.
- Reduce cognitive load; preserve hierarchy, contrast, keyboard and touch accessibility.
- Produce concrete states for loading, empty, error and success.
- Specify responsive behavior and component tokens.
- Avoid decorative repetition, unnecessary effects and generic template styling.
- Distinguish design proposals from usability-tested findings.

## Estados e critérios de aceite

1. Identifique a ação principal e trace entrada, sucesso, falha e recuperação. Para cada estado, indique o que aparece, o foco inicial e o próximo passo disponível.
2. Reuse padrões e tokens existentes. Defina como a tela se adapta a largura estreita, texto ampliado e textos longos sem cortar ações essenciais.
3. Percorra a interface por toque e teclado. Confira rótulos acessíveis, ordem de foco, contraste e mensagens de erro vinculadas aos campos. Registre os cenários realmente inspecionados.
4. Em uma ação assíncrona, preserve os dados digitados quando houver falha, sinalize o andamento e verifique o efeito de cliques repetidos.

Em formulários, experimente uma entrada plausível na notação local, uma resposta válida porém incorreta e um campo vazio. Confirme que os valores dos outros campos sobrevivem ao erro, o foco aponta para a correção e o resultado só é atualizado após o envio.

## Source and status
- Adapted from user-provided original Markdown documents: 01_UX_UI_CORE.md, 02_UX_UI_PATTERNS.md, 03_UX_UI_TEMPLATES.md.
- This is a **reviewed derivative**, not a verbatim copy of internal/confidential source material.
- **Status:** rascunho. Registre a interface, o motor e as interações realmente exercitados.
- Verify tools, versions and official docs in the target environment before execution.
- No third-party code or dependency is bundled.
