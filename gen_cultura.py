#!/usr/bin/env python3
"""
NUC Vision Editorial — Cultura Empresarial
"Se sua empresa depende de você pra tudo, o problema não é sua equipe."
7 slides | posicionamento estratégico | foco: donos de empresa
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
# SLIDE 1 — HOOK / HERO
# Trio na sala de reunião full bleed; headline massiva Anton;
# frase-gancho que provoca identificação imediata
# ============================================================
def slide1():
    img = photo_uri("trio_reuniao.png")
    pos = photo_position("trio_reuniao.png")
    return f'''<div class="slide" style="background:{INK["void"]};">
      {logo_mark(dark_bg=True, size=26)}
      {slide_index(1, TOTAL)}

      <!-- FULL-BLEED PHOTO — overlay pesado no topo libera tipografia -->
      <div style="position:absolute;inset:0;z-index:1;">
        <img src="{img}" style="width:100%;height:100%;object-fit:cover;
                   object-position:{pos};filter:contrast(1.06) saturate(1.02) brightness(0.78);">
        <div style="position:absolute;inset:0;background:linear-gradient(180deg,
                    rgba(10,15,26,0.90) 0%, rgba(10,15,26,0.65) 40%,
                    rgba(10,15,26,0.18) 68%, transparent 100%);
                    pointer-events:none;"></div>
      </div>

      {overlay_noise(0.28, blend="soft-light", z=4)}

      <!-- DISPLAY STACK — setup em corpo + punchline Anton -->
      <div style="position:absolute;top:56px;left:28px;right:28px;z-index:15;">
        {kicker("Cultura Empresarial", color="rgba(255,255,255,0.62)")}

        <!-- SETUP: corpo de texto, legível, provocativo -->
        <div style="margin-top:16px;font-family:{FONTS["body"]};font-size:27px;
                    font-weight:600;color:#fff;line-height:1.10;
                    letter-spacing:{TRACK["tight"]};
                    text-shadow:0 3px 18px rgba(0,0,0,0.6);">
          Se sua empresa<br>depende de você,
        </div>

        <!-- PUNCHLINE: Anton massivo — impacto máximo -->
        <div style="margin-top:18px;line-height:0.86;">
          <div class="display" style="font-size:72px;color:#fff;
                      text-shadow:0 4px 28px rgba(0,0,0,0.55);">VOCÊ TEM</div>
          <div class="display" style="font-size:52px;color:{ACCENT["primary"]};
                      text-shadow:0 4px 28px rgba(0,0,0,0.55),
                                  0 0 32px rgba(30,197,242,0.40);">UM PROBLEMA.</div>
        </div>
      </div>

      <!-- watermark -->
      <div style="position:absolute;bottom:40px;left:28px;z-index:18;">
        <div style="font-family:{FONTS["body"]};font-size:9px;font-weight:600;
                    color:rgba(255,255,255,0.40);letter-spacing:{TRACK["label"]};
                    text-transform:uppercase;">@nucvision · agencianuc.com.br</div>
      </div>

      {progress_bar(1, TOTAL)}
    </div>'''

# ============================================================
# SLIDE 2 — QUEBRA DE PERCEPÇÃO
# Dark tipográfico — o empresário identifica os "sintomas" errados
# ============================================================
def slide2():
    return f'''<div class="slide" style="{bg_dark_atmo()}">
      {overlay_noise(0.55)}
      {slide_index(2, TOTAL)}

      <div style="position:absolute;top:50%;left:28px;right:28px;z-index:10;
                  transform:translateY(-54%);">
        {kicker("A Percepção Errada", color=ACCENT["mist"])}

        <div style="font-family:{FONTS["body"]};font-size:22px;font-weight:600;
                    color:#fff;line-height:1.15;letter-spacing:{TRACK["tight"]};
                    margin-top:16px;">
          Você acha que o problema<br>está nas
          <span style="color:{ACCENT["light"]};">vendas.</span>
        </div>
        <div style="font-family:{FONTS["body"]};font-size:22px;font-weight:600;
                    color:#fff;line-height:1.15;letter-spacing:{TRACK["tight"]};
                    margin-top:4px;">
          No <span style="color:{ACCENT["light"]};">marketing.</span>
        </div>
        <div style="font-family:{FONTS["body"]};font-size:22px;font-weight:600;
                    color:#fff;line-height:1.15;letter-spacing:{TRACK["tight"]};
                    margin-top:4px;">
          Nas <span style="color:{ACCENT["light"]};">pessoas.</span>
        </div>

        <!-- Hairline -->
        <div style="height:1px;width:48px;background:rgba(255,255,255,0.25);
                    margin:26px 0 20px;"></div>

        <div class="display" style="font-size:46px;color:{ACCENT["primary"]};
                    line-height:0.86;letter-spacing:{TRACK["tight"]};
                    text-shadow:0 0 28px rgba(30,197,242,0.4);">EFEITO.</div>
        <div style="font-family:{FONTS["body"]};font-size:13.5px;
                    color:rgba(255,255,255,0.65);line-height:1.5;margin-top:12px;
                    max-width:320px;font-weight:300;">
          Isso é só o efeito. A causa é mais profunda —
          e quase ninguém vê.
        </div>
      </div>

      {progress_bar(2, TOTAL)}
    </div>'''

# ============================================================
# SLIDE 3 — DIAGNÓSTICO IMPLÍCITO
# Paper editorial — lista limpa dos sintomas de cultura fraca
# ============================================================
def slide3():
    items = [
        ("01", "Cada um trabalha do seu jeito",  "Sem padrão, sem previsibilidade."),
        ("02", "Decisões mudam o tempo todo",     "Direção indefinida = equipe travada."),
        ("03", "Ninguém sabe o que é esperado",   "Expectativas implícitas viram conflito."),
        ("04", "Resultado depende de quem está",  "Ausência do dono = tudo para."),
    ]
    rows = "".join(f'<div style="margin-bottom:8px;">{feature_row(n, l, d, dark=False)}</div>'
                   for n, l, d in items)

    return f'''<div class="slide" style="{bg_paper_atmo()}">
      {logo_mark(dark_bg=False, size=24)}
      {slide_index(3, TOTAL, light=True)}

      <div style="position:absolute;top:62px;left:24px;right:24px;bottom:52px;
                  z-index:10;overflow:hidden;">
        {kicker("Sintomas Visíveis", color=ACCENT["primary"], light=True)}

        <div style="margin-top:10px;margin-bottom:18px;">
          <div style="font-family:{FONTS["body"]};font-size:20px;font-weight:600;
                      color:{INK["deep"]};line-height:1.12;letter-spacing:{TRACK["tight"]};">
            Quando não existe
          </div>
          <div style="font-family:{FONTS["body"]};font-size:20px;font-weight:700;
                      line-height:1.12;letter-spacing:{TRACK["tight"]};
                      background:linear-gradient(120deg,{ACCENT["primary"]} 0%,{ACCENT["vivid"]} 100%);
                      -webkit-background-clip:text;background-clip:text;
                      -webkit-text-fill-color:transparent;color:transparent;">
            cultura forte:
          </div>
        </div>

        {rows}
      </div>

      {progress_bar(3, TOTAL, light=True)}
    </div>'''

# ============================================================
# SLIDE 4 — DOR REAL
# Dark slide com foto de Iago como background — autoridade + urgência
# A mensagem "você virou o gargalo" é a dor mais visceral
# ============================================================
def slide4():
    img = photo_uri("iago_office_3.png")
    pos = photo_position("iago_office_3.png")

    items = [
        ("01", "Você é o gargalo",         "Nada avança sem você."),
        ("02", "Equipe não sustenta",       "Resultado some quando você some."),
        ("03", "Crescimento travado",       "Escalar virou um risco, não uma meta."),
        ("04", "Esgotamento é só questão   de tempo", "O modelo não aguenta."),
    ]
    rows = "".join(f'<div style="margin-bottom:7px;">{feature_row(n, l, d, dark=True)}</div>'
                   for n, l, d in items)

    return f'''<div class="slide" style="background:{INK["void"]};">
      {slide_index(4, TOTAL)}

      <!-- PHOTO BG — Iago autoridade, overlay pesado -->
      <div style="position:absolute;inset:0;z-index:1;">
        <img src="{img}" style="width:100%;height:100%;object-fit:cover;
                   object-position:{pos};filter:contrast(1.08) saturate(1.0) brightness(0.55);">
        <div style="position:absolute;inset:0;background:linear-gradient(135deg,
                    rgba(10,15,26,0.85) 0%, rgba(10,15,26,0.60) 55%,
                    rgba(10,15,26,0.82) 100%);pointer-events:none;"></div>
      </div>

      {overlay_noise(0.40, blend="soft-light", z=4)}

      <div style="position:absolute;top:50px;left:24px;right:24px;bottom:50px;
                  z-index:15;overflow:hidden;">
        {kicker("A Dor Real", color=ACCENT["mist"])}

        <div style="margin-top:10px;margin-bottom:16px;">
          <div style="font-family:{FONTS["body"]};font-size:22px;font-weight:600;
                      color:#fff;line-height:1.12;letter-spacing:{TRACK["tight"]};">
            E aí acontece
          </div>
          <div style="font-family:{FONTS["body"]};font-size:22px;font-weight:700;
                      line-height:1.12;letter-spacing:{TRACK["tight"]};
                      color:{ACCENT["light"]};">
            o previsível:
          </div>
        </div>

        {rows}
      </div>

      {progress_bar(4, TOTAL)}
    </div>'''

# ============================================================
# SLIDE 5 — INSIGHT ESTRATÉGICO
# Brand gradient — definição direta de cultura forte
# Anton massivo + lista condensada
# ============================================================
def slide5():
    # V4 FLAGSHIP STYLE — fundo claro, Anton enorme na cor da marca,
    # corpo de texto limpo, photo card arredondado na base
    img = photo_uri("trio_reuniao.png")
    pos = photo_position("trio_reuniao.png")
    return f'''<div class="slide" style="{bg_paper_atmo()}">
      {logo_mark(dark_bg=False, size=24)}
      {slide_index(5, TOTAL, light=True)}

      <!-- CONTENT BLOCK — top half -->
      <div style="position:absolute;top:58px;left:28px;right:28px;z-index:10;">
        {kicker("O Que Cultura Forte É", color=ACCENT["primary"], light=True)}

        <!-- ANTON MASSIVO na cor primária da marca -->
        <div style="margin-top:12px;line-height:0.86;">
          <div class="display" style="font-size:62px;color:{ACCENT["primary"]};
                      letter-spacing:{TRACK["tight"]};">CULTURA</div>
          <div class="display" style="font-size:62px;color:{ACCENT["primary"]};
                      letter-spacing:{TRACK["tight"]};">NÃO É</div>
          <div class="display" style="font-size:50px;color:{INK["deep"]};
                      letter-spacing:{TRACK["tight"]};">DISCURSO.</div>
        </div>

        <!-- Hairline editorial -->
        <div style="height:1.5px;width:40px;background:{ACCENT["primary"]};
                    opacity:0.5;margin:14px 0 12px;border-radius:2px;"></div>

        <!-- CORPO — limpo, direto, bem espaçado -->
        <div style="font-family:{FONTS["body"]};font-size:13.5px;font-weight:400;
                    color:{GRAY["600"]};line-height:1.58;max-width:320px;">
          É padrão, previsibilidade e consistência —
          o que faz sua empresa funcionar
          <strong style="color:{INK["deep"]};font-weight:600;">mesmo sem você.</strong>
        </div>
      </div>

      <!-- PHOTO CARD — base arredondada, estilo V4 Flagship -->
      <div style="position:absolute;bottom:44px;left:22px;right:22px;height:175px;
                  border-radius:{RADIUS["xl"]}px;overflow:hidden;
                  box-shadow:0 16px 40px rgba(10,15,26,0.18),
                             0 4px 12px rgba(10,15,26,0.08);">
        <img src="{img}" style="width:100%;height:100%;object-fit:cover;
                   object-position:{pos};filter:contrast(1.06) saturate(1.04);">
        <!-- overlay suave só na base para texto se necessário -->
        <div style="position:absolute;inset:0;background:linear-gradient(180deg,
                    transparent 40%, rgba(10,15,26,0.35) 100%);"></div>
      </div>

      {progress_bar(5, TOTAL, light=True)}
    </div>'''

# ============================================================
# SLIDE 6 — PONTE COM SOLUÇÃO
# Portrait bg — Lucas como âncora de autoridade
# Copy: sem diagnóstico, você continua corrigindo sintomas
# ============================================================
def slide6():
    return f'''<div class="slide" style="background:{INK["void"]};">
      {slide_index(6, TOTAL)}

      <!-- FULL BLEED PHOTO -->
      <div style="position:absolute;inset:0;z-index:1;">
        {photo_layered("lucas_3.jpeg", "portrait")}
      </div>

      {overlay_noise(0.32, blend="soft-light", z=4)}

      <!-- TOP TEXT -->
      <div style="position:absolute;top:36px;left:28px;right:28px;z-index:15;">
        {kicker("O Ponto Cego", color=ACCENT["mist"])}

        <div style="font-family:{FONTS["body"]};font-size:22px;font-weight:600;
                    color:#fff;line-height:1.12;letter-spacing:{TRACK["tight"]};
                    margin-top:12px;text-shadow:0 3px 16px rgba(0,0,0,0.65);">
          Sem um diagnóstico
        </div>
        <div style="font-family:{FONTS["body"]};font-size:22px;font-weight:600;
                    line-height:1.12;letter-spacing:{TRACK["tight"]};
                    margin-top:2px;
                    background:linear-gradient(120deg,{ACCENT["light"]} 0%,{ACCENT["electric"]} 100%);
                    -webkit-background-clip:text;background-clip:text;
                    -webkit-text-fill-color:transparent;color:transparent;
                    filter:drop-shadow(0 2px 8px rgba(0,0,0,0.4));">
          estruturado,
        </div>
      </div>

      <!-- GLASS CARD BOTTOM -->
      <div style="position:absolute;bottom:62px;left:24px;right:24px;z-index:18;">
        {glass_card(
            f'<div style="font-family:{FONTS["body"]};font-size:13px;'
            f'color:rgba(255,255,255,0.92);line-height:1.55;font-weight:400;">'
            f'você continua tentando corrigir <strong style="color:{ACCENT["light"]};'
            f'font-weight:600;">sintomas</strong> sem chegar na raiz '
            f'do problema.</div>',
            padding="15px 17px", dark=True
        )}
      </div>

      {progress_bar(6, TOTAL)}
    </div>'''

# ============================================================
# SLIDE 7 — CTA
# Trio foto full bleed (mesma do hero = bookend visual)
# Glass card qualificador + pill DIAGNÓSTICO + instrução
# ============================================================
def slide7():
    img = photo_uri("lucas_derick.jpeg")
    pos = photo_position("lucas_derick.jpeg")
    return f'''<div class="slide" style="background:{INK["void"]};">
      {logo_mark(dark_bg=True, size=32)}
      {slide_index(7, TOTAL)}

      <!-- FULL BLEED PHOTO — overlay escuro no topo e base -->
      <div style="position:absolute;inset:0;z-index:1;">
        <img src="{img}" style="width:100%;height:100%;object-fit:cover;
                   object-position:{pos};filter:contrast(1.06) saturate(1.02) brightness(0.72);">
        <div style="position:absolute;inset:0;background:linear-gradient(180deg,
                    rgba(29,77,143,0.45) 0%, rgba(10,15,26,0.20) 35%,
                    rgba(10,15,26,0.60) 68%, rgba(10,15,26,0.92) 100%);
                    pointer-events:none;"></div>
      </div>

      {overlay_noise(0.32, blend="soft-light", z=4)}

      <!-- QUALIFIER PILL (top glass) -->
      <div style="position:absolute;top:82px;left:28px;right:28px;z-index:15;">
        {glass_card(
            f'<div style="font-family:{FONTS["body"]};font-size:12px;'
            f'color:#fff;line-height:1.5;font-weight:400;text-align:center;">'
            f'Quer entender onde sua empresa está travando?<br>'
            f'<strong style="font-weight:700;">Identificamos a raiz — não o sintoma.</strong></div>',
            padding="13px 18px", dark=True, radius=RADIUS["lg"]
        )}
      </div>

      <!-- CTA WORD -->
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
caption = "Sua empresa depende de você pra tudo? Isso não é dedicação — é falta de estrutura."
html = html_shell(slides, TOTAL, caption)

OUT = Path("/home/user/Meu-espa-o/nucvision-editorial.html")
OUT.write_text(html, encoding="utf-8")
print(f"OK {OUT} ({len(html):,} chars)")
