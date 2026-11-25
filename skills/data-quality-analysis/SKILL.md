---
name: data-quality-analysis
description: Inspect tabular data, reconcile totals, and produce reproducible analyses. Use for CSVs, spreadsheets, exports, and KPI discrepancies.
---

# Conferir dados e reconciliar totais

1. Identifique o que cada linha representa, a chave, o período coberto, as unidades e as regras de cálculo. Leia a política da fonte, inclusive qual data controla o período. Preserve os dados brutos e conserve uma referência ao arquivo e à linha ou ao identificador de origem. Trabalhe em memória ou em uma cópia.
2. Confira esquema, datas, valores ausentes, tipos e faixas. Examine a cardinalidade antes e depois de unir tabelas. Em exportações sobrepostas, agrupe pela chave e compare os campos relevantes. Distinga cópias idênticas de versões conflitantes. IDs distintos podem ter o mesmo valor. Resolva os conflitos segundo a regra da fonte. Na falta de regra, isole as versões em disputa, quantifique o impacto e esclareça a decisão que alterar o resultado.
3. Faça as contas com unidades compatíveis. Para dinheiro, use decimal exato ou unidades inteiras da moeda e aplique a convenção de sinais da fonte. Antes de preencher meses sem registros com zero, confirme a cobertura do período. Se a cobertura for desconhecida, declare a lacuna.
4. Reconcilie o número de linhas de entrada com as contadas, as cópias removidas e as demais exclusões. Recalcule os totais por grupo e do período. Para explicar diferenças, indique regra, registros afetados e origem. Confira se a versão exportada preserva cabeçalho, precisão, codificação e ordenação exigidos.
5. Entregue o resultado no formato pedido, com as premissas e os limites que afetam sua leitura. Mantenha as evidências necessárias para reproduzir cada total.
