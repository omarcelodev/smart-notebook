# Smart Notebook

Organizador automático de notas do Obsidian usando um LLM local (Ollama). Observa cofres configurados, envia cada `.md` modificado para o modelo e grava uma versão estruturada em um arquivo `.organized.md` ao lado do original.

---

## Sumário

- [Funcionalidades](#funcionalidades)
- [Arquitetura](#arquitetura)
- [Estrutura do projeto](#estrutura-do-projeto)
- [Configuração](#configuração)
- [Como executar](#como-executar)
- [Requisitos](#requisitos)
- [Como funciona](#como-funciona)
- [Limitações](#limitações)
- [Licença](#licença)

---

## Funcionalidades

- Monitora um ou mais cofres do Obsidian configurados em `src/config/config.json`.
- Observa alterações em arquivos Markdown (`watchdog`) com **debounce** via `threading.Timer`, evitando reprocessar durante a digitação.
- Ignora arquivos cujo nome já contém `.organized` para evitar loop infinito.
- Envia o conteúdo bruto para um LLM através do endpoint HTTP do Ollama (`/api/chat`).
- Persiste a resposta como `<nome>.organized.md` na mesma pasta do original.
- Nunca inventa conteúdo — o prompt de sistema restringe o modelo a **reorganizar** o que já existe (ver `src/prompts.py`).

## Arquitetura

Fluxo linear, sem framework web ou banco de dados:

```
[watchdog] ──► MarkdownHandler ──► processor ──► llm (Ollama) ──► output (.organized.md)
                  (debounce)         (orquestra)    (HTTP /api/chat)
```

- **Watcher** (`src/watcher.py`) — `FileSystemEventHandler` da lib `watchdog`. Cada `on_modified` agenda um `threading.Timer` cancelável por arquivo; só dispara `process_file` após `delay` segundos sem novas alterações.
- **Processor** (`src/processor.py`) — lê o `.md`, chama o LLM e delega a gravação.
- **LLM** (`src/llm.py`) — monta o payload JSON para `http://localhost:11434/api/chat` com `stream=False` e timeout de 120 s.
- **Output** (`src/output.py`) — escreve `<stem>.organized<suffix>` ao lado do original.
- **Config** (`src/config.py` + `src/config/config.json`) — modelo `pydantic.BaseModel` validado a partir do JSON.
- **Prompts** (`src/prompts.py`) — `SYSTEM_PROMPT` carregado em tempo de execução (sem hardcode).

## Estrutura do projeto

```
smartnotebook/
├── .venv/
├── README.md
└── src/
    ├── main.py                # ponto de entrada (python -m src.main)
    ├── watcher.py             # observer + debounce por arquivo
    ├── processor.py           # lê .md → chama LLM → grava saída
    ├── llm.py                 # cliente HTTP do Ollama (/api/chat)
    ├── output.py              # salva <nome>.organized.md
    ├── prompts.py             # system prompt
    ├── config.py              # modelo pydantic + loader
    └── config/
        └── config.json        # cofres, modelo, delay, extensões
```

## Configuração

Edite `src/config/config.json`:

```json
{
  "version": "0.1.0",
  "vaults": [
    "C:\\Users\\marce\\OneDrive\\Documentos\\Teste automação"
  ],
  "provider": "ollama",
  "model": "minimax-m3:cloud",
  "delay": 8,
  "overwrite": false,
  "extensions": [".md"]
}
```

| Campo        | Tipo        | Descrição                                                                 |
|--------------|-------------|---------------------------------------------------------------------------|
| `vaults`     | `string[]`  | Caminhos absolutos dos cofres a monitorar.                                |
| `provider`   | `string`    | Provedor LLM. Hoje apenas `ollama`.                                       |
| `model`      | `string`    | Nome do modelo conforme registrado no Ollama (`ollama list`).             |
| `delay`      | `int`       | Segundos de espera após a última modificação antes de processar (debounce). |
| `overwrite`  | `bool`      | Reservado para versões futuras — sobrescrever `.organized.md` existente.  |
| `extensions` | `string[]`  | Extensões observadas. Hoje apenas `.md`.                                  |

## Como executar

```bash
# 1. ambiente virtual (já presente em .venv/)
python -m venv .venv
.venv\Scripts\activate

# 2. dependências
pip install -r requirements.txt

# 3. garantir que o Ollama está rodando e o modelo está baixado
ollama serve
ollama pull <modelo-definido-em-config.json>

# 4. iniciar o app (a partir da raiz do projeto)
python -m src.main
```

A saída no console mostra o modelo, a quantidade de cofres e o delay, e segue listando cada arquivo processado. Para encerrar: `Ctrl+C`.

## Requisitos

**Sistema**

- Windows 11 (testado em `10.0.26200`).
- Ollama instalado e em execução em `http://localhost:11434`.
- Modelo previamente baixado (`ollama pull <modelo>`).

**Python**

- Python 3.13.
- Dependências (definidas em `requirements.txt`):
  - `watchdog` — observação de arquivos.
  - `requests` — cliente HTTP para o Ollama.
  - `pydantic` — validação do `config.json`.

**Não funcionais**

- Baixo consumo de RAM (sem estado persistente, sem cache).
- Código modular: trocar de modelo = editar `config.json`.
- Trocar de provedor = ajustar `src/llm.py` (hoje hardcoded em Ollama).

## Como funciona

1. `main.py` carrega `config.json` via `pydantic` e inicia o `Observer` do `watchdog` para cada cofre.
2. Ao detectar `on_modified` em um `.md` cujo stem **não** contenha `.organized`, o handler:
   - Cancela o `Timer` anterior daquele arquivo (se houver).
   - Cria um novo `Timer` para `delay` segundos.
3. Quando o timer expira, `processor.process_file` lê o arquivo, monta a mensagem `{system, user}` e faz `POST /api/chat`.
4. O conteúdo retornado é gravado como `<stem>.organized.md` na mesma pasta.

## Limitações

- Não recursão inteligente: arquivos gerados pelo próprio app (`*.organized.md`) são filtrados pelo nome, não por metadata — renomear manualmente pode causar reprocessamento.
- Provedor Ollama é o único suportado hoje; a URL é constante em `src/llm.py`.
- Sem fila persistente: se o app for encerrado durante um debounce, o evento é perdido.
- Sem testes automatizados ainda.
- `overwrite` é lido do config mas ainda não é aplicado na gravação.

---

## Licença

A definir.