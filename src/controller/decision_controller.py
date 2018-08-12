from PyQt5 import uic
import combat_controller
import splash_controller
import logging

decision_ui = 'src/view/decision.ui'
decision_form, decision_view_class = uic.loadUiType(decision_ui)


class DecisionController(decision_view_class, decision_form):
    def __init__(self):
        super(decision_view_class, self).__init__()
        logging.debug(self)
        self.setupUi(self)
        self.fight_button.clicked.connect(self.change)
        self.back_button.clicked.connect(self.back)

    def change(self):
        self.main = combat_controller.CombatController()
        self.main.show()
        self.close()

    def back(self):
        self.main = splash_controller.SplashController()
        self.main.show()
        self.close()
