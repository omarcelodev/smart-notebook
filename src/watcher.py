from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from processor import process_file
import hashlib
import time
import threading
import logging

logger = logging.getLogger("smart-notebook")

class MarkdownHandler(FileSystemEventHandler):

    def __init__(self, delay=8, model="", overwrite=False):
        self.delay = delay
        self.model = model
        self.overwrite = overwrite
        self.timers = {}
        self.hashes = {}
        self.processing = set()
        self.lock = threading.RLock()

    def on_created(self, event):
        self.on_modified(event)

    def on_modified(self, event):
        if event.is_directory:
            return

        file_path = Path(event.src_path)

        if ".organized" in file_path.stem:
            return

        if file_path.suffix != ".md":
            return

        with self.lock:
            self._schedule(file_path)


    def _schedule(self, file_path):
        # Cancela o timer anterior desse arquivo
        if file_path in self.timers:
            self.timers[file_path].cancel()

        # Cria um novo timer
        timer = threading.Timer(
            self.delay,
            self._run_processing,
            args=[file_path]
        )

        self.timers[file_path] = timer
        timer.start()


    def _file_hash(self, file_path):
        try:
            return hashlib.sha256(
                file_path.read_bytes()
            ).hexdigest()

        except FileNotFoundError:
            # Arquivo apagado/renomeado durante o debounce: normal, não é erro
            logger.warning(f"Arquivo não encontrado: {file_path}")
            return None

        except OSError as e:
            logger.error(f"Falha ao ler arquivo {file_path}: {e}")
            return None


    def _run_processing(self, file_path):

        with self.lock:
            self.timers.pop(file_path, None)

            # Já tem uma chamada em voo pra esse arquivo: reagenda
            if file_path in self.processing:
                logger.info(f"Processamento em andamento, reagendando: {file_path}")
                self._schedule(file_path)
                return

            digest = self._file_hash(file_path)

            if digest is None:
                return

            if self.hashes.get(file_path) == digest:
                logger.info(f"Conteúdo inalterado, pulando: {file_path}")
                return

            self.processing.add(file_path)

        try:
            process_file(
                file_path,
                self.model,
                self.overwrite
            )

            with self.lock:
                self.hashes[file_path] = digest

        except Exception:
            logger.exception(f"Erro inesperado ao processar {file_path}")

        finally:
            with self.lock:
                self.processing.discard(file_path)


def start_watcher(vaults: list[str], delay=8, model="", overwrite=False):

    event_handler = MarkdownHandler(
        delay,
        model,
        overwrite
    )
    observer = Observer()

    monitored = 0

    for vault in vaults:

        path = Path(vault)

        if not path.exists():
            logger.warning(f"Cofre não encontrado: {vault}")
            continue

        observer.schedule(
            event_handler,
            str(path),
            recursive=True
        )

        monitored += 1

        logger.info(f"Monitorando: {vault}")


    if monitored == 0:
        raise SystemExit("Nenhum cofre válido para monitorar")


    observer.start()


    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        logger.info("Encerrando Smart Notebook")
        observer.stop()


    observer.join()
