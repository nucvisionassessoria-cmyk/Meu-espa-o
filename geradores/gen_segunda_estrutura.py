#!/usr/bin/env python3
"""
Carrossel Segunda-feira — "Você não precisa de mais vendas. Precisa de estrutura."
7 slides: S1-S3 escuro, S4 claro (virada), S5-S6 escuro, S7 CTA escuro
"""
import sys, base64, asyncio
from pathlib import Path
sys.path.insert(0, "/home/user/Meu-espa-o")
from design_system import LOGO_URI
from playwright.async_api import async_playwright

FOTOS  = Path("/home/user/Meu-espa-o/fotos/geradas")
OUTPUT = Path("/home/user/Meu-espa-o/output/segunda-estrutura")
OUTPUT.mkdir(parents=True, exist_ok=True)

VW, VH = 420, 525
SCALE  = 1080 / VW
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

CYAN       = "#1EC5F2"
INK        = "#06090F"
INK2       = "#0b0f1e"
LIGHT_BG   = "#EEF3F8"
LIGHT_TEXT = "#1A2E4D"
LIGHT_SUB  = "rgba(26,46,77,0.60)"

FONT_LINK = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@1,600;1,700&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
"""

def photo_b64(name):
    p = FOTOS / name
    return f"data:image/png;base64,{base64.b64encode(p.read_bytes()).decode()}"

def logo_html(dark=True):
    filt = "brightness(0) invert(1) drop-shadow(0 2px 10px rgba(0,0,0,0.7))" if dark else "drop-shadow(0 1px 4px rgba(26,46,77,0.18))"
    return f'''<div style="position:absolute;top:20px;left:0;right:0;display:flex;
        justify-content:center;z-index:30;">
        <img src="{LOGO_URI}" style="height:56px;width:auto;filter:{filt};">
    </div>'''

def kicker(txt, dark=True):
    return f'''<div style="display:flex;align-items:center;gap:8px;margin-bottom:10px;">
        <div style="width:20px;height:1.5px;background:{CYAN};opacity:0.8;"></div>
        <span style="font-family:'Space Grotesk',sans-serif;font-size:9.5px;font-weight:700;
                     letter-spacing:0.22em;text-transform:uppercase;color:{CYAN};">{txt}</span>
    </div>'''

def insight_box(bold_line, sub_line="", accent=False, dark=True):
    if dark:
        bg  = "rgba(30,197,242,0.10)" if accent else "rgba(255,255,255,0.06)"
        bdr = "rgba(30,197,242,0.28)" if accent else "rgba(255,255,255,0.10)"
        bold_c = "#fff"
        sub_c  = "rgba(255,255,255,0.50)"
    else:
        bg  = "rgba(30,197,242,0.08)"
        bdr = "rgba(30,197,242,0.22)"
        bold_c = LIGHT_TEXT
        sub_c  = LIGHT_SUB
    sub = (f'<div style="font-family:\'Space Grotesk\',sans-serif;font-size:11.5px;'
           f'color:{sub_c};line-height:1.55;margin-top:5px;">{sub_line}</div>'
           if sub_line else "")
    return f'''<div style="background:{bg};border:1px solid {bdr};border-radius:14px;
        padding:14px 18px;backdrop-filter:blur(8px);">
        <div style="font-family:'Space Grotesk',sans-serif;font-size:12.5px;font-weight:600;
                    color:{bold_c};line-height:1.45;">{bold_line}</div>
        {sub}
    </div>'''

GRAIN = '''<div style="position:absolute;inset:0;z-index:50;pointer-events:none;opacity:0.06;
    mix-blend-mode:overlay;
    background-image:url('data:image/svg+xml;utf8,<svg xmlns=%22http://www.w3.org/2000/svg%22 width=%22120%22 height=%22120%22><filter id=%22n%22><feTurbulence type=%22fractalNoise%22 baseFrequency=%220.9%22 numOctaves=%222%22/></filter><rect width=%22100%25%22 height=%22100%25%22 filter=%22url(%23n)%22/></svg>');
    background-size:180px 180px;"></div>'''

GRAIN_LIGHT = '''<div style="position:absolute;inset:0;z-index:50;pointer-events:none;opacity:0.035;
    mix-blend-mode:multiply;
    background-image:url('data:image/svg+xml;utf8,<svg xmlns=%22http://www.w3.org/2000/svg%22 width=%22120%22 height=%22120%22><filter id=%22n%22><feTurbulence type=%22fractalNoise%22 baseFrequency=%220.9%22 numOctaves=%222%22/></filter><rect width=%22100%25%22 height=%22100%25%22 filter=%22url(%23n)%22/></svg>');
    background-size:180px 180px;"></div>'''


# ── S1 GANCHO ─────────────────────────────────────────────────────────────────
def slide1():
    img = photo_b64("s1_dono_noite.png")
    return f'''
<div style="width:{VW}px;height:{VH}px;position:relative;overflow:hidden;background:{INK};">
  <div style="position:absolute;inset:0;z-index:0;">
    <img src="{img}" style="width:100%;height:100%;object-fit:cover;
         filter:brightness(0.45) contrast(1.08) saturate(0.75);">
  </div>
  <div style="position:absolute;inset:0;z-index:1;
    background:linear-gradient(180deg,
      rgba(6,9,15,0.82) 0%,
      rgba(6,9,15,0.25) 38%,
      transparent 55%,
      rgba(6,9,15,0.70) 72%,
      {INK} 92%);"></div>
  {GRAIN}
  {logo_html(dark=True)}
  <div style="position:absolute;top:72px;left:32px;right:32px;z-index:20;">
    {kicker("A Crença")}
    <div style="font-family:'Space Grotesk',sans-serif;font-size:17px;font-weight:600;
                color:rgba(255,255,255,0.75);letter-spacing:0.02em;
                text-transform:uppercase;margin-top:10px;line-height:1.35;">
      Todo dono quer uma coisa.
    </div>
    <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:700;
                font-size:64px;line-height:0.86;color:#fff;margin-top:10px;">
      Mais<br>
      <span style="color:{CYAN};">clientes.</span>
    </div>
  </div>
  <div style="position:absolute;bottom:32px;left:32px;right:32px;z-index:20;">
    {insight_box("Mas e se o problema não for a falta deles?", dark=True)}
  </div>
</div>'''


# ── S2 CURIOSIDADE ────────────────────────────────────────────────────────────
def slide2():
    img = photo_b64("s4_engrenagem.png")
    return f'''
<div style="width:{VW}px;height:{VH}px;position:relative;overflow:hidden;background:{INK};">
  <div style="position:absolute;inset:0;z-index:0;">
    <img src="{img}" style="width:100%;height:100%;object-fit:cover;
         filter:brightness(0.42) contrast(1.10) saturate(0.68);">
  </div>
  <div style="position:absolute;inset:0;z-index:1;
    background:linear-gradient(180deg,
      rgba(6,9,15,0.85) 0%,
      rgba(6,9,15,0.28) 40%,
      transparent 56%,
      rgba(6,9,15,0.72) 74%,
      {INK} 94%);"></div>
  {GRAIN}
  {logo_html(dark=True)}
  <div style="position:absolute;top:72px;left:32px;right:32px;z-index:20;">
    {kicker("O Que Acontece")}
    <div style="font-family:'Space Grotesk',sans-serif;font-size:17px;font-weight:600;
                color:rgba(255,255,255,0.75);letter-spacing:0.02em;
                text-transform:uppercase;margin-top:10px;line-height:1.35;">
      Quando a demanda chega sem estrutura.
    </div>
    <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:700;
                font-size:58px;line-height:0.88;color:#fff;margin-top:10px;">
      O cliente aparece.<br>
      <span style="color:{CYAN};">A operação trava.</span>
    </div>
  </div>
  <div style="position:absolute;bottom:32px;left:32px;right:32px;z-index:20;">
    {insight_box(
      "Prazo furado. Atendimento irregular. Produto inconsistente.",
      "E o dono apagando incêndio em tudo.",
      dark=True
    )}
  </div>
</div>'''


# ── S3 ESCALADA ───────────────────────────────────────────────────────────────
def slide3():
    img = photo_b64("s3_doente.png")
    return f'''
<div style="width:{VW}px;height:{VH}px;position:relative;overflow:hidden;background:{INK};">
  <div style="position:absolute;inset:0;z-index:0;">
    <img src="{img}" style="width:100%;height:100%;object-fit:cover;
         filter:brightness(0.40) contrast(1.08) saturate(0.65);">
  </div>
  <div style="position:absolute;inset:0;z-index:1;
    background:linear-gradient(180deg,
      rgba(6,9,15,0.88) 0%,
      rgba(6,9,15,0.28) 42%,
      transparent 58%,
      rgba(6,9,15,0.75) 76%,
      {INK} 95%);"></div>
  {GRAIN}
  {logo_html(dark=True)}
  <div style="position:absolute;top:72px;left:32px;right:32px;z-index:20;">
    {kicker("O Diagnóstico")}
    <div style="font-family:'Space Grotesk',sans-serif;font-size:17px;font-weight:600;
                color:rgba(255,255,255,0.75);letter-spacing:0.02em;
                text-transform:uppercase;margin-top:10px;line-height:1.35;">
      Com o tempo, uma coisa fica clara.
    </div>
    <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:700;
                font-size:58px;line-height:0.88;color:#fff;margin-top:10px;">
      Você virou a<br>
      <span style="color:{CYAN};">engrenagem</span><br>
      principal.
    </div>
  </div>
  <div style="position:absolute;bottom:32px;left:32px;right:32px;z-index:20;">
    {insight_box(
      "Se você para, a empresa para.",
      "Isso não é dedicação. É falta de processo.",
      accent=True, dark=True
    )}
  </div>
</div>'''


# ── S4 VIRADA — SLIDE CLARO ───────────────────────────────────────────────────
def slide4():
    return f'''
<div style="width:{VW}px;height:{VH}px;position:relative;overflow:hidden;background:{LIGHT_BG};">
  <div style="position:absolute;inset:0;z-index:1;pointer-events:none;
    background-image:radial-gradient(circle,rgba(26,46,77,0.055) 1px,transparent 1px);
    background-size:28px 28px;"></div>
  <div style="position:absolute;top:0;left:0;right:0;height:3px;background:{CYAN};z-index:10;"></div>
  {GRAIN_LIGHT}
  {logo_html(dark=False)}
  <div style="position:absolute;top:72px;left:32px;right:32px;z-index:20;">
    {kicker("A Verdade", dark=False)}
    <div style="font-family:'Space Grotesk',sans-serif;font-size:17px;font-weight:600;
                color:rgba(26,46,77,0.60);letter-spacing:0.02em;
                text-transform:uppercase;margin-top:10px;line-height:1.35;">
      Mais cliente sem estrutura
    </div>
    <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:700;
                font-size:56px;line-height:0.90;color:{LIGHT_TEXT};margin-top:10px;">
      não é crescimento.<br>
      <span style="color:{CYAN};">É mais pressão</span><br>
      sobre o dono.
    </div>
  </div>
  <div style="position:absolute;bottom:32px;left:32px;right:32px;z-index:20;">
    <div style="background:rgba(30,197,242,0.08);border:1px solid rgba(30,197,242,0.22);
        border-radius:14px;padding:14px 18px;">
      <div style="font-family:'Space Grotesk',sans-serif;font-size:12.5px;font-weight:600;
                  color:{LIGHT_TEXT};line-height:1.45;">Cada novo cliente é mais uma responsabilidade que passa pela sua cabeça.</div>
      <div style="font-family:'Space Grotesk',sans-serif;font-size:11.5px;
                  color:{LIGHT_SUB};line-height:1.55;margin-top:5px;">Não pela operação.</div>
    </div>
  </div>
</div>'''


# ── S5 REVELAÇÃO ──────────────────────────────────────────────────────────────
def slide5():
    img = photo_b64("s2_crescimento.png")
    return f'''
<div style="width:{VW}px;height:{VH}px;position:relative;overflow:hidden;background:{INK};">
  <div style="position:absolute;inset:0;z-index:0;">
    <img src="{img}" style="width:100%;height:100%;object-fit:cover;
         filter:brightness(0.38) contrast(1.10) saturate(0.72);">
  </div>
  <div style="position:absolute;inset:0;z-index:1;
    background:linear-gradient(180deg,
      rgba(6,9,15,0.88) 0%,
      rgba(6,9,15,0.25) 40%,
      transparent 56%,
      rgba(6,9,15,0.72) 74%,
      {INK} 94%);"></div>
  {GRAIN}
  {logo_html(dark=True)}
  <div style="position:absolute;top:72px;left:32px;right:32px;z-index:20;">
    {kicker("A Sequência Correta")}
    <div style="font-family:'Space Grotesk',sans-serif;font-size:17px;font-weight:600;
                color:rgba(255,255,255,0.75);letter-spacing:0.02em;
                text-transform:uppercase;margin-top:10px;line-height:1.35;">
      Antes de escalar, existe uma ordem.
    </div>
    <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:700;
                font-size:60px;line-height:0.88;color:#fff;margin-top:10px;">
      <span style="color:{CYAN};">Estrutura</span> primeiro.<br>
      Demanda depois.
    </div>
  </div>
  <div style="position:absolute;bottom:32px;left:32px;right:32px;z-index:20;">
    {insight_box(
      "Processo, time, cultura, indicadores.",
      "Quando a base está pronta, a demanda multiplica resultado.",
      accent=True, dark=True
    )}
  </div>
</div>'''


# ── S6 INSIGHT ────────────────────────────────────────────────────────────────
def slide6():
    img = photo_b64("s5_equipe.png")
    return f'''
<div style="width:{VW}px;height:{VH}px;position:relative;overflow:hidden;background:{INK2};">
  <div style="position:absolute;inset:0;z-index:0;">
    <img src="{img}" style="width:100%;height:100%;object-fit:cover;
         filter:brightness(0.35) contrast(1.08) saturate(0.68);">
  </div>
  <div style="position:absolute;inset:0;z-index:1;
    background:linear-gradient(180deg,
      rgba(11,15,30,0.90) 0%,
      rgba(11,15,30,0.28) 42%,
      transparent 58%,
      rgba(11,15,30,0.78) 76%,
      {INK2} 95%);"></div>
  {GRAIN}
  {logo_html(dark=True)}
  <div style="position:absolute;top:72px;left:32px;right:32px;z-index:20;">
    {kicker("NUC Vision")}
    <div style="font-family:'Space Grotesk',sans-serif;font-size:17px;font-weight:600;
                color:rgba(255,255,255,0.75);letter-spacing:0.02em;
                text-transform:uppercase;margin-top:10px;line-height:1.35;">
      É aqui que a gente entra.
    </div>
    <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:700;
                font-size:60px;line-height:0.88;color:#fff;margin-top:10px;">
      Antes do marketing,<br>
      <span style="color:{CYAN};">o núcleo.</span>
    </div>
  </div>
  <div style="position:absolute;bottom:32px;left:32px;right:32px;z-index:20;">
    {insight_box(
      "A NUC não chega para gerar demanda.",
      "Chega para organizar o que vai receber essa demanda. E aí sim escalar.",
      accent=True, dark=True
    )}
  </div>
</div>'''


# ── S7 CTA ────────────────────────────────────────────────────────────────────
def slide7():
    return f'''
<div style="width:{VW}px;height:{VH}px;position:relative;overflow:hidden;background:{INK};">
  <div style="position:absolute;inset:0;z-index:0;
    background:radial-gradient(ellipse 80% 60% at 50% 65%, rgba(30,197,242,0.07) 0%, transparent 70%);"></div>
  <div style="position:absolute;inset:0;z-index:1;pointer-events:none;
    background-image:radial-gradient(circle,rgba(255,255,255,0.022) 1px,transparent 1px);
    background-size:28px 28px;"></div>
  {GRAIN}
  {logo_html(dark=True)}
  <div style="position:absolute;inset:0;z-index:20;display:flex;flex-direction:column;
              align-items:center;justify-content:center;padding:32px;text-align:center;">
    <div style="font-family:'Space Grotesk',sans-serif;font-size:9.5px;font-weight:700;
                letter-spacing:0.22em;text-transform:uppercase;color:{CYAN};margin-bottom:22px;opacity:0.8;">
      Estrutura · Crescimento · Resultado
    </div>
    <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:700;
                font-size:50px;line-height:0.92;color:#fff;margin-bottom:28px;">
      Se você sentiu que<br>está preso na<br>
      <span style="color:{CYAN};">operação,</span><br>
      começa por aqui.
    </div>
    <div style="background:{CYAN};color:{INK};font-family:'Space Grotesk',sans-serif;
                font-size:12px;font-weight:700;letter-spacing:0.10em;text-transform:uppercase;
                padding:14px 36px;border-radius:999px;
                box-shadow:0 0 28px rgba(30,197,242,0.30);">
      Siga @nucvision
    </div>
  </div>
</div>'''


# ── EXPORT ────────────────────────────────────────────────────────────────────
SLIDES = {
    "s1_gancho":      slide1(),
    "s2_curiosidade": slide2(),
    "s3_escalada":    slide3(),
    "s4_virada":      slide4(),
    "s5_revelacao":   slide5(),
    "s6_insight":     slide6(),
    "s7_cta":         slide7(),
}

async def export():
    async with async_playwright() as p:
        browser = await p.chromium.launch(executable_path=CHROME)
        for name, body_html in SLIDES.items():
            html = f"""<!DOCTYPE html><html lang="pt-BR"><head>
<meta charset="UTF-8">{FONT_LINK}
<style>*{{margin:0;padding:0;box-sizing:border-box;}}body{{background:#000;}}</style>
</head><body>{body_html}</body></html>"""
            page = await browser.new_page(
                viewport={"width": VW, "height": VH},
                device_scale_factor=SCALE,
            )
            await page.set_content(html, wait_until="networkidle")
            await page.wait_for_timeout(3000)
            out = OUTPUT / f"{name}.png"
            await page.screenshot(
                path=str(out),
                clip={"x": 0, "y": 0, "width": VW, "height": VH},
            )
            await page.close()
            print(f"  → {out.name}")
        await browser.close()
    print("✓ Concluído.")

asyncio.run(export())
