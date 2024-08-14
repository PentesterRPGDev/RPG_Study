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
    util.check_bag(user)
    cbt.melee(user, spider)
    util.check_bag(user)
