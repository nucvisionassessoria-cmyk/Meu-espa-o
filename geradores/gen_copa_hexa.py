#!/usr/bin/env python3
"""
NUC Vision - Carrossel Copa Hexa (MODO HYPE)
Adaptacao oportunista do post V4 "Brasil rumo ao Hexa" (29/06).
Roteiro: skills/oportunista-trend/exemplos/copa-hexa-roteiro.md
Modelo: POLEMICA. Palette override: verde+amarelo+azul Brasil + ciano NUC so no CTA.

USA OS PRIMITIVES OFICIAIS DO design_system.py (NUC):
- kicker(), display_pill(), stat_block(), glass_card(), logo_mark()
- TYPE escalas + TRACK letter-spacings + LINE line-heights
- Classe .display (Anton, uppercase, tracking tight, line 0.88)
"""
import sys, base64
from pathlib import Path
sys.path.insert(0, "/home/user/Meu-espa-o")
sys.path.insert(0, "/home/user/Meu-espa-o/geradores")
from design_system import (
    FONTS, FONT_LINK, LOGO_URI, html_shell,
    TYPE, TRACK, LINE, RADIUS, SHADOW, ACCENT, INK, PAPER, GRAY,
    kicker, display_pill, stat_block, glass_card, logo_mark,
    slide_index, photo_uri, overlay_vignette, overlay_noise,
)
from nuc_realism import REALISM_CSS, GRAO_OVERLAY

TOTAL = 8

# ============================================================
# PALETTE OVERRIDE — MODO HYPE / COPA 2026
# Suspende dark+ciano padrao NUC. Verde-amarelo-azul Brasil.
# Ciano NUC mantido APENAS no logo (institucional).
# ============================================================
VERDE   = "#009C3B"
AMARELO = "#FFDF00"
AMARELO_DARK = "#D4B300"
AZUL    = "#002776"
AZUL_DEEP = "#001A52"
BRANCO  = "#FFFFFF"

CAPTION = (
    "A Nike gastou R$ 200 milhoes pra errar a camisa do Hexa. E voce esta gastando "
    "o silencio da sua marca pra errar o maior momento de marketing do ano. Em ambos "
    "os casos, o erro e o mesmo: confundir evento com narrativa. Desliza ate o fim - "
    "no ultimo slide tem o framework. Comenta HEXA que mando direto na DM. "
    "@nucvision #copadomundo #hexa #marketing #posicionamento #pme"
)

# ============================================================
# HELPERS COPA — variantes dos primitives NUC com palette Copa
# ============================================================

def flag_stripe(top=False, bottom=False, height=6):
    """Faixa horizontal verde-amarelo-azul (codigo Brasil)."""
    pos = "top:0" if top else "bottom:0"
    return (f'<div style="position:absolute;{pos};left:0;right:0;height:{height}px;z-index:25;'
            f'background:linear-gradient(90deg,{VERDE} 0%,{VERDE} 33%,'
            f'{AMARELO} 33%,{AMARELO} 66%,{AZUL} 66%,{AZUL} 100%);'
            f'box-shadow:0 0 22px rgba(0,156,59,0.30);"></div>')

def kicker_copa(text):
    """kicker NUC com palette Copa (amarelo + tracking label oficial)."""
    return kicker(text, color=AMARELO)

def _pill_inline(word, bg, color, size):
    """Pill local com font-family completa (Anton + fallback sans-serif).
    Patch local pq display_pill() do design_system nao tem fallback e cai
    pra Times em alguns cenarios de render."""
    return (f'<span style="display:inline-block;background:{bg};color:{color};'
            f'padding:6px 18px 10px;border-radius:{RADIUS["lg"]}px;'
            f'font-family:{FONTS["display"]},sans-serif;font-size:{size}px;'
            f'font-weight:400;line-height:0.86;letter-spacing:{TRACK["tight"]};'
            f'text-transform:uppercase;box-shadow:{SHADOW["glow"]};">{word}</span>')

def display_pill_copa(word, size=None):
    """Pill: amarelo bg + azul text (palette Copa)."""
    return _pill_inline(word, AMARELO, AZUL, size or TYPE["display_md"])

def display_pill_invert(word, size=None):
    """Pill invertido: azul bg + amarelo text (pra fundo amarelo)."""
    return _pill_inline(word, AZUL, AMARELO, size or TYPE["display_md"])

def bridge_copa(text):
    """Bridge italic NUC com linha + cor amarela (palette Copa)."""
    return (f'<div style="display:flex;align-items:flex-start;gap:10px;margin-top:18px;">'
            f'<div style="width:24px;height:2px;background:{AMARELO};flex-shrink:0;margin-top:8px;'
            f'box-shadow:0 0 12px rgba(255,223,0,0.55);"></div>'
            f'<span style="font-family:{FONTS["body"]},sans-serif;font-size:{TYPE["body"]}px;'
            f'font-style:italic;color:{AMARELO};line-height:{LINE["headline"]};'
            f'font-weight:500;letter-spacing:0.01em;">{text}</span></div>')

def stat_block_copa(number, label):
    """stat_block NUC com numero amarelo + label branco."""
    return stat_block(number, label, accent_color=AMARELO, dark=True)

def kicker_pill_topo(text):
    """Kicker dentro de glass_card escuro no topo (estilo NUC + Copa)."""
    inner = (f'<div style="font-family:{FONTS["body"]},sans-serif;font-size:{TYPE["kicker"]}px;'
             f'font-weight:700;color:{AMARELO};letter-spacing:{TRACK["label"]};'
             f'text-transform:uppercase;">{text}</div>')
    return (f'<div style="position:absolute;top:60px;left:0;right:0;'
            f'display:flex;justify-content:center;z-index:14;">'
            f'<div style="padding:7px 16px;background:rgba(0,10,31,0.65);'
            f'backdrop-filter:blur(12px) saturate(160%);'
            f'-webkit-backdrop-filter:blur(12px) saturate(160%);'
            f'border:1px solid rgba(255,223,0,0.22);border-radius:{RADIUS["pill"]}px;'
            f'box-shadow:{SHADOW["card"]};">{inner}</div></div>')


# ============================================================
# SLIDE 1 — GANCHO (Vinicius beijando escudo do V4)
# ============================================================
def slide1():
    vini = photo_uri("copa_vinicius_escudo.jpg")
    return f'''<div class="slide" style="overflow:hidden;
        background:radial-gradient(ellipse 130% 95% at 50% 30%,#C7510B 0%,#7E2606 60%,#1A0500 100%);">
      <div style="position:absolute;top:0;left:0;right:0;bottom:0;z-index:2;
                  background:url('{vini}') center 0%/cover no-repeat;
                  filter:contrast(1.06) saturate(1.08) brightness(0.97);"></div>
      <div style="position:absolute;inset:0;z-index:3;
                  background:radial-gradient(ellipse 120% 90% at 50% 30%,
                    transparent 35%,rgba(0,0,0,0.45) 78%,rgba(0,0,0,0.82) 100%);"></div>
      <div style="position:absolute;bottom:0;left:0;right:0;height:58%;z-index:4;
                  background:linear-gradient(180deg,transparent 0%,
                    rgba(0,10,31,0.78) 35%,rgba(0,10,31,0.97) 100%);"></div>
      {flag_stripe(top=True, height=6)}
      {logo_mark(dark_bg=True, size=26, position="top-center")}
      {kicker_pill_topo("LEITURA DE MERCADO · COPA 2026")}

      <!-- Headline ANTON oficial com classe display + escala TYPE -->
      <div style="position:absolute;bottom:95px;left:22px;right:22px;z-index:12;">
        <div class="display" style="font-size:{TYPE["display_md"]}px;color:{BRANCO};
                    text-shadow:0 4px 18px rgba(0,0,0,0.65);">
          A NIKE ACABOU<br>DE {display_pill_copa("ERRAR", size=TYPE["display_md"])}<br>A CAMISA DO HEXA.
        </div>
      </div>
      <div style="position:absolute;bottom:28px;left:22px;right:22px;z-index:12;">
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:{TYPE["body"]}px;font-weight:500;
                    color:rgba(255,255,255,0.85);line-height:{LINE["headline"]};
                    text-shadow:0 2px 6px rgba(0,0,0,0.7);">
          R$ 200 milhões em ativação — pro pior marketing de Copa do ano.
        </div>
        <div style="margin-top:10px;display:inline-flex;align-items:center;gap:8px;
                    font-family:{FONTS["body"]},sans-serif;font-size:{TYPE["caption"]}px;font-weight:700;
                    color:{AMARELO};letter-spacing:{TRACK["kicker"]};text-transform:uppercase;">
          DESLIZE <span style="font-size:16px;">›››</span>
        </div>
      </div>
    </div>'''


# ============================================================
# SLIDE 2 — CURIOSIDADE (tipografico puro, fundo azul Brasil)
# ============================================================
def slide2():
    return f'''<div class="slide" style="overflow:hidden;
        background:linear-gradient(165deg,{AZUL_DEEP} 0%,{AZUL} 55%,#000A1F 100%);">
      {logo_mark(dark_bg=True, size=26, position="top-center")}
      <div style="position:absolute;top:70px;left:28px;right:28px;z-index:10;">
        {kicker_copa("01 · O FATO")}
        <div class="display" style="font-size:{TYPE["display_md"]}px;color:{BRANCO};
                    margin-top:18px;">
          A CAMISA EM SI<br>{display_pill_copa("AGRADOU")}.
        </div>
        <div class="display" style="font-size:{TYPE["display_md"]}px;color:rgba(255,255,255,0.42);
                    margin-top:14px;">
          A HISTÓRIA QUE<br>A NIKE CONTOU<br>EM CIMA DELA,
        </div>
        <div class="display" style="font-size:{TYPE["display_lg"]}px;color:{AMARELO};
                    margin-top:8px;text-shadow:0 4px 22px rgba(255,223,0,0.25);">
          NÃO.
        </div>
      </div>
      <div style="position:absolute;bottom:42px;left:28px;right:28px;z-index:12;">
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:{TYPE["body"]}px;font-weight:500;
                    color:rgba(255,255,255,0.65);line-height:{LINE["headline"]};">
          Gola retrô, amarelo clássico, geometrias da bandeira — todos<br>
          os códigos certos no produto.
        </div>
        {bridge_copa("E mesmo assim, o torcedor não comprou a narrativa.")}
      </div>
      {overlay_vignette(0.32, z=3)}
    </div>'''


# ============================================================
# SLIDE 3 — ESCALADA (fundo claro NUC, respiro editorial)
# ============================================================
def slide3():
    return f'''<div class="slide" style="overflow:hidden;
        background:linear-gradient(180deg,{PAPER["warm"]} 0%,{PAPER["soft"]} 100%);">
      {logo_mark(dark_bg=False, size=26, position="top-center")}
      <div style="position:absolute;top:70px;left:28px;right:28px;z-index:10;">
        {kicker("02 · A REGRA", color=VERDE)}
        <div class="display" style="font-size:{TYPE["display_md"]}px;color:{AZUL};
                    margin-top:18px;">
          MARCA NÃO SE<br>CONSTRÓI NO<br>{display_pill_copa("PRODUTO")}.
        </div>
        <div class="display" style="font-size:{TYPE["headline"]}px;color:rgba(0,39,118,0.55);
                    margin-top:16px;letter-spacing:{TRACK["tight"]};line-height:{LINE["headline"]};">
          SE CONSTRÓI<br>NA NARRATIVA<br>EM VOLTA DELE.
        </div>
      </div>
      <div style="position:absolute;bottom:42px;left:28px;right:28px;z-index:12;">
        <div style="height:1px;background:rgba(0,39,118,0.18);margin-bottom:18px;"></div>
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:{TYPE["body"]}px;font-weight:500;
                    color:rgba(0,39,118,0.78);line-height:{LINE["headline"]};">
          O produto pode ser excelente. Se a história que a marca<br>
          conta em volta dele não casar com o que o público sente,<br>
          ele <strong>falha como produto cultural</strong>.
        </div>
        <div style="display:flex;align-items:flex-start;gap:10px;margin-top:18px;">
          <div style="width:24px;height:2px;background:{VERDE};flex-shrink:0;margin-top:8px;"></div>
          <span style="font-family:{FONTS["body"]},sans-serif;font-size:{TYPE["body"]}px;
                font-style:italic;color:{VERDE};line-height:{LINE["headline"]};font-weight:500;">
            E é aqui que a maioria das empresas erra.
          </span>
        </div>
      </div>
      {flag_stripe(bottom=True, height=4)}
    </div>'''


# ============================================================
# SLIDE 4 — VIRADA (Neymar+Ancelotti com taca, do V4)
# ============================================================
def slide4():
    foto = photo_uri("copa_neymar_ancelotti.jpg")
    return f'''<div class="slide" style="overflow:hidden;
        background:linear-gradient(180deg,#01270F 0%,#013D1A 45%,#000A1F 100%);">
      {logo_mark(dark_bg=True, size=26, position="top-center")}
      <div style="position:absolute;top:72px;left:0;right:0;display:flex;
                  justify-content:center;z-index:10;">
        {kicker("03 · A VIRADA", color=AMARELO)}
      </div>
      <!-- Numeral 24 atras como elemento atmosferico -->
      <div style="position:absolute;top:70px;left:0;right:0;text-align:center;z-index:2;
                  font-family:{FONTS["display"]},sans-serif;font-size:280px;
                  color:rgba(255,223,0,0.08);line-height:1;
                  letter-spacing:{TRACK["tightest"]};">
        24
      </div>
      <div style="position:absolute;top:108px;left:22px;right:22px;z-index:12;text-align:center;">
        <div class="display" style="font-size:{TYPE["display_md"]}px;color:{BRANCO};">
          A NARRATIVA<br>DO HEXA JÁ<br>{display_pill_copa("ESTAVA PRONTA", size=TYPE["headline"])}
        </div>
        <div class="display" style="font-size:{TYPE["headline_sm"]}px;color:rgba(255,255,255,0.85);
                    margin-top:12px;letter-spacing:{TRACK["tight"]};">
          HÁ 24 ANOS.
        </div>
      </div>
      <!-- Faixa horizontal Neymar+Ancelotti embaixo -->
      <div style="position:absolute;bottom:0;left:0;right:0;height:240px;z-index:8;
                  overflow:hidden;
                  background:url('{foto}') center 40%/cover no-repeat;
                  filter:contrast(1.05) saturate(1.02);"></div>
      <div style="position:absolute;bottom:200px;left:0;right:0;height:80px;z-index:9;
                  background:linear-gradient(180deg,rgba(0,10,31,1) 0%,
                    rgba(0,10,31,0.4) 60%,transparent 100%);"></div>
      <div style="position:absolute;bottom:240px;left:0;right:0;height:2px;z-index:10;
                  background:{AMARELO};opacity:0.65;
                  box-shadow:0 0 18px rgba(255,223,0,0.55);"></div>
      <div style="position:absolute;top:268px;left:22px;right:22px;z-index:12;text-align:center;">
        {bridge_copa("Maior campeã. 24 anos sem título. O melhor técnico do mundo no comando. A Nike ignorou.")}
      </div>
    </div>'''


# ============================================================
# SLIDE 5 — ESCALADA (cards R$ 200 MI vs R$ 0, palette Copa)
# ============================================================
def slide5():
    return f'''<div class="slide" style="overflow:hidden;
        background:linear-gradient(165deg,#0F1320 0%,{AZUL} 55%,{AZUL_DEEP} 100%);">
      {logo_mark(dark_bg=True, size=26, position="top-center")}
      <div style="position:absolute;top:72px;left:28px;right:28px;z-index:10;">
        {kicker_copa("04 · A ATERRISSAGEM")}
        <div class="display" style="font-size:{TYPE["display_md"]}px;color:{BRANCO};
                    margin-top:18px;">
          E A SUA EMPRESA<br>ESTÁ FAZENDO<br>{display_pill_copa("O MESMO")}<br>AGORA.
        </div>
      </div>
      <div style="position:absolute;bottom:42px;left:24px;right:24px;z-index:12;">
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:18px;">
          <div style="background:rgba(255,223,0,0.10);border:1px solid rgba(255,223,0,0.30);
                      border-radius:{RADIUS["md"]}px;padding:14px;
                      box-shadow:{SHADOW["card"]};">
            <div style="font-family:{FONTS["display"]},sans-serif;font-size:{TYPE["headline"]}px;
                        color:{AMARELO};line-height:0.9;letter-spacing:{TRACK["tight"]};">
              R$ 200 MI
            </div>
            <div style="font-family:{FONTS["body"]},sans-serif;font-size:{TYPE["caption"]}px;
                        color:rgba(255,255,255,0.72);margin-top:6px;line-height:1.35;
                        letter-spacing:{TRACK["wide"]};text-transform:uppercase;
                        font-weight:600;">
              o que a Nike gastou pra errar
            </div>
          </div>
          <div style="background:rgba(255,223,0,0.10);border:1px solid rgba(255,223,0,0.30);
                      border-radius:{RADIUS["md"]}px;padding:14px;
                      box-shadow:{SHADOW["card"]};">
            <div style="font-family:{FONTS["display"]},sans-serif;font-size:{TYPE["headline"]}px;
                        color:{AMARELO};line-height:0.9;letter-spacing:{TRACK["tight"]};">
              R$ 0
            </div>
            <div style="font-family:{FONTS["body"]},sans-serif;font-size:{TYPE["caption"]}px;
                        color:rgba(255,255,255,0.72);margin-top:6px;line-height:1.35;
                        letter-spacing:{TRACK["wide"]};text-transform:uppercase;
                        font-weight:600;">
              o que você está gastando — e perdendo
            </div>
          </div>
        </div>
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:{TYPE["body"]}px;font-weight:500;
                    color:rgba(255,255,255,0.68);line-height:{LINE["headline"]};">
          Mesma cegueira de narrativa, escala diferente. No maior<br>
          momento de marca do ano.
        </div>
      </div>
      {overlay_vignette(0.30, z=3)}
    </div>'''


# ============================================================
# SLIDE 6 — REVELACAO (fundo amarelo, contraste maximo)
# ============================================================
def slide6():
    return f'''<div class="slide" style="overflow:hidden;
        background:radial-gradient(ellipse at 50% 50%,#FFE948 0%,{AMARELO} 50%,{AMARELO_DARK} 100%);">
      {logo_mark(dark_bg=False, size=26, position="top-center")}
      <div style="position:absolute;top:72px;left:0;right:0;display:flex;
                  justify-content:center;z-index:10;">
        {kicker("05 · A REVELAÇÃO", color=AZUL)}
      </div>
      <div style="position:absolute;top:108px;left:22px;right:22px;z-index:12;">
        <div class="display" style="font-size:{TYPE["headline"]}px;color:{AZUL};
                    line-height:{LINE["display"]};">
          QUEM ENTENDE<br>O HEXA COMO<br>{display_pill_invert("NARRATIVA", size=TYPE["headline"])}
        </div>
        <div class="display" style="font-size:{TYPE["headline_sm"]}px;color:rgba(0,39,118,0.65);
                    margin-top:12px;letter-spacing:{TRACK["tight"]};">
          E NÃO COMO EVENTO,
        </div>
        <div class="display" style="font-size:{TYPE["headline"]}px;color:{AZUL};
                    margin-top:12px;">
          PEGA O REBOTE<br>SEM PATROCINAR<br>A SELEÇÃO.
        </div>
      </div>
      <div style="position:absolute;bottom:42px;left:28px;right:28px;z-index:12;text-align:center;">
        <div style="height:1px;background:rgba(0,39,118,0.30);margin-bottom:14px;"></div>
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:{TYPE["body"]}px;font-weight:600;
                    color:{AZUL};line-height:{LINE["headline"]};font-style:italic;">
          O jogo é mais simples do que a Nike fez parecer.
        </div>
      </div>
    </div>'''


# ============================================================
# SLIDE 7 — INSIGHT (fundo azul Brasil, manifesto)
# ============================================================
def slide7():
    return f'''<div class="slide" style="overflow:hidden;
        background:linear-gradient(180deg,#000A1F 0%,{AZUL} 100%);">
      {logo_mark(dark_bg=True, size=26, position="top-center")}
      <div style="position:absolute;top:72px;left:0;right:0;display:flex;
                  justify-content:center;z-index:10;">
        {kicker_copa("06 · O INSIGHT")}
      </div>
      <!-- Aspas gigantes atmosferico -->
      <div style="position:absolute;top:6px;left:14px;
                  font-family:{FONTS["display"]},sans-serif;font-size:200px;
                  color:rgba(255,223,0,0.10);line-height:1;z-index:2;
                  letter-spacing:{TRACK["tightest"]};">"</div>
      <div style="position:absolute;top:124px;left:22px;right:22px;z-index:12;">
        <div class="display" style="font-size:{TYPE["headline"]}px;color:{BRANCO};
                    line-height:{LINE["display"]};">
          VOCÊ NÃO PRECISA<br>DO {display_pill_copa("AMARELINHO", size=TYPE["headline"])}<br>NA CAMISA.
        </div>
        <div style="height:1px;background:rgba(255,223,0,0.40);margin:22px 0;
                    box-shadow:0 0 12px rgba(255,223,0,0.30);"></div>
        <div class="display" style="font-size:{TYPE["headline"]}px;color:{AMARELO};
                    line-height:{LINE["display"]};
                    text-shadow:0 0 22px rgba(255,223,0,0.25);">
          PRECISA DELE<br>NA HISTÓRIA QUE<br>VOCÊ CONTA.
        </div>
      </div>
      <div style="position:absolute;bottom:42px;left:28px;right:28px;z-index:12;text-align:center;">
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:{TYPE["caption"]}px;font-weight:700;
                    color:rgba(255,255,255,0.55);line-height:1.5;
                    letter-spacing:{TRACK["label"]};text-transform:uppercase;">
          NUC Vision · Marketing, Vendas & Performance
        </div>
      </div>
      {flag_stripe(bottom=True, height=6)}
    </div>'''


# ============================================================
# SLIDE 8 — CTA (selecao em formacao do V4 + CTA Comente HEXA)
# ============================================================
def slide8():
    selecao = photo_uri("copa_selecao_formacao.jpg")
    tatica_svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 525" '
                  'preserveAspectRatio="xMidYMid slice">'
                  '<g stroke="rgba(255,255,255,0.16)" stroke-width="1.5" fill="none">'
                  '<circle cx="210" cy="262" r="62"/>'
                  '<line x1="210" y1="0" x2="210" y2="525"/>'
                  '<rect x="0" y="0" width="420" height="525"/>'
                  '<rect x="60" y="0" width="300" height="120"/>'
                  '<rect x="120" y="0" width="180" height="60"/>'
                  '<path d="M 80 360 Q 150 300 200 320" stroke-dasharray="6 5"/>'
                  '<path d="M 340 360 Q 270 300 230 320" stroke-dasharray="6 5"/>'
                  '</g></svg>')
    import base64 as _b64
    tatica_b64 = _b64.b64encode(tatica_svg.encode()).decode()

    return f'''<div class="slide" style="overflow:hidden;
        background:linear-gradient(165deg,#000A1F 0%,{AZUL} 50%,#001440 100%);">
      <!-- Foto selecao no topo -->
      <div style="position:absolute;top:0;left:0;right:0;height:320px;z-index:2;
                  background:url('{selecao}') center 35%/cover no-repeat;
                  filter:contrast(1.06) saturate(1.05);"></div>
      <div style="position:absolute;top:200px;left:0;right:0;height:160px;z-index:3;
                  background:linear-gradient(180deg,transparent 0%,
                    rgba(1,39,22,0.85) 65%,rgba(1,61,26,1) 100%);"></div>
      <!-- Fundo verde com tatica abaixo -->
      <div style="position:absolute;top:320px;left:0;right:0;bottom:0;z-index:4;
                  background:linear-gradient(180deg,#013D1A 0%,{VERDE} 50%,#003015 100%);"></div>
      <div style="position:absolute;top:320px;left:0;right:0;bottom:0;z-index:5;
                  background-image:url('data:image/svg+xml;base64,{tatica_b64}');
                  background-size:cover;opacity:0.9;"></div>
      <div style="position:absolute;top:318px;left:0;right:0;height:3px;z-index:8;
                  background:{AMARELO};box-shadow:0 0 22px rgba(255,223,0,0.65);"></div>
      {logo_mark(dark_bg=True, size=26, position="top-center")}
      {kicker_pill_topo("A COMISSÃO TÉCNICA · NUC VISION")}

      <!-- Headline + CTA usando primitives oficiais (sizes reduzidos) -->
      <div style="position:absolute;top:332px;left:22px;right:22px;z-index:14;text-align:center;">
        <div class="display" style="font-size:{TYPE["headline_sm"]}px;color:{BRANCO};
                    text-shadow:0 3px 12px rgba(0,0,0,0.55);">
          FRAMEWORK DE MARCA<br>PRA COPA · {display_pill_copa("GRÁTIS", size=TYPE["headline_sm"])}
        </div>
        <div style="margin-top:8px;font-family:{FONTS["body"]},sans-serif;font-size:{TYPE["caption"]}px;
                    font-weight:500;color:rgba(255,255,255,0.88);line-height:{LINE["headline"]};
                    text-shadow:0 2px 6px rgba(0,0,0,0.4);">
          Como pegar o rebote do Hexa sem patrocinar a seleção.
        </div>
      </div>
      <!-- CTA full-width oficial (palette Copa) -->
      <div style="position:absolute;bottom:18px;left:18px;right:18px;z-index:15;
                  background:{AMARELO};border-radius:{RADIUS["md"]}px;padding:14px 16px;
                  display:flex;align-items:center;justify-content:center;gap:12px;
                  box-shadow:0 14px 34px rgba(0,0,0,0.55),inset 0 -3px 0 rgba(0,0,0,0.18);">
        <span class="display" style="font-size:{TYPE["headline_sm"]}px;color:{AZUL};
                                     letter-spacing:{TRACK["normal"]};">COMENTE</span>
        <span style="background:{AZUL};color:{AMARELO};padding:5px 12px 7px;
                     border-radius:{RADIUS["sm"]}px;font-family:{FONTS["display"]},sans-serif;
                     font-size:{TYPE["headline_sm"]}px;letter-spacing:{TRACK["wide"]};
                     text-transform:uppercase;">HEXA</span>
        <span style="font-family:{FONTS["body"]},sans-serif;font-size:16px;color:{AZUL};">⬇</span>
      </div>
      {overlay_vignette(0.35, z=3)}
    </div>'''


def main():
    raw = [slide1(), slide2(), slide3(), slide4(), slide5(), slide6(), slide7(), slide8()]
    parts = []
    for s in raw:
        idx = s.rfind("</div>")
        parts.append(s[:idx] + GRAO_OVERLAY + s[idx:])
    slides = f"<style>{REALISM_CSS}</style>" + "".join(parts)
    html = html_shell(slides, TOTAL, CAPTION)
    out = Path("/home/user/Meu-espa-o/previews/nucvision-copa-hexa.html")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print(f"OK preview: {out}")


if __name__ == "__main__":
    main()
