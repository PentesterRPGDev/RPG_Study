''' Responsible script to make the player. '''
from random import randint

class Player:
    ''' Create player of runescape. '''
    def __init__(self, name) -> None:
        self.name: str = name
        self.hp: int = 1000000
        self.atk_lvl: int = 1
        self.str_lvl: int = 19999
        self.def_lvl: int = 1
        self.bag: list = [
            {'item name': 'Gold Coins', 'quantity': 0},
            {'item name': 'Bronze Sword', 'quantity': 1}
        ]

    def __str__(self) -> str:
        return f'{self.name} logged in.\n'

    def melee_dmg(self) -> int:
        ''' Calculates the melee damage made by the user.'''
        dmg = 0.5 + (self.str_lvl * randint(0, 65) / 640)
        return int(round(dmg))

user = Player('User')

if __name__ == "__main__":
    print('please run rs3.py instead.')
