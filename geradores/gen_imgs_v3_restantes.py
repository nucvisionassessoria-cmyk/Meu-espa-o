#!/usr/bin/env python3
"""Gera as 4 imagens humanizadas restantes (S4, S5, S7, S8) via Imagen 4."""
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

PROMPTS = {
    "v3_s4_postits.png": (
        "Editorial photography of a real office wall covered with 12 to 15 paper "
        "sticky notes in muted colors (pale yellow, faded peach, soft mint, off-white). "
        "Each note slightly tilted at different angles, some with illegible handwritten "
        "marks in black or blue pen, two or three notes blank, one note half-falling. "
        "Wall is plain warm white with subtle texture. Natural side window light "
        "creating soft shadows under each note. Composition is mid-shot, notes filling "
        "the frame but with breathing room. The arrangement looks human and lived-in, "
        "NOT organized in a grid. "
        "NO logos, NO brands, NO readable text, NO people, NO arrows, NO icons, NO "
        "digital elements, NO computer screens. "
        "Photorealistic, magazine quality, soft natural light, vertical 4:5, "
        "documentary editorial style."
    ),
    "v3_s5_sobrecarga.png": (
        "Editorial photography of a small wooden desk that is visibly overloaded. "
        "Stack of paper folders piled unevenly on one side, several loose printed "
        "sheets fanning out, a calculator face-down, a smartphone (NO logo) lying on "
        "top with a blurred notification glow, a half-empty coffee mug pushed to the "
        "edge, an open agenda book with handwritten appointments, a pen tossed "
        "carelessly. An empty office chair pushed back, slightly visible at the edge "
        "of frame. Low warm light from a desk lamp, deep shadows, slightly "
        "claustrophobic mood. The desk feels like someone just stepped away mid-crisis. "
        "NO people, NO logos, NO brands, NO readable text, NO holograms, NO gears, NO "
        "futuristic elements, NO stock photo aesthetic. "
        "Photorealistic, cinematic, vertical 4:5, shallow depth of field."
    ),
    "v3_s7_notebook_fechado.png": (
        "Editorial still life. A closed premium aluminum laptop (NO logo, NO brand) "
        "resting on a clean light wood desk, with a matte fountain pen placed neatly "
        "across the top of the closed lid, perfectly parallel to the laptop edge. "
        "A small leather notebook stacked underneath, aligned. Empty white ceramic "
        "coffee cup on a saucer to the side, finished. Everything in calm order, "
        "intentional, finished, ready. Soft morning light from above-left, "
        "minimalist composition with significant negative space on the right side "
        "for text overlay. "
        "NO people, NO logos, NO brands, NO text in image, NO icons, NO digital "
        "elements visible. "
        "Photorealistic, Kinfolk-style editorial, vertical 4:5, calm and structured."
    ),
    "v3_s8_mesa_organizada.png": (
        "Top-down (flat lay) editorial photography of a clean organized workspace. "
        "A premium aluminum laptop (NO logo) centered, slightly open. To its right, "
        "a leather notebook squared neatly next to a black ballpoint pen. To its left, "
        "a white ceramic coffee cup half-full of espresso on a saucer. A small green "
        "plant in a terracotta pot at the top corner. Everything intentionally placed, "
        "breathing room between objects, light oak wood surface visible. Natural "
        "morning daylight from above creating soft, even illumination with subtle "
        "shadows. Composition feels deliberate, calm, premium. "
        "NO people, NO logos, NO brands, NO text in image, NO icons, NO holograms, "
        "NO stock photo aesthetic. "
        "Photorealistic, flat lay editorial, vertical 4:5, magazine quality."
    ),
}

for filename, prompt in PROMPTS.items():
    print(f"→ Gerando {filename}...")
    response = client.models.generate_images(
        model="imagen-4.0-generate-001",
        prompt=prompt,
        config={"number_of_images": 1, "aspect_ratio": "3:4"},
    )
    response.generated_images[0].image.save(str(OUT / filename))
    print(f"  ✓ {OUT / filename}")

print("\n✓ Concluído.")
