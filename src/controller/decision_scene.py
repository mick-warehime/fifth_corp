"""Module for defining and controlling decision scenes."""
from typing import Dict
from typing import List
from typing import NamedTuple

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, \
    QHBoxLayout, QPushButton

from controller.communication import Signals

_IMAGE_DIR = '../data/images/'


class DecisionSceneData(NamedTuple):  # type: ignore
    prompt: str
    image_file: str
    choices: Dict[str, 'DecisionSceneData']


class DecisionControllerV2(QWidget):

    def __init__(self, data: DecisionSceneData, signals: Signals) -> None:
        super().__init__()

        self.signals = signals
        self.buttons: List[QPushButton] = []

        top_half = self._prompt_box(data.prompt, data.image_file)
        bottom_half = self._decisions_box(data.choices)

        layout = QVBoxLayout()
        layout.addLayout(top_half)
        layout.addLayout(bottom_half)

        self.setLayout(layout)

    def _change_scene(self, data: DecisionSceneData) -> None:
        self.signals.emit(data)

    def _decisions_box(self,
                       choices: Dict[str, DecisionSceneData]) -> QVBoxLayout:
        decision_box = QVBoxLayout()
        for description, scene_data in choices.items():
            qbtn = QPushButton(description, self)
            qbtn.clicked.connect(lambda: self._change_scene(scene_data))
            qbtn.resize(qbtn.sizeHint())
            self.buttons.append(qbtn)
            decision_box.addWidget(qbtn)

        qbtn_final = QPushButton('Quit', self)
        qbtn_final.clicked.connect(QApplication.instance().quit)
        qbtn_final.resize(qbtn_final.sizeHint())
        decision_box.addWidget(qbtn_final)

        return decision_box

    def _prompt_box(self, prompt: str, image_file: str) -> QHBoxLayout:
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


def example_scene_data() -> DecisionSceneData:
    _PROMPT_0 = (
        'You come upon a derelict charging station. Some lights flicker inside'
        ' and your sensors detect motion within. Your audioscopes fainly'
        ' sense an alarm signal.')
    _IMAGE_0 = 'derelict_store.png'
    _PROMPT_1 = (
        'The place is empty but seems to have been recently occupied. '
        'You find some small loot on the ground and see a working power '
        'outlet.')
    _IMAGE_1 = ''
    _PROMPT_2 = (
        'The place is crawling with small robo-mites! A tech-robot is '
        'trapped under some fallen debris and is currently in the process'
        ' of being disassembled. It emits a weak distress beacon, asking'
        ' for help.')
    _IMAGE_2 = ''
    scene_1 = DecisionSceneData(_PROMPT_1, _IMAGE_1, {})
    scene_2 = DecisionSceneData(_PROMPT_2, _IMAGE_2, {})
    scene_0 = DecisionSceneData(_PROMPT_0, _IMAGE_0, {'Investigate': scene_1,
                                                      'Robo-mites': scene_2})
    return scene_0
