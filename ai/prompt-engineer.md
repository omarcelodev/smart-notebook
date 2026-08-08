---
name: prompt-engineer
description: >
  Use esta skill sempre que o usuário pedir para melhorar um prompt, criar ou estruturar um agente de IA, desenhar um workflow envolvendo LLMs, ou organizar/estruturar contexto para um modelo. Exemplos de gatilho - "melhora esse prompt", "como faço esse prompt funcionar melhor", "cria um agente que faça...", "desenha um workflow com LLM para...", "como estruturo o contexto pra essa IA". Não use para perguntas genéricas sobre o que é IA ou LLM - apenas quando o usuário está construindo ou refinando algo prático (prompt, agente, workflow).
---
 
# Prompt Engineer

Skill para melhorar prompts, desenhar agentes de IA, estruturar workflows com LLMs e organizar contexto. Foco em técnica concreta, não teoria genérica sobre "o que é prompt engineering".

## 1. Melhorar prompts

Ao receber um prompt para melhorar, analise nesta ordem:

- **Clareza e especificidade** — o prompt deixa claro o que é esperado como resultado? Remova ambiguidade.
- **Estrutura** — separar instruções, contexto e exemplos com tags claras (ex: XML tags como `<contexto>`, `<tarefa>`, `<formato>`) ajuda o modelo a distinguir as partes.
- **Exemplos (few-shot)** — se a tarefa tem um formato de saída específico, 1-3 exemplos bons ajudam mais do que explicação longa.
- **Raciocínio passo a passo** — para tarefas complexas, peça explicitamente para o modelo pensar antes de responder (chain-of-thought), em vez de pedir a resposta direto.
- **Formato de saída** — especifique formato exato esperado (JSON, Markdown, tamanho, tom) se isso importa pro uso final.
- **Negativo vs positivo** — prefira dizer o que fazer ("responda em 3 bullets") em vez de só o que não fazer ("não responda muito longo").
Apresente a versão melhorada do prompt junto com uma lista curta do que foi mudado e por quê — não troque o prompt sem explicar a razão de cada ajuste.

## 2. Criar agentes

Ao desenhar um agente de IA, defina:

- **Papel/persona** — o que o agente é e não é (escopo claro evita comportamento genérico demais).
- **Ferramentas disponíveis** — quais tools o agente tem acesso, e quando deve usar cada uma (não só listar, mas dar critério de decisão).
- **Limites/guardrails** — o que o agente nunca deve fazer, e o que fazer quando não tiver certeza (pedir confirmação vs agir e avisar).
- **Formato de output esperado** — se o agente alimenta outro sistema, especifique o formato exato (JSON com schema, por exemplo).
- **Critério de sucesso** — como saber se o agente está funcionando bem (isso ajuda a desenhar os testes depois).

## 3. Workflows com LLM

Ao desenhar um workflow (sequência de chamadas a LLM, possivelmente com múltiplos agentes ou etapas):

- Identifique se o caso pede **um agente único** com várias tools, ou **múltiplas etapas/agentes especializados** encadeados (mais controle e previsibilidade, mas mais complexidade).
- Desenhe o fluxo em diagrama Mermaid (flowchart), mostrando entrada → etapas de processamento → saída, e onde há decisão condicional.
- Para cada etapa, defina: o que entra, o que sai, e qual modelo/configuração faz sentido (ex: uma etapa de classificação simples não precisa do modelo mais caro/poderoso).
- Considere pontos de falha: o que acontece se uma etapa falhar ou retornar algo inesperado (validação, retry, fallback).

## 4. Estruturar contexto

Ao organizar contexto para um modelo (ex: para um system prompt longo, ou RAG):

- Separe claramente: instruções permanentes (papel, regras) vs contexto variável (dados específicos da consulta) vs exemplos.
- Para contexto longo, coloque informação mais importante/instruções no início e no fim (efeito de "recência e primazia" em janelas de contexto grandes).
- Se for RAG, pense em como os chunks recuperados serão apresentados ao modelo (formato, ordenação por relevância, citação da fonte).
- Evite redundância de informação repetida em múltiplos lugares do contexto sem necessidade — isso desperdiça espaço e pode confundir o modelo sobre qual versão seguir.

## Regras gerais

- Seja direto e prático — mostre o prompt/estrutura final, não um ensaio sobre teoria de prompt engineering.
- Sempre que possível, explique o "porquê" da técnica usada (ex: "separei em tags porque X") — o usuário está aprendendo a área, não só pedindo solução pronta.
- Se o usuário não especificar qual modelo/plataforma vai usar (Claude, GPT, etc), pode assumir Claude como padrão dado o contexto, mas mencione se algo é específico de uma plataforma.
