
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
    stackable = getattr(item.info, 'stackable')
    new_item = deepcopy(item)
    if bag_item(mob) == item_name:
        if stackable:
            print('This was used.')
            edit_item(new_item, item_quantity)
        if not stackable:
            add_multi_items(mob, new_item, item_quantity)
    if bag_item(mob) != item_name:
        if stackable:
            add_item(mob, new_item, item_quantity)
        if not stackable:
            add_multi_items(mob, new_item, item_quantity)

def edit_item(mob, new_item, item_quantity):
    '''
    Sum existant item quantity + new item quantity.
    '''
    for _ in mob:
        quantity = getattr(_.info, 'quantity')
        setattr(new_item.info, 'quantity', item_quantity + quantity)

def add_multi_items(mob, new_item, item_quantity):
    '''
    Add (item x quantity) to bag.
    '''
    for _ in range(item_quantity):
        mob.bag.append(new_item)

def add_item(mob, new_item, item_quantity):
    '''
    
    Checks if item is stackable or not.
    If true, add item and increment item quantity.
    If false, add item multiple times.
    
    '''
    mob.bag.append(new_item)
    setattr(new_item.info, 'quantity', item_quantity)

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
    for item in mob.bag:
        return item.info.name
    return 'No items found in bag.'

bag_append(goblin, bronze_sword, 2)
bag_append(goblin, coins, 100)
bag_append(goblin, coins, 100)
print(f'{goblin.info.name} bag:\n{goblin.bag}')
