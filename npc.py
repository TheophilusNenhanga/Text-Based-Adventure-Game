"""This file will have the npc(non player character) classes and will have their attributes"""

import enchantments
import items
import random


class NonPlayerCharacter:
	def __init__(self):
		self.name = "NonPlayerCharacter"

	def __str__(self):
		return self.name

	all_items = [
		items.CrustyBread(), items.HealingPotion(), items.SharpenedShield(), items.RustySword(),
		items.BattleAxe(), items.MetalClub(), items.ShinySword(), items.BowAndArrow(), items.Mace(),
		items.DefenciveClothing(), items.ReinforcedMetalArmour(), items.ChainMail(), items.StrongHealingPotion(),
		items.SnakeApple(), items.RottenFlesh(), items.Apple()
	]

	# This functions randomly chooses 10 items to be in the trader's inventory
	@classmethod
	def generate_inventory(cls, inventory_to_be_filled):
		for _ in range(10):
			a = NonPlayerCharacter.all_items[random.randint(0, (len(NonPlayerCharacter.all_items) - 1))]
			inventory_to_be_filled.append(a)
		return inventory_to_be_filled


class Trader(NonPlayerCharacter):
	def __init__(self):
		super().__init__()
		self.name = "Trader"
		self.gold = 250
		self.inventory = NonPlayerCharacter.all_items


class Enchanter(NonPlayerCharacter):
	def __init__(self):
		super().__init__()
		self.name = "Enchanter"
		self.inventory = [
			enchantments.Hydration(), enchantments.Dehydration(), enchantments.Honed(), enchantments.Extinguishing(),
			enchantments.Suction()
		]
