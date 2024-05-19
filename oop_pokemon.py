# oop_pokemon.py
from game import Game
from pokemon import Pikachu, Hitokage, Zenigame
import random

pikachu = Pikachu()
hitokage = Hitokage()
zenigame = Zenigame()
pokemons = [pikachu, hitokage, zenigame]
two_pokemons = random.sample(pokemons, 2)

game = Game(two_pokemons[0], two_pokemons[1])
game.battle()
