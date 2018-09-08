"""Tests for resolution_controller.py."""
from PyQt5.QtCore import Qt
from unittest.mock import patch

import app
from controller.decision_controller import DecisionController
from controller.main_window_controller import MainWindow

app.initialize_globals()


def test_decision_controller_choice_resolution(qtbot):
    main = MainWindow()

    main.signals.load_scene.emit('start')

    controller = main.takeCentralWidget()

    assert isinstance(controller, DecisionController)

    with patch.object(main, 'change_view') as mock_method:
        qtbot.mouseClick(controller.buttons[0], Qt.LeftButton)

    mock_method.assert_called_once()
