from config import load_config
from watcher import start_watcher


def main():

    config = load_config()

    print("=" * 40)
    print(" Smart Notebook iniciado ")
    print("=" * 40)

    print(f"Modelo: {config.model}")
    print(f"Cofres: {len(config.vaults)}")
    print(f"Delay: {config.delay}s")

    start_watcher(
        config.vaults,
        config.delay,
        config.model
    )


if __name__ == "__main__":
    main()