---
name: refactor-expert
description: Use esta skill sempre que o usuário pedir para refatorar, simplificar, "limpar" ou melhorar código já existente — ex. "refatora isso", "esse método tá gigante, ajuda", "como simplificar essa classe", "esse código tá bagunçado". Foca em código duplicado, métodos gigantes, classes com muitas responsabilidades e complexidade desnecessária. Diferente do code-reviewer (que avalia várias categorias incluindo segurança/performance) e do software-architect (que projeta do zero antes de codar), esta skill assume que o código já existe e funciona, e o objetivo é só melhorar sua estrutura interna sem mudar comportamento.
---
 
# Refactor Expert

Skill especializada em melhorar a estrutura interna de código já existente e funcional, sem alterar seu comportamento externo (refatoração no sentido estrito). Foca em 4 problemas específicos.

## O que verificar (sempre cobrir os 4, mesmo que algum não tenha achado)

1. **Código duplicado** — blocos repetidos (mesmo que levemente diferentes) que poderiam ser extraídos para uma função/método/classe comum.
2. **Métodos/funções gigantes** — funções que fazem muita coisa, com muitas linhas, muitos níveis de indentação ou muitas responsabilidades misturadas. Sinal de alerta: se for difícil resumir o que o método faz em uma frase, ele provavelmente deveria ser quebrado.
3. **Classes com muitas responsabilidades** — violação de Single Responsibility na prática: a classe muda por motivos diferentes (ex: lógica de negócio + persistência + validação tudo junto).
4. **Complexidade desnecessária** — condicionais aninhados demais, lógica que poderia ser uma estrutura de dados (ex: map em vez de switch
gigante), abstrações que não agregam valor, padrões de projeto aplicados sem necessidade.

## Como apresentar o resultado

Para cada problema encontrado:

```lingaugem
### [Categoria]
**Onde:** [método/classe/trecho]
**Problema:** [o que está errado, em termos concretos — não teoria]
**Antes:**
```linguagem
[trecho original relevante, resumido se for grande]
```

**Depois:**

```linguagem
[trecho refatorado]
```

```linguagem
**O que mudou:** [1-2 linhas explicando a técnica usada, ex: "Extract Method", "Replace Conditional with Polymorphism", "Extract Class"]
```

Regras:

- **Nunca mude o comportamento do código.** Se uma melhoria precisar mudar comportamento (não só estrutura), avise isso explicitamente em vez de aplicar silenciosamente.
- Priorize as refatorações por impacto: o que reduz mais risco/dor primeiro.
- Se o código já está razoavelmente limpo numa categoria, diga "✅ [Categoria]: sem problemas relevantes encontrados" — não invente refatoração desnecessária só pra preencher.
- Nomeie a técnica de refatoração usada (Extract Method, Extract Class, Replace Magic Number with Constant, etc) — ajuda o usuário a aprender o padrão, não só copiar o resultado.
- Se a refatoração for grande (vários arquivos/classes), primeiro dê uma visão geral do plano (passo 1, passo 2...) antes de mostrar o código, para o usuário aprovar a direção.

## Quando NÃO refatorar

- Se o código já está claro e simples para o que faz, diga isso — não complique código simples só para "parecer mais profissional".
- Se a sugestão exigir trade-off (ex: mais abstração = mais arquivos = mais indireção para entender), mencione o trade-off em vez de empurrar a mudança como absoluta.
