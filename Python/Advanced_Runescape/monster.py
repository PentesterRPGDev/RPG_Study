
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
    '''

    Add item object to the bag and specify the quantity.
    Uses check_item to check if item is stackable or not.

    '''
    item_name = getattr(item.info, 'name')
    for i in mob.bag:
        if i.info.name == item_name:
            check_item(mob, item, item_quantity)
            break
        if i.info.name != item_name:
            check_item(mob, item, item_quantity)
            break
    else:
        check_item(mob, item, item_quantity)

def check_item(mob, item, item_quantity):
    '''
    
    Checks if item is stackable or not.
    If true, add item and increment item quantity.
    If false, add item multiple times.
    
    '''
    new_item = deepcopy(item)
    stackable = getattr(item.info, 'stackable')
    if stackable:
        mob.bag.append(new_item)
        setattr(new_item.info, 'quantitt', item_quantity)
    if not stackable:
        for _ in range(item_quantity):
            mob.bag.append(new_item)

bag_append(goblin, bronze_sword, 2)
bag_append(goblin, coins, 100)
print(f'{goblin.info.name} bag:\n{goblin.bag}')
