from pathlib import Path


def save_organized_note(
    original_file: Path,
    content: str
):

    new_name = (
        original_file.stem 
        + ".organized"
        + original_file.suffix
    )

    output_path = original_file.parent / new_name

    with open(
        output_path,
        "w",
        encoding="utf-8"
    ) as file:
        file.write(content)

    return output_path