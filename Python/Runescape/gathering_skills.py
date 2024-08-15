''' Create gathering skills for the game. '''
from gathering_skills_exp import GatheringSkillsExp

class GatheringSkills(GatheringSkillsExp):
    ''' Create class for gathering skills. '''
    def __init__(self) -> None:
        super().__init__()
        self.woodcutting: int = 1
        self.fishing: int = 1
        self.mining: int = 1

    def __str__(self) -> str:
        return (
            'Total skill levels:\n'
            f'woodcutting lvl: {self.woodcutting}. xp: {self.woodcutting_xp}.\n'
            f'fishing lvl: {self.fishing}. xp: {self.fishing_xp}.\n'
            f'mining lvl: {self.mining}. xp: {self.mining_xp}.\n'
        )

if __name__ == '__main__':
    print('Please run runescape_simulation.py instead.')
