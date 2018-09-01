import os
import sys
from typing import NamedTuple, Dict, Iterable

from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, \
    QHBoxLayout, QPushButton, QMainWindow

_IMAGE_DIR = '../data/images/'

_PROMPT_0 = (
    'You come upon a derelict charging station. Some lights flicker inside and'
    ' your sensors detect motion within. Your audioscopes fainly sense a '
    ' an alarm signal.')
_IMAGE_0 = 'derelict_store.png'

_PROMPT_1 = ('The place is empty but seems to have been recently occupied. '
             'You find some small loot on the ground and see a working power '
             'outlet.')
_IMAGE_1 = ''

_PROMPT_2 = ('The place is crawling with small robo-mites! A tech-robot is '
             'trapped under some fallen debris and is currently in the process'
             ' of being disassembled. It emits a weak distress beacon, asking'
             ' for help.')
_IMAGE_2 = ''

DecisionSceneData = NamedTuple('DecisionSceneData',
                               [('prompt', str), ('image_file', str),
                                ('choices', Dict[str, 'DecisionSceneData'])])

_WIDTH = 800
_HEIGHT = 600


class Communicator(QObject):
    """
    This is a signal. It has connect and emit methods.
    Usage:

    Suppose there is a function my_fun which takes a DecisionSceneData object
    as input.
    Then:

    load_decision_scene.connect(my_fun)
    links this signal to that function.

    When load_decision_scene.emit(data) is invoked,
    this calls my_fun(data).
    I.e. a signal is sent out containing data, and is received by my_fun.


    """
    load_decision_scene = pyqtSignal(DecisionSceneData)


class MainWindow(QMainWindow):

    def __init__(self, initial_scene_data: DecisionSceneData) -> None:
        super().__init__()

        self.setGeometry(200, 200, _WIDTH, _HEIGHT)

        self.comm = Communicator()
        self.comm.load_decision_scene.connect(self._change_view_decision)

        self._change_view_decision(initial_scene_data)

    def _change_view_decision(self, scene_data: DecisionSceneData) -> None:
        self.change_view(DecisionControllerV2(scene_data, self.comm))

    def change_view(self, widget: QWidget) -> None:
        self.current = widget
        self.takeCentralWidget()
        self.setCentralWidget(widget)
        self.show()


class DecisionControllerV2(QWidget):

    def __init__(self, data: DecisionSceneData, comm: Communicator,
                 *args: Iterable, **kwargs: Dict) -> None:
        super().__init__(*args, **kwargs)

        self.comm = comm

        top_half = self._prompt_box(data.prompt, data.image_file)
        bottom_half = self._decisions_box(data.choices)

        layout = QVBoxLayout()
        layout.addLayout(top_half)
        layout.addLayout(bottom_half)

        self.setLayout(layout)

    def _change_scene(self, data: DecisionSceneData) -> None:
        self.comm.load_decision_scene.emit(data)

    def _decisions_box(self, choices: Dict[str, DecisionSceneData]) -> None:
        bottom_half = QVBoxLayout()
        for description, scene_data in choices.items():
            qbtn = QPushButton(description, self)
            qbtn.clicked.connect(lambda: self._change_scene(scene_data))
            qbtn.resize(qbtn.sizeHint())
            bottom_half.addWidget(qbtn)

        qbtn_final = QPushButton('Quit', self)
        qbtn_final.clicked.connect(QApplication.instance().quit)
        qbtn_final.resize(qbtn_final.sizeHint())
        bottom_half.addWidget(qbtn_final)
        # bottom_half.addStretch(0)
        return bottom_half

    def _prompt_box(self, prompt: str, image_file: str) -> None:
        prompt_label = QLabel(prompt, self)
        prompt_label.setWordWrap(True)

        top_half = QHBoxLayout()
        top_half.addWidget(prompt_label)

        if image_file:
            pic = QLabel(self)
            width = self.window().size().width() * 0.7
            pixmap = QPixmap(_IMAGE_DIR + image_file).scaledToWidth(width)
            pic.setPixmap(pixmap)
            top_half.addWidget(pic)

        return top_half


if __name__ == '__main__':
    scene_1 = DecisionSceneData(_PROMPT_1, _IMAGE_1, {})
    scene_2 = DecisionSceneData(_PROMPT_2, _IMAGE_2, {})
    scene_0 = DecisionSceneData(_PROMPT_0, _IMAGE_0, {'Investigate': scene_1,
                                                      'Robo-mites': scene_2})

    app = QApplication(sys.argv)

    main_window = MainWindow(scene_0)

    sys.exit(app.exec_())
