from PyQt5.QtWidgets import QMainWindow, QWidget


class WidgetController(QWidget):
    def __init__(self, main_window: QMainWindow) -> None:
        super(QWidget, self).__init__()
        self.main_window = main_window
