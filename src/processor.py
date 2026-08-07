from pathlib import Path

from llm import ask_llm
from output import save_organized_note


def read_markdown(file_path: Path) -> str:

    if not file_path.exists():
        print(f"⚠️ Arquivo não encontrado: {file_path}")
        return ""
    
    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:
        return file.read()



def process_file(
    file_path: Path,
    model: str
):

    print(f"\n📖 Lendo: {file_path}")

    content = read_markdown(file_path)

    if not content.strip():
        print(f"⚠️ Conteúdo vazio: {file_path}")
        return

    print("🤖 Enviando para IA...")

    organized_content = ask_llm(
        content,
        model
    )

    print("💾 Salvando resultado...")

    output = save_organized_note(
        file_path,
        organized_content
    )

    print(f"✅ Criado: {output}")