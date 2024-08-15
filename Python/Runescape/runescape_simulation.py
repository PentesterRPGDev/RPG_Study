''' Create runescape simulation game. '''
from player import user
from monster import goblin, spider, baby_dragon
from utils import util
# from combat import cbt

if __name__ == '__main__':
    util.slow_txt(
        f'{user}\n{goblin}\n{spider}\n{baby_dragon}\n'
    )
    util.slow_txt(
        f'{user.combat_skills}\n{user.gathering_skills}'
    )
