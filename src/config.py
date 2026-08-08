import json
from pathlib import Path
from pydantic import BaseModel

BASE_DIR = Path(__file__).resolve().parent
CONFIG_PATH = BASE_DIR / "config" / "config.json"


class Config(BaseModel):
    version: str
    vaults: list[str]
    model: str
    delay: int
    overwrite: bool

def load_config() -> Config:
    try:
        data = json.loads(
            CONFIG_PATH.read_text(
                encoding="utf-8"
            )
        )

    except FileNotFoundError:
        raise SystemExit(
            f"❌ Configuração não encontrada: {CONFIG_PATH}"
        )

    except json.JSONDecodeError as e:
        raise SystemExit(
            f"❌ Configuração com JSON inválido: {e}"
        )

    return Config(**data)