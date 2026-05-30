#!/usr/bin/env python3
"""
NUC Vision — Carrossel Trend v2: "A marca que não fez nada venceu"
Geração DO ZERO, arco diferente do anterior:
  Modelo 2 — Quebra de Crença (crença → conflito → evidência → revelação).
  Hook = paradoxo (não "perdeu bilhões"). Sem balões/prints fabricados —
  reação de mercado tratada como LEITURA/análise (Seção -1, caminho B).
Formato: 420×525px → exportado a 1080×1350px.
"""
import sys, base64
from pathlib import Path
sys.path.insert(0, "/home/user/Meu-espa-o")
sys.path.insert(0, "/home/user/Meu-espa-o/geradores")
from design_system import (
    INK, ACCENT, FONTS, LOGO_URI, overlay_vignette, html_shell,
)
from nuc_realism import (
    REALISM_CSS, GRAO_OVERLAY, fundo_profundo, recorte, sombra_contato, card,
)

FOTOS = Path("/home/user/Meu-espa-o/fotos")
TOTAL = 7
CAPTION = ("A marca que não fez nada venceu a que fez tudo. Parece contradição, "
           "mas é a regra de posicionamento mais ignorada do mercado. "
           "Desliza até o fim. 👇 "
           "#posicionamento #marca #branding #ferrari #lamborghini #nucvision")

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
    return (f'<span style="background:{ACCENT["primary"]};color:#06121c;'
            f'padding:0 11px 4px;border-radius:8px;'
            f'box-shadow:0 6px 24px rgba(30,197,242,0.45);">{word}</span>')

def dot_grid(color="rgba(30,197,242,0.06)", sp=28, z=0):
    return (f'<div style="position:absolute;inset:0;z-index:{z};'
            f'background-image:radial-gradient(circle,{color} 1.2px,transparent 1.2px);'
            f'background-size:{sp}px {sp}px;"></div>')

def bridge(text):
    return (f'<div style="display:flex;align-items:center;gap:9px;margin-top:18px;">'
            f'<div style="width:22px;height:2px;background:{ACCENT["primary"]};flex-shrink:0;"></div>'
            f'<span style="font-family:{FONTS["body"]},sans-serif;font-size:12.5px;'
            f'font-style:italic;color:{ACCENT["primary"]};line-height:1.45;font-weight:500;">{text}</span></div>')

def disclaimer(text):
    """Marca leitura/análise — NÃO finge ser print/manchete real (Seção -1)."""
    return (f'<div style="font-family:{FONTS["body"]},sans-serif;font-size:9px;'
            f'letter-spacing:0.04em;color:rgba(255,255,255,0.32);margin-top:14px;">{text}</div>')


# ── S1 · GANCHO (paradoxo, tipográfico forte + 2 carros confrontados) ──────────

def slide1():
    luce  = photo_uri("ferrari_luce_trim.png")
    lambo = photo_uri("lamborghini_trim.png")
    return f'''<div class="slide" style="overflow:hidden;
        background:radial-gradient(ellipse 120% 90% at 50% 70%,#15121F 0%,#0B0D16 55%,#06070D 100%);">
      {dot_grid(color="rgba(255,255,255,0.05)")}
      {logo()}

      <!-- TÍTULO no topo, ocupando a metade de cima -->
      <div style="position:absolute;top:62px;left:28px;right:28px;z-index:12;">
        {kicker("Leitura de Mercado")}
        <div class="display" style="font-size:43px;color:#fff;line-height:0.90;">
          A MARCA QUE<br>NÃO FEZ {hl("NADA")}
        </div>
        <div class="display" style="font-size:43px;color:rgba(255,255,255,0.45);
                    line-height:0.90;margin-top:8px;">
          VENCEU A QUE<br>FEZ <span style="color:#fff;">TUDO.</span>
        </div>
      </div>

      <!-- dois carros confrontados embaixo, sangrando levemente -->
      <div style="position:absolute;bottom:74px;left:0;right:0;height:200px;z-index:1;
                  background:radial-gradient(ellipse at 30% 60%,rgba(220,50,50,0.16),transparent 60%),
                    radial-gradient(ellipse at 72% 55%,rgba(220,180,20,0.18),transparent 60%);
                  filter:blur(8px);"></div>
      <div class="subject" style="position:absolute;bottom:62px;left:-44px;width:236px;z-index:2;
                  filter:grayscale(0.55) brightness(0.8);">
        <img src="{luce}" style="width:100%;display:block;">
      </div>
      <div class="subject" style="position:absolute;bottom:50px;right:-40px;width:248px;z-index:3;
                  transform:scaleX(-1);">
        <img src="{lambo}" style="width:100%;display:block;">
      </div>

      <!-- selo PASSE -->
      <div style="position:absolute;bottom:24px;left:50%;transform:translateX(-50%);z-index:14;
                  display:inline-flex;align-items:center;gap:8px;
                  background:rgba(255,255,255,0.10);border:1px solid rgba(255,255,255,0.28);
                  padding:8px 18px;border-radius:999px;backdrop-filter:blur(8px);">
        <span style="font-family:{FONTS["body"]},sans-serif;font-size:11px;color:#fff;
                     font-weight:700;letter-spacing:0.1em;">ENTENDA O PARADOXO ››</span>
      </div>
    </div>'''


# ── S2 · CRENÇA (a crença que todos têm — tipográfico, fundo limpo) ────────────

def slide2():
    return f'''<div class="slide" style="overflow:hidden;
        background:linear-gradient(165deg,#0E1320 0%,{INK["deep"]} 60%,#070910 100%);">
      {dot_grid(color="rgba(30,197,242,0.05)")}
      {logo()}

      <div style="position:absolute;top:58px;left:28px;right:28px;bottom:0;
                  display:flex;flex-direction:column;justify-content:center;z-index:10;">
        {kicker("O Que Todo Mundo Acredita")}
        <div class="display" style="font-size:38px;color:#fff;line-height:0.96;margin-bottom:18px;">
          "PRA CRESCER,<br>TEM QUE SE<br>{hl("REINVENTAR")}."
        </div>
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:14px;
                    color:rgba(255,255,255,0.72);line-height:1.62;max-width:316px;">
          Inovar sempre. Acompanhar toda tendência. Mudar antes de ficar para trás.
          É o que o mercado repete como verdade absoluta.
        </div>
        {bridge("Foi exatamente o que uma das marcas decidiu fazer.")}
      </div>
    </div>'''


# ── S3 · CONFLITO (Ferrari apostou na mudança e foi punida — Luce protagonista) ─

def slide3():
    luce = photo_uri("ferrari_luce_trim.png")
    return f'''<div class="slide" style="overflow:hidden;background:#0b0710;">
      {fundo_profundo(luce, extra_style="filter:blur(22px) brightness(0.40) saturate(1.05);")}
      {dot_grid(color="rgba(255,255,255,0.04)")}
      {logo()}

      <div style="position:absolute;top:58px;left:28px;right:28px;z-index:10;">
        {kicker("A Aposta")}
        <div class="display" style="font-size:35px;color:#fff;line-height:0.92;">
          UMA DELAS MUDOU<br>{hl("RADICALMENTE")}
        </div>
      </div>

      <!-- Luce centralizada, ancorada -->
      <div style="position:absolute;top:188px;left:50%;transform:translateX(-50%);
                  width:300px;height:130px;z-index:1;
                  background:radial-gradient(ellipse at 50% 60%,rgba(90,170,225,0.20),transparent 66%);filter:blur(6px);"></div>
      <div class="subject" style="position:absolute;top:178px;left:50%;transform:translateX(-50%);width:308px;z-index:2;">
        <img src="{luce}" style="width:100%;display:block;">
      </div>

      <div style="position:absolute;left:0;right:0;bottom:0;height:42%;z-index:8;
                  background:linear-gradient(180deg,transparent,rgba(11,7,16,0.6) 28%,#0b0710 60%);"></div>
      <div style="position:absolute;left:0;right:0;bottom:0;padding:0 28px 40px;z-index:10;">
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:13.5px;
                    color:rgba(255,255,255,0.78);line-height:1.6;max-width:312px;">
          Apostou numa virada de identidade para acompanhar o mercado.
          A leitura nas redes foi dura — e o valor da marca sentiu o baque.
        </div>
        {disclaimer("Leitura de repercussão pública, não cotação oficial.")}
        {bridge("Enquanto isso, a concorrente fez o oposto.")}
      </div>
    </div>'''


# ── S4 · EVIDÊNCIA (Lamborghini recusou a tendência — Lambo viva, vencedora) ────

def slide4():
    lambo = photo_uri("lamborghini_trim.png")
    return f'''<div class="slide" style="overflow:hidden;background:#0a0a06;">
      {fundo_profundo(lambo, extra_style="filter:blur(22px) brightness(0.42) saturate(1.15);")}
      {dot_grid(color="rgba(255,255,255,0.04)")}
      {logo()}

      <div style="position:absolute;top:58px;left:28px;right:28px;z-index:10;">
        {kicker("A Recusa")}
        <div class="display" style="font-size:35px;color:#fff;line-height:0.92;">
          A OUTRA SE RECUSOU<br>A {hl("MUDAR")}
        </div>
      </div>

      <div style="position:absolute;top:188px;left:50%;transform:translateX(-50%);
                  width:300px;height:130px;z-index:1;
                  background:radial-gradient(ellipse at 50% 60%,rgba(220,180,20,0.22),transparent 68%);filter:blur(8px);"></div>
      <div class="subject" style="position:absolute;top:182px;left:50%;transform:translateX(-50%) rotate(-2deg);width:308px;z-index:2;">
        <img src="{lambo}" style="width:100%;display:block;">
      </div>

      <div style="position:absolute;left:0;right:0;bottom:0;height:42%;z-index:8;
                  background:linear-gradient(180deg,transparent,rgba(10,10,6,0.62) 30%,#0a0a06 62%);"></div>
      <div style="position:absolute;left:0;right:0;bottom:0;padding:0 28px 40px;z-index:10;">
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:13.5px;
                    color:rgba(255,255,255,0.78);line-height:1.6;max-width:312px;">
          Manteve a identidade, ignorou a pressão por reinvenção —
          e <strong style="color:#fff;">saiu na frente sem gastar com isso.</strong>
        </div>
        {bridge("E aqui está a regra que quase ninguém entende.")}
      </div>
    </div>'''


# ── S5 · REVELAÇÃO (a crença quebra — coerência, não inovação) ─────────────────

def slide5():
    return f'''<div class="slide" style="overflow:hidden;
        background:radial-gradient(ellipse 110% 85% at 50% 38%,#0E2236 0%,{INK["void"]} 58%,#040509 100%);">
      {dot_grid(color="rgba(30,197,242,0.05)")}
      <div style="position:absolute;top:36%;left:50%;transform:translate(-50%,-50%);
                  width:320px;height:320px;z-index:1;pointer-events:none;
                  background:radial-gradient(circle,rgba(30,197,242,0.14),transparent 66%);filter:blur(8px);"></div>
      {logo()}

      <div style="position:absolute;top:58px;left:28px;right:28px;bottom:0;
                  display:flex;flex-direction:column;justify-content:center;z-index:10;">
        {kicker("A Regra")}
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:15px;
                    color:rgba(255,255,255,0.55);line-height:1.5;margin-bottom:14px;">
          O mercado não recompensou quem mudou mais.
        </div>
        <div class="display" style="font-size:40px;color:#fff;line-height:0.94;margin-bottom:16px;">
          RECOMPENSOU<br>QUEM FOI<br>{hl("COERENTE")}
        </div>
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:14px;
                    color:rgba(255,255,255,0.72);line-height:1.62;max-width:316px;">
          Posicionamento não é inovar sem parar. É saber o que você
          <strong style="color:#fff;">não abre mão de ser</strong> — mesmo sob pressão.
        </div>
      </div>
      {overlay_vignette(0.36, z=3)}
    </div>'''


# ── S6 · INSIGHT (frase memorável, tipográfico puro) ───────────────────────────

def slide6():
    return f'''<div class="slide" style="overflow:hidden;
        background:radial-gradient(ellipse 100% 80% at 70% 34%,#101A2C 0%,{INK["void"]} 60%,#040509 100%);">
      {dot_grid(color="rgba(255,255,255,0.035)")}
      <div style="position:absolute;top:36%;right:24%;transform:translate(50%,-50%);
                  width:300px;height:300px;z-index:1;pointer-events:none;
                  background:radial-gradient(circle,rgba(30,197,242,0.16),transparent 66%);filter:blur(6px);"></div>
      {logo()}

      <div class="display" style="position:absolute;top:66px;right:24px;z-index:9;
                  font-size:150px;line-height:0.7;color:{ACCENT["primary"]};opacity:0.20;">”</div>
      <div style="position:absolute;top:158px;left:30px;z-index:10;">{kicker("O Insight")}</div>

      <div style="position:absolute;top:190px;left:30px;right:30px;z-index:10;">
        <div class="display" style="font-size:40px;color:#fff;line-height:1.0;">
          O MERCADO NÃO<br>PUNE QUEM
        </div>
        <div class="display" style="font-size:40px;color:rgba(255,255,255,0.45);line-height:1.0;margin:6px 0;">
          NÃO MUDA.
        </div>
        <div class="display" style="font-size:40px;color:#fff;line-height:1.0;margin-top:16px;">
          PUNE QUEM TRAI<br>A PRÓPRIA<br>{hl("IDENTIDADE.")}
        </div>
      </div>
      {overlay_vignette(0.42, z=3)}
    </div>'''


# ── S7 · CTA ─────────────────────────────────────────────────────────────────

def slide7():
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
    raw = [slide1(), slide2(), slide3(), slide4(), slide5(), slide6(), slide7()]
    parts = []
    for s in raw:
        idx = s.rfind("</div>")
        parts.append(s[:idx] + GRAO_OVERLAY + s[idx:])
    slides = f"<style>{REALISM_CSS}</style>" + "".join(parts)
    html = html_shell(slides, TOTAL, CAPTION)
    out = Path("/home/user/Meu-espa-o/previews/nucvision-ferrari-lambo-v2.html")
    out.write_text(html, encoding="utf-8")
    print(f"✓ {out}")

if __name__ == "__main__":
    main()
