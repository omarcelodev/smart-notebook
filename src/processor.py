from pathlib import Path
from llm import ask_llm
from output import save_organized_note
import requests
import logging

logger = logging.getLogger("smart-notebook")

def read_markdown(file_path: Path) -> str:

    if not file_path.exists():
        logger.warning(f"Arquivo não encontrado: {file_path}")
        return ""
    try:
        with open(
            file_path,
        "r",
        encoding="utf-8"
        ) as file:
            return file.read()
        
    except OSError as e:
        logger.error(f"Falha ao ler arquivo {file_path}: {e}")
        return ""



def process_file(
    file_path: Path,
    model: str,
    overwrite: bool = False
):

    logger.info(f"Lendo: {file_path}")

    content = read_markdown(file_path)

    if not content.strip():
        logger.warning(f"Conteúdo vazio: {file_path}")
        return

    logger.info(f"Enviando conteúdo para IA: {file_path}")
                
    try:
        organized_content = ask_llm(
            content,
            model
        )

    except requests.RequestException as e:
        logger.error(f"Falha ao contatar o modelo: {e}")
        return

    except ValueError as e:
        logger.error(f"Resposta inválida do modelo: {e}")
        return

    logger.info("Salvando resultado")

    output = save_organized_note(
        file_path,
        organized_content,
        overwrite
    )

    if output is None:
        return
    
    logger.info(f"Nota organizada: {output}")