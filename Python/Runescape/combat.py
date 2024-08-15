''' Responsible for combat mechanics of runescape. '''
from utils import util
from player import user

class Combat:
    ''' Responsible class for combat. '''
    @staticmethod
    def is_alive(character) -> bool:
        ''' Check if character is alive. '''
        return character.hp > 0

    @staticmethod
    def melee(char, mob) -> None:
        ''' Responsible for melee fights. '''
        util.slow_txt(
            f'{char.name} is fighting {mob.name}.\n'
            )
        while cbt.is_alive(char):
            util.slow_txt(
                f'{mob.name} has {mob.hp} hp. '
                f'{char.name} has {char.hp} hp.\n'
                )
            mob.hp -= char.melee_dmg()
            if not cbt.is_alive(mob):
                util.slow_txt(
                    f'{mob.name} is dead.\n\n'
                    f'{char.name} has earned {mob.xp} atk xp '
                    f'and {mob.hp_xp} hp xp.\n'
                    )
                util.xp_up(user, 'atk', mob.xp)
                util.xp_up(user, 'hp', mob.hp_xp)
                util.drop(mob, char)
                break
            if not cbt.is_alive(char):
                util.slow_txt(
                    f'You died fighting against {mob.name}.'
                    )
                break
            char.hp -= mob.melee_dmg()

cbt = Combat()

if __name__ == '__main__':
    print('please run runescape_simulation.py instead.')
