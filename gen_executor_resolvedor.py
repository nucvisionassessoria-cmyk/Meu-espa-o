#!/usr/bin/env python3
"""
NUC Vision Editorial — Quem está dentro do seu negócio: executor ou resolvedor?
Posicionamento estratégico | linguagem madura | empresários B2B
8 slides — desconforto inteligente + autoridade reflexiva
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

# ============================================================
# SLIDE 1 — SPLIT HERO
# Derick braços cruzados (direito) + pergunta provocadora (esquerdo)
# ============================================================
def slide1():
    img = photo_uri("derick_bracos_cruzados.jpg")
    pos = photo_position("derick_bracos_cruzados.jpg")
    return f'''<div class="slide" style="background:{INK["void"]};overflow:hidden;">
      {slide_index(1, TOTAL)}

      <!-- PAINEL DIREITO — foto -->
      <div style="position:absolute;right:0;top:0;bottom:0;width:48%;z-index:2;">
        <img src="{img}" style="width:100%;height:100%;object-fit:cover;
                   object-position:{pos};filter:contrast(1.06) saturate(0.92) brightness(0.78);">
        <div style="position:absolute;inset:0;background:linear-gradient(90deg,
                    rgba(5,8,15,0.95) 0%, rgba(5,8,15,0.55) 22%,
                    rgba(5,8,15,0.10) 50%, transparent 100%);
                    pointer-events:none;"></div>
        <div style="position:absolute;inset:0;background:linear-gradient(180deg,
                    transparent 50%, rgba(5,8,15,0.70) 100%);
                    pointer-events:none;"></div>
      </div>

      <!-- PAINEL ESQUERDO — texto -->
      <div style="position:absolute;left:0;top:0;bottom:0;width:56%;z-index:10;
                  display:flex;flex-direction:column;justify-content:center;
                  padding:28px 16px 28px 24px;">

        {logo_mark(dark_bg=True, size=22)}

        <div style="margin-top:22px;">
          {kicker("Diagnóstico", color="rgba(255,255,255,0.52)")}
        </div>

        <div style="margin-top:12px;font-family:{FONTS["body"]};font-size:14px;
                    font-weight:500;color:rgba(255,255,255,0.70);
                    line-height:1.30;letter-spacing:{TRACK["tight"]};
                    max-width:200px;">
          Quem está dentro<br>do seu negócio:
        </div>

        <div style="margin-top:14px;line-height:0.86;">
          <div class="display" style="font-size:54px;color:#fff;
                      letter-spacing:{TRACK["tight"]};
                      text-shadow:0 3px 18px rgba(0,0,0,0.55);">EXECUTOR</div>
          <div class="display" style="font-size:34px;color:{ACCENT["primary"]};
                      letter-spacing:{TRACK["wide"]};margin:6px 0 4px;
                      text-shadow:0 0 24px rgba(30,197,242,0.40);">OU</div>
          <div class="display" style="font-size:48px;color:{ACCENT["primary"]};
                      letter-spacing:{TRACK["tight"]};
                      text-shadow:0 3px 18px rgba(0,0,0,0.55),
                                  0 0 28px rgba(30,197,242,0.35);">RESOLVEDOR?</div>
        </div>

        <div style="height:1.5px;width:36px;background:rgba(255,255,255,0.22);
                    margin:18px 0 12px;border-radius:2px;"></div>

        <div style="font-family:{FONTS["body"]};font-size:12px;font-weight:400;
                    color:rgba(255,255,255,0.60);line-height:1.50;max-width:200px;">
          A diferença muda<br>o seu resultado.
        </div>

        <div style="margin-top:16px;font-family:{FONTS["body"]};font-size:9px;
                    font-weight:600;color:rgba(255,255,255,0.30);
                    letter-spacing:{TRACK["label"]};text-transform:uppercase;">
          @nucvision · Operação · B2B
        </div>
      </div>

      {overlay_noise(0.25, blend="soft-light", z=5)}
      {progress_bar(1, TOTAL)}
    </div>'''

# ============================================================
# SLIDE 2 — TENSÃO TIPOGRÁFICA
# A frase que para o feed — entrega ≠ avanço
# ============================================================
def slide2():
    return f'''<div class="slide" style="{bg_dark_atmo()}">
      {overlay_noise(0.50)}
      {slide_index(2, TOTAL)}

      <div style="position:absolute;top:50%;left:28px;right:28px;z-index:10;
                  transform:translateY(-52%);">
        {kicker("A Confusão", color=ACCENT["mist"])}

        <div style="font-family:{FONTS["body"]};font-size:22px;font-weight:500;
                    color:rgba(255,255,255,0.72);line-height:1.20;
                    letter-spacing:{TRACK["tight"]};margin-top:16px;">
          Você tem cronograma.<br>
          Tem reunião.<br>
          Tem
          <span style="color:#fff;font-weight:700;">relatório.</span>
        </div>

        <div style="height:1px;width:48px;background:rgba(255,255,255,0.22);
                    margin:22px 0 18px;"></div>

        <div class="display" style="font-size:50px;color:#fff;
                    line-height:0.88;letter-spacing:{TRACK["tight"]};">VOCÊ JÁ TEM</div>
        <div class="display" style="font-size:50px;color:#fff;
                    line-height:0.88;letter-spacing:{TRACK["tight"]};">ENTREGA.</div>
        <div class="display" style="font-size:48px;color:{ACCENT["primary"]};
                    line-height:0.88;letter-spacing:{TRACK["tight"]};margin-top:6px;
                    text-shadow:0 0 28px rgba(30,197,242,0.38);">FALTA AVANÇO.</div>

        <div style="font-family:{FONTS["body"]};font-size:13px;font-weight:300;
                    color:rgba(255,255,255,0.62);line-height:1.55;margin-top:18px;
                    max-width:320px;">
          Cronograma e relatório não viraram resultado —
          <strong style="color:#fff;font-weight:600;">e você sabe disso.</strong>
        </div>
      </div>

      {progress_bar(2, TOTAL)}
    </div>'''

# ============================================================
# SLIDE 3 — A ARMADILHA
# Iago no escritório como backdrop + 4 sinais de executor disfarçado
# ============================================================
def slide3():
    img = photo_uri("iago_office_3.png")
    pos = photo_position("iago_office_3.png")

    return f'''<div class="slide" style="background:{INK["void"]};">
      {slide_index(3, TOTAL)}

      <div style="position:absolute;inset:0;z-index:1;">
        <img src="{img}" style="width:100%;height:100%;object-fit:cover;
                   object-position:{pos};filter:contrast(1.08) saturate(0.88) brightness(0.45);">
        <div style="position:absolute;inset:0;background:linear-gradient(135deg,
                    rgba(10,15,26,0.90) 0%, rgba(10,15,26,0.55) 55%,
                    rgba(10,15,26,0.82) 100%);pointer-events:none;"></div>
      </div>

      {overlay_noise(0.38, blend="soft-light", z=4)}

      <div style="position:absolute;top:44px;left:24px;right:24px;bottom:50px;
                  z-index:15;overflow:hidden;">
        {kicker("Sinais Que Doem", color=ACCENT["mist"])}

        <div style="margin-top:10px;margin-bottom:14px;">
          <div style="font-family:{FONTS["body"]};font-size:19px;font-weight:600;
                      color:#fff;line-height:1.15;letter-spacing:{TRACK["tight"]};">
            Você contratou um fornecedor.
          </div>
          <div style="font-family:{FONTS["body"]};font-size:19px;font-weight:700;
                      color:{ACCENT["light"]};line-height:1.15;letter-spacing:{TRACK["tight"]};">
            Mas continua apagando incêndio?
          </div>
        </div>

        {''.join([f'<div style="margin-bottom:7px;">{feature_row(n, l, d, dark=True)}</div>'
          for n, l, d in [
            ("01", "RECEBE RELATÓRIO",  "Mas não recebe direção do que fazer com ele."),
            ("02", "TEM CRONOGRAMA",     "Mas continua sem clareza do todo."),
            ("03", "TEM REUNIÃO SEMANAL","Mas o problema da semana passada está aí."),
            ("04", "ENTREGA NO PRAZO",   "Mas o resultado não veio."),
          ]])}
      </div>

      {progress_bar(3, TOTAL)}
    </div>'''

# ============================================================
# SLIDE 4 — DIAGNÓSTICO
# Paper bg — 4 áreas que executor não toca
# ============================================================
def slide4():
    items = [
        ("01", "CULTURA E COBRANÇA",      "O time avança ou só preenche tarefa?"),
        ("02", "PROCESSO INVISÍVEL",       "Os gargalos que ninguém vê seguem ali."),
        ("03", "LIDERANÇA SOBRECARREGADA", "Resposta certa não pode depender de você."),
        ("04", "TIME DESALINHADO",         "Cada um faz a parte. Ninguém fecha o todo."),
    ]
    rows = "".join(f'<div style="margin-bottom:8px;">{feature_row(n, l, d, dark=False)}</div>'
                   for n, l, d in items)

    return f'''<div class="slide" style="{bg_paper_atmo()}">
      {logo_mark(dark_bg=False, size=24)}
      {slide_index(4, TOTAL, light=True)}

      <div style="position:absolute;top:62px;left:24px;right:24px;bottom:52px;
                  z-index:10;overflow:hidden;">
        {kicker("O Que Executor Não Toca", color=ACCENT["primary"], light=True)}

        <div style="margin-top:10px;margin-bottom:18px;">
          <div style="font-family:{FONTS["body"]};font-size:19px;font-weight:600;
                      color:{INK["deep"]};line-height:1.15;letter-spacing:{TRACK["tight"]};">
            Não falta entrega.
          </div>
          <div style="font-family:{FONTS["body"]};font-size:19px;font-weight:700;
                      line-height:1.15;letter-spacing:{TRACK["tight"]};
                      background:linear-gradient(120deg,{ACCENT["primary"]} 0%,{ACCENT["vivid"]} 100%);
                      -webkit-background-clip:text;background-clip:text;
                      -webkit-text-fill-color:transparent;color:transparent;">
            Falta resolver:
          </div>
        </div>

        {rows}
      </div>

      {progress_bar(4, TOTAL, light=True)}
    </div>'''

# ============================================================
# SLIDE 5 — V4 FLAGSHIP STYLE (OBRIGATÓRIO)
# Fundo claro, Anton brand color, foto card com trio_reuniao
# ============================================================
def slide5():
    img = photo_uri("trio_reuniao.png")
    pos = photo_position("trio_reuniao.png")
    return f'''<div class="slide" style="{bg_paper_atmo()}">
      {logo_mark(dark_bg=False, size=24)}
      {slide_index(5, TOTAL, light=True)}

      <!-- ZONA TEXTO — bounded -->
      <div style="position:absolute;top:48px;left:28px;right:28px;bottom:226px;
                  z-index:10;overflow:hidden;">
        {kicker("A Virada de Chave", color=ACCENT["primary"], light=True)}

        <div style="margin-top:10px;line-height:0.86;">
          <div class="display" style="font-size:54px;color:{ACCENT["primary"]};
                      letter-spacing:{TRACK["tight"]};">VOCÊ CONTRATA</div>
          <div class="display" style="font-size:54px;color:{ACCENT["primary"]};
                      letter-spacing:{TRACK["tight"]};">AVANÇO,</div>
          <div class="display" style="font-size:46px;color:{INK["deep"]};
                      letter-spacing:{TRACK["tight"]};">NÃO TAREFA.</div>
        </div>

        <div style="height:1.5px;width:40px;background:{ACCENT["primary"]};
                    opacity:0.5;margin:12px 0 10px;border-radius:2px;"></div>

        <div style="font-family:{FONTS["body"]};font-size:13px;font-weight:400;
                    color:{GRAY["600"]};line-height:1.50;max-width:300px;">
          Estrutura não é cronograma.
          <strong style="color:{INK["deep"]};font-weight:600;">É movimento real.</strong>
        </div>
      </div>

      <!-- ZONA FOTO CARD -->
      <div style="position:absolute;bottom:36px;left:22px;right:22px;height:160px;
                  border-radius:{RADIUS["xl"]}px;overflow:hidden;
                  box-shadow:0 16px 40px rgba(10,15,26,0.18),
                             0 4px 12px rgba(10,15,26,0.08);">
        <img src="{img}" style="width:100%;height:100%;object-fit:cover;
                   object-position:{pos};filter:contrast(1.06) saturate(1.04);">
        <div style="position:absolute;inset:0;background:linear-gradient(180deg,
                    transparent 35%, rgba(10,15,26,0.30) 100%);"></div>
      </div>

      {progress_bar(5, TOTAL, light=True)}
    </div>'''

# ============================================================
# SLIDE 6 — CONTRASTE EM COLUNAS
# Executor vs Resolvedor — verbos lado a lado
# ============================================================
def slide6():
    body_font = FONTS["body"]
    primary = ACCENT["primary"]
    radius_lg = RADIUS["lg"]
    track_tight = TRACK["tight"]
    track_label = TRACK["label"]

    def col_item_white(text):
        return (f'<div style="font-family:{body_font};font-size:13px;'
                f'font-weight:500;color:rgba(255,255,255,0.78);'
                f'line-height:1.30;margin-bottom:9px;padding-left:10px;'
                f'border-left:1.5px solid rgba(255,255,255,0.20);">{text}</div>')

    def col_item_primary(text):
        return (f'<div style="font-family:{body_font};font-size:13px;'
                f'font-weight:600;color:#fff;line-height:1.30;'
                f'margin-bottom:9px;padding-left:10px;'
                f'border-left:1.5px solid {primary};">{text}</div>')

    exec_items = "".join(col_item_white(v) for v in
        ["Cumpre prazo.","Entrega tarefa.","Reporta status.","Espera direção."])
    resv_items = "".join(col_item_primary(v) for v in
        ["Destrava processo.","Estrutura time.","Toma decisão.","Acelera avanço."])

    return f'''<div class="slide" style="{bg_dark_atmo()}">
      {overlay_noise(0.45)}
      {slide_index(6, TOTAL)}

      <div style="position:absolute;top:48px;left:24px;right:24px;z-index:10;">
        {kicker("A Diferença Real", color=ACCENT["mist"])}

        <div style="font-family:{body_font};font-size:18px;font-weight:600;
                    color:#fff;line-height:1.18;letter-spacing:{track_tight};
                    margin-top:12px;">
          Dois fornecedores. <span style="color:{ACCENT["light"]};">Mundos opostos.</span>
        </div>
      </div>

      <div style="position:absolute;top:128px;left:24px;right:24px;bottom:90px;
                  z-index:10;display:flex;gap:12px;">

        <div style="flex:1;background:rgba(255,255,255,0.04);
                    border:1px solid rgba(255,255,255,0.10);
                    border-radius:{radius_lg}px;padding:18px 16px;">
          <div style="font-family:{body_font};font-size:9px;font-weight:700;
                      color:rgba(255,255,255,0.45);letter-spacing:{track_label};
                      text-transform:uppercase;margin-bottom:8px;">Executor</div>
          <div class="display" style="font-size:26px;color:#fff;
                      line-height:0.92;letter-spacing:{track_tight};
                      margin-bottom:18px;">FAZ.</div>
          {exec_items}
        </div>

        <div style="flex:1;background:linear-gradient(160deg,rgba(30,197,242,0.10) 0%,rgba(10,15,26,0.20) 100%);
                    border:1px solid {primary};
                    border-radius:{radius_lg}px;padding:18px 16px;
                    box-shadow:0 0 32px rgba(30,197,242,0.18);">
          <div style="font-family:{body_font};font-size:9px;font-weight:700;
                      color:{primary};letter-spacing:{track_label};
                      text-transform:uppercase;margin-bottom:8px;">Resolvedor</div>
          <div class="display" style="font-size:26px;color:{primary};
                      line-height:0.92;letter-spacing:{track_tight};
                      margin-bottom:18px;
                      text-shadow:0 0 20px rgba(30,197,242,0.40);">RESOLVE.</div>
          {resv_items}
        </div>
      </div>

      <!-- BODY FOOTER -->
      <div style="position:absolute;bottom:50px;left:24px;right:24px;z-index:10;">
        <div style="font-family:{FONTS["body"]};font-size:12px;font-weight:300;
                    color:rgba(255,255,255,0.60);line-height:1.50;
                    text-align:center;">
          Um cumpre prazo.
          <strong style="color:#fff;font-weight:700;">O outro entrega virada.</strong>
        </div>
      </div>

      {progress_bar(6, TOTAL)}
    </div>'''

# ============================================================
# SLIDE 7 — INSIGHT BRAND GRADIENT
# Frase-síntese antes do fechamento reflexivo
# ============================================================
def slide7():
    return f'''<div class="slide" style="{bg_brand_atmo()}">
      {overlay_noise(0.40)}
      {overlay_vignette(0.26)}
      {slide_index(7, TOTAL)}

      <div style="position:absolute;top:50%;left:28px;right:28px;z-index:15;
                  transform:translateY(-50%);">
        {kicker("A Síntese", color="rgba(255,255,255,0.68)")}

        <div class="display" style="font-size:62px;color:#fff;line-height:0.88;
                    letter-spacing:{TRACK["tight"]};margin-top:18px;
                    text-shadow:0 6px 28px rgba(0,0,0,0.32);">OPERAÇÃO</div>
        <div class="display" style="font-size:54px;color:#fff;line-height:0.88;
                    letter-spacing:{TRACK["tight"]};
                    text-shadow:0 6px 28px rgba(0,0,0,0.32);">NÃO É TAREFA.</div>

        <div style="height:1.5px;width:40px;background:rgba(255,255,255,0.40);
                    margin:18px 0 14px;border-radius:2px;"></div>

        <div class="display" style="font-size:48px;color:{ACCENT["ice"]};
                    line-height:0.88;letter-spacing:{TRACK["tight"]};
                    text-shadow:0 6px 28px rgba(0,0,0,0.32),
                                0 0 32px rgba(224,244,251,0.25);">É RESULTADO.</div>

        <div style="font-family:{FONTS["body"]};font-size:13.5px;font-weight:300;
                    color:rgba(255,255,255,0.80);line-height:1.55;margin-top:22px;
                    max-width:310px;">
          Quem entende a diferença
          <strong style="color:#fff;font-weight:600;">contrata diferente.</strong>
        </div>
      </div>

      {progress_bar(7, TOTAL)}
    </div>'''

# ============================================================
# SLIDE 8 — CLOSER REFLEXIVO
# Lucas + Derick juntos como autoridade dupla — pergunta final, sem CTA comercial
# ============================================================
def slide8():
    img = photo_uri("lucas_derick.jpeg")
    pos = photo_position("lucas_derick.jpeg")
    return f'''<div class="slide" style="background:{INK["void"]};">
      {logo_mark(dark_bg=True, size=28)}
      {slide_index(8, TOTAL)}

      <div style="position:absolute;inset:0;z-index:1;">
        <img src="{img}" style="width:100%;height:100%;object-fit:cover;
                   object-position:{pos};filter:contrast(1.08) saturate(1.0) brightness(0.55);">
        <div style="position:absolute;inset:0;background:linear-gradient(180deg,
                    rgba(10,15,26,0.85) 0%, rgba(10,15,26,0.45) 30%,
                    rgba(10,15,26,0.55) 60%, rgba(10,15,26,0.95) 100%);
                    pointer-events:none;"></div>
      </div>

      {overlay_noise(0.30, blend="soft-light", z=4)}
      {overlay_vignette(0.30)}

      <!-- TOPO — pergunta provocativa em destaque -->
      <div style="position:absolute;top:78px;left:28px;right:28px;z-index:15;">
        {kicker("A Pergunta Que Fica", color="rgba(255,255,255,0.70)")}

        <div style="margin-top:14px;line-height:0.92;">
          <div class="display" style="font-size:42px;color:#fff;
                      letter-spacing:{TRACK["tight"]};
                      text-shadow:0 4px 24px rgba(0,0,0,0.55);">A PRÓXIMA</div>
          <div class="display" style="font-size:42px;color:#fff;
                      letter-spacing:{TRACK["tight"]};
                      text-shadow:0 4px 24px rgba(0,0,0,0.55);">REUNIÃO VAI</div>
          <div class="display" style="font-size:42px;color:#fff;
                      letter-spacing:{TRACK["tight"]};
                      text-shadow:0 4px 24px rgba(0,0,0,0.55);">TRAZER RELATÓRIO</div>
          <div class="display" style="font-size:42px;color:{ACCENT["primary"]};
                      letter-spacing:{TRACK["tight"]};
                      text-shadow:0 4px 24px rgba(0,0,0,0.55),
                                  0 0 32px rgba(30,197,242,0.40);">OU RESULTADO?</div>
        </div>
      </div>

      <!-- FECHAMENTO — autoridade reflexiva, sem CTA comercial -->
      <div style="position:absolute;bottom:54px;left:28px;right:28px;z-index:18;">
        <div style="height:1px;width:48px;background:rgba(255,255,255,0.35);
                    margin-bottom:18px;"></div>
        <div style="font-family:{FONTS["body"]};font-size:14px;font-weight:400;
                    color:rgba(255,255,255,0.85);line-height:1.50;
                    letter-spacing:{TRACK["tight"]};max-width:340px;">
          A diferença não está no fornecedor.
          <strong style="color:#fff;font-weight:700;">Está em quem entra na operação.</strong>
        </div>
        <div style="margin-top:16px;font-family:{FONTS["body"]};font-size:9px;
                    font-weight:600;color:rgba(255,255,255,0.50);
                    letter-spacing:{TRACK["label"]};text-transform:uppercase;">
          @nucvision
        </div>
      </div>

      {progress_bar(8, TOTAL)}
    </div>'''

# ============================================================
# COMPOSE
# ============================================================
slides = "".join([slide1(), slide2(), slide3(), slide4(),
                  slide5(), slide6(), slide7(), slide8()])
caption = ("Quem está dentro do seu negócio: executor ou resolvedor? "
           "A diferença não está no fornecedor — está em quem entra na operação.")
html = html_shell(slides, TOTAL, caption)

OUT = Path("/home/user/Meu-espa-o/nucvision-editorial.html")
OUT.write_text(html, encoding="utf-8")
print(f"OK {OUT} ({len(html):,} chars)")
