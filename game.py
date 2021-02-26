"""This script will have the game loop. will reference the other modules as it will not have its own classes"""
from player import Player
import world
from collections import OrderedDict
import time
from datetime import datetime
import traceback
import files
import os
import pickle
import colorama
from colorama import Fore, Style
import sys


colorama.init(autoreset=True)
directory = "caver"
parent_dir = os.getcwd()
paths = os.path.join(parent_dir, directory)


player_story = """
...CAVER...

The Story

The player has lived in a cave their whole life. The player lives in a small village in the cave.
The player may live in the cave, but it is clear that the player does not come from the cave.
Compared to the other people that live in the cave the player has more muscle and a more well-defined bone structure.
The player has been in the cave for as long as they can remember, but the people of the cave could remember more.
The player knows that they are different from the people of the cave but still treats them as their own.

Tales have been told. Tales of a bright yellow ball that floats far above.
Tales of a bright white ball that floats with many small white dots to accompany it.
Tales of a vast expanse of land that is not confined by the dark walls of a cave.
These are the tales that the character has grown up to. However, the player has never left the cave.
No one dares to try and leave the cave. There is only one way to leave the cave. It is treacherous and unforgiving.
It holds many vicious beasts. No one can make it through.

No one, except one man. An old man, who many in the village called senile. In the days of his prime, he left the cave 
and witnessed the outside world. He saw first hand what the outside world was like. He now can only tell the tales of 
technology that surpassed his comprehension and people who, to him looked like muscular giants. He is the only one 
who has seen the legendary yellow ball, the one called ‘sun’. The tales of the outside world where he was known as a 
Caver. 

Alas, the people of the cave are slowly dying. Their resources are dwindling. The old risk their lives every time 
they awake from their slumber. The old man is at the greatest risk. He is the oldest of all the people of the cave. 
He was the one to find the player and rescue him from death's door. Once upon a time. The player sees the old man as 
a father figure. The love he had for the old man was great 

The player has to save the people of the cave. The player has to save their friends. The player has to save the old man. 
Save his father. The player will now have to journey out of the cave. The player will encounter many dangers, 
but the player must survive or else. 

You are the player. You are a Caver.
Will you survive?
"""

run_once: int = 0
num: int = 0


def exit_screen():
	"""This functions generates the exit screen.
	This screen is only used once the player has died.
	Once any way of resetting the game is found. This function will no longer be used"""

	global num, run_once

	print("---------CAVER---------\n")
	print("Thank you for playing the game.")
	print(
		"""
1. Read The Player's Story
2. Leaderboard
3. Credits
4. Quit Game

Hope you enjoyed! 
		"""
	)

	while True:
		choice = input("\nWhat would you like to do \n")

		if choice in ["1.", "1", "one", "ONE"]:
			try:
				story = open(paths + "\\story.txt", "r")
				storyline = story.read()
				print(f"{Fore.LIGHTBLUE_EX}{storyline}{Fore.RESET}")

				# for line in story:
				# 	print(line)

				story.seek(0)
				story.close()

				exit_screen()

			except FileNotFoundError:
				print(player_story)

		elif choice in ["2.", "2", "two", "TWO"]:
			try:
				lead = pickle.load(open(paths + "\\leaders.dat", "rb"))
				for item in lead:
					if len(lead) == 1:
						print("-----There is no leaderboard.-----")
						print("Play the game to be the first on the leaderboard.")

						continue
					while run_once == 0:
						num = 0
						run_once = 1

					if num == 0:
						print(item)
						num += 1
					else:
						print(f"{num}. {item}")
						num += 1
				num = 0

			except FileNotFoundError:
				print("-----There is no leaderboard.-----")
				print("Play the game to be the first on the leaderboard.")

		elif choice in ["3.", "3", "three", "THREE"]:
			try:
				with open(paths + "\\credits.txt", "r") as credit:
					text = credit.read()
				print(text)
			except FileNotFoundError:
				print("Sorry the credits could not be loaded.")

		elif choice in ["4.", "4", "four", "FOUR"]:
			print("Are you sure you want to exit?\n(Y)es\n(N)o")
			choice2 = input()
			if choice2 in ["yes", "Y", "y", "YES", "Yes"]:
				print("Goodbye. We hope you enjoyed the game.")
				time.sleep(2.5)
				sys.exit()
			if choice2 in ["no", "N", "n", "NO", "No"]:
				exit_screen()
		else:
			print("Invalid Action\n")
			exit_screen()


def start_screen():
	"""This function generates the start screen that the player see when eer they start the game"""
	global num, run_once
	print("---------CAVER---------\n")
	print("Welcome to the game.")
	print(
		"""
1. Play Caver
2. Read The Player's Story
3. Leaderboard
4. Credits
5. Quit Game

If it is your first time playing the game.
We recommend that you read the player's story. 
This will give you a background of the game. 

Hope you enjoy! 
		"""
	)

	while True:
		choice = input("\nWhat would you like to do \n")
		if choice in ["1.", "1", "one", "ONE"]:
			try:
				play()
			except Exception as error:
				print("There was an error.")
				print(error)
				print("")
				print(traceback.format_exc())
				print("\n")

		elif choice in ["2.", "2", "two", "TWO"]:
			try:
				story = open(paths + "\\story.txt", "r")
				storyline = story.read()
				print(f"{Fore.LIGHTBLUE_EX}{storyline}{Fore.RESET}")

				# for line in story:
				# 	print(line)

				story.seek(0)
				story.close()
				start_screen()
			except FileNotFoundError:
				print(player_story)

		elif choice in ["3.", "3", "three", "THREE"]:
			try:
				lead = pickle.load(open(paths + "\\leaders.dat", "rb"))
				for item in lead:
					if len(lead) == 1:
						print("-----There is no leaderboard.-----")
						print("Play the game to be the first on the leaderboard")
						continue

					while run_once == 0:
						num = 0
						run_once = 1

					if num == 0:
						print(item)
						num += 1
					else:
						print(f"{num}. {item}")
						num += 1
					with open(paths + "\\leaderboard.txt", "a") as f:
						f.writelines(f"{num}. {item}")
				num = 0

			except FileNotFoundError:
				print("-----There is no leaderboard.-----")
				print("Play the game to be the first on the leaderboard")

		elif choice.lower() in ["4.", "4", "four"]:
			try:
				with open(paths + "\\credits.txt", "r") as credit:
					text = credit.read()
				print(text)
			except FileNotFoundError:
				print("Sorry the credits could not be loaded")

		elif choice.lower() in ["5.", "5", "five"]:
			print("Are you sure you want to exit?\n(Y)es\n(N)o")
			choice2 = input()
			if choice2 in ["yes", "Y", "y", "YES", "Yes"]:
				print("Goodbye. We hope you enjoyed the game")
				time.sleep(2.5)
				exit(1)
			if choice2 in ["no", "N", "n", "NO", "No"]:
				start_screen()

		else:
			print(f"{Style.BRIGHT}Invalid Action\n")
			start_screen()


def play():
	"""This function runs the game and constantly checks whether the game has been completed or if the player has died."""

	def end(player_arg):
		"""This function is called once the player has died or has won the game.
		It deals with the leaderboard and storing of data."""
		def finding_highest(string):
			"""This function is the key used to sort the leaderboard scores"""
			_leader = string.split()
			try:
				_leader = int(_leader[2])
			except (ValueError, TypeError):
				return
			return _leader

		valid = False
		name = "XXX"
		while not valid:
			name = input("Please enter your initials\n")
			if len(name) < 5 and name.isalpha() and " " not in name:
				valid = True

		print(f"Your score was: {player_arg.score}")
		# lead = open(files.path+"\\leaderboard.txt", "ab")
		new_leader = f"{name} --------- {player_arg.score} --------- {datetime.today().date()}"

		leader_list = list()
		leads = pickle.load(open(paths + "\\leaders.dat", "rb"))
		leader = [lead for lead in leads]

		temp = leader[1:]
		leader_list.append(new_leader)
		leader_list += temp

		leader_list.sort(key=finding_highest, reverse=True)
		# leader_list = _leader + leader_list

		final_list = [leader[0]] + leader_list
		pickle.dump(final_list, open(paths + "\\leaders.dat", "wb"))

		# lead.writelines(new_leader)
		# lead.close()

		print("\n")
		print("-You will now be taken to the exit screen-")
		print("\n")
		time.sleep(1)
		input("Press any button")
		os.system("cls")
		exit_screen()

	print("""-------CAVER-------""")
	world.parse_world_dsl()
	player = Player()
	while player.is_alive() and not player.victory:
		room = world.tile_at(player.x, player.y)
		print(room.intro_text())

		if isinstance(room, world.EnemyChallengeTile) and room.fight:
			player.attack()

		room.modify_player(player)
		if player.is_alive() and not player.victory:
			choose_action(room, player)
		elif not player.is_alive():
			print(
				f"""{Fore.RED}
Your journey has come to an early end
		---GAME OVER---
{Fore.RESET}
            """
				  )
			end(player)
		elif player.is_alive() and player.victory:
			end(player)


def get_player_command():
	"""This function returns the user's input, which is the chosen action."""
	print("")
	return input(f"{Style.BRIGHT}Action:{Style.RESET_ALL}\n")


def get_available_actions(room, player):
	"""This function finds the possible actions that the player can make depending on the tile that the player is in
	and the tiles around the player."""

	actions = OrderedDict()
	print("")
	print(f"{Style.BRIGHT}Choose an action: ")
	if player:
		action_adder(actions, "d", player.print_details, "Print Player Details")
	if player.inventory:
		action_adder(actions, "i", player.print_inventory, "Print Inventory")
	if isinstance(room, world.TraderTile):
		action_adder(actions, "t", player.trade, "Trade")
	if isinstance(room, world.ArmourSmithTile):
		action_adder(actions, "t", player.trade, "Trade")
	if isinstance(room, world.WeaponSmithTile):
		action_adder(actions, "t", player.trade, "Trade")
	if isinstance(room, world.EnchanterTile):
		action_adder(actions, "en", player.enchant, "Enchant")
	if isinstance(room, world.QuestTile):
		action_adder(actions, "t", player.talk, "Talk")
	if isinstance(room, world.StoryTellerTile1):
		action_adder(actions, "c", player.converse, "Converse")
	if isinstance(room, world.StoryTellerTile2):
		action_adder(actions, "c", player.converse, "Converse")
	if isinstance(room, world.StoryTellerTile3):
		action_adder(actions, "c", player.converse, "Converse")
	if isinstance(room, world.EnemyTile1) and room.enemy.is_alive():
		action_adder(actions, "a", player.attack, "Attack")
	if isinstance(room, world.EnemyTile2) and room.enemy.is_alive():
		action_adder(actions, "a", player.attack, "Attack")
	if isinstance(room, world.EnemyTile3) and room.enemy.is_alive():
		action_adder(actions, "a", player.attack, "Attack")
	if isinstance(room, world.EnemyTile4) and room.enemy.is_alive():
		action_adder(actions, "a", player.attack, "Attack")
	if isinstance(room, world.GeoEnemy) or isinstance(room, world.GeoBoss) and room.enemy.is_alive():
		action_adder(actions, "a", player.attack, "Attack")
	if isinstance(room, world.HydroEnemy) or isinstance(room, world.HydroBoss) and room.enemy.is_alive():
		action_adder(actions, "a", player.attack, "Attack")
	if isinstance(room, world.PyroEnemy) or isinstance(room, world.PyroBoss) and room.enemy.is_alive():
		action_adder(actions, "a", player.attack, "Attack")
	if isinstance(room, world.AeroEnemy) or isinstance(room, world.AeroBoss) and room.enemy.is_alive():
		action_adder(actions, "a", player.attack, "Attack")
	if isinstance(room, world.EnemyChallengeTile) and room.enemy.is_alive() and not room.fight and not room.escape and not room.completed:
		action_adder(actions, "c", player.converse, "Converse")
	if isinstance(room, world.EnemyChallengeTile) and room.enemy.is_alive() and room.fight and not room.escape and not room.completed:
		action_adder(actions, "a", player.attack, "Attack")
	else:
		if world.tile_at(room.x, room.y - 1):
			try:
				if room.enemy.fight() is False:
					action_adder(actions, "n", player.move_north, "Go North")
			except AttributeError:
				action_adder(actions, "n", player.move_north, "Go North")

		if world.tile_at(room.x, room.y + 1):
			try:
				if room.enemy.fight() is False:
					action_adder(actions, "s", player.move_south, "Go South")
			except AttributeError:
				action_adder(actions, "s", player.move_south, "Go South")

		if world.tile_at(room.x + 1, room.y):
			try:
				if room.enemy.fight() is False:
					action_adder(actions, "e", player.move_east, "Go East")
			except AttributeError:
				action_adder(actions, "e", player.move_east, "Go East")

		if world.tile_at(room.x - 1, room.y):
			try:
				if room.enemy.fight() is False:
					action_adder(actions, "w", player.move_west, "Go West")
			except AttributeError:
				action_adder(actions, "w", player.move_west, "Go West")

	if player.hp < 100:
		action_adder(actions, "h", player.heal, "Heal")

	return actions


def action_adder(action_dict, hotkey, action, name):
	"""This function adds the actions that the player can make on the given tile and displays these actions
	onto the screen."""

	action_dict[hotkey.lower()] = action
	action_dict[hotkey.upper()] = action
	print(f"{hotkey}: {name}")


def choose_action(room, player):
	"""This function asks the player for its chosen action and verifies if the action is valid or not."""
	action = None
	while not action:
		available_actions = get_available_actions(room, player)
		action_input = input(f"{Style.BRIGHT}\nAction: \n")
		action = available_actions.get(action_input)
		if action:
			action()
		else:
			print(f"{Style.BRIGHT}\nInvalid Action\n")


if __name__ == "__main__":
	files.create_files(paths)
	files.dump(paths)
	start_screen()
