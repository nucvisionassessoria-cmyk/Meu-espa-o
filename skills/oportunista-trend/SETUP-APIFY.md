# Setup Apify — status: CONFIGURADO ✓

A integração Apify deste repositório **já está configurada** automaticamente
via API. Os recursos criados na conta `nucvision` do Apify estão registrados
em `config.json`. Você não precisa criar actor, task ou schedule manualmente.

## O que já existe (não mexa)

| Recurso       | ID                  | Nome                          |
|---------------|---------------------|-------------------------------|
| Actor         | `shu8hvrXbJbY3Eb9W` | `apify/instagram-scraper`     |
| Actor Task    | `j2tmGjNuaE08d2pWa` | `v4company-weekly`            |
| Schedule      | `kIXAD0b5O93wcer8k` | `v4company-weekly-schedule`   |
| Próxima execução automática | — | toda segunda às 06:00 UTC (≈ 03:00 BRT) |

A task roda o `apify/instagram-scraper` apontado para
`https://www.instagram.com/v4company/` com limite de 30 posts dos últimos
7 dias. Cada execução gera um dataset novo — a skill busca sempre o
último run bem-sucedido da task quando precisa dos dados.

## Único passo que falta — env var APIFY_TOKEN

Pra eu conseguir ler o dataset nas próximas sessões (sem você ter que
colar o token toda vez), precisa salvar o token nas **Variáveis de
ambiente** do environment Claude Code on the web.

**Onde:** mesma tela onde você liberou o "Acesso à rede" — descer até o
campo **"Variáveis de ambiente"** e adicionar uma linha:

```
APIFY_TOKEN=apify_api_xxxxxxxxxxxx
```

(substituindo pelo token real)

**Sobre o aviso "não adicione segredos":** o aviso é para ambientes
compartilhados com outros colaboradores. Se você é o único usando este
environment (caso normal pra workspace pessoal), o risco prático é zero —
ninguém mais tem acesso. Se em algum momento você adicionar outras pessoas
no environment, rotacione o token (gere um novo no Apify e revogue o antigo).

## Como verificar que tá tudo certo

Numa sessão futura, basta pedir "**me dá as artes trends da semana**".
A skill vai:

1. Ler `APIFY_TOKEN` do ambiente.
2. Buscar o último run da task `v4company-weekly` via API.
3. Carregar os posts do dataset, baixar imagens.
4. Rodar as 4 etapas (ranking → engenharia reversa → adaptação → hand-off).
5. Entregar as artes via `nuc-carrossel`.

## Custo real

Primeira execução de teste consumiu ~$0.05 de crédito (13 segundos de
runtime). Estimativa mensal:
- 4 execuções automáticas (1 por semana) × ~$0.10 = **$0.40/mês**
- + execuções manuais que você pedir
- Total dentro do crédito gratuito de **$5/mês**

## O que fazer se algo quebrar

| Sintoma                                | Provável causa                        | Ação                                                        |
|---------------------------------------|---------------------------------------|-------------------------------------------------------------|
| Skill diz "APIFY_TOKEN não encontrado" | Env var não salvou                    | Voltar nas configs e adicionar de novo                      |
| Skill diz "task sem runs recentes"    | Schedule desligado / falhou           | Console Apify → Schedules → reativar                        |
| Dataset vem vazio                     | Instagram alterou layout do perfil    | Atualizar versão do actor; pode esperar fix da Apify        |
| Skill diz "token inválido"            | Token expirado / revogado             | Gerar token novo no Apify e atualizar env var               |

## Comandos úteis (debug manual)

```bash
# Último run da task
curl -s "https://api.apify.com/v2/actor-tasks/j2tmGjNuaE08d2pWa/runs?status=SUCCEEDED&limit=1&token=${APIFY_TOKEN}"

# Items do dataset de um run
curl -s "https://api.apify.com/v2/datasets/<datasetId>/items?token=${APIFY_TOKEN}&clean=true&format=json"

# Disparar um run agora (sem esperar segunda)
curl -s -X POST "https://api.apify.com/v2/actor-tasks/j2tmGjNuaE08d2pWa/runs?token=${APIFY_TOKEN}"
```
