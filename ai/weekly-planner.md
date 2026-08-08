---
name: weekly-planner
description: >
  Use esta skill sempre que o usuário pedir para organizar a semana, montar uma rotina, distribuir horários entre faculdade, trabalho, estudos, inglês e natação, ou pedir ajuda para encaixar uma nova atividade na agenda. Exemplos de gatilho - "monta minha semana", "como encaixo X na minha rotina", "organiza meus horários", "tô sem tempo pra estudar, ajuda a reorganizar". Gera um cronograma semanal realista considerando os compromissos fixos e os blocos de tempo livre disponíveis.
---
 
# Weekly Planner

Skill para organizar a semana considerando os compromissos fixos do usuário (faculdade noturna, trabalho como estagiário, estudos de Data Engineering/IA, inglês, natação) e distribuir o tempo disponível de forma realista — sem sobrecarregar.

## Compromissos fixos conhecidos (usar como base, ajustar se o usuário corrigir)

- **Faculdade**: curso noturno de Engenharia de Software na UniGoiás
- **Trabalho**: estágio de suporte na ChatPro (período diurno, presumivelmente)
- **Estudos paralelos**: Data Engineering/IA, projetos pessoais (ex: sistema de barbearia)
- **Inglês**: a definir frequência com o usuário se não tiver sido informada
- **Natação**: a definir frequência com o usuário se não tiver sido informada
Se a frequência/horário de inglês ou natação não estiver clara, pergunte antes de encaixar no cronograma — não invente horário fixo sem confirmação.

## Como montar o cronograma

1. **Mapeie os blocos fixos primeiro** — faculdade (noite) e trabalho (dia) já ocupam a maior parte do dia útil. Coloque isso como inegociável.
2. **Identifique os blocos livres reais** — manhã antes do trabalho, intervalos, fim de semana. Seja realista: não empilhe estudo pesado logo depois de um dia cheio de trabalho + faculdade sem nenhum espaço de descanso.
3. **Distribua as atividades restantes** (estudos de Data/IA, inglês, natação, projetos pessoais) nos blocos livres, considerando:
   - Inglês e natação geralmente funcionam melhor em horários fixos e recorrentes (rotina ajuda a criar hábito) — sugira dias/horários fixos em vez de "encaixar quando der".
   - Estudos de Data Engineering/IA e projetos pessoais precisam de blocos mais longos e de energia mental alta (evite colocar logo após um dia exaustivo se possível).
   - Deixe pelo menos 1 bloco de descanso real na semana sem compromisso — sustentabilidade da rotina importa mais que preencher 100% do tempo.

## Formato de saída

```markdown
## Segunda
- [horário] [atividade]
- [horário] [atividade]
 
## Terça
...
```

Ou, se o usuário preferir visão semanal compacta, uma tabela com dias nas colunas e blocos de horário nas linhas.

No final, adicione uma seção curta:

```markdown
## Observações
- [trade-offs feitos, ex: "natação ficou só 2x/semana pra não sobrecarregar quinta"]
- [sugestão de ajuste se a rotina parecer apertada demais]
```

## Regras gerais

- Antes de gerar o cronograma, confirme com o usuário: dias e horários de faculdade, horário de trabalho, e frequência desejada de inglês e natação — se algum desses já foi mencionado antes na conversa, não pergunte de novo, use o que já foi dito.
- Seja honesto se a semana proposta pelo usuário for irrealista (ex: querer encaixar tudo sem nenhum tempo de descanso) — aponte isso diretamente em vez de só montar uma grade apertada sem comentar.
- Priorize consistência sobre intensidade: é melhor 3 blocos curtos e fixos de estudo do que 1 bloco gigante esporádico.
- Não sugira cortar sono para encaixar atividades.
