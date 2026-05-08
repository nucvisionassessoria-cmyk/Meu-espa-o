#!/usr/bin/env python3
"""
NUC Vision Editorial — Executor ou Resolvedor? (v2)
Arco narrativo progressivo | design ousado | linguagem B2B madura
8 slides — cada slide = novo ângulo, sem repetição de insight
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
# SLIDE 1 — GANCHO (split hero)
# Derick olhar direto + pergunta que divide
# ============================================================
def slide1():
    img = photo_uri("derick_bracos_cruzados.jpg")
    pos = photo_position("derick_bracos_cruzados.jpg")
    return f'''<div class="slide" style="background:{INK["void"]};overflow:hidden;">
      {slide_index(1, TOTAL)}

      <div style="position:absolute;right:0;top:0;bottom:0;width:48%;z-index:2;">
        <img src="{img}" style="width:100%;height:100%;object-fit:cover;
                   object-position:{pos};filter:contrast(1.08) saturate(0.90) brightness(0.78);">
        <div style="position:absolute;inset:0;background:linear-gradient(90deg,
                    rgba(5,8,15,0.97) 0%, rgba(5,8,15,0.50) 20%,
                    rgba(5,8,15,0.08) 50%, transparent 100%);"></div>
        <div style="position:absolute;inset:0;background:linear-gradient(180deg,
                    transparent 48%, rgba(5,8,15,0.75) 100%);"></div>
      </div>

      <div style="position:absolute;left:0;top:0;bottom:0;width:56%;z-index:10;
                  display:flex;flex-direction:column;justify-content:center;
                  padding:28px 16px 28px 22px;">
        {logo_mark(dark_bg=True, size=20)}

        <div style="margin-top:24px;">
          {kicker("Diagnóstico Direto", color="rgba(255,255,255,0.48)")}
        </div>

        <div style="margin-top:14px;font-family:{FONTS["body"]};font-size:13px;
                    font-weight:400;color:rgba(255,255,255,0.62);
                    line-height:1.35;max-width:190px;">
          Quem entrou no seu negócio essa semana:
        </div>

        <div style="margin-top:16px;line-height:0.84;">
          <div class="display" style="font-size:52px;color:#fff;
                      letter-spacing:{TRACK["tight"]};
                      text-shadow:0 2px 16px rgba(0,0,0,0.60);">EXECUTOR</div>
          <div style="display:flex;align-items:center;gap:10px;margin:8px 0 6px;">
            <div style="height:1px;flex:1;background:rgba(255,255,255,0.18);"></div>
            <div class="display" style="font-size:22px;color:{ACCENT["primary"]};
                        letter-spacing:{TRACK["wide"]};
                        text-shadow:0 0 20px rgba(30,197,242,0.50);">OU</div>
            <div style="height:1px;flex:1;background:{ACCENT["primary"]};opacity:0.4;"></div>
          </div>
          <div class="display" style="font-size:46px;color:{ACCENT["primary"]};
                      letter-spacing:{TRACK["tight"]};
                      text-shadow:0 2px 16px rgba(0,0,0,0.55),
                                  0 0 32px rgba(30,197,242,0.40);">RESOLVEDOR?</div>
        </div>

        <div style="margin-top:20px;font-family:{FONTS["body"]};font-size:9px;
                    font-weight:600;color:rgba(255,255,255,0.28);
                    letter-spacing:{TRACK["label"]};text-transform:uppercase;">
          @nucvision · Operação · B2B
        </div>
      </div>

      {overlay_noise(0.22, blend="soft-light", z=5)}
      {progress_bar(1, TOTAL)}
    </div>'''

# ============================================================
# SLIDE 2 — TENSÃO / CANCELAMENTO VISUAL
# "PRESENÇA" riscada → novo ângulo: você paga por presença, não por progresso
# Técnica: palavra cancelada com linha diagonal absoluta
# ============================================================
def slide2():
    return f'''<div class="slide" style="{bg_dark_atmo()}">
      {overlay_noise(0.52)}
      {slide_index(2, TOTAL)}

      <!-- NÚMERO GIGANTE de fundo (watermark) -->
      <div class="display" style="position:absolute;bottom:-20px;right:-10px;
                  font-size:220px;color:rgba(255,255,255,0.025);
                  line-height:1;letter-spacing:-0.04em;z-index:1;
                  pointer-events:none;user-select:none;">2</div>

      <div style="position:absolute;top:50%;left:28px;right:28px;z-index:10;
                  transform:translateY(-54%);">
        {kicker("O Que Você Está Pagando", color=ACCENT["mist"])}

        <div style="margin-top:20px;">
          <!-- PRESENÇA riscada -->
          <div style="position:relative;display:inline-block;margin-bottom:4px;">
            <div class="display" style="font-size:58px;color:rgba(255,255,255,0.28);
                        letter-spacing:{TRACK["tight"]};">PRESENÇA.</div>
            <div style="position:absolute;top:48%;left:-4px;right:-4px;
                        height:3px;background:rgba(255,255,255,0.55);
                        transform:rotate(-2deg);border-radius:2px;"></div>
          </div>

          <div style="margin-top:2px;">
            <div class="display" style="font-size:58px;color:{ACCENT["primary"]};
                        letter-spacing:{TRACK["tight"]};
                        text-shadow:0 0 40px rgba(30,197,242,0.45);">PROGRESSO.</div>
          </div>
        </div>

        <div style="height:1px;width:48px;background:rgba(255,255,255,0.20);
                    margin:22px 0 16px;"></div>

        <div style="font-family:{FONTS["body"]};font-size:14px;font-weight:400;
                    color:rgba(255,255,255,0.70);line-height:1.55;max-width:320px;">
          Seu time está ocupado.<br>
          Seu negócio está parado.<br>
          <strong style="color:#fff;font-weight:700;">Presença e progresso não são a mesma coisa.</strong>
        </div>
      </div>

      {progress_bar(2, TOTAL)}
    </div>'''

# ============================================================
# SLIDE 3 — PROVA CONCRETA (setor específico)
# Agência de marketing: entregou tudo. Cliente não chegou.
# Foto Iago como backdrop de decisão
# ============================================================
def slide3():
    img = photo_uri("iago_office_1.png")
    pos = photo_position("iago_office_1.png")

    rows_data = [
        ("01", "CAMPANHA RODANDO",    "Impressões, cliques, entrega técnica perfeita."),
        ("02", "RELATÓRIO SEMANAL",   "Números bonitos. Nenhum diz o porquê não converte."),
        ("03", "REUNIÃO DE ALINHAMENTO","Cronograma aprovado. Processo comercial, intocado."),
        ("04", "ENTREGOU O ESCOPO",   "Tudo no prazo. O cliente que devia chegar não veio."),
    ]
    rows_html = "".join(
        f'<div style="margin-bottom:6px;">{feature_row(n, l, d, dark=True)}</div>'
        for n, l, d in rows_data
    )

    return f'''<div class="slide" style="background:{INK["void"]};">
      {slide_index(3, TOTAL)}

      <div style="position:absolute;inset:0;z-index:1;">
        <img src="{img}" style="width:100%;height:100%;object-fit:cover;
                   object-position:{pos};filter:contrast(1.06) saturate(0.85) brightness(0.40);">
        <div style="position:absolute;inset:0;background:linear-gradient(150deg,
                    rgba(10,15,26,0.92) 0%, rgba(10,15,26,0.50) 55%,
                    rgba(10,15,26,0.85) 100%);"></div>
      </div>

      {overlay_noise(0.35, blend="soft-light", z=4)}

      <div style="position:absolute;top:42px;left:24px;right:24px;bottom:50px;
                  z-index:15;overflow:hidden;">
        {kicker("O Cenário Comum", color=ACCENT["mist"])}

        <div style="margin-top:10px;margin-bottom:14px;">
          <div style="font-family:{FONTS["body"]};font-size:18px;font-weight:500;
                      color:#fff;line-height:1.18;letter-spacing:{TRACK["tight"]};">
            Sua agência de marketing
          </div>
          <div style="font-family:{FONTS["body"]};font-size:18px;font-weight:700;
                      color:{ACCENT["light"]};line-height:1.18;letter-spacing:{TRACK["tight"]};">
            entregou tudo certinho.
          </div>
        </div>

        {rows_html}

        <div style="margin-top:10px;font-family:{FONTS["body"]};font-size:12px;
                    font-weight:300;color:rgba(255,255,255,0.55);line-height:1.50;">
          O escopo foi entregue. O problema real —
          <strong style="color:rgba(255,255,255,0.85);font-weight:600;">nunca estava no escopo.</strong>
        </div>
      </div>

      {progress_bar(3, TOTAL)}
    </div>'''

# ============================================================
# SLIDE 4 — RAIZ (fundo ICE — choque visual)
# Background frio, inesperado. Uma verdade que desconforta.
# ============================================================
def slide4():
    ice_bg = ACCENT["ice"]
    return f'''<div class="slide" style="background:{ice_bg};overflow:hidden;">
      {logo_mark(dark_bg=False, size=22)}
      {slide_index(4, TOTAL, light=True)}

      <!-- NÚMERO WATERMARK -->
      <div class="display" style="position:absolute;bottom:-30px;right:-20px;
                  font-size:240px;color:rgba(10,15,26,0.06);
                  line-height:1;letter-spacing:-0.04em;z-index:1;
                  pointer-events:none;">4</div>

      <div style="position:absolute;top:50%;left:28px;right:28px;z-index:10;
                  transform:translateY(-52%);">
        {kicker("A Causa Real", color=ACCENT["deep"], light=True)}

        <div style="margin-top:18px;line-height:0.88;">
          <div class="display" style="font-size:50px;color:{INK["deep"]};
                      letter-spacing:{TRACK["tight"]};">O PROBLEMA</div>
          <div class="display" style="font-size:50px;color:{INK["deep"]};
                      letter-spacing:{TRACK["tight"]};">NUNCA ESTAVA</div>
          <div class="display" style="font-size:50px;
                      background:linear-gradient(120deg,{ACCENT["primary"]} 0%,{ACCENT["vivid"]} 100%);
                      -webkit-background-clip:text;background-clip:text;
                      -webkit-text-fill-color:transparent;
                      letter-spacing:{TRACK["tight"]};">NO BRIEFING.</div>
        </div>

        <div style="height:2px;width:48px;
                    background:linear-gradient(90deg,{ACCENT["primary"]},transparent);
                    margin:22px 0 18px;border-radius:2px;"></div>

        <div style="font-family:{FONTS["body"]};font-size:14px;font-weight:400;
                    color:{GRAY["700"]};line-height:1.60;max-width:330px;">
          Estava no processo comercial que ninguém tocou.<br>
          No time que ninguém cobrou.<br>
          Na liderança que ninguém estruturou.<br>
          <strong style="color:{INK["deep"]};font-weight:700;">Isso não cabe no escopo de ninguém — cabe no compromisso de poucos.</strong>
        </div>
      </div>

      {progress_bar(4, TOTAL, light=True)}
    </div>'''

# ============================================================
# SLIDE 5 — VIRADA / V4 FLAGSHIP (obrigatório)
# Fundo claro, Anton brand color, photo card com trio
# ============================================================
def slide5():
    img = photo_uri("trio_reuniao.png")
    pos = photo_position("trio_reuniao.png")
    return f'''<div class="slide" style="{bg_paper_atmo()}">
      {logo_mark(dark_bg=False, size=24)}
      {slide_index(5, TOTAL, light=True)}

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

      <div style="position:absolute;bottom:36px;left:22px;right:22px;height:160px;
                  border-radius:{RADIUS["xl"]}px;overflow:hidden;
                  box-shadow:0 16px 40px rgba(10,15,26,0.18),0 4px 12px rgba(10,15,26,0.08);">
        <img src="{img}" style="width:100%;height:100%;object-fit:cover;
                   object-position:{pos};filter:contrast(1.06) saturate(1.04);">
        <div style="position:absolute;inset:0;background:linear-gradient(180deg,
                    transparent 35%, rgba(10,15,26,0.28) 100%);"></div>
      </div>

      {progress_bar(5, TOTAL, light=True)}
    </div>'''

# ============================================================
# SLIDE 6 — CONTRASTE (dual column com glow)
# Executor vs Resolvedor — cada verbo em oposição direta
# ============================================================
def slide6():
    bf = FONTS["body"]
    pr = ACCENT["primary"]
    rl = RADIUS["lg"]
    tt = TRACK["tight"]
    tl = TRACK["label"]

    def item_dim(text):
        return (f'<div style="display:flex;align-items:baseline;gap:6px;'
                f'margin-bottom:10px;">'
                f'<div style="width:3px;height:3px;border-radius:50%;'
                f'background:rgba(255,255,255,0.30);flex-shrink:0;margin-top:6px;"></div>'
                f'<div style="font-family:{bf};font-size:13px;font-weight:500;'
                f'color:rgba(255,255,255,0.65);line-height:1.28;">{text}</div></div>')

    def item_bright(text):
        return (f'<div style="display:flex;align-items:baseline;gap:6px;'
                f'margin-bottom:10px;">'
                f'<div style="width:3px;height:3px;border-radius:50%;'
                f'background:{pr};flex-shrink:0;margin-top:6px;"></div>'
                f'<div style="font-family:{bf};font-size:13px;font-weight:600;'
                f'color:#fff;line-height:1.28;">{text}</div></div>')

    exec_items = "".join(item_dim(v) for v in
        ["Cumpre o que foi pedido.","Entrega no prazo.","Reporta o que fez.","Espera o próximo briefing."])
    resv_items = "".join(item_bright(v) for v in
        ["Pergunta o que não foi pedido.","Destrava o que trava o prazo.","Aponta o que ninguém viu.","Decide antes do incêndio."])

    return f'''<div class="slide" style="{bg_dark_atmo()}">
      {overlay_noise(0.42)}
      {slide_index(6, TOTAL)}

      <div style="position:absolute;top:46px;left:24px;right:24px;z-index:10;">
        {kicker("Dois Mundos", color=ACCENT["mist"])}
        <div style="font-family:{bf};font-size:17px;font-weight:600;
                    color:#fff;line-height:1.20;letter-spacing:{tt};margin-top:12px;">
          Mesma semana. <span style="color:{ACCENT["light"]};">Resultados opostos.</span>
        </div>
      </div>

      <div style="position:absolute;top:122px;left:22px;right:22px;bottom:72px;
                  z-index:10;display:flex;gap:10px;">

        <div style="flex:1;background:rgba(255,255,255,0.035);
                    border:1px solid rgba(255,255,255,0.08);
                    border-radius:{rl}px;padding:16px 14px;opacity:0.85;">
          <div style="font-family:{bf};font-size:9px;font-weight:700;
                      color:rgba(255,255,255,0.38);letter-spacing:{tl};
                      text-transform:uppercase;margin-bottom:6px;">Executor</div>
          <div class="display" style="font-size:30px;color:rgba(255,255,255,0.45);
                      line-height:0.90;letter-spacing:{tt};margin-bottom:14px;">FAZ.</div>
          {exec_items}
        </div>

        <div style="flex:1;
                    background:linear-gradient(160deg,rgba(30,197,242,0.12) 0%,rgba(10,15,26,0.15) 100%);
                    border:1.5px solid {pr};
                    border-radius:{rl}px;padding:16px 14px;
                    box-shadow:0 0 44px rgba(30,197,242,0.22),
                               inset 0 1px 0 rgba(255,255,255,0.06);">
          <div style="font-family:{bf};font-size:9px;font-weight:700;
                      color:{pr};letter-spacing:{tl};
                      text-transform:uppercase;margin-bottom:6px;">Resolvedor</div>
          <div class="display" style="font-size:30px;color:{pr};
                      line-height:0.90;letter-spacing:{tt};margin-bottom:14px;
                      text-shadow:0 0 24px rgba(30,197,242,0.50);">RESOLVE.</div>
          {resv_items}
        </div>
      </div>

      <div style="position:absolute;bottom:36px;left:24px;right:24px;z-index:10;
                  text-align:center;">
        <div style="font-family:{bf};font-size:11px;font-weight:300;
                    color:rgba(255,255,255,0.50);letter-spacing:0.02em;">
          Um entrega o escopo. <strong style="color:#fff;font-weight:700;">O outro entrega a virada.</strong>
        </div>
      </div>

      {progress_bar(6, TOTAL)}
    </div>'''

# ============================================================
# SLIDE 7 — PRINCÍPIO / BLEED TEXT
# Anton gigante sangrando fora da tela — efeito editorial de revista
# ============================================================
def slide7():
    return f'''<div class="slide" style="background:{INK["rich"]};overflow:hidden;">
      {overlay_noise(0.45)}
      {overlay_vignette(0.35)}
      {slide_index(7, TOTAL)}

      <!-- TIPOGRAFIA SANGRANDO -->
      <div style="position:absolute;top:50%;left:0;right:0;z-index:10;
                  transform:translateY(-52%);padding-left:22px;">

        {kicker("O Princípio", color="rgba(255,255,255,0.50)")}

        <div style="margin-top:16px;line-height:0.86;">
          <div class="display" style="font-size:70px;color:#fff;
                      line-height:0.86;letter-spacing:-0.02em;
                      text-shadow:0 8px 40px rgba(0,0,0,0.40);">OPERAÇÃO</div>
          <div class="display" style="font-size:70px;
                      background:linear-gradient(95deg,{ACCENT["primary"]} 0%,{ACCENT["vivid"]} 100%);
                      -webkit-background-clip:text;background-clip:text;
                      -webkit-text-fill-color:transparent;
                      line-height:0.86;letter-spacing:-0.02em;">CONSTRÓI.</div>
        </div>

        <div style="margin-top:28px;max-width:320px;">
          <div style="height:1.5px;width:36px;
                      background:rgba(255,255,255,0.30);margin-bottom:14px;
                      border-radius:2px;"></div>
          <div style="font-family:{FONTS["body"]};font-size:14px;font-weight:400;
                      color:rgba(255,255,255,0.75);line-height:1.58;">
            Não o que você fez.<br>
            Não o que você entregou.<br>
            <strong style="color:#fff;font-weight:700;">O que você estruturou — permanece.</strong>
          </div>
        </div>
      </div>

      {progress_bar(7, TOTAL)}
    </div>'''

# ============================================================
# SLIDE 8 — ESPELHO (reflexão final, sem CTA comercial)
# Lucas + Derick — pergunta que o leitor leva pra casa
# ============================================================
def slide8():
    img = photo_uri("lucas_derick.jpeg")
    pos = photo_position("lucas_derick.jpeg")
    return f'''<div class="slide" style="background:{INK["void"]};">
      {logo_mark(dark_bg=True, size=26)}
      {slide_index(8, TOTAL)}

      <div style="position:absolute;inset:0;z-index:1;">
        <img src="{img}" style="width:100%;height:100%;object-fit:cover;
                   object-position:{pos};filter:contrast(1.10) saturate(0.95) brightness(0.48);">
        <div style="position:absolute;inset:0;background:linear-gradient(180deg,
                    rgba(10,15,26,0.88) 0%, rgba(10,15,26,0.42) 30%,
                    rgba(10,15,26,0.52) 62%, rgba(10,15,26,0.97) 100%);"></div>
      </div>

      {overlay_noise(0.28, blend="soft-light", z=4)}
      {overlay_vignette(0.32)}

      <div style="position:absolute;top:76px;left:26px;right:26px;z-index:15;">
        {kicker("A Pergunta Que Fica", color="rgba(255,255,255,0.62)")}

        <div style="margin-top:16px;line-height:0.90;">
          <div class="display" style="font-size:44px;color:#fff;
                      letter-spacing:{TRACK["tight"]};
                      text-shadow:0 4px 22px rgba(0,0,0,0.60);">SE VOCÊ</div>
          <div class="display" style="font-size:44px;color:#fff;
                      letter-spacing:{TRACK["tight"]};
                      text-shadow:0 4px 22px rgba(0,0,0,0.60);">SUMISSE POR</div>
          <div class="display" style="font-size:44px;color:{ACCENT["primary"]};
                      letter-spacing:{TRACK["tight"]};
                      text-shadow:0 4px 22px rgba(0,0,0,0.60),
                                  0 0 36px rgba(30,197,242,0.40);">30 DIAS —</div>
          <div class="display" style="font-size:38px;color:#fff;margin-top:4px;
                      letter-spacing:{TRACK["tight"]};
                      text-shadow:0 4px 22px rgba(0,0,0,0.60);">O QUE PARARIA?</div>
        </div>
      </div>

      <div style="position:absolute;bottom:48px;left:26px;right:26px;z-index:18;">
        <div style="height:1px;width:44px;background:rgba(255,255,255,0.32);
                    margin-bottom:16px;"></div>
        <div style="font-family:{FONTS["body"]};font-size:13.5px;font-weight:400;
                    color:rgba(255,255,255,0.82);line-height:1.52;max-width:340px;">
          A resposta diz tudo sobre<br>
          <strong style="color:#fff;font-weight:700;">quem realmente sustenta a sua operação.</strong>
        </div>
        <div style="margin-top:18px;font-family:{FONTS["body"]};font-size:9px;
                    font-weight:600;color:rgba(255,255,255,0.40);
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
caption = ("Executor ou Resolvedor? Se você sumisse por 30 dias, o que pararia? "
           "A resposta diz tudo sobre quem sustenta sua operação.")
html = html_shell(slides, TOTAL, caption)

OUT = Path("/home/user/Meu-espa-o/nucvision-editorial.html")
OUT.write_text(html, encoding="utf-8")
print(f"OK {OUT} ({len(html):,} chars)")
