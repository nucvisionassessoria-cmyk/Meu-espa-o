#!/usr/bin/env python3
"""
NUC Vision Editorial — 87% do seu marketing não funciona
Carrossel 8 slides | hero V4-style com Derick + Iago
Aplica continuidade narrativa: cada slide nasce do anterior.
"""
import sys
from pathlib import Path
sys.path.insert(0, "/home/user/Meu-espa-o")

from design_system import (
    INK, PAPER, ACCENT, GRAY, FONTS, TYPE, TRACK, LINE,
    RADIUS, SHADOW,
    bg_brand_atmo, bg_dark_atmo, bg_paper_atmo,
    overlay_noise, overlay_vignette,
    kicker, display_pill, glass_card, number_marker,
    feature_row, slide_index, progress_bar, logo_mark,
    photo_layered, photo_uri, photo_position,
    html_shell,
)

TOTAL = 8

# ============================================================
# SLIDE 1 — GANCHO (V4-style hero) | Derick + Iago
# Termina com pergunta aberta: "qual parte é?"
# ============================================================
def slide1():
    derick = photo_uri("derick_bracos_cruzados.jpg")
    iago   = photo_uri("iago_bracos_cruzados.png")

    # Fotos altas (410px) para rostos aparecerem na zona visível sem fade.
    # INK["void"] = #05080F — mesma cor usada em todos os gradients de fade,
    # garantindo que bordas das fotos dissolvam naturalmente no fundo.
    # Sem "center seam div" — o fade lateral de cada foto resolve sozinho.
    return f'''<div class="slide" style="background:{INK["void"]};overflow:hidden;">

      <!-- Camada 1: atmosfera unificada de fundo -->
      <div style="position:absolute;inset:0;z-index:1;
                  background:
                    radial-gradient(ellipse 80% 55% at 50% -5%,  rgba(30,197,242,0.16) 0%, transparent 55%),
                    radial-gradient(ellipse 55% 40% at  8% 100%, rgba(20,30,52,0.80) 0%, transparent 55%),
                    radial-gradient(ellipse 55% 40% at 92% 100%, rgba(20,30,52,0.80) 0%, transparent 55%),
                    {INK["void"]};"></div>

      <!-- DERICK — esquerda (JPG fundo estúdio)
           Container estreito e recuado para que o fundo claro não alcance
           o centro do slide. 3 fades right em cascata + brightness baixo. -->
      <div style="position:absolute;left:-28px;bottom:0;width:252px;height:410px;z-index:4;">
        <img src="{derick}" style="width:100%;height:100%;object-fit:cover;
                   object-position:50% 8%;
                   filter:contrast(1.05) saturate(0.78) brightness(0.86);">
        <div style="position:absolute;inset:0;background:linear-gradient(180deg,
                    {INK["void"]} 0%, rgba(5,8,15,0.90) 6%, rgba(5,8,15,0.10) 20%, transparent 34%);"></div>
        <div style="position:absolute;inset:0;background:linear-gradient(90deg,
                    transparent 0%, transparent 32%,
                    rgba(5,8,15,0.40) 50%, rgba(5,8,15,0.88) 65%, {INK["void"]} 76%);"></div>
        <div style="position:absolute;inset:0;background:linear-gradient(90deg,
                    transparent 0%, transparent 48%, {INK["void"]} 73%);"></div>
        <div style="position:absolute;inset:0;background:linear-gradient(270deg,
                    transparent 0%, transparent 90%, rgba(5,8,15,0.35) 100%);"></div>
      </div>

      <!-- IAGO — direita (PNG RGBA, transparência natural) -->
      <div style="position:absolute;right:-28px;bottom:0;width:262px;height:410px;z-index:4;">
        <img src="{iago}" style="width:100%;height:100%;object-fit:cover;
                   object-position:50% 0%;
                   filter:contrast(1.05) saturate(0.78) brightness(0.86);">
        <div style="position:absolute;inset:0;background:linear-gradient(180deg,
                    {INK["void"]} 0%, rgba(5,8,15,0.90) 6%, rgba(5,8,15,0.10) 20%, transparent 34%);"></div>
        <div style="position:absolute;inset:0;background:linear-gradient(270deg,
                    transparent 0%, transparent 40%,
                    rgba(5,8,15,0.30) 58%, rgba(5,8,15,0.76) 76%, {INK["void"]} 88%);"></div>
        <div style="position:absolute;inset:0;background:linear-gradient(90deg,
                    transparent 0%, transparent 90%, rgba(5,8,15,0.35) 100%);"></div>
      </div>

      <!-- Camada 2: escurecimento do topo para legibilidade do texto -->
      <div style="position:absolute;top:0;left:0;right:0;height:240px;z-index:7;
                  background:linear-gradient(180deg,
                    {INK["void"]} 0%, rgba(5,8,15,0.92) 28%, rgba(5,8,15,0.55) 55%, transparent 100%);
                  pointer-events:none;"></div>

      <!-- Camada 3: split-lighting center — cobertura larga do centro do slide.
           32% de largura = ~134px, cobre o seam entre x=143–277.
           Rostos (x≈80 e x≈310) ficam fora do oval, sem escurecer. -->
      <div style="position:absolute;left:0;right:0;bottom:0;height:420px;z-index:6;
                  background:radial-gradient(ellipse 32% 100% at 50% 65%,
                    {INK["void"]} 0%, rgba(5,8,15,0.88) 35%, rgba(5,8,15,0.40) 60%, transparent 100%);
                  pointer-events:none;"></div>

      <!-- Camada 3b: boost de luz suave no lado esquerdo (Derick)
           Radial limitado a x=0–160, preserva o seam central intacto. -->
      <div style="position:absolute;left:0;bottom:80px;width:180px;height:360px;z-index:5;
                  background:radial-gradient(ellipse 90% 70% at 22% 48%,
                    rgba(255,255,255,0.07) 0%, rgba(255,255,255,0.02) 45%, transparent 75%);
                  pointer-events:none;"></div>

      <!-- Camada 4: glow ciano unificado — conecta os dois sócios ao ambiente -->
      <div style="position:absolute;top:0;left:0;right:0;bottom:0;z-index:8;
                  background:radial-gradient(ellipse 60% 35% at 50% 52%,
                    rgba(30,197,242,0.08) 0%, transparent 65%);
                  pointer-events:none;"></div>

      <!-- TEXTO — centrado, acima da zona de rostos -->
      <div style="position:absolute;top:0;left:0;right:0;z-index:12;
                  display:flex;flex-direction:column;align-items:center;
                  padding-top:24px;">
        {logo_mark(dark_bg=True, size=20)}

        <div style="margin-top:16px;">
          {kicker("Diagnóstico do Mercado", color="rgba(255,255,255,0.52)")}
        </div>

        <!-- Pill 87% com glow ciano -->
        <div style="margin-top:12px;display:inline-block;
                    background:linear-gradient(135deg, {ACCENT["primary"]} 0%, {ACCENT["vivid"]} 100%);
                    padding:5px 24px 10px;border-radius:{RADIUS["lg"]}px;
                    box-shadow:0 10px 28px rgba(30,197,242,0.45),
                               0 0 56px rgba(30,197,242,0.22),
                               inset 0 1px 0 rgba(255,255,255,0.28);">
          <span class="display" style="font-size:76px;color:#fff;line-height:0.86;
                       letter-spacing:{TRACK["tight"]};
                       text-shadow:0 2px 10px rgba(0,0,0,0.30);">87%</span>
        </div>

        <div style="margin-top:12px;text-align:center;line-height:0.94;">
          <div class="display" style="font-size:29px;color:#fff;
                      letter-spacing:{TRACK["tight"]};
                      text-shadow:0 2px 18px rgba(0,0,0,0.80);">DO SEU MARKETING</div>
          <div class="display" style="font-size:29px;color:rgba(255,255,255,0.88);
                      letter-spacing:{TRACK["tight"]};margin-top:2px;
                      text-shadow:0 2px 18px rgba(0,0,0,0.80);">NÃO FUNCIONA.</div>
        </div>
      </div>

      <!-- Tagline de baixo — âncora visual, z-index alto para ficar sobre tudo -->
      <div style="position:absolute;bottom:34px;left:0;right:0;z-index:18;
                  text-align:center;">
        <div style="font-family:{FONTS["body"]};font-size:13px;font-weight:500;
                    color:rgba(255,255,255,0.88);line-height:1.4;
                    text-shadow:0 2px 14px rgba(0,0,0,0.95);">
          E você ainda <strong style="color:#fff;font-weight:700;">não sabe qual parte é.</strong>
        </div>
        <div style="margin-top:8px;font-family:{FONTS["body"]};font-size:9px;
                    font-weight:600;color:rgba(255,255,255,0.40);
                    letter-spacing:{TRACK["label"]};text-transform:uppercase;">
          @nucvision · Diagnóstico B2B
        </div>
      </div>

      {slide_index(1, TOTAL)}
      {overlay_noise(0.20, blend="soft-light", z=10)}
      {progress_bar(1, TOTAL)}
    </div>'''

# ============================================================
# SLIDE 2 — CONTINUAÇÃO DIRETA
# Não inicia ideia nova. Continua o gancho explicando POR QUE.
# Termina provocando: "como assim medir?"
# ============================================================
def slide2():
    return f'''<div class="slide" style="{bg_paper_atmo()}">
      {slide_index(2, TOTAL, light=True)}

      <!-- watermark "2" -->
      <div class="display" style="position:absolute;bottom:-40px;right:-20px;
                  font-size:280px;color:rgba(10,15,26,0.04);
                  line-height:1;letter-spacing:-0.04em;z-index:1;
                  pointer-events:none;user-select:none;">2</div>

      <div style="display:flex;justify-content:center;padding-top:28px;position:relative;z-index:5;">
        {logo_mark(dark_bg=False, size=22)}
      </div>

      <div style="position:absolute;top:104px;left:30px;right:30px;z-index:10;">
        {kicker("E não para por aí…", light=True)}

        <div style="margin-top:22px;line-height:1.0;">
          <div class="display" style="font-size:46px;color:{INK["deep"]};
                      letter-spacing:{TRACK["tight"]};">O PROBLEMA</div>
          <div class="display" style="font-size:46px;color:{INK["deep"]};
                      letter-spacing:{TRACK["tight"]};margin-top:2px;">NÃO É QUANTO</div>
          <div class="display" style="font-size:46px;color:{ACCENT["primary"]};
                      letter-spacing:{TRACK["tight"]};margin-top:2px;
                      text-shadow:0 2px 18px rgba(30,197,242,0.20);">VOCÊ INVESTE.</div>
        </div>

        <div style="margin-top:26px;height:1.5px;width:48px;
                    background:{ACCENT["primary"]};"></div>

        <div style="margin-top:22px;font-family:{FONTS["body"]};font-size:14.5px;
                    font-weight:400;color:{GRAY["700"]};line-height:1.55;
                    max-width:340px;">
          É o que você <strong style="color:{INK["deep"]};font-weight:700;">não
          consegue medir</strong> — e por isso continua repetindo o mesmo
          investimento esperando resultado diferente.
        </div>
      </div>

      <!-- bottom hint -->
      <div style="position:absolute;bottom:42px;left:30px;right:30px;z-index:10;">
        <div style="font-family:{FONTS["body"]};font-size:11px;font-weight:600;
                    color:{GRAY["500"]};letter-spacing:{TRACK["wide"]};
                    text-transform:uppercase;">
          → Continua no próximo
        </div>
      </div>

      {progress_bar(2, TOTAL, light=True)}
    </div>'''

# ============================================================
# SLIDE 3 — APROFUNDAMENTO
# Mostra o erro escondido: o que a maioria mede vs o que importa.
# Termina provocando: "então estou olhando pro lado errado?"
# ============================================================
def slide3():
    def row(left, right):
        return (f'<div style="display:flex;align-items:center;gap:14px;'
                f'padding:13px 14px;background:rgba(255,255,255,0.04);'
                f'border:1px solid rgba(255,255,255,0.08);'
                f'border-radius:{RADIUS["md"]}px;margin-bottom:8px;">'
                f'<div style="flex:1;font-family:{FONTS["body"]};font-size:12.5px;'
                f'color:rgba(255,255,255,0.42);text-decoration:line-through;'
                f'text-decoration-color:rgba(255,255,255,0.3);">{left}</div>'
                f'<div style="font-family:{FONTS["display"]};font-size:14px;'
                f'color:{ACCENT["primary"]};">→</div>'
                f'<div style="flex:1;font-family:{FONTS["body"]};font-size:12.5px;'
                f'font-weight:600;color:#fff;">{right}</div>'
                f'</div>')

    return f'''<div class="slide" style="{bg_dark_atmo()}">
      {overlay_noise(0.45)}
      {slide_index(3, TOTAL)}

      <div style="display:flex;justify-content:center;padding-top:26px;position:relative;z-index:5;">
        {logo_mark(dark_bg=True, size=20)}
      </div>

      <div style="position:absolute;top:78px;left:24px;right:24px;z-index:10;">
        {kicker("E é aqui que muita gente erra", color=ACCENT["mist"])}

        <div style="margin-top:14px;line-height:0.94;">
          <div class="display" style="font-size:34px;color:#fff;
                      letter-spacing:{TRACK["tight"]};">O QUE VOCÊ MEDE</div>
          <div class="display" style="font-size:34px;color:{ACCENT["primary"]};
                      letter-spacing:{TRACK["tight"]};margin-top:2px;
                      text-shadow:0 0 24px rgba(30,197,242,0.35);">DETERMINA O QUE CRESCE.</div>
        </div>

        <div style="margin-top:22px;">
          <div style="display:flex;gap:14px;padding:0 14px 8px;">
            <div style="flex:1;font-family:{FONTS["body"]};font-size:9.5px;
                        font-weight:700;color:rgba(255,255,255,0.4);
                        letter-spacing:{TRACK["label"]};text-transform:uppercase;">
              A maioria mede
            </div>
            <div style="width:14px;"></div>
            <div style="flex:1;font-family:{FONTS["body"]};font-size:9.5px;
                        font-weight:700;color:{ACCENT["mist"]};
                        letter-spacing:{TRACK["label"]};text-transform:uppercase;">
              O que gera receita
            </div>
          </div>
          {row("Impressões", "CAC por canal")}
          {row("Cliques", "LTV do cliente")}
          {row("Alcance", "Receita por origem")}
          {row("Seguidores", "Taxa de fechamento")}
        </div>
      </div>

      <div style="position:absolute;bottom:42px;left:24px;right:24px;z-index:10;">
        <div style="font-family:{FONTS["body"]};font-size:12.5px;
                    color:rgba(255,255,255,0.72);line-height:1.45;
                    font-style:italic;">
          A maioria conta o que dá conforto.<br>
          <strong style="color:#fff;font-weight:700;font-style:normal;">
          Não o que dá lucro.</strong>
        </div>
      </div>

      {progress_bar(3, TOTAL)}
    </div>'''

# ============================================================
# SLIDE 4 — VIRADA (ICE background)
# "Só que existe um ângulo que muda tudo."
# Termina provocando: "como clareza muda o jogo?"
# ============================================================
def slide4():
    return f'''<div class="slide" style="background:{ACCENT["ice"]};overflow:hidden;">
      <!-- watermark "4" -->
      <div class="display" style="position:absolute;top:-40px;left:-30px;
                  font-size:340px;color:rgba(10,15,26,0.05);
                  line-height:1;letter-spacing:-0.04em;z-index:1;
                  pointer-events:none;user-select:none;">4</div>

      <div style="display:flex;justify-content:center;padding-top:28px;position:relative;z-index:5;">
        {logo_mark(dark_bg=False, size=22)}
      </div>

      {slide_index(4, TOTAL, light=True)}

      <div style="position:absolute;top:50%;left:30px;right:30px;z-index:10;
                  transform:translateY(-52%);">
        {kicker("Mas existe um ponto que muda tudo", light=True)}

        <div style="margin-top:20px;line-height:0.96;">
          <div class="display" style="font-size:50px;color:{INK["deep"]};
                      letter-spacing:{TRACK["tight"]};">O PROBLEMA</div>
          <div class="display" style="font-size:50px;color:{INK["deep"]};
                      letter-spacing:{TRACK["tight"]};margin-top:2px;">NUNCA FOI</div>
          <div class="display" style="font-size:58px;
                      background:linear-gradient(95deg, {ACCENT["primary"]} 0%, {ACCENT["vivid"]} 100%);
                      -webkit-background-clip:text;-webkit-text-fill-color:transparent;
                      background-clip:text;
                      letter-spacing:{TRACK["tight"]};margin-top:6px;">VOLUME.</div>
          <div class="display" style="font-size:58px;color:{INK["deep"]};
                      letter-spacing:{TRACK["tight"]};margin-top:4px;">FOI</div>
          <div class="display" style="font-size:58px;color:{INK["deep"]};
                      letter-spacing:{TRACK["tight"]};margin-top:2px;">CLAREZA.</div>
        </div>

        <div style="margin-top:24px;height:1.5px;width:48px;
                    background:{ACCENT["primary"]};"></div>

        <div style="margin-top:20px;font-family:{FONTS["body"]};font-size:13.5px;
                    color:{GRAY["700"]};line-height:1.55;max-width:330px;">
          Você não precisa fazer mais. Precisa enxergar melhor o que já está fazendo.
        </div>
      </div>

      {progress_bar(4, TOTAL, light=True)}
    </div>'''

# ============================================================
# SLIDE 5 — EXPLICAÇÃO (V4 Flagship + dashboard)
# Por que clareza > volume. Como aparece na prática.
# Termina puxando: "como isso muda o dia a dia?"
# ============================================================
def slide5():
    img = photo_uri("dashboard_laptop.png")
    pos = photo_position("dashboard_laptop.png")
    return f'''<div class="slide" style="{bg_paper_atmo()}">
      {slide_index(5, TOTAL, light=True)}

      <div style="display:flex;justify-content:center;padding-top:26px;position:relative;z-index:5;">
        {logo_mark(dark_bg=False, size=22)}
      </div>

      <!-- ZONA TEXTO -->
      <div style="position:absolute;top:78px;left:28px;right:28px;
                  bottom:248px;overflow:hidden;z-index:10;">
        {kicker("Por isso, antes de investir mais", light=True)}

        <div style="margin-top:14px;line-height:0.96;">
          <div class="display" style="font-size:62px;color:{ACCENT["primary"]};
                      letter-spacing:{TRACK["tight"]};">CLAREZA</div>
          <div class="display" style="font-size:62px;color:{ACCENT["primary"]};
                      letter-spacing:{TRACK["tight"]};margin-top:2px;">ANTES DE</div>
          <div class="display" style="font-size:62px;color:{INK["deep"]};
                      letter-spacing:{TRACK["tight"]};margin-top:2px;">VERBA.</div>
        </div>

        <div style="margin-top:14px;height:1.5px;width:40px;
                    background:{ACCENT["primary"]};"></div>

        <div style="margin-top:12px;font-family:{FONTS["body"]};font-size:13px;
                    color:{GRAY["600"]};line-height:1.5;max-width:320px;">
          Quando cada real é rastreável, <strong style="color:{INK["deep"]};">cada
          decisão pesa diferente</strong> — e o orçamento começa a render mais.
        </div>
      </div>

      <!-- ZONA FOTO CARD -->
      <div style="position:absolute;bottom:44px;left:28px;right:28px;
                  height:178px;border-radius:{RADIUS["xl"]}px;overflow:hidden;
                  box-shadow:0 18px 44px rgba(10,15,26,0.22),
                             0 6px 14px rgba(10,15,26,0.10);z-index:10;">
        <img src="{img}" style="width:100%;height:100%;object-fit:cover;
                   object-position:{pos};
                   filter:contrast(1.06) saturate(1.04) brightness(0.96);">
        <div style="position:absolute;inset:0;background:linear-gradient(180deg,
                    transparent 40%, rgba(10,15,26,0.30) 100%);"></div>
        <div style="position:absolute;left:18px;bottom:14px;
                    font-family:{FONTS["body"]};font-size:10.5px;font-weight:600;
                    color:#fff;letter-spacing:{TRACK["wide"]};
                    text-transform:uppercase;
                    text-shadow:0 1px 6px rgba(0,0,0,0.6);">
          Painel de indicadores · Cliente NUC Vision
        </div>
      </div>

      {progress_bar(5, TOTAL, light=True)}
    </div>'''

# ============================================================
# SLIDE 6 — APLICAÇÃO PRÁTICA (Dual column glow)
# Os dois mundos lado a lado.
# Termina puxando síntese inevitável.
# ============================================================
def slide6():
    def item_dim(text):
        return (f'<div style="font-family:{FONTS["body"]};font-size:12px;'
                f'color:rgba(255,255,255,0.42);line-height:1.45;'
                f'padding:9px 0;border-bottom:1px solid rgba(255,255,255,0.06);">'
                f'{text}</div>')

    def item_bright(text):
        return (f'<div style="font-family:{FONTS["body"]};font-size:12px;'
                f'font-weight:600;color:#fff;line-height:1.45;'
                f'padding:9px 0;border-bottom:1px solid rgba(30,197,242,0.20);">'
                f'{text}</div>')

    items_a = (item_dim("Investe achando") +
               item_dim("Decide na intuição") +
               item_dim("Repete o mesmo erro") +
               item_dim("Estagna sem entender"))

    items_b = (item_bright("Investe sabendo") +
               item_bright("Decide pelo número") +
               item_bright("Corta o que não rende") +
               item_bright("Escala o que funciona"))

    return f'''<div class="slide" style="{bg_dark_atmo()}">
      {overlay_noise(0.42)}
      {slide_index(6, TOTAL)}

      <div style="display:flex;justify-content:center;padding-top:26px;position:relative;z-index:5;">
        {logo_mark(dark_bg=True, size=20)}
      </div>

      <div style="position:absolute;top:78px;left:24px;right:24px;z-index:10;">
        {kicker("Na prática, são dois negócios", color=ACCENT["mist"])}

        <div style="margin-top:14px;line-height:0.96;">
          <div class="display" style="font-size:32px;color:#fff;
                      letter-spacing:{TRACK["tight"]};">DOIS NEGÓCIOS,</div>
          <div class="display" style="font-size:32px;color:{ACCENT["primary"]};
                      letter-spacing:{TRACK["tight"]};margin-top:2px;
                      text-shadow:0 0 24px rgba(30,197,242,0.35);">DUAS REALIDADES.</div>
        </div>
      </div>

      <!-- DUAL COLUMN -->
      <div style="position:absolute;top:208px;left:24px;right:24px;z-index:10;
                  display:flex;gap:14px;">

        <!-- coluna A — sem dado -->
        <div style="flex:1;padding:16px 14px;
                    background:rgba(255,255,255,0.025);
                    border:1px solid rgba(255,255,255,0.08);
                    border-radius:{RADIUS["md"]}px;">
          <div style="font-family:{FONTS["body"]};font-size:9.5px;font-weight:700;
                      color:rgba(255,255,255,0.45);
                      letter-spacing:{TRACK["label"]};text-transform:uppercase;
                      margin-bottom:8px;">
            SEM DADO
          </div>
          {items_a}
        </div>

        <!-- coluna B — com dado (glow) -->
        <div style="flex:1;padding:16px 14px;
                    background:linear-gradient(135deg, rgba(30,197,242,0.12) 0%, rgba(30,197,242,0.04) 100%);
                    border:1px solid rgba(30,197,242,0.32);
                    border-radius:{RADIUS["md"]}px;
                    box-shadow:0 0 36px rgba(30,197,242,0.22),
                               inset 0 1px 0 rgba(255,255,255,0.10);">
          <div style="font-family:{FONTS["body"]};font-size:9.5px;font-weight:700;
                      color:{ACCENT["primary"]};
                      letter-spacing:{TRACK["label"]};text-transform:uppercase;
                      margin-bottom:8px;">
            COM DADO
          </div>
          {items_b}
        </div>
      </div>

      <div style="position:absolute;bottom:40px;left:24px;right:24px;z-index:10;
                  font-family:{FONTS["body"]};font-size:11.5px;
                  color:rgba(255,255,255,0.62);line-height:1.45;font-style:italic;">
        A diferença entre os dois <strong style="color:#fff;font-weight:700;
        font-style:normal;">não é orçamento. É clareza.</strong>
      </div>

      {progress_bar(6, TOTAL)}
    </div>'''

# ============================================================
# SLIDE 7 — SÍNTESE (bleed gradient)
# Amarra tudo. Princípio inegável.
# Termina com afirmação que prepara o espelho.
# ============================================================
def slide7():
    return f'''<div class="slide" style="{bg_brand_atmo()}">
      {overlay_noise(0.38, blend="overlay")}
      {overlay_vignette(0.4)}
      {slide_index(7, TOTAL)}

      <div style="display:flex;justify-content:center;padding-top:26px;position:relative;z-index:5;">
        {logo_mark(dark_bg=True, size=22)}
      </div>

      <div style="position:absolute;top:50%;left:0;right:0;z-index:10;
                  transform:translateY(-50%);text-align:center;padding:0 26px;">
        {kicker("É por isso que", color="rgba(255,255,255,0.78)")}

        <div style="margin-top:16px;line-height:0.94;">
          <div class="display" style="font-size:48px;color:#fff;
                      letter-spacing:{TRACK["tight"]};
                      text-shadow:0 4px 24px rgba(0,0,0,0.45);">NÃO EXISTE</div>
          <div class="display" style="font-size:48px;color:#fff;
                      letter-spacing:{TRACK["tight"]};margin-top:4px;
                      text-shadow:0 4px 24px rgba(0,0,0,0.45);">CRESCIMENTO</div>
          <div class="display" style="font-size:42px;color:rgba(255,255,255,0.82);
                      letter-spacing:{TRACK["tight"]};margin-top:6px;
                      text-shadow:0 4px 24px rgba(0,0,0,0.45);">SEM</div>
          <div class="display" style="font-size:42px;
                      background:linear-gradient(95deg, #fff 0%, {ACCENT["ice"]} 100%);
                      -webkit-background-clip:text;-webkit-text-fill-color:transparent;
                      background-clip:text;
                      letter-spacing:{TRACK["tight"]};margin-top:4px;">DIAGNÓSTICO.</div>
        </div>

        <div style="margin-top:26px;height:1.5px;width:48px;
                    background:rgba(255,255,255,0.55);margin-left:auto;margin-right:auto;"></div>

        <div style="margin-top:20px;font-family:{FONTS["body"]};font-size:13.5px;
                    color:rgba(255,255,255,0.88);line-height:1.5;max-width:340px;
                    margin-left:auto;margin-right:auto;
                    text-shadow:0 2px 10px rgba(0,0,0,0.35);">
          Tudo o que veio antes do dado, é só palpite caro.
        </div>
      </div>

      {progress_bar(7, TOTAL)}
    </div>'''

# ============================================================
# SLIDE 8 — ESPELHO (sem CTA comercial)
# Devolve a pergunta. Lucas + Derick photo de fundo.
# ============================================================
def slide8():
    img = photo_uri("lucas_derick.jpeg")
    pos = photo_position("lucas_derick.jpeg")
    return f'''<div class="slide" style="background:{INK["void"]};overflow:hidden;">
      <!-- foto fundo -->
      <div style="position:absolute;inset:0;z-index:1;">
        <img src="{img}" style="width:100%;height:100%;object-fit:cover;
                   object-position:{pos};
                   filter:contrast(1.08) saturate(0.86) brightness(0.55);">
        <div style="position:absolute;inset:0;background:linear-gradient(180deg,
                    rgba(5,8,15,0.55) 0%, rgba(5,8,15,0.78) 55%, rgba(5,8,15,0.92) 100%);"></div>
      </div>

      {overlay_noise(0.30, z=4)}
      {slide_index(8, TOTAL)}

      <div style="display:flex;justify-content:center;padding-top:26px;position:relative;z-index:10;">
        {logo_mark(dark_bg=True, size=22)}
      </div>

      <div style="position:absolute;top:130px;left:26px;right:26px;z-index:14;">
        {kicker("Agora a pergunta volta pra você", color=ACCENT["mist"])}

        <div style="margin-top:16px;line-height:0.94;">
          <div class="display" style="font-size:42px;color:#fff;
                      letter-spacing:{TRACK["tight"]};
                      text-shadow:0 4px 22px rgba(0,0,0,0.65);">SE VOCÊ NÃO SABE</div>
          <div class="display" style="font-size:48px;color:{ACCENT["primary"]};
                      letter-spacing:{TRACK["tight"]};margin-top:4px;
                      text-shadow:0 4px 22px rgba(0,0,0,0.65),
                                  0 0 36px rgba(30,197,242,0.40);">OS SEUS 13%,</div>
          <div class="display" style="font-size:38px;color:#fff;margin-top:8px;
                      letter-spacing:{TRACK["tight"]};
                      text-shadow:0 4px 22px rgba(0,0,0,0.65);">O QUE VOCÊ ESTÁ</div>
          <div class="display" style="font-size:38px;color:#fff;margin-top:2px;
                      letter-spacing:{TRACK["tight"]};
                      text-shadow:0 4px 22px rgba(0,0,0,0.65);">OTIMIZANDO?</div>
        </div>
      </div>

      <div style="position:absolute;bottom:48px;left:26px;right:26px;z-index:18;">
        <div style="height:1px;width:44px;background:rgba(255,255,255,0.32);
                    margin-bottom:16px;"></div>
        <div style="font-family:{FONTS["body"]};font-size:13.5px;font-weight:400;
                    color:rgba(255,255,255,0.84);line-height:1.5;max-width:340px;">
          Antes de gastar o próximo real, descubra<br>
          <strong style="color:#fff;font-weight:700;">o que realmente está dando retorno.</strong>
        </div>
        <div style="margin-top:18px;font-family:{FONTS["body"]};font-size:9px;
                    font-weight:600;color:rgba(255,255,255,0.42);
                    letter-spacing:{TRACK["label"]};text-transform:uppercase;">
          @nucvision
        </div>
      </div>

      {progress_bar(8, TOTAL)}
    </div>'''

# ============================================================
# COMPOSE
# ============================================================
slides = "".join([slide1(), slide2(), slide3(), slide4(),
                  slide5(), slide6(), slide7(), slide8()])
caption = ("87% do seu marketing não funciona — e você ainda não sabe qual parte é. "
           "Antes de investir mais, entenda o que realmente está dando retorno.")
html = html_shell(slides, TOTAL, caption)

OUT = Path("/home/user/Meu-espa-o/nucvision-editorial.html")
OUT.write_text(html, encoding="utf-8")
print(f"OK {OUT} ({len(html):,} chars)")
