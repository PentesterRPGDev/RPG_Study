from monster_info import MonsterInfo
from monster_skills import MonsterSkills
from monster_exp import MonsterExp

class Monster:
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

print(goblin)
print(f'{goblin!r}')
