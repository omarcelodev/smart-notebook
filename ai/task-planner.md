---
name: task-planner
description: >
  Use esta skill sempre que o usuário descrever uma ideia de projeto/sistema e pedir para transformar em tarefas, fases, roadmap ou plano de execução — ex. "quero criar um sistema de X, como organizo isso", "transforma essa ideia em tarefas", "monta um roadmap pra isso", "quais as fases desse projeto". Quebra a ideia em fases lógicas com tarefas dentro de cada uma, ordenadas por dependência e prioridade. Não use para planejamento de arquitetura técnica detalhada (isso é o software-architect) — esta skill foca no "o quê" e "em que ordem", não no "como" tecnicamente implementar.
---
 
# Task Planner

Skill para transformar uma ideia de projeto em um plano de execução faseado. O foco é responder "por onde eu começo e em que ordem" — não desenhar arquitetura técnica (isso é outra skill).

## Como estruturar o plano

1. **Identifique o núcleo mínimo (MVP)** — o que é absolutamente essencial pra o sistema funcionar e gerar valor real, mesmo que básico. Isso geralmente é a Fase 1.
2. **Identifique dependências** — uma tarefa/fase só deve vir depois de outra se realmente depende dela (ex: não dá pra ter "agenda" sem "cadastro de usuário" primeiro, mas "dashboard" pode vir bem depois pois depende de dados já existirem).
3. **Agrupe em fases** — cada fase deve ter um objetivo coeso (não misturar autenticação com relatórios na mesma fase). Normalmente 3-5 fases é o ideal; mais que isso, considere agrupar.
4. **Dentro de cada fase, liste as tarefas** — específicas e acionáveis (não "fazer backend", mas "criar endpoint de cadastro de usuário").

## Formato de saída

```markdown
## Fase 1: [nome da fase, ex: Fundação]
- [tarefa específica]
- [tarefa específica]
 
## Fase 2: [nome da fase]
- ...
 
## Fase 3: [nome da fase]
- ...
```

Depois das fases, adicione uma seção curta:

```markdown
## Por que essa ordem
[1-3 linhas explicando a lógica de dependência entre as fases]
```

## Regras

- Sempre nomeie a fase com algo descritivo (ex: "Fundação", "Core do produto", "Monetização", "Refinamento"), não só "Fase 1, 2, 3" sem contexto — isso ajuda a entender o objetivo de cada etapa.
- Tarefas devem ser concretas e verificáveis (dá pra saber quando estão "prontas"), não vagas.
- Se o usuário não especificar prazo/recursos disponíveis (ex: projeto sozinho vs equipe, part-time vs full-time), assuma um ritmo razoável de projeto pessoal/estudante e não inclua estimativa de tempo a menos que ele peça — focar na ordem lógica, não em cronograma.
- Se a ideia for muito vaga (ex: "quero criar um app"), faça 1-2 perguntas objetivas sobre o domínio/público antes de gerar o plano — fases genéricas demais não ajudam.
- Quando fizer sentido, separe explicitamente o que é MVP (fases iniciais) do que é "nice to have" (fases finais), para o usuário saber até onde precisa ir pra já ter algo validável.
- Não entre em detalhe técnico de implementação (isso é responsabilidade da skill software-architect) — foque em "o quê" fazer e "em que ordem", não "como" tecnicamente construir.

## Quando o usuário já tiver um projeto em andamento

Se parte do sistema já existe (ex: cadastro e login já feitos), comece o plano a partir do que falta, reconhecendo o que já está pronto em vez de re-listar do zero.
