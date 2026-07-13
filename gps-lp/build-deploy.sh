#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# build-deploy.sh — monta o pacote de produção para a Hostinger (subpastas).
# Projeto é HTML estático puro: não há bundler. "Build" = montar as pastas
# self-contained (cada LP com seu próprio assets/, caminhos relativos) + home.
#
# Uso:   bash build-deploy.sh
# Saída: gps-lp/deploy-hostinger/  (+ zips na mesma pasta)
# ---------------------------------------------------------------------------
set -euo pipefail
cd "$(dirname "$0")"                 # gps-lp/
OUT="deploy-hostinger"
rm -rf "$OUT"
mkdir -p "$OUT"

# home no domínio raiz
cp home/index.html "$OUT/index.html"
# imagem de compartilhamento (OG) da home fica na raiz
cp assets/og-share.jpg "$OUT/og-share.jpg" 2>/dev/null || true

# monta uma pasta self-contained a partir de uma LP.
#   $1 = pasta final (na public_html)   $2 = html de origem
build_folder(){
  local dst="$1" src="$2"
  mkdir -p "$OUT/$dst/assets"
  # caminhos: ../assets/ -> assets/  (P1 já usa assets/, então é no-op nele)
  sed "s#url('../assets/#url('assets/#g; s#url(\"../assets/#url(\"assets/#g" "$src" > "$OUT/$dst/index.html"
  # copia SÓ as fotos usadas (as extras ficam de fora do deploy)
  cp assets/*.jpg "$OUT/$dst/assets/" 2>/dev/null || true
  cp assets/*.png "$OUT/$dst/assets/" 2>/dev/null || true
  # vídeos: só os que essa LP realmente referencia (arquivos pesados — não espalhar pras outras)
  { grep -oE 'assets/[A-Za-z0-9_-]+\.mp4' "$src" || true; } | sort -u | while read -r v; do
    cp "$v" "$OUT/$dst/assets/" 2>/dev/null || true
  done
}

build_folder "ebookjuridico"     "p2/index.html"   # RH / Gestão / Jurídico
build_folder "ebookcnpj"         "index.html"      # Empresário / PME (CNPJ)
build_folder "ebookoportunidade" "p3/index.html"   # Profissional (oportunidade)

# ---- pacotes .zip ----
# Opção A: ecossistema inteiro (extrai dentro de public_html)
( cd "$OUT" && rm -f ../deploy-hostinger.zip && zip -qr ../deploy-hostinger.zip . )
# Opção B: um zip por LP (extrai dentro da pasta correspondente)
for d in ebookjuridico ebookcnpj ebookoportunidade; do
  ( cd "$OUT/$d" && rm -f "../../deploy-$d.zip" && zip -qr "../../deploy-$d.zip" . )
done

echo "OK — estrutura em $OUT/ e zips gerados:"
ls -1 deploy-hostinger.zip deploy-ebook*.zip 2>/dev/null
