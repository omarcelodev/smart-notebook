import json
from pathlib import Path
from pydantic import BaseModel

BASE_DIR = Path(__file__).resolve().parent
CONFIG_PATH = BASE_DIR / "config" / "config.json"


class Config(BaseModel):
    version: str
    vaults: list[str]
    provider: str
    model: str
    delay: int
    overwrite: bool
    extensions: list[str]


def load_config() -> Config:
    with open(CONFIG_PATH, "r", encoding="utf-8") as file:
        data = json.load(file)

    return Config(**data)