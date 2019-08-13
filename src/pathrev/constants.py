# -*- coding: utf-8 -*-

"""This module contains all the constants used in pathrev package."""

import os

MODULE_NAME = 'pathrev'
DEFAULT_pathrev_DIR = os.path.join(os.path.expanduser('~'), '.pathrev')
pathrev_DIR = os.environ.get('pathrev_DIRECTORY', DEFAULT_pathrev_DIR)


def get_data_dir() -> str:
    """Ensure the appropriate pathrev data directory exists for the given module, then returns the file path."""
    os.makedirs(pathrev_DIR, exist_ok=True)
    return pathrev_DIR
