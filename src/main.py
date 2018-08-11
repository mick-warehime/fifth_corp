from game import Game
import logging
import os
from constants import constants


def clear_log(log_file: str) -> None:
    f = open(log_file, 'r+')
    f.truncate(0)


def initialize_logging() -> None:
    log_file = 'src/logging/game.log'
    clear_log(log_file)

    fmt = "%(asctime)s {} [%(levelname)s]  %(message)s".format(constants.VERSION)
    formatter = logging.Formatter(fmt)
    logger = logging.getLogger()
    logger.setLevel("DEBUG")

    file_logger = logging.FileHandler(log_file)
    file_logger.setFormatter(formatter)
    logger.addHandler(file_logger)

    console_logger = logging.StreamHandler()
    console_logger.setFormatter(formatter)
    logger.addHandler(console_logger)


if __name__ == '__main__':
    initialize_logging()
    g = Game()
    g.run()
