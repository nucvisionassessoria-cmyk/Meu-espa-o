#!/usr/bin/env python3
"""Carrossel completo v3 — Segunda — 8 slides com layouts variados e pontes costuradas."""
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

def kicker(txt, dark=True):
    c = CYAN
    return f'''<div style="display:flex;align-items:center;gap:8px;margin-bottom:14px;">
      <div style="width:18px;height:1.5px;background:{c};"></div>
      <span style="font-family:'Space Grotesk',sans-serif;font-size:9px;font-weight:700;
                   letter-spacing:0.22em;text-transform:uppercase;color:{c};">{txt}</span>
    </div>'''

def bridge(txt, dark=True):
    bdr = "rgba(30,197,242,0.30)"
    col = CYAN
    return f'''<div style="padding-top:12px;border-top:1px solid {bdr};
      font-family:'Space Grotesk',sans-serif;font-style:italic;font-size:12.5px;
      font-weight:500;color:{col};">{txt}</div>'''

GRAIN = '''<div style="position:absolute;inset:0;z-index:50;pointer-events:none;opacity:0.06;mix-blend-mode:overlay;background-image:url('data:image/svg+xml;utf8,<svg xmlns=%22http://www.w3.org/2000/svg%22 width=%22120%22 height=%22120%22><filter id=%22n%22><feTurbulence type=%22fractalNoise%22 baseFrequency=%220.9%22 numOctaves=%222%22/></filter><rect width=%22100%25%22 height=%22100%25%22 filter=%22url(%23n)%22/></svg>');background-size:180px 180px;"></div>'''

GRAIN_LIGHT = '''<div style="position:absolute;inset:0;z-index:50;pointer-events:none;opacity:0.035;mix-blend-mode:multiply;background-image:url('data:image/svg+xml;utf8,<svg xmlns=%22http://www.w3.org/2000/svg%22 width=%22120%22 height=%22120%22><filter id=%22n%22><feTurbulence type=%22fractalNoise%22 baseFrequency=%220.9%22 numOctaves=%222%22/></filter><rect width=%22100%25%22 height=%22100%25%22 filter=%22url(%23n)%22/></svg>');background-size:180px 180px;"></div>'''


# ── S1 IMPACTO ───────────────────────────────────────────────────────────────
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
    <div style="margin-top:14px;">{bridge("Está no que acontece depois.")}</div>
  </div>
</div>'''


# ── S2 CONTEXTO (claro) ──────────────────────────────────────────────────────
def s2():
    img = b64("v3_s2_notebook_caderno.png")
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
    {kicker("O que ninguém olha")}
    <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:700;
                font-size:28px;line-height:1.0;color:{LIGHT_TEXT};">
      Depois do interesse,<br>é onde quase toda<br>venda <span style="color:{CYAN};">morre.</span>
    </div>
    <div style="font-family:'Space Grotesk',sans-serif;font-size:12px;font-weight:400;
                color:{LIGHT_SUB};line-height:1.65;margin-top:18px;">
      O cliente chama, demonstra curiosidade, pede informação. E nesse intervalo entre o
      <span style="color:{LIGHT_TEXT};font-weight:600;">"tenho interesse"</span> e o
      <span style="color:{LIGHT_TEXT};font-weight:600;">"fechei"</span>, a empresa começa a
      perder dinheiro sem perceber.
    </div>
  </div>
  <div style="position:absolute;left:28px;right:28px;bottom:24px;z-index:20;">
    {bridge("E esse vazamento tem etapas claras.", dark=False)}
  </div>
</div>'''


# ── S3 SINTOMA (escuro, lista, sem foto) ─────────────────────────────────────
def s3():
    items = [
        ("01", "O cliente chama."),
        ("02", "A resposta demora horas. Ou um dia."),
        ("03", "O atendimento muda conforme quem responde."),
        ("04", "O follow-up depende da memória de alguém."),
        ("05", "O lead esfria antes de virar proposta."),
    ]
    cards = "".join(f'''
      <div style="display:flex;align-items:flex-start;gap:14px;padding:12px 0;
                  border-bottom:1px solid rgba(255,255,255,0.08);">
        <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:700;
                    font-size:22px;color:{CYAN};line-height:1;min-width:30px;">{n}</div>
        <div style="font-family:'Space Grotesk',sans-serif;font-size:13.5px;font-weight:500;
                    color:#fff;line-height:1.4;">{t}</div>
      </div>''' for n, t in items)
    return f'''
<div style="width:{VW}px;height:{VH}px;position:relative;overflow:hidden;background:{INK};">
  <div style="position:absolute;inset:0;z-index:0;
    background:radial-gradient(ellipse 70% 50% at 50% 30%, rgba(30,197,242,0.05) 0%, transparent 70%),
               radial-gradient(circle, rgba(255,255,255,0.018) 1px, transparent 1px);
    background-size:auto, 24px 24px;"></div>
  {GRAIN}
  {logo(dark=True)}
  <div style="position:absolute;top:88px;left:30px;right:30px;z-index:20;">
    {kicker("Onde o lead morre")}
    <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:700;
                font-size:30px;line-height:1.0;color:#fff;">
      São <span style="color:{CYAN};">essas</span> etapas:
    </div>
    <div style="margin-top:14px;">{cards}</div>
  </div>
  <div style="position:absolute;left:30px;right:30px;bottom:24px;z-index:20;">
    {bridge("Nada disso é falta de cliente. É outra coisa.")}
  </div>
</div>'''


# ── S4 CAUSA (claro, foto post-its à direita) ────────────────────────────────
def s4():
    img = b64("v3_s4_postits.png")
    return f'''
<div style="width:{VW}px;height:{VH}px;position:relative;overflow:hidden;background:{LIGHT_BG};">
  <div style="position:absolute;right:0;top:0;bottom:0;width:42%;z-index:0;">
    <img src="{img}" style="width:100%;height:100%;object-fit:cover;">
    <div style="position:absolute;inset:0;background:linear-gradient(270deg, transparent 65%, {LIGHT_BG} 100%);"></div>
  </div>
  <div style="position:absolute;top:0;left:0;right:0;height:3px;background:{CYAN};z-index:10;"></div>
  {GRAIN_LIGHT}
  {logo(dark=False)}
  <div style="position:absolute;top:88px;left:28px;right:46%;z-index:20;">
    {kicker("Por que isso acontece")}
    <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:700;
                font-size:32px;line-height:0.95;color:{LIGHT_TEXT};">
      É falta de<br><span style="color:{CYAN};">processo.</span>
    </div>
    <div style="margin-top:20px;display:flex;flex-direction:column;gap:14px;">
      <div>
        <div style="font-family:'Space Grotesk',sans-serif;font-size:11.5px;font-weight:700;
                    color:{LIGHT_TEXT};line-height:1.3;">Sem rotina,</div>
        <div style="font-family:'Space Grotesk',sans-serif;font-size:11.5px;font-weight:400;
                    color:{LIGHT_SUB};line-height:1.4;">cada conversa começa do zero.</div>
      </div>
      <div>
        <div style="font-family:'Space Grotesk',sans-serif;font-size:11.5px;font-weight:700;
                    color:{LIGHT_TEXT};line-height:1.3;">Sem padrão,</div>
        <div style="font-family:'Space Grotesk',sans-serif;font-size:11.5px;font-weight:400;
                    color:{LIGHT_SUB};line-height:1.4;">cada pessoa atende de um jeito.</div>
      </div>
      <div>
        <div style="font-family:'Space Grotesk',sans-serif;font-size:11.5px;font-weight:700;
                    color:{LIGHT_TEXT};line-height:1.3;">Sem acompanhamento,</div>
        <div style="font-family:'Space Grotesk',sans-serif;font-size:11.5px;font-weight:400;
                    color:{LIGHT_SUB};line-height:1.4;">a oportunidade esfria sozinha.</div>
      </div>
    </div>
  </div>
  <div style="position:absolute;left:28px;right:28px;bottom:24px;z-index:20;">
    {bridge("Quando isso vira regra, quem segura tudo é uma pessoa só.", dark=False)}
  </div>
</div>'''


# ── S5 CONSEQUÊNCIA (escuro, número gigante + foto desfocada de fundo) ──────
def s5():
    img = b64("v3_s5_sobrecarga.png")
    return f'''
<div style="width:{VW}px;height:{VH}px;position:relative;overflow:hidden;background:{INK};">
  <div style="position:absolute;inset:0;z-index:0;">
    <img src="{img}" style="width:100%;height:100%;object-fit:cover;
         filter:brightness(0.40) contrast(1.10) saturate(0.65) blur(2px);">
  </div>
  <div style="position:absolute;inset:0;z-index:1;
    background:linear-gradient(180deg, rgba(6,9,15,0.78) 0%, rgba(6,9,15,0.40) 50%, rgba(6,9,15,0.92) 100%);"></div>
  {GRAIN}
  {logo(dark=True)}
  <div style="position:absolute;top:84px;left:30px;right:30px;z-index:20;">
    {kicker("O custo invisível")}
    <div style="font-family:'Space Grotesk',sans-serif;font-size:14px;font-weight:600;
                color:rgba(255,255,255,0.80);letter-spacing:0.02em;text-transform:uppercase;">
      Você.
    </div>
  </div>
  <div style="position:absolute;left:30px;right:30px;top:170px;z-index:20;
              display:flex;align-items:flex-start;gap:18px;">
    <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:700;
                font-size:160px;line-height:0.8;color:{CYAN};
                text-shadow:0 0 60px rgba(30,197,242,0.30);">1</div>
    <div style="padding-top:42px;">
      <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:700;
                  font-size:24px;line-height:1.0;color:#fff;">
        pessoa segurando<br>a empresa inteira.
      </div>
    </div>
  </div>
  <div style="position:absolute;left:30px;right:30px;bottom:78px;z-index:20;">
    <div style="font-family:'Space Grotesk',sans-serif;font-size:12px;font-weight:400;
                color:rgba(255,255,255,0.75);line-height:1.6;">
      Cada novo cliente vira mais uma cobrança, mais uma decisão, mais um pedido na sua cabeça.
      Mais demanda não trouxe crescimento. <span style="color:#fff;font-weight:600;">Trouxe peso.</span>
    </div>
  </div>
  <div style="position:absolute;left:30px;right:30px;bottom:24px;z-index:20;">
    {bridge("Talvez a pergunta que você está fazendo seja a errada.")}
  </div>
</div>'''


# ── S6 VIRADA (claro, respiro, pergunta riscada) ─────────────────────────────
def s6():
    return f'''
<div style="width:{VW}px;height:{VH}px;position:relative;overflow:hidden;background:{LIGHT_BG};">
  <div style="position:absolute;inset:0;z-index:1;pointer-events:none;
    background-image:radial-gradient(circle,rgba(26,46,77,0.055) 1px,transparent 1px);
    background-size:28px 28px;"></div>
  <div style="position:absolute;top:0;left:0;right:0;height:3px;background:{CYAN};z-index:10;"></div>
  {GRAIN_LIGHT}
  {logo(dark=False)}
  <div style="position:absolute;inset:0;z-index:20;display:flex;flex-direction:column;
              align-items:center;justify-content:center;padding:64px 32px 32px;text-align:center;">
    {kicker("A pergunta certa")}
    <div style="font-family:'Space Grotesk',sans-serif;font-size:14px;font-weight:500;
                color:rgba(26,46,77,0.45);line-height:1.4;margin-bottom:24px;
                text-decoration:line-through;text-decoration-thickness:1.5px;
                text-decoration-color:rgba(26,46,77,0.45);">
      Como atrair mais clientes?
    </div>
    <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:700;
                font-size:40px;line-height:1.02;color:{LIGHT_TEXT};max-width:340px;">
      Onde estamos<br>
      <span style="color:{CYAN};">desperdiçando</span><br>
      os que já chegam?
    </div>
  </div>
  <div style="position:absolute;left:28px;right:28px;bottom:24px;z-index:20;">
    {bridge("Essa pergunta muda a ordem das coisas.", dark=False)}
  </div>
</div>'''


# ── S7 CAMINHO (escuro, checklist editorial + foto à direita) ───────────────
def s7():
    img = b64("v3_s7_notebook_fechado.png")
    items = [
        ("Tempo de resposta", "defina um padrão."),
        ("Roteiro de atendimento", "pare de improvisar."),
        ("Responsável claro", "por cada etapa."),
        ("CRM simples", "registrando tudo."),
        ("Próximo passo definido", "em toda conversa."),
    ]
    cards = "".join(f'''
      <div style="display:flex;align-items:baseline;gap:10px;padding:8px 0;
                  border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="font-family:'Space Grotesk',sans-serif;font-size:9.5px;font-weight:700;
                    color:{CYAN};min-width:18px;">0{i+1}</div>
        <div>
          <span style="font-family:'Space Grotesk',sans-serif;font-size:12px;font-weight:700;
                       color:#fff;">{t}</span>
          <span style="font-family:'Space Grotesk',sans-serif;font-size:12px;font-weight:400;
                       color:rgba(255,255,255,0.65);"> {s}</span>
        </div>
      </div>''' for i, (t, s) in enumerate(items))
    return f'''
<div style="width:{VW}px;height:{VH}px;position:relative;overflow:hidden;background:{INK2};">
  <div style="position:absolute;right:0;top:0;bottom:0;width:38%;z-index:0;">
    <img src="{img}" style="width:100%;height:100%;object-fit:cover;
         filter:brightness(0.55) contrast(1.08) saturate(0.75);">
    <div style="position:absolute;inset:0;background:linear-gradient(270deg, transparent 55%, {INK2} 100%);"></div>
  </div>
  {GRAIN}
  {logo(dark=True)}
  <div style="position:absolute;top:84px;left:28px;right:42%;z-index:20;">
    {kicker("Estrutura antes de demanda")}
    <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:700;
                font-size:26px;line-height:1.0;color:#fff;">
      Antes de aumentar tráfego,<br>
      organize <span style="color:{CYAN};">5 coisas:</span>
    </div>
  </div>
  <div style="position:absolute;top:228px;left:28px;right:28px;z-index:20;">
    {cards}
  </div>
  <div style="position:absolute;left:28px;right:28px;bottom:24px;z-index:20;">
    {bridge("Com isso pronto, cada lead que entra começa a render de verdade.")}
  </div>
</div>'''


# ── S8 FECHAMENTO + CTA (humano — Iago sócio NUC) ───────────────────────────
def s8():
    iago = f"data:image/png;base64,{base64.b64encode(Path('/home/user/Meu-espa-o/fotos/iago_cutout.png').read_bytes()).decode()}"
    return f'''
<div style="width:{VW}px;height:{VH}px;position:relative;overflow:hidden;
            background:radial-gradient(ellipse 60% 80% at 75% 60%, #0d2540 0%, {INK} 60%, #03060c 100%);">
  <div style="position:absolute;inset:0;z-index:0;pointer-events:none;
    background-image:radial-gradient(circle,rgba(255,255,255,0.022) 1px,transparent 1px);
    background-size:24px 24px;"></div>
  <div style="position:absolute;right:-8%;bottom:0;width:75%;height:88%;z-index:5;
    background:radial-gradient(ellipse 60% 50% at 50% 35%, rgba(30,197,242,0.25) 0%, transparent 65%);
    filter:blur(20px);"></div>

  <div style="position:absolute;right:-12%;bottom:-2%;height:90%;z-index:10;">
    <img src="{iago}" style="height:100%;width:auto;
         filter:brightness(1.02) contrast(1.06) saturate(1.02)
                drop-shadow(0 8px 24px rgba(0,0,0,0.6))
                drop-shadow(0 0 18px rgba(30,197,242,0.20));">
  </div>

  <div style="position:absolute;right:8%;bottom:8%;width:55%;height:12%;z-index:9;
    background:radial-gradient(closest-side, rgba(0,0,0,0.55), transparent 75%);
    filter:blur(14px);"></div>

  {GRAIN}
  {logo(dark=True)}

  <div style="position:absolute;top:88px;left:28px;right:52%;z-index:20;">
    {kicker("NUC Vision")}
    <div style="font-family:'Space Grotesk',sans-serif;font-size:12px;font-weight:600;
                color:rgba(255,255,255,0.72);letter-spacing:0.02em;text-transform:uppercase;
                margin-bottom:14px;">
      E aí o jogo muda.
    </div>
    <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:700;
                font-size:32px;line-height:0.98;color:#fff;">
      Crescer não é só<br>
      atrair mais.<br>
      É <span style="color:{CYAN};">desperdiçar<br>menos.</span>
    </div>
    <div style="font-family:'Space Grotesk',sans-serif;font-size:11.5px;font-weight:400;
                color:rgba(255,255,255,0.78);line-height:1.6;margin-top:18px;">
      A NUC entra <span style="color:#fff;font-weight:600;">antes</span> do marketing,
      organiza o núcleo da empresa e prepara a operação para receber, conduzir e converter o que já chega.
    </div>
  </div>

  <div style="position:absolute;left:28px;bottom:32px;z-index:20;width:48%;">
    <div style="font-family:'Space Grotesk',sans-serif;font-size:9px;font-weight:700;
                letter-spacing:0.18em;text-transform:uppercase;color:rgba(255,255,255,0.45);
                margin-bottom:8px;">
      Iago · Sócio
    </div>
    <div style="background:{CYAN};color:{INK};font-family:'Space Grotesk',sans-serif;
                font-size:10.5px;font-weight:700;letter-spacing:0.10em;text-transform:uppercase;
                padding:13px 16px;border-radius:999px;text-align:center;
                box-shadow:0 6px 22px rgba(30,197,242,0.40);">
      Diagnóstico · @nucvision
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
