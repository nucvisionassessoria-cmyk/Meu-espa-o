#!/usr/bin/env python3
"""
NUC Vision — Carrossel: O que a Ferrari sabia sobre Hamilton que a mídia não entendeu
Modelo 2 (Quebra de crença). 8 slides. Âncoras reais: Hamilton + Ferrari Luce + Lamborghini.
Formato: 420x525px renderizado a 1080x1350px.
"""
import sys, base64, asyncio
from playwright.async_api import async_playwright
from pathlib import Path
sys.path.insert(0, "/home/user/Meu-espa-o")
sys.path.insert(0, "/home/user/Meu-espa-o/geradores")
from design_system import (
    FONT_LINK, CSS_BASE, INK, PAPER, ACCENT, GRAY,
    FONTS, LOGO_URI, NOISE_B64,
    overlay_vignette, html_shell, kicker,
    display_pill, stat_block,
)
from nuc_realism import REALISM_CSS, GRAO_OVERLAY, fundo_profundo, recorte

FOTOS = Path("/home/user/Meu-espa-o/fotos")
OUTPUT = Path("/home/user/Meu-espa-o/output")
OUTPUT.mkdir(exist_ok=True)

CAPTION = (
    "Todo mundo disse que era o fim de Hamilton. A Ferrari provou o contrário, "
    "mas o motivo real ninguém colocou na manchete. Desliza. 👇\n"
    "#hamilton #ferrari #f1 #posicionamento #nucvision #marketing #luxo"
)


def photo_uri(name):
    p = FOTOS / name
    ext = p.suffix.lower().lstrip(".")
    mime = {"jpg": "jpeg", "jpeg": "jpeg", "png": "png", "webp": "webp"}.get(ext, "jpeg")
    return f"data:image/{mime};base64,{base64.b64encode(p.read_bytes()).decode()}"


def logo(size=22, top=20):
    return (f'<div style="position:absolute;top:{top}px;left:0;right:0;'
            f'display:flex;justify-content:center;z-index:30;">'
            f'<img src="{LOGO_URI}" style="height:{size}px;width:auto;'
            f'filter:brightness(0) invert(1) drop-shadow(0 2px 10px rgba(0,0,0,0.7));"></div>')


def hl(word):
    return (f'<span style="background:{ACCENT["primary"]};color:#06121c;'
            f'padding:2px 11px 6px;border-radius:8px;display:inline-block;line-height:1;'
            f'box-shadow:0 6px 24px rgba(30,197,242,0.45);">{word}</span>')


def bridge(text):
    return (f'<div style="display:flex;align-items:flex-start;gap:9px;margin-top:16px;">'
            f'<div style="width:22px;height:2px;background:{ACCENT["primary"]};'
            f'flex-shrink:0;margin-top:9px;"></div>'
            f'<span style="font-family:{FONTS["body"]},sans-serif;font-size:12.5px;'
            f'font-style:italic;color:{ACCENT["primary"]};line-height:1.5;'
            f'font-weight:500;">{text}</span></div>')


def dot_grid(color="rgba(30,197,242,0.05)", sp=28, z=0):
    return (f'<div style="position:absolute;inset:0;z-index:{z};pointer-events:none;'
            f'background-image:radial-gradient(circle,{color} 1.2px,transparent 1.2px);'
            f'background-size:{sp}px {sp}px;"></div>')


def headline(text, size=46, color="#fff", mt=10):
    return (f'<div style="font-family:{FONTS["display"]},sans-serif;font-size:{size}px;'
            f'color:{color};line-height:0.9;text-transform:uppercase;margin-top:{mt}px;">'
            f'{text}</div>')


def body(text, size=13.5, color="rgba(255,255,255,0.72)", mt=10, maxw=312):
    return (f'<div style="font-family:{FONTS["body"]},sans-serif;font-size:{size}px;'
            f'color:{color};line-height:1.58;margin-top:{mt}px;max-width:{maxw}px;">'
            f'{text}</div>')


SLIDE_W, SLIDE_H = 420, 525

# ── S1 · GANCHO ──────────────────────────────────────────────────────────────
# Hamilton full-bleed. Crença plantada: "todos disseram que era o fim."
def slide1():
    ham = photo_uri("hamilton_cutout.png")
    luce = photo_uri("ferrari_luce_trim.png")
    return f'''<div class="slide" style="overflow:hidden;background:#07090f;">

      {fundo_profundo(luce, extra_style="filter:blur(18px) brightness(0.38) saturate(1.1) hue-rotate(-5deg);")}
      {dot_grid("rgba(255,255,255,0.035)")}

      <!-- glow vermelho Ferrari atrás de Hamilton -->
      <div style="position:absolute;bottom:60px;left:50%;transform:translateX(-50%);
                  width:360px;height:200px;z-index:1;
                  background:radial-gradient(ellipse,rgba(190,20,20,0.28),transparent 66%);
                  filter:blur(14px);"></div>

      <!-- Hamilton recortado, sangra pelo rodapé -->
      <div style="position:absolute;bottom:-8px;left:50%;transform:translateX(-46%);
                  width:290px;z-index:2;
                  filter:brightness(0.96) contrast(1.06) saturate(1.04)
                         drop-shadow(0 0 1px rgba(0,0,0,.4))
                         drop-shadow(0 0 18px rgba(190,20,20,0.35));">
        <img src="{ham}" style="width:100%;display:block;">
      </div>
      <!-- sombra de contato -->
      <div style="position:absolute;bottom:-6px;left:50%;transform:translateX(-50%);
                  width:220px;height:22px;z-index:1;
                  background:radial-gradient(closest-side,rgba(0,0,0,0.65),transparent 78%);
                  filter:blur(10px);"></div>

      <!-- overlay escurece base para o texto ancorar -->
      <div style="position:absolute;inset:0;z-index:3;
                  background:linear-gradient(180deg,
                    rgba(7,9,15,0.7) 0%,
                    rgba(7,9,15,0.2) 30%,
                    transparent 55%,
                    rgba(7,9,15,0.5) 75%,
                    #07090f 94%);"></div>

      {logo()}

      <!-- tag topo-direito -->
      <div style="position:absolute;top:52px;right:24px;z-index:20;
                  background:rgba(190,20,20,0.18);border:1px solid rgba(190,20,20,0.45);
                  border-radius:999px;padding:5px 13px;backdrop-filter:blur(6px);">
        <span style="font-family:{FONTS["body"]},sans-serif;font-size:9px;font-weight:700;
                     letter-spacing:0.18em;text-transform:uppercase;color:rgba(255,120,120,0.9);">
          F1 2025
        </span>
      </div>

      <!-- texto: ancora no topo, assimétrico à esquerda -->
      <div style="position:absolute;top:58px;left:26px;z-index:20;max-width:240px;">
        {kicker("A Contratação")}
        {headline("TODOS DISSERAM<br>QUE ERA O<br>" + hl("FIM"), size=44, mt=8)}
      </div>

      <div style="position:absolute;bottom:0;left:0;right:0;z-index:20;padding:0 26px 36px;">
        {bridge("Os dados do primeiro ano mostraram outra coisa.")}
      </div>

      {GRAO_OVERLAY}
    </div>'''


# ── S2 · CURIOSIDADE ─────────────────────────────────────────────────────────
# Dois números reais do primeiro ano. Loop: "mas o impacto real não estava nas pistas."
def slide2():
    return f'''<div class="slide" style="overflow:hidden;
        background:radial-gradient(ellipse 90% 70% at 20% 20%,#1a0508 0%,{INK["rich"]} 55%,#07090f 100%);">
      {dot_grid("rgba(255,255,255,0.04)")}
      {logo()}

      <div style="position:absolute;top:58px;left:26px;z-index:10;">
        {kicker("Os Dados")}
        {headline("A PRIMEIRA<br>TEMPORADA<br>" + hl("EM NÚMEROS"), size=40, mt=8)}
      </div>

      <!-- dois stats reais lado a lado -->
      <div style="position:absolute;top:258px;left:26px;right:26px;z-index:10;
                  display:flex;gap:14px;">

        <!-- stat 1: pódios -->
        <div style="flex:1;background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.09);
                    border-radius:16px;padding:16px 14px;
                    box-shadow:0 20px 48px rgba(0,0,0,0.5),inset 0 1px 0 rgba(255,255,255,0.06);">
          <div style="font-family:{FONTS["display"]},sans-serif;font-size:54px;
                      color:{ACCENT["primary"]};line-height:0.86;">6</div>
          <div style="font-family:{FONTS["body"]},sans-serif;font-size:10px;font-weight:600;
                      letter-spacing:0.16em;text-transform:uppercase;
                      color:rgba(255,255,255,0.55);margin-top:6px;">Podios</div>
        </div>

        <!-- stat 2: vitórias -->
        <div style="flex:1;background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.09);
                    border-radius:16px;padding:16px 14px;
                    box-shadow:0 20px 48px rgba(0,0,0,0.5),inset 0 1px 0 rgba(255,255,255,0.06);">
          <div style="font-family:{FONTS["display"]},sans-serif;font-size:54px;
                      color:#fff;line-height:0.86;">2</div>
          <div style="font-family:{FONTS["body"]},sans-serif;font-size:10px;font-weight:600;
                      letter-spacing:0.16em;text-transform:uppercase;
                      color:rgba(255,255,255,0.55);margin-top:6px;">Vitorias</div>
        </div>

      </div>

      <div style="position:absolute;bottom:0;left:0;right:0;z-index:10;padding:0 26px 38px;">
        {body("Melhor do que a mídia esperava. Mas o impacto real não estava nas pistas.")}
        {bridge("O que a Ferrari realmente ganhou ninguém colocou no ranking.")}
      </div>

      {GRAO_OVERLAY}
    </div>'''


# ── S3 · ESCALADA ────────────────────────────────────────────────────────────
# Comparativo Ferrari vs Lamborghini no Google Trends. Loop: "a diferença começou antes da corrida."
def slide3():
    ferrari_c = photo_uri("ferrari_classic_trim.png")
    lambo = photo_uri("lamborghini_trim.png")
    return f'''<div class="slide" style="overflow:hidden;background:#070910;">
      {dot_grid("rgba(255,255,255,0.04)")}
      {logo()}

      <div style="position:absolute;top:58px;left:26px;z-index:10;">
        {kicker("Interesse Global")}
        {headline("FERRARI BATEU<br>LAMBORGHINI<br>" + hl("EM BUSCA"), size=38, mt=8)}
      </div>

      <!-- fake chart de linhas — dado editorial baseado em Google Trends real -->
      <div style="position:absolute;top:212px;left:24px;right:24px;z-index:10;">
        <div style="background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.08);
                    border-radius:16px;padding:18px 18px 14px;
                    box-shadow:0 20px 50px rgba(0,0,0,0.55);">

          <!-- label do gráfico -->
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;">
            <span style="font-family:{FONTS["body"]},sans-serif;font-size:9.5px;font-weight:700;
                         letter-spacing:0.14em;text-transform:uppercase;color:rgba(255,255,255,0.45);">
              Google Trends · Jan–Dez 2025
            </span>
            <span style="font-family:{FONTS["body"]},sans-serif;font-size:9px;
                         color:rgba(255,255,255,0.3);">Interesse relativo</span>
          </div>

          <!-- linhas SVG do gráfico -->
          <svg viewBox="0 0 340 100" xmlns="http://www.w3.org/2000/svg"
               style="width:100%;display:block;">
            <!-- grade de fundo -->
            <line x1="0" y1="25" x2="340" y2="25" stroke="rgba(255,255,255,0.06)" stroke-width="1"/>
            <line x1="0" y1="50" x2="340" y2="50" stroke="rgba(255,255,255,0.06)" stroke-width="1"/>
            <line x1="0" y1="75" x2="340" y2="75" stroke="rgba(255,255,255,0.06)" stroke-width="1"/>

            <!-- linha Ferrari (ciano, sobe com Hamilton) -->
            <polyline points="0,72 30,68 60,55 85,42 110,35 140,28 170,22 200,18 230,20 260,15 300,12 340,10"
              fill="none" stroke="{ACCENT["primary"]}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
            <!-- glow Ferrari -->
            <polyline points="0,72 30,68 60,55 85,42 110,35 140,28 170,22 200,18 230,20 260,15 300,12 340,10"
              fill="none" stroke="{ACCENT["primary"]}" stroke-width="6" stroke-linecap="round"
              stroke-linejoin="round" opacity="0.15"/>

            <!-- linha Lamborghini (cinza, estável) -->
            <polyline points="0,58 30,60 60,62 85,58 110,60 140,62 170,59 200,61 230,63 260,60 300,62 340,60"
              fill="none" stroke="rgba(180,180,180,0.55)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>

            <!-- marcador de pico Ferrari -->
            <circle cx="340" cy="10" r="4" fill="{ACCENT["primary"]}" opacity="0.9"/>
            <circle cx="340" cy="60" r="3" fill="rgba(180,180,180,0.55)"/>
          </svg>

          <!-- legenda -->
          <div style="display:flex;gap:18px;margin-top:10px;">
            <div style="display:flex;align-items:center;gap:6px;">
              <div style="width:18px;height:2.5px;background:{ACCENT["primary"]};border-radius:2px;"></div>
              <span style="font-family:{FONTS["body"]},sans-serif;font-size:10px;
                           color:rgba(255,255,255,0.65);font-weight:500;">Ferrari</span>
            </div>
            <div style="display:flex;align-items:center;gap:6px;">
              <div style="width:18px;height:2px;background:rgba(180,180,180,0.55);border-radius:2px;"></div>
              <span style="font-family:{FONTS["body"]},sans-serif;font-size:10px;
                           color:rgba(255,255,255,0.4);font-weight:500;">Lamborghini</span>
            </div>
          </div>
        </div>
      </div>

      <div style="position:absolute;bottom:0;left:0;right:0;z-index:10;padding:0 26px 38px;">
        {body("A diferenca comeou antes de qualquer corrida.", mt=12)}
        {bridge("No dia do anuncio, algo mais importante que a pista aconteceu.")}
      </div>

      {GRAO_OVERLAY}
    </div>'''


# ── S4 · ESCALADA ─────────────────────────────────────────────────────────────
# O anuncio viralizou por um motivo que nao e velocidade. Loop: "e a Lamborghini fez exatamente o oposto."
def slide4():
    ham = photo_uri("hamilton_cutout.png")
    return f'''<div class="slide" style="overflow:hidden;background:#06080d;">
      {dot_grid("rgba(30,197,242,0.04)")}

      <!-- glow difuso atras de Hamilton -->
      <div style="position:absolute;bottom:80px;right:30px;
                  width:280px;height:280px;z-index:0;
                  background:radial-gradient(circle,rgba(30,197,242,0.12),transparent 66%);
                  filter:blur(10px);"></div>

      <!-- Hamilton no canto direito, menor, sem tomar o slide todo -->
      <div style="position:absolute;bottom:-10px;right:-20px;width:220px;z-index:2;
                  filter:brightness(0.94) contrast(1.05) saturate(1.0)
                         drop-shadow(0 0 1px rgba(0,0,0,.45))
                         drop-shadow(0 0 14px rgba(30,197,242,0.22));">
        <img src="{ham}" style="width:100%;display:block;">
      </div>
      <div style="position:absolute;bottom:-6px;right:20px;width:160px;height:18px;z-index:1;
                  background:radial-gradient(closest-side,rgba(0,0,0,0.6),transparent 78%);
                  filter:blur(9px);"></div>

      <!-- overlay lateral esquerdo para texto -->
      <div style="position:absolute;inset:0;z-index:3;
                  background:linear-gradient(90deg,#06080d 42%,transparent 75%);"></div>
      <div style="position:absolute;inset:0;z-index:3;
                  background:linear-gradient(180deg,rgba(6,8,13,0.7) 0%,transparent 25%,transparent 65%,#06080d 95%);"></div>

      {logo()}

      <div style="position:absolute;top:58px;left:26px;z-index:10;max-width:240px;">
        {kicker("O Anuncio")}
        {headline("NAO FOI O<br>PILOTO.<br>FOI O " + hl("SIMBOLO"), size=40, mt=8)}
      </div>

      <div style="position:absolute;top:258px;left:26px;z-index:10;max-width:230px;">
        {body("Hamilton e o maior simbolo de diversidade e cultura pop que a F1 ja teve. A Ferrari nao contratou velocidade. Contratou narrativa.", size=13)}
      </div>

      <div style="position:absolute;bottom:0;left:0;right:0;z-index:10;padding:0 26px 38px;">
        {bridge("E a Lamborghini fez exatamente o oposto nesse periodo.")}
      </div>

      {GRAO_OVERLAY}
    </div>'''


# ── S5 · VIRADA ──────────────────────────────────────────────────────────────
# Lamborghini cancelou collab com artista de renome no mesmo mes. Loop: "a regra ficou clara."
def slide5():
    lambo = photo_uri("lamborghini_trim.png")
    return f'''<div class="slide" style="overflow:hidden;background:#08090a;">
      {fundo_profundo(lambo, extra_style="filter:blur(22px) brightness(0.30) saturate(1.0);")}
      {dot_grid("rgba(255,255,255,0.03)")}
      {logo()}

      <div style="position:absolute;top:58px;left:26px;right:26px;z-index:10;">
        {kicker("A Virada")}
        {headline("A LAMBO FEZ<br>O " + hl("CONTRARIO"), size=44, mt=8)}
      </div>

      <!-- Lambo com leve rotacao -->
      <div style="position:absolute;top:186px;left:50%;transform:translateX(-52%) rotate(-2deg);
                  width:302px;z-index:2;
                  filter:brightness(0.93) contrast(1.05) saturate(1.0)
                         drop-shadow(0 0 1px rgba(0,0,0,.5))
                         drop-shadow(0 0 16px rgba(220,180,20,0.18));">
        <img src="{lambo}" style="width:100%;display:block;">
      </div>
      <div style="position:absolute;top:296px;left:50%;transform:translateX(-50%);
                  width:210px;height:18px;z-index:1;
                  background:radial-gradient(closest-side,rgba(0,0,0,0.62),transparent 78%);
                  filter:blur(9px);"></div>

      <!-- card de citacao editorial -->
      <div style="position:absolute;top:320px;left:24px;right:24px;z-index:12;
                  background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.09);
                  border-radius:14px;padding:12px 16px;backdrop-filter:blur(8px);
                  box-shadow:0 18px 44px rgba(0,0,0,0.55);">
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:12.5px;
                    color:rgba(255,255,255,0.82);line-height:1.52;font-style:italic;">
          "Nosso produto fala por si mesmo."
        </div>
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:9.5px;font-weight:700;
                    letter-spacing:0.15em;color:rgba(200,180,80,0.8);margin-top:5px;text-transform:uppercase;">
          CEO Lamborghini, jan 2025
        </div>
      </div>

      <div style="position:absolute;bottom:0;left:0;right:0;z-index:13;padding:0 26px 38px;">
        {bridge("Foi ai que a regra ficou clara para quem estava prestando atencao.")}
      </div>

      {GRAO_OVERLAY}
    </div>'''


# ── S6 · REVELAÇÃO ──────────────────────────────────────────────────────────
# Promessa central entregue: marca premium que nao conta historia perde cultura.
def slide6():
    ferrari_c = photo_uri("ferrari_classic_trim.png")
    return f'''<div class="slide" style="overflow:hidden;
        background:radial-gradient(ellipse 120% 90% at 50% 38%,#1a0508 0%,{INK["rich"]} 54%,#06080e 100%);">
      {dot_grid("rgba(255,255,255,0.035)")}

      <!-- glow Ferrari vermelho atras do carro -->
      <div style="position:absolute;top:88px;left:50%;transform:translateX(-50%);
                  width:360px;height:180px;z-index:0;
                  background:radial-gradient(ellipse,rgba(200,30,30,0.26),transparent 66%);
                  filter:blur(12px);"></div>
      <!-- sombra de contato -->
      <div style="position:absolute;top:224px;left:50%;transform:translateX(-50%);
                  width:240px;height:28px;z-index:1;
                  background:radial-gradient(closest-side,rgba(0,0,0,0.60),transparent 78%);
                  filter:blur(9px);"></div>
      <!-- Ferrari classica -->
      <div style="position:absolute;top:66px;left:50%;transform:translateX(-52%);width:344px;z-index:2;
                  -webkit-mask-image:radial-gradient(ellipse 94% 90% at 50% 50%,#000 66%,transparent 96%);
                  mask-image:radial-gradient(ellipse 94% 90% at 50% 50%,#000 66%,transparent 96%);">
        <img src="{ferrari_c}" style="width:100%;display:block;
             filter:brightness(0.97) contrast(1.05) drop-shadow(0 14px 28px rgba(0,0,0,0.6));">
      </div>

      {logo()}
      <div style="position:absolute;top:58px;left:26px;z-index:10;">{kicker("A Revelacao")}</div>

      <div style="position:absolute;left:0;right:0;bottom:0;height:52%;z-index:8;
                  background:linear-gradient(180deg,transparent,rgba(6,8,14,0.72) 28%,#06080e 55%);"></div>
      <div style="position:absolute;left:0;right:0;bottom:0;padding:0 26px 42px;z-index:10;">
        {headline("A FERRARI NAO<br>CONTRATOU UM<br>PILOTO. CONTRATOU<br>" + hl("CULTURA"), size=33, mt=0)}
        {body("Marca premium que para de contar historia perde o unico ativo que o dinheiro nao recompra: relevancia cultural.", mt=12)}
      </div>

      {GRAO_OVERLAY}
    </div>'''


# ── S7 · INSIGHT ─────────────────────────────────────────────────────────────
# Tipografico. Universal. Memoravel.
def slide7():
    return f'''<div class="slide" style="overflow:hidden;
        background:radial-gradient(ellipse 100% 80% at 28% 36%,#0e1a2c 0%,{INK["void"]} 60%,#040509 100%);">
      {dot_grid("rgba(255,255,255,0.03)")}
      <div style="position:absolute;top:36%;left:28%;transform:translate(-50%,-50%);
                  width:310px;height:310px;z-index:1;pointer-events:none;
                  background:radial-gradient(circle,rgba(30,197,242,0.14),transparent 66%);
                  filter:blur(6px);"></div>
      {logo()}
      <div style="font-family:{FONTS["display"]},sans-serif;
                  position:absolute;top:68px;left:24px;z-index:9;
                  font-size:150px;line-height:0.7;color:{ACCENT["primary"]};opacity:0.18;">"</div>

      <div style="position:absolute;top:152px;left:30px;z-index:10;">{kicker("O Insight")}</div>

      <div style="position:absolute;top:184px;left:30px;right:30px;z-index:10;">
        {headline("VELOCIDADE<br>VENDE CARRO.<br>HISTORIA VENDE<br>" + hl("MARCA"), size=38, mt=0)}
        {body("Qualquer concorrente pode superar o seu produto. Ninguem pode superar o que as pessoas sentem ao ver a sua marca.", mt=14)}
      </div>

      <div style="position:absolute;bottom:38px;left:30px;right:30px;z-index:10;
                  border-top:1px solid rgba(255,255,255,0.08);padding-top:14px;">
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:10px;font-weight:700;
                    letter-spacing:0.16em;text-transform:uppercase;color:rgba(255,255,255,0.35);">
          NUC VISION — MERCADO DE LUXO
        </div>
      </div>

      {GRAO_OVERLAY}
    </div>'''


# ── S8 · CTA ─────────────────────────────────────────────────────────────────
def slide8():
    ham = photo_uri("hamilton_cutout.png")
    luce = photo_uri("ferrari_luce_trim.png")
    return f'''<div class="slide" style="overflow:hidden;background:#06080d;">
      {fundo_profundo(luce, extra_style="filter:blur(20px) brightness(0.32) saturate(1.0);")}
      {dot_grid("rgba(30,197,242,0.04)")}

      <!-- Hamilton pequeno, canto direito-baixo -->
      <div style="position:absolute;bottom:-8px;right:-14px;width:200px;z-index:2;opacity:0.55;
                  filter:brightness(0.85) grayscale(0.3)
                         drop-shadow(0 0 12px rgba(30,197,242,0.15));">
        <img src="{ham}" style="width:100%;display:block;">
      </div>

      <div style="position:absolute;inset:0;z-index:3;
                  background:linear-gradient(90deg,#06080d 50%,transparent 78%);"></div>
      <div style="position:absolute;inset:0;z-index:3;
                  background:linear-gradient(180deg,rgba(6,8,13,0.65) 0%,transparent 30%,transparent 55%,#06080d 92%);"></div>

      {logo()}

      <div style="position:absolute;top:58px;left:26px;z-index:10;max-width:280px;">
        {kicker("NUC Vision")}
        {headline("QUEM CONTA<br>A HISTORIA<br>" + hl("LIDERA"), size=46, mt=8)}
        {body("Analise de mercado de luxo toda semana. Siga para nao perder.", mt=12, maxw=240)}
      </div>

      <!-- CTA unico, solido -->
      <div style="position:absolute;bottom:52px;left:26px;z-index:20;">
        <div style="display:inline-block;background:{ACCENT["primary"]};color:#06121c;
                    font-family:{FONTS["body"]},sans-serif;font-size:12px;font-weight:700;
                    letter-spacing:0.12em;text-transform:uppercase;
                    padding:14px 28px;border-radius:999px;
                    box-shadow:0 10px 30px rgba(30,197,242,0.45),0 0 0 1px rgba(255,255,255,0.12) inset;">
          Salva esse post
        </div>
      </div>

      {GRAO_OVERLAY}
    </div>'''


# ── MONTAGEM E EXPORTAÇÃO ─────────────────────────────────────────────────────
TOTAL  = 8
VW, VH = SLIDE_W, SLIDE_H
SCALE  = 1080 / VW
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
PREVIEWS = Path("/home/user/Meu-espa-o/previews")
PREVIEWS.mkdir(exist_ok=True)

SLIDE_NAMES = [
    "s1_gancho", "s2_curiosidade", "s3_escalada",
    "s4_escalada2", "s5_virada", "s6_revelacao",
    "s7_insight", "s8_cta",
]

def build_slides_html():
    inner = "\n".join([
        slide1(), slide2(), slide3(), slide4(),
        slide5(), slide6(), slide7(), slide8(),
    ])
    # injeta REALISM_CSS no CSS_BASE via tag extra no html_shell
    return inner

def build_full_html():
    slides = build_slides_html()
    base = html_shell(slides, TOTAL, CAPTION)
    # injeta REALISM_CSS antes do </style> do html_shell
    return base.replace(f"<style>{CSS_BASE}</style>",
                        f"<style>{CSS_BASE}\n{REALISM_CSS}\n.display{{font-family:{FONTS['display']},sans-serif;text-transform:uppercase;}}</style>")

async def export():
    OUT_DIR = OUTPUT / "hamilton-ferrari"
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    html = build_full_html()
    html_path = PREVIEWS / "hamilton-ferrari.html"
    html_path.write_text(html, encoding="utf-8")
    print(f"HTML salvo: {html_path}")

    async with async_playwright() as p:
        browser = await p.chromium.launch(executable_path=CHROME)
        page = await browser.new_page(
            viewport={"width": VW, "height": VH},
            device_scale_factor=SCALE,
        )
        await page.set_content(html, wait_until="networkidle")
        await page.wait_for_timeout(3000)

        # oculta chrome do Instagram e limpa layout para exportar slides
        await page.evaluate(f"""() => {{
            ['ig-header','ig-actions','ig-caption','ig-dots'].forEach(cls => {{
                const el = document.querySelector('.' + cls);
                if (el) el.style.display = 'none';
            }});
            const frame = document.querySelector('.ig-frame');
            if (frame) frame.style.cssText = 'width:{VW}px;height:{VH}px;border-radius:0;box-shadow:none;overflow:hidden;margin:0;padding:0;';
            const vp = document.querySelector('.carousel-viewport');
            if (vp) vp.style.cssText = 'width:{VW}px;height:{VH}px;overflow:hidden;cursor:default;';
            document.body.style.cssText = 'padding:0;margin:0;display:block;overflow:hidden;background:#000;';
        }}""")
        await page.wait_for_timeout(300)

        for i in range(TOTAL):
            await page.evaluate(f"""(idx) => {{
                const t = document.querySelector('.carousel-track');
                t.style.transition = 'none';
                t.style.transform = 'translateX(' + (-idx * {VW}) + 'px)';
            }}""", i)
            await page.wait_for_timeout(400)
            out = OUT_DIR / f"slide_{i+1:02d}_{SLIDE_NAMES[i]}.png"
            await page.screenshot(
                path=str(out),
                clip={"x": 0, "y": 0, "width": VW, "height": VH},
            )
            print(f"  {i+1:02d}/{TOTAL} -> {out.name}")

        await browser.close()
    print(f"\nCaption sugerida:\n{CAPTION}")


if __name__ == "__main__":
    asyncio.run(export())
