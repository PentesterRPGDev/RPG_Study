'''
Creates bag utilities. 
'''
from copy import deepcopy
from monster import Monster
from item import Item

class Bag:
    '''
    Using Bag as a static to reuse the same Bag class for both Monster and Player.
    Each instance of Monster/Player have its own bag list.
    '''
    @staticmethod
    def append(mob: Monster, item: Item, quantity: int) -> None:
        '''
        Create a copy of class Item.
        Append the copy inside Monster bag list.
        Pros: Avoid having same item in different monsters.
        Pros: Monster can drop two non stackable items with same name.

        Received Args:
        mob: Monster = Monster.
        item: Item = Item.
        quantity: int = Quantity.

        Used Args:
        new_item: Item = Create a copy of the item.
        '''
        new_item = deepcopy(item)
        for bag_item in mob.bag:
            if bag_item.name == item.name:
                Bag.handle_bag_item(mob, bag_item, quantity, new_item)
                break
        else:
            Bag.handle_new_item(mob, item, quantity, new_item)

    @staticmethod
    def handle_bag_item(mob: Monster, bag_item: Item, quantity: int, new_item: Item) -> None:
        '''
        If there are items in bag edit item.
        If item is stackable, update quantity of item's copy.
        If item is not stackable, create multiple copies of the item.
        '''
        if bag_item.stackable:
            bag_item.quantity += quantity
        if not bag_item.stackable:
            for _ in range(quantity):
                mob.bag.append(new_item)

    @staticmethod
    def handle_new_item(mob: Monster, item: Item, quantity: int, new_item: Item) -> None:
        '''
        If there are no items in bag create new item.
        If new item is stackable, copy item and update quantity.
        If new item is not stackable, create multiple copies of the item.
        '''
        if item.stackable:
            mob.bag.append(new_item)
            new_item.quantity += quantity
        if not item.stackable:
            for _ in range(quantity):
                mob.bag.append(new_item)

if __name__ == '__main__':
    print('Please run rs3.py instead.')
