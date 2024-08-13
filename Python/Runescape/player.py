''' Responsible script to make the player. '''
from random import randint
from combat_skills import CombatSkills
from gathering_skills import GatheringSkills
from utils import util


class Player(CombatSkills, GatheringSkills):
    ''' Create player of runescape. '''
    def __init__(self, name) -> None:
        super().__init__()
        GatheringSkills.__init__(self)
        self.name: str = name
        self.combat_skills: CombatSkills = CombatSkills()
        self.gathering_skills:GatheringSkills = GatheringSkills()
        self.bag: list = [
            {'item name': 'Gold Coins', 'quantity': 0},
            {'item name': 'Bronze Sword', 'quantity': 1}
        ]

    def __str__(self) -> str:
        return f'{self.name} logged in.\n'

    def melee_dmg(self) -> int:
        ''' Calculates the melee damage made by the user.'''
        dmg = 0.5 + (self.str_lvl * randint(0, 65) / 640)
        util.slow_txt(f'{self.name} hits {int(round(dmg))}.\n')
        return int(round(dmg))

user = Player('User')

if __name__ == "__main__":
    print('Please run runescape_simulation.py instead.')
