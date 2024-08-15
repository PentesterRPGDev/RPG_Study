''' Create runescape simulation game. '''
from player import user
from monster import goblin, spider, baby_dragon
from utils import util
from combat import cbt

if __name__ == '__main__':
    util.slow_txt(
        f'\n{user}'
        f'\n{goblin}'
        f'\n{spider}'
        f'\n{baby_dragon}'
        )
    cbt.melee(user, goblin)
    print(
        f'{user.name} has a total of {user.atk_xp} xp in atk '
        f'and a total of {user.hp_xp} xp in hp.\n'
        )
    util.check_bag(user)
    cbt.melee(user, spider)
    print(
        f'{user.name} has a total of {user.atk_xp} xp in atk '
        f'and a total of {user.hp_xp} xp in hp.\n'
        )
    util.check_bag(user)
