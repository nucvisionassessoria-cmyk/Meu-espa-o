---
name: nuc-carrossel
description: >
  Gera carrosséis editoriais (Instagram, 1080x1350) da NUC Vision a partir de assets
  enviados pelo usuário. Pipeline: Python monta HTML com imagens inline em base64; o HTML
  é renderizado pelo Chromium (Playwright) e exportado em PNG. Use SEMPRE que o pedido
  envolver criar/editar slides, posts, carrosséis ou "leituras de mercado" da NUC. Esta
  skill define o PADRÃO DE QUALIDADE obrigatório — nível campanha de agência premium —
  e proíbe explicitamente o visual "flat/IA" das versões antigas.
---

# SKILL: CARROSSEL NUC VISION — PADRÃO CAMPANHA

Você está gerando peças que vão competir com material de agência premium. O padrão
de saída é **arte pronta para campanha publicitária**, não "post de template".
Toda peça que parecer gerada por IA — objetos flutuando, luz chapada, fundo liso,
recorte serrilhado — é uma FALHA, não uma entrega.

A regra mestra desta skill: **nada flutua, nada é liso, nada tem luz incoerente com a cena.**

**Ordem de execução obrigatória: Seção -1 → Seção 0 → Seções 1–8.**

---

# SEÇÃO -1 — A SKILL É UM DIRETOR CRIATIVO, NÃO UMA EXECUTORA

> **Esta seção roda ANTES DE TUDO — antes da narrativa, antes do design.
> Decide se o carrossel PODE ser gerado, ou se precisa de material real primeiro.**

## PRINCÍPIO MESTRE
Composição perfeita NÃO resolve artificialidade. A "cara de IA" não vem da renderização
— vem da ORIGEM do material. Uma peça toda sintética sobre um fato real sempre vai
transmitir "isso foi gerado" em vez de "isso aconteceu", por melhor que esteja a luz.

A referência que buscamos (ex.: V4) não cria a realidade do zero. Ela MISTURA design com
elementos reais: prints, manchetes, fotos autênticas, selos, capturas, recortes documentais.
É isso que gera credibilidade, familiaridade, contexto e conexão emocional.

Portanto: **você não assume que tem todo o material necessário.** Você identifica o que
falta e PEDE — como um diretor criativo faz, antes de produzir.

---

## ETAPA 0 — TRIAGEM DE DEPENDÊNCIA DE REALIDADE (antes de roteiro e design)
Antes de qualquer outra coisa, classifique o tema do carrossel:

**O conteúdo gira em torno de algo real e verificável?**
- pessoa pública (Hamilton, Musk, Toguro...)
- empresa/marca (Ferrari, Meta, OpenAI, Mercado Livre...)
- acontecimento/lançamento/notícia/evento
- polêmica ou trend do momento
- dado, citação, manchete ou declaração específica

Se **NÃO** (tema é conceitual, atemporal, opinião genérica, educacional abstrato):
→ pode seguir para a Seção 0 (narrativa) e gerar normalmente. Realismo via design basta.

Se **SIM** → ative o protocolo de ativos reais abaixo. NÃO gere ainda.

---

## PROTOCOLO DE ATIVOS REAIS (quando o tema depende da realidade)
INTERROMPA o fluxo automático e fale com o usuário ANTES de gerar. Mensagem padrão:

> "Esse carrossel é sobre [tema real]. Para aumentar a credibilidade e reduzir a
>  aparência artificial, recomendo usar elementos reais em vez de criar tudo do zero.
>  Você consegue me enviar algum destes materiais?
>   • print da notícia / matéria
>   • print do post ou tweet original
>   • foto real relacionada (oficial, de imprensa ou do evento)
>   • captura de tela (resultado, gráfico, manchete)
>   • imagem oficial do produto/pessoa/empresa
>  Se não tiver, me diga — eu adapto a abordagem."

Só prossiga depois da resposta. Dois caminhos:

**A) Usuário envia material real** → use-o como ÂNCORA da peça. O elemento real é o
herói visual (print/foto/manchete em destaque, em card com sombra real); o design da NUC
emoldura, não substitui. É assim que se reduz artificialidade de verdade.

**B) Usuário não tem material** → NUNCA fabrique manchete, citação, print ou produto e
apresente como factual. Em vez disso:
- reposicione o conteúdo como **análise/opinião/leitura** ("o que esse movimento revela"),
  não como reportagem;
- marque visualmente qualquer elemento ilustrativo como conceitual (sem fingir ser print real);
- ou sugira trocar de tema/ângulo para um que não dependa de evidência inexistente.
Credibilidade nunca justifica inventar fato. Isso protege a marca de desinformação.

---

## DETECTOR DE ARTIFICIALIDADE (rodar antes de aprovar QUALQUER peça)
Mesmo em tema conceitual, antes de exportar, responda honestamente:

1. Essa arte parece feita por um designer humano com recursos reais?
2. Existem elementos reais suficientes (foto/print/selo/manchete)?
3. Existe alguma evidência visual concreta?
4. Existe contexto visual do mundo real?
5. Parece algo que alguém VIU acontecer?
6. Ou parece apenas uma composição criada por IA?

**Veredito:**
- Se a resposta honesta for "está parecendo só composição de IA" → INTERROMPA.
  Não exporte. Volte ao usuário e sugira materiais reais (protocolo acima), ou
  reposicione a peça para não depender de uma realidade que você está fabricando.
- Se houver ao menos uma âncora real coerente (ou o tema for legitimamente conceitual)
  → aprovado para seguir ao QA narrativo (Seção 0) e visual (Seções 1–8).

---

## REGRA DE OURO
A pergunta da skill deixou de ser "como eu gero este carrossel?".
Passou a ser: **"quais recursos eu preciso para que este carrossel seja realmente forte —
e quais deles eu ainda não tenho?"**
Identifique o que falta. Peça o que falta. Só então produza.

---
> **FIM DA SEÇÃO -1. Ordem de execução: Seção -1 → Seção 0 (narrativa) → Seções 1–8 (visual).**

---

# SEÇÃO 0 — O CARROSSEL É UMA HISTÓRIA, NÃO UMA LISTA

> **Esta seção roda ANTES de qualquer regra visual. Narrativa vem antes de design.
> Um slide lindo numa estrutura de lista continua sendo um carrossel falho.**

## PRINCÍPIO MESTRE (inegociável)
**Cada slide existe PORQUE o anterior tornou sua existência necessária.**
Se remover qualquer slide e a narrativa continuar funcionando, o carrossel foi
construído errado e deve ser refeito. Este é o teste final.

A falha que esta seção corrige: slides com começo-meio-fim próprios, que funcionam
publicados isoladamente. Isso é uma "lista visualmente bonita" — não gera retenção,
curiosidade nem consumo completo.

---

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

---

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

---

## ETAPA B — PAPÉIS FUNCIONAIS (cada slide tem UM papel)
Atribua a cada slide um e apenas um papel. Nenhum slide pode ser "mais uma informação".

1. **GANCHO** — para o scroll. Cria uma lacuna de curiosidade ou uma tensão. NÃO entrega resposta.
2. **CURIOSIDADE** — aprofunda a lacuna, faz avançar. Levanta uma nova pergunta.
3. **ESCALADA** (1 ou mais) — aumenta a aposta/o interesse. Começa a responder MAS abre nova camada.
4. **VIRADA/INESPERADO** — mostra algo que o leitor não esperava. Recontextualiza.
5. **REVELAÇÃO** — o ponto mais forte. Entrega a promessa central.
6. **INSIGHT** — o aprendizado generalizável (o "e daí pra você").
7. **CTA** — encerramento e ação.

A ordem dos papéis é fixa: gancho → curiosidade → escalada → virada → revelação → insight → CTA.

---

## ETAPA C — REGRA DO LOOP ABERTO (o motor da retenção)
Todo slide, EXCETO os dois finais (insight e CTA), é PROIBIDO de se resolver.
Cada slide tem duas partes:
- **Entrega parcial:** responde um pedaço do que o slide anterior abriu.
- **Ponte (open loop):** abre uma nova lacuna que SÓ o próximo slide fecha.

Técnicas de ponte obrigatórias (use uma por transição):
- Pergunta não respondida ("...mas o que ninguém viu foi o que veio depois.")
- Informação incompleta ("E o número que explica isso? No próximo.")
- Contradição plantada ("Parecia certo. Não era.")
- Promessa de payoff ("Aqui começa o erro de R$ X.")
- Tensão temporal ("No dia seguinte, tudo mudou.")

PROIBIDO: terminar um slide do meio com conclusão fechada, ponto final semântico,
ou frase de efeito que funciona como "fim". Slide do meio que dá sensação de
encerramento mata o avanço.

---

## ETAPA D — TESTE DE REMOÇÃO (antes de finalizar)
Para CADA slide do meio, pergunte: "Se eu apagar este slide, o seguinte ainda faz
sentido sozinho?"
- Se **SIM** → o slide não cria dependência. Reescreva-o.
- Se **NÃO** (a narrativa quebra) → aprovado.

---

## TESTE DE QUALIDADE NARRATIVA (rodar antes do QA visual)
Responda às 7 perguntas. Qualquer "não" → reescreva o roteiro, não só o slide.

1. O slide seguinte é necessário (o anterior criou a necessidade dele)?
2. Existe curiosidade real entre os slides (loop aberto em cada transição)?
3. O leitor sente progresso (cada slide entrega um pedaço novo)?
4. Existe UMA história sendo contada (um único arco, um único modelo)?
5. Se eu apagar um slide do meio, a narrativa quebra?
6. O conteúdo gera sensação de descoberta (a promessa fica escondida até a revelação)?
7. O último slide recompensa o tempo investido (payoff > expectativa do gancho)?

Só depois de TODOS "sim" → siga para as Seções 1–8 (regras visuais).

---

## EXEMPLO DE ARCO (Modelo 5 — Polêmica, tema Ferrari/Lambo)
- S1 GANCHO: "Uma marca lendária acabou de cometer um erro de R$ bilhões." (não diz qual)
- S2 CURIOSIDADE: o que aconteceu — mas "a reação foi pior que o lançamento".
- S3 ESCALADA: a reação do mercado — "mas o detalhe que ninguém comentou foi a concorrente".
- S4 VIRADA: a concorrente não fez nada e venceu — "e o motivo não é o que parece".
- S5 ESCALADA: o que a concorrente realmente fez (1 movimento) — "isso revela uma regra".
- S6 REVELAÇÃO: a regra de posicionamento (a promessa central, enfim entregue).
- S7 INSIGHT: o que isso ensina pra qualquer marca/leitor.
- S8 CTA.
Note: nenhum slide do meio fecha. Cada um entrega 1 peça e abre a próxima.

---
> **FIM DA SEÇÃO 0. As Seções 1–8 entram DEPOIS deste roteiro aprovado.**

---

## 1. CONTEXTO DO PIPELINE (respeite as restrições)

- Saída: PNG 1080x1350 (4:5 Instagram), renderizado por **Chromium headless** a 2.571x.
- Você escreve **Python que gera strings HTML** com imagens inline em base64 (`photo_uri()`).
- O motor de render é Chromium real → você tem CSS COMPLETO: `filter`, `box-shadow`,
  `mix-blend-mode`, `backdrop-filter`, pseudo-elementos `::before/::after`, SVG, `radial-gradient`.
- Os recortes (PNG RGBA) já chegam prontos via `rembg`/flood-fill. Seu trabalho é
  **integrá-los a uma cena com física correta**, não apenas posicioná-los.
- Sempre que existir o helper `nuc_realism.py` no repo, IMPORTE e use suas funções
  (`fundo_profundo`, `recorte`, `card`, `GRAO_OVERLAY`, `REALISM_CSS`). Elas já
  implementam as regras abaixo. Não reinvente.

---

## 2. OS 5 NÃO-NEGOCIÁVEIS (reprovação automática)

Antes de exportar, TODA peça precisa cumprir os 5. Se violar 1, reescreva o slide.

### 2.1 SOMBRA DE CONTATO — nada flutua
Todo recorte (carro, pessoa, objeto) precisa de uma sombra elíptica difusa "no chão",
ancorando-o à cena. Sem isso, vira adesivo colado.
```css
.subject::after{
  content:""; position:absolute; left:8%; right:8%; bottom:-4%; height:9%;
  background:radial-gradient(closest-side, rgba(0,0,0,.62), transparent 78%);
  filter:blur(10px); z-index:1;
}
```

### 2.2 COERÊNCIA DE LUZ — sujeito conversa com o fundo
O recorte (luz de estúdio) precisa ser igualado ao fundo (escuro/atmosférico) via
color match + light wrap. Mesma direção e temperatura de luz.
```css
.subject>img{
  filter: brightness(.96) contrast(1.06) saturate(1.04)
          drop-shadow(0 0 1px rgba(0,0,0,.35))      /* trata borda dura */
          drop-shadow(0 0 14px var(--accent)40);    /* light wrap do accent */
}
```

### 2.3 PROFUNDIDADE EM 3 CAMADAS — por BLUR, nunca por opacity
- **L1 fundo:** cena/atmosfera com `filter:blur(12-16px)` + vinheta radial. Proibido
  gradient chapado e proibido fingir profundidade com `opacity` baixa.
- **L2 sujeito:** nítido, iluminado, com sombra de contato.
- **L3 grafismo:** cards/CTA com `box-shadow` PROJETADA (não só borda em glow).
```css
.depth-bg{position:absolute;inset:0;background-size:cover;
  filter:blur(14px) brightness(.55) saturate(1.05); transform:scale(1.08);}
.depth-bg::after{content:"";position:absolute;inset:0;
  background:radial-gradient(120% 90% at 50% 42%, transparent 38%, rgba(0,0,0,.55));}
```

### 2.4 GRÃO / TEXTURA — proibido fundo perfeitamente liso
Toda peça leva uma camada de ruído fotográfico por cima de TUDO. É o que mata o
"liso de render".
```css
.grain{position:absolute;inset:0;z-index:50;pointer-events:none;
  opacity:.07; mix-blend-mode:overlay;
  background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='120' height='120'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>");
  background-size:180px 180px;}
```
Adicione `<div class="grain"></div>` como ÚLTIMO filho de cada `.slide`.

### 2.5 BORDAS TRATADAS — sem recorte de tesoura
Todo PNG recortado recebe feather + light wrap (vide 2.2). Nunca uma borda dura,
serrilhada ou com halo branco. Se o asset vier sujo, peça novo recorte ao usuário.

---

## 3. IDENTIDADE NUC (preservar — é o trunfo, não mexa por mexer)

- **Tema:** dark editorial noturno. Fundos #06-0E (quase preto azulado), não preto puro.
- **Accent:** ciano `#1EC5F2` (hex oficial da marca, alinhado ao design_system). Aplicado
  em kicker, highlight box e light wrap.
- **Tipografia:** condensada PESADA, CAIXA-ALTA, para headlines. Hierarquia obrigatória:
  `kicker fino ciano` → `headline branca massiva` → `corpo cinza`.
- **Highlight box:** fundo ciano + texto escuro, em UMA palavra-chave por slide.

Mantenha isso. A identidade tipográfica do NUC é superior à da concorrência —
o problema NUNCA foi o design gráfico, foi a produção fotográfica. Não troque o sistema.

---

## 4. COMPOSIÇÃO (saia do empilhamento central simétrico)

- **Integração tipo↔imagem:** o título deve OCLUIR parte do sujeito (passar atrás/na
  frente do carro), via `z-index` intercalado. Proibido título preso num retângulo
  flutuante isolado da cena.
- **Assimetria:** quebre a simetria em pelo menos 1 eixo. Use diagonal, sobreposição
  de camadas, sangria do sujeito para fora do quadro.
- **Profundidade de cards:** quando empilhar fotos/cards (ex.: provas), gire levemente
  (`rotate(-2deg)`) e sobreponha com sombra → sensação de "pilha na mesa".
- **Fluxo de leitura:** preserve o de cima-para-baixo (kicker → headline → corpo → CTA).

---

## 5. TIPOGRAFIA E COPY (acabamento que entrega valor)

- **Contraste mínimo AA (4.5:1)** em todo texto-chave. PROIBIDO preto-sobre-preto
  (erro da versão antiga, slide "NÃO PRECISA DE"). De-ênfase nunca abaixo de 40%.
- **Revisão de copy obrigatória** antes de exportar: concordância, ortografia,
  **um único idioma por peça**. Erros como "TODO SEMANA" (era TODA) ou "ABSOLUTE
  DECEPÇÃO" (mistura EN+PT) reprovam a peça inteira — num cover, destroem percepção
  de valor instantaneamente.
- **CTA com presença:** pill com fill sólido + glow OU sombra projetada. Nunca cinza
  apagado sobre fundo escuro.

---

## 6. PROVA E HONESTIDADE (credibilidade é design)

- Quando a peça apresentar dado/case/manchete, ancore com **ativo visual coerente**
  (print, selo, gráfico) — prova exibida = autoridade.
- **NUNCA** apresente produto, manchete ou dado **fabricado** como se fosse factual.
  Se o ativo não é verificável, trate como conceitual/opinativo, não como notícia real.
- **NUNCA** recolora a lataria/superfície de um asset "na unha" para fingir outro
  produto — gera reflexo incoerente, tell clássica de IA. Use um asset coerente
  ou peça o correto.

---

## 7. ANTI-PADRÕES — o "modelo medíocre" que está PROIBIDO

Se você se pegar fazendo qualquer um destes, PARE e corrija:

- ❌ Carro/pessoa flutuando sem sombra de contato.
- ❌ Fundo de `linear/radial-gradient` chapado sem textura, blur ou vinheta.
- ❌ Recorte com luz de estúdio colado em fundo difuso (sem color match).
- ❌ Fundo perfeitamente liso, sem grão.
- ❌ Profundidade simulada com `opacity` em vez de `blur`.
- ❌ Título num retângulo de UI isolado, sem oclusão com a imagem.
- ❌ Cards "no mesmo plano Z" (só borda em glow, sem sombra projetada).
- ❌ Layout 100% simétrico, centralizado, retangular, estático.
- ❌ Texto de baixo contraste / preto-sobre-preto.
- ❌ Erro de português ou mistura de idiomas.
- ❌ Fontes genéricas (Inter, Roboto, Arial, system). Use a condensada da marca.

---

## 8. CHECKLIST DE QA — rode ANTES de exportar cada slide

Verifique mentalmente cada item. Reprovou em 1 → reescreva o slide, não exporte.

- [ ] Todo recorte tem sombra de contato (`.subject::after`)?
- [ ] Luz do sujeito bate com o fundo (color match + light wrap)?
- [ ] Fundo tem profundidade por BLUR + vinheta (não opacity, não gradient chapado)?
- [ ] Camada `.grain` presente cobrindo a peça inteira?
- [ ] Bordas do recorte tratadas (feather, sem halo/serrilha)?
- [ ] Cards/CTA com sombra PROJETADA (3 camadas Z reais)?
- [ ] Título ocluído/integrado à imagem (não UI flutuante)?
- [ ] Composição com assimetria/diagonal (não empilhamento central)?
- [ ] Todo texto-chave ≥ AA? Nenhum preto-sobre-preto?
- [ ] Copy revisada (ortografia, concordância, idioma único)?
- [ ] CTA com presença visual forte?
- [ ] Se há case/dado: lastro visual coerente e NÃO enganoso?

---

## 9. FLUXO DE TRABALHO

**FASE -1 — DIREÇÃO CRIATIVA (Seção -1 — roda PRIMEIRO):**
1. Classifique: o tema depende de realidade verificável (pessoa/marca/notícia)?
2. Se sim: interrompa e peça materiais reais ao usuário (prints, fotos, manchetes).
3. Rode o detector de artificialidade. Se reprovar, não avance.
4. Só depois que a âncora real estiver em mãos (ou o tema for conceitual): prossiga.

**FASE NARRATIVA (Seção 0 — obrigatória antes de qualquer código):**
5. Escolha o modelo de arco (A–E) e escreva o arco em 1 frase por beat.
6. Atribua papel funcional a cada slide (gancho / curiosidade / escalada / virada / revelação / insight / CTA).
7. Escreva o copy de cada slide com loop aberto — proibido fechar no meio.
8. Rode o teste de remoção. Qualquer slide removível = reescrever.
9. Rode o teste de qualidade narrativa (7 perguntas). Só avança com todos "sim".

**FASE VISUAL (Seções 1–8 — só depois da narrativa aprovada):**
10. Leia os assets que o usuário subiu em `/fotos`.
11. Importe `nuc_realism` se existir; senão, implemente as regras da seção 2 inline.
12. Para cada slide: monte fundo (L1) → recorte ancorado (L2) → tipo+grafismo (L3) → grão.
13. Rode o QA visual da seção 8 em cada slide.
14. Exporte via Playwright. Entregue os PNG 1080x1350.
15. Se algum asset impedir o padrão (recorte sujo, foto de baixa resolução), AVISE o
    usuário e peça o asset correto em vez de entregar abaixo do padrão.
