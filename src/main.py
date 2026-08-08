from logging import config

from config import load_config
from watcher import start_watcher
from logger import setup_logger

logger = setup_logger()

def main():

    config = load_config()

    logger.info("Smart Notebook iniciado")
    logger.info(f"Modelo: {config.model}")
    logger.info(f"Cofres: {len(config.vaults)}")
    logger.info(f"Delay: {config.delay}s")

    start_watcher(
        config.vaults,
        config.delay,
        config.model,
        config.overwrite
    )


if __name__ == "__main__":
    main()