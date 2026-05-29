#!/usr/bin/env python3
"""
Recorta o fundo branco da foto do Hamilton (estúdio) preservando os
logos brancos internos do macacão. Usa flood-fill a partir das bordas:
só o branco CONECTADO à borda externa vira transparente.
Gera fotos/hamilton_cutout.png (RGBA com alpha esfumado).
"""
from pathlib import Path
import numpy as np
from scipy import ndimage
from PIL import Image, ImageFilter

SRC = Path("/home/user/Meu-espa-o/fotos/Gemini_Generated_Image_bk8amybk8amybk8a.png")
OUT = Path("/home/user/Meu-espa-o/fotos/hamilton_cutout.png")

im = Image.open(SRC).convert("RGB")
arr = np.asarray(im).astype(np.int16)

# máscara de "quase branco": canais altos e baixa saturação
mx = arr.max(axis=2)
mn = arr.min(axis=2)
whiteish = (mn > 218) & ((mx - mn) < 24)

# componentes conectados do branco
lbl, n = ndimage.label(whiteish)

# rótulos que tocam qualquer borda = fundo
border = set(lbl[0, :]) | set(lbl[-1, :]) | set(lbl[:, 0]) | set(lbl[:, -1])
border.discard(0)
bg = np.isin(lbl, list(border))

# alpha: 0 no fundo, 255 no sujeito
alpha = np.where(bg, 0, 255).astype(np.uint8)

# esfuma a borda do recorte para não ficar serrilhado
alpha_img = Image.fromarray(alpha).filter(ImageFilter.GaussianBlur(1.4))

rgba = im.convert("RGBA")
rgba.putalpha(alpha_img)

# corta para a bounding box do sujeito (remove margens transparentes)
bbox = rgba.getbbox()
if bbox:
    rgba = rgba.crop(bbox)

rgba.save(OUT)
print(f"✓ {OUT}  {rgba.size}")
