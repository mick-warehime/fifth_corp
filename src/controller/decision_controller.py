from typing import Dict, Any, List

from PyQt5.QtGui import QPixmap

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, \
    QApplication, QHBoxLayout, QLabel

from controller.communication import SignalsAccess
from model.decision_scene import DecisionSceneData
from model.resolutions import Choice
from model.scene_library import ScenesAccess

_IMAGE_DIR = 'src/data/images/'


class DecisionController(QWidget, ScenesAccess, SignalsAccess):

    def __init__(self, data: DecisionSceneData, *args: Any,
                 **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        self.buttons: List[QPushButton] = []
        top_half = self._prompt_box(data.prompt, data.image_file)
        bottom_half = self._decisions_box(data.choices)

        layout = QVBoxLayout()
        layout.addLayout(top_half)
        layout.addLayout(bottom_half)

        self.setLayout(layout)

    def _resolve_scene(self, resolution_name: str) -> None:
        res_data = self.library.get_resolution_data(resolution_name)
        resolution = Choice(res_data)
        self.signals.load_scene.emit(resolution.resolve())

    def _decisions_box(self, choices: Dict[str, str]) -> QVBoxLayout:
        bottom_half = QVBoxLayout()

        for description, resolution_name in choices.items():
            qbtn = QPushButton(description, self)
            qbtn.clicked.connect(lambda: self._resolve_scene(resolution_name))
            qbtn.resize(qbtn.sizeHint())
            self.buttons.append(qbtn)
            bottom_half.addWidget(qbtn)

        qbtn_final = QPushButton('Quit', self)
        qbtn_final.clicked.connect(QApplication.instance().quit)
        qbtn_final.resize(qbtn_final.sizeHint())
        self.buttons.append(qbtn_final)
        bottom_half.addWidget(qbtn_final)
        return bottom_half

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
