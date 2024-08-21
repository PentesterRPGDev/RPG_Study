'''
Responsible for player class.
'''
from os import system
from player_info import PlayerInfo
from player_skills import PlayerSkills
from player_exp import PlayerExp

class Player(PlayerSkills, PlayerExp, PlayerInfo):
    '''
    Creates Player class.
    Initiate PlayerSkills and PlayerExp.
    '''
    def __init__(self) -> None:
        super().__init__()
        PlayerExp.__init__(self)
        PlayerInfo.__init__(self)
        self.bag: list = []

    def __str__(self) -> str:
        return f'{self.name} has logged in.'

    def __repr__(self) -> str:
        return (
            f'Player:(\n'
            f'PlayerInfo: [name: {self.name}, examine: {self.examine}, '
            f'membership: {self.membership}],\n'
            f'PlayerSkills: [health: {self.health}, attack: {self.attack}, '
            f'strength: {self.strength}, defense: {self.defense}],\n'
            f'PlayerExp: [health_xp: {self.health_xp}, attack_xp: {self.attack_xp}, '
            f'strength_xp: {self.strength_xp}, defense_xp: {self.defense_xp}]\n)'
        )

    def register(self) -> str:
        '''
        Register Player's name.
        Only accepts letters as nickname.
        '''
        while True:
            print('Only letters are allowed. Nickname must have at least 5 letters.')
            new_user = input('Choose a nickname:\n> ')
            if not new_user.isalpha() and not len(new_user) > 3:
                system('clear')
                print(f'Invalid nickname: {new_user}.\n')
            if new_user.isalpha() and len(new_user) >= 3:
                player.name = new_user.capitalize()
                print(f'{player.name} successfully registered.')
                return player.name

player = Player()

if __name__ == '__main__':
    print('Please run rs3.py instead.')
