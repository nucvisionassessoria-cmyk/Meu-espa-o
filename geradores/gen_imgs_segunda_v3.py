#!/usr/bin/env python3
"""Gera imagens humanizadas via Imagen 4 (Gemini) para o carrossel de Segunda v3."""
import os
from pathlib import Path
from google import genai

env = {}
for line in Path("/home/user/Meu-espa-o/.env").read_text().splitlines():
    if "=" in line and not line.strip().startswith("#"):
        k, v = line.split("=", 1)
        env[k.strip()] = v.strip().strip('"').strip("'")
client = genai.Client(api_key=env["GEMINI_API_KEY"])

OUT = Path("/home/user/Meu-espa-o/fotos/geradas")
OUT.mkdir(parents=True, exist_ok=True)

PROMPTS = {
    "v3_s1_mesa_demanda.png": (
        "Editorial photography, top-down 3/4 view of a real wooden desk after hours. "
        "A modern smartphone (NO logo, NO brand visible) lying screen-up with several "
        "blurred notification bubbles glowing on its dark screen. Half-empty matte black "
        "ceramic coffee mug next to it, coffee surface still. An open notebook with "
        "handwritten notes (illegible scribbles), a black ballpoint pen resting "
        "diagonally. Warm low side light from a window, deep shadows on the right side "
        "of the frame creating a natural dark area for typography overlay. "
        "Cinematic editorial mood, shallow depth of field, real materials, visible wood "
        "grain, slight dust particles in light beam. Color palette: warm browns, deep "
        "blacks, single cyan glow from phone screen. "
        "NO people, NO logos, NO brands, NO text in image, NO gears, NO holograms, NO "
        "3D graphics, NO futuristic elements, NO stock photo aesthetic. "
        "Vertical 4:5 composition, photorealistic, shot on Hasselblad, f/2.8."
    ),
    "v3_s2_notebook_caderno.png": (
        "Editorial still life photography. Close-up of an open premium aluminum laptop "
        "(NO logo visible, NO Apple, NO brand) on a clean light marble or pale oak desk. "
        "A leather-bound notebook lies next to the laptop, opened to a page with "
        "minimal handwritten notes in black ink. A matte fountain pen rests across the "
        "notebook page. The laptop screen is dim/off, showing only a soft reflection. "
        "Natural daylight from above-left, soft shadows, no harsh contrast. "
        "Background is intentionally minimalist with negative space on the right side "
        "for text overlay. Light, airy, calm atmosphere. Real textures: brushed "
        "aluminum, leather grain, paper fibers. Color palette: warm whites, soft "
        "beiges, muted aluminum greys. "
        "NO people, NO logos, NO brands, NO text in image, NO icons, NO gears, NO "
        "futuristic elements. Editorial magazine quality, shot like Kinfolk magazine, "
        "vertical 4:5 composition, photorealistic, soft natural light."
    ),
}

for filename, prompt in PROMPTS.items():
    print(f"→ Gerando {filename}...")
    response = client.models.generate_images(
        model="imagen-4.0-generate-001",
        prompt=prompt,
        config={"number_of_images": 1, "aspect_ratio": "3:4"},
    )
    img = response.generated_images[0].image
    img.save(str(OUT / filename))
    print(f"  ✓ salva em {OUT / filename}")

print("\n✓ Todas as imagens geradas.")
