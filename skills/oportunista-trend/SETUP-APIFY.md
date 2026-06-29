# Setup único — Apify scraper do @v4company

Depois desses 5 passos (~15 min), seu único trabalho semanal é abrir o chat
e pedir "me dá as artes trends da semana". O resto roda sozinho.

---

## 1. Criar conta Apify (2 min)

Vai em <https://apify.com> → **Sign up** → use o login do Google
(`nucvisionassessoria@gmail.com` mesmo). O plano gratuito dá **$5 de crédito
por mês**, o que cobre semanas inteiras de scraping do V4 com folga.

## 2. Abrir o actor `apify/instagram-scraper` (1 min)

Console Apify → **Store** → busca por "Instagram Scraper" → escolhe o
oficial **apify/instagram-scraper** (azul, com selo verificado) → **Try
for free**.

## 3. Configurar o input do actor (3 min)

Cola o JSON abaixo no campo "Input" (modo JSON):

```json
{
  "directUrls": ["https://www.instagram.com/v4company/"],
  "resultsType": "posts",
  "resultsLimit": 30,
  "addParentData": false,
  "enhanceUserSearchWithFacebookPage": false,
  "isUserReelFeedURL": false,
  "isUserTaggedFeedURL": false,
  "onlyPostsNewerThan": "7 days"
}
```

Salva. (`resultsLimit: 30` é gordura — V4 publica 5–15/semana, com 30 a
gente nunca perde nada.)

## 4. Criar o schedule semanal (4 min)

Console Apify → **Schedules** → **Create new schedule**.

- **Name:** `v4company-weekly`
- **Cron:** `0 6 * * 1` (toda segunda-feira às 6h UTC ≈ 3h Brasília)
- **Actor:** `apify/instagram-scraper`
- **Input:** mesmo JSON do passo 3
- **Storage:** cria um **dataset named** novo chamado `v4company_weekly`
  (Settings do schedule → "Save dataset as named dataset" → nome:
  `v4company_weekly`). Isso garante que o dataset não muda de ID toda semana.

Salva e ativa.

Roda **uma vez manualmente** agora (`Run schedule now`) pra ter dado já
hoje, sem esperar até segunda. Vai consumir ~$0.05 do crédito.

## 5. Pegar token e ID, salvar no ambiente (5 min)

### 5a. Gerar o token
Console Apify → canto superior direito (avatar) → **Settings** →
**Integrations** → **Personal API tokens** → **Create new token**.
- Nome: `claude-code-readonly`
- Permissões: marca apenas **Read** em Actors, Datasets, Key-value stores.
- Copia o token (formato `apify_api_...`).

### 5b. Pegar o ID do dataset
Console Apify → **Storage** → **Datasets** → clica em `v4company_weekly` →
copia o ID que aparece na URL (formato sem hífen, ~17 caracteres).

### 5c. Salvar no ambiente Claude Code on the web
Abre as configurações do seu **environment** no Claude Code on the web
(o painel onde você gerencia a conexão deste repo) → **Environment
variables** → adiciona dois:

```
APIFY_TOKEN=apify_api_xxxxxxxxxxxx
APIFY_V4_DATASET_ID=xxxxxxxxxxxxx
```

Salva. Pronto.

---

## Como vai funcionar daqui pra frente

Toda segunda 6h UTC o Apify roda sozinho, varre os últimos 7 dias do
`@v4company`, grava no dataset `v4company_weekly` (sobrescreve com o lote
novo). Quando você abrir o chat e pedir "me dá as artes trends da semana",
eu:

1. Chamo `GET https://api.apify.com/v2/datasets/${APIFY_V4_DATASET_ID}/items?token=${APIFY_TOKEN}`
2. Baixo as imagens dos posts em `scratchpad/v4-week/`.
3. Rodo as 4 etapas da skill (ranking → engenharia reversa → adaptação).
4. Decido se é MODO HYPE ou MODO TREND.
5. Passo o roteiro pra `nuc-carrossel` produzir os PNGs.
6. Te entrego as artes prontas.

## Custo esperado

- Free tier: $5/mês de crédito.
- Custo médio: ~$0.05–0.15 por execução do schedule (instagram-scraper).
- 4 execuções/mês = ~$0.20–0.60.
- Sobra crédito pra rodar manual quando quiser.

## O que fazer se o Apify falhar

Se eu chamar o dataset e vier vazio (schedule não rodou, token expirou,
actor com erro), eu te aviso na hora e ofereço o fallback manual:

> "O Apify não retornou dados. Quer me mandar 3–5 prints do feed V4 da
> semana e a gente segue assim hoje?"

## Renovação do token

Tokens Apify não expiram, mas podem ser revogados manualmente. Se um dia
parar de funcionar, repete o passo 5a e atualiza o env var.
