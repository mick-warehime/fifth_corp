from PyQt5.QtWidgets import QLabel
from PyQt5.uic import loadUi
import logging


class Card(QLabel):

    def __init__(self, name: str, text: str, callback) -> None:
        self.name = name
        self.text = text
        self.callback = callback

        super(Card, self).__init__()
        loadUi('src/view/card.ui', self)
        self.card_name.setText(name)
        self.card_name.setStyleSheet('color: white')
        self.card_text.setText(text)
        self.card_text.setStyleSheet('background: rgba(200,200,200,255)')
        self.card_image.setStyleSheet('background: white')
        self.setStyleSheet('background: gray; selection-background-color: blue')

    def mouseDoubleClickEvent(self, event):
        super(Card, self).mouseDoubleClickEvent(event)
        logging.info('Played: {}'.format(self))
        self.callback(self)

    def enterEvent(self, event):
        logging.info('Hovering over: {}'.format(self))

    def leaveEvent(self, event):
        logging.info('Stopped hovering over: {}'.format(self))

    def __str__(self) -> str:
        return '[{}] {}'.format(self.name, self.text)
