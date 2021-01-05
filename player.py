"""This script will have the player class and will control how the player will interact with the rest of the game"""
import items
import world
import random
import colorama
from colorama import Fore, Style


colorama.init(autoreset=True)


class Player:
	"""This is the player class. This class defines the player and its attributes."""
	def __init__(self):
		self.victory = False
		self.kindness = False
		self.inventory = [items.Hand(), items.RustySword(), items.CrustyBread()]
		self.x = world.start_tile_location[0]
		self.y = world.start_tile_location[1]
		self.gold = 50
		self.crystals = 5
		self.name = ""
		self.hp = 100
		self.score = 0

	def is_alive(self):
		"""This function checks if the player is alive"""
		return self.hp > 0

	def move(self, dx, dy):
		"""This function moves the player on the map. This function is used in other functions
		 to move in particular directions"""
		self.x += dx
		self.y += dy

	def move_north(self):
		"""This function moves the player one tile to the north(one tile upwards)"""
		self.move(dx=0, dy=-1)

	def move_east(self):
		"""This function moves the player one tile to the east(one tile to the right)"""
		self.move(dx=1, dy=0)

	def move_south(self):
		"""This function moves the player one tile to the south(one tile downwards)"""
		self.move(dx=0, dy=1)

	def move_west(self):
		"""This function moves the player one tile to the west(one tile to the left)"""
		self.move(dx=-1, dy=0)

	def print_inventory(self):
		"""This function displays all the items in the player's inventory"""
		print("")
		print(f"{Style.BRIGHT}Inventory")
		for item in self.inventory:
			print("* " + str(item))
		print(f"{Fore.YELLOW}Gold: {self.gold}")
		print(f"{Fore.CYAN}Crystals: {self.crystals}")
		print("")

	def print_details(self):
		"""The function will return  and print all of the player's details"""
		print("")

		def get_details(self_param):
			"""This function will get the player's details"""
			keys = list(vars(self_param).keys())
			values = list(vars(self_param).values())
			i: int = 6
			detail_list: list = []
			for x in range(len(keys) - 7):
				i += 1
				a = f"{keys[i]} : {values[i]}"
				detail_list.append(a)

			return detail_list

		details = get_details(self)
		print(f"{Style.BRIGHT}Player Details")
		for attribute in details:
			print("* " + attribute)
		print("")

	def most_powerful_weapon(self):
		"""This function returns the weapon in the player's inventory that has the most damage"""
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
		"""This function returns the item in the player's inventory with the most defence """
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
		"""This function is called whenever the player and the enemy meet. This function makes the player
		attack the enemy. This function also rewards the player if they are victorious"""
		best_weapon = self.most_powerful_weapon()

		room = world.tile_at(self.x, self.y)
		enemy = room.enemy

		# The player attacking the enemy
		print(f"\nYou use a {best_weapon} against the {Fore.LIGHTRED_EX}{enemy.name}")
		try:
			affect_type = best_weapon.enchantment.type_affect
			if enemy.type in affect_type:
				try:
					attack_multiplier = best_weapon.enchantment.damage_multiplier()
					defence_multiplier = 0.1 * enemy.defence
					damage_dealt = (best_weapon.damage * attack_multiplier) - (best_weapon.damage * defence_multiplier)
					enemy.hp = round(enemy.hp, 0) - round(damage_dealt, 0)
				except AttributeError:
					defence_multiplier = 0.1 * enemy.defence
					damage_dealt = best_weapon.damage - best_weapon.damage * defence_multiplier
					enemy.hp = round(enemy.hp, 0) - round(damage_dealt, 0)
		except AttributeError:
			defence_multiplier = 0.1 * enemy.defence
			damage_dealt = best_weapon.damage - best_weapon.damage * defence_multiplier
			enemy.hp = round(enemy.hp, 0) - round(damage_dealt, 0)

		if not enemy.is_alive():
			print(f"You killed the {Fore.LIGHTRED_EX}{enemy.name}")
			amount = enemy.reward
			self.gold += amount
			self.score += enemy.score
			print(f"You receive {Fore.YELLOW}{amount} gold")
			amount = random.randint(0, 2)
			if amount == 0:
				pass
			else:
				self.crystals += amount
				print(f"You receive {Fore.CYAN}{amount} crystals")
		else:
			print(f"{Fore.LIGHTRED_EX}{enemy.name}{Fore.RESET}, has {Fore.LIGHTRED_EX}{round(enemy.hp, 0)} HP {Fore.RESET}remaining")

	def heal(self):
		"""This function is used when the player wants to recover hp. The function will check for consumables and
		recover hp using the consumables that the player has in its inventory"""
		consumables = [item for item in self.inventory if isinstance(item, items.Consumable)]
		if not consumables:
			print("You do not have any items to heal you\n")
			return

		print("Choose at item to use to heal")
		for i, item in enumerate(consumables, 1):
			print(f"{i}.{item}")

		choice = None
		valid = False
		while not valid and choice not in ["Q", "q"]:
			choice = input("")
			try:
				to_eat = consumables[int(choice) - 1]
				self.hp = round(min(100, self.hp + to_eat.healing_value), 0)
				self.inventory.remove(to_eat)
				print(f"Current HP: {Fore.GREEN}{round(self.hp, 0)}")
				valid = True
			except(ValueError, IndexError):
				if choice in ["Q", "q"]:
					return
				else:
					print(f"{Style.BRIGHT}Invalid choice, Try again\n")

	def trade(self):
		"""This function is used when the player wishes to trade with a trader"""
		room = world.tile_at(self.x, self.y)
		room.check_if_trade(self)

	def enchant(self):
		"""This function is used when the player wishes to enchant an item """
		room = world.tile_at(self.x, self.y)
		room.check_if_enchant(self)

	def talk(self):
		"""This function is used when the player wants to talk and initiate a quest"""
		room = world.tile_at(self.x, self.y)
		room.talk(self)

	def converse(self):
		"""This function is used when the player wants to converse with story telling NPCs"""
		room = world.tile_at(self.x, self.y)
		room.converse(self)
