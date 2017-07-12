import items
class Player():
    def __init__(self):
        self.currentPlace = "";
        self.hp = 100;
        self.inventory = items.Gold(15)
        self.hunger = 0
        self.alive = True

