'''
Responsible for Item class.
'''
from item_info import ItemInfo

class Item:
    '''
    Create Item object.
    
    Item object:
    ItemInfo = name, examine, quantity, stackable, membership.
    '''
    def __init__(self, info: ItemInfo) -> None:
        self.info = info

    def __str__(self) -> str:
        return f'Item {self.info.name} has been created.'

    def __repr__(self) -> str:
        return (
            f'Item:(\n'
            f'ItemInfo:{self.info.__dict__}\n)'
        )

    @property
    def name(self) -> str:
        '''
        Get item name.
        '''
        return self.info.name

    @property
    def quantity(self) -> int:
        '''
        Get item quantity.
        Set item quantity + value
        '''
        return self.info.quantity

    @quantity.setter
    def quantity(self, value):
        self.info.quantity = value

    @property
    def stackable(self) -> bool:
        '''
        Get if item is stackable or not.
        '''
        return self.info.stackable

coins = Item(
    ItemInfo('Gold coins', 'Shiny currency', 0, True, False)
)

bronze_scimitar = Item(
    ItemInfo('Bronze sword', 'A sharp sword.', 1, False, False)
)

if __name__ == '__main__':
    print('Please run rs3.py instead.')
