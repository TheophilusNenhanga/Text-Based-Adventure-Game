"""This script will have the world class. It deals with the world map, its dynamics and how it can be interacted with"""
import random
import enemies
import npc
import items
import time
import colorama
from colorama import Fore, Style
import story


colorama.init(autoreset=True)


class MapTile:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.completed = False

	def intro_text(self):
		raise NotImplementedError("Create a subclass instead")

	def modify_player(self, player, mod=None):
		pass


class StartTile(MapTile):
	def intro_text(self):
		return f"""{Fore.LIGHTBLUE_EX}
This is where your journey begins!
Will you be the one to save the village?
        """


class BoringTile(MapTile):
	def intro_text(self):
		return f"""{Style.DIM}
Nothing much happens here.
You must continue onwards.
        """

	def modify_player(self, player, mod=None):
		player.score += 1


class CorridorTile(MapTile):
	def intro_text(self):
		return """
This seems to be a corridor. 
I wonder where it leads. 
		"""

	def modify_player(self, player, mod=None):
		player.score += 1


class VictoryTile(MapTile):
	def modify_player(self, player, mod=None):
		player.victory = True
		player.score += 25

	def intro_text(self):
		return f"""{Fore.LIGHTYELLOW_EX}
You see a bright light in the distance...
...it grows as you get closer!
It's sunlight.
            
Victory is yours!\n 
        """


class FindGoldTile(MapTile):
	def __init__(self, x, y):
		super().__init__(x, y)
		self.gold = random.randint(25, 35)
		self.gold_claimed = False

	def modify_player(self, player, mod=None):
		player.score += 5

		if not self.gold_claimed:
			self.gold_claimed = True
			player.gold = player.gold + self.gold
			print(f"{Fore.YELLOW}+{self.gold} gold added")

	def intro_text(self):
		if self.gold_claimed:
			return """
Another unremarkable part of the cave.
You must forge onwards. 
            """
		else:
			return f"""
Someone dropped some {Fore.YELLOW}gold.{Fore.RESET}
You glance to your left and your right to make sure you are not being watched.
Then you sneakily pick up the {Fore.YELLOW}gold{Fore.RESET}
            """


class FindCrystalTile(MapTile):
	def __init__(self, x, y):
		super().__init__(x, y)
		self.crystals = random.randint(5, 15)
		self.crystal_claimed = False

	def modify_player(self, player, mod=None):
		player.score += 5

		if not self.crystal_claimed:
			self.crystal_claimed = True
			player.crystals = player.crystals + self.crystals
			print(f"{Fore.CYAN}+{self.crystals} crystals added")

	def intro_text(self):
		if self.crystal_claimed:
			return """
You have been here before,
There is nothing new to see here.
			"""
		else:
			return f"""
You see something glowing in the distance
Could it be? {Fore.CYAN}A crystal?{Fore.RESET}
I wonder what you could use that for.
			"""


# Level 1 Enemies
class EnemyTile1(MapTile):
	def __init__(self, x, y):
		r = random.random()
		if r < 0.2:
			self.enemy = enemies.BatSwarm(1)
			self.alive_text = self.enemy.alive_text()
			self.dead_text = self.enemy.dead_text()
		elif r < 0.4:
			self.enemy = enemies.OvergrownInsect(1)
			self.alive_text = self.enemy.alive_text()
			self.dead_text = self.enemy.dead_text()
		elif r < 0.6:
			self.enemy = enemies.SkeletalWarrior(1)
			self.alive_text = self.enemy.alive_text()
			self.dead_text = self.enemy.dead_text()
		elif r < 0.8:
			self.enemy = enemies.GiantSpider(1)
			self.alive_text = self.enemy.alive_text()
			self.dead_text = self.enemy.dead_text()
		elif r < 0.99:
			self.enemy = enemies.Undead(1)
			self.alive_text = self.enemy.alive_text()
			self.dead_text = self.enemy.dead_text()

		else:
			self.enemy = enemies.Lamia(1)
			self.alive_text = self.enemy.alive_text()
			self.dead_text = self.enemy.dead_text()

		super().__init__(x, y)

	def intro_text(self):
		text = self.alive_text if self.enemy.is_alive() else self.dead_text
		return text

	def modify_player(self, player, mod=None):
		# Enemy is attacking the player
		if self.enemy.is_alive():
			try:
				defence_multiplier = 0.1 * player.most_defence().defence
				damage_dealt = self.enemy.damage - self.enemy.damage * defence_multiplier
				player.hp = player.hp - damage_dealt
				print(f"Enemy does {damage_dealt} damage. You have {round(player.hp, 0)} HP remaining\n")
			except AttributeError:
				player.hp = player.hp - self.enemy.damage
				print(f"Enemy does {self.enemy.damage} damage. You have {round(player.hp, 0)} HP remaining\n")

		if not self.enemy.is_alive():
			self.completed = True


# Level 2 Enemies
class EnemyTile2(MapTile):
	def __init__(self, x, y):
		r = random.random()
		if r < 0.2:
			self.enemy = enemies.BatSwarm(2)
			self.alive_text = self.enemy.alive_text()
			self.dead_text = self.enemy.dead_text()
		elif r < 0.4:
			self.enemy = enemies.OvergrownInsect(2)
			self.alive_text = self.enemy.alive_text()
			self.dead_text = self.enemy.dead_text()
		elif r < 0.6:
			self.enemy = enemies.SkeletalWarrior(2)
			self.alive_text = self.enemy.alive_text()
			self.dead_text = self.enemy.dead_text()
		elif r < 0.8:
			self.enemy = enemies.GiantSpider(2)
			self.alive_text = self.enemy.alive_text()
			self.dead_text = self.enemy.dead_text()
		elif r < 0.99:
			self.enemy = enemies.Undead(2)
			self.alive_text = self.enemy.alive_text()
			self.dead_text = self.enemy.dead_text()

		else:
			self.enemy = enemies.Lamia(2)
			self.alive_text = self.enemy.alive_text()
			self.dead_text = self.enemy.dead_text()

		super().__init__(x, y)

	def intro_text(self):
		text = self.alive_text if self.enemy.is_alive() else self.dead_text
		return text

	def modify_player(self, player, mod=None):
		# Enemy is attacking the player
		if self.enemy.is_alive():
			try:
				defence_multiplier = 0.1 * player.most_defence().defence
				damage_dealt = self.enemy.damage - self.enemy.damage * defence_multiplier
				player.hp = player.hp - damage_dealt
				print(f"Enemy does {damage_dealt} damage. You have {round(player.hp, 0)} HP remaining\n")
			except AttributeError:
				player.hp = player.hp - self.enemy.damage
				print(f"Enemy does {self.enemy.damage} damage. You have {round(player.hp, 0)} HP remaining\n")

		if not self.enemy.is_alive():
			self.completed = True


#  Level 3 enemies
class EnemyTile3(MapTile):
	def __init__(self, x, y):
		r = random.random()
		if r < 0.2:
			self.enemy = enemies.BatSwarm(3)
			self.alive_text = self.enemy.alive_text()
			self.dead_text = self.enemy.dead_text()
		elif r < 0.4:
			self.enemy = enemies.OvergrownInsect(3)
			self.alive_text = self.enemy.alive_text()
			self.dead_text = self.enemy.dead_text()
		elif r < 0.6:
			self.enemy = enemies.SkeletalWarrior(3)
			self.alive_text = self.enemy.alive_text()
			self.dead_text = self.enemy.dead_text()
		elif r < 0.8:
			self.enemy = enemies.GiantSpider(3)
			self.alive_text = self.enemy.alive_text()
			self.dead_text = self.enemy.dead_text()
		elif r < 0.99:
			self.enemy = enemies.Undead(3)
			self.alive_text = self.enemy.alive_text()
			self.dead_text = self.enemy.dead_text()
		else:
			self.enemy = enemies.Lamia(3)
			self.alive_text = self.enemy.alive_text()
			self.dead_text = self.enemy.dead_text()

		super().__init__(x, y)

	def intro_text(self):
		text = self.alive_text if self.enemy.is_alive() else self.dead_text
		return text

	def modify_player(self, player, mod=None):
		# Enemy is attacking the player
		if self.enemy.is_alive():
			try:
				defence_multiplier = 0.1 * player.most_defence().defence
				damage_dealt = self.enemy.damage - self.enemy.damage * defence_multiplier
				player.hp = player.hp - damage_dealt
				print(f"Enemy does {damage_dealt} damage. You have {round(player.hp, 0)} HP remaining")
			except AttributeError:
				player.hp = player.hp - self.enemy.damage
				print(f"Enemy does {self.enemy.damage} damage. You have {round(player.hp, 0)} HP remaining")

		if not self.enemy.is_alive():
			self.completed = True


# Level 4 enemies
class EnemyTile4(MapTile):
	def __init__(self, x, y):
		r = random.random()
		if r < 0.2:
			self.enemy = enemies.BatSwarm(4)
			self.alive_text = self.enemy.alive_text()
			self.dead_text = self.enemy.dead_text()
		elif r < 0.4:
			self.enemy = enemies.OvergrownInsect(4)
			self.alive_text = self.enemy.alive_text()
			self.dead_text = self.enemy.dead_text()
		elif r < 0.6:
			self.enemy = enemies.SkeletalWarrior(4)
			self.alive_text = self.enemy.alive_text()
			self.dead_text = self.enemy.dead_text()
		elif r < 0.8:
			self.enemy = enemies.GiantSpider(4)
			self.alive_text = self.enemy.alive_text()
			self.dead_text = self.enemy.dead_text()
		elif r < 0.99:
			self.enemy = enemies.Undead(4)
			self.alive_text = self.enemy.alive_text()
			self.dead_text = self.enemy.dead_text()

		else:
			self.enemy = enemies.Lamia(4)
			self.alive_text = self.enemy.alive_text()
			self.dead_text = self.enemy.dead_text()

		super().__init__(x, y)

	def intro_text(self):
		text = self.alive_text if self.enemy.is_alive() else self.dead_text
		return text

	def modify_player(self, player, mod=None):
		# Enemy is attacking the player
		if self.enemy.is_alive():
			try:
				defence_multiplier = 0.1 * player.most_defence().defence
				damage_dealt = self.enemy.damage - self.enemy.damage * defence_multiplier
				player.hp = player.hp - damage_dealt
				print(f"Enemy does {damage_dealt} damage. You have {round(player.hp, 0)} HP remaining")
			except AttributeError:
				player.hp = player.hp - self.enemy.damage
				print(f"Enemy does {self.enemy.damage} damage. You have {round(player.hp, 0)} HP remaining")

		if not self.enemy.is_alive():
			self.completed = True


class GeoEnemy(MapTile):
	def __init__(self, x, y):
		r = random.random()
		if r < 0.33:
			self.enemy = enemies.Ogre()
			self.alive_text = self.enemy.alive_text()
			self.dead_text = self.enemy.dead_text()
		elif r < 0.66:
			self.enemy = enemies.Golem()
			self.alive_text = self.enemy.alive_text()
			self.dead_text = self.enemy.dead_text()
		else:
			self.enemy = enemies.Gargoyle()
			self.alive_text = self.enemy.alive_text()
			self.dead_text = self.enemy.dead_text()

		super().__init__(x, y)

	def intro_text(self):
		text = self.alive_text if self.enemy.is_alive() else self.dead_text
		return text

	def modify_player(self, player, mod=None):
		if self.enemy.is_alive():
			try:
				defence_multiplier = 0.1 * player.most_defence().defence
				damage_dealt = self.enemy.damage - self.enemy.damage * defence_multiplier
				player.hp = player.hp - damage_dealt
				print(f"Enemy does {damage_dealt} damage. You have {round(player.hp, 0)} HP remaining\n")
			except AttributeError:
				player.hp = player.hp - self.enemy.damage
				print(f"Enemy does {self.enemy.damage} damage. You have {round(player.hp, 0)} HP remaining\n")

		if not self.enemy.is_alive():
			self.completed = True


class HydroEnemy(MapTile):
	def __init__(self, x, y):
		r = random.random()
		if r < 0.33:
			self.enemy = enemies.Hydra()
			self.alive_text = self.enemy.alive_text()
			self.dead_text = self.enemy.dead_text()
		elif r < 0.66:
			self.enemy = enemies.WaterNymph()
			self.alive_text = self.enemy.alive_text()
			self.dead_text = self.enemy.dead_text()
		else:
			self.enemy = enemies.SeaSerpent()
			self.alive_text = self.enemy.alive_text()
			self.dead_text = self.enemy.dead_text()

		super().__init__(x, y)

	def intro_text(self):
		text = self.alive_text if self.enemy.is_alive() else self.dead_text
		return text

	def modify_player(self, player, mod=None):
		if self.enemy.is_alive():
			try:
				defence_multiplier = 0.1 * player.most_defence().defence
				damage_dealt = self.enemy.damage - self.enemy.damage * defence_multiplier
				player.hp = player.hp - damage_dealt
				print(f"Enemy does {damage_dealt} damage. You have {round(player.hp, 0)} HP remaining\n")
			except AttributeError:
				player.hp = player.hp - self.enemy.damage
				print(f"Enemy does {self.enemy.damage} damage. You have {round(player.hp, 0)} HP remaining\n")

		if not self.enemy.is_alive():
			self.completed = True


class PyroEnemy(MapTile):
	def __init__(self, x, y):
		r = random.random()
		if r < 0.33:
			self.enemy = enemies.HellHound()
			self.alive_text = self.enemy.alive_text()
			self.dead_text = self.enemy.dead_text()

		elif r < 0.66:
			self.enemy = enemies.BabyPhoenix()
			self.alive_text = self.enemy.alive_text()
			self.dead_text = self.enemy.dead_text()
		else:
			self.enemy = enemies.Salamander()
			self.alive_text = self.enemy.alive_text()
			self.dead_text = self.enemy.dead_text()

		super().__init__(x, y)

	def intro_text(self):
		text = self.alive_text if self.enemy.is_alive() else self.dead_text
		return text

	def modify_player(self, player, mod=None):
		if self.enemy.is_alive():
			try:
				defence_multiplier = 0.1 * player.most_defence().defence
				damage_dealt = self.enemy.damage - self.enemy.damage * defence_multiplier
				player.hp = player.hp - damage_dealt
				print(f"Enemy does {damage_dealt} damage. You have {round(player.hp, 0)} HP remaining\n")
			except AttributeError:
				player.hp = player.hp - self.enemy.damage
				print(f"Enemy does {self.enemy.damage} damage. You have {round(player.hp, 0)} HP remaining\n")

		if not self.enemy.is_alive():
			self.completed = True


class AeroEnemy(MapTile):
	def __init__(self, x, y):
		r = random.random()
		if r < 0.33:
			self.enemy = enemies.Harpy()
			self.alive_text = self.enemy.alive_text()
			self.dead_text = self.enemy.dead_text()
		elif r < 0.66:
			self.enemy = enemies.ThunderBird()
			self.alive_text = self.enemy.alive_text()
			self.dead_text = self.enemy.dead_text()
		else:
			self.enemy = enemies.Manticore()
			self.alive_text = self.enemy.alive_text()
			self.dead_text = self.enemy.dead_text()

		super().__init__(x, y)

	def intro_text(self):
		text = self.alive_text if self.enemy.is_alive() else self.dead_text
		return text

	def modify_player(self, player, mod=None):
		if self.enemy.is_alive():
			try:
				defence_multiplier = 0.1 * player.most_defence().defence
				damage_dealt = self.enemy.damage - self.enemy.damage * defence_multiplier
				player.hp = player.hp - damage_dealt
				print(f"The {Fore.RED}{self.enemy.name}{Fore.RESET} does {self.enemy.damage} damage. You have {Fore.GREEN}{round(player.hp, 0)} {Fore.RESET}HP remaining\n")
			except AttributeError:
				player.hp = player.hp - self.enemy.damage
				print(f"The {Fore.RED}{self.enemy.name}{Fore.RESET} does {self.enemy.damage} damage. You have {Fore.GREEN}{round(player.hp, 0)} {Fore.RESET}HP remaining\n")

		if not self.enemy.is_alive():
			self.completed = True


class GeoBoss(MapTile):
	def __init__(self, x, y):
		self.enemy = enemies.Geomancer()
		self.alive_text = self.enemy.alive_text()
		self.dead_text = self.enemy.dead_text()
		super().__init__(x, y)

	def intro_text(self):
		text = self.alive_text if self.enemy.is_alive() else self.dead_text
		return text

	def modify_player(self, player, mod=None):
		if self.enemy.is_alive():
			try:
				defence_multiplier = 0.1 * player.most_defence().defence
				damage_dealt = self.enemy.damage - self.enemy.damage * defence_multiplier
				player.hp = player.hp - damage_dealt
				print(f"The {Fore.RED}{self.enemy.name}{Fore.RESET} does {self.enemy.damage} damage. You have {Fore.GREEN}{round(player.hp, 0)} {Fore.RESET}HP remaining\n")
			except AttributeError:
				player.hp = player.hp - self.enemy.damage
				print(f"The {Fore.RED}{self.enemy.name}{Fore.RESET} does {self.enemy.damage} damage. You have {Fore.GREEN}{round(player.hp, 0)} {Fore.RESET}HP remaining\n")

		if not self.enemy.is_alive():
			self.completed = True


class HydroBoss(MapTile):
	def __init__(self, x, y):
		self.enemy = enemies.Hydromancer()
		self.alive_text = self.enemy.alive_text()
		self.dead_text = self.enemy.alive_text()
		super().__init__(x, y)

	def intro_text(self):
		text = self.alive_text if self.enemy.is_alive() else self.dead_text
		return text

	def modify_player(self, player, mod=None):
		if self.enemy.is_alive():
			try:
				defence_multiplier = 0.1 * player.most_defence().defence
				damage_dealt = self.enemy.damage - self.enemy.damage * defence_multiplier
				player.hp = player.hp - damage_dealt
				print(f"The {Fore.RED}{self.enemy.name}{Fore.RESET} does {self.enemy.damage} damage. You have {Fore.GREEN}{round(player.hp, 0)} {Fore.RESET}HP remaining\n")
			except AttributeError:
				player.hp = player.hp - self.enemy.damage
				print(
					f"The {Fore.RED}{self.enemy.name}{Fore.RESET} does {self.enemy.damage} damage. You have {Fore.GREEN}{round(player.hp, 0)} {Fore.RESET}HP remaining\n")

		if not self.enemy.is_alive():
			self.completed = True


class PyroBoss(MapTile):
	def __init__(self, x, y):
		self.enemy = enemies.Pyromancer()
		self.alive_text = self.enemy.alive_text()
		self.dead_text = self.enemy.dead_text()
		super().__init__(x, y)

	def intro_text(self):
		text = self.alive_text if self.enemy.is_alive() else self.dead_text
		return text

	def modify_player(self, player, mod=None):
		if self.enemy.is_alive():
			try:
				defence_multiplier = 0.1 * player.most_defence().defence
				damage_dealt = self.enemy.damage - self.enemy.damage * defence_multiplier
				player.hp = player.hp - damage_dealt
				print(
					f"The {Fore.RED}{self.enemy.name}{Fore.RESET} does {self.enemy.damage} damage. You have {Fore.GREEN}{round(player.hp, 0)} {Fore.RESET}HP remaining\n")
			except AttributeError:
				player.hp = player.hp - self.enemy.damage
				print(
					f"The {Fore.RED}{self.enemy.name}{Fore.RESET} does {self.enemy.damage} damage. You have {Fore.GREEN}{round(player.hp, 0)} {Fore.RESET}HP remaining\n")

		if not self.enemy.is_alive():
			self.completed = True


class AeroBoss(MapTile):
	def __init__(self, x, y):
		self.enemy = enemies.Aeromancer()
		self.alive_text = self.enemy.alive_text()
		self.dead_text = self.enemy.dead_text()
		super().__init__(x, y)

	def intro_text(self):
		text = self.alive_text if self.enemy.is_alive() else self.dead_text
		return text

	def modify_player(self, player, mod=None):
		if self.enemy.is_alive():
			try:
				defence_multiplier = 0.1 * player.most_defence().defence
				damage_dealt = self.enemy.damage - self.enemy.damage * defence_multiplier
				player.hp = player.hp - damage_dealt
				print(f"The {Fore.RED}{self.enemy.name}{Fore.RESET} does {damage_dealt} damage. You have {Fore.GREEN}{round(player.hp, 0)} HP {Fore.RESET}remaining\n")
			except AttributeError:
				player.hp = player.hp - self.enemy.damage
				print(f"The {Fore.RED}{self.enemy.name}{Fore.RESET} does {self.enemy.damage} damage. You have {Fore.GREEN}{round(player.hp, 0)} {Fore.RESET}HP remaining\n")

		if not self.enemy.is_alive():
			self.completed = True


class TraderTile(MapTile):
	def __init__(self, x, y):
		super().__init__(x, y)
		self.trader = npc.Trader()

	def intro_text(self):
		return """
A frail not-quite human, not-quite creature squats in the corner.
Clinking his gold coins together. He looks ready to trade.
		"""

	def trade(self, buyer, seller):
		for i, item in enumerate(seller.inventory, 1):
			print(f"{i}.{item.name} - {item.value} Gold")
		while True:
			user_input = input("Choose an item or press Q to exit: ")
			if user_input in ["q", "Q"]:
				return
			else:
				try:
					choice = int(user_input)
					to_swap = seller.inventory[choice - 1]
					self.swap(seller, buyer, to_swap)
				except (ValueError, IndexError):
					print("Invalid Choice\n")

	@staticmethod
	def swap(seller, buyer, item):
		if item.value > buyer.gold:
			print("That's too expensive for you\n")
			return
		seller.inventory.remove(item)
		buyer.inventory.append(item)
		seller.gold = seller.gold + item.value
		buyer.gold = buyer.gold - item.value
		print(f"{Style.BRIGHT}Trade Complete\n")

	def check_if_trade(self, player):
		while True:
			print("Would you like to (B)uy (S)ell or (Q)uit")
			user_input = input()
			if user_input in ["q", "Q"]:
				return
			elif user_input in ["b", "B"]:
				print("Here is what is available to be bought: ")
				self.trade(buyer=player, seller=self.trader)
			elif user_input in ["s", "S"]:
				print("Here is what can be sold: ")
				self.trade(buyer=self.trader, seller=player)
			else:
				print(f"{Style.BRIGHT}\nInvalid Choice\n")


class WeaponSmithTile(MapTile):
	def __init__(self, x, y):
		super().__init__(x, y)
		self.trader = npc.WeaponSmith()

	def intro_text(self):
		return """
A frail not-quite human, not-quite creature squats in the corner.
Clinking his gold coins together. He looks ready to trade.
Weapon Smith
		"""

	def trade(self, buyer, seller):
		for i, item in enumerate(seller.inventory, 1):
			if isinstance(buyer, npc.WeaponSmith):
				if item.sellable and isinstance(item, items.Weapon):
					print(f"{i}.{item.name} - {item.value} Gold")

			elif isinstance(buyer, npc.ArmourSmith):
				if item.sellable and isinstance(item, items.Defencive):
					print(f"{i}.{item.name} - {item.value} Gold")

			elif isinstance(buyer, npc.Trader):
				if item.sellable and isinstance(item, items.Consumable):
					print(f"{i}.{item.name} - {item.value} Gold")

			else:
				if item.sellable:
					print(f"{i}.{item.name} - {item.value} Gold")

		while True:
			user_input = input("Choose an item or press Q to exit: ")
			if user_input in ["q", "Q"]:
				return
			else:
				try:
					choice = int(user_input)
					to_swap = seller.inventory[choice - 1]
					self.swap(seller, buyer, to_swap)
				except (ValueError, IndexError):
					print(f"{Style.BRIGHT}\nInvalid Choice\n")

	@staticmethod
	def swap(seller, buyer, item):
		if item.value > buyer.gold:
			print("That's too expensive for you\n")
			return
		seller.inventory.remove(item)
		buyer.inventory.append(item)
		seller.gold = seller.gold + item.value
		buyer.gold = buyer.gold - item.value
		print(f"{Style.BRIGHT}Trade Complete\n")

	def check_if_trade(self, player):
		while True:
			print("Would you like to (B)uy (S)ell or (Q)uit")
			user_input = input()
			if user_input in ["q", "Q"]:
				return
			elif user_input in ["b", "B"]:
				print("Here is what is available to be bought: ")
				self.trade(buyer=player, seller=self.trader)
			elif user_input in ["s", "S"]:
				print("Here is what can be sold: ")
				self.trade(buyer=self.trader, seller=player)
			else:
				print(f"{Style.BRIGHT}\nInvalid Choice\n")


class ArmourSmithTile(MapTile):
	def __init__(self, x, y):
		super().__init__(x, y)
		self.trader = npc.ArmourSmith()

	def intro_text(self):
		return """
A frail not-quite human, not-quite creature squats in the corner.
Clinking his gold coins together. He looks ready to trade.
Armour Smith
		"""

	def trade(self, buyer, seller):
		for i, item in enumerate(seller.inventory, 1):
			if isinstance(buyer, npc.WeaponSmith):
				if item.sellable and isinstance(item, items.Weapon):
					print(f"{i}.{item.name} - {item.value} Gold")

			elif isinstance(buyer, npc.ArmourSmith):
				if item.sellable and isinstance(item, items.Defencive):
					print(f"{i}.{item.name} - {item.value} Gold")

			elif isinstance(buyer, npc.Trader):
				if item.sellable and isinstance(item, items.Consumable):
					print(f"{i}.{item.name} - {item.value} Gold")

			else:
				if item.sellable:
					print(f"{i}.{item.name} - {item.value} Gold")

		while True:
			user_input = input("Choose an item or press Q to exit: ")
			if user_input in ["q", "Q"]:
				return
			else:
				try:
					choice = int(user_input)
					to_swap = seller.inventory[choice - 1]
					self.swap(seller, buyer, to_swap)
				except (ValueError, IndexError):
					print(f"{Style.BRIGHT}\nInvalid Choice\n")

	@staticmethod
	def swap(seller, buyer, item):
		if item.value > buyer.gold:
			print("That's too expensive for you\n")
			return
		seller.inventory.remove(item)
		buyer.inventory.append(item)
		seller.gold = seller.gold + item.value
		buyer.gold = buyer.gold - item.value
		print(f"{Style.BRIGHT}Trade Complete\n")

	def check_if_trade(self, player):
		while True:
			print("Would you like to (B)uy (S)ell or (Q)uit")
			user_input = input()
			if user_input in ["q", "Q"]:
				return
			elif user_input in ["b", "B"]:
				print("Here is what is available to be bought: ")
				self.trade(buyer=player, seller=self.trader)
			elif user_input in ["s", "S"]:
				print("Here is what can be sold: ")
				self.trade(buyer=self.trader, seller=player)
			else:
				print("Invalid Choice\n")


class EnchanterTile(MapTile):
	def __init__(self, x, y):
		super().__init__(x, y)
		self.enchanter = npc.Enchanter()

	def intro_text(self):
		return f"""
An old wizard with a long white beard, looks into your eyes. 
		He seems to hold the power of magic.

{Style.BRIGHT}(Please note that you can only have one enchantment per item.){Style.RESET_ALL}
			"""

	def enchant(self, buyer, seller):
		for i, item in enumerate(seller.inventory, 1):
			print(f"{i}. {item.name} - {item.value} Crystals ")
		while True:
			user_input = input("Choose an item or press Q to exit")
			if user_input in ["Q", "q"]:
				return
			else:
				try:
					choice = int(user_input)
					to_swap = seller.inventory[choice - 1]
					self.en(buyer, to_swap)
				except (ValueError, IndexError):
					print(f"{Style.BRIGHT}\nInvalid Choice\n")

	# the function en enchants the item
	@staticmethod
	def en(buyer, item):
		if item.value > buyer.crystals:
			print("That is too expensive for you.\n")
			return
		buyer.most_powerful_weapon().enchantment = item
		buyer.crystals -= item.value
		buyer.most_powerful_weapon().name = f"{buyer.most_powerful_weapon().name} ({item.name})"
		buyer.score += 10
		print(f"{Style.BRIGHT}Enchantment Complete")

	def check_if_enchant(self, player):
		while True:
			print("Would you like to (E)nchant, or (Q)uit")
			user_input = input()
			if user_input in ["Q", "q"]:
				return
			elif user_input in ["E", "e"]:
				print("These are the available enchantments:")
				self.enchant(buyer=player, seller=self.enchanter)
			else:
				print(f"{Style.BRIGHT}\nInvalid Choice\n")


class QuestTile(MapTile):
	def __init__(self, x, y):
		super().__init__(x, y)
		self.completed = False
		self.quest_lady = npc.QuestLady()
		self.encounter = 1

	def intro_text(self):
		if self.completed:
			return f"""
The {self.quest_lady.name} sees you and grins.
She has no quest for you.
Maybe next time. 
				"""
		else:
			return f"""
You see a {Fore.LIGHTMAGENTA_EX}{self.quest_lady.name}{Fore.RESET}.
She seems to be plotting something devious.
Will you be her helping hand?
			"""

	def talk(self, player):
		if not self.completed:
			print("Will you help the old lady?")
			choice1 = input("(Y)es or (N)o\n")
			if choice1 not in ["yes", "YES", "y", "Y"]:
				return

			print(
				f"""
 You have made a wise decision
You must seek out a mysterious {Fore.LIGHTBLUE_EX}{items.MagicalItem().name}{Fore.RESET}
			"""
				)

			print(f"""
Have you found the {Fore.LIGHTBLUE_EX}{items.MagicalItem().name}{Fore.RESET}?
				""")

			choice2 = input("(Y)es or (N)o\n")
			if choice2 not in ["yes", "YES", "y", "Y"]:
				return
			else:
				QuestTile.item_found(self, player)

	def item_found(self, player):
		quest_item = [item for item in player.inventory if isinstance(item, items.Quests)]
		if quest_item:
			player.score += 15
			self.completed = True
			self.quest_completed(self=self, player=player, item=quest_item)
		else:
			return f"""
				You have not found the {Fore.LIGHTBLUE_EX}{items.MagicalItem().name}{Fore.RESET} yet.
			"""

	@staticmethod
	def quest_completed(self, player, item):
		self.encounter += 1
		if self.completed:
			print(f"You have found and retrieved the {Fore.LIGHTBLUE_EX}{items.MagicalItem().name}{Fore.RESET}\n")
			player.gold += self.quest_lady.gold
			print(f"You have received {Fore.YELLOW}{self.quest_lady.gold} gold {Fore.RESET}")
			player.crystals += self.quest_lady.crystals
			print(f"You have received {Fore.CYAN}{self.quest_lady.crystals} crystals{Fore.RESET}\n")
			try:
				if item in player.inventory:
					player.inventory.remove(item)
				elif items.MagicalItem() in player.inventory:
					player.inventory.remove(items.MagicalItem())
				else:
					pass
			except ValueError:
				pass
		else:
			print("You have not completed the quest.")
			if self.encounter > 3:
				player.gold -= 3
				player.crystals -= 1


class FindQuestItemTile(MapTile):
	def __init__(self, x, y):
		super().__init__(x, y)
		self.item = items.MagicalItem()
		self.item_claimed = False

	def intro_text(self):
		if self.item_claimed:
			return f"""
There is nothing to see here.
It seems you have already claimed the {Fore.LIGHTBLUE_EX}{items.MagicalItem().name}{Fore.RESET}.
You must forge onwards.
			"""
		else:
			return f"""
You see a soft glow. 
You have found it. The {self.item.name}
Now you can return to the {Fore.LIGHTMAGENTA_EX}suspicious old woman{Fore.RESET}.
			"""

	def modify_player(self, player, mod=None):
		player.score += 5

		if not self.item_claimed:
			self.item_claimed = True
			item = self.item
			player.inventory.append(item)
			print(f"You have found the {Fore.LIGHTBLUE_EX}{item.name}{Fore.RESET}\n")


class StoryTellerTile1(MapTile):
	encounter = 1

	def __init__(self, x, y):
		super().__init__(x, y)
		self.storyteller = npc.StoryTeller1()

	def intro_text(self):
		if self.encounter == 1:
			return f"""
You meet a {Fore.LIGHTMAGENTA_EX}{npc.StoryTeller1().name}{Fore.RESET}. 
Her face is covered with moles and hair creeps out her nose.
She might have a story to tell.
			"""
		else:
			return f"""Just the same{Fore.LIGHTMAGENTA_EX}{npc.StoryTeller1().name}{Fore.RESET} from earlier.\n"""

	def converse(self, player):
		if self.encounter == 1:
			self.encounter += 1

			try:
				print(self.storyteller.messages[1])
				player.name = input()

				print(f"""\n{Fore.LIGHTMAGENTA_EX}{player.name}?""")
				print(self.storyteller.messages[2])
				time.sleep(1)

				print(self.storyteller.messages[3])
				yes_no = input()

				if yes_no.lower() in ["yes", "y", "yeah"]:
					print(self.storyteller.messages[3.1])
				if yes_no.lower() in ["no", "n", "nope"]:
					print(self.storyteller.messages[3.2])
					valid = False
					while not valid:
						print("Are you here to save the village, or what?")
						save_village = input()
						if save_village.lower() in ["yes", "y", "yeah"]:
							valid = True
							print(self.storyteller.messages[3.3])
							print(self.storyteller.messages[3.1])
						else:
							print(self.storyteller.messages[3.4])

				print(self.storyteller.messages[4])

				while True:
					print("""
Will you:
(1.)Pay the old woman
or
(2.)Refuse to pay the old woman""")
					choice = input()
					if choice.lower() in ["yes", "y", "yeah", "1", "1."]:
						print(self.storyteller.messages[4.1])
						player.kindness = True
						self.modify_player(player, mod=1)
						print("")
						return
					elif choice.lower() in ["no", "n", "nope", "2", "2."]:
						player.kindness = False
						print(self.storyteller.messages[4.2])
						print("")
						return
					else:
						continue

			except KeyError:
				pass

		elif self.encounter == 2:
			self.encounter += 1
			print(f"""{Style.DIM}{Fore.LIGHTMAGENTA_EX}
What was your name again?
{player.name}, was it?
			
			""")
			if player.kindness:
				print(self.storyteller.messages[5])
				self.modify_player(player, mod=2)
				print(self.storyteller.messages[5.1])
				return
			if not player.kindness:
				print(self.storyteller.messages[6])
				return
		elif self.encounter == 3:
			print(self.storyteller.messages[6])
			return

	def modify_player(self, player, mod=None):
		if mod == 1:
			self.storyteller.gold += 5
			player.gold -= 5
			print(f"You have given the {Fore.LIGHTMAGENTA_EX}{self.storyteller.name}{Fore.RESET}{Fore.YELLOW} 5 gold\n")
			player.score += 5

		if mod == 2:
			to_give_gold = self.storyteller.gold
			to_give_crystal = self.storyteller.crystals
			self.storyteller.gold -= to_give_gold
			self.storyteller.crystals -= to_give_crystal
			player.gold += to_give_gold
			player.crystals += to_give_crystal
			print(f"The {Fore.LIGHTMAGENTA_EX}{self.storyteller.name}{Fore.RESET} has given you {Fore.YELLOW}{to_give_gold} gold\n")
			print(f"The {Fore.LIGHTMAGENTA_EX}{self.storyteller.name}{Fore.RESET} has given you {Fore.CYAN}{to_give_crystal} crystals\n")
			player.score += 10


class StoryTellerTile2(MapTile):
	encounter = 1

	def __init__(self, x, y):
		super().__init__(x, y)
		self.storyteller = npc.StoryTeller2()

	def intro_text(self):
		if self.encounter == 1:
			return f"""
You see an {Fore.LIGHTMAGENTA_EX}{npc.StoryTeller2().name}{Fore.RESET}.
He starts smiling at you, his smile is quite awkward. 
His hands begin to flail, as he walks towards you.
"""
		else:
			return f"""Just the same{Fore.LIGHTMAGENTA_EX}{npc.StoryTeller2().name}{Fore.RESET} from earlier.\n"""

	def converse(self, player):
		if self.encounter == 1:
			self.encounter += 1

			try:
				print(f"{self.storyteller.messages['1']}\n")
				choice = input()  # First choice
				if choice.lower() in ["yes", "y", "yeah", "1", "1."]:  # If the player says yes
					print(f"{self.storyteller.messages['1yes']}")

					choice2 = input()  # Second Choice
					if choice2.lower() in ["yes", "y", "yeah", "1", "1."]:
						print(f"{self.storyteller.messages['2yes']}")
					else:
						print(f"{self.storyteller.messages['2no']}")

				elif choice.lower() in ["no", "n", "nope", "2", "2."]:  # If the player says no
					print(f"{self.storyteller.messages['1no']}")

					choice2 = input()  # Second Choice if the player had said no earlier
					if choice2.lower() in ["yes", "y", "yeah", "1", "1."]:
						print(f"{self.storyteller.messages['3']}")
					elif choice2.lower() in ["no", "n", "nope", "2", "2."]:
						print(f"{self.storyteller.messages['2no']}")
					else:
						print(f"{self.storyteller.messages['2no']}")

				else:
					print(f"{self.storyteller.messages['1else']}")  # If the player does not give a valid response

				print(f"{self.storyteller.messages['3']}")

				print(f"{self.storyteller.messages['understand']}")
				choice3 = input()
				if choice3:
					print(f"{self.storyteller.messages['3.5']}")

				print("")
				print(f"{self.storyteller.messages['4']}")
				choice4 = input()

				if choice4.lower() in ["yes", "y", "yeah", "1", "1."]:
					if player.kindness:
						self.modify_player(player, mod=2)
					elif not player.kindness:
						self.modify_player(player, mod=1)
					else:
						self.modify_player(player, mod=1)

					print(f"{self.storyteller.messages['4yes']}")

				elif choice4.lower() in ["no", "n", "nope", "2", "2."]:
					print(f"{self.storyteller.messages['4no']}")

			except KeyError:
				print(self.storyteller.messages["forgotten"])
		elif self.encounter == 2:
			print(self.storyteller.messages["before"])

	def modify_player(self, player, mod=None):
		try:
			if mod == 1:
				to_give = self.storyteller.inventory[0]
				player.inventory.append(to_give)
				print(f"The {Fore.LIGHTMAGENTA_EX}{self.storyteller.name}{Fore.RESET} has given you: {to_give.name}\n")
			elif mod == 2:
				to_give = self.storyteller.inventory[0]
				player.inventory.append(to_give)
				print(f"The {Fore.LIGHTMAGENTA_EX}{self.storyteller.name}{Fore.RESET} has given you: {to_give.name}\n")

				amount: int = random.randint(60, 90)
				print(f"The {Fore.LIGHTMAGENTA_EX}{self.storyteller.name}{Fore.RESET} has given you: {Fore.YELLOW}{amount} gold {Fore.RESET}\n")
				player.gold += amount
			else:
				pass

		except IndexError:
			amount: int = random.randint(40, 65)
			print(f"You receive {Fore.YELLOW}{amount} gold {Fore.RESET}")
			player.gold += amount


class EnemyChallengeTile(MapTile):
	encounter = 1

	def __init__(self, x, y):
		super().__init__(x, y)
		self.enemy = enemies.Challenger()
		self.story = story.challenger1
		self.fight = False
		self.escape = False
		self.completed = False

	def intro_text(self):
		self.encounter += 1
		if self.encounter == 1:
			if self.enemy.is_alive():
				self.completed = True
				return self.enemy.alive_text()
			else:
				return self.enemy.dead_text()
		else:
			if self.enemy.is_alive() and not self.fight:
				return f"""\nI am the {self.enemy.name}. Nothing that you do can stop me."""
			if self.enemy.is_alive() and self.fight:
				return f"""The {Fore.LIGHTRED_EX}{self.enemy.name}{Fore.RESET} is still alive\n"""
			else:
				return self.enemy.dead_text()

	def converse(self, player):

		def looking_through_input(user_input, look_through):
			split = user_input.lower().split()
			for word in split:
				if word in look_through:
					return True

			return False

		destroy = False
		try:
			print(f"{self.story['1']}")
			purpose = input("")
			if looking_through_input(purpose, story.possibilities1):
				print(f"{self.story['1y']}")
				_ = input("")
				if _:
					print(f"{self.story['1yw']}\n")
					print(f"{self.story['challenge']}\n")
					challenge = input()
					if looking_through_input(challenge, ["yes", "y", "fight", "1", "accept"]):
						print(f"{self.story['accept']}")
						self.fight = True
						self.modify_player(player)
						if not self.enemy.is_alive() and player.is_alive():
							print(f"{self.story['victory']}")
						elif self.enemy.is_alive() and not player.is_alive():
							print(f"{self.story['defeat']}")
						else:
							print(f"{self.story['defeat']}")
					elif looking_through_input(challenge, ["no", "n", "decline", "2", "don't", "do not", "reject"]):
						print(f"{self.story['decline']}")
						self.fight = True
						self.modify_player(player)
					else:
						print(f"{self.story['fight_else']}")
						self.fight = True
						self.modify_player(player)

			elif len(purpose) > 25:
				print(f"{self.story['1long']}")
				y_n = input("")
				if looking_through_input(y_n, ["yes", "y", "yeah", "1", "1."]):
					print(f"{self.story['against']}\n")
					print(f"{self.story['challenge']}")
					ans = input("")
					if looking_through_input(ans, ["yes", "y", "yeah", "1", "1.", "accept", "fight"]):
						print(f"{self.story['accept']}\n")
						self.fight = True
						self.modify_player(player)
					elif looking_through_input(ans, ["no", "n", "decline", "2", "don't", "do not", "reject"]):
						print(f"{self.story['decline']}")
						self.fight = True
						self.modify_player(player)
					else:
						print(f"{self.story['fight_else']}")
						self.fight = True
						self.modify_player(player)
				elif looking_through_input(y_n, ["no", "n", "decline", "2", "don't", "do not", "reject"]):
					print(f"{self.story['destroy']}\n")
					question = input()
					if looking_through_input(question, ["yes", "y", "yeah", "1", "1."]):
						destroy = True
						self.escape = True
						# From here the player goes on to lose the game
					else:
						print(f"{self.story['late']}")
						destroy = True
						self.escape = True
						# From here the player goes on tp lose the game
			else:
				print(f"{self.story['destroy']}")
				question = input()
				if looking_through_input(question, ["yes", "y", "yeah", "1", "1."]):
					destroy = True
					self.escape = True
				# From here the player goes on to lose the game
				else:
					print(f"{self.story['against']}\n")
					print(f"{self.story['challenge']}")
					fight = input()
					if looking_through_input(fight, ["yes", "y", "yeah", "1", "1.", "accept", "fight"]):
						print(f"{self.story['accept']}\n")
						self.fight = True
						self.modify_player(player)
					elif looking_through_input(fight, ["no", "n", "decline", "2", "don't", "do not", "reject"]):
						print(f"{self.story['revenge']}\n")
						destroy = True
						self.escape = True

			if destroy:
				for x in story.the_end_abandon:
					if len(x) < 25:
						print(x)
						time.sleep(0.4)
					if len(x) > 25:
						print(x)
						time.sleep(0.8)

				self.modify_player(player, mod=0)
				self.modify_player(player, mod=1)

		except KeyError:
			print("""You are from the village aren't you?
			I can tell. 
			I hat that village, they exiled me and left me for dead. 
			I shall kill you and take my first step towards revenge.
			""")
			self.fight = True
			self.modify_player(player)

	def modify_player(self, player, mod=None):
		if mod == 0:
			if self.enemy.is_alive():
				lost = player.hp * 0.5
				player.hp -= lost
				print(f"The {self.enemy.name} attacks you. You have {Fore.GREEN}{player.hp} HP {Fore.RESET}remaining")

				self.enemy.hp -= self.enemy.hp
				print(f"{self.story['escape_die']}")


		if self.enemy.is_alive() and self.fight:
			try:
				defence_multiplier = 0.1 * player.most_defence().defence
				damage_dealt = self.enemy.damage - self.enemy.damage * defence_multiplier
				player.hp = player.hp - damage_dealt
				print(f"The {Fore.RED}{self.enemy.name}{Fore.RESET} does {self.enemy.damage} damage. You have {Fore.GREEN}{round(player.hp, 0)} {Fore.RESET}HP remaining\n")
			except AttributeError:
				player.hp = player.hp - self.enemy.damage
				print(f"The {Fore.RED}{self.enemy.name}{Fore.RESET} does {self.enemy.damage} damage. You have {Fore.GREEN}{round(player.hp, 0)} {Fore.RESET}HP remaining\n")


# ST start Tile
# VT Victory Tile

# FG Find Gold
# FC Find Crystals
# FI Find Quest Item Tile

# EN1 Enemy Tile1
# EN2 Enemy Tile2
# EN3 Enemy Tile3
# EN4 Enemy Tile4

# AE Aero Enemy
# HE Hydro Enemy
# PE Pyro enemy
# GE Geo Enemy

# ET Enchanter Tile
# TT Trader Tile
# QT Quest Tile

# BT Boring Tile
# Corridor Tile

# AST Armour smith Tile
# WST Weapon smith Tile
# ST1 Story Teller Tile 1
# ST2 Story Teller Tile 2


world_dsl = """
|   |   |   |   |   |   |   |   |   |   |   |   |   |ST |CT |CT |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |ST1|EN1|EN1|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |FG |BT |BT |BT |   |FG |EN1|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |TT |   |BT |   |   |FQI|EN1|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |EN1|BT |   |BT |EN1|BT |BT |BT |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |BT |   |QT |BT |   |   |BT |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |WST|EN1|BT |EN1|BT |BT |BT |   |   |   |   |   |   |   |   |   |   |   |   |ET |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |ET |AST|FC |   |BT |TT |   |EN1|   |   |   |   |   |   |   |   |   |   |   |BT |CT |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |BT |EN1|BT |CT |EN1|EN1|BT |EN1|   |   |   |   |   |   |   |   |   |   |EN4|TT |CT |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |BT |   |   |CT |   |BT |   |FC |   |   |   |   |   |   |   |   |   |BT |BT |   |CT |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |BT |EN1|BT |CT |BT |BT |   |   |   |   |   |   |   |   |   |   |EN4|BT |   |   |CT |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |CT |   |   |   |   |   |   |   |   |   |   |   |BT |BT |   |   |   |CT |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |FG |BT |FC |   |   |   |   |   |   |   |   |   |EN3|BT |EN4|EN4|BT |   |EN4|BT |BT |EN4|   |   |
|   |   |FC |EN2|BT |FG |BT |EN1|BT |EN2|FC |   |   |TT |GE |GE |GE |ET |   |   |   |   |   |   |   |BT |BT |   |   |   |BT |EN4|CT |   |   |AE |   |   |
|   |   |   |   |   |BT |BT |   |   |   |   |   |   |   |   |GE |   |   |   |   |   |   |   |   |FG |TT |   |   |   |   |ECT|   |CT |   |AE |AE |   |   |
|   |   |   |   |   |EN |BT |   |   |   |   |   |   |QT |   |GB |   |   |   |   |   |   |   |   |EN4|   |   |   |   |   |FQI|   |CT |AE |AE |AB |CT |VT |
|   |   |   |HE |HE |   |EN2|ET |WST|EN |BT |   |BT |EN2|   |CT |   |   |   |   |   |   |   |   |FC |BT |   |   |   |   |BT |   |CT |   |AE |AE |   |   |
|BT |BT |HB |HE |HE |BT |BT |   |   |   |FC |BT |EN2|EN1|ST2|CT |   |   |   |   |   |   |   |   |   |BT |BT |   |   |   |BT |   |CT |   |   |AE |   |   |
|CT |   |BT |HE |HE |   |BT |EN2|FG |EN2|EN2|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |EN3|BT |   |   |EN4|   |CT |   |   |EN |   |   |
|CT |   |BT |EN2|FQI|EN2|EN2|   |BT |   |BT |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |BT |BT |BT |EN3|EN4|CT |BT |EN4|BT |   |   |
|CT |   |   |AST|   |   |   |   |TT |EN2|BT |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |EN4|BT |   |   |   |   |   |   |   |   |
|CT |   |   |BT |BT |EN2|EN2|BT |BT |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |BT |BT |QT |BT |   |   |   |   |   |
|CT |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |BT |EN2|   |   |   |   |   |
|CT |   |TT |FC |   |   |   |BT |EN |EN3|BT |WST|BT |EN |EN2|TT |   |   |BT |   |   |   |   |   |   |   |   |   |   |   |   |   |EN2|   |   |   |   |   |
|CT |   |EN2|   |EN3|QT |   |BT |   |CT |   |   |   |   |   |BT |EN2|   |PE |PE |   |   |   |   |   |   |BT |BT |FC |FG |WST|   |BT |   |   |   |   |   |
|BT |BT |BT |BT |EN3|BT |BT |EN3|   |ECT|EN3|FG |BT |BT |EN3|ET |EN3|PE |BT |BT |PE |PB |CT |CT |CT |CT |BT |BT |FC |FG |BT |BT |BT |   |   |   |   |   |
|   |   |FG |   |EN2|   |EN3|   |   |CT |   |   |AST|   |   |BT |EN3|   |PE |PE |   |   |   |   |   |   |BT |BT |ET |TT |AST|   |   |   |   |   |   |   |
|   |   |ET |EN2|   |BT |FQI|FG |EN3|CT |   |   |BT |EN1|FC |TT |   |   |BT |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
"""


def is_dsl_valid(dsl):
	if dsl.count("|ST |") != 1:
		return False
	if dsl.count("|VT |") == 0:
		return False
	lines = dsl.splitlines()
	lines = [ln for ln in lines if ln]
	pipe_counts = [line.count("|") for line in lines]
	for count in pipe_counts:
		if count != pipe_counts[0]:
			return False

	return True


tile_type_dict = {
				"VT ": VictoryTile,
				"BT ": BoringTile,
				"EN1": EnemyTile1,
				"EN2": EnemyTile2,
				"EN3": EnemyTile3,
				"EN4": EnemyTile4,
				"ST ": StartTile,
				"FG ": FindGoldTile,
				"TT ": TraderTile,
				"GE ": GeoEnemy,
				"HE ": HydroEnemy,
				"PE ": PyroEnemy,
				"AE ": AeroEnemy,
				"GB ": GeoBoss,
				"HB ": HydroBoss,
				"PB ": PyroBoss,
				"AB ": AeroBoss,
				"ET ": EnchanterTile,
				"FC ": FindCrystalTile,
				"QT ": QuestTile,
				"FQI": FindQuestItemTile,
				"WST": WeaponSmithTile,
				"AST": ArmourSmithTile,
				"CT ": CorridorTile,
				"ST1": StoryTellerTile1,
				"ST2": StoryTellerTile2,
				"ECT": EnemyChallengeTile,
				"   ": None
}

world_map = []
start_tile_location = None


def parse_world_dsl():
	if not is_dsl_valid(world_dsl):
		raise SyntaxError("DSL is invalid")

	dsl_lines = world_dsl.splitlines()
	dsl_lines = [x for x in dsl_lines if x]

	for y, dsl_row in enumerate(dsl_lines):
		row = []
		dsl_cells = dsl_row.split("|")
		dsl_cells = [c for c in dsl_cells if c]
		for x, dsl_cell in enumerate(dsl_cells):
			tile_type = tile_type_dict.get(dsl_cell)
			if tile_type == StartTile:
				global start_tile_location
				start_tile_location = x, y
			row.append(tile_type(x, y) if tile_type else None)
		world_map.append(row)


def tile_at(x, y):
	if x < 0 or y < 0:
		return None
	try:
		return world_map[y][x]
	except IndexError:
		return None
