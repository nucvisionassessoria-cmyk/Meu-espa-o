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
        background:radial-gradient(ellipse 130% 100% at 50% 32%,#241016 0%,#12101C 45%,#0B0D16 100%);">

      {dot_grid(color="rgba(255,255,255,0.06)", z=0)}

      <!-- glow vermelho dramático (clima Ferrari) atrás dele -->
      <div style="position:absolute;top:40px;left:50%;transform:translateX(-50%);
                  width:360px;height:320px;z-index:0;
                  background:radial-gradient(ellipse,rgba(196,30,40,0.30),transparent 68%);
                  filter:blur(14px);"></div>

      <!-- HAMILTON — dissolve nas laterais e embaixo, sem borda dura -->
      <div style="position:absolute;top:34px;left:50%;transform:translateX(-50%);
                  width:102%;z-index:1;
                  -webkit-mask-image:linear-gradient(to bottom,
                    black 0%, black 55%, transparent 85%),
                    linear-gradient(to right,
                    transparent 0%, black 8%, black 92%, transparent 100%);
                  -webkit-mask-composite:destination-in;
                  mask-image:linear-gradient(to bottom,
                    black 0%, black 55%, transparent 85%),
                    linear-gradient(to right,
                    transparent 0%, black 8%, black 92%, transparent 100%);
                  mask-composite:intersect;">
        <img src="{hamilton}"
             style="width:100%;display:block;
                    filter:grayscale(1) contrast(1.12) brightness(1.0);">
      </div>

      <!-- fade inferior para o título respirar sobre o corpo -->
      <div style="position:absolute;bottom:0;left:0;right:0;height:50%;z-index:2;
                  background:linear-gradient(180deg,transparent 0%,
                    rgba(11,13,22,0.55) 40%,rgba(11,13,22,0.95) 72%,#0B0D16 100%);"></div>

      <!-- halo de luz atrás do carro (mata o bloco preto chapado) -->
      <div style="position:absolute;bottom:120px;right:-40px;z-index:3;
                  width:320px;height:260px;
                  background:radial-gradient(ellipse at 55% 50%,
                    rgba(90,170,225,0.30) 0%,rgba(90,170,225,0.10) 38%,transparent 70%);
                  filter:blur(8px);pointer-events:none;"></div>

      <!-- FERRARI LUCE flutuando (em cor, contrastando com o P&B) -->
      <div style="position:absolute;bottom:150px;right:-26px;z-index:4;width:236px;
                  transform:rotate(-7deg);
                  -webkit-mask-image:radial-gradient(ellipse 82% 82% at 50% 50%,#000 62%,transparent 92%);
                  mask-image:radial-gradient(ellipse 82% 82% at 50% 50%,#000 62%,transparent 92%);
                  filter:drop-shadow(0 10px 30px rgba(0,0,0,0.55))
                         drop-shadow(0 0 26px rgba(70,160,220,0.35));">
        <img src="{photo_uri('FERRARI_LUCE_FRONT_3Q_16x9_RGB_WEB_SOCIALS_1920x1080-1000x1000.png')}" style="width:100%;display:block;">
      </div>

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
    luce = photo_uri("ferrari_luce_trim.png")
    return f'''<div class="slide" style="overflow:hidden;
        background:linear-gradient(165deg,#141826 0%,{INK["deep"]} 52%,#0A0C16 100%);">
      {dot_grid(color="rgba(255,255,255,0.05)")}
      {logo()}

      <!-- ZONA 1 · KICKER (topo, abaixo do logo) -->
      <div style="position:absolute;top:60px;left:28px;right:28px;z-index:10;">
        {kicker("O Que Aconteceu · 26 Mai 2026")}
      </div>

      <!-- ZONA 2 · CARRO (terço central, respirando) -->
      <div style="position:absolute;top:142px;left:50%;transform:translateX(-50%);
                  width:300px;height:140px;z-index:0;
                  background:radial-gradient(ellipse at 50% 55%,
                    rgba(90,170,225,0.26),transparent 66%);filter:blur(6px);"></div>
      <div style="position:absolute;top:120px;left:50%;transform:translateX(-50%);
                  width:300px;z-index:2;
                  filter:drop-shadow(0 16px 30px rgba(0,0,0,0.45));">
        <img src="{luce}" style="width:100%;display:block;">
      </div>

      <!-- ZONA 3 · TEXTO (base, sem sobrepor o carro) -->
      <div style="position:absolute;left:0;right:0;bottom:0;height:46%;z-index:8;
                  background:linear-gradient(180deg,transparent 0%,
                    rgba(10,12,22,0.55) 26%,#0A0C16 58%);"></div>
      <div style="position:absolute;left:0;right:0;bottom:0;padding:0 32px 52px;z-index:10;">
        <div class="display" style="font-size:40px;color:#fff;line-height:0.92;margin-bottom:14px;">
          A FERRARI LANÇOU<br>A <span style="background:{ACCENT["primary"]};color:#06121c;
              padding:0 12px 4px;border-radius:8px;
              box-shadow:0 4px 20px rgba(30,197,242,0.45);">LUCE</span>
        </div>
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:13.5px;
                    color:rgba(255,255,255,0.76);line-height:1.62;max-width:320px;">
          Primeiro carro elétrico da marca, a €550 mil, desenhado com o
          ex-chefe de design da Apple. Resultado: comparado a Nissan nas redes,
          acusado de <strong style="color:#fff;">"destruir uma lenda"</strong> —
          e ações caindo <strong style="color:{ACCENT["primary"]};">8% em 24h</strong>.
        </div>
      </div>
    </div>'''


# ── SLIDE 3 — O ponto que ninguém viu ─────────────────────────────────────────

def slide3():
    luce = photo_uri("ferrari_luce_trim.png")
    return f'''<div class="slide" style="overflow:hidden;background:{INK["void"]};">
      {dot_grid(color="rgba(255,255,255,0.04)")}
      {logo()}

      <!-- ZONA 1 · KICKER -->
      <div style="position:absolute;top:60px;left:28px;z-index:10;">
        {kicker("A Virada")}
      </div>

      <!-- ZONA 2 · LUCE full-bleed com overlay pesado, serve de fundo -->
      <div style="position:absolute;top:0;left:0;right:0;bottom:0;z-index:1;overflow:hidden;">
        <div style="position:absolute;top:80px;left:50%;transform:translateX(-52%) rotate(-8deg);
                    width:460px;opacity:0.35;filter:grayscale(1) contrast(1.1);">
          <img src="{luce}" style="width:100%;display:block;">
        </div>
        <!-- overlay que deixa os 40% de cima e de baixo escuros -->
        <div style="position:absolute;inset:0;
                    background:linear-gradient(180deg,
                      {INK["void"]} 12%,transparent 38%,transparent 58%,{INK["void"]} 86%);"></div>
      </div>

      <!-- ZONA 3 · TEXTO centralizado, por cima do overlay -->
      <div style="position:absolute;top:0;left:0;right:0;bottom:0;
                  display:flex;flex-direction:column;justify-content:center;
                  padding:0 28px;z-index:10;">
        <div class="display" style="font-size:38px;color:rgba(255,255,255,0.28);
                    line-height:1;margin-bottom:10px;">
          ISSO NÃO É<br>SÓ POLÊMICA.
        </div>
        <div style="width:44px;height:2px;background:{ACCENT["primary"]};
                    border-radius:2px;margin-bottom:10px;"></div>
        <div class="display" style="font-size:38px;color:#fff;line-height:1;margin-bottom:20px;">
          É UMA AULA DE<br><span style="background:{ACCENT["primary"]};color:#06121c;
            padding:0 12px 4px;border-radius:8px;">MERCADO.</span>
        </div>
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:13.5px;
                    color:rgba(255,255,255,0.56);line-height:1.6;max-width:300px;">
          O que aconteceu com a Ferrari revela algo
          muito maior do que uma decisão de design ruim.
        </div>
      </div>
    </div>'''


# ── SLIDE 4 — Leitura estratégica ─────────────────────────────────────────────

def slide4():
    ferrari_c = photo_uri("ferrari_classic_trim.png")
    luce      = photo_uri("ferrari_luce_trim.png")
    return f'''<div class="slide" style="overflow:hidden;
        background:linear-gradient(160deg,#1A0608 0%,{INK["rich"]} 50%,#0A0C18 100%);">
      {dot_grid("rgba(255,255,255,0.04)")}
      {logo()}

      <!-- ZONA 1 · KICKER -->
      <div style="position:absolute;top:60px;left:28px;z-index:10;">
        {kicker("Leitura Estratégica")}
      </div>

      <!-- ZONA 2 · DOIS CARROS lado a lado (antes × depois) -->
      <!-- halos -->
      <div style="position:absolute;top:108px;left:16px;width:180px;height:120px;z-index:1;
                  background:radial-gradient(ellipse,rgba(220,50,50,0.32),transparent 70%);
                  filter:blur(8px);"></div>
      <div style="position:absolute;top:120px;right:10px;width:160px;height:100px;z-index:1;
                  background:radial-gradient(ellipse,rgba(90,170,225,0.22),transparent 70%);
                  filter:blur(8px);"></div>

      <!-- Ferrari clássica — esquerda, maior -->
      <div style="position:absolute;top:88px;left:-20px;width:260px;z-index:2;
                  filter:drop-shadow(0 10px 24px rgba(0,0,0,0.55));">
        <img src="{ferrari_c}" style="width:100%;display:block;">
      </div>
      <!-- label ANTES -->
      <div style="position:absolute;top:200px;left:16px;z-index:4;
                  font-family:{FONTS["body"]},sans-serif;font-size:9px;font-weight:700;
                  letter-spacing:0.18em;color:rgba(220,80,80,0.85);text-transform:uppercase;">
        A ESSÊNCIA
      </div>

      <!-- Luce — direita, menor e acinzentada -->
      <div style="position:absolute;top:136px;right:-14px;width:200px;z-index:2;
                  filter:grayscale(0.6) brightness(0.75) drop-shadow(0 8px 20px rgba(0,0,0,0.5));">
        <img src="{luce}" style="width:100%;display:block;">
      </div>
      <!-- label DEPOIS -->
      <div style="position:absolute;top:220px;right:14px;z-index:4;
                  font-family:{FONTS["body"]},sans-serif;font-size:9px;font-weight:700;
                  letter-spacing:0.18em;color:rgba(150,150,180,0.75);text-transform:uppercase;">
        A APOSTA
      </div>

      <!-- ZONA 3 · TEXTO base -->
      <div style="position:absolute;left:0;right:0;bottom:0;height:44%;z-index:8;
                  background:linear-gradient(180deg,transparent,rgba(10,12,24,0.7) 36%,#0A0C18 65%);"></div>
      <div style="position:absolute;left:0;right:0;bottom:0;padding:0 32px 52px;z-index:10;">
        <div class="display" style="font-size:38px;color:#fff;line-height:0.92;margin-bottom:12px;">
          A FERRARI ABRIU MÃO<br>DA <span style="background:{ACCENT["primary"]};color:#06121c;
              padding:0 10px 4px;border-radius:8px;">ESSÊNCIA.</span>
        </div>
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:13.5px;
                    color:rgba(255,255,255,0.66);line-height:1.6;max-width:300px;">
          Não foi erro de design. Foi abrir mão do posicionamento sob pressão.
          <strong style="color:{ACCENT["primary"]};">O mercado sentiu na hora.</strong>
        </div>
      </div>
    </div>'''


# ── SLIDE 5 — Lamborghini capitaliza ──────────────────────────────────────────

def slide5():
    luce  = photo_uri("ferrari_luce_trim.png")
    lambo = photo_uri("lamborghini_trim.png")
    return f'''<div class="slide" style="overflow:hidden;background:{INK["void"]};">
      {dot_grid(color="rgba(255,255,255,0.04)")}
      {logo()}

      <!-- ZONA 1 · KICKER + HEADLINE -->
      <div style="position:absolute;top:58px;left:28px;right:28px;z-index:10;">
        {kicker("No Dia Seguinte")}
        <div class="display" style="font-size:34px;color:#fff;line-height:0.92;margin-bottom:6px;">
          A LAMBORGHINI FEZ<br>UM ÚNICO <span style="background:{ACCENT["primary"]};
            color:#06121c;padding:0 10px 4px;border-radius:8px;">MOVIMENTO.</span>
        </div>
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:12px;
                    color:rgba(255,255,255,0.5);line-height:1.45;margin-top:8px;">
          <em style="color:rgba(255,255,255,0.8);">"Cancelar nosso elétrico foi a decisão certa."</em>
          — CEO Lamborghini
        </div>
      </div>

      <!-- ZONA 2 · DOIS CARROS frente a frente (linha divisória no centro) -->
      <!-- divisor central -->
      <div style="position:absolute;left:50%;top:210px;bottom:118px;width:1px;
                  background:linear-gradient(180deg,transparent,rgba(30,197,242,0.5) 20%,
                    rgba(30,197,242,0.5) 80%,transparent);z-index:6;"></div>

      <!-- halos -->
      <div style="position:absolute;top:196px;left:0;width:50%;height:180px;z-index:1;
                  background:radial-gradient(ellipse at 60% 50%,rgba(90,170,225,0.2),transparent 70%);
                  filter:blur(6px);"></div>
      <div style="position:absolute;top:196px;right:0;width:50%;height:180px;z-index:1;
                  background:radial-gradient(ellipse at 40% 50%,rgba(220,180,20,0.22),transparent 70%);
                  filter:blur(6px);"></div>

      <!-- Luce — esquerda, acinzentada (perdedor) -->
      <div style="position:absolute;top:210px;left:-20px;width:230px;z-index:2;
                  filter:grayscale(0.65) brightness(0.78) drop-shadow(0 8px 20px rgba(0,0,0,0.5));">
        <img src="{luce}" style="width:100%;display:block;">
      </div>
      <div style="position:absolute;top:208px;left:14px;z-index:5;">
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:9px;font-weight:700;
                    letter-spacing:0.18em;color:rgba(255,100,100,0.85);text-transform:uppercase;">
          FERRARI · −8%</div>
      </div>

      <!-- Lambo — direita, em cor vibrante (vencedor) -->
      <div style="position:absolute;top:226px;right:-14px;width:230px;z-index:2;
                  filter:drop-shadow(0 10px 26px rgba(0,0,0,0.5));">
        <img src="{lambo}" style="width:100%;display:block;">
      </div>
      <div style="position:absolute;top:224px;right:14px;z-index:5;text-align:right;">
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:9px;font-weight:700;
                    letter-spacing:0.18em;color:{ACCENT["primary"]};text-transform:uppercase;">
          LAMBO · NA FRENTE</div>
      </div>

      <!-- ZONA 3 · BASE com frase conclusiva -->
      <div style="position:absolute;left:0;right:0;bottom:0;height:30%;z-index:8;
                  background:linear-gradient(180deg,transparent,rgba(5,6,10,0.75) 38%,{INK["void"]} 65%);"></div>
      <div style="position:absolute;left:0;right:0;bottom:0;padding:0 32px 52px;z-index:10;">
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:13px;
                    color:rgba(255,255,255,0.62);line-height:1.55;">
          Sem campanha. Sem investimento. Só <strong style="color:#fff;">saber quem é</strong>
          — e não abrir mão disso.
        </div>
      </div>
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
    return f'''<div class="slide" style="overflow:hidden;
        background:radial-gradient(ellipse 100% 80% at 28% 32%,#101A2C 0%,{INK["void"]} 60%,#040509 100%);">
      {dot_grid(color="rgba(255,255,255,0.035)")}

      <!-- glow de apoio, descentralizado -->
      <div style="position:absolute;top:38%;left:30%;transform:translate(-50%,-50%);
                  width:300px;height:300px;z-index:1;pointer-events:none;
                  background:radial-gradient(circle,rgba(30,197,242,0.16),transparent 66%);
                  filter:blur(6px);"></div>
      {logo()}

      <!-- aspa gigante -->
      <div class="display" style="position:absolute;top:64px;left:24px;z-index:9;
                  font-size:150px;line-height:0.7;color:{ACCENT["primary"]};opacity:0.22;">“</div>

      <!-- kicker -->
      <div style="position:absolute;top:150px;left:30px;z-index:10;">
        {kicker("O Insight")}
      </div>

      <!-- statement alinhado à esquerda, com margem -->
      <div style="position:absolute;top:182px;left:30px;right:30px;z-index:10;">
        <div class="display" style="font-size:42px;color:#fff;line-height:0.98;">
          QUEM TEM<br>POSICIONAMENTO<br>CLARO
        </div>
        <div class="display" style="font-size:42px;color:rgba(255,255,255,0.45);
                    line-height:1.05;margin-top:14px;">
          NÃO PRECISA DE<br>
          <span style="background:{ACCENT["primary"]};color:#06121c;
                padding:0 12px 5px;border-radius:9px;
                box-shadow:0 6px 26px rgba(30,197,242,0.5);">CAMPANHA</span><br>
          <span style="color:#fff;">PARA SE DEFENDER.</span>
        </div>
      </div>

      {overlay_vignette(0.42, z=3)}
    </div>'''


# ── SLIDE 8 — Fechamento forte ────────────────────────────────────────────────

def slide8():
    ferrari_c = photo_uri("ferrari_classic_trim.png")
    return f'''<div class="slide" style="overflow:hidden;
        background:linear-gradient(168deg,#180608 0%,#0E0A18 55%,{INK["void"]} 100%);">
      {dot_grid("rgba(255,255,255,0.04)")}
      {logo()}

      <!-- ZONA 1 · KICKER -->
      <div style="position:absolute;top:60px;left:28px;z-index:10;">
        {kicker("O Que Esse Case Revela")}
      </div>

      <!-- ZONA 2 · Ferrari clássica no centro, glow vermelho, imponente -->
      <div style="position:absolute;top:100px;left:50%;transform:translateX(-50%);
                  width:380px;height:200px;z-index:0;
                  background:radial-gradient(ellipse at 50% 55%,rgba(200,40,40,0.28),transparent 66%);
                  filter:blur(10px);"></div>
      <div style="position:absolute;top:80px;left:50%;transform:translateX(-52%);
                  width:360px;z-index:2;
                  -webkit-mask-image:radial-gradient(ellipse 94% 90% at 50% 50%,#000 68%,transparent 96%);
                  mask-image:radial-gradient(ellipse 94% 90% at 50% 50%,#000 68%,transparent 96%);">
        <img src="{ferrari_c}" style="width:100%;display:block;
             filter:drop-shadow(0 14px 30px rgba(0,0,0,0.6));">
      </div>

      <!-- ZONA 3 · TEXTO base -->
      <div style="position:absolute;left:0;right:0;bottom:0;height:50%;z-index:8;
                  background:linear-gradient(180deg,transparent,rgba(14,10,24,0.65) 32%,#0E0A18 60%);"></div>
      <div style="position:absolute;left:0;right:0;bottom:0;padding:0 32px 52px;z-index:10;">
        <div class="display" style="font-size:40px;color:#fff;line-height:0.90;margin-bottom:14px;">
          MARCA FORTE<br>NÃO SEGUE<br>TODA <span style="background:{ACCENT["primary"]};
            color:#06121c;padding:0 10px 4px;border-radius:8px;">TENDÊNCIA.</span>
        </div>
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:13.5px;
                    color:rgba(255,255,255,0.66);line-height:1.6;max-width:300px;">
          A Lamborghini sabia quem era.
          <strong style="color:#fff;">E ganhou sem fazer nada.</strong>
        </div>
      </div>
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
