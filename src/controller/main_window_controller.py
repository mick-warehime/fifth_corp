import sys

from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication
from PyQt5.uic import loadUi
import controller
from controller.communication import SignalsAccess
from controller.decision_controller import DecisionControllerV2
from model.scene_library import example_scenes_and_resolutions, ScenesAccess

_WINDOW_WIDTH = 800
_WINDOW_HEIGHT = 600


class MainWindowController(QMainWindow):

    def __init__(self) -> None:
        super(QMainWindow, self).__init__()
        loadUi('src/view/main_window.ui', self)
        self.set_view(controller.CombatController(self))

    def set_view(self, widget: QWidget) -> None:
        self.takeCentralWidget()
        self.setCentralWidget(widget)


class MainWindow(QMainWindow, ScenesAccess, SignalsAccess):

    def __init__(self) -> None:
        super().__init__()

        self.setGeometry(200, 200, _WINDOW_WIDTH, _WINDOW_HEIGHT)

        self._current_scene = None
        self.signals.load_scene.connect(self._build_and_change_scene)

        self._build_and_change_scene('start')

    def _build_and_change_scene(self, scene_name: str) -> None:
        data = self.library.get_scene_data(scene_name)
        self._current_scene = DecisionControllerV2(data)

        self.change_view(self._current_scene)

    def change_view(self, widget: QWidget) -> None:
        self.takeCentralWidget()
        self.setCentralWidget(widget)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    SignalsAccess.initialize()
    scenes, resolutions = example_scenes_and_resolutions()
    ScenesAccess.load_library(scenes, resolutions)

    main_window = MainWindow()

    sys.exit(app.exec_())
