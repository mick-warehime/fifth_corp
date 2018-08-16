import controller
from model import CombatModel
from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5.uic import loadUi
from cards import Card
from typing import List


class CombatController(QWidget):

    def __init__(self, main_window: QMainWindow) -> None:
        super(QWidget, self).__init__()
        self.main_window = main_window
        loadUi('src/view/combat.ui', self)
        self.combat_model = CombatModel()
        self.update_display()
        self.hand = []
        self.create_deck()

    def add_card_to_hand(self, card: Card) -> None:
        self.hand.append(card)
        self.hand_container.addWidget(card)
        card.show()

    def remove_card_from_hand(self, card: Card) -> None:
        self.hand.remove(card)
        self.hand_container.removeWidget(card)
        card.hide()

    def play_card(self, card: Card) -> None:
        self.remove_card_from_hand(card)
        self.combat_model.player_plays_card(card)
        self.update_display()
        if self.combat_model.combat_over():
            self.next_scene()

    def draw_hand(self) -> None:
        self.create_deck()

    def create_deck(self) -> List[Card]:
        for i in range(8):
            c = Card('Card %d' % i, 'Card %d does a thing' % i, self.play_card)
            self.add_card_to_hand(c)

    def update_display(self):
        self.player_life.setText('Player Life: {}'.format(self.combat_model.player_life))
        self.enemy_life.setText('Enemy Life: {}'.format(self.combat_model.enemy_life))

    def next_scene(self):
        if self.combat_model.player_dead():
            self.main_window.set_view(controller.CombatController(self.main_window))
        else:
            self.main_window.set_view(controller.SplashController(self.main_window))
