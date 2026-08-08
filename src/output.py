from pathlib import Path
import logging

logger = logging.getLogger("smart-notebook")

def save_organized_note(
    original_file: Path,
    content: str,
    overwrite: bool = False
):

    new_name = (
        original_file.stem 
        + ".organized"
        + original_file.suffix
    )

    output_path = original_file.parent / new_name

    if output_path.exists() and not overwrite:
        logger.info(f"Nota já existe, pulando: {output_path}")
        return None
    try:
        with open(
            output_path,
            "w",
            encoding="utf-8"
        ) as file:
            file.write(content)

    except OSError as e:
        logger.error(f"Falha ao salvar nota {output_path}: {e}")

        return None