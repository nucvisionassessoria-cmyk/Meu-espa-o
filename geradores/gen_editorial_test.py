#!/usr/bin/env python3
"""
NUC Vision — Teste de estilo editorial puro (sem foto)
Slide de referência: tipografia massiva + dados + composição assimétrica
"""
import sys, base64, asyncio
from pathlib import Path
sys.path.insert(0, "/home/user/Meu-espa-o")
sys.path.insert(0, "/home/user/Meu-espa-o/geradores")
from design_system import (
    FONT_LINK, CSS_BASE, INK, ACCENT, GRAY, FONTS, LOGO_URI,
    NOISE_B64, html_shell, kicker,
)
from nuc_realism import REALISM_CSS, GRAO_OVERLAY

FOTOS   = Path("/home/user/Meu-espa-o/fotos")
OUTPUT  = Path("/home/user/Meu-espa-o/output")
PREVIEWS = Path("/home/user/Meu-espa-o/previews")
OUTPUT.mkdir(exist_ok=True)
PREVIEWS.mkdir(exist_ok=True)

VW, VH  = 420, 525
SCALE   = 1080 / VW
CHROME  = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

CAPTION = "Teste editorial NUC Vision"

def logo(size=22, top=20):
    return (f'<div style="position:absolute;top:{top}px;left:0;right:0;'
            f'display:flex;justify-content:center;z-index:30;">'
            f'<img src="{LOGO_URI}" style="height:{size}px;width:auto;'
            f'filter:brightness(0) invert(1) drop-shadow(0 2px 10px rgba(0,0,0,0.7));"></div>')


# ── SLIDE 1: GANCHO — tipografia explosiva, dado central, assimetria total ────
def slide_gancho():
    return f'''<div class="slide" style="overflow:hidden;
        background:radial-gradient(ellipse 110% 80% at 8% 90%, #0d1f35 0%, {INK["void"]} 55%, #04060b 100%);">

      <!-- grade de pontos sutil -->
      <div style="position:absolute;inset:0;z-index:0;pointer-events:none;
                  background-image:radial-gradient(circle,rgba(30,197,242,0.06) 1.2px,transparent 1.2px);
                  background-size:28px 28px;"></div>

      <!-- glow ciano canto inferior esquerdo -->
      <div style="position:absolute;bottom:-40px;left:-40px;width:320px;height:320px;z-index:1;
                  background:radial-gradient(circle,rgba(30,197,242,0.18),transparent 66%);
                  filter:blur(18px);pointer-events:none;"></div>

      <!-- linha diagonal decorativa -->
      <div style="position:absolute;top:0;right:120px;width:1px;height:100%;z-index:2;
                  background:linear-gradient(180deg,transparent,rgba(30,197,242,0.20) 30%,rgba(30,197,242,0.20) 70%,transparent);
                  transform:rotate(8deg);transform-origin:top center;"></div>

      {logo()}

      <!-- número gigante de fundo — elemento gráfico, não informação -->
      <div style="position:absolute;top:-18px;right:-12px;z-index:1;
                  font-family:{FONTS['display']},sans-serif;font-size:260px;line-height:1;
                  color:rgba(30,197,242,0.06);letter-spacing:-0.04em;user-select:none;">
        1
      </div>

      <!-- bloco de texto principal — ancorado à esquerda, alto -->
      <div style="position:absolute;top:62px;left:26px;right:26px;z-index:10;">
        <div style="font-family:{FONTS['body']},sans-serif;font-size:9.5px;font-weight:700;
                    letter-spacing:0.22em;text-transform:uppercase;color:{ACCENT['primary']};
                    display:flex;align-items:center;gap:8px;margin-bottom:14px;">
          <div style="width:22px;height:1px;background:{ACCENT['primary']};opacity:0.6;"></div>
          Posicionamento de Marca
        </div>

        <div style="font-family:{FONTS['display']},sans-serif;font-size:52px;line-height:0.88;
                    color:#fff;text-transform:uppercase;letter-spacing:-0.01em;">
          A MARCA<br>QUE
          <span style="background:{ACCENT['primary']};color:#06121c;
                       padding:2px 14px 8px;border-radius:10px;display:inline-block;
                       box-shadow:0 8px 28px rgba(30,197,242,0.5);line-height:0.92;">
            CALA
          </span><br>PERDE.
        </div>
      </div>

      <!-- divisor horizontal -->
      <div style="position:absolute;top:258px;left:26px;right:100px;height:1px;z-index:10;
                  background:linear-gradient(90deg,rgba(30,197,242,0.5),transparent);"></div>

      <!-- stat central -->
      <div style="position:absolute;top:274px;left:26px;z-index:10;">
        <div style="font-family:{FONTS['display']},sans-serif;font-size:72px;line-height:0.86;
                    color:{ACCENT['primary']};letter-spacing:-0.02em;">
          73<span style="font-size:36px;opacity:0.7;">%</span>
        </div>
        <div style="font-family:{FONTS['body']},sans-serif;font-size:11px;font-weight:500;
                    color:rgba(255,255,255,0.5);letter-spacing:0.06em;text-transform:uppercase;
                    margin-top:4px;max-width:200px;line-height:1.4;">
          dos consumidores de luxo escolhem marca pela narrativa, nao pelo produto
        </div>
        <div style="font-family:{FONTS['body']},sans-serif;font-size:9px;font-weight:600;
                    color:rgba(255,255,255,0.25);letter-spacing:0.12em;text-transform:uppercase;
                    margin-top:8px;">
          Fonte: Bain Luxury Report 2025
        </div>
      </div>

      <!-- ponte inferior -->
      <div style="position:absolute;bottom:0;left:0;right:0;z-index:10;padding:0 26px 36px;">
        <div style="display:flex;align-items:flex-start;gap:9px;">
          <div style="width:22px;height:2px;background:{ACCENT['primary']};
                      flex-shrink:0;margin-top:9px;"></div>
          <span style="font-family:{FONTS['body']},sans-serif;font-size:12.5px;
                       font-style:italic;color:{ACCENT['primary']};line-height:1.5;font-weight:500;">
            E a Ferrari acabou de provar isso da pior forma.
          </span>
        </div>
      </div>

      {GRAO_OVERLAY}
    </div>'''


# ── SLIDE 2: DADO — layout Bloomberg, dois stats, sem foto ────────────────────
def slide_dado():
    return f'''<div class="slide" style="overflow:hidden;background:{INK['void']};">

      <!-- faixa de cor no topo — elemento editorial -->
      <div style="position:absolute;top:0;left:0;right:0;height:4px;z-index:20;
                  background:linear-gradient(90deg,{ACCENT['primary']},rgba(30,197,242,0.2));"></div>

      <div style="position:absolute;inset:0;z-index:0;pointer-events:none;
                  background-image:radial-gradient(circle,rgba(255,255,255,0.03) 1px,transparent 1px);
                  background-size:32px 32px;"></div>

      {logo()}

      <!-- label de seção -->
      <div style="position:absolute;top:56px;left:26px;z-index:10;
                  font-family:{FONTS['body']},sans-serif;font-size:9.5px;font-weight:700;
                  letter-spacing:0.22em;text-transform:uppercase;color:{ACCENT['primary']};
                  display:flex;align-items:center;gap:8px;">
        <div style="width:22px;height:1px;background:{ACCENT['primary']};opacity:0.6;"></div>
        Os Numeros
      </div>

      <!-- headline -->
      <div style="position:absolute;top:80px;left:26px;right:26px;z-index:10;">
        <div style="font-family:{FONTS['display']},sans-serif;font-size:38px;line-height:0.9;
                    color:#fff;text-transform:uppercase;">
          O QUE OS<br>DADOS
          <span style="background:{ACCENT['primary']};color:#06121c;
                       padding:1px 12px 6px;border-radius:8px;
                       box-shadow:0 6px 22px rgba(30,197,242,0.45);">REVELAM</span>
        </div>
      </div>

      <!-- dois cards de stat lado a lado -->
      <div style="position:absolute;top:188px;left:26px;right:26px;z-index:10;display:flex;gap:12px;">

        <div style="flex:1;border-left:2px solid {ACCENT['primary']};padding-left:14px;">
          <div style="font-family:{FONTS['display']},sans-serif;font-size:58px;line-height:0.86;
                      color:#fff;letter-spacing:-0.02em;">
            -18<span style="font-size:28px;color:{ACCENT['primary']};">%</span>
          </div>
          <div style="font-family:{FONTS['body']},sans-serif;font-size:10.5px;font-weight:600;
                      color:rgba(255,255,255,0.5);text-transform:uppercase;letter-spacing:0.08em;
                      margin-top:6px;line-height:1.4;">
            Valor de marca Ferrari em 48h apos o lancamento
          </div>
        </div>

        <div style="flex:1;border-left:2px solid rgba(255,255,255,0.15);padding-left:14px;">
          <div style="font-family:{FONTS['display']},sans-serif;font-size:58px;line-height:0.86;
                      color:rgba(255,255,255,0.35);letter-spacing:-0.02em;">
            +12<span style="font-size:28px;color:rgba(255,255,255,0.2);">%</span>
          </div>
          <div style="font-family:{FONTS['body']},sans-serif;font-size:10.5px;font-weight:600;
                      color:rgba(255,255,255,0.25);text-transform:uppercase;letter-spacing:0.08em;
                      margin-top:6px;line-height:1.4;">
            Interesse em Lamborghini no mesmo periodo
          </div>
        </div>

      </div>

      <!-- linha separadora -->
      <div style="position:absolute;top:352px;left:26px;right:26px;height:1px;z-index:10;
                  background:rgba(255,255,255,0.07);"></div>

      <!-- insight textual -->
      <div style="position:absolute;top:366px;left:26px;right:26px;z-index:10;">
        <div style="font-family:{FONTS['body']},sans-serif;font-size:13px;
                    color:rgba(255,255,255,0.62);line-height:1.6;max-width:330px;">
          Nenhuma das duas mudou o carro. Uma mudou a narrativa. A outra deixou a narrativa falar por si.
        </div>
      </div>

      <!-- ponte -->
      <div style="position:absolute;bottom:0;left:0;right:0;z-index:10;padding:0 26px 36px;">
        <div style="display:flex;align-items:flex-start;gap:9px;">
          <div style="width:22px;height:2px;background:{ACCENT['primary']};
                      flex-shrink:0;margin-top:9px;"></div>
          <span style="font-family:{FONTS['body']},sans-serif;font-size:12.5px;
                       font-style:italic;color:{ACCENT['primary']};line-height:1.5;font-weight:500;">
            Mas quem realmente ganhou nao foi nenhuma das duas.
          </span>
        </div>
      </div>

      {GRAO_OVERLAY}
    </div>'''


# ── SLIDE 3: REVELAÇÃO — tipografia de manifesto, sem foto, impacto maximo ───
def slide_revelacao():
    return f'''<div class="slide" style="overflow:hidden;
        background:radial-gradient(ellipse 100% 70% at 50% 100%, #0a1e14 0%, {INK['void']} 60%, #030509 100%);">

      <div style="position:absolute;inset:0;z-index:0;pointer-events:none;
                  background-image:radial-gradient(circle,rgba(30,197,242,0.04) 1.2px,transparent 1.2px);
                  background-size:28px 28px;"></div>

      <!-- glow verde/ciano embaixo -->
      <div style="position:absolute;bottom:-60px;left:50%;transform:translateX(-50%);
                  width:380px;height:280px;z-index:1;
                  background:radial-gradient(ellipse,rgba(30,197,242,0.15),transparent 66%);
                  filter:blur(20px);pointer-events:none;"></div>

      {logo()}

      <div style="position:absolute;top:56px;left:26px;z-index:10;
                  font-family:{FONTS['body']},sans-serif;font-size:9.5px;font-weight:700;
                  letter-spacing:0.22em;text-transform:uppercase;color:{ACCENT['primary']};
                  display:flex;align-items:center;gap:8px;">
        <div style="width:22px;height:1px;background:{ACCENT['primary']};opacity:0.6;"></div>
        A Revelacao
      </div>

      <!-- citacao enorme centralizada -->
      <div style="position:absolute;top:92px;left:26px;right:26px;z-index:10;">

        <!-- aspas decorativas -->
        <div style="font-family:{FONTS['display']},sans-serif;font-size:100px;line-height:0.6;
                    color:{ACCENT['primary']};opacity:0.2;margin-bottom:-8px;">"</div>

        <div style="font-family:{FONTS['display']},sans-serif;font-size:36px;line-height:0.95;
                    color:#fff;text-transform:uppercase;letter-spacing:-0.01em;">
          VELOCIDADE<br>VENDE
          <span style="background:{ACCENT['primary']};color:#06121c;
                       padding:2px 12px 7px;border-radius:8px;
                       box-shadow:0 6px 22px rgba(30,197,242,0.5);">CARRO.</span><br>
          HISTORIA<br>VENDE
          <span style="font-style:normal;color:{ACCENT['primary']};"> MARCA.</span>
        </div>
      </div>

      <!-- linha divisora -->
      <div style="position:absolute;top:326px;left:26px;width:60px;height:2px;z-index:10;
                  background:{ACCENT['primary']};opacity:0.6;"></div>

      <!-- atribuicao -->
      <div style="position:absolute;top:342px;left:26px;right:26px;z-index:10;">
        <div style="font-family:{FONTS['body']},sans-serif;font-size:11px;
                    color:rgba(255,255,255,0.4);letter-spacing:0.1em;text-transform:uppercase;">
          NUC Vision — Analise de Mercado de Luxo
        </div>
      </div>

      <!-- texto de insight -->
      <div style="position:absolute;top:374px;left:26px;right:26px;z-index:10;">
        <div style="font-family:{FONTS['body']},sans-serif;font-size:13px;
                    color:rgba(255,255,255,0.6);line-height:1.6;max-width:330px;">
          Qualquer concorrente pode superar seu produto. Ninguem pode superar o que as pessoas sentem ao ver sua marca.
        </div>
      </div>

      <!-- CTA -->
      <div style="position:absolute;bottom:0;left:0;right:0;z-index:10;padding:0 26px 38px;">
        <div style="display:inline-block;background:{ACCENT['primary']};color:#06121c;
                    font-family:{FONTS['body']},sans-serif;font-size:12px;font-weight:700;
                    letter-spacing:0.12em;text-transform:uppercase;
                    padding:14px 28px;border-radius:999px;
                    box-shadow:0 10px 30px rgba(30,197,242,0.45);">
          Salva esse post
        </div>
      </div>

      {GRAO_OVERLAY}
    </div>'''


# ── MONTAGEM ──────────────────────────────────────────────────────────────────
SLIDES = [slide_gancho, slide_dado, slide_revelacao]
NOMES  = ["s1_gancho", "s2_dado", "s3_revelacao"]
TOTAL  = len(SLIDES)

def build_html():
    inner = "\n".join(fn() for fn in SLIDES)
    base = html_shell(inner, TOTAL, CAPTION)
    return base.replace(
        f"<style>{CSS_BASE}</style>",
        f"<style>{CSS_BASE}\n{REALISM_CSS}\n"
        f".display{{font-family:{FONTS['display']},sans-serif;text-transform:uppercase;}}</style>"
    )

async def export():
    OUT_DIR = OUTPUT / "editorial-test"
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    html = build_html()
    html_path = PREVIEWS / "editorial-test.html"
    html_path.write_text(html, encoding="utf-8")

    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        browser = await p.chromium.launch(executable_path=CHROME)
        page = await browser.new_page(
            viewport={"width": VW, "height": VH},
            device_scale_factor=SCALE,
        )
        await page.set_content(html, wait_until="networkidle")
        await page.wait_for_timeout(2500)

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
            await page.wait_for_timeout(350)
            out = OUT_DIR / f"slide_{i+1:02d}_{NOMES[i]}.png"
            await page.screenshot(
                path=str(out),
                clip={"x": 0, "y": 0, "width": VW, "height": VH},
            )
            print(f"  {i+1}/{TOTAL} -> {out.name}")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(export())
    print("Pronto!")
