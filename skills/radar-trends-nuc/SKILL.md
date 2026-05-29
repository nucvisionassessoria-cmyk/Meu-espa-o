---
name: radar-trends-nuc
description: >
  Radar de trends e gerador de carrosséis estratégicos para a NUC Vision.
  Monitora assuntos em alta, polêmicas, cases e movimentos culturais do
  momento, transformando-os em carrosséis com leitura de mercado, gancho
  forte e narrativa progressiva. Use esta skill sempre que o usuário disser
  "oi", "olá", "bom dia", "boa tarde", ou pedir trends, assuntos em alta,
  carrossel de trend, carrossel de polêmica, surfar hype, conteúdo estratégico
  baseado em assunto atual, ou qualquer variação de "o que está em alta agora".
  A skill busca trends reais, constrói leitura estratégica e entrega carrossel
  completo com texto, direção visual, legenda e CTA — tudo alinhado à identidade
  NUC Vision.
---

# RADAR DE TRENDS E CARROSSÉIS ESTRATÉGICOS — NUC VISION

Esta skill transforma assuntos em alta em carrosséis que geram atenção,
autoridade e posicionamento para a NUC Vision. A premissa central é simples:
toda trend relevante contém uma lição de mercado. A skill encontra essa lição
e a transforma em conteúdo que vale ser salvo.

---

## ⚡ REGRA PRINCIPAL

**Não falar sobre a trend. Usar a trend como entrada para uma lição.**

A estrutura é sempre:
`Polêmica/trend → leitura estratégica → desenvolvimento → insight → fechamento forte → CTA leve`

Nunca entregar só "isso aconteceu e é interessante". Sempre chegar em
"isso revela algo importante sobre mercado, atenção, posicionamento ou crescimento".

**A NUC Vision NÃO deve aparecer no meio da narrativa.**
A autoridade vem da qualidade da leitura, não da autopromoção. O carrossel
deve fazer o leitor pensar "essa empresa enxerga o mercado de um jeito diferente"
— não "essa empresa está tentando vender o serviço dela em cima de uma trend".
A menção à NUC Vision fica apenas no CTA final, como assinatura de marca.

---

## FLUXO QUANDO O USUÁRIO INICIAR COM "OI" / SAUDAÇÃO SIMPLES

Ao receber "oi", "olá", "bom dia", "boa tarde", "e aí", "opa" ou qualquer
saudação informal:

### Passo 1 — Buscar trends atuais
Use WebSearch ou WebFetch para identificar assuntos em alta no momento.
Fontes prioritárias:
- Google Trends Brasil
- Twitter/X trending topics
- Portais: UOL, G1, Exame, Veja, Meio & Mensagem, Adweek Brasil
- Redes: Threads, Instagram trending, LinkedIn viral
- Casos de marca: campanhas, polêmicas corporativas, cases de crescimento
- Cases de creators/influenciadores com repercussão em negócios

**Se não houver acesso à internet:**
> "Oi! Meu acesso à internet está limitado agora. Me manda um link, print
> ou o nome de alguma trend/polêmica do momento que você queira usar — e eu
> transformo em carrossel estratégico."

### Passo 2 — Avaliar e selecionar 3 a 5 trends

Para cada trend encontrada, avaliar:
- Potencial de atenção (0–10)
- Conexão com negócios/mercado (0–10)
- Potencial de insight estratégico (0–10)
- Risco reputacional (baixo/médio/alto)
- Facilidade de narrar em carrossel

Selecionar apenas as que têm conexão real com: marketing, vendas,
posicionamento, autoridade, estrutura, branding, funil, crescimento ou
comportamento de mercado.

### Passo 3 — Apresentar ao usuário

Seguir o template `templates/resposta-inicial-trends.md`.

---

## FLUXO QUANDO O USUÁRIO ESCOLHER UMA TREND

Ao escolher, executar nesta ordem:

### Fase A — Roteiro estratégico
1. Leitura estratégica completa
2. Ideia central + título do carrossel
3. Estrutura de 7–10 slides (texto de cada lâmina + função narrativa)

### Fase B — CURADORIA VISUAL (ETAPA OBRIGATÓRIA — NÃO PULAR)

**Um carrossel não retém atenção só com tipografia em fundo escuro.**
Cada slide precisa de uma imagem real que represente o que está sendo dito e
ajude o leitor a visualizar o assunto. Antes de montar qualquer coisa:

1. Para CADA slide, definir **qual imagem específica ele precisa** — o
   objeto, a cena, o rosto, o produto, o contraste visual que sustenta o texto.
2. Montar o **briefing visual** (ver `templates/briefing-visual.md`): uma lista
   numerada, slide por slide, dizendo exatamente que imagem é necessária.
3. **Pedir essas imagens ao usuário.** Como não há acesso para baixar imagens
   da internet, o usuário precisa fornecê-las (upload no repositório, em
   `/home/user/Meu-espa-o/fotos/`). Para cada item, dar:
   - o que a imagem deve mostrar (objetivo)
   - uma sugestão de busca ("procure no Google por...")
   - alternativa caso não ache a ideal
4. Só seguir para a Fase C **depois** que o usuário disponibilizar as imagens
   (ou confirmar explicitamente que quer seguir sem alguma delas).

Regra de ouro: **mínimo de 1 imagem real por slide de conteúdo.** Slides
puramente tipográficos só são permitidos para o INSIGHT FORTE (clímax) e,
opcionalmente, o CTA. Todos os demais devem ter base visual.

### Fase C — Montagem final
Depois das imagens em mãos:
4. Direção visual detalhada de cada slide (texto + imagem + composição)
5. Legenda para Instagram
6. CTA final
7. Sugestões de capa (3 opções)
8. Observação de design/identidade visual
9. Adaptação para Reels (se fizer sentido)
10. Gerar HTML + exportar PNGs

Seguir o template `templates/carrossel-trend.md`.

---

## EMPRESA: NUC VISION

A NUC Vision é uma consultoria de estruturação comercial, marketing e
performance. Não é apenas agência de marketing. Atua em:

- Diagnóstico de gargalos invisíveis que travam crescimento
- Estruturação do processo comercial
- CRM e gestão de leads
- Posicionamento estratégico
- Marketing e tráfego pago com base em dados
- Atendimento e conversão
- Performance e crescimento sustentável

**Uso da NUC Vision no carrossel:**
A NUC Vision aparece como **assinatura**, não como protagonista.
- No desenvolvimento dos slides: NÃO mencionar a NUC Vision, salvo se a
  conexão for completamente orgânica e não parecer propaganda
- No slide de fechamento: pode aparecer de forma sutil, institucional
- No CTA final: sempre presente, sempre leve — jamais como "fale conosco"
  ou "contrate a NUC Vision"

**O tema de mercado conectado à trend** (posicionamento, vendas, branding,
funil, autoridade etc.) deve emergir como análise do assunto — não como
vitrine dos serviços da empresa. O leitor deve chegar à lição por conta
própria, não ser conduzido até ela por um anúncio disfarçado.

---

## PÚBLICO-ALVO DO CONTEÚDO

Escrever pensando em:
- Empresários e donos de negócios locais
- Prestadores de serviço (médicos, advogados, profissionais liberais)
- Gestores e empreendedores
- Estudantes de marketing e vendas
- Outras agências
- Curiosos atraídos pela polêmica

**Nível:** compreensível para quem não é especialista, mas inteligente o
suficiente para gerar percepção de autoridade em quem já conhece o mercado.

---

## TOM DE VOZ

### Slide 1 (gancho): direto, provocativo, polêmico quando necessário
### Slides 2–7 (desenvolvimento): consultivo, estratégico, sem ser chato
### Slide final (CTA): firme, confiante, sem mendigar engajamento

**Exemplos de gancho corretos:**
- "O mercado acabou de provar que currículo não é mais suficiente."
- "Essa polêmica mostra o que muita empresa ainda não entendeu."
- "O caso [X] não é só fofoca. É uma aula de posicionamento."
- "Essa trend explica por que algumas marcas crescem e outras somem."
- "O que aconteceu com [X] revela uma verdade incômoda sobre mercado."

**Evitar:** linguagem ofensiva gratuita, sensacionalismo sem substância,
explorar tragédias/sofrimento, afirmar fatos sem fonte, atacar pessoas
sem embasamento.

---

## ESTRUTURA NARRATIVA OBRIGATÓRIA

Todo carrossel deve seguir esta progressão:

```
1. ATENÇÃO      → "Isso aconteceu."
2. TENSÃO       → "Mas o ponto não é esse."
3. VIRADA       → "O que isso revela sobre mercado é maior."
4. EXPLICAÇÃO   → "Hoje, quem domina [X] consegue [Y]."
5. QUEBRA       → "O erro que a maioria comete aqui é..."
6. REVELAÇÃO    → "O que isso diz sobre mercado, marca, atenção ou comportamento."
7. INSIGHT      → Frase memorável que resume a lição.
8. FECHAMENTO   → Conclusão forte — sem citar a NUC Vision.
9. CTA          → Leve. Para seguir o perfil. Nunca para contratar.
```

Cada slide deve criar tensão suficiente para o leitor querer passar para o próximo.
Slide de fechamento: conclusão forte da narrativa, independente da empresa.
CTA: último slide, limpo, leve — assinatura de marca, não anúncio.

**O que evitar em qualquer slide que não seja o CTA:**
- "Na NUC Vision, fazemos isso..."
- "Aqui na NUC Vision, aplicamos..."
- "É por isso que o trabalho da NUC Vision..."
- "Se sua empresa precisa disso, fale com a NUC Vision..."
- "A NUC Vision ajuda empresas a..."

Essas frases só aparecem se o usuário pedir **explicitamente** um carrossel
mais institucional ou comercial.

---

## IDENTIDADE VISUAL DA NUC VISION

Ao descrever direção visual, referenciar sempre:

**Paleta:**
- Fundo: `#050810` (void escuro) ou `#0A0F1A` (navy profundo)
- Destaque: `#1EC5F2` (ciano vibrante) — pills, ícones, bordas, destaques
- Texto: branco (`#FFFFFF`) ou `rgba(255,255,255,0.75)` para secundário
- Gradiente: `linear-gradient(165deg, #1D4D8F 0%, #2591E6 55%, #5DD6F5 100%)`

**Tipografia:**
- Headline display: Anton (bold condensed, maiúsculas)
- Corpo e kickers: Space Grotesk (500–700)
- Hierarquia: display 44–80px / headline 22–32px / corpo 13–15px / kicker 10px

**Elementos visuais recorrentes:**
- Pill ciano com palavra-chave em destaque
- Kicker superior (tag uppercase pequena em ciano)
- Grade de pontos ou linhas sutil no fundo
- Vinheta leve nas bordas
- Divisor horizontal 2px ciano
- Logotipo NUC Vision no topo centralizado (branco em fundos escuros)

**Estilo editorial:**
- Slides com contraste alto
- Pouco texto por slide
- Espaço negativo como elemento de design
- Não parece apresentação corporativa — parece editorial de mídia premium

**GANCHO (SLIDE 1) — REGRA INEGOCIÁVEL:**
O slide 1 SEMPRE traz a pessoa/figura central da trend em destaque máximo e
**aparecendo por inteiro** — corpo, rosto e gesto visíveis. Nunca cortar a
cara, as mãos ou o gesto que dá força à imagem (ex: braços levantados).
- Se a foto vier com fundo de estúdio (branco), **recortar o fundo** e compor
  a pessoa sobre um cenário dramático que reforce o tema (ver
  `geradores/cutout_hamilton.py` como referência de recorte com PIL).
- `object-fit:cover` é PROIBIDO em foto de pessoa no gancho — corta o gesto.
  Usar a figura recortada em escala grande, ancorada, com gesto inteiro no quadro.
- Composição editorial: figura grande e central → balão de comentário viral
  (com grifo amarelo de marca-texto) no topo → título GIGANTE embaixo →
  pill "PASSE PARA O LADO ››". Espelhar a referência editorial enviada.
- Conferir o PNG exportado e, se a cara ou o gesto estiverem cortados ou
  cobertos pelo texto, refazer antes de entregar.

**SAFE-AREA — MARGEM DE SEGURANÇA OBRIGATÓRIA (igual mídia profissional):**
Nada de texto nem borda dura de imagem encosta nos limites do slide.
- Margem mínima: **laterais 32px, topo abaixo do logo, base 52px** (no canvas
  420×525). Nenhuma linha de texto pode terminar colada no rodapé.
- Texto é **conciso**: corpo de 2–3 linhas no máximo por slide. Parede de texto
  amontoada embaixo é amador — corte palavras até respirar. (Referência: slides
  da V4 — título forte, corpo curto, imagem como card contido com folga.)
- Quando a imagem for um bloco no rodapé, trate-a como **card contido** (cantos
  arredondados + margem em volta), não sangrando até a borda — a menos que seja
  hero full-bleed proposital (slide 1).
- Conferir o PNG: se o texto está a menos de ~40px da base, ou empilhado/denso,
  encurtar o texto e subir o bloco. Refazer até respirar.

**COMPOSIÇÃO E ESPAÇO — REGRA PERMANENTE (NÃO ERRAR):**
Todo slide é dividido em zonas verticais claras, com respiro. Nunca jogar
imagem no topo e amontoar texto embaixo, nem deixar espaço sobrando sem função.
- Pense o slide em 3 zonas: **topo** (logo + kicker), **meio** (imagem/elemento
  visual respirando, centralizada), **base** (headline + corpo, ancorada).
- Distribua o espaço: nenhuma zona deve ficar com vazio morto enquanto outra
  fica espremida. Se sobrou espaço no topo, a imagem ou o texto sobe.
- Imagem e texto **não disputam o mesmo espaço**: separe com gradiente de
  transição. Texto nunca cai por cima de área clara/colorida da imagem.
- **Contraste de leitura é obrigatório.** Palavra de destaque (ciano) sobre
  fundo escuro precisa de contraste real — se a cor da imagem competir, use
  **pill** (fundo ciano + texto escuro `#06121c`) em vez de texto ciano solto.
  Nunca deixar título azul sumir no fundo azul/escuro.
- Trim das margens transparentes do PNG antes de posicionar (ver
  `geradores/cutout_hamilton.py` / `getbbox`) para controlar escala e posição.
- Conferir SEMPRE o PNG exportado: se houver vazio morto, texto ilegível,
  imagem cortada ou bloco chapado, refazer antes de entregar.

**IMAGEM EM CADA SLIDE — REGRA CRÍTICA DE RETENÇÃO:**
O que segura a pessoa no carrossel é o visual, não o texto. Por isso:
- Todo slide de conteúdo tem uma imagem real representando o assunto
  (foto do produto, da pessoa, da cena, da marca, do objeto, do contraste)
- A imagem pode ser: fundo full-bleed com overlay escuro + texto por cima;
  meia-tela (imagem em cima, texto embaixo); card lateral; ou comparação
  lado a lado (ex: produto A vs produto B)
- Tratamento padrão: grayscale ou dessaturado + overlay gradiente escuro para
  o texto ciano/branco respirar por cima — coerência editorial premium
- Slides 100% tipográficos: SÓ no insight forte (clímax) e, se quiser, no CTA
- Se faltar imagem para um slide, PEDIR ao usuário antes de montar —
  nunca preencher com fundo vazio "para resolver"

**Fotos disponíveis no repositório** (`/home/user/Meu-espa-o/fotos/`):
- `derick_bracos_cruzados.jpg`, `iago_bracos_cruzados.png` — sócios posando
- `trio_reuniao.png` — os três sócios em reunião
- `lucas_derick.jpeg` — dupla de sócios
- `dashboard_laptop.png` — tela de dashboard/dados

---

## CTAs PADRÃO (variar conforme o tema)

O CTA deve soar como convite editorial, não como chamada comercial.
Tom: "siga para ver mais análises assim" — nunca "contrate", "fale conosco" ou "saiba mais".

- "Siga a NUC Vision para acompanhar leituras estratégicas sobre mercado, vendas e posicionamento."
- "Quer enxergar os movimentos do mercado com mais clareza? Siga a NUC Vision."
- "Para mais análises sobre negócios, mercado e crescimento, acompanhe a NUC Vision."
- "Siga a NUC Vision para ver o que está por trás das trends, marcas e movimentos do mercado."
- "Siga a NUC Vision. Aqui a gente lê o mercado antes de falar sobre ele."

---

## CRITÉRIOS DE AVALIAÇÃO DE TRENDS

Priorizar trends que tenham:

| Critério                        | Peso |
|---------------------------------|------|
| Potencial de atenção/viralidade | Alto |
| Conexão com negócios/mercado    | Alto |
| Possibilidade de insight real   | Alto |
| Potencial visual                | Médio|
| Risco reputacional baixo        | Alto |
| Facilidade de narrar 7–10 slides| Médio|

A melhor trend **não é** a mais famosa. É a que permite a leitura
estratégica mais rica para a NUC Vision.

---

## CUIDADOS COM POLÊMICAS

✓ Pode usar polêmicas como gancho
✓ Pode ter tom direto e provocativo
✓ Pode questionar decisões de marcas ou figuras públicas com base em fatos

✗ Não afirmar fatos sem fonte verificável
✗ Não difamar pessoas
✗ Não explorar tragédias ou sofrimento como entretenimento
✗ Não usar linguagem ofensiva gratuita
✗ Não publicar algo que prejudique a reputação da NUC Vision

---

## REFERÊNCIAS DE RACIOCÍNIO

Ver `examples/exemplo-toguro-smed.md` para modelo completo de como
transformar uma trend em carrossel estratégico.

Ver `templates/carrossel-trend.md` para o formato de entrega.

Ver `templates/direcao-visual.md` para como descrever a direção de cada slide.
