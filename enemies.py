"""This script is for the enemies class that will have all of the enemies that will be in the game"""
import random
import colorama
import items
from colorama import Fore


colorama.init(autoreset=True)


class Enemy:
	"""This is the base class for all enemies."""
	def __init__(self):
		self.name = "Enemy"
		self.hp = 0
		self.damage = 0
		self.score = 5
		self.reward = random.randint(1, 8)

	def __str__(self):
		return f"{Fore.LIGHTRED_EX}{self.name}"

	def is_alive(self):
		"""This function checks if the enemy is still alive"""
		return self.hp > 0

	def fight(self):
		"""This function checks if an enemy is in a fight"""
		if self.is_alive() is True:
			fight = True
		else:
			fight = False
		return fight

	def alive_text(self):
		"""This function returns a string if the enemy is alive"""
		return f"""The {self.name} is still alive"""

	def dead_text(self):
		"""This function returns a string if the enmey is dead"""
		f"""The {self.name} has been defeated"""


class GiantSpider(Enemy):
	def __init__(self, level):
		super().__init__()
		self.name = "Giant Spider"

		if level == 1:
			self.hp = 10
			self.damage = 8
		elif level == 2:
			self.hp = 12
			self.damage = 12
		elif level == 3:
			self.hp = 20
			self.damage = 15
		elif level == 4:
			self.hp = 25
			self.damage = 18
		else:
			self.hp = 10
			self.damage = 12

		self.defence = 0
		self.type = "normal"

	def alive_text(self):
		return f"""
A {Fore.LIGHTRED_EX}{self.name}{Fore.RESET} crawls down from the wall.
It stands right in front of you, 
You are its prey.\n
                            """

	def dead_text(self):
		return f"""
The corpse of a dead {Fore.LIGHTRED_EX}{self.name}{Fore.RESET} lies before you.
Your victory is now certain.\n
                            """


class OvergrownInsect(Enemy):
	def __init__(self, level):
		super().__init__()
		self.name = "Overgrown Insect"

		if level == 1:
			self.hp = 10
			self.damage = 7
		elif level == 2:
			self.hp = 15
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

	def alive_text(self):
		return f"""
A {Fore.LIGHTRED_EX}{self.name}{Fore.RESET} sets its eyes on you.
Will you make it out alive?\n
                            """

	def dead_text(self):
		return f"""
The {Fore.LIGHTRED_EX}{self.name}{Fore.RESET} is dead.
You fought valiantly, 
Its corpse is now your trophy.\n
                            """


class Undead(Enemy):
	def __init__(self, level):
		super().__init__()
		self.name = "Undead"

		if level == 1:
			self.hp = 15
			self.damage = 6
		elif level == 2:
			self.hp = 16
			self.damage = 10
		elif level == 3:
			self.hp = 20
			self.damage = 14
		elif level == 4:
			self.hp = 35
			self.damage = 20
		else:
			self.hp = 25
			self.damage = 15

		self.defence = 0
		self.type = "normal"

	def alive_text(self):
		return """
A dead explorer's corpse rises.
Will you join him in the dance of death?\n
                    """

	def dead_text(self):
		return """
Can a dead person die again?
Hmm, Maybe?\n
                                """


class SkeletalWarrior(Enemy):
	def __init__(self, level):
		super().__init__()
		self.name = "Skeletal Warrior"

		if level == 1:
			self.hp = 12
			self.damage = 12
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

	def alive_text(self):
		return f"""
The rattling of bones. 
The hastening of your death?
A {Fore.LIGHTRED_EX}{self.name}{Fore.RESET}\n
                            """

	def dead_text(self):
		return f"""
The {Fore.LIGHTRED_EX}{self.name}{Fore.RESET} is dead.
Only its bones remain.\n
                                """


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

	def alive_text(self):
		return f"""
A {Fore.LIGHTRED_EX}{self.name}{Fore.RESET} fly right above your head.
Each looking more blood thirsty than the last.\n
                """

	def dead_text(self):
		return f"""
You have done it.
The {Fore.LIGHTRED_EX}{self.name}{Fore.RESET} didn't have a chance.\n
                        """


class Lamia(Enemy):
	def __init__(self, level):
		super().__init__()
		self.name = "Lamia"

		if level == 1:
			self.hp = 30
			self.damage = 20
		elif level == 2:
			self.hp = 35
			self.damage = 25
		elif level == 3:
			self.hp = 40
			self.damage = 30
		elif level == 4:
			self.hp = 45
			self.damage = 35
		else:
			self.hp = 25
			self.damage = 15

		self.defence = 0
		self.type = "normal"

	def alive_text(self):
		return f"""
A {Fore.LIGHTRED_EX}{self.name}{Fore.RESET} stands before you.
Your luck has run out.
Is it time to say goodbye?\n
                        """

	def dead_text(self):
		return """
You have escaped death. 
You won't be so lucky next time\n
                                """


# The rock based enemies
class Ogre(Enemy):
	def __init__(self):
		super().__init__()
		self.name = "Ogre"
		self.hp = 18
		self.damage = 9
		self.defence = 0
		self.type = "rock"
		self.score = 7

	def alive_text(self):
		return f"""
The ground begins to shake.
A blood thirsty {Fore.LIGHTRED_EX}{self.name}{Fore.RESET} stands before you
How long do you have to live?
                """

	def dead_text(self):
		return f"""
The ground is still shaking.
But, the {Fore.LIGHTRED_EX}{self.name}{Fore.RESET} is dead.
You must be getting close. 
			"""


class Golem(Enemy):
	def __init__(self):
		super().__init__()
		self.name = "Golem"
		self.hp = 20
		self.damage = 10
		self.defence = 0
		self.type = "rock"
		self.score = 7

	def alive_text(self):
		return f"""
The ground begins to shake. 
Could it be this hunky {Fore.LIGHTRED_EX}{self.name}{Fore.RESET}?
			"""

	def dead_text(self):
		return f"""
The ground is still shaking.
The {Fore.LIGHTRED_EX}{self.name}{Fore.RESET} is now just a pile of rocks.
You must be getting close.
			"""


class Gargoyle(Enemy):
	def __init__(self):
		super().__init__()
		self.name = "Gargoyle"
		self.hp = 24
		self.damage = 12
		self.defence = 0
		self.type = "rock"
		self.score = 7

	def alive_text(self):
		return f"""
The ground begins to shake.
The {Fore.LIGHTRED_EX}{self.name}{Fore.RESET} sheds its stony surface. 
It is ready to attack.
			"""

	def dead_text(self):
		return """
The ground is still shaking.
Even its stony skin wouldn't have made a difference
You must be getting close.
			"""


# The water based enemies
class Hydra(Enemy):
	def __init__(self):
		super().__init__()
		self.name = "Hydra"
		self.hp = 25
		self.damage = 14
		self.defence = 2
		self.type = "water"
		self.score = 7

	def alive_text(self):
		return f"""
You begin to hear crashing waves.
A {Fore.LIGHTRED_EX}{self.name}{Fore.RESET} stands before you. 
All of its eyes looking straight at you.
								"""

	def dead_text(self):
		return f"""
The sound of crashing waves intensifies
The {Fore.LIGHTRED_EX}{self.name}{Fore.RESET} is dead and,
You have 3 heads to prove it.
You must be getting close. 
			"""


class WaterNymph(Enemy):
	def __init__(self):
		super().__init__()
		self.name = "Water Nymph"
		self.hp = 20
		self.damage = 10
		self.defence = 2
		self.type = "water"
		self.score = 7

	def alive_text(self):
		return f"""
You begin to hear crashing waves.
You have disturbed the waters of a {Fore.LIGHTRED_EX}{self.name}{Fore.RESET}.
You have incurred her wrath.
							"""

	def dead_text(self):
		return f"""
The sound of crashing waves intensifies.
She did not stand a chance.
You must be getting close.
			"""


class SeaSerpent(Enemy):
	def __init__(self):
		super().__init__()
		self.name = "Sea Serpent"
		self.hp = 25
		self.damage = 15
		self.defence = 2
		self.type = "water"
		self.score = 7

	def alive_text(self):
		return f"""
You begin to hear crashing waves.
A {Fore.LIGHTRED_EX}{self.name}{Fore.RESET}, 
Have you just slithered into your death?
							"""

	def dead_text(self):
		return """
The sound of crashing waves intensifies.
Next time you might not be that lucky.
You must be getting close.
			"""


# The fire based enemies
class BabyPhoenix(Enemy):
	def __init__(self):
		super().__init__()
		self.name = "Baby Phoenix"
		self.hp = 8
		self.damage = 25
		self.defence = 2
		self.type = "fire"
		self.score = 7

	def alive_text(self):
		return f"""
It's getting hotter by the second.
A {Fore.LIGHTRED_EX}{self.name}{Fore.RESET} flaps its fiery wings
Will you burned along with everything else?
							"""

	def dead_text(self):
		return f"""
The ground below you is now magma.
You have extinguished the {Fore.LIGHTRED_EX}{self.name}{Fore.RESET}

You must be getting close.

			"""


class Salamander(Enemy):
	def __init__(self):
		super().__init__()
		self.name = "Salamander"
		self.hp = 10
		self.damage = 30
		self.defence = 2
		self.type = "fire"
		self.score = 7

	def alive_text(self):
		return f"""
It is getting hotter by the second
A {Fore.LIGHTRED_EX}{self.name}{Fore.RESET} stands before you.
A giant fiery lizard.
Will you be charred? 
							"""

	def dead_text(self):
		return """
The ground below you is magma.
It seems nothing can stop you

You must be getting close

			"""


class HellHound(Enemy):
	def __init__(self):
		super().__init__()
		self.name = "Hell Hound"
		self.hp = 14
		self.damage = 25
		self.defence = 2
		self.type = "fire"
		self.score = 7

	def alive_text(self):
		return f"""
It's getting hotter by the second.
A {Fore.LIGHTRED_EX}{self.name}{Fore.RESET} of incredible size is before you
Has  your luck run out?
								"""

	def dead_text(self):
		return f"""
The ground below you is now magma.
You turned that {Fore.LIGHTRED_EX}{self.name}{Fore.RESET} into a hell puppy.

You must be getting close.  """


# The air based enemies
class Harpy(Enemy):
	def __init__(self):
		super().__init__()
		self.name = "Harpy"
		self.hp = 22
		self.damage = 15
		self.defence = 2
		self.type = "air"
		self.score = 7

	def alive_text(self):
		return f"""
The air seems to be getting thinner.
Yor mere presence has angered a {Fore.LIGHTRED_EX}{self.name}{Fore.RESET}.
You shall face death by its talons
								"""

	def dead_text(self):
		return f"""
You can barely breathe now.
The {Fore.LIGHTRED_EX}{self.name}{Fore.RESET} has fallen. 
You have clipped its once might wings

							You must be getting close. 

			"""


class ThunderBird(Enemy):
	def __init__(self):
		super().__init__()
		self.name = "Thunder Bird"
		self.hp = 25
		self.damage = 20
		self.defence = 2
		self.type = "air"
		self.score = 7

	def alive_text(self):
		return f"""
The air seems to be getting thinner.
Will you survive its onslaught?
							"""

	def dead_text(self):
		return f"""
You can barely breathe now
The {Fore.LIGHTRED_EX}{self.name}{Fore.RESET} is dead. 
Hmm, how much do those feathers cost?

You must be getting close.

			"""


class Manticore(Enemy):
	def __init__(self):
		super().__init__()
		self.name = "Manticore"
		self.hp = 25
		self.damage = 25
		self.defence = 2
		self.type = "air"
		self.score = 7

	def alive_text(self):
		return f"""
The air is getting thinner.
A {Fore.LIGHTRED_EX}{self.name}{Fore.RESET} stands before you.
It is unconquerable.
							"""

	def dead_text(self):
		return f"""
You can barely breathe now.
You have conquered the unconquerable
Could you save humanity?

You must be getting close

			"""


# The Boss Enemies
class Geomancer(Enemy):
	def __init__(self):
		super().__init__()
		self.name = "Geomancer"
		self.hp = 50
		self.damage = 16
		self.defence = 0
		self.type = "rock"
		self.score = 15
		self.reward = random.randint(10, 20)

	def alive_text(self):
		return f"""
The ground is now shaking violently.
The rocks in front of you begin to move.
Spikes made of rock begin to grow out of the roof of the cave.
You are in its presence;
The {Fore.LIGHTRED_EX}{self.name}{Fore.RESET}!

		"""

	def dead_text(self):
		return f"""
The ground stops shaking. 
Everything is silent. 
The rocks before you begin to disintegrate.
The {Fore.LIGHTRED_EX}{self.name}{Fore.RESET} is dead.

The ground begins to crumble.
		"""


class Hydromancer(Enemy):
	def __init__(self):
		super().__init__()
		self.name = "Hydromancer"
		self.hp = 65
		self.damage = 22
		self.defence = 0
		self.type = "water"
		self.score = 15
		self.reward = random.randint(15, 25)

	def alive_text(self):
		return f"""
The crashing waves are are more violent than ever.
The water level is rising. 
The terrace you are standing on is not enough. 
The waves are raging. 
As if a hurricane is about to erupt within the cave.
The {Fore.LIGHTRED_EX}{self.name}{Fore.RESET} is before you 
		"""

	def dead_text(self):
		return f"""
The waves retreat.
The violent storm comes to an end. 
A soft mist begins to fall. 
The {Fore.LIGHTRED_EX}{self.name}{Fore.RESET}is dead,
You are victorious.
		"""


class Pyromancer(Enemy):
	def __init__(self):
		super().__init__()
		self.name = "Pyromancer"
		self.hp = 75
		self.damage = 26
		self.defence = 1
		self.type = "fire"
		self.score = 15
		self.reward = random.randint(25, 30)

	def alive_text(self):
		return f"""
The ground below you is now beginning to bubble. 
The heat is more than you can bear. 
The sweat falling from your face evaporates before it hits the ground
The {Fore.LIGHTRED_EX}{self.name}{Fore.RESET} must be close by, 
and your death?

		"""

	def dead_text(self):
		return f"""
The temperature suddenly drops.
The magma cools. 
You have done it. 
The great {Fore.LIGHTRED_EX}{self.name}{Fore.RESET} has fallen by your hands
		"""


class Aeromancer(Enemy):
	def __init__(self):
		super().__init__()
		self.name = "Aeromancer"
		self.hp = 80
		self.damage = 35
		self.defence = 2
		self.type = "air"
		self.score = 15
		self.reward = random.randint(35, 45)

	def alive_text(self):
		return f"""
You can barely breathe now. 
Will you did for suffocation before the fight begins
Have you come this far just to die?
Will the {Fore.LIGHTRED_EX}{self.name}{Fore.RESET} be your end?

		"""

	def dead_text(self):
		return f"""
A lifeless figure is all you see.
The {Fore.LIGHTRED_EX}{self.name}{Fore.RESET} is dead.
You have made it this far
You are a worthy warrior.

Is this the end?
Have you really finished the game?

You still do not know the answers to all the questions that cloud your mind

Your journey is far from over...
		"""


class Challenger(Enemy):
	"""This is teh challenger class. The challenger is human enemy that converses and fights with the player"""
	def __init__(self):
		super().__init__()
		self.name = "Exiled Villager"
		self.hp = 90
		self.type = "human"
		self.score = 10
		self.reward = random.randint(35, 45)

		def generate_inventory():
			"""This function generates the challengers inventory"""
			all_weapons = [w for w in items.inventory if isinstance(w, items.Weapon)]
			random.shuffle(all_weapons)
			all_defensive = [d for d in items.inventory if isinstance(d, items.Defencive)]
			random.shuffle(all_defensive)
			all_consumables = [c for c in items.inventory if isinstance(c, items.Consumable)]
			random.shuffle(all_consumables)

			try:
				all_weapons.remove(items.Excalibur())
				all_weapons.remove(items.BattleAxe())
				all_weapons.remove(items.WoodenClub())
				all_weapons.remove(items.BluntSpear())

				all_defensive.remove(items.ReinforcedMetalArmour())
				all_defensive.remove(items.MetalArmour())
			except ValueError:
				pass

			weapons = random.sample(all_weapons, 1)
			defensive = random.sample(all_defensive, 1)
			consumables = random.sample(all_consumables, 1)

			inventory = weapons + defensive + consumables
			return inventory

		self.inventory: list = generate_inventory()
		self.damage = self.most_powerful_weapon().damage
		self.defence = self.most_defence().defence

	def alive_text(self):
		return f"""
I am The {Fore.RED}{self.name}{Fore.RESET}. Nothing that you do can stop me.\n
"""

	def dead_text(self):
		return f"""
How can it be. 
Me, The {Fore.RED}{self.name}{Fore.RESET}.
How could I be defeated by the likes of you. 
I must get my revenge.
One day you shall pay for what you have done to me.\n
"""

	def most_powerful_weapon(self):
		"""This function returns the weapon in the challenger's inventory that has the most damage"""
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
		"""This function returns the item in the challenger's inventory with the most defence """
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

	def heal(self):
		"""This function heals the challenger"""
		consumables = [item for item in self.inventory if isinstance(item, items.Consumable)]
		if not consumables:
			return

		try:
			if self.hp < 50:
				to_eat = consumables[0]
				self.hp = round(min(100, self.hp + to_eat.healing_value), 0)
				consumables.remove(to_eat)
				self.inventory.remove(to_eat)
				print(f"\nThe {self.name} has used {Fore.GREEN}'{to_eat.name}'")
		except IndexError:
			return
