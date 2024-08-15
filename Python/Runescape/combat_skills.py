''' Combat Skills. '''
from combat_skills_exp import CombatSkillsExp

class CombatSkills(CombatSkillsExp):
    ''' Responsible for all combat skills of the Player class. '''
    def __init__(self) -> None:
        super().__init__()
        self.health: int = 10
        self.attack: int = 1
        self.strength: int = 1
        self.defense: int = 1

    def __str__(self) -> str:
        return (
        'Total combat levels:\n'
        f'health lvl: {self.health}. xp: {self.health_xp}.\n'
        f'attack lvl: {self.attack}. xp: {self.attack_xp}.\n'
        f'strength lvl: {self.strength}. xp: {self.strength_xp}.\n'
        f'defense lvl: {self.defense}. xp: {self.defense_xp}.\n'
        )

if __name__ == '__main__':
    print(
        'Run runescape_simulation.py instead.'
        )
