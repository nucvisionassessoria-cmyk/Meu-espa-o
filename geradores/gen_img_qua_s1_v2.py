#!/usr/bin/env python3
"""Nova imagem S1 Quarta — dono homem trabalhando tarde da noite."""
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
    "Editorial cinematic photography of a Brazilian male business owner in his "
    "late thirties or early forties, photographed from a side-three-quarter angle "
    "in his home office late at night. He sits at his desk facing a laptop screen "
    "(NO logo, NO brand), the only strong light source — a warm screen glow on his "
    "face. He is on the phone, holding it to his ear, slightly hunched, expression "
    "of focused exhaustion. His other hand is on the mouse. The desk has stacks "
    "of papers, an open notebook, a half-empty coffee mug, and a calculator. "
    "Behind him, the room fades into darkness with a window showing distant blurred "
    "city lights. He wears a simple dark polo or button-down shirt, slightly "
    "wrinkled. Mood: the founder who never stopped working, the man behind the "
    "company. Composition leaves natural negative space in the lower foreground "
    "(out of focus) for text overlay. "
    "NO logos, NO brands, NO text in image, NO other people, NO holograms, NO "
    "gears, NO futuristic elements, NO posed studio look, NO clean empty office. "
    "Photorealistic, magazine editorial, vertical 4:5, shot on Hasselblad, "
    "shallow depth of field, real skin texture, warm dim lighting."
)

print("→ Gerando qua_s1_dono_homem.png...")
response = client.models.generate_images(
    model="imagen-4.0-generate-001",
    prompt=prompt,
    config={"number_of_images": 1, "aspect_ratio": "3:4"},
)
response.generated_images[0].image.save(str(OUT / "qua_s1_dono_homem.png"))
print(f"  ✓ {OUT / 'qua_s1_dono_homem.png'}")
