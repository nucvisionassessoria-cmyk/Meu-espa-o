#!/usr/bin/env python3
"""
NUC Vision — Carrossel Trend: Ferrari vs Lamborghini
Formato: 420×525px → exportado a 1080×1350px
"""
import sys, base64
from pathlib import Path
sys.path.insert(0, "/home/user/Meu-espa-o")
from design_system import (
    FONT_LINK, CSS_BASE, INK, PAPER, ACCENT, GRAY,
    FONTS, TYPE, TRACK, LINE, RADIUS, SHADOW,
    LOGO_URI, NOISE_B64,
    overlay_noise, overlay_vignette, logo_mark,
    ig_frame_open, ig_frame_close, html_shell,
)

FOTOS = Path("/home/user/Meu-espa-o/fotos")
TOTAL = 9
CAPTION = ("A Ferrari perdeu R$ 30 bilhões em valor de mercado em um dia. "
           "A Lamborghini não fez nada — e saiu na frente. "
           "Desliza e entende o que isso revela sobre posicionamento de verdade. 👇 "
           "#posicionamento #marketing #ferrari #lamborghini #nucvision #estrategia")

# ── helpers ────────────────────────────────────────────────────────────────────

def photo_uri(name):
    p = FOTOS / name
    ext = p.suffix.lower().lstrip(".")
    mime = {"jpg":"jpeg","jpeg":"jpeg","png":"png","webp":"webp"}.get(ext,"jpeg")
    return f"data:image/{mime};base64,{base64.b64encode(p.read_bytes()).decode()}"

def noise(op=0.32, z=2):
    return (f'<div style="position:absolute;inset:0;z-index:{z};'
            f'background-image:url(\'data:image/svg+xml;base64,{NOISE_B64}\');'
            f'background-size:240px 240px;opacity:{op};mix-blend-mode:overlay;pointer-events:none;"></div>')

def logo(white=True, size=22, top=20):
    flt = "filter:brightness(0) invert(1) drop-shadow(0 2px 10px rgba(0,0,0,0.7));" if white else ""
    return (f'<div style="position:absolute;top:{top}px;left:0;right:0;'
            f'display:flex;justify-content:center;z-index:20;">'
            f'<img src="{LOGO_URI}" style="height:{size}px;width:auto;{flt}"></div>')

def kicker(text):
    return (f'<div style="font-family:{FONTS["body"]},sans-serif;font-size:10px;'
            f'font-weight:700;letter-spacing:0.2em;text-transform:uppercase;'
            f'color:{ACCENT["primary"]};margin-bottom:10px;">{text}</div>')

def pill(word, size=46):
    return (f'<span class="display" style="display:inline-block;'
            f'background:{ACCENT["primary"]};color:#fff;padding:2px 18px 8px;'
            f'border-radius:12px;font-size:{size}px;'
            f'box-shadow:0 4px 24px rgba(30,197,242,0.5);">{word}</span>')

def hr(w=44, mt=14):
    return (f'<div style="width:{w}px;height:2px;background:{ACCENT["primary"]};'
            f'border-radius:2px;margin-top:{mt}px;"></div>')

def dot_grid(color="rgba(30,197,242,0.07)", sp=28, z=0):
    return (f'<div style="position:absolute;inset:0;z-index:{z};'
            f'background-image:radial-gradient(circle,{color} 1.2px,transparent 1.2px);'
            f'background-size:{sp}px {sp}px;"></div>')

def comment_bubble(text, highlight=False, max_w=205):
    """Simula um print de comentário viral — estilo rede social.
    highlight=True aplica grifo amarelo de marca-texto atrás das palavras."""
    hl = ("background:linear-gradient(transparent 12%,#FFE600 12%,#FFE600 88%,transparent 88%);"
          "box-decoration-break:clone;-webkit-box-decoration-break:clone;"
          "padding:0 1px;") if highlight else ""
    return (
        f'<div style="background:#fff;border-radius:14px;padding:12px 15px;'
        f'max-width:{max_w}px;box-shadow:0 10px 36px rgba(0,0,0,0.5);">'
        f'<div style="display:flex;align-items:center;gap:8px;margin-bottom:8px;">'
        f'<div style="width:26px;height:26px;border-radius:50%;'
        f'background:#cfcfcf;filter:blur(0.5px);flex-shrink:0;"></div>'
        f'<div style="width:96px;height:9px;background:#d4d4d4;border-radius:4px;filter:blur(1.2px);"></div>'
        f'</div>'
        f'<div style="font-family:{FONTS["body"]},sans-serif;font-size:13px;'
        f'color:#111;line-height:1.5;font-weight:600;">'
        f'<span style="{hl}">{text}</span></div>'
        f'</div>'
    )


# ── SLIDE 1 — HOOK com foto do Hamilton ────────────────────────────────────────

def slide1():
    hamilton = photo_uri("hamilton_cutout.png")

    bubble = comment_bubble(
        "Enzo Ferrari deve estar se revirando no túmulo neste exato momento.",
        highlight=True, max_w=215,
    )

    return f'''<div class="slide" style="overflow:hidden;
        background:radial-gradient(ellipse 120% 90% at 50% 30%,#1A0A0E 0%,#0A0A12 45%,#040509 100%);">

      {dot_grid(color="rgba(255,255,255,0.045)", z=0)}

      <!-- glow vermelho dramático (clima Ferrari) atrás dele -->
      <div style="position:absolute;top:40px;left:50%;transform:translateX(-50%);
                  width:360px;height:320px;z-index:0;
                  background:radial-gradient(ellipse,rgba(196,30,40,0.30),transparent 68%);
                  filter:blur(14px);"></div>

      <!-- HAMILTON recortado — rosto + mãos no topo, corpo descendo -->
      <div style="position:absolute;top:34px;left:50%;transform:translateX(-50%);
                  width:102%;z-index:1;">
        <img src="{hamilton}"
             style="width:100%;display:block;
                    filter:grayscale(1) contrast(1.12) brightness(1.0)
                           drop-shadow(0 12px 40px rgba(0,0,0,0.6));">
      </div>

      <!-- fade inferior para o título respirar sobre o corpo -->
      <div style="position:absolute;bottom:0;left:0;right:0;height:50%;z-index:2;
                  background:linear-gradient(180deg,transparent 0%,
                    rgba(4,5,9,0.55) 40%,rgba(4,5,9,0.95) 72%,#040509 100%);"></div>

      {noise(0.14, z=3)}
      {logo()}

      <!-- comentário viral grifado — sobre o peito, rosto livre -->
      <div style="position:absolute;top:212px;left:14px;z-index:12;">
        {bubble}
      </div>

      <!-- TÍTULO GIGANTE embaixo -->
      <div style="position:absolute;bottom:0;left:0;right:0;z-index:11;padding:0 22px 38px;">
        <div class="display" style="font-size:40px;color:#fff;line-height:0.92;
                    text-shadow:0 4px 30px rgba(0,0,0,0.8);">ABSOLUTE</div>
        <div class="display" style="font-size:62px;color:#fff;line-height:0.86;
                    margin-bottom:18px;text-shadow:0 4px 30px rgba(0,0,0,0.8);">
          DECEP<span style="color:{ACCENT["primary"]};">ÇÃO</span>
        </div>
        <div style="display:inline-flex;align-items:center;gap:8px;
                    background:rgba(255,255,255,0.10);border:1px solid rgba(255,255,255,0.30);
                    padding:9px 20px;border-radius:999px;backdrop-filter:blur(8px);">
          <span style="font-family:{FONTS["body"]},sans-serif;font-size:12px;
                       color:#fff;font-weight:700;letter-spacing:0.08em;">
            PASSE PARA O LADO ››
          </span>
        </div>
      </div>
    </div>'''


# ── SLIDE 2 — O que aconteceu ──────────────────────────────────────────────────

def slide2():
    return f'''<div class="slide" style="background:{INK["deep"]};">
      {dot_grid()}
      {noise()}
      {logo()}
      <div style="position:absolute;top:58px;left:0;right:0;bottom:0;
                  display:flex;flex-direction:column;justify-content:center;
                  padding:0 28px;z-index:10;">
        {kicker("O Que Aconteceu")}
        <div class="display" style="font-size:46px;color:#fff;margin-bottom:16px;">
          26 DE MAIO<br>DE 2026.
        </div>
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:14px;
                    color:rgba(255,255,255,0.72);line-height:1.65;">
          A Ferrari lança o <strong style="color:#fff;">Luce</strong> —
          primeiro carro elétrico da marca, a €550 mil.<br><br>
          Design feito com o ex-chefe de design da Apple.<br><br>
          Resultado: comparado a Nissan nas redes.
          O ex-CEO disse que estavam
          <strong style="color:{ACCENT["primary"]};">"destruindo uma lenda".</strong>
          Ações caíram <strong style="color:{ACCENT["primary"]};">8%</strong> em 24h.
        </div>
        {hr(44, 20)}
      </div>
      {overlay_vignette(0.3, z=3)}
    </div>'''


# ── SLIDE 3 — O ponto que ninguém viu ─────────────────────────────────────────

def slide3():
    p = pill("MERCADO.", 36)
    return f'''<div class="slide" style="background:{INK["void"]};">
      {noise(0.28)}
      <!-- linha ciano vertical no centro -->
      <div style="position:absolute;left:50%;top:0;bottom:0;width:1px;
                  background:linear-gradient(180deg,transparent 5%,
                  {ACCENT["primary"]} 25%,{ACCENT["primary"]} 75%,transparent 95%);
                  transform:translateX(-50%);z-index:5;opacity:0.4;"></div>
      {logo()}
      <div style="position:absolute;top:58px;left:0;right:0;bottom:0;
                  display:flex;flex-direction:column;justify-content:center;
                  padding:0 28px;z-index:10;">
        {kicker("A Virada")}
        <div class="display" style="font-size:38px;color:rgba(255,255,255,0.35);
                    line-height:1;margin-bottom:12px;">
          ISSO NÃO É<br>SÓ POLÊMICA.
        </div>
        <div class="display" style="font-size:38px;color:#fff;line-height:1;margin-bottom:20px;">
          É UMA AULA DE {p}
        </div>
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:13.5px;
                    color:rgba(255,255,255,0.58);line-height:1.6;">
          O que aconteceu com a Ferrari revela algo
          muito maior do que uma decisão de design ruim.
        </div>
      </div>
      {overlay_vignette(0.35, z=3)}
    </div>'''


# ── SLIDE 4 — Leitura estratégica ─────────────────────────────────────────────

def slide4():
    return f'''<div class="slide" style="background:{INK["rich"]};">
      {dot_grid("rgba(30,197,242,0.06)", 36)}
      {noise()}
      {logo()}
      <div style="position:absolute;top:58px;left:0;right:0;bottom:0;
                  display:flex;flex-direction:column;justify-content:center;
                  padding:0 28px;z-index:10;">
        {kicker("Leitura Estratégica")}
        <div class="display" style="font-size:40px;color:#fff;
                    line-height:0.95;margin-bottom:20px;">
          A FERRARI<br>ABRIU MÃO<br>DA SUA<br>
          <span style="color:{ACCENT["primary"]};">ESSÊNCIA.</span>
        </div>
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:13.5px;
                    color:rgba(255,255,255,0.65);line-height:1.65;">
          Não foi um erro de design.<br>
          Foi uma decisão de abandonar o posicionamento
          que construiu décadas de valor de marca —
          sob pressão de uma tendência de mercado.
        </div>
        {hr(44, 18)}
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:12px;
                    color:{ACCENT["primary"]};font-weight:600;margin-top:12px;">
          O mercado sentiu. E reagiu na hora.
        </div>
      </div>
      {overlay_vignette(0.28, z=3)}
    </div>'''


# ── SLIDE 5 — Lamborghini capitaliza ──────────────────────────────────────────

def slide5():
    # cards de comparação
    card_ferrari = (
        f'<div style="flex:1;background:rgba(255,80,80,0.08);border:1px solid rgba(255,80,80,0.25);'
        f'border-radius:12px;padding:14px 12px;">'
        f'<div style="font-family:{FONTS["body"]},sans-serif;font-size:9px;font-weight:700;'
        f'letter-spacing:0.2em;color:rgba(255,80,80,0.8);text-transform:uppercase;margin-bottom:8px;">FERRARI</div>'
        f'<div style="font-family:{FONTS["body"]},sans-serif;font-size:12px;'
        f'color:rgba(255,255,255,0.65);line-height:1.5;">'
        f'Lança o Luce.<br>Tenta seguir a tendência.<br>Perde 8% em bolsa.</div>'
        f'<div style="font-size:20px;margin-top:10px;">📉</div>'
        f'</div>'
    )
    card_lambo = (
        f'<div style="flex:1;background:rgba(30,197,242,0.08);border:1px solid rgba(30,197,242,0.25);'
        f'border-radius:12px;padding:14px 12px;">'
        f'<div style="font-family:{FONTS["body"]},sans-serif;font-size:9px;font-weight:700;'
        f'letter-spacing:0.2em;color:{ACCENT["primary"]};text-transform:uppercase;margin-bottom:8px;">LAMBORGHINI</div>'
        f'<div style="font-family:{FONTS["body"]},sans-serif;font-size:12px;'
        f'color:rgba(255,255,255,0.65);line-height:1.5;">'
        f'Cancela seu EV.<br>Diz que foi a decisão certa.<br>Sai na frente.</div>'
        f'<div style="font-size:20px;margin-top:10px;">📈</div>'
        f'</div>'
    )

    return f'''<div class="slide" style="background:{INK["void"]};">
      {noise(0.3)}
      {logo()}
      <div style="position:absolute;top:58px;left:0;right:0;bottom:0;
                  display:flex;flex-direction:column;justify-content:center;
                  padding:0 24px;z-index:10;">
        {kicker("No Dia Seguinte")}
        <div class="display" style="font-size:36px;color:#fff;
                    line-height:0.95;margin-bottom:8px;">
          A LAMBORGHINI<br>FEZ UM ÚNICO<br>
          <span style="color:{ACCENT["primary"]};">MOVIMENTO.</span>
        </div>
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:12.5px;
                    color:rgba(255,255,255,0.55);margin-bottom:18px;line-height:1.5;">
          Sem campanha. Sem investimento. Sem anúncio.<br>
          Só uma frase do CEO: <em style="color:#fff;">"cancelar nosso elétrico foi a decisão certa."</em>
        </div>
        <div style="display:flex;gap:10px;">{card_ferrari}{card_lambo}</div>
      </div>
      {overlay_vignette(0.3, z=3)}
    </div>'''


# ── SLIDE 6 — Quebra de crença ────────────────────────────────────────────────

def slide6():
    def item_riscado(t):
        return (
            f'<div style="display:flex;align-items:center;gap:10px;margin-bottom:10px;">'
            f'<div style="width:18px;height:18px;border-radius:4px;background:rgba(255,80,80,0.2);'
            f'border:1px solid rgba(255,80,80,0.4);display:flex;align-items:center;'
            f'justify-content:center;font-size:10px;color:rgba(255,80,80,0.8);flex-shrink:0;">✕</div>'
            f'<span style="font-family:{FONTS["body"]},sans-serif;font-size:13px;'
            f'color:rgba(255,255,255,0.35);text-decoration:line-through;">{t}</span>'
            f'</div>'
        )
    items  = item_riscado("Posicionamento é slogan")
    items += item_riscado("Posicionamento é identidade visual")
    items += item_riscado("Posicionamento é se modernizar sempre")

    return f'''<div class="slide" style="background:{INK["deep"]};">
      {dot_grid("rgba(30,197,242,0.05)", 32)}
      {noise(0.28)}
      {logo()}
      <div style="position:absolute;top:58px;left:0;right:0;bottom:0;
                  display:flex;flex-direction:column;justify-content:center;
                  padding:0 28px;z-index:10;">
        {kicker("A Quebra de Crença")}
        <div class="display" style="font-size:36px;color:#fff;
                    line-height:0.95;margin-bottom:20px;">
          POSICIONAMENTO<br>NÃO É ISSO:
        </div>
        {items}
        <div style="margin-top:18px;padding:14px 16px;
                    background:rgba(30,197,242,0.08);border-radius:12px;
                    border:1px solid rgba(30,197,242,0.2);">
          <div style="font-family:{FONTS["body"]},sans-serif;font-size:13.5px;
                      color:#fff;line-height:1.55;font-weight:500;">
            Posicionamento é saber o que você <strong>não abre mão de ser</strong>
            — nem quando o mercado pressiona.
          </div>
        </div>
      </div>
      {overlay_vignette(0.3, z=3)}
    </div>'''


# ── SLIDE 7 — Insight forte ───────────────────────────────────────────────────

def slide7():
    return f'''<div class="slide" style="background:{INK["void"]};">
      {noise(0.25)}
      <!-- glow radial central -->
      <div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);
                  width:340px;height:340px;
                  background:radial-gradient(circle,rgba(30,197,242,0.12) 0%,transparent 65%);
                  z-index:1;pointer-events:none;"></div>
      {logo()}
      <div style="position:absolute;top:0;left:0;right:0;bottom:0;
                  display:flex;flex-direction:column;align-items:center;
                  justify-content:center;padding:0 28px;z-index:10;text-align:center;">
        <div class="display" style="font-size:48px;color:#fff;
                    line-height:0.92;margin-bottom:16px;">
          QUEM TEM<br>POSICIONAMENTO<br>CLARO
        </div>
        <div class="display" style="font-size:36px;line-height:1;">
          NÃO PRECISA DE<br>{pill("CAMPANHA", 34)}<br>
          <span style="font-size:36px;color:#fff;">PARA SE DEFENDER.</span>
        </div>
      </div>
      {overlay_vignette(0.4, z=3)}
    </div>'''


# ── SLIDE 8 — Fechamento forte ────────────────────────────────────────────────

def slide8():
    return f'''<div class="slide" style="background:{INK["deep"]};">
      {dot_grid("rgba(30,197,242,0.06)", 30)}
      {noise(0.3)}
      {logo()}
      <div style="position:absolute;top:58px;left:0;right:0;bottom:0;
                  display:flex;flex-direction:column;justify-content:center;
                  padding:0 28px;z-index:10;">
        {kicker("O Que Esse Case Revela")}
        <div class="display" style="font-size:42px;color:#fff;
                    line-height:0.95;margin-bottom:20px;">
          MARCA FORTE<br>NÃO SEGUE<br>TODA {pill("TENDÊNCIA.", 36)}
        </div>
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:13.5px;
                    color:rgba(255,255,255,0.62);line-height:1.65;">
          A Ferrari tentou modernizar e perdeu o que tinha de mais valioso:
          a certeza de que um Ferrari só pode ser um Ferrari.<br><br>
          A Lamborghini sabia quem era. E ganhou sem fazer nada.
        </div>
        {hr(44, 18)}
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:12px;
                    color:rgba(255,255,255,0.38);margin-top:12px;">
          Isso vale pra qualquer empresa — do supercarro à padaria da esquina.
        </div>
      </div>
      {overlay_vignette(0.3, z=3)}
    </div>'''


# ── SLIDE 9 — CTA ─────────────────────────────────────────────────────────────

def slide9():
    return f'''<div class="slide" style="background:linear-gradient(155deg,{INK["rich"]} 0%,#0A1628 55%,{INK["void"]} 100%);">
      {noise(0.28)}
      <!-- glow topo -->
      <div style="position:absolute;top:-60px;left:50%;transform:translateX(-50%);
                  width:260px;height:200px;
                  background:radial-gradient(ellipse,rgba(30,197,242,0.18) 0%,transparent 70%);
                  z-index:1;pointer-events:none;"></div>
      {logo(size=26)}
      <div style="position:absolute;top:0;left:0;right:0;bottom:0;
                  display:flex;flex-direction:column;align-items:center;
                  justify-content:center;padding:0 28px;z-index:10;text-align:center;">
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:11px;font-weight:700;
                    letter-spacing:0.22em;text-transform:uppercase;
                    color:{ACCENT["primary"]};margin-bottom:14px;">@nucvision</div>
        <div class="display" style="font-size:34px;color:#fff;
                    line-height:1;margin-bottom:8px;">
          LEITURAS ASSIM
        </div>
        <div class="display" style="font-size:34px;color:{ACCENT["primary"]};
                    margin-bottom:24px;">TODO SEMANA.</div>
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:13px;
                    color:rgba(255,255,255,0.5);margin-bottom:28px;line-height:1.5;">
          Siga a NUC Vision para acompanhar leituras<br>
          estratégicas sobre marcas, mercado e posicionamento.
        </div>
        <div style="background:{ACCENT["primary"]};color:#fff;
                    font-family:{FONTS["body"]},sans-serif;font-size:13px;font-weight:700;
                    letter-spacing:0.1em;text-transform:uppercase;
                    padding:13px 32px;border-radius:999px;
                    box-shadow:0 6px 28px rgba(30,197,242,0.45);">
          SEGUIR AGORA
        </div>
      </div>
      {overlay_vignette(0.3, z=3)}
    </div>'''


# ── Assembly ───────────────────────────────────────────────────────────────────

def main():
    slides = "".join([
        slide1(), slide2(), slide3(), slide4(), slide5(),
        slide6(), slide7(), slide8(), slide9(),
    ])
    html = html_shell(slides, TOTAL, CAPTION)
    out = Path("/home/user/Meu-espa-o/previews/nucvision-ferrari-lambo.html")
    out.write_text(html, encoding="utf-8")
    print(f"✓ {out}")

if __name__ == "__main__":
    main()
