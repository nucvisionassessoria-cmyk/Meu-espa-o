#!/usr/bin/env python3
"""
NUC Vision — Carrossel Copa Hexa (MODO HYPE)
Adaptacao oportunista do post V4 "Brasil rumo ao Hexa" (29/06).
Roteiro em skills/oportunista-trend/exemplos/copa-hexa-roteiro.md
Modelo: POLEMICA. Palette override: verde+amarelo+azul Brasil + ciano NUC so no CTA.
Formato: 420x525 -> exportado para 1080x1350.
"""
import sys, base64
from pathlib import Path
sys.path.insert(0, "/home/user/Meu-espa-o")
sys.path.insert(0, "/home/user/Meu-espa-o/geradores")
from design_system import FONTS, FONT_LINK, LOGO_URI, html_shell, overlay_vignette, overlay_noise
from nuc_realism import REALISM_CSS, GRAO_OVERLAY

FOTOS = Path("/home/user/Meu-espa-o/fotos")
TOTAL = 8

# Copa palette override
VERDE  = "#009C3B"
AMARELO = "#FFDF00"
AZUL   = "#002776"
BRANCO = "#FFFFFF"
CIANO  = "#1EC5F2"   # so logo + assinatura
PRETO  = "#0A0F1A"

CAPTION = (
    "A Nike gastou R$ 200 milhoes pra errar a camisa do Hexa. E voce esta gastando "
    "o silencio da sua marca pra errar o maior momento de marketing do ano. Em ambos "
    "os casos, o erro e o mesmo: confundir evento com narrativa. Desliza ate o fim - "
    "no ultimo slide tem o framework. 🇧🇷 Comenta HEXA que mando direto na DM. "
    "@nucvision #copadomundo #hexa #marketing #posicionamento #pme"
)

def photo_uri(name):
    p = FOTOS / name
    ext = p.suffix.lower().lstrip(".")
    mime = {"jpg":"jpeg","jpeg":"jpeg","png":"png","webp":"webp"}.get(ext,"jpeg")
    return f"data:image/{mime};base64,{base64.b64encode(p.read_bytes()).decode()}"

def logo(white=True, size=28, top=18, color=None):
    if color:
        flt = f"filter:brightness(0) saturate(100%) invert({1 if white else 0}) drop-shadow(0 2px 8px rgba(0,0,0,0.45));"
    else:
        flt = "filter:brightness(0) invert(1) drop-shadow(0 2px 10px rgba(0,0,0,0.55));" if white else ""
    return (f'<div style="position:absolute;top:{top}px;left:0;right:0;'
            f'display:flex;justify-content:center;z-index:30;">'
            f'<img src="{LOGO_URI}" style="height:{size}px;width:auto;{flt}"></div>')

def kicker(text, color=None):
    c = color or AMARELO
    return (f'<div style="font-family:{FONTS["body"]},sans-serif;font-size:10px;'
            f'font-weight:700;letter-spacing:0.22em;text-transform:uppercase;'
            f'color:{c};margin-bottom:12px;">{text}</div>')

def hl_yellow(word):
    """Highlight estilo marca-texto amarelo (codigo da Copa)."""
    return (f'<span style="background:{AMARELO};color:{AZUL};'
            f'padding:1px 10px 5px;border-radius:6px;font-weight:inherit;'
            f'box-shadow:0 4px 16px rgba(255,223,0,0.35);">{word}</span>')

def bridge(text, color=None):
    c = color or AMARELO
    return (f'<div style="display:flex;align-items:flex-start;gap:10px;margin-top:22px;">'
            f'<div style="width:24px;height:2px;background:{c};flex-shrink:0;margin-top:9px;"></div>'
            f'<span style="font-family:{FONTS["body"]},sans-serif;font-size:13px;'
            f'font-style:italic;color:{c};line-height:1.45;font-weight:500;">{text}</span></div>')

def flag_stripe(top=False, bottom=False, height=8):
    """Faixa verde-amarelo-azul (codigo Brasil) — sutil."""
    pos = "top:0" if top else "bottom:0"
    return (f'<div style="position:absolute;{pos};left:0;right:0;height:{height}px;z-index:25;'
            f'background:linear-gradient(90deg,{VERDE} 0%,{VERDE} 33%,'
            f'{AMARELO} 33%,{AMARELO} 66%,{AZUL} 66%,{AZUL} 100%);'
            f'box-shadow:0 0 24px rgba(0,156,59,0.25);"></div>')

def tatica_bg():
    """Fundo verde com linhas de tabela tatica de futebol — codigo do CTA V4."""
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 525" '
           'preserveAspectRatio="xMidYMid slice">'
           # Lateral lines and circle (vague pitch)
           '<g stroke="rgba(255,255,255,0.16)" stroke-width="1.5" fill="none">'
           '<circle cx="210" cy="262" r="62"/>'
           '<line x1="210" y1="0" x2="210" y2="525"/>'
           '<rect x="0" y="0" width="420" height="525"/>'
           '<rect x="60" y="0" width="300" height="120"/>'
           '<rect x="120" y="0" width="180" height="60"/>'
           '<rect x="60" y="405" width="300" height="120"/>'
           '<rect x="120" y="465" width="180" height="60"/>'
           # Tactical arrows
           '<path d="M 80 360 Q 150 300 200 320" stroke-dasharray="6 5"/>'
           '<path d="M 340 360 Q 270 300 230 320" stroke-dasharray="6 5"/>'
           '<path d="M 105 165 L 175 220" stroke-dasharray="6 5"/>'
           '</g>'
           # X and O marks (tactical chalk)
           '<g font-family="Anton" font-size="22" fill="rgba(255,223,0,0.55)" text-anchor="middle">'
           '<text x="100" y="170">X</text>'
           '<text x="320" y="170">X</text>'
           '<text x="100" y="370">O</text>'
           '<text x="320" y="370">O</text>'
           '</g></svg>')
    b64 = base64.b64encode(svg.encode()).decode()
    return (f'<div style="position:absolute;inset:0;z-index:1;'
            f'background-image:url(\'data:image/svg+xml;base64,{b64}\');'
            f'background-size:cover;opacity:0.9;"></div>')


# =============================================================================
# SLIDE 1 — GANCHO: "A Nike acabou de gastar R$ 200 mi pra errar a camisa do Hexa"
# =============================================================================
def slide1():
    return f'''<div class="slide" style="overflow:hidden;
        background:radial-gradient(ellipse 130% 90% at 50% 100%,#013D1A 0%,{AZUL} 60%,#000A1F 100%);">
      {flag_stripe(top=True, height=6)}
      {logo()}
      <div style="position:absolute;top:62px;left:0;right:0;text-align:center;z-index:10;">
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:10px;font-weight:700;
                    letter-spacing:0.28em;text-transform:uppercase;color:{AMARELO};">
          LEITURA DE MERCADO · COPA 2026
        </div>
      </div>
      <!-- Big silhueta troféu/escudo no fundo, sutil -->
      <div style="position:absolute;top:140px;left:50%;transform:translateX(-50%);
                  font-family:{FONTS["display"]},sans-serif;font-size:340px;
                  color:rgba(255,223,0,0.06);line-height:1;z-index:2;">★</div>
      <div style="position:absolute;top:115px;left:24px;right:24px;z-index:12;">
        <div class="display" style="font-family:{FONTS["display"]},sans-serif;
                    font-size:54px;color:{BRANCO};line-height:0.92;letter-spacing:-0.01em;">
          A NIKE<br>ACABOU DE<br>{hl_yellow("ERRAR")}<br>A CAMISA<br>DO HEXA.
        </div>
      </div>
      <div style="position:absolute;bottom:34px;left:24px;right:24px;z-index:12;">
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:13px;font-weight:500;
                    color:rgba(255,255,255,0.72);line-height:1.45;">
          R$ 200 milhões em ativação — pra fazer o pior marketing<br>
          de Copa do ano.
        </div>
        <div style="margin-top:18px;display:inline-flex;align-items:center;gap:8px;
                    font-family:{FONTS["body"]},sans-serif;font-size:11px;font-weight:700;
                    color:{AMARELO};letter-spacing:0.18em;text-transform:uppercase;">
          DESLIZE <span style="font-size:16px;">›››</span>
        </div>
      </div>
      {overlay_vignette(0.35,z=3)}
    </div>'''


# =============================================================================
# SLIDE 2 — CURIOSIDADE: "A camisa em si agradou. A historia que contaram, nao."
# =============================================================================
def slide2():
    return f'''<div class="slide" style="overflow:hidden;
        background:linear-gradient(165deg,{AZUL} 0%,#0A1A40 55%,#040818 100%);">
      {logo()}
      <div style="position:absolute;top:74px;left:28px;right:28px;z-index:10;">
        {kicker("01 · O FATO")}
        <div class="display" style="font-family:{FONTS["display"]},sans-serif;
                    font-size:42px;color:{BRANCO};line-height:0.95;letter-spacing:-0.01em;">
          A CAMISA EM SI<br>{hl_yellow("AGRADOU")}.
        </div>
        <div class="display" style="font-family:{FONTS["display"]},sans-serif;
                    font-size:42px;color:rgba(255,255,255,0.42);line-height:0.95;
                    margin-top:8px;letter-spacing:-0.01em;">
          A HISTÓRIA QUE<br>A NIKE CONTOU<br>EM CIMA DELA,
        </div>
        <div class="display" style="font-family:{FONTS["display"]},sans-serif;
                    font-size:54px;color:{AMARELO};line-height:0.95;margin-top:6px;
                    letter-spacing:-0.01em;">
          NÃO.
        </div>
      </div>
      <div style="position:absolute;bottom:46px;left:28px;right:28px;z-index:12;">
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:13px;font-weight:500;
                    color:rgba(255,255,255,0.62);line-height:1.5;">
          Gola retrô, amarelo clássico, geometrias da bandeira — todos<br>
          os códigos certos no produto.
        </div>
        {bridge("E mesmo assim, o torcedor não comprou a narrativa.")}
      </div>
      {overlay_vignette(0.3,z=3)}
    </div>'''


# =============================================================================
# SLIDE 3 — ESCALADA: "Marca nao se constroi no produto. Se constroi na narrativa."
# =============================================================================
def slide3():
    return f'''<div class="slide" style="overflow:hidden;
        background:linear-gradient(180deg,{BRANCO} 0%,#F5F7FA 100%);">
      {logo(white=False, color=AZUL)}
      <div style="position:absolute;top:74px;left:28px;right:28px;z-index:10;">
        {kicker("02 · A REGRA", color=VERDE)}
        <div class="display" style="font-family:{FONTS["display"]},sans-serif;
                    font-size:48px;color:{AZUL};line-height:0.95;letter-spacing:-0.01em;">
          MARCA NÃO SE<br>CONSTRÓI NO<br>{hl_yellow("PRODUTO")}.
        </div>
        <div style="margin-top:14px;font-family:{FONTS["display"]},sans-serif;
                    font-size:32px;color:rgba(0,39,118,0.55);line-height:1;letter-spacing:-0.005em;">
          SE CONSTRÓI<br>NA NARRATIVA<br>EM VOLTA DELE.
        </div>
      </div>
      <div style="position:absolute;bottom:32px;left:28px;right:28px;z-index:12;">
        <div style="height:1px;background:rgba(0,39,118,0.18);margin-bottom:18px;"></div>
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:13px;font-weight:500;
                    color:rgba(0,39,118,0.78);line-height:1.5;">
          O produto pode ser excelente. Se a história que a marca<br>
          conta em volta dele não casar com o que o público sente,<br>
          ele <strong>falha como produto cultural</strong>.
        </div>
        {bridge("E é aqui que a maioria das empresas erra.", color=VERDE)}
      </div>
      {flag_stripe(bottom=True, height=4)}
    </div>'''


# =============================================================================
# SLIDE 4 — VIRADA: "A narrativa do Hexa ja estava pronta ha 24 anos."
# =============================================================================
def slide4():
    return f'''<div class="slide" style="overflow:hidden;
        background:radial-gradient(ellipse at 50% 30%,#015A26 0%,{VERDE} 35%,#003015 100%);">
      {logo()}
      <div style="position:absolute;top:72px;left:0;right:0;text-align:center;z-index:10;">
        {kicker("03 · A VIRADA")}
      </div>
      <!-- numero gigante 24 atras do titulo -->
      <div style="position:absolute;top:80px;left:0;right:0;text-align:center;z-index:2;
                  font-family:{FONTS["display"]},sans-serif;font-size:280px;
                  color:rgba(255,223,0,0.10);line-height:1;letter-spacing:-0.04em;">
        24
      </div>
      <div style="position:absolute;top:140px;left:24px;right:24px;z-index:12;text-align:center;">
        <div class="display" style="font-family:{FONTS["display"]},sans-serif;
                    font-size:42px;color:{BRANCO};line-height:0.95;letter-spacing:-0.01em;">
          A NARRATIVA<br>DO HEXA JÁ<br>{hl_yellow("ESTAVA PRONTA")}
        </div>
        <div style="margin-top:12px;font-family:{FONTS["display"]},sans-serif;
                    font-size:26px;color:rgba(255,255,255,0.85);line-height:1;">
          HÁ 24 ANOS.
        </div>
      </div>
      <div style="position:absolute;bottom:38px;left:28px;right:28px;z-index:12;text-align:center;">
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:12px;font-weight:500;
                    color:rgba(255,255,255,0.72);line-height:1.5;">
          Maior campeã. 24 anos sem o título.<br>
          Melhor técnico da história no comando.
        </div>
        {bridge("A Nike ignorou tudo isso e foi inventar outra história.")}
      </div>
      {overlay_vignette(0.4,z=3)}
    </div>'''


# =============================================================================
# SLIDE 5 — ESCALADA: "Sua empresa esta fazendo o mesmo agora."
# =============================================================================
def slide5():
    return f'''<div class="slide" style="overflow:hidden;
        background:linear-gradient(165deg,#0F1320 0%,{AZUL} 55%,#0A1A40 100%);">
      {logo()}
      <div style="position:absolute;top:74px;left:28px;right:28px;z-index:10;">
        {kicker("04 · A ATERRISSAGEM")}
        <div class="display" style="font-family:{FONTS["display"]},sans-serif;
                    font-size:46px;color:{BRANCO};line-height:0.94;letter-spacing:-0.01em;">
          E A SUA EMPRESA<br>ESTÁ FAZENDO<br>{hl_yellow("O MESMO")}<br>AGORA.
        </div>
      </div>
      <div style="position:absolute;bottom:40px;left:28px;right:28px;z-index:12;">
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:20px;">
          <div style="background:rgba(255,223,0,0.10);border:1px solid rgba(255,223,0,0.32);
                      border-radius:10px;padding:12px;">
            <div style="font-family:{FONTS["display"]},sans-serif;font-size:26px;
                        color:{AMARELO};line-height:1;">R$ 200 MI</div>
            <div style="font-family:{FONTS["body"]},sans-serif;font-size:10px;
                        color:rgba(255,255,255,0.72);margin-top:6px;line-height:1.35;">
              o que a Nike gastou pra errar
            </div>
          </div>
          <div style="background:rgba(255,223,0,0.10);border:1px solid rgba(255,223,0,0.32);
                      border-radius:10px;padding:12px;">
            <div style="font-family:{FONTS["display"]},sans-serif;font-size:26px;
                        color:{AMARELO};line-height:1;">R$ 0</div>
            <div style="font-family:{FONTS["body"]},sans-serif;font-size:10px;
                        color:rgba(255,255,255,0.72);margin-top:6px;line-height:1.35;">
              o que você está gastando — e perdendo
            </div>
          </div>
        </div>
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:12.5px;font-weight:500;
                    color:rgba(255,255,255,0.68);line-height:1.5;">
          Mesma cegueira de narrativa, escala diferente. No maior<br>
          momento de marca do ano.
        </div>
      </div>
      {overlay_vignette(0.3,z=3)}
    </div>'''


# =============================================================================
# SLIDE 6 — REVELACAO: "Quem entende o hexa como narrativa pega o rebote sem patrocinar."
# =============================================================================
def slide6():
    return f'''<div class="slide" style="overflow:hidden;
        background:radial-gradient(ellipse at 50% 50%,#FFE948 0%,{AMARELO} 50%,#D4B300 100%);">
      {logo(white=False, color=AZUL)}
      <div style="position:absolute;top:70px;left:0;right:0;text-align:center;z-index:10;">
        {kicker("05 · A REVELAÇÃO", color=AZUL)}
      </div>
      <div style="position:absolute;top:120px;left:22px;right:22px;z-index:12;">
        <div class="display" style="font-family:{FONTS["display"]},sans-serif;
                    font-size:36px;color:{AZUL};line-height:0.96;letter-spacing:-0.01em;">
          QUEM ENTENDE<br>O HEXA COMO<br><span style="background:{AZUL};color:{AMARELO};
                    padding:1px 12px 6px;border-radius:6px;">NARRATIVA</span>
        </div>
        <div class="display" style="font-family:{FONTS["display"]},sans-serif;
                    font-size:26px;color:rgba(0,39,118,0.7);line-height:1;
                    margin-top:14px;letter-spacing:-0.01em;">
          E NÃO COMO EVENTO,
        </div>
        <div class="display" style="font-family:{FONTS["display"]},sans-serif;
                    font-size:32px;color:{AZUL};line-height:0.96;
                    margin-top:14px;letter-spacing:-0.01em;">
          PEGA O REBOTE<br>SEM PATROCINAR<br>A SELEÇÃO.
        </div>
      </div>
      <div style="position:absolute;bottom:42px;left:28px;right:28px;z-index:12;text-align:center;">
        <div style="height:1px;background:rgba(0,39,118,0.28);margin-bottom:14px;"></div>
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:12.5px;font-weight:600;
                    color:{AZUL};line-height:1.4;font-style:italic;">
          O jogo é mais simples do que a Nike fez parecer.
        </div>
      </div>
    </div>'''


# =============================================================================
# SLIDE 7 — INSIGHT: "Voce nao precisa do amarelinho na camisa. Precisa na historia."
# =============================================================================
def slide7():
    return f'''<div class="slide" style="overflow:hidden;
        background:linear-gradient(180deg,#000A1F 0%,{AZUL} 100%);">
      {logo()}
      <div style="position:absolute;top:72px;left:0;right:0;text-align:center;z-index:10;">
        {kicker("06 · O INSIGHT")}
      </div>
      <!-- Quote marks gigantes atras -->
      <div style="position:absolute;top:8px;left:14px;
                  font-family:{FONTS["display"]},sans-serif;font-size:200px;
                  color:rgba(255,223,0,0.10);line-height:1;z-index:2;">"</div>
      <div style="position:absolute;top:124px;left:24px;right:24px;z-index:12;">
        <div class="display" style="font-family:{FONTS["display"]},sans-serif;
                    font-size:34px;color:{BRANCO};line-height:0.98;letter-spacing:-0.01em;">
          VOCÊ NÃO PRECISA<br>DO {hl_yellow("AMARELINHO")}<br>NA CAMISA.
        </div>
        <div style="height:1px;background:rgba(255,223,0,0.40);margin:22px 0;"></div>
        <div class="display" style="font-family:{FONTS["display"]},sans-serif;
                    font-size:34px;color:{AMARELO};line-height:0.98;
                    letter-spacing:-0.01em;">
          PRECISA DELE<br>NA HISTÓRIA QUE<br>VOCÊ CONTA.
        </div>
      </div>
      <div style="position:absolute;bottom:42px;left:28px;right:28px;z-index:12;text-align:center;">
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:11px;font-weight:600;
                    color:rgba(255,255,255,0.55);line-height:1.5;
                    letter-spacing:0.18em;text-transform:uppercase;">
          NUC Vision · Marketing, Vendas & Performance
        </div>
      </div>
      {flag_stripe(bottom=True, height=6)}
    </div>'''


# =============================================================================
# SLIDE 8 — CTA: trio_reuniao + comissao tecnica + Comente HEXA
# =============================================================================
def slide8():
    trio = photo_uri("trio_reuniao.png")
    return f'''<div class="slide" style="overflow:hidden;
        background:linear-gradient(165deg,#015A26 0%,{VERDE} 45%,#003015 100%);">
      {tatica_bg()}
      {logo()}
      <div style="position:absolute;top:60px;left:0;right:0;text-align:center;z-index:10;">
        {kicker("DA COMISSÃO TÉCNICA · NUC VISION")}
      </div>
      <!-- Trio com tratamento sepia/amarelo overlay para clima de campo -->
      <div style="position:absolute;top:88px;left:50%;transform:translateX(-50%);
                  width:230px;height:160px;z-index:11;overflow:hidden;border-radius:12px;
                  box-shadow:0 18px 44px rgba(0,0,0,0.55),inset 0 0 0 2px {AMARELO};">
        <div style="position:absolute;inset:0;background:
            linear-gradient(180deg,rgba(0,156,59,0.10) 0%,rgba(0,39,118,0.35) 100%),
            url('{trio}') center/cover no-repeat;
            filter:contrast(1.05) saturate(1.1);"></div>
      </div>
      <!-- Confete amarelo -->
      <div style="position:absolute;top:60px;left:30px;width:14px;height:6px;
                  background:{AMARELO};transform:rotate(-15deg);z-index:5;"></div>
      <div style="position:absolute;top:140px;right:24px;width:12px;height:5px;
                  background:{AMARELO};transform:rotate(25deg);z-index:5;"></div>
      <div style="position:absolute;top:88px;right:48px;width:10px;height:4px;
                  background:{BRANCO};transform:rotate(-30deg);z-index:5;"></div>
      <div style="position:absolute;top:230px;left:18px;width:8px;height:4px;
                  background:{AMARELO};transform:rotate(45deg);z-index:5;"></div>
      <div style="position:absolute;top:280px;right:14px;width:12px;height:4px;
                  background:{BRANCO};transform:rotate(-10deg);z-index:5;"></div>
      <!-- Headline + CTA -->
      <div style="position:absolute;top:268px;left:22px;right:22px;z-index:12;text-align:center;">
        <div class="display" style="font-family:{FONTS["display"]},sans-serif;
                    font-size:34px;color:{BRANCO};line-height:0.95;letter-spacing:-0.01em;
                    text-shadow:0 4px 14px rgba(0,0,0,0.5);">
          FRAMEWORK DE MARCA<br>PRA COPA · {hl_yellow("GRÁTIS")}
        </div>
        <div style="margin-top:10px;font-family:{FONTS["body"]},sans-serif;font-size:12.5px;
                    font-weight:500;color:rgba(255,255,255,0.86);line-height:1.45;
                    text-shadow:0 2px 6px rgba(0,0,0,0.4);">
          Como pegar o rebote do Hexa sem patrocinar a seleção.
        </div>
      </div>
      <!-- CTA full-width estilo V4 -->
      <div style="position:absolute;bottom:22px;left:18px;right:18px;z-index:15;
                  background:{AMARELO};border-radius:10px;padding:18px 16px;
                  display:flex;align-items:center;justify-content:center;gap:10px;
                  box-shadow:0 14px 34px rgba(0,0,0,0.55),inset 0 -3px 0 rgba(0,0,0,0.18);">
        <span style="font-family:{FONTS["display"]},sans-serif;font-size:24px;
                     color:{AZUL};letter-spacing:0.02em;">COMENTE</span>
        <span style="background:{AZUL};color:{AMARELO};padding:5px 12px 7px;
                     border-radius:6px;font-family:{FONTS["display"]},sans-serif;
                     font-size:24px;letter-spacing:0.04em;">HEXA</span>
        <span style="font-family:{FONTS["body"]},sans-serif;font-size:18px;
                     color:{AZUL};">⬇</span>
      </div>
      {overlay_vignette(0.35,z=3)}
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
