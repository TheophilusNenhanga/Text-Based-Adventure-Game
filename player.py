"""This file will have the player class and will control how the player will interact with the rest of the game"""
import items
import world
import random


class Player:
    def __init__(self):
        self.inventory = [items.Rock(), items.RustySword(), items.CrustyBread(), items.WoodenShield()]
        self.x = world.start_tile_location[0]
        self.y = world.start_tile_location[1]
        self.hp = 100
        self.gold = 200
        self.victory = False

    def is_alive(self):
        return self.hp > 0

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_west(self):
        self.move(dx=-1, dy=0)

    def print_inventory(self):
        print("")
        print("Inventory")
        for item in self.inventory:
            print("* " + str(item))
        print(f"Gold: {self.gold}")

    def most_powerful_weapon(self):
        max_damage = 0
        best_weapon = None
        for item in self.inventory:
            try:
                if item.damage > max_damage:
                    best_weapon = item
                    max_damage = item.damage
            except AttributeError:
                pass

        return best_weapon

    def most_defence(self):
        max_defence = 0
        best_defence = None
        for item in self.inventory:
            try:
                if item.defence > max_defence:
                    best_defence = item
                    max_defence = item.defence
            except AttributeError:
                pass

        return best_defence

        # The player is attacking the enemy
    def attack(self):
        best_weapon = self.most_powerful_weapon()

        room = world.tile_at(self.x, self.y)
        enemy = room.enemy

        # The player attacking the enemy
        print(f"\nYou use a {best_weapon} against the {enemy.name}")
        try:
            affect_type = best_weapon.enchantment.type_affect
            if enemy.type in affect_type:
                try:
                    attack_multiplier = best_weapon.enchantment.damage_multiplier()
                    defence_multiplier = 0.1 * enemy.defence
                    damage_dealt = (best_weapon.damage * attack_multiplier) - (best_weapon.damage * defence_multiplier)
                    enemy.hp = enemy.hp - damage_dealt
                except AttributeError:
                    defence_multiplier = 0.1 * enemy.defence
                    damage_dealt = best_weapon.damage - best_weapon.damage * defence_multiplier
                    enemy.hp = enemy.hp - damage_dealt
        except AttributeError:
            defence_multiplier = 0.1 * enemy.defence
            damage_dealt = best_weapon.damage - best_weapon.damage * defence_multiplier
            enemy.hp = enemy.hp - damage_dealt

        if not enemy.is_alive():
            print(f"You killed the {enemy.name}")
            amount = random.randint(1,10)
            self.gold += amount
            print(f"You recieve {amount} gold")
        else:
            print(f"{enemy.name}, hp is now {enemy.hp}")

    def heal(self):
        consumables = [item for item in self.inventory if isinstance(item, items.Consumable)]
        if not consumables:
            print("You do not have any items to heal you\n")
            return

        for i, item in enumerate(consumables, 1):
            print("Choose at item to use to heal")
            print(f"{i}.{item}")

        valid = False
        while not valid:
            choice = input("")
            try:
                to_eat = consumables[int(choice) - 1]
                self.hp = min(100, self.hp + to_eat.healing_value)
                self.inventory.remove(to_eat)
                print(f"Current HP: {self.hp}")
                valid = True
            except(ValueError, IndexError):
                print("Invalid choice, Try again\n")

    def trade(self):
        room = world.tile_at(self.x, self.y)
        room.check_if_trade(self)

    def enchant(self):
        room = world.tile_at(self.x, self.y)
        room.check_if_enchant(self)
