''' Responsible script to make the player. '''
from os import system
from random import randint
from combat_skills import CombatSkills
from gathering_skills import GatheringSkills
from utils import util

class Player(CombatSkills, GatheringSkills):
    ''' Create player of runescape. '''
    def __init__(self, name: str = '', active_melee_skill: int = 0) -> None:
        super().__init__()
        GatheringSkills.__init__(self)
        self.name = name
        self.combat_skills: CombatSkills = CombatSkills()
        self.gathering_skills: GatheringSkills = GatheringSkills()
        self.active_melee_skill = active_melee_skill
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

    @property
    def active_melee_skill(self) -> int:
        '''

        Getter for atk, str, def skill as active.
        Activate melee skill based on user choice. 
        
        '''
        return self._active_melee_skill

    @active_melee_skill.setter
    def active_melee_skill(self, choice: str) -> None:
        '''
        Setter for active melee skill.
        Rule: Only 1 of the 3 skills can be choosen.
        '''
        while True:
            choice = input(
                'Choose a melee skill to train:\n'
                '1: If you want to train atk.\n'
                '2: If you want to train str.\n'
                '3: If you want to train def.\n> '
                )
            if choice in ("1"):
                self._active_melee_skill = self.atk_lvl
                break
            if choice in ("2"):
                self._active_melee_skill = self.str_lvl
                break
            if choice in ("3"):
                self._active_melee_skill = self.def_lvl
                break
            if choice not in ('1', '2', '3'):
                print('Invalid choice.')

    def melee_dmg(self) -> int:
        ''' Calculates the melee damage made by the user.'''
        dmg = 0.5 + (self.str_lvl * randint(0, 65) / 640)
        util.slow_txt(
            f'{self.name} hits {int(round(dmg))}.\n'
            )
        return int(round(dmg))

system('clear')
user = Player()
system('clear')

if __name__ == "__main__":
    print('please run runescape_simulation.py instead.')
