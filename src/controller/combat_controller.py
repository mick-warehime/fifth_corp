from PyQt5 import uic

combat_ui = 'src/view/combat.ui'
combat_form, combat_view_class = uic.loadUiType(combat_ui)


class CombatController(combat_view_class, combat_form):
    def __init__(self):
        super(combat_view_class, self).__init__()
        self.setupUi(self)
