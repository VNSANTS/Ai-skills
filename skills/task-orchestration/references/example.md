# Exemplo de orquestração

Pedido fictício: "Pegue os cinco CSVs públicos desta pasta, gere uma planilha mensal e prepare um resumo para a equipe". O projeto usa Python para importação, não expõe seleção de modelo e permite criar arquivos locais. O usuário pediu preparação, então o resumo é entregue como rascunho.

## Brief

Entregar uma planilha com totais mensais reconciliados e um resumo com resultados e limitações. Preservar os CSVs de origem. Descobrir moeda e período pelos arquivos ou pelas instruções do projeto. Se duas moedas aparecem sem regra de conversão, revisar os totais por moeda e pedir decisão apenas se um total combinado for obrigatório.

## Roteiro

| Etapa | Depende de | Recursos | Aceite |
|---|---|---|---|
| Inventariar entradas e definir colunas | Pedido | Coordenador, leitura de arquivos, data-quality-analysis | Esquema, unidade e chaves registrados |
| Gerar a planilha | Esquema | Executor de dados, Python e ferramenta de planilha disponível | Saída abre e os totais batem com as fontes |
| Conferir regras de negócio | Esquema | Revisor somente leitura, data-quality-analysis | Chaves, nulos, moedas e exceções documentados |
| Preparar resumo | Planilha e revisão | Executor, document-editing | Números e período correspondem à versão final |
| Integrar e conferir | Todas | Coordenador, deliverable-review | Planilha e rascunho conferidos e entregues |

A geração e a revisão de regras podem começar juntas após fechar o esquema. Ambas comunicam incompatibilidades ao coordenador, que atualiza o esquema antes da nova exportação. Se agentes não estiverem disponíveis, o coordenador faz as duas etapas em sequência. O modelo fica como automático neste ambiente.

## Falhas e recuperação

Se uma exportação for interrompida, verifique se o arquivo de saída está completo antes de reexecutar. Gere a nova planilha em uma saída separada e faça a conferência antes de substituir a versão de entrega. Se há uma linha repetida com o mesmo valor e descrição, confirme a chave da transação antes de removê-la. Atualize o resumo somente com totais validados.
