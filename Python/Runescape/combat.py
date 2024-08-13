''' Responsible for combat mechanics of runescape. '''
from utils import util

class Combat:
    ''' Responsible class for combat. '''
    @staticmethod
    def is_alive(character) -> bool:
        ''' Check if character is alive. '''
        return character.hp > 0

    @staticmethod
    def melee(char, mob) -> None:
        ''' Responsible for melee fights. '''
        print(f'{char.name} is fighting {mob.name}')
        while cbt.is_alive(char):
            print(f'{mob.name} has {mob.hp} hp.\n{char.name} has {char.hp} hp.\n')
            mob.hp -= char.melee_dmg()
            char.hp -= mob.melee_dmg()
            if not cbt.is_alive(mob):
                print(f'{mob.name} is dead.\n')
                util.drop(mob, char)
                break
            if not cbt.is_alive(char):
                print(f'You died fighting against {mob.name}.')
                break

cbt = Combat()

if __name__ == '__main__':
    print('please run rs3.py instead.')
