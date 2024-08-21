'''
Creates bag utilities. 
'''
from copy import deepcopy
from monster import Monster, goblin
from player import Player, player
from item import Item, coins, bronze_scimitar

class Bag:
    '''
    Using Bag as a static to reuse the same Bag class for both Monster and Player.
    Each instance of Monster/Player have its own bag list.
    '''
    @staticmethod
    def append(char: Monster | Player, item: Item, quantity: int) -> None:
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
        for bag_item in char.bag:
            if bag_item.name == item.name:
                Bag.handle_bag_item(char, bag_item, quantity, new_item)
                break
        else:
            Bag.handle_new_item(char, item, quantity, new_item)

    @staticmethod
    def handle_bag_item(char: Monster | Player, bag_item: Item, quantity: int, new_item: Item) -> None:
        '''
        If there are items in bag edit item.
        If item is stackable, update quantity of item's copy.
        If item is not stackable, create multiple copies of the item.
        '''
        if bag_item.stackable:
            bag_item.quantity += quantity
        if not bag_item.stackable:
            for _ in range(quantity):
                char.bag.append(new_item)

    @staticmethod
    def handle_new_item(char: Monster | Player, item: Item, quantity: int, new_item: Item) -> None:
        '''
        If there are no items in bag create new item.
        If new item is stackable, copy item and update quantity.
        If new item is not stackable, create multiple copies of the item.
        '''
        if item.stackable:
            char.bag.append(new_item)
            new_item.quantity += quantity
        if not item.stackable:
            for _ in range(quantity):
                char.bag.append(new_item)

    @staticmethod
    def remove(char: Monster | Player, item: Item, quantity: int) -> bool:
        '''
        Remove quantity x item from bag.
        '''
        for bag_item in char.bag:
            if bag_item.name == item.name:
                if item.stackable:
                    bag_item.quantity -= quantity
                    return True
                if not item.stackable:
                    for _ in range(quantity):
                        char.bag.remove(bag_item)
                    return True
                break
        else:
            print(f'Bag has no {item.name}.')
            return False

Bag.append(goblin, coins, 4)
Bag.remove(goblin, coins, 4)
print(goblin.bag)

if __name__ == '__main__':
    print('Please run rs3.py instead.')
