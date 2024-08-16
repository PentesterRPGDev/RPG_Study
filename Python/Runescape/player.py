''' Responsible script to make the player. '''
from os import system
from random import randint
from combat_skills import CombatSkills
from gathering_skills import GatheringSkills
from utils import util

class Player(CombatSkills, GatheringSkills):
    ''' Create player of runescape. '''
    def __init__(self, name: str = '') -> None:
        super().__init__()
        GatheringSkills.__init__(self)
        self.name = name
        self.combat_skills = CombatSkills()
        self.gathering_skills = GatheringSkills()
        self.bag: list = [
            {'item name': 'Gold Coins', 'quantity': 0},
            {'item name': 'Bronze Sword', 'quantity': 1}
        ]

    def __str__(self) -> str:
        return f'{self.name} logged in.\n'

    @property
    def name(self) -> str:
        '''
        
        Get the nickname from setter, accessing the name attribute.
        
        '''
        return self._name

    @name.setter
    def name(self, nickname: str) -> None:
        '''

        Set rules for registering the nickname:
        Check if username contains letters only.
        
        '''
        while True:
            nickname = input('Adventurer nickname:\n> ')
            if not nickname.isalpha():
                util.slow_txt(
                    f'{nickname} is an invalid nickname.\n'
                    'Please do not use digits or symbols.'
                    )
            else:
                self._name = nickname
                break

    def melee_dmg(self) -> int:
        ''' Calculates the melee damage made by the user.'''
        dmg = 0.5 + (self.strength * randint(0, 65) / 640)
        util.slow_txt(
            f'{self.name} hits {int(round(dmg))}.\n'
            )
        return int(round(dmg))

    def xp_up(self, mob_xp: int) -> None:
        ''' Test to fix xp upgrade. '''
        print(f'Test b: {self.combat_skills.health_xp}.')
        self.combat_skills.health_xp += mob_xp
        print(f'Test c: {self.combat_skills.health_xp}\nTest m: {mob_xp}.')

system('clear')
user = Player()
system('clear')

if __name__ == "__main__":
    print('please run runescape_simulation.py instead.')
