#!/usr/bin/env python3
"""Quarta — 'O dono virou o gargalo' — 8 slides escuros + Derick no S8."""
import sys, base64, asyncio
from pathlib import Path
sys.path.insert(0, "/home/user/Meu-espa-o")
from design_system import LOGO_URI
from playwright.async_api import async_playwright

FOTOS  = Path("/home/user/Meu-espa-o/fotos")
GER    = Path("/home/user/Meu-espa-o/fotos/geradas")
OUTPUT = Path("/home/user/Meu-espa-o/output/quarta-gargalo")
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

def bridge(txt):
    return f'''<div style="padding-top:12px;border-top:1px solid rgba(30,197,242,0.30);
      font-family:'Space Grotesk',sans-serif;font-style:italic;font-size:12.5px;
      font-weight:500;color:{CYAN};">{txt}</div>'''

GRAIN = '''<div style="position:absolute;inset:0;z-index:50;pointer-events:none;opacity:0.06;mix-blend-mode:overlay;background-image:url('data:image/svg+xml;utf8,<svg xmlns=%22http://www.w3.org/2000/svg%22 width=%22120%22 height=%22120%22><filter id=%22n%22><feTurbulence type=%22fractalNoise%22 baseFrequency=%220.9%22 numOctaves=%222%22/></filter><rect width=%22100%25%22 height=%22100%25%22 filter=%22url(%23n)%22/></svg>');background-size:180px 180px;"></div>'''

GRAIN_LIGHT = '''<div style="position:absolute;inset:0;z-index:50;pointer-events:none;opacity:0.035;mix-blend-mode:multiply;background-image:url('data:image/svg+xml;utf8,<svg xmlns=%22http://www.w3.org/2000/svg%22 width=%22120%22 height=%22120%22><filter id=%22n%22><feTurbulence type=%22fractalNoise%22 baseFrequency=%220.9%22 numOctaves=%222%22/></filter><rect width=%22100%25%22 height=%22100%25%22 filter=%22url(%23n)%22/></svg>');background-size:180px 180px;"></div>'''


# ── S1 IMPACTO ───────────────────────────────────────────────────────────────
def s1():
    img = b64(GER / "qua_s1_dono_homem.png")
    return f'''
<div style="width:{VW}px;height:{VH}px;position:relative;overflow:hidden;background:{INK};">
  <div style="position:absolute;inset:0;z-index:0;">
    <img src="{img}" style="width:100%;height:100%;object-fit:cover;filter:brightness(0.72) contrast(1.08) saturate(0.90);">
  </div>
  <div style="position:absolute;inset:0;z-index:1;
    background:linear-gradient(180deg, rgba(6,9,15,0.20) 0%, rgba(6,9,15,0.10) 35%, rgba(6,9,15,0.60) 65%, rgba(6,9,15,0.96) 100%);"></div>
  {GRAIN}
  {logo(dark=True)}
  <div style="position:absolute;left:30px;right:30px;bottom:28px;z-index:20;">
    <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:700;
                font-size:38px;line-height:1.0;color:#fff;letter-spacing:-0.01em;
                text-shadow:0 2px 18px rgba(0,0,0,0.55);">
      Sua empresa não cresce<br>
      porque você é <span style="color:{CYAN};">bom demais.</span>
    </div>
    <div style="font-family:'Space Grotesk',sans-serif;font-size:12.5px;font-weight:400;
                color:rgba(255,255,255,0.80);line-height:1.55;margin-top:14px;max-width:340px;">
      Você acha que é dedicação, provavelmente virou dependência.
    </div>
    <div style="margin-top:14px;">{bridge("É um problema antes de ser uma virtude.")}</div>
  </div>
</div>'''


# ── S2 CONTEXTO ──────────────────────────────────────────────────────────────
def s2():
    img = b64(GER / "qua_s2_panorama_empresa.png")
    return f'''
<div style="width:{VW}px;height:{VH}px;position:relative;overflow:hidden;background:{INK};">
  <div style="position:absolute;left:0;top:0;bottom:0;width:48%;z-index:0;">
    <img src="{img}" style="width:100%;height:100%;object-fit:cover;filter:brightness(0.65) contrast(1.05) saturate(0.85);">
    <div style="position:absolute;inset:0;background:linear-gradient(90deg, transparent 55%, {INK} 100%);"></div>
  </div>
  {GRAIN}
  {logo(dark=True)}
  <div style="position:absolute;top:88px;left:50%;right:28px;z-index:20;">
    {kicker("O padrão")}
    <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:700;
                font-size:26px;line-height:1.02;color:#fff;">
      Em toda empresa que para de crescer, tem <span style="color:{CYAN};">uma pessoa</span> que carrega tudo.
    </div>
    <div style="font-family:'Space Grotesk',sans-serif;font-size:12px;font-weight:400;
                color:rgba(255,255,255,0.80);line-height:1.65;margin-top:18px;">
      É ela quem aprova proposta, atende cliente difícil, resolve crise, lembra prazo, decide preço.
      <span style="color:#fff;font-weight:600;">E quase sempre é o dono.</span>
    </div>
  </div>
  <div style="position:absolute;left:28px;right:28px;bottom:24px;z-index:20;">
    {bridge("O problema começa quando essa pessoa não consegue mais soltar.")}
  </div>
</div>'''


# ── S3 SINTOMA (lista escura) ────────────────────────────────────────────────
def s3():
    items = [
        ("01", "Nenhuma decisão sai sem passar por você."),
        ("02", "Os colaboradores te pedem orientação até pro óbvio."),
        ("03", "Quando você viaja, as vendas caem."),
        ("04", "Você não tira 1 dia sem responder mensagem."),
        ("05", "Toda crise volta pro seu colo."),
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
    {kicker("Você é o gargalo se...")}
    <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:700;
                font-size:26px;line-height:1.02;color:#fff;">
      Pelo menos <span style="color:{CYAN};">3 desses</span> são você:
    </div>
    <div style="margin-top:14px;">{cards}</div>
  </div>
  <div style="position:absolute;left:30px;right:30px;bottom:24px;z-index:20;">
    {bridge("Isso não é dedicação. É concentração de poder por falta de processo.")}
  </div>
</div>'''


# ── S4 CAUSA (claro — quebra de ritmo) ──────────────────────────────────────
def s4():
    img = b64(GER / "qua_s4_agenda_lotada.png")
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
    <div style="display:flex;align-items:center;gap:8px;margin-bottom:14px;">
      <div style="width:18px;height:1.5px;background:{CYAN};"></div>
      <span style="font-family:'Space Grotesk',sans-serif;font-size:9px;font-weight:700;
                   letter-spacing:0.22em;text-transform:uppercase;color:{CYAN};">A causa real</span>
    </div>
    <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:700;
                font-size:30px;line-height:0.98;color:{LIGHT_TEXT};">
      Falta divisão clara de <span style="color:{CYAN};">responsabilidade.</span>
    </div>
    <div style="font-family:'Space Grotesk',sans-serif;font-size:11.5px;font-weight:400;
                color:{LIGHT_SUB};line-height:1.65;margin-top:16px;">
      Time pode até trabalhar bem, mas se ninguém é dono de etapa nenhuma, qualquer
      travamento volta pra cima de uma única pessoa.
      <span style="color:{LIGHT_TEXT};font-weight:600;">E essa pessoa é sempre quem fundou.</span>
    </div>
  </div>
  <div style="position:absolute;left:28px;right:28px;bottom:24px;z-index:20;
              padding-top:12px;border-top:1px solid rgba(30,197,242,0.30);">
    <div style="font-family:'Space Grotesk',sans-serif;font-style:italic;font-size:12.5px;
                font-weight:500;color:{LIGHT_TEXT};">
      Quanto mais a empresa cresce assim, mais o dono trabalha.
    </div>
  </div>
</div>'''


# ── S5 CONSEQUÊNCIA (escuro, número gigante) ────────────────────────────────
def s5():
    img = b64(GER / "qua_s5_sombra_dono.png")
    return f'''
<div style="width:{VW}px;height:{VH}px;position:relative;overflow:hidden;background:{INK};">
  <div style="position:absolute;inset:0;z-index:0;">
    <img src="{img}" style="width:100%;height:100%;object-fit:cover;
         filter:brightness(0.36) contrast(1.10) saturate(0.62) blur(2px);">
  </div>
  <div style="position:absolute;inset:0;z-index:1;
    background:linear-gradient(180deg, rgba(6,9,15,0.78) 0%, rgba(6,9,15,0.40) 50%, rgba(6,9,15,0.92) 100%);"></div>
  {GRAIN}
  {logo(dark=True)}
  <div style="position:absolute;top:84px;left:30px;right:30px;z-index:20;">
    {kicker("O efeito invisível")}
    <div style="font-family:'Space Grotesk',sans-serif;font-size:13px;font-weight:600;
                color:rgba(255,255,255,0.80);letter-spacing:0.02em;text-transform:uppercase;">
      Quando o dono falta
    </div>
  </div>
  <div style="position:absolute;left:30px;right:30px;top:165px;z-index:20;
              display:flex;align-items:flex-start;gap:18px;">
    <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:700;
                font-size:160px;line-height:0.82;color:{CYAN};
                text-shadow:0 0 60px rgba(30,197,242,0.30);">1</div>
    <div style="padding-top:42px;">
      <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:700;
                  font-size:24px;line-height:1.0;color:#fff;">
        ausência basta<br>para a operação<br>parar.
      </div>
    </div>
  </div>
  <div style="position:absolute;left:30px;right:30px;bottom:78px;z-index:20;">
    <div style="font-family:'Space Grotesk',sans-serif;font-size:12px;font-weight:400;
                color:rgba(255,255,255,0.78);line-height:1.6;">
      Não é porque o time é ruim. É porque a empresa nunca foi feita para
      <span style="color:#fff;font-weight:600;">funcionar sem você.</span>
    </div>
  </div>
  <div style="position:absolute;left:30px;right:30px;bottom:24px;z-index:20;">
    {bridge("E aí o crescimento vira o inimigo.")}
  </div>
</div>'''


# ── S6 VIRADA (claro respiro) ───────────────────────────────────────────────
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
    <div style="display:flex;align-items:center;gap:8px;margin-bottom:22px;">
      <div style="width:18px;height:1.5px;background:{CYAN};"></div>
      <span style="font-family:'Space Grotesk',sans-serif;font-size:9px;font-weight:700;
                   letter-spacing:0.22em;text-transform:uppercase;color:{CYAN};">A nova pergunta</span>
    </div>
    <div style="font-family:'Space Grotesk',sans-serif;font-size:14px;font-weight:500;
                color:rgba(26,46,77,0.45);line-height:1.4;margin-bottom:22px;
                text-decoration:line-through;text-decoration-thickness:1.5px;
                text-decoration-color:rgba(26,46,77,0.45);">
      Como produzir mais?
    </div>
    <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:700;
                font-size:40px;line-height:1.02;color:{LIGHT_TEXT};max-width:340px;">
      Como <span style="color:{CYAN};">sair</span> do centro<br>
      da operação?
    </div>
  </div>
  <div style="position:absolute;left:28px;right:28px;bottom:24px;z-index:20;
              padding-top:12px;border-top:1px solid rgba(30,197,242,0.30);">
    <div style="font-family:'Space Grotesk',sans-serif;font-style:italic;font-size:12.5px;
                font-weight:500;color:{LIGHT_TEXT};">
      Essa virada separa empresa de empreendimento pessoal.
    </div>
  </div>
</div>'''


# ── S7 CAMINHO (escuro, checklist editorial) ────────────────────────────────
def s7():
    img = b64(GER / "qua_s7_notebook_planejamento.png")
    items = [
        ("Mapeie", "tudo que SÓ você decide hoje."),
        ("Classifique", "o que é regra, critério ou decisão sua."),
        ("Defina", "1 responsável por área crítica."),
        ("Crie", "cadência de revisão semanal ou quinzenal."),
        ("Reserve", "4h por semana fora da operação."),
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
  <div style="position:absolute;right:0;top:0;bottom:0;width:36%;z-index:0;">
    <img src="{img}" style="width:100%;height:100%;object-fit:cover;
         filter:brightness(0.55) contrast(1.08) saturate(0.78);">
    <div style="position:absolute;inset:0;background:linear-gradient(270deg, transparent 55%, {INK2} 100%);"></div>
  </div>
  {GRAIN}
  {logo(dark=True)}
  <div style="position:absolute;top:84px;left:28px;right:42%;z-index:20;">
    {kicker("Para sair do centro")}
    <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:700;
                font-size:24px;line-height:1.02;color:#fff;">
      <span style="color:{CYAN};">5 movimentos</span> antes de qualquer contratação:
    </div>
  </div>
  <div style="position:absolute;top:228px;left:28px;right:28px;z-index:20;">
    {cards}
  </div>
  <div style="position:absolute;left:28px;right:28px;bottom:24px;z-index:20;">
    {bridge("Com isso, o crescimento da empresa para de te custar a sua vida.")}
  </div>
</div>'''


# ── S8 CTA (Derick) ──────────────────────────────────────────────────────────
def s8():
    derick = b64(FOTOS / "derick_1_cutout.png")
    return f'''
<div style="width:{VW}px;height:{VH}px;position:relative;overflow:hidden;
            background:radial-gradient(ellipse 60% 80% at 75% 60%, #0d2540 0%, {INK} 60%, #03060c 100%);">
  <div style="position:absolute;inset:0;z-index:0;pointer-events:none;
    background-image:radial-gradient(circle,rgba(255,255,255,0.022) 1px,transparent 1px);
    background-size:24px 24px;"></div>
  <div style="position:absolute;right:-8%;bottom:0;width:75%;height:88%;z-index:5;
    background:radial-gradient(ellipse 60% 50% at 50% 35%, rgba(30,197,242,0.25) 0%, transparent 65%);
    filter:blur(20px);"></div>

  <div style="position:absolute;right:-12%;bottom:0;height:100%;z-index:10;
              display:flex;align-items:flex-end;">
    <img src="{derick}" style="height:100%;width:auto;display:block;
         filter:brightness(1.04) contrast(1.06) saturate(1.02)
                drop-shadow(0 8px 24px rgba(0,0,0,0.6))
                drop-shadow(0 0 18px rgba(30,197,242,0.20));">
  </div>

  {GRAIN}
  {logo(dark=True)}

  <div style="position:absolute;top:92px;left:28px;right:42%;z-index:20;">
    {kicker("NUC Vision")}
    <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:700;
                font-size:28px;line-height:1.02;color:#fff;">
      A empresa precisa crescer<br>
      sem <span style="color:{CYAN};">depender de você.</span>
    </div>
    <div style="font-family:'Space Grotesk',sans-serif;font-size:12px;font-weight:400;
                color:rgba(255,255,255,0.80);line-height:1.6;margin-top:18px;">
      A NUC organiza o núcleo para que o dono saia da operação <span style="color:#fff;font-weight:600;">sem perder controle.</span>
    </div>
  </div>

  <div style="position:absolute;left:0;right:0;bottom:0;z-index:30;
              background:{CYAN};padding:20px 26px;text-align:center;
              box-shadow:0 -10px 32px rgba(0,0,0,0.45);">
    <div style="font-family:'Space Grotesk',sans-serif;font-size:14px;font-weight:700;
                color:{INK};line-height:1.3;letter-spacing:0.005em;">
      Reconheceu sua empresa? Comenta <span style="font-weight:800;">GARGALO</span>
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
