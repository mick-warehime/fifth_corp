import controller
from PyQt5.QtWidgets import QMainWindow

def combat_controller():
    m = QMainWindow()
    return controller.CombatController(m)

def test_hello_world(qtbot):
    assert combat_controller() is not None
