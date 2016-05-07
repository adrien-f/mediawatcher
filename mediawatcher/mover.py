import shutil
from pathlib import Path

from guessit import guessit


class MediaWatcherMover(object):
    """
    Where the magic happens.

    Either scan a given list of folders or lookup a specific file.
    """
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger

    def scan(self):
        """
        Recursively scan a list of folders.
        """
        paths = [Path(directory) for directory in self.config.watch]

        def recursive(r_path):
            self.logger.info('Scanning {}'.format(r_path))
            for child in r_path.iterdir():
                if child.is_dir():
                    recursive(child)
                self.lookup(child)

        for path in paths:
            recursive(path)

        self.logger.info('Done scanning.')

    def lookup(self, path):
        """
        Dispatch the path based on the guess of its type
        :param path: The path to look up
        """
        if set(path.suffixes).isdisjoint({'.mkv', '.mp4', '.avi'}):
            self.logger.info('File ignored: {}'.format(path))
            return
        guess = guessit(str(path))
        if guess['type'] == 'movie':
            self.lookup_movie(path, guess)
        elif guess['type'] == 'episode':
            if 'season' not in guess:
                self.lookup_anime(path, guess)
            else:
                self.lookup_tv(path, guess)

    def lookup_movie(self, path, guess):
        self.logger.info('Looking up movie: {}'.format(path))
        move_folder = Path(self.config.output_movies) / Path(guess['title'])
        if not move_folder.exists():
            move_folder.mkdir()
        move_path = move_folder / Path('{}.{}'.format(guess['title'], guess['container']))
        if move_path.exists():
            raise FileExistsError('{} already exists, ignoring.'.format(move_path))
        if not self.config.mock:
            shutil.move(path, str(move_path))
        self.logger.info('Moved movie from {} to {}'.format(path, move_path))

    def lookup_tv(self, path, guess):
        self.logger.info('Looking up tv episode: {}'.format(path))
        move_folder = Path(self.config.output_tv) / Path(guess['title'])
        if not move_folder.exists():
            move_folder.mkdir()
        move_folder /= Path('Season {:02d}'.format(guess['season']))
        if not move_folder.exists():
            move_folder.mkdir()
        move_path = move_folder / Path(
            '{} s{:02d}e{:02d}.{}'.format(guess['title'], guess['season'], guess['episode'], guess['container']))
        if move_path.exists():
            raise FileExistsError('{} already exists, ignoring.'.format(move_path))
        if not self.config.mock:
            shutil.move(path, str(move_path))
        self.logger.info('Moved tv episode from {} to {}'.format(path, move_path))

    def lookup_anime(self, path, guess):
        self.logger.info('Looking up anime episode: {}'.format(path))
        move_folder = Path(self.config.output_anime) / Path(guess['title'])
        if not move_folder.exists():
            move_folder.mkdir()
        move_path = move_folder / Path(
                '{} - {:02d}.{}'.format(guess['title'], guess['episode'], guess['container']))
        if move_path.exists():
            raise FileExistsError('{} already exists, ignoring.'.format(move_path))
        if not self.config.mock:
            shutil.move(path, str(move_path))
        self.logger.info('Moved anime episode from {} to {}'.format(path, move_path))
