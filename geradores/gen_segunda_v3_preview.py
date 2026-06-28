#!/usr/bin/env python3
"""Preview v3 — 3 primeiros slides do carrossel de Segunda."""
import sys, base64, asyncio
from pathlib import Path
sys.path.insert(0, "/home/user/Meu-espa-o")
from design_system import LOGO_URI
from playwright.async_api import async_playwright

FOTOS  = Path("/home/user/Meu-espa-o/fotos/geradas")
OUTPUT = Path("/home/user/Meu-espa-o/output/segunda-v3")
OUTPUT.mkdir(parents=True, exist_ok=True)

VW, VH = 420, 525
SCALE  = 1080 / VW
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

CYAN, INK, INK2 = "#1EC5F2", "#06090F", "#0b0f1e"
LIGHT_BG, LIGHT_TEXT, LIGHT_SUB = "#EEF3F8", "#1A2E4D", "rgba(26,46,77,0.62)"

FONTS = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@1,600;1,700&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
"""

def b64(name):
    return f"data:image/png;base64,{base64.b64encode((FOTOS/name).read_bytes()).decode()}"

def logo(dark=True):
    f = "brightness(0) invert(1) drop-shadow(0 2px 10px rgba(0,0,0,0.7))" if dark else "drop-shadow(0 1px 4px rgba(26,46,77,0.18))"
    return f'<div style="position:absolute;top:20px;left:0;right:0;display:flex;justify-content:center;z-index:30;"><img src="{LOGO_URI}" style="height:48px;width:auto;filter:{f};"></div>'

GRAIN = '''<div style="position:absolute;inset:0;z-index:50;pointer-events:none;opacity:0.06;mix-blend-mode:overlay;background-image:url('data:image/svg+xml;utf8,<svg xmlns=%22http://www.w3.org/2000/svg%22 width=%22120%22 height=%22120%22><filter id=%22n%22><feTurbulence type=%22fractalNoise%22 baseFrequency=%220.9%22 numOctaves=%222%22/></filter><rect width=%22100%25%22 height=%22100%25%22 filter=%22url(%23n)%22/></svg>');background-size:180px 180px;"></div>'''

GRAIN_LIGHT = '''<div style="position:absolute;inset:0;z-index:50;pointer-events:none;opacity:0.035;mix-blend-mode:multiply;background-image:url('data:image/svg+xml;utf8,<svg xmlns=%22http://www.w3.org/2000/svg%22 width=%22120%22 height=%22120%22><filter id=%22n%22><feTurbulence type=%22fractalNoise%22 baseFrequency=%220.9%22 numOctaves=%222%22/></filter><rect width=%22100%25%22 height=%22100%25%22 filter=%22url(%23n)%22/></svg>');background-size:180px 180px;"></div>'''


# ── S1 IMPACTO — imagem dominante, headline grande, ponte destacada ────────
def s1():
    img = b64("v3_s1_mesa_demanda.png")
    return f'''
<div style="width:{VW}px;height:{VH}px;position:relative;overflow:hidden;background:{INK};">
  <div style="position:absolute;inset:0;z-index:0;">
    <img src="{img}" style="width:100%;height:100%;object-fit:cover;filter:brightness(0.78) contrast(1.05) saturate(0.95);">
  </div>
  <div style="position:absolute;inset:0;z-index:1;
    background:linear-gradient(180deg, rgba(6,9,15,0.15) 0%, rgba(6,9,15,0.05) 35%, rgba(6,9,15,0.55) 65%, rgba(6,9,15,0.95) 100%);"></div>
  {GRAIN}
  {logo(dark=True)}
  <div style="position:absolute;left:30px;right:30px;bottom:28px;z-index:20;">
    <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:700;
                font-size:42px;line-height:0.95;color:#fff;letter-spacing:-0.01em;
                text-shadow:0 2px 18px rgba(0,0,0,0.5);">
      Mais clientes não consertam<br>
      uma operação que<br>
      <span style="color:{CYAN};">não conduz.</span>
    </div>
    <div style="font-family:'Space Grotesk',sans-serif;font-size:12.5px;font-weight:400;
                color:rgba(255,255,255,0.78);line-height:1.55;margin-top:14px;max-width:340px;">
      Você acha que precisa de tráfego. Mas o problema raramente está em quem chega.
    </div>
    <div style="margin-top:14px;padding-top:12px;border-top:1px solid rgba(30,197,242,0.35);
                font-family:'Space Grotesk',sans-serif;font-style:italic;font-size:12.5px;
                font-weight:500;color:{CYAN};letter-spacing:0.01em;">
      Está no que acontece depois.
    </div>
  </div>
</div>'''


# ── S2 CONTEXTO — claro, foto sangrando à esquerda, texto à direita ────────
def s2():
    img = b64("v3_s2_notebook_caderno.png")
    return f'''
<div style="width:{VW}px;height:{VH}px;position:relative;overflow:hidden;background:{LIGHT_BG};">
  <div style="position:absolute;left:0;top:0;bottom:0;width:48%;z-index:0;">
    <img src="{img}" style="width:100%;height:100%;object-fit:cover;">
    <div style="position:absolute;inset:0;
      background:linear-gradient(90deg, transparent 60%, {LIGHT_BG} 100%);"></div>
  </div>
  <div style="position:absolute;top:0;left:0;right:0;height:3px;background:{CYAN};z-index:10;"></div>
  {GRAIN_LIGHT}
  {logo(dark=False)}

  <div style="position:absolute;top:88px;left:50%;right:28px;z-index:20;">
    <div style="display:flex;align-items:center;gap:8px;margin-bottom:14px;">
      <div style="width:18px;height:1.5px;background:{CYAN};"></div>
      <span style="font-family:'Space Grotesk',sans-serif;font-size:9px;font-weight:700;
                   letter-spacing:0.22em;text-transform:uppercase;color:{CYAN};">O que ninguém olha</span>
    </div>
    <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:700;
                font-size:28px;line-height:1.0;color:{LIGHT_TEXT};">
      Depois do interesse,<br>
      é onde quase toda<br>
      venda <span style="color:{CYAN};">morre.</span>
    </div>
    <div style="font-family:'Space Grotesk',sans-serif;font-size:12px;font-weight:400;
                color:{LIGHT_SUB};line-height:1.65;margin-top:18px;">
      O cliente chama, demonstra curiosidade, pede informação. E nesse intervalo entre o
      <span style="color:{LIGHT_TEXT};font-weight:600;">"tenho interesse"</span> e o
      <span style="color:{LIGHT_TEXT};font-weight:600;">"fechei"</span>, a empresa começa a
      perder dinheiro sem perceber.
    </div>
  </div>

  <div style="position:absolute;left:28px;right:28px;bottom:24px;z-index:20;
              padding-top:14px;border-top:1px solid rgba(30,197,242,0.30);">
    <div style="font-family:'Space Grotesk',sans-serif;font-style:italic;font-size:12px;
                font-weight:500;color:{LIGHT_TEXT};">
      E esse vazamento tem etapas claras.
    </div>
  </div>
</div>'''


# ── S3 SINTOMA — lista escura, sem foto, cards numerados ───────────────────
def s3():
    items = [
        ("01", "O cliente chama."),
        ("02", "A resposta demora horas. Ou um dia."),
        ("03", "O atendimento muda conforme quem responde."),
        ("04", "O follow-up depende da memória de alguém."),
        ("05", "O lead esfria antes de virar proposta."),
    ]
    cards = ""
    for n, txt in items:
        cards += f'''
        <div style="display:flex;align-items:flex-start;gap:14px;padding:12px 0;
                    border-bottom:1px solid rgba(255,255,255,0.08);">
          <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:700;
                      font-size:22px;color:{CYAN};line-height:1;min-width:30px;">{n}</div>
          <div style="font-family:'Space Grotesk',sans-serif;font-size:13.5px;font-weight:500;
                      color:#fff;line-height:1.4;">{txt}</div>
        </div>'''

    return f'''
<div style="width:{VW}px;height:{VH}px;position:relative;overflow:hidden;background:{INK};">
  <div style="position:absolute;inset:0;z-index:0;
    background:radial-gradient(ellipse 70% 50% at 50% 30%, rgba(30,197,242,0.05) 0%, transparent 70%),
               radial-gradient(circle, rgba(255,255,255,0.018) 1px, transparent 1px);
    background-size:auto, 24px 24px;"></div>
  {GRAIN}
  {logo(dark=True)}

  <div style="position:absolute;top:88px;left:30px;right:30px;z-index:20;">
    <div style="display:flex;align-items:center;gap:8px;margin-bottom:14px;">
      <div style="width:18px;height:1.5px;background:{CYAN};"></div>
      <span style="font-family:'Space Grotesk',sans-serif;font-size:9px;font-weight:700;
                   letter-spacing:0.22em;text-transform:uppercase;color:{CYAN};">Onde o lead morre</span>
    </div>
    <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:700;
                font-size:30px;line-height:1.0;color:#fff;margin-bottom:8px;">
      São <span style="color:{CYAN};">essas</span> etapas:
    </div>
    <div style="margin-top:14px;">
      {cards}
    </div>
  </div>

  <div style="position:absolute;left:30px;right:30px;bottom:24px;z-index:20;
              padding-top:12px;border-top:1px solid rgba(30,197,242,0.30);">
    <div style="font-family:'Space Grotesk',sans-serif;font-style:italic;font-size:12.5px;
                font-weight:500;color:{CYAN};">
      Nada disso é falta de cliente. É outra coisa.
    </div>
  </div>
</div>'''


SLIDES = {"s1_impacto": s1(), "s2_contexto": s2(), "s3_sintoma": s3()}

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(executable_path=CHROME)
        for name, html_body in SLIDES.items():
            html = f"""<!DOCTYPE html><html><head><meta charset="UTF-8">{FONTS}
<style>*{{margin:0;padding:0;box-sizing:border-box;}}body{{background:#000;}}</style>
</head><body>{html_body}</body></html>"""
            page = await browser.new_page(viewport={"width": VW, "height": VH}, device_scale_factor=SCALE)
            await page.set_content(html, wait_until="networkidle")
            await page.wait_for_timeout(3000)
            await page.screenshot(path=str(OUTPUT/f"{name}.png"), clip={"x":0,"y":0,"width":VW,"height":VH})
            await page.close()
            print(f"  → {name}.png")
        await browser.close()

asyncio.run(run())
