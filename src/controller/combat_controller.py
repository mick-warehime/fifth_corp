from controller.communication import SignalsAccess
from model import CombatModel
from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
from cards import Card
from typing import List

from model.combat_model import CombatData


class CombatController(QWidget, SignalsAccess):

    def __init__(self, data: CombatData) -> None:
        super(QWidget, self).__init__()
        loadUi('src/view/combat.ui', self)
        self._data = data
        self.combat_model = CombatModel()
        self.update_display()
        self.hand: List[Card] = []
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

    def create_deck(self) -> None:
        for i in range(8):
            c = Card('Card %d' % i, 'Card %d does a thing' % i, self.play_card)
            self.add_card_to_hand(c)

    def update_display(self) -> None:
        self.player_life.setText(
                'Player Life: {}'.format(self.combat_model.player_life))
        self.enemy_life.setText(
                'Enemy Life: {}'.format(self.combat_model.enemy_life))

    def next_scene(self) -> None:
        if self.combat_model.player_dead():
            self.signals.load_scene.emit('start')
        else:
            self.signals.load_scene.emit(self._data.victory_scene)
