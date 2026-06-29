# Skills — NUC Vision

Cópia versionada das skills de geração de carrossel usadas neste projeto.
Elas vivem em `/root/.claude/skills/` no ambiente de execução (config local),
mas são guardadas aqui no repo para não se perderem entre sessões.

## Skills

- **`nuc-carrossel/`** — Padrão de qualidade obrigatório (nível campanha de
  agência). Define a arquitetura narrativa (Seção 0: arco → papéis → loop aberto
  → teste de remoção) e as regras visuais anti-"cara de IA" (sombra de contato,
  profundidade por blur, grão, color match). Usa `geradores/nuc_realism.py`.
- **`radar-trends-nuc/`** — Radar de trends e roteiro estratégico (Fases A/B/C:
  estratégia → curadoria visual → montagem).
- **`oportunista-trend/`** — Radar oportunista semanal sobre `@v4company`.
  Lê o dataset de um schedule Apify semanal (`apify/instagram-scraper`),
  ranqueia por sinais públicos (comentários/likes, view count), classifica
  modo (HYPE vs TREND) com inspeção visual da imagem do post, e devolve
  roteiro adaptado pra `nuc-carrossel` produzir. Em MODO HYPE rouba palette
  e códigos visuais do evento (Copa, Olimpíada etc.). Setup único do Apify
  em `oportunista-trend/SETUP-APIFY.md`. Windsor entra só pro tracking do
  pós-publicação NUC.

## Como reinstalar (novo ambiente / nova sessão)

```bash
cp -r skills/nuc-carrossel       /root/.claude/skills/
cp -r skills/radar-trends-nuc    /root/.claude/skills/
cp -r skills/oportunista-trend   /root/.claude/skills/
```

O Claude Code detecta automaticamente qualquer diretório com `SKILL.md`
dentro de `/root/.claude/skills/`.

## Pipeline de geração (referência)

1. Assets em `fotos/` → recorte (`geradores/cutout_*.py` / `rembg`) → PNG RGBA.
2. `geradores/gen_*.py` embute as imagens em base64 e monta o HTML
   (`previews/*.html`), aplicando `nuc_realism.py`.
3. `geradores/export_*.py` (Playwright/Chromium, 420×525 @ 2.571×) exporta os
   PNGs finais 1080×1350 em `output/`.
