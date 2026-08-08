---
name: documentation-writer
description: Use esta skill sempre que o usuário pedir para gerar, criar ou atualizar documentação de um projeto/código — ex. "cria um README pra esse projeto", "documenta essa API", "gera o Swagger/OpenAPI disso", "preciso de documentação técnica desse módulo", "cria um diagrama de arquitetura pra documentação". Cobre README, especificação Swagger/OpenAPI, diagramas (Mermaid) e documentação técnica de código/módulos. Não use para comentários inline pontuais em uma única função — isso é trivial e não precisa desta skill.
---
 
# Documentation Writer

Skill para gerar documentação completa e profissional a partir de código ou da descrição de um projeto. O objetivo é que a documentação gerada seja útil de verdade — para outro dev (ou para o próprio usuário no futuro) entender e usar o projeto sem precisar perguntar nada.

## Tipos de documentação que esta skill cobre

### 1. README

Estrutura padrão (adaptar conforme o projeto, omitir seções que não se aplicam):

```markdown
# Nome do Projeto
 
Breve descrição (1-2 frases: o que é e pra que serve).
 
## Tecnologias usadas
- ...
 
## Pré-requisitos
- ...
 
## Como instalar / rodar localmente
[passo a passo, comandos exatos]
 
## Estrutura do projeto
[árvore de pastas comentada, se relevante]
 
## Endpoints / Funcionalidades principais
[resumo, com link para a doc de API se houver Swagger]
 
## Variáveis de ambiente
[se aplicável, tabela com nome/descrição/obrigatório]
 
## Como contribuir
[se for projeto aberto/colaborativo — omitir se for pessoal]
 
## Licença
[se aplicável]
```

### 2. Swagger / OpenAPI

- Gere a especificação em YAML (formato OpenAPI 3.x), cobrindo: paths, methods, parameters, request body, responses (incluindo códigos de erro relevantes, não só 200), e schemas reutilizáveis em `components/schemas`.
- Baseie-se nos controllers/rotas reais do código fornecido — não invente endpoints que não existem.
- Se o usuário usa Spring Boot, pode também sugerir o uso de anotações `springdoc-openapi` (`@Operation`, `@ApiResponse`) no código, além do YAML gerado.

### 3. Diagramas

Gere em Mermaid, escolhendo o tipo mais adequado ao que está sendo documentado:

- **Diagrama de classes** — para modelagem de entidades/domínio
- **Diagrama de sequência** — para fluxos de requisição entre camadas (controller → service → repository)
- **Diagrama ER** — para estrutura de banco de dados
- **Flowchart** — para lógica de processo/decisão

### 4. Documentação técnica de módulo/código

Para documentar uma classe, módulo ou serviço específico:

```markdown
## [Nome do módulo/classe]
 
**Responsabilidade:** [o que essa peça faz, em 1-2 frases]
 
**Principais métodos/funções:**
- `nomeDoMetodo(parametros)`: [o que faz, o que retorna, exceptions que pode lançar]
 
**Dependências:** [o que esse módulo usa/depende]
 
**Usado por:** [quem chama esse módulo, se identificável]
```

## Regras gerais

- Documente o que o código **realmente faz**, nunca invente funcionalidade que não existe no trecho fornecido.
- Se faltar contexto pra alguma seção (ex: não sabe se tem licença, não sabe o nome real do projeto), deixe um placeholder claro como `[definir]` em vez de inventar.
- Markdown deve ser compatível com Obsidian quando o usuário pedir pra salvar como nota: deixar linha em branco antes de tabelas.
- Para projetos grandes, pergunte objetivamente qual tipo de documentação ele quer primeiro (README, API, diagrama, doc técnica) em vez de gerar tudo de uma vez sem necessidade — a menos que ele já tenha pedido "documentação completa".
- Seja direto na escrita da documentação: frases claras, sem enrolação corporativa.
