from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5.uic import loadUi


class CombatController(QWidget):
    def __init__(self, main_window: QMainWindow) -> None:
        super(QWidget, self).__init__()
        self.main_window = main_window
        loadUi('src/view/combat.ui', self)
