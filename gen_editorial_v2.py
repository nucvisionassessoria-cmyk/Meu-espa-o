#!/usr/bin/env python3
"""
NUC Vision Editorial Carousel v2 — Premium agency-grade layouts
Theme: Por que sua empresa não cresce mesmo vendendo
Each slide is a distinct editorial composition.
"""
import sys
from pathlib import Path
sys.path.insert(0, "/home/user/Meu-espa-o")

from design_system import (
    INK, PAPER, ACCENT, GRAY, FONTS, TYPE, TRACK, LINE,
    RADIUS, SHADOW, W, H,
    bg_brand_atmo, bg_dark_atmo, bg_paper_atmo, bg_split,
    overlay_noise, overlay_vignette,
    kicker, display_pill, stat_block, glass_card, number_marker,
    feature_row, slide_index, progress_bar, logo_mark,
    photo_layered, photo_uri, photo_position,
    html_shell,
)

TOTAL = 7

# ============================================================
# SLIDE 1 — MAGAZINE COVER HERO
# Photo full bleed bottom; bold display word straddling the seam;
# editorial kicker + headline anchored top
# ============================================================
def slide1():
    return f'''<div class="slide" style="{bg_brand_atmo()}">
      {overlay_noise(0.4)}
      {logo_mark(dark_bg=True, size=26)}
      {slide_index(1, TOTAL)}

      <!-- TOP TEXT BLOCK -->
      <div style="position:absolute;top:64px;left:28px;right:28px;z-index:15;">
        {kicker("Diagnóstico Estratégico", color="rgba(255,255,255,0.78)")}
        <div style="font-family:{FONTS["body"]};font-size:30px;font-weight:600;
                    color:#fff;line-height:1.02;letter-spacing:{TRACK["tight"]};
                    margin-top:14px;">Sua empresa<br>vende.</div>
      </div>

      <!-- PHOTO BOTTOM (full bleed) -->
      <div style="position:absolute;bottom:0;left:0;right:0;height:54%;z-index:5;overflow:hidden;">
        {photo_layered("lucas_derick.jpeg", "hero")}
      </div>

      <!-- DISPLAY PILL straddling the seam -->
      <div style="position:absolute;top:46%;left:28px;right:28px;z-index:18;text-align:left;">
        {display_pill("MAS NÃO CRESCE.", accent="white", size=44, glow=False)}
      </div>

      <!-- BOTTOM-LEFT WATERMARK -->
      <div style="position:absolute;bottom:30px;left:28px;z-index:18;">
        <div style="font-family:{FONTS["body"]};font-size:9px;font-weight:600;
                    color:rgba(255,255,255,0.55);letter-spacing:{TRACK["label"]};
                    text-transform:uppercase;">@nucvision · Estrutura · Crescimento</div>
      </div>

      {progress_bar(1, TOTAL)}
    </div>'''

# ============================================================
# SLIDE 2 — MANIFESTO TIPOGRÁFICO
# One dominant typographic statement on premium dark background
# ============================================================
def slide2():
    return f'''<div class="slide" style="{bg_dark_atmo()}">
      {overlay_noise(0.55)}
      {slide_index(2, TOTAL)}

      <div style="position:absolute;top:50%;left:28px;right:28px;z-index:10;
                  transform:translateY(-50%);">
        {kicker("A Realidade", color=ACCENT["mist"])}

        <div class="display" style="font-size:64px;color:#fff;line-height:0.86;
                    letter-spacing:-0.03em;margin-top:18px;
                    text-shadow:0 6px 32px rgba(0,0,0,0.4);">VENDA</div>
        <div class="display" style="font-size:64px;color:#fff;line-height:0.86;
                    letter-spacing:-0.03em;
                    text-shadow:0 6px 32px rgba(0,0,0,0.4);">NÃO É</div>
        <div class="display" style="font-size:64px;
                    background:linear-gradient(120deg,{ACCENT["primary"]} 0%,{ACCENT["electric"]} 100%);
                    -webkit-background-clip:text;background-clip:text;
                    -webkit-text-fill-color:transparent;color:transparent;
                    line-height:0.86;letter-spacing:-0.03em;
                    filter:drop-shadow(0 0 24px rgba(30,197,242,0.4));">CRESCER.</div>

        <!-- Hairline divider -->
        <div style="height:1px;width:48px;background:rgba(255,255,255,0.3);
                    margin:32px 0 22px;"></div>

        <div style="font-family:{FONTS["body"]};font-size:14px;
                    color:rgba(255,255,255,0.72);line-height:1.55;max-width:340px;
                    font-weight:300;">
          Vender é <strong style="color:#fff;font-weight:600;">resultado</strong>.
          Crescer é <strong style="color:#fff;font-weight:600;">estrutura</strong>.
          E quase ninguém vê a diferença a tempo.
        </div>
      </div>

      {progress_bar(2, TOTAL)}
    </div>'''

# ============================================================
# SLIDE 3 — EDITORIAL PORTRAIT (full-bleed photo + glass caption)
# Lucas full bleed; headline overlaid top in display; glass card bottom
# ============================================================
def slide3():
    return f'''<div class="slide" style="background:{INK["void"]};">
      {slide_index(3, TOTAL)}

      <!-- FULL BLEED PHOTO -->
      <div style="position:absolute;inset:0;z-index:1;">
        {photo_layered("lucas_3.jpeg", "portrait")}
      </div>

      {overlay_noise(0.35, blend="soft-light", z=4)}

      <!-- TOP TEXT -->
      <div style="position:absolute;top:36px;left:28px;right:28px;z-index:15;">
        {kicker("O Diagnóstico", color=ACCENT["mist"])}
        <div style="font-family:{FONTS["body"]};font-size:24px;font-weight:600;
                    color:#fff;line-height:1.1;letter-spacing:{TRACK["tight"]};
                    margin-top:12px;text-shadow:0 4px 20px rgba(0,0,0,0.6);">
          O problema não está<br>
          no que você vende.
        </div>
        <div style="font-family:{FONTS["body"]};font-size:24px;font-weight:600;
                    line-height:1.1;letter-spacing:{TRACK["tight"]};margin-top:6px;
                    background:linear-gradient(120deg,{ACCENT["light"]} 0%,{ACCENT["electric"]} 100%);
                    -webkit-background-clip:text;background-clip:text;
                    -webkit-text-fill-color:transparent;color:transparent;
                    filter:drop-shadow(0 2px 8px rgba(0,0,0,0.3));">
          Está no que você não vê.
        </div>
      </div>

      <!-- GLASS CAPTION CARD BOTTOM -->
      <div style="position:absolute;bottom:62px;left:24px;right:24px;z-index:18;">
        {glass_card(
            f'<div style="font-family:{FONTS["body"]};font-size:12.5px;'
            f'color:rgba(255,255,255,0.92);line-height:1.5;font-weight:400;">'
            f'Empresas estagnadas quase sempre têm '
            f'<strong style="color:{ACCENT["light"]};font-weight:600;">gargalos invisíveis</strong> '
            f'em processo, marketing, time e dados.</div>',
            padding="14px 16px", dark=True
        )}
      </div>

      {progress_bar(3, TOTAL)}
    </div>'''

# ============================================================
# SLIDE 4 — REFINED CATALOG (numbered editorial list)
# Light bg with sophisticated tinting; numbered rows with display markers
# ============================================================
def slide4():
    items = [
        ("01", "Operação desorganizada", "Você sabe o que vende — mas não como produz."),
        ("02", "Dados sem leitura",      "Os números existem, ninguém interpreta."),
        ("03", "Time sem processo",       "Cada um faz do seu jeito, sem padrão."),
        ("04", "Marketing desconectado",  "Gera lead, mas o lead não converte."),
        ("05", "Atendimento sem padrão",  "Cliente vive uma experiência aleatória."),
    ]
    rows = "".join(f'<div style="margin-bottom:8px;">{feature_row(n, l, d, dark=False)}</div>'
                   for n, l, d in items)

    return f'''<div class="slide" style="{bg_paper_atmo()}">
      {logo_mark(dark_bg=False, size=24)}
      {slide_index(4, TOTAL, light=True)}

      <div style="position:absolute;top:62px;left:24px;right:24px;z-index:10;">
        {kicker("Os Gargalos", color=ACCENT["primary"], light=True)}

        <div style="display:flex;align-items:baseline;gap:10px;margin-top:10px;
                    margin-bottom:20px;">
          <div class="display" style="font-size:46px;color:{ACCENT["primary"]};line-height:0.86;
                      letter-spacing:{TRACK["tight"]};">5</div>
          <div style="font-family:{FONTS["body"]};font-size:21px;font-weight:600;
                      color:{INK["deep"]};line-height:1.1;letter-spacing:{TRACK["tight"]};">
            falhas invisíveis<br>que travam crescimento.
          </div>
        </div>

        {rows}
      </div>

      {progress_bar(4, TOTAL, light=True)}
    </div>'''

# ============================================================
# SLIDE 5 — DIPTYCH (two photos with editorial captions)
# Two photos with strong conceptual contrast; refined frames + labels
# ============================================================
def slide5():
    img_office = photo_uri("iago_office_2.png")
    img_field  = photo_uri("iago_2.png")
    pos_office = photo_position("iago_office_2.png")
    pos_field  = photo_position("iago_2.png")

    return f'''<div class="slide" style="{bg_dark_atmo()}">
      {overlay_noise(0.45)}
      {slide_index(5, TOTAL)}

      <!-- TOP TEXT -->
      <div style="position:absolute;top:36px;left:28px;right:60px;z-index:15;">
        {kicker("Metodologia", color=ACCENT["mist"])}
        <div style="font-family:{FONTS["body"]};font-size:22px;font-weight:600;
                    color:#fff;line-height:1.12;letter-spacing:{TRACK["tight"]};
                    margin-top:10px;">
          Diagnóstico real exige
        </div>
        <div style="font-family:{FONTS["body"]};font-size:22px;font-weight:600;
                    line-height:1.12;letter-spacing:{TRACK["tight"]};
                    background:linear-gradient(120deg,{ACCENT["light"]} 0%,{ACCENT["electric"]} 100%);
                    -webkit-background-clip:text;background-clip:text;
                    -webkit-text-fill-color:transparent;color:transparent;">
          presença real.
        </div>
      </div>

      <!-- DIPTYCH photos -->
      <div style="position:absolute;bottom:78px;left:24px;right:24px;height:260px;z-index:10;">
        <!-- LEFT photo (larger, top-anchored) -->
        <div style="position:absolute;top:0;left:0;width:74%;height:80%;
                    border-radius:{RADIUS["md"]}px;overflow:hidden;
                    box-shadow:{SHADOW["drama"]};">
          <img src="{img_office}" style="width:100%;height:100%;object-fit:cover;
                       object-position:{pos_office};filter:contrast(1.06) saturate(1.04);">
          <div style="position:absolute;inset:0;background:linear-gradient(180deg,
                      transparent 60%, rgba(10,15,26,0.55) 100%);"></div>
          <div style="position:absolute;bottom:10px;left:12px;
                      font-family:{FONTS["body"]};font-size:9px;font-weight:600;
                      color:#fff;text-transform:uppercase;letter-spacing:{TRACK["label"]};
                      background:rgba(10,15,26,0.6);padding:4px 10px;border-radius:{RADIUS["pill"]}px;
                      backdrop-filter:blur(8px);border:1px solid rgba(255,255,255,0.12);">
            Estratégia
          </div>
        </div>

        <!-- RIGHT photo (smaller, bottom-anchored, overlapping) -->
        <div style="position:absolute;bottom:0;right:0;width:55%;height:56%;
                    border-radius:{RADIUS["md"]}px;overflow:hidden;
                    box-shadow:{SHADOW["drama"]};
                    border:3px solid {INK["deep"]};">
          <img src="{img_field}" style="width:100%;height:100%;object-fit:cover;
                       object-position:{pos_field};filter:contrast(1.06) saturate(1.04);">
          <div style="position:absolute;inset:0;background:linear-gradient(180deg,
                      transparent 55%, rgba(10,15,26,0.6) 100%);"></div>
          <div style="position:absolute;bottom:10px;left:12px;
                      font-family:{FONTS["body"]};font-size:9px;font-weight:600;
                      color:#fff;text-transform:uppercase;letter-spacing:{TRACK["label"]};
                      background:{ACCENT["primary"]};padding:4px 10px;border-radius:{RADIUS["pill"]}px;
                      box-shadow:{SHADOW["card"]};">
            Execução
          </div>
        </div>
      </div>

      <!-- BOTTOM CAPTION -->
      <div style="position:absolute;bottom:48px;left:24px;right:24px;z-index:15;text-align:center;">
        <div style="font-family:{FONTS["body"]};font-size:11.5px;
                    color:rgba(255,255,255,0.65);line-height:1.45;font-weight:400;">
          Estratégia que funciona é estratégia que
          <strong style="color:#fff;font-weight:600;">vê o que acontece</strong>.
        </div>
      </div>

      {progress_bar(5, TOTAL)}
    </div>'''

# ============================================================
# SLIDE 6 — PULL QUOTE / FILOSOFIA
# Massive single statement — premium brand gradient + atmospheric layers
# ============================================================
def slide6():
    return f'''<div class="slide" style="{bg_brand_atmo()}">
      {overlay_noise(0.4)}
      {overlay_vignette(0.3)}
      {logo_mark(dark_bg=True, size=24)}
      {slide_index(6, TOTAL)}

      <div style="position:absolute;top:50%;left:28px;right:28px;z-index:15;
                  transform:translateY(-50%);text-align:left;">
        {kicker("A Filosofia NUC", color="rgba(255,255,255,0.85)")}

        <div class="display" style="font-size:50px;color:#fff;line-height:0.86;
                    letter-spacing:-0.03em;margin-top:20px;
                    text-shadow:0 8px 36px rgba(0,0,0,0.32);">ESTRUTURA</div>
        <div class="display" style="font-size:50px;color:#fff;line-height:0.86;
                    letter-spacing:-0.03em;
                    text-shadow:0 8px 36px rgba(0,0,0,0.32);">GERA</div>
        <div class="display" style="font-size:50px;color:{ACCENT["ice"]};
                    line-height:0.86;letter-spacing:-0.03em;
                    text-shadow:0 8px 36px rgba(0,0,0,0.32),
                                0 0 32px rgba(224,244,251,0.25);">CRESCIMENTO.</div>

        <!-- Hairline divider -->
        <div style="height:1px;width:48px;background:rgba(255,255,255,0.35);
                    margin:30px 0 20px;"></div>

        <div style="font-family:{FONTS["body"]};font-size:13.5px;
                    color:rgba(255,255,255,0.88);line-height:1.55;max-width:300px;
                    font-weight:400;">
          Sem estrutura, você só vende.<br>
          Com estrutura, você
          <strong style="color:#fff;font-weight:700;">escala</strong>.
        </div>
      </div>

      {progress_bar(6, TOTAL)}
    </div>'''

# ============================================================
# SLIDE 7 — CTA WITH OVERLAPPING GLASS CARD
# Hero photo + frosted glass action card + display CTA word
# ============================================================
def slide7():
    return f'''<div class="slide" style="background:{INK["void"]};">
      {logo_mark(dark_bg=True, size=32)}
      {slide_index(7, TOTAL)}

      <!-- FULL BLEED PHOTO with cta treatment -->
      <div style="position:absolute;inset:0;z-index:1;">
        {photo_layered("lucas_derick.jpeg", "cta")}
      </div>

      {overlay_noise(0.35, blend="soft-light", z=4)}

      <!-- OFFER QUALIFIER PILL (top, glass) -->
      <div style="position:absolute;top:88px;left:28px;right:28px;z-index:15;">
        {glass_card(
            f'<div style="font-family:{FONTS["body"]};font-size:12px;'
            f'color:#fff;line-height:1.5;font-weight:400;text-align:center;">'
            f'Se sua empresa fatura acima de '
            f'<strong style="font-weight:700;">R$ 100K/mês</strong> e está pronta '
            f'pra estruturar o próximo nível</div>',
            padding="14px 18px", dark=True, radius=RADIUS["lg"]
        )}
      </div>

      <!-- CTA WORD with glow -->
      <div style="position:absolute;bottom:128px;left:0;right:0;z-index:18;text-align:center;">
        <div style="font-family:{FONTS["body"]};font-size:11px;font-weight:500;
                    color:rgba(255,255,255,0.78);letter-spacing:{TRACK["wide"]};
                    text-transform:uppercase;margin-bottom:10px;">Comente</div>
        <span class="display" style="display:inline-block;background:#fff;
              color:{ACCENT["deep"]};padding:8px 28px 14px;border-radius:{RADIUS["lg"]}px;
              font-size:42px;line-height:0.86;letter-spacing:-0.02em;
              box-shadow:0 16px 48px rgba(10,15,26,0.5),
                         0 0 36px rgba(30,197,242,0.3),
                         inset 0 1px 0 rgba(255,255,255,0.6);">DIAGNÓSTICO</span>
        <div style="font-family:{FONTS["body"]};font-size:11px;
                    color:rgba(255,255,255,0.85);margin-top:14px;line-height:1.4;
                    padding:0 36px;font-weight:400;">
          e um <strong style="font-weight:700;">especialista NUC</strong>
          entra em contato com você.
        </div>
      </div>

      {progress_bar(7, TOTAL)}
    </div>'''

# ============================================================
# COMPOSE
# ============================================================
slides = "".join([slide1(), slide2(), slide3(), slide4(), slide5(), slide6(), slide7()])
caption = "Sua empresa vende mas não cresce? Pode estar travada em gargalos invisíveis."
html = html_shell(slides, TOTAL, caption)

OUT = Path("/home/user/Meu-espa-o/nucvision-editorial.html")
OUT.write_text(html, encoding="utf-8")
print(f"OK {OUT} ({len(html):,} chars)")
