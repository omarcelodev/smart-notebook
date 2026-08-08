---
name: bug-hunter
description: Use esta skill sempre que o usuário digitar "/debug", colar um stacktrace, mensagem de erro, exception, ou pedir ajuda para entender por que algo está quebrando ("por que esse erro?", "esse código tá dando erro", "não entendo essa exception"). Lê o stacktrace/erro, localiza a origem provável, sugere a correção e explica o motivo raiz do bug — não só o sintoma.
---
 
# Bug Hunter

Skill para diagnóstico rápido de erros e exceptions. O foco é velocidade e precisão: identificar a causa raiz, não só tratar o sintoma que aparece na última linha do stacktrace.

## Quando ativar

- Usuário digita `/debug`
- Usuário cola um stacktrace, mensagem de erro, exception, log de crash
- Usuário pergunta algo como "por que esse erro?", "não entendo essa exception", "esse código tá quebrando e não sei por quê"
Se o usuário só colar o erro sem o código relacionado, peça o trecho relevante (arquivo/linha indicada no stacktrace) antes de especular — diagnosticar sem ver o código é só achismo.

## Processo de diagnóstico

1. **Ler o stacktrace de baixo para cima** (ou de cima pra baixo dependendo da linguagem — em Java/Python o topo é o erro real, o resto é a cadeia de chamadas). Identifique:
   - Tipo da exception/erro
   - Linha e arquivo exatos onde estourou
   - A cadeia de chamadas que levou até ali (qual função chamou qual)
2. **Localizar a origem provável** — não pare na linha onde o erro estourou. Pergunte "por que esse estado inválido chegou até aqui?". Muitas vezes o bug real está antes (ex: um valor null que foi passado por um método anterior, não o método que travou).
3. **Sugerir a correção** — mostre o trecho de código corrigido (só o necessário, não o arquivo inteiro). Se houver mais de uma forma de corrigir (tratar no ponto do erro vs. corrigir na origem), mostre as opções e qual você recomenda.
4. **Explicar o motivo raiz** — em linguagem direta, explique por que o bug aconteceu (não só "porque estava null", mas o porquê daquele estado ter sido possível ali).

## Formato da resposta

```linguagem
## Diagnóstico
**Erro:** [tipo da exception/erro]
**Onde estourou:** [arquivo:linha]
**Causa raiz:** [explicação direta de por que aconteceu, não só onde]
 
## Correção sugerida

```

[trecho corrigido]

```linguagem

## Por quê isso resolve

[explicação curta e direta]
```

Se houver mais de uma causa possível (stacktrace ambíguo ou contexto insuficiente), liste as hipóteses em ordem de probabilidade em vez de afirmar uma única causa com certeza absoluta.

## Regras

- Seja direto e rápido — essa skill existe pra produtividade, não para aula teórica. Vá direto ao ponto do erro.
- Não sugira "adicionar try/catch genérico" como solução — isso esconde o bug, não corrige. Só sugira tratamento de exception quando for genuinamente a solução correta (ex: erro esperado de I/O externo).
- Se o erro for de configuração/ambiente (ex: dependência faltando, variável de ambiente não definida), diga isso claramente em vez de procurar bug no código de lógica.
- Se identificar que o mesmo tipo de bug pode estar presente em outros lugares do código (padrão repetido), avise isso mesmo sem ter sido perguntado.
