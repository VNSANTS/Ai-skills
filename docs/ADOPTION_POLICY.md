# Admissão, segurança, licença e custo

## O que cada status significa
- **metadata-verified-only:** proprietário/nome, URL, estrelas, atividade e SPDX extraídos da API do GitHub. **Não** significa inspeção de código, testes, reputação ou licença aprovada.
- **unverified:** identidade ou metadados insuficientes; nenhuma instalação.
- **installed/tested:** somente após evidência rastreável (ambiente, versão, comando, resultado e revisão de permissões). Nenhum recurso externo recebe essa marca no catálogo atual.

## Portas obrigatórias para instalar/importar
1. Identificar repositório canônico, release/commit e finalidade; evitar forks desconhecidos.
2. Ler o texto integral de LICENSE/NOTICE e conferir dependências e arquivos redistribuídos. Campo `license` da API é só pista.
3. Inspecionar todos os arquivos executáveis relevantes: `SKILL.md`, hooks, instaladores, scripts, pipelines e configurações MCP. Revisar exfiltração, curl-pipe-shell, alterações de PATH/config global, atualização automática e telemetria.
4. Conferir compatibilidade no ambiente alvo (Windows 10, Termux/Ubuntu ARM64, Codex CLI, Claude Code, etc.).
5. Usar ambiente descartável sem chaves reais; observar alterações no filesystem, rede e permissões. Registrar versão e hash.
6. Exigir autorização explícita para instalar hooks globais, alterar agentes, tocar produção, armazenar credenciais, usar segurança ofensiva ou comprar serviços.
7. Manter orçamento adicional R$ 0, sem fallback para modelos pagos. Uso de software gratuito não garante serviço gratuito: verificar cotas, taxas, requisitos e termos vigentes.
8. Documentar testes e falhas, não superestimar economia de tokens e conferir funcionalidades com testes equivalentes.

## Observações relevantes
- **RTK:** documentação atual diferencia binários/funcionalidades Apache-2.0 e BUSL-1.1. Não presumir que toda edição tem somente a licença mostrada no GitHub.
- **Headroom:** atua sobre conteúdo enviado aos modelos; revisar configuração de proxy, armazenamento local e roteamento de chaves antes de adotar.
- **FreeLLMAPI:** pode agregar planos gratuitos, mas a validade das cotas, termos de cada provedor e roteamento de chaves devem ser verificados. Não ativar serviços pagos.
- **Strix:** testes de segurança apenas com autorização expressa e alvo dentro do escopo.
- **Postiz:** hospedagem e APIs externas podem custar; nenhuma implantação pressuposta.
- **Conteúdo bíblico:** separar correção textual verificável de divergências denominacionais; não alterar doutrina sem consentimento.

## Direitos de terceiros
Catálogo com links/metadados autorais é distinto de copiar Skills, vídeos, prompts e scripts protegidos. Não há espelhamento de terceiros. Manter atribuição e cumprir restrições de cada licença em futuras importações.
