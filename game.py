# game.py
import random

class Game:
    def __init__(self, pokemon1, pokemon2):
        self._pokemon1 = pokemon1
        self._pokemon2 = pokemon2

    def battle(self):
        self._start()
        first, second = self._decide_order()
        winner, loser = self._attack(first, second)
        self._show_result(winner, loser)

    def _start(self):
        print(f'{self._pokemon1.name}があらわれた。{self._pokemon1.name}のHPは{self._pokemon1.hp}で、すばやさは{self._pokemon1.spd}だ。')
        print(f'{self._pokemon2.name}があらわれた。{self._pokemon2.name}のHPは{self._pokemon2.hp}で、すばやさは{self._pokemon2.spd}だ。')

    def _decide_order(self):
        if self._pokemon1.spd > self._pokemon2.spd:
            return (self._pokemon1, self._pokemon2)
        elif self._pokemon2.spd > self._pokemon1.spd:
            return (self._pokemon2, self._pokemon1)
        else:
            return tuple(random.shuffle([self._pokemon1, self._pokemon2]))

    def _attack(self, first, second):
        while True:
            first.attack(second)
            if second.is_fainted():
                return (first, second)

            second.attack(first)
            if first.is_fainted():
                return (second, first)

    def _show_result(self, winner, loser):
        print(f'{loser.name}はたおれた。{winner.name}のかち！')