---
name: android-pwa-release
description: Prepare and verify Android APK and PWA releases for shared web codebases. Use for Capacitor builds, signing checks, OAuth or deep-link regressions, and staging smoke tests.
---

# Release Android e PWA

1. Identifique o commit, o ambiente, o gerenciador de dependências e os comandos de build definidos no projeto. Confirme pacote e versão do Android, origem pública da PWA e os destinos esperados de autenticação.
2. Gere o build web com as variáveis do ambiente escolhido. Em projetos Capacitor, sincronize o Android depois do build web e verifique se o artefato inclui os assets recém-gerados.
3. Confirme variante, versão, hash e certificado do APK usando as ferramentas do projeto. Em atualização, compare o certificado com a versão distribuída e confira a progressão do código de versão. Preserve chaves e senhas fora de logs e commits.
4. Teste Android e navegador separadamente. Exercite login, retorno OAuth, expiração de sessão e recuperação de senha conforme o escopo. Na PWA, verifique carregamento após uma atualização do service worker, se houver. No Android, verifique atualização sobre a versão anterior quando esse for o caminho de distribuição.
5. Registre o ambiente, o dispositivo ou emulador usado, os resultados e o artefato correspondente. Publique somente no destino autorizado.

Exemplo: se a PWA retorna ao domínio de staging após OAuth, trace a origem usada no frontend, as URLs permitidas no provedor e a rota de callback antes de mudar regras que também atendem ao Android.
