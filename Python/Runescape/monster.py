''' Responsible script for creating monsters. '''
from random import randint
from utils import util


class Monster:
    ''' Create monsters of runescape '''
    def __init__(self, name, hp, atk_lvl, str_lvl, def_lvl, xp) -> None:
        self.name: str = name
        self.hp: int = hp
        self.atk_lvl: int = atk_lvl
        self.str_lvl: int = str_lvl
        self.def_lvl: int = def_lvl
        self.bag: list = []
        self.xp: int = xp

    def __str__(self) -> str:
        return f'{self.name} spawned.\n'

    def melee_dmg(self) -> int:
        ''' Calculates the melee damage made by the user.'''
        dmg = 0.5 + (self.str_lvl * randint(0, 65) / 640)
        util.slow_txt(f'{self.name} hits {int(round(dmg))}.\n')
        return int(round(dmg))

goblin = Monster('Goblin', 5, 1, 1, 0, 5)
goblin.bag = [
    {'item name': 'Gold Coins', 'quantity': 10},
    {'item name': 'Bronze Sword', 'quantity': 1},
    {'item name': 'Gold Coins', 'quantity': 10},
    {'item name': 'Bronze Arrows', 'quantity': 100}
]

spider = Monster('Spider', 5, 1, 1, 0, 5)
spider.bag = [
    {'item name': 'Gold Coins', 'quantity': 10},
    {'item name': 'Bronze Sword', 'quantity': 1},
    {'item name': 'Gold Coins', 'quantity': 10},
    {'item name': 'Bronze Arrows', 'quantity': 100}
]

baby_dragon = Monster('Baby Dragon', 50, 1, 99, 1, 1000)
baby_dragon.bag = [
    {'item name': 'Gold Coins', 'quantity': 10000},
    {'item name': 'Rune Sword', 'quantity': 1},
    {'item name': 'Air Runes', 'quantity': 500}
]

if __name__ == '__main__':
    print('Please run runescape_simulation.py instead.')
