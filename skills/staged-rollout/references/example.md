# Exemplo fictício de transição de processo

Uma organização quer substituir uma planilha de pedidos por um novo formulário interno. Durante o piloto, uma equipe usa o formulário e a planilha recebe somente uma exportação de conferência, identificada como tal. Cada pedido tem identificador único.

| Estágio | Verificação | Critério de avanço |
|---|---|---|
| Teste isolado | Enviar pedidos sintéticos, exportar e conferir IDs, quantidades e datas | Todos os campos conciliados |
| Piloto autorizado | Conferir os pedidos de um turno e registrar divergências | Zero pedidos perdidos ou duplicados |
| Adoção geral | Conferir os registros no início do próximo turno | Totais conferidos e suporte disponível |

**Recuperação autorizada no piloto:** pausar novas entradas, exportar os pedidos recebidos, importar na planilha por identificador, reconciliar a contagem e reabrir o fluxo anterior. Se houver ID ausente na exportação, mantenha novas entradas pausadas até localizar e conciliar o registro.

**Caso simples:** renomear um botão interno sem mudar seu fluxo exige apenas verificar o texto na interface e preservar um caminho de reversão.
