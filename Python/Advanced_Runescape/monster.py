
from copy import deepcopy
from monster_info import MonsterInfo
from monster_skills import MonsterSkills
from monster_exp import MonsterExp
from item import coins, bronze_sword

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

print(goblin.bag)
print(spider.bag)

def bag_append(mob, item, item_quantity):
    stackable = getattr(item.info, 'stackable')
    item_name = getattr(item.info, 'name')
    new_item = deepcopy(item)
    for i in mob.bag:
        if i.info.name == item_name:
            if stackable:
                mob.bag.append(new_item)
                setattr(new_item.info, 'quantity', item_quantity)
                break
            if not stackable:
                for _ in range(item_quantity):
                    mob.bag.append(new_item)
        if i.info.name != item_name:
            if stackable:
                mob.bag.append(new_item)
                setattr(new_item.info, 'quantity', item_quantity)
                break
            if not stackable:
                for _ in range(item_quantity):
                    mob.bag.append(new_item)
    else:
        if stackable:
            mob.bag.append(new_item)
            setattr(new_item.info, 'quantity', item_quantity)
        if not stackable:
            for _ in range(item_quantity):
                mob.bag.append(new_item)

bag_append(goblin, bronze_sword, 2)
bag_append(goblin, coins, 100)
print(f'{goblin.info.name} bag:\n{goblin.bag}')
