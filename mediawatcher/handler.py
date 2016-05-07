from pathlib import Path
from watchdog.events import FileSystemEventHandler


class MediaWatcherHandler(FileSystemEventHandler):
    """
    Simple FSE Handler for watchdog.
    """

    def __init__(self, mover, logger):
        self.mover = mover
        self.logger = logger

    def on_created(self, event):
        self.logger.info('File created: {}'.format(event.src_path))
        self.mover.lookup(Path(event.src_path))

    def on_modified(self, event):
        self.logger.info('File modified: {}'.format(event.src_path))
        self.mover.lookup(Path(event.src_path))