#!/usr/bin/env python3
"""Quarta v2 — O dono virou o gargalo. Metáforas conceituais, tipografia ousada."""
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
WINE = "#3a0f15"   # paleta complementar — bordeaux profundo (S5 castelo)
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


# ── S1 IMPACTO — chiaroscuro portrait, tipografia invade ─────────────────────
def s1():
    img = b64(GER / "qua_s1_dono_chiaroscuro.png")
    return f'''
<div style="width:{VW}px;height:{VH}px;position:relative;overflow:hidden;background:#000;">
  <div style="position:absolute;inset:0;z-index:0;">
    <img src="{img}" style="width:100%;height:100%;object-fit:cover;filter:contrast(1.10) saturate(0.85);">
  </div>
  <div style="position:absolute;inset:0;z-index:1;
    background:linear-gradient(180deg, rgba(0,0,0,0.10) 0%, rgba(0,0,0,0.05) 35%, rgba(0,0,0,0.60) 70%, rgba(0,0,0,0.96) 100%);"></div>
  {GRAIN}
  {logo(dark=True)}
  <div style="position:absolute;left:28px;right:28px;bottom:28px;z-index:20;">
    <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:700;
                font-size:54px;line-height:0.92;color:#fff;letter-spacing:-0.02em;
                text-shadow:0 2px 24px rgba(0,0,0,0.7);">
      Sua empresa<br>
      não cresce<br>
      porque <span style="color:{CYAN};">você</span><br>
      é bom demais.
    </div>
    <div style="font-family:'Space Grotesk',sans-serif;font-size:12.5px;font-weight:400;
                color:rgba(255,255,255,0.82);line-height:1.55;margin-top:16px;max-width:300px;">
      Você acha que é dedicação, provavelmente virou dependência.
    </div>
    <div style="margin-top:14px;">{bridge("É um problema antes de ser uma virtude.")}</div>
  </div>
</div>'''


# ── S2 CONTEXTO — cadeira solo no auditório, tipografia oclui parcialmente ──
def s2():
    img = b64(GER / "qua_s2_cadeira_auditorio.png")
    return f'''
<div style="width:{VW}px;height:{VH}px;position:relative;overflow:hidden;background:#000;">
  <div style="position:absolute;inset:0;z-index:0;">
    <img src="{img}" style="width:100%;height:100%;object-fit:cover;filter:brightness(0.85) contrast(1.10) saturate(0.80);">
  </div>
  <div style="position:absolute;inset:0;z-index:1;
    background:linear-gradient(180deg, rgba(0,0,0,0.70) 0%, rgba(0,0,0,0.15) 40%, rgba(0,0,0,0.55) 78%, rgba(0,0,0,0.96) 100%);"></div>
  {GRAIN}
  {logo(dark=True)}
  <div style="position:absolute;top:80px;left:28px;right:28px;z-index:20;">
    {kicker("O padrão")}
    <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:700;
                font-size:36px;line-height:0.98;color:#fff;text-shadow:0 2px 18px rgba(0,0,0,0.65);">
      Em toda empresa<br>
      que parou, existe<br>
      <span style="color:{CYAN};">uma cadeira</span><br>
      que carrega tudo.
    </div>
  </div>
  <div style="position:absolute;left:28px;right:28px;bottom:78px;z-index:20;">
    <div style="font-family:'Space Grotesk',sans-serif;font-size:12px;font-weight:400;
                color:rgba(255,255,255,0.78);line-height:1.6;max-width:340px;">
      É ela quem aprova proposta, atende cliente difícil, resolve crise, decide preço.
      <span style="color:#fff;font-weight:600;">E quase sempre é a sua.</span>
    </div>
  </div>
  <div style="position:absolute;left:28px;right:28px;bottom:24px;z-index:20;">
    {bridge("O problema começa quando ninguém mais consegue se sentar nela.")}
  </div>
</div>'''


# ── S3 SINTOMA — lista escura limpa ─────────────────────────────────────────
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
                font-size:30px;line-height:1.0;color:#fff;">
      Pelo menos <span style="color:{CYAN};">3 desses</span><br>são você:
    </div>
    <div style="margin-top:14px;">{cards}</div>
  </div>
  <div style="position:absolute;left:30px;right:30px;bottom:24px;z-index:20;">
    {bridge("Isso não é dedicação, é falta de processo virando dependência.")}
  </div>
</div>'''


# ── S4 CAUSA — agenda lotada (claro, still life editorial) ──────────────────
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
    {kicker("A causa real", color=LIGHT_TEXT)}
    <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:700;
                font-size:30px;line-height:0.98;color:{LIGHT_TEXT};">
      Ninguém é dono<br>
      de <span style="color:{CYAN};">etapa<br>nenhuma.</span>
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


# ── S5 CONSEQUÊNCIA — castelo de cartas, paleta vinho/dourado ───────────────
def s5():
    img = b64(GER / "qua_s5_castelo_cartas.png")
    GOLD = "#d4af37"
    return f'''
<div style="width:{VW}px;height:{VH}px;position:relative;overflow:hidden;background:#0a0608;">
  <div style="position:absolute;inset:0;z-index:0;">
    <img src="{img}" style="width:100%;height:100%;object-fit:cover;filter:brightness(0.78) contrast(1.10) saturate(0.85) hue-rotate(-5deg);">
  </div>
  <div style="position:absolute;inset:0;z-index:1;
    background:linear-gradient(180deg, rgba(58,15,21,0.45) 0%, rgba(10,6,8,0.10) 35%, rgba(10,6,8,0.70) 75%, rgba(10,6,8,0.97) 100%);"></div>
  {GRAIN}
  {logo(dark=True)}
  <div style="position:absolute;top:80px;left:28px;right:28px;z-index:20;">
    {kicker("O efeito invisível", color=GOLD)}
    <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:700;
                font-size:46px;line-height:0.94;color:#fff;letter-spacing:-0.01em;
                text-shadow:0 2px 18px rgba(0,0,0,0.7);">
      Basta <span style="color:{GOLD};">1 carta</span><br>
      sair do lugar.
    </div>
  </div>
  <div style="position:absolute;left:28px;right:28px;bottom:78px;z-index:20;">
    <div style="font-family:'Space Grotesk',sans-serif;font-size:12px;font-weight:400;
                color:rgba(255,255,255,0.82);line-height:1.6;max-width:340px;">
      Não é porque o time é ruim. É porque a empresa nunca foi feita para
      <span style="color:#fff;font-weight:600;">funcionar sem você.</span>
    </div>
  </div>
  <div style="position:absolute;left:28px;right:28px;bottom:24px;z-index:20;">
    {bridge("Talvez a pergunta que você está fazendo seja a errada.", color=GOLD)}
  </div>
</div>'''


# ── S6 VIRADA (claro respiro) ────────────────────────────────────────────────
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
    {kicker("A nova pergunta")}
    <div style="font-family:'Space Grotesk',sans-serif;font-size:14px;font-weight:500;
                color:rgba(26,46,77,0.45);line-height:1.4;margin-bottom:22px;
                text-decoration:line-through;text-decoration-thickness:1.5px;
                text-decoration-color:rgba(26,46,77,0.45);">
      Como produzir mais?
    </div>
    <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:700;
                font-size:42px;line-height:1.0;color:{LIGHT_TEXT};max-width:340px;">
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


# ── S7 CAMINHO — post-its em quadrantes ─────────────────────────────────────
def s7():
    img = b64(GER / "qua_s7_postits_quadrantes.png")
    items = [
        ("Mapeie", "tudo que SÓ você decide hoje."),
        ("Classifique", "o que é regra, critério ou decisão sua."),
        ("Defina", "1 responsável por área crítica."),
        ("Crie", "cadência de revisão semanal ou quinzenal."),
        ("Reserve", "4h por semana fora da operação."),
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
    {kicker("Para sair do centro")}
    <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:700;
                font-size:26px;line-height:1.0;color:{LIGHT_TEXT};">
      <span style="color:{CYAN};">5 movimentos</span><br>
      antes de qualquer<br>contratação:
    </div>
  </div>
  <div style="position:absolute;top:232px;left:28px;right:28px;z-index:20;">
    {cards}
  </div>
  <div style="position:absolute;left:28px;right:28px;bottom:24px;z-index:20;
              padding-top:12px;border-top:1px solid rgba(30,197,242,0.30);">
    <div style="font-family:'Space Grotesk',sans-serif;font-style:italic;font-size:12.5px;
                font-weight:500;color:{LIGHT_TEXT};">
      Com isso, o crescimento da empresa para de custar a sua vida.
    </div>
  </div>
</div>'''


# ── S8 CTA — Derick (padrão V4 corrigido) ───────────────────────────────────
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

  <div style="position:absolute;right:-22%;bottom:64px;height:88%;z-index:10;
              display:flex;align-items:flex-end;">
    <img src="{derick}" style="height:100%;width:auto;display:block;
         filter:brightness(1.05) contrast(1.06) saturate(1.02)
                drop-shadow(0 8px 24px rgba(0,0,0,0.6))
                drop-shadow(0 0 18px rgba(30,197,242,0.20));">
  </div>

  {GRAIN}
  {logo(dark=True)}

  <div style="position:absolute;top:92px;left:28px;right:48%;z-index:20;">
    {kicker("NUC Vision")}
    <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:700;
                font-size:28px;line-height:1.02;color:#fff;">
      A empresa precisa<br>
      crescer sem<br>
      <span style="color:{CYAN};">depender de você.</span>
    </div>
    <div style="font-family:'Space Grotesk',sans-serif;font-size:11.5px;font-weight:400;
                color:rgba(255,255,255,0.80);line-height:1.6;margin-top:16px;">
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
