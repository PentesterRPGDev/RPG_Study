
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
goblin.bag.append(coins)

def bag_append(mob, item, item_quantity):
    '''

    Add item object to the bag and specify the quantity.
    Uses check_item to check if item is stackable or not.

    '''
    item_name = getattr(item.info, 'name')
    for _ in range(item_quantity):
        if bag_item(mob) == item_name:
            print("Item found inside bag.")
            check_item(mob, item, item_quantity)
            break
        if bag_item(mob) != item_name:
            print('Item was not found in bag.')
            check_item(mob, item, item_quantity)
            break


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
        setattr(new_item.info, 'quantity', item_quantity)
    if not stackable:
        for _ in range(item_quantity):
            mob.bag.append(new_item)


class Test:
    def add_item(self, mob, item, item_quantity) -> None:
        item_name = getattr(item.info, 'name')
        stackable = getattr(item.info, 'quantity')
        new_item = deepcooy(item)


def handle_existant_item(mob, item):
    if bag_item(mob) == item_name(item):
        

def handle_new_item(mob, item):
    if bag_item(mob) != item_name(item):
        if stackable:
            mob.bag.append(new_item)
            change_quantity(new_item)
        if not stackable:
            for _ in range(item_quantity):
                mob.bag.append

def bag_item(mob) -> str:
    '''

    Bag_item:
    Inside monster bag: list.
    Check name of item: class Item.info.name.
    If bag has items:
        Return item name: str.
    If bag has no items:
    Return: 'No items found in bag.': str.

    '''
    for bag_item in mob.bag:
        return bag_item.info.name
    return 'No items found in bag.'

bag_append(goblin, bronze_sword, 2)
bag_append(goblin, coins, 100)
bag_append(goblin, coins, 100)
print(f'{goblin.info.name} bag:\n{goblin.bag}')
print(bag_item(goblin))
