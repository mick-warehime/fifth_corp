from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5.uic import loadUi
import controller


class MainWindowController(QMainWindow):

    def __init__(self) -> None:
        super(QMainWindow, self).__init__()
        loadUi('src/view/main_window.ui', self)
        self.set_view(controller.SplashController(self))

    def set_view(self, widget: QWidget) -> None:
        self.takeCentralWidget()
        self.setCentralWidget(widget)
