#!/usr/bin/env python3
"""
Carrossel Segunda-feira v2 — "Mais clientes sem estrutura não resolvem o crescimento."
8 slides com desenvolvimento narrativo real: etiqueta + headline + corpo (35-65 palavras) + transição.
S4 e S6 são slides claros (quebra de ritmo interno).
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
        <img src="{LOGO_URI}" style="height:52px;width:auto;filter:{filt};">
    </div>'''

def kicker(txt, dark=True):
    return f'''<div style="display:flex;align-items:center;gap:8px;margin-bottom:10px;">
        <div style="width:18px;height:1.5px;background:{CYAN};opacity:0.85;"></div>
        <span style="font-family:'Space Grotesk',sans-serif;font-size:9px;font-weight:700;
                     letter-spacing:0.22em;text-transform:uppercase;color:{CYAN};">{txt}</span>
    </div>'''

def headline(txt, dark=True, size=46):
    color = "#fff" if dark else LIGHT_TEXT
    return f'''<div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:700;
                font-size:{size}px;line-height:0.92;color:{color};margin-top:6px;">{txt}</div>'''

def body(txt, dark=True):
    color = "rgba(255,255,255,0.80)" if dark else LIGHT_SUB
    return f'''<div style="font-family:'Space Grotesk',sans-serif;font-size:13px;
                font-weight:400;color:{color};line-height:1.65;margin-top:14px;">{txt}</div>'''

def transition_box(txt, dark=True, accent=False):
    if dark:
        bg  = "rgba(30,197,242,0.10)" if accent else "rgba(255,255,255,0.06)"
        bdr = "rgba(30,197,242,0.30)" if accent else "rgba(255,255,255,0.10)"
        col = "#fff"
    else:
        bg  = "rgba(30,197,242,0.08)"
        bdr = "rgba(30,197,242,0.22)"
        col = LIGHT_TEXT
    return f'''<div style="background:{bg};border:1px solid {bdr};border-radius:14px;
        padding:13px 18px;backdrop-filter:blur(8px);">
        <div style="font-family:'Space Grotesk',sans-serif;font-size:12px;font-weight:600;
                    color:{col};line-height:1.45;">{txt}</div>
    </div>'''

GRAIN = '''<div style="position:absolute;inset:0;z-index:50;pointer-events:none;opacity:0.06;
    mix-blend-mode:overlay;
    background-image:url('data:image/svg+xml;utf8,<svg xmlns=%22http://www.w3.org/2000/svg%22 width=%22120%22 height=%22120%22><filter id=%22n%22><feTurbulence type=%22fractalNoise%22 baseFrequency=%220.9%22 numOctaves=%222%22/></filter><rect width=%22100%25%22 height=%22100%25%22 filter=%22url(%23n)%22/></svg>');
    background-size:180px 180px;"></div>'''

GRAIN_LIGHT = '''<div style="position:absolute;inset:0;z-index:50;pointer-events:none;opacity:0.035;
    mix-blend-mode:multiply;
    background-image:url('data:image/svg+xml;utf8,<svg xmlns=%22http://www.w3.org/2000/svg%22 width=%22120%22 height=%22120%22><filter id=%22n%22><feTurbulence type=%22fractalNoise%22 baseFrequency=%220.9%22 numOctaves=%222%22/></filter><rect width=%22100%25%22 height=%22100%25%22 filter=%22url(%23n)%22/></svg>');
    background-size:180px 180px;"></div>'''


# ── S1 A CRENÇA ───────────────────────────────────────────────────────────────
def slide1():
    img = photo_b64("s1_dono_noite.png")
    return f'''
<div style="width:{VW}px;height:{VH}px;position:relative;overflow:hidden;background:{INK};">
  <div style="position:absolute;inset:0;z-index:0;">
    <img src="{img}" style="width:100%;height:100%;object-fit:cover;
         filter:brightness(0.42) contrast(1.06) saturate(0.70);">
  </div>
  <div style="position:absolute;inset:0;z-index:1;
    background:linear-gradient(180deg,
      rgba(6,9,15,0.92) 0%,
      rgba(6,9,15,0.75) 45%,
      rgba(6,9,15,0.50) 60%,
      rgba(6,9,15,0.82) 80%,
      {INK} 95%);"></div>
  {GRAIN}
  {logo_html(dark=True)}
  <div style="position:absolute;top:80px;left:32px;right:32px;z-index:20;">
    {kicker("A Crença")}
    {headline('Todo dono quer<br>mais <span style="color:{CYAN};">clientes.</span>'.format(CYAN=CYAN))}
    {body("Quando as vendas travam, essa parece a resposta mais óbvia. Mas nem sempre a empresa precisa de mais pessoas chegando. Às vezes, ela precisa entender por que as pessoas que já chegam não avançam.")}
  </div>
  <div style="position:absolute;bottom:28px;left:32px;right:32px;z-index:20;">
    {transition_box("Antes de buscar mais demanda, olhe para o caminho da venda.")}
  </div>
</div>'''


# ── S2 A QUEBRA ───────────────────────────────────────────────────────────────
def slide2():
    img = photo_b64("s4_engrenagem.png")
    return f'''
<div style="width:{VW}px;height:{VH}px;position:relative;overflow:hidden;background:{INK};">
  <div style="position:absolute;inset:0;z-index:0;">
    <img src="{img}" style="width:100%;height:100%;object-fit:cover;
         filter:brightness(0.40) contrast(1.08) saturate(0.65);">
  </div>
  <div style="position:absolute;inset:0;z-index:1;
    background:linear-gradient(180deg,
      rgba(6,9,15,0.93) 0%,
      rgba(6,9,15,0.78) 48%,
      rgba(6,9,15,0.52) 62%,
      rgba(6,9,15,0.84) 80%,
      {INK} 96%);"></div>
  {GRAIN}
  {logo_html(dark=True)}
  <div style="position:absolute;top:80px;left:32px;right:32px;z-index:20;">
    {kicker("A Quebra")}
    {headline('O cliente<br>até <span style="color:{CYAN};">aparece.</span>'.format(CYAN=CYAN))}
    {body("Ele chama no WhatsApp, pede informação, responde um anúncio ou demonstra interesse. Só que, quando a operação não tem processo, esse interesse não é conduzido com clareza até a compra.")}
  </div>
  <div style="position:absolute;bottom:28px;left:32px;right:32px;z-index:20;">
    {transition_box("É nesse intervalo que muita venda se perde.")}
  </div>
</div>'''


# ── S3 O SINTOMA ──────────────────────────────────────────────────────────────
def slide3():
    img = photo_b64("s3_doente.png")
    return f'''
<div style="width:{VW}px;height:{VH}px;position:relative;overflow:hidden;background:{INK};">
  <div style="position:absolute;inset:0;z-index:0;">
    <img src="{img}" style="width:100%;height:100%;object-fit:cover;
         filter:brightness(0.38) contrast(1.09) saturate(0.62);">
  </div>
  <div style="position:absolute;inset:0;z-index:1;
    background:linear-gradient(180deg,
      rgba(6,9,15,0.93) 0%,
      rgba(6,9,15,0.78) 48%,
      rgba(6,9,15,0.50) 62%,
      rgba(6,9,15,0.84) 80%,
      {INK} 96%);"></div>
  {GRAIN}
  {logo_html(dark=True)}
  <div style="position:absolute;top:80px;left:32px;right:32px;z-index:20;">
    {kicker("O Sintoma")}
    {headline('A operação trava<br>no <span style="color:{CYAN};">atendimento.</span>'.format(CYAN=CYAN))}
    {body("Resposta lenta, mensagem genérica, falta de follow-up e ausência de próximo passo fazem o lead esfriar. O cliente não perdeu interesse no produto. Muitas vezes, ele perdeu segurança na empresa.")}
  </div>
  <div style="position:absolute;bottom:28px;left:32px;right:32px;z-index:20;">
    {transition_box("O problema deixa de ser atração e vira condução.")}
  </div>
</div>'''


# ── S4 A CAUSA — SLIDE CLARO ─────────────────────────────────────────────────
def slide4():
    return f'''
<div style="width:{VW}px;height:{VH}px;position:relative;overflow:hidden;background:{LIGHT_BG};">
  <div style="position:absolute;inset:0;z-index:1;pointer-events:none;
    background-image:radial-gradient(circle,rgba(26,46,77,0.055) 1px,transparent 1px);
    background-size:28px 28px;"></div>
  <div style="position:absolute;top:0;left:0;right:0;height:3px;background:{CYAN};z-index:10;"></div>
  {GRAIN_LIGHT}
  {logo_html(dark=False)}
  <div style="position:absolute;top:80px;left:32px;right:32px;z-index:20;">
    {kicker("A Causa", dark=False)}
    {headline('Falta estrutura para<br><span style="color:{CYAN};">aproveitar</span><br>a demanda.'.format(CYAN=CYAN), dark=False, size=42)}
    {body("Sem rotina comercial, padrão de atendimento, responsáveis claros e acompanhamento, cada lead é tratado de um jeito. A empresa gera oportunidade, mas não tem sistema para transformar oportunidade em venda.", dark=False)}
  </div>
  <div style="position:absolute;bottom:28px;left:32px;right:32px;z-index:20;">
    {transition_box("E quando não existe sistema, tudo volta para o dono.", dark=False)}
  </div>
</div>'''


# ── S5 A CONSEQUÊNCIA ─────────────────────────────────────────────────────────
def slide5():
    img = photo_b64("s2_crescimento.png")
    return f'''
<div style="width:{VW}px;height:{VH}px;position:relative;overflow:hidden;background:{INK};">
  <div style="position:absolute;inset:0;z-index:0;">
    <img src="{img}" style="width:100%;height:100%;object-fit:cover;
         filter:brightness(0.36) contrast(1.10) saturate(0.68);">
  </div>
  <div style="position:absolute;inset:0;z-index:1;
    background:linear-gradient(180deg,
      rgba(6,9,15,0.93) 0%,
      rgba(6,9,15,0.78) 48%,
      rgba(6,9,15,0.50) 62%,
      rgba(6,9,15,0.82) 80%,
      {INK} 96%);"></div>
  {GRAIN}
  {logo_html(dark=True)}
  <div style="position:absolute;top:80px;left:32px;right:32px;z-index:20;">
    {kicker("A Consequência")}
    {headline('Mais clientes sem estrutura<br>viram mais <span style="color:{CYAN};">pressão.</span>'.format(CYAN=CYAN), size=40)}
    {body("Cada nova conversa exige cobrança, correção, decisão e acompanhamento. O dono começa a sentir que vender mais não trouxe crescimento. Trouxe mais urgência, mais retrabalho e mais dependência dele.")}
  </div>
  <div style="position:absolute;bottom:28px;left:32px;right:32px;z-index:20;">
    {transition_box("Demanda sem base não escala. Ela sobrecarrega.", accent=True)}
  </div>
</div>'''


# ── S6 A VIRADA — SLIDE CLARO ─────────────────────────────────────────────────
def slide6():
    return f'''
<div style="width:{VW}px;height:{VH}px;position:relative;overflow:hidden;background:{LIGHT_BG};">
  <div style="position:absolute;inset:0;z-index:1;pointer-events:none;
    background-image:radial-gradient(circle,rgba(26,46,77,0.055) 1px,transparent 1px);
    background-size:28px 28px;"></div>
  <div style="position:absolute;top:0;left:0;right:0;height:3px;background:{CYAN};z-index:10;"></div>
  {GRAIN_LIGHT}
  {logo_html(dark=False)}
  <div style="position:absolute;top:80px;left:32px;right:32px;z-index:20;">
    {kicker("A Virada", dark=False)}
    {headline('O problema não<br>é querer vender <span style="color:{CYAN};">mais.</span>'.format(CYAN=CYAN), dark=False, size=42)}
    {body("O problema é tentar vender mais antes de entender onde a empresa está vazando resultado. Sem diagnóstico, o marketing vira tentativa e o comercial continua apagando incêndio.", dark=False)}
  </div>
  <div style="position:absolute;bottom:28px;left:32px;right:32px;z-index:20;">
    {transition_box("Antes de acelerar, é preciso encontrar o gargalo.", dark=False)}
  </div>
</div>'''


# ── S7 O CAMINHO ──────────────────────────────────────────────────────────────
def slide7():
    img = photo_b64("s5_equipe.png")
    return f'''
<div style="width:{VW}px;height:{VH}px;position:relative;overflow:hidden;background:{INK2};">
  <div style="position:absolute;inset:0;z-index:0;">
    <img src="{img}" style="width:100%;height:100%;object-fit:cover;
         filter:brightness(0.33) contrast(1.08) saturate(0.65);">
  </div>
  <div style="position:absolute;inset:0;z-index:1;
    background:linear-gradient(180deg,
      rgba(11,15,30,0.93) 0%,
      rgba(11,15,30,0.78) 48%,
      rgba(11,15,30,0.50) 62%,
      rgba(11,15,30,0.84) 80%,
      {INK2} 96%);"></div>
  {GRAIN}
  {logo_html(dark=True)}
  <div style="position:absolute;top:80px;left:32px;right:32px;z-index:20;">
    {kicker("O Caminho")}
    {headline('<span style="color:{CYAN};">Estrutura</span> primeiro.<br>Demanda depois.'.format(CYAN=CYAN))}
    {body("Quando atendimento, follow-up, responsáveis e processo estão claros, cada lead passa a ser melhor aproveitado. A empresa para de depender de volume e começa a melhorar conversão.")}
  </div>
  <div style="position:absolute;bottom:28px;left:32px;right:32px;z-index:20;">
    {transition_box("É isso que transforma procura em crescimento real.", accent=True)}
  </div>
</div>'''


# ── S8 FECHAMENTO CTA ─────────────────────────────────────────────────────────
def slide8():
    return f'''
<div style="width:{VW}px;height:{VH}px;position:relative;overflow:hidden;background:{INK};">
  <div style="position:absolute;inset:0;z-index:0;
    background:radial-gradient(ellipse 80% 60% at 50% 55%, rgba(30,197,242,0.07) 0%, transparent 70%);"></div>
  <div style="position:absolute;inset:0;z-index:1;pointer-events:none;
    background-image:radial-gradient(circle,rgba(255,255,255,0.022) 1px,transparent 1px);
    background-size:28px 28px;"></div>
  {GRAIN}
  {logo_html(dark=True)}
  <div style="position:absolute;top:80px;left:32px;right:32px;z-index:20;">
    {kicker("Conclusão")}
    {headline('Mais clientes só ajudam quando a empresa sabe o que fazer com eles.', size=38)}
    {body("Antes de investir em tráfego, conteúdo ou campanhas, entenda se sua operação está pronta para receber, conduzir e converter as oportunidades que já chegam.")}
    <div style="font-family:'Space Grotesk',sans-serif;font-size:13px;font-weight:600;
                color:{CYAN};margin-top:14px;line-height:1.5;">
      Crescer não é só atrair mais. É desperdiçar menos.
    </div>
  </div>
  <div style="position:absolute;bottom:28px;left:32px;right:32px;z-index:20;">
    <div style="background:{CYAN};color:{INK};font-family:'Space Grotesk',sans-serif;
                font-size:12px;font-weight:700;letter-spacing:0.10em;text-transform:uppercase;
                padding:13px 0;border-radius:999px;text-align:center;
                box-shadow:0 0 28px rgba(30,197,242,0.28);">
      Siga @nucvision
    </div>
  </div>
</div>'''


# ── EXPORT ────────────────────────────────────────────────────────────────────
SLIDES = {
    "s1_crenca":      slide1(),
    "s2_quebra":      slide2(),
    "s3_sintoma":     slide3(),
    "s4_causa":       slide4(),
    "s5_consequencia":slide5(),
    "s6_virada":      slide6(),
    "s7_caminho":     slide7(),
    "s8_cta":         slide8(),
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
