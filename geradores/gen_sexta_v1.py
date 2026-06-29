#!/usr/bin/env python3
"""Sexta — 'Marketing não conserta operação' — claro, com S3 e S6 escuros (quebra)."""
import sys, base64, asyncio
from pathlib import Path
sys.path.insert(0, "/home/user/Meu-espa-o")
from design_system import LOGO_URI
from playwright.async_api import async_playwright

FOTOS  = Path("/home/user/Meu-espa-o/fotos")
GER    = Path("/home/user/Meu-espa-o/fotos/geradas")
OUTPUT = Path("/home/user/Meu-espa-o/output/sexta-marketing")
OUTPUT.mkdir(parents=True, exist_ok=True)

VW, VH = 420, 525
SCALE  = 1080 / VW
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

CYAN, INK, INK2 = "#1EC5F2", "#06090F", "#0b0f1e"
LIGHT_BG, LIGHT_TEXT, LIGHT_SUB = "#EEF3F8", "#1A2E4D", "rgba(26,46,77,0.62)"
LIGHT_BORDER = "rgba(26,46,77,0.10)"

FONTS = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@1,600;1,700&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
"""

def b64(path):
    return f"data:image/png;base64,{base64.b64encode(Path(path).read_bytes()).decode()}"

def logo(dark=True):
    f = "brightness(0) invert(1) drop-shadow(0 2px 10px rgba(0,0,0,0.7))" if dark else "drop-shadow(0 1px 4px rgba(26,46,77,0.18))"
    return f'<div style="position:absolute;top:20px;left:0;right:0;display:flex;justify-content:center;z-index:30;"><img src="{LOGO_URI}" style="height:48px;width:auto;filter:{f};"></div>'

def kicker(txt, dark=True):
    return f'''<div style="display:flex;align-items:center;gap:8px;margin-bottom:14px;">
      <div style="width:18px;height:1.5px;background:{CYAN};"></div>
      <span style="font-family:'Space Grotesk',sans-serif;font-size:9px;font-weight:700;
                   letter-spacing:0.22em;text-transform:uppercase;color:{CYAN};">{txt}</span>
    </div>'''

def bridge(txt, dark=True):
    bdr = "rgba(30,197,242,0.30)"
    col = CYAN if dark else LIGHT_TEXT
    if not dark:
        col_italic = LIGHT_TEXT
    else:
        col_italic = CYAN
    return f'''<div style="padding-top:12px;border-top:1px solid {bdr};
      font-family:'Space Grotesk',sans-serif;font-style:italic;font-size:12.5px;
      font-weight:500;color:{col_italic};">{txt}</div>'''

GRAIN = '''<div style="position:absolute;inset:0;z-index:50;pointer-events:none;opacity:0.06;mix-blend-mode:overlay;background-image:url('data:image/svg+xml;utf8,<svg xmlns=%22http://www.w3.org/2000/svg%22 width=%22120%22 height=%22120%22><filter id=%22n%22><feTurbulence type=%22fractalNoise%22 baseFrequency=%220.9%22 numOctaves=%222%22/></filter><rect width=%22100%25%22 height=%22100%25%22 filter=%22url(%23n)%22/></svg>');background-size:180px 180px;"></div>'''

GRAIN_LIGHT = '''<div style="position:absolute;inset:0;z-index:50;pointer-events:none;opacity:0.035;mix-blend-mode:multiply;background-image:url('data:image/svg+xml;utf8,<svg xmlns=%22http://www.w3.org/2000/svg%22 width=%22120%22 height=%22120%22><filter id=%22n%22><feTurbulence type=%22fractalNoise%22 baseFrequency=%220.9%22 numOctaves=%222%22/></filter><rect width=%22100%25%22 height=%22100%25%22 filter=%22url(%23n)%22/></svg>');background-size:180px 180px;"></div>'''


# ── S1 IMPACTO (claro, capa) ────────────────────────────────────────────────
def s1():
    img = b64(GER / "sex_s1_mesa_premium.png")
    return f'''
<div style="width:{VW}px;height:{VH}px;position:relative;overflow:hidden;background:{LIGHT_BG};">
  <div style="position:absolute;inset:0;z-index:0;">
    <img src="{img}" style="width:100%;height:100%;object-fit:cover;filter:brightness(1.0) contrast(1.02);">
  </div>
  <div style="position:absolute;inset:0;z-index:1;
    background:linear-gradient(180deg, rgba(238,243,248,0.10) 0%, rgba(238,243,248,0.30) 40%, rgba(238,243,248,0.85) 70%, rgba(238,243,248,0.98) 100%);"></div>
  <div style="position:absolute;top:0;left:0;right:0;height:3px;background:{CYAN};z-index:10;"></div>
  {GRAIN_LIGHT}
  {logo(dark=False)}
  <div style="position:absolute;left:30px;right:30px;bottom:28px;z-index:20;">
    <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:700;
                font-size:36px;line-height:0.98;color:{LIGHT_TEXT};letter-spacing:-0.01em;">
      Marketing não conserta<br>
      empresa quebrada.<br>
      <span style="color:{CYAN};">Acelera o que já existe.</span>
    </div>
    <div style="font-family:'Space Grotesk',sans-serif;font-size:12.5px;font-weight:400;
                color:{LIGHT_SUB};line-height:1.6;margin-top:14px;max-width:340px;">
      Anúncio bom em operação fraca vira só mais cliente reclamando mais rápido.
    </div>
    <div style="margin-top:14px;">{bridge("A pergunta certa não é 'qual agência contratar?'.", dark=False)}</div>
  </div>
</div>'''


# ── S2 CONTEXTO (claro, foto + texto) ───────────────────────────────────────
def s2():
    img = b64(GER / "sex_s2_megafone_metafora.png")
    return f'''
<div style="width:{VW}px;height:{VH}px;position:relative;overflow:hidden;background:{LIGHT_BG};">
  <div style="position:absolute;left:0;top:0;bottom:0;width:48%;z-index:0;">
    <img src="{img}" style="width:100%;height:100%;object-fit:cover;">
    <div style="position:absolute;inset:0;background:linear-gradient(90deg, transparent 60%, {LIGHT_BG} 100%);"></div>
  </div>
  <div style="position:absolute;top:0;left:0;right:0;height:3px;background:{CYAN};z-index:10;"></div>
  {GRAIN_LIGHT}
  {logo(dark=False)}
  <div style="position:absolute;top:88px;left:50%;right:28px;z-index:20;">
    {kicker("A pergunta certa", dark=False)}
    <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:700;
                font-size:26px;line-height:1.02;color:{LIGHT_TEXT};">
      <span style="color:{CYAN};">"O que minha operação entrega bem hoje?"</span>
    </div>
    <div style="font-family:'Space Grotesk',sans-serif;font-size:11.5px;font-weight:400;
                color:{LIGHT_SUB};line-height:1.65;margin-top:18px;">
      Porque o marketing amplifica exatamente essa entrega. Se for boa, vira
      <span style="color:{LIGHT_TEXT};font-weight:600;">reputação.</span>
      Se for irregular, vira <span style="color:{LIGHT_TEXT};font-weight:600;">reclamação pública.</span>
    </div>
  </div>
  <div style="position:absolute;left:28px;right:28px;bottom:24px;z-index:20;">
    {bridge("Tem agência boa entregando resultado pra empresa errada.", dark=False)}
  </div>
</div>'''


# ── S3 SINTOMA (escuro — quebra de ritmo) ───────────────────────────────────
def s3():
    items = [
        ("01", "Nenhum padrão de atendimento documentado."),
        ("02", "Comercial improvisa preço por cliente."),
        ("03", "Pós-venda depende do dono."),
        ("04", "Métrica acompanhada é só faturamento."),
        ("05", "Não tem CRM nem planilha confiável."),
    ]
    cards = "".join(f'''
      <div style="display:flex;align-items:flex-start;gap:14px;padding:10px 0;
                  border-bottom:1px solid rgba(255,255,255,0.08);">
        <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:700;
                    font-size:20px;color:{CYAN};line-height:1;min-width:28px;">{n}</div>
        <div style="font-family:'Space Grotesk',sans-serif;font-size:12.5px;font-weight:500;
                    color:#fff;line-height:1.4;">{t}</div>
      </div>''' for n, t in items)
    return f'''
<div style="width:{VW}px;height:{VH}px;position:relative;overflow:hidden;background:{INK};">
  <div style="position:absolute;inset:0;z-index:0;
    background:radial-gradient(ellipse 70% 50% at 50% 25%, rgba(30,197,242,0.05) 0%, transparent 70%),
               radial-gradient(circle, rgba(255,255,255,0.018) 1px, transparent 1px);
    background-size:auto, 24px 24px;"></div>
  {GRAIN}
  {logo(dark=True)}
  <div style="position:absolute;top:88px;left:30px;right:30px;z-index:20;">
    {kicker("Você ainda não está pronto se...")}
    <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:700;
                font-size:26px;line-height:1.02;color:#fff;">
      Pelo menos <span style="color:{CYAN};">3 desses</span> são você:
    </div>
    <div style="margin-top:14px;">{cards}</div>
  </div>
  <div style="position:absolute;left:30px;right:30px;bottom:24px;z-index:20;">
    {bridge("Investir em marketing aqui é multiplicar o caos.")}
  </div>
</div>'''


# ── S4 CAUSA (claro, foto à direita) ────────────────────────────────────────
def s4():
    img = b64(GER / "sex_s4_promessa_entrega.png")
    return f'''
<div style="width:{VW}px;height:{VH}px;position:relative;overflow:hidden;background:{LIGHT_BG};">
  <div style="position:absolute;right:0;top:0;bottom:0;width:44%;z-index:0;">
    <img src="{img}" style="width:100%;height:100%;object-fit:cover;">
    <div style="position:absolute;inset:0;background:linear-gradient(270deg, transparent 60%, {LIGHT_BG} 100%);"></div>
  </div>
  <div style="position:absolute;top:0;left:0;right:0;height:3px;background:{CYAN};z-index:10;"></div>
  {GRAIN_LIGHT}
  {logo(dark=False)}
  <div style="position:absolute;top:88px;left:28px;right:48%;z-index:20;">
    {kicker("Por que isso acontece", dark=False)}
    <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:700;
                font-size:28px;line-height:0.98;color:{LIGHT_TEXT};">
      Todo marketing parte de uma <span style="color:{CYAN};">promessa.</span>
    </div>
    <div style="font-family:'Space Grotesk',sans-serif;font-size:11.5px;font-weight:400;
                color:{LIGHT_SUB};line-height:1.65;margin-top:16px;">
      E toda promessa precisa ser sustentada por uma operação que entrega.
      Quando a promessa é maior que a entrega,
      <span style="color:{LIGHT_TEXT};font-weight:600;">o crescimento vira problema reputacional.</span>
    </div>
  </div>
  <div style="position:absolute;left:28px;right:28px;bottom:24px;z-index:20;">
    {bridge("Daí vem a inversão que pouca gente faz.", dark=False)}
  </div>
</div>'''


# ── S5 CONSEQUÊNCIA (claro, número + foto fundo) ────────────────────────────
def s5():
    img = b64(GER / "sex_s5_dinheiro_perdido.png")
    return f'''
<div style="width:{VW}px;height:{VH}px;position:relative;overflow:hidden;background:{LIGHT_BG};">
  <div style="position:absolute;inset:0;z-index:0;">
    <img src="{img}" style="width:100%;height:100%;object-fit:cover;
         filter:brightness(1.05) contrast(0.95) saturate(0.80) blur(1.5px);">
  </div>
  <div style="position:absolute;inset:0;z-index:1;
    background:linear-gradient(180deg, rgba(238,243,248,0.85) 0%, rgba(238,243,248,0.55) 45%, rgba(238,243,248,0.95) 95%);"></div>
  <div style="position:absolute;top:0;left:0;right:0;height:3px;background:{CYAN};z-index:10;"></div>
  {GRAIN_LIGHT}
  {logo(dark=False)}
  <div style="position:absolute;top:84px;left:30px;right:30px;z-index:20;">
    {kicker("O custo de inverter", dark=False)}
    <div style="font-family:'Space Grotesk',sans-serif;font-size:13px;font-weight:600;
                color:{LIGHT_SUB};letter-spacing:0.02em;text-transform:uppercase;">
      Cada real investido sem base
    </div>
  </div>
  <div style="position:absolute;left:30px;right:30px;top:170px;z-index:20;
              display:flex;align-items:flex-start;gap:8px;">
    <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:700;
                font-size:130px;line-height:0.82;color:{CYAN};">R$</div>
    <div style="padding-top:0px;">
      <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:700;
                  font-size:130px;line-height:0.82;color:{LIGHT_TEXT};">100k</div>
    </div>
  </div>
  <div style="position:absolute;left:30px;right:30px;bottom:78px;z-index:20;">
    <div style="font-family:'Space Grotesk',sans-serif;font-size:12px;font-weight:400;
                color:{LIGHT_SUB};line-height:1.6;">
      em mídia vira <span style="color:{LIGHT_TEXT};font-weight:600;">ruído</span> quando a operação
      não converte. O lead chega, percebe a desorganização, e leva a sensação ruim adiante.
    </div>
  </div>
  <div style="position:absolute;left:30px;right:30px;bottom:24px;z-index:20;
              padding-top:12px;border-top:1px solid rgba(30,197,242,0.30);">
    <div style="font-family:'Space Grotesk',sans-serif;font-style:italic;font-size:12.5px;
                font-weight:500;color:{LIGHT_TEXT};">
      Por isso a NUC nasceu na outra ponta.
    </div>
  </div>
</div>'''


# ── S6 VIRADA (escuro respiro — quebra de ritmo) ────────────────────────────
def s6():
    return f'''
<div style="width:{VW}px;height:{VH}px;position:relative;overflow:hidden;background:{INK};">
  <div style="position:absolute;inset:0;z-index:0;
    background:radial-gradient(ellipse 70% 50% at 50% 40%, rgba(30,197,242,0.06) 0%, transparent 70%),
               radial-gradient(circle, rgba(255,255,255,0.02) 1px, transparent 1px);
    background-size:auto, 26px 26px;"></div>
  {GRAIN}
  {logo(dark=True)}
  <div style="position:absolute;inset:0;z-index:20;display:flex;flex-direction:column;
              align-items:center;justify-content:center;padding:64px 32px 32px;text-align:center;">
    <div style="display:flex;align-items:center;gap:8px;margin-bottom:22px;">
      <div style="width:18px;height:1.5px;background:{CYAN};"></div>
      <span style="font-family:'Space Grotesk',sans-serif;font-size:9px;font-weight:700;
                   letter-spacing:0.22em;text-transform:uppercase;color:{CYAN};">A inversão</span>
    </div>
    <div style="font-family:'Space Grotesk',sans-serif;font-size:14px;font-weight:500;
                color:rgba(255,255,255,0.45);line-height:1.4;margin-bottom:22px;
                text-decoration:line-through;text-decoration-thickness:1.5px;
                text-decoration-color:rgba(255,255,255,0.45);">
      Quando contrato agência?
    </div>
    <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:700;
                font-size:38px;line-height:1.02;color:#fff;max-width:340px;">
      Quando minha operação está <span style="color:{CYAN};">pronta para receber?</span>
    </div>
  </div>
  <div style="position:absolute;left:28px;right:28px;bottom:24px;z-index:20;">
    {bridge("Essa virada inverte a ordem do projeto inteiro.")}
  </div>
</div>'''


# ── S7 CAMINHO (claro, ordem certa + foto) ──────────────────────────────────
def s7():
    img = b64(GER / "sex_s7_ordem_certa.png")
    items = [
        ("Diagnóstico", "do núcleo da empresa."),
        ("Padronização", "do que entrega valor."),
        ("Promessa", "coerente com a entrega."),
        ("Estrutura", "comercial pronta para volume."),
        ("Marketing", "só agora, e como combustível."),
    ]
    cards = "".join(f'''
      <div style="display:flex;align-items:baseline;gap:10px;padding:8px 0;
                  border-bottom:1px solid {LIGHT_BORDER};">
        <div style="font-family:'Space Grotesk',sans-serif;font-size:9.5px;font-weight:700;
                    color:{CYAN};min-width:18px;">0{i+1}</div>
        <div>
          <span style="font-family:'Space Grotesk',sans-serif;font-size:12px;font-weight:700;
                       color:{LIGHT_TEXT};">{t}</span>
          <span style="font-family:'Space Grotesk',sans-serif;font-size:12px;font-weight:400;
                       color:{LIGHT_SUB};"> {s}</span>
        </div>
      </div>''' for i, (t, s) in enumerate(items))
    return f'''
<div style="width:{VW}px;height:{VH}px;position:relative;overflow:hidden;background:{LIGHT_BG};">
  <div style="position:absolute;right:0;top:0;bottom:0;width:36%;z-index:0;">
    <img src="{img}" style="width:100%;height:100%;object-fit:cover;">
    <div style="position:absolute;inset:0;background:linear-gradient(270deg, transparent 55%, {LIGHT_BG} 100%);"></div>
  </div>
  <div style="position:absolute;top:0;left:0;right:0;height:3px;background:{CYAN};z-index:10;"></div>
  {GRAIN_LIGHT}
  {logo(dark=False)}
  <div style="position:absolute;top:84px;left:28px;right:42%;z-index:20;">
    {kicker("A ordem certa", dark=False)}
    <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:700;
                font-size:24px;line-height:1.02;color:{LIGHT_TEXT};">
      <span style="color:{CYAN};">5 etapas</span> que antecedem a primeira campanha:
    </div>
  </div>
  <div style="position:absolute;top:228px;left:28px;right:28px;z-index:20;">
    {cards}
  </div>
  <div style="position:absolute;left:28px;right:28px;bottom:24px;z-index:20;">
    {bridge("Invertendo a ordem, marketing vira combustível, não risco.", dark=False)}
  </div>
</div>'''


# ── S8 CTA (Lucas, claro — variação clara do padrão V4) ─────────────────────
def s8():
    lucas = b64(FOTOS / "lucas_polo_nuc_cutout.png")
    return f'''
<div style="width:{VW}px;height:{VH}px;position:relative;overflow:hidden;
            background:radial-gradient(ellipse 60% 80% at 75% 60%, #DBE8F2 0%, {LIGHT_BG} 60%, #E2EAF1 100%);">
  <div style="position:absolute;inset:0;z-index:0;pointer-events:none;
    background-image:radial-gradient(circle,rgba(26,46,77,0.05) 1px,transparent 1px);
    background-size:24px 24px;"></div>
  <div style="position:absolute;right:-8%;bottom:0;width:75%;height:88%;z-index:5;
    background:radial-gradient(ellipse 60% 50% at 50% 35%, rgba(30,197,242,0.18) 0%, transparent 65%);
    filter:blur(20px);"></div>
  <div style="position:absolute;top:0;left:0;right:0;height:3px;background:{CYAN};z-index:10;"></div>

  <div style="position:absolute;right:-14%;bottom:0;height:100%;z-index:10;
              display:flex;align-items:flex-end;">
    <img src="{lucas}" style="height:100%;width:auto;display:block;
         filter:brightness(1.06) contrast(1.05) saturate(1.02)
                drop-shadow(0 8px 24px rgba(26,46,77,0.30))
                drop-shadow(0 0 18px rgba(30,197,242,0.18));">
  </div>

  {GRAIN_LIGHT}
  {logo(dark=False)}

  <div style="position:absolute;top:92px;left:28px;right:42%;z-index:20;">
    {kicker("NUC Vision", dark=False)}
    <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:700;
                font-size:28px;line-height:1.02;color:{LIGHT_TEXT};">
      Marketing vem depois.<br>
      <span style="color:{CYAN};">Sempre depois.</span>
    </div>
    <div style="font-family:'Space Grotesk',sans-serif;font-size:12px;font-weight:400;
                color:{LIGHT_SUB};line-height:1.6;margin-top:18px;">
      A NUC entra antes do marketing para deixar a empresa pronta para
      <span style="color:{LIGHT_TEXT};font-weight:600;">escalar com segurança.</span>
    </div>
  </div>

  <div style="position:absolute;left:0;right:0;bottom:0;z-index:30;
              background:{CYAN};padding:20px 26px;text-align:center;
              box-shadow:0 -10px 32px rgba(26,46,77,0.30);">
    <div style="font-family:'Space Grotesk',sans-serif;font-size:14px;font-weight:700;
                color:{INK};line-height:1.3;letter-spacing:0.005em;">
      Reconheceu sua empresa? Comenta <span style="font-weight:800;">NÚCLEO</span>
      <span style="font-weight:500;font-size:13px;">e a gente conversa.</span>
    </div>
  </div>
</div>'''


SLIDES = {
    "s1_impacto":      s1(),
    "s2_contexto":     s2(),
    "s3_sintoma":      s3(),
    "s4_causa":        s4(),
    "s5_consequencia": s5(),
    "s6_virada":       s6(),
    "s7_caminho":      s7(),
    "s8_cta":          s8(),
}

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
    print("✓ Concluído.")

asyncio.run(run())
