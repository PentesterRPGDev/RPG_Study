from item_info import ItemInfo

class Item:
    def __init__(self, info: ItemInfo) -> None:
        self.info = info

    def __str__(self) -> str:
        return f'Item {self.info.name} has been created.'

    def __repr__(self) -> str:
        return (
            f'Item:(\n'
            f'ItemInfo:{self.info.__dict__}\n)'
        )

coins = Item(
    ItemInfo('gold coins', 'shiny currency', 1, True, False)
    )
bag = []
bag.append(coins)
bag.append(coins)
print(coins)
print(f'{coins!r}')