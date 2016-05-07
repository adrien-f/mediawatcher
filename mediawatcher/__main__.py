#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse

import yaml

from mediawatcher import MediaWatcher


def main():
    parser = argparse.ArgumentParser(description='Watch directories and move media files accordingly.')
    parser.add_argument('-c', dest='config', help='path to the config file in YAML', required=True)
    args = parser.parse_args()

    with open(args.config) as f:
        config_yaml = yaml.load(f)

    watcher = MediaWatcher({**MediaWatcher.default_config, **config_yaml})
    watcher.startup()
    watcher.watch()

if __name__ == '__main__':
    main()

