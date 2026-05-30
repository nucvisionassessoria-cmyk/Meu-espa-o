---
name: nuc-carrossel
description: >
  Gera carrosséis editoriais (Instagram, 1080x1350) da NUC Vision a partir de assets
  enviados pelo usuário. Pipeline: Python monta HTML com imagens inline em base64; o HTML
  é renderizado pelo Chromium (Playwright) e exportado em PNG. Use SEMPRE que o pedido
  envolver criar/editar slides, posts, carrosséis ou "leituras de mercado" da NUC. Esta
  skill define DOIS padrões obrigatórios: (1) narrativa contínua com dependência entre
  slides e (2) produção visual nível campanha de agência premium. Proíbe tanto o
  "carrossel-lista" quanto o visual "flat/IA" das versões antigas.
---

# SKILL: CARROSSEL NUC VISION — NARRATIVA + PADRÃO CAMPANHA

Ordem de execução obrigatória:
**SEÇÃO 0 (roteiro) → SEÇÕES 1–8 (produção visual).**
Primeiro a história inteira é definida; só depois qualquer slide é desenhado.

=================================================================================
# SEÇÃO 0 — O CARROSSEL É UMA HISTÓRIA, NÃO UMA LISTA
=================================================================================

## PRINCÍPIO MESTRE (inegociável)
**Cada slide existe PORQUE o anterior tornou sua existência necessária.**
Se remover qualquer slide e a narrativa continuar funcionando, o carrossel foi
construído errado e deve ser refeito. Este é o teste final (ver QA narrativo).

A falha que esta seção corrige: slides com começo-meio-fim próprios, que funcionam
publicados isoladamente. Isso é uma "lista visualmente bonita" — não gera retenção,
curiosidade nem consumo completo.

## ORDEM DAS OPERAÇÕES (a causa raiz)
É PROIBIDO escrever qualquer slide antes de existir o roteiro completo. A dependência
narrativa só nasce se a história inteira for definida ANTES de qualquer slide.

Fluxo obrigatório:
1. **Definir o arco completo** (Etapa A) — antes de pensar em layout.
2. **Atribuir um papel funcional a cada slide** (Etapa B).
3. **Escrever cada slide com loop aberto** (Etapa C) — proibido fechar sozinho.
4. **Rodar o teste de remoção** (Etapa D).
5. SÓ ENTÃO aplicar as regras visuais (Seções 1–8).

NUNCA gere "slide por slide" decidindo o conteúdo na hora de desenhar. Isso reproduz
o problema. O roteiro é um artefato separado que precede o design.

## ETAPA A — CONSTRUIR O ARCO (antes de tudo)
Escolha UM dos 5 modelos conforme o tema e escreva o arco em uma frase por beat:

- **Modelo 1 — Investigação:** problema → pistas → descoberta → conclusão.
- **Modelo 2 — Quebra de crença:** crença → conflito → evidência → nova visão.
- **Modelo 3 — História:** contexto → tensão → desenvolvimento → resolução.
- **Modelo 4 — Explicação progressiva:** pergunta → aprofundamento → descoberta → aplicação.
- **Modelo 5 — Polêmica:** fato → interpretação → conflito → explicação → insight.

Defina a **promessa central** (o que o leitor vai descobrir no final) e mantenha-a
ESCONDIDA até a revelação. Toda a tração vem da distância entre a promessa do slide 1
e a entrega no slide final.

## ETAPA B — PAPÉIS FUNCIONAIS (cada slide tem UM papel)
Atribua a cada slide um e apenas um papel. Nenhum slide pode ser "mais uma informação".

1. **GANCHO** — para o scroll. Cria uma lacuna de curiosidade ou tensão. NÃO entrega resposta.
2. **CURIOSIDADE** — aprofunda a lacuna, faz avançar. Levanta uma nova pergunta.
3. **ESCALADA** (1+) — aumenta a aposta/o interesse. Começa a responder MAS abre nova camada.
4. **VIRADA/INESPERADO** — mostra algo que o leitor não esperava. Recontextualiza.
5. **REVELAÇÃO** — o ponto mais forte. Entrega a promessa central.
6. **INSIGHT** — o aprendizado generalizável (o "e daí pra você").
7. **CTA** — encerramento e ação.

O número de slides de ESCALADA varia com o tema (carrossel típico: 6–10 slides).
Ordem dos papéis é fixa: gancho → curiosidade → escalada → virada → revelação → insight → CTA.

## ETAPA C — REGRA DO LOOP ABERTO (o motor da retenção)
Todo slide, EXCETO os dois finais (insight e CTA), é PROIBIDO de se resolver.
Cada slide tem duas partes:
- **Entrega parcial:** responde um pedaço do que o slide anterior abriu.
- **Ponte (open loop):** abre uma nova lacuna que SÓ o próximo slide fecha.

Técnicas de ponte (use uma por transição):
- Pergunta não respondida ("...mas o que ninguém viu foi o que veio depois.")
- Informação incompleta ("E o número que explica isso? No próximo.")
- Contradição plantada ("Parecia certo. Não era.")
- Promessa de payoff ("Aqui começa o erro de R$ X.")
- Tensão temporal ("No dia seguinte, tudo mudou.")

PROIBIDO: terminar um slide do meio com conclusão fechada, ponto final semântico ou
frase de efeito que funciona como "fim". Slide do meio que dá sensação de encerramento
mata o avanço.

## ETAPA D — TESTE DE REMOÇÃO (antes de finalizar o roteiro)
Para CADA slide do meio: "Se eu apagar este slide, o seguinte ainda faz sentido sozinho?"
- Se SIM → não cria dependência. Reescreva (a entrega dele precisa ser pré-requisito do
  próximo, e a ponte precisa abrir o próximo).
- Se NÃO (a narrativa quebra) → aprovado.

## TESTE DE QUALIDADE NARRATIVA (rodar antes do QA visual)
Qualquer "não" → reescreva o roteiro, não só o slide.
1. O slide seguinte é necessário (o anterior criou a necessidade dele)?
2. Existe curiosidade real entre os slides (loop aberto em cada transição)?
3. O leitor sente progresso (cada slide entrega um pedaço novo)?
4. Existe UMA história sendo contada (um único arco, um único modelo)?
5. Se eu apagar um slide do meio, a narrativa quebra?
6. O conteúdo gera sensação de descoberta (promessa escondida até a revelação)?
7. O último slide recompensa o tempo investido (payoff > expectativa do gancho)?

## EXEMPLO DE ARCO (Modelo 5 — Polêmica, tema Ferrari/Lambo)
- S1 GANCHO: "Uma marca lendária acabou de cometer um erro de R$ bilhões." (não diz qual)
- S2 CURIOSIDADE: o fato — mas "a reação foi pior que o lançamento".
- S3 ESCALADA: a reação do mercado — "mas o detalhe que ninguém comentou foi a concorrente".
- S4 VIRADA: a concorrente não fez nada e venceu — "e o motivo não é o que parece".
- S5 ESCALADA: o que a concorrente realmente fez (1 movimento) — "isso revela uma regra".
- S6 REVELAÇÃO: a regra de posicionamento (a promessa central, enfim entregue).
- S7 INSIGHT: o que isso ensina pra qualquer marca/leitor.
- S8 CTA.
Nenhum slide do meio fecha. Cada um entrega 1 peça e abre a próxima.

=================================================================================
# SEÇÕES 1–8 — PRODUÇÃO VISUAL (PADRÃO CAMPANHA)
=================================================================================

Você está gerando peças que competem com material de agência premium. Padrão de saída:
**arte pronta para campanha**, não "post de template". Toda peça que parecer gerada por
IA — objetos flutuando, luz chapada, fundo liso, recorte serrilhado — é uma FALHA.

Regra mestra visual: **nada flutua, nada é liso, nada tem luz incoerente com a cena.**

## 1. CONTEXTO DO PIPELINE
- Saída: PNG 1080x1350 (4:5), renderizado por **Chromium headless** a 2.571x.
- Você escreve **Python que gera strings HTML** com imagens inline em base64 (`photo_uri()`).
- Motor = Chromium real → CSS COMPLETO: `filter`, `box-shadow`, `mix-blend-mode`,
  `backdrop-filter`, `::before/::after`, SVG, `radial-gradient`.
- Recortes (PNG RGBA) chegam via `rembg`/flood-fill. Seu trabalho é **integrá-los a uma
  cena com física correta**, não só posicioná-los.
- Se existir `nuc_realism.py` no repo, IMPORTE e use (`fundo_profundo`, `recorte`, `card`,
  `GRAO_OVERLAY`, `REALISM_CSS`). Não reinvente.

## ÂNCORA VISUAL OBRIGATÓRIA (anti-downgrade)
Todo slide — exceto, no máximo, os de INSIGHT puro e CTA — PRECISA de uma âncora visual
(recorte de carro/pessoa, foto, print, comparativo, ou elemento gráfico forte). É PROIBIDO
um carrossel virar majoritariamente slides de texto sobre fundo escuro. Se um slide só tem
texto, pergunte: existe imagem que reforça este beat? Se sim, use. Texto puro é exceção,
não regra. (Isto reverte o erro em que a peça perdeu as imagens e virou lista de frases.)

## 2. OS 5 NÃO-NEGOCIÁVEIS (reprovação automática)
### 2.1 SOMBRA DE CONTATO — nada flutua
```css
.subject::after{content:"";position:absolute;left:8%;right:8%;bottom:-4%;height:9%;
  background:radial-gradient(closest-side, rgba(0,0,0,.62), transparent 78%);
  filter:blur(10px);z-index:1;}
```
### 2.2 COERÊNCIA DE LUZ — sujeito conversa com o fundo (color match + light wrap)
```css
.subject>img{filter:brightness(.96) contrast(1.06) saturate(1.04)
  drop-shadow(0 0 1px rgba(0,0,0,.35)) drop-shadow(0 0 14px var(--accent)40);}
```
### 2.3 PROFUNDIDADE EM 3 CAMADAS — por BLUR, nunca por opacity
- L1 fundo: `filter:blur(12-16px)` + vinheta radial. Proibido gradient chapado / opacity.
- L2 sujeito: nítido, iluminado, com sombra de contato.
- L3 grafismo: cards/CTA com `box-shadow` PROJETADA.
```css
.depth-bg{position:absolute;inset:0;background-size:cover;
  filter:blur(14px) brightness(.55) saturate(1.05);transform:scale(1.08);}
.depth-bg::after{content:"";position:absolute;inset:0;
  background:radial-gradient(120% 90% at 50% 42%, transparent 38%, rgba(0,0,0,.55));}
```
### 2.4 GRÃO / TEXTURA — proibido fundo perfeitamente liso
```css
.grain{position:absolute;inset:0;z-index:50;pointer-events:none;opacity:.07;
  mix-blend-mode:overlay;
  background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='120' height='120'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>");
  background-size:180px 180px;}
```
Adicione `<div class="grain"></div>` como ÚLTIMO filho de cada `.slide`.
### 2.5 BORDAS TRATADAS — sem recorte de tesoura
Feather + light wrap (vide 2.2). Nunca borda dura/serrilhada/halo. Asset sujo → peça novo.

## 3. IDENTIDADE NUC (preservar — é o trunfo)
- Tema: dark editorial noturno. Fundos #06–0E (quase preto azulado), não preto puro.
- Accent: ciano `#1EC5F2` (hex oficial, alinhado ao design_system). Em kicker, highlight box, light wrap.
- Tipografia: condensada PESADA, CAIXA-ALTA, nas headlines. Hierarquia: kicker fino ciano →
  headline branca massiva → corpo cinza.
- Highlight box: fundo ciano + texto escuro, em UMA palavra-chave por slide.
Não troque o sistema tipográfico — ele é superior ao da concorrência.

## 4. COMPOSIÇÃO (saia do empilhamento central simétrico)
- Integração tipo↔imagem: título OCLUI parte do sujeito (z-index intercalado). Proibido
  título preso em retângulo flutuante isolado da cena.
- Assimetria: quebre a simetria em ≥1 eixo (diagonal, sobreposição, sangria pra fora).
- Profundidade de cards: ao empilhar fotos/cards, gire (`rotate(-2deg)`) e sobreponha com sombra.
- Fluxo: preserve cima→baixo (kicker → headline → corpo → CTA).

## 5. TIPOGRAFIA E COPY
- Contraste mínimo AA (4.5:1) em todo texto-chave. PROIBIDO preto-sobre-preto. De-ênfase ≥40%.
- Revisão de copy obrigatória: concordância, ortografia, idioma único. "TODO SEMANA" ou
  "ABSOLUTE DECEPÇÃO" reprovam a peça.
- CTA com presença: fill sólido + glow OU sombra. Nunca cinza apagado.

## 6. PROVA E HONESTIDADE
- Dado/case/manchete → ancore com ativo visual coerente (print/selo/gráfico).
- NUNCA apresente produto/manchete/dado fabricado como factual. Sem ativo verificável →
  trate como conceitual/opinativo, não como notícia.
- NUNCA recolora lataria "na unha" pra fingir outro produto (reflexo incoerente = tell de IA).

## 7. ANTI-PADRÕES PROIBIDOS
- ❌ Carro/pessoa flutuando sem sombra de contato.
- ❌ Fundo gradient chapado sem textura/blur/vinheta.
- ❌ Recorte de estúdio colado em fundo difuso (sem color match).
- ❌ Fundo perfeitamente liso, sem grão.
- ❌ Profundidade por opacity em vez de blur.
- ❌ Título em retângulo de UI isolado, sem oclusão.
- ❌ Cards no mesmo plano Z (só borda em glow, sem sombra projetada).
- ❌ Layout 100% simétrico/centralizado/estático.
- ❌ Texto de baixo contraste / preto-sobre-preto.
- ❌ Erro de português ou mistura de idiomas.
- ❌ Fontes genéricas (Inter, Roboto, Arial, system). Use a condensada da marca.
- ❌ Carrossel virar lista de slides de texto sem âncora visual (ver "Âncora visual obrigatória").

## 8. CHECKLIST DE QA VISUAL — antes de exportar cada slide
- [ ] Slide tem âncora visual (não é texto puro, salvo insight/CTA)?
- [ ] Todo recorte tem sombra de contato?
- [ ] Luz do sujeito bate com o fundo (color match + light wrap)?
- [ ] Fundo com profundidade por BLUR + vinheta (não opacity/gradient chapado)?
- [ ] Camada `.grain` cobrindo a peça inteira?
- [ ] Bordas do recorte tratadas (sem halo/serrilha)?
- [ ] Cards/CTA com sombra PROJETADA?
- [ ] Título ocluído/integrado à imagem?
- [ ] Composição com assimetria/diagonal?
- [ ] Texto-chave ≥ AA, nenhum preto-sobre-preto?
- [ ] Copy revisada (ortografia, concordância, idioma único)?
- [ ] CTA com presença forte?

## 9. FLUXO DE TRABALHO
1. Rode a SEÇÃO 0: defina arco, papéis, loops e o teste de remoção. NÃO desenhe antes.
2. Leia os assets em `/fotos`. Importe `nuc_realism` se existir.
3. Por slide: fundo (L1) → recorte ancorado (L2) → tipo+grafismo (L3) → grão.
4. Rode o QA narrativo (Seção 0) e o QA visual (Seção 8).
5. Exporte via Playwright. Entregue os PNG 1080x1350.
6. Se um asset impedir o padrão (recorte sujo, baixa resolução), avise e peça o correto.
