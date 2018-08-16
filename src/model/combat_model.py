class CombatModel(object):

    def __init__(self):
        self.player_life = 10
        self.enemy_life = 10
        self.player_turn = True

    def player_plays_card(self, card):
        self.enemy_life = self.enemy_life - 5
        self.player_turn = False
        self.enemy_plays_card()

    def enemy_plays_card(self):
        self.player_life = self.player_life - 1
        self.player_turn = True

    def combat_over(self):
        return self.player_dead() or self.enemy_dead()

    def player_dead(self):
        return self.player_life <= 0

    def enemy_dead(self):
        return self.enemy_life <= 0
