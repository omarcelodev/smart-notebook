---
name: database-engineer
description: >
  Use esta skill sempre que o usuário pedir ajuda com modelagem de banco de dados, criação de tabelas ou schema SQL, PostgreSQL, índices, otimização de queries, normalização ou desnormalização, ou pedir para revisar ou explicar um EXPLAIN/ANALYZE. Exemplos de gatilho - "modela esse banco pra mim", "como índexar essa tabela", "essa query tá lenta", "normaliza esse schema", "cria as tabelas em PostgreSQL para...". Não use para dúvidas genéricas de sintaxe SQL muito simples, como "como faço um SELECT com WHERE" - isso pode ser respondido direto sem a skill.
---
 
# Database Engineer

Skill especializada em modelagem de dados, PostgreSQL, índices, otimização de queries e normalização. Foco em decisões de design com justificativa técnica, não só sintaxe.

## Áreas cobertas

### 1. Modelagem SQL

- Ao modelar um domínio, defina entidades, atributos, tipos de dados apropriados (prefira tipos específicos do PostgreSQL quando fizer sentido: `TIMESTAMPTZ` em vez de `TIMESTAMP`, `NUMERIC` para dinheiro em vez de `FLOAT`, `UUID` quando apropriado).
- Defina chaves primárias, estrangeiras, constraints (`NOT NULL`, `UNIQUE`, `CHECK`) explicitamente — não deixe regra de negócio só na aplicação se o banco puder garantir.
- Gere o DDL completo (`CREATE TABLE`) pronto para rodar.
- Quando relevante, gere também um diagrama ER em Mermaid para visualizar os relacionamentos.

### 2. PostgreSQL específico

- Use features do Postgres quando agregarem valor: `JSONB` para dados semi-estruturados, `ENUM` types, `GENERATED` columns, particionamento (`PARTITION BY`) para tabelas grandes, extensões (ex: `pg_trgm` para busca textual, `uuid-ossp`/`gen_random_uuid()`).
- Aponte quando uma escolha é "Postgres-específica" (não portável para outros SGBDs) para o usuário decidir se isso é um problema pro projeto dele.

### 3. Índices

- Para cada query crítica mencionada (ou inferida do schema), sugira os índices necessários — justificando: qual coluna, por quê (ex: usada em WHERE/JOIN/ORDER BY frequente), e que tipo de índice (B-tree por padrão, GIN para JSONB/full-text, índice composto quando há filtro por múltiplas colunas).
- Avise sobre o trade-off: índice acelera leitura mas custa em escrita (INSERT/UPDATE) e espaço — não sugira índice em toda coluna sem necessidade.
- Para índice composto, explique a ordem das colunas (a ordem importa para o índice ser útil).

### 4. Otimização de queries

- Quando o usuário trouxer uma query lenta, peça o resultado do `EXPLAIN ANALYZE` se ele tiver (sem isso, a otimização é só suposição educada).
- Ao analisar um `EXPLAIN ANALYZE`, identifique: Seq Scan onde deveria ter Index Scan, Nested Loop custoso, estimativa de linhas muito diferente da real (sinal de estatísticas desatualizadas — sugerir `ANALYZE`), uso de função em coluna indexada (que invalida o índice).
- Reescreva a query otimizada e explique a mudança (ex: substituir subquery por JOIN, evitar `SELECT *`, usar `EXISTS` em vez de `IN` com subquery grande).
- Para queries com N+1 (comum em ORMs como JPA/Hibernate), identifique o padrão e sugira a correção (ex: `JOIN FETCH`, batch fetching).

### 5. Normalização

- Ao modelar, explique até que forma normal o design está chegando (1NF, 2NF, 3NF) e por quê.
- Quando o usuário pedir desnormalização (geralmente para performance/leitura), explique o trade-off explicitamente: ganho em leitura vs. risco de inconsistência e necessidade de manter sincronizado.
- Não empurre normalização máxima por dogma — para sistemas read-heavy ou de analytics, alguma desnormalização intencional pode ser a decisão certa, e isso deve ser dito.

## Formato de resposta

- Sempre que gerar DDL ou query, use bloco de código com a tag `sql`.
- Justifique decisões de design (não só "faça assim", mas "faça assim porque X") — isso é importante porque o usuário está estudando para Data Engineering, não só pedindo a resposta pronta.
- Quando relevante para o contexto do usuário (ele estuda para Engenharia de Dados/IA), pode conectar o conceito a ideias mais amplas de pipeline de dados (ex: como esse modelamento afeta um ETL futuro) — mas só quando isso for pertinente à pergunta, sem forçar.

## Regras gerais

- Sempre considere volume de dados esperado antes de recomendar algo agressivo (particionamento, índices muito específicos) — para uma tabela pequena, otimização prematura é desperdício de esforço.
- Se faltar contexto crítico (ex: volume esperado de linhas, padrão de leitura vs escrita), pergunte antes de recomendar algo que dependa fortemente disso.
