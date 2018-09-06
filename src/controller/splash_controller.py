from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.uic import loadUi

from controller.communication import SignalsAccess


class SplashController(QWidget, SignalsAccess):
    def __init__(self) -> None:
        super(QWidget, self).__init__()
        loadUi('src/view/splash.ui', self)
        self.newgame_button.clicked.connect(self._start_game)
        self.newgame_button.setShortcut("N")
        self.quit_button.clicked.connect(QApplication.instance().quit)

    def _start_game(self) -> None:
        self.signals.load_scene.emit('start')
