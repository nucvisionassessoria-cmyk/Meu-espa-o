# Prompts para gerar imagens no Gemini — Copa Hexa V2

Como o ambiente Claude Code on the web não tem `GEMINI_API_KEY`
configurado, as imagens são geradas manualmente em <https://gemini.google.com>
(modo "Gerar imagem") e baixadas para `/home/user/Meu-espa-o/fotos/`.

Quando estiverem na pasta com os nomes EXATOS abaixo, é só pedir
"re-roda o carrossel Copa Hexa" e a skill produz o V2 com as figuras
ancoradas no padrão NUC.

---

## 1. `copa_vinicius_escudo.png` (slide 1 — gancho)

**Equivalente V4:** Vinicius Jr beijando o escudo do Brasil, fundo
laranja texturizado (`copa_slide_01.jpg` do V4 baixado).

**Prompt:**
```
Cinematic editorial portrait of Vinicius Junior, Brazilian football
player, kissing the CBF Brazilian national team shield on his chest,
wearing the yellow Brazilian national team jersey with green collar
details, intense focused expression with closed eyes, vertical 9:16
framing, dramatic warm orange textured background like a stadium at
sunset, side rim light from the right creating cinematic shadow on
his face, shallow depth of field, photorealistic, magazine cover
quality, dramatic mood, high contrast.
```

---

## 2. `copa_neymar_ancelotti_taca.png` (slide 4 — virada)

**Equivalente V4:** Neymar + Ancelotti com troféu da Copa (slide 7 V4 —
fundo "A NARRATIVA JÁ ESTAVA PRONTA").

**Prompt:**
```
Iconic photograph of Neymar Junior wearing yellow Brazil jersey number
10 and Carlo Ancelotti in coach attire, both raising a golden FIFA
World Cup trophy together at a Brazilian football stadium, both with
joyful expressions, dramatic golden hour stadium lighting, crowd in
deep background out of focus, vertical 4:5 framing, emotional
victorious moment, photojournalism style, photorealistic, slight
vintage warm grade.
```

---

## 3. `copa_camisa_brasil_mockup.png` (slide 5 — escalada)

**Equivalente V4:** designer Rachel Denti mostrando a camisa no phone
mockup (slide 5 V4). Como ela é pessoa exclusiva do V4, substituímos
pelo OBJETO central (a camisa) em editorial limpo.

**Prompt:**
```
Studio editorial mockup of a yellow Brazilian national team football
jersey from 2026 World Cup, mounted on a faceless dark mannequin torso
against a dramatic dark grey gradient studio background, dramatic side
key light from the left highlighting fabric texture and geometric
green and blue detail patterns from the Brazilian flag, vertical 4:5
framing, magazine product photography, photorealistic, slight reflection
on the surface below.
```

---

## 4. `copa_torcida_brasil.png` (slide 8 — CTA)

**Equivalente V4:** sócios V4 vestidos de árbitro (slide 11 V4). Como
os sócios deles são exclusivos, equivalente do mesmo registro emocional
(celebração intensa) é torcida brasileira em festa.

**Prompt:**
```
Massive Brazilian football crowd celebrating victory at a stadium, sea
of fans wearing yellow Brazilian national team jerseys with green and
blue painted faces, Brazilian flags waving everywhere, hands raised in
pure euphoria, golden hour stadium lighting, slight motion blur on some
figures conveying movement, vertical 4:5 framing, photorealistic,
emotional moment of national celebration, no specific recognizable
faces in foreground.
```

---

## Como usar

1. Abre <https://gemini.google.com> (com sua conta Google).
2. Pra cada prompt acima, escreve "gere uma imagem com este prompt:" e cola.
3. Quando a imagem aparecer, clica em baixar.
4. Renomeia conforme o nome do arquivo de cada seção (ex:
   `copa_vinicius_escudo.png`).
5. Move pra `/home/user/Meu-espa-o/fotos/` (ou faz upload via Cowork web).
6. Volta no chat e fala: "**imagens prontas**".
7. Eu re-rodo o gerador (`gen_copa_hexa.py v2`) com as figuras
   ancoradas (sombra de contato + light wrap + grão) seguindo
   `nuc-carrossel`.

## Se uma imagem sair ruim

Se o Gemini errar (jogador irreconhecível, composição ruim), volta o
prompt com ajuste. Padrões úteis pra reforçar:
- Mudou cara: adiciona "with realistic facial features, recognizable
  Brazilian football star face"
- Composição: "centered framing, subject occupies center 60% of frame"
- Cor: "vibrant yellow Brazil jersey color #FFDF00, deep green collar
  #009C3B"

## Backup: gerar via Imagen 4 API (futuro)

Quando salvar `GEMINI_API_KEY` no environment, a skill passa a chamar
Imagen 4 direto via API e zera o trabalho manual aqui. Anota como
melhoria do próximo ciclo.
