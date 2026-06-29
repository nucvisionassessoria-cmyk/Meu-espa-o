#!/usr/bin/env python3
"""Imagens v2 — metáforas conceituais para Quarta e Sexta. Mais ousadia visual."""
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
    # ── QUARTA (escuro) ──
    "qua_s1_dono_chiaroscuro.png": (
        "Editorial portrait photography in dramatic chiaroscuro lighting. A Brazilian "
        "male business owner in his late thirties, photographed from a slight three-"
        "quarter angle, only one side of his face illuminated by a single warm light "
        "source from camera-left. The other half of his face fades into deep shadow. "
        "He is looking down and slightly away, expression of controlled exhaustion, "
        "the weight of decisions visible in his eyes. He wears a simple dark shirt. "
        "Background is pitch black. Style inspired by Vanity Fair portraits and "
        "Caravaggio paintings. Real skin texture, every pore visible, slight stubble. "
        "Composition leaves significant negative space on one side for typography. "
        "NO logos, NO brands, NO text in image, NO computer, NO desk, NO other people, "
        "NO posed corporate smile, NO clean studio look. "
        "Photorealistic, cinematic, vertical 4:5, shot on Hasselblad, f/1.8, museum-"
        "quality portrait."
    ),
    "qua_s2_cadeira_auditorio.png": (
        "Surreal editorial cinematic photography. A single empty black leather "
        "executive office chair positioned at the dead center of a vast empty "
        "auditorium or conference hall. The chair is illuminated by one dramatic "
        "theatrical spotlight from directly above, creating a perfect circle of "
        "light around it. The rest of the auditorium fades into deep blackness — "
        "rows of empty seats barely visible in the shadows on the sides. Polished "
        "dark wood floor reflects the chair slightly. Atmosphere: theatrical, "
        "lonely, the weight of a single position. Conceptual symbolic still life. "
        "NO people, NO logos, NO text in image, NO holograms, NO modern tech, "
        "NO digital elements. "
        "Photorealistic, cinematic dramatic lighting, vertical 4:5, mood inspired "
        "by stage photography and film noir."
    ),
    "qua_s4_pratos_circo.png": (
        "Conceptual editorial still life photography on a dark theatrical background. "
        "Three or four thin tall wooden sticks rising from a wooden surface, each "
        "balancing a different real office object spinning precariously on top: one "
        "stick holds a thick paper file folder tilting dangerously, another holds an "
        "open leather notebook, another holds a small calculator about to fall, "
        "another holds a smartphone (NO logo) at an extreme angle. Some objects on "
        "the verge of crashing. Single dramatic warm side light from camera-left "
        "creating long deep shadows. Mood: precarious balance, about to collapse. "
        "NO people, NO logos, NO brands, NO text in image, NO actual circus plates "
        "(use the office objects instead), NO holograms. "
        "Photorealistic, fine art conceptual still life, vertical 4:5, dramatic "
        "chiaroscuro lighting."
    ),
    "qua_s5_castelo_cartas.png": (
        "Editorial fine art photography. An impossibly tall and elaborate house of "
        "cards constructed from generic plain white playing cards (NO suits visible, "
        "NO brand markings) standing on a dark polished wood office desk. The "
        "structure rises seven or eight levels high, tilting subtly to one side, on "
        "the verge of collapse. One single card is starting to slip out of the base. "
        "Dramatic chiaroscuro side lighting from camera-right, deep black background "
        "fading to absolute darkness. Symbolic of extreme fragility holding "
        "everything together. "
        "NO people, NO logos, NO brands, NO text in image, NO suit symbols on the "
        "cards (hearts/spades), NO modern elements. "
        "Photorealistic, museum-quality fine art still life, vertical 4:5, "
        "dramatic warm side light."
    ),
    "qua_s7_postits_quadrantes.png": (
        "Editorial documentary photography of a real office wall divided into four "
        "clear visual quadrants by thin painted lines. Each quadrant contains a "
        "cluster of paper sticky notes in different muted colors: top-left quadrant "
        "has pale yellow notes, top-right has soft mint green notes, bottom-left "
        "has muted peach notes, bottom-right has plain white notes. Each cluster "
        "has 3 to 5 sticky notes neatly arranged but not perfectly aligned. Some "
        "notes have illegible handwriting. The visual division between quadrants "
        "is clear and intentional. Warm natural side light from camera-left "
        "creating soft shadows under each note. Symbolic of clear division of "
        "responsibilities. "
        "NO people, NO logos, NO brands, NO readable text, NO digital elements, "
        "NO icons. "
        "Photorealistic, magazine-quality documentary editorial, vertical 4:5."
    ),

    # ── SEXTA (claro, com 1 ou 2 quebras) ──
    "sex_s1_megafone_castelo.png": (
        "Conceptual fine art still life photography on a clean off-white seamless "
        "background. In the foreground (left half of frame): a massive vintage brass "
        "megaphone, gleaming, aimed toward the right. In the background (right half, "
        "midground distance): a small fragile house of cards built from generic "
        "playing cards (NO suits visible), some cards beginning to topple from the "
        "implied force of the megaphone. Subtle motion blur on the falling cards. "
        "Soft natural daylight from above-left, gentle shadows. The composition "
        "creates visual cause-and-effect: amplification destroying fragile "
        "structure. Symbolic, editorial. "
        "NO people, NO logos, NO brands, NO text in image, NO sound waves drawn, "
        "NO digital elements, NO suit symbols on cards. "
        "Photorealistic, fine art conceptual still life, vertical 4:5, magazine "
        "quality."
    ),
    "sex_s2_porta_campo.png": (
        "Surreal editorial photography in the style of René Magritte but "
        "photorealistic. A single tall white wooden door, freestanding without any "
        "wall around it, planted in the middle of a vast open empty grassy field. "
        "The door is slightly ajar, revealing only soft light inside. Wide open "
        "blue sky above with a few small clouds, golden hour soft side light "
        "casting a long shadow of the door across the grass. The horizon stretches "
        "wide and empty. Mood: dreamlike, contemplative, conceptual — the right "
        "question stands alone. "
        "NO people, NO logos, NO brands, NO text in image, NO buildings, NO other "
        "objects, NO animals. "
        "Photorealistic, surreal editorial photography, vertical 4:5, large format "
        "feel, magazine quality."
    ),
    "sex_s4_caixas_contraste.png": (
        "Editorial conceptual still life photography on clean white marble surface. "
        "Two boxes placed side by side with intention. On the left: a large luxurious "
        "premium gift box, glossy black with a thin gold ribbon untied, lid lifted, "
        "revealing almost-empty interior — only a small piece of crumpled tissue "
        "paper inside. On the right: a smaller modest plain cardboard box, opened, "
        "revealing real useful contents — a leather notebook, a pen, and a small "
        "wooden ruler. The visual contrast between the impressive promise (left) "
        "and the modest real delivery (right) is the subject. Soft natural daylight "
        "from above, deliberate gentle shadows. "
        "NO people, NO logos, NO brands, NO readable text, NO logos on packaging, "
        "NO holograms. "
        "Photorealistic, fine art editorial conceptual still life, vertical 4:5, "
        "Kinfolk magazine style."
    ),
    "sex_s5_dinheiro_vento.png": (
        "Surreal editorial photography. Several paper banknotes (generic, NO "
        "readable numbers or text, plain greenish-grey color) caught mid-air, "
        "flying and tumbling diagonally across the frame, motion blur on some "
        "bills. Setting: an empty pale countryside road stretching into the "
        "distance, soft pale sky, golden hour low light. The notes appear to be "
        "blown by strong wind, scattering away from the camera. Mood: investment "
        "lost to nothing, money turned into noise carried by the wind. "
        "NO people, NO logos, NO brands, NO readable currency text, NO specific "
        "denomination visible, NO buildings, NO cars. "
        "Photorealistic, fine art editorial conceptual, vertical 4:5, melancholic "
        "cinematic mood."
    ),
    "sex_s7_dominos_ordem.png": (
        "Editorial fine art conceptual photography. A row of five elegant matte "
        "black domino tiles standing upright in perfect order on a clean light "
        "wood surface, evenly spaced. The first domino on the left is beginning "
        "to tip forward toward the second, frozen mid-fall. The rest stand still, "
        "ready in sequence. Dramatic strong side light from camera-right casting "
        "long parallel shadows behind each tile. Shallow depth of field, the first "
        "domino sharp, the back ones slightly soft. Mood: deliberate sequence, "
        "controlled momentum. "
        "NO people, NO logos, NO brands, NO text in image, NO dots on the dominos "
        "(plain matte black tiles), NO digital elements. "
        "Photorealistic, museum-quality fine art still life, vertical 4:5, "
        "minimalist editorial."
    ),
}

for filename, prompt in PROMPTS.items():
    print(f"→ {filename}...")
    response = client.models.generate_images(
        model="imagen-4.0-generate-001",
        prompt=prompt,
        config={"number_of_images": 1, "aspect_ratio": "3:4"},
    )
    response.generated_images[0].image.save(str(OUT / filename))
    print(f"  ✓")

print("\n✓ 10 imagens conceituais geradas.")
