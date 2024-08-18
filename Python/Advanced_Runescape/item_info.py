class ItemInfo:
    def __init__(self, name: str, examine: str, quantity: int, stackable: bool, membership: bool) -> None:
        self.name = name
        self.examine = examine
        self.quantity = quantity
        self.stackable = stackable
        self.membership = membership
