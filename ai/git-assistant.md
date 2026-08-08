---
name: git-assistant
description: Use esta skill sempre que o usuário digitar "/git-commit", "/pr" ou "/changelog", ou pedir para gerar mensagem de commit, descrição de Pull Request, ou changelog a partir de mudanças de código (diff, lista de arquivos alterados, ou descrição do que foi feito). Gera commits semânticos (Conventional Commits), descrições de PR estruturadas, e changelogs organizados por tipo de mudança.
---
 
# Git Assistant

Skill para gerar artefatos de Git padronizados: commits semânticos, descrições de Pull Request e changelogs. Foco em consistência com o padrão **Conventional Commits**.

## Quando ativar

- `/git-commit` — gerar mensagem de commit a partir do diff/mudança descrita
- `/pr` — gerar descrição de Pull Request
- `/changelog` — gerar ou atualizar changelog
- Pedidos diretos como "gera o commit disso", "escreve a descrição do PR", "atualiza o changelog"
Se o usuário não colar o diff/mudança, peça um resumo do que foi alterado antes de gerar — não invente o conteúdo do commit.

## 1. Commits semânticos (`/git-commit`)

Formato: `tipo(escopo): descrição curta no imperativo`

**Tipos válidos:**

- `feat` — nova funcionalidade
- `fix` — correção de bug
- `refactor` — mudança de estrutura sem alterar comportamento
- `docs` — documentação
- `test` — testes
- `chore` — manutenção, configs, dependências
- `style` — formatação, sem mudança de lógica
- `perf` — melhoria de performance
**Regras:**
- Descrição no imperativo, minúscula, sem ponto final: `implement JWT authentication`, não `Implemented JWT authentication.`
- Escopo entre parênteses é opcional, mas recomendado quando o projeto tem módulos claros (ex: `auth`, `api`, `db`).
- Se a mudança for grande/quebra compatibilidade, adicione `BREAKING CHANGE:` no corpo do commit, explicando o impacto.
- Se houver múltiplas mudanças não relacionadas no mesmo diff, avise o usuário que seria melhor separar em commits distintos, e sugira como dividir.
- Gere a mensagem curta (linha de título) e, se a mudança for complexa, um corpo opcional explicando o "porquê" (não o "o quê", que já está no diff).
Exemplo de saída:

```linguagem
feat(auth): implement JWT authentication
 
Adds token generation and validation middleware to replace
the previous session-based auth.
```

## 2. Pull Requests (`/pr`)

Estrutura:

```markdown
## O que foi feito
[resumo direto das mudanças, em bullets se houver mais de uma]
 
## Por quê
[motivação/contexto da mudança]
 
## Como testar
[passos pra quem for revisar validar localmente]
 
## Checklist
- [ ] Testes passando
- [ ] Sem warnings/erros de lint
- [ ] Documentação atualizada (se aplicável)
```

Adapte o checklist conforme o que for relevante para o projeto (ex: se não há suite de testes configurada, não inclua esse item como obrigatório).

## 3. Changelog (`/changelog`)

Use o formato **Keep a Changelog** agrupado por tipo:

```markdown
## [Não lançado]
 
### Adicionado
- ...
 
### Corrigido
- ...
 
### Modificado
- ...
 
### Removido
- ...
```

- Gere a entrada com base nos commits/mudanças fornecidas, agrupando por tipo (feat → Adicionado, fix → Corrigido, refactor/chore → Modificado, etc).
- Se o usuário já tiver um CHANGELOG.md existente, adicione a nova entrada no topo, mantendo o histórico anterior intacto — não reescreva entradas antigas.

## Regras gerais

- Seja direto: gere o artefato pedido sem explicação longa de Conventional Commits a menos que o usuário pergunte sobre o padrão em si.
- Nunca invente o que foi mudado — baseie-se sempre no diff/descrição fornecida pelo usuário.
- Se o diff misturar tipos diferentes de mudança (ex: feat + fix juntos), aponte isso e sugira separar, mesmo gerando uma sugestão de mensagem única se o usuário preferir não dividir.
