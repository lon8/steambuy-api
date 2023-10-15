class Item:
    def __init__(self, name, cost, item_type):
        self.name = name
        self.cost = cost
        self.item_type = item_type

class Game(Item):
    def __init__(self, name, cost):
        super().__init__(name, cost, "Game")

class GiftCard(Item):
    def __init__(self, cost):
        super().__init__("Gift Card", cost, "Gift Card")