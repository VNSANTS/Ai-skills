# Prompt reutilizável — pesquisar e catalogar recursos de IA

Pesquise fontes primárias para encontrar ferramentas, Skills, MCPs, agents, hooks, regras, prompts, SDKs e bibliotecas relevantes para o objetivo atual.
1. Consulte INDEX.md, catalog/*.json e docs/UNRESOLVED.md; evite duplicatas.
2. Priorize repositórios oficiais, boa manutenção e comunidade ativa; estrelas são apenas critério de descoberta.
3. Confirme nome canônico, URL, descrição, licença detectada, data da última atualização e estrelas com data da consulta.
4. Identifique tipos corretamente. Não classifique framework/SDK como Skill.
5. Sinalize riscos: licenças restritivas, scripts remotos, hooks, MCPs com acesso amplo, exfiltração, telemetria, dependências e provedores pagos.
6. Registre recursos no JSON da categoria com status metadata-verified-only; sem instalação.
7. Execute scripts/validate_catalog.py; atualize INDEX.md e checkpoint. Não altere produção.
8. Limite custo adicional a R$ 0 e não inicie modelos pagos nem fallback automático.
Entregue relatório breve: adicionados, já existentes, não confirmados e testes realmente feitos.
