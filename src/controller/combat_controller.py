from pyqt.combat_form import Ui_CombatForm
from PyQt5.QtWidgets import QWidget


class CombatController(QWidget, Ui_CombatForm):
    def __init__(self) -> None:
        super(QWidget, self).__init__()
        self.setupUi(self)
