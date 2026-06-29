---
name: oportunista-trend
description: >
  Radar oportunista semanal sobre o perfil @v4company. Detecta a publicação
  da semana de maior potencial via Windsor.ai (Instagram organic — saves+shares,
  comentários/alcance, watch_time) e a transforma em post NUC usando UM DE
  DOIS MODOS: (1) MODO HYPE — quando o V4 está surfando um evento cultural
  forte (Copa do Mundo, eleição, Oscar, Carnaval, lançamento esportivo etc.),
  esta skill "rouba como artista" os códigos visuais do evento (palette do
  evento, atletas/figuras, vocabulário de torcida) para a NUC pegar o mesmo
  rebote de hype; (2) MODO TREND — para qualquer publicação não-evento, copia
  só a ESTRUTURA narrativa e devolve com identidade visual NUC integralmente
  preservada. Em qualquer modo, a produção visual final é delegada à skill
  `nuc-carrossel`. Use quando o usuário pedir "oportunista da semana",
  "analisa o V4", "roubar estrutura/visual do V4", "trend semanal V4",
  "o que rodou no V4 essa semana". Cadência sugerida: 1x/semana.
---

# SKILL: OPORTUNISTA-TREND — V4 → NUC (HYPE OU TREND)

## POSICIONAMENTO

**É:** um radar dedicado a UM concorrente/referência (`@v4company`), que
identifica qual publicação da semana vale ser canibalizada, decide em qual
modo canibalizar (HYPE ou TREND) e devolve um roteiro pronto para a
`nuc-carrossel` produzir.

**NÃO é:**
- A `radar-trends-nuc` (essa varre web/Twitter/Google Trends, roda em
  saudações). Esta foca em UM perfil só.
- Um copiador de texto. Estrutura e códigos visuais são livres — frase,
  palavra-chave e slogan são proibidos de cópia literal.
- Um gerador de visual. Quem desenha é a `nuc-carrossel`.

---

## OS DOIS MODOS — A DECISÃO MAIS IMPORTANTE DA SKILL

A primeira pergunta antes de adaptar qualquer publicação é:

> "O V4 está surfando um EVENTO CULTURAL com códigos visuais próprios, ou
> está fazendo conteúdo de mercado/negócio padrão?"

A resposta define todo o resto.

### MODO 1 — HYPE / ROUBAR COMO ARTISTA
**Quando:** a publicação V4 está montada sobre um evento cultural forte com
gramática visual reconhecível: Copa do Mundo, Olimpíada, eleição,
Carnaval, Oscar/Grammy, lançamento esportivo grande (F1, NBA Finals),
morte/aposentadoria de figura pública, BBB final etc.

**Sinais de que é HYPE:**
- Paleta do post foge da paleta-padrão V4 (cores nacionais, cores de uniforme,
  preto-e-dourado de premiação etc.).
- Sujeito é um atleta, artista, político ou personagem público — não um
  dirigente V4 ou conceito abstrato.
- Vocabulário tem palavras de torcida/celebração ("é hexa", "vai Brasil",
  "tomou", "ganhou" usados literalmente, não como metáfora).
- Timing: publicado em janela de pico do evento (semana do jogo, dia do
  voto, noite da premiação).

**Comportamento neste modo — ROUBAR COMO ARTISTA:**

1. **Palette do evento, NÃO palette NUC.** Override explícito.
   Copa Brasil = `#009C3B` verde · `#FFDF00` amarelo · `#002776` azul ·
   `#FFFFFF` branco. Olimpíada = palette do anel. Eleição = vermelho/azul/
   neutro institucional. Etc. A palette padrão NUC (`#06–0E` dark + ciano
   `#1EC5F2`) entra em pausa. Só o LOGO NUC e o CTA podem manter cor
   institucional — o resto do slide veste o evento.

2. **Figura central do evento.** Se o V4 usou um atleta/figura, a NUC USA
   um atleta/figura COMPARÁVEL (mesmo esporte, mesma natureza pública),
   nunca a mesma pessoa que o V4 — distinção visual é o que evita o
   "copiou descaradamente". Reporta ao usuário qual figura V4 usou e
   propõe 2–3 alternativas para a NUC.

3. **Vocabulário de torcida adaptado.** Mesmo registro emocional (euforia,
   tensão, celebração), palavras diferentes. Se V4 escreveu "PODE COMEMORAR",
   NUC escreve algo como "DEU CERTO" ou "É AGORA" — mesma carga, palavras
   distintas.

4. **Sócio do dia OPCIONAL neste modo.** Se a figura do evento já é o
   protagonista visual, o sócio fica fora ou aparece pequeno em um slide de
   transição. Forçar Iago/Derick/Lucas no meio de uma campanha de Copa
   enfraquece o hype. Em HYPE, a regra de rotação semanal (Seg/Qua/Sex) é
   suspensa salvo pedido explícito do usuário.

5. **NUC entra só no CTA + assinatura.** Igual ao MODO TREND. A presença
   da NUC vem da consistência do CTA e do logo, não da palette.

### MODO 2 — TREND PADRÃO
**Quando:** a publicação V4 é sobre marketing, vendas, gestão, polêmica
corporativa, comportamento de mercado, dado, comparativo — tudo que
não seja um evento cultural específico com códigos visuais próprios.

**Comportamento neste modo:**
- Copia SÓ a estrutura narrativa (arco, papéis, pontes, tipo de CTA).
- Identidade visual é 100% NUC: palette dark `#06–0E` + ciano `#1EC5F2`,
  Space Grotesk/Anton, sócio do dia conforme rotação (Seg=Iago, Qua=Derick,
  Sex=Lucas), regras da `nuc-carrossel` integrais.
- Cases/exemplos do universo NUC (PME, prestador de serviço, gestor).

### Quando estiver em dúvida
**Default = MODO TREND.** O risco de errar para hype (copiar visual demais
e parecer mau gosto) é maior que o risco de errar para trend (perder um
pouco do rebote do hype). Em caso de dúvida, reportar a decisão ao usuário
antes de adaptar.

---

## FONTE DE DADOS — WINDSOR.AI

Conector: **Instagram (organic)** do Windsor.ai, filtrado para `@v4company`.

Tools MCP usadas (nesta ordem):
1. `mcp__Windsor_ai__get_connectors` — confirma instagram conectado E
   `@v4company` autorizado nessa conta.
2. `mcp__Windsor_ai__get_fields` — descobre os campos disponíveis.
3. `mcp__Windsor_ai__get_data` — puxa publicações dos últimos 7 dias.

Campos mínimos (se faltar algum, reportar e seguir com o que tem):
`date`, `permalink`, `media_type` (carrossel/reels/feed), `caption`,
`reach`, `likes`, `comments`, `saves`, `shares`, `views`, `avg_watch_time`
(reels), **`media_url` ou `thumbnail_url`** (essencial para extrair os
códigos visuais do MODO HYPE).

### Por que `media_url` é crítico
Sem ver a imagem do post V4, é impossível decidir entre HYPE e TREND com
confiança e impossível extrair palette/figura. Se o Windsor não devolver
`media_url`, a skill ABRE o `permalink` (Instagram público) e inspeciona
o thumbnail antes de classificar o modo. Sem nenhuma visão visual da peça
→ marca como MODO TREND por segurança e avisa "modo decidido sem inspeção
visual — confirme antes de produzir".

### Edge case — V4 não autorizado no Windsor da conta
Se `get_connectors` mostrar instagram conectado mas sem `@v4company`, ou
`get_data` voltar vazio → parar e perguntar:

> "@v4company não está autorizado neste Windsor. Você quer:
> (a) autorizar agora — eu gero a URL via `get_connector_authorization_url`;
> (b) seguir só com sinais públicos (alcance estimado por likes+comentários
> visíveis no permalink) — relatório com nota de limitação?"

Nunca inventar métrica. Nunca completar com memória/treino.

---

## PROTOCOLO SEMANAL — 4 ETAPAS

### ETAPA 1 — COLETA
Puxa todas as publicações de `@v4company` nos últimos 7 dias (janela móvel
a partir de hoje). Mantém todos os campos por publicação.

### ETAPA 2 — RANKING + CLASSIFICAÇÃO DE MODO
Score = PERFORMANCE (Windsor) × ALINHAMENTO (avaliação textual).

**Performance, em ordem de força:**
1. `(saves + shares) / reach` — valor real percebido.
2. `comments / reach` — taxa de discussão.
3. Reels: `avg_watch_time / video_length` — retenção.
4. `likes / reach` — tiebreaker apenas.

**Alinhamento NUC (0–10):** legenda + tema vs ICP NUC (empresário/PME,
dono de serviço, gestor — comercial, funil, posicionamento, autoridade).
Conteúdo interno V4 (cultura, vaga, recado institucional, dicas para
começar agência) tem alinhamento baixo mesmo que tenha bombado.

**Vencedora:** melhor combinação com alinhamento ≥ 6. Empate técnico →
`saves+shares` decide.

**Classificação de MODO da vencedora** (HYPE ou TREND) usando a lista de
sinais acima, com inspeção visual da `media_url`.

Documenta o ranking inteiro + a classificação de modo (não só a escolhida).
O usuário precisa poder discordar.

### ETAPA 3 — ENGENHARIA REVERSA
Sempre documenta:

- **Gancho** (slide 1 / 1ª frase) literal.
- **Promessa central.**
- **Modelo narrativo** (1 dos 5 da `nuc-carrossel`).
- **Beats** — slide a slide, papel + 1 frase do que entrega.
- **Pontes** — tipo de loop em cada transição (vocabulário `nuc-carrossel`:
  pergunta não respondida / informação incompleta / contradição plantada /
  promessa de payoff / tensão temporal).
- **CTA** — tipo e palavra-chave.
- **Sinais Windsor que explicam a performance.**

**Se MODO HYPE, adicionar:**
- **Códigos visuais do evento extraídos** — palette (3–5 cores
  dominantes com hex), figura/atleta usado, símbolo gráfico (bandeira,
  troféu, número, slogan), vocabulário de torcida usado.
- **Janela de pico do evento** — quando a NUC ainda pega rebote (publicar
  D-1 a D+2 do pico; depois disso o hype esfria e o post vira tardio).

### ETAPA 4 — ADAPTAÇÃO
Reescreve mantendo a estrutura, nunca o texto.

| Sempre mantém                       | Sempre substitui                          |
|-------------------------------------|-------------------------------------------|
| Modelo narrativo                    | Tema/exemplo do universo V4 → NUC         |
| Sequência de papéis                 | Tom V4 → tom editorial NUC                |
| Tipo de loop aberto                 | Gancho equivalente em força, nunca igual  |
| Força e função do CTA               | Palavra-chave do CTA = tema NUC           |

**Se MODO TREND:**
- Identidade visual 100% NUC (palette dark + ciano, Space Grotesk, sócio
  do dia conforme rotação).
- Cases/exemplos do universo NUC (PME, prestador de serviço).
- CTA editorial NUC ("Comenta PALAVRA", "Salva esse", "Manda pra quem
  precisa") — palavra-chave do tema NUC.

**Se MODO HYPE:**
- **Palette override:** declara explicitamente as 3–5 cores do evento
  (com hex) que a `nuc-carrossel` deve usar nos slides, suspendendo a
  palette dark+ciano.
- **Figura do evento:** propõe 2–3 atletas/figuras COMPARÁVEIS mas
  distintos do que o V4 usou; pede ao usuário escolher ou enviar a foto
  (mesma natureza, mesma carga simbólica — não a mesma pessoa).
- **Vocabulário de torcida adaptado** — mesma euforia, palavras distintas.
- **Sócio do dia:** rotação suspensa salvo pedido explícito do usuário.
- **CTA + assinatura NUC mantêm cor institucional** (logo branco + accent
  ciano no CTA) — é o único elemento que costura o post à marca.

### Hand-off para a `nuc-carrossel`
Entregar para a `nuc-carrossel`:
- Arco completo (SEÇÃO 0 / Etapa A).
- Papéis por slide (Etapa B).
- Pontes/loops por transição (Etapa C).
- Teste de remoção OK (Etapa D).
- Legenda Instagram + CTA + assinatura @nucvision.
- **Em MODO HYPE:** bloco "PALETTE OVERRIDE" com as cores do evento + a
  instrução explícita "suspenda dark+ciano padrão neste carrossel; logo e
  CTA mantêm cor institucional". A `nuc-carrossel` honra essa override.
- **Em MODO TREND:** sócio do dia + nenhuma override.

A `nuc-carrossel` assume daí (produção, QA, export PNG).

---

## REGRAS INVIOLÁVEIS

1. **Nunca copia texto literal do V4** — estrutura, ângulo e códigos visuais
   são livres; frase, palavra-chave e slogan, não. Se um trecho ficar
   parecido demais, reescrever do zero.
2. **Nunca usa A MESMA figura/atleta que o V4 usou.** Em MODO HYPE, sempre
   uma figura comparável mas distinta. Mesma pessoa + mesma palette + mesma
   estrutura = plágio visível.
3. **Se nenhuma publicação V4 da semana conectar com ICP NUC** (conteúdo
   interno, vaga, comunicado institucional, dicas para começar agência) →
   reporta "sem oportunidade clara essa semana" e ENCERRA. Não força só
   pra cumprir cadência.
4. **Dados sempre do Windsor.** Sem invenção de métrica, sem completar com
   memória. Sem Windsor → sem ranking → reporta.
5. **Modo HYPE só dispara com inspeção visual da peça V4.** Sem ver a
   imagem, default = MODO TREND. Hype mal classificado vira post fora de
   janela e parece desespero.
6. **NUC só aparece no CTA + assinatura**, em ambos os modos. Nada de
   "aqui na NUC fazemos" no meio.
7. **Produção visual é da `nuc-carrossel`.** Esta skill não desenha slide,
   só passa o roteiro e (em HYPE) a palette override.
8. **Documenta o ranking inteiro + classificação de modo**, não só a
   escolhida. O usuário precisa poder discordar da escolha E do modo.

---

## SAÍDA PADRÃO (relatório antes de chamar a `nuc-carrossel`)

Um único relatório em texto, nesta ordem:

1. **Ranking semanal** — tabela: data, formato, métricas Windsor,
   alinhamento NUC, **modo detectado (HYPE/TREND)**, vencedora marcada.
2. **Publicação escolhida** — link + justificativa (performance + modo).
3. **Engenharia reversa** — gancho, promessa, modelo, beats, pontes, CTA,
   leitura dos sinais Windsor. **Se HYPE:** + códigos visuais extraídos +
   janela de pico.
4. **Roteiro NUC adaptado** — arco completo slide a slide, com loops
   abertos explícitos, legenda e CTA prontos. **Se HYPE:** + bloco
   PALETTE OVERRIDE + propostas de figura comparável. **Se TREND:** +
   sócio do dia.
5. **Pergunta de confirmação:** "Mando para a `nuc-carrossel` produzir os
   PNGs ou quer ajustar antes? (Se HYPE: confirme a figura escolhida.)"

Só chama a `nuc-carrossel` depois do "vai".
