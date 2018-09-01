import sys

from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication
from PyQt5.uic import loadUi
import controller
from controller.communication import Signals
from controller.decision_scene import DecisionSceneData, DecisionControllerV2, example_scene

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


class MainWindow(QMainWindow):

    def __init__(self, initial_scene_data: DecisionSceneData) -> None:
        super().__init__()

        self.setGeometry(200, 200, _WINDOW_WIDTH, _WINDOW_HEIGHT)

        self.comm = Signals()
        self.comm.load_decision_scene.connect(self._change_view_decision)

        self._change_view_decision(initial_scene_data)

    def _change_view_decision(self, scene_data: DecisionSceneData) -> None:
        self.change_view(DecisionControllerV2(scene_data, self.comm))

    def change_view(self, widget: QWidget) -> None:
        self.current = widget
        self.takeCentralWidget()
        self.setCentralWidget(widget)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main_window = MainWindow(example_scene())

    sys.exit(app.exec_())
