import decision_controller
from pyqt.splash_form import Ui_SplashForm
from PyQt5.QtWidgets import QWidget


class SplashController(QWidget, Ui_SplashForm):
    def __init__(self) -> None:
        super(QWidget, self).__init__()
        print(self)
        self.setupUi(self)
        self.newgame_button.clicked.connect(self.change)
        self.newgame_button.setShortcut("N")

    def change(self) -> None:
        self.main = decision_controller.DecisionController()
        self.main.show()
        self.close()
