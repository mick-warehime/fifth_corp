from game import Game
import logging
import os
from constants import constants


def initialize_logging() -> None:
    log_file = 'logging/example.log'
    try:
        os.remove(log_file)
    except OSError:
        pass

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
