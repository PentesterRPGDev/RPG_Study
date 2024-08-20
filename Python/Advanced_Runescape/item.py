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
    ItemInfo('Gold coins', 'Shiny currency', 0, True, False)
    )

bronze_scimitar = Item(
    ItemInfo('Bronze sword', 'A sharp sword.', 1, False, False)
)

if __name__ == '__main__':
    pass
