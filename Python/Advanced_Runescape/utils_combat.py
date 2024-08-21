# import time
# import threading
from random import randint
# from player import player
# from monster import Monster, MonsterInfo, MonsterExp, MonsterSkills #goblin # spider
# from item import coins, bronze_scimitar

class Combat:

    @staticmethod
    def is_alive(char) -> bool:
        '''
        Check if character is alive.
        Usable in both Monster and Player.
        '''
        return char.health > 0

    @staticmethod
    def damage(char) -> int:
        '''
        Calculate character damage based on strength.
        Damage is equal to:
        0.5 + (strength lvl times random number between 0 and 65) divided by 640.
        '''
        dmg = 0.5 + (char.strength * randint(0, 65) / 640)
        print(f'{char.name} hits {int(round(dmg))} damage.')
        return int(round(dmg))

    @staticmethod
    def fight(char, mob) -> None:
        '''
        Allows Player to fight versus Monster.
        '''
        while cb.is_alive(char) and cb.is_alive(mob):
            print(f'\nFighting {mob.name}:')
            fighting = input('1. Fight\n2. Run\n> ')
            if fighting.lower() in ('2', 'run'):
                print(f'You\'ve ran away from {mob.name}...')
                break
            if fighting.lower() in ('1', 'fight'):
                mob.health -= cb.damage(char)
                print(f'{mob.name} has {mob.health} hp.')
                if not cb.is_alive(mob):
                    print('Monster dies:')
                    del mob
                    break
                char.health -= cb.damage(mob)
                print(f'{char.name} has {char.health} hp.')
                if not cb.is_alive(char):
                    print('Player dies:')
                    break

cb = Combat()

if __name__ == '__main__':
    print('Please run rs3.py instead.')
