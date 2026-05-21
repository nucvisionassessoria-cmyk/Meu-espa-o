#!/usr/bin/env python3
"""
NUC Vision Editorial — Contratar por Competência ou por Cultura?
Posicionamento estratégico | linguagem direta | donos de empresa
7 slides — debate provocativo com dois lados defendíveis
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

TOTAL = 7

# ============================================================
# SLIDE 1 — HOOK
# Pergunta que divide — sem resposta fácil, gera tensão
# ============================================================
def slide1():
    img = photo_uri("trio_reuniao.png")
    pos = photo_position("trio_reuniao.png")
    return f'''<div class="slide" style="background:{INK["void"]};">
      {logo_mark(dark_bg=True, size=26)}
      {slide_index(1, TOTAL)}

      <div style="position:absolute;inset:0;z-index:1;">
        <img src="{img}" style="width:100%;height:100%;object-fit:cover;
                   object-position:{pos};filter:contrast(1.07) saturate(1.02) brightness(0.72);">
        <div style="position:absolute;inset:0;background:linear-gradient(180deg,
                    rgba(10,15,26,0.92) 0%, rgba(10,15,26,0.68) 42%,
                    rgba(10,15,26,0.20) 68%, transparent 100%);
                    pointer-events:none;"></div>
      </div>

      {overlay_noise(0.28, blend="soft-light", z=4)}

      <div style="position:absolute;top:56px;left:28px;right:28px;z-index:15;">
        {kicker("Contratação Estratégica", color="rgba(255,255,255,0.60)")}

        <div style="margin-top:16px;font-family:{FONTS["body"]};font-size:26px;
                    font-weight:600;color:#fff;line-height:1.10;
                    letter-spacing:{TRACK["tight"]};
                    text-shadow:0 3px 18px rgba(0,0,0,0.6);">
          Você contrata pelo<br>currículo ou pela cultura?
        </div>

        <div style="margin-top:20px;line-height:0.86;">
          <div class="display" style="font-size:72px;color:#fff;
                      text-shadow:0 4px 28px rgba(0,0,0,0.55);">A RESPOSTA</div>
          <div class="display" style="font-size:54px;color:{ACCENT["primary"]};
                      text-shadow:0 4px 28px rgba(0,0,0,0.55),
                                  0 0 32px rgba(30,197,242,0.40);">DEFINE O TIME.</div>
        </div>
      </div>

      <div style="position:absolute;bottom:40px;left:28px;z-index:18;">
        <div style="font-family:{FONTS["body"]};font-size:9px;font-weight:600;
                    color:rgba(255,255,255,0.38);letter-spacing:{TRACK["label"]};
                    text-transform:uppercase;">@nucvision · agencianuc.com.br</div>
      </div>

      {progress_bar(1, TOTAL)}
    </div>'''

# ============================================================
# SLIDE 2 — QUEBRA DE PERCEPÇÃO
# A ilusão do craque — todo mundo já cometeu esse erro
# ============================================================
def slide2():
    return f'''<div class="slide" style="{bg_dark_atmo()}">
      {overlay_noise(0.52)}
      {slide_index(2, TOTAL)}

      <div style="position:absolute;top:50%;left:28px;right:28px;z-index:10;
                  transform:translateY(-52%);">
        {kicker("O Erro Clássico", color=ACCENT["mist"])}

        <div style="font-family:{FONTS["body"]};font-size:24px;font-weight:600;
                    color:#fff;line-height:1.12;letter-spacing:{TRACK["tight"]};
                    margin-top:16px;">
          Você encontra alguém
          <span style="color:{ACCENT["light"]};">brilhante.</span>
        </div>
        <div style="font-family:{FONTS["body"]};font-size:24px;font-weight:600;
                    color:#fff;line-height:1.12;letter-spacing:{TRACK["tight"]};
                    margin-top:4px;">
          Currículo impecável.
          <span style="color:{ACCENT["light"]};">Contrata.</span>
        </div>

        <div style="height:1px;width:48px;background:rgba(255,255,255,0.22);
                    margin:26px 0 20px;"></div>

        <div class="display" style="font-size:52px;color:{ACCENT["primary"]};
                    line-height:0.86;letter-spacing:{TRACK["tight"]};
                    text-shadow:0 0 28px rgba(30,197,242,0.38);">E DESTRÓI</div>
        <div class="display" style="font-size:52px;color:#fff;
                    line-height:0.86;letter-spacing:{TRACK["tight"]};">O TIME.</div>

        <div style="font-family:{FONTS["body"]};font-size:13px;
                    color:rgba(255,255,255,0.60);line-height:1.55;margin-top:18px;
                    max-width:320px;font-weight:300;">
          Competência sem alinhamento cultural
          não soma — <strong style="color:#fff;font-weight:600;">subtrai</strong>.
        </div>
      </div>

      {progress_bar(2, TOTAL)}
    </div>'''

# ============================================================
# SLIDE 3 — A DOR DO GESTOR
# Iago como backdrop de autoridade — quem toma a decisão
# 4 sinais de que a contratação foi errada
# ============================================================
def slide3():
    img = photo_uri("iago_office_3.png")
    pos = photo_position("iago_office_3.png")

    return f'''<div class="slide" style="background:{INK["void"]};">
      {slide_index(3, TOTAL)}

      <div style="position:absolute;inset:0;z-index:1;">
        <img src="{img}" style="width:100%;height:100%;object-fit:cover;
                   object-position:{pos};filter:contrast(1.08) saturate(0.95) brightness(0.50);">
        <div style="position:absolute;inset:0;background:linear-gradient(135deg,
                    rgba(10,15,26,0.88) 0%, rgba(10,15,26,0.55) 55%,
                    rgba(10,15,26,0.80) 100%);pointer-events:none;"></div>
      </div>

      {overlay_noise(0.38, blend="soft-light", z=4)}

      <div style="position:absolute;top:44px;left:24px;right:24px;bottom:50px;
                  z-index:15;overflow:hidden;">
        {kicker("Quando Dá Errado", color=ACCENT["mist"])}

        <div style="margin-top:10px;margin-bottom:16px;">
          <div style="font-family:{FONTS["body"]};font-size:21px;font-weight:600;
                      color:#fff;line-height:1.12;letter-spacing:{TRACK["tight"]};">
            O craque que destrói
          </div>
          <div style="font-family:{FONTS["body"]};font-size:21px;font-weight:700;
                      color:{ACCENT["light"]};line-height:1.12;letter-spacing:{TRACK["tight"]};">
            o que levou anos pra construir:
          </div>
        </div>

        {''.join([f'<div style="margin-bottom:7px;">{feature_row(n, l, d, dark=True)}</div>'
          for n, l, d in [
            ("01", "Clima deteriora rápido",     "Um perfil fora do padrão contamina o time."),
            ("02", "Processo vira exceção",       "O craque faz do jeito dele. Os outros copiam."),
            ("03", "Liderança perde autoridade",  "Concessões viram precedente."),
            ("04", "Resultado cai junto",         "Competência individual não vira resultado coletivo."),
          ]])}
      </div>

      {progress_bar(3, TOTAL)}
    </div>'''

# ============================================================
# SLIDE 4 — O OUTRO LADO
# Paper lista — os 4 critérios que definem cultura na contratação
# ============================================================
def slide4():
    items = [
        ("01", "Valores na prática",      "Como age sob pressão, não o que fala na entrevista."),
        ("02", "Relação com erro",        "Esconde ou aprende? Define o padrão do time."),
        ("03", "Ritmo de execução",       "Urgência ou enrolação? Ritmo contamina."),
        ("04", "Ego ou equipe?",          "Quem brilha sozinho apaga o grupo."),
    ]
    rows = "".join(f'<div style="margin-bottom:8px;">{feature_row(n, l, d, dark=False)}</div>'
                   for n, l, d in items)

    return f'''<div class="slide" style="{bg_paper_atmo()}">
      {logo_mark(dark_bg=False, size=24)}
      {slide_index(4, TOTAL, light=True)}

      <div style="position:absolute;top:62px;left:24px;right:24px;bottom:52px;
                  z-index:10;overflow:hidden;">
        {kicker("O Que Realmente Avaliar", color=ACCENT["primary"], light=True)}

        <div style="margin-top:10px;margin-bottom:18px;">
          <div style="font-family:{FONTS["body"]};font-size:20px;font-weight:600;
                      color:{INK["deep"]};line-height:1.12;letter-spacing:{TRACK["tight"]};">
            Antes do currículo,
          </div>
          <div style="font-family:{FONTS["body"]};font-size:20px;font-weight:700;
                      line-height:1.12;letter-spacing:{TRACK["tight"]};
                      background:linear-gradient(120deg,{ACCENT["primary"]} 0%,{ACCENT["vivid"]} 100%);
                      -webkit-background-clip:text;background-clip:text;
                      -webkit-text-fill-color:transparent;color:transparent;">
            avalie isso:
          </div>
        </div>

        {rows}
      </div>

      {progress_bar(4, TOTAL, light=True)}
    </div>'''

# ============================================================
# SLIDE 5 — V4 FLAGSHIP STYLE
# Fundo claro, Anton na cor primária, corpo direto
# Equipe de cultura forte como photo card na base
# ============================================================
def slide5():
    img = photo_uri("equipe_cultura.jpg")
    pos = photo_position("equipe_cultura.jpg")
    return f'''<div class="slide" style="{bg_paper_atmo()}">
      {logo_mark(dark_bg=False, size=24)}
      {slide_index(5, TOTAL, light=True)}

      <div style="position:absolute;top:58px;left:28px;right:28px;z-index:10;">
        {kicker("A Verdade Sobre Cultura", color=ACCENT["primary"], light=True)}

        <div style="margin-top:12px;line-height:0.86;">
          <div class="display" style="font-size:62px;color:{ACCENT["primary"]};
                      letter-spacing:{TRACK["tight"]};">CULTURA</div>
          <div class="display" style="font-size:62px;color:{ACCENT["primary"]};
                      letter-spacing:{TRACK["tight"]};">NÃO SE</div>
          <div class="display" style="font-size:54px;color:{INK["deep"]};
                      letter-spacing:{TRACK["tight"]};">DECLARA.</div>
        </div>

        <div style="height:1.5px;width:40px;background:{ACCENT["primary"]};
                    opacity:0.5;margin:14px 0 12px;border-radius:2px;"></div>

        <div style="font-family:{FONTS["body"]};font-size:13.5px;font-weight:400;
                    color:{GRAY["600"]};line-height:1.58;max-width:320px;">
          Se pratica, contrata e demite.
          <strong style="color:{INK["deep"]};font-weight:600;">Cada pessoa que entra
          confirma ou corrói o que você construiu.</strong>
        </div>
      </div>

      <div style="position:absolute;bottom:44px;left:22px;right:22px;height:175px;
                  border-radius:{RADIUS["xl"]}px;overflow:hidden;
                  box-shadow:0 16px 40px rgba(10,15,26,0.18),
                             0 4px 12px rgba(10,15,26,0.08);">
        <img src="{img}" style="width:100%;height:100%;object-fit:cover;
                   object-position:{pos};filter:contrast(1.06) saturate(1.04);">
        <div style="position:absolute;inset:0;background:linear-gradient(180deg,
                    transparent 40%, rgba(10,15,26,0.30) 100%);"></div>
      </div>

      {progress_bar(5, TOTAL, light=True)}
    </div>'''

# ============================================================
# SLIDE 6 — O INSIGHT FINAL
# Brand gradient — a síntese provocativa do debate
# ============================================================
def slide6():
    return f'''<div class="slide" style="{bg_brand_atmo()}">
      {overlay_noise(0.40)}
      {overlay_vignette(0.26)}
      {slide_index(6, TOTAL)}

      <div style="position:absolute;top:50%;left:28px;right:28px;z-index:15;
                  transform:translateY(-50%);">
        {kicker("A Síntese", color="rgba(255,255,255,0.68)")}

        <div class="display" style="font-size:56px;color:#fff;line-height:0.86;
                    letter-spacing:{TRACK["tight"]};margin-top:18px;
                    text-shadow:0 6px 28px rgba(0,0,0,0.32);">CONTRATE</div>
        <div class="display" style="font-size:56px;color:#fff;line-height:0.86;
                    letter-spacing:{TRACK["tight"]};
                    text-shadow:0 6px 28px rgba(0,0,0,0.32);">PELA CULTURA,</div>
        <div class="display" style="font-size:46px;color:{ACCENT["ice"]};
                    line-height:0.86;letter-spacing:{TRACK["tight"]};
                    text-shadow:0 6px 28px rgba(0,0,0,0.32),
                                0 0 28px rgba(224,244,251,0.20);">TREINE A TÉCNICA.</div>

        <div style="height:1px;width:48px;background:rgba(255,255,255,0.28);
                    margin:26px 0 18px;"></div>

        <div style="font-family:{FONTS["body"]};font-size:13.5px;
                    color:rgba(255,255,255,0.82);line-height:1.55;max-width:310px;
                    font-weight:300;">
          Técnica se aprende.
          Valores, postura e ritmo —
          <strong style="color:#fff;font-weight:600;">você não ensina em 90 dias.</strong>
        </div>
      </div>

      {progress_bar(6, TOTAL)}
    </div>'''

# ============================================================
# SLIDE 7 — CTA
# Lucas + Derick como bookend de autoridade
# ============================================================
def slide7():
    img = photo_uri("lucas_derick.jpeg")
    pos = photo_position("lucas_derick.jpeg")
    return f'''<div class="slide" style="background:{INK["void"]};">
      {logo_mark(dark_bg=True, size=32)}
      {slide_index(7, TOTAL)}

      <div style="position:absolute;inset:0;z-index:1;">
        <img src="{img}" style="width:100%;height:100%;object-fit:cover;
                   object-position:{pos};filter:contrast(1.06) saturate(1.02) brightness(0.72);">
        <div style="position:absolute;inset:0;background:linear-gradient(180deg,
                    rgba(29,77,143,0.45) 0%, rgba(10,15,26,0.20) 35%,
                    rgba(10,15,26,0.60) 68%, rgba(10,15,26,0.92) 100%);
                    pointer-events:none;"></div>
      </div>

      {overlay_noise(0.30, blend="soft-light", z=4)}

      <div style="position:absolute;top:82px;left:28px;right:28px;z-index:15;">
        {glass_card(
            f'<div style="font-family:{FONTS["body"]};font-size:12px;'
            f'color:#fff;line-height:1.5;font-weight:400;text-align:center;">'
            f'Sua empresa está contratando certo —<br>'
            f'ou repetindo os mesmos erros de time?<br>'
            f'<strong style="font-weight:700;">Identifique a raiz antes do próximo processo.</strong></div>',
            padding="13px 18px", dark=True, radius=RADIUS["lg"]
        )}
      </div>

      <div style="position:absolute;bottom:118px;left:0;right:0;z-index:18;text-align:center;">
        <div style="font-family:{FONTS["body"]};font-size:11px;font-weight:500;
                    color:rgba(255,255,255,0.75);letter-spacing:{TRACK["wide"]};
                    text-transform:uppercase;margin-bottom:10px;">Comente</div>
        <span class="display" style="display:inline-block;background:#fff;
              color:{ACCENT["deep"]};padding:8px 28px 14px;border-radius:{RADIUS["lg"]}px;
              font-size:40px;line-height:0.86;letter-spacing:-0.02em;
              box-shadow:0 16px 48px rgba(10,15,26,0.5),
                         0 0 36px rgba(30,197,242,0.28),
                         inset 0 1px 0 rgba(255,255,255,0.6);">DIAGNÓSTICO</span>
        <div style="font-family:{FONTS["body"]};font-size:11px;
                    color:rgba(255,255,255,0.82);margin-top:14px;line-height:1.4;
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
caption = "Você contrata pelo currículo ou pela cultura? Essa resposta define o time que você vai ter."
html = html_shell(slides, TOTAL, caption)

OUT = Path("/home/user/Meu-espa-o/nucvision-editorial.html")
OUT.write_text(html, encoding="utf-8")
print(f"OK {OUT} ({len(html):,} chars)")
