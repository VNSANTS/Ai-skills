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

1. Use o Windows PowerShell 5.1 ou posterior e a distribuição completa do Git for Windows, que inclui o Git Bash. Clone seu `VNSANTS/Ai-skills` em um disco com espaço para a cópia de trabalho e os objetos Git da revisão. Não execute um comando de clone recursivo.
2. A partir da raiz local da biblioteca, execute o importador PowerShell revisado em `scripts/import-repository-snapshot.ps1`:
   
   ```powershell
   powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\import-repository-snapshot.ps1
   ```
3. Por padrão, o script usa a branch `main` de `ctresb/leis`. Ele extrai os arquivos rastreados em uma pasta temporária, compara os nomes e os bytes com a árvore do commit e grava `NEXUS_BACKUP_MANIFEST.md` com origem, branch, commit e contagem. Só então publica a pasta em `repositories/leis/`. Uma nova execução preserva um destino já existente e informa o conflito.
4. Revise o diretório, confirme a licença, espaço disponível, LFS e limites do GitHub (especialmente arquivos acima de 100 MB), depois:
   
   ```powershell
   git add -- repositories/leis
   git commit -m "backup: archive ctresb/leis tracked files"
   git push origin main
   ```
5. **Só chame de backup concluído após o push e uma verificação de que os arquivos podem ser baixados independentemente do original.**

O snapshot preserva os bytes registrados na revisão escolhida. O script interrompe a importação quando encontra um submódulo, link simbólico, ponteiro Git LFS ou conflito com o nome do manifesto. Para arquivar uma origem com Git LFS, obtenha e confira também os objetos referenciados. No Windows, um arquivo executável Unix pode ser gravado como arquivo comum. Para preservar o histórico integral, use `git clone --mirror` ou `git bundle` em armazenamento compatível com o volume.

Para testar o importador sem baixar a coleção, execute o comando abaixo com Python 3 e Git. A suíte cria repositórios Git temporários no próprio computador. No Windows, ela chama a interface PowerShell acima e testa junções de diretório. No Linux, ela executa o mesmo auxiliar Bash que faz a importação.

```console
python -m unittest discover -s tests -p test_import_repository_snapshot.py -v
```

### Outros repositórios do catálogo

O projeto tem outros registros em `INDEX.md`, `catalog/` e `tools/` que apontam para fontes externas. Eles são **metadados, links e fichas locais**, não clones. A verificação na árvore Git do `Ai-skills` encontrou somente um submódulo, o `leis`, que foi removido. O importador aceita `-Source`, `-Branch` e `-Destination` para importar individualmente outros projetos, respeitando capacidade e licença.

Antes de citar legislação em decisões reais, confira a norma em sua publicação oficial. O próprio projeto de origem avisa que OCR e conversões podem conter erros.
