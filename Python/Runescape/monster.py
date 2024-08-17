''' Responsible script for creating monsters. '''
import csv
from random import randint
from monster_skills import MonsterSkills
from monster_exp import MonsterEXP
from utils import util

class Monster:
    '''
    Create monster class. 
    '''
    def __init__(self, name: str, skills: MonsterSkills, xp: MonsterEXP) -> None:
        self.name = name
        self.skills = skills
        self.xp = xp
        self.bag: list = []

    def __str__(self) -> str:
        return f'{self.name} spawned.\n'

    def __repr__(self) -> str:
        return (
            f'\nname: {self.name}\nhealth: {self.skills.health}'
            f'\nattack: {self.skills.attack}\nstrength: {self.skills.strength}'
            f'\ndefense: {self.skills.defense}\nhealth_xp: {self.xp.health_xp}'
            f'\ncombat_xp: {self.xp.combat_xp}\n'
            )

    def add_item(self, item: list) -> None:
        ''' Allows adding items to the bag. '''
        return self.bag.append(item)

    def melee_dmg(self) -> int:
        ''' Calculates the melee damage made by the user.'''
        dmg = 0.5 + (self.skills.strength * randint(0, 65) / 640)
        util.print_slow_txt(
            f'{self.name} hits {int(round(dmg))}.\n'
            )
        return int(round(dmg))

class MakeMonsters:
    ''' Loads csv monsters into the game as objects. '''
    def create(self, row):
        ''' Receive row as argument to create monster. '''
        return (
            Monster(row[0],
            MonsterSkills(*map(int, row[1:5])),
            MonsterEXP(int(row[5]), float(row[6]))
            ))

create_monster = MakeMonsters()
with open('csv/monsters_db.csv', 'r', encoding='utf-8') as file:
    monsters_data = list(csv.reader(file))
    monsters_data.pop(0)

monsters = []
for monster_row in monsters_data:
    monsters.append(create_monster.create(monster_row))

goblin = monsters[0]
spider = monsters[1]
print(goblin.bag)
goblin.add_item(('gold coins', 10, 'shiny but useful.', True))
print(goblin.bag)

if __name__ == '__main__':
    print('Please run runescape_simulation.py instead.')
