from typing import NamedTuple

from cards import Card
from model.interface import SceneData


class CombatData(NamedTuple, SceneData):  # type: ignore
    """Placeholder for data defining a combat"""
    victory_scene: str


class CombatModel(object):

    def __init__(self) -> None:
        self.player_life = 10
        self.enemy_life = 10
        self.player_turn = True

    def player_plays_card(self, card: Card) -> None:
        self.enemy_life = self.enemy_life - 5
        self.player_turn = False
        self.enemy_plays_card()

    def enemy_plays_card(self) -> None:
        self.player_life = self.player_life - 1
        self.player_turn = True

    def combat_over(self) -> bool:
        return self.player_dead() or self.enemy_dead()

    def player_dead(self) -> bool:
        return self.player_life <= 0

    def enemy_dead(self) -> bool:
        return self.enemy_life <= 0
