''' Responsible script for creating monsters. '''
from random import randint
from monster_skills import MonsterSkills
from monster_exp import MonsterEXP
from utils import util

class Monster():
    ''' Create monsters of runescape '''
    def __init__(self, name: str, skills: MonsterSkills, xp: MonsterEXP) -> None:
        self.name = name
        self.skills = skills
        self.xp = xp
        self.bag: list = []

    def __str__(self) -> str:
        return f'{self.name} spawned.\n'

    def melee_dmg(self) -> int:
        ''' Calculates the melee damage made by the user.'''
        dmg = 0.5 + (self.skills.strength * randint(0, 65) / 640)
        util.slow_txt(
            f'{self.name} hits {int(round(dmg))}.\n'
            )
        return int(round(dmg))

goblin = Monster('Goblin', MonsterSkills(5, 1, 1, 0), MonsterEXP(5, 12.5))
goblin.bag = [
    {'item name': 'Gold Coins', 'quantity': 10},
    {'item name': 'Bronze Sword', 'quantity': 1},
    {'item name': 'Gold Coins', 'quantity': 10},
    {'item name': 'Bronze Arrows', 'quantity': 100}
]

spider = Monster('Spider', MonsterSkills(5, 1, 1, 0), MonsterEXP(5, 12.5))
spider.bag = [
    {'item name': 'Gold Coins', 'quantity': 10},
    {'item name': 'Bronze Sword', 'quantity': 1},
    {'item name': 'Gold Coins', 'quantity': 10},
    {'item name': 'Bronze Arrows', 'quantity': 100}
]

baby_dragon = Monster('Baby Dragon', MonsterSkills(5, 1, 1, 0), MonsterEXP(5, 12.5))
baby_dragon.bag = [
    {'item name': 'Gold Coins', 'quantity': 10000},
    {'item name': 'Rune Sword', 'quantity': 1},
    {'item name': 'Air Runes', 'quantity': 500}
]

if __name__ == '__main__':
    print('Please run runescape_simulation.py instead.')
