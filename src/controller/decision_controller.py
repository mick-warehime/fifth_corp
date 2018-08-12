import combat_controller
import splash_controller
from pyqt.decision_form import Ui_DecisionForm
from PyQt5.QtWidgets import QWidget
import logging


class DecisionController(QWidget, Ui_DecisionForm):
    def __init__(self) -> None:
        super(QWidget, self).__init__()
        logging.debug(self)
        self.setupUi(self)
        self.fight_button.clicked.connect(self.change)
        self.back_button.clicked.connect(self.back)

    def change(self) -> None:
        self.main = combat_controller.CombatController()
        self.main.show()
        self.close()

    def back(self) -> None:
        self.main = splash_controller.SplashController()
        self.main.show()
        self.close()
