# Brasil IPTV 🇧🇷

Projeto comunitário e open-source para organizar canais brasileiros gratuitos e autorizados.

O objetivo é disponibilizar playlists M3U/M3U8, EPG XMLTV, logos e um catálogo web, com atualizações e validações automatizadas.

## 🇧🇷 Objetivos

- Reunir canais brasileiros com autorização verificável.
- Organizar canais por categoria.
- Disponibilizar playlists M3U e M3U8.
- Organizar programação EPG no formato XMLTV.
- Validar links de transmissão.
- Automatizar atualizações com GitHub Actions.
- Manter o projeto gratuito e aberto à comunidade.

## ⚖️ Regras de autorização

Só serão adicionados canais quando houver evidência de autorização para retransmissão ou redistribuição.

A existência de uma transmissão pública na internet não significa autorização automática para incluí-la em uma playlist IPTV.

Não serão utilizados:
- Links privados ou protegidos.
- Streams com tokens ou credenciais.
- Fontes sem procedência verificável.
- Conteúdo sem autorização de redistribuição.

## 📺 Categorias

- Canais públicos
- Canais educativos
- Canais legislativos
- Canais universitários
- Canais culturais
- Canais regionais
- Canais comunitários

## 📂 Estrutura do projeto

```text
Brasil-IPTV/
├── sources/
│   ├── channels.json
│   ├── playlists.json
│   └── epg_sources.json
├── scripts/
├── output/
├── reports/
├── site/
├── tests/
└── .github/
    └── workflows/
