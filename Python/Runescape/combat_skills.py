''' Combat Skills. '''
from combat_skills_xp import CombatSkillsExp

class CombatSkills(CombatSkillsExp):
    ''' Responsible for all combat skills of the Player class. '''
    def __init__(self) -> None:
        super().__init__()
        self.hp: int = 10
        self.atk_lvl: int = 1
        self.str_lvl: int = 1
        self.def_lvl: int = 1

if __name__ == '__main__':
    print(
        'Run runescape_simulation.py instead.'
        )
