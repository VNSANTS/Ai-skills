# Verificação de 25 de novembro de 2026

As 34 skills próprias foram aplicadas a exercícios com entradas sintéticas. A tabela registra o que foi observado e onde a cobertura termina.

| Área | Evidência |
|---|---|
| Orquestração, dados e documentos | Um coordenador integrou dois CSVs e um agente independente refez o cálculo em centavos. Das dez linhas, seis eventos somaram R$ 20,10 líquidos, duas linhas eram cópias e duas continham valores conflitantes. O resumo distinguiu mês sem dados de mês com valor zero. Em outro caso, uma decisão sobre a data de competência mudou a distribuição mensal. O texto revisado preservou os trechos exigidos. |
| Engenharia | Duas conexões SQLite disputaram a última unidade. Uma falha intermediária preservou o estoque e a repetição do pedido produziu um único efeito. Um grafo Git com mudanças na base distinguiu um check antigo do resultado da integração. Também foram exercitados a ordem dos testes, estados assíncronos obsoletos, 32 casos de acesso a dados e fontes em conflito em uma busca. |
| Android e PWA | Um teste de JavaScript em Node simulou os eventos do service worker e o cache da aba antiga. Uma comparação de hashes detectou um pacote com recurso desatualizado. Assinatura Android, navegador móvel, OAuth real, PostgreSQL/Supabase e execução em Flutter precisam de validação no produto de destino. |
| Planejamento, pesquisa e operação | Um piloto sintético revelou um registro ausente. Amostras com contagens iguais também revelaram ID duplicado, substituição de ID e horário alterado. A autorização para operar mudou durante o exercício. A retomada conferiu sua versão, o escopo e as fontes antes de prosseguir. |
| Design, educação e comunicação | Uma oficina fictícia gerou um questionário, uma folha A4, quatro telas de projeção e uma faixa. O formulário foi percorrido por teclado no Qt WebEngine. As oito combinações de resposta produziram as pontuações previstas. Em seis combinações de largura e tamanho de texto, a tabela coube inclusive com texto a 200% em uma janela de 320 px. Projeção em sala e aprendizagem de um público real exigem observação no local. |
| Automação e desenho de testes | O importador trabalha sobre um repositório Git temporário. A suíte cobre seleção de branch, comparação dos bytes, conflito no destino, falha e repetição, duas importações simultâneas e entradas cujo conteúdo completo não está no commit. |

O [exercício de recebimentos](../examples/recebimentos/README.md) disponibiliza as mesmas entradas usadas no teste de orquestração e os critérios para repetir a conferência.

O [índice](../INDEX.md) contém os metadados consultados no GitHub para 147 projetos. Quatro nomes históricos foram reconciliados pelo ID estável e três caminhos antigos responderam HTTP 404. Os projetos de terceiros têm avaliação documental. As [fontes do Instagram](../INDEX.md#skills-descobertas-no-instagram) e os [vídeos do YouTube](../INDEX.md#skills-e-ferramentas-descobertas-no-youtube) permitem conferir as demonstrações. O custo em tokens de modelos e a economia em projetos de produção não foram medidos.

## Reproduzir os testes

Na raiz do repositório, use Python 3.11 ou posterior e Git. O catálogo pode ser validado só com a biblioteca padrão. Para validar Markdown e YAML, instale as dependências no ambiente Python escolhido.

```console
python scripts/validate_catalog.py
python -m pip install -r scripts/requirements-validation.txt
python scripts/validate_library.py
python -m unittest discover -s tests -v
```

O validador verifica metadados, IDs e aliases, arquivos de skill e sua presença no índice, links locais, âncoras Markdown e projetos anunciados no índice externo. Os testes do importador criam repositórios locais descartáveis. No Windows, eles chamam a interface PowerShell com Git for Windows instalado. A CI também abre um projeto Git descartável com o Codex CLI 0.172.0 e solicita a lista de skills sem iniciar um turno de modelo. Com essa versão disponível no PATH, rode `python scripts/check_codex_discovery.py` para repetir a descoberta. O binário usado na CI vem do [release oficial](https://github.com/openai/codex/releases/tag/rust-v0.172.0) e é conferido pelo SHA-256. Os resultados por revisão ficam no [GitHub Actions](https://github.com/VNSANTS/Ai-skills/actions/workflows/catalog-validation.yml). O procedimento e os limites da cópia de arquivos externos estão no [guia de importação](EXTERNAL_REPOSITORIES.md).
