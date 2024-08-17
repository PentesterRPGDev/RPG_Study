''' Create runescape simulation game. '''
from player import user
from monster import goblin, spider
from utils import util
from combat import cbt

if __name__ == '__main__':
    util.print_slow_txt(
        f'{user}\n'
    )
    cbt.melee(user, goblin)
    util.cbt_lvl_up(user)
    util.non_cbt_lvl_up(user)
    cbt.melee(user, spider)
    util.cbt_lvl_up(user)
    util.non_cbt_lvl_up(user)
    util.print_slow_txt(
        f'{user.combat_skills}\n{user.gathering_skills}'
    )
