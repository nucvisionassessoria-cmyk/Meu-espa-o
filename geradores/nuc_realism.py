# nuc_realism.py
# ---------------------------------------------------------------------------
# Drop-in para o pipeline NUC (Python -> HTML inline -> Playwright/Chromium).
# Resolve as 5 tells de "cara de IA" via CSS puro renderizado pelo Chromium:
#   1) sombra de contato (nada flutua)
#   2) coerência de luz sujeito<->fundo (color match + light wrap)
#   3) profundidade real em 3 camadas (blur + vinheta, NUNCA opacity)
#   4) grão/textura em toda a peca (proibido fundo liso)
#   5) bordas tratadas (drop-shadow de borda + feather do recorte)
#
# COMO USAR (3 passos):
#   1. from nuc_realism import REALISM_CSS, recorte, fundo_profundo, card, GRAO_OVERLAY
#   2. injete REALISM_CSS dentro do <style> do seu html_shell()  (uma vez)
#   3. troque a <img> crua do carro por recorte(...) e o fundo por fundo_profundo(...)
#      e adicione GRAO_OVERLAY como ULTIMO filho de cada .slide
# ---------------------------------------------------------------------------

# Cor de accent da marca (ciano NUC Vision). Alinhada ao design_system.
ACCENT = "#1EC5F2"

# Bloco de CSS reutilizavel. Injete uma unica vez no <style> global.
REALISM_CSS = f"""
/* ---------- CAMADA 1: FUNDO COM PROFUNDIDADE REAL ---------- */
.depth-bg {{
  position: absolute; inset: 0; z-index: 0;
  background-size: cover; background-position: center;
  filter: blur(14px) brightness(0.55) saturate(1.05);   /* profundidade por BLUR, nao opacity */
  transform: scale(1.08);                                /* esconde borda do blur */
}}
.depth-bg::after {{                                       /* vinheta: foca o centro */
  content: ""; position: absolute; inset: 0;
  background: radial-gradient(120% 90% at 50% 42%,
              transparent 38%, rgba(0,0,0,.55) 100%);
}}

/* ---------- CAMADA 2: RECORTE (sujeito) ANCORADO E INTEGRADO ---------- */
.subject {{
  position: relative; display: inline-block; z-index: 2;
}}
.subject > img {{
  display: block; position: relative; z-index: 2;
  /* color match: alinha o recorte ao fundo escuro da cena */
  filter:
    brightness(0.96) contrast(1.06) saturate(1.04)
    drop-shadow(0 0 1px rgba(0,0,0,.35))                 /* feather/borda dura */
    drop-shadow(0 0 14px {ACCENT}40);                    /* light wrap ciano sutil */
}}
.subject::after {{                                        /* SOMBRA DE CONTATO (o objeto toca o chao) */
  content: ""; position: absolute; z-index: 1;
  left: 8%; right: 8%; bottom: -4%;
  height: 9%;
  background: radial-gradient(closest-side,
              rgba(0,0,0,.62), rgba(0,0,0,0) 78%);
  filter: blur(10px);
  /* deslocada na direcao da luz (luz vem do alto-frente -> sombra um pouco pra baixo) */
}}

/* ---------- CAMADA 3: GRAFISMO COM SOMBRA PROJETADA ---------- */
.card {{
  position: relative; z-index: 3;
  background: rgba(14,20,30,.72);
  border: 1px solid rgba(255,255,255,.08);
  border-radius: 18px;
  backdrop-filter: blur(8px);
  box-shadow:
    0 24px 60px rgba(0,0,0,.55),                          /* sombra projetada -> descola do plano */
    inset 0 1px 0 rgba(255,255,255,.06);                  /* highlight de borda superior */
}}
.cta {{
  position: relative; z-index: 3;
  background: {ACCENT};
  border-radius: 999px;
  box-shadow: 0 10px 30px {ACCENT}66, 0 0 0 1px rgba(255,255,255,.12) inset;
}}

/* ---------- GRAO GLOBAL (proibido fundo liso) ---------- */
.grain {{
  position: absolute; inset: 0; z-index: 50; pointer-events: none;
  opacity: .07; mix-blend-mode: overlay;
  background-image: url("data:image/svg+xml;utf8,\
<svg xmlns='http://www.w3.org/2000/svg' width='120' height='120'>\
<filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2'/>\
</filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>");
  background-size: 180px 180px;
}}
"""

# Overlay de grao: adicione como ULTIMO filho de cada .slide
GRAO_OVERLAY = '<div class="grain"></div>'


def fundo_profundo(data_uri: str, *, extra_style: str = "") -> str:
    """Fundo com profundidade real (blur + vinheta). Use uma foto de ambiente
    OU o proprio recorte borrado como atmosfera. NUNCA um gradient chapado."""
    return (f'<div class="depth-bg" style="background-image:url(\'{data_uri}\');'
            f'{extra_style}"></div>')


def recorte(data_uri: str, *, largura="62%", left="6%", bottom="0%",
            extra_style="", img_style="") -> str:
    """Recorte do carro/pessoa JA ancorado (sombra de contato) e integrado
    (color match + light wrap). Substitui a <img> crua do seu slide.

    largura/left/bottom controlam o posicionamento dentro do slide."""
    return (
        f'<div class="subject" style="position:absolute;'
        f'width:{largura};left:{left};bottom:{bottom};{extra_style}">'
        f'<img src="{data_uri}" style="width:100%;{img_style}"></div>'
    )


def sombra_contato(*, left="8%", right="8%", bottom="-4%", height="9%",
                   alpha=0.62, blur=10) -> str:
    """Sombra de contato isolada — para colar embaixo de um sujeito que ja
    tem layout proprio (sem trocar o posicionamento existente)."""
    return (
        f'<div style="position:absolute;left:{left};right:{right};'
        f'bottom:{bottom};height:{height};z-index:-1;'
        f'background:radial-gradient(closest-side,rgba(0,0,0,{alpha}),'
        f'rgba(0,0,0,0) 78%);filter:blur({blur}px);pointer-events:none;"></div>'
    )


def card(conteudo_html: str, *, style="") -> str:
    """Card/box com sombra projetada (3a camada Z)."""
    return f'<div class="card" style="padding:22px 26px;{style}">{conteudo_html}</div>'
