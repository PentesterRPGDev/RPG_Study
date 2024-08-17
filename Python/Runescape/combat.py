''' Responsible for combat mechanics of runescape. '''
from utils import util

class Combat:
    ''' Responsible class for combat. '''
    @staticmethod
    def c_is_alive(char) -> bool:
        ''' Check if main character is alive. '''
        return char.health > 0

    @staticmethod
    def m_is_alive(mob) -> bool:
        ''' Check if monster is alive. '''
        return mob.skills.health > 0

    @staticmethod
    def melee(char, mob) -> None:
        ''' Responsible for melee fights. '''
        util.print_slow_txt(
            f'{char.name} is fighting {mob.name}.\n'
            )
        while cbt.c_is_alive(char):
            util.print_slow_txt(
                f'{mob.name} has {mob.skills.health} hp. '
                f'{char.name} has {char.health} hp.\n'
                )
            mob.skills.health -= char.melee_dmg()
            if not cbt.m_is_alive(mob):
                util.print_slow_txt(
                    f'{mob.name} is dead.\n\n'
                    f'{char.name} has earned {int(mob.xp.combat_xp)} atk xp '
                    f'and {int(mob.xp.health_xp)} hp xp.\n'
                    )
                util.xp_up(char, 'hp', mob)
                util.xp_up(char, 'atk', mob)
                util.xp_up(char, 'str', mob)
                util.xp_up(char, 'def', mob)
                util.drop(mob, char)
                break
            char.health -= mob.melee_dmg()
            if not cbt.c_is_alive(char):
                util.print_slow_txt(
                    f'You died fighting against {mob.name}.\n'
                    )
                break
        else:
            util.print_slow_txt(
                f'{char.name} has no health. You can\'t fight.\n'
                )


cbt = Combat()

if __name__ == '__main__':
    print('please run runescape_simulation.py instead.')
