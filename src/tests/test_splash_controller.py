"""Tests for splash_controller.py."""
from PyQt5.QtCore import Qt
from unittest.mock import patch

import app
from controller.main_window_controller import MainWindow
from controller.splash_controller import SplashController

app.initialize_globals()


def test_splash_screen_new_clicked_loads_scene(qtbot):
    splash = SplashController()
    main = MainWindow()

    with patch.object(main, 'change_view') as mock_method:
        qtbot.mouseClick(splash.newgame_button, Qt.LeftButton)

    mock_method.assert_called_once()
