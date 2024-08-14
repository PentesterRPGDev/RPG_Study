''' Responsible for xp count in combat skills. '''

class CombatSkillsExp:
    ''' Class that takes care of xp. '''
    def __init__(self) -> None:
        self.hp_xp: int = 0
        self.atk_xp: int = 0
        self.str_xp: int = 0
        self.def_xp: int = 0

    def __str__(self) -> str:
        return f'Hp xp: {self.hp_xp}.'

if __name__ == '__main__':
    print(
        'Run runescape_simulation.py instead.'
    )
