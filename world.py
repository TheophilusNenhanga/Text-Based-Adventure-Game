"""This script will have the world class. It deals with the world map, its dynamics and how it can be interacted with"""
import random
import enemies
import npc
import items


class MapTile:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def intro_text(self):
		raise NotImplementedError("Create a subclass instead")

	def modify_player(self, player):
		pass


class StartTile(MapTile):
	def intro_text(self):
		return """
                    This is where your journey begins!
                    Will you be the one to save humanity?
                    Will you get the answers which you seek?
        """


class BoringTile(MapTile):
	def intro_text(self):
		return """
                Nothing much happens here.
                You must continue onwards.
        """

	def modify_player(self, player):
		player.score += 1


class CorridorTile(MapTile):
	def intro_text(self):
		return """
				This seems to be a corridor. 
				I wonder where it leads. 
		"""

	def modify_player(self, player):
		player.score += 1


class VictoryTile(MapTile):
	def modify_player(self, player):
		player.victory = True
		player.score += 25

	def intro_text(self):
		return """
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

	def modify_player(self, player):
		player.score += 5

		if not self.gold_claimed:
			self.gold_claimed = True
			player.gold = player.gold + self.gold
			print(f"+{self.gold} gold added")

	def intro_text(self):
		if self.gold_claimed:
			return """
            Another unremarkable part of the cave.
            You must forge onwards. 
            """
		else:
			return """
                                    Someone dropped some gold.
            You glance to your left and your right to make sure you are not being watched.
                                    Then you sneakily pick up the gold
            """


class FindCrystalTile(MapTile):
	def __init__(self, x, y):
		super().__init__(x, y)
		self.crystals = random.randint(5, 15)
		self.crystal_claimed = False

	def modify_player(self, player):
		player.score += 5

		if not self.crystal_claimed:
			self.crystal_claimed = True
			player.crystals = player.crystals + self.crystals
			print(f"+{self.crystals} crystals added")

	def intro_text(self):
		if self.crystal_claimed:
			return """
					You have been here before,
				There is nothing new to see here.
			"""
		else:
			return """
				You see something glowing in the distance
					Could it be? A crystal?
				I wonder what you could use that for.
			"""


class EnemyTile(MapTile):
	def __init__(self, x, y):
		r = random.random()
		if r < 0.2:
			self.enemy = enemies.BatSwarm()
			self.alive_text = """
                A colony of bats fly right above your head.
                Each looking more blood thirsty than the last.\n
                """
			self.dead_text = """
                                    You have done it.
                        The colony of bats didn't have a chance.\n
                        """
		elif r < 0.4:
			self.enemy = enemies.OvergrownInsect()
			self.alive_text = """
                        A giant centipede sets its eyes on you.
                            Will you make it out alive?\n
                            """
			self.dead_text = """
                                The centipede is dead.
                                You fought valiantly, 
                            Its corpse is now your trophy.\n
                            """
		elif r < 0.6:
			self.enemy = enemies.SkeletalWarrior()
			self.alive_text = """
                                The rattling of bones. 
                            The hastening of your death?\n
                            """
			self.dead_text = """
                            The skeletal warrior is dead.
                                Only its bones remain.\n
                                """
		elif r < 0.8:
			self.enemy = enemies.GiantSpider()
			self.alive_text = """
                        A giant spider crawls down from the wall.
                            It stands right in front of you, 
                            You are its prey.\n
                            """
			self.dead_text = """
                        The corpse of a dead spider lies before you.
                            Your victory is now certain.\n
                            """
		elif r < 0.99:
			self.enemy = enemies.Undead()
			self.alive_text = """
                        A dead explorer's corpse rises.
                    Will you join him in the dance of death?\n
                    """
			self.dead_text = """
                        Can a dead person die again?
                                Hmm, Maybe?\n
                                """

		else:
			self.enemy = enemies.Lamia()
			self.alive_text = """
                        A lamia stands before you.
                        Your luck has run out.
                        Is it time to say goodbye?\n
                        """
			self.dead_text = """
                                    You have escaped death. 
                                You won't be so lucky next time\n
                                """

		super().__init__(x, y)

	def intro_text(self):
		text = self.alive_text if self.enemy.is_alive() else self.dead_text
		return text

	def modify_player(self, player):
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


class GeoEnemy(MapTile):
	def __init__(self, x, y):
		r = random.random()
		if r < 0.33:
			self.enemy = enemies.Ogre()
			self.alive_text = """
            The ground begins to shake.
            A blood thirsty Ogre stands before you
            How long do you have to live?
                """
			self.dead_text = """
				The ground is still shaking.
					But, the Ogre is dead.
				You must be getting close. 
			"""
		elif r < 0.66:
			self.enemy = enemies.Golem()
			self.alive_text = """
							The ground begins to shake. 
								Could it be this hunky golem?
			"""
			self.dead_text = """
							The ground is still shaking.
								The golem is now just a pile of rocks.
							You must be getting close.
			"""
		else:
			self.enemy = enemies.Gargoyle()
			self.alive_text = """
							The ground begins to shake.
								The gargoyle sheds its stony surface. 
								It is ready to attack.
			"""
			self.dead_text = """
							The ground is still shaking.
								Even its stony skin wouldn't have made a difference
							You must be getting close.
			"""

		super().__init__(x, y)

	def intro_text(self):
		text = self.alive_text if self.enemy.is_alive() else self.dead_text
		return text

	def modify_player(self, player):
		if self.enemy.is_alive():
			try:
				defence_multiplier = 0.1 * player.most_defence().defence
				damage_dealt = self.enemy.damage - self.enemy.damage * defence_multiplier
				player.hp = player.hp - damage_dealt
				print(f"Enemy does {damage_dealt} damage. You have {round(player.hp, 0)} HP remaining")
			except AttributeError:
				player.hp = player.hp - self.enemy.damage
				print(f"Enemy does {self.enemy.damage} damage. You have {round(player.hp, 0)} HP remaining")


class HydroEnemy(MapTile):
	def __init__(self, x, y):
		r = random.random()
		if r < 0.33:
			self.enemy = enemies.Hydra()
			self.alive_text = """
							You begin to hear crashing waves.
								A hydra stands before you. 
								All of its eyes looking straight at you.
								"""
			self.dead_text = """
							The sound of crashing waves intensifies
								The Hydra is dead and,
								You have 3 heads to prove it.
							You must be getting close. 
			"""
		elif r < 0.66:
			self.enemy = enemies.WaterNymph()
			self.alive_text = """
							You begin to hear crashing waves.
								You have disturbed the waters of a water nymph.
								You have incurred her wrath.
							"""
			self.dead_text = """
							The sound of crashing waves intensifies.
								She did not stand a chance.
							You must be getting close.
			"""
		else:
			self.enemy = enemies.SeaSerpent()
			self.alive_text = """
								You begin to hear crashing waves.
									A Sea serpent, 
									Have you just slithered into your death?
							"""
			self.dead_text = """
							The sound of crashing waves intensifies.
								Next time you might not be that lucky.
							You must be getting close.
			"""

		super().__init__(x, y)

	def intro_text(self):
		text = self.alive_text if self.enemy.is_alive() else self.dead_text
		return text

	def modify_player(self, player):
		if self.enemy.is_alive():
			try:
				defence_multiplier = 0.1 * player.most_defence().defence
				damage_dealt = self.enemy.damage - self.enemy.damage * defence_multiplier
				player.hp = player.hp - damage_dealt
				print(f"Enemy does {damage_dealt} damage. You have {round(player.hp, 0)} HP remaining")
			except AttributeError:
				player.hp = player.hp - self.enemy.damage
				print(f"Enemy does {self.enemy.damage} damage. You have {round(player.hp, 0)} HP remaining")


class PyroEnemy(MapTile):
	def __init__(self, x, y):
		r = random.random()
		if r < 0.33:
			self.enemy = enemies.HellHound()
			self.alive_text = """
							It's getting hotter by the second.
								A hell hound of incredible size is before you
								Has  your luck run out?
								"""
			self.dead_text = """
							The ground below you is now magma.
								You turned that hell hound into a puppy.

							You must be getting close. 

			"""
		elif r < 0.66:
			self.enemy = enemies.BabyPhoenix()
			self.alive_text = """
							It's getting hotter by the second.
								A phoenix flaps its fiery wings
								Will you burned along with everything else?
							"""
			self.dead_text = """
							The ground below you is now magma.
								You have extinguished the fiery phoenix

							You must be getting close.

			"""
		else:
			self.enemy = enemies.Salamander()
			self.alive_text = """
								It is getting hotter by the second
									A salamander stands before you.
									A giant fiery lizard.
									Will you be charred? 
							"""
			self.dead_text = """
							The ground below you is magma.
								It seems nothing can stop you

							You must be getting close

			"""

		super().__init__(x, y)

	def intro_text(self):
		text = self.alive_text if self.enemy.is_alive() else self.dead_text
		return text

	def modify_player(self, player):
		if self.enemy.is_alive():
			try:
				defence_multiplier = 0.1 * player.most_defence().defence
				damage_dealt = self.enemy.damage - self.enemy.damage * defence_multiplier
				player.hp = player.hp - damage_dealt
				print(f"Enemy does {damage_dealt} damage. You have {round(player.hp, 0)} HP remaining")
			except AttributeError:
				player.hp = player.hp - self.enemy.damage
				print(f"Enemy does {self.enemy.damage} damage. You have {round(player.hp, 0)} HP remaining")


class AeroEnemy(MapTile):
	def __init__(self, x, y):
		r = random.random()
		if r < 0.33:
			self.enemy = enemies.Harpy()
			self.alive_text = """
							The air seems to be getting thinner.
								Yor mere presence has angered a harpy.
								You shall face death by its talons
								"""
			self.dead_text = """
							You can barely breathe now.
								The harpy has fallen. 
								You have clipped its once might wings

							You must be getting close. 

			"""
		elif r < 0.66:
			self.enemy = enemies.ThunderBird()
			self.alive_text = """
							The air seems to be getting thinner.
								Will you survive its lightning?
							"""
			self.dead_text = """
							You can barely breathe now
								The thunderbird is dead. 
								Hmm, how much do those feathers cost?

							You must be getting close.

			"""
		else:
			self.enemy = enemies.Manticore()
			self.alive_text = """
								The air is getting thinner.
									A winged manticore stands before you.
									It is unconquerable.
							"""
			self.dead_text = """
							You can barely breathe now.
								You have conquered the unconquerable
								Could you save humanity?

							You must be getting close

			"""

		super().__init__(x, y)

	def intro_text(self):
		text = self.alive_text if self.enemy.is_alive() else self.dead_text
		return text

	def modify_player(self, player):
		if self.enemy.is_alive():
			try:
				defence_multiplier = 0.1 * player.most_defence().defence
				damage_dealt = self.enemy.damage - self.enemy.damage * defence_multiplier
				player.hp = player.hp - damage_dealt
				print(f"Enemy does {damage_dealt} damage. You have {round(player.hp, 0)} HP remaining")
			except AttributeError:
				player.hp = player.hp - self.enemy.damage
				print(f"Enemy does {self.enemy.damage} damage. You have {round(player.hp, 0)} HP remaining")


class GeoBoss(MapTile):
	def __init__(self, x, y):
		self.enemy = enemies.Geomancer()
		self.alive_text = """
						The ground is now shaking violently.
						The rocks in front of you begin to move.
						Spikes made of rock begin to grow out of the roof of the cave.
						You are in its presence;
						The GEOMANCER!

		"""
		self.dead_text = """
						The ground stops shaking. 
						Everything is silent. 
						The rocks before you begin to disintegrate.
						The GEOMANCER is dead.

						All that is left is a scroll?
						What could this mean?

						The ground begins to crumble.
						Before you fall into the darkness you grab the scroll

						...It might come in handy

		"""
		super().__init__(x, y)

	def intro_text(self):
		text = self.alive_text if self.enemy.is_alive() else self.dead_text
		return text

	def modify_player(self, player):
		if self.enemy.is_alive():
			try:
				defence_multiplier = 0.1 * player.most_defence().defence
				damage_dealt = self.enemy.damage - self.enemy.damage * defence_multiplier
				player.hp = player.hp - damage_dealt
				print(f"The Geomancer does {damage_dealt} damage. You have {round(player.hp, 0)} HP remaining")
			except AttributeError:
				player.hp = player.hp - self.enemy.damage
				print(f"The Geomancer does {self.enemy.damage} damage. You have {round(player.hp, 0)} HP remaining")


class HydroBoss(MapTile):
	def __init__(self, x, y):
		self.enemy = enemies.Hydromancer()
		self.alive_text = """
						The crashing waves are are more violent than ever.
						The water level is rising. 
						The terrace you are standing on is not enough. 
						The waves are raging. 
						As if a hurricane is about to erupt within the cave.
						The HYDROMANCER is before you 
		"""
		self.dead_text = """
						The waves retreat.
						The violent storm comes to an end. 
						A soft mist begins to fall. 
						The HYDROMANCER is dead,
						You are victorious.

						All that is left is a scroll?
						What could this mean?

						Now you an continue on your path. 
						Where will you go next?
		"""
		super().__init__(x, y)

	def intro_text(self):
		text = self.alive_text if self.enemy.is_alive() else self.dead_text
		return text

	def modify_player(self, player):
		if self.enemy.is_alive():
			try:
				defence_multiplier = 0.1 * player.most_defence().defence
				damage_dealt = self.enemy.damage - self.enemy.damage * defence_multiplier
				player.hp = player.hp - damage_dealt
				print(f"The Hyrdomancer does {damage_dealt} damage. You have {round(player.hp, 0)} HP remaining")
			except AttributeError:
				player.hp = player.hp - self.enemy.damage
				print(f"The Hydromancer does {self.enemy.damage} damage. You have {round(player.hp, 0)} HP remaining")


class PyroBoss(MapTile):
	def __init__(self, x, y):
		self.enemy = enemies.Pyromancer()
		self.alive_text = """
						The ground below you is now beginning to bubble. 
						The heat is more than you can bear. 
						The sweat falling from your face evaporates before it hits the ground
						The PYROMANCER must be close by, 
						and your death?

		"""
		self.dead_text = """
						The temperature suddenly drops.
						The magma cools. 
						You have done it. 
						The great PYROMANCER has fallen by your hands

						All that is left is a scroll?
						What could this mean?

						Now you an continue on your path. 
						Where will you go next?

		"""
		super().__init__(x, y)

	def intro_text(self):
		text = self.alive_text if self.enemy.is_alive() else self.dead_text
		return text

	def modify_player(self, player):
		if self.enemy.is_alive():
			try:
				defence_multiplier = 0.1 * player.most_defence().defence
				damage_dealt = self.enemy.damage - self.enemy.damage * defence_multiplier
				player.hp = player.hp - damage_dealt
				print(f"The Pyromancer does {damage_dealt} damage. You have {round(player.hp, 0)} HP remaining")
			except AttributeError:
				player.hp = player.hp - self.enemy.damage
				print(f"The Pyromancer does {self.enemy.damage} damage. You have {round(player.hp, 0)} HP remaining")


class AeroBoss(MapTile):
	def __init__(self, x, y):
		self.enemy = enemies.Aeromancer()
		self.alive_text = """
						You can barely breathe now. 
						Will you did for suffocation before the fight begins
						Have you come this far just to die?
						Will the AEROMANCER be your end?

		"""
		self.dead_text = """
						A lifeless figure is all you see.
						The AEROMANCER is dead.
						You have made it this far
						You are a worthy warrior.

						All that is left is a scroll?
						What could this mean?

						Is this the end?
						Have you really finished the game?
						Wait, but where is Almus?
					You still do not know the answers to all the questions that cloud your mind

						Your journey is far from over.
		"""
		super().__init__(x, y)

	def intro_text(self):
		text = self.alive_text if self.enemy.is_alive() else self.dead_text
		return text

	def modify_player(self, player):
		if self.enemy.is_alive():
			try:
				defence_multiplier = 0.1 * player.most_defence().defence
				damage_dealt = self.enemy.damage - self.enemy.damage * defence_multiplier
				player.hp = player.hp - damage_dealt
				print(f"The Aeromancer does {damage_dealt} damage. You have {round(player.hp, 0)} HP remaining")
			except AttributeError:
				player.hp = player.hp - self.enemy.damage
				print(f"The Aeromancer does {self.enemy.damage} damage. You have {round(player.hp, 0)} HP remaining")


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
		print("Trade Complete\n")

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

# The enchanter will be implemented the same way as the trader


class EnchanterTile(MapTile):
	def __init__(self, x, y):
		super().__init__(x, y)
		self.enchanter = npc.Enchanter()

	def intro_text(self):
		return """
			An old wizard with a long white beard, looks into your eyes. 
					He seems to hold the power of magic.

			(Please note that you can only have one enchantment per item.)
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
					print("Invalid Choice\n")

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
		print("Enchantment Complete")

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
				print("Invalid Choice\n")


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
					You see a {self.quest_lady.name}.
				She seems to be plotting something devious.
					Will you be her helping hand?
			"""

	def talk(self, player):
		if not self.completed:
			print("Will you help the old lady?")
			choice1 = input("(Y)es or (N)o")
			if choice1 not in ["yes", "YES", "y", "Y"]:
				return

			print(
				"""
				  You have made a wise decision
			You must seek out a mysterious magical item
			"""
				)

			print(f"""
				Have you found the {items.MagicalItem().name}?
				""")

			choice2 = input("(Y)es or (N)o")
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
			return """
				You have not found the item yet.
			"""

	@staticmethod
	def quest_completed(self, player, item):
		self.encounter += 1
		if self.completed:
			print(f"You have found and retrieved the {items.MagicalItem().name}")
			player.gold += self.quest_lady.gold
			print(f"You have received {self.quest_lady.gold} gold")
			player.crystals += self.quest_lady.crystals
			print(f"You have received {self.quest_lady.crystals} crystals")
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
			return """
						There is nothing to see here.
				It seems you have already claimed the magical item.
						  You must forge onwards.
			"""
		else:
			return f"""
						You see a soft glow. 
				You have found it. The {self.item.name}
			Now you can return to the suspicious old woman.
			"""

	def modify_player(self, player):
		player.score += 5

		if not self.item_claimed:
			self.item_claimed = True
			item = self.item
			player.inventory.append(item)
			print(f"You have found the {item.name}\n")


# ST start Tile
# VT Victory Tile

# FG Find Gold
# FC Find Crystals
# FI Find Quest Item Tile

# EN Enemy Tile
# AE Aero Enemy
# HE Hydro Enemy
# PE Pyro enemy
# GE Geo Enemy

# ET Enchanter Tile
# TT Trader Tile
# QT Quest Tile

# BT Boring Tile
# Corridor Tile


world_dsl = """
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |ST |EN |EN |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |FG |BT |BT |BT |   |FG |EN |BT |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |TT |   |BT |   |   |FQI|EN |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |EN |BT |   |BT |EN |BT |BT |BT |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |BT |   |QT |BT |   |   |BT |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |BT |EN |BT |EN |BT |BT |BT |   |   |   |   |   |   |   |   |   |   |   |   |ET |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |ET |BT |FC |   |BT |TT |   |EN |   |   |   |   |   |   |   |   |   |   |   |BT |BT |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |BT |EN |BT |BT |EN |EN |BT |EN |   |   |   |   |   |   |   |   |   |   |BT |TT |BT |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |BT |   |   |BT |   |BT |   |FC |   |   |   |   |   |   |   |   |   |BT |BT |   |BT |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |BT |EN |BT |BT |BT |BT |   |   |   |   |   |   |   |   |   |   |EN |BT |   |   |BT |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |BT |   |   |   |   |   |   |   |   |   |   |   |BT |BT |   |   |   |BT |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |FG |BT |FC |   |   |   |   |   |   |   |   |   |EN |BT |EN |EN |BT |   |EN |BT |BT |EN |   |   |
|   |   |FC |EN |BT |FG |BT |EN |BT |EN |FC |   |   |TT |GE |GE |GE |ET |   |   |   |   |   |   |   |BT |BT |   |   |   |BT |EN |BT |   |   |AE |   |   |
|   |   |   |   |   |BT |BT |   |   |   |   |   |   |   |   |GE |   |   |   |   |   |   |   |   |FG |BT |   |   |   |   |BT |   |BT |   |AE |AE |   |   |
|   |   |   |   |   |EN |BT |   |   |   |   |   |   |QT |   |GB |   |   |   |   |   |   |   |   |EN |   |   |   |   |   |FQI|   |BT |AE |AE |AB |BT |VT |
|   |   |   |HE |HE |   |EN |ET |BT |EN |BT |   |BT |EN |   |BT |   |   |   |   |   |   |   |   |FC |BT |   |   |   |   |BT |   |BT |   |AE |AE |   |   |
|BT |BT |HB |HE |HE |BT |BT |   |   |   |FC |BT |EN |EN |BT |BT |   |   |   |   |   |   |   |   |   |BT |BT |   |   |   |BT |   |BT |   |   |AE |   |   |
|CT |   |BT |HE |HE |   |BT |EN |FG |   |EN |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |EN |BT |   |   |BT |   |BT |   |   |EN |   |   |
|CT |   |BT |BT |FQI|EN |EN |   |BT |   |BT |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |BT |BT |BT |EN |EN |BT |BT |EN |BT |   |   |
|CT |   |   |BT |   |   |   |   |TT |EN |BT |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |EN |BT |   |   |   |   |   |   |   |   |
|CT |   |   |BT |BT |EN |EN |BT |BT |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |BT |BT |QT |BT |   |   |   |   |   |
|CT |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |BT |EN |   |   |   |   |   |
|CT |   |TT |FC |   |   |   |BT |EN |EN |BT |BT |BT |EN |EN |TT |   |   |BT |   |   |   |   |   |   |   |   |   |   |   |   |   |EN |   |   |   |   |   |
|CT |   |EN |   |EN |QT |   |BT |   |BT |   |   |   |   |   |BT |EN |   |PE |PE |   |   |   |   |   |   |BT |BT |FC |FG |BT |   |BT |   |   |   |   |   |
|BT |BT |BT |BT |EN |BT |BT |EN |   |BT |EN |FG |BT |BT |EN |ET |EN |PE |BT |BT |PE |PB |CT |CT |CT |CT |BT |BT |FC |FG |BT |BT |BT |   |   |   |   |   |
|   |   |FG |   |EN |   |EN |   |   |BT |   |   |BT |   |   |BT |EN |   |PE |PE |   |   |   |   |   |   |BT |BT |ET |TT |BT |   |   |   |   |   |   |   |
|   |   |ET |EN |   |BT |FQI|FG |EN |BT |   |   |BT |EN |FC |TT |   |   |BT |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
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
				"EN ": EnemyTile,
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
