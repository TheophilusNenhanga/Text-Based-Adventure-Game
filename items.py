"""This script will have the items class that will will have all items that will be available in the game"""
import random
import colorama
from colorama import Fore


colorama.init(autoreset=True)


class Weapon:
	"""Base class for all items that are used for attacking purposes."""
	def __init__(self):

		self.name = "Weapon"
		self.description = "Used for attacking"
		self.damage = 0
		self.enchantment = None
		self.defence = 0
		self.value = 0

	def __str__(self):
		return f"{self.name}, (Damage:{self.damage})"


class Hand(Weapon):
	def __init__(self):
		super().__init__()
		self.name = "Bare hands"
		self.description = "if all else fails"
		self.value = 9999
		self.damage = 1
		self.sellable = False


class Rock(Weapon):
	def __init__(self):
		super().__init__()
		self.name = "Rock"
		self.description = "A fist sized rock, perfect for bludgeoning"
		self.damage = 1
		self.value = 5
		self.enchantment = None
		self.sellable = True
		self.attacks = {
			1: ("Rock Throw", 0.1, 25),
			2: ("Rock Sling", 0.3, 15),
			3: ("Rock Pummel", 0.5, 10)
		}


class Dagger(Weapon):
	def __init__(self):
		super().__init__()
		self.name = "Rock"
		self.description = """
        A small dagger.
        Somewhat more dangerous than a rock.
        """
		self.damage = 3
		self.value = 20
		self.enchantment = None
		self.sellable = True
		self.attacks = {
			1: ("Stab", 0.1, 15),
			2: ("Dagger Throw", 0.3, 15),
			3: ("Dagger Slicer", 0.5, 10)
		}


class RustySword(Weapon):
	def __init__(self):
		super().__init__()
		self.name = "Rusty Sword"
		self.description = """
        A small sword with some rust.
        It has definitely seen better days. 
        """
		self.damage = 8
		self.value = 35
		self.enchantment = None
		self.sellable = True
		self.attacks = {
			1: ("Sword Slash", 0.1, 15),
			2: ("Counter Attack", 0.3, 10),
			3: ("Passata Sotto", 0.5, 5)
		}


class ShinySword(Weapon):
	def __init__(self):
		super().__init__()
		self.name = "Shiny Sword"
		self.description = """
        This one has some shine to it.
        And it packs a real punch.
        """
		self.damage = 14
		self.value = 70
		self.enchantment = None
		self.sellable = True
		self.attacks = {
			1: ("Sword Slash", 0.1, 15),
			2: ("Counter Attack", 0.3, 10),
			3: ("Passata Sotto", 0.5, 5)
		}


class LightSaber(Weapon):
	def __init__(self):
		super().__init__()
		self.name = "Light Saber"
		self.description = """
        This one is light. 
        Agile and Sharp.
        """
		self.damage = 18
		self.value = 85
		self.enchantment = None
		self.sellable = True
		self.attacks = {
			1: ("Saber Swipe", 0.1, 15),
			2: ("Counter Attack", 0.3, 10),
			3: ("Double Slash", 0.5, 5)
		}


class HeavySaber(Weapon):
	def __init__(self):
		super().__init__()
		self.name = "Heavy Saber"
		self.description = """
        Much heavier. 
        Much more damage.
        """
		self.damage = 24
		self.value = 105
		self.enchantment = None
		self.sellable = True
		self.attacks = {
			1: ("Saber Swipe", 0.1, 15),
			2: ("Counter Attack", 0.3, 10),
			3: ("Double Slash", 0.5, 5)
		}


class BattleAxe(Weapon):
	def __init__(self):
		super().__init__()
		self.name = "Battle Axe"
		self.description = """
        You can't battle without it.
        You can't lose with it.
        """
		self.damage = 28
		self.value = 125
		self.enchantment = None
		self.sellable = True
		self.attacks = {
			1: ("Basic Chop", 0.1, 15),
			2: ("Swift Chop", 0.3, 10),
			3: ("Axe Cleave", 0.5, 5)
		}


class Mace(Weapon):
	def __init__(self):
		super().__init__()
		self.name = "Mace"
		self.description = """
        Don't get too close.
        It hurts.
        """
		self.damage = 28
		self.value = 120
		self.enchantment = None
		self.sellable = True
		self.attacks = {
			1: ("Mace Hit", 0.1, 15),
			2: ("Mace Hammer", 0.3, 10),
			3: ("Triple Mace Bash", 0.5, 5)
		}


class SharpenedShield(Weapon):
	def __init__(self):
		super().__init__()
		self.name = "Sharpened Shield"
		self.description = """
        It may just be a shield,
        But i would still keep my distance.
        """
		self.damage = 10
		self.defence = 2
		self.value = 80
		self.enchantment = None
		self.sellable = True
		self.attacks = {
			1: ("Shield Slash", 2, 15),
			2: ("Quick Attack", 4, 10),
			3: ("Shield Bash", 6, 5)
		}


class BowAndArrow(Weapon):
	def __init__(self):
		super().__init__()
		self.name = "Bow and Arrow"
		self.description = """
        What is stronger
        The bow or the arrow?
        """
		self.damage = 12
		self.value = 55
		self.enchantment = None
		self.sellable = True
		self.attacks = {
			1: ("Bow Swipe", 0.1, 15),
			2: ("Multi Arrow Shot", 0.3, 10),
			3: ("Piercing Arrow Snipe", 0.5, 5)
		}


class WoodenClub(Weapon):
	def __init__(self):
		super().__init__()
		self.name = "Wooden Club"
		self.description = """
        I hope you're embarrassed.
        You couldn't even hurt a fly.
        """
		self.damage = 4
		self.value = 15
		self.enchantment = None
		self.sellable = True
		self.attacks = {
			1: ("Club Hit", 0.1, 15),
			2: ("Club Pound", 0.3, 10),
			3: ("Triple Club Hammer", 0.5, 5)
		}


class MetalClub(Weapon):
	def __init__(self):
		super().__init__()
		self.name = "Metal Club"
		self.description = """
        Now this can put up a fight.
        Enemies beware!
        """
		self.damage = 9
		self.value = 50
		self.enchantment = None
		self.sellable = True
		self.attacks = {
			1: ("Club Hit", 0.1, 15),
			2: ("Club Pound", 0.3, 10),
			3: ("Triple Club Hammer", 0.5, 5)
		}


class Pike(Weapon):
	def __init__(self):
		super().__init__()
		self.name = "Pike"
		self.description = """
	        	  Poke, Poke, Pike!
	        And all the enemies take a hike.
	        """
		self.damage = 16
		self.value = 80
		self.enchantment = None
		self.sellable = True
		self.attacks = {
			1: ("Sword Slash", 0.1, 15),
			2: ("Counter Attack", 0.3, 10),
			3: ("Poke Poke Stab", 0.5, 5)
		}


class BluntSpear(Weapon):
	def __init__(self):
		super().__init__()
		self.name = "Blunt Spear"
		self.description = """
	        		It's a spear.
	        But, It'll probably let you down
	        """
		self.damage = 6
		self.value = 28
		self.enchantment = None
		self.sellable = True
		self.attacks = {
			1: ("Poke", 0.1, 15),
			2: ("Spear Toss", 0.3, 10),
			3: ("Double stab", 0.5, 5)
		}


class SharpSpear(Weapon):
	def __init__(self):
		super().__init__()
		self.name = "Sharp Spear"
		self.description = """
	        		It's a spear.
	        This one won't let you down.
	        """
		self.damage = 12
		self.value = 55
		self.enchantment = None
		self.sellable = True
		self.attacks = {
			1: ("Poke", 0.1, 15),
			2: ("Spear Toss", 0.3, 10),
			3: ("Double stab", 0.5, 5)
		}


class Excalibur(Weapon):
	def __init__(self):
		super().__init__()
		self.name = "Excalibur"
		self.description = """
				A legendary sword.
			Forged long ago outside the cave. 
		It cannot rest until more blood is shed. 
		"""
		self.damage = 35
		self.value = 300
		self.enchantment = None
		self.sellable = True
		self.attacks = {
			1: ("Sword Slash", 0.1, 15),
			2: ("Counter Attack", 0.3, 10),
			3: ("Passata Sotto", 0.5, 5)
		}


class Consumable:
	"""Base class for all items used to restore health"""
	def __init__(self):
		self.value = 1
		self.name = ""
		self.healing_value = 1
		self.sellable = True

	def __str__(self):
		return f"{self.name} {Fore.GREEN}+{self.healing_value} HP{Fore.RESET}"


class SnakeApple(Consumable):
	def __init__(self):
		super().__init__()
		self.name = "Snake Apple"
		self.healing_value = -10
		self.value = 15

	def __str__(self):
		return f"{self.name} {Fore.LIGHTRED_EX}{self.healing_value} HP{Fore.RESET}"


class RottenFlesh(Consumable):
	def __init__(self):
		super().__init__()
		self.name = "Rotten Flesh"
		self.healing_value = 5
		self.value = 10


class CrustyBread(Consumable):
	def __init__(self):
		super().__init__()
		self.name = "Crusty Bread"
		self.healing_value = 10
		self.value = 20


class Apple(Consumable):
	def __init__(self):
		super().__init__()
		self.name = "Apple"
		self.healing_value = 15
		self.value = 25


class FreshBread(Consumable):
	def __init__(self):
		super().__init__()
		self.name = "Fresh Bread"
		self.healing_value = 25
		self.value = 50


class CookedInsectFlesh(Consumable):
	def __init__(self):
		super().__init__()
		self.name = "Cooked Insect Flesh"
		self.healing_value = 30
		self.value = 45


class HealingPotion(Consumable):
	def __init__(self):
		super().__init__()
		self.name = "Healing Potion"
		self.healing_value = 25
		self.value = 40


class LuckyFruit(Consumable):
	def __init__(self):
		super().__init__()
		self.name = "Lucky Fruit?"
		self.healing_value = random.randint(20, 40)
		self.value = random.randint(30, 60)


class StrongHealingPotion(Consumable):
	def __init__(self):
		super().__init__()
		self.name = "Strong Healing Potion"
		self.healing_value = 55
		self.value = 85


class HyperHealingPotion(Consumable):
	def __init__(self):
		super().__init__()
		self.name = "Hyper Healing Potion"
		self.healing_value = 75
		self.value = 115


class Defencive:
	"""Base class for all items used to mitigate damage"""
	def __init__(self):
		self.value = 1
		self.name = ""
		self.defence = 0.1
		self.sellable = True

	def __str__(self):
		return f"{self.name}, Defence: ({self.defence})"


class WoodenShield(Defencive):
	def __init__(self):
		super().__init__()
		self.name = "Wooden Shield"
		self.description = """
        You might just be better off without it
        """
		self.defence = 1
		self.value = 10


class DefenciveClothing(Defencive):
	def __init__(self):
		super().__init__()
		self.name = "Tough clothes"
		self.description = """
        Well you have to wear something
        """
		self.defence = 2
		self.value = 45


class MetalShield(Defencive):
	def __init__(self):
		super().__init__()
		self.name = "Metal Shield"
		self.description = """
        This might just come in handy
        """
		self.defence = 2.5
		self.value = 20


class ChainMail(Defencive):
	def __init__(self):
		super().__init__()
		self.name = "Chain mail"
		self.description = """
        It's just chain mail
        Don't get your hopes up
        """
		self.defence = 3
		self.value = 60


class MetalArmour(Defencive):
	def __init__(self):
		super().__init__()
		self.name = "Metal Armour"
		self.description = """
        You can enter battle happily
        Nothing can get through this
        """
		self.defence = 4
		self.value = 75


class ReinforcedMetalArmour(Defencive):
	def __init__(self):
		super().__init__()
		self.name = "Reinforced Metal Armour"
		self.description = """
        Nothing gets past this
        """
		self.defence = 5
		self.value = 90


class Quests:
	"""Base class for all quest relayed items."""
	def __init__(self):
		self.name = "Quest item"
		self.description = "A item used for quests"
		self.sellable = False

	def __str__(self):
		return self.name


class MagicalItem(Quests):
	"""Item needed to complete a quest"""
	def __init__(self):
		super().__init__()
		self.name = "Magical item"
		self.value = 1
		self.description = "A magical item, with an unknown magical use"


class Extras:
	"""Base class of extra items that are concepts from the game's continuation"""
	def __init__(self):
		self.name = "Extras"
		self.value = 0 
		self.sellable = False
		self.description = "An extra item that does not affect the game"

	def __str__(self):
		return f"{Fore.LIGHTYELLOW_EX}{self.name}{Fore.RESET}"


class Cash(Extras):
	"""Extra item from third story teller"""
	def __init__(self):
		super().__init__()
		self.name = "Cash"
		self.value = 10
		self.description = "The currency used in the outside world"


class MechaDagger(Extras, Weapon):
	"""Extra item from third story teller"""
	def __init__(self):
		super().__init__()
		self.name = "Mecha Dagger"
		self.value = 300
		self.damage = 18
		self.sellable = False
		self.description = "A simple dagger that has been upgraded with the power of technology"


class Progression:
	"""The base class for all items that are necessary to complete the game."""
	def __init__(self):
		self.name = "Progression"
		self.value = 9999
		self.sellable = False
		self.description = "These items are used for game progression."
	
	def __str__(self):
		return self.name


class GeoStone(Progression):
	"""The stone from the first level"""
	def __init__(self):
		super().__init__()
		self.name = "Geo Stone"


class HydroStone(Progression):
	"""Stone from the second level"""
	def __init__(self):
		super().__init__()
		self.name = "HydroStone"


class PyroStone(Progression):
	"""Stone from the third level"""
	def __init__(self):
		super().__init__()
		self.name = "PyroStone"


class AeroStone(Progression):
	"""Stone from the fourth level"""
	def __init__(self):
		super().__init__()
		self.name = "AeroStone"


inventory: list = [
		SnakeApple(), RottenFlesh(), CrustyBread(), Apple(), FreshBread(),
		CookedInsectFlesh(), HealingPotion(), LuckyFruit(), StrongHealingPotion(),
		HyperHealingPotion(), WoodenShield(), DefenciveClothing(), MetalShield(),
		ChainMail(), MetalArmour(), ReinforcedMetalArmour(), ShinySword(), LightSaber(),
		HeavySaber(), BattleAxe(), Mace(), SharpenedShield(), BowAndArrow(),
		WoodenClub(), MetalClub(), Pike(), BluntSpear(), SharpSpear(), Excalibur()
	]
