"""
NUC Vision Design System v2 — Premium agency-grade tokens and primitives.
Use this as the SINGLE source of truth for any carousel generation.
Imports from brand.py for canonical colors/fonts.
"""
import sys, base64
from pathlib import Path

sys.path.insert(0, "/home/user/Meu-espa-o")
from brand import (
    BRAND_PRIMARY, BRAND_LIGHT, BRAND_MEDIUM, BRAND_DARK, BRAND_NAVY,
    LIGHT_BG, LIGHT_BORDER, FONT_NAME, get_logo_uri, HANDLE, SUBTITLE,
)

LOGO_URI = get_logo_uri()
FOTOS_DIR = Path("/home/user/Meu-espa-o/fotos")

# ============================================================
# COLOR SYSTEM — extended palette built around NUC brand
# ============================================================
INK = {
    "void":   "#05080F",
    "deep":   "#0A0F1A",
    "rich":   "#0F1729",
    "medium": "#1A2440",
    "fade":   "#2A3650",
}
PAPER = {
    "warm":   "#F5F7FA",
    "soft":   "#EDF1F7",
    "cool":   "#E8EEF5",
    "border": "#D8E0EC",
    "dim":    "#B5C0D0",
}
ACCENT = {
    "ice":      "#E0F4FB",
    "mist":     "#A5DFF0",
    "primary":  BRAND_PRIMARY,
    "vivid":    "#0AB6E8",
    "electric": "#00D4FF",
    "deep":     BRAND_DARK,
    "navy":     BRAND_NAVY,
    "medium":   BRAND_MEDIUM,
    "light":    BRAND_LIGHT,
}
GRAY = {
    "100": "#F8F9FB", "200": "#EEF1F5", "300": "#D8DEE7", "400": "#A8B2C2",
    "500": "#7A8597", "600": "#525C6E", "700": "#363D4D", "800": "#1F2433", "900": "#10131C",
}

# ============================================================
# TYPOGRAPHY
# ============================================================
FONTS = {
    "display": "'Anton'",
    "body":    "'Space Grotesk'",
    "mono":    "'JetBrains Mono'",
}
FONT_LINK = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
             '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
             '<link href="https://fonts.googleapis.com/css2?family=Anton&'
             'family=Space+Grotesk:wght@300;400;500;600;700&'
             'family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">')

TYPE = {
    "manifesto":   104, "display_xl": 88, "display_lg": 64, "display_md": 46,
    "headline":    30,  "headline_sm": 22, "title": 18, "subtitle": 15,
    "body":        13.5, "small": 12, "caption": 11, "kicker": 10, "micro": 9,
}
TRACK = {
    "tightest": "-0.04em", "tight": "-0.02em", "normal": "0",
    "wide": "0.04em", "kicker": "0.18em", "label": "0.22em",
}
LINE = {"display": 0.88, "headline": 1.05, "body": 1.5, "tight": 1.2}

# ============================================================
# DESIGN TOKENS
# ============================================================
RADIUS = {"xs": 6, "sm": 10, "md": 14, "lg": 18, "xl": 24, "pill": 999}
SHADOW = {
    "subtle": "0 1px 3px rgba(0,0,0,0.08), 0 1px 2px rgba(0,0,0,0.04)",
    "card":   "0 4px 14px rgba(10,15,26,0.10), 0 2px 5px rgba(10,15,26,0.05)",
    "lift":   "0 14px 36px rgba(10,15,26,0.22), 0 5px 10px rgba(10,15,26,0.10)",
    "drama":  "0 28px 72px rgba(10,15,26,0.50), 0 10px 20px rgba(10,15,26,0.28)",
    "glow":   "0 0 32px rgba(30,197,242,0.42), 0 6px 18px rgba(30,197,242,0.22)",
    "inset_top":    "inset 0 1px 0 rgba(255,255,255,0.14)",
    "inset_bottom": "inset 0 -1px 0 rgba(0,0,0,0.22)",
}

# ============================================================
# NOISE / GRAIN texture for atmospheric backgrounds
# ============================================================
def _noise_b64():
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" width="240" height="240">'
           '<filter id="n"><feTurbulence type="fractalNoise" baseFrequency="0.92" '
           'numOctaves="2" stitchTiles="stitch" seed="7"/>'
           '<feColorMatrix values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 0.55 0"/>'
           '</filter><rect width="100%" height="100%" filter="url(#n)"/></svg>')
    return base64.b64encode(svg.encode()).decode()

NOISE_B64 = _noise_b64()

def overlay_noise(opacity=0.5, blend="overlay", z=2):
    return (f'<div style="position:absolute;inset:0;'
            f'background-image:url(\'data:image/svg+xml;base64,{NOISE_B64}\');'
            f'background-size:240px 240px;opacity:{opacity};'
            f'mix-blend-mode:{blend};pointer-events:none;z-index:{z};"></div>')

def overlay_vignette(strength=0.5, z=3):
    return (f'<div style="position:absolute;inset:0;'
            f'background:radial-gradient(ellipse 110% 80% at center, '
            f'transparent 30%, rgba(0,0,0,{strength}) 100%);'
            f'pointer-events:none;z-index:{z};"></div>')

# ============================================================
# BACKGROUND GENERATORS — multi-layer atmospheric
# ============================================================
def bg_brand_atmo():
    """Premium brand gradient: light source + depth + noise."""
    return (f'background:'
            f'radial-gradient(ellipse 80% 60% at 22% -5%, rgba(255,255,255,0.22) 0%, transparent 55%),'
            f'radial-gradient(ellipse 90% 70% at 85% 105%, rgba(10,15,26,0.55) 0%, transparent 60%),'
            f'linear-gradient(155deg, {ACCENT["deep"]} 0%, {BRAND_MEDIUM} 38%, {BRAND_LIGHT} 78%, {ACCENT["mist"]} 100%);')

def bg_dark_atmo():
    """Premium dark: cyan glow corner + navy depth + noise."""
    return (f'background:'
            f'radial-gradient(ellipse 65% 55% at 92% 8%, rgba(30,197,242,0.22) 0%, transparent 60%),'
            f'radial-gradient(ellipse 75% 65% at -5% 100%, rgba(29,77,143,0.35) 0%, transparent 65%),'
            f'linear-gradient(165deg, {INK["void"]} 0%, {INK["medium"]} 50%, {INK["rich"]} 100%);')

def bg_paper_atmo():
    """Sophisticated light: warm tint + subtle cyan glow."""
    return (f'background:'
            f'radial-gradient(ellipse 90% 80% at 100% 0%, rgba(30,197,242,0.08) 0%, transparent 50%),'
            f'radial-gradient(ellipse 80% 70% at 0% 100%, rgba(29,77,143,0.04) 0%, transparent 60%),'
            f'linear-gradient(170deg, {PAPER["warm"]} 0%, {PAPER["soft"]} 100%);')

def bg_split(top_color, bottom_color, split_pct=50):
    """Hard split background — for editorial layouts."""
    return f'background:linear-gradient(180deg, {top_color} 0%, {top_color} {split_pct}%, {bottom_color} {split_pct}%, {bottom_color} 100%);'

# ============================================================
# COMPONENTS — refined primitives
# ============================================================
def kicker(text, color=None, light=False, with_line=True):
    c = color or (ACCENT["primary"] if light else ACCENT["mist"])
    line = (f'<span style="display:inline-block;width:22px;height:1px;'
            f'background:{c};opacity:0.55;margin-right:2px;"></span>') if with_line else ''
    return (f'<div style="display:inline-flex;align-items:center;gap:8px;'
            f'font-family:{FONTS["body"]};font-size:{TYPE["kicker"]}px;font-weight:600;'
            f'color:{c};letter-spacing:{TRACK["label"]};text-transform:uppercase;">'
            f'{line}{text}</div>')

def display_pill(word, accent="white", text_color=None, size=None, glow=False):
    s = size or TYPE["display_md"]
    if accent == "white":
        bg, c = "#fff", text_color or ACCENT["deep"]
    elif accent == "primary":
        bg, c = ACCENT["primary"], "#fff"
    elif accent == "deep":
        bg, c = ACCENT["deep"], "#fff"
    else:
        bg, c = accent, text_color or "#fff"
    sh = SHADOW["glow"] if glow else SHADOW["lift"]
    return (f'<span style="display:inline-block;background:{bg};color:{c};'
            f'padding:8px 24px 14px;border-radius:{RADIUS["lg"]}px;'
            f'font-family:{FONTS["display"]};font-size:{s}px;line-height:0.86;'
            f'letter-spacing:{TRACK["tight"]};text-transform:uppercase;'
            f'box-shadow:{sh};">{word}</span>')

def stat_block(number, label, accent_color=None, dark=True):
    c = accent_color or ACCENT["primary"]
    label_c = "rgba(255,255,255,0.7)" if dark else GRAY["500"]
    return (f'<div style="display:flex;flex-direction:column;align-items:flex-start;">'
            f'<div style="font-family:{FONTS["display"]};font-size:{TYPE["display_xl"]}px;'
            f'color:{c};line-height:0.86;letter-spacing:{TRACK["tight"]};">{number}</div>'
            f'<div style="font-family:{FONTS["body"]};font-size:{TYPE["small"]}px;'
            f'color:{label_c};font-weight:500;text-transform:uppercase;'
            f'letter-spacing:{TRACK["wide"]};margin-top:8px;">{label}</div></div>')

def glass_card(content_html, padding="20px 22px", dark=False, radius=None):
    r = radius if radius is not None else RADIUS["md"]
    if dark:
        bg = "rgba(10,15,26,0.62)"
        border = "rgba(255,255,255,0.10)"
    else:
        bg = "rgba(255,255,255,0.88)"
        border = "rgba(255,255,255,0.5)"
    return (f'<div style="background:{bg};border:1px solid {border};'
            f'border-radius:{r}px;backdrop-filter:blur(24px) saturate(160%);'
            f'-webkit-backdrop-filter:blur(24px) saturate(160%);padding:{padding};'
            f'box-shadow:{SHADOW["lift"]}, {SHADOW["inset_top"]};">{content_html}</div>')

def number_marker(num, big=False, color=None):
    s = TYPE["display_lg"] if big else TYPE["display_md"]
    c = color or ACCENT["primary"]
    return (f'<span style="font-family:{FONTS["display"]};font-size:{s}px;'
            f'line-height:0.86;letter-spacing:{TRACK["tight"]};color:{c};">{num}</span>')

def feature_row(num, label, desc, dark=False):
    """Refined editorial row with numbered marker + gradient backdrop."""
    if dark:
        bg = "linear-gradient(135deg, rgba(255,255,255,0.05) 0%, rgba(255,255,255,0.02) 100%)"
        border = "rgba(255,255,255,0.08)"
        label_c = "#fff"
        desc_c = "rgba(255,255,255,0.6)"
    else:
        bg = "linear-gradient(135deg, #fff 0%, rgba(245,247,250,0.5) 100%)"
        border = PAPER["border"]
        label_c = INK["deep"]
        desc_c = GRAY["500"]
    return (f'<div style="display:flex;align-items:center;gap:16px;padding:14px 16px;'
            f'background:{bg};border:1px solid {border};border-radius:{RADIUS["md"]}px;'
            f'box-shadow:{SHADOW["subtle"]};">'
            f'<div style="font-family:{FONTS["display"]};font-size:30px;line-height:0.86;'
            f'color:{ACCENT["primary"]};letter-spacing:{TRACK["tight"]};min-width:34px;">{num}</div>'
            f'<div style="flex:1;">'
            f'<div style="font-family:{FONTS["body"]};font-weight:700;font-size:{TYPE["small"]}px;'
            f'color:{label_c};text-transform:uppercase;letter-spacing:{TRACK["wide"]};'
            f'line-height:1.15;">{label}</div>'
            f'<div style="font-family:{FONTS["body"]};font-size:{TYPE["caption"]}px;'
            f'color:{desc_c};line-height:1.45;margin-top:3px;">{desc}</div>'
            f'</div></div>')

def slide_index(idx, total, light=False):
    """Refined slide counter pill."""
    if light:
        bg = "rgba(10,15,26,0.06)"
        c  = INK["deep"]
        bd = "rgba(10,15,26,0.10)"
    else:
        bg = "rgba(10,15,26,0.50)"
        c  = "rgba(255,255,255,0.95)"
        bd = "rgba(255,255,255,0.14)"
    return (f'<div style="position:absolute;top:22px;right:24px;background:{bg};color:{c};'
            f'font-family:{FONTS["body"]};font-size:{TYPE["caption"]}px;font-weight:500;'
            f'padding:5px 13px;border-radius:{RADIUS["pill"]}px;border:1px solid {bd};'
            f'backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);'
            f'z-index:30;letter-spacing:0.02em;">'
            f'<span style="font-weight:700;">{idx}</span>'
            f'<span style="opacity:0.45;margin:0 4px;">/</span>'
            f'<span style="opacity:0.7;">{total}</span></div>')

def progress_bar(idx, total, light=False):
    pct = (idx / total) * 100
    if light:
        track = "rgba(10,15,26,0.08)"
        fill = f"linear-gradient(90deg,{ACCENT['primary']} 0%,{ACCENT['vivid']} 100%)"
    else:
        track = "rgba(255,255,255,0.14)"
        fill = "linear-gradient(90deg,#fff 0%,rgba(255,255,255,0.7) 100%)"
    return (f'<div style="position:absolute;bottom:0;left:0;right:0;'
            f'padding:18px 28px 22px;z-index:25;display:flex;align-items:center;gap:10px;">'
            f'<div style="flex:1;height:2px;background:{track};border-radius:2px;overflow:hidden;">'
            f'<div style="height:100%;width:{pct}%;background:{fill};border-radius:2px;"></div>'
            f'</div></div>')

def logo_mark(dark_bg=True, size=28, position="top-center"):
    if dark_bg:
        treatment = "filter:brightness(0) invert(1) drop-shadow(0 4px 14px rgba(0,0,0,0.7));"
    else:
        treatment = "filter:drop-shadow(0 2px 8px rgba(10,15,26,0.14));"
    if position == "top-left":
        wrap = "position:absolute;top:24px;left:26px;z-index:20;"
    elif position == "top-right":
        wrap = "position:absolute;top:24px;right:26px;z-index:20;"
    else:
        wrap = "position:absolute;top:22px;left:0;right:0;display:flex;justify-content:center;z-index:20;"
    return (f'<div style="{wrap}"><img src="{LOGO_URI}" '
            f'style="height:{size}px;width:auto;max-width:200px;object-fit:contain;{treatment}"></div>')

# ============================================================
# PHOTO SYSTEM — focal-point-aware crops + cinematic treatments
# ============================================================
PHOTO_META = {
    "trio_reuniao.png":   {"focal": (50, 40), "type": "trio_portrait",      "best": ["hero", "cta", "authority"]},
    "equipe_cultura.jpg": {"focal": (50, 42), "type": "team_collaboration",  "best": ["culture", "team", "flagship"]},
    "lucas_derick.jpeg":  {"focal": (50, 30), "type": "duo_action",         "best": ["hero", "cta", "context"]},
    "lucas_3.jpeg":       {"focal": (50, 38), "type": "solo_full_body",     "best": ["protagonist", "authority"]},
    "lucas_2.jpeg":       {"focal": (50, 18), "type": "solo_full_body",     "best": ["protagonist"]},
    "lucas_1.jpeg":       {"focal": (50, 35), "type": "solo_bust",          "best": ["hero", "portrait"]},
    "iago_office_1.png":  {"focal": (45, 30), "type": "solo_bust",          "best": ["portrait", "hero"]},
    "iago_office_2.png":  {"focal": (50, 22), "type": "solo_full_body",     "best": ["protagonist", "authority"]},
    "iago_office_3.png":  {"focal": (50, 25), "type": "solo_full_body",     "best": ["protagonist"]},
    "iago_2.png":         {"focal": (45, 32), "type": "action_environment", "best": ["context", "process"]},
    "iago_1.png":         {"focal": (50, 35), "type": "action_environment", "best": ["context"]},
    "derick_1.png":       {"focal": (50, 28), "type": "solo_bust",          "best": ["protagonist"]},
}

def photo_uri(name):
    p = FOTOS_DIR / name
    ext = p.suffix.lower().lstrip(".")
    mime = {"jpg": "jpeg", "jpeg": "jpeg", "png": "png", "webp": "webp"}.get(ext, "jpeg")
    b64 = base64.b64encode(p.read_bytes()).decode()
    return f"data:image/{mime};base64,{b64}"

def photo_position(name):
    meta = PHOTO_META.get(name, {"focal": (50, 30)})
    fx, fy = meta["focal"]
    return f"{fx}% {fy}%"

PHOTO_OVERLAYS = {
    "hero":       "linear-gradient(180deg, rgba(29,77,143,0.55) 0%, transparent 22%, transparent 55%, rgba(10,15,26,0.85) 100%)",
    "portrait":   "linear-gradient(180deg, rgba(10,15,26,0.50) 0%, transparent 30%, transparent 70%, rgba(10,15,26,0.78) 100%)",
    "cta":        "linear-gradient(180deg, rgba(29,77,143,0.45) 0%, rgba(29,77,143,0.18) 30%, rgba(10,15,26,0.55) 65%, rgba(10,15,26,0.92) 100%)",
    "card":       "linear-gradient(180deg, rgba(10,15,26,0.0) 55%, rgba(10,15,26,0.65) 100%)",
    "split_left": "linear-gradient(90deg, rgba(10,15,26,0.0) 50%, rgba(10,15,26,0.85) 100%)",
    "diptych":    "linear-gradient(180deg, rgba(10,15,26,0.15) 0%, rgba(10,15,26,0.55) 100%)",
}

def photo_layered(name, treatment="hero", grading=True):
    """Photo with cinematic grading + atmospheric overlay."""
    uri = photo_uri(name)
    pos = photo_position(name)
    grade = "filter:contrast(1.06) saturate(1.04) brightness(0.97);" if grading else ""
    overlay = PHOTO_OVERLAYS.get(treatment, PHOTO_OVERLAYS["portrait"])
    return (f'<img src="{uri}" style="width:100%;height:100%;object-fit:cover;'
            f'object-position:{pos};{grade}">'
            f'<div style="position:absolute;inset:0;background:{overlay};'
            f'pointer-events:none;"></div>')

# ============================================================
# IG FRAME WRAPPER (compatibility with export pipeline — DO NOT CHANGE dims)
# ============================================================
W, H = 420, 525

def ig_frame_open(handle=None, subtitle=None):
    handle = handle or HANDLE
    subtitle = subtitle or SUBTITLE
    return f'''<div class="ig-frame">
      <div class="ig-header">
        <div class="ig-avatar"><img src="{LOGO_URI}" style="height:18px;filter:brightness(0) invert(1);"></div>
        <div><div class="ig-handle">{handle}</div><div class="ig-sub">{subtitle}</div></div>
      </div>
      <div class="carousel-viewport"><div class="carousel-track">'''

def ig_frame_close(total, caption):
    dots = "".join(['<span class="active"></span>' if i==0 else '<span></span>' for i in range(total)])
    return f'''</div></div>
      <div class="ig-dots">{dots}</div>
      <div class="ig-actions">♡ 💬 ↗</div>
      <div class="ig-caption"><strong>{HANDLE}</strong> {caption}</div>
    </div>'''

CSS_BASE = f'''
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{ font-family:{FONTS["body"]},sans-serif; background:#0a0a0a;
         min-height:100vh; display:flex; align-items:center; justify-content:center; padding:20px; }}
  .display {{ font-family:{FONTS["display"]},sans-serif; letter-spacing:{TRACK["tight"]}; line-height:{LINE["display"]}; text-transform:uppercase; font-weight:400; }}
  .ig-frame {{ width:{W}px; max-width:{W}px; background:#fff; border-radius:18px; overflow:hidden; box-shadow:0 24px 80px rgba(0,0,0,0.6); }}
  .ig-header {{ display:flex; align-items:center; gap:10px; padding:12px 16px; border-bottom:1px solid #efefef; }}
  .ig-avatar {{ width:38px; height:38px; border-radius:50%; background:{BRAND_PRIMARY}; display:flex; align-items:center; justify-content:center; }}
  .ig-handle {{ font-weight:600; font-size:14px; color:#262626; }}
  .ig-sub {{ font-size:11px; color:#8e8e8e; }}
  .carousel-viewport {{ width:{W}px; height:{H}px; aspect-ratio:4/5; overflow:hidden; position:relative; cursor:grab; }}
  .carousel-track {{ display:flex; height:100%; transition:transform 0.3s ease; }}
  .slide {{ flex-shrink:0; width:{W}px; height:{H}px; position:relative; overflow:hidden; }}
  .ig-dots {{ display:flex; justify-content:center; gap:4px; padding:8px; }}
  .ig-dots span {{ width:6px; height:6px; border-radius:50%; background:#dbdbdb; }}
  .ig-dots span.active {{ background:{BRAND_PRIMARY}; }}
  .ig-actions {{ display:flex; gap:14px; padding:8px 16px; font-size:18px; }}
  .ig-caption {{ padding:8px 16px 16px; font-size:13px; color:#262626; line-height:1.4; }}
'''

def html_shell(slides_html, total, caption):
    swipe_js = '''
      const track = document.querySelector('.carousel-track');
      const dots = document.querySelectorAll('.ig-dots span');
      let cur = 0;
      document.querySelector('.carousel-viewport').addEventListener('click', (e) => {
        const r = e.currentTarget.getBoundingClientRect();
        const x = e.clientX - r.left;
        if (x > r.width * 0.6 && cur < TOTAL - 1) cur++;
        else if (x < r.width * 0.4 && cur > 0) cur--;
        track.style.transform = `translateX(${-cur * 420}px)`;
        dots.forEach((d,i) => d.classList.toggle('active', i === cur));
      });
    '''.replace("TOTAL", str(total))
    return f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<title>NUC Vision Editorial</title>
{FONT_LINK}
<style>{CSS_BASE}</style>
</head>
<body>
{ig_frame_open()}{slides_html}{ig_frame_close(total, caption)}
<script>{swipe_js}</script>
</body>
</html>'''
