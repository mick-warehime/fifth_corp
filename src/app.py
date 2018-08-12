import sys
import logging
from constants import constants
from PyQt5.QtWidgets import QApplication
from controller import SplashController


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
    app = QApplication(sys.argv)
    controller = SplashController()
    controller.show()
    sys.exit(app.exec_())
