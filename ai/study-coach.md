---
name: study-coach
description: >
  Use esta skill sempre que o usuário pedir para montar um plano ou cronograma de estudos cobrindo uma ou mais matérias/tecnologias (ex: "monta um plano de estudos pra C, Estrutura de Dados, SQL, Spring Boot e Inglês", "como devo estudar pra essas matérias", "cria um cronograma de estudo pra essa lista de assuntos"). Diferente da weekly-planner (que organiza a semana toda incluindo faculdade/trabalho/lazer) e do study-mode (que conduz uma sessão de ensino ativa em tempo real), esta skill foca em planejar o QUE estudar, em qual ordem, e com que profundidade, ao longo do tempo — o conteúdo do plano de estudos em si, não a agenda da semana nem a sessão de ensino.
---
 
# Study Coach

Skill para criar planos de estudo estruturados cobrindo uma ou mais matérias/tecnologias. O foco é decidir **o que estudar, em qual ordem, e com que profundidade** — diferente de organizar a agenda da semana (weekly-planner) ou de conduzir uma sessão de ensino interativa (study-mode).

## Como montar o plano

1. **Avalie dependências entre os temas** — alguns assuntos são pré-requisito de outros (ex: lógica/C antes de Estrutura de Dados, SQL básico antes de modelagem avançada). Ordene o plano respeitando isso.
2. **Avalie o nível atual do usuário em cada tema** — se não souber, pergunte rapidamente (iniciante / já viu o básico / só precisa revisar) antes de definir profundidade. Não trate tudo como do zero se o usuário já tem base.
3. **Divida cada tema em sub-tópicos concretos** — não deixe "estudar SQL" como bloco único; quebre em (ex: DDL/DML/DQL → JOINs → subqueries → índices...).
4. **Distribua ao longo do tempo disponível** — se o usuário não informar quanto tempo/dia ele tem, pergunte antes de gerar o cronograma (isso muda completamente o ritmo do plano).
5. **Inclua revisão espaçada** — tópicos já estudados devem reaparecer periodicamente no cronograma para reforço, não só ser estudados uma vez e abandonados.

## Formato de saída

```markdown
## Plano de Estudos
 
### Ordem recomendada dos temas
1. [tema] — porquê vem primeiro
2. [tema] — ...
 
### Cronograma
**Semana 1-2: [tema]**
- Sub-tópicos: ...
- Meta da etapa: [o que o usuário deve conseguir fazer/explicar ao final]
 
**Semana 3: [tema]**
...
 
### Revisão
- [quando e o que revisar, ex: "semana 5: revisão rápida de C antes de avançar pra Spring Boot"]
```

Adapte a granularidade (semanas vs dias) conforme o tempo total disponível informado pelo usuário.

## Regras gerais

- Sempre explique a ordem escolhida — não é arbitrária, depende de pré-requisitos reais entre os temas.
- Defina uma "meta de saída" clara por etapa (o que o usuário deve conseguir fazer, não só "ter lido sobre"), pra ele saber quando pode avançar.
- Para temas técnicos como Inglês, que não tem fim definido como uma matéria de faculdade, trate como atividade contínua e recorrente ao longo de todo o plano, não como uma fase isolada que "termina".
- Se o usuário já tiver mencionado a rotina semanal dele (faculdade, trabalho) em conversas anteriores, leve isso em conta pra não propor um ritmo irreal — mas não recrie a agenda completa da semana, isso é papel da weekly-planner. Esta skill foca no conteúdo e na sequência do estudo.
- Se o plano envolver matérias que já fazem parte do currículo da faculdade do usuário, evite redundância — pergunte se o plano deve complementar ou substituir o que já é cobrido lá.
- Sugira pelo menos um critério prático de avaliação de progresso por tema (ex: "resolver N exercícios de tal tipo sem consultar material" para saber se está dominado).
