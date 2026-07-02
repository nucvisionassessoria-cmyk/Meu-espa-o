#!/usr/bin/env python3
"""
NUC Vision — Carrossel Copa Hexa (adaptado do post V4 "Brasil rumo ao Hexa")
Modelo POLEMICA. Filosofia cover band:
  - CONTEUDO E IMAGENS = copia do V4 (Vinicius, Neymar+Ancelotti, selecao)
  - CASCA VISUAL      = NUC oficial (dark navy + ciano, Anton em manifestos
                        curtos, Space Grotesk 22px com highlight ciano em
                        palavras-chave, kicker Title Case, progress_bar,
                        slide_index, glass_card, feature_row, split hero)
Referencia: gen_apagar_incendio.py (carrossel-v1 oficial NUC).
Formato: 420x525 (exportado a 1080x1350).
"""
import sys
from pathlib import Path
sys.path.insert(0, "/home/user/Meu-espa-o")

from design_system import (
    INK, PAPER, ACCENT, GRAY, FONTS, TYPE, TRACK, LINE,
    RADIUS, SHADOW, W, H,
    bg_brand_atmo, bg_dark_atmo, bg_paper_atmo,
    overlay_noise, overlay_vignette,
    kicker, display_pill, glass_card, number_marker,
    feature_row, slide_index, progress_bar, logo_mark,
    photo_layered, photo_uri, photo_position,
    html_shell,
)

TOTAL = 8

CAPTION = (
    "A Nike gastou R$ 200 milhões pra errar a camisa do Hexa. E a lição não é "
    "sobre camisa — é sobre a diferença entre produto e narrativa. Desliza até "
    "o fim para o framework. Comente HEXA e um estrategista NUC te manda direto. "
    "@nucvision"
)


# ============================================================
# SLIDE 1 — GANCHO / SPLIT HERO
# Vinicius beijando o escudo (direita) + headline provocadora (esquerda)
# ============================================================
def slide1():
    img = photo_uri("copa_vinicius_escudo.jpg")
    return f'''<div class="slide" style="background:{INK["void"]};overflow:hidden;">
      {slide_index(1, TOTAL)}

      <!-- PAINEL DIREITO — Vinicius beijando escudo -->
      <div style="position:absolute;right:0;top:0;bottom:0;width:52%;z-index:2;">
        <img src="{img}" style="width:100%;height:100%;object-fit:cover;
                   object-position:52% 8%;filter:contrast(1.05) saturate(0.98) brightness(0.82);">
        <div style="position:absolute;inset:0;background:linear-gradient(90deg,
                    rgba(5,8,15,0.95) 0%, rgba(5,8,15,0.55) 22%,
                    rgba(5,8,15,0.10) 52%, transparent 100%);
                    pointer-events:none;"></div>
        <div style="position:absolute;inset:0;background:linear-gradient(180deg,
                    transparent 55%, rgba(5,8,15,0.72) 100%);
                    pointer-events:none;"></div>
      </div>

      <!-- PAINEL ESQUERDO — texto -->
      <div style="position:absolute;left:0;top:0;bottom:0;width:56%;z-index:10;
                  display:flex;flex-direction:column;justify-content:center;
                  padding:28px 16px 28px 24px;">

        {logo_mark(dark_bg=True, size=22)}

        <div style="margin-top:26px;">
          {kicker("Leitura de Mercado", color="rgba(255,255,255,0.55)")}
        </div>

        <div style="margin-top:14px;line-height:0.86;">
          <div class="display" style="font-size:56px;color:#fff;
                      letter-spacing:{TRACK["tight"]};
                      text-shadow:0 3px 18px rgba(0,0,0,0.55);">A NIKE</div>
          <div class="display" style="font-size:56px;color:#fff;
                      letter-spacing:{TRACK["tight"]};
                      text-shadow:0 3px 18px rgba(0,0,0,0.55);">ERROU</div>
          <div class="display" style="font-size:50px;color:{ACCENT["primary"]};
                      letter-spacing:{TRACK["tight"]};
                      text-shadow:0 3px 18px rgba(0,0,0,0.55),
                                  0 0 28px rgba(30,197,242,0.35);">A CAMISA.</div>
        </div>

        <div style="height:1.5px;width:36px;background:rgba(255,255,255,0.24);
                    margin:16px 0 14px;border-radius:2px;"></div>

        <div style="font-family:{FONTS["body"]},sans-serif;font-size:13px;font-weight:400;
                    color:rgba(255,255,255,0.68);line-height:1.52;max-width:210px;">
          R$ 200 milhões em ativação para<br>
          <strong style="color:#fff;font-weight:600;">o pior marketing de Copa do ano.</strong>
        </div>

        <div style="margin-top:16px;font-family:{FONTS["body"]},sans-serif;font-size:9px;
                    font-weight:600;color:rgba(255,255,255,0.32);
                    letter-spacing:{TRACK["label"]};text-transform:uppercase;">
          @nucvision · Copa 2026 · Posicionamento
        </div>
      </div>

      {overlay_noise(0.24, blend="soft-light", z=5)}
      {progress_bar(1, TOTAL)}
    </div>'''


# ============================================================
# SLIDE 2 — CURIOSIDADE
# Tipografia mista: Space Grotesk 22px com highlight ciano
# ============================================================
def slide2():
    return f'''<div class="slide" style="{bg_dark_atmo()}">
      {overlay_noise(0.48)}
      {slide_index(2, TOTAL)}

      <div style="position:absolute;top:50%;left:28px;right:28px;z-index:10;
                  transform:translateY(-52%);">
        {kicker("O Fato", color=ACCENT["mist"])}

        <div style="font-family:{FONTS["body"]},sans-serif;font-size:22px;font-weight:400;
                    color:rgba(255,255,255,0.70);line-height:1.22;
                    letter-spacing:{TRACK["tight"]};margin-top:16px;">
          A camisa em si
          <span style="color:#fff;font-weight:600;">agradou.</span>
        </div>
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:22px;font-weight:400;
                    color:rgba(255,255,255,0.70);line-height:1.22;
                    letter-spacing:{TRACK["tight"]};margin-top:4px;">
          A história que a Nike contou
          <span style="color:{ACCENT["light"]};font-weight:600;">não.</span>
        </div>

        <div style="height:1px;width:48px;background:rgba(255,255,255,0.22);
                    margin:24px 0 20px;"></div>

        <div class="display" style="font-size:52px;color:{ACCENT["primary"]};
                    line-height:0.86;letter-spacing:{TRACK["tight"]};
                    text-shadow:0 0 32px rgba(30,197,242,0.38);">PRODUTO CERTO,</div>
        <div class="display" style="font-size:52px;color:#fff;
                    line-height:0.86;letter-spacing:{TRACK["tight"]};">NARRATIVA</div>
        <div class="display" style="font-size:42px;color:rgba(255,255,255,0.44);
                    line-height:0.86;letter-spacing:{TRACK["tight"]};">ERRADA.</div>

        <div style="font-family:{FONTS["body"]},sans-serif;font-size:13px;
                    color:rgba(255,255,255,0.55);line-height:1.55;margin-top:18px;
                    max-width:310px;font-weight:300;">
          Gola retrô. Amarelo clássico. Geometrias da bandeira.
          <strong style="color:#fff;font-weight:600;">O torcedor não comprou a história.</strong>
        </div>
      </div>

      {progress_bar(2, TOTAL)}
    </div>'''


# ============================================================
# SLIDE 3 — A REGRA (fundo claro papel)
# ============================================================
def slide3():
    return f'''<div class="slide" style="{bg_paper_atmo()}">
      {logo_mark(dark_bg=False, size=24)}
      {slide_index(3, TOTAL, light=True)}

      <div style="position:absolute;top:74px;left:24px;right:24px;bottom:52px;
                  z-index:10;overflow:hidden;">
        {kicker("A Regra", color=ACCENT["primary"], light=True)}

        <div style="margin-top:14px;line-height:0.86;">
          <div class="display" style="font-size:54px;color:{INK["deep"]};
                      letter-spacing:{TRACK["tight"]};">MARCA NÃO SE</div>
          <div class="display" style="font-size:54px;color:{INK["deep"]};
                      letter-spacing:{TRACK["tight"]};">CONSTRÓI</div>
          <div class="display" style="font-size:48px;
                      letter-spacing:{TRACK["tight"]};
                      background:linear-gradient(120deg,{ACCENT["primary"]} 0%,{ACCENT["vivid"]} 100%);
                      -webkit-background-clip:text;background-clip:text;
                      -webkit-text-fill-color:transparent;color:transparent;">NO PRODUTO.</div>
        </div>

        <div style="height:1.5px;width:40px;background:{ACCENT["primary"]};
                    opacity:0.5;margin:14px 0 12px;border-radius:2px;"></div>

        <div style="font-family:{FONTS["body"]},sans-serif;font-size:14px;font-weight:400;
                    color:{GRAY["600"]};line-height:1.52;max-width:320px;">
          Ela nasce na
          <strong style="color:{INK["deep"]};font-weight:700;">narrativa em volta</strong>
          dele. O produto pode ser excelente — se a história que a marca conta
          não casar com o que o público sente,
          <strong style="color:{INK["deep"]};font-weight:600;">ele falha como produto cultural.</strong>
        </div>
      </div>

      {progress_bar(3, TOTAL, light=True)}
    </div>'''


# ============================================================
# SLIDE 4 — A VIRADA
# Neymar + Ancelotti com taca (card no rodape) + headline em cima
# ============================================================
def slide4():
    img = photo_uri("copa_neymar_ancelotti.jpg")
    return f'''<div class="slide" style="background:{INK["void"]};overflow:hidden;">
      {logo_mark(dark_bg=True, size=24)}
      {slide_index(4, TOTAL)}

      <!-- ZONA TEXTO — topo -->
      <div style="position:absolute;top:60px;left:28px;right:28px;bottom:236px;
                  z-index:10;overflow:hidden;">
        {kicker("A História Que Já Existia", color=ACCENT["mist"])}

        <div style="margin-top:12px;line-height:0.86;">
          <div class="display" style="font-size:50px;color:#fff;
                      letter-spacing:{TRACK["tight"]};">A NARRATIVA</div>
          <div class="display" style="font-size:50px;color:#fff;
                      letter-spacing:{TRACK["tight"]};">DO HEXA</div>
          <div class="display" style="font-size:44px;color:{ACCENT["primary"]};
                      letter-spacing:{TRACK["tight"]};
                      text-shadow:0 0 28px rgba(30,197,242,0.32);">JÁ ESTAVA PRONTA.</div>
        </div>

        <div style="height:1.5px;width:36px;background:rgba(255,255,255,0.24);
                    margin:14px 0 12px;border-radius:2px;"></div>

        <div style="font-family:{FONTS["body"]},sans-serif;font-size:13px;font-weight:400;
                    color:rgba(255,255,255,0.68);line-height:1.52;max-width:310px;">
          Maior campeã. 24 anos sem título.
          <strong style="color:#fff;font-weight:600;">O melhor técnico do mundo no comando.</strong>
          A Nike ignorou e foi inventar outra.
        </div>
      </div>

      <!-- ZONA FOTO CARD — Neymar + Ancelotti com a taca -->
      <div style="position:absolute;bottom:36px;left:22px;right:22px;height:180px;
                  border-radius:{RADIUS["xl"]}px;overflow:hidden;
                  box-shadow:0 16px 40px rgba(10,15,26,0.55),
                             0 4px 12px rgba(10,15,26,0.30);">
        <img src="{img}" style="width:100%;height:100%;object-fit:cover;
                   object-position:50% 40%;filter:contrast(1.06) saturate(1.02);">
        <div style="position:absolute;inset:0;background:linear-gradient(180deg,
                    transparent 55%, rgba(10,15,26,0.35) 100%);"></div>
      </div>

      {overlay_noise(0.28, blend="soft-light", z=5)}
      {progress_bar(4, TOTAL)}
    </div>'''


# ============================================================
# SLIDE 5 — A ATERRISSAGEM (4 sinais numerados dark)
# ============================================================
def slide5():
    return f'''<div class="slide" style="{bg_dark_atmo()}">
      {overlay_noise(0.42)}
      {slide_index(5, TOTAL)}

      <div style="position:absolute;top:60px;left:24px;right:24px;bottom:50px;
                  z-index:15;overflow:hidden;">
        {kicker("Onde Voce Esta", color=ACCENT["mist"])}

        <div style="margin-top:12px;margin-bottom:18px;">
          <div style="font-family:{FONTS["body"]},sans-serif;font-size:20px;font-weight:600;
                      color:#fff;line-height:1.12;letter-spacing:{TRACK["tight"]};">
            E a sua empresa
          </div>
          <div style="font-family:{FONTS["body"]},sans-serif;font-size:20px;font-weight:700;
                      color:{ACCENT["light"]};line-height:1.12;letter-spacing:{TRACK["tight"]};">
            está fazendo o mesmo agora.
          </div>
        </div>

        {''.join([f'<div style="margin-bottom:8px;">{feature_row(n, l, d, dark=True)}</div>'
          for n, l, d in [
            ("01", "R$ 200 milhões",       "O que a Nike gastou pra errar a Copa toda."),
            ("02", "Silêncio total",       "O que a sua marca está gastando na mesma janela."),
            ("03", "Zero rebote",           "Mesma cegueira de narrativa, escala diferente."),
            ("04", "Maior momento",         "No único mês em que o Brasil todo olha pra marca."),
          ]])}
      </div>

      {progress_bar(5, TOTAL)}
    </div>'''


# ============================================================
# SLIDE 6 — A REVELACAO (brand gradient — insight)
# ============================================================
def slide6():
    return f'''<div class="slide" style="{bg_brand_atmo()}">
      {overlay_noise(0.40)}
      {overlay_vignette(0.26)}
      {slide_index(6, TOTAL)}

      <div style="position:absolute;top:50%;left:28px;right:28px;z-index:15;
                  transform:translateY(-50%);">
        {kicker("A Diferença", color="rgba(255,255,255,0.72)")}

        <div class="display" style="font-size:46px;color:#fff;line-height:0.88;
                    letter-spacing:{TRACK["tight"]};margin-top:18px;
                    text-shadow:0 6px 28px rgba(0,0,0,0.32);">QUEM ENTENDE</div>
        <div class="display" style="font-size:46px;color:#fff;line-height:0.88;
                    letter-spacing:{TRACK["tight"]};
                    text-shadow:0 6px 28px rgba(0,0,0,0.32);">O HEXA COMO</div>
        <div class="display" style="font-size:46px;color:#fff;line-height:0.88;
                    letter-spacing:{TRACK["tight"]};
                    text-shadow:0 6px 28px rgba(0,0,0,0.32);">NARRATIVA,</div>

        <div style="height:1px;width:36px;background:rgba(255,255,255,0.30);
                    margin:14px 0 12px;"></div>

        <div class="display" style="font-size:38px;color:{ACCENT["ice"]};
                    line-height:0.88;letter-spacing:{TRACK["tight"]};
                    text-shadow:0 6px 28px rgba(0,0,0,0.32),
                                0 0 28px rgba(224,244,251,0.22);">PEGA O REBOTE</div>
        <div class="display" style="font-size:38px;color:{ACCENT["ice"]};
                    line-height:0.88;letter-spacing:{TRACK["tight"]};
                    text-shadow:0 6px 28px rgba(0,0,0,0.32),
                                0 0 28px rgba(224,244,251,0.22);">SEM PATROCINAR.</div>

        <div style="height:1px;width:48px;background:rgba(255,255,255,0.30);
                    margin:24px 0 16px;"></div>

        <div style="font-family:{FONTS["body"]},sans-serif;font-size:13.5px;
                    color:rgba(255,255,255,0.86);line-height:1.55;max-width:320px;
                    font-weight:300;">
          O jogo é mais simples do que a Nike
          <strong style="color:#fff;font-weight:600;">fez parecer.</strong>
        </div>
      </div>

      {progress_bar(6, TOTAL)}
    </div>'''


# ============================================================
# SLIDE 7 — O INSIGHT (frase que muda a perspectiva)
# ============================================================
def slide7():
    return f'''<div class="slide" style="{bg_dark_atmo()}">
      {overlay_noise(0.44)}
      {slide_index(7, TOTAL)}

      <div style="position:absolute;top:50%;left:28px;right:28px;z-index:15;
                  transform:translateY(-52%);">
        {kicker("A Regra Final", color=ACCENT["mist"])}

        <div class="display" style="font-size:44px;color:#fff;line-height:0.88;
                    letter-spacing:{TRACK["tight"]};margin-top:16px;">
          VOCÊ NÃO PRECISA</div>
        <div class="display" style="font-size:44px;color:#fff;line-height:0.88;
                    letter-spacing:{TRACK["tight"]};">DO AMARELINHO</div>
        <div class="display" style="font-size:44px;color:rgba(255,255,255,0.45);
                    line-height:0.88;letter-spacing:{TRACK["tight"]};">NA CAMISA.</div>

        <div style="height:1.5px;width:56px;background:{ACCENT["primary"]};
                    opacity:0.7;margin:22px 0 18px;border-radius:2px;
                    box-shadow:0 0 18px rgba(30,197,242,0.45);"></div>

        <div class="display" style="font-size:44px;color:{ACCENT["primary"]};
                    line-height:0.88;letter-spacing:{TRACK["tight"]};
                    text-shadow:0 0 32px rgba(30,197,242,0.38);">PRECISA DELE</div>
        <div class="display" style="font-size:44px;color:{ACCENT["primary"]};
                    line-height:0.88;letter-spacing:{TRACK["tight"]};
                    text-shadow:0 0 32px rgba(30,197,242,0.38);">NA HISTÓRIA.</div>

        <div style="font-family:{FONTS["body"]},sans-serif;font-size:13px;
                    color:rgba(255,255,255,0.60);line-height:1.52;margin-top:20px;
                    max-width:310px;font-weight:300;">
          A Copa não é sobre camisa. É sobre a
          <strong style="color:#fff;font-weight:600;">história que só existe uma vez a cada 4 anos.</strong>
        </div>
      </div>

      {progress_bar(7, TOTAL)}
    </div>'''


# ============================================================
# SLIDE 8 — CTA
# Selecao em formacao + glass_card + display_pill "HEXA"
# ============================================================
def slide8():
    img = photo_uri("copa_selecao_formacao.jpg")
    return f'''<div class="slide" style="background:{INK["void"]};">
      {logo_mark(dark_bg=True, size=30)}
      {slide_index(8, TOTAL)}

      <div style="position:absolute;inset:0;z-index:1;">
        <img src="{img}" style="width:100%;height:100%;object-fit:cover;
                   object-position:50% 35%;filter:contrast(1.06) saturate(1.02) brightness(0.65);">
        <div style="position:absolute;inset:0;background:linear-gradient(180deg,
                    rgba(29,77,143,0.45) 0%, rgba(10,15,26,0.20) 32%,
                    rgba(10,15,26,0.68) 68%, rgba(10,15,26,0.95) 100%);
                    pointer-events:none;"></div>
      </div>

      {overlay_noise(0.30, blend="soft-light", z=4)}

      <div style="position:absolute;top:78px;left:28px;right:28px;z-index:15;">
        {glass_card(
            f'<div style="font-family:{FONTS["body"]},sans-serif;font-size:12px;'
            f'color:#fff;line-height:1.55;font-weight:400;text-align:center;">'
            f'Como uma marca sem R$ 200 milhões consegue pegar<br>'
            f'o mesmo rebote do Hexa que a Nike não conseguiu?<br>'
            f'<strong style="font-weight:700;">Tem framework para isso.</strong></div>',
            padding="14px 18px", dark=True, radius=RADIUS["lg"]
        )}
      </div>

      <div style="position:absolute;bottom:118px;left:0;right:0;z-index:18;text-align:center;">
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:11px;font-weight:500;
                    color:rgba(255,255,255,0.78);letter-spacing:{TRACK["wide"]};
                    text-transform:uppercase;margin-bottom:10px;">Comente</div>
        <span class="display" style="display:inline-block;background:#fff;
              color:{ACCENT["deep"]};padding:8px 34px 14px;border-radius:{RADIUS["lg"]}px;
              font-size:48px;line-height:0.86;letter-spacing:-0.02em;
              box-shadow:0 16px 48px rgba(10,15,26,0.55),
                         0 0 36px rgba(30,197,242,0.32),
                         inset 0 1px 0 rgba(255,255,255,0.6);">HEXA</span>
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:11px;
                    color:rgba(255,255,255,0.84);margin-top:14px;line-height:1.4;
                    padding:0 36px;font-weight:400;">
          e um <strong style="font-weight:700;">estrategista NUC</strong>
          te manda o framework de marca para a Copa.
        </div>
      </div>

      {progress_bar(8, TOTAL)}
    </div>'''


# ============================================================
# COMPOSE
# ============================================================
slides = "".join([slide1(), slide2(), slide3(), slide4(),
                  slide5(), slide6(), slide7(), slide8()])
html = html_shell(slides, TOTAL, CAPTION)

OUT = Path("/home/user/Meu-espa-o/previews/nucvision-copa-hexa.html")
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(html, encoding="utf-8")
print(f"OK preview: {OUT} ({len(html):,} chars)")
