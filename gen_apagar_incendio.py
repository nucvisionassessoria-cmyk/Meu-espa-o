#!/usr/bin/env python3
"""
NUC Vision Editorial — Você não tem uma empresa. Você tem uma rotina de apagar incêndio.
Diagnóstico brutal | dono preso na operação | caminho para sair
7 slides — split hero com Iago + tipografia progressiva
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
# SLIDE 1 — SPLIT HERO
# Iago braços cruzados (direito) + headline provocadora (esquerdo)
# ============================================================
def slide1():
    img = photo_uri("iago_bracos_cruzados.png")
    pos = photo_position("iago_bracos_cruzados.png")
    return f'''<div class="slide" style="background:{INK["void"]};overflow:hidden;">
      {slide_index(1, TOTAL)}

      <!-- PAINEL DIREITO — foto -->
      <div style="position:absolute;right:0;top:0;bottom:0;width:48%;z-index:2;">
        <img src="{img}" style="width:100%;height:100%;object-fit:cover;
                   object-position:{pos};filter:contrast(1.06) saturate(0.95) brightness(0.82);">
        <!-- gradiente no seam esquerdo para fundir com o painel dark -->
        <div style="position:absolute;inset:0;background:linear-gradient(90deg,
                    rgba(5,8,15,0.95) 0%, rgba(5,8,15,0.55) 22%,
                    rgba(5,8,15,0.10) 50%, transparent 100%);
                    pointer-events:none;"></div>
        <!-- gradiente inferior -->
        <div style="position:absolute;inset:0;background:linear-gradient(180deg,
                    transparent 50%, rgba(5,8,15,0.70) 100%);
                    pointer-events:none;"></div>
      </div>

      <!-- PAINEL ESQUERDO — texto -->
      <div style="position:absolute;left:0;top:0;bottom:0;width:56%;z-index:10;
                  display:flex;flex-direction:column;justify-content:center;
                  padding:28px 16px 28px 24px;">

        {logo_mark(dark_bg=True, size=22)}

        <div style="margin-top:24px;">
          {kicker("Diagnóstico", color="rgba(255,255,255,0.52)")}
        </div>

        <div style="margin-top:14px;line-height:0.86;">
          <div class="display" style="font-size:62px;color:#fff;
                      letter-spacing:{TRACK["tight"]};
                      text-shadow:0 3px 18px rgba(0,0,0,0.55);">VOCÊ NÃO</div>
          <div class="display" style="font-size:62px;color:#fff;
                      letter-spacing:{TRACK["tight"]};
                      text-shadow:0 3px 18px rgba(0,0,0,0.55);">TEM UMA</div>
          <div class="display" style="font-size:56px;color:{ACCENT["primary"]};
                      letter-spacing:{TRACK["tight"]};
                      text-shadow:0 3px 18px rgba(0,0,0,0.55),
                                  0 0 28px rgba(30,197,242,0.35);">EMPRESA.</div>
        </div>

        <div style="height:1.5px;width:36px;background:rgba(255,255,255,0.22);
                    margin:16px 0 14px;border-radius:2px;"></div>

        <div style="font-family:{FONTS["body"]};font-size:13px;font-weight:400;
                    color:rgba(255,255,255,0.68);line-height:1.52;max-width:200px;">
          Você tem uma rotina de<br>
          <strong style="color:#fff;font-weight:600;">apagar incêndio.</strong>
        </div>

        <div style="margin-top:16px;font-family:{FONTS["body"]};font-size:9px;
                    font-weight:600;color:rgba(255,255,255,0.30);
                    letter-spacing:{TRACK["label"]};text-transform:uppercase;">
          @nucvision · Gestão · Estrutura
        </div>
      </div>

      {overlay_noise(0.25, blend="soft-light", z=5)}
      {progress_bar(1, TOTAL)}
    </div>'''

# ============================================================
# SLIDE 2 — QUEBRA TIPOGRÁFICA
# O ciclo que nunca acaba — brutal e direto
# ============================================================
def slide2():
    return f'''<div class="slide" style="{bg_dark_atmo()}">
      {overlay_noise(0.50)}
      {slide_index(2, TOTAL)}

      <div style="position:absolute;top:50%;left:28px;right:28px;z-index:10;
                  transform:translateY(-52%);">
        {kicker("O Ciclo Vicioso", color=ACCENT["mist"])}

        <div style="font-family:{FONTS["body"]};font-size:22px;font-weight:400;
                    color:rgba(255,255,255,0.70);line-height:1.22;
                    letter-spacing:{TRACK["tight"]};margin-top:16px;">
          Acordou hoje pensando em
          <span style="color:#fff;font-weight:600;">estratégia?</span>
        </div>
        <div style="font-family:{FONTS["body"]};font-size:22px;font-weight:400;
                    color:rgba(255,255,255,0.70);line-height:1.22;
                    letter-spacing:{TRACK["tight"]};margin-top:4px;">
          Ou já estava apagando
          <span style="color:{ACCENT["light"]};font-weight:600;">fogo às 8h?</span>
        </div>

        <div style="height:1px;width:48px;background:rgba(255,255,255,0.20);
                    margin:24px 0 20px;"></div>

        <div class="display" style="font-size:58px;color:{ACCENT["primary"]};
                    line-height:0.86;letter-spacing:{TRACK["tight"]};
                    text-shadow:0 0 32px rgba(30,197,242,0.38);">O URGENTE</div>
        <div class="display" style="font-size:58px;color:#fff;
                    line-height:0.86;letter-spacing:{TRACK["tight"]};">SEQUESTRA</div>
        <div class="display" style="font-size:44px;color:rgba(255,255,255,0.42);
                    line-height:0.86;letter-spacing:{TRACK["tight"]};">O IMPORTANTE.</div>

        <div style="font-family:{FONTS["body"]};font-size:13px;
                    color:rgba(255,255,255,0.55);line-height:1.55;margin-top:18px;
                    max-width:310px;font-weight:300;">
          Todo dia você sai do operacional
          para resolver o que
          <strong style="color:#fff;font-weight:600;">nunca deveria ter chegado até você.</strong>
        </div>
      </div>

      {progress_bar(2, TOTAL)}
    </div>'''

# ============================================================
# SLIDE 3 — OS SINAIS
# Iago como backdrop — 4 sintomas de quem virou bombeiro
# ============================================================
def slide3():
    img = photo_uri("derick_1.png")
    pos = photo_position("derick_1.png")

    return f'''<div class="slide" style="background:{INK["void"]};">
      {slide_index(3, TOTAL)}

      <div style="position:absolute;inset:0;z-index:1;">
        <img src="{img}" style="width:100%;height:100%;object-fit:cover;
                   object-position:{pos};filter:contrast(1.08) saturate(0.90) brightness(0.45);">
        <div style="position:absolute;inset:0;background:linear-gradient(135deg,
                    rgba(10,15,26,0.90) 0%, rgba(10,15,26,0.55) 55%,
                    rgba(10,15,26,0.82) 100%);pointer-events:none;"></div>
      </div>

      {overlay_noise(0.38, blend="soft-light", z=4)}

      <div style="position:absolute;top:44px;left:24px;right:24px;bottom:50px;
                  z-index:15;overflow:hidden;">
        {kicker("4 Sinais de Alerta", color=ACCENT["mist"])}

        <div style="margin-top:10px;margin-bottom:16px;">
          <div style="font-family:{FONTS["body"]};font-size:20px;font-weight:600;
                      color:#fff;line-height:1.12;letter-spacing:{TRACK["tight"]};">
            Você não é empresário.
          </div>
          <div style="font-family:{FONTS["body"]};font-size:20px;font-weight:700;
                      color:{ACCENT["light"]};line-height:1.12;letter-spacing:{TRACK["tight"]};">
            Você é o principal funcionário.
          </div>
        </div>

        {''.join([f'<div style="margin-bottom:7px;">{feature_row(n, l, d, dark=True)}</div>'
          for n, l, d in [
            ("01", "Sem você, trava",          "A empresa para quando você some por dois dias."),
            ("02", "Reunião sem pauta",         "Problemas chegam até você porque ninguém decide sozinho."),
            ("03", "Plano nunca executado",     "Você pensa em crescer, mas o dia não deixa."),
            ("04", "Equipe espera sua ordem",   "Delegou o cargo, não a responsabilidade."),
          ]])}
      </div>

      {progress_bar(3, TOTAL)}
    </div>'''

# ============================================================
# SLIDE 4 — O DIAGNÓSTICO
# Paper lista — 4 raízes do problema (não sintomas)
# ============================================================
def slide4():
    items = [
        ("01", "Sem processos reais",        "Tudo depende de você porque nada está documentado."),
        ("02", "Time sem autonomia",          "Você não delegou — apenas transferiu tarefas."),
        ("03", "Ausência de indicadores",     "Sem painel, você só sabe que errou depois do estrago."),
        ("04", "Cultura de dependência",      "O time aprendeu que a resposta certa é: pergunta pro Iago."),
    ]
    rows = "".join(f'<div style="margin-bottom:8px;">{feature_row(n, l, d, dark=False)}</div>'
                   for n, l, d in items)

    return f'''<div class="slide" style="{bg_paper_atmo()}">
      {logo_mark(dark_bg=False, size=24)}
      {slide_index(4, TOTAL, light=True)}

      <div style="position:absolute;top:62px;left:24px;right:24px;bottom:52px;
                  z-index:10;overflow:hidden;">
        {kicker("A Raiz do Problema", color=ACCENT["primary"], light=True)}

        <div style="margin-top:10px;margin-bottom:18px;">
          <div style="font-family:{FONTS["body"]};font-size:20px;font-weight:600;
                      color:{INK["deep"]};line-height:1.12;letter-spacing:{TRACK["tight"]};">
            Não é falta de esforço.
          </div>
          <div style="font-family:{FONTS["body"]};font-size:20px;font-weight:700;
                      line-height:1.12;letter-spacing:{TRACK["tight"]};
                      background:linear-gradient(120deg,{ACCENT["primary"]} 0%,{ACCENT["vivid"]} 100%);
                      -webkit-background-clip:text;background-clip:text;
                      -webkit-text-fill-color:transparent;color:transparent;">
            É falta de estrutura:
          </div>
        </div>

        {rows}
      </div>

      {progress_bar(4, TOTAL, light=True)}
    </div>'''

# ============================================================
# SLIDE 5 — V4 FLAGSHIP STYLE (OBRIGATÓRIO)
# Fundo claro, Anton brand color, photo card base
# ============================================================
def slide5():
    img = photo_uri("iago_bracos_cruzados.png")
    pos = photo_position("iago_bracos_cruzados.png")
    return f'''<div class="slide" style="{bg_paper_atmo()}">
      {logo_mark(dark_bg=False, size=24)}
      {slide_index(5, TOTAL, light=True)}

      <!-- ZONA TEXTO — bounded para nunca invadir o card -->
      <div style="position:absolute;top:48px;left:28px;right:28px;bottom:226px;
                  z-index:10;overflow:hidden;">
        {kicker("A Virada", color=ACCENT["primary"], light=True)}

        <div style="margin-top:10px;line-height:0.86;">
          <div class="display" style="font-size:54px;color:{ACCENT["primary"]};
                      letter-spacing:{TRACK["tight"]};">ESTRUTURA</div>
          <div class="display" style="font-size:54px;color:{ACCENT["primary"]};
                      letter-spacing:{TRACK["tight"]};">É O QUE</div>
          <div class="display" style="font-size:44px;color:{INK["deep"]};
                      letter-spacing:{TRACK["tight"]};">TE LIBERTA.</div>
        </div>

        <div style="height:1.5px;width:40px;background:{ACCENT["primary"]};
                    opacity:0.5;margin:12px 0 10px;border-radius:2px;"></div>

        <div style="font-family:{FONTS["body"]};font-size:13px;font-weight:400;
                    color:{GRAY["600"]};line-height:1.50;max-width:300px;">
          Processos e autonomia colocam você
          <strong style="color:{INK["deep"]};font-weight:600;">no lugar certo: estratégia.</strong>
        </div>
      </div>

      <!-- ZONA FOTO CARD — separada por respiro de ~32px -->
      <div style="position:absolute;bottom:36px;left:22px;right:22px;height:160px;
                  border-radius:{RADIUS["xl"]}px;overflow:hidden;
                  box-shadow:0 16px 40px rgba(10,15,26,0.18),
                             0 4px 12px rgba(10,15,26,0.08);">
        <img src="{img}" style="width:100%;height:100%;object-fit:cover;
                   object-position:{pos};filter:contrast(1.06) saturate(1.02);">
        <div style="position:absolute;inset:0;background:linear-gradient(180deg,
                    transparent 35%, rgba(10,15,26,0.35) 100%);"></div>
      </div>

      {progress_bar(5, TOTAL, light=True)}
    </div>'''

# ============================================================
# SLIDE 6 — INSIGHT FINAL
# Brand gradient — a sentença que muda a perspectiva
# ============================================================
def slide6():
    return f'''<div class="slide" style="{bg_brand_atmo()}">
      {overlay_noise(0.40)}
      {overlay_vignette(0.26)}
      {slide_index(6, TOTAL)}

      <div style="position:absolute;top:50%;left:28px;right:28px;z-index:15;
                  transform:translateY(-50%);">
        {kicker("A Diferença", color="rgba(255,255,255,0.68)")}

        <div class="display" style="font-size:52px;color:#fff;line-height:0.86;
                    letter-spacing:{TRACK["tight"]};margin-top:18px;
                    text-shadow:0 6px 28px rgba(0,0,0,0.32);">ENQUANTO</div>
        <div class="display" style="font-size:52px;color:#fff;line-height:0.86;
                    letter-spacing:{TRACK["tight"]};
                    text-shadow:0 6px 28px rgba(0,0,0,0.32);">VOCÊ APAGA,</div>
        <div class="display" style="font-size:42px;color:{ACCENT["ice"]};
                    line-height:0.86;letter-spacing:{TRACK["tight"]};
                    text-shadow:0 6px 28px rgba(0,0,0,0.32),
                                0 0 28px rgba(224,244,251,0.20);">O CONCORRENTE</div>
        <div class="display" style="font-size:42px;color:{ACCENT["ice"]};
                    line-height:0.86;letter-spacing:{TRACK["tight"]};
                    text-shadow:0 6px 28px rgba(0,0,0,0.32),
                                0 0 28px rgba(224,244,251,0.20);">CONSTRÓI.</div>

        <div style="height:1px;width:48px;background:rgba(255,255,255,0.28);
                    margin:24px 0 16px;"></div>

        <div style="font-family:{FONTS["body"]};font-size:13.5px;
                    color:rgba(255,255,255,0.82);line-height:1.55;max-width:310px;
                    font-weight:300;">
          Empresa que depende do dono é empresa que
          <strong style="color:#fff;font-weight:600;">cresce até o limite do dono.</strong>
        </div>
      </div>

      {progress_bar(6, TOTAL)}
    </div>'''

# ============================================================
# SLIDE 7 — CTA
# lucas_derick.jpeg — autoridade + chamada de ação
# ============================================================
def slide7():
    img = photo_uri("lucas_derick.jpeg")
    pos = photo_position("lucas_derick.jpeg")
    return f'''<div class="slide" style="background:{INK["void"]};">
      {logo_mark(dark_bg=True, size=32)}
      {slide_index(7, TOTAL)}

      <div style="position:absolute;inset:0;z-index:1;">
        <img src="{img}" style="width:100%;height:100%;object-fit:cover;
                   object-position:{pos};filter:contrast(1.06) saturate(1.02) brightness(0.70);">
        <div style="position:absolute;inset:0;background:linear-gradient(180deg,
                    rgba(29,77,143,0.45) 0%, rgba(10,15,26,0.18) 35%,
                    rgba(10,15,26,0.62) 68%, rgba(10,15,26,0.94) 100%);
                    pointer-events:none;"></div>
      </div>

      {overlay_noise(0.30, blend="soft-light", z=4)}

      <div style="position:absolute;top:82px;left:28px;right:28px;z-index:15;">
        {glass_card(
            f'<div style="font-family:{FONTS["body"]};font-size:12px;'
            f'color:#fff;line-height:1.5;font-weight:400;text-align:center;">'
            f'Sua empresa funciona sem você por uma semana —<br>'
            f'ou você é o único que sabe onde tudo está?<br>'
            f'<strong style="font-weight:700;">Descubra o que está te prendendo na operação.</strong></div>',
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
                         inset 0 1px 0 rgba(255,255,255,0.6);">LIBERDADE</span>
        <div style="font-family:{FONTS["body"]};font-size:11px;
                    color:rgba(255,255,255,0.82);margin-top:14px;line-height:1.4;
                    padding:0 36px;font-weight:400;">
          e um <strong style="font-weight:700;">especialista NUC</strong>
          vai te ajudar a sair da operação.
        </div>
      </div>

      {progress_bar(7, TOTAL)}
    </div>'''

# ============================================================
# COMPOSE
# ============================================================
slides = "".join([slide1(), slide2(), slide3(), slide4(), slide5(), slide6(), slide7()])
caption = "Você não tem uma empresa. Você tem uma rotina de apagar incêndio. Veja os 4 sinais e como sair disso."
html = html_shell(slides, TOTAL, caption)

OUT = Path("/home/user/Meu-espa-o/nucvision-editorial.html")
OUT.write_text(html, encoding="utf-8")
print(f"OK {OUT} ({len(html):,} chars)")
