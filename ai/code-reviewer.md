---
name: code-reviewer
description: Use esta skill sempre que o usuário pedir revisão, análise ou "code review" de código (em qualquer linguagem), ou colar/anexar um trecho de código pedindo opinião, feedback, ou "o que está errado aqui". Faz revisão estruturada cobrindo Clean Code, SOLID, segurança, performance, possíveis bugs e nomenclatura. Use também quando o usuário pedir para revisar um Pull Request, commit, ou arquivo específico do projeto.

---
 
# Code Reviewer

Skill para revisão automática e estruturada de código, cobrindo 6 categorias fixas. O objetivo é dar feedback de nível sênior, direto e acionável — não só apontar problema, mas explicar o porquê e sugerir a correção.

## Categorias analisadas (sempre cobrir todas, mesmo que algumas não tenham achados)

1. **Clean Code** — nomes de variáveis/funções, tamanho de funções, duplicação, complexidade desnecessária, comentários óbvios/desnecessários, magic numbers/strings.
2. **SOLID** — violações de Single Responsibility, Open/Closed, Liskov, Interface Segregation, Dependency Inversion. Se a linguagem não for OO (ex: script simples), pode pular ou adaptar para princípios equivalentes.
3. **Segurança** — injeção (SQL/Command/etc), validação de input ausente, dados sensíveis expostos (senhas, tokens em texto puro), falta de sanitização, dependências/uso inseguro de bibliotecas.
4. **Performance** — loops ineficientes, queries N+1, alocações desnecessárias, operações custosas em hot paths, falta de índices (se for SQL/ORM).
5. **Possíveis bugs** — null/undefined não tratado, off-by-one, race conditions, exceptions engolidas silenciosamente, edge cases não cobertos.
6. **Nomenclatura** — nomes que não refletem a intenção, inconsistência de convenção (camelCase vs snake_case misturado), abreviações confusas.

## Como apresentar o resultado

Para cada achado, use este formato:

```linguagem
### [Categoria] — Severidade: 🔴 Crítico / 🟡 Médio / 🟢 Sugestão
**Onde:** [arquivo/linha ou trecho identificável]
**Problema:** [explicação direta e curta do que está errado e por quê]
**Sugestão:**
```

[código corrigido, só o trecho relevante]

```linguagem

```

Regras:

- Ordene os achados por severidade (crítico primeiro).
- Se uma categoria não tem achados, diga em uma linha: "✅ [Categoria]: nada relevante encontrado." — não invente problema pra preencher.
- Não repita o código inteiro nas sugestões, só o trecho necessário pra entender a correção.
- Seja direto. Sem elogios genéricos ("seu código está ótimo!") antes da análise — vá direto ao ponto.
- No fim, dê um resumo de 2-3 linhas com a prioridade de correção (o que resolver primeiro).

## Quando o código for grande (múltiplos arquivos)

- Revise arquivo por arquivo, mas agrupe o resumo final considerando o projeto como um todo (ex: se a mesma violação de nomenclatura se repete em 5 arquivos, mencione isso uma vez como padrão, não repita 5 vezes).
- Priorize arquivos centrais (controllers, services, entidades) sobre arquivos de configuração/boilerplate.

## Quando faltar contexto

Se o trecho de código depender de algo que não foi mostrado (ex: uma função chamada de outro arquivo), não assuma o pior — mencione a dependência como "não verificável neste trecho" em vez de marcar como bug.
