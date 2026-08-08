from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from processor import process_file
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


    def _run_processing(self, file_path):
        self.timers.pop(file_path, None)

        process_file(
            file_path,
            self.model,
            self.overwrite
    )


def start_watcher(vaults: list[str], delay=8, model="", overwrite=False):

    event_handler = MarkdownHandler(
        delay,
        model,
        overwrite
    )
    observer = Observer()

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

        logger.info(f"Monitorando: {vault}")


    observer.start()


    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        logger.info("Encerrando Smart Notebook")
        observer.stop()


    observer.join()