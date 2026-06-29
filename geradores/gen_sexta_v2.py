#!/usr/bin/env python3
"""Sexta v2 — Marketing não conserta operação. Metáforas conceituais, paleta variada."""
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
SEPIA_BG, SEPIA_TEXT = "#F2EBDC", "#3D2E1F"   # paleta complementar S2 porta no campo
TERRA = "#A0432A"  # acento terracota S5

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

def kicker(txt, color=None):
    c = color or CYAN
    return f'''<div style="display:flex;align-items:center;gap:8px;margin-bottom:14px;">
      <div style="width:18px;height:1.5px;background:{c};"></div>
      <span style="font-family:'Space Grotesk',sans-serif;font-size:9px;font-weight:700;
                   letter-spacing:0.22em;text-transform:uppercase;color:{c};">{txt}</span>
    </div>'''

def bridge(txt, color=None):
    c = color or CYAN
    return f'''<div style="padding-top:12px;border-top:1px solid {c}4D;
      font-family:'Space Grotesk',sans-serif;font-style:italic;font-size:12.5px;
      font-weight:500;color:{c};">{txt}</div>'''

GRAIN = '''<div style="position:absolute;inset:0;z-index:50;pointer-events:none;opacity:0.06;mix-blend-mode:overlay;background-image:url('data:image/svg+xml;utf8,<svg xmlns=%22http://www.w3.org/2000/svg%22 width=%22120%22 height=%22120%22><filter id=%22n%22><feTurbulence type=%22fractalNoise%22 baseFrequency=%220.9%22 numOctaves=%222%22/></filter><rect width=%22100%25%22 height=%22100%25%22 filter=%22url(%23n)%22/></svg>');background-size:180px 180px;"></div>'''

GRAIN_LIGHT = '''<div style="position:absolute;inset:0;z-index:50;pointer-events:none;opacity:0.035;mix-blend-mode:multiply;background-image:url('data:image/svg+xml;utf8,<svg xmlns=%22http://www.w3.org/2000/svg%22 width=%22120%22 height=%22120%22><filter id=%22n%22><feTurbulence type=%22fractalNoise%22 baseFrequency=%220.9%22 numOctaves=%222%22/></filter><rect width=%22100%25%22 height=%22100%25%22 filter=%22url(%23n)%22/></svg>');background-size:180px 180px;"></div>'''


# ── S1 IMPACTO — megafone vs castelo de cartas, claro ───────────────────────
def s1():
    img = b64(GER / "sex_s1_megafone_castelo.png")
    return f'''
<div style="width:{VW}px;height:{VH}px;position:relative;overflow:hidden;background:{LIGHT_BG};">
  <div style="position:absolute;inset:0;z-index:0;">
    <img src="{img}" style="width:100%;height:100%;object-fit:cover;filter:brightness(1.0) contrast(1.04);">
  </div>
  <div style="position:absolute;inset:0;z-index:1;
    background:linear-gradient(180deg, rgba(238,243,248,0.20) 0%, rgba(238,243,248,0.08) 35%, rgba(238,243,248,0.85) 72%, rgba(238,243,248,0.98) 100%);"></div>
  <div style="position:absolute;top:0;left:0;right:0;height:3px;background:{CYAN};z-index:10;"></div>
  {GRAIN_LIGHT}
  {logo(dark=False)}
  <div style="position:absolute;left:28px;right:28px;bottom:28px;z-index:20;">
    <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:700;
                font-size:46px;line-height:0.94;color:{LIGHT_TEXT};letter-spacing:-0.01em;">
      Marketing não<br>
      conserta empresa<br>
      <span style="color:{CYAN};">quebrada.</span>
    </div>
    <div style="font-family:'Space Grotesk',sans-serif;font-size:12.5px;font-weight:400;
                color:{LIGHT_SUB};line-height:1.6;margin-top:14px;max-width:340px;">
      Acelera o que já existe. Anúncio bom em operação fraca vira só mais cliente reclamando mais rápido.
    </div>
    <div style="margin-top:14px;">{bridge("A pergunta certa não é 'qual agência contratar?'.", color=LIGHT_TEXT)}</div>
  </div>
</div>'''


# ── S2 CONTEXTO — still life editorial claro ────────────────────────────────
def s2():
    img = b64(GER / "v3_s2_notebook_caderno.png")
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
    {kicker("A pergunta certa", color=LIGHT_TEXT)}
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
    {bridge("Tem agência boa entregando resultado pra empresa errada.", color=LIGHT_TEXT)}
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
                font-size:30px;line-height:1.0;color:#fff;">
      Pelo menos <span style="color:{CYAN};">3 desses</span><br>são você:
    </div>
    <div style="margin-top:14px;">{cards}</div>
  </div>
  <div style="position:absolute;left:30px;right:30px;bottom:24px;z-index:20;">
    {bridge("Investir em marketing aqui é multiplicar o caos.")}
  </div>
</div>'''


# ── S4 CAUSA — caixas contraste, claro ──────────────────────────────────────
def s4():
    img = b64(GER / "sex_s4_caixas_contraste.png")
    return f'''
<div style="width:{VW}px;height:{VH}px;position:relative;overflow:hidden;background:{LIGHT_BG};">
  <div style="position:absolute;inset:0;z-index:0;">
    <img src="{img}" style="width:100%;height:100%;object-fit:cover;filter:brightness(1.0) contrast(1.03);">
  </div>
  <div style="position:absolute;inset:0;z-index:1;
    background:linear-gradient(180deg, rgba(238,243,248,0.10) 0%, rgba(238,243,248,0.05) 35%, rgba(238,243,248,0.88) 72%, rgba(238,243,248,0.98) 100%);"></div>
  <div style="position:absolute;top:0;left:0;right:0;height:3px;background:{CYAN};z-index:10;"></div>
  {GRAIN_LIGHT}
  {logo(dark=False)}
  <div style="position:absolute;left:28px;right:28px;bottom:28px;z-index:20;">
    {kicker("Por que isso acontece", color=LIGHT_TEXT)}
    <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:700;
                font-size:38px;line-height:0.96;color:{LIGHT_TEXT};">
      Quando a <span style="color:{CYAN};">promessa</span><br>
      é maior que a<br>
      entrega.
    </div>
    <div style="font-family:'Space Grotesk',sans-serif;font-size:11.5px;font-weight:400;
                color:{LIGHT_SUB};line-height:1.6;margin-top:14px;max-width:340px;">
      Todo marketing parte de uma promessa. E toda promessa precisa de uma operação que entrega.
      <span style="color:{LIGHT_TEXT};font-weight:600;">Senão o crescimento vira problema reputacional.</span>
    </div>
    <div style="margin-top:14px;">{bridge("Daí vem a inversão que pouca gente faz.", color=LIGHT_TEXT)}</div>
  </div>
</div>'''


# ── S5 CONSEQUÊNCIA — dinheiro voando, paleta terracota/sépia ───────────────
def s5():
    img = b64(GER / "sex_s5_dinheiro_vento.png")
    return f'''
<div style="width:{VW}px;height:{VH}px;position:relative;overflow:hidden;background:{SEPIA_BG};">
  <div style="position:absolute;inset:0;z-index:0;">
    <img src="{img}" style="width:100%;height:100%;object-fit:cover;filter:brightness(1.02) contrast(1.06) saturate(0.92);">
  </div>
  <div style="position:absolute;inset:0;z-index:1;
    background:linear-gradient(180deg, rgba(242,235,220,0.10) 0%, rgba(242,235,220,0.10) 35%, rgba(242,235,220,0.90) 72%, rgba(242,235,220,0.98) 100%);"></div>
  <div style="position:absolute;top:0;left:0;right:0;height:3px;background:{TERRA};z-index:10;"></div>
  {GRAIN_LIGHT}
  {logo(dark=False)}
  <div style="position:absolute;left:28px;right:28px;bottom:28px;z-index:20;">
    {kicker("O custo de inverter", color=TERRA)}
    <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:700;
                font-size:46px;line-height:0.94;color:{SEPIA_TEXT};">
      Cada real vira<br>
      <span style="color:{TERRA};">ruído.</span>
    </div>
    <div style="font-family:'Space Grotesk',sans-serif;font-size:12px;font-weight:400;
                color:rgba(61,46,31,0.78);line-height:1.6;margin-top:14px;max-width:340px;">
      Quando a operação não converte, o lead chega, percebe a desorganização e
      <span style="color:{SEPIA_TEXT};font-weight:600;">leva a sensação ruim adiante.</span>
    </div>
    <div style="margin-top:14px;">{bridge("Por isso a NUC nasceu na outra ponta.", color=TERRA)}</div>
  </div>
</div>'''


# ── S6 VIRADA (escuro respiro) ──────────────────────────────────────────────
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
    {kicker("A inversão")}
    <div style="font-family:'Space Grotesk',sans-serif;font-size:14px;font-weight:500;
                color:rgba(255,255,255,0.45);line-height:1.4;margin-bottom:22px;
                text-decoration:line-through;text-decoration-thickness:1.5px;
                text-decoration-color:rgba(255,255,255,0.45);">
      Quando contrato agência?
    </div>
    <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:700;
                font-size:40px;line-height:1.0;color:#fff;max-width:340px;">
      Quando minha operação<br>
      está <span style="color:{CYAN};">pronta para receber?</span>
    </div>
  </div>
  <div style="position:absolute;left:28px;right:28px;bottom:24px;z-index:20;">
    {bridge("Essa virada inverte a ordem do projeto inteiro.")}
  </div>
</div>'''


# ── S7 CAMINHO — still life editorial blocos alinhados, claro ───────────────
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
                  border-bottom:1px solid rgba(26,46,77,0.10);">
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
  <div style="position:absolute;right:0;top:0;bottom:0;width:38%;z-index:0;">
    <img src="{img}" style="width:100%;height:100%;object-fit:cover;">
    <div style="position:absolute;inset:0;background:linear-gradient(270deg, transparent 55%, {LIGHT_BG} 100%);"></div>
  </div>
  <div style="position:absolute;top:0;left:0;right:0;height:3px;background:{CYAN};z-index:10;"></div>
  {GRAIN_LIGHT}
  {logo(dark=False)}
  <div style="position:absolute;top:84px;left:28px;right:42%;z-index:20;">
    {kicker("A ordem certa", color=LIGHT_TEXT)}
    <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:700;
                font-size:26px;line-height:1.0;color:{LIGHT_TEXT};">
      <span style="color:{CYAN};">5 etapas</span> antes da<br>primeira campanha:
    </div>
  </div>
  <div style="position:absolute;top:232px;left:28px;right:28px;z-index:20;">
    {cards}
  </div>
  <div style="position:absolute;left:28px;right:28px;bottom:24px;z-index:20;
              padding-top:12px;border-top:1px solid rgba(30,197,242,0.30);">
    <div style="font-family:'Space Grotesk',sans-serif;font-style:italic;font-size:12.5px;
                font-weight:500;color:{LIGHT_TEXT};">
      Invertendo a ordem, marketing vira combustível, não risco.
    </div>
  </div>
</div>'''


# ── S8 CTA — Lucas (já corrigido) ───────────────────────────────────────────
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

  <div style="position:absolute;right:-32%;bottom:64px;height:84%;z-index:10;
              display:flex;align-items:flex-end;">
    <img src="{lucas}" style="height:100%;width:auto;display:block;
         filter:brightness(1.06) contrast(1.05) saturate(1.02)
                drop-shadow(0 8px 24px rgba(26,46,77,0.30))
                drop-shadow(0 0 18px rgba(30,197,242,0.18));">
  </div>

  {GRAIN_LIGHT}
  {logo(dark=False)}

  <div style="position:absolute;top:92px;left:28px;right:48%;z-index:20;">
    {kicker("NUC Vision", color=LIGHT_TEXT)}
    <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:700;
                font-size:28px;line-height:1.02;color:{LIGHT_TEXT};">
      Marketing vem<br>depois.<br>
      <span style="color:{CYAN};">Sempre depois.</span>
    </div>
    <div style="font-family:'Space Grotesk',sans-serif;font-size:11.5px;font-weight:400;
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
