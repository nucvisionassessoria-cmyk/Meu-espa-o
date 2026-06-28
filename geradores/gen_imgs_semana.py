#!/usr/bin/env python3
"""Gera todas as imagens humanizadas para Quarta (Derick) e Sexta (Lucas) via Imagen 4."""
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
    # ── QUARTA — "O dono virou o gargalo" (escuro) ──
    "qua_s1_dono_noite.png": (
        "Editorial cinematic photography. A real home office at night. A small warm "
        "desk lamp is the only light source, casting golden glow on a wooden desk with "
        "an open laptop (NO logo, NO brand) showing a dim screen. Window in background "
        "is dark, showing distant city lights blurred. Empty leather office chair "
        "pushed slightly back. Coffee mug on desk, cold and untouched. Stack of "
        "papers, an open notebook with handwritten lists, a phone face-down. Mood: "
        "late, tired, the room of someone who never stops working. Deep shadows, "
        "warm rim light. "
        "NO people visible, NO logos, NO brands, NO text in image, NO gears, NO "
        "holograms, NO futuristic elements. "
        "Photorealistic, cinematic, vertical 4:5, shallow depth of field."
    ),
    "qua_s2_panorama_empresa.png": (
        "Wide editorial photography of a real small business office at dusk, seen from "
        "above and behind. Empty workstations with personal items still on desks "
        "(notebooks, mugs, jackets on chairs). Long shadows from late afternoon light "
        "through large windows. The office is well-organized but clearly waiting for "
        "people. One desk in the foreground is more cluttered than the rest — the "
        "founder's desk, with extra papers, a tablet, multiple notebooks, a "
        "calculator. Mood: silent, suspended, ready. "
        "NO people, NO logos, NO brands, NO text, NO digital screens visible. "
        "Photorealistic, editorial documentary, vertical 4:5, warm tones."
    ),
    "qua_s4_agenda_lotada.png": (
        "Editorial flat-lay photography of a real paper agenda book opened on a clean "
        "light desk. Every single hour is filled with handwritten appointments in "
        "black and blue ink, some entries crossed out, some highlighted in yellow "
        "marker, a few sticky notes covering parts of the page. Pen and reading "
        "glasses to the side. Coffee cup half-empty in the corner. Natural daylight "
        "from above, soft shadows. The agenda visually overwhelms the frame. "
        "NO people, NO logos, NO brands, NO digital elements, NO smartphones. "
        "Photorealistic, top-down editorial flat-lay, vertical 4:5, magazine quality."
    ),
    "qua_s5_sombra_dono.png": (
        "Cinematic editorial photography. A single empty office chair in the center "
        "of a dimly lit conference room, illuminated by one overhead spotlight. The "
        "rest of the room fades into darkness. Long polished table reflects the chair "
        "subtly. Mood: the weight of a single position holding everything. Symbolic, "
        "minimalist, dramatic. "
        "NO people, NO logos, NO brands, NO text, NO holograms. "
        "Photorealistic, cinematic, vertical 4:5, deep blacks, single light source."
    ),
    "qua_s7_notebook_planejamento.png": (
        "Editorial still life photography. A leather notebook open on a wooden desk, "
        "filled with handwritten planning: a list of names with roles next to them, "
        "arrows connecting tasks, deadlines circled. A premium aluminum laptop (NO "
        "logo) is partially visible to the side. A black fountain pen rests across "
        "the notebook. Small minimalist desk plant in a terracotta pot in the corner. "
        "Soft natural side light, deliberate composition with negative space on the "
        "right for text overlay. "
        "NO people, NO logos, NO brands, NO readable text in image. "
        "Photorealistic, Kinfolk editorial, vertical 4:5, calm and structured."
    ),

    # ── SEXTA — "Marketing não conserta operação" (claro) ──
    "sex_s1_mesa_premium.png": (
        "Editorial flat-lay photography of a premium minimalist workspace, top-down "
        "view. A premium aluminum laptop (NO logo, NO brand) centered, screen showing "
        "a soft solid color (no UI). A leather notebook neatly placed to its right, "
        "a black fountain pen across it. A white ceramic espresso cup half-full on a "
        "saucer to its left. A small green plant in a white pot at the top corner. "
        "Light oak wood surface, breathing room between objects. Natural diffused "
        "morning daylight from above. Composition feels deliberate, calm, premium, "
        "ready for big decisions. "
        "NO people, NO logos, NO brands, NO text in image, NO icons, NO holograms. "
        "Photorealistic, magazine-quality flat-lay, vertical 4:5."
    ),
    "sex_s2_megafone_metafora.png": (
        "Editorial still life photography on a clean light marble background. A "
        "vintage brass megaphone resting on its side, casting a soft real shadow. "
        "Next to it, a small cracked ceramic pot — visually broken but still standing. "
        "Composition is minimalist, deliberate, symbolic: a tool of amplification "
        "next to something fragile. Soft natural light from the side, no harsh "
        "contrast. Generous negative space on the right for text overlay. "
        "NO people, NO logos, NO brands, NO text in image, NO digital elements, "
        "NO megaphone facing camera. "
        "Photorealistic, fine art still life, vertical 4:5, Kinfolk magazine style."
    ),
    "sex_s4_promessa_entrega.png": (
        "Editorial still life. A clean light wood desk with two contrasting objects "
        "placed side by side with intention. On the left: a beautifully wrapped "
        "premium package with a thin black ribbon, pristine. On the right: an opened "
        "package showing simpler, more modest contents inside — a plain notebook and "
        "a basic pen. The contrast between the promise (the wrapping) and the "
        "delivery (the contents) is the subject. Soft natural daylight from above-"
        "left, gentle shadows, refined composition. Generous negative space at top "
        "for text overlay. "
        "NO people, NO logos, NO brands, NO readable text, NO logos on packaging. "
        "Photorealistic, editorial conceptual still life, vertical 4:5."
    ),
    "sex_s5_dinheiro_perdido.png": (
        "Editorial still life on a clean light desk. A few paper Brazilian banknotes "
        "(generic, no readable text or value) crumpled and partially torn, scattered "
        "next to a half-empty coffee cup that has spilled a small ring on the desk. "
        "An open agenda book in the background, slightly out of focus, with some "
        "ink-smudged pages. Mood: investment that went wrong, money turned into "
        "noise. Soft natural side light, restrained composition with negative space "
        "above for text. "
        "NO people, NO logos, NO brands, NO readable text, NO specific currency "
        "denomination visible. "
        "Photorealistic, editorial fine art, vertical 4:5, melancholic but refined."
    ),
    "sex_s7_ordem_certa.png": (
        "Editorial flat-lay photography. A clean light oak desk seen from above with "
        "five small simple wooden blocks lined up in a perfect row, each block bearing "
        "no markings. To the right of the row, a leather notebook is open with "
        "minimal handwritten planning. A black fountain pen rests parallel to the "
        "notebook edge. A white ceramic coffee cup half-full at the bottom of the "
        "frame. Composition: deliberate sequence, structure, calm. Natural morning "
        "daylight from above, soft even shadows. Generous breathing room. "
        "NO people, NO logos, NO brands, NO readable text, NO icons, NO digital "
        "elements. "
        "Photorealistic, premium flat-lay, vertical 4:5, magazine quality."
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

print("\n✓ 10 imagens geradas.")
