''' Create runescape simulation game. '''
from player import user
from monster import goblin, spider, baby_dragon
from utils import util
from combat import cbt

if __name__ == '__main__':
    util.slow_txt(f'\n{user}')
    util.slow_txt(f'\n{goblin}')
    util.slow_txt(f'\n{spider}')
    util.slow_txt(f'\n{baby_dragon}')
    util.xp_up(user, 125)
    print(
        f'\n{user.name} has killed 10 goblins and earned 125xp.'
    )
    print(
        f'Total hp xp: {user.hp_xp}.'
        )
    util.lvl_up(user, 1)
    print(
        f'Congratulation {user.name} you advanced hp lvl to {user.hp_lvl}!!!'
        )
    # cbt.melee(user, goblin)
    # util.check_bag(user)
    # cbt.melee(user, spider)
    # util.check_bag(user)
    # cbt.melee(user, baby_dragon)
    # util.check_bag(user)
