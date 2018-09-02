from PyQt5 import QtCore
from controller.decision_scene import DecisionControllerV2
from controller.decision_scene import example_scene_data
from mock import MagicMock


# you need the magic qtbot to run pytest + qt
# https://media.readthedocs.org/pdf/pytest-qt/master/pytest-qt.pdf

def test_load_scene_from_data(qtbot):
    scene_data = example_scene_data()
    scene = DecisionControllerV2(scene_data, None)

    n_choices = len(scene_data.choices)
    n_buttons = len(scene.buttons)

    assert n_buttons == n_choices


def test_clicking_button_emits_signal(qtbot):
    scene_data = example_scene_data()
    scene = DecisionControllerV2(scene_data, MagicMock())

    qtbot.mouseClick(scene.buttons[0], QtCore.Qt.LeftButton)

    scene.signals.emit.assert_called_once()
