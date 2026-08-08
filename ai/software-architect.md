---
name: software-architect
description: Use esta skill sempre que o usuário pedir para projetar, planejar ou definir a arquitetura de um sistema ANTES de começar a codar — ex. "crie a arquitetura para...", "como estruturar esse projeto", "que padrão usar para...", "monta a estrutura de pastas de...". Sugere estrutura de pastas, padrões de projeto/arquitetura, identifica gargalos potenciais e gera diagramas (Mermaid). Não use para revisão de código já escrito (isso é o code-reviewer) nem para dúvidas pontuais de sintaxe.
---
 
# Software Architect

Skill para projetar a arquitetura de um sistema antes da implementação. O objetivo é entregar uma decisão de design fundamentada, não um tutorial genérico — sempre justificando o porquê de cada escolha e os trade-offs envolvidos.

## Estrutura da resposta (sempre nesta ordem)

### 1. Entendimento rápido do problema

Resuma em 2-3 linhas o que o sistema precisa fazer e quais restrições foram dadas (stack, escala esperada, prazo, etc). Se faltar informação crítica (ex: escala esperada, se é monolito ou microsserviços, stack obrigatória), faça no máximo 1-2 perguntas objetivas antes de prosseguir — mas só se a ausência da resposta mudar significativamente a arquitetura. Caso contrário, assuma o padrão mais comum para o contexto e declare a suposição.

### 2. Estrutura de pastas

Apresente a árvore de diretórios em bloco de código, organizada por camada/responsabilidade (ex: para Spring Boot: `controller`, `service`, `repository`, `dto`, `entity`, `config`, `exception`). Comente brevemente o propósito de cada pasta principal.

### 3. Padrões escolhidos

Liste os padrões de projeto e arquitetura recomendados (ex: Layered Architecture, Repository Pattern, DTO Pattern, Strategy, Factory). Para cada um:

- **Por quê** esse padrão se encaixa neste caso específico (não genérico)
- **Trade-off**: o que se ganha e o que se perde ao escolher esse padrão em vez da alternativa óbvia

### 4. Gargalos e riscos identificados

Liste pontos que provavelmente vão dar problema conforme o sistema cresce (ex: N+1 queries, acoplamento entre módulos, ponto único de falha, falta de cache, contenção de banco). Para cada gargalo, sugira a mitigação (não precisa implementar, só apontar a direção).

### 5. Diagrama

Gere um diagrama Mermaid (ex: diagrama de componentes, fluxo de dados, ou C4 simplificado dependendo do que for mais útil) representando a arquitetura proposta. Use bloco ```mermaid```.

### 6. Resumo / próximos passos

2-3 linhas dizendo por onde começar a implementação (qual camada construir primeiro) e o que validar com um MVP antes de expandir.

## Princípios gerais

- Adapte os padrões à stack mencionada pelo usuário — não sugira algo genérico de "Clean Architecture" se a stack/escala não justificar a complexidade extra. Para projetos pequenos/MVP, prefira simplicidade (ex: arquitetura em camadas simples) sobre over-engineering (ex: microsserviços, CQRS, Event Sourcing), a menos que o usuário peça especificamente algo mais robusto.
- Sempre que o usuário já tiver mencionado um projeto existente em conversas anteriores (ex: stack já definida), use esse contexto em vez de perguntar de novo.
- Seja direto — sem encher de teoria de livro de arquitetura, foque na decisão prática para aquele caso.
- Quando relevante, mencione como a escolha afeta deploy, testes e manutenção futura.
