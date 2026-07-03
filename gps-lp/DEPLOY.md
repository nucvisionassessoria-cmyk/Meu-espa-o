# Deploy — Landing Pages Programa GPS (Hostinger)

## Estrutura da pasta (esta pasta `gps-lp/` = raiz do site)
```
gps-lp/
├── index.html          → LP P1 (Empresário)          → seudominio.com/
├── p2/index.html       → LP P2 (RH · Gestão · Jurídico) → seudominio.com/p2/
├── p3/index.html       → LP P3 (Profissional do nicho)  → seudominio.com/p3/
└── assets/             → FOTOS E LOGOS (compartilhados pelas 3 LPs)
    ├── README.md       → nomes exatos de cada arquivo
    ├── cidinei-hero.jpg
    ├── cidinei-autoridade.jpg
    ├── ebook-capa.jpg
    ├── prova-sbt.jpg
    ├── prova-globo.jpg
    ├── prova-cdl.jpg
    ├── galeria-bora.jpg
    ├── galeria-publico.jpg
    └── galeria-sicoob.jpg
```

## Passo a passo na Hostinger (hPanel → Gerenciador de Arquivos)
1. Entre em **hPanel → Sites → Gerenciador de Arquivos** e abra a pasta **`public_html`**.
2. **Envie o CONTEÚDO da pasta `gps-lp/`** (não a pasta em si) para dentro de `public_html`:
   - `index.html`, a pasta `p2/`, a pasta `p3/` e a pasta `assets/`.
   - Dica: compacte `gps-lp` em .zip, suba o .zip em `public_html`, extraia e mova o conteúdo pra raiz (ou suba já extraído).
3. Coloque as **fotos** dentro de `public_html/assets/` com os nomes exatos do `assets/README.md`.
4. Pronto:
   - **P1** → `https://seudominio.com/`
   - **P2** → `https://seudominio.com/p2/`
   - **P3** → `https://seudominio.com/p3/`

## Observações
- É um site **estático** (HTML/CSS/JS puro) — não precisa de Node, PHP nem banco.
- As 3 LPs usam **a mesma pasta `assets/`** (P2/P3 apontam para `../assets/`).
- O botão de compra abre o **checkout Greenn** em nova aba, com UTM por público
  (`utm_content=p2_rh_juridico` / `p3_profissional`) para você separar as conversões.
- HTTPS: ative o SSL grátis da Hostinger (hPanel → Segurança → SSL).
- Enquanto as fotos não sobem, cada slot mostra um placeholder premium (nada quebra).
