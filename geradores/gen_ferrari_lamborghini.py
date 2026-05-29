#!/usr/bin/env python3
"""
NUC Vision — Carrossel Trend: Ferrari Luce vs Lamborghini
Reconstruído com SEÇÃO 0 (arco narrativo, loops abertos) + nuc_realism.
Arco (Modelo 5 — Polêmica): gancho → curiosidade → escalada → virada →
escalada → revelação → insight → CTA. Promessa central escondida até S6.
Formato: 420×525px → exportado a 1080×1350px.
"""
import sys, base64
from pathlib import Path
sys.path.insert(0, "/home/user/Meu-espa-o")
sys.path.insert(0, "/home/user/Meu-espa-o/geradores")
from design_system import (
    FONT_LINK, CSS_BASE, INK, PAPER, ACCENT, GRAY,
    FONTS, TYPE, TRACK, LINE, RADIUS, SHADOW,
    LOGO_URI, NOISE_B64,
    overlay_noise, overlay_vignette, logo_mark,
    ig_frame_open, ig_frame_close, html_shell,
)
from nuc_realism import (
    REALISM_CSS, GRAO_OVERLAY, fundo_profundo, recorte, sombra_contato, card,
)

FOTOS = Path("/home/user/Meu-espa-o/fotos")
TOTAL = 8
CAPTION = ("Uma das marcas mais lendárias do mundo perdeu bilhões em um dia — "
           "e a concorrente venceu sem fazer nada. O que separa as duas não é "
           "produto. É posicionamento. Desliza até o fim. 👇 "
           "#posicionamento #marketing #ferrari #lamborghini #nucvision #estrategia")

# ── helpers ────────────────────────────────────────────────────────────────────

def photo_uri(name):
    p = FOTOS / name
    ext = p.suffix.lower().lstrip(".")
    mime = {"jpg":"jpeg","jpeg":"jpeg","png":"png","webp":"webp"}.get(ext,"jpeg")
    return f"data:image/{mime};base64,{base64.b64encode(p.read_bytes()).decode()}"

def logo(white=True, size=22, top=20):
    flt = "filter:brightness(0) invert(1) drop-shadow(0 2px 10px rgba(0,0,0,0.7));" if white else ""
    return (f'<div style="position:absolute;top:{top}px;left:0;right:0;'
            f'display:flex;justify-content:center;z-index:30;">'
            f'<img src="{LOGO_URI}" style="height:{size}px;width:auto;{flt}"></div>')

def kicker(text, color=None):
    c = color or ACCENT["primary"]
    return (f'<div style="font-family:{FONTS["body"]},sans-serif;font-size:10px;'
            f'font-weight:700;letter-spacing:0.22em;text-transform:uppercase;'
            f'color:{c};margin-bottom:10px;">{text}</div>')

def hl(word):
    """Highlight box: fundo ciano, texto escuro — UMA palavra-chave por slide."""
    return (f'<span style="background:{ACCENT["primary"]};color:#06121c;'
            f'padding:0 11px 4px;border-radius:8px;'
            f'box-shadow:0 6px 24px rgba(30,197,242,0.45);">{word}</span>')

def dot_grid(color="rgba(30,197,242,0.06)", sp=28, z=0):
    return (f'<div style="position:absolute;inset:0;z-index:{z};'
            f'background-image:radial-gradient(circle,{color} 1.2px,transparent 1.2px);'
            f'background-size:{sp}px {sp}px;"></div>')

def bridge(text):
    """Ponte de loop aberto — frase curta ciano que empurra para o próximo slide."""
    return (f'<div style="display:flex;align-items:center;gap:9px;margin-top:18px;">'
            f'<div style="width:22px;height:2px;background:{ACCENT["primary"]};flex-shrink:0;"></div>'
            f'<span style="font-family:{FONTS["body"]},sans-serif;font-size:12.5px;'
            f'font-style:italic;color:{ACCENT["primary"]};line-height:1.45;'
            f'font-weight:500;">{text}</span></div>')

def comment_bubble(text, highlight=False, max_w=205):
    hlc = ("background:linear-gradient(transparent 12%,#FFE600 12%,#FFE600 88%,transparent 88%);"
           "box-decoration-break:clone;-webkit-box-decoration-break:clone;padding:0 1px;") if highlight else ""
    return (
        f'<div style="background:#fff;border-radius:14px;padding:12px 15px;'
        f'max-width:{max_w}px;box-shadow:0 16px 40px rgba(0,0,0,0.55);">'
        f'<div style="display:flex;align-items:center;gap:8px;margin-bottom:8px;">'
        f'<div style="width:26px;height:26px;border-radius:50%;background:#cfcfcf;filter:blur(0.5px);flex-shrink:0;"></div>'
        f'<div style="width:96px;height:9px;background:#d4d4d4;border-radius:4px;filter:blur(1.2px);"></div></div>'
        f'<div style="font-family:{FONTS["body"]},sans-serif;font-size:13px;color:#111;line-height:1.5;font-weight:600;">'
        f'<span style="{hlc}">{text}</span></div></div>'
    )


# ── S1 · GANCHO ────────────────────────────────────────────────────────────────
# Papel: parar o scroll. Promessa escondida. Loop: "qual decisão?"

def slide1():
    hamilton = photo_uri("hamilton_cutout.png")
    luce     = photo_uri("FERRARI_LUCE_FRONT_3Q_16x9_RGB_WEB_SOCIALS_1920x1080-1000x1000.png")
    return f'''<div class="slide" style="overflow:hidden;
        background:radial-gradient(ellipse 130% 100% at 50% 30%,#241016 0%,#12101C 45%,#0B0D16 100%);">
      {dot_grid(color="rgba(255,255,255,0.05)", z=0)}

      <!-- glow vermelho dramático atrás do piloto -->
      <div style="position:absolute;top:36px;left:50%;transform:translateX(-50%);
                  width:360px;height:320px;z-index:0;
                  background:radial-gradient(ellipse,rgba(196,30,40,0.30),transparent 68%);filter:blur(14px);"></div>

      <!-- HAMILTON (recorte dissolvido nas bordas) -->
      <div style="position:absolute;top:30px;left:50%;transform:translateX(-50%);width:102%;z-index:1;
                  -webkit-mask-image:linear-gradient(to bottom,black 0%,black 52%,transparent 82%),
                    linear-gradient(to right,transparent 0%,black 8%,black 92%,transparent 100%);
                  -webkit-mask-composite:destination-in;
                  mask-image:linear-gradient(to bottom,black 0%,black 52%,transparent 82%),
                    linear-gradient(to right,transparent 0%,black 8%,black 92%,transparent 100%);
                  mask-composite:intersect;">
        <img src="{hamilton}" style="width:100%;display:block;filter:grayscale(1) contrast(1.12);">
      </div>

      <!-- fade inferior -->
      <div style="position:absolute;bottom:0;left:0;right:0;height:56%;z-index:2;
                  background:linear-gradient(180deg,transparent 0%,rgba(11,13,22,0.55) 38%,
                    rgba(11,13,22,0.95) 70%,#0B0D16 100%);"></div>

      <!-- halo atrás da Luce -->
      <div style="position:absolute;bottom:128px;right:-40px;z-index:3;width:320px;height:250px;
                  background:radial-gradient(ellipse at 55% 50%,rgba(90,170,225,0.30),
                    rgba(90,170,225,0.10) 38%,transparent 70%);filter:blur(8px);"></div>

      <!-- FERRARI LUCE flutuando, integrada (light wrap) -->
      <div style="position:absolute;bottom:158px;right:-24px;z-index:4;width:228px;transform:rotate(-7deg);
                  -webkit-mask-image:radial-gradient(ellipse 82% 82% at 50% 50%,#000 62%,transparent 92%);
                  mask-image:radial-gradient(ellipse 82% 82% at 50% 50%,#000 62%,transparent 92%);
                  filter:brightness(0.97) saturate(1.05)
                         drop-shadow(0 12px 30px rgba(0,0,0,0.55))
                         drop-shadow(0 0 26px rgba(70,160,220,0.35));">
        <img src="{luce}" style="width:100%;display:block;">
      </div>

      {logo()}

      <!-- TÍTULO GIGANTE embaixo (caixa-alta PT puro) -->
      <div style="position:absolute;bottom:0;left:0;right:0;z-index:12;padding:0 26px 40px;">
        {kicker("O Caso · Maio 2026")}
        <div class="display" style="font-size:46px;color:#fff;line-height:0.90;
                    text-shadow:0 4px 30px rgba(0,0,0,0.85);">PERDEU</div>
        <div class="display" style="font-size:46px;color:#fff;line-height:0.90;
                    text-shadow:0 4px 30px rgba(0,0,0,0.85);">BILHÕES EM</div>
        <div class="display" style="font-size:46px;color:#fff;line-height:0.90;margin-bottom:16px;
                    text-shadow:0 4px 30px rgba(0,0,0,0.85);">UM <span style="color:{ACCENT["primary"]};">ÚNICO DIA.</span></div>
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:13px;
                    color:rgba(255,255,255,0.7);line-height:1.5;max-width:300px;">
          Sem acidente. Sem escândalo. Uma das marcas mais lendárias do mundo
          tomou <strong style="color:#fff;">uma única decisão</strong> — e o mercado puniu na hora.
        </div>
      </div>
    </div>'''


# ── S2 · CURIOSIDADE ─────────────────────────────────────────────────────────
# Entrega: qual marca / qual decisão. Loop: "não foi o carro — foi o que revelou."

def slide2():
    luce = photo_uri("ferrari_luce_trim.png")
    return f'''<div class="slide" style="overflow:hidden;background:#080b13;">
      {fundo_profundo(luce, extra_style="filter:blur(22px) brightness(0.40) saturate(1.1);")}
      {dot_grid(color="rgba(255,255,255,0.05)")}
      {logo()}

      <div style="position:absolute;top:60px;left:28px;right:28px;z-index:10;">
        {kicker("A Decisão")}
        <div class="display" style="font-size:36px;color:#fff;line-height:0.92;">
          A FERRARI LANÇOU<br>SEU PRIMEIRO {hl("ELÉTRICO")}
        </div>
      </div>

      <!-- carro ancorado, título acima ocluindo a traseira -->
      <div style="position:absolute;top:188px;left:50%;transform:translateX(-50%);
                  width:300px;height:130px;z-index:1;
                  background:radial-gradient(ellipse at 50% 60%,rgba(90,170,225,0.22),transparent 66%);filter:blur(6px);"></div>
      <div class="subject" style="position:absolute;top:178px;left:50%;transform:translateX(-50%);width:312px;z-index:2;">
        <img src="{luce}" style="width:100%;display:block;">
      </div>

      <div style="position:absolute;left:0;right:0;bottom:0;height:42%;z-index:8;
                  background:linear-gradient(180deg,transparent,rgba(8,11,19,0.6) 28%,#080b13 60%);"></div>
      <div style="position:absolute;left:0;right:0;bottom:0;padding:0 28px 40px;z-index:10;">
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:13.5px;
                    color:rgba(255,255,255,0.78);line-height:1.6;max-width:316px;">
          A <strong style="color:#fff;">Luce</strong>: €550 mil, desenhada com o ex-chefe
          de design da Apple. Mas não foi o carro que derrubou a ação.
        </div>
        {bridge("Foi o que esse lançamento revelou sobre a marca.")}
      </div>
    </div>'''


# ── S3 · ESCALADA ──────────────────────────────────────────────────────────────
# Entrega: a reação do mercado. Loop: "uma concorrente fez 1 movimento que ninguém viu."

def slide3():
    luce = photo_uri("ferrari_luce_trim.png")
    b1 = comment_bubble("Isso virou um Nissan de €550 mil…", highlight=True, max_w=196)
    b2 = comment_bubble("Enzo deve estar se revirando no túmulo.", max_w=196)
    return f'''<div class="slide" style="overflow:hidden;background:{INK["void"]};">
      {dot_grid(color="rgba(255,255,255,0.04)")}

      <!-- Luce desaturada como atmosfera diagonal -->
      <div style="position:absolute;top:120px;left:50%;transform:translateX(-46%) rotate(-9deg);
                  width:440px;z-index:0;opacity:0.30;filter:grayscale(1) contrast(1.1) blur(1px);">
        <img src="{luce}" style="width:100%;display:block;">
      </div>
      <div style="position:absolute;inset:0;z-index:1;
                  background:linear-gradient(180deg,{INK["void"]} 14%,transparent 40%,transparent 56%,{INK["void"]} 88%);"></div>
      {logo()}

      <div style="position:absolute;top:60px;left:28px;right:28px;z-index:10;">
        {kicker("A Reação · −8% em 24h")}
        <div class="display" style="font-size:35px;color:#fff;line-height:0.92;">
          A INTERNET<br>{hl("DESTRUIU")} O CARRO
        </div>
      </div>

      <!-- balões empilhados levemente girados (pilha na mesa) -->
      <div style="position:absolute;top:182px;left:22px;z-index:11;transform:rotate(-3deg);">{b1}</div>
      <div style="position:absolute;top:262px;right:18px;z-index:12;transform:rotate(2.5deg);">{b2}</div>

      <div style="position:absolute;left:0;right:0;bottom:0;padding:0 28px 40px;z-index:13;">
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:13px;
                    color:rgba(255,255,255,0.66);line-height:1.55;max-width:312px;">
          Acusada de <strong style="color:#fff;">"destruir uma lenda"</strong>,
          a Ferrari virou piada em 24 horas.
        </div>
        {bridge("Mas, enquanto riam dela, uma concorrente fez um único movimento.")}
      </div>
    </div>'''


# ── S4 · VIRADA ──────────────────────────────────────────────────────────────
# Entrega: a Lambo não fez nada e venceu. Loop: "o motivo não é o que parece."

def slide4():
    lambo = photo_uri("lamborghini_trim.png")
    return f'''<div class="slide" style="overflow:hidden;background:#0a0a06;">
      {fundo_profundo(lambo, extra_style="filter:blur(22px) brightness(0.42) saturate(1.15);")}
      {dot_grid(color="rgba(255,255,255,0.04)")}
      {logo()}

      <div style="position:absolute;top:58px;left:28px;right:28px;z-index:10;">
        {kicker("A Virada")}
        <div class="display" style="font-size:35px;color:#fff;line-height:0.92;">
          A LAMBORGHINI<br>NÃO LANÇOU {hl("NADA")}
        </div>
      </div>

      <!-- Lambo centralizada e contida, com leve inclinação -->
      <div style="position:absolute;top:188px;left:50%;transform:translateX(-50%);
                  width:300px;height:130px;z-index:1;
                  background:radial-gradient(ellipse at 50% 60%,rgba(220,180,20,0.22),transparent 68%);filter:blur(8px);"></div>
      <div class="subject" style="position:absolute;top:182px;left:50%;
                  transform:translateX(-50%) rotate(-2deg);width:308px;z-index:2;">
        <img src="{lambo}" style="width:100%;display:block;">
      </div>

      <div style="position:absolute;left:0;right:0;bottom:0;height:40%;z-index:8;
                  background:linear-gradient(180deg,transparent,rgba(10,10,6,0.62) 30%,#0a0a06 62%);"></div>
      <div style="position:absolute;left:0;right:0;bottom:0;padding:0 28px 40px;z-index:10;">
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:13.5px;
                    color:rgba(255,255,255,0.78);line-height:1.6;max-width:300px;">
          O CEO só disse: <em style="color:#fff;">"cancelar nosso elétrico foi a decisão certa."</em>
          E saiu na frente.
        </div>
        {bridge("Mas o motivo de ela vencer não é o que parece.")}
      </div>
    </div>'''


# ── S5 · ESCALADA ──────────────────────────────────────────────────────────────
# Entrega: não foi sorte — ela sabia quem era. Loop: "isso expõe uma regra."

def slide5():
    luce  = photo_uri("ferrari_luce_trim.png")
    lambo = photo_uri("lamborghini_trim.png")
    return f'''<div class="slide" style="overflow:hidden;background:{INK["void"]};">
      {dot_grid(color="rgba(255,255,255,0.04)")}
      {logo()}

      <div style="position:absolute;top:56px;left:28px;right:28px;z-index:10;">
        {kicker("Não Foi Sorte")}
        <div class="display" style="font-size:33px;color:#fff;line-height:0.96;">
          UMA REAGIU.<br>A OUTRA SABIA<br>{hl("QUEM ELA ERA")}
        </div>
      </div>

      <!-- confronto: Ferrari apagada à esquerda, Lambo viva à direita -->
      <div style="position:absolute;left:50%;top:188px;bottom:150px;width:1px;z-index:6;
                  background:linear-gradient(180deg,transparent,rgba(30,197,242,0.5) 20%,rgba(30,197,242,0.5) 80%,transparent);"></div>
      <div style="position:absolute;top:182px;right:0;width:55%;height:170px;z-index:1;
                  background:radial-gradient(ellipse at 45% 50%,rgba(220,180,20,0.22),transparent 70%);filter:blur(6px);"></div>

      <!-- Luce perdedora, cinza -->
      <div style="position:absolute;top:196px;left:-26px;width:228px;z-index:2;
                  filter:grayscale(0.7) brightness(0.72) drop-shadow(0 8px 20px rgba(0,0,0,0.5));">
        <img src="{luce}" style="width:100%;display:block;">
      </div>
      <div style="position:absolute;top:192px;left:14px;z-index:5;
                  font-family:{FONTS["body"]},sans-serif;font-size:9px;font-weight:700;
                  letter-spacing:0.18em;color:rgba(255,100,100,0.85);text-transform:uppercase;">FERRARI · REAGIU</div>

      <!-- Lambo vencedora, viva e ancorada -->
      <div class="subject" style="position:absolute;top:212px;right:-18px;width:242px;z-index:2;">
        <img src="{lambo}" style="width:100%;display:block;">
      </div>
      <div style="position:absolute;top:208px;right:14px;z-index:5;text-align:right;
                  font-family:{FONTS["body"]},sans-serif;font-size:9px;font-weight:700;
                  letter-spacing:0.18em;color:{ACCENT["primary"]};text-transform:uppercase;">LAMBO · NÃO SE MOVEU</div>

      <div style="position:absolute;left:0;right:0;bottom:0;height:30%;z-index:8;
                  background:linear-gradient(180deg,transparent,rgba(5,6,10,0.78) 36%,{INK["void"]} 64%);"></div>
      <div style="position:absolute;left:0;right:0;bottom:0;padding:0 28px 40px;z-index:10;">
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:13px;
                    color:rgba(255,255,255,0.66);line-height:1.55;max-width:312px;">
          Sem campanha, sem investimento. Só não abrir mão do que ela é.
        </div>
        {bridge("E é exatamente aí que aparece a regra que separa as duas.")}
      </div>
    </div>'''


# ── S6 · REVELAÇÃO ─────────────────────────────────────────────────────────────
# Entrega a PROMESSA CENTRAL. Aqui pode fechar a tensão. Ferrari clássica = essência.

def slide6():
    ferrari_c = photo_uri("ferrari_classic_trim.png")
    return f'''<div class="slide" style="overflow:hidden;
        background:radial-gradient(ellipse 120% 90% at 50% 36%,#1A0608 0%,{INK["rich"]} 52%,#070910 100%);">
      {dot_grid(color="rgba(255,255,255,0.04)")}

      <!-- Ferrari clássica imponente no topo, ocluída pelo título -->
      <div style="position:absolute;top:110px;left:50%;transform:translateX(-50%);
                  width:380px;height:190px;z-index:0;
                  background:radial-gradient(ellipse at 50% 55%,rgba(200,40,40,0.28),transparent 66%);filter:blur(10px);"></div>
      <div style="position:absolute;top:214px;left:50%;transform:translateX(-50%);
                  width:236px;height:30px;z-index:1;
                  background:radial-gradient(closest-side,rgba(0,0,0,0.6),transparent 78%);filter:blur(9px);"></div>
      <div style="position:absolute;top:84px;left:50%;transform:translateX(-52%);width:352px;z-index:2;
                  -webkit-mask-image:radial-gradient(ellipse 94% 90% at 50% 50%,#000 66%,transparent 96%);
                  mask-image:radial-gradient(ellipse 94% 90% at 50% 50%,#000 66%,transparent 96%);">
        <img src="{ferrari_c}" style="width:100%;display:block;
             filter:brightness(0.97) contrast(1.05) saturate(1.04) drop-shadow(0 14px 30px rgba(0,0,0,0.6));">
      </div>
      {logo()}

      <!-- kicker sobreposto ao topo -->
      <div style="position:absolute;top:60px;left:28px;z-index:10;">{kicker("A Regra")}</div>

      <div style="position:absolute;left:0;right:0;bottom:0;height:52%;z-index:8;
                  background:linear-gradient(180deg,transparent,rgba(7,9,16,0.7) 30%,#070910 60%);"></div>
      <div style="position:absolute;left:0;right:0;bottom:0;padding:0 28px 40px;z-index:10;">
        <div class="display" style="font-size:37px;color:#fff;line-height:0.96;margin-bottom:12px;">
          POSICIONAMENTO É<br>O QUE VOCÊ<br>{hl("NÃO ABRE MÃO")}<br>DE SER.
        </div>
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:13.5px;
                    color:rgba(255,255,255,0.72);line-height:1.6;max-width:312px;">
          A Ferrari abriu mão da essência sob pressão. A Lamborghini não.
          <strong style="color:#fff;">Foi só isso.</strong>
        </div>
      </div>
    </div>'''


# ── S7 · INSIGHT ───────────────────────────────────────────────────────────────
# Aprendizado universal. Tipográfico puro (permitido no clímax).

def slide7():
    return f'''<div class="slide" style="overflow:hidden;
        background:radial-gradient(ellipse 100% 80% at 30% 34%,#101A2C 0%,{INK["void"]} 60%,#040509 100%);">
      {dot_grid(color="rgba(255,255,255,0.035)")}
      <div style="position:absolute;top:38%;left:30%;transform:translate(-50%,-50%);
                  width:300px;height:300px;z-index:1;pointer-events:none;
                  background:radial-gradient(circle,rgba(30,197,242,0.16),transparent 66%);filter:blur(6px);"></div>
      {logo()}

      <div class="display" style="position:absolute;top:66px;left:24px;z-index:9;
                  font-size:150px;line-height:0.7;color:{ACCENT["primary"]};opacity:0.22;">“</div>
      <div style="position:absolute;top:154px;left:30px;z-index:10;">{kicker("O Insight")}</div>

      <div style="position:absolute;top:186px;left:30px;right:30px;z-index:10;">
        <div class="display" style="font-size:42px;color:#fff;line-height:0.98;">
          QUEM TEM<br>POSICIONAMENTO<br>CLARO
        </div>
        <div class="display" style="font-size:42px;color:rgba(255,255,255,0.5);line-height:1.05;margin-top:14px;">
          NÃO PRECISA DE<br>{hl("CAMPANHA")}<br>
          <span style="color:#fff;">PARA SE DEFENDER.</span>
        </div>
      </div>
      {overlay_vignette(0.42, z=3)}
    </div>'''


# ── S8 · CTA ─────────────────────────────────────────────────────────────────

def slide8():
    return f'''<div class="slide" style="overflow:hidden;
        background:linear-gradient(155deg,{INK["rich"]} 0%,#0A1628 55%,{INK["void"]} 100%);">
      <div style="position:absolute;top:-60px;left:50%;transform:translateX(-50%);width:260px;height:200px;z-index:1;
                  background:radial-gradient(ellipse,rgba(30,197,242,0.18) 0%,transparent 70%);pointer-events:none;"></div>
      {logo(size=26)}
      <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;
                  justify-content:center;padding:0 28px;z-index:10;text-align:center;">
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:11px;font-weight:700;
                    letter-spacing:0.22em;text-transform:uppercase;color:{ACCENT["primary"]};margin-bottom:14px;">@nucvision</div>
        <div class="display" style="font-size:34px;color:#fff;line-height:1;margin-bottom:8px;">LEITURAS ASSIM</div>
        <div class="display" style="font-size:34px;color:{ACCENT["primary"]};margin-bottom:24px;">TODA SEMANA.</div>
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:13px;
                    color:rgba(255,255,255,0.55);margin-bottom:28px;line-height:1.5;">
          Siga a NUC Vision para acompanhar leituras<br>
          estratégicas sobre marcas, mercado e posicionamento.
        </div>
        <div class="cta" style="color:#06121c;font-family:{FONTS["body"]},sans-serif;font-size:13px;
                    font-weight:700;letter-spacing:0.1em;text-transform:uppercase;padding:13px 32px;">
          SEGUIR AGORA
        </div>
      </div>
      {overlay_vignette(0.3, z=3)}
    </div>'''


# ── Assembly ───────────────────────────────────────────────────────────────────

def main():
    raw = [slide1(), slide2(), slide3(), slide4(), slide5(), slide6(), slide7(), slide8()]
    parts = []
    for s in raw:
        idx = s.rfind("</div>")
        parts.append(s[:idx] + GRAO_OVERLAY + s[idx:])
    slides = f"<style>{REALISM_CSS}</style>" + "".join(parts)
    html = html_shell(slides, TOTAL, CAPTION)
    out = Path("/home/user/Meu-espa-o/previews/nucvision-ferrari-lambo.html")
    out.write_text(html, encoding="utf-8")
    print(f"✓ {out}")

if __name__ == "__main__":
    main()
