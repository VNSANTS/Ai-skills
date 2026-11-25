# Primeiro teste da orquestração

Dois pontos de atendimento exportaram os recebimentos do trimestre. As planilhas têm registros em comum e uma divergência de valor. Todos os dados deste exercício são fictícios.

Dê ao agente acesso à pasta [entradas](entradas/) e à skill de orquestração. Em uma sessão nova, envie este pedido:

> Use a task-orchestration para preparar o relatório trimestral da coordenação a partir dos dois CSVs e da política em entradas/. Entregue os recebimentos por mês em CSV e um resumo em Markdown, em português. Faça a conferência de forma independente quando houver agente disponível. Grave as saídas em outra pasta.

As entradas são [east.csv](entradas/east.csv), [west.csv](entradas/west.csv) e a [política da coordenação](entradas/policy.txt). Para avaliar o agente, abra o gabarito só depois de receber os arquivos.

<details>
<summary>Conferir o resultado</summary>

| Mês | Eventos aceitos | Bruto | Reembolsos | Líquido |
|---|---:|---:|---:|---:|
| 2026-01 | 3 | R$ 20,20 | R$ 0,20 | R$ 20,00 |
| 2026-02 | 3 | R$ 4,15 | R$ 4,05 | R$ 0,10 |

As dez linhas contêm seis eventos aceitos. R01 e R02 são duas vendas legítimas de mesmo valor. As cópias idênticas de R03 e R04 contam uma vez por ID. As duas versões de R90 (R$ 7,50 e R$ 7,00) ficam fora dos totais. O líquido do período apurado é R$ 20,10. Março deve aparecer no texto como mês sem dados disponíveis.

Abra o CSV e o resumo. Confira se os números coincidem entre si e se o resumo permite localizar os registros usados e os excluídos. Compare as entradas com o original para confirmar sua preservação.

</details>
