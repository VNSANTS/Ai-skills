# Repositórios externos: estado real dos backups

> **Situação em 22/11/2026:** os repositórios listados nesta biblioteca são referências e fichas. **Não existem backups independentes desses repositórios armazenados aqui.**

## ctresb/leis

- **Origem:** https://github.com/ctresb/leis
- **Conteúdo:** legislação brasileira em Markdown, com documentos convertidos automaticamente/OCR
- **Destino solicitado:** `repositories/leis/` (conteúdo real, não Git submodule)
- **Estado atual:** **PENDENTE DE IMPORTAÇÃO COMPLETA**; o submódulo Git anterior foi removido
- **GitHub consultado:** 22/11/2026, 2.940 estrelas (snapshot de popularidade), último push informado 2026-11-02 17:54:35 UTC
- **Commit da origem conferido:** `c9f21b4ab11aa0d7ca6fe861d75028e94219c2d6`
- **Tamanho GitHub informado:** 8.582.635 KB (aprox. 8,2 GiB, que não é o tamanho garantido da pasta extraída)
- **Licença:** a API retorna `Other/NOASSERTION`; o arquivo LICENSE declara MIT para o código em `scripts/`, e esclarece o estatuto de atos oficiais reproduzidos
- **Verificações:** proprietário, metadados, árvore de topo e licença lidos. Código e textos jurídicos não foram auditados.

### Por que não foi copiado diretamente

A conexão disponível para alterações no GitHub não oferece transferência massiva/clone Git ou importação de milhares de arquivos. O repositório de origem é gigantesco, com histórico de muitos commits. Tentar fingir uma cópia com submódulo ou alguns arquivos causaria falsa sensação de segurança. Não há confirmação de que o repositório de destino possa acomodar o conteúdo nos limites de arquivos, tamanho total ou cotas do GitHub.

### Importar arquivos completos (snapshot independente) pelo Windows

1. Clone seu `VNSANTS/Ai-skills` em um disco com espaço suficiente. Não execute um comando de clone recursivo.
2. A partir da raiz local da biblioteca, execute o importador PowerShell revisado em `scripts/import-repository-snapshot.ps1`:
   
   ```powershell
   powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\import-repository-snapshot.ps1
   ```
3. O script baixa o estado integral dos **arquivos rastreados** da branch `main` de `ctresb/leis`, copia para `repositories/leis/` sem o diretório `.git`, verifica a presença dos arquivos e registra o commit de origem.
4. Revise o diretório, confirme a licença, espaço disponível, LFS e limites do GitHub (especialmente arquivos acima de 100 MB), depois:
   
   ```powershell
   git add -- repositories/leis
   git commit -m "backup: archive ctresb/leis tracked files"
   git push origin main
   ```
5. **Só chame de backup concluído após o push e uma verificação de que os arquivos podem ser baixados independentemente do original.**

**Limitação:** esse processo preserva os arquivos da revisão escolhida, não os 323 mil+ commits históricos, branches e tags; para preservar também o histórico integral, é necessário `git clone --mirror` / `git bundle` em armazenamento compatível com o volume, fora de uma pasta Git comum. Se existirem objetos Git LFS, eles também devem ser obtidos e validados antes de afirmar completude.

### Outros repositórios do catálogo

O projeto tem outros registros em `INDEX.md`, `catalog/` e `tools/` que apontam para fontes externas. Eles são **metadados, links e fichas locais**, não clones. A verificação na árvore Git do `Ai-skills` encontrou somente um submódulo, o `leis`, que foi removido. O importador aceita `-Source`, `-Branch` e `-Destination` para importar individualmente outros projetos, respeitando capacidade e licença.

Antes de citar legislação em decisões reais, confira a norma em sua publicação oficial. O próprio projeto de origem avisa que OCR e conversões podem conter erros.
