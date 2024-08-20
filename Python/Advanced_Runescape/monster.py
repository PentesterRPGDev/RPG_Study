from copy import deepcopy
from monster_info import MonsterInfo
from monster_skills import MonsterSkills
from monster_exp import MonsterExp
from item import Item, coins, bronze_scimitar

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

#goblin.bag.append(coins)

def bag_append(mob: Monster, item: Item, quantity: int) -> None:
    '''
    Create a copy of class Item.
    Avoid having same object in different monsters.

    Received Arguments:
    mob: Monster = Monster.
    item: Item = Item.
    quantity: int = Quantity.

    Used Arguments:
    new_item: Item = Create a copy of the item.
    '''
    new_item = deepcopy(item)
    for bag_item in mob.bag:
        if bag_item.name == item.name:
            if bag_item.stackable:
                bag_item.quantity += quantity
            if not bag_item.stackable:
                for _ in range(quantity):
                    mob.bag.append(new_item)
                break
    if not bag_item in mob.bag:
        print('Doing fine.')

def handle_existent_item():
    '''
    If there are items in bag with the same name.
    If item is stackable, update quantity of item's copy.
    If item is not stackable, create multiple copies of the item.
    '''
    pass

def handle_new_item():
    '''
    If there are no items in bag.
    If new item is stackable, copy item and update quantity.
    If new item is not stackable, create multiple copies of the item.
    '''
    pass

bag_append(goblin, bronze_scimitar, 2)
bag_append(goblin, coins, 100)
print(f'{goblin.info.name} bag:\n{goblin.bag}')
