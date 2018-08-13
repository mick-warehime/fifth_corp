from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5.uic import loadUi
from .decision_controller import DecisionController


class SplashController(QWidget):
    def __init__(self, main_window: QMainWindow) -> None:
        super(QWidget, self).__init__()
        self.main_window = main_window
        loadUi('src/view/splash.ui', self)
        self.newgame_button.clicked.connect(self.change)
        self.newgame_button.setShortcut("N")

    def change(self) -> None:
        self.main_window.set_view(DecisionController(self.main_window))
