'''

Organize monster exp separated for better design.

'''
class MonsterEXP:
    ''' Responsible for all exp drops of the Monster class. '''
    def __init__(self, health_xp: int, combat_xp: float) -> None:
        self.health_xp = health_xp
        self.combat_xp = combat_xp

if __name__ == '__main__':
    print('Please run runescape_simulation.py instead.')
