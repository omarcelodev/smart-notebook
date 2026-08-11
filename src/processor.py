from pathlib import Path
from time import perf_counter
from config import Config
from llm import ask_llm
from output import organized_path, save_organized_note
import requests
import logging

logger = logging.getLogger("smart-notebook")

def read_markdown(file_path: Path) -> str | None:

    if not file_path.exists():
        logger.warning(f"Arquivo não encontrado: {file_path}")
        return None
    try:
        with open(
            file_path,
        "r",
        encoding="utf-8"
        ) as file:
            return file.read()

    except OSError as e:
        logger.error(f"Falha ao ler arquivo {file_path}: {e}")
        return None

    except UnicodeDecodeError as e:
        logger.error(f"Arquivo não está em UTF-8 {file_path}: {e}")
        return None



def process_file(
    file_path: Path,
    config: Config
):

    output_path = organized_path(file_path)

    if output_path.exists() and not config.overwrite:
        logger.info(f"Nota já organizada, pulando: {output_path}")
        return

    logger.info(f"Lendo: {file_path}")

    content = read_markdown(file_path)

    if content is None:
        return

    if not content.strip():
        logger.warning(f"Conteúdo vazio: {file_path}")
        return

    logger.info(f"Enviando conteúdo para IA: {file_path}")

    started = perf_counter()

    try:
        organized_content = ask_llm(
            content,
            config
        )

    except requests.RequestException as e:
        logger.error(f"Falha ao contatar o modelo: {e}")
        return

    except ValueError as e:
        logger.error(f"Resposta inválida do modelo: {e}")
        return

    logger.info(f"Resposta recebida em {perf_counter() - started:.1f}s")

    output = save_organized_note(
        file_path,
        organized_content,
        config.overwrite
    )

    if output is None:
        return

    logger.info(f"Nota organizada: {output}")
