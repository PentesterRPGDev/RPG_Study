''' Responsible script for creating monsters. '''
import pandas as pd
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

class LoadMonster:
    '''
    Loads csv monsters into the game as objects.
    '''
    def create(self, row):
        '''
        Receive each row from monsters database as argument to create monster.
        '''
        return (
            Monster(row[0],
            MonsterSkills(*map(int, row[1:5])),
            MonsterEXP(int(row[5]), float(row[6]))
            ))

load_monster = LoadMonster()
monster_db = pd.read_csv('Python/Runescape/csv/monsters_db.csv')

monsters = []
for index, monster_row in monster_db.iterrows():
    monsters.append(load_monster.create(monster_row.tolist()))

goblin = monsters[0]
print(monsters)
goblin.add_item(('gold coins', 10, 'shiny but useful.', True))
print(goblin.bag)

if __name__ == '__main__':
    print('Please run runescape_simulation.py instead.')
