---
name: meeting-summarizer
description: >
  Use esta skill sempre que o usuário pedir para resumir uma reunião (transcrição/ata), um PDF, um artigo, ou uma documentação técnica. Exemplos de gatilho - "resume essa reunião", "resume esse PDF", "faz um resumo desse artigo", "resume essa documentação". Gera um resumo estruturado adaptado ao tipo de conteúdo (reunião vs material de leitura), destacando decisões, ações e pontos-chave. Não use para gerar documentação nova do zero (isso é a documentation-writer) — esta skill resume conteúdo já existente.
---
 
# Meeting Summarizer

Skill para resumir conteúdo já existente — reuniões, PDFs, artigos e documentações — adaptando o formato ao tipo de material. Diferente da `documentation-writer`, que **cria** documentação nova, esta skill **resume** algo que já existe.

## Tipo 1: Reuniões (transcrição ou ata)

Estrutura de saída:

```markdown
## Resumo da Reunião
 
**Participantes:** [se identificável]
**Data:** [se identificável]
 
### Principais pontos discutidos
- [ponto 1]
- [ponto 2]
 
### Decisões tomadas
- [decisão 1]
- [decisão 2]
 
### Ações / Próximos passos
- [ ] [ação] — responsável: [nome, se identificável]
- [ ] [ação] — responsável: [nome, se identificável]
 
### Pendências / Pontos em aberto
- [o que ficou sem decisão definitiva e precisa ser retomado]
```

- Separe claramente **decisão tomada** de **ideia discutida mas não decidida** — isso é o erro mais comum em resumo de reunião e pode gerar mal-entendido.
- Se não houver responsável claro para uma ação, marque como "a definir" em vez de assumir alguém.

## Tipo 2: PDFs / Artigos / Documentações (material de leitura)

Estrutura de saída:

```markdown
## Resumo: [título do material]
 
**Tipo:** [artigo / paper / documentação técnica / etc]
 
### Ideia central
[1-3 frases — o que o material defende ou explica, no nível mais alto]
 
### Principais pontos
- [ponto 1]
- [ponto 2]
 
### Conceitos/termos importantes
- **[termo]**: [definição curta, se o material define algo técnico relevante]
 
### Conclusão / Takeaway
[o que fazer com essa informação, ou a conclusão do autor]
```

- Para documentação técnica (ex: docs de API, biblioteca), priorize: o que a ferramenta faz, como usar (exemplo mínimo), e limitações/gotchas mencionados.
- Para artigos/papers, diferencie claramente fato apresentado pelo autor de opinião/interpretação do autor.

## Regras gerais (copyright e fidelidade)

- **Nunca reproduza trechos extensos do material original.** Resuma com suas próprias palavras; cite no máximo frases muito curtas quando a formulação exata for essencial (ex: uma definição técnica precisa).
- Não invente conclusão ou decisão que não está no material — se algo for ambíguo no original, diga isso em vez de resolver a ambiguidade por conta própria.
- Para materiais longos (ex: PDF de várias páginas), pode estruturar o resumo por seção/capítulo em vez de um bloco único, se isso ajudar a navegação.
- Pergunte o nível de detalhe esperado se o usuário não especificar (resumo executivo de poucas linhas vs resumo completo estruturado) apenas quando o material for muito longo e a ambiguidade for relevante — para a maioria dos casos, assuma o formato estruturado padrão acima.
- Markdown compatível com Obsidian quando o usuário pedir para salvar como nota (linha em branco antes de tabelas, etc).
