# Smart Notebook

Organizador automático de notas do Obsidian usando um LLM local (Ollama). Observa os cofres configurados, envia cada `.md` modificado para o modelo e grava uma versão estruturada em `<nome>.organized.md` ao lado do original.

---

## Sumário

- [Funcionalidades](#funcionalidades)
- [Como funciona](#como-funciona)
- [Estrutura do projeto](#estrutura-do-projeto)
- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Configuração](#configuração)
- [Como executar](#como-executar)
- [Limitações](#limitações)
- [Licença](#licença)

---

## Funcionalidades

- Monitora um ou mais cofres do Obsidian (recursivamente) definidos em `src/config/config.json`.
- Reage a criação e modificação de arquivos `.md` com **debounce** por arquivo, evitando reprocessar durante a digitação.
- Ignora arquivos cujo nome já contém `.organized`, evitando loop infinito.
- Compara o **hash SHA-256** do conteúdo antes de chamar o modelo: se nada mudou de fato, pula o arquivo.
- Evita chamadas concorrentes para o mesmo arquivo — se já houver uma em andamento, o evento é reagendado.
- Respeita a flag `overwrite`: com `false`, notas já organizadas não são reprocessadas nem sobrescritas.
- Nunca inventa conteúdo — o system prompt restringe o modelo a **reorganizar** o que já existe (`src/prompts.py`).
- Logging estruturado no console (`data | nível | mensagem`), incluindo o tempo de resposta do modelo.

## Como funciona

Fluxo linear, sem framework web e sem banco de dados:

```
[watchdog] ──► MarkdownHandler ──► processor ──► llm (Ollama) ──► output
              (debounce + hash)   (orquestra)   (HTTP /api/chat)  (.organized.md)
```

1. `main.py` carrega e valida o `config.json` e inicia um `Observer` do `watchdog` para cada cofre existente. Se nenhum cofre for válido, o app encerra.
2. Ao detectar criação/modificação de um `.md` cujo nome **não** contenha `.organized`, o handler cancela o timer anterior daquele arquivo e agenda um novo para `delay` segundos.
3. Quando o timer dispara, o handler calcula o hash do arquivo. Se for igual ao último processado, ignora.
4. `processor.process_file` verifica se a saída já existe (respeitando `overwrite`), lê o Markdown e envia `{system, user}` para `POST <ollama_url>` com `stream: false` e o `timeout` definido na configuração.
5. A resposta é gravada como `<nome>.organized.md` na mesma pasta do original.

Módulos:

| Arquivo | Responsabilidade |
|---|---|
| `src/main.py` | Ponto de entrada: carrega config, loga o resumo e inicia o watcher. |
| `src/watcher.py` | `FileSystemEventHandler` com debounce, hash e controle de concorrência. |
| `src/processor.py` | Lê o `.md`, chama o LLM, trata erros e delega a gravação. |
| `src/llm.py` | Cliente HTTP do Ollama (`/api/chat`), com URL e timeout vindos da config. |
| `src/output.py` | Monta o caminho `<nome>.organized.md` e salva o resultado. |
| `src/config.py` | Modelo `pydantic` + carregamento do `config.json`. |
| `src/prompts.py` | `SYSTEM_PROMPT` do organizador de notas. |
| `src/logger.py` | Configuração do logging. |

## Estrutura do projeto

```
smartnotebook/
├── LICENSE
├── README.md
└── src/
    ├── main.py
    ├── watcher.py
    ├── processor.py
    ├── llm.py
    ├── output.py
    ├── prompts.py
    ├── config.py
    ├── logger.py
    └── config/
        ├── config.example.json   # modelo versionado
        └── config.json           # config real (ignorada pelo Git)
```

## Requisitos

- Windows (desenvolvido e testado no Windows 11).
- Python 3.13.
- [Ollama](https://ollama.com) instalado e rodando (por padrão em `http://localhost:11434`), com o modelo já baixado.
- Dependências Python: `watchdog`, `requests`, `pydantic`.

## Instalação

```bash
python -m venv .venv
.venv\Scripts\activate
pip install watchdog requests pydantic
```

## Configuração

Copie o exemplo e edite com os seus caminhos:

```bash
copy src\config\config.example.json src\config\config.json
```

```json
{
    "version": "0.1.0",
    "vaults": [
        "C:\\Caminho\\Para\\Seu\\Cofre"
    ],
    "model": "minimax-m3:cloud",
    "delay": 8,
    "overwrite": false,
    "ollama_url": "http://localhost:11434/api/chat",
    "timeout": 120
}
```

| Campo | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `version` | `string` | sim | Versão do arquivo de configuração. |
| `vaults` | `string[]` | sim | Caminhos absolutos dos cofres a monitorar (barras invertidas escapadas). Cofres inexistentes são avisados e ignorados. |
| `model` | `string` | sim | Nome do modelo conforme o `ollama list`. |
| `delay` | `int` | sim | Segundos de espera após a última modificação antes de processar (debounce). |
| `overwrite` | `bool` | sim | Se `true`, reprocessa e sobrescreve o `.organized.md` existente. |
| `ollama_url` | `string` | não | Endpoint de chat do Ollama. Default: `http://localhost:11434/api/chat`. Útil para apontar para o Ollama de outra máquina ou porta. |
| `timeout` | `int` | não | Segundos de espera pela resposta do modelo. Default: `120`. |

Os cinco primeiros campos são obrigatórios: o `pydantic` falha na inicialização se algum estiver faltando ou com o tipo errado. `ollama_url` e `timeout` podem ser omitidos e caem no default.

## Como executar

Com o Ollama em execução e o modelo baixado:

```bash
ollama pull <modelo-definido-no-config.json>
python src/main.py
```

> Execute pela raiz do projeto. Os módulos usam imports simples, então o entrypoint é `src/main.py` (e não `python -m src.main`).

O console mostra o modelo, a quantidade de cofres, o delay e depois cada arquivo processado. Para encerrar: `Ctrl+C`.

## Limitações

- Apenas Ollama é suportado (a URL é configurável, mas o formato de payload e resposta é o da API do Ollama).
- Arquivos gerados pelo app são filtrados pelo nome (`.organized`), não por metadados — renomear manualmente pode causar reprocessamento.
- Sem fila persistente: se o app for encerrado durante o debounce, o evento é perdido. O cache de hashes também vive apenas em memória.
- Só processa arquivos em UTF-8; outros encodings são registrados como erro e ignorados.
- Sem testes automatizados.

## Licença

[MIT](LICENSE) © 2026 Marcelo Gomes
