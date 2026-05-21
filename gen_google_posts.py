#!/usr/bin/env python3
"""
NUC Vision — Google Meu Negócio Posts
10 posts independentes, formato quadrado 420×420 → exportados a 1080×1080px
"""
import sys
from pathlib import Path
sys.path.insert(0, "/home/user/Meu-espa-o")
from design_system import (
    FONT_LINK, INK, PAPER, ACCENT, GRAY,
    FONTS, TRACK, LINE, LOGO_URI, NOISE_B64,
    overlay_vignette,
)

VW = VH = 420
TOTAL = 10

# ── Shared helpers ─────────────────────────────────────────────────────────────

def noise_layer(opacity=0.32, z=2):
    return (f'<div style="position:absolute;inset:0;z-index:{z};'
            f'background-image:url(\'data:image/svg+xml;base64,{NOISE_B64}\');'
            f'background-size:240px 240px;opacity:{opacity};'
            f'mix-blend-mode:overlay;pointer-events:none;"></div>')

def logo_top(white=True, size=22, top=18):
    flt = ("filter:brightness(0) invert(1) "
           "drop-shadow(0 2px 10px rgba(0,0,0,0.6));") if white else ""
    return (f'<div style="position:absolute;top:{top}px;left:0;right:0;'
            f'display:flex;justify-content:center;z-index:20;">'
            f'<img src="{LOGO_URI}" style="height:{size}px;width:auto;{flt}"></div>')

def bottom_strip(text="agencianuc.com.br", light=False):
    fg     = ACCENT["primary"] if not light else INK["medium"]
    border = "rgba(30,197,242,0.15)" if not light else PAPER["border"]
    return (
        f'<div style="position:absolute;bottom:0;left:0;right:0;z-index:22;'
        f'padding:10px 22px;border-top:1px solid {border};'
        f'display:flex;justify-content:space-between;align-items:center;">'
        f'<span style="font-family:{FONTS["body"]},sans-serif;font-size:9.5px;'
        f'font-weight:700;letter-spacing:0.2em;text-transform:uppercase;'
        f'color:{fg};">NUC VISION</span>'
        f'<span style="font-family:{FONTS["body"]},sans-serif;font-size:9.5px;'
        f'color:{fg};opacity:0.65;">{text}</span></div>'
    )

def kicker(text, color=None):
    c = color or ACCENT["primary"]
    return (f'<div style="font-family:{FONTS["body"]},sans-serif;font-size:10px;'
            f'font-weight:700;letter-spacing:0.2em;text-transform:uppercase;'
            f'color:{c};margin-bottom:10px;">{text}</div>')

def pill_word(word, size=42):
    return (
        f'<span class="display" style="display:inline-block;'
        f'background:{ACCENT["primary"]};color:#fff;'
        f'padding:2px 16px 7px;border-radius:12px;font-size:{size}px;'
        f'box-shadow:0 4px 22px rgba(30,197,242,0.45);">{word}</span>'
    )

def dot_grid(color="rgba(30,197,242,0.07)", spacing=28, z=0):
    return (f'<div style="position:absolute;inset:0;z-index:{z};'
            f'background-image:radial-gradient(circle,{color} 1.2px,transparent 1.2px);'
            f'background-size:{spacing}px {spacing}px;"></div>')

def hr_line(width=44, mt=14):
    return (f'<div style="width:{width}px;height:2px;background:{ACCENT["primary"]};'
            f'border-radius:2px;margin-top:{mt}px;"></div>')

def glow_radial(top=-80, width=280, opacity_hex="rgba(30,197,242,0.13)"):
    return (
        f'<div style="position:absolute;top:{top}px;left:50%;'
        f'transform:translateX(-50%);width:{width}px;height:200px;'
        f'background:radial-gradient(ellipse,{opacity_hex} 0%,transparent 70%);'
        f'z-index:1;pointer-events:none;"></div>'
    )

# ── POST 1 — Autoridade: não é marketing, é estrutura ─────────────────────────

def post1():
    p = pill_word("MARKETING.", 40)
    return f'''<div class="slide" style="background:{INK["void"]};">
      {dot_grid()}
      {noise_layer(0.3)}
      {glow_radial()}
      {logo_top()}
      <div style="position:absolute;top:55px;left:0;right:0;bottom:42px;
                  display:flex;flex-direction:column;justify-content:center;
                  padding:0 26px;z-index:10;">
        {kicker("Sobre a NUC Vision")}
        <div class="display" style="font-size:44px;color:#fff;margin-bottom:14px;">
          VOCÊ NÃO<br>PRECISA DE<br>MAIS {p}
        </div>
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:13.5px;
                    color:rgba(255,255,255,0.58);line-height:1.55;">
          Antes de qualquer campanha, identificamos<br>
          o que está travando o crescimento<br>
          da sua empresa.
        </div>
        {hr_line()}
      </div>
      {bottom_strip()}
      {overlay_vignette(0.38, z=3)}
    </div>'''


# ── POST 2 — Gargalos invisíveis ───────────────────────────────────────────────

def _gargalo_row(label, dot_color):
    return (
        f'<div style="display:flex;align-items:center;gap:12px;'
        f'padding:9px 14px;margin-bottom:7px;'
        f'background:rgba(255,255,255,0.04);border-radius:8px;'
        f'border:1px solid rgba(255,255,255,0.07);">'
        f'<div style="width:8px;height:8px;border-radius:50%;flex-shrink:0;'
        f'background:{dot_color};box-shadow:0 0 8px {dot_color};"></div>'
        f'<span style="font-family:{FONTS["body"]},sans-serif;font-size:13px;'
        f'color:rgba(255,255,255,0.82);font-weight:500;">{label}</span>'
        f'</div>'
    )

def post2():
    rows  = _gargalo_row("Atendimento lento",        "rgba(255,80,80,0.9)")
    rows += _gargalo_row("Sem processo comercial",   "rgba(255,160,40,0.9)")
    rows += _gargalo_row("CRM desorganizado",        "rgba(255,80,80,0.9)")
    rows += _gargalo_row("Posicionamento confuso",   "rgba(255,160,40,0.9)")
    rows += _gargalo_row("Tráfego sem retorno",      "rgba(255,80,80,0.9)")

    p = pill_word("SEM VOCÊ VER", 26)
    return f'''<div class="slide" style="background:{INK["deep"]};">
      {dot_grid("rgba(30,197,242,0.05)", 32)}
      {noise_layer(0.28)}
      {logo_top()}
      <div style="position:absolute;top:55px;left:0;right:0;bottom:42px;
                  display:flex;flex-direction:column;justify-content:center;
                  padding:0 24px;z-index:10;">
        {kicker("Gargalos Invisíveis")}
        <div class="display" style="font-size:34px;color:#fff;
                    margin-bottom:16px;line-height:0.95;">
          O QUE TRAVA<br>SEU NEGÓCIO<br>{p}
        </div>
        {rows}
      </div>
      {bottom_strip()}
      {overlay_vignette(0.3, z=3)}
    </div>'''


# ── POST 3 — Processo: arrume a casa antes de anunciar ────────────────────────

def _step_box(icon, label):
    return (
        f'<div style="display:flex;flex-direction:column;align-items:center;gap:6px;flex:1;">'
        f'<div style="width:40px;height:40px;border-radius:10px;'
        f'background:rgba(30,197,242,0.12);border:1px solid rgba(30,197,242,0.25);'
        f'display:flex;align-items:center;justify-content:center;font-size:18px;">{icon}</div>'
        f'<span style="font-family:{FONTS["body"]},sans-serif;font-size:10px;'
        f'font-weight:600;color:rgba(255,255,255,0.65);text-transform:uppercase;'
        f'letter-spacing:0.1em;">{label}</span></div>'
    )

def _arrow_sep():
    return (
        f'<div style="color:rgba(30,197,242,0.5);font-size:14px;padding-top:10px;">→</div>'
    )

def post3():
    steps_html = _arrow_sep().join([
        _step_box("🔍", "Diagnóstico"),
        _step_box("🏗", "Estrutura"),
        _step_box("📊", "Estratégia"),
        _step_box("🚀", "Campanha"),
    ])
    p = pill_word("ARRUME A CASA.", 34)
    return f'''<div class="slide" style="background:linear-gradient(155deg,{INK["rich"]} 0%,{INK["void"]} 100%);">
      {dot_grid("rgba(30,197,242,0.06)", 36)}
      {noise_layer(0.3)}
      {logo_top()}
      <div style="position:absolute;top:55px;left:0;right:0;bottom:42px;
                  display:flex;flex-direction:column;justify-content:center;
                  padding:0 26px;z-index:10;">
        {kicker("Método NUC Vision")}
        <div class="display" style="font-size:42px;color:#fff;margin-bottom:6px;">
          ANTES DE<br>ANUNCIAR,
        </div>
        <div class="display" style="font-size:34px;margin-bottom:20px;">{p}</div>
        <div style="display:flex;align-items:flex-start;gap:4px;">
          {steps_html}
        </div>
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:12px;
                    color:rgba(255,255,255,0.42);margin-top:12px;line-height:1.5;">
          Estruturamos o comercial antes de ativar qualquer campanha.
        </div>
      </div>
      {bottom_strip()}
      {overlay_vignette(0.35, z=3)}
    </div>'''


# ── POST 4 — CRM e gestão de leads ────────────────────────────────────────────

def post4():
    cyan = ACCENT["primary"]
    wm   = (f'<div class="display" style="position:absolute;right:-14px;top:50%;'
            f'transform:translateY(-50%);font-size:200px;line-height:1;'
            f'color:rgba(30,197,242,0.05);z-index:1;pointer-events:none;'
            f'user-select:none;">0</div>')
    return f'''<div class="slide" style="background:{INK["void"]};">
      {noise_layer(0.32)}
      {wm}
      {logo_top()}
      <div style="position:absolute;top:55px;left:0;right:0;bottom:42px;
                  display:flex;flex-direction:column;justify-content:center;
                  padding:0 26px;z-index:10;">
        {kicker("CRM · Gestão de Leads")}
        <div class="display" style="font-size:50px;color:{cyan};line-height:0.9;margin-bottom:10px;">
          QUANTOS<br>LEADS
        </div>
        <div class="display" style="font-size:30px;color:#fff;margin-bottom:16px;">
          VOCÊ PERDEU<br>ESSA SEMANA?
        </div>
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:13px;
                    color:rgba(255,255,255,0.57);line-height:1.55;">
          CRM desorganizado, follow-up inexistente<br>
          e conversas esquecidas destroem<br>
          faturamento silenciosamente.
        </div>
        {hr_line(48, 14)}
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:12px;
                    color:{cyan};font-weight:600;margin-top:10px;">
          A NUC Vision implementa e organiza seu CRM.
        </div>
      </div>
      {bottom_strip()}
    </div>'''


# ── POST 5 — Tráfego pago sem estratégia ──────────────────────────────────────

def post5():
    cyan = ACCENT["primary"]
    funnel_svg = (
        f'<svg width="90" height="150" viewBox="0 0 90 150" xmlns="http://www.w3.org/2000/svg">'
        f'<polygon points="5,0 85,0 62,55 28,55" fill="{cyan}" opacity="0.9"/>'
        f'<rect x="32" y="60" width="26" height="38" rx="4" fill="{cyan}" opacity="0.7"/>'
        f'<rect x="40" y="102" width="10" height="28" rx="3" fill="rgba(255,80,80,0.8)"/>'
        f'<ellipse cx="45" cy="118" rx="6" ry="3.5" fill="{INK["void"]}"/>'
        f'</svg>'
    )
    p = pill_word("GASTO.", 38)
    return f'''<div class="slide" style="background:{INK["void"]};">
      {noise_layer(0.3)}
      <div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);
                  width:300px;height:300px;
                  background:radial-gradient(circle,rgba(30,197,242,0.09) 0%,transparent 65%);
                  z-index:1;pointer-events:none;"></div>
      <div style="position:absolute;right:18px;top:50%;transform:translateY(-50%);
                  opacity:0.18;z-index:1;">{funnel_svg}</div>
      {logo_top()}
      <div style="position:absolute;top:55px;left:0;right:0;bottom:42px;
                  display:flex;flex-direction:column;justify-content:center;
                  padding:0 26px;z-index:10;">
        {kicker("Tráfego Pago")}
        <div class="display" style="font-size:40px;color:#fff;margin-bottom:12px;">
          TRÁFEGO SEM<br>ESTRATÉGIA É {p}
        </div>
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:13px;
                    color:rgba(255,255,255,0.57);line-height:1.55;">
          Enchemos o topo do funil. Mas se o<br>
          fundo está furado, nada converte.
        </div>
        {hr_line(40, 12)}
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:11.5px;
                    color:rgba(255,255,255,0.4);margin-top:8px;">
          Analisamos funil, oferta, landing page e<br>
          atendimento antes de ativar qualquer anúncio.
        </div>
      </div>
      {bottom_strip()}
      {overlay_vignette(0.4, z=3)}
    </div>'''


# ── POST 6 — Posicionamento: clareza primeiro ─────────────────────────────────

def _pos_row_left(text):
    return (
        f'<div style="font-family:{FONTS["body"]},sans-serif;font-size:11px;'
        f'color:rgba(255,255,255,0.28);line-height:1;margin-bottom:9px;'
        f'text-decoration:line-through;">{text}</div>'
    )

def _pos_row_right(text):
    return (
        f'<div style="font-family:{FONTS["body"]},sans-serif;font-size:11px;'
        f'color:rgba(255,255,255,0.88);line-height:1;margin-bottom:9px;">{text}</div>'
    )

def post6():
    questions = [
        "Para quem é?",
        "Qual problema resolve?",
        "Por que é diferente?",
        "Qual resultado entrega?",
    ]
    left_rows  = "".join(_pos_row_left(q)  for q in questions)
    right_rows = "".join(_pos_row_right(q) for q in questions)

    cyan = ACCENT["primary"]
    divider = (
        f'<div style="position:absolute;left:50%;top:0;bottom:0;width:1px;'
        f'background:linear-gradient(180deg,transparent 5%,{cyan} 30%,{cyan} 70%,transparent 95%);'
        f'transform:translateX(-50%);z-index:8;"></div>'
    )
    footer = (
        f'<div style="position:absolute;bottom:42px;left:0;right:0;z-index:10;'
        f'padding:8px 22px;text-align:center;'
        f'border-top:1px solid rgba(255,255,255,0.06);'
        f'font-family:{FONTS["body"]},sans-serif;font-size:11px;'
        f'color:rgba(255,255,255,0.45);">'
        f'Se o cliente não entende o que você faz, ele não compra.</div>'
    )
    return f'''<div class="slide" style="background:{INK["void"]};">
      {noise_layer(0.28)}
      <div style="position:absolute;left:0;top:0;width:50%;bottom:0;
                  background:rgba(0,0,0,0.22);z-index:0;"></div>
      {divider}
      {logo_top()}
      <div style="position:absolute;top:55px;left:0;right:0;bottom:85px;
                  display:flex;z-index:10;">
        <div style="flex:1;padding:0 14px 0 22px;display:flex;flex-direction:column;justify-content:center;">
          <div style="font-family:{FONTS["body"]},sans-serif;font-size:9px;font-weight:700;
                      letter-spacing:0.2em;text-transform:uppercase;
                      color:rgba(255,80,80,0.7);margin-bottom:10px;">SEM</div>
          <div class="display" style="font-size:22px;color:rgba(255,255,255,0.22);
                      margin-bottom:14px;line-height:1.05;">POSICIO-<br>NAMENTO</div>
          {left_rows}
        </div>
        <div style="flex:1;padding:0 14px 0 20px;display:flex;flex-direction:column;justify-content:center;">
          <div style="font-family:{FONTS["body"]},sans-serif;font-size:9px;font-weight:700;
                      letter-spacing:0.2em;text-transform:uppercase;
                      color:{cyan};margin-bottom:10px;">COM</div>
          <div class="display" style="font-size:22px;color:#fff;
                      margin-bottom:14px;line-height:1.05;">POSICIO-<br>NAMENTO</div>
          {right_rows}
        </div>
      </div>
      {footer}
      {bottom_strip()}
    </div>'''


# ── POST 7 — Atendimento: estatística de impacto ──────────────────────────────

def post7():
    cyan = ACCENT["primary"]
    wm = (
        f'<div class="display" style="position:absolute;left:-8px;top:50%;'
        f'transform:translateY(-55%);font-size:160px;line-height:1;'
        f'color:rgba(30,197,242,0.06);z-index:1;pointer-events:none;'
        f'user-select:none;">70%</div>'
    )
    return f'''<div class="slide" style="background:{INK["deep"]};">
      {dot_grid("rgba(30,197,242,0.06)", 30)}
      {noise_layer(0.3)}
      {wm}
      {logo_top()}
      <div style="position:absolute;top:55px;left:0;right:0;bottom:42px;
                  display:flex;flex-direction:column;justify-content:center;
                  padding:0 26px;z-index:10;">
        {kicker("Atendimento · Conversão")}
        <div class="display" style="font-size:72px;color:{cyan};
                    line-height:0.88;margin-bottom:8px;">70%</div>
        <div class="display" style="font-size:24px;color:#fff;
                    margin-bottom:14px;line-height:1.05;">
          DOS LEADS NÃO<br>RECEBEM UM<br>SEGUNDO CONTATO.
        </div>
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:13px;
                    color:rgba(255,255,255,0.55);line-height:1.55;">
          Atendimento lento e follow-up inexistente<br>
          destroem faturamento silenciosamente.
        </div>
        {hr_line(40, 12)}
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:11.5px;
                    color:{cyan};font-weight:600;margin-top:8px;">
          A NUC Vision estrutura seu fluxo de atendimento.
        </div>
      </div>
      {bottom_strip()}
      {overlay_vignette(0.3, z=3)}
    </div>'''


# ── POST 8 — Diagnóstico estratégico ──────────────────────────────────────────

def _diag_row(icon, text):
    return (
        f'<div style="display:flex;align-items:center;gap:10px;'
        f'padding:8px 12px;margin-bottom:6px;'
        f'background:rgba(30,197,242,0.06);border-radius:8px;'
        f'border:1px solid rgba(30,197,242,0.14);">'
        f'<span style="font-size:14px;flex-shrink:0;">{icon}</span>'
        f'<span style="font-family:{FONTS["body"]},sans-serif;font-size:12px;'
        f'color:rgba(255,255,255,0.8);font-weight:500;">{text}</span>'
        f'</div>'
    )

def post8():
    items  = _diag_row("🏗", "Estrutura comercial e processos")
    items += _diag_row("💬", "Atendimento e velocidade de resposta")
    items += _diag_row("📊", "CRM e gestão de leads")
    items += _diag_row("🎯", "Posicionamento e clareza de oferta")
    items += _diag_row("📡", "Presença digital e tráfego")
    items += _diag_row("⚙️", "Gargalos operacionais invisíveis")

    p = pill_word("DIAGNÓSTICO.", 28)
    return f'''<div class="slide" style="background:{INK["void"]};">
      {dot_grid("rgba(30,197,242,0.07)", 26)}
      {noise_layer(0.3)}
      {logo_top()}
      <div style="position:absolute;top:55px;left:0;right:0;bottom:42px;
                  display:flex;flex-direction:column;justify-content:center;
                  padding:0 22px;z-index:10;">
        {kicker("Método · Antes de Qualquer Solução")}
        <div class="display" style="font-size:32px;color:#fff;margin-bottom:4px;">
          ANTES DE QUALQUER SOLUÇÃO:
        </div>
        <div class="display" style="font-size:28px;margin-bottom:16px;">{p}</div>
        {items}
      </div>
      {bottom_strip()}
      {overlay_vignette(0.3, z=3)}
    </div>'''


# ── POST 9 — Crescimento sustentável ──────────────────────────────────────────

def post9():
    cyan = ACCENT["primary"]
    void = INK["void"]
    svg = (
        f'<svg width="420" height="420" viewBox="0 0 420 420" xmlns="http://www.w3.org/2000/svg">'
        f'<polyline points="20,350 80,290 130,310 175,220 220,270 265,155 300,230 340,110 390,85"'
        f' fill="none" stroke="rgba(255,80,80,0.7)" stroke-width="2" stroke-dasharray="7,4"/>'
        f'<polyline points="20,370 90,330 160,295 230,255 300,210 370,158"'
        f' fill="none" stroke="{cyan}" stroke-width="2.5"/>'
        f'<circle cx="230" cy="255" r="4" fill="{cyan}"/>'
        f'<circle cx="300" cy="210" r="4" fill="{cyan}"/>'
        f'<circle cx="370" cy="158" r="4" fill="{cyan}"/>'
        f'</svg>'
    )
    legend_red = (
        f'<div style="display:flex;align-items:center;gap:7px;">'
        f'<div style="width:18px;height:2px;background:rgba(255,80,80,0.7);'
        f'border-radius:1px;border-top:1px dashed rgba(255,80,80,0.7);"></div>'
        f'<span style="font-family:{FONTS["body"]},sans-serif;font-size:11px;'
        f'color:rgba(255,255,255,0.42);">Sem estrutura</span></div>'
    )
    legend_cyan = (
        f'<div style="display:flex;align-items:center;gap:7px;">'
        f'<div style="width:18px;height:2px;background:{cyan};border-radius:1px;"></div>'
        f'<span style="font-family:{FONTS["body"]},sans-serif;font-size:11px;'
        f'color:rgba(255,255,255,0.75);">Com estrutura</span></div>'
    )
    p = pill_word("CAOS.", 38)
    return f'''<div class="slide" style="background:{void};">
      {noise_layer(0.32)}
      <div style="position:absolute;inset:0;z-index:1;opacity:0.18;pointer-events:none;">{svg}</div>
      {logo_top()}
      <div style="position:absolute;top:55px;left:0;right:0;bottom:42px;
                  display:flex;flex-direction:column;justify-content:center;
                  padding:0 26px;z-index:10;">
        {kicker("Crescimento Sustentável")}
        <div class="display" style="font-size:42px;color:#fff;margin-bottom:8px;">
          CRESCER RÁPIDO<br>SEM ESTRUTURA
        </div>
        <div class="display" style="font-size:40px;margin-bottom:18px;">É {p}</div>
        <div style="display:flex;gap:16px;margin-bottom:14px;">
          {legend_red}{legend_cyan}
        </div>
        <div style="font-family:{FONTS["body"]},sans-serif;font-size:13px;
                    color:rgba(255,255,255,0.53);line-height:1.55;">
          A NUC Vision trabalha para que o crescimento<br>
          seja previsível, organizado e sustentável.
        </div>
      </div>
      {bottom_strip()}
      {overlay_vignette(0.4, z=3)}
    </div>'''


# ── POST 10 — Diferencial NUC Vision (CTA) ────────────────────────────────────

def _service_row(icon, label):
    return (
        f'<div style="display:flex;align-items:center;gap:8px;margin-bottom:8px;">'
        f'<div style="width:24px;height:24px;border-radius:6px;flex-shrink:0;'
        f'background:rgba(30,197,242,0.15);border:1px solid rgba(30,197,242,0.25);'
        f'display:flex;align-items:center;justify-content:center;font-size:11px;">{icon}</div>'
        f'<span style="font-family:{FONTS["body"]},sans-serif;font-size:11.5px;'
        f'color:rgba(255,255,255,0.82);font-weight:500;">{label}</span>'
        f'</div>'
    )

def post10():
    services  = _service_row("🔍", "Diagnóstico de gargalos invisíveis")
    services += _service_row("🏗", "Estruturação do processo comercial")
    services += _service_row("📊", "CRM e gestão de leads")
    services += _service_row("🎯", "Posicionamento estratégico")
    services += _service_row("📡", "Tráfego pago com base em dados")
    services += _service_row("📈", "Performance e conversão")

    cyan = ACCENT["primary"]
    cta = (
        f'<div style="display:inline-block;background:{cyan};color:#fff;'
        f'font-family:{FONTS["body"]},sans-serif;font-size:12px;font-weight:700;'
        f'letter-spacing:0.1em;text-transform:uppercase;padding:10px 22px;'
        f'border-radius:999px;box-shadow:0 6px 24px rgba(30,197,242,0.4);">'
        f'Fale com a NUC Vision →</div>'
    )
    return f'''<div class="slide" style="background:linear-gradient(155deg,{INK["rich"]} 0%,#0A1628 55%,{INK["void"]} 100%);">
      {dot_grid("rgba(30,197,242,0.08)", 30)}
      {noise_layer(0.3)}
      {glow_radial(-50, 260, "rgba(30,197,242,0.16)")}
      {logo_top(size=26)}
      <div style="position:absolute;top:58px;left:0;right:0;bottom:42px;
                  display:flex;flex-direction:column;justify-content:center;
                  padding:0 22px;z-index:10;">
        <div class="display" style="font-size:28px;color:#fff;margin-bottom:2px;">
          ESTRUTURA COMERCIAL,
        </div>
        <div class="display" style="font-size:28px;color:{cyan};margin-bottom:16px;">
          MARKETING E PERFORMANCE.
        </div>
        {services}
        <div style="margin-top:14px;">{cta}</div>
      </div>
      {bottom_strip()}
      {overlay_vignette(0.3, z=3)}
    </div>'''


# ── CSS ───────────────────────────────────────────────────────────────────────

CSS = f"""
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{ font-family:{FONTS["body"]},sans-serif; background:#0a0a0a;
         min-height:100vh; display:flex; align-items:center;
         justify-content:center; padding:20px; }}
  .display {{ font-family:{FONTS["display"]},sans-serif;
              letter-spacing:{TRACK["tight"]}; line-height:{LINE["display"]};
              text-transform:uppercase; font-weight:400; }}
  .post-frame {{ width:{VW}px; background:#111; border-radius:18px;
                 overflow:hidden; box-shadow:0 24px 80px rgba(0,0,0,0.65); }}
  .carousel-viewport {{ width:{VW}px; height:{VH}px; overflow:hidden;
                         position:relative; cursor:grab; }}
  .carousel-track {{ display:flex; height:100%; transition:transform 0.3s ease; }}
  .slide {{ flex-shrink:0; width:{VW}px; height:{VH}px;
            position:relative; overflow:hidden; }}
  .post-nav {{ position:fixed; bottom:24px; left:50%; transform:translateX(-50%);
               display:flex; align-items:center; gap:12px;
               background:rgba(0,0,0,0.7); padding:8px 18px;
               border-radius:999px; backdrop-filter:blur(10px); }}
  .post-nav button {{ background:rgba(30,197,242,0.25); color:#fff; border:none;
                      padding:6px 16px; border-radius:999px; cursor:pointer;
                      font-family:{FONTS["body"]},sans-serif; font-size:12px; font-weight:600; }}
  .post-nav button:hover {{ background:rgba(30,197,242,0.5); }}
  .post-nav .idx {{ color:rgba(255,255,255,0.7);
                    font-family:{FONTS["body"]},sans-serif; font-size:12px; }}
"""

SWIPE_JS = f"""
  const track = document.querySelector('.carousel-track');
  const idx   = document.querySelector('.idx');
  let cur = 0; const total = {TOTAL};
  function go(n) {{
    cur = Math.max(0, Math.min(total - 1, cur + n));
    track.style.transform = 'translateX(' + (-cur * {VW}) + 'px)';
    idx.textContent = (cur + 1) + ' / ' + total;
  }}
  document.querySelector('.carousel-viewport').addEventListener('click', (e) => {{
    const x = e.clientX - e.currentTarget.getBoundingClientRect().left;
    go(x > {VW * 0.6} ? 1 : x < {VW * 0.4} ? -1 : 0);
  }});
  document.addEventListener('keydown', (e) => {{
    if (e.key === 'ArrowRight') go(1);
    if (e.key === 'ArrowLeft')  go(-1);
  }});
"""


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    posts = [
        post1(), post2(), post3(), post4(), post5(),
        post6(), post7(), post8(), post9(), post10(),
    ]
    slides_html = "\n".join(posts)

    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<title>NUC Vision — Google Meu Negócio Posts</title>
{FONT_LINK}
<style>{CSS}</style>
</head>
<body>
<div class="post-frame">
  <div class="carousel-viewport">
    <div class="carousel-track">
{slides_html}
    </div>
  </div>
</div>
<div class="post-nav">
  <button onclick="go(-1)">← Anterior</button>
  <span class="idx">1 / {TOTAL}</span>
  <button onclick="go(1)">Próximo →</button>
</div>
<script>{SWIPE_JS}</script>
</body>
</html>"""

    out = Path("/home/user/Meu-espa-o/nucvision-googleposts.html")
    out.write_text(html, encoding="utf-8")
    print(f"✓ Preview: {out}")


if __name__ == "__main__":
    main()
