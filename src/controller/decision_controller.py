import controller
from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5.uic import loadUi


class DecisionController(QWidget):
    def __init__(self, main_window: QMainWindow) -> None:
        super(QWidget, self).__init__()
        self.main_window = main_window
        loadUi('src/view/decision.ui', self)
        self.fight_button.clicked.connect(self.change)
        self.back_button.clicked.connect(self.back)

    def change(self) -> None:
        self.main_window.set_view(controller.CombatController(self.main_window))

    def back(self) -> None:
        self.main_window.set_view(controller.SplashController(self.main_window))
