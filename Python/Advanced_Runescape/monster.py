'''
Responsible for Monster class.
'''
from monster_info import MonsterInfo
from monster_skills import MonsterSkills
from monster_exp import MonsterExp

class Monster:
    '''
    Create Monster object.
    
    Monster object:
    MonsterInfo = name, examine, membership.
    MonsterSkills = health, attack, strength, defense.
    MonsterExp = health_xp, combat_xp
    '''
    def __init__(self, info: MonsterInfo, skills: MonsterSkills, xp: MonsterExp) -> None:
        self.info = info
        self.skills = skills
        self.xp = xp
        self.bag: list = []

    def __str__(self) -> str:
        return f'{self.info.name} has spawned.'

    def __repr__(self) -> str:
        return (
            f'Monster:(\n'
            f'MonsterInfo: {self.info.__dict__},\n'
            f'MonsterSkills: {self.skills.__dict__},\n'
            f'MonsterExp: {self.xp.__dict__}\n)'
        )

    @property
    def health(self):
        '''
        Allow self.health instead of self.skills.health.
        '''
        return self.skills.health

    @health.setter
    def health(self, value):
        '''
        Allow health to update it's value.
        '''
        self.skills.health = value

    @property
    def strength(self):
        '''
        Allow self.strength instead of self.skills.strength,
        '''
        return self.skills.strength

    @property
    def name(self):
        '''
        Allow self.name instead of self.info.name
        '''
        return self.info.name

goblin = Monster(
    MonsterInfo(
        'Goblin', 'An ugly green creature.', False
        ),
    MonsterSkills(
        5, 1, 1, 1
        ),
    MonsterExp(
        5, 12.5
        )
    )

spider = Monster(
    MonsterInfo(
        'Spider', 'Tiny but can use web.', False
    ),
    MonsterSkills(
        3, 1, 1, 1
    ),
    MonsterExp(
        3, 7.5
    )
)

if __name__ == '__main__':
    print('Please run rs3.py instead.')
