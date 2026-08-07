# Smart Notebook

## Objetivo

Organizar automaticamente notas do Obsidian utilizando um LLM local (Ollama).

## Funcionalidades

- Monitorar apenas cofres específicos.
- Detectar alterações em arquivos `.md`.
- Esperar alguns segundos após a última alteração (debounce).
- Enviar o conteúdo para um LLM.
- Receber Markdown organizado.
- Salvar o resultado em um arquivo `.smart.md`.
- Nunca inventar conteúdo — apenas reorganizar o que já existe.

## Requisitos funcionais

- Monitorar arquivos Markdown.
- Configurar múltiplos cofres.
- Escolher o modelo do Ollama.
- Criar logs.
- Ignorar arquivos temporários e os próprios `.smart.md` (evitar loop infinito).
- Permitir desligar a automação.

## Requisitos não funcionais

- Rodar em Windows.
- Consumir pouca RAM.
- Código modular.
- Fácil de trocar de modelo.
- Fácil de testar.

## Estrutura

``` nd
app/
├── main.py       # ponto de entrada
├── watcher.py    # observa o cofre
├── processor.py  # debounce + orquestra leitura/LLM/salvar
├── llm.py        # conversa com o Ollama
├── config.py     # configurações (cofres, modelo, tempo de espera)
├── logger.py     # logs
└── utils.py      # funções auxiliares
```

## Como rodar

```bash
pip install -r requirements.txt
python -m app.main   # roda a partir da raiz do projeto (não de dentro de app/)
```
