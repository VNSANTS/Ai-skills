---
name: staged-rollout
description: Plan and verify staged changes with release gates and recovery steps. Use for publishing risky updates, transitioning workflows, or rolling out changes to software, data, and operations.
---

# Implantação gradual

## Escolha o nível de controle

Use o fluxo completo quando dados, usuários ou operações dependam da mudança. Se a alteração for pequena, local e reversível, confira a versão final e registre a forma de desfazer.

## Planeje e verifique

1. Identifique a revisão, o ambiente, o público afetado e as dependências. Determine se o estado anterior pode ser restaurado e quais dados gerados após a mudança precisam ser preservados.
2. Defina os estágios disponíveis, como teste isolado, piloto e adoção geral. Para cada estágio, registre público, janela, indicador, limiar e responsável. Inclua caminho normal e recuperação.
3. Escreva critérios para avançar, pausar ou recuperar. Em alterações irreversíveis, prove no ambiente de teste que existe uma correção à frente ou uma restauração utilizável antes do estágio que precisa dessa proteção.
4. Quando houver autorização para executar, avance por estágio e confira revisão e ambiente antes de qualquer alteração. Registre a evidência observada. Se o estágio falhar, interrompa a expansão e siga o procedimento de recuperação autorizado.
5. Verifique o resultado com sinais observáveis do público afetado. Confirme os dados gerados no intervalo, registre o estado final e encaminhe itens de monitoramento que tenham responsável.

Ao transferir registros, use o mesmo horário de corte na origem e no destino. Compare IDs e campos que precisam ser preservados. Quando um horário representar um instante, considere o fuso. Procure IDs ausentes, inesperados e duplicados mesmo quando os totais coincidirem. Se a recuperação importar dados, repita a importação em uma cópia e confira se cada registro existente ou criado no intervalo continua íntegro e aparece uma única vez.

Quando houver processo formal de implantação, use seus critérios e aprovações. Consulte [o exemplo](references/example.md) para uma transição que precisa preservar registros criados durante o piloto.
