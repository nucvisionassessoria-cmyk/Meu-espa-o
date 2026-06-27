#!/usr/bin/env python3
"""
Teste do novo padrão visual NUC v2.
2 slides: S1 Modo A (condensada/impacto) + S2 Modo B (serif/elegância).
"""
import base64, asyncio
from pathlib import Path
from playwright.async_api import async_playwright

FOTOS   = Path("/home/user/Meu-espa-o/fotos/geradas")
OUTPUT  = Path("/home/user/Meu-espa-o/output/teste-v2")
OUTPUT.mkdir(parents=True, exist_ok=True)

VW, VH = 420, 525
SCALE  = 1080 / VW
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

CYAN   = "#1EC5F2"
INK    = "#06090F"

def photo_b64(name):
    p = FOTOS / name
    return f"data:image/png;base64,{base64.b64encode(p.read_bytes()).decode()}"

FONT_LINK = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@1,600;1,700&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
"""

LOGO_B64 = base64.b64encode(
    Path("/home/user/Meu-espa-o/assets/LOGO DA NUC VISION.png").read_bytes()
).decode()

def logo_html():
    return f'''<div style="position:absolute;top:22px;left:0;right:0;display:flex;
        justify-content:center;z-index:30;">
        <img src="data:image/png;base64,{LOGO_B64}"
             style="height:24px;width:auto;
                    filter:brightness(0) invert(1) drop-shadow(0 2px 8px rgba(0,0,0,0.6));">
    </div>'''

def kicker(txt):
    return f'''<div style="display:flex;align-items:center;gap:8px;margin-bottom:10px;">
        <div style="width:20px;height:1.5px;background:{CYAN};opacity:0.7;"></div>
        <span style="font-family:'Space Grotesk',sans-serif;font-size:9.5px;font-weight:700;
                     letter-spacing:0.22em;text-transform:uppercase;color:{CYAN};">{txt}</span>
    </div>'''

def insight_box(bold_line, sub_line="", accent=False):
    bg  = "rgba(30,197,242,0.10)" if accent else "rgba(255,255,255,0.06)"
    bdr = "rgba(30,197,242,0.28)" if accent else "rgba(255,255,255,0.10)"
    sub = (f'<div style="font-family:\'Space Grotesk\',sans-serif;font-size:11.5px;'
           f'color:rgba(255,255,255,0.50);line-height:1.55;margin-top:5px;">{sub_line}</div>'
           if sub_line else "")
    return f'''<div style="background:{bg};border:1px solid {bdr};border-radius:14px;
        padding:14px 18px;backdrop-filter:blur(8px);">
        <div style="font-family:'Space Grotesk',sans-serif;font-size:12.5px;font-weight:600;
                    color:#fff;line-height:1.45;">{bold_line}</div>
        {sub}
    </div>'''

GRAIN = '''<div style="position:absolute;inset:0;z-index:50;pointer-events:none;opacity:0.06;
    mix-blend-mode:overlay;
    background-image:url('data:image/svg+xml;utf8,<svg xmlns=%22http://www.w3.org/2000/svg%22 width=%22120%22 height=%22120%22><filter id=%22n%22><feTurbulence type=%22fractalNoise%22 baseFrequency=%220.9%22 numOctaves=%222%22/></filter><rect width=%22100%25%22 height=%22100%25%22 filter=%22url(%23n)%22/></svg>');
    background-size:180px 180px;"></div>'''


# ── SLIDE 1 · GANCHO ──────────────────────────────────────────────────────────
def slide1():
    img = photo_b64("s1_dono_noite.png")
    return f'''
<div style="width:{VW}px;height:{VH}px;position:relative;overflow:hidden;background:{INK};">

  <!-- foto full-bleed -->
  <div style="position:absolute;inset:0;z-index:0;">
    <img src="{img}" style="width:100%;height:100%;object-fit:cover;
         filter:brightness(0.50) contrast(1.06) saturate(0.78);">
  </div>

  <!-- gradiente: pesado em cima + base sólida embaixo -->
  <div style="position:absolute;inset:0;z-index:1;
    background:linear-gradient(180deg,
      rgba(6,9,15,0.80) 0%,
      rgba(6,9,15,0.30) 35%,
      transparent 55%,
      rgba(6,9,15,0.72) 72%,
      {INK} 94%);"></div>

  {GRAIN}
  {logo_html()}

  <!-- conteúdo — bloco superior, respiro generoso do logo -->
  <div style="position:absolute;top:72px;left:32px;right:32px;z-index:20;">

    {kicker("Diagnóstico")}

    <!-- setup line: legível, presente, mas subordinada -->
    <div style="font-family:'Space Grotesk',sans-serif;font-size:17px;font-weight:600;
                color:rgba(255,255,255,0.75);letter-spacing:0.02em;
                text-transform:uppercase;margin-top:10px;line-height:1.35;">
      Você construiu um negócio.
    </div>

    <!-- payoff: Cormorant Garamond italic — alto contraste, elegante -->
    <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:700;
                font-size:62px;line-height:0.86;color:#fff;margin-top:10px;">
      Ou uma prisão<br>
      <span style="color:{CYAN};">com CNPJ?</span>
    </div>

  </div>

  <!-- pill: movido para baixo, dentro da zona segura, não compete -->
  <div style="position:absolute;bottom:130px;right:32px;z-index:20;
    background:rgba(255,55,55,0.14);border:1px solid rgba(255,70,70,0.35);
    border-radius:999px;padding:5px 14px;backdrop-filter:blur(8px);">
    <span style="font-family:'Space Grotesk',sans-serif;font-size:9px;font-weight:700;
                 letter-spacing:0.15em;text-transform:uppercase;color:rgba(255,110,110,0.88);">
      3 anos sem férias
    </span>
  </div>

  <!-- insight container — rodapé -->
  <div style="position:absolute;bottom:32px;left:32px;right:32px;z-index:20;">
    {insight_box(
      "Se você para, a empresa para.",
      "O sinal mais claro apareceu numa segunda-feira de janeiro."
    )}
  </div>

</div>'''


# ── SLIDE 2 · REVELAÇÃO ───────────────────────────────────────────────────────
def slide2():
    img = photo_b64("s6_dispensavel.png")
    return f'''
<div style="width:{VW}px;height:{VH}px;position:relative;overflow:hidden;background:#07090c;">

  <!-- foto full-bleed -->
  <div style="position:absolute;inset:0;z-index:0;">
    <img src="{img}" style="width:100%;height:100%;object-fit:cover;
         filter:brightness(0.44) contrast(1.05) saturate(0.70);">
  </div>

  <!-- gradiente: janela no centro, escuro nas pontas -->
  <div style="position:absolute;inset:0;z-index:1;
    background:linear-gradient(180deg,
      rgba(7,9,12,0.72) 0%,
      rgba(7,9,12,0.18) 32%,
      transparent 52%,
      rgba(7,9,12,0.68) 72%,
      #07090c 92%);"></div>

  <!-- dot grid mínimo -->
  <div style="position:absolute;inset:0;z-index:2;pointer-events:none;
    background-image:radial-gradient(circle,rgba(255,255,255,0.022) 1px,transparent 1px);
    background-size:28px 28px;"></div>

  {GRAIN}
  {logo_html()}

  <!-- conteúdo principal -->
  <div style="position:absolute;top:72px;left:32px;right:32px;z-index:20;">

    {kicker("A Revelação")}

    <!-- setup line -->
    <div style="font-family:'Space Grotesk',sans-serif;font-size:17px;font-weight:600;
                color:rgba(255,255,255,0.75);letter-spacing:0.02em;
                text-transform:uppercase;margin-top:10px;line-height:1.35;">
      O objetivo não é ser indispensável.
    </div>

    <!-- payoff: Cormorant Garamond italic -->
    <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:700;
                font-size:62px;line-height:0.86;color:#fff;margin-top:10px;">
      É você ser<br>
      <span style="color:{CYAN};">dispensável.</span>
    </div>

    <!-- divisor sutil após headline -->
    <div style="margin-top:20px;width:38px;height:1px;
                background:{CYAN};opacity:0.45;"></div>

  </div>

  <!-- insight container — rodapé, variante com borda ciano -->
  <div style="position:absolute;bottom:32px;left:32px;right:32px;z-index:20;">
    {insight_box(
      "Não é abandono. É liberdade.",
      "Quando a empresa funciona sem você, você escolhe onde colocar sua energia.",
      accent=True
    )}
  </div>

</div>'''


# ── MONTAGEM E EXPORT ──────────────────────────────────────────────────────────
HTML = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
{FONT_LINK}
<style>
  * {{ margin:0;padding:0;box-sizing:border-box; }}
  body {{ background:#000; }}
</style>
</head>
<body>
{slide1()}
{slide2()}
</body>
</html>"""

SLIDE_HTML = {
    "slide_01_modo_A_condensada": slide1(),
    "slide_02_modo_B_serif":      slide2(),
}

async def export():
    async with async_playwright() as p:
        browser = await p.chromium.launch(executable_path=CHROME)
        for name, body_html in SLIDE_HTML.items():
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
