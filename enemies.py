"""This script is for the enemies class that will have all of the enemies that will be in the game"""
import random
import colorama
from colorama import Fore, Style


colorama.init(autoreset=True)


class Enemy:
	def __init__(self):
		self.name = "Enemy"
		self.hp = 0
		self.damage = 0
		self.score = 10
		self.reward = random.randint(1, 8)

	def __str__(self):
		return f"{Style.BRIGHT}{Fore.LIGHTRED_EX}{self.name}"

	def is_alive(self):
		return self.hp > 0

	def fight(self):
		if self.is_alive() is True:
			fight = True
		else:
			fight = False
		return fight


class GiantSpider(Enemy):
	def __init__(self, level):
		super().__init__()
		self.name = "Giant Spider"

		if level == 1:
			self.hp = 10
			self.damage = 10
		elif level == 2:
			self.hp = 12
			self.damage = 10
		elif level == 3:
			self.hp = 20
			self.damage = 15
		elif level == 4:
			self.hp = 25
			self.damage = 18
		else:
			self.hp = 15
			self.damage = 15

		self.defence = 0
		self.type = "normal"


class OvergrownInsect(Enemy):
	def __init__(self, level):
		super().__init__()
		self.name = "Overgrown Insect"

		if level == 1:
			self.hp = 10
			self.damage = 10
		elif level == 2:
			self.hp = 15
			self.damage = 15
		elif level == 3:
			self.hp = 20
			self.damage = 20
		elif level == 4:
			self.hp = 25
			self.damage = 25
		else:
			self.hp = 15
			self.damage = 15

		self.defence = 0
		self.type = "normal"


class Undead(Enemy):
	def __init__(self, level):
		super().__init__()
		self.name = "Undead"

		if level == 1:
			self.hp = 15
			self.damage = 10
		elif level == 2:
			self.hp = 25
			self.damage = 15
		elif level == 3:
			self.hp = 30
			self.damage = 20
		elif level == 4:
			self.hp = 35
			self.damage = 25
		else:
			self.hp = 25
			self.damage = 15

		self.defence = 0
		self.type = "normal"


class SkeletalWarrior(Enemy):
	def __init__(self, level):
		super().__init__()
		self.name = "Skeletal Warrior"

		if level == 1:
			self.hp = 12
			self.damage = 15
		elif level == 2:
			self.hp = 15
			self.damage = 20
		elif level == 3:
			self.hp = 20
			self.damage = 25
		elif level == 4:
			self.hp = 25
			self.damage = 35
		else:
			self.hp = 15
			self.damage = 25

		self.defence = 0
		self.type = "normal"


class BatSwarm(Enemy):
	def __init__(self, level):
		super().__init__()
		self.name = "Swarm of Bats"

		if level == 1:
			self.hp = 15
			self.damage = 8
		elif level == 2:
			self.hp = 15
			self.damage = 10
		elif level == 3:
			self.hp = 20
			self.damage = 18
		elif level == 4:
			self.hp = 30
			self.damage = 20
		else:
			self.hp = 20
			self.damage = 15
		self.defence = 0
		self.type = "normal"


class Lamia(Enemy):
	def __init__(self, level):
		super().__init__()
		self.name = "Lamia"

		if level == 1:
			self.hp = 35
			self.damage = 25
		elif level == 2:
			self.hp = 45
			self.damage = 30
		elif level == 3:
			self.hp = 55
			self.damage = 35
		elif level == 4:
			self.hp = 65
			self.damage = 45
		else:
			self.hp = 15
			self.damage = 15

		self.defence = 0
		self.type = "normal"


# The rock based enemies
class Ogre(Enemy):
	def __init__(self):
		super().__init__()
		self.name = "Ogre"
		self.hp = 30
		self.damage = 5
		self.defence = 0
		self.type = "rock"
		self.score = 15


class Golem(Enemy):
	def __init__(self):
		super().__init__()
		self.name = "Golem"
		self.hp = 45
		self.damage = 5
		self.defence = 0
		self.type = "rock"
		self.score = 15


class Gargoyle(Enemy):
	def __init__(self):
		super().__init__()
		self.name = "Gargoyle"
		self.hp = 30
		self.damage = 10
		self.defence = 0
		self.type = "rock"
		self.score = 15


# The water based enemies
class Hydra(Enemy):
	def __init__(self):
		super().__init__()
		self.name = "Hydra"
		self.hp = 30
		self.damage = 10
		self.defence = 2
		self.type = "water"
		self.score = 20


class WaterNymph(Enemy):
	def __init__(self):
		super().__init__()
		self.name = "Water Nymph"
		self.hp = 20
		self.damage = 10
		self.defence = 2
		self.type = "water"
		self.score = 20


class SeaSerpent(Enemy):
	def __init__(self):
		super().__init__()
		self.name = "Sea Serpent"
		self.hp = 25
		self.damage = 15
		self.defence = 2
		self.type = "water"
		self.score = 20


# The fire based enemies
class BabyPhoenix(Enemy):
	def __init__(self):
		super().__init__()
		self.name = "Baby Phoenix"
		self.hp = 10
		self.damage = 25
		self.defence = 2
		self.type = "fire"
		self.score = 25


class Salamander(Enemy):
	def __init__(self):
		super().__init__()
		self.name = "Salamander"
		self.hp = 15
		self.damage = 30
		self.defence = 2
		self.type = "fire"
		self.score = 25


class HellHound(Enemy):
	def __init__(self):
		super().__init__()
		self.name = "Hell Hound"
		self.hp = 20
		self.damage = 25
		self.defence = 2
		self.type = "fire"
		self.score = 25


# The air based enemies
class Harpy(Enemy):
	def __init__(self):
		super().__init__()
		self.name = "Harpy"
		self.hp = 25
		self.damage = 15
		self.defence = 2
		self.type = "air"
		self.score = 30


class ThunderBird(Enemy):
	def __init__(self):
		super().__init__()
		self.name = "Thunder Bird"
		self.hp = 25
		self.damage = 20
		self.defence = 2
		self.type = "air"
		self.score = 30


class Manticore(Enemy):
	def __init__(self):
		super().__init__()
		self.name = "Manticore"
		self.hp = 30
		self.damage = 30
		self.defence = 2
		self.type = "air"
		self.score = 30


# The Boss Enemies
class Geomancer(Enemy):
	def __init__(self):
		super().__init__()
		self.name = "Geomancer"
		self.hp = 70
		self.damage = 15
		self.defence = 0
		self.type = "rock"
		self.score = 45
		self.reward = random.randint(10, 20)


class Hydromancer(Enemy):
	def __init__(self):
		super().__init__()
		self.name = "Hydromancer"
		self.hp = 90
		self.damage = 25
		self.defence = 1
		self.type = "water"
		self.score = 55
		self.reward = random.randint(15, 25)


class Pyromancer(Enemy):
	def __init__(self):
		super().__init__()
		self.name = "Pyromancer"
		self.hp = 110
		self.damage = 35
		self.defence = 3
		self.type = "fire"
		self.score = 65
		self.reward = random.randint(25, 30)


class Aeromancer(Enemy):
	def __init__(self):
		super().__init__()
		self.name = "Aeromancer"
		self.hp = 130
		self.damage = 45
		self.defence = 3
		self.type = "air"
		self.score = 75
		self.reward = random.randint(35, 45)


class Challenger(Enemy):
	def __init__(self):
		super().__init__()
		self.name = "Evil Wanderer"
		self.hp = 100
		self.score = 50
		self.reward = random.randint(50, 60)
