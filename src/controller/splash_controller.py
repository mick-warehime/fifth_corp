from PyQt5 import uic
import decision_controller

splash_ui = 'src/view/splash.ui'
splash_form, splash_view_class = uic.loadUiType(splash_ui)


class SplashController(splash_view_class, splash_form):
    def __init__(self):
        super(splash_view_class, self).__init__()
        print(self)
        self.setupUi(self)
        self.newgame_button.clicked.connect(self.change)
        self.newgame_button.setShortcut("N")

    def change(self):
        self.main = decision_controller.DecisionController()
        self.main.show()
        self.close()
