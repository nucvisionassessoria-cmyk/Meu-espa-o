#!/usr/bin/env python3
"""
NUC Vision — Brand Configuration
Use this file in any carousel generator to load brand assets automatically.
"""
from pathlib import Path
import base64, io

# ── Identity ──────────────────────────────────────────────────────────────────
BRAND_NAME    = "NUC VISION"
HANDLE        = "@nucvision"
SUBTITLE      = "Estrutura · Crescimento · Resultado"

# ── Color System ──────────────────────────────────────────────────────────────
BRAND_PRIMARY = "#1EC5F2"   # Ciano vibrante — barra de progresso, ícones, tags
BRAND_LIGHT   = "#5DD6F5"   # Ciano claro — tags em fundo escuro
BRAND_MEDIUM  = "#2591E6"   # Azul médio — gradiente
BRAND_DARK    = "#1D4D8F"   # Azul profundo — CTA text, âncora do gradiente
BRAND_NAVY    = "#1A2E4D"   # Azul escuro institucional — texto principal

LIGHT_BG      = "#EEF3F8"   # Fundo claro (slides ímpares)
LIGHT_BORDER  = "#D4DFE9"   # Divisor em fundo claro
DARK_BG       = "#111827"   # Fundo escuro (slides pares)

GRADIENT      = f"linear-gradient(165deg, {BRAND_DARK} 0%, {BRAND_MEDIUM} 55%, {BRAND_LIGHT} 100%)"

# ── Typography ────────────────────────────────────────────────────────────────
FONT_URL      = "https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&display=swap"
FONT_NAME     = "Space Grotesk"

# ── Logo ──────────────────────────────────────────────────────────────────────
_LOGO_FILE    = Path(__file__).parent / "IMG_3622.PNG"

def get_logo_b64() -> str:
    """Returns base64-encoded logo PNG (transparent background)."""
    return base64.b64encode(_LOGO_FILE.read_bytes()).decode()

def get_logo_uri() -> str:
    """Returns data URI ready to use in <img src='...'>."""
    return f"data:image/png;base64,{get_logo_b64()}"

def logo_img(height_px: int = 28, shadow: bool = False) -> str:
    """Returns <img> tag with correct sizing and optional drop-shadow."""
    shadow_css = "filter:drop-shadow(0 3px 12px rgba(0,0,0,0.28)) drop-shadow(0 1px 3px rgba(0,0,0,0.18));" if shadow else ""
    return (f'<img src="{get_logo_uri()}" '
            f'style="height:{height_px}px;width:auto;max-width:{height_px*7}px;'
            f'object-fit:contain;{shadow_css}">')

def logo_lockup(dark: bool = False, large: bool = False) -> str:
    """
    Returns logo HTML ready for slide insertion.
    - dark=False → light slide (logo inline, dark text visible)
    - dark=True  → dark/gradient slide (floating logo with shadow)
    - large=True → CTA slide size
    """
    h = 44 if large else 24
    return logo_img(height_px=h, shadow=dark)


# ── Quick test ────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print(f"Brand:    {BRAND_NAME}")
    print(f"Handle:   {HANDLE}")
    print(f"Primary:  {BRAND_PRIMARY}")
    print(f"Font:     {FONT_NAME}")
    uri = get_logo_uri()
    print(f"Logo URI: {uri[:60]}... ({len(uri)} chars)")
    print("✓ Brand config OK")
