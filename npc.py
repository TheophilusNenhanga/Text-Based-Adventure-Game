# This file will have the npc(non player character) classes and will have their attributes

import items


class NonPlayerCharacter:
    def __init__(self):
        self.name = "NonPlayerCharacter"

    def __str__(self):
        return self.name


class Trader(NonPlayerCharacter):
    def __init__(self):
        super().__init__()
        self.name = "Trader"
        self.gold = 250
        self.inventory = [items.CrustyBread(), items.HealingPotion(), items.SharpenedShield(), items.RustySword(),
                          items.BattleAxe(), items.MetalClub(), items.ShinySword(), items.BowAndArrow(), items.Mace()]


class Enchanter(NonPlayerCharacter):
    def __init__(self):
        super().__init__()
        self.name = "Enchanter"
        self.gold = 200
        self.inventory = []