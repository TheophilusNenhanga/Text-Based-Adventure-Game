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
	"""This is the base class for all tile on the game map"""
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.completed = False

	def intro_text(self):
		"""This is the base function for all tile introduction text"""
		raise NotImplementedError("Create a subclass instead")

	def modify_player(self, player, mod=None):
		"""This is the base function to modify the player thoughout the game"""
		pass

	def converse(self, player):
		"""This is the base class used when interacting with some NPC's"""
		pass

	@staticmethod
	def looking_through_input(user_input, look_through):
		"""This function is used when lookign for keywords in user input"""
		split = user_input.lower().split()
		for word in split:
			if word in look_through:
				return True

		return False


class StartTile(MapTile):
	"""This class is the tile that the player starts the game on."""
	def intro_text(self):
		return f"""{Fore.LIGHTBLUE_EX}
This is where your journey begins!
Will you be the one to save the village?
        """


class BoringTile(MapTile):
	"""This tile is a plain tile with no other functionality.
	It is also the base class for other tiles."""
	def intro_text(self):
		return f"""{Style.DIM}
Nothing much happens here.
You must continue onwards.
        """

	def modify_player(self, player, mod=None):
		player.score += 1


class BoringTileStone(BoringTile):
	"""The boring tile for the first levl"""
	def intro_text(self):
		text = story.stone_texts[random.randint(0, len(story.stone_texts)-1)]
		return text


class BoringTileWater(BoringTile):
	"""The boring tile for the second level"""
	def intro_text(self):
		text = story.water_texts[random.randint(0, len(story.water_texts)-1)]
		return text


class BoringTileFire(BoringTile):
	"""The boring tile for the third level"""
	def intro_text(self):
		text = story.fire_texts[random.randint(0, len(story.fire_texts)-1)]
		return text


class BoringTileAir(BoringTile):
	"""The boring tile for the fourth level"""
	def intro_text(self):
		text = story.air_texts[random.randint(0, len(story.air_texts)-1)]
		return text


class CorridorTile(MapTile):
	"""A plain tile with no other functionality.
	This tile is also a base class for other tiles."""
	def intro_text(self):
		return """
This seems to be a corridor. 
I wonder where it leads. 
		"""

	def modify_player(self, player, mod=None):
		player.score += 1


class CorridorTileStone(CorridorTile):
	"""Corridor tile for the first level"""
	def intro_text(self):
		try:
			text = story.corridor_texts["stone"]
			return text
		except KeyError:
			return "This is a rocky corridor"


class CorridorTileWater(CorridorTile):
	"""Corridor tile for the second level"""
	def intro_text(self):
		try:
			text = story.corridor_texts["water"]
			return text
		except KeyError:
			return "This is a watery corridor"


class CorridorTileFire(CorridorTile):
	"""Corridor tile for the third level"""
	def intro_text(self):
		try:
			text = story.corridor_texts["fire"]
			return text
		except KeyError:
			return "This is a fiery corridor"


class CorridorTileAir(CorridorTile):
	"""Corridor tile for the fourth level"""
	def intro_text(self):
		try:
			text = story.corridor_texts["air"]
			return text
		except KeyError:
			return "This is a airy corridor"


class VictoryTile(MapTile):
	"""Tile that declares the player's victory.
	The last tile in the game."""
	def modify_player(self, player, mod=None):
		player.victory = True
		player.score += 25

	def intro_text(self):
		return f"""{Fore.LIGHTYELLOW_EX}{story.complete}"""


class FindGoldTile(MapTile):
	"""This tile has a random amount of gold for the player to collect"""
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
	"""This tile has a random amount of crystals for the player to collect"""
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
	"""This tile has level 1 enemies"""
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
	"""This tile has level 2 enemies"""
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


class EnemyTile3(MapTile):
	"""This tile has level 3 enemies"""
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


class EnemyTile4(MapTile):
	"""This tile has level 4 enemies"""
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
	"""This tile has level 1 special enemies"""
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
	"""This tile has level 2 special enemies"""
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
	"""This tile has level 3 special enemies"""
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
	"""This tile has level 4 special enemies"""
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
	"""Thsi is the level 1 diety"""
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
			player.boss = 1


class HydroBoss(MapTile):
	"""This is the level 2 diety"""
	def __init__(self, x, y):
		self.enemy = enemies.Hydromancer()
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
				print(
					f"The {Fore.RED}{self.enemy.name}{Fore.RESET} does {self.enemy.damage} damage. You have {Fore.GREEN}{round(player.hp, 0)} {Fore.RESET}HP remaining\n")

		if not self.enemy.is_alive():
			self.completed = True
			player.boss = 2


class PyroBoss(MapTile):
	"""This is the level 3 deity"""
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
			player.boss = 3


class AeroBoss(MapTile):
	"""This is the level 4 deity"""
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
			player.boss = 4


class TraderTile(MapTile):
	"""This tile has the trader"""
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
	"""This tile has the weapon smith"""
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
	"""This tile has the armour smith"""
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
	"""This tile has the enchanter"""
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
	"""This tile has the quest lady(quest NPC)"""
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
	"""This tile has the quest item needed to complete a quest"""
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
	"""This tile has the first story teller"""
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
			return f"""Just the same {Fore.LIGHTMAGENTA_EX}{npc.StoryTeller1().name}{Fore.RESET} from earlier.\n"""

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
	"""This tile has the second story teller"""
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
	"""This tile has the enemy player"""
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


class StoryTellerTile3(MapTile):
	"""This tile has the third story teller"""
	encounter = 0

	def __init__(self, x, y):
		super().__init__(x, y)
		self.storyteller = npc.StoryTeller3()

	def intro_text(self):
		if self.encounter == 0:
			return f"""
You see an old and distinguished-looking man. 
His hair is slick and he is wearing a black suit. 
					"""
		else:
			return f"""
There he is again, your uncle. 
{Fore.LIGHTMAGENTA_EX}{self.storyteller.name}{Fore.RESET}
			"""

	def ready_to_goodbye(self, player):
		print(self.storyteller.messages["ready"])
		reply1 = input()
		if self.looking_through_input(reply1, ["yes", "y", "yeah", "1", "1."]):
			print(self.storyteller.messages["give"])
			self.modify_player(player, 1)
			print(self.storyteller.messages["given"])
			print(self.storyteller.messages["what-to-say"])
			reply2 = input()
			if self.looking_through_input(reply2, ["thanks", "thank you", "thnx", "thx", "grateful"]):
				print(self.storyteller.messages["gratitude"])
			else:
				print(self.storyteller.messages["ungrateful"])

			print(self.storyteller.messages["nephew"])
			print("")
			print(self.storyteller.messages["goodbye"])
		else:
			print("Well you look ready enough to me.")
			print("Let me give you something that might help ypu along the way.")
			self.modify_player(player, 1)
			print(self.storyteller.messages["given"])
			print(self.storyteller.messages["what-to-say"])
			reply2 = input()
			if self.looking_through_input(reply2, ["thanks", "thank you", "thnx", "thx", "grateful"]):
				print(self.storyteller.messages["gratitude"])
			else:
				print(self.storyteller.messages["ungrateful"])
			print(self.storyteller.messages["nephew"])
			print("")
			print(self.storyteller.messages["goodbye"])

	def about_to_tell(self):
		print(self.storyteller.messages["here-i-go"])
		for line in self.storyteller.messages["STORY"]:
			if len(line) > 30:
				time.sleep(3.5)
				print(line)
			elif len(line) > 20:
				time.sleep(2)
				print(line)
			else:
				time.sleep(1.5)
				print(line)

	def converse(self, player):
		self.encounter += 1
		if self.encounter == 1:
			try:
				print(self.storyteller.messages['one'])
				ans1 = input()
				if ans1:
					print(self.storyteller.messages["two"])
					ans2 = input()
					if self.looking_through_input(ans2, ["yes", "y", "yeah", "1", "1."]):
						print(self.storyteller.messages["remember"])
						ans3 = input()
						if ans3 == self.storyteller.name.lower():
							print(self.storyteller.messages["correct"])
							ans4 = input()
							if self.looking_through_input(ans4, ["yes", "y", "yeah", "1", "1."]):
								print(self.storyteller.messages["correct-story"])
								self.about_to_tell()
								self.ready_to_goodbye(player)

							else:
								print(self.storyteller.messages["tell"])
								self.about_to_tell()
								self.ready_to_goodbye(player)
						else:
							print(self.storyteller.messages["wrong_name"])
							print(self.storyteller.messages["forget"])
							y_n = input()
							if self.looking_through_input(y_n, ["yes", "y", "yeah", "1", "1."]):
								print(self.storyteller.messages["who_i_am"])
								self.about_to_tell()
								self.ready_to_goodbye(player)

							else:
								print(self.storyteller.messages["rude"])
								self.about_to_tell()
								self.ready_to_goodbye(player)
									
					else:
						print(self.storyteller.messages["forget"])
						resp1 = input()
						if self.looking_through_input(resp1, ["yes", "y", "yeah", "1", "1."]):
							print(self.storyteller.messages["tell"])
							self.about_to_tell()
							self.ready_to_goodbye(player)

				else:
					print(self.storyteller.messages["nothing"])
					self.about_to_tell()
					self.ready_to_goodbye(player)

			except KeyError:
				print("It seems something has gone wrong.")
				print("The man standing before you, tells you that he is your uncle?!\n")
				print("He seems to have something to give you.")
				self.modify_player(player)
				print("The man who was standing in front of you begins to walk away.")
				print("It seems it is up to you to save the world.")
				print("Continue your adventure...\n")
				print("You have almost reached the end...")
		else:
			print("Nephew, what are you doing here.\nIs that cowardice I smell.\nGo on, continue your adventure!")

	def modify_player(self, player, mod=None):
		if self.encounter == 1 and mod == 1:
			pass
		else:
			return

		def give(player_arg):
			giving = [items.MechaDagger(), items.Cash()]
			player_arg.inventory.extend(giving)
			for _ in giving:
				print(f"{Fore.LIGHTMAGENTA_EX}{self.storyteller.name}{Fore.RESET} has given you: {Fore.LIGHTBLUE_EX}{_.name}{Fore.RESET}")
			print("")

		try:
			if self.storyteller.inventory:
				to_give = self.storyteller.inventory
				player.inventory.extend(to_give)
				for item in to_give:
					print(f"{Fore.LIGHTMAGENTA_EX}{self.storyteller.name}{Fore.RESET} has given you: {Fore.LIGHTBLUE_EX}{item.name}{Fore.RESET}")
				print("")
				self.storyteller.inventory.clear()
			else:
				give(player)
		except (TypeError, ValueError):
			try:
				give(player)
			except (AttributeError, IndexError):
				print("It seems that I have nothing to give you.")


class RandomCharacterTile(MapTile):
	"""This tile gives the player random messages"""
	def __init__(self, x, y):
		super().__init__(x, y)
		self.story = npc.TalkingCharacter()

	def intro_text(self):
		text = random.sample(self.story.messages, 1)
		text = f"{Fore.LIGHTMAGENTA_EX}{text[0]}{Fore.RESET}"
		return text


class LevelTile1(MapTile):
	"""This tile tells the player ehat level that are on"""
	def __init__(self, x, y):
		super().__init__(x, y)
		try:
			self.story = story.levels["level1"]
		except KeyError:
			self.story = "LEVEL 1"

	def intro_text(self):
		return self.story


class LevelTile2(MapTile):
	"""This tile tells the player ehat level that are on"""
	def __init__(self, x, y):
		super().__init__(x, y)
		try:
			self.story = story.levels["level2"]
		except KeyError:
			self.story = "LEVEL 2"

	def intro_text(self):
		return self.story


class LevelTile3(MapTile):
	"""This tile tells the player ehat level that are on"""
	def __init__(self, x, y):
		super().__init__(x, y)
		try:
			self.story = story.levels["level3"]
		except KeyError:
			self.story = "LEVEL 3"

	def intro_text(self):
		return self.story


class LevelTile4(MapTile):
	"""This tile tells the player ehat level that are on"""
	def __init__(self, x, y):
		super().__init__(x, y)
		try:
			self.story = story.levels["level4"]
		except KeyError:
			self.story = "LEVEL 4" 

	def intro_text(self):
		return self.story
		

class StoneTile(MapTile):
	"""This tile is used to give the player a stone (needed fro progression)."""
	def __init__(self, x, y):
		super().__init__(x, y)
		self.item = None
		self.taken = False
		
	def intro_text(self):
		return """
		You see a glowing stone levitating before you. 
		Why does it seem important. 
		What secrets does this glowing stone hold"""

	def give_stone(self, player):
		print(f"""
		The sought after {Fore.BLUE}{self.item.name}{Fore.RESET}
		Will you take the stone?
		""")
		take = input("")
		print("")
		if self.looking_through_input(take, ["yes", "y", "yeah", "yea", "yip"]):
			print(f"You have taken the {Fore.BLUE}{self.item.name}{Fore.RESET}")
			player.inventory.append(self.item)
			self.taken = True
		elif self.looking_through_input(take, ["no", "n", "nope", "nay"]):
			print("You are the fated hero...CORONA")
			print(f"The {Fore.BLUE}{self.item.name}{Fore.RESET} levitates towards you.")
			print("This is something you cannot refuse.")
			player.inventory.append(self.item)
			self.taken = True
		else:
			self.modify_player(player, None)

	def modify_player(self, player, mod=None):
		if self.taken:
			return

		if player.boss == 1:
			self.item = items.GeoStone()
			self.give_stone(player)
		elif player.boss == 2:
			self.item = items.HydroStone()
			self.give_stone(player)
		elif player.boss == 3:
			self.item = items.PyroStone()
			self.give_stone(player)
		elif player.boss == 4:
			self.item = items.AeroStone()
			self.give_stone(player)


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

# RCT Random Character Tile

# LT1 Level Tile 1
# LT1 Level Tile 2
# LT1 Level Tile 3
# LT1 Level Tile 4

# STT Stone Tile Tile

# BTS Boring Tile Stone
# BTW Boring Tile Water
# BTF Boring Tile Fire
# BTA Boring Tile Air


world_dsl = """
|   |   |   |   |   |   |   |   |   |   |   |   |ST |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |LT1|CTS|CTS|CTS|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |ST1|EN1|RCT|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |FG |BTS|BTS|BTS|   |FG |EN1|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |TT |   |BTS|   |   |FQI|EN1|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |EN1|CTS|   |RCT|EN1|CTS|CTS|BTS|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |CTS|   |QT |BTS|   |   |BTS|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |WST|EN1|BTS|EN1|BTS|BTS|BTS|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |ET |AST|FC |   |BTS|TT |   |EN1|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |BTS|EN1|BTS|TT |EN1|EN1|BTS|EN1|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |BTS|   |   |CTS|   |BTS|   |FC |   |   |   |   |   |   |   |   |   |BTA|BTA|TT |ET |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |BTS|EN1|ET |CTS|BTS|RCT|   |   |   |   |   |   |   |   |   |   |EN4|BTA|EN4|   |CTA|   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |CTS|   |   |   |   |   |   |   |   |   |   |   |BTA|BT |   |   |   |CTA|   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |FG |BTS|FC |   |   |   |   |   |   |   |   |   |EN3|BTA|EN4|EN4|BTA|   |EN4|BTA|BTA|EN4|   |   |
|   |   |FC |EN2|BTW|FG |CTW|EN1|BT |EN2|FC |   |   |   |GE |GE |GE |   |   |   |   |   |   |   |   |   |FG |EN3|   |   |BTA|EN4|CTA|   |   |AE |   |   |
|   |   |   |   |   |BTW|CTW|   |   |   |   |   |   |   |   |GE |   |   |   |   |   |   |   |   |   |   |   |BT |   |   |ECT|   |CTA|AE |AE |AE |   |   |
|   |   |   |   |   |EN2|CTW|   |   |   |   |   |   |QT |   |GB |   |   |   |   |   |   |   |   |   |   |   |EN4|TT |   |FQI|   |AE |AE |AE |AB |STT|VT |
|   |   |   |HE |HE |   |EN2|ET |WST|EN |RCT|   |RCT|EN2|   |STT|   |   |   |   |   |   |   |   |   |   |   |FC |EN4|WST|BTA|   |CTA|AE |AE |AE |   |   |
|BT |STT|HB |HE |HE |BTW|BTW|   |   |   |FC |BTW|EN2|EN1|ST2|LT2|   |   |   |   |   |   |   |   |   |   |FG |EN4|   |   |BTA|   |CTA|   |   |AE |   |   |
|CTW|   |CTW|HE |HE |   |BTW|EN2|FG |EN2|EN2|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |EN3|BT |   |   |EN4|   |RCT|   |   |EN |   |   |
|CTW|   |CTW|EN2|FQI|EN2|EN2|   |BTW|   |BTW|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |CTA|CTA|CTA|EN3|EN4|TT |BTA|EN4|BTA|   |   |
|CTW|   |   |AST|   |   |   |   |TT |EN2|BTW|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |EN4|BTA|   |   |EN4|   |   |   |   |   |
|CTW|   |   |BTW|RCT|EN2|EN2|BTW|BTW|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |BTA|BTA|QT |ST3|   |   |   |   |   |
|CTF|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |EN2|   |   |   |   |   |
|CTF|   |TT |FC |   |   |   |CTF|EN2|EN3|BT |WST|RCT|EN |EN2|TT |   |   |BTF|   |   |   |   |   |   |   |   |   |   |   |   |   |EN1|   |   |   |   |   |
|CTF|   |EN2|   |EN3|QT |   |CTF|   |CTF|   |   |   |   |   |BTF|EN2|   |PE |PE |   |   |   |   |   |   |BT |BTA|FC |FG |WST|   |BTA|   |   |   |   |   |
|LT3|BTF|BTF|BTF|EN3|RCT|BTF|EN3|   |ECT|EN3|FG |BTF|BTF|EN3|ET |EN3|PE |PE |BT |PE |PB |STT|LT4|CTA|CTA|RCT|BTA|FC |FG |CTA|CTA|CTA|   |   |   |   |   |
|   |   |FG |   |EN2|   |EN3|   |   |CTF|   |   |AST|   |   |BTF|EN3|   |PE |PE |   |   |   |   |   |   |BTA|BTA|ET |TT |AST|   |   |   |   |   |   |   |
|   |   |ET |EN2|   |BTF|FQI|FG |EN3|CTF|   |   |BTF|EN1|FC |TT |   |   |BTF|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
"""


def is_dsl_valid(dsl):
	"""This function checks if the dsl is valid"""
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
				"ST3": StoryTellerTile3,
				"ECT": EnemyChallengeTile,
				"RCT": RandomCharacterTile,
				"LT1": LevelTile1,
				"LT2": LevelTile2,
				"LT3": LevelTile3,
				"LT4": LevelTile4,
				"STT": StoneTile,
				"BTS": BoringTileStone,
				"BTW": BoringTileWater,
				"BTF": BoringTileFire,
				"BTA": BoringTileAir,
				"CTS": CorridorTileStone,
				"CTW": CorridorTileWater,
				"CTF": CorridorTileFire,
				"CTA": CorridorTileAir,
				"   ": None
}

world_map = []
start_tile_location = None


def parse_world_dsl():
	"""This function creates the map from the dsl"""
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
	"""This function checks current position and returns it"""
	if x < 0 or y < 0:
		return None
	try:
		return world_map[y][x]
	except IndexError:
		return None
