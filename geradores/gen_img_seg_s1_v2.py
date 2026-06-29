#!/usr/bin/env python3
"""Nova imagem S1 Segunda — empresária sem tempo, cena editorial."""
from pathlib import Path
from google import genai

env = {}
for line in Path("/home/user/Meu-espa-o/.env").read_text().splitlines():
    if "=" in line and not line.strip().startswith("#"):
        k, v = line.split("=", 1)
        env[k.strip()] = v.strip().strip('"').strip("'")
client = genai.Client(api_key=env["GEMINI_API_KEY"])

OUT = Path("/home/user/Meu-espa-o/fotos/geradas")

prompt = (
    "Editorial cinematic photography of a real Brazilian businesswoman in her early "
    "thirties, mid-action at her desk, photographed slightly from the side at "
    "shoulder height. She is on her smartphone (NO logo, NO brand) pressed to her "
    "ear, looking down at a laptop screen (NO logo) with multiple open windows, "
    "while writing something quickly on a paper notepad with her free hand. "
    "Surrounding her: stacks of paper folders, sticky notes on the monitor edge, "
    "a half-finished cup of coffee, a calculator, an open agenda. The expression "
    "on her face shows controlled stress, focused but pressured. She wears a simple "
    "elegant black blouse, hair tied back. The office is modest but real — natural "
    "warm light from a window on the left, depth of field blurring the background "
    "slightly. The right third of the frame has natural negative space (a wall) "
    "for text overlay. Mood: a competent owner overwhelmed by simultaneous demands. "
    "NO logos, NO brands, NO text in image, NO multiple people, NO holograms, NO "
    "futuristic elements, NO stock photo aesthetic, NO posed smile, NO clean empty "
    "desk. Photorealistic, magazine editorial, vertical 4:5, shot on Hasselblad, "
    "natural skin texture, real workplace details."
)

print("→ Gerando seg_s1_empresaria.png...")
response = client.models.generate_images(
    model="imagen-4.0-generate-001",
    prompt=prompt,
    config={"number_of_images": 1, "aspect_ratio": "3:4"},
)
response.generated_images[0].image.save(str(OUT / "seg_s1_empresaria.png"))
print(f"  ✓ {OUT / 'seg_s1_empresaria.png'}")
