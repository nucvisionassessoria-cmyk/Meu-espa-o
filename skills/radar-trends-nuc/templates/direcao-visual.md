# Template: Direção Visual dos Slides

Use este template para descrever a direção de design de cada slide.
O objetivo é que um designer (ou o gerador de HTML da NUC Vision) consiga
reproduzir o slide com clareza.

---

## ESTRUTURA PADRÃO DE DESCRIÇÃO VISUAL

```
Direção visual:
- Fundo: [#050810 void / #0A0F1A navy / gradiente da marca / fundo do print]
- Elemento principal: [imagem / print / manchete / rosto / logo / abstrato]
- Headline: [tamanho / peso / cor / posição]
- Destaque: [qual palavra ou frase vai para PILL CIANO]
- Kicker (tag superior): ["TEXTO EM CIANO" — ex: "POSICIONAMENTO", "CASE", "DADOS"]
- Textura de fundo: [grade de pontos / linhas / noise / limpo]
- Glow/atmosfera: [radial ciano suave no centro / sem / atmosfera escura lateral]
- Logo NUC Vision: [presente no topo centralizado, branco / ausente]
- Foto dos sócios: [qual foto / posição / tratamento / ausente]
- Vinheta: [leve nas bordas / sem]
- Sentimento visual: [impacto / tensão / clareza / provocação / autoridade / fechamento]
```

---

## VOCABULÁRIO POR TIPO DE SLIDE

### Slide de HOOK (gancho máximo)
```
- Fundo: escuro ou com imagem da trend em overlay escuro (0.6 opacidade)
- Headline: Anton, grande (60–80px), branco, 1–2 linhas
- Pill ciano: na palavra de maior impacto
- Kicker: tag do tema em ciano (10px, uppercase, tracking alto)
- Sem excesso de elementos — só o gancho
- Sentimento: urgência, curiosidade, provocação
```

### Slide de CONTEXTUALIZAÇÃO
```
- Fundo: escuro (#0A0F1A)
- Kicker: "O QUE ACONTECEU" em ciano
- Headline pequena ou média + corpo de texto branco 75%
- Possível print/manchete em segundo plano, baixa opacidade
- Grade de pontos sutil como textura
- Sentimento: informativo, direto
```

### Slide de VIRADA ESTRATÉGICA
```
- Elemento de ruptura visual: linha divisória ciano, mudança de paleta
- Texto em duas partes: "isso não é apenas X" / "é Y"
- Pode usar split visual (esquerda apagada, direita iluminada)
- Sentimento: surpresa, mudança de perspectiva
```

### Slide de EXPLICAÇÃO / DESENVOLVIMENTO
```
- Layout com hierarquia: headline menor (22–28px) + corpo (13–15px)
- Pode usar lista com bullets em ciano ou cards com bordas ciano
- Fundo escuro com textura sutil
- Sentimento: construção de raciocínio, clareza
```

### Slide de QUEBRA DE CRENÇA
```
- Elemento de contraste: tachado / comparação lado a lado / "X" visual
- Tom mais tenso: fundo levemente mais escuro ou com vinheta forte
- Headline direta, sem rodeios
- Sentimento: desconforto produtivo, identificação com o erro
```

### Slide de APLICAÇÃO PRÁTICA
```
- Layout limpo: 3–4 bullets com ícones pequenos
- Cards com fundo rgba(30,197,242,0.06) e borda rgba(30,197,242,0.15)
- Espaço entre itens generoso
- Sentimento: acionável, útil, concreto
```

### Slide de INSIGHT FORTE
```
- Impacto máximo: headline 60–80px Anton, pill ciano na frase-chave
- Espaço negativo generoso — deixar a frase respirar
- Sem elementos secundários
- Pode usar radial glow ciano sutil no centro
- Sentimento: memorável, poderoso, digno de print
```

### Slide de CONEXÃO NUC VISION
```
- Logo NUC Vision em destaque (branco, centralizado ou top-left maior)
- Fundo com gradiente da marca (navy → ciano) ou escuro com glow
- Texto conectando a lição ao que a NUC faz — específico
- Possível foto dos sócios em segundo plano (overlay 0.3)
- Sentimento: institucional, confiante, sem ser vendedor
```

### Slide de CTA
```
- Slide mais limpo da sequência
- Logo NUC Vision centralizado
- Handle @nucvision em destaque
- CTA em pill ciano: texto branco bold
- Fundo: gradiente da marca ou escuro com glow superior
- Sem poluição visual
- Sentimento: encerramento limpo, convite claro
```

---

## IDENTIDADE VISUAL RÁPIDA (referência)

```
Cores:
  void    = #050810   (fundo principal)
  navy    = #0A0F1A   (fundo secundário)
  rich    = #0F1729   (fundo com profundidade)
  ciano   = #1EC5F2   (destaque principal)
  branco  = #FFFFFF   (texto principal)
  muted   = rgba(255,255,255,0.65)  (texto secundário)

Pill ciano:
  background: #1EC5F2
  color: #fff
  padding: 2px 16px 7px
  border-radius: 12px
  box-shadow: 0 4px 22px rgba(30,197,242,0.45)

Kicker:
  font: Space Grotesk 700
  size: 10px
  color: #1EC5F2
  letter-spacing: 0.2em
  text-transform: uppercase

Grade de pontos:
  background-image: radial-gradient(circle, rgba(30,197,242,0.07) 1.2px, transparent 1.2px)
  background-size: 28px 28px

Divisor:
  width: 44px; height: 2px; background: #1EC5F2; border-radius: 2px

Gradiente da marca:
  linear-gradient(165deg, #1D4D8F 0%, #2591E6 55%, #5DD6F5 100%)
```

---

## FOTOS DO REPOSITÓRIO

Referenciar pelo nome ao sugerir uso:

| Arquivo | Descrição | Melhor uso |
|---------|-----------|------------|
| `derick_bracos_cruzados.jpg` | Derick posando, braços cruzados, camisa NUC Vision | Slide de autoridade, CTA |
| `iago_bracos_cruzados.png` | Iago posando, braços cruzados, camisa NUC Vision | Slide de autoridade, CTA |
| `trio_reuniao.png` | Três sócios em reunião | Hero, slide institucional |
| `lucas_derick.jpeg` | Lucas e Derick juntos, ambiente de trabalho | Slide de conexão NUC |
| `dashboard_laptop.png` | Tela de dashboard/dados em laptop | Slide sobre dados, estrutura, CRM |
