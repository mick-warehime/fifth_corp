"""Controller for handling the main game window."""

from PyQt5.QtWidgets import QMainWindow, QWidget
from controller.communication import SignalsAccess
from controller.factory import build_scene
from controller.splash_controller import SplashController
from model.scene_library import ScenesAccess

_WINDOW_WIDTH = 800
_WINDOW_HEIGHT = 600


class MainWindow(QMainWindow, ScenesAccess, SignalsAccess):

    def __init__(self) -> None:
        super().__init__()

        self.setGeometry(200, 200, _WINDOW_WIDTH, _WINDOW_HEIGHT)

        self.signals.load_scene.connect(self._build_and_change_scene)

        self.change_view(SplashController())

    def _build_and_change_scene(self, scene_name: str) -> None:
        data = self.library.get_scene_data(scene_name)
        self.change_view(build_scene(data))

    def change_view(self, widget: QWidget) -> None:
        self.resize(widget.size().width(), widget.size().height())
        self.takeCentralWidget()
        self.setCentralWidget(widget)
        self.show()
