#!/usr/bin/env python3
"""
NUC Vision — Empresa que depende 1000% do dono
Modelo 2 (Quebra de crença). 8 slides. Imagen 4 nas âncoras visuais.
"""
import sys, base64, asyncio
from pathlib import Path
sys.path.insert(0, "/home/user/Meu-espa-o")
sys.path.insert(0, "/home/user/Meu-espa-o/geradores")
from design_system import (
    FONT_LINK, CSS_BASE, INK, ACCENT, GRAY, FONTS, LOGO_URI,
    NOISE_B64, html_shell, kicker,
)
from nuc_realism import REALISM_CSS, GRAO_OVERLAY, fundo_profundo, recorte
from playwright.async_api import async_playwright

FOTOS    = Path("/home/user/Meu-espa-o/fotos/geradas")
OUTPUT   = Path("/home/user/Meu-espa-o/output/empresa-dono")
PREVIEWS = Path("/home/user/Meu-espa-o/previews")
OUTPUT.mkdir(parents=True, exist_ok=True)
PREVIEWS.mkdir(exist_ok=True)

VW, VH  = 420, 525
SCALE   = 1080 / VW
CHROME  = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
TOTAL   = 8

CAPTION = (
    "Se a sua empresa para quando você para, você não tem uma empresa. "
    "Tem um emprego disfarçado de negócio. Desliza. 👇\n"
    "#gestao #empresario #escalabilidade #nucvision #organizacao #lideranca #negocios"
)

def photo_uri(name):
    p = FOTOS / name
    ext = p.suffix.lower().lstrip(".")
    mime = {"jpg":"jpeg","jpeg":"jpeg","png":"png","webp":"webp"}.get(ext,"jpeg")
    return f"data:image/{mime};base64,{base64.b64encode(p.read_bytes()).decode()}"

def logo(size=22, top=20):
    return (f'<div style="position:absolute;top:{top}px;left:0;right:0;'
            f'display:flex;justify-content:center;z-index:30;">'
            f'<img src="{LOGO_URI}" style="height:{size}px;width:auto;'
            f'filter:brightness(0) invert(1) drop-shadow(0 2px 10px rgba(0,0,0,0.7));"></div>')

def hl(word, color=None):
    bg = color or ACCENT["primary"]
    tc = "#06121c"
    return (f'<span style="background:{bg};color:{tc};'
            f'padding:2px 12px 7px;border-radius:8px;display:inline-block;line-height:0.92;'
            f'box-shadow:0 6px 24px rgba(30,197,242,0.45);">{word}</span>')

def bridge(text):
    return (f'<div style="display:flex;align-items:flex-start;gap:9px;margin-top:14px;">'
            f'<div style="width:22px;height:2px;background:{ACCENT["primary"]};'
            f'flex-shrink:0;margin-top:9px;"></div>'
            f'<span style="font-family:{FONTS["body"]},sans-serif;font-size:12.5px;'
            f'font-style:italic;color:{ACCENT["primary"]};line-height:1.5;font-weight:500;">'
            f'{text}</span></div>')

def dot_grid(color="rgba(30,197,242,0.05)", sp=28, z=0):
    return (f'<div style="position:absolute;inset:0;z-index:{z};pointer-events:none;'
            f'background-image:radial-gradient(circle,{color} 1.2px,transparent 1.2px);'
            f'background-size:{sp}px {sp}px;"></div>')

def headline(txt, size=44, mt=8):
    return (f'<div style="font-family:{FONTS["display"]},sans-serif;font-size:{size}px;'
            f'color:#fff;line-height:0.9;text-transform:uppercase;margin-top:{mt}px;">'
            f'{txt}</div>')

def body(txt, size=13, color="rgba(255,255,255,0.68)", mt=10, maxw=312):
    return (f'<div style="font-family:{FONTS["body"]},sans-serif;font-size:{size}px;'
            f'color:{color};line-height:1.58;margin-top:{mt}px;max-width:{maxw}px;">'
            f'{txt}</div>')

def kicker_line(txt):
    return (f'<div style="font-family:{FONTS["body"]},sans-serif;font-size:9.5px;font-weight:700;'
            f'letter-spacing:0.22em;text-transform:uppercase;color:{ACCENT["primary"]};'
            f'display:flex;align-items:center;gap:8px;">'
            f'<div style="width:22px;height:1px;background:{ACCENT["primary"]};opacity:0.6;"></div>'
            f'{txt}</div>')


# ── S1 · GANCHO ──────────────────────────────────────────────────────────────
def slide1():
    img = photo_uri("s1_dono_noite.png")
    return f'''<div class="slide" style="overflow:hidden;background:#060810;">

      <!-- foto full-bleed com overlay pesado embaixo -->
      <div style="position:absolute;inset:0;z-index:0;">
        <img src="{img}" style="width:100%;height:100%;object-fit:cover;
             filter:brightness(0.6) contrast(1.08) saturate(0.85);">
      </div>
      <div style="position:absolute;inset:0;z-index:1;
                  background:linear-gradient(180deg,
                    rgba(6,8,16,0.55) 0%,
                    transparent 28%,
                    transparent 48%,
                    rgba(6,8,16,0.7) 68%,
                    #060810 90%);"></div>
      {dot_grid("rgba(255,255,255,0.025)", z=2)}

      <!-- tag topo -->
      <div style="position:absolute;top:52px;right:24px;z-index:20;
                  background:rgba(255,60,60,0.18);border:1px solid rgba(255,60,60,0.4);
                  border-radius:999px;padding:5px 13px;backdrop-filter:blur(6px);">
        <span style="font-family:{FONTS["body"]},sans-serif;font-size:9px;font-weight:700;
                     letter-spacing:0.18em;text-transform:uppercase;color:rgba(255,120,120,0.95);">
          3 anos sem ferias
        </span>
      </div>

      {logo()}

      <!-- texto topo esquerdo -->
      <div style="position:absolute;top:58px;left:26px;z-index:20;max-width:260px;">
        {kicker_line("O Diagnostico")}
        {headline("SE VOCE<br>PARA, A<br>EMPRESA " + hl("PARA."), size=46, mt=8)}
      </div>

      <div style="position:absolute;bottom:0;left:0;right:0;z-index:20;padding:0 26px 36px;">
        {body("Voce construiu um negocio. Ou construiu uma prisao com CNPJ?")}
        {bridge("O sinal mais claro apareceu numa segunda-feira de janeiro.")}
      </div>

      {GRAO_OVERLAY}
    </div>'''


# ── S2 · CURIOSIDADE ─────────────────────────────────────────────────────────
def slide2():
    img = photo_uri("s2_crescimento.png")
    return f'''<div class="slide" style="overflow:hidden;background:#07090f;">

      {fundo_profundo(img, extra_style="filter:blur(20px) brightness(0.35) saturate(0.9);")}
      {dot_grid("rgba(255,255,255,0.035)", z=1)}

      <!-- foto contida no lado direito, integrada -->
      <div style="position:absolute;top:0;right:0;bottom:0;width:55%;z-index:2;overflow:hidden;">
        <img src="{img}" style="width:100%;height:100%;object-fit:cover;
             filter:brightness(0.72) contrast(1.05) saturate(0.9)
                    drop-shadow(-8px 0 24px rgba(6,8,15,0.8));">
        <div style="position:absolute;inset:0;
                    background:linear-gradient(90deg,#07090f 0%,transparent 40%);"></div>
      </div>

      <div style="position:absolute;inset:0;z-index:3;
                  background:linear-gradient(90deg,#07090f 42%,transparent 72%);"></div>
      <div style="position:absolute;inset:0;z-index:3;
                  background:linear-gradient(180deg,rgba(7,9,15,0.65) 0%,transparent 22%,transparent 65%,#07090f 94%);"></div>

      {logo()}

      <div style="position:absolute;top:58px;left:26px;z-index:10;max-width:225px;">
        {kicker_line("O Paradoxo")}
        {headline("NEGOCIO<br>CRESCE.<br>DONO " + hl("AFUNDA."), size=40, mt=8)}
      </div>

      <!-- dois stats verticais -->
      <div style="position:absolute;top:252px;left:26px;z-index:10;">
        <div style="display:flex;flex-direction:column;gap:14px;max-width:210px;">
          <div style="border-left:2px solid {ACCENT["primary"]};padding-left:12px;">
            <div style="font-family:{FONTS["display"]},sans-serif;font-size:32px;
                        color:{ACCENT["primary"]};line-height:0.86;">+240%</div>
            <div style="font-family:{FONTS["body"]},sans-serif;font-size:10px;font-weight:600;
                        color:rgba(255,255,255,0.45);text-transform:uppercase;
                        letter-spacing:0.08em;margin-top:4px;">faturamento em 3 anos</div>
          </div>
          <div style="border-left:2px solid rgba(255,80,80,0.5);padding-left:12px;">
            <div style="font-family:{FONTS["display"]},sans-serif;font-size:32px;
                        color:rgba(255,100,100,0.8);line-height:0.86;">-100%</div>
            <div style="font-family:{FONTS["body"]},sans-serif;font-size:10px;font-weight:600;
                        color:rgba(255,255,255,0.45);text-transform:uppercase;
                        letter-spacing:0.08em;margin-top:4px;">tempo livre do dono</div>
          </div>
        </div>
      </div>

      <div style="position:absolute;bottom:0;left:0;right:0;z-index:10;padding:0 26px 36px;">
        {bridge("Ate que chegou o dia que ele nao podia levantar da cama.")}
      </div>

      {GRAO_OVERLAY}
    </div>'''


# ── S3 · ESCALADA ─────────────────────────────────────────────────────────────
def slide3():
    img = photo_uri("s3_doente.png")
    return f'''<div class="slide" style="overflow:hidden;background:#060710;">

      <div style="position:absolute;inset:0;z-index:0;">
        <img src="{img}" style="width:100%;height:100%;object-fit:cover;
             filter:brightness(0.52) contrast(1.1) saturate(0.75);">
      </div>
      <div style="position:absolute;inset:0;z-index:1;
                  background:linear-gradient(180deg,
                    rgba(6,7,16,0.72) 0%,
                    rgba(6,7,16,0.2) 35%,
                    transparent 55%,
                    rgba(6,7,16,0.75) 75%,
                    #060710 94%);"></div>

      {logo()}

      <!-- numero de chamadas perdidas — elemento dramatico -->
      <div style="position:absolute;top:52px;right:24px;z-index:20;
                  background:rgba(255,50,50,0.22);border:1px solid rgba(255,50,50,0.5);
                  border-radius:14px;padding:8px 16px;text-align:center;
                  backdrop-filter:blur(6px);">
        <div style="font-family:{FONTS["display"]},sans-serif;font-size:28px;
                    color:rgba(255,100,100,0.95);line-height:0.9;">47</div>
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:8.5px;font-weight:700;
                    letter-spacing:0.12em;color:rgba(255,120,120,0.7);
                    text-transform:uppercase;margin-top:3px;">chamadas<br>perdidas</div>
      </div>

      <div style="position:absolute;top:58px;left:26px;z-index:20;max-width:230px;">
        {kicker_line("O Dia Zero")}
        {headline("ELE FICOU<br>DOENTE.<br>TUDO " + hl("PAROU."), size=44, mt=8)}
      </div>

      <div style="position:absolute;bottom:0;left:0;right:0;z-index:20;padding:0 26px 36px;">
        {body("Clientes sem resposta. Equipe paralisada. Pedidos represados. Uma gripe revelou a fragilidade de tudo que ele construiu.")}
        {bridge("O problema nao era falta de funcionario. Era outra coisa.")}
      </div>

      {GRAO_OVERLAY}
    </div>'''


# ── S4 · VIRADA ───────────────────────────────────────────────────────────────
def slide4():
    img = photo_uri("s4_engrenagem.png")
    return f'''<div class="slide" style="overflow:hidden;background:#08070a;">

      {fundo_profundo(img, extra_style="filter:blur(18px) brightness(0.3) saturate(0.8);")}
      {dot_grid("rgba(255,255,255,0.03)", z=1)}

      <!-- engrenagem contida, integrada ao layout -->
      <div style="position:absolute;top:110px;left:50%;transform:translateX(-48%);
                  width:280px;z-index:2;
                  -webkit-mask-image:radial-gradient(ellipse 88% 88% at 50% 50%,#000 55%,transparent 90%);
                  mask-image:radial-gradient(ellipse 88% 88% at 50% 50%,#000 55%,transparent 90%);">
        <img src="{img}" style="width:100%;display:block;
             filter:brightness(0.85) contrast(1.1) saturate(0.7)
                    drop-shadow(0 0 20px rgba(30,197,242,0.2));">
      </div>
      <!-- sombra de contato -->
      <div style="position:absolute;top:290px;left:50%;transform:translateX(-50%);
                  width:200px;height:18px;z-index:1;
                  background:radial-gradient(closest-side,rgba(0,0,0,0.65),transparent 78%);
                  filter:blur(9px);"></div>

      <div style="position:absolute;inset:0;z-index:3;
                  background:linear-gradient(180deg,rgba(8,7,10,0.7) 0%,transparent 22%,transparent 55%,#08070a 82%);"></div>

      {logo()}

      <div style="position:absolute;top:58px;left:26px;z-index:10;">
        {kicker_line("A Causa Real")}
        {headline("NAO E FALTA<br>DE " + hl("EQUIPE."), size=40, mt=8)}
      </div>

      <div style="position:absolute;bottom:0;left:0;right:0;z-index:10;padding:0 26px 40px;">
        {body("E falta de estrutura. Quando tudo depende de uma unica engrenagem central, qualquer abalo trava o sistema inteiro.", mt=0)}
        {bridge("Empresas que escalam fizeram uma coisa diferente.")}
      </div>

      {GRAO_OVERLAY}
    </div>'''


# ── S5 · ESCALADA 2 ──────────────────────────────────────────────────────────
def slide5():
    img = photo_uri("s5_equipe.png")
    return f'''<div class="slide" style="overflow:hidden;background:#060c0a;">

      {fundo_profundo(img, extra_style="filter:blur(22px) brightness(0.32) saturate(1.0);")}
      {dot_grid("rgba(30,197,242,0.04)", z=1)}

      <!-- foto no topo, ocupando metade superior -->
      <div style="position:absolute;top:0;left:0;right:0;height:52%;z-index:2;overflow:hidden;">
        <img src="{img}" style="width:100%;height:100%;object-fit:cover;object-position:center top;
             filter:brightness(0.78) contrast(1.06) saturate(0.95);">
        <div style="position:absolute;inset:0;
                    background:linear-gradient(180deg,rgba(6,12,10,0.4) 0%,rgba(6,12,10,0.0) 50%,#060c0a 100%);"></div>
      </div>

      <div style="position:absolute;inset:0;z-index:3;
                  background:linear-gradient(180deg,transparent 38%,#060c0a 62%);"></div>

      {logo()}

      <!-- tag topo -->
      <div style="position:absolute;top:52px;right:24px;z-index:20;
                  background:rgba(30,197,242,0.14);border:1px solid rgba(30,197,242,0.35);
                  border-radius:999px;padding:5px 13px;backdrop-filter:blur(6px);">
        <span style="font-family:{FONTS["body"]},sans-serif;font-size:9px;font-weight:700;
                     letter-spacing:0.18em;text-transform:uppercase;color:{ACCENT["primary"]};">
          Como escalar
        </span>
      </div>

      <div style="position:absolute;bottom:0;left:0;right:0;z-index:10;padding:0 26px 36px;">
        {kicker_line("O Modelo")}
        {headline("CADA UM<br>SABE O<br>QUE " + hl("FAZER."), size=42, mt=8)}
        {body("Processos documentados. Papeis claros. Decisoes descentralizadas. Sem o dono precisar ser consultado para tudo.", mt=12)}
        {bridge("Mas tem um detalhe que ninguem conta sobre essa transicao.")}
      </div>

      {GRAO_OVERLAY}
    </div>'''


# ── S6 · REVELAÇÃO ────────────────────────────────────────────────────────────
def slide6():
    img = photo_uri("s6_dispensavel.png")
    return f'''<div class="slide" style="overflow:hidden;background:#07090c;">

      <div style="position:absolute;inset:0;z-index:0;">
        <img src="{img}" style="width:100%;height:100%;object-fit:cover;
             filter:brightness(0.58) contrast(1.08) saturate(0.9);">
      </div>
      <div style="position:absolute;inset:0;z-index:1;
                  background:linear-gradient(180deg,
                    rgba(7,9,12,0.65) 0%,
                    transparent 30%,
                    transparent 52%,
                    rgba(7,9,12,0.72) 70%,
                    #07090c 92%);"></div>
      {dot_grid("rgba(255,255,255,0.02)", z=2)}

      {logo()}

      <div style="position:absolute;top:58px;left:26px;z-index:20;max-width:280px;">
        {kicker_line("A Revelacao")}
        {headline("O OBJETIVO<br>E VOCE SER<br>" + hl("DISPENSAVEL."), size=38, mt=8)}
      </div>

      <div style="position:absolute;bottom:0;left:0;right:0;z-index:20;padding:0 26px 40px;">
        {body("Nao e abandono. E liberdade. Quando a empresa funciona sem voce presente, voce pode escolher onde colocar sua energia.", mt=0)}
        {body("Isso nao acontece por acaso. Precisa ser construido.", mt=8, color="rgba(255,255,255,0.45)")}
        {bridge("E exatamente aqui que a NUC Vision entra.")}
      </div>

      {GRAO_OVERLAY}
    </div>'''


# ── S7 · INSIGHT / NUC ────────────────────────────────────────────────────────
def slide7():
    img = photo_uri("s7_nuc.png")
    return f'''<div class="slide" style="overflow:hidden;background:#060a0f;">

      {fundo_profundo(img, extra_style="filter:blur(20px) brightness(0.3) saturate(0.85);")}
      {dot_grid("rgba(30,197,242,0.04)", z=1)}

      <!-- foto integrada lado direito -->
      <div style="position:absolute;top:0;right:0;bottom:0;width:50%;z-index:2;overflow:hidden;">
        <img src="{img}" style="width:100%;height:100%;object-fit:cover;
             filter:brightness(0.7) contrast(1.06) saturate(0.9);">
        <div style="position:absolute;inset:0;
                    background:linear-gradient(90deg,#060a0f 0%,transparent 45%);"></div>
      </div>

      <div style="position:absolute;inset:0;z-index:3;
                  background:linear-gradient(90deg,#060a0f 40%,transparent 68%);"></div>
      <div style="position:absolute;inset:0;z-index:3;
                  background:linear-gradient(180deg,rgba(6,10,15,0.65) 0%,transparent 20%,transparent 65%,#060a0f 94%);"></div>

      {logo()}

      <div style="position:absolute;top:58px;left:26px;z-index:10;max-width:230px;">
        {kicker_line("NUC Vision")}
        {headline("ESTRUTURA<br>QUE<br>" + hl("ESCALA."), size=42, mt=8)}
      </div>

      <!-- 3 pilares verticais -->
      <div style="position:absolute;top:236px;left:26px;z-index:10;max-width:210px;">
        <div style="display:flex;flex-direction:column;gap:12px;">
          <div style="display:flex;align-items:center;gap:10px;">
            <div style="width:6px;height:6px;border-radius:50%;background:{ACCENT["primary"]};flex-shrink:0;"></div>
            <div style="font-family:{FONTS["body"]},sans-serif;font-size:12px;font-weight:600;color:rgba(255,255,255,0.8);">Mapeamento de processos</div>
          </div>
          <div style="display:flex;align-items:center;gap:10px;">
            <div style="width:6px;height:6px;border-radius:50%;background:{ACCENT["primary"]};flex-shrink:0;"></div>
            <div style="font-family:{FONTS["body"]},sans-serif;font-size:12px;font-weight:600;color:rgba(255,255,255,0.8);">Estrutura de gestao e times</div>
          </div>
          <div style="display:flex;align-items:center;gap:10px;">
            <div style="width:6px;height:6px;border-radius:50%;background:{ACCENT["primary"]};flex-shrink:0;"></div>
            <div style="font-family:{FONTS["body"]},sans-serif;font-size:12px;font-weight:600;color:rgba(255,255,255,0.8);">Cultura que funciona sem voce</div>
          </div>
        </div>
      </div>

      <div style="position:absolute;bottom:0;left:0;right:0;z-index:10;padding:0 26px 38px;">
        {body("Transformamos empresas que dependem de uma pessoa em negócios que funcionam por sistema.", mt=0)}
      </div>

      {GRAO_OVERLAY}
    </div>'''


# ── S8 · CTA ─────────────────────────────────────────────────────────────────
def slide8():
    return f'''<div class="slide" style="overflow:hidden;
        background:radial-gradient(ellipse 110% 80% at 10% 95%, #0d1a10 0%, {INK["void"]} 55%, #040609 100%);">

      {dot_grid("rgba(30,197,242,0.05)", z=0)}

      <!-- glow ciano embaixo esquerdo -->
      <div style="position:absolute;bottom:-50px;left:-30px;width:300px;height:300px;z-index:1;
                  background:radial-gradient(circle,rgba(30,197,242,0.16),transparent 66%);
                  filter:blur(18px);pointer-events:none;"></div>

      <!-- numero decorativo de fundo -->
      <div style="position:absolute;bottom:-20px;right:-10px;z-index:1;
                  font-family:{FONTS["display"]},sans-serif;font-size:280px;line-height:1;
                  color:rgba(30,197,242,0.04);user-select:none;letter-spacing:-0.04em;">N</div>

      {logo()}

      <div style="position:absolute;top:72px;left:26px;right:26px;z-index:10;">
        {kicker_line("Proximo Passo")}

        <div style="font-family:{FONTS["display"]},sans-serif;font-size:48px;line-height:0.88;
                    color:#fff;text-transform:uppercase;margin-top:10px;">
          PRONTO PRA<br>
          <span style="background:{ACCENT["primary"]};color:#06121c;
                       padding:2px 14px 8px;border-radius:10px;
                       box-shadow:0 8px 28px rgba(30,197,242,0.5);">SAIR</span><br>
          DO MEIO?
        </div>
      </div>

      <!-- linha divisora -->
      <div style="position:absolute;top:272px;left:26px;right:80px;height:1px;z-index:10;
                  background:linear-gradient(90deg,rgba(30,197,242,0.4),transparent);"></div>

      <div style="position:absolute;top:288px;left:26px;right:26px;z-index:10;">
        {body("A NUC Vision trabalha com empresarios que querem crescer sem depender de si mesmos para tudo. Se esse e o seu momento, vamos conversar.", mt=0, maxw=340)}
      </div>

      <!-- CTA -->
      <div style="position:absolute;bottom:0;left:0;right:0;z-index:20;padding:0 26px 44px;">
        <div style="display:inline-block;background:{ACCENT["primary"]};color:#06121c;
                    font-family:{FONTS["body"]},sans-serif;font-size:12px;font-weight:700;
                    letter-spacing:0.12em;text-transform:uppercase;
                    padding:16px 32px;border-radius:999px;
                    box-shadow:0 12px 32px rgba(30,197,242,0.5);">
          Fala com a NUC
        </div>
        {body("Link na bio", size=10, color="rgba(255,255,255,0.3)", mt=10)}
      </div>

      {GRAO_OVERLAY}
    </div>'''


# ── MONTAGEM ──────────────────────────────────────────────────────────────────
SLIDE_FNS  = [slide1, slide2, slide3, slide4, slide5, slide6, slide7, slide8]
SLIDE_NOMES = ["s1_gancho","s2_curiosidade","s3_escalada","s4_virada",
               "s5_escalada2","s6_revelacao","s7_nuc","s8_cta"]

def build_html():
    inner = "\n".join(fn() for fn in SLIDE_FNS)
    base  = html_shell(inner, TOTAL, CAPTION)
    return base.replace(
        f"<style>{CSS_BASE}</style>",
        f"<style>{CSS_BASE}\n{REALISM_CSS}\n"
        f".display{{font-family:{FONTS['display']},sans-serif;text-transform:uppercase;}}</style>"
    )

async def export():
    html = build_html()
    html_path = PREVIEWS / "empresa-dono.html"
    html_path.write_text(html, encoding="utf-8")
    print(f"HTML: {html_path}")

    async with async_playwright() as p:
        browser = await p.chromium.launch(executable_path=CHROME)
        page = await browser.new_page(
            viewport={"width": VW, "height": VH},
            device_scale_factor=SCALE,
        )
        await page.set_content(html, wait_until="networkidle")
        await page.wait_for_timeout(3000)

        await page.evaluate(f"""() => {{
            ['ig-header','ig-actions','ig-caption','ig-dots'].forEach(cls => {{
                const el = document.querySelector('.' + cls);
                if (el) el.style.display = 'none';
            }});
            const frame = document.querySelector('.ig-frame');
            if (frame) frame.style.cssText = 'width:{VW}px;height:{VH}px;border-radius:0;box-shadow:none;overflow:hidden;margin:0;padding:0;';
            const vp = document.querySelector('.carousel-viewport');
            if (vp) vp.style.cssText = 'width:{VW}px;height:{VH}px;overflow:hidden;cursor:default;';
            document.body.style.cssText = 'padding:0;margin:0;display:block;overflow:hidden;background:#000;';
        }}""")
        await page.wait_for_timeout(300)

        for i in range(TOTAL):
            await page.evaluate(f"""(idx) => {{
                const t = document.querySelector('.carousel-track');
                t.style.transition = 'none';
                t.style.transform = 'translateX(' + (-idx * {VW}) + 'px)';
            }}""", i)
            await page.wait_for_timeout(400)
            out = OUTPUT / f"slide_{i+1:02d}_{SLIDE_NOMES[i]}.png"
            await page.screenshot(
                path=str(out),
                clip={"x": 0, "y": 0, "width": VW, "height": VH},
            )
            print(f"  {i+1}/{TOTAL} -> {out.name}")

        await browser.close()
    print(f"\nCaption:\n{CAPTION}")

if __name__ == "__main__":
    asyncio.run(export())
