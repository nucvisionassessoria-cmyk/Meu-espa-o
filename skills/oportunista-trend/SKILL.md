---
name: oportunista-trend
description: >
  Radar oportunista semanal sobre o perfil @v4company (Instagram). Puxa as
  publicações dos últimos 7 dias via Windsor.ai, ranqueia por sinais reais de
  retenção e propagação (saves+shares, comentários/alcance, watch_time),
  escolhe UMA publicação alinhada ao posicionamento NUC Vision, faz a
  engenharia reversa da estrutura e produz uma versão ADAPTADA — nunca copiada
  — para a NUC. A produção visual final é delegada à skill `nuc-carrossel`
  (engata, não duplica). Use quando o usuário pedir "oportunista da semana",
  "analisa o V4", "roubar estrutura do V4", "trend semanal V4", "o que rodou
  no V4 essa semana" ou variações. Cadência sugerida: 1x/semana (segunda).
---

# SKILL: OPORTUNISTA-TREND — V4 → NUC EM 4 ETAPAS

## POSICIONAMENTO (o que esta skill É e o que NÃO é)

**É:** um radar focado em UM concorrente/referência (@v4company), com dados
quantitativos do Windsor.ai, que devolve um carrossel NUC com estrutura
inspirada na publicação V4 que mais performou na semana e tem ângulo
adaptável ao ICP NUC.

**NÃO é:**
- A `radar-trends-nuc` (essa varre web/Twitter/Google Trends e roda em
  saudações como "oi"). Esta aqui ignora trends gerais.
- Um copiador de texto. Nunca reproduz frase literal do V4.
- Um gerador de visual. A produção visual é da `nuc-carrossel`.

**Engate obrigatório:** quando o roteiro adaptado estiver pronto, esta skill
invoca a `nuc-carrossel` passando o roteiro completo (arco + papéis + loops).
Todas as regras visuais, anti-cara-de-IA, profundidade, grão, light wrap,
âncora visual, padrão campanha — vêm de lá. Não duplicar nada.

---

## FONTE DE DADOS — WINDSOR.AI (única)

Conector: **Instagram (organic)** do Windsor.ai, filtrado para o perfil
`@v4company`.

Tools MCP usadas (nesta ordem):
1. `mcp__Windsor_ai__get_connectors` — confirma que o connector instagram
   está conectado E que `@v4company` está autorizado nessa conta.
2. `mcp__Windsor_ai__get_fields` — descobre os campos disponíveis para o
   connector instagram.
3. `mcp__Windsor_ai__get_data` — puxa as publicações dos últimos 7 dias.

Campos mínimos requeridos (se faltar algum, reportar e seguir com os que tem):
`date`, `permalink`, `media_type` (carrossel/reels/feed), `caption`,
`reach` (alcance), `likes`, `comments`, `saves` (salvamentos),
`shares` (compartilhamentos), `views`, `avg_watch_time` (apenas reels).

### Edge case — V4 não autorizado no Windsor da conta
Se `get_connectors` mostrar instagram conectado MAS sem `@v4company`, OU se
`get_data` voltar vazio para o handle, parar de cara e perguntar ao usuário:

> "O perfil @v4company não está autorizado neste Windsor. Você quer:
> (a) autorizar agora (eu te passo o URL do `get_connector_authorization_url`), ou
> (b) seguir só com métricas públicas (likes + comentários) com a nota de
> limitação no relatório?"

Não inventar dados. Não usar memória/treino para preencher métricas.

---

## PROTOCOLO SEMANAL — 4 ETAPAS

### ETAPA 1 — COLETA
Puxa do Windsor TODAS as publicações de `@v4company` nos últimos 7 dias
(janela móvel a partir da data de hoje). Mantém um único dataset com todos
os campos acima por publicação.

### ETAPA 2 — RANKING DE OPORTUNIDADE
Score = combinação de PERFORMANCE (Windsor) × ALINHAMENTO (avaliação textual).

**Performance (sinais Windsor, ordem de força):**
1. `(saves + shares) / reach` → sinal mais forte de valor real percebido.
2. `comments / reach` → taxa de discussão/polêmica produtiva.
3. Para reels: `avg_watch_time / video_length` (taxa de retenção).
4. `likes / reach` → sinal mais fraco; tiebreaker apenas.

**Alinhamento NUC (avaliação textual, 0–10):**
Lê a legenda + tema da publicação e avalia se conecta com o ICP NUC
(empresário/PME, dono de serviço, gestor que precisa estruturar comercial,
funil, posicionamento, autoridade, crescimento sustentável). Conteúdo
puramente interno V4 (cultura, comunicado, dicas para iniciar agência) tem
alinhamento baixo, mesmo que tenha bombado.

**Vencedora:** melhor combinação entre performance e alinhamento ≥ 6.
Empate técnico → escolhe o de maior `saves+shares`. Documenta o ranking
inteiro (não só a escolhida) para o usuário poder discordar.

### ETAPA 3 — ENGENHARIA REVERSA
Para a publicação vencedora, documenta em texto curto:

- **Gancho** (slide 1 / 1ª frase) — palavra a palavra, como referência.
- **Promessa central** (o que o leitor espera receber).
- **Modelo narrativo** — qual dos 5 da `nuc-carrossel`:
  investigação / quebra de crença / história / explicação progressiva / polêmica.
- **Beats** — slide por slide: papel (gancho/curiosidade/escalada/virada/
  revelação/insight/CTA) + 1 frase resumindo a entrega de cada um.
- **Pontes** — que tipo de loop aberto liga cada slide ao próximo
  (pergunta não respondida / informação incompleta / contradição plantada /
  promessa de payoff / tensão temporal — vocabulário da `nuc-carrossel`).
- **Tipo de CTA** usado pelo V4.
- **Sinais Windsor que explicam a performance** — qual métrica disparou
  (alta taxa de saves? muitos comentários? alto watch_time?), e a leitura
  estratégica disso (ex: "saves altos = serviu de referência, leitor quis
  reler — isso indica densidade informacional, não polêmica").

### ETAPA 4 — ADAPTAÇÃO PARA A NUC

Reescreve TUDO mantendo a estrutura, jamais o texto:

| Mantém                              | Substitui                                |
|-------------------------------------|------------------------------------------|
| Modelo narrativo                    | Tema/exemplos do universo V4 → NUC       |
| Sequência de papéis                 | Tom V4 → tom editorial NUC               |
| Tipo de loop aberto entre slides    | Gancho equivalente em força, nunca igual |
| Força e função do CTA               | Palavra-chave do CTA = tema NUC          |

Regras de tradução:
- Gancho NUC com mesma carga emocional do V4, vocabulário diferente. Se o
  V4 usou polêmica de marca famosa, NUC usa polêmica de comportamento de
  mercado (PME, gestor, agência) — sem nomear empresa específica salvo se
  for fato público verificável.
- Cases/exemplos: do universo NUC (empresário local, prestador de serviço,
  PME que estruturou comercial). Nunca mencionar cliente V4.
- Tom: editorial direto, sem em-dash, sem "aqui na NUC fazemos X" no meio
  da narrativa — a NUC só assina no CTA (regra já fixada em `radar-trends-nuc`).
- CTA full-width contextual com palavra-chave do tema. Padrão "Comenta
  PALAVRA" quando o tema permite (vale também "Salva esse" ou "Manda pra
  quem precisa" se a estrutura do V4 favorecer).
- Sócio do dia: rotação fixa por dia da semana de publicação prevista:
  **Segunda = Iago**, **Quarta = Derick**, **Sexta = Lucas**. Foto vem de
  `fotos/iago_bracos_cruzados.png`, `fotos/derick_bracos_cruzados.jpg`,
  ou um cutout de `fotos/lucas_derick.jpeg` (Lucas isolado — se não houver
  asset limpo de Lucas sozinho, reportar e pedir).

### Hand-off para a `nuc-carrossel`
Quando o roteiro adaptado estiver fechado, entregar para a `nuc-carrossel`:
- Arco completo (Etapa A da SEÇÃO 0 dela).
- Papéis por slide (Etapa B).
- Pontes/loops por transição (Etapa C).
- Teste de remoção OK (Etapa D).
- Legenda Instagram pronta (texto editorial + CTA + assinatura @nucvision).
- Sócio do dia identificado.

A `nuc-carrossel` assume daí em diante (produção visual + QA + export PNG).

---

## REGRAS INVIOLÁVEIS

1. **Nunca copia texto literal do V4.** Estrutura, ângulo e lógica narrativa
   são livres; frase, palavra-chave, slogan — não. Se um trecho vier
   parecido demais, reescrever do zero.
2. **Se NENHUMA publicação V4 da semana conectar com o ICP NUC** (ex:
   conteúdo puramente interno de cultura V4, dicas para começar agência,
   comunicado institucional sem leitura de mercado, vaga, anúncio) →
   reportar "sem oportunidade clara essa semana" e ENCERRAR. Não forçar
   adaptação só pra cumprir cadência — produzir lixo enfraquece o feed.
3. **Dados sempre do Windsor.** É proibido inventar métrica, completar com
   memória ou estimativa de treino. Sem Windsor → sem ranking → reportar.
4. **NUC só aparece no CTA** (regra herdada da `radar-trends-nuc`). Nada de
   "aqui na NUC fazemos" no meio da narrativa.
5. **Produção visual é da `nuc-carrossel`.** Esta skill não desenha slide,
   não escolhe paleta, não escreve CSS. Entrega roteiro estruturado e
   delega.
6. **Documenta o ranking inteiro**, não só a escolhida. O usuário precisa
   poder discordar da escolha e pedir a segunda colocada.

---

## SAÍDA PADRÃO (o que esta skill devolve ANTES de chamar a nuc-carrossel)

Um único relatório em texto, nesta ordem:

1. **Ranking semanal** — tabela com data, formato, métricas-chave Windsor,
   nota de alinhamento NUC, e a vencedora marcada.
2. **Publicação escolhida** — link + por que ela.
3. **Engenharia reversa** — gancho original, promessa, modelo, beats,
   pontes, CTA, leitura dos sinais Windsor.
4. **Roteiro NUC adaptado** — arco completo, slide a slide, com loops
   abertos explícitos, legenda e CTA prontos, sócio do dia indicado.
5. **Pergunta de confirmação:** "Mando para a `nuc-carrossel` produzir os
   PNGs ou quer ajustar o roteiro antes?"

Só chama a `nuc-carrossel` depois do "vai".
