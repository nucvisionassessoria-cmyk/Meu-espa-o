---
name: oportunista-trend
description: >
  Radar oportunista semanal sobre o perfil @v4company. Lê o dataset de um
  schedule semanal Apify (actor `apify/instagram-scraper`) que coleta os
  posts públicos do V4 com imagem, caption, likes e comentários. Detecta a
  publicação da semana de maior potencial via sinais públicos
  (commentsCount/likesCount, volume de comentários reais, view count em
  reels) e a transforma em post NUC usando UM DE DOIS MODOS: (1) MODO HYPE —
  quando o V4 está surfando um evento cultural forte (Copa do Mundo,
  Olimpíada, eleição, Carnaval, premiação), esta skill "rouba como artista"
  os códigos visuais do evento (palette, figuras, vocabulário de torcida)
  pra NUC pegar o mesmo rebote de hype; (2) MODO TREND — pra qualquer
  publicação não-evento, copia só a ESTRUTURA narrativa e devolve com
  identidade visual NUC integral. Em qualquer modo, a produção visual final
  é delegada à `nuc-carrossel`. Windsor.ai é usado só pro lado NUC
  (tracking pós-publicação). Use quando o usuário pedir "oportunista da
  semana", "artes trends da semana", "analisa o V4", "roubar estrutura/visual
  do V4". Cadência sugerida: 1x/semana. Setup único em SETUP-APIFY.md.
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

## FONTES DE DADOS — DOIS LADOS, DUAS FONTES

### Lado V4 (peer/concorrente) — APIFY
O Instagram (via Meta Graph API) só devolve métricas das contas que
autorizaram o app. `@v4company` não autorizou e nunca vai autorizar —
Windsor não enxerga isso. A fonte certa pro lado V4 é um scraper público:

**Actor:** `apify/instagram-scraper` (rodando em schedule semanal).
**Setup do usuário:** ver `SETUP-APIFY.md`.

**Variáveis de ambiente esperadas no runtime:**
- `APIFY_TOKEN` — token de API read-only da conta Apify.
- `APIFY_V4_DATASET_ID` — ID do dataset onde o schedule semanal grava
  os resultados (também aceita `APIFY_V4_ACTOR_ID` pra pegar o último run).

**Chamada que a skill faz:**
```
GET https://api.apify.com/v2/datasets/${APIFY_V4_DATASET_ID}/items
    ?token=${APIFY_TOKEN}&clean=true&format=json
```
Devolve JSON com (campos por item, conforme actor):
`url` (permalink), `timestamp`, `caption`, `likesCount`, `commentsCount`,
`type` (Image/Video/Sidecar), `displayUrl` (imagem principal),
`videoUrl` (se reel), `videoViewCount`, `images[]` (carrossel),
`ownerUsername`.

**O que NÃO vem (limitação pública):** `saves`, `shares`, `reach`,
`watch_time`. Isso é dado privado do dono — nenhum scraper público pega.
Pra ranking, a skill usa só os sinais visíveis:
1. `commentsCount / likesCount` → taxa de discussão (proxy para
   saves+shares, que normalmente correlaciona).
2. `likesCount` absoluto → atenção bruta.
3. (Reels) `videoViewCount` → reach proxy.

Se em algum momento o V4 expor mais sinais (BFF público, embed widget),
a skill incorpora — mas hoje é esse o teto.

### Lado NUC (own/casa) — WINDSOR.AI
Pro tracking de como o post adaptado performa DEPOIS de publicado, e pra
calibrar a skill ao longo do tempo (entender o que funciona pra NUC), a
fonte é Windsor.

Conector: `instagram` (organic), conta `nucvision` (id `17841477107725223`).

Tools MCP usadas:
1. `mcp__Windsor_ai__get_data` — puxa as métricas reais (`media_saved`,
   `media_shares`, `media_reach`, `media_reel_avg_watch_time`) dos
   carrosséis NUC publicados via esta skill.
2. Compara performance NUC pós-publicação vs. o post-fonte V4 — ratio
   de eco. Isso vira aprendizado pra próxima semana.

Esse loop de calibração é OPCIONAL no primeiro mês (sem dado histórico
ainda). A partir do segundo mês a skill começa a usar isso pra refinar
escolhas.

---

## PROTOCOLO SEMANAL — 4 ETAPAS

### ETAPA 1 — COLETA
Lê o dataset Apify do schedule semanal (chamada documentada acima em
"Lado V4 — APIFY"). Filtra `timestamp` nos últimos 7 dias. Mantém
`url`, `timestamp`, `caption`, `likesCount`, `commentsCount`, `type`,
`displayUrl`, `videoUrl`, `videoViewCount`.

Pra cada item, baixa a imagem (`displayUrl`) localmente em
`scratchpad/v4-week/` pra inspeção visual posterior (palette, figura,
mode classification).

### ETAPA 2 — RANKING + CLASSIFICAÇÃO DE MODO
Score = PERFORMANCE (sinais públicos) × ALINHAMENTO (avaliação textual).

**Performance — sinais públicos disponíveis, em ordem de força:**
1. `commentsCount / likesCount` → taxa de discussão (proxy de saves+shares).
2. `likesCount` absoluto → atenção bruta.
3. Reels: `videoViewCount` → reach proxy.
4. Volume de comentários >150 com 2+ palavras → discussão real (não bot).

**Por que não usamos saves/shares/reach:** Meta não expõe esses dados
publicamente. Nenhum scraper pega. A skill assume essa cegueira e
compensa com o sinal de comentários, que historicamente correlaciona.

**Alinhamento NUC (0–10):** legenda + tema vs ICP NUC (empresário/PME,
dono de serviço, gestor — comercial, funil, posicionamento, autoridade).
Conteúdo interno V4 (cultura, vaga, recado institucional, dicas pra
começar agência) tem alinhamento baixo mesmo que tenha bombado.

**Vencedora:** melhor combinação com alinhamento ≥ 6. Empate técnico →
`commentsCount` decide.

**Classificação de MODO da vencedora** (HYPE ou TREND) com inspeção
visual da imagem baixada em `scratchpad/v4-week/`.

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
4. **Dados sempre do Apify dataset configurado.** Sem invenção de métrica,
   sem completar com memória/treino. Se o dataset não estiver disponível
   (token inválido, schedule falhou, dataset vazio) → reporta o erro
   específico e pede ao usuário pra checar a Apify, ou aceita print no
   chat como fallback manual.
5. **Modo HYPE só dispara com inspeção visual da peça V4** (imagem baixada
   via `displayUrl` em `scratchpad/v4-week/`). Sem ver a imagem, default
   = MODO TREND. Hype mal classificado vira post fora de janela e parece
   desespero.
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
