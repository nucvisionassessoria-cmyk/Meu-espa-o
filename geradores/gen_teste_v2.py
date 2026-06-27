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
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Playfair+Display:ital,wght@1,700;1,900&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
"""

LOGO_B64 = base64.b64encode(
    Path("/home/user/Meu-espa-o/assets/logo-nuc.png").read_bytes()
).decode() if Path("/home/user/Meu-espa-o/assets/logo-nuc.png").exists() else ""

def logo_html():
    if LOGO_B64:
        return f'''<div style="position:absolute;top:22px;left:0;right:0;display:flex;
            justify-content:center;z-index:30;">
            <img src="data:image/png;base64,{LOGO_B64}"
                 style="height:24px;width:auto;
                        filter:brightness(0) invert(1) drop-shadow(0 2px 8px rgba(0,0,0,0.6));">
        </div>'''
    # fallback: wordmark em texto
    return f'''<div style="position:absolute;top:22px;left:0;right:0;display:flex;
        justify-content:center;z-index:30;">
        <span style="font-family:'Space Grotesk',sans-serif;font-size:11px;font-weight:700;
                     letter-spacing:0.22em;color:rgba(255,255,255,0.85);text-transform:uppercase;">
            NUC VISION
        </span>
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


# ── SLIDE 1 · MODO A (condensada/impacto) ─────────────────────────────────────
def slide1():
    img = photo_b64("s1_dono_noite.png")
    return f'''
<div style="width:{VW}px;height:{VH}px;position:relative;overflow:hidden;background:{INK};">

  <!-- foto full-bleed -->
  <div style="position:absolute;inset:0;z-index:0;">
    <img src="{img}" style="width:100%;height:100%;object-fit:cover;
         filter:brightness(0.55) contrast(1.08) saturate(0.82);">
  </div>

  <!-- gradiente: pesado em cima e embaixo, janela no meio -->
  <div style="position:absolute;inset:0;z-index:1;
    background:linear-gradient(180deg,
      rgba(6,9,15,0.72) 0%,
      transparent 30%,
      transparent 52%,
      rgba(6,9,15,0.68) 68%,
      {INK} 92%);"></div>

  <!-- grão -->
  {GRAIN}

  {logo_html()}

  <!-- tag superior direita -->
  <div style="position:absolute;top:54px;right:28px;z-index:20;
    background:rgba(255,55,55,0.16);border:1px solid rgba(255,70,70,0.38);
    border-radius:999px;padding:5px 13px;backdrop-filter:blur(6px);">
    <span style="font-family:'Space Grotesk',sans-serif;font-size:9px;font-weight:700;
                 letter-spacing:0.16em;text-transform:uppercase;color:rgba(255,120,120,0.9);">
      3 anos sem férias
    </span>
  </div>

  <!-- conteúdo principal — topo esquerdo -->
  <div style="position:absolute;top:56px;left:32px;z-index:20;max-width:260px;">
    {kicker("O Diagnóstico")}

    <!-- MODO A: Anton condensada, caixa-alta, impacto -->
    <div style="font-family:'Anton',sans-serif;font-size:50px;line-height:0.88;
                color:#fff;text-transform:uppercase;letter-spacing:0.01em;">
      SE VOCÊ<br>
      PARA,<br>
      A EMPRESA<br>
      <span style="background:{CYAN};color:#06121c;
                   padding:1px 10px 6px;border-radius:8px;display:inline-block;line-height:0.9;
                   box-shadow:0 6px 20px rgba(30,197,242,0.4);">PARA.</span>
    </div>
  </div>

  <!-- insight container — rodapé -->
  <div style="position:absolute;bottom:32px;left:32px;right:32px;z-index:20;">
    {insight_box(
      "Você construiu um negócio. Ou uma prisão com CNPJ?",
      "O sinal mais claro apareceu numa segunda-feira de janeiro."
    )}
  </div>

</div>'''


# ── SLIDE 2 · MODO B (serif italic/elegância) ─────────────────────────────────
def slide2():
    img = photo_b64("s6_dispensavel.png")
    return f'''
<div style="width:{VW}px;height:{VH}px;position:relative;overflow:hidden;background:#07090c;">

  <!-- foto full-bleed com tratamento suave -->
  <div style="position:absolute;inset:0;z-index:0;">
    <img src="{img}" style="width:100%;height:100%;object-fit:cover;
         filter:brightness(0.48) contrast(1.06) saturate(0.75);">
  </div>

  <!-- vinheta suave: mais leve que o S1, menos dramático -->
  <div style="position:absolute;inset:0;z-index:1;
    background:linear-gradient(180deg,
      rgba(7,9,12,0.60) 0%,
      transparent 28%,
      transparent 50%,
      rgba(7,9,12,0.65) 68%,
      #07090c 90%);"></div>

  <!-- dot grid sutil -->
  <div style="position:absolute;inset:0;z-index:2;pointer-events:none;
    background-image:radial-gradient(circle,rgba(255,255,255,0.028) 1px,transparent 1px);
    background-size:26px 26px;"></div>

  {GRAIN}

  {logo_html()}

  <!-- conteúdo principal -->
  <div style="position:absolute;top:56px;left:32px;right:32px;z-index:20;">
    {kicker("A Revelação")}

    <!-- MODO B: Playfair Display italic, mixed-case, elegância -->
    <div style="font-family:'Playfair Display',serif;font-style:italic;font-weight:700;
                font-size:48px;line-height:0.92;color:#fff;margin-top:4px;">
      O objetivo<br>é você ser<br>
      <span style="color:{CYAN};">dispensável.</span>
    </div>

    <!-- linha de contraste suave abaixo da headline -->
    <div style="margin-top:16px;width:44px;height:1.5px;
                background:linear-gradient(90deg,{CYAN},transparent);opacity:0.6;"></div>
  </div>

  <!-- insight container — rodapé -->
  <div style="position:absolute;bottom:32px;left:32px;right:32px;z-index:20;">
    {insight_box(
      "Não é abandono. É liberdade.",
      "Quando a empresa funciona sem você presente, você escolhe onde colocar sua energia. Isso se constrói.",
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
