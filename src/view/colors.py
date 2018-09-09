"""Module for setting colors in widgets."""
from enum import Enum

from PyQt5.QtWidgets import QWidget


class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLACK = 'black'

    def set_color(self, widget: QWidget) -> None:
        widget.setStyleSheet('color: {}'.format(self.value))
