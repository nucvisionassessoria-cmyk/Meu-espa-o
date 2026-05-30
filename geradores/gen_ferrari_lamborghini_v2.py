#!/usr/bin/env python3
"""
NUC Vision — Carrossel Ferrari Luce: A História do Colapso
Gerado do zero: Modelo 3 (História), âncoras reais como heróis visuais.
Formato: 420×525px → exportado a 1080×1350px.
"""
import sys, base64
from pathlib import Path
sys.path.insert(0, "/home/user/Meu-espa-o")
sys.path.insert(0, "/home/user/Meu-espa-o/geradores")
from design_system import (
    FONT_LINK, CSS_BASE, INK, PAPER, ACCENT, GRAY,
    FONTS, LOGO_URI, NOISE_B64,
    overlay_vignette, html_shell,
)
from nuc_realism import REALISM_CSS, GRAO_OVERLAY, fundo_profundo

FOTOS = Path("/home/user/Meu-espa-o/fotos")
TOTAL = 8
CAPTION = (
    "Dois homens. Um carro azul. E uma das marcas mais lendárias do mundo "
    "prestes a perder bilhões — sem saber ainda. O que aconteceu com a Ferrari "
    "é uma das maiores lições de posicionamento dos últimos anos. Desliza. 👇\n"
    "#ferrari #posicionamento #marketing #lamborghini #nucvision #estrategia"
)

def photo_uri(name):
    p = FOTOS / name
    ext = p.suffix.lower().lstrip(".")
    mime = {"jpg":"jpeg","jpeg":"jpeg","png":"png","webp":"webp"}.get(ext,"jpeg")
    return f"data:image/{mime};base64,{base64.b64encode(p.read_bytes()).decode()}"

def logo(size=22, top=20):
    return (f'<div style="position:absolute;top:{top}px;left:0;right:0;'
            f'display:flex;justify-content:center;z-index:30;">'
            f'<img src="{LOGO_URI}" style="height:{size}px;width:auto;'
            f'filter:brightness(0) invert(1) drop-shadow(0 2px 10px rgba(0,0,0,0.7));"></div>')

def kicker(text):
    return (f'<div style="font-family:{FONTS["body"]},sans-serif;font-size:10px;'
            f'font-weight:700;letter-spacing:0.22em;text-transform:uppercase;'
            f'color:{ACCENT["primary"]};margin-bottom:10px;">{text}</div>')

def hl(word):
    return (f'<span style="background:{ACCENT["primary"]};color:#06121c;'
            f'padding:0 11px 5px;border-radius:8px;'
            f'box-shadow:0 6px 24px rgba(30,197,242,0.45);">{word}</span>')

def bridge(text):
    return (f'<div style="display:flex;align-items:flex-start;gap:9px;margin-top:16px;">'
            f'<div style="width:22px;height:2px;background:{ACCENT["primary"]};'
            f'flex-shrink:0;margin-top:9px;"></div>'
            f'<span style="font-family:{FONTS["body"]},sans-serif;font-size:12.5px;'
            f'font-style:italic;color:{ACCENT["primary"]};line-height:1.5;'
            f'font-weight:500;">{text}</span></div>')

def dot_grid(color="rgba(30,197,242,0.06)", sp=28, z=0):
    return (f'<div style="position:absolute;inset:0;z-index:{z};pointer-events:none;'
            f'background-image:radial-gradient(circle,{color} 1.2px,transparent 1.2px);'
            f'background-size:{sp}px {sp}px;"></div>')

def news_card(img_uri, headline, source="Forbes Brasil"):
    """Card de manchete real — âncora de prova factual."""
    return (
        f'<div style="background:#fff;border-radius:14px;overflow:hidden;'
        f'box-shadow:0 20px 60px rgba(0,0,0,0.65),0 2px 0 rgba(255,255,255,0.08) inset;">'
        f'<img src="{img_uri}" style="width:100%;display:block;height:110px;object-fit:cover;">'
        f'<div style="padding:10px 13px 13px;">'
        f'<div style="font-family:{FONTS["body"]},sans-serif;font-size:9px;font-weight:700;'
        f'letter-spacing:0.15em;text-transform:uppercase;color:#c00;margin-bottom:5px;">{source}</div>'
        f'<div style="font-family:{FONTS["body"]},sans-serif;font-size:12.5px;font-weight:700;'
        f'color:#111;line-height:1.4;">{headline}</div>'
        f'</div></div>'
    )


# ── S1 · GANCHO ──────────────────────────────────────────────────────────────
# Herói: foto do THE REVEAL — evento real, cena documental
# Técnica: full-bleed com overlay + título cortado pelo carro

def slide1():
    reveal = photo_uri("Captura de tela 2026-05-29 205423.png")
    return f'''<div class="slide" style="overflow:hidden;background:#06080e;">

      <!-- REVEAL foto como hero full-bleed -->
      <div style="position:absolute;inset:0;z-index:0;">
        <img src="{reveal}" style="width:100%;height:100%;object-fit:cover;
             filter:brightness(0.55) saturate(0.9) contrast(1.05);">
      </div>

      <!-- overlay gradiente: abre no topo, fecha embaixo -->
      <div style="position:absolute;inset:0;z-index:1;
                  background:linear-gradient(180deg,
                    rgba(6,8,14,0.62) 0%,
                    transparent 30%,
                    transparent 52%,
                    rgba(6,8,14,0.75) 70%,
                    #06080e 92%);"></div>

      <!-- tag "evento real" top-right -->
      <div style="position:absolute;top:52px;right:28px;z-index:20;
                  background:rgba(255,255,255,0.10);border:1px solid rgba(255,255,255,0.25);
                  border-radius:999px;padding:5px 13px;backdrop-filter:blur(6px);">
        <span style="font-family:{FONTS["body"]},sans-serif;font-size:9px;font-weight:700;
                     letter-spacing:0.18em;text-transform:uppercase;color:#fff;">
          MAI 2026 · AO VIVO
        </span>
      </div>

      {logo()}

      <!-- TÍTULO: ancora no rodapé, grande, com linha de kicker -->
      <div style="position:absolute;bottom:0;left:0;right:0;z-index:10;padding:0 28px 40px;">
        {kicker("O Lançamento")}
        <div class="display" style="font-size:50px;color:#fff;line-height:0.88;
                    text-shadow:0 4px 30px rgba(0,0,0,0.9);">
          DOIS HOMENS.<br>UM CARRO {hl("AZUL")}.
        </div>
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:13px;
                    color:rgba(255,255,255,0.72);line-height:1.55;margin-top:10px;max-width:310px;">
          Naquela sala, ninguém sabia ainda o que ia acontecer
          com o valor da marca nas próximas 24 horas.
        </div>
        {bridge("O que aconteceu naquela sala mudou a Ferrari para sempre.")}
      </div>
    </div>'''


# ── S2 · CURIOSIDADE ─────────────────────────────────────────────────────────
# Ferrari + Apple — a aposta máxima. Loop: "a imprensa celebrou. Até as ações abrirem."

def slide2():
    luce = photo_uri("FERRARI_LUCE_FRONT_3Q_16x9_RGB_WEB_SOCIALS_1920x1080-1000x1000.png")
    return f'''<div class="slide" style="overflow:hidden;background:#080b12;">
      {fundo_profundo(luce, extra_style="filter:blur(22px) brightness(0.38) saturate(1.1);")}
      {dot_grid("rgba(255,255,255,0.04)")}
      {logo()}

      <div style="position:absolute;top:58px;left:28px;right:28px;z-index:10;">
        {kicker("A Aposta")}
        <div class="display" style="font-size:38px;color:#fff;line-height:0.92;">
          FERRARI +<br>{hl("APPLE")} DESIGN.
        </div>
      </div>

      <!-- Luce como card contido, com sombra de contato -->
      <div style="position:absolute;top:178px;left:50%;transform:translateX(-50%);
                  width:300px;height:120px;z-index:1;
                  background:radial-gradient(ellipse at 50% 60%,rgba(90,170,225,0.20),transparent 68%);
                  filter:blur(7px);"></div>
      <div style="position:absolute;top:172px;left:50%;transform:translateX(-50%);
                  width:220px;height:22px;z-index:1;
                  background:radial-gradient(closest-side,rgba(0,0,0,0.55),transparent 78%);
                  filter:blur(9px);bottom:auto;"></div>
      <div class="subject" style="position:absolute;top:160px;left:50%;
                  transform:translateX(-50%);width:304px;z-index:2;">
        <img src="{luce}" style="width:100%;display:block;">
      </div>

      <div style="position:absolute;left:0;right:0;bottom:0;height:42%;z-index:8;
                  background:linear-gradient(180deg,transparent,rgba(8,11,18,0.62) 28%,#080b12 58%);"></div>
      <div style="position:absolute;left:0;right:0;bottom:0;padding:0 28px 40px;z-index:10;">
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:13.5px;
                    color:rgba(255,255,255,0.76);line-height:1.6;max-width:312px;">
          O ex-chefe de design da Apple ao lado da Ferrari.
          A imprensa celebrou. A Luce parecia o futuro.
        </div>
        {bridge("Até as ações abrirem na manhã seguinte.")}
      </div>
    </div>'''


# ── S3 · ESCALADA ────────────────────────────────────────────────────────────
# ÂNCORA REAL: card da Forbes Brasil como prova factual
# Loop: "mas o número não era o problema real"

def slide3():
    forbes = photo_uri("Captura de tela 2026-05-29 205320.png")
    luce   = photo_uri("FERRARI_LUCE_FRONT_3Q_16x9_RGB_WEB_SOCIALS_1920x1080-1000x1000.png")
    card   = news_card(forbes, "O Que Derrubou as Ações da Ferrari após o Lançamento do Carro Elétrico Luce")
    return f'''<div class="slide" style="overflow:hidden;background:#07090f;">
      {dot_grid("rgba(255,255,255,0.04)")}

      <!-- Luce dessaturada e enorme como fundo de atmosfera -->
      <div style="position:absolute;top:90px;left:50%;transform:translateX(-48%) rotate(-10deg);
                  width:480px;z-index:0;opacity:0.18;filter:grayscale(1) blur(1.5px);">
        <img src="{luce}" style="width:100%;display:block;">
      </div>
      <div style="position:absolute;inset:0;z-index:1;
                  background:linear-gradient(180deg,#07090f 16%,transparent 38%,transparent 56%,#07090f 86%);"></div>

      {logo()}
      <div style="position:absolute;top:58px;left:28px;z-index:10;">
        {kicker("A Queda · −8% em 24h")}
        <div class="display" style="font-size:46px;color:#fff;line-height:0.88;">
          A IMPRENSA<br>{hl("REGISTROU")}.
        </div>
      </div>

      <!-- CARD ÂNCORA REAL — Forbes Brasil -->
      <div style="position:absolute;top:210px;left:24px;right:24px;z-index:12;
                  transform:rotate(-1.5deg);">
        {card}
      </div>

      <div style="position:absolute;left:0;right:0;bottom:0;padding:0 28px 40px;z-index:13;">
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:13px;
                    color:rgba(255,255,255,0.62);line-height:1.55;">
          Bilhões evaporaram em horas.
        </div>
        {bridge("Mas o número não era o problema real.")}
      </div>
    </div>'''


# ── S4 · ESCALADA ────────────────────────────────────────────────────────────
# O mercado não reagiu ao carro — reagiu ao sinal. Loop: "uma concorrente percebeu antes."

def slide4():
    ferrari_c = photo_uri("ferrari_classic_trim.png")
    luce      = photo_uri("ferrari_luce_trim.png")
    return f'''<div class="slide" style="overflow:hidden;
        background:linear-gradient(160deg,#150508 0%,{INK["rich"]} 52%,#070910 100%);">
      {dot_grid("rgba(255,255,255,0.04)")}
      {logo()}

      <div style="position:absolute;top:58px;left:28px;right:28px;z-index:10;">
        {kicker("O Sinal")}
        <div class="display" style="font-size:36px;color:#fff;line-height:0.92;">
          NÃO FOI O CARRO.<br>FOI O QUE ELE {hl("DIZIA")}.
        </div>
      </div>

      <!-- Comparação clássica vs Luce — antes × depois -->
      <div style="position:absolute;top:196px;left:-18px;width:246px;z-index:2;
                  filter:drop-shadow(0 10px 22px rgba(0,0,0,0.55));">
        <img src="{ferrari_c}" style="width:100%;display:block;">
      </div>
      <div style="position:absolute;top:192px;left:14px;z-index:4;
                  font-family:{FONTS["body"]},sans-serif;font-size:8.5px;font-weight:700;
                  letter-spacing:0.18em;color:rgba(220,80,80,0.9);text-transform:uppercase;">
        O QUE ERA</div>

      <!-- divisor central -->
      <div style="position:absolute;left:50%;top:190px;bottom:148px;width:1px;z-index:6;
                  background:linear-gradient(180deg,transparent,rgba(30,197,242,0.4) 20%,rgba(30,197,242,0.4) 80%,transparent);"></div>

      <div style="position:absolute;top:206px;right:-10px;width:226px;z-index:2;
                  filter:grayscale(0.55) brightness(0.8) drop-shadow(0 8px 18px rgba(0,0,0,0.5));">
        <img src="{luce}" style="width:100%;display:block;">
      </div>
      <div style="position:absolute;top:204px;right:14px;z-index:4;text-align:right;
                  font-family:{FONTS["body"]},sans-serif;font-size:8.5px;font-weight:700;
                  letter-spacing:0.18em;color:rgba(150,150,180,0.8);text-transform:uppercase;">
        O QUE VIROU</div>

      <div style="position:absolute;left:0;right:0;bottom:0;height:32%;z-index:8;
                  background:linear-gradient(180deg,transparent,rgba(7,9,16,0.7) 34%,#070910 62%);"></div>
      <div style="position:absolute;left:0;right:0;bottom:0;padding:0 28px 40px;z-index:10;">
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:13px;
                    color:rgba(255,255,255,0.66);line-height:1.55;max-width:312px;">
          O mercado não puniu o elétrico. Puniu a sinalização de que a Ferrari
          estava deixando de ser ela mesma.
        </div>
        {bridge("E uma concorrente percebeu isso antes de todo mundo.")}
      </div>
    </div>'''


# ── S5 · VIRADA ──────────────────────────────────────────────────────────────
# Lamborghini faz 1 movimento. Loop: "não foi sorte — foi posicionamento."

def slide5():
    lambo = photo_uri("lamborghini_trim.png")
    return f'''<div class="slide" style="overflow:hidden;background:#09090a;">
      {fundo_profundo(lambo, extra_style="filter:blur(22px) brightness(0.35) saturate(1.2);")}
      {dot_grid("rgba(255,255,255,0.04)")}
      {logo()}

      <div style="position:absolute;top:58px;left:28px;right:28px;z-index:10;">
        {kicker("A Virada")}
        <div class="display" style="font-size:38px;color:#fff;line-height:0.92;">
          A LAMBORGHINI<br>FEZ UM {hl("ÚNICO GESTO")}.
        </div>
      </div>

      <!-- Lambo centralizada e contida -->
      <div style="position:absolute;top:180px;left:50%;transform:translateX(-50%);
                  width:300px;height:128px;z-index:1;
                  background:radial-gradient(ellipse at 50% 55%,rgba(220,180,20,0.20),transparent 68%);
                  filter:blur(7px);"></div>
      <div class="subject" style="position:absolute;top:174px;left:50%;
                  transform:translateX(-50%) rotate(-2deg);width:308px;z-index:2;">
        <img src="{lambo}" style="width:100%;display:block;">
      </div>

      <!-- citação real do CEO como card -->
      <div style="position:absolute;top:306px;left:24px;right:24px;z-index:12;
                  background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.10);
                  border-radius:14px;padding:12px 16px;backdrop-filter:blur(8px);">
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:12.5px;
                    color:rgba(255,255,255,0.85);line-height:1.5;font-style:italic;">
          "Cancelar nosso elétrico foi a decisão certa."
        </div>
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:10px;font-weight:700;
                    letter-spacing:0.15em;color:{ACCENT["primary"]};margin-top:5px;text-transform:uppercase;">
          — CEO Lamborghini
        </div>
      </div>

      <div style="position:absolute;left:0;right:0;bottom:0;padding:0 28px 40px;z-index:13;">
        {bridge("Não foi sorte. Foi ela saber exatamente o que não abriria mão de ser.")}
      </div>
    </div>'''


# ── S6 · REVELAÇÃO ─────────────────────────────────────────────────────────
# Entrega a promessa central. Ferrari clássica como ícone da essência perdida.

def slide6():
    ferrari_c = photo_uri("ferrari_classic_trim.png")
    return f'''<div class="slide" style="overflow:hidden;
        background:radial-gradient(ellipse 120% 90% at 50% 38%,#1a0608 0%,{INK["rich"]} 54%,#06080e 100%);">
      {dot_grid("rgba(255,255,255,0.035)")}

      <!-- glow vermelho atrás do carro -->
      <div style="position:absolute;top:96px;left:50%;transform:translateX(-50%);
                  width:380px;height:190px;z-index:0;
                  background:radial-gradient(ellipse,rgba(200,40,40,0.26),transparent 66%);
                  filter:blur(10px);"></div>
      <!-- sombra de contato -->
      <div style="position:absolute;top:236px;left:50%;transform:translateX(-50%);
                  width:240px;height:30px;z-index:1;
                  background:radial-gradient(closest-side,rgba(0,0,0,0.58),transparent 78%);
                  filter:blur(9px);"></div>
      <div style="position:absolute;top:76px;left:50%;transform:translateX(-52%);width:356px;z-index:2;
                  -webkit-mask-image:radial-gradient(ellipse 94% 90% at 50% 50%,#000 66%,transparent 96%);
                  mask-image:radial-gradient(ellipse 94% 90% at 50% 50%,#000 66%,transparent 96%);">
        <img src="{ferrari_c}" style="width:100%;display:block;
             filter:brightness(0.97) contrast(1.05) drop-shadow(0 14px 28px rgba(0,0,0,0.6));">
      </div>

      {logo()}
      <div style="position:absolute;top:58px;left:28px;z-index:10;">{kicker("A Revelação")}</div>

      <div style="position:absolute;left:0;right:0;bottom:0;height:54%;z-index:8;
                  background:linear-gradient(180deg,transparent,rgba(6,8,14,0.72) 30%,#06080e 58%);"></div>
      <div style="position:absolute;left:0;right:0;bottom:0;padding:0 28px 40px;z-index:10;">
        <div class="display" style="font-size:36px;color:#fff;line-height:0.94;margin-bottom:12px;">
          NÃO FOI O {hl("ELÉTRICO")}.<br>FOI A FERRARI<br>TENTANDO SER<br>OUTRA MARCA.
        </div>
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:13px;
                    color:rgba(255,255,255,0.66);line-height:1.6;max-width:308px;">
          O mercado não pune inovação. Pune a perda de identidade.
        </div>
      </div>
    </div>'''


# ── S7 · INSIGHT ─────────────────────────────────────────────────────────────
# Tipográfico puro. Memorável. Universal.

def slide7():
    return f'''<div class="slide" style="overflow:hidden;
        background:radial-gradient(ellipse 100% 80% at 28% 36%,#0e1a2c 0%,{INK["void"]} 60%,#040509 100%);">
      {dot_grid("rgba(255,255,255,0.03)")}
      <div style="position:absolute;top:36%;left:28%;transform:translate(-50%,-50%);
                  width:310px;height:310px;z-index:1;pointer-events:none;
                  background:radial-gradient(circle,rgba(30,197,242,0.14),transparent 66%);
                  filter:blur(6px);"></div>
      {logo()}
      <div class="display" style="position:absolute;top:68px;left:24px;z-index:9;
                  font-size:150px;line-height:0.7;color:{ACCENT["primary"]};opacity:0.18;">"</div>

      <div style="position:absolute;top:152px;left:30px;z-index:10;">{kicker("O Insight")}</div>

      <div style="position:absolute;top:184px;left:30px;right:30px;z-index:10;">
        <div class="display" style="font-size:40px;color:#fff;line-height:0.98;margin-bottom:16px;">
          A MARCA MAIS FORTE<br>NÃO É A QUE<br>MAIS {hl("INOVA")}.
        </div>
        <div class="display" style="font-size:40px;color:rgba(255,255,255,0.5);line-height:1.04;">
          É A QUE MAIS SABE<br>O QUE NÃO VAI<br>
          <span style="color:#fff;">MUDAR.</span>
        </div>
      </div>
      {overlay_vignette(0.40, z=3)}
    </div>'''


# ── S8 · CTA ─────────────────────────────────────────────────────────────────

def slide8():
    return f'''<div class="slide" style="overflow:hidden;
        background:linear-gradient(155deg,{INK["rich"]} 0%,#0a1628 55%,{INK["void"]} 100%);">
      <div style="position:absolute;top:-50px;left:50%;transform:translateX(-50%);
                  width:260px;height:200px;z-index:1;pointer-events:none;
                  background:radial-gradient(ellipse,rgba(30,197,242,0.16),transparent 70%);"></div>
      {logo(size=26)}
      <div style="position:absolute;inset:0;display:flex;flex-direction:column;
                  align-items:center;justify-content:center;padding:0 30px;z-index:10;text-align:center;">
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:11px;font-weight:700;
                    letter-spacing:0.22em;text-transform:uppercase;
                    color:{ACCENT["primary"]};margin-bottom:14px;">@nucvision</div>
        <div class="display" style="font-size:34px;color:#fff;line-height:1;margin-bottom:8px;">
          LEITURAS ASSIM
        </div>
        <div class="display" style="font-size:34px;color:{ACCENT["primary"]};margin-bottom:24px;">
          TODA SEMANA.
        </div>
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:13px;
                    color:rgba(255,255,255,0.5);margin-bottom:28px;line-height:1.55;">
          Siga a NUC Vision para acompanhar leituras<br>
          estratégicas sobre marcas, mercado e posicionamento.
        </div>
        <div class="cta" style="color:#06121c;font-family:{FONTS["body"]},sans-serif;
                    font-size:13px;font-weight:700;letter-spacing:0.1em;
                    text-transform:uppercase;padding:13px 34px;">
          SEGUIR AGORA
        </div>
      </div>
      {overlay_vignette(0.28, z=3)}
    </div>'''


# ── Assembly ──────────────────────────────────────────────────────────────────

def main():
    raw = [slide1(), slide2(), slide3(), slide4(), slide5(), slide6(), slide7(), slide8()]
    parts = []
    for s in raw:
        idx = s.rfind("</div>")
        parts.append(s[:idx] + GRAO_OVERLAY + s[idx:])
    slides = f"<style>{REALISM_CSS}</style>" + "".join(parts)
    html = html_shell(slides, TOTAL, CAPTION)
    out = Path("/home/user/Meu-espa-o/previews/nucvision-ferrari-lambo-v2.html")
    out.write_text(html, encoding="utf-8")
    print(f"✓ {out}")

if __name__ == "__main__":
    main()
