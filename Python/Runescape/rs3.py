''' Create runescape simulation game. '''
from player import user
from monster import goblin, green_dragon
from utils import util
from combat import cbt

if __name__ == '__main__':
    print(user)
    print(goblin)
    print(green_dragon)
    cbt.melee(user, goblin)
    util.check_bag(user)
    cbt.melee(user, green_dragon)
    util.check_bag(user)
