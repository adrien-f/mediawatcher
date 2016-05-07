import sys
import time
from collections import namedtuple
from pathlib import Path

from logbook import Logger, StreamHandler
from watchdog.observers import Observer

from mediawatcher.handler import MediaWatcherHandler
from mediawatcher.mover import MediaWatcherMover

MediaWatcherConfig = namedtuple('MediaWatcherConfig', ['watch', 'output_anime', 'output_tv', 'output_movies', 'mock'])


class MediaWatcher(object):

    default_config = {
        'mock': False
    }

    def __init__(self, config):
        self.config = MediaWatcherConfig(**config)
        StreamHandler(sys.stdout).push_application()
        self.logger = Logger('MediaWatcher')
        self.mover = MediaWatcherMover(self.config, self.logger)
        self.handler = MediaWatcherHandler(self.mover, self.logger)
        self.observer = Observer()
        self.setup_watch()

    def startup(self):
        self.logger.info('Performing initial scan.')
        self.mover.scan()
        self.logger.info('Initial scan done, ready to watch {} folder{}.'.format(len(self.config.watch), 's' if len(
            self.config.watch) != 1 else ''))

    def setup_watch(self):
        for directory in self.config.watch:
            path = Path(directory)
            if not path.is_dir():
                raise FileNotFoundError('Directory {} not found on system.'.format(directory))
            self.observer.schedule(self.handler, str(path), recursive=True)

    def watch(self):
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()





