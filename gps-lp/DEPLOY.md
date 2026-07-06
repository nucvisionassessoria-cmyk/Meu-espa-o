# Deploy — Ecossistema Programa GPS (Hostinger · hospedagem compartilhada)

Projeto **HTML estático puro** (sem framework/bundler). O "build" apenas monta
pastas **self-contained** (cada LP com seu próprio `assets/` e caminhos
relativos), prontas para subir em subpastas da `public_html` — sem editar nada
depois do upload.

## Mapa das páginas
| Pasta na Hostinger | URL final | = LP interna | Público |
|---|---|---|---|
| `/` (raiz) | cidineimartins.com.br | `home/` | Hub — links para as 3 |
| `ebookjuridico/` | /ebookjuridico | `p2/` | RH · Gestão · Jurídico |
| `ebookcnpj/` | /ebookcnpj | `index.html` (P1) | Empresário / PME |
| `ebookoportunidade/` | /ebookoportunidade | `p3/` | Profissional da área |

## Gerar o build
```bash
cd gps-lp
bash build-deploy.sh
```
Gera `gps-lp/deploy-hostinger/` e os zips:
```
deploy-hostinger/
├── index.html                (home)
├── ebookjuridico/   index.html + assets/
├── ebookcnpj/       index.html + assets/
└── ebookoportunidade/ index.html + assets/
```
+ `deploy-hostinger.zip` (ecossistema inteiro) e um zip por LP
(`deploy-ebookjuridico.zip`, `deploy-ebookcnpj.zip`, `deploy-ebookoportunidade.zip`).

## Subir na Hostinger (hPanel → Gerenciador de Arquivos → `public_html`)

**Opção recomendada (por pasta):** para cada LP, entre na pasta correspondente
(crie se não existir), envie o **zip da LP** e **extraia lá dentro**:
- `deploy-ebookjuridico.zip` → dentro de `public_html/ebookjuridico/`
- `deploy-ebookcnpj.zip` → dentro de `public_html/ebookcnpj/`
- `deploy-ebookoportunidade.zip` → dentro de `public_html/ebookoportunidade/`
- home: envie o `index.html` (da raiz do `deploy-hostinger/`) direto em `public_html/`.

Cada zip contém já `index.html` + `assets/` — extraiu, funcionou.

**Alternativa (tudo de uma vez):** envie `deploy-hostinger.zip` em `public_html`,
extraia e mova o conteúdo para a raiz (ou extraia direto).

Depois ative o **SSL grátis** (hPanel → Segurança → SSL).

## Por que funciona em subpasta
- Nenhum caminho absoluto `/…`. As fotos são referenciadas como `assets/…`
  (relativo), que resolve certo em qualquer subpasta.
- Sem SPA/router, sem base path, **sem `.htaccess`** necessário (páginas estáticas).
- Links externos (checkout Greenn, Google Fonts) são `https://…` — corretos.
- Favicon é inline (data URI) — não busca `/favicon.ico`.

## Observações
- **`ebook-capa.jpg` ainda não existe** — o e-book mostra a capa em texto
  (fallback). Quando tiver a arte, coloque `assets/ebook-capa.jpg` em cada pasta.
- Fotos já otimizadas (~1600px). Cada LP pesa ~1,7 MB.
- Sem vídeos no projeto (nada pesado a otimizar).
- Pendências de marketing (não bloqueiam o deploy): Pixel/GA4, OG tags,
  depoimentos reais — ver conversa.
