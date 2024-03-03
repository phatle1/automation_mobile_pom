import sys
import time
import inspect
import logging
import builtins
from pathlib import Path
from functools import wraps

from colorlog import ColoredFormatter


class logger:
    def __init__(self, logger, file_level=logging.INFO):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        parent_path = Path(__file__).resolve().parents[1]
        fmt = logging.Formatter('%(asctime)s - %(filename)s:[%(lineno)s] - [%(levelname)s] - %(message)s')
        current_time = time.strftime("%Y-%m-%d_%H-%M-%S")
        log_file_name = f'{parent_path}/logs/log{current_time}.txt'
        # "a" to append the logs in same file, "w" to generate new logs and delete old one

        file_handler = logging.FileHandler(log_file_name, mode="w")
        file_handler.setFormatter(fmt)
        file_handler.setLevel(file_level)
        self.logger.addHandler(file_handler)


log = logger(__name__, logging.INFO)
