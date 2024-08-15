''' Responsible for xp count in combat skills. '''

class CombatSkillsExp:
    ''' Class that takes care of xp. '''
    def __init__(self) -> None:
        self.health_xp: int = 0
        self.attack_xp: int = 0
        self.strength_xp: int = 0
        self.defense_xp: int = 0

if __name__ == '__main__':
    print(
        'Run runescape_simulation.py instead.'
    )
